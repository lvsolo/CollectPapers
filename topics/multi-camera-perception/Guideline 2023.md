# Multi-camera Perception — 2023 Guideline

> 领域: 多相机 / 多视角感知（环视、深度估计与 3D 预测）
> 论文数: 3 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Adversarial Training of Self-supervised Monocular Depth Estimation against Physical-World Attacks.
- **链接**: [arXiv:2301.13487](https://arxiv.org/abs/2301.13487) · 📚 被引 17
- **作者**: Zhiyuan Cheng, James Liang, Guanhong Tao, Dongfang Liu, Xiangyu Zhang
- **🏷️ 机构**: Purdue University, West Lafayette, IN, USA, Rochester Institute of Technology, Rochester, NY, USA, Meta AI, Menlo Park, CA, USA
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular Depth Estimation (MDE) is a critical component in applications such as autonomous driving. There are various attacks against MDE networks. These attacks, especially the physical ones, pose a great threat to the security of such systems. Traditional adversarial training method requires ground-truth labels hence cannot be directly applied to self-supervised MDE that does not have ground-truth depth. Some self-supervised model hardening techniques (e.g., contrastive learning) ignore the domain knowledge of MDE and can hardly achieve optimal performance. In this work, we propose a novel adversarial training method for self-supervised MDE models based on view synthesis without using ground-truth depth. We improve adversarial robustness against physical-world attacks using L0-norm-bounded perturbation in training. We compare our method with supervised learning based and contrastive learning based methods that are tailored for MDE. Results on two representative MDE networks show that we achieve better robustness against various adversarial attacks with nearly no benign performance degradation.

</details>

## 跨领域论文（完整笔记在其他领域）

- BEVDistill: Cross-Modal BEV Distillation for Multi-View 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Time Will Tell: New Outlooks and A Baseline for Temporal Multi-View 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
