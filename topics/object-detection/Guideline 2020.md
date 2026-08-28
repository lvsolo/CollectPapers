# Object Detection — 2020 Guideline

> 领域: 通用 2D 目标检测（检测器架构、密集预测、小物体/旋转框/NMS 等）
> 论文数: 12 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Detection as Regression: Certified Object Detection with Median Smoothing.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/0dd1bc593a91620daecf7723d2235624-Abstract.html)
- **作者**: Ping-yeh Chiang, Michael J. Curry, Ahmed Abdelkader, Aounon Kumar, John Dickerson, Tom Goldstein
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### Generalized Focal Loss: Learning Qualified and Distributed Bounding Boxes for Dense Object Detection.
- **链接**: [arXiv:2006.04388](https://arxiv.org/abs/2006.04388) · [代码](https://github.com/implus/GFocal)
- **作者**: Xiang Li, Wenhai Wang, Lijun Wu, Shuo Chen, Xiaolin Hu, Jun Li et al.
- **🏷️ 机构**: Shanghai AI Lab
- **会议**: NeurIPS 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> One-stage detector basically formulates object detection as dense classification and localization. The classification is usually optimized by Focal Loss and the box location is commonly learned under Dirac delta distribution. A recent trend for one-stage detectors is to introduce an individual prediction branch to estimate the quality of localization, where the predicted quality facilitates the classification to improve detection performance. This paper delves into the representations of the above three fundamental elements: quality estimation, classification and localization. Two problems are discovered in existing practices, including (1) the inconsistent usage of the quality estimation and classification between training and inference and (2) the inflexible Dirac delta distribution for localization when there is ambiguity and uncertainty in complex scenes. To address the problems, we design new representations for these elements. Specifically, we merge the quality estimation into the class prediction vector to form a joint representation of localization quality and classification, and use a vector to represent arbitrary distribution of box locations. The improved representations eliminate the inconsistency risk and accurately depict the flexible distribution in real data, but contain continuous labels, which is beyond the scope of Focal Loss. We then propose Generalized Focal Loss (GFL) that generalizes Focal Loss from its discrete form to the continuous version for successful optimization. On COCO test-dev, GFL achieves 45.0\% AP using ResNet-101 backbone, surpassing state-of-the-art SAPD (43.5\%) and ATSS (43.6\%) with higher or comparable inference speed, under the same backbone and training settings. Notably, our best model can achieve a single-model single-scale AP of 48.2\%, at 10 FPS on a single 2080Ti GPU. Code and models are available at https://github.com/implus/GFocal.

</details>

### RepPoints v2: Verification Meets Regression for Object Detection.
- **链接**: [arXiv:2007.08508](https://arxiv.org/abs/2007.08508) · [代码](https://github.com/Scalsol/RepPointsV2)
- **作者**: Yihong Chen, Zheng Zhang, Yue Cao, Liwei Wang, Stephen Lin, Han Hu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Verification and regression are two general methodologies for prediction in neural networks. Each has its own strengths: verification can be easier to infer accurately, and regression is more efficient and applicable to continuous target variables. Hence, it is often beneficial to carefully combine them to take advantage of their benefits. In this paper, we take this philosophy to improve state-of-the-art object detection, specifically by RepPoints. Though RepPoints provides high performance, we find that its heavy reliance on regression for object localization leaves room for improvement. We introduce verification tasks into the localization prediction of RepPoints, producing RepPoints v2, which provides consistent improvements of about 2.0 mAP over the original RepPoints on the COCO object detection benchmark using different backbones and training methods. RepPoints v2 also achieves 52.1 mAP on COCO \texttt{test-dev} by a single model. Moreover, we show that the proposed approach can more generally elevate other object detection frameworks as well as applications such as instance segmentation. The code is available at https://github.com/Scalsol/RepPointsV2.

</details>

### RelationNet++: Bridging Visual Representations for Object Detection via Transformer Decoder.
- **链接**: [arXiv:2010.15831](https://arxiv.org/abs/2010.15831) · [代码](https://github.com/microsoft/RelationNet2)
- **作者**: Cheng Chi, Fangyun Wei, Han Hu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing object detection frameworks are usually built on a single format of object/part representation, i.e., anchor/proposal rectangle boxes in RetinaNet and Faster R-CNN, center points in FCOS and RepPoints, and corner points in CornerNet. While these different representations usually drive the frameworks to perform well in different aspects, e.g., better classification or finer localization, it is in general difficult to combine these representations in a single framework to make good use of each strength, due to the heterogeneous or non-grid feature extraction by different representations. This paper presents an attention-based decoder module similar as that in Transformer~\cite{vaswani2017attention} to bridge other representations into a typical object detector built on a single representation format, in an end-to-end fashion. The other representations act as a set of \emph{key} instances to strengthen the main \emph{query} representation features in the vanilla detectors. Novel techniques are proposed towards efficient computation of the decoder module, including a \emph{key sampling} approach and a \emph{shared location embedding} approach. The proposed module is named \emph{bridging visual representations} (BVR). It can perform in-place and we demonstrate its broad effectiveness in bridging other representations into prevalent object detection frameworks, including RetinaNet, Faster R-CNN, FCOS and ATSS, where about $1.5\sim3.0$ AP improvements are achieved. In particular, we improve a state-of-the-art framework with a strong backbone by about $2.0$ AP, reaching $52.7$ AP on COCO test-dev. The resulting network is named RelationNet++. The code will be available at https://github.com/microsoft/RelationNet2.

</details>

### Comprehensive Attention Self-Distillation for Weakly-Supervised Object Detection.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/c3535febaff29fcb7c0d20cbe94391c7-Abstract.html)
- **作者**: Zeyi Huang, Yang Zou, B. V. K. Vijaya Kumar, Dong Huang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### A Ranking-based, Balanced Loss Function Unifying Classification and Localisation in Object Detection.
- **链接**: [arXiv:2009.13592](https://arxiv.org/abs/2009.13592) · [代码](https://github.com/kemaloksuz/aLRPLoss)
- **作者**: Kemal Oksuz, Baris Can Cam, Emre Akbas, Sinan Kalkan
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose average Localisation-Recall-Precision (aLRP), a unified, bounded, balanced and ranking-based loss function for both classification and localisation tasks in object detection. aLRP extends the Localisation-Recall-Precision (LRP) performance metric (Oksuz et al., 2018) inspired from how Average Precision (AP) Loss extends precision to a ranking-based loss function for classification (Chen et al., 2020). aLRP has the following distinct advantages: (i) aLRP is the first ranking-based loss function for both classification and localisation tasks. (ii) Thanks to using ranking for both tasks, aLRP naturally enforces high-quality localisation for high-precision classification. (iii) aLRP provides provable balance between positives and negatives. (iv) Compared to on average $\sim$6 hyperparameters in the loss functions of state-of-the-art detectors, aLRP Loss has only one hyperparameter, which we did not tune in practice. On the COCO dataset, aLRP Loss improves its ranking-based predecessor, AP Loss, up to around $5$ AP points, achieves $48.9$ AP without test time augmentation and outperforms all one-stage detectors. Code available at: https://github.com/kemaloksuz/aLRPLoss .

</details>

### UWSOD: Toward Fully-Supervised-Level Capacity Weakly Supervised Object Detection.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/4e0928de075538c593fbdabb0c5ef2c3-Abstract.html)
- **作者**: Yunhang Shen, Rongrong Ji, Zhiwei Chen, Yongjian Wu, Feiyue Huang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### Fine-Grained Dynamic Head for Object Detection.
- **链接**: [arXiv:2012.03519](https://arxiv.org/abs/2012.03519) · [代码](https://github.com/StevenGrove/DynamicHead)
- **作者**: Lin Song, Yanwei Li, Zhengkai Jiang, Zeming Li, Hongbin Sun, Jian Sun et al.
- **🏷️ 机构**: MEGVII, XJTU
- **会议**: NeurIPS 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The Feature Pyramid Network (FPN) presents a remarkable approach to alleviate the scale variance in object representation by performing instance-level assignments. Nevertheless, this strategy ignores the distinct characteristics of different sub-regions in an instance. To this end, we propose a fine-grained dynamic head to conditionally select a pixel-level combination of FPN features from different scales for each instance, which further releases the ability of multi-scale feature representation. Moreover, we design a spatial gate with the new activation function to reduce computational complexity dramatically through spatially sparse convolutions. Extensive experiments demonstrate the effectiveness and efficiency of the proposed method on several state-of-the-art detection benchmarks. Code is available at https://github.com/StevenGrove/DynamicHead.

</details>

### Restoring Negative Information in Few-Shot Object Detection.
- **链接**: [arXiv:2010.11714](https://arxiv.org/abs/2010.11714) · [代码](https://github.com/yang-yk/NP-RepMet)
- **作者**: Yukuan Yang, Fangyun Wei, Miaojing Shi, Guoqi Li
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Few-shot learning has recently emerged as a new challenge in the deep learning field: unlike conventional methods that train the deep neural networks (DNNs) with a large number of labeled data, it asks for the generalization of DNNs on new classes with few annotated samples. Recent advances in few-shot learning mainly focus on image classification while in this paper we focus on object detection. The initial explorations in few-shot object detection tend to simulate a classification scenario by using the positive proposals in images with respect to certain object class while discarding the negative proposals of that class. Negatives, especially hard negatives, however, are essential to the embedding space learning in few-shot object detection. In this paper, we restore the negative information in few-shot object detection by introducing a new negative- and positive-representative based metric learning framework and a new inference scheme with negative and positive representatives. We build our work on a recent few-shot pipeline RepMet with several new modules to encode negative information for both training and testing. Extensive experiments on ImageNet-LOC and PASCAL VOC show our method substantially improves the state-of-the-art few-shot object detection solutions. Our code is available at https://github.com/yang-yk/NP-RepMet.

</details>

### CoADNet: Collaborative Aggregation-and-Distribution Networks for Co-Salient Object Detection.
- **链接**: [arXiv:2011.04887](https://arxiv.org/abs/2011.04887)
- **作者**: Qijian Zhang, Runmin Cong, Junhui Hou, Chongyi Li, Yao Zhao
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Co-Salient Object Detection (CoSOD) aims at discovering salient objects that repeatedly appear in a given query group containing two or more relevant images. One challenging issue is how to effectively capture co-saliency cues by modeling and exploiting inter-image relationships. In this paper, we present an end-to-end collaborative aggregation-and-distribution network (CoADNet) to capture both salient and repetitive visual patterns from multiple images. First, we integrate saliency priors into the backbone features to suppress the redundant background information through an online intra-saliency guidance structure. After that, we design a two-stage aggregate-and-distribute architecture to explore group-wise semantic interactions and produce the co-saliency features. In the first stage, we propose a group-attentional semantic aggregation module that models inter-image relationships to generate the group-wise semantic representations. In the second stage, we propose a gated group distribution module that adaptively distributes the learned group semantics to different individuals in a dynamic gating mechanism. Finally, we develop a group consistency preserving decoder tailored for the CoSOD task, which maintains group constraints during feature decoding to predict more consistent full-resolution co-saliency maps. The proposed CoADNet is evaluated on four prevailing CoSOD benchmark datasets, which demonstrates the remarkable performance improvement over ten state-of-the-art competitors.

</details>

### Few-Cost Salient Object Detection with Adversarial-Paced Learning.
- **链接**: [arXiv:2104.01928](https://arxiv.org/abs/2104.01928) · [代码](https://github.com/hb-stone/FC-SOD)
- **作者**: Dingwen Zhang, Haibin Tian, Jungong Han
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Detecting and segmenting salient objects from given image scenes has received great attention in recent years. A fundamental challenge in training the existing deep saliency detection models is the requirement of large amounts of annotated data. While gathering large quantities of training data becomes cheap and easy, annotating the data is an expensive process in terms of time, labor and human expertise. To address this problem, this paper proposes to learn the effective salient object detection model based on the manual annotation on a few training images only, thus dramatically alleviating human labor in training models. To this end, we name this task as the few-cost salient object detection and propose an adversarial-paced learning (APL)-based framework to facilitate the few-cost learning scenario. Essentially, APL is derived from the self-paced learning (SPL) regime but it infers the robust learning pace through the data-driven adversarial learning mechanism rather than the heuristic design of the learning regularizer. Comprehensive experiments on four widely-used benchmark datasets demonstrate that the proposed method can effectively approach to the existing supervised deep salient object detection models with only 1k human-annotated training images. The project page is available at https://github.com/hb-stone/FC-SOD.

</details>

## 跨领域论文（完整笔记在其他领域）

- Every View Counts: Cross-View Consistency in 3D Object Detection with Hybrid-Cylindrical-Spherical Voxelization. → [3d-detection](../3d-detection/Guideline%202020.md)
