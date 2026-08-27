# CollectPapers

自动收集我关心的研究领域的论文，两条线并行：

1. **顶会 Guideline 线**：CVPR / ECCV / ICCV / NeurIPS / ICLR / ICML（2020→2026）录用论文，
   按 16 个领域归类，每领域每年一份 `Guideline 20xx.md`，按重要性排序，含论文链接/作者/机构/摘要与核心内容。
2. **arXiv 日报线**：每天抓取 arXiv 新论文，过滤出相关领域的，生成 `daily/arxiv_report_YYYY-MM-DD.md`
   （配置 LLM Key 后带中文评估：星级/相关度/核心贡献/创新点/方法/结果）。

<!-- AUTO-INDEX-BEGIN -->
## 📂 领域索引（顶会 Guideline）

| 领域 | 说明 |
|------|------|
| **Object Detection** | 通用 2D 目标检测（检测器架构、密集预测、小物体/旋转框/NMS 等）<br/>[2025](topics/object-detection/Guideline%202025.md) [2024](topics/object-detection/Guideline%202024.md) [2023](topics/object-detection/Guideline%202023.md) [2022](topics/object-detection/Guideline%202022.md) [2021](topics/object-detection/Guideline%202021.md) [2020](topics/object-detection/Guideline%202020.md) |
| **Autonomous Driving** | 自动驾驶感知与系统（端到端驾驶、规划、驾驶场景理解、数据集基准）<br/>[2025](topics/autonomous-driving/Guideline%202025.md) [2024](topics/autonomous-driving/Guideline%202024.md) [2023](topics/autonomous-driving/Guideline%202023.md) [2022](topics/autonomous-driving/Guideline%202022.md) [2021](topics/autonomous-driving/Guideline%202021.md) [2020](topics/autonomous-driving/Guideline%202020.md) |
| **3D Detection** | 3D 目标检测（LiDAR / 相机 / 多模态融合）<br/>[2025](topics/3d-detection/Guideline%202025.md) [2024](topics/3d-detection/Guideline%202024.md) [2023](topics/3d-detection/Guideline%202023.md) [2022](topics/3d-detection/Guideline%202022.md) [2021](topics/3d-detection/Guideline%202021.md) [2020](topics/3d-detection/Guideline%202020.md) |
| **BEV** | 鸟瞰图感知（BEV 特征、BEV 检测/分割/预测）<br/>[2025](topics/bev/Guideline%202025.md) [2024](topics/bev/Guideline%202024.md) [2023](topics/bev/Guideline%202023.md) [2022](topics/bev/Guideline%202022.md) [2021](topics/bev/Guideline%202021.md) [2020](topics/bev/Guideline%202020.md) |
| **Occupancy** | 占用栅格 / 占用网络（Occupancy Prediction / Occ3D）<br/>[2025](topics/occupancy/Guideline%202025.md) [2024](topics/occupancy/Guideline%202024.md) [2023](topics/occupancy/Guideline%202023.md) [2022](topics/occupancy/Guideline%202022.md) [2021](topics/occupancy/Guideline%202021.md) [2020](topics/occupancy/Guideline%202020.md) |
| **Multi-camera Perception** | 多相机 / 多视角感知（环视、深度估计与 3D 预测）<br/>[2025](topics/multi-camera-perception/Guideline%202025.md) [2024](topics/multi-camera-perception/Guideline%202024.md) [2023](topics/multi-camera-perception/Guideline%202023.md) [2022](topics/multi-camera-perception/Guideline%202022.md) [2021](topics/multi-camera-perception/Guideline%202021.md) [2020](topics/multi-camera-perception/Guideline%202020.md) |
| **Tracking** | 目标跟踪（MOT / 3D 跟踪 / 多目标多相机跟踪）<br/>[2025](topics/tracking/Guideline%202025.md) [2024](topics/tracking/Guideline%202024.md) [2023](topics/tracking/Guideline%202023.md) [2022](topics/tracking/Guideline%202022.md) [2021](topics/tracking/Guideline%202021.md) [2020](topics/tracking/Guideline%202020.md) |
| **Open-set Detection** | 开放类检测总类（开放词表 OVD / 开放世界 OWOD / 开集 OOD / 未知类检测）<br/>[2025](topics/open-set-detection/Guideline%202025.md) [2024](topics/open-set-detection/Guideline%202024.md) [2023](topics/open-set-detection/Guideline%202023.md) [2022](topics/open-set-detection/Guideline%202022.md) [2021](topics/open-set-detection/Guideline%202021.md) [2020](topics/open-set-detection/Guideline%202020.md) |
| **FOD Detection** | 自动驾驶路面异物/异常物体检测（Road Anomaly / 小物体检测 / 可碾压性判断）<br/>[2021](topics/fod-detection/Guideline%202021.md) |
| **VLM** | 视觉语言模型（多模态大模型、CLIP 系、grounding）<br/>[2025](topics/vlm/Guideline%202025.md) [2024](topics/vlm/Guideline%202024.md) [2023](topics/vlm/Guideline%202023.md) [2022](topics/vlm/Guideline%202022.md) [2021](topics/vlm/Guideline%202021.md) [2020](topics/vlm/Guideline%202020.md) |
| **Vision Transformer** | 视觉 Transformer（ViT、混合架构、高效注意力）<br/>[2025](topics/vision-transformer/Guideline%202025.md) [2024](topics/vision-transformer/Guideline%202024.md) [2023](topics/vision-transformer/Guideline%202023.md) [2022](topics/vision-transformer/Guideline%202022.md) |
| **Self-supervised Vision** | 视觉自监督学习（对比学习、MAE、DINO 系）<br/>[2025](topics/self-supervised-vision/Guideline%202025.md) [2024](topics/self-supervised-vision/Guideline%202024.md) [2023](topics/self-supervised-vision/Guideline%202023.md) [2022](topics/self-supervised-vision/Guideline%202022.md) [2021](topics/self-supervised-vision/Guideline%202021.md) [2020](topics/self-supervised-vision/Guideline%202020.md) |
| **Video Understanding** | 视频理解（动作识别、时序动作、视频大模型）<br/>[2025](topics/video-understanding/Guideline%202025.md) [2024](topics/video-understanding/Guideline%202024.md) [2023](topics/video-understanding/Guideline%202023.md) [2022](topics/video-understanding/Guideline%202022.md) [2021](topics/video-understanding/Guideline%202021.md) [2020](topics/video-understanding/Guideline%202020.md) |
| **Multimodal** | 多模态学习（图文对齐、融合、多模态融合感知）<br/>[2025](topics/multimodal/Guideline%202025.md) [2024](topics/multimodal/Guideline%202024.md) [2023](topics/multimodal/Guideline%202023.md) [2022](topics/multimodal/Guideline%202022.md) [2021](topics/multimodal/Guideline%202021.md) [2020](topics/multimodal/Guideline%202020.md) |
| **Continual Learning** | 持续学习 / 增量学习（含 VLM/多模态场景）<br/>[2025](topics/continual-learning/Guideline%202025.md) [2024](topics/continual-learning/Guideline%202024.md) [2023](topics/continual-learning/Guideline%202023.md) [2022](topics/continual-learning/Guideline%202022.md) [2021](topics/continual-learning/Guideline%202021.md) [2020](topics/continual-learning/Guideline%202020.md) |
| **Neural Architecture Search** | 神经架构搜索（NAS、Zero-Cost、搜索空间）<br/>[2025](topics/neural-architecture-search/Guideline%202025.md) [2024](topics/neural-architecture-search/Guideline%202024.md) [2023](topics/neural-architecture-search/Guideline%202023.md) [2022](topics/neural-architecture-search/Guideline%202022.md) [2021](topics/neural-architecture-search/Guideline%202021.md) [2020](topics/neural-architecture-search/Guideline%202020.md) |
| **Network Pruning** | 网络剪枝 / 模型压缩（结构化剪枝、稀疏化）<br/>[2025](topics/network-pruning/Guideline%202025.md) [2024](topics/network-pruning/Guideline%202024.md) [2023](topics/network-pruning/Guideline%202023.md) [2022](topics/network-pruning/Guideline%202022.md) [2021](topics/network-pruning/Guideline%202021.md) [2020](topics/network-pruning/Guideline%202020.md) |
| **Knowledge Distillation** | 知识蒸馏（特征/逻辑蒸馏、VLM 蒸馏、自蒸馏）<br/>[2025](topics/knowledge-distillation/Guideline%202025.md) |

