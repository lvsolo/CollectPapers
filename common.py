"""CollectPapers 共享库：领域分类、arXiv/DBLP 抓取、LLM 评估、机构标注。"""

import html
import json
import os
import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent
CONFIG = yaml.safe_load((ROOT / "config.yaml").read_text(encoding="utf-8"))

ARXIV_NS = {"a": "http://www.w3.org/2005/Atom"}
UA = "CollectPapers/1.0 (github.com/lvsolo/CollectPapers; research paper tracker)"
CACHE_DIR = ROOT / ".cache"
CACHE_DIR.mkdir(exist_ok=True)


# ----------------------------------------------------------------------
# HTTP helpers（带磁盘缓存 + 简单退避）
# ----------------------------------------------------------------------
def _cache_path(key: str) -> Path:
    safe = re.sub(r"[^A-Za-z0-9_.-]", "_", key)[:180]
    return CACHE_DIR / f"{safe}.json"


def http_get(url: str, *, cache_hours: float = 0.0, timeout: int = 30,
             retries: int = 4, headers: dict | None = None) -> bytes | None:
    """GET with disk cache and exponential backoff. Returns None on final failure."""
    cp = _cache_path(f"get:{url}")
    if cache_hours > 0 and cp.exists():
        age = time.time() - cp.stat().st_mtime
        if age < cache_hours * 3600:
            return json.loads(cp.read_text())["data"].encode()

    hdrs = {"User-Agent": UA}
    if headers:
        hdrs.update(headers)
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=hdrs)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                data = r.read()
            if cache_hours > 0:
                cp.write_text(json.dumps({"data": data.decode("utf-8", "replace")}))
            return data
        except Exception as e:  # noqa: BLE001 - network layer, degrade gracefully
            wait = min(3 ** attempt + 2, 40)
            log(f"  ! GET failed ({e}), retry in {wait}s: {url[:100]}")
            time.sleep(wait)
    return None


def http_get_json(url: str, **kw):
    raw = http_get(url, **kw)
    if raw is None:
        return None
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return None


def log(msg: str) -> None:
    print(msg, flush=True)


def clean_text(s: str) -> str:
    """解码 HTML 实体、去除 DBLP 作者数字后缀、压缩空白。"""
    s = html.unescape(s or "")
    s = re.sub(r"\s+\d{4}$", "", s)  # DBLP 消歧后缀 "Xinyu Huang 0001"
    return " ".join(s.split())


# ----------------------------------------------------------------------
# 领域分类
# ----------------------------------------------------------------------
class Classifier:
    def __init__(self, topics: list[dict]):
        self.topics = topics
        self._compiled = []
        for t in topics:
            kws = [k.lower() for k in t.get("keywords", [])]
            must = re.compile(t["must_any"], re.I) if t.get("must_any") else None
            exc = [re.compile(e, re.I) for e in t.get("exclude", [])]
            self._compiled.append((t, kws, must, exc))

    def classify(self, title: str, abstract: str) -> list[tuple[dict, int]]:
        """返回 [(topic_dict, score)]，score = 摘要命中数*2 + 标题命中数*3。"""
        text = f"{title}\n{abstract}".lower()
        title_l = title.lower()
        out = []
        for t, kws, must, excs in self._compiled:
            if must and not (must.search(title) or must.search(text)):
                continue
            if any(e.search(title) for e in excs):
                continue
            score = sum(3 for k in kws if k in title_l) + sum(2 for k in kws if k in text)
            if score > 0:
                out.append((t, score))
        return out


def get_classifier() -> Classifier:
    return Classifier(CONFIG["topics"])


# ----------------------------------------------------------------------
# arXiv 抓取
# ----------------------------------------------------------------------
def arxiv_fetch(query: str, max_results: int, sortby: str = "submittedDate") -> list[dict]:
    """按查询抓 arXiv，返回 [{arxiv_id,title,abstract,authors,cats,date,url}]。"""
    q = urllib.parse.quote(query)
    url = (f"http://export.arxiv.org/api/query?search_query={q}"
           f"&max_results={max_results}&sortBy={sortby}&sortOrder=descending")
    raw = http_get(url, cache_hours=6, retries=3)
    if raw is None:
        return []
    try:
        root = ET.fromstring(raw)
    except ET.ParseError:
        return []
    papers = []
    for e in root.findall("a:entry", ARXIV_NS):
        aid = (e.findtext("a:id", "", ARXIV_NS) or "").split("/abs/")[-1]
        aid = re.sub(r"v\d+$", "", aid)
        papers.append({
            "arxiv_id": aid,
            "title": " ".join((e.findtext("a:title", "", ARXIV_NS) or "").split()),
            "abstract": " ".join((e.findtext("a:summary", "", ARXIV_NS) or "").split()),
            "authors": [a.findtext("a:name", "", ARXIV_NS) for a in e.findall("a:author", ARXIV_NS)],
            "cats": [c.get("term") for c in e.findall("a:category", ARXIV_NS)],
            "date": e.findtext("a:published", "", ARXIV_NS)[:10],
            "url": f"https://arxiv.org/abs/{aid}",
        })
    return papers


