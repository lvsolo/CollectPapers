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
                    institution_for, importance_score, log, get_classifier)

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
    "object detection", "3d object detection", "lidar", "point cloud",
    "bird's eye view", "bev", "occupancy", "multi-view", "multi-camera",
    "monocular depth", "multi-object tracking", "tracking", "open vocabulary",
    "open-world", "zero-shot detection", "road anomaly", "obstacle detection",
    "traversability", "autonomous driving", "driving", "vision-language",
    "multimodal", "vision transformer", "self-supervised", "contrastive learning",
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
    """按标题在 DBLP 全库搜 arXiv 版本（期刊 CoRR）。返回 arXiv id 或 None。
    网络失败（限流/5xx）计入全局失败计数，供自适应退避。"""
    q = urllib.parse.quote(title[:150])
    data = http_get_json(
        f"https://dblp.org/search/publ/api?q={q}&format=json&h=10",
        cache_hours=336, retries=2, timeout=15)
    if not data:
        common._dblp_fail_count[0] += 1
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
    """引用数：Crossref 主源（免费稳定）→ S2 备源。带磁盘缓存。"""
    # 1) Crossref
    cr = common.crossref_paper(title)
    if cr is not None:
        return cr["citations"]
    # 2) S2 兜底（限流返回 None）
    q = urllib.parse.quote(title[:200])
    common._s2_throttle()
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
                  citations_budget=400, do_institutions=True) -> list[dict]:
    """补 arXiv 摘要 + S2 引用数 + 作者机构。in-place 修改并返回。"""
    # 1) arXiv id → 批量摘要
    if do_abstract:
        need = [p for p in papers if not p.get("abstract")]
        # 没有 arxiv_id 的先反查（DBLP 全库检索 CoRR 版本）。
        # 限速自适应：连续失败即加倍间隔（DBLP 5xx/断连时保命），成功则缓慢恢复
        delay = 0.8
        for p in need:
            if not p.get("arxiv_id"):
                before = common._dblp_fail_count
                p["arxiv_id"] = dblp_find_arxiv(p["title"], p.get("authors", []))
                if common._dblp_fail_count > before:
                    delay = min(delay * 2, 8.0)   # 失败：退避
                else:
                    delay = max(delay * 0.9, 0.8)  # 成功：缓慢恢复
                time.sleep(delay)
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
    # 2) 引用数 + 3) 机构：Crossref 一次并行批量查询同时拿两个字段（磁盘缓存优先）
    if do_citations or do_institutions:
        need = [p for p in papers
                if p.get("citations") is None or not p.get("institutions")]
        # 先走已有磁盘缓存（affiliations.json 里同时缓存过机构的不再查）
        to_query = []
        for p in need:
            cached = common._affil_cache().get(p["title"].lower().rstrip(". ")[:180])
            if cached and p.get("citations") is None:
                p["citations"] = -1  # 占位，后面由 crossref 填（缓存里无引用数）
            to_query.append(p)
        t0 = time.time()
        results = common.crossref_batch([p["title"] for p in to_query]) if to_query else {}
        n_c, n_i = 0, 0
        for p in to_query:
            r = results.get(p["title"])
            if r:
                if p.get("citations") is None:
                    p["citations"] = r["citations"]; n_c += 1
                if not p.get("institutions") and r["affiliations"]:
                    p["institutions"] = ", ".join(r["affiliations"][:3]); n_i += 1
            if p.get("citations") == -1:
                p["citations"] = None  # 占位还原
        # 映射表兜底（零网络）
        for p in to_query:
            if not p.get("institutions"):
                inst = institution_for(p.get("authors") or [])
                if inst:
                    p["institutions"] = inst; n_i += 1
        if to_query:
            log(f"  enrich: crossref batch {len(results)}/{len(to_query)} hit in {time.time()-t0:.0f}s "
                f"(citations {n_c}, institutions {n_i})")
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
        cite = f" · 📚 被引 {paper['citations']}"
    if llm_eval:
        stars = f" **{'⭐' * llm_eval.get('stars', 3)}** (相关度: {llm_eval.get('relevance', '?')}%)"
    title_line = f"### {paper['title']}{stars}"
    if not primary:
        title_line += f" *(→ 完整笔记见 [{cross_links[0] if cross_links else '其他领域'}])*"
    lines.append(title_line)
    links = []
    if paper.get("arxiv_id"):
        # arXiv 链接优先且唯一入口（用户无法访问付费出版页）
        links.append(f"[arXiv:{paper['arxiv_id']}](https://arxiv.org/abs/{paper['arxiv_id']})")
    if paper.get("code"):
        links.append(f"[代码]({paper['code']})")
    if not links and paper.get("ee"):
        # 仅当完全没有 arXiv id 时才退回 DOI（总比没有强）
        links.append(f"[出版页]({paper['ee']})")
    lines.append(f"- **链接**: {' · '.join(links) if links else '（无）'}{cite}")
    authors = paper.get("authors") or []
    if authors:
        astr = ", ".join(authors[:6]) + (" et al." if len(authors) > 6 else "")
        # 机构必显示：映射表 → S2 反查（enrich 阶段已预算好 → paper['institutions']）
        inst = paper.get("institutions") or institution_for(authors) or "（机构待查）"
        lines.append(f"- **作者**: {astr}")
        lines.append(f"- **🏷️ 机构**: {inst}")
    lines.append(f"- **会议**: {paper['venue']} {paper['year']}")
    if llm_eval and llm_eval.get("summary_cn"):
        lines.append(f"- **摘要（中）**: {llm_eval['summary_cn']}")
        if llm_eval.get("summary_en"):
            lines.append(f"- **摘要（英）**: {llm_eval['summary_en']}")
        for k, label in [("contribution", "核心贡献"), ("innovation", "创新点"),
                         ("result", "结果")]:
            if llm_eval.get(k):
                lines.append(f"- **{label}**: {llm_eval[k]}")
    # arXiv 原始摘要：无论有无 LLM 总结都附上（带总结 + 不带总结的摘要都要有）
    if paper.get("abstract"):
        lines.append("")
        lines.append("<details><summary>📄 arXiv 原始摘要（点击展开）</summary>")
        lines.append("")
        lines.append(f"> {paper['abstract']}")
        lines.append("")
        lines.append("</details>")
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
            # 主领域归属必须确定性：同一论文在【命中它的所有领域里 slug 字母序最小】的领域展开。
            # （此前按遍历顺序"先到先得"，不同批次轮次间会漂移，论文会在领域间搬家）
            for p in papers:
                norm = p["title"].lower().rstrip(". ")
                # 收集该论文命中的所有 slug（本 bucket 内）
                owners = sorted({s for s in bucket
                                 for pp in bucket[s].get(year, [])
                                 if pp["title"].lower().rstrip(". ") == norm} | {slug})
                owner = owners[0]
                if owner != slug:
                    p["_cross_from"] = owner
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
def _rewrite_batches(all_papers: dict) -> None:
    """enrich 后把 arXiv id/摘要/机构/引用回写进 .cache/batches/*.json，
    使 llm-only 重建渲染时能拿到完整数据（否则只有 DBLP 原始字段，链接会退化为 DOI）。"""
    batch_dir = ROOT / ".cache" / "batches"
    if not batch_dir.exists():
        return
    for bf in batch_dir.glob("*.json"):
        try:
            papers = json.loads(bf.read_text())
        except json.JSONDecodeError:
            continue
        dirty = False
        for p in papers:
            ep = all_papers.get(p.get("title"))
            if not ep:
                continue
            for k in ("arxiv_id", "abstract", "institutions", "citations", "code", "url"):
                if ep.get(k) and p.get(k) != ep[k]:
                    p[k] = ep[k]
                    dirty = True
        if dirty:
            bf.write_text(json.dumps(papers, ensure_ascii=False, default=str))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--conference", default=None)
    ap.add_argument("--year", type=int, default=None)
    ap.add_argument("--no-enrich", action="store_true", help="跳过摘要/引用 enrich")
    ap.add_argument("--citations-budget", type=int, default=400)
    ap.add_argument("--force", action="store_true", help="忽略会议公布窗口强制抓取")
    ap.add_argument("--no-llm", action="store_true",
                    help="分批模式1: 只抓取+归类+enrich，跳过 LLM（matrix collect 阶段用）")
    ap.add_argument("--llm-only", action="store_true",
                    help="分批模式2: 复用 HTTP 缓存重建 bucket，只跑 LLM 评估（llm-eval 阶段用）")
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

    # 会议公布状态：只对"当年"判断（历史年份是稳定数据，永远全量）。
    # 语义：当前月 < 公示月 → 当年会议尚未公布，跳过；已过公示月 → 已公布，照常抓。
    # 另：ECCV 仅偶数年、ICCV 仅奇数年，不存在的届次直接跳过。
    this_month = dt.date.today().month
    this_year = dt.date.today().year
    if not args.force:
        active = []
        for c in confs:
            if this_year in years:
                if c.get("even_years_only") and this_year % 2 != 0:
                    log(f"[skip] {c['name']} {this_year}: 双年会，本年不举办")
                    continue
                if c.get("odd_years_only") and this_year % 2 != 1:
                    log(f"[skip] {c['name']} {this_year}: 双年会，本年不举办")
                    continue
                am = c.get("announce_month")
                if am and this_month < am:
                    log(f"[skip] {c['name']} {this_year}: {am} 月才公示录用，当前 {this_month} 月尚未公布（--force 可强制）")
                    continue
            active.append(c)
        confs = active

    classifier = Classifier(CONFIG["topics"])
    bucket: dict[str, dict[int, list]] = {}
    dblp_enabled = CONFIG.get("sources", {}).get("dblp", True)

    for conf in confs:
        for year in years:
            if args.llm_only:
                break  # llm-only 不重新抓 DBLP，跳到后面的 batch 重建段
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
            if papers:
                # 保存这个会议-年的原始数据，供 --llm-only 阶段复用
                batch_dir = ROOT / ".cache" / "batches"
                batch_dir.mkdir(exist_ok=True)
                (batch_dir / f"{conf['dblp_venue']}-{year}.json").write_text(
                    json.dumps([p for p in papers], ensure_ascii=False, default=str))

    # 去重（同领域同标题）
    for slug in bucket:
        for year in bucket[slug]:
            seen = {}
            for p in bucket[slug][year]:
                seen.setdefault(p["title"].lower().rstrip(". "), p)
            bucket[slug][year] = list(seen.values())

    if args.llm_only:
        # 分批模式2: 不重新抓 DBLP，从落盘的 batch 文件重建 bucket（HTTP 缓存兜底）
        batch_dir = ROOT / ".cache" / "batches"
        classifier = get_classifier()
        for bf in sorted(batch_dir.glob("*.json")):
            m = re.match(r"([A-Za-z]+)-(\d{4})", bf.stem)
            if not m:
                continue
            if args.conference and m.group(1).lower() != args.conference.lower():
                continue
            if args.year and int(m.group(2)) != args.year:
                continue
            try:
                papers = json.loads(bf.read_text())
            except json.JSONDecodeError:
                continue
            log(f"[llm-only] rebuilding {bf.stem}: {len(papers)} papers")
            for p in papers:
                cls = classifier.classify(p["title"], p.get("abstract", ""))
                for t, score in cls:
                    p2 = dict(p)
                    p2["cls_score"] = score
                    bucket.setdefault(t["slug"], {}).setdefault(int(m.group(2)), []).append(p2)

    if not args.no_enrich and not args.llm_only and bucket:
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
        # enrich 后回写 batch 文件（arXiv id/摘要/机构/引用），llm-only 重建时直接可用
        _rewrite_batches(all_papers)
        # 代码链接：arXiv 摘要自报 GitHub（快，零网络）→ PWC 兜底（慢，限 top 150）
        for title, p in list(all_papers.items())[:400]:
            if not p.get("code"):
                link = common.code_link_from_abstract(p.get("abstract", ""))
                if link:
                    p["code"] = link
        for title, p in list(all_papers.items())[:150]:
            if not p.get("code"):
                r = common.pwc_link(title)
                if r:
                    p["code"] = r.get("official") or r.get("page")
                time.sleep(0.4)

    # 每年上限
    cap = CONFIG.get("max_papers_per_year", 120)
    cap_old = CONFIG.get("max_papers_per_year_before_2022", 60)
    for slug in bucket:
        for year in bucket[slug]:
            papers = bucket[slug][year]
            papers.sort(key=lambda p: -importance_score(p))
            bucket[slug][year] = papers[: (cap_old if year < 2022 else cap)]

    # LLM 中英对照摘要（可选，与日报线同一套评估器；--no-llm 跳过留给下一阶段）
    llm = common.LLM()
    if llm.active and not args.no_llm:
        # 只评每领域每年的前 N 篇（成本控制；其余保持英文摘要降级渲染）
        n_eval = CONFIG.get("llm", {}).get("guideline_eval_topn", 25)
        count = 0
        log(f"LLM evaluation for guideline top-{n_eval} per topic-year ...")
        for slug in bucket:
            for year in bucket[slug]:
                top = bucket[slug][year][:n_eval]
                plist = [{"arxiv_id": p.get("arxiv_id") or p["title"], "title": p["title"],
                          "abstract": p.get("abstract", "")} for p in top]
                results = common.llm_eval_papers(llm, plist, "、".join(t["name"] for t in CONFIG["topics"]))
                by_id = {r.get("_arxiv_id"): r for r in results if r.get("_arxiv_id")}
                for p in top:
                    ev = by_id.get(p.get("arxiv_id") or p["title"])
                    if ev:
                        p["llm"] = ev
                        count += 1
                log(f"  [{slug} {year}] {len(results)}/{len(top)} evaluated")
        log(f"LLM evaluated {count} papers in total")
    else:
        # --no-llm 批次阶段：从磁盘缓存恢复已评估论文的摘要（LLM 不激活也能带上），
        # 防止批次重渲染时把 llm-eval 阶段已写入的摘要冲掉
        eval_cache_path = common.CACHE_DIR / "llm_evals.json"
        eval_cache = {}
        if eval_cache_path.exists():
            try:
                eval_cache = json.loads(eval_cache_path.read_text())
            except json.JSONDecodeError:
                pass
        v = common.EVAL_PROMPT_VERSION
        restored = 0
        for slug in bucket:
            for year in bucket[slug]:
                for p in bucket[slug][year]:
                    for key in (p.get("arxiv_id"), p["title"]):
                        if key and eval_cache.get(f"{key}|{v}"):
                            p["llm"] = eval_cache[f"{key}|{v}"]
                            restored += 1
                            break
        if restored:
            log(f"restored {restored} LLM summaries from cache (batch-mode render)")

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
