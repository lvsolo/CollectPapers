# CLAUDE.md

本仓库自动收集论文，两条独立数据线，共享 `common.py`（分类器/抓取/LLM）与 `config.yaml`。

## 常用命令

```bash
python3 daily_arxiv.py --days 3          # 日报（本地调试用，会写 .cache/daily_seen.json）
python3 collect.py --conference CVPR --year 2024 --no-enrich   # 顶会线小范围调试
python3 collect.py                       # 顶会线全量（慢：DBLP 限速 2s/请求）
python3 update_readme.py                 # 刷新 README 自动索引区
```

依赖：仅 `pyyaml`（用 urllib，不装 requests）。

## 架构

- `config.yaml` — 所有可调参数：16 个领域（topics，关键词/must_any/exclude/weight）、会议、上限、LLM 配置、作者→机构映射。**改这个文件后 push，顶会 workflow 自动重跑**。
- `common.py` — `Classifier`（标题+摘要关键词打分）、arXiv 抓取（带 .cache 磁盘缓存）、`LLM`（OpenAI 兼容，无 Key 自动 disabled）、`http_get`（退避重试）。
- `collect.py` — DBLP 检索（venue:XXX + 关键词轮询）→ 归类 → arXiv 摘要 + S2 引用 enrich → `topics/<slug>/Guideline <year>.md`。同一论文跨领域只在最高分领域完整展开，其余给链接（防重复）。
- `daily_arxiv.py` — cs.CV 近 N 天 → 过滤 → 每领域 top-K → LLM 批量中文评估（可选）→ `daily/arxiv_report_<date>.md`。`daily_seen.json` 跨运行去重。

## 数据源现状（2026-08 探测）

| 源 | 状态 | 用途 |
|----|------|------|
| DBLP | ✅ | 顶会论文列表（注意 2s 限速，快了断连） |
| arXiv API | ✅ | 摘要、日报主源 |
| Semantic Scholar | ⚠️ 限流 ~1rps | 引用数（重要性排序），带缓存+退避 |
| OpenReview | ❌ 有 challenge 验证 | 暂不可用，机构靠 config 的 author_map |
| Papers with Code | ⚠️ | 代码链接，best-effort |

## 注意

- 生成物（topics/ daily/ README 索引区）由 bot 自动提交，人工改动会被下次运行覆盖；人工内容写在自动标记（`<!-- AUTO-INDEX -->`）之外。
- `.cache/` 整体 gitignore，仅 `daily_seen.json` 入库。
- 日期语义：日报的"最近 N 天"按 arXiv 提交日期过滤；周日/周一数据空是正常的。
