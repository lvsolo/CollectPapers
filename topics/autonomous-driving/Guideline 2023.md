# Autonomous Driving — 2023 Guideline

> 领域: 自动驾驶感知与系统（端到端驾驶、规划、驾驶场景理解、数据集基准）
> 论文数: 1 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Transcendental Idealism of Planner: Evaluating Perception from Planning Perspective for Autonomous Driving.
- **链接**: [arXiv:2306.07276](https://arxiv.org/abs/2306.07276)
- **作者**: Weixin Li, Xiaodong Yang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Evaluating the performance of perception modules in autonomous driving is one of the most critical tasks in developing the complex intelligent system. While module-level unit test metrics adopted from traditional computer vision tasks are feasible to some extent, it remains far less explored to measure the impact of perceptual noise on the driving quality of autonomous vehicles in a consistent and holistic manner. In this work, we propose a principled framework that provides a coherent and systematic understanding of the impact an error in the perception module imposes on an autonomous agent's planning that actually controls the vehicle. Specifically, the planning process is formulated as expected utility maximisation, where all input signals from upstream modules jointly provide a world state description, and the planner strives for the optimal action by maximising the expected utility determined by both world states and actions. We show that, under practical conditions, the objective function can be represented as an inner product between the world state description and the utility function in a Hilbert space. This geometric interpretation enables a novel way to analyse the impact of noise in world state estimation on planning and leads to a universal metric for evaluating perception. The whole framework resembles the idea of transcendental idealism in the classical philosophical literature, which gives the name to our approach.

</details>
