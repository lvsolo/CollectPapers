#!/usr/bin/env python3
"""日报线：每天抓 arXiv 新论文 → 领域过滤 → LLM 中文评估（可选）→ daily/arxiv_report_YYYY-MM-DD.md

用法:
    python3 daily_arxiv.py                # 今天
    python3 daily_arxiv.py --days 2       # 补昨天的
"""

import argparse
import datetime as dt
import json
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common  # noqa: E402
from common import (CONFIG, ROOT, LLM, arxiv_fetch, get_classifier,
                    institution_for, llm_eval_papers, log)

TOPIC_NAMES = "、".join(t["name"] for t in CONFIG["topics"])
TOPIC_BY_NAME = {t["name"]: t for t in CONFIG["topics"]}


def _merge_report(existing: str, new_lines: list[str], groups: dict,
                  topic_by_name: dict) -> list[str]:
    """同一天二次运行时，把新论文条目合并进已有报告（按标题去重，不丢旧内容）。"""
    import re as _re
    # 已有报告里的论文标题集合
    have = set(_re.findall(r"^### \d+\. (.+?)\s*(?:\*\*.*)?$", existing, _re.M))
    # 抽出新报告里、已有报告没有的完整条目块（### 到下一个 ###/## 之前）
    additions: list[str] = []
    blocks = _re.split(r"(?=^### )", "\n".join(new_lines), flags=_re.M)
    for b in blocks:
        m = _re.match(r"### \d+\. (.+?)\s*(?:\*\*.*)?$", b.strip().splitlines()[0] if b.strip() else "")
        if m and m.group(1).strip() not in have and b.strip():
            additions.append(b.rstrip())
    if not additions:
        return existing.splitlines()
    # 简单策略：追加到文末统计节之前，并在统计后补一行说明
    parts = existing.split("## 📊 统计")
    head = parts[0].rstrip()
    merged = head.splitlines()
    merged.append("")
    merged.append("---")
    merged.append("")
    merged.append("## 🆕 当日更新（后续运行新增）")
    merged.append("")
    merged.extend(additions)
    if len(parts) > 1:
        merged.append("")
        merged.append("## 📊 统计")
        merged.append(parts[1].rstrip())
    return merged


