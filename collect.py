#!/usr/bin/env python3
"""顶会 Guideline 线：从 DBLP 拉取六大顶会论文 → 领域归类 → 补摘要/引用 → 生成按领域的分年份 Guideline。

用法:
    python3 collect.py                    # 全量（首次）
    python3 collect.py --conference CVPR --year 2024   # 小范围调试
    python3 collect.py --no-enrich        # 跳过 arXiv/S2 enrich（快速）
"""

import argparse
import datetime as dt
import json
import re
import sys
import time
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common  # noqa: E402
from common import (CONFIG, ROOT, Classifier, arxiv_by_ids, http_get_json,
                    institution_for, importance_score, log)

DBLP_API = "https://dblp.org/search/publ/api"
S2_API = "https://api.semanticscholar.org/graph/v1/paper"


# ----------------------------------------------------------------------
# DBLP 抓取
# ----------------------------------------------------------------------
def dblp_conference_papers(venue: str, year: int, hint: str | None = None) -> list[dict]:
    """DBLP venue 检索。hint: 领域关键词（空则用大类词跑多轮，太慢，不推荐）。

    DBLP search API 不支持纯 venue+year 浏览，因此用 venue:XXX + 关键词组合查询，
    关键词来自所有 topics 的 must_any 核心 token（去重后）。
    """
    if hint:
        queries = [hint]
    else:
        queries = QUERIES_BY_CONFERENCE
    seen: dict[str, dict] = {}
    for q in queries:
        qstr = f"venue:{venue}: {q}"
        offset = 0
        while True:
            url = (f"{DBLP_API}?q={urllib.parse.quote(qstr)}"
                   f"&format=json&h=100&f={offset}")
            data = http_get_json(url, cache_hours=72, retries=3)
            if not data:
                break
            hits = data.get("result", {}).get("hits", {})
            total = int(hits.get("@total", "0"))
            hit_list = hits.get("hit", [])
            if isinstance(hit_list, dict):
                hit_list = [hit_list]
            for h in hit_list:
                info = h.get("info", {})
                title = common.clean_text(info.get("title", ""))
                year_s = str(info.get("year", ""))
                if year_s != str(year):
                    continue
                # 只要正文（去掉 workshop/co-located 杂项：DBLP venue 字段带后缀）
                v = str(info.get("venue", venue))
                if v != venue:
                    continue
                key = title.lower().rstrip(". ")
                if key in seen:
                    continue
                authors_raw = info.get("authors", {}).get("author", [])
                if isinstance(authors_raw, dict):
                    authors_raw = [authors_raw]
                seen[key] = {
                    "title": title,
                    "authors": [common.clean_text(a.get("text", "")) for a in authors_raw],
                    "year": year,
                    "venue": venue,
                    "ee": info.get("ee", ""),
                    "doi": info.get("doi", ""),
                    "arxiv_id": None,
                }
            offset += 100
            if offset >= total or offset > 2000:
                break
            time.sleep(2.5)  # DBLP 礼貌限速，429/断连时由 http_get 退避重试兜底
        time.sleep(1.5)  # 关键词轮次之间也留间隔
    return list(seen.values())


# 每个领域的核心检索词（标题命中概率高）
QUERIES_BY_CONFERENCE = [
    "3d object detection", "lidar", "point cloud", "bird's eye view", "bev",
    "occupancy", "multi-view", "multi-camera", "monocular depth",
    "multi-object tracking", "tracking", "open vocabulary", "open-world",
    "zero-shot detection", "foreign object", "vision-language", "multimodal",
    "vision transformer", "self-supervised", "contrastive learning",
    "masked image", "video understanding", "action recognition",
    "continual learning", "incremental learning", "architecture search",
    "pruning", "sparsity", "distillation", "knowledge distillation",
]


# ----------------------------------------------------------------------
# Enrichment
# ----------------------------------------------------------------------
def find_arxiv_id(paper: dict) -> str | None:
    """从 DBLP ee 链接识别 arXiv id；没有时用 DBLP 自身的 arXiv 关联查询。"""
    ee = paper.get("ee", "") or ""
    m = re.search(r"arxiv\.org/abs/(\d{4}\.\d{4,5}|[a-z\-]+/\d{7})", ee, re.I)
    if m:
        return m.group(1)
    return None


