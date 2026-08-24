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

# S2 免费档全局限速（跨函数共享）：两次请求至少间隔 1.3s
_S2_LAST = [0.0]


def _s2_throttle() -> None:
    wait = 1.3 - (time.time() - _S2_LAST[0])
    if wait > 0:
        time.sleep(wait)
    _S2_LAST[0] = time.time()


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
GITHUB_RE = re.compile(
    r"(?:https?://)?(?:www\.)?github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)", re.I)


def code_link_from_abstract(abstract: str) -> str | None:
    """从 arXiv 摘要里提取作者自报的 GitHub 仓库链接（最可信的官方代码源）。"""
    if not abstract:
        return None
    for m in GITHUB_RE.finditer(abstract):
        repo = m.group(1).rstrip(".")
        # 过滤明显不是论文代码库的（github.io 主页、org 主页等）
        if repo.lower().endswith((".github.io",)):
            continue
        parts = repo.split("/")
        if len(parts) == 2 and all(parts):
            return f"https://github.com/{repo}"
    return None


def pwc_link(title: str) -> dict | None:
    """查询 Papers with Code。返回 {'official': github_url|None, 'page': pwc_url}。"""
    q = urllib.parse.quote(title[:120])
    data = http_get_json(
        f"https://paperswithcode.com/api/v1/search/?q={q}&per_page=3",
        cache_hours=168, retries=1, timeout=15)
    if not data or not data.get("results"):
        return None
    for r in data["results"]:
        p = r.get("paper") or {}
        if _title_sim(title, p.get("title", "")) <= 0.82:
            continue
        out = {"official": None, "page": None}
        if r.get("url"):
            out["page"] = (f"https://paperswithcode.com{r['url']}"
                           if r["url"].startswith("/") else r["url"])
        pid = str(p.get("id", ""))
        if pid:
            detail = http_get_json(
                f"https://paperswithcode.com/api/v1/papers/{pid}/",
                cache_hours=168, retries=1, timeout=15)
            if detail and detail.get("official_implementation"):
                out["official"] = detail["official_implementation"]
        return out
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
- "summary_cn": 3-4 句中文概括，必须回答：①这篇论文针对什么问题 ②提出了什么方法/做了什么 ③相比已有工作的改进点 ④取得的效果（摘要中有数据就引用具体数据）。写给本领域研究者看，不要空话。
- "summary_en": 2-3 句英文概括，同上四点，用纯正学术英语。
- "assessment": 1-2 句中文总体评估（为什么值得关注）
- "contribution": 1 句中文：核心贡献
- "innovation": 1 句中文：创新点
- "result": 1 句中文：取得的效果

多篇论文时输出 JSON 数组，如 [{{...}}, {{...}}]。