def fetch_recent(days: int) -> list[dict]:
    """抓最近 N 天（按提交日期过滤）的 cs.CV 新论文。窗口按北京时间算。"""
    today_bj = (dt.datetime.utcnow() + dt.timedelta(hours=8)).date()
    since = (today_bj - dt.timedelta(days=days)).isoformat()
    cats = CONFIG["daily"]["categories"]
    query = " OR ".join(f"cat:{c}" for c in cats)
    log(f"fetching arXiv [{', '.join(cats)}] since {since} ...")
    papers = arxiv_fetch(query, max_results=800)  # 按提交时间倒序
    out = [p for p in papers if p["date"] >= since]
    log(f"  {len(papers)} fetched, {len(out)} within {days} day(s)")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=None, help="回看天数（默认取配置 lookback_days）")
    args = ap.parse_args()

    dcfg = CONFIG["daily"]
    days = args.days or dcfg.get("lookback_days", 2)
    papers = fetch_recent(days)
    if not papers:
        log("no papers fetched, exit")
        return 1

    # 去重：跳过以往报告已收录的
    seen_db = ROOT / ".cache" / "daily_seen.json"
    seen: dict[str, str] = json.loads(seen_db.read_text()) if seen_db.exists() else {}
    fresh = [p for p in papers if seen.get(p["arxiv_id"]) != p["date"]]
    log(f"  {len(fresh)} not yet reported")
    if not fresh:
        log("nothing new today")
        return 0

    # 关键词分类
    classifier = get_classifier()
    classified: list[tuple[dict, list]] = []
    for p in fresh:
        cls = classifier.classify(p["title"], p["abstract"])
        if cls:
            classified.append((p, cls))
    log(f"  {len(classified)} match at least one topic")

    # 按最佳领域归类（分数最高的），并应用每领域/总量上限
    max_per = dcfg.get("max_papers_per_topic", 8)
    max_total = dcfg.get("max_total", 60)
    by_topic: dict[str, list] = {}
    for p, cls in classified:
        best = max(cls, key=lambda x: x[1] * x[0].get("weight", 1.0))
        by_topic.setdefault(best[0]["name"], []).append((p, best[1]))
    selected: list[tuple[dict, dict, int]] = []  # (paper, topic, score)
    for tname, lst in by_topic.items():
        lst.sort(key=lambda x: -x[1])
        for p, s in lst[:max_per]:
            selected.append((p, TOPIC_BY_NAME[tname], s))
    # 总量控制：优先高相关领域分数
    selected.sort(key=lambda x: -x[2] * x[1].get("weight", 1.0))
    selected = selected[:max_total]
    log(f"  selected {len(selected)} papers for report")

    # 硬性保护：没有新内容时绝不写文件（防止空报告覆盖已有内容）
    if not selected:
        log("no new papers to add — keep existing report untouched")
        return 0

    # LLM 评估（可选）
    llm = LLM()
    evals: dict[str, dict] = {}
    # 引用数预取（Crossref 主源；新论文多数为 0，有值的显示）
    for p, _, _ in selected:
        cr = common.crossref_paper(p["title"])
        if cr is not None:
            p["citations"] = cr["citations"]
        time.sleep(0.15)

    if llm.active:
        log(f"LLM evaluation enabled (model={llm.model})")
        plist = [{"arxiv_id": p["arxiv_id"], "title": p["title"],
                  "abstract": p["abstract"]} for p, _, _ in selected]
        results = llm_eval_papers(llm, plist, TOPIC_NAMES)
        for r in results:
            if r.get("_arxiv_id"):
                evals[r["_arxiv_id"]] = r
        log(f"  {len(evals)}/{len(plist)} papers evaluated by LLM")
    else:
        log("LLM not configured (no LLM_API_KEY), fallback to excerpt mode")

    # 渲染 markdown
    # 北京时间日期（日报按北京日切，与用户作息一致；runner 是 UTC）
    today = (dt.datetime.utcnow() + dt.timedelta(hours=8)).date().isoformat()
    lines = [f"# 📚 arXiv 每日论文报告（我的领域）", ""]
    lines.append(f"**报告日期**: {today}  ")
    lines.append(f"**论文来源**: [arXiv {'/'.join(dcfg['categories'])} Recent](https://arxiv.org/list/{dcfg['categories'][0]}/recent)  ")
    n_llm = len(evals)
    lines.append(f"**关注论文数**: {len(selected)} 篇"
                 + (f"（其中 {n_llm} 篇经大模型中文评估）" if n_llm else "（关键词匹配模式，未配置 LLM）"))
    lines.append("")
    lines.append(f"> 匹配领域: {TOPIC_NAMES}")
    lines.append("")

    # 目录
    groups: dict[str, list] = {}
    for p, t, s in selected:
        groups.setdefault(t["name"], []).append((p, s))
    if groups:
        lines.append("## 📑 目录")
        lines.append("")
        for tname in sorted(groups, key=lambda n: -len(groups[n])):
            slug = TOPIC_BY_NAME[tname]["slug"]
            lines.append(f"- [{tname}](#{slug}) ({len(groups[tname])}篇)")
        lines.append("")

    for tname in sorted(groups, key=lambda n: -len(groups[n])):
        t = TOPIC_BY_NAME[tname]
        lines.append(f"## {tname}")
        lines.append("")
        for i, (p, s) in enumerate(sorted(groups[tname], key=lambda x: -x[1]), 1):
            ev = evals.get(p["arxiv_id"])
            stars = f" **{'⭐' * ev.get('stars', 3)}** (相关度: {ev.get('relevance', '?')}%, 质量: {ev.get('quality', '?')})" if ev else ""
            lines.append(f"### {i}. {p['title']}{stars}")
            lines.append("")
            lines.append(f"- **arXiv ID**: [{p['arxiv_id']}]({p['url']})  · [📄 PDF](https://arxiv.org/pdf/{p['arxiv_id']})")
            authors = p.get("authors") or []
            if authors:
                astr = ", ".join(authors[:3]) + (f" et al. ({len(authors)} authors)" if len(authors) > 3 else "")
                lines.append(f"- **作者**: {astr}")
            # 机构必显示：映射表 → Crossref/S2 反查 → 待查标记
            inst = common.institutions_for_paper(p)
            lines.append(f"- **🏷️ 机构**: {inst}")
            # 代码库：arXiv 摘要自报 GitHub 优先，PWC 兜底（有才显示）
            code = common.code_link_from_abstract(p.get("abstract", ""))
            if not code:
                pwc = common.pwc_link(p["title"])
                if pwc:
                    code = pwc.get("official") or pwc.get("page")
            if code:
                lines.append(f"- **💻 代码**: [{code.replace('https://', '')}]({code})")
            # 引用数（Crossref；新论文通常为 0，>=1 才显示）
            cites = p.get("citations")
            meta = f"- **提交日期**: {p['date']} · **分类**: {', '.join(p.get('cats', [])[:3])}"
            if cites:
                meta += f" · **📚 被引**: {cites}"
            lines.append(meta)
            if ev:
                if ev.get("summary_cn"):
                    lines.append(f"- **摘要（中）**: {ev['summary_cn']}")
                if ev.get("summary_en"):
                    lines.append(f"- **摘要（英）**: {ev['summary_en']}")
                for k, label in [("assessment", "**评估**"), ("contribution", "**核心贡献**"),
                                 ("innovation", "**创新点**"), ("result", "**结果**")]:
                    if ev.get(k):
                        lines.append(f"- {label}: {ev[k]}")
            # arXiv 原始摘要全文（折叠，供对照原文）
            ab = p.get("abstract", "")
            if ab:
                lines.append("")
                lines.append("<details><summary>📄 arXiv 原始摘要（点击展开）</summary>")
                lines.append("")
                lines.append(f"> {ab}")
                lines.append("")
                lines.append("</details>")
            lines.append("")
        lines.append("---")
        lines.append("")

    # 统计
    lines.append("## 📊 统计")
    lines.append("")
    lines.append("| 领域 | 论文数 |")
    lines.append("|------|--------|")
    for tname in sorted(groups, key=lambda n: -len(groups[n])):
        lines.append(f"| {tname} | {len(groups[tname])} |")
    lines.append(f"| **总计** | **{len(selected)}** |")

    out_dir = ROOT / dcfg.get("report_dir", "daily")
    out_dir.mkdir(exist_ok=True)
    out = out_dir / f"arxiv_report_{today}.md"
    if out.exists():
        # 同一天多次运行：追加合并（新论文插到各领域分组），不覆盖已有内容
        existing = out.read_text(encoding="utf-8")
        if existing.strip():
            lines = _merge_report(existing, lines, groups, TOPIC_BY_NAME)
    out.write_text("\n".join(lines), encoding="utf-8")
    log(f"wrote {out.relative_to(ROOT)} ({len(selected)} new papers this run)")

    # 更新 seen
    for p, _, _ in selected:
        seen[p["arxiv_id"]] = p["date"]
    seen_db.write_text(json.dumps(seen, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