def dblp_find_arxiv(title: str, authors: list[str]) -> str | None:
    """按标题在 DBLP 全库搜 arXiv 版本（期刊 CoRR）。返回 arXiv id 或 None。"""
    q = urllib.parse.quote(title[:150])
    data = http_get_json(
        f"https://dblp.org/search/publ/api?q={q}&format=json&h=10",
        cache_hours=336, retries=2, timeout=15)
    if not data:
        return None
    hits = data.get("result", {}).get("hits", {}).get("hit", [])
    if isinstance(hits, dict):
        hits = [hits]
    for h in hits:
        info = h.get("info", {})
        t = common.clean_text(info.get("title", "")).lower().rstrip(". ")
        if t != title.lower().rstrip(". "):
            continue
        if "informal" not in str(info.get("type", "")).lower():
            continue  # CoRR（arXiv）条目在 DBLP 里标记为 informal
        ees = info.get("ee", [])
        if isinstance(ees, str):
            ees = [ees]
        for ee in ees:
            m = re.search(r"arxiv\.org/abs/(\d{4}\.\d{4,5}|[a-z\-]+/\d{7})", ee, re.I)
            if m:
                return m.group(1)
            m = re.search(r"doi\.org/10\.48550/arXiv\.(\S+)", ee, re.I)
            if m:
                return m.group(1)
    return None


def s2_citations(title: str) -> int | None:
    """Semantic Scholar 引用数（限流严重，仅对最终入选论文调用）。"""
    q = urllib.parse.quote(title[:200])
    data = http_get_json(
        f"{S2_API}/search/match?query={q}&fields=citationCount",
        cache_hours=168, retries=2, timeout=15,
        headers={"x-api-key": _s2_key()} if _s2_key() else None)
    if not data or data.get("code") == 404:
        return None
    try:
        return int(data["data"][0]["citationCount"])
    except (KeyError, IndexError, TypeError, ValueError):
        return None


def _s2_key() -> str:
    import os
    return os.environ.get("S2_API_KEY", "")


def enrich_papers(papers: list[dict], *, do_abstract=True, do_citations=True,
                  citations_budget=400) -> list[dict]:
    """补 arXiv 摘要 + S2 引用数。in-place 修改并返回。"""
    # 1) arXiv id → 批量摘要
    if do_abstract:
        need = [p for p in papers if not p.get("abstract")]
        # 没有 arxiv_id 的先反查（DBLP 全库检索 CoRR 版本）
        for p in need:
            if not p.get("arxiv_id"):
                p["arxiv_id"] = dblp_find_arxiv(p["title"], p.get("authors", []))
                time.sleep(0.5)
        ids = [p["arxiv_id"] for p in need if p.get("arxiv_id")]
        log(f"  enrich: fetching abstracts for {len(ids)}/{len(need)} papers")
        fetched = {a["arxiv_id"]: a for a in arxiv_by_ids(ids)}
        for p in need:
            a = fetched.get(p.get("arxiv_id"))
            if a:
                p["abstract"] = a["abstract"]
                p["arxiv_authors"] = a["authors"]
            if p.get("arxiv_id"):
                p.setdefault("url", f"https://arxiv.org/abs/{p['arxiv_id']}")
    # 2) 引用数（预算内）
    if do_citations:
        got = 0
        for p in papers:
            if got >= citations_budget:
                break
            if p.get("citations") is None:
                c = s2_citations(p["title"])
                if c is not None:
                    p["citations"] = c
                    got += 1
                time.sleep(1.2)  # 免费 S2 ~1 rps
    return papers


# ----------------------------------------------------------------------
# Guideline 生成
# ----------------------------------------------------------------------
def extract_summary(paper: dict) -> str:
    """无 LLM 时的摘录式摘要：抽 1-2 句关键句。"""
    ab = paper.get("abstract") or ""
    if not ab:
        return "（暂无摘要）"
    sents = re.split(r"(?<=[.!?])\s+", ab)
    keep = []
    for s in sents:
        if re.search(r"\b(we propose|we present|this paper (proposes|presents|introduces)|"
                     r"we introduce|our method|we develop|state-of-the-art|outperform)", s, re.I):
            keep.append(s)
        if len(keep) >= 2:
            break
    if not keep and sents:
        keep = sents[:1]
    return " ".join(keep)[:600]


