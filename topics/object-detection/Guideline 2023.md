# Object Detection — 2023 Guideline

> 领域: 通用 2D 目标检测（检测器架构、密集预测、小物体/旋转框/NMS 等）
> 论文数: 14 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### DINO: DETR with Improved DeNoising Anchor Boxes for End-to-End Object Detection.
- **链接**: [出版页](https://openreview.net/forum?id=3mRwyG5one)
- **作者**: Hao Zhang, Feng Li, Shilong Liu, Lei Zhang, Hang Su, Jun Zhu et al.
- **🏷️ 机构**: PolyU / OPPO
- **会议**: ICLR 2023

### Learning Object-Language Alignments for Open-Vocabulary Object Detection.
- **链接**: [出版页](https://openreview.net/forum?id=mjHlitXvReu)
- **作者**: Chuang Lin, Peize Sun, Yi Jiang, Ping Luo, Lizhen Qu, Gholamreza Haffari et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### The KFIoU Loss for Rotated Object Detection.
- **链接**: [arXiv:2201.12558](https://arxiv.org/abs/2201.12558)
- **作者**: Xue Yang, Yue Zhou, Gefan Zhang, Jirui Yang, Wentao Wang, Junchi Yan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Differing from the well-developed horizontal object detection area whereby the computing-friendly IoU based loss is readily adopted and well fits with the detection metrics. In contrast, rotation detectors often involve a more complicated loss based on SkewIoU which is unfriendly to gradient-based training. In this paper, we propose an effective approximate SkewIoU loss based on Gaussian modeling and Gaussian product, which mainly consists of two items. The first term is a scale-insensitive center point loss, which is used to quickly narrow the distance between the center points of the two bounding boxes. In the distance-independent second term, the product of the Gaussian distributions is adopted to inherently mimic the mechanism of SkewIoU by its definition, and show its alignment with the SkewIoU loss at trend-level within a certain distance (i.e. within 9 pixels). This is in contrast to recent Gaussian modeling based rotation detectors e.g. GWD loss and KLD loss that involve a human-specified distribution distance metric which require additional hyperparameter tuning that vary across datasets and detectors. The resulting new loss called KFIoU loss is easier to implement and works better compared with exact SkewIoU loss, thanks to its full differentiability and ability to handle the non-overlapping cases. We further extend our technique to the 3-D case which also suffers from the same issues as 2-D. Extensive results on various public datasets (2-D/3-D, aerial/text/face images) with different base detectors show the effectiveness of our approach.

</details>

### H2RBox: Horizontal Box Annotation is All You Need for Oriented Object Detection.
- **链接**: [arXiv:2210.06742](https://arxiv.org/abs/2210.06742) · [代码](https://github.com/yangxue0827/h2rbox-mmrotate)
- **作者**: Xue Yang, Gefan Zhang, Wentong Li, Yue Zhou, Xuehui Wang, Junchi Yan
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Oriented object detection emerges in many applications from aerial images to autonomous driving, while many existing detection benchmarks are annotated with horizontal bounding box only which is also less costive than fine-grained rotated box, leading to a gap between the readily available training corpus and the rising demand for oriented object detection. This paper proposes a simple yet effective oriented object detection approach called H2RBox merely using horizontal box annotation for weakly-supervised training, which closes the above gap and shows competitive performance even against those trained with rotated boxes. The cores of our method are weakly- and self-supervised learning, which predicts the angle of the object by learning the consistency of two different views. To our best knowledge, H2RBox is the first horizontal box annotation-based oriented object detector. Compared to an alternative i.e. horizontal box-supervised instance segmentation with our post adaption to oriented object detection, our approach is not susceptible to the prediction quality of mask and can perform more robustly in complex scenes containing a large number of dense objects and outliers. Experimental results show that H2RBox has significant performance and speed advantages over horizontal box-supervised instance segmentation methods, as well as lower memory requirements. While compared to rotated box-supervised oriented object detectors, our method shows very close performance and speed. The source code is available at PyTorch-based \href{https://github.com/yangxue0827/h2rbox-mmrotate}{MMRotate} and Jittor-based \href{https://github.com/yangxue0827/h2rbox-jittor}{JDet}.

</details>

### Proposal-Contrastive Pretraining for Object Detection from Fewer Data.
- **链接**: [arXiv:2310.16835](https://arxiv.org/abs/2310.16835)
- **作者**: Quentin Bouniot, Romaric Audigier, Angélique Loesch, Amaury Habrard
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The use of pretrained deep neural networks represents an attractive way to achieve strong results with few data available. When specialized in dense problems such as object detection, learning local rather than global information in images has proven to be more efficient. However, for unsupervised pretraining, the popular contrastive learning requires a large batch size and, therefore, a lot of resources. To address this problem, we are interested in transformer-based object detectors that have recently gained traction in the community with good performance and with the particularity of generating many diverse object proposals. In this work, we present Proposal Selection Contrast (ProSeCo), a novel unsupervised overall pretraining approach that leverages this property. ProSeCo uses the large number of object proposals generated by the detector for contrastive learning, which allows the use of a smaller batch size, combined with object-level features to learn local information in the images. To improve the effectiveness of the contrastive loss, we introduce the object location information in the selection of positive examples to take into account multiple overlapping object proposals. When reusing pretrained backbone, we advocate for consistency in learning local information between the backbone and the detection head. We show that our method outperforms state of the art in unsupervised pretraining for object detection on standard and novel benchmarks in learning with fewer data.

</details>

### Towards Robust Object Detection Invariant to Real-World Domain Shifts.
- **链接**: [出版页](https://openreview.net/forum?id=vqSyt8D3ny)
- **作者**: Qi Fan, Mattia Segù, Yu-Wing Tai, Fisher Yu, Chi-Keung Tang, Bernt Schiele et al.
- **🏷️ 机构**: ETH Zurich
- **会议**: ICLR 2023

### Open-Vocabulary Object Detection upon Frozen Vision and Language Models.
- **链接**: [出版页](https://openreview.net/forum?id=MIMwy4kh9lf)
- **作者**: Weicheng Kuo, Yin Cui, Xiuye Gu, A. J. Piergiovanni, Anelia Angelova
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Weakly Supervised Knowledge Transfer with Probabilistic Logical Reasoning for Object Detection.
- **链接**: [arXiv:2303.05148](https://arxiv.org/abs/2303.05148)
- **作者**: Martijn Oldenhof, Adam Arany, Yves Moreau, Edward De Brouwer
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Training object detection models usually requires instance-level annotations, such as the positions and labels of all objects present in each image. Such supervision is unfortunately not always available and, more often, only image-level information is provided, also known as weak supervision. Recent works have addressed this limitation by leveraging knowledge from a richly annotated domain. However, the scope of weak supervision supported by these approaches has been very restrictive, preventing them to use all available information. In this work, we propose ProbKT, a framework based on probabilistic logical reasoning that allows to train object detection models with arbitrary types of weak supervision. We empirically show on different datasets that using all available information is beneficial as our ProbKT leads to significant improvement on target domain and better generalization compared to existing baselines. We also showcase the ability of our approach to handle complex logic statements as supervision signal.

</details>

### Active Learning for Object Detection with Evidential Deep Learning and Hierarchical Uncertainty Aggregation.
- **链接**: [出版页](https://openreview.net/forum?id=MnEjsw-vj-X)
- **作者**: Younghyun Park, Wonjeong Choi, Soyeong Kim, Dong-Jun Han, Jaekyun Moon
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### ODAM: Gradient-based Instance-Specific Visual Explanations for Object Detection.
- **链接**: [arXiv:2304.06354](https://arxiv.org/abs/2304.06354)
- **作者**: Chenyang Zhao, Antoni B. Chan
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose the gradient-weighted Object Detector Activation Maps (ODAM), a visualized explanation technique for interpreting the predictions of object detectors. Utilizing the gradients of detector targets flowing into the intermediate feature maps, ODAM produces heat maps that show the influence of regions on the detector's decision for each predicted attribute. Compared to previous works classification activation maps (CAM), ODAM generates instance-specific explanations rather than class-specific ones. We show that ODAM is applicable to both one-stage detectors and two-stage detectors with different types of detector backbones and heads, and produces higher-quality visual explanations than the state-of-the-art both effectively and efficiently. We next propose a training scheme, Odam-Train, to improve the explanation ability on object discrimination of the detector through encouraging consistency between explanations for detections on the same object, and distinct explanations for detections on different objects. Based on the heat maps produced by ODAM with Odam-Train, we propose Odam-NMS, which considers the information of the model's explanation for each prediction to distinguish the duplicate detected objects. We present a detailed analysis of the visualized explanations of detectors and carry out extensive experiments to validate the effectiveness of the proposed ODAM.

</details>

## 跨领域论文（完整笔记在其他领域）

- BEVDistill: Cross-Modal BEV Distillation for Multi-View 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Exploring Active 3D Object Detection from a Generalization Perspective. → [3d-detection](../3d-detection/Guideline%202023.md)
- Time Will Tell: New Outlooks and A Baseline for Temporal Multi-View 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- DBQ-SSD: Dynamic Ball Query for Efficient 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
