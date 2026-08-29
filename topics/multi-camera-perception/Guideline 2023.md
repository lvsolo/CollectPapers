# Multi-camera Perception — 2023 Guideline

> 领域: 多相机 / 多视角感知（环视、深度估计与 3D 预测）
> 论文数: 4 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Provably Learning Diverse Features in Multi-View Data with Midpoint Mixup.
- **链接**: [arXiv:2210.13512](https://arxiv.org/abs/2210.13512)
- **作者**: Muthu Chidambaram, Xiang Wang, Chenwei Wu, Rong Ge
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Mixup is a data augmentation technique that relies on training using random convex combinations of data points and their labels. In recent years, Mixup has become a standard primitive used in the training of state-of-the-art image classification models due to its demonstrated benefits over empirical risk minimization with regards to generalization and robustness. In this work, we try to explain some of this success from a feature learning perspective. We focus our attention on classification problems in which each class may have multiple associated features (or views) that can be used to predict the class correctly. Our main theoretical results demonstrate that, for a non-trivial class of data distributions with two features per class, training a 2-layer convolutional network using empirical risk minimization can lead to learning only one feature for almost all classes while training with a specific instantiation of Mixup succeeds in learning both features for every class. We also show empirically that these theoretical insights extend to the practical settings of image benchmarks modified to have multiple features.

</details>

### The Role of Entropy and Reconstruction in Multi-View Self-Supervised Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v202/rodri-guez-galvez23a.html)
- **作者**: Borja Rodríguez Gálvez, Arno Blaas, Pau Rodríguez, Adam Golinski, Xavier Suau, Jason Ramapuram et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Information-Theoretic State Space Model for Multi-View Reinforcement Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v202/hwang23c.html)
- **作者**: HyeongJoo Hwang, Seokin Seo, Youngsoo Jang, Sungyoon Kim, Geon-Hyeong Kim, Seunghoon Hong et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Multi-View Masked World Models for Visual Robotic Manipulation.
- **链接**: [arXiv:2302.02408](https://arxiv.org/abs/2302.02408)
- **作者**: Younggyo Seo, Junsu Kim, Stephen James, Kimin Lee, Jinwoo Shin, Pieter Abbeel
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Visual robotic manipulation research and applications often use multiple cameras, or views, to better perceive the world. How else can we utilize the richness of multi-view data? In this paper, we investigate how to learn good representations with multi-view data and utilize them for visual robotic manipulation. Specifically, we train a multi-view masked autoencoder which reconstructs pixels of randomly masked viewpoints and then learn a world model operating on the representations from the autoencoder. We demonstrate the effectiveness of our method in a range of scenarios, including multi-view control and single-view control with auxiliary cameras for representation learning. We also show that the multi-view masked autoencoder trained with multiple randomized viewpoints enables training a policy with strong viewpoint randomization and transferring the policy to solve real-robot tasks without camera calibration and an adaptation procedure. Video demonstrations are available at: https://sites.google.com/view/mv-mwm.

</details>
