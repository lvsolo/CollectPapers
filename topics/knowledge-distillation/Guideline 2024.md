# Knowledge Distillation — 2024 Guideline

> 领域: 知识蒸馏（特征/逻辑蒸馏、VLM 蒸馏、自蒸馏）
> 论文数: 3 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: [2022](Guideline%202022.md)

### MVIP-NeRF: Multi-View 3D Inpainting on NeRF Scenes via Diffusion Prior. **⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2405.02859](https://arxiv.org/abs/2405.02859) · 📚 被引 27
- **作者**: Honghua Chen, Chen Change Loy, Xingang Pan
- **🏷️ 机构**: Nanyang Technological University,S-Lab
- **会议**: CVPR 2024
- **摘要（中）**: ①针对NeRF场景修复中依赖2D修复器导致跨视角不一致和几何质量差的问题。②提出了MVIP-NeRF，利用扩散先验进行多视图联合修复，通过基于分数蒸馏采样（SDS）的迭代优化同时处理外观和几何，并引入法线图作为几何表示，定义法线SDS损失以促进几何修复与外观对齐。③相比现有方法，创新性地从多视图联合蒸馏扩散先验，确保跨视角一致性，并显式建模几何。④实验表明该方法在合成和真实场景中均优于基线，有效提升修复质量和一致性。
- **摘要（英）**: This paper addresses the limitations of NeRF inpainting methods that rely on 2D inpainters, which cause view inconsistency and poor geometry. It proposes MVIP-NeRF, which leverages diffusion priors via Score Distillation Sampling for joint multi-view inpainting, incorporating normal map-based geometric supervision. The method improves cross-view consistency and geometry alignment, outperforming baselines on synthetic and real scenes.
- **核心贡献**: 提出首个利用扩散先验进行多视图联合NeRF修复的方法，兼顾外观与几何。
- **创新点**: 设计多视图SDS分数函数和法线SDS损失，实现跨视角一致的几何与外观修复。
- **结果**: 在合成和真实场景中显著提升修复质量和跨视角一致性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite the emergence of successful NeRF inpainting methods built upon explicit RGB and depth 2D inpainting supervisions, these methods are inherently constrained by the capabilities of their underlying 2D inpainters. This is due to two key reasons: (i) independently inpainting constituent images results in view-inconsistent imagery, and (ii) 2D inpainters struggle to ensure high-quality geometry completion and alignment with inpainted RGB images. To overcome these limitations, we propose a novel approach called MVIP-NeRF that harnesses the potential of diffusion priors for NeRF inpainting, addressing both appearance and geometry aspects. MVIP-NeRF performs joint inpainting across multiple views to reach a consistent solution, which is achieved via an iterative optimization process based on Score Distillation Sampling (SDS). Apart from recovering the rendered RGB images, we also extract normal maps as a geometric representation and define a normal SDS loss that motivates accurate geometry inpainting and alignment with the appearance. Additionally, we formulate a multi-view SDS score function to distill generative priors simultaneously from different view images, ensuring consistent visual completion when dealing with large view variations. Our experimental results show better appearance and geometry recovery than previous NeRF inpainting methods.

</details>

## 跨领域论文（完整笔记在其他领域）

- Weak-to-Strong 3D Object Detection with X-Ray Distillation. → [3d-detection](../3d-detection/Guideline%202024.md)
- On the Road to Portability: Compressing End-to-End Motion Planner for Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202024.md)
