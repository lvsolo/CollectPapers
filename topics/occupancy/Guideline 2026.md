# Occupancy — 2026 Guideline

> 领域: 占用栅格 / 占用网络（Occupancy Prediction / Occ3D）
> 论文数: 1 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### VerseCrafter: Dynamic Realistic Video World Model with 4D Geometric Control
- **链接**: [arXiv:2601.05138](https://arxiv.org/abs/2601.05138)
- **作者**: Sixiao Zheng, Minghao Yin, Wenbo Hu, Xiaoyu Li, Ying Shan, Yanwei Fu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2026

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Video world models aim to simulate dynamic, real-world environments, yet existing methods struggle to provide unified and precise control over camera and multi-object motion, as videos inherently capture dynamics in the projected 2D image plane. To bridge this gap, we introduce VerseCrafter, a geometry-driven video world model that generates dynamic, realistic videos from a unified 4D geometric world state. Our approach is centered on a novel 4D Geometric Control representation, which encodes the world state as a static background point cloud and per-object 3D Gaussian trajectories. This representation captures each object's motion path and probabilistic 3D occupancy over time, providing a flexible, category-agnostic alternative to rigid bounding boxes and parametric models. We render 4D Geometric Control into 4D control maps for a pretrained video diffusion model, enabling high-fidelity, view-consistent video generation that faithfully follows the specified dynamics. To enable training at scale, we develop an automatic data engine and construct VerseControl4D, a real-world dataset of 35K training samples with automatically derived prompts and rendered 4D control maps. Extensive experiments show that VerseCrafter achieves superior visual quality and more accurate control over camera and multi-object motion than prior methods.

</details>
<!-- COMPLETE v1 papers=1 -->
