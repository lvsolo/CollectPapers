# Object Detection — 2021 Guideline

> 领域: 通用 2D 目标检测（检测器架构、密集预测、小物体/旋转框/NMS 等）
> 论文数: 60 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Dynamic DETR: End-to-End Object Detection with Dynamic Attention.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00298) · 📚 被引 407
- **作者**: Xiyang Dai, Yinpeng Chen, Jianwei Yang, Pengchuan Zhang, Lu Yuan, Lei Zhang
- **🏷️ 机构**: Microsoft
- **会议**: ICCV 2021

### MosaicOS: A Simple and Effective Use of Object-Centric Images for Long-Tailed Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00047) · 📚 被引 37
- **作者**: Cheng Zhang, Tai-Yu Pan, Yandong Li, Hexiang Hu, Dong Xuan, Soravit Changpinyo et al.
- **🏷️ 机构**: The Ohio State University, Google Research, University of Southern California
- **会议**: ICCV 2021

### Uncertainty-Guided Transformer Reasoning for Camouflaged Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00411) · 📚 被引 310
- **作者**: Fan Yang, Qiang Zhai, Xin Li, Rui Huang, Ao Luo, Hong Cheng et al.
- **🏷️ 机构**: AIQ, Uestc, Megvii
- **会议**: ICCV 2021

