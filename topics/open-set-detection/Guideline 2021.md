# Open-set Detection — 2021 Guideline

> 领域: 开放类检测总类（开放词表 OVD / 开放世界 OWOD / 开集 OOD / 未知类检测）
> 论文数: 2 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Open-Vocabulary Object Detection Using Captions.
- **链接**: [arXiv:2011.10678](https://arxiv.org/abs/2011.10678) · 📚 被引 402
- **作者**: Alireza Zareian, Kevin Dela Rosa, Derek Hao Hu, Shih-Fu Chang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

- **摘要（英，原文）**:

  > Despite the remarkable accuracy of deep neural networks in object detection, they are costly to train and scale due to supervision requirements. Particularly, learning more object categories typically requires proportionally more bounding box annotations. Weakly supervised and zero-shot learning techniques have been explored to scale object detectors to more categories with less supervision, but they have not been as successful and widely adopted as supervised models. In this paper, we put forth a novel formulation of the object detection problem, namely open-vocabulary object detection, which is more general, more practical, and more effective than weakly supervised and zero-shot approaches. We propose a new method to train object detectors using bounding box annotations for a limited set of object categories, as well as image-caption pairs that cover a larger variety of objects at a significantly lower cost. We show that the proposed method can detect and localize objects for which no bounding box annotation is provided during training, at a significantly higher accuracy than zero-shot approaches. Meanwhile, objects with bounding box annotation can be detected almost as accurately as supervised methods, which is significantly better than weakly supervised baselines. Accordingly, we establish a new state of the art for scalable object detection.

### Neighborhood Contrastive Learning for Novel Class Discovery.
- **链接**: [arXiv:2106.10731](https://arxiv.org/abs/2106.10731)
- **作者**: Zhun Zhong, Enrico Fini, Subhankar Roy, Zhiming Luo, Elisa Ricci, Nicu Sebe
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

- **摘要（英，原文）**:

  > In this paper, we address Novel Class Discovery (NCD), the task of unveiling new classes in a set of unlabeled samples given a labeled dataset with known classes. We exploit the peculiarities of NCD to build a new framework, named Neighborhood Contrastive Learning (NCL), to learn discriminative representations that are important to clustering performance. Our contribution is twofold. First, we find that a feature extractor trained on the labeled set generates representations in which a generic query sample and its neighbors are likely to share the same class. We exploit this observation to retrieve and aggregate pseudo-positive pairs with contrastive learning, thus encouraging the model to learn more discriminative representations. Second, we notice that most of the instances are easily discriminated by the network, contributing less to the contrastive loss. To overcome this issue, we propose to generate hard negatives by mixing labeled and unlabeled samples in the feature space. We experimentally demonstrate that these two ingredients significantly contribute to clustering performance and lead our model to outperform state-of-the-art methods by a large margin (e.g., clustering accuracy +13% on CIFAR-100 and +8% on ImageNet).