## 📰 最近日报（arXiv daily）

- [2026-08-24](daily/arxiv_report_2026-08-24.md)

<!-- AUTO-INDEX-END -->

## 目录结构

```
config.yaml          # 领域/关键词/会议/数量上限 —— 想改关注领域只改这里
common.py            # 共享库：分类器、arXiv/DBLP/S2 抓取、LLM 评估
collect.py           # 顶会线脚本
daily_arxiv.py       # 日报线脚本
update_readme.py     # 刷新本页索引
topics/<slug>/Guideline 20xx.md
daily/arxiv_report_YYYY-MM-DD.md
```

## 定时任务（GitHub Actions）

| Workflow | 频率 | 内容 |
|----------|------|------|
| Daily arXiv Report | 每天北京时间 02:23（UTC 18:23） | 抓最近 3 天 arXiv，去重后生成当日报告 |
| Conference Guidelines Update | 每两天北京时间 02:41（UTC 18:41） | 增量刷新六大顶会 Guideline（增量缓存，非公布季自动跳过） |

两者均支持 Actions 页面手动触发（workflow_dispatch）。修改 `config.yaml` 会自动触发顶会线重刷。

## 领域列表

3D Detection · BEV · Occupancy · Multi-camera Perception · Tracking · Open Vocabulary Detection ·
FOD Detection · VLM · Vision Transformer · 自监督视觉 · 视频理解 · Multimodal · Continual Learning ·
Neural Architecture Search · Network Pruning · Knowledge Distillation

（在 `config.yaml` 的 `topics:` 里增删，改完 push 即生效）

## 可选配置（让日报带中文评估）

在仓库 Settings → Secrets → Actions 里添加：

| Secret | 说明 | 示例 |
|--------|------|------|
| `LLM_API_BASE` | OpenAI 兼容接口地址 | `https://api.deepseek.com/v1` |
| `LLM_API_KEY` | API Key | `sk-...` |
| `LLM_MODEL` | 模型名 | `deepseek-chat` |
| `S2_API_KEY` | （可选）Semantic Scholar Key，提升引用数抓取成功率 | 免费申请 |

不配置时日报自动降级为关键词+摘要摘录模式，其余功能不受影响。

## 本地运行

```bash
pip install pyyaml
python3 daily_arxiv.py            # 日报
python3 collect.py                # 顶会全量（首次较慢）
python3 collect.py --conference CVPR --year 2024 --no-enrich   # 调试
```