### Robust Object Detection via Instance-Level Temporal Cycle Confusion.
- **链接**: [arXiv:2104.08381](https://arxiv.org/abs/2104.08381) · [代码](https://github.com/xinw1012/cycle-confusion) · 📚 被引 25
- **作者**: Xin Wang, Thomas E. Huang, Benlin Liu, Fisher Yu, Xiaolong Wang, Joseph E. Gonzalez et al.
- **🏷️ 机构**: Microsoft Research, ETH Z&#x00FC;rich, University of Washington
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Building reliable object detectors that are robust to domain shifts, such as various changes in context, viewpoint, and object appearances, is critical for real-world applications. In this work, we study the effectiveness of auxiliary self-supervised tasks to improve the out-of-distribution generalization of object detectors. Inspired by the principle of maximum entropy, we introduce a novel self-supervised task, instance-level temporal cycle confusion (CycConf), which operates on the region features of the object detectors. For each object, the task is to find the most different object proposals in the adjacent frame in a video and then cycle back to itself for self-supervision. CycConf encourages the object detector to explore invariant structures across instances under various motions, which leads to improved model robustness in unseen domains at test time. We observe consistent out-of-domain performance improvements when training object detectors in tandem with self-supervised tasks on large-scale video datasets (BDD100K and Waymo open data). The joint training framework also establishes a new state-of-the-art on standard unsupervised domain adaptative detection benchmarks (Cityscapes, Foggy Cityscapes, and Sim10K). The code and models are available at https://github.com/xinw1012/cycle-confusion.

</details>

### CaT: Weakly Supervised Object Detection with Category Transfer.
- **链接**: [arXiv:2108.07487](https://arxiv.org/abs/2108.07487) · [代码](https://github.com/MediaBrain-SJTU/CaT) · 📚 被引 24
- **作者**: Tianyue Cao, Lianyu Du, Xiaoyun Zhang, Siheng Chen, Ya Zhang, Yanfeng Wang
- **🏷️ 机构**: Shanghai Jiao Tong University,Cooperative Medianet Innovation Center
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> A large gap exists between fully-supervised object detection and weakly-supervised object detection. To narrow this gap, some methods consider knowledge transfer from additional fully-supervised dataset. But these methods do not fully exploit discriminative category information in the fully-supervised dataset, thus causing low mAP. To solve this issue, we propose a novel category transfer framework for weakly supervised object detection. The intuition is to fully leverage both visually-discriminative and semantically-correlated category information in the fully-supervised dataset to enhance the object-classification ability of a weakly-supervised detector. To handle overlapping category transfer, we propose a double-supervision mean teacher to gather common category information and bridge the domain gap between two datasets. To handle non-overlapping category transfer, we propose a semantic graph convolutional network to promote the aggregation of semantic features between correlated categories. Experiments are conducted with Pascal VOC 2007 as the target weakly-supervised dataset and COCO as the source fully-supervised dataset. Our category transfer framework achieves 63.5% mAP and 80.3% CorLoc with 5 overlapping categories between two datasets, which outperforms the state-of-the-art methods. Codes are avaliable at https://github.com/MediaBrain-SJTU/CaT.

</details>

### Dual Bipartite Graph Learning: A General Approach for Domain Adaptive Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00270) · 📚 被引 59
- **作者**: Chaoqi Chen, Jiongcheng Li, Zebiao Zheng, Yue Huang, Xinghao Ding, Yizhou Yu
- **🏷️ 机构**: The University of Hong Kong, Xiamen University
- **会议**: ICCV 2021

### Robust Small Object Detection on the Water Surface through Fusion of Camera and Millimeter Wave Radar.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01498) · 📚 被引 93
- **作者**: Yuwei Cheng, Hu Xu, Yimin Liu
- **🏷️ 机构**: Tsinghua University, ORCA-Uboat
- **会议**: ICCV 2021

### Active Learning for Deep Object Detection via Probabilistic Modeling.
- **链接**: [arXiv:2103.16130](https://arxiv.org/abs/2103.16130) · 📚 被引 110
- **作者**: Jiwoong Choi, Ismail Elezi, Hyuk-Jae Lee, Clément Farabet, José M. Álvarez
- **🏷️ 机构**: Seoul National University, Technical University of Munich, NVIDIA
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Active learning aims to reduce labeling costs by selecting only the most informative samples on a dataset. Few existing works have addressed active learning for object detection. Most of these methods are based on multiple models or are straightforward extensions of classification methods, hence estimate an image's informativeness using only the classification head. In this paper, we propose a novel deep active learning approach for object detection. Our approach relies on mixture density networks that estimate a probabilistic distribution for each localization and classification head's output. We explicitly estimate the aleatoric and epistemic uncertainty in a single forward pass of a single model. Our method uses a scoring function that aggregates these two types of uncertainties for both heads to obtain every image's informativeness score. We demonstrate the efficacy of our approach in PASCAL VOC and MS-COCO datasets. Our approach outperforms single-model based methods and performs on par with multi-model based methods at a fraction of the computing cost.

</details>

### Multitask AET with Orthogonal Tangent Regularity for Dark Object Detection.
- **链接**: [arXiv:2205.03346](https://arxiv.org/abs/2205.03346) · [代码](https://github.com/cuiziteng/MAET) · 📚 被引 170
- **作者**: Ziteng Cui, Guo-Jun Qi, Lin Gu, Shaodi You, Zenghui Zhang, Tatsuya Harada
- **🏷️ 机构**: Shanghai Jiao Tong University, Innopeak Technology,Seattle Research Center, RIKEN AIP
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Dark environment becomes a challenge for computer vision algorithms owing to insufficient photons and undesirable noise. To enhance object detection in a dark environment, we propose a novel multitask auto encoding transformation (MAET) model which is able to explore the intrinsic pattern behind illumination translation. In a self-supervision manner, the MAET learns the intrinsic visual structure by encoding and decoding the realistic illumination-degrading transformation considering the physical noise model and image signal processing (ISP). Based on this representation, we achieve the object detection task by decoding the bounding box coordinates and classes. To avoid the over-entanglement of two tasks, our MAET disentangles the object and degrading features by imposing an orthogonal tangent regularity. This forms a parametric manifold along which multitask predictions can be geometrically formulated by maximizing the orthogonality between the tangents along the outputs of respective tasks. Our framework can be implemented based on the mainstream object detection architecture and directly trained end-to-end using normal target detection datasets, such as VOC and COCO. We have achieved the state-of-the-art performance using synthetic and real-world datasets. Code is available at https://github.com/cuiziteng/MAET.

</details>

### TF-Blender: Temporal Feature Blender for Video Object Detection.
- **链接**: [arXiv:2108.05821](https://arxiv.org/abs/2108.05821) · 📚 被引 168
- **作者**: Yiming Cui, Liqi Yan, Zhiwen Cao, Dongfang Liu
- **🏷️ 机构**: University of Florida,USA, Fudan University,China, Purdue University,USA
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Video objection detection is a challenging task because isolated video frames may encounter appearance deterioration, which introduces great confusion for detection. One of the popular solutions is to exploit the temporal information and enhance per-frame representation through aggregating features from neighboring frames. Despite achieving improvements in detection, existing methods focus on the selection of higher-level video frames for aggregation rather than modeling lower-level temporal relations to increase the feature representation. To address this limitation, we propose a novel solution named TF-Blender,which includes three modules: 1) Temporal relation mod-els the relations between the current frame and its neighboring frames to preserve spatial information. 2). Feature adjustment enriches the representation of every neigh-boring feature map; 3) Feature blender combines outputs from the first two modules and produces stronger features for the later detection tasks. For its simplicity, TF-Blender can be effortlessly plugged into any detection network to improve detection behavior. Extensive evaluations on ImageNet VID and YouTube-VIS benchmarks indicate the performance guarantees of using TF-Blender on recent state-of-the-art methods.

</details>

### Boosting Weakly Supervised Object Detection via Learning Bounding Box Adjusters.
- **链接**: [arXiv:2108.01499](https://arxiv.org/abs/2108.01499) · [代码](https://github.com/DongSky/lbba_boosted_wsod) · 📚 被引 45
- **作者**: Bowen Dong, Zitong Huang, Yuelin Guo, Qilong Wang, Zhenxing Niu, Wangmeng Zuo
- **🏷️ 机构**: Harbin Institute of Technology, Tianjin University, Alibaba Damo Academay
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Weakly-supervised object detection (WSOD) has emerged as an inspiring recent topic to avoid expensive instance-level object annotations. However, the bounding boxes of most existing WSOD methods are mainly determined by precomputed proposals, thereby being limited in precise object localization. In this paper, we defend the problem setting for improving localization performance by leveraging the bounding box regression knowledge from a well-annotated auxiliary dataset. First, we use the well-annotated auxiliary dataset to explore a series of learnable bounding box adjusters (LBBAs) in a multi-stage training manner, which is class-agnostic. Then, only LBBAs and a weakly-annotated dataset with non-overlapped classes are used for training LBBA-boosted WSOD. As such, our LBBAs are practically more convenient and economical to implement while avoiding the leakage of the auxiliary well-annotated dataset. In particular, we formulate learning bounding box adjusters as a bi-level optimization problem and suggest an EM-like multi-stage training algorithm. Then, a multi-stage scheme is further presented for LBBA-boosted WSOD. Additionally, a masking strategy is adopted to improve proposal classification. Experimental results verify the effectiveness of our method. Our method performs favorably against state-of-the-art WSOD methods and knowledge transfer model with similar problem setting. Code is publicly available at \url{https://github.com/DongSky/lbba_boosted_wsod}.

</details>

### TOOD: Task-aligned One-stage Object Detection.
- **链接**: [arXiv:2108.07755](https://arxiv.org/abs/2108.07755) · [代码](https://github.com/fcjian/TOOD) · 📚 被引 1378
- **作者**: Chengjian Feng, Yujie Zhong, Yu Gao, Matthew R. Scott, Weilin Huang
- **🏷️ 机构**: Intellifusion Inc, Meituan Inc, ByteDance Inc
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> One-stage object detection is commonly implemented by optimizing two sub-tasks: object classification and localization, using heads with two parallel branches, which might lead to a certain level of spatial misalignment in predictions between the two tasks. In this work, we propose a Task-aligned One-stage Object Detection (TOOD) that explicitly aligns the two tasks in a learning-based manner. First, we design a novel Task-aligned Head (T-Head) which offers a better balance between learning task-interactive and task-specific features, as well as a greater flexibility to learn the alignment via a task-aligned predictor. Second, we propose Task Alignment Learning (TAL) to explicitly pull closer (or even unify) the optimal anchors for the two tasks during training via a designed sample assignment scheme and a task-aligned loss. Extensive experiments are conducted on MS-COCO, where TOOD achieves a 51.1 AP at single-model single-scale testing. This surpasses the recent one-stage detectors by a large margin, such as ATSS (47.7 AP), GFL (48.2 AP), and PAA (49.0 AP), with fewer parameters and FLOPs. Qualitative results also demonstrate the effectiveness of TOOD for better aligning the tasks of object classification and localization. Code is available at https://github.com/fcjian/TOOD.

</details>

### Exploring Classification Equilibrium in Long-Tailed Object Detection.
- **链接**: [arXiv:2108.07507](https://arxiv.org/abs/2108.07507) · [代码](https://github.com/fcjian/LOCE) · 📚 被引 103
- **作者**: Chengjian Feng, Yujie Zhong, Weilin Huang
- **🏷️ 机构**: Intellifusion Inc., Meituan Inc., Tao Technology,Alibaba Group
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The conventional detectors tend to make imbalanced classification and suffer performance drop, when the distribution of the training data is severely skewed. In this paper, we propose to use the mean classification score to indicate the classification accuracy for each category during training. Based on this indicator, we balance the classification via an Equilibrium Loss (EBL) and a Memory-augmented Feature Sampling (MFS) method. Specifically, EBL increases the intensity of the adjustment of the decision boundary for the weak classes by a designed score-guided loss margin between any two classes. On the other hand, MFS improves the frequency and accuracy of the adjustment of the decision boundary for the weak classes through over-sampling the instance features of those classes. Therefore, EBL and MFS work collaboratively for finding the classification equilibrium in long-tailed detection, and dramatically improve the performance of tail classes while maintaining or even improving the performance of head classes. We conduct experiments on LVIS using Mask R-CNN with various backbones including ResNet-50-FPN and ResNet-101-FPN to show the superiority of the proposed method. It improves the detection performance of tail classes by 15.6 AP, and outperforms the most recent long-tailed object detectors by more than 1 AP. Code is available at https://github.com/fcjian/LOCE.

</details>

### Mutual Supervision for Dense Object Detection.
- **链接**: [arXiv:2109.05986](https://arxiv.org/abs/2109.05986) · 📚 被引 42
- **作者**: Ziteng Gao, Limin Wang, Gangshan Wu
- **🏷️ 机构**: Nanjing University,State Key Laboratory for Novel Software Technology,China
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The classification and regression head are both indispensable components to build up a dense object detector, which are usually supervised by the same training samples and thus expected to have consistency with each other for detecting objects accurately in the detection pipeline. In this paper, we break the convention of the same training samples for these two heads in dense detectors and explore a novel supervisory paradigm, termed as Mutual Supervision (MuSu), to respectively and mutually assign training samples for the classification and regression head to ensure this consistency. MuSu defines training samples for the regression head mainly based on classification predicting scores and in turn, defines samples for the classification head based on localization scores from the regression head. Experimental results show that the convergence of detectors trained by this mutual supervision is guaranteed and the effectiveness of the proposed method is verified on the challenging MS COCO benchmark. We also find that tiling more anchors at the same location benefits detectors and leads to further improvements under this training scheme. We hope this work can inspire further researches on the interaction of the classification and regression task in detection and the supervision paradigm for detectors, especially separately for these two heads.

</details>

### Query Adaptive Few-Shot Object Detection with Heterogeneous Graph Convolutional Networks.
- **链接**: [arXiv:2112.09791](https://arxiv.org/abs/2112.09791) · 📚 被引 133
- **作者**: Guangxing Han, Yicheng He, Shiyuan Huang, Jiawei Ma, Shih-Fu Chang
- **🏷️ 机构**: Columbia University
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Few-shot object detection (FSOD) aims to detect never-seen objects using few examples. This field sees recent improvement owing to the meta-learning techniques by learning how to match between the query image and few-shot class examples, such that the learned model can generalize to few-shot novel classes. However, currently, most of the meta-learning-based methods perform pairwise matching between query image regions (usually proposals) and novel classes separately, therefore failing to take into account multiple relationships among them. In this paper, we propose a novel FSOD model using heterogeneous graph convolutional networks. Through efficient message passing among all the proposal and class nodes with three different types of edges, we could obtain context-aware proposal features and query-adaptive, multiclass-enhanced prototype representations for each class, which could help promote the pairwise matching and improve final FSOD accuracy. Extensive experimental results show that our proposed model, denoted as QA-FewDet, outperforms the current state-of-the-art approaches on the PASCAL VOC and MSCOCO FSOD benchmarks under different shots and evaluation metrics.

</details>

### Towards Rotation Invariance in Object Detection.
- **链接**: [arXiv:2109.13488](https://arxiv.org/abs/2109.13488) · [代码](https://github.com/akasha-imaging/ICCV2021) · 📚 被引 15
- **作者**: Agastya Kalra, Guy Stoppi, Bradley Brown, Rishav Agarwal, Achuta Kadambi
- **🏷️ 机构**: Akasha Imaging,Palo Alto,CA
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Rotation augmentations generally improve a model's invariance/equivariance to rotation - except in object detection. In object detection the shape is not known, therefore rotation creates a label ambiguity. We show that the de-facto method for bounding box label rotation, the Largest Box Method, creates very large labels, leading to poor performance and in many cases worse performance than using no rotation at all. We propose a new method of rotation augmentation that can be implemented in a few lines of code. First, we create a differentiable approximation of label accuracy and show that axis-aligning the bounding box around an ellipse is optimal. We then introduce Rotation Uncertainty (RU) Loss, allowing the model to adapt to the uncertainty of the labels. On five different datasets (including COCO, PascalVOC, and Transparent Object Bin Picking), this approach improves the rotational invariance of both one-stage and two-stage architectures when measured with AP, AP50, and AP75. The code is available at https://github.com/akasha-imaging/ICCV2021.

</details>

### ODAM: Object Detection, Association, and Mapping using Posed RGB Video.
- **链接**: [arXiv:2108.10165](https://arxiv.org/abs/2108.10165) · 📚 被引 27
- **作者**: Kejie Li, Daniel DeTone, Steven Chen, Minh Vo, Ian Reid, Hamid Rezatofighi et al.
- **🏷️ 机构**: The University of Adelaide, Facebook Reality Labs Research, Monash University
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Localizing objects and estimating their extent in 3D is an important step towards high-level 3D scene understanding, which has many applications in Augmented Reality and Robotics. We present ODAM, a system for 3D Object Detection, Association, and Mapping using posed RGB videos. The proposed system relies on a deep learning front-end to detect 3D objects from a given RGB frame and associate them to a global object-based map using a graph neural network (GNN). Based on these frame-to-model associations, our back-end optimizes object bounding volumes, represented as super-quadrics, under multi-view geometry constraints and the object scale prior. We validate the proposed system on ScanNet where we show a significant improvement over existing RGB-only methods.

</details>

### Parallel Rectangle Flip Attack: A Query-based Black-box Attack against Object Detection.
- **链接**: [arXiv:2201.08970](https://arxiv.org/abs/2201.08970) · 📚 被引 40
- **作者**: Siyuan Liang, Baoyuan Wu, Yanbo Fan, Xingxing Wei, Xiaochun Cao
- **🏷️ 机构**: Chinese Academy of Sciences,Institute of Information Engineering,Beijing,China, The Chinese University of Hong Kong,School of Data Science,Shenzhen,China, Tencent,Shenzhen,China
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Object detection has been widely used in many safety-critical tasks, such as autonomous driving. However, its vulnerability to adversarial examples has not been sufficiently studied, especially under the practical scenario of black-box attacks, where the attacker can only access the query feedback of predicted bounding-boxes and top-1 scores returned by the attacked model. Compared with black-box attack to image classification, there are two main challenges in black-box attack to detection. Firstly, even if one bounding-box is successfully attacked, another sub-optimal bounding-box may be detected near the attacked bounding-box. Secondly, there are multiple bounding-boxes, leading to very high attack cost. To address these challenges, we propose a Parallel Rectangle Flip Attack (PRFA) via random search. We explain the difference between our method with other attacks in Fig.~\ref{fig1}. Specifically, we generate perturbations in each rectangle patch to avoid sub-optimal detection near the attacked region. Besides, utilizing the observation that adversarial perturbations mainly locate around objects' contours and critical points under white-box attacks, the search space of attacked rectangles is reduced to improve the attack efficiency. Moreover, we develop a parallel mechanism of attacking multiple rectangles simultaneously to further accelerate the attack process. Extensive experiments demonstrate that our method can effectively and efficiently attack various popular object detectors, including anchor-based and anchor-free, and generate transferable adversarial examples.

</details>

### Domain-Invariant Disentangled Network for Generalizable Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00865) · 📚 被引 72
- **作者**: Chuang Lin, Zehuan Yuan, Sicheng Zhao, Peize Sun, Changhu Wang, Jianfei Cai
- **🏷️ 机构**: Monash University,Dept of Data Science and AI, ByteDance AI Lab, Columbia University
- **会议**: ICCV 2021

### Self-Supervised Object Detection via Generative Image Synthesis.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00849)
- **作者**: Siva Karthik Mustikovela, Shalini De Mello, Aayush Prakash, Umar Iqbal, Sifei Liu, Thu Nguyen-Phuoc et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### Rank & Sort Loss for Object Detection and Instance Segmentation.
- **链接**: [arXiv:2107.11669](https://arxiv.org/abs/2107.11669) · [代码](https://github.com/kemaloksuz/RankSortLoss) · 📚 被引 46
- **作者**: Kemal Oksuz, Baris Can Cam, Emre Akbas, Sinan Kalkan
- **🏷️ 机构**: Middle East Technical University,Dept. of Computer Engineering,Ankara,Turkey
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose Rank & Sort (RS) Loss, a ranking-based loss function to train deep object detection and instance segmentation methods (i.e. visual detectors). RS Loss supervises the classifier, a sub-network of these methods, to rank each positive above all negatives as well as to sort positives among themselves with respect to (wrt.) their localisation qualities (e.g. Intersection-over-Union - IoU). To tackle the non-differentiable nature of ranking and sorting, we reformulate the incorporation of error-driven update with backpropagation as Identity Update, which enables us to model our novel sorting error among positives. With RS Loss, we significantly simplify training: (i) Thanks to our sorting objective, the positives are prioritized by the classifier without an additional auxiliary head (e.g. for centerness, IoU, mask-IoU), (ii) due to its ranking-based nature, RS Loss is robust to class imbalance, and thus, no sampling heuristic is required, and (iii) we address the multi-task nature of visual detectors using tuning-free task-balancing coefficients. Using RS Loss, we train seven diverse visual detectors only by tuning the learning rate, and show that it consistently outperforms baselines: e.g. our RS Loss improves (i) Faster R-CNN by ~ 3 box AP and aLRP Loss (ranking-based baseline) by ~ 2 box AP on COCO dataset, (ii) Mask R-CNN with repeat factor sampling (RFS) by 3.5 mask AP (~ 7 AP for rare classes) on LVIS dataset; and also outperforms all counterparts. Code is available at: https://github.com/kemaloksuz/RankSortLoss

</details>

### MFNet: Multi-filter Directive Network for Weakly Supervised Salient Object Detection.
- **链接**: [arXiv:2112.01732](https://arxiv.org/abs/2112.01732) · 📚 被引 85
- **作者**: Yongri Piao, Jian Wang, Miao Zhang, Huchuan Lu
- **🏷️ 机构**: Dalian University of Technology,China
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Weakly supervised salient object detection (WSOD) targets to train a CNNs-based saliency network using only low-cost annotations. Existing WSOD methods take various techniques to pursue single "high-quality" pseudo label from low-cost annotations and then develop their saliency networks. Though these methods have achieved good performance, the generated single label is inevitably affected by adopted refinement algorithms and shows prejudiced characteristics which further influence the saliency networks. In this work, we introduce a new multiple-pseudo-label framework to integrate more comprehensive and accurate saliency cues from multiple labels, avoiding the aforementioned problem. Specifically, we propose a multi-filter directive network (MFNet) including a saliency network as well as multiple directive filters. The directive filter (DF) is designed to extract and filter more accurate saliency cues from the noisy pseudo labels. The multiple accurate cues from multiple DFs are then simultaneously propagated to the saliency network with a multi-guidance loss. Extensive experiments on five datasets over four metrics demonstrate that our method outperforms all the existing congeneric methods. Moreover, it is also worth noting that our framework is flexible enough to apply to existing methods and improve their performance.

</details>

### DeFRCN: Decoupled Faster R-CNN for Few-Shot Object Detection.
- **链接**: [arXiv:2108.09017](https://arxiv.org/abs/2108.09017) · 📚 被引 363
- **作者**: Limeng Qiao, Yuxuan Zhao, Zhiyuan Li, Xi Qiu, Jianan Wu, Chi Zhang
- **🏷️ 机构**: Megvii Technology
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Few-shot object detection, which aims at detecting novel objects rapidly from extremely few annotated examples of previously unseen classes, has attracted significant research interest in the community. Most existing approaches employ the Faster R-CNN as basic detection framework, yet, due to the lack of tailored considerations for data-scarce scenario, their performance is often not satisfactory. In this paper, we look closely into the conventional Faster R-CNN and analyze its contradictions from two orthogonal perspectives, namely multi-stage (RPN vs. RCNN) and multi-task (classification vs. localization). To resolve these issues, we propose a simple yet effective architecture, named Decoupled Faster R-CNN (DeFRCN). To be concrete, we extend Faster R-CNN by introducing Gradient Decoupled Layer for multi-stage decoupling and Prototypical Calibration Block for multi-task decoupling. The former is a novel deep layer with redefining the feature-forward operation and gradient-backward operation for decoupling its subsequent layer and preceding layer, and the latter is an offline prototype-based classification model with taking the proposals from detector as input and boosting the original classification scores with additional pairwise scores for calibration. Extensive experiments on multiple benchmarks show our framework is remarkably superior to other existing approaches and establishes a new state-of-the-art in few-shot literature.

</details>

### CrossDet: Crossline Representation for Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00318) · 📚 被引 19
- **作者**: Heqian Qiu, Hongliang Li, Qingbo Wu, Jianhua Cui, Zichen Song, Lanxiao Wang et al.
- **🏷️ 机构**: University of Electronic Science and Technology of China,Chengdu,China
- **会议**: ICCV 2021

### SimROD: A Simple Adaptation Method for Robust Object Detection.
- **链接**: [arXiv:2107.13389](https://arxiv.org/abs/2107.13389) · 📚 被引 47
- **作者**: Rindra Ramamonjison, Amin Banitalebi-Dehkordi, Xinyu Kang, Xiaolong Bai, Yong Zhang
- **🏷️ 机构**: Huawei Technologies Canada Co., Ltd, University of British Columbia, Huawei Cloud
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper presents a Simple and effective unsupervised adaptation method for Robust Object Detection (SimROD). To overcome the challenging issues of domain shift and pseudo-label noise, our method integrates a novel domain-centric augmentation method, a gradual self-labeling adaptation procedure, and a teacher-guided fine-tuning mechanism. Using our method, target domain samples can be leveraged to adapt object detection models without changing the model architecture or generating synthetic data. When applied to image corruptions and high-level cross-domain adaptation benchmarks, our method outperforms prior baselines on multiple domain adaptation benchmarks. SimROD achieves new state-of-the-art on standard real-to-synthetic and cross-camera setup benchmarks. On the image corruption benchmark, models adapted with our method achieved a relative robustness improvement of 15-25% AP50 on Pascal-C and 5-6% AP on COCO-C and Cityscapes-C. On the cross-domain benchmark, our method outperformed the best baseline performance by up to 8% AP50 on Comic dataset and up to 4% on Watercolor dataset.

</details>

### Seeking Similarities over Differences: Similarity-based Domain Alignment for Adaptive Object Detection.
- **链接**: [arXiv:2110.01428](https://arxiv.org/abs/2110.01428) · 📚 被引 74
- **作者**: Farzaneh Rezaeianaran, Rakshith Shetty, Rahaf Aljundi, Daniel Olmeda Reino, Shanshan Zhang, Bernt Schiele
- **🏷️ 机构**: Max Planck Institute for Informatics, Toyota Motor Europe, Nanjing University of Science and Technology
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In order to robustly deploy object detectors across a wide range of scenarios, they should be adaptable to shifts in the input distribution without the need to constantly annotate new data. This has motivated research in Unsupervised Domain Adaptation (UDA) algorithms for detection. UDA methods learn to adapt from labeled source domains to unlabeled target domains, by inducing alignment between detector features from source and target domains. Yet, there is no consensus on what features to align and how to do the alignment. In our work, we propose a framework that generalizes the different components commonly used by UDA methods laying the ground for an in-depth analysis of the UDA design space. Specifically, we propose a novel UDA algorithm, ViSGA, a direct implementation of our framework, that leverages the best design choices and introduces a simple but effective method to aggregate features at instance-level based on visual similarity before inducing group alignment via adversarial training. We show that both similarity-based grouping and adversarial training allows our model to focus on coarsely aligning feature groups, without being forced to match all instances across loosely aligned domains. Finally, we examine the applicability of ViSGA to the setting where labeled data are gathered from different sources. Experiments show that not only our method outperforms previous single-source approaches on Sim2Real and Adverse Weather, but also generalizes well to the multi-source setting.

</details>

### Scene Context-Aware Salient Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00412) · 📚 被引 69
- **作者**: Avishek Siris, Jianbo Jiao, Gary K. L. Tam, Xianghua Xie, Rynson W. H. Lau
- **🏷️ 机构**: Swansea University,Department of Computer Science, University of Oxford, City University of Hong Kong
- **会议**: ICCV 2021

### Rethinking Transformer-based Set Prediction for Object Detection.
- **链接**: [arXiv:2011.10881](https://arxiv.org/abs/2011.10881) · 📚 被引 287
- **作者**: Zhiqing Sun, Shengcao Cao, Yiming Yang, Kris Kitani
- **🏷️ 机构**: Carnegie Mellon University
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> DETR is a recently proposed Transformer-based method which views object detection as a set prediction problem and achieves state-of-the-art performance but demands extra-long training time to converge. In this paper, we investigate the causes of the optimization difficulty in the training of DETR. Our examinations reveal several factors contributing to the slow convergence of DETR, primarily the issues with the Hungarian loss and the Transformer cross-attention mechanism. To overcome these issues we propose two solutions, namely, TSP-FCOS (Transformer-based Set Prediction with FCOS) and TSP-RCNN (Transformer-based Set Prediction with RCNN). Experimental results show that the proposed methods not only converge much faster than the original DETR, but also significantly outperform DETR and other baselines in terms of detection accuracy.

</details>

### Disentangled High Quality Salient Object Detection.
- **链接**: [arXiv:2108.03551](https://arxiv.org/abs/2108.03551) · 📚 被引 30
- **作者**: Lv Tang, Bo Li, Yijie Zhong, Shouhong Ding, Mofei Song
- **🏷️ 机构**: Tencent,Youtu Lab,Shanghai,China, Southeast University,The School of Computer Science and Engineering,Nanjing,China
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Aiming at discovering and locating most distinctive objects from visual scenes, salient object detection (SOD) plays an essential role in various computer vision systems. Coming to the era of high resolution, SOD methods are facing new challenges. The major limitation of previous methods is that they try to identify the salient regions and estimate the accurate objects boundaries simultaneously with a single regression task at low-resolution. This practice ignores the inherent difference between the two difficult problems, resulting in poor detection quality. In this paper, we propose a novel deep learning framework for high-resolution SOD task, which disentangles the task into a low-resolution saliency classification network (LRSCN) and a high-resolution refinement network (HRRN). As a pixel-wise classification task, LRSCN is designed to capture sufficient semantics at low-resolution to identify the definite salient, background and uncertain image regions. HRRN is a regression task, which aims at accurately refining the saliency value of pixels in the uncertain region to preserve a clear object boundary at high-resolution with limited GPU memory. It is worth noting that by introducing uncertainty into the training process, our HRRN can well address the high-resolution refinement task without using any high-resolution training data. Extensive experiments on high-resolution saliency datasets as well as some widely used saliency benchmarks show that the proposed method achieves superior performance compared to the state-of-the-art methods.

</details>

### Knowledge Mining and Transferring for Domain Adaptive Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00900) · 📚 被引 51
- **作者**: Kun Tian, Chenghao Zhang, Ying Wang, Shiming Xiang, Chunhong Pan
- **🏷️ 机构**: Chinese Academy of Sciences,National Laboratory of Pattern Recognition, Institute of Automation
- **会议**: ICCV 2021

### Reconcile Prediction Consistency for Balanced Object Detection.
- **链接**: [arXiv:2108.10809](https://arxiv.org/abs/2108.10809) · 📚 被引 40
- **作者**: Keyang Wang, Lei Zhang
- **🏷️ 机构**: Chongqing University,Learning Intelligence &#x0026; Vision Essential (LiVE) Group School of Microelectronics and Communication Engineering,China
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Classification and regression are two pillars of object detectors. In most CNN-based detectors, these two pillars are optimized independently. Without direct interactions between them, the classification loss and the regression loss can not be optimized synchronously toward the optimal direction in the training phase. This clearly leads to lots of inconsistent predictions with high classification score but low localization accuracy or low classification score but high localization accuracy in the inference phase, especially for the objects of irregular shape and occlusion, which severely hurts the detection performance of existing detectors after NMS. To reconcile prediction consistency for balanced object detection, we propose a Harmonic loss to harmonize the optimization of classification branch and localization branch. The Harmonic loss enables these two branches to supervise and promote each other during training, thereby producing consistent predictions with high co-occurrence of top classification and localization in the inference phase. Furthermore, in order to prevent the localization loss from being dominated by outliers during training phase, a Harmonic IoU loss is proposed to harmonize the weight of the localization loss of different IoU-level samples. Comprehensive experiments on benchmarks PASCAL VOC and MS COCO demonstrate the generality and effectiveness of our model for facilitating existing object detectors to state-of-the-art accuracy.

</details>

### Universal-Prototype Enhancing for Few-Shot Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00943) · 📚 被引 108
- **作者**: Aming Wu, Yahong Han, Linchao Zhu, Yi Yang
- **🏷️ 机构**: Xidian University,School of Electronic Engineering,Xi&#x2019;an,China, Tianjin University,College of Intelligence and Computing,Tianjin,China, University of Technology,ReLER Lab, AAII,Sydney
- **会议**: ICCV 2021

### Vector-Decomposed Disentanglement for Domain-Invariant Object Detection.
- **链接**: [arXiv:2108.06685](https://arxiv.org/abs/2108.06685) · 📚 被引 126
- **作者**: Aming Wu, Rui Liu, Yahong Han, Linchao Zhu, Yi Yang
- **🏷️ 机构**: Tianjin University,College of Intelligence and Computing,China, University of Technology Sydney,ReLER Lab, Aaii
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> To improve the generalization of detectors, for domain adaptive object detection (DAOD), recent advances mainly explore aligning feature-level distributions between the source and single-target domain, which may neglect the impact of domain-specific information existing in the aligned features. Towards DAOD, it is important to extract domain-invariant object representations. To this end, in this paper, we try to disentangle domain-invariant representations from domain-specific representations. And we propose a novel disentangled method based on vector decomposition. Firstly, an extractor is devised to separate domain-invariant representations from the input, which are used for extracting object proposals. Secondly, domain-specific representations are introduced as the differences between the input and domain-invariant representations. Through the difference operation, the gap between the domain-specific and domain-invariant representations is enlarged, which promotes domain-invariant representations to contain more domain-irrelevant information. In the experiment, we separately evaluate our method on the single- and compound-target case. For the single-target case, experimental results of four domain-shift scenes show our method obtains a significant performance gain over baseline methods. Moreover, for the compound-target case (i.e., the target is a compound of two different domains without domain labels), our method outperforms baseline methods by around 4%, which demonstrates the effectiveness of our method.

</details>

### Oriented R-CNN for Object Detection.
- **链接**: [arXiv:2108.05699](https://arxiv.org/abs/2108.05699) · [代码](https://github.com/jbwang1997/OBBDetection)
- **作者**: Xingxing Xie, Gong Cheng, Jiabao Wang, Xiwen Yao, Junwei Han
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Current state-of-the-art two-stage detectors generate oriented proposals through time-consuming schemes. This diminishes the detectors' speed, thereby becoming the computational bottleneck in advanced oriented object detection systems. This work proposes an effective and simple oriented object detection framework, termed Oriented R-CNN, which is a general two-stage oriented detector with promising accuracy and efficiency. To be specific, in the first stage, we propose an oriented Region Proposal Network (oriented RPN) that directly generates high-quality oriented proposals in a nearly cost-free manner. The second stage is oriented R-CNN head for refining oriented Regions of Interest (oriented RoIs) and recognizing them. Without tricks, oriented R-CNN with ResNet50 achieves state-of-the-art detection accuracy on two commonly-used datasets for oriented object detection including DOTA (75.87% mAP) and HRSC2016 (96.50% mAP), while having a speed of 15.1 FPS with the image size of 1024$\times$1024 on a single RTX 2080Ti. We hope our work could inspire rethinking the design of oriented detectors and serve as a baseline for oriented object detection. Code is available at https://github.com/jbwang1997/OBBDetection.

</details>

### DetCo: Unsupervised Contrastive Learning for Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00828)
- **作者**: Enze Xie, Jian Ding, Wenhai Wang, Xiaohang Zhan, Hang Xu, Peize Sun et al.
- **🏷️ 机构**: Shanghai AI Lab
- **会议**: ICCV 2021

### End-to-End Semi-Supervised Object Detection with Soft Teacher.
- **链接**: [arXiv:2106.09018](https://arxiv.org/abs/2106.09018) · 📚 被引 509
- **作者**: Mengde Xu, Zheng Zhang, Han Hu, Jianfeng Wang, Lijuan Wang, Fangyun Wei et al.
- **🏷️ 机构**: Huazhong University of Science and Technology, Microsoft
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper presents an end-to-end semi-supervised object detection approach, in contrast to previous more complex multi-stage methods. The end-to-end training gradually improves pseudo label qualities during the curriculum, and the more and more accurate pseudo labels in turn benefit object detection training. We also propose two simple yet effective techniques within this framework: a soft teacher mechanism where the classification loss of each unlabeled bounding box is weighed by the classification score produced by the teacher network; a box jittering approach to select reliable pseudo boxes for the learning of box regression. On the COCO benchmark, the proposed approach outperforms previous methods by a large margin under various labeling ratios, i.e. 1\%, 5\% and 10\%. Moreover, our approach proves to perform also well when the amount of labeled data is relatively large. For example, it can improve a 40.9 mAP baseline detector trained using the full COCO training set by +3.6 mAP, reaching 44.5 mAP, by leveraging the 123K unlabeled images of COCO. On the state-of-the-art Swin Transformer based object detector (58.9 mAP on test-dev), it can still significantly improve the detection accuracy by +1.5 mAP, reaching 60.4 mAP, and improve the instance segmentation accuracy by +1.2 mAP, reaching 52.4 mAP. Further incorporating with the Object365 pre-trained model, the detection accuracy reaches 61.3 mAP and the instance segmentation accuracy reaches 53.0 mAP, pushing the new state-of-the-art.

</details>

### Multi-Source Domain Adaptation for Object Detection.
- **链接**: [arXiv:2106.15793](https://arxiv.org/abs/2106.15793) · 📚 被引 46
- **作者**: Xingxu Yao, Sicheng Zhao, Pengfei Xu, Jufeng Yang
- **🏷️ 机构**: Nankai University,China, Columbia University,USA, Didi Chuxing,China
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> To reduce annotation labor associated with object detection, an increasing number of studies focus on transferring the learned knowledge from a labeled source domain to another unlabeled target domain. However, existing methods assume that the labeled data are sampled from a single source domain, which ignores a more generalized scenario, where labeled data are from multiple source domains. For the more challenging task, we propose a unified Faster R-CNN based framework, termed Divide-and-Merge Spindle Network (DMSN), which can simultaneously enhance domain invariance and preserve discriminative power. Specifically, the framework contains multiple source subnets and a pseudo target subnet. First, we propose a hierarchical feature alignment strategy to conduct strong and weak alignments for low- and high-level features, respectively, considering their different effects for object detection. Second, we develop a novel pseudo subnet learning algorithm to approximate optimal parameters of pseudo target subset by weighted combination of parameters in different source subnets. Finally, a consistency regularization for region proposal network is proposed to facilitate each subnet to learn more abstract invariances. Extensive experiments on different adaptation scenarios demonstrate the effectiveness of the proposed model.

</details>

### Dynamic Context-Sensitive Filtering Network for Video Salient Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00158) · 📚 被引 112
- **作者**: Miao Zhang, Jie Liu, Yifei Wang, Yongri Piao, Shunyu Yao, Wei Ji et al.
- **🏷️ 机构**: Dalian University of Technology,China, University of Alberta,Canada
- **会议**: ICCV 2021

### GraphFPN: Graph Feature Pyramid Network for Object Detection.
- **链接**: [arXiv:2108.00580](https://arxiv.org/abs/2108.00580) · 📚 被引 127
- **作者**: Gangming Zhao, Weifeng Ge, Yizhou Yu
- **🏷️ 机构**: Fudan University,Nebula AI Group, School of Computer Science, The University of Hong Kong,Department of Computer Science
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Feature pyramids have been proven powerful in image understanding tasks that require multi-scale features. State-of-the-art methods for multi-scale feature learning focus on performing feature interactions across space and scales using neural networks with a fixed topology. In this paper, we propose graph feature pyramid networks that are capable of adapting their topological structures to varying intrinsic image structures and supporting simultaneous feature interactions across all scales. We first define an image-specific superpixel hierarchy for each input image to represent its intrinsic image structures. The graph feature pyramid network inherits its structure from this superpixel hierarchy. Contextual and hierarchical layers are designed to achieve feature interactions within the same scale and across different scales. To make these layers more powerful, we introduce two types of local channel attention for graph neural networks by generalizing global channel attention for convolutional neural networks. The proposed graph feature pyramid network can enhance the multiscale features from a convolutional feature pyramid network. We evaluate our graph feature pyramid network in the object detection task by integrating it into the Faster R-CNN algorithm. The modified algorithm outperforms not only previous state-of-the-art feature pyramid-based methods with a clear margin but also other popular detection methods on both MS-COCO 2017 validation and test datasets.

</details>

## 跨领域论文（完整笔记在其他领域）

- RangeDet: In Defense of Range View for LiDAR-based 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202021.md)
- iNAS: Integral NAS for Device-Aware Salient Object Detection. → [neural-architecture-search](../neural-architecture-search/Guideline%202021.md)
- Fog Simulation on Real LiDAR Point Clouds for 3D Object Detection in Adverse Weather. → [3d-detection](../3d-detection/Guideline%202021.md)
- Gated3D: Monocular 3D Object Detection From Temporal Illumination Cues. → [3d-detection](../3d-detection/Guideline%202021.md)
- Exploring Geometry-aware Contrast and Clustering Harmonization for Self-supervised 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202021.md)
- Group-Free 3D Object Detection via Transformers. → [3d-detection](../3d-detection/Guideline%202021.md)
- AutoShape: Real-Time Shape-Aware Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202021.md)
- Geometry Uncertainty Projection Network for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202021.md)
- Multi-Echo LiDAR for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202021.md)
- Pyramid R-CNN: Towards Better Performance and Adaptability for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202021.md)
- Voxel Transformer for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202021.md)
- An End-to-End Transformer Model for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202021.md)
- Is Pseudo-Lidar needed for Monocular 3D Object detection? → [3d-detection](../3d-detection/Guideline%202021.md)
- RandomRooms: Unsupervised Pre-training from Synthetic Shapes and Randomized Layouts for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202021.md)
- Improving 3D Object Detection with Channel-wise Transformer. → [3d-detection](../3d-detection/Guideline%202021.md)
- Geometry-based Distance Decomposition for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202021.md)
- Are we Missing Confidence in Pseudo-LiDAR Methods for Monocular 3D Object Detection? → [3d-detection](../3d-detection/Guideline%202021.md)
- You Don't Only Look Once: Constructing Spatial-Temporal Memory for Integrated 3D Object Detection and Tracking. → [3d-detection](../3d-detection/Guideline%202021.md)
- Wanderlust: Online Continual Object Detection in the Real World. → [continual-learning](../continual-learning/Guideline%202021.md)
- VENet: Voting Enhancement Network for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202021.md)
- SPG: Unsupervised Domain Adaptation for 3D Object Detection via Semantic Point Generation. → [3d-detection](../3d-detection/Guideline%202021.md)