def render_paper_md(paper: dict, llm_eval: dict | None, primary: bool,
                    cross_links: list[str]) -> str:
    """渲染单篇论文的 markdown 块。primary=True 表示完整收录；False 为跨领域链接。"""
    lines = []
    stars = ""
    cite = ""
    if paper.get("citations") is not None:
        cite = f" · 📚 {paper['citations']} citations"
    if llm_eval:
        stars = f" **{'⭐' * llm_eval.get('stars', 3)}** (相关度: {llm_eval.get('relevance', '?')}%)"
    title_line = f"### {paper['title']}{stars}"
    if not primary:
        title_line += f" *(→ 完整笔记见 [{cross_links[0] if cross_links else '其他领域'}])*"
    lines.append(title_line)
    links = []
    if paper.get("arxiv_id"):
        links.append(f"[arXiv:{paper['arxiv_id']}](https://arxiv.org/abs/{paper['arxiv_id']})")
    if paper.get("ee") and "arxiv" not in (paper.get("ee") or ""):
        links.append(f"[出版页]({paper['ee']})")
    if paper.get("code"):
        links.append(f"[代码]({paper['code']})")
    lines.append(f"- **链接**: {' · '.join(links) if links else '（无）'}{cite}")
    authors = paper.get("authors") or []
    if authors:
        astr = ", ".join(authors[:6]) + (" et al." if len(authors) > 6 else "")
        inst = institution_for(authors)
        line = f"- **作者**: {astr}"
        if inst:
            line += f"　🏷️ **机构**: {inst}"
        lines.append(line)
    lines.append(f"- **会议**: {paper['venue']} {paper['year']}")
    if llm_eval and llm_eval.get("assessment"):
        lines.append(f"- **评估**: {llm_eval['assessment']}")
        for k, label in [("contribution", "核心贡献"), ("innovation", "创新点"),
                         ("method", "方法"), ("result", "结果")]:
            if llm_eval.get(k):
                lines.append(f"- **{label}**: {llm_eval[k]}")
    else:
        lines.append(f"- **摘要摘录**: {extract_summary(paper)}")
    return "\n".join(lines)


def generate_guidelines(bucket: dict, out_dir: Path) -> list[Path]:
    """bucket: {slug: {year: [papers]}} → topics/<slug>/Guideline <year>.md"""
    written = []
    classifier = Classifier(CONFIG["topics"])
    topic_by_slug = {t["slug"]: t for t in CONFIG["topics"]}
    # 跨领域去重：同一篇论文（title 归一）只在一个领域完整展开，其余领域给链接
    primary_owner: dict[str, str] = {}   # norm_title -> slug（第一个收录的领域）
    for slug in sorted(bucket.keys()):
        for year in sorted(bucket[slug].keys(), reverse=True):
            papers = bucket[slug][year]
            papers.sort(key=lambda p: -importance_score(p))
            md = [f"# {topic_by_slug[slug]['name']} — {year} Guideline", ""]
            md.append(f"> 领域: {topic_by_slug[slug].get('description', '')}")
            md.append(f"> 论文数: {len(papers)} · 按重要性排序（引用数/标题信号启发式）")
            md.append("")
            md.append(f"> 同领域其他年份: " + ", ".join(
                f"[{y}]({'Guideline%20' + str(y) + '.md'})"
                for y in sorted(bucket[slug].keys(), reverse=True) if y != year))
            md.append("")
            for p in papers:
                norm = p["title"].lower().rstrip(". ")
                if norm in primary_owner and primary_owner[norm] != slug:
                    p["_cross_from"] = primary_owner[norm]
                else:
                    primary_owner[norm] = slug
            full = [p for p in papers if "_cross_from" not in p]
            cross = [p for p in papers if "_cross_from" in p]
            for p in full:
                md.append(render_paper_md(p, p.get("llm"), True, []))
                md.append("")
            if cross:
                md.append("## 跨领域论文（完整笔记在其他领域）")
                md.append("")
                for p in cross:
                    other = primary_owner[p["title"].lower().rstrip(". ")]
                    md.append(f"- {p['title']} → [{other}](../{other}/Guideline%20{year}.md)")
                md.append("")
            out = out_dir / slug / f"Guideline {year}.md"
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text("\n".join(md), encoding="utf-8")
            written.append(out)
    return written


