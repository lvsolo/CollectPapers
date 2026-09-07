# Occupancy — 2026 Guideline

> 领域: 占用栅格 / 占用网络（Occupancy Prediction / Occ3D）
> 论文数: 1 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份:

### VerseCrafter: Dynamic Realistic Video World Model with 4D Geometric Control **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2601.05138](https://arxiv.org/abs/2601.05138)
- **作者**: Sixiao Zheng, Minghao Yin, Wenbo Hu, Xiaoyu Li, Ying Shan, Yanwei Fu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2026
- **摘要（中）**: ①针对视频世界模型难以统一且精确控制相机与多物体运动的问题，现有方法受限于2D图像平面投影。②提出VerseCrafter，一种几何驱动的视频世界模型，采用新颖的4D几何控制表示，将世界状态编码为静态背景点云和每个物体的3D高斯轨迹，并渲染为4D控制图以引导预训练视频扩散模型。③相比刚性边界框和参数化模型，该表示是类别无关的，能捕捉物体运动路径和概率性3D占用，实现高保真、视角一致的视频生成。④构建了包含35K训练样本的VerseControl4D真实世界数据集，实验表明该方法能忠实遵循指定动态生成高质量视频。
- **摘要（英）**: This paper addresses the challenge of unified and precise control over camera and multi-object motion in video world models, which are limited by 2D projection. It proposes VerseCrafter, a geometry-driven model using a 4D Geometric Control representation with static background point clouds and per-object 3D Gaussian trajectories, rendered into control maps for a pretrained video diffusion model. This category-agnostic approach outperforms rigid bounding boxes, and a 35K-sample dataset enables high-fidelity, view-consistent video generation.
- **核心贡献**: 提出一种统一的4D几何控制表示和配套数据引擎，实现动态视频的精确几何控制。
- **创新点**: 利用3D高斯轨迹和概率占用替代传统边界框，实现类别无关的物体运动控制。
- **结果**: 在35K真实样本上训练，生成视频在动态保真度和视角一致性上表现优异。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Video world models aim to simulate dynamic, real-world environments, yet existing methods struggle to provide unified and precise control over camera and multi-object motion, as videos inherently capture dynamics in the projected 2D image plane. To bridge this gap, we introduce VerseCrafter, a geometry-driven video world model that generates dynamic, realistic videos from a unified 4D geometric world state. Our approach is centered on a novel 4D Geometric Control representation, which encodes the world state as a static background point cloud and per-object 3D Gaussian trajectories. This representation captures each object's motion path and probabilistic 3D occupancy over time, providing a flexible, category-agnostic alternative to rigid bounding boxes and parametric models. We render 4D Geometric Control into 4D control maps for a pretrained video diffusion model, enabling high-fidelity, view-consistent video generation that faithfully follows the specified dynamics. To enable training at scale, we develop an automatic data engine and construct VerseControl4D, a real-world dataset of 35K training samples with automatically derived prompts and rendered 4D control maps. Extensive experiments show that VerseCrafter achieves superior visual quality and more accurate control over camera and multi-object motion than prior methods.

</details>

<!-- COMPLETE v1 papers=1 -->
