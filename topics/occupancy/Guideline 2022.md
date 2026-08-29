# Occupancy — 2022 Guideline

> 领域: 占用栅格 / 占用网络（Occupancy Prediction / Occ3D）
> 论文数: 1 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### End-to-End Trajectory Distribution Prediction Based on Occupancy Grid Maps.
- **链接**: [arXiv:2203.16910](https://arxiv.org/abs/2203.16910) · 📚 被引 49
- **作者**: Ke Guo, Wenxi Liu, Jia Pan
- **🏷️ 机构**: The University of Hong Kong, College of Computer and Data Science, Fuzhou University
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we aim to forecast a future trajectory distribution of a moving agent in the real world, given the social scene images and historical trajectories. Yet, it is a challenging task because the ground-truth distribution is unknown and unobservable, while only one of its samples can be applied for supervising model learning, which is prone to bias. Most recent works focus on predicting diverse trajectories in order to cover all modes of the real distribution, but they may despise the precision and thus give too much credit to unrealistic predictions. To address the issue, we learn the distribution with symmetric cross-entropy using occupancy grid maps as an explicit and scene-compliant approximation to the ground-truth distribution, which can effectively penalize unlikely predictions. In specific, we present an inverse reinforcement learning based multi-modal trajectory distribution forecasting framework that learns to plan by an approximate value iteration network in an end-to-end manner. Besides, based on the predicted distribution, we generate a small set of representative trajectories through a differentiable Transformer-based network, whose attention mechanism helps to model the relations of trajectories. In experiments, our method achieves state-of-the-art performance on the Stanford Drone Dataset and Intersection Drone Dataset.

</details>