def arxiv_by_ids(ids: list[str]) -> list[dict]:
    """按 id_list 批量取论文详情（用于顶会线补摘要）。"""
    if not ids:
        return []
    out = []
    for i in range(0, len(ids), 60):
        chunk = ids[i:i + 60]
        url = (f"http://export.arxiv.org/api/query?id_list={','.join(chunk)}"
               f"&max_results={len(chunk)}")
        raw = http_get(url, cache_hours=168, retries=3)
        if raw is None:
            continue
        try:
            root = ET.fromstring(raw)
        except ET.ParseError:
            continue
        for e in root.findall("a:entry", ARXIV_NS):
            aid = (e.findtext("a:id", "", ARXIV_NS) or "").split("/abs/")[-1]
            aid = re.sub(r"v\d+$", "", aid)
            # arXiv 对失效 id 会返回 error entry（title = 'Error')
            if not aid or (e.findtext("a:title", "", ARXIV_NS) or "").strip() == "Error":
                continue
            out.append({
                "arxiv_id": aid,
                "title": " ".join((e.findtext("a:title", "", ARXIV_NS) or "").split()),
                "abstract": " ".join((e.findtext("a:summary", "", ARXIV_NS) or "").split()),
                "authors": [a.findtext("a:name", "", ARXIV_NS) for a in e.findall("a:author", ARXIV_NS)],
                "cats": [c.get("term") for c in e.findall("a:category", ARXIV_NS)],
                "date": e.findtext("a:published", "", ARXIV_NS)[:10],
                "url": f"https://arxiv.org/abs/{aid}",
            })
    return out


# ----------------------------------------------------------------------
# 代码库链接（Papers with Code，best-effort）
# ----------------------------------------------------------------------
def pwc_link(title: str) -> str | None:
    """查询 Papers with Code API。限流时静默降级。"""
    q = urllib.parse.quote(title[:120])
    data = http_get_json(
        f"https://paperswithcode.com/api/v1/search/?q={q}&per_page=3",
        cache_hours=168, retries=1, timeout=15)
    if not data or not data.get("results"):
        return None
    for r in data["results"]:
        if r.get("paper") and _title_sim(title, r["paper"].get("title", "")) > 0.82:
            if r.get("implementation_count", 0) > 0 or r.get("url"):
                # pwc 返回的 url 是页面；官方 repo 需要另一跳，这里给 PWC 页面即可
                return f"https://paperswithcode.com{r['url']}" if r["url"].startswith("/") else r["url"]
    return None


def _title_sim(a: str, b: str) -> float:
    wa, wb = set(a.lower().split()), set(b.lower().split())
    if not wa or not wb:
        return 0.0
    return len(wa & wb) / max(len(wa), len(wb))


# ----------------------------------------------------------------------
# LLM 中文评估（无 Key 自动降级）
# ----------------------------------------------------------------------
class LLM:
    def __init__(self):
        cfg = CONFIG.get("llm", {})
        self.enabled = cfg.get("enabled", False)
        base = os.environ.get(cfg.get("api_base_env", "LLM_API_BASE"), cfg.get("default_base", ""))
        key = os.environ.get(cfg.get("api_key_env", "LLM_API_KEY"), "")
        model = os.environ.get(cfg.get("model_env", "LLM_MODEL"), cfg.get("default_model", ""))
        self.base = base.rstrip("/")
        self.key = key
        self.model = model
        self.temperature = cfg.get("temperature", 0.2)
        self.timeout = cfg.get("timeout", 120)
        self.batch = cfg.get("max_papers_per_call", 6)
        # 有 key 且有 base 才真正启用
        if not (key and base and model):
            self.enabled = False

    @property
    def active(self) -> bool:
        return self.enabled

    def chat(self, system: str, user: str) -> str | None:
        payload = json.dumps({
            "model": self.model,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            "temperature": self.temperature,
        }).encode()
        req = urllib.request.Request(
            f"{self.base}/chat/completions",
            data=payload,
            headers={"Content-Type": "application/json",
                     "Authorization": f"Bearer {self.key}",
                     "User-Agent": UA})
        for attempt in range(3):
            try:
                with urllib.request.urlopen(req, timeout=self.timeout) as r:
                    out = json.loads(r.read())
                return out["choices"][0]["message"]["content"]
            except Exception as e:  # noqa: BLE001
                log(f"  ! LLM call failed ({e}), attempt {attempt + 1}/3")
                time.sleep(2 ** attempt)
        return None


