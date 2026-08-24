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


def fetch_recent(days: int) -> list[dict]:
    """抓最近 N 天（按提交日期过滤）的 cs.CV 新论文。"""
    since = (dt.date.today() - dt.timedelta(days=days)).isoformat()
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

    # LLM 评估（可选）
    llm = LLM()
    evals: dict[str, dict] = {}
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
    today = dt.date.today().isoformat()
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
            # 机构必显示：映射表 → S2 反查 → 待查标记
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
            lines.append(f"- **提交日期**: {p['date']} · **分类**: {', '.join(p.get('cats', [])[:3])}")
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
    out.write_text("\n".join(lines), encoding="utf-8")
    log(f"wrote {out.relative_to(ROOT)}")

    # 更新 seen
    for p, _, _ in selected:
        seen[p["arxiv_id"]] = p["date"]
    seen_db.write_text(json.dumps(seen, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
