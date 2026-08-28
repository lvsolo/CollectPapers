# Object Detection — 2022 Guideline

> 领域: 通用 2D 目标检测（检测器架构、密集预测、小物体/旋转框/NMS 等）
> 论文数: 7 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Pix2seq: A Language Modeling Framework for Object Detection.
- **链接**: [arXiv:2109.10852](https://arxiv.org/abs/2109.10852)
- **作者**: Ting Chen, Saurabh Saxena, Lala Li, David J. Fleet, Geoffrey E. Hinton
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present Pix2Seq, a simple and generic framework for object detection. Unlike existing approaches that explicitly integrate prior knowledge about the task, we cast object detection as a language modeling task conditioned on the observed pixel inputs. Object descriptions (e.g., bounding boxes and class labels) are expressed as sequences of discrete tokens, and we train a neural network to perceive the image and generate the desired sequence. Our approach is based mainly on the intuition that if a neural network knows about where and what the objects are, we just need to teach it how to read them out. Beyond the use of task-specific data augmentations, our approach makes minimal assumptions about the task, yet it achieves competitive results on the challenging COCO dataset, compared to highly specialized and well optimized detection algorithms.

</details>

### Open-vocabulary Object Detection via Vision and Language Knowledge Distillation.
- **链接**: [出版页](https://openreview.net/forum?id=lL3lnMbR4WU)
- **作者**: Xiuye Gu, Tsung-Yi Lin, Weicheng Kuo, Yin Cui
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

### Decoupled Adaptation for Cross-Domain Object Detection.
- **链接**: [arXiv:2110.02578](https://arxiv.org/abs/2110.02578)
- **作者**: Junguang Jiang, Baixu Chen, Jianmin Wang, Mingsheng Long
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Cross-domain object detection is more challenging than object classification since multiple objects exist in an image and the location of each object is unknown in the unlabeled target domain. As a result, when we adapt features of different objects to enhance the transferability of the detector, the features of the foreground and the background are easy to be confused, which may hurt the discriminability of the detector. Besides, previous methods focused on category adaptation but ignored another important part for object detection, i.e., the adaptation on bounding box regression. To this end, we propose D-adapt, namely Decoupled Adaptation, to decouple the adversarial adaptation and the training of the detector. Besides, we fill the blank of regression domain adaptation in object detection by introducing a bounding box adaptor. Experiments show that D-adapt achieves state-of-the-art results on four cross-domain object detection tasks and yields 17% and 21% relative improvement on benchmark datasets Clipart1k and Comic2k in particular.

</details>

### GiraffeDet: A Heavy-Neck Paradigm for Object Detection.
- **链接**: [arXiv:2202.04256](https://arxiv.org/abs/2202.04256) · [代码](https://github.com/jyqi/GiraffeDet)
- **作者**: Yiqi Jiang, Zhiyu Tan, Junyan Wang, Xiuyu Sun, Ming Lin, Hao Li
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In conventional object detection frameworks, a backbone body inherited from image recognition models extracts deep latent features and then a neck module fuses these latent features to capture information at different scales. As the resolution in object detection is much larger than in image recognition, the computational cost of the backbone often dominates the total inference cost. This heavy-backbone design paradigm is mostly due to the historical legacy when transferring image recognition models to object detection rather than an end-to-end optimized design for object detection. In this work, we show that such paradigm indeed leads to sub-optimal object detection models. To this end, we propose a novel heavy-neck paradigm, GiraffeDet, a giraffe-like network for efficient object detection. The GiraffeDet uses an extremely lightweight backbone and a very deep and large neck module which encourages dense information exchange among different spatial scales as well as different levels of latent semantics simultaneously. This design paradigm allows detectors to process the high-level semantic information and low-level spatial information at the same priority even in the early stage of the network, making it more effective in detection tasks. Numerical evaluations on multiple popular object detection benchmarks show that GiraffeDet consistently outperforms previous SOTA models across a wide spectrum of resource constraints. The source code is available at https://github.com/jyqi/GiraffeDet.

</details>

## 跨领域论文（完整笔记在其他领域）

- Sparse DETR: Efficient End-to-End Object Detection with Learnable Sparsity. → [network-pruning](../network-pruning/Guideline%202022.md)
- MonoDistill: Learning Spatial Features for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- WeakM3D: Towards Weakly Supervised Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