论文列表：
{papers}"""


EVAL_PROMPT_VERSION = "v2"  # 改 prompt 时递增，使旧缓存失效


def llm_eval_papers(llm: LLM, papers: list[dict], topic_names: str) -> list[dict]:
    """批量评估，结果按 (arxiv_id|prompt版本) 磁盘缓存 —— 重复运行不重复计费。"""
    cache_path = CACHE_DIR / "llm_evals.json"
    cache: dict = {}
    if cache_path.exists():
        try:
            cache = json.loads(cache_path.read_text())
        except json.JSONDecodeError:
            cache = {}

    def key(pid: str) -> str:
        return f"{pid}|{EVAL_PROMPT_VERSION}"

    results, todo = [], []
    for p in papers:
        pid = p.get("arxiv_id") or p.get("title")
        hit = cache.get(key(pid))
        if hit:
            results.append(hit)
        else:
            todo.append(p)
    if papers:
        log(f"  LLM cache: {len(results)}/{len(papers)} hit, {len(todo)} to evaluate")

    dirty = False
    for i in range(0, len(todo), llm.batch):
        batch = todo[i:i + llm.batch]
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
                item["_arxiv_id"] = batch[item["id"] - 1]["arxiv_id"]  # arxiv_id 或 title 作键
                results.append(item)
                cache[key(item["_arxiv_id"])] = item
                dirty = True
        time.sleep(1)  # 温和限速
    if dirty:
        cache_path.write_text(json.dumps(cache, ensure_ascii=False))
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
AFFIL_CACHE = CACHE_DIR / "affiliations.json"


def _affil_cache() -> dict:
    if AFFIL_CACHE.exists():
        try:
            return json.loads(AFFIL_CACHE.read_text())
        except json.JSONDecodeError:
            return {}
    return {}


def _save_affil(cache: dict) -> None:
    AFFIL_CACHE.write_text(json.dumps(cache, ensure_ascii=False))


def crossref_paper(title: str) -> dict | None:
    """Crossref 查论文：返回 {'citations': int, 'affiliations': [str]}。免费无需 Key。
    实测数据质量好（BEVFormer → 南大/上海AI Lab/NVIDIA + 261 引用）。"""
    q = urllib.parse.quote(title[:250])
    data = http_get_json(
        f"https://api.crossref.org/works?query.bibliographic={q}&rows=1"
        f"&select=title,is-referenced-by-count,author",
        cache_hours=0, retries=2, timeout=15)
    if not data:
        return None
    try:
        item = data["message"]["items"][0]
    except (KeyError, IndexError):
        return None
    # 标题相似度校验（crossref 是模糊检索，防错配）
    got = (item.get("title") or [""])[0]
    if _title_sim(title, got) < 0.7:
        return None
    out = {"citations": item.get("is-referenced-by-count", 0), "affiliations": []}
    for a in item.get("author", [])[:8]:
        for aff in (a.get("affiliation") or []):
            name = aff.get("name")
            if name and name not in out["affiliations"]:
                out["affiliations"].append(name)
    return out


def s2_affiliations(title: str, authors: list[str]) -> list[str] | None:
    """机构反查：Crossref 主源（免费稳定）→ S2 备源（限流严重）。None=未查到。"""
    cache = _affil_cache()
    key = title.lower().rstrip(". ")[:180]
    if key in cache:
        return cache[key]  # 可能是 []（确认过没有）

    insts: list[str] | None = None
    # 1) Crossref（不限流，优先）
    cr = crossref_paper(title)
    if cr and cr["affiliations"]:
        insts = cr["affiliations"][:3]
    # 2) S2 兜底（Crossref 无机构数据时才走，限流返回 None 不缓存）
    if insts is None:
        import os
        q = urllib.parse.quote(title[:200])
        headers = {"x-api-key": os.environ["S2_API_KEY"]} if os.environ.get("S2_API_KEY") else None
        _s2_throttle()
        data = http_get_json(
            f"https://api.semanticscholar.org/graph/v1/paper/search/match?query={q}"
            f"&fields=authors.name,authors.affiliations",
            cache_hours=0, retries=2, timeout=15, headers=headers)
        if data is not None and data.get("data"):
            insts = []
            try:
                for a in data["data"][0].get("authors", []):
                    for aff in (a.get("affiliations") or []):
                        if aff and aff not in insts:
                            insts.append(aff)
                insts = insts[:3] or None
            except (KeyError, IndexError, TypeError):
                insts = None
        elif data is None and cr is None:
            return None  # 两源都网络失败：不写缓存，下次重试
    cache[key] = insts or []  # 查到了（含确认没有=负缓存）
    _save_affil(cache)
    return insts


def institution_for(authors: list[str]) -> str | None:
    """本地映射表快速通道（config.yaml author_map）。"""
    amap = CONFIG.get("institutions", {}).get("author_map", {})
    hits = []
    for a in authors[:8]:
        inst = amap.get(a)
        if inst and inst not in hits:
            hits.append(inst)
    return ", ".join(hits[:2]) if hits else None


def institutions_for_paper(paper: dict, *, online: bool = True) -> str:
    """机构标注主入口：映射表 → S2 反查 → '（机构待查）'。
    所有渲染端必须调用此函数，保证每篇论文都有机构行。"""
    authors = paper.get("authors") or paper.get("arxiv_authors") or []
    local = institution_for(authors)
    if local:
        return local
    if online:
        s2 = s2_affiliations(paper["title"], authors)
        if s2:
            # 取前三个不同机构（第一作者单位最有分量）
            return ", ".join(s2[:3])
    return "（机构待查）"


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