EVAL_SYSTEM = """你是一位计算机视觉与机器学习领域的资深研究员，负责为自动驾驶感知/视觉方向的研究者筛选和评估论文。
你必须严格按照要求的 JSON 格式输出，不要输出任何 JSON 以外的文字（包括 markdown 代码块标记）。"""

EVAL_PROMPT = """请评估以下 {n} 篇 arXiv 论文（领域：{topics}）。对每篇论文输出一个 JSON 对象，包含：
- "id": 论文序号（如下所列）
- "stars": 1-5 整数星级（重要性与质量综合）
- "relevance": 0-100 整数，与用户研究领域的相关度
- "quality": 0.0-1.0 浮点，方法质量/实验充分度
- "topic": 从以下领域中选择最匹配的一个：{topic_names}
- "assessment": 2-3 句中文总体评估（为什么值得关注/属于什么方向）
- "contribution": 1-2 句中文：核心贡献
- "innovation": 1-2 句中文：创新点
- "method": 2-3 句中文：方法概述
- "result": 1-2 句中文：取得的效果（摘要中有数据就引用数据）
- "impact": 1 句中文：相关性与影响

多篇论文时输出 JSON 数组，如 [{{...}}, {{...}}]。

论文列表：
{papers}"""


def llm_eval_papers(llm: LLM, papers: list[dict], topic_names: str) -> list[dict]:
    """批量评估，返回 [{id, stars, relevance, quality, topic, assessment, ...}]。失败返回 []。"""
    results = []
    for i in range(0, len(papers), llm.batch):
        batch = papers[i:i + llm.batch]
        listing = "\n\n".join(
            f"[{j+1}] 标题: {p['title']}\n    摘要: {p.get('abstract', '')[:1200]}"
            for j, p in enumerate(batch))
        user = EVAL_PROMPT.format(n=len(batch), topics=topic_names,
                                  topic_names=topic_names, papers=listing)
        resp = llm.chat(EVAL_SYSTEM, user)
        if not resp:
            continue
        parsed = _extract_json(resp)
        if parsed is None:
            continue
        if isinstance(parsed, dict):
            parsed = [parsed]
        for item in parsed:
            try:
                item["id"] = int(item.get("id", 0))
            except (TypeError, ValueError):
                continue
            if 1 <= item["id"] <= len(batch):
                item["_arxiv_id"] = batch[item["id"] - 1]["arxiv_id"]
                results.append(item)
        time.sleep(1)  # 温和限速
    return results


def _extract_json(text: str):
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(json)?\s*|\s*```$", "", text, flags=re.S)
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        m = re.search(r"[\[{].*[\]}]", text, re.S)
        if m:
            try:
                return json.loads(m.group())
            except json.JSONDecodeError:
                return None
    return None


# ----------------------------------------------------------------------
# 机构标注
# ----------------------------------------------------------------------
def institution_for(authors: list[str]) -> str | None:
    amap = CONFIG.get("institutions", {}).get("author_map", {})
    hits = []
    for a in authors[:8]:
        inst = amap.get(a)
        if inst and inst not in hits:
            hits.append(inst)
    return ", ".join(hits[:2]) if hits else None


# ----------------------------------------------------------------------
# 重要性排序
# ----------------------------------------------------------------------
IMPORTANT_TOKENS = [
    # 方法名/基准（这些词出现在标题里往往意味着领域里程碑论文）
    r"\bbeit\b", r"\bbeit\b", r"\b(bevdet|bevfusion|bevformer|lift.?splat.?shoot)\b",
    r"\b(centerpoint|pointpillars|pointnet|votenet|smoke|caddit|mmdet3d)\b",
    r"\b(mask2former|oneformer|dino|detr|deformable.?detr|dino.?detr|grounding.?dino)\b",
    r"\b(mae|dino|mocov\d|simclr|byol|ibot)\b",
    r"\b(survey|benchmark|challenge)\b",
    r"\b(swin|vit|deit|pvt)\b",
]


def importance_score(paper: dict, cls_score: float = 0, citations: int | None = None) -> float:
    """启发式重要性：引用数 > 标题信号 > 分类置信度。"""
    s = 0.0
    title = paper.get("title", "")
    for pat in IMPORTANT_TOKENS:
        if re.search(pat, title, re.I):
            s += 2.0
            break
    if citations is not None:
        import math
        s += min(10.0, math.log10(max(citations, 1)) * 3)
    s += min(cls_score, 12) * 0.4
    return s
