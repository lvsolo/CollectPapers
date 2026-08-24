#!/usr/bin/env python3
"""更新 README：目录索引 + 最近日报链接 + 统计。由 workflow 自动调用。"""

import sys
import datetime as dt
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import CONFIG, ROOT, log  # noqa: E402

MARKER_BEGIN = "<!-- AUTO-INDEX-BEGIN -->"
MARKER_END = "<!-- AUTO-INDEX-END -->"


def build_index() -> str:
    parts = []
    # 1) 领域索引
    parts.append("## 📂 领域索引（顶会 Guideline）\n")
    parts.append("| 领域 | 说明 |")
    parts.append("|------|------|")
    for t in CONFIG["topics"]:
        d = ROOT / "topics" / t["slug"]
        years = sorted(d.glob("Guideline *.md")) if d.exists() else []
        if years:
            links = " ".join(
                f"[{p.stem.split()[-1]}](topics/{t['slug']}/{p.name.replace(' ', '%20')})"
                for p in reversed(years))
            parts.append(f"| **{t['name']}** | {t.get('description','')}<br/>{links} |")
        else:
            parts.append(f"| {t['name']} | {t.get('description','')}（暂无） |")

    # 2) 最近日报
    parts.append("\n## 📰 最近日报（arXiv daily）\n")
    daily_dir = ROOT / CONFIG["daily"].get("report_dir", "daily")
    reports = sorted(daily_dir.glob("arxiv_report_*.md")) if daily_dir.exists() else []
    if reports:
        for p in reports[-1:-11:-1]:
            date = p.stem.replace("arxiv_report_", "")
            parts.append(f"- [{date}](daily/{p.name})")
    else:
        parts.append("（暂无，等待第一次定时任务）")
    return "\n".join(parts) + "\n"


def main() -> int:
    readme = ROOT / "README.md"
    if not readme.exists():
        log("README.md missing, skip")
        return 0
    content = readme.read_text(encoding="utf-8")
    if MARKER_BEGIN not in content:
        log("README.md has no auto-index markers, skip")
        return 0
    head = content.split(MARKER_BEGIN)[0]
    tail = content.split(MARKER_END)[1] if MARKER_END in content else ""
    updated = f"{head}{MARKER_BEGIN}\n{build_index()}\n{MARKER_END}{tail}"
    if updated != content:
        readme.write_text(updated, encoding="utf-8")
        log("README.md updated")
    else:
        log("README.md unchanged")
    return 0


if __name__ == "__main__":
    sys.exit(main())
