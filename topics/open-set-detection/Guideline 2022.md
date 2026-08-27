# Open-set Detection — 2022 Guideline

> 领域: 开放类检测总类（开放词表 OVD / 开放世界 OWOD / 开集 OOD / 未知类检测）
> 论文数: 7 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### DenseHybrid: Hybrid Anomaly Detection for Dense Open-Set Recognition.
- **链接**: [arXiv:2207.02606](https://arxiv.org/abs/2207.02606) · 📚 被引 60
- **作者**: Matej Grcic, Petra Bevandic, Sinisa Segvic
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

- **摘要（英，原文）**:

  > Anomaly detection can be conceived either through generative modelling of regular training data or by discriminating with respect to negative training data. These two approaches exhibit different failure modes. Consequently, hybrid algorithms present an attractive research goal. Unfortunately, dense anomaly detection requires translational equivariance and very large input resolutions. These requirements disqualify all previous hybrid approaches to the best of our knowledge. We therefore design a novel hybrid algorithm based on reinterpreting discriminative logits as a logarithm of the unnormalized joint distribution $\hat{p}(\mathbf{x}, \mathbf{y})$. Our model builds on a shared convolutional representation from which we recover three dense predictions: i) the closed-set class posterior $P(\mathbf{y}|\mathbf{x})$, ii) the dataset posterior $P(d_{in}|\mathbf{x})$, iii) unnormalized data likelihood $\hat{p}(\mathbf{x})$. The latter two predictions are trained both on the standard training data and on a generic negative dataset. We blend these two predictions into a hybrid anomaly score which allows dense open-set recognition on large natural images. We carefully design a custom loss for the data likelihood in order to avoid backpropagation through the untractable normalizing constant $Z(θ)$. Experiments evaluate our contributions on standard dense anomaly detection benchmarks as well as in terms of open-mIoU - a novel metric for dense open-set performance. Our submissions achieve state-of-the-art performance despite neglectable computational overhead over the standard semantic segmentation baseline.

### OpenLDN: Learning to Discover Novel Classes for Open-World Semi-Supervised Learning.
- **链接**: [arXiv:2207.02261](https://arxiv.org/abs/2207.02261) · 📚 被引 36
- **作者**: Mamshad Nayeem Rizve, Navid Kardan, Salman Khan, Fahad Shahbaz Khan, Mubarak Shah
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

- **摘要（英，原文）**:

  > Semi-supervised learning (SSL) is one of the dominant approaches to address the annotation bottleneck of supervised learning. Recent SSL methods can effectively leverage a large repository of unlabeled data to improve performance while relying on a small set of labeled data. One common assumption in most SSL methods is that the labeled and unlabeled data are from the same data distribution. However, this is hardly the case in many real-world scenarios, which limits their applicability. In this work, instead, we attempt to solve the challenging open-world SSL problem that does not make such an assumption. In the open-world SSL problem, the objective is to recognize samples of known classes, and simultaneously detect and cluster samples belonging to novel classes present in unlabeled data. This work introduces OpenLDN that utilizes a pairwise similarity loss to discover novel classes. Using a bi-level optimization rule this pairwise similarity loss exploits the information available in the labeled set to implicitly cluster novel class samples, while simultaneously recognizing samples from known classes. After discovering novel classes, OpenLDN transforms the open-world SSL problem into a standard SSL problem to achieve additional performance gains using existing SSL methods. Our extensive experiments demonstrate that OpenLDN outperforms the current state-of-the-art methods on multiple popular classification benchmarks while providing a better accuracy/training time trade-off.

## 跨领域论文（完整笔记在其他领域）

- Open Vocabulary Object Detection with Pseudo Bounding-Box Labels. → [object-detection](../object-detection/Guideline%202022.md)
- Open-Set Semi-Supervised Object Detection. → [object-detection](../object-detection/Guideline%202022.md)
- Class-Agnostic Object Detection with Multi-modal Transformer. → [multimodal](../multimodal/Guideline%202022.md)
- Simple Open-Vocabulary Object Detection. → [object-detection](../object-detection/Guideline%202022.md)
- Few-Shot Class-Incremental Learning from an Open-Set Perspective. → [continual-learning](../continual-learning/Guideline%202022.md)
