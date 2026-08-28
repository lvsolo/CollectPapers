# Open-set Detection — 2025 Guideline

> 领域: 开放类检测总类（开放词表 OVD / 开放世界 OWOD / 开集 OOD / 未知类检测）
> 论文数: 4 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Any3DIS: Class-Agnostic 3D Instance Segmentation by 2D Mask Tracking.
- **链接**: [arXiv:2411.16183](https://arxiv.org/abs/2411.16183) · 📚 被引 2
- **作者**: Phuc Nguyen, Minh Luu, Anh Tuan Tran, Cuong Pham, Khoi Nguyen
- **🏷️ 机构**: MovianAI, Qualcomm AI Research, Qualcomm Vietnam Company Limited
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing 3D instance segmentation methods frequently encounter issues with over-segmentation, leading to redundant and inaccurate 3D proposals that complicate downstream tasks. This challenge arises from their unsupervised merging approach, where dense 2D instance masks are lifted across frames into point clouds to form 3D candidate proposals without direct supervision. These candidates are then hierarchically merged based on heuristic criteria, often resulting in numerous redundant segments that fail to combine into precise 3D proposals. To overcome these limitations, we propose a 3D-Aware 2D Mask Tracking module that uses robust 3D priors from a 2D mask segmentation and tracking foundation model (SAM-2) to ensure consistent object masks across video frames. Rather than merging all visible superpoints across views to create a 3D mask, our 3D Mask Optimization module leverages a dynamic programming algorithm to select an optimal set of views, refining the superpoints to produce a final 3D proposal for each object. Our approach achieves comprehensive object coverage within the scene while reducing unnecessary proposals, which could otherwise impair downstream applications. Evaluations on ScanNet200 and ScanNet++ confirm the effectiveness of our method, with improvements across Class-Agnostic, Open-Vocabulary, and Open-Ended 3D Instance Segmentation tasks.

</details>

## 跨领域论文（完整笔记在其他领域）

- Percept, Memory, and Imagine: World Feature Simulating for Open-Domain Unknown Object Detection. → [object-detection](../object-detection/Guideline%202025.md)
- OW-OVD: Unified Open World and Open Vocabulary Object Detection. → [object-detection](../object-detection/Guideline%202025.md)
- ODE: Open-Set Evaluation of Hallucinations in Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202025.md)
