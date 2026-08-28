# Object Detection — 2021 Guideline

> 领域: 通用 2D 目标检测（检测器架构、密集预测、小物体/旋转框/NMS 等）
> 论文数: 5 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Deformable DETR: Deformable Transformers for End-to-End Object Detection.
- **链接**: [arXiv:2010.04159](https://arxiv.org/abs/2010.04159) · [代码](https://github.com/fundamentalvision/Deformable-DETR)
- **作者**: Xizhou Zhu, Weijie Su, Lewei Lu, Bin Li, Xiaogang Wang, Jifeng Dai
- **🏷️ 机构**: Tsinghua / Shanghai AI Lab, CUHK / Shanghai AI Lab
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> DETR has been recently proposed to eliminate the need for many hand-designed components in object detection while demonstrating good performance. However, it suffers from slow convergence and limited feature spatial resolution, due to the limitation of Transformer attention modules in processing image feature maps. To mitigate these issues, we proposed Deformable DETR, whose attention modules only attend to a small set of key sampling points around a reference. Deformable DETR can achieve better performance than DETR (especially on small objects) with 10 times less training epochs. Extensive experiments on the COCO benchmark demonstrate the effectiveness of our approach. Code is released at https://github.com/fundamentalvision/Deformable-DETR.

</details>

### Unbiased Teacher for Semi-Supervised Object Detection.
- **链接**: [arXiv:2102.09480](https://arxiv.org/abs/2102.09480)
- **作者**: Yen-Cheng Liu, Chih-Yao Ma, Zijian He, Chia-Wen Kuo, Kan Chen, Peizhao Zhang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Semi-supervised learning, i.e., training networks with both labeled and unlabeled data, has made significant progress recently. However, existing works have primarily focused on image classification tasks and neglected object detection which requires more annotation effort. In this work, we revisit the Semi-Supervised Object Detection (SS-OD) and identify the pseudo-labeling bias issue in SS-OD. To address this, we introduce Unbiased Teacher, a simple yet effective approach that jointly trains a student and a gradually progressing teacher in a mutually-beneficial manner. Together with a class-balance loss to downweight overly confident pseudo-labels, Unbiased Teacher consistently improved state-of-the-art methods by significant margins on COCO-standard, COCO-additional, and VOC datasets. Specifically, Unbiased Teacher achieves 6.8 absolute mAP improvements against state-of-the-art method when using 1% of labeled data on MS-COCO, achieves around 10 mAP improvements against the supervised baseline when using only 0.5, 1, 2% of labeled data on MS-COCO.

</details>

### Loss Function Discovery for Object Detection via Convergence-Simulation Driven Search.
- **链接**: [arXiv:2102.04700](https://arxiv.org/abs/2102.04700) · [代码](https://github.com/PerdonLiu/CSE-Autoloss)
- **作者**: Peidong Liu, Gengwei Zhang, Bochao Wang, Hang Xu, Xiaodan Liang, Yong Jiang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Designing proper loss functions for vision tasks has been a long-standing research direction to advance the capability of existing models. For object detection, the well-established classification and regression loss functions have been carefully designed by considering diverse learning challenges. Inspired by the recent progress in network architecture search, it is interesting to explore the possibility of discovering new loss function formulations via directly searching the primitive operation combinations. So that the learned losses not only fit for diverse object detection challenges to alleviate huge human efforts, but also have better alignment with evaluation metric and good mathematical convergence property. Beyond the previous auto-loss works on face recognition and image classification, our work makes the first attempt to discover new loss functions for the challenging object detection from primitive operation levels. We propose an effective convergence-simulation driven evolutionary search algorithm, called CSE-Autoloss, for speeding up the search progress by regularizing the mathematical rationality of loss candidates via convergence property verification and model optimization simulation. CSE-Autoloss involves the search space that cover a wide range of the possible variants of existing losses and discovers best-searched loss function combination within a short time (around 1.5 wall-clock days). We conduct extensive evaluations of loss function search on popular detectors and validate the good generalization capability of searched losses across diverse architectures and datasets. Our experiments show that the best-discovered loss function combinations outperform default combinations by 1.1% and 0.8% in terms of mAP for two-stage and one-stage detectors on COCO respectively. Our searched losses are available at https://github.com/PerdonLiu/CSE-Autoloss.

</details>

### PolarNet: Learning to Optimize Polar Keypoints for Keypoint Based Object Detection.
- **链接**: [出版页](https://openreview.net/forum?id=TYXs_y84xRj)
- **作者**: Xiongwei Wu, Doyen Sahoo, Steven C. H. Hoi
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

### Improve Object Detection with Feature-based Knowledge Distillation: Towards Accurate and Efficient Detectors.
- **链接**: [出版页](https://openreview.net/forum?id=uKhGRvM8QNH)
- **作者**: Linfeng Zhang, Kaisheng Ma
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021