# ----------------------------------------------------------------------
# 主流程
# ----------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--conference", default=None)
    ap.add_argument("--year", type=int, default=None)
    ap.add_argument("--no-enrich", action="store_true", help="跳过摘要/引用 enrich")
    ap.add_argument("--citations-budget", type=int, default=400)
    ap.add_argument("--force", action="store_true", help="忽略会议公布窗口强制抓取")
    args = ap.parse_args()

    confs = CONFIG["conferences"]
    if args.conference:
        confs = [c for c in confs if c["name"].lower() == args.conference.lower()]
        if not confs:
            log(f"unknown conference {args.conference}")
            return 1
    years = list(range(CONFIG["start_year"], CONFIG["end_year"] + 1))
    if args.year:
        years = [args.year]

    # 会议公布窗口：只有"当前年份"受窗口控制（历史年份是稳定数据，永远全量）
    this_month = dt.date.today().month
    this_year = dt.date.today().year
    if not args.force:
        active = []
        for c in confs:
            months = c.get("publish_months")
            if months and this_year in years and this_month not in months:
                log(f"[skip] {c['name']} {this_year}: 当前月份 {this_month} 不在公布窗口 {months}（--force 可强制）")
                continue
            active.append(c)
        confs = active
        if this_year in years and this_month == 1:
            # 1月时 NeurIPS 已收尾，跳过当年其余会议的空跑
            pass

    classifier = Classifier(CONFIG["topics"])
    bucket: dict[str, dict[int, list]] = {}
    dblp_enabled = CONFIG.get("sources", {}).get("dblp", True)

    for conf in confs:
        for year in years:
            log(f"[{conf['name']} {year}] fetching from DBLP...")
            papers = dblp_conference_papers(conf["dblp_venue"], year) if dblp_enabled else []
            log(f"  got {len(papers)} raw papers")
            matched = 0
            for p in papers:
                p["arxiv_id"] = find_arxiv_id(p)
                cls = classifier.classify(p["title"], p.get("abstract", ""))
                for t, score in cls:
                    p2 = dict(p)
                    p2["cls_score"] = score
                    bucket.setdefault(t["slug"], {}).setdefault(year, []).append(p2)
                if cls:
                    matched += 1
            log(f"  matched into topics: {matched}")

    # 去重（同领域同标题）
    for slug in bucket:
        for year in bucket[slug]:
            seen = {}
            for p in bucket[slug][year]:
                seen.setdefault(p["title"].lower().rstrip(". "), p)
            bucket[slug][year] = list(seen.values())

    if not args.no_enrich and bucket:
        total = sum(len(ps) for ys in bucket.values() for ps in ys.values())
        log(f"enriching {total} papers (abstracts + citations)...")
        all_papers = {}
        for slug in bucket:
            for year in bucket[slug]:
                for p in bucket[slug][year]:
                    all_papers[p["title"]] = p  # 同一论文共享 enrich
        enrich_papers(list(all_papers.values()),
                      do_citations=not args.no_enrich,
                      citations_budget=args.citations_budget)
        # 代码链接（仅 top 论文，PWC 慢）
        for title, p in list(all_papers.items())[:150]:
            if not p.get("code"):
                link = common.pwc_link(title)
                if link:
                    p["code"] = link
                time.sleep(0.4)

    # 每年上限
    cap = CONFIG.get("max_papers_per_year", 120)
    cap_old = CONFIG.get("max_papers_per_year_before_2022", 60)
    for slug in bucket:
        for year in bucket[slug]:
            papers = bucket[slug][year]
            papers.sort(key=lambda p: -importance_score(p))
            bucket[slug][year] = papers[: (cap_old if year < 2022 else cap)]

    written = generate_guidelines(bucket, ROOT / "topics")
    log(f"wrote {len(written)} guideline files:")
    for w in written:
        log(f"  {w.relative_to(ROOT)}")
    # 持久化原始数据供增量/调试
    (ROOT / ".cache" / "last_bucket.json").write_text(
        json.dumps({s: {str(y): [{k: v for k, v in p.items() if k != 'llm'}
                                 for p in ps] for y, ps in ys.items()}
                    for s, ys in bucket.items()}, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
