# Self-supervised Vision — 2021 Guideline

> 领域: 视觉自监督学习（对比学习、MAE、DINO 系）
> 论文数: 7 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Self-Point-Flow: Self-Supervised Scene Flow Estimation From Point Clouds With Optimal Transport and Random Walk.
- **链接**: [arXiv:2105.08248](https://arxiv.org/abs/2105.08248) · 📚 被引 45
- **作者**: Ruibo Li, Guosheng Lin, Lihua Xie
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Due to the scarcity of annotated scene flow data, self-supervised scene flow learning in point clouds has attracted increasing attention. In the self-supervised manner, establishing correspondences between two point clouds to approximate scene flow is an effective approach. Previous methods often obtain correspondences by applying point-wise matching that only takes the distance on 3D point coordinates into account, introducing two critical issues: (1) it overlooks other discriminative measures, such as color and surface normal, which often bring fruitful clues for accurate matching; and (2) it often generates sub-par performance, as the matching is operated in an unconstrained situation, where multiple points can be ended up with the same corresponding point. To address the issues, we formulate this matching task as an optimal transport problem. The output optimal assignment matrix can be utilized to guide the generation of pseudo ground truth. In this optimal transport, we design the transport cost by considering multiple descriptors and encourage one-to-one matching by mass equality constraints. Also, constructing a graph on the points, a random walk module is introduced to encourage the local consistency of the pseudo labels. Comprehensive experiments on FlyingThings3D and KITTI show that our method achieves state-of-the-art performance among self-supervised learning methods. Our self-supervised method even performs on par with some supervised learning approaches, although we do not need any ground truth flow for training.

</details>

### Self-Supervised Learning on 3D Point Clouds by Learning Discrete Generative Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Eckart_Self-Supervised_Learning_on_3D_Point_Clouds_by_Learning_Discrete_Generative_CVPR_2021_paper.html) · 📚 被引 54
- **作者**: Benjamin Eckart, Wentao Yuan, Chao Liu, Jan Kautz
- **🏷️ 机构**: NVIDIA, University of Washington
- **会议**: CVPR 2021

### The Temporal Opportunist: Self-Supervised Multi-Frame Monocular Depth.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Watson_The_Temporal_Opportunist_Self-Supervised_Multi-Frame_Monocular_Depth_CVPR_2021_paper.html) · 📚 被引 316
- **作者**: Jamie Watson, Oisin Mac Aodha, Victor Prisacariu, Gabriel J. Brostow, Michael Firman
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### STaR: Self-Supervised Tracking and Reconstruction of Rigid Objects in Motion With Neural Rendering.
- **链接**: [arXiv:2101.01602](https://arxiv.org/abs/2101.01602) · 📚 被引 61
- **作者**: Wentao Yuan, Zhaoyang Lv, Tanner Schmidt, Steven Lovegrove
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present STaR, a novel method that performs Self-supervised Tracking and Reconstruction of dynamic scenes with rigid motion from multi-view RGB videos without any manual annotation. Recent work has shown that neural networks are surprisingly effective at the task of compressing many views of a scene into a learned function which maps from a viewing ray to an observed radiance value via volume rendering. Unfortunately, these methods lose all their predictive power once any object in the scene has moved. In this work, we explicitly model rigid motion of objects in the context of neural representations of radiance fields. We show that without any additional human specified supervision, we can reconstruct a dynamic scene with a single rigid object in motion by simultaneously decomposing it into its two constituent parts and encoding each with its own neural representation. We achieve this by jointly optimizing the parameters of two neural radiance fields and a set of rigid poses which align the two fields at each frame. On both synthetic and real world datasets, we demonstrate that our method can render photorealistic novel views, where novelty is measured on both spatial and temporal axes. Our factored representation furthermore enables animation of unseen object motion.

</details>

## 跨领域论文（完整笔记在其他领域）

- There Is More Than Meets the Eye: Self-Supervised Multi-Object Detection and Tracking With Sound by Distilling Multimodal Knowledge. → [multimodal](../multimodal/Guideline%202021.md)
- Self-Supervised Learning of Depth Inference for Multi-View Stereo. → [multi-camera-perception](../multi-camera-perception/Guideline%202021.md)
- Self-Supervised Pillar Motion Learning for Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202021.md)
