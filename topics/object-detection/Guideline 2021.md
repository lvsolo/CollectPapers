# Object Detection — 2021 Guideline

> 领域: 通用 2D 目标检测（检测器架构、密集预测、小物体/旋转框/NMS 等）
> 论文数: 16 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Dynamic DETR: End-to-End Object Detection with Dynamic Attention.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00298) · 📚 被引 405
- **作者**: Xiyang Dai, Yinpeng Chen, Jianwei Yang, Pengchuan Zhang, Lu Yuan, Lei Zhang
- **🏷️ 机构**: Microsoft
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> DEtection TRansformer (DETR) for object detection reaches competitive performance compared with Faster R-CNN via a transformer encoder-decoder architecture. However, trained with scratch transformers, DETR needs large-scale training data and an extreme long training schedule even on COCO dataset. Inspired by the great success of pre-training transformers in natural language processing, we propose a novel pretext task named random query patch detection in Unsupervised Pre-training DETR (UP-DETR). Specifically, we randomly crop patches from the given image and then feed them as queries to the decoder. The model is pre-trained to detect these query patches from the input image. During the pre-training, we address two critical issues: multi-task learning and multi-query localization. (1) To trade off classification and localization preferences in the pretext task, we find that freezing the CNN backbone is the prerequisite for the success of pre-training transformers. (2) To perform multi-query localization, we develop UP-DETR with multi-query patch detection with attention mask. Besides, UP-DETR also provides a unified perspective for fine-tuning object detection and one-shot detection tasks. In our experiments, UP-DETR significantly boosts the performance of DETR with faster convergence and higher average precision on object detection, one-shot detection and panoptic segmentation. Code and pre-training models: https://github.com/dddzg/up-detr.

</details>

### Robust Object Detection via Instance-Level Temporal Cycle Confusion.
- **链接**: [arXiv:2104.08381](https://arxiv.org/abs/2104.08381) · [代码](https://github.com/xinw1012/cycle-confusion) · 📚 被引 25
- **作者**: Xin Wang, Thomas E. Huang, Benlin Liu, Fisher Yu, Xiaolong Wang, Joseph E. Gonzalez et al.
- **🏷️ 机构**: Microsoft Research, ETH Z&#x00FC;rich, University of Washington
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Visual salient object detection (SOD) aims at finding the salient object(s) that attract human attention, while camouflaged object detection (COD) on the contrary intends to discover the camouflaged object(s) that hidden in the surrounding. In this paper, we propose a paradigm of leveraging the contradictory information to enhance the detection ability of both salient object detection and camouflaged object detection. We start by exploiting the easy positive samples in the COD dataset to serve as hard positive samples in the SOD task to improve the robustness of the SOD model. Then, we introduce a similarity measure module to explicitly model the contradicting attributes of these two tasks. Furthermore, considering the uncertainty of labeling in both tasks' datasets, we propose an adversarial learning network to achieve both higher order similarity measure and network confidence estimation. Experimental results on benchmark datasets demonstrate that our solution leads to state-of-the-art (SOTA) performance for both tasks.

</details>

</details>

### CaT: Weakly Supervised Object Detection with Category Transfer.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00306) · 📚 被引 24
- **作者**: Tianyue Cao, Lianyu Du, Xiaoyun Zhang, Siheng Chen, Ya Zhang, Yanfeng Wang
- **🏷️ 机构**: Shanghai Jiao Tong University,Cooperative Medianet Innovation Center
- **会议**: ICCV 2021

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
- **链接**: [arXiv:2108.05821](https://arxiv.org/abs/2108.05821)
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
- **链接**: [arXiv:2108.07755](https://arxiv.org/abs/2108.07755) · [代码](https://github.com/fcjian/TOOD) · 📚 被引 1377
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
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00325) · 📚 被引 133
- **作者**: Guangxing Han, Yicheng He, Shiyuan Huang, Jiawei Ma, Shih-Fu Chang
- **🏷️ 机构**: Columbia University
- **会议**: ICCV 2021

### Towards Rotation Invariance in Object Detection.
- **链接**: [arXiv:2109.13488](https://arxiv.org/abs/2109.13488) · [代码](https://github.com/akasha-imaging/ICCV2021) · 📚 被引 15
- **作者**: Agastya Kalra, Guy Stoppi, Bradley Brown, Rishav Agarwal, Achuta Kadambi
- **🏷️ 机构**: Akasha Imaging,Palo Alto,CA
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Rotation augmentations generally improve a model's invariance/equivariance to rotation - except in object detection. In object detection the shape is not known, therefore rotation creates a label ambiguity. We show that the de-facto method for bounding box label rotation, the Largest Box Method, creates very large labels, leading to poor performance and in many cases worse performance than using no rotation at all. We propose a new method of rotation augmentation that can be implemented in a few lines of code. First, we create a differentiable approximation of label accuracy and show that axis-aligning the bounding box around an ellipse is optimal. We then introduce Rotation Uncertainty (RU) Loss, allowing the model to adapt to the uncertainty of the labels. On five different datasets (including COCO, PascalVOC, and Transparent Object Bin Picking), this approach improves the rotational invariance of both one-stage and two-stage architectures when measured with AP, AP50, and AP75. The code is available at https://github.com/akasha-imaging/ICCV2021.

</details>

### ODAM: Object Detection, Association, and Mapping using Posed RGB Video.
- **链接**: [arXiv:2108.10165](https://arxiv.org/abs/2108.10165)
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

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Supervised learning based object detection frameworks demand plenty of laborious manual annotations, which may not be practical in real applications. Semi-supervised object detection (SSOD) can effectively leverage unlabeled data to improve the model performance, which is of great significance for the application of object detection models. In this paper, we revisit SSOD and propose Instant-Teaching, a completely end-to-end and effective SSOD framework, which uses instant pseudo labeling with extended weak-strong data augmentations for teaching during each training iteration. To alleviate the confirmation bias problem and improve the quality of pseudo annotations, we further propose a co-rectify scheme based on Instant-Teaching, denoted as Instant-Teaching$^*$. Extensive experiments on both MS-COCO and PASCAL VOC datasets substantiate the superiority of our framework. Specifically, our method surpasses state-of-the-art methods by 4.2 mAP on MS-COCO when using $2\%$ labeled data. Even with full supervised information of MS-COCO, the proposed method still outperforms state-of-the-art methods by about 1.0 mAP. On PASCAL VOC, we can achieve more than 5 mAP improvement by applying VOC07 as labeled data and VOC12 as unlabeled data.

</details>

> We propose Rank & Sort (RS) Loss, a ranking-based loss function to train deep object detection and instance segmentation methods (i.e. visual detectors). RS Loss supervises the classifier, a sub-network of these methods, to rank each positive above all negatives as well as to sort positives among themselves with respect to (wrt.) their localisation qualities (e.g. Intersection-over-Union - IoU). To tackle the non-differentiable nature of ranking and sorting, we reformulate the incorporation of error-driven update with backpropagation as Identity Update, which enables us to model our novel sorting error among positives. With RS Loss, we significantly simplify training: (i) Thanks to our sorting objective, the positives are prioritized by the classifier without an additional auxiliary head (e.g. for centerness, IoU, mask-IoU), (ii) due to its ranking-based nature, RS Loss is robust to class imbalance, and thus, no sampling heuristic is required, and (iii) we address the multi-task nature of visual detectors using tuning-free task-balancing coefficients. Using RS Loss, we train seven diverse visual detectors only by tuning the learning rate, and show that it consistently outperforms baselines: e.g. our RS Loss improves (i) Faster R-CNN by ~ 3 box AP and aLRP Loss (ranking-based baseline) by ~ 2 box AP on COCO dataset, (ii) Mask R-CNN with repeat factor sampling (RFS) by 3.5 mask AP (~ 7 AP for rare classes) on LVIS dataset; and also outperforms all counterparts. Code is available at: https://github.com/kemaloksuz/RankSortLoss

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose a novel point annotated setting for the weakly semi-supervised object detection task, in which the dataset comprises small fully annotated images and large weakly annotated images by points. It achieves a balance between tremendous annotation burden and detection performance. Based on this setting, we analyze existing detectors and find that these detectors have difficulty in fully exploiting the power of the annotated points. To solve this, we introduce a new detector, Point DETR, which extends DETR by adding a point encoder. Extensive experiments conducted on MS-COCO dataset in various data settings show the effectiveness of our method. In particular, when using 20% fully labeled data from COCO, our detector achieves a promising performance, 33.3 AP, which outperforms a strong baseline (FCOS) by 2.0 AP, and we demonstrate the point annotations bring over 10 points in various AR metrics.

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Weakly supervised salient object detection (WSOD) targets to train a CNNs-based saliency network using only low-cost annotations. Existing WSOD methods take various techniques to pursue single "high-quality" pseudo label from low-cost annotations and then develop their saliency networks. Though these methods have achieved good performance, the generated single label is inevitably affected by adopted refinement algorithms and shows prejudiced characteristics which further influence the saliency networks. In this work, we introduce a new multiple-pseudo-label framework to integrate more comprehensive and accurate saliency cues from multiple labels, avoiding the aforementioned problem. Specifically, we propose a multi-filter directive network (MFNet) including a saliency network as well as multiple directive filters. The directive filter (DF) is designed to extract and filter more accurate saliency cues from the noisy pseudo labels. The multiple accurate cues from multiple DFs are then simultaneously propagated to the saliency network with a multi-guidance loss. Extensive experiments on five datasets over four metrics demonstrate that our method outperforms all the existing congeneric methods. Moreover, it is also worth noting that our framework is flexible enough to apply to existing methods and improve their performance.

</details>

### DeFRCN: Decoupled Faster R-CNN for Few-Shot Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00856) · 📚 被引 363
- **作者**: Limeng Qiao, Yuxuan Zhao, Zhiyuan Li, Xi Qiu, Jianan Wu, Chi Zhang
- **🏷️ 机构**: Megvii Technology
- **会议**: ICCV 2021

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

### Seeking Similarities over Differences: Similarity-based Domain Alignment for Adaptive Object Detection.
- **链接**: [arXiv:2110.01428](https://arxiv.org/abs/2110.01428) · 📚 被引 74
- **作者**: Farzaneh Rezaeianaran, Rakshith Shetty, Rahaf Aljundi, Daniel Olmeda Reino, Shanshan Zhang, Bernt Schiele
- **🏷️ 机构**: Max Planck Institute for Informatics, Toyota Motor Europe, Nanjing University of Science and Technology
- **会议**: ICCV 2021

### Scene Context-Aware Salient Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00412) · 📚 被引 69
- **作者**: Avishek Siris, Jianbo Jiao, Gary K. L. Tam, Xianghua Xie, Rynson W. H. Lau
- **🏷️ 机构**: Swansea University,Department of Computer Science, University of Oxford, City University of Hong Kong
- **会议**: ICCV 2021

### Rethinking Transformer-based Set Prediction for Object Detection.
- **链接**: [arXiv:2011.10881](https://arxiv.org/abs/2011.10881)
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
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00361) · 📚 被引 40
- **作者**: Keyang Wang, Lei Zhang
- **🏷️ 机构**: Chongqing University,Learning Intelligence &#x0026; Vision Essential (LiVE) Group School of Microelectronics and Communication Engineering,China
- **会议**: ICCV 2021

### Universal-Prototype Enhancing for Few-Shot Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00943) · 📚 被引 108
- **作者**: Aming Wu, Yahong Han, Linchao Zhu, Yi Yang
- **🏷️ 机构**: Xidian University,School of Electronic Engineering,Xi&#x2019;an,China, Tianjin University,College of Intelligence and Computing,Tianjin,China, University of Technology,ReLER Lab, AAII,Sydney
- **会议**: ICCV 2021

### Vector-Decomposed Disentanglement for Domain-Invariant Object Detection.
- **链接**: [arXiv:2108.06685](https://arxiv.org/abs/2108.06685)
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

> Transfer learning with pre-training on large-scale datasets has played an increasingly significant role in computer vision and natural language processing recently. However, as there exist numerous application scenarios that have distinctive demands such as certain latency constraints and specialized data distributions, it is prohibitively expensive to take advantage of large-scale pre-training for per-task requirements. In this paper, we focus on the area of object detection and present a transfer learning system named GAIA, which could automatically and efficiently give birth to customized solutions according to heterogeneous downstream needs. GAIA is capable of providing powerful pre-trained weights, selecting models that conform to downstream demands such as latency constraints and specified data domains, and collecting relevant data for practitioners who have very few datapoints for their tasks. With GAIA, we achieve promising results on COCO, Objects365, Open Images, Caltech, CityPersons, and UODB which is a collection of datasets including KITTI, VOC, WiderFace, DOTA, Clipart, Comic, and more. Taking COCO as an example, GAIA is able to efficiently produce models covering a wide range of latency from 16ms to 53ms, and yields AP from 38.2 to 46.5 without whistles and bells. To benefit every practitioner in the community of object detection, GAIA is released at https://github.com/GAIA-vision.

</details>

</details>

### You Only Look at One Sequence: Rethinking Transformer in Vision through Object Detection.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/dc912a253d1e9ba40e2c597ed2376640-Abstract.html)
- **作者**: Yuxin Fang, Bencheng Liao, Xinggang Wang, Jiemin Fang, Jiyang Qi, Rui Wu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Object detection is an important computer vision task with plenty of real-world applications; therefore, how to enhance its robustness against adversarial attacks has emerged as a crucial issue. However, most of the previous defense methods focused on the classification task and had few analysis in the context of the object detection task. In this work, to address the issue, we present a novel class-aware robust adversarial training paradigm for the object detection task. For a given image, the proposed approach generates an universal adversarial perturbation to simultaneously attack all the occurred objects in the image through jointly maximizing the respective loss for each object. Meanwhile, instead of normalizing the total loss with the number of objects, the proposed approach decomposes the total loss into class-wise losses and normalizes each class loss using the number of objects for the class. The adversarial training based on the class weighted loss can not only balances the influence of each class but also effectively and evenly improves the adversarial robustness of trained models for all the object classes as compared with the previous defense methods. Furthermore, with the recent development of fast adversarial training, we provide a fast version of the proposed algorithm which can be trained faster than the traditional adversarial training while keeping comparable performance. With extensive experiments on the challenging PASCAL-VOC and MS-COCO datasets, the evaluation results demonstrate that the proposed defense methods can effectively enhance the robustness of the object detection models.

</details>

### Scale-Aware Automatic Augmentation for Object Detection.
- **链接**: [arXiv:2103.17220](https://arxiv.org/abs/2103.17220) · [代码](https://github.com/Jia-Research-Lab/SA-AutoAug) · 📚 被引 49
- **作者**: Yukang Chen, Yanwei Li, Tao Kong, Lu Qi, Ruihang Chu, Lei Li et al.
- **🏷️ 机构**: CUHK / SmartMore
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose Scale-aware AutoAug to learn data augmentation policies for object detection. We define a new scale-aware search space, where both image- and box-level augmentations are designed for maintaining scale invariance. Upon this search space, we propose a new search metric, termed Pareto Scale Balance, to facilitate search with high efficiency. In experiments, Scale-aware AutoAug yields significant and consistent improvement on various object detectors (e.g., RetinaNet, Faster R-CNN, Mask R-CNN, and FCOS), even compared with strong multi-scale training baselines. Our searched augmentation policies are transferable to other datasets and box-level tasks beyond object detection (e.g., instance segmentation and keypoint estimation) to improve performance. The search cost is much less than previous automated augmentation approaches for object detection. It is notable that our searched policies have meaningful patterns, which intuitively provide valuable insight for human data augmentation design. Code and models will be available at https://github.com/Jia-Research-Lab/SA-AutoAug.

</details>

### AQD: Towards Accurate Quantized Object Detection.
- **链接**: [arXiv:2007.06919](https://arxiv.org/abs/2007.06919) · [代码](https://github.com/ziplab/QTool) · 📚 被引 27
- **作者**: Peng Chen, Jing Liu, Bohan Zhuang, Mingkui Tan, Chunhua Shen
- **🏷️ 机构**: ZJU
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Network quantization allows inference to be conducted using low-precision arithmetic for improved inference efficiency of deep neural networks on edge devices. However, designing aggressively low-bit (e.g., 2-bit) quantization schemes on complex tasks, such as object detection, still remains challenging in terms of severe performance degradation and unverifiable efficiency on common hardware. In this paper, we propose an Accurate Quantized object Detection solution, termed AQD, to fully get rid of floating-point computation. To this end, we target using fixed-point operations in all kinds of layers, including the convolutional layers, normalization layers, and skip connections, allowing the inference to be executed using integer-only arithmetic. To demonstrate the improved latency-vs-accuracy trade-off, we apply the proposed methods on RetinaNet and FCOS. In particular, experimental results on MS-COCO dataset show that our AQD achieves comparable or even better performance compared with the full-precision counterpart under extremely low-bit schemes, which is of great practical value. Source code and models are available at: https://github.com/ziplab/QTool

</details>

### Robust and Accurate Object Detection via Adversarial Learning.
- **链接**: [arXiv:2103.13886](https://arxiv.org/abs/2103.13886) · [代码](https://github.com/google/automl) · 📚 被引 60
- **作者**: Xiangning Chen, Cihang Xie, Mingxing Tan, Li Zhang, Cho-Jui Hsieh, Boqing Gong
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Data augmentation has become a de facto component for training high-performance deep image classifiers, but its potential is under-explored for object detection. Noting that most state-of-the-art object detectors benefit from fine-tuning a pre-trained classifier, we first study how the classifiers' gains from various data augmentations transfer to object detection. The results are discouraging; the gains diminish after fine-tuning in terms of either accuracy or robustness. This work instead augments the fine-tuning stage for object detectors by exploring adversarial examples, which can be viewed as a model-dependent data augmentation. Our method dynamically selects the stronger adversarial images sourced from a detector's classification and localization branches and evolves with the detector to ensure the augmentation policy stays current and relevant. This model-dependent augmentation generalizes to different object detectors better than AutoAugment, a model-agnostic augmentation policy searched based on one particular detector. Our approach boosts the performance of state-of-the-art EfficientDets by +1.1 mAP on the COCO object detection benchmark. It also improves the detectors' robustness against natural distortions by +3.8 mAP and against domain shift by +1.3 mAP. Models are available at https://github.com/google/automl/tree/master/efficientdet/Det-AdvProp.md

</details>

### Dynamic Head: Unifying Object Detection Heads With Attentions.
- **链接**: [arXiv:2106.08322](https://arxiv.org/abs/2106.08322) · [代码](https://github.com/microsoft/DynamicHead) · 📚 被引 942
- **作者**: Xiyang Dai, Yinpeng Chen, Bin Xiao, Dongdong Chen, Mengchen Liu, Lu Yuan et al.
- **🏷️ 机构**: Microsoft,Redmond,USA
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The complex nature of combining localization and classification in object detection has resulted in the flourished development of methods. Previous works tried to improve the performance in various object detection heads but failed to present a unified view. In this paper, we present a novel dynamic head framework to unify object detection heads with attentions. By coherently combining multiple self-attention mechanisms between feature levels for scale-awareness, among spatial locations for spatial-awareness, and within output channels for task-awareness, the proposed approach significantly improves the representation ability of object detection heads without any computational overhead. Further experiments demonstrate that the effectiveness and efficiency of the proposed dynamic head on the COCO benchmark. With a standard ResNeXt-101-DCN backbone, we largely improve the performance over popular object detectors and achieve a new state-of-the-art at 54.0 AP. Furthermore, with latest transformer backbone and extra data, we can push current best COCO result to a new record at 60.6 AP. The code will be released at https://github.com/microsoft/DynamicHead.

</details>

### General Instance Distillation for Object Detection.
- **链接**: [arXiv:2103.02340](https://arxiv.org/abs/2103.02340) · 📚 被引 235
- **作者**: Xing Dai, Zeren Jiang, Zhao Wu, Yiping Bao, Zhicheng Wang, Si Liu et al.
- **🏷️ 机构**: MEGVII Technology, BeiHang University
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In recent years, knowledge distillation has been proved to be an effective solution for model compression. This approach can make lightweight student models acquire the knowledge extracted from cumbersome teacher models. However, previous distillation methods of detection have weak generalization for different detection frameworks and rely heavily on ground truth (GT), ignoring the valuable relation information between instances. Thus, we propose a novel distillation method for detection tasks based on discriminative instances without considering the positive or negative distinguished by GT, which is called general instance distillation (GID). Our approach contains a general instance selection module (GISM) to make full use of feature-based, relation-based and response-based knowledge for distillation. Extensive results demonstrate that the student model achieves significant AP improvement and even outperforms the teacher in various detection frameworks. Specifically, RetinaNet with ResNet-50 achieves 39.1% in mAP with GID on COCO dataset, which surpasses the baseline 36.2% by 2.9%, and even better than the ResNet-101 based teacher model with 38.1% AP.

</details>

### Unbiased Mean Teacher for Cross-Domain Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Deng_Unbiased_Mean_Teacher_for_Cross-Domain_Object_Detection_CVPR_2021_paper.html) · 📚 被引 336
- **作者**: Jinhong Deng, Wen Li, Yuhua Chen, Lixin Duan
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Group Collaborative Learning for Co-Salient Object Detection.
- **链接**: [arXiv:2104.01108](https://arxiv.org/abs/2104.01108) · 📚 被引 101
- **作者**: Qi Fan, Deng-Ping Fan, Huazhu Fu, Chi-Keung Tang, Ling Shao, Yu-Wing Tai
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a novel group collaborative learning framework (GCoNet) capable of detecting co-salient objects in real time (16ms), by simultaneously mining consensus representations at group level based on the two necessary criteria: 1) intra-group compactness to better formulate the consistency among co-salient objects by capturing their inherent shared attributes using our novel group affinity module; 2) inter-group separability to effectively suppress the influence of noisy objects on the output by introducing our new group collaborating module conditioning the inconsistent consensus. To learn a better embedding space without extra computational overhead, we explicitly employ auxiliary classification supervision. Extensive experiments on three challenging benchmarks, i.e., CoCA, CoSOD3k, and Cosal2015, demonstrate that our simple GCoNet outperforms 10 cutting-edge models and achieves the new state-of-the-art. We demonstrate this paper's new technical contributions on a number of important downstream computer vision applications including content aware co-segmentation, co-localization based automatic thumbnails, etc.

</details>

### Generalized Few-Shot Object Detection Without Forgetting.
- **链接**: [arXiv:2105.09491](https://arxiv.org/abs/2105.09491) · 📚 被引 166
- **作者**: Zhibo Fan, Yuchen Ma, Zeming Li, Jian Sun
- **🏷️ 机构**: MEGVII
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently few-shot object detection is widely adopted to deal with data-limited situations. While most previous works merely focus on the performance on few-shot categories, we claim that detecting all classes is crucial as test samples may contain any instances in realistic applications, which requires the few-shot detector to learn new concepts without forgetting. Through analysis on transfer learning based methods, some neglected but beneficial properties are utilized to design a simple yet effective few-shot detector, Retentive R-CNN. It consists of Bias-Balanced RPN to debias the pretrained RPN and Re-detector to find few-shot class objects without forgetting previous knowledge. Extensive experiments on few-shot detection benchmarks show that Retentive R-CNN significantly outperforms state-of-the-art methods on overall performance among all settings as it can achieve competitive results on few-shot classes and does not degrade the base class performance at all. Our approach has demonstrated that the long desired never-forgetting learner is available in object detection.

</details>

### OTA: Optimal Transport Assignment for Object Detection.
- **链接**: [arXiv:2103.14259](https://arxiv.org/abs/2103.14259) · [代码](https://github.com/Megvii-BaseDetection/OTA) · 📚 被引 484
- **作者**: Zheng Ge, Songtao Liu, Zeming Li, Osamu Yoshie, Jian Sun
- **🏷️ 机构**: MEGVII
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advances in label assignment in object detection mainly seek to independently define positive/negative training samples for each ground-truth (gt) object. In this paper, we innovatively revisit the label assignment from a global perspective and propose to formulate the assigning procedure as an Optimal Transport (OT) problem -- a well-studied topic in Optimization Theory. Concretely, we define the unit transportation cost between each demander (anchor) and supplier (gt) pair as the weighted summation of their classification and regression losses. After formulation, finding the best assignment solution is converted to solve the optimal transport plan at minimal transportation costs, which can be solved via Sinkhorn-Knopp Iteration. On COCO, a single FCOS-ResNet-50 detector equipped with Optimal Transport Assignment (OTA) can reach 40.7% mAP under 1X scheduler, outperforming all other existing assigning methods. Extensive experiments conducted on COCO and CrowdHuman further validate the effectiveness of our proposed OTA, especially its superiority in crowd scenarios. The code is available at https://github.com/Megvii-BaseDetection/OTA.

</details>

### Depth From Camera Motion and Object Detection.
- **链接**: [arXiv:2103.01468](https://arxiv.org/abs/2103.01468) · 📚 被引 33
- **作者**: Brent A. Griffin, Jason J. Corso
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper addresses the problem of learning to estimate the depth of detected objects given some measurement of camera motion (e.g., from robot kinematics or vehicle odometry). We achieve this by 1) designing a recurrent neural network (DBox) that estimates the depth of objects using a generalized representation of bounding boxes and uncalibrated camera movement and 2) introducing the Object Depth via Motion and Detection Dataset (ODMD). ODMD training data are extensible and configurable, and the ODMD benchmark includes 21,600 examples across four validation and test sets. These sets include mobile robot experiments using an end-effector camera to locate objects from the YCB dataset and examples with perturbations added to camera motion or bounding box data. In addition to the ODMD benchmark, we evaluate DBox in other monocular application domains, achieving state-of-the-art results on existing driving and robotics benchmarks and estimating the depth of objects using a camera phone.

</details>

### Positive-Unlabeled Data Purification in the Wild for Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Guo_Positive-Unlabeled_Data_Purification_in_the_Wild_for_Object_Detection_CVPR_2021_paper.html) · 📚 被引 7
- **作者**: Jianyuan Guo, Kai Han, Han Wu, Chao Zhang, Xinghao Chen, Chunjing Xu et al.
- **🏷️ 机构**: Huawei Technologies,Noah&#x2019;s Ark Lab, University of Sydney,School of Computer Science, Faculty of Engineering, Peking University,Key Lab of Machine Perception (MOE),Dept. of Machine Intelligence
- **会议**: CVPR 2021

### Beyond Bounding-Box: Convex-Hull Feature Adaptation for Oriented and Densely Packed Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Guo_Beyond_Bounding-Box_Convex-Hull_Feature_Adaptation_for_Oriented_and_Densely_Packed_CVPR_2021_paper.html) · 📚 被引 244
- **作者**: Zonghao Guo, Chang Liu, Xiaosong Zhang, Jianbin Jiao, Xiangyang Ji, Qixiang Ye
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### ReDet: A Rotation-Equivariant Detector for Aerial Object Detection.
- **链接**: [arXiv:2103.07733](https://arxiv.org/abs/2103.07733) · 📚 被引 889
- **作者**: Jiaming Han, Jian Ding, Nan Xue, Gui-Song Xia
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Informative and Consistent Correspondence Mining for Cross-Domain Weakly Supervised Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Hou_Informative_and_Consistent_Correspondence_Mining_for_Cross-Domain_Weakly_Supervised_Object_CVPR_2021_paper.html) · 📚 被引 16
- **作者**: Luwei Hou, Yu Zhang, Kui Fu, Jia Li
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Dense Relation Distillation With Context-Aware Aggregation for Few-Shot Object Detection.
- **链接**: [arXiv:2103.17115](https://arxiv.org/abs/2103.17115) · [代码](https://github.com/hzhupku/DCNet) · 📚 被引 192
- **作者**: Hanzhe Hu, Shuai Bai, Aoxue Li, Jinshi Cui, Liwei Wang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Conventional deep learning based methods for object detection require a large amount of bounding box annotations for training, which is expensive to obtain such high quality annotated data. Few-shot object detection, which learns to adapt to novel classes with only a few annotated examples, is very challenging since the fine-grained feature of novel object can be easily overlooked with only a few data available. In this work, aiming to fully exploit features of annotated novel object and capture fine-grained features of query object, we propose Dense Relation Distillation with Context-aware Aggregation (DCNet) to tackle the few-shot detection problem. Built on the meta-learning based framework, Dense Relation Distillation module targets at fully exploiting support features, where support features and query feature are densely matched, covering all spatial locations in a feed-forward fashion. The abundant usage of the guidance information endows model the capability to handle common challenges such as appearance changes and occlusions. Moreover, to better capture scale-aware features, Context-aware Aggregation module adaptively harnesses features from different scales for a more comprehensive feature representation. Extensive experiments illustrate that our proposed approach achieves state-of-the-art results on PASCAL VOC and MS COCO datasets. Code will be made available at https://github.com/hzhupku/DCNet.

</details>

### SAIL-VOS 3D: A Synthetic Dataset and Baselines for Object Detection and 3D Mesh Reconstruction From Video Data.
- **链接**: [arXiv:2105.08612](https://arxiv.org/abs/2105.08612) · 📚 被引 15
- **作者**: Yuan-Ting Hu, Jiahong Wang, Raymond A. Yeh, Alexander G. Schwing
- **🏷️ 机构**: University of Illinois at Urbana-Champaign
- **会议**: CVPR 2021

### Interpolation-Based Semi-Supervised Learning for Object Detection.
- **链接**: [arXiv:2006.02158](https://arxiv.org/abs/2006.02158) · 📚 被引 45
- **作者**: Jisoo Jeong, Vikas Verma, Minsung Hyun, Juho Kannala, Nojun Kwak
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Calibrated RGB-D Salient Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Ji_Calibrated_RGB-D_Salient_Object_Detection_CVPR_2021_paper.html)
- **作者**: Wei Ji, Jingjing Li, Shuang Yu, Miao Zhang, Yongri Piao, Shunyu Yao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Towards Open World Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Joseph_Towards_Open_World_Object_Detection_CVPR_2021_paper.html)
- **作者**: K. J. Joseph, Salman H. Khan, Fahad Shahbaz Khan, Vineeth N. Balasubramanian
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### UniT: Unified Knowledge Transfer for Any-Shot Object Detection and Segmentation.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Khandelwal_UniT_Unified_Knowledge_Transfer_for_Any-Shot_Object_Detection_and_Segmentation_CVPR_2021_paper.html) · 📚 被引 24
- **作者**: Siddhesh Khandelwal, Raghav Goyal, Leonid Sigal
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Transformation Invariant Few-Shot Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Li_Transformation_Invariant_Few-Shot_Object_Detection_CVPR_2021_paper.html) · 📚 被引 88
- **作者**: Aoxue Li, Zhenguo Li
- **🏷️ 机构**: Huawei Noah&#x2019;s Ark Lab,China
- **会议**: CVPR 2021

### Generalized Focal Loss V2: Learning Reliable Localization Quality Estimation for Dense Object Detection.
- **链接**: [arXiv:2011.12885](https://arxiv.org/abs/2011.12885) · [代码](https://github.com/implus/GFocalV2) · 📚 被引 399
- **作者**: Xiang Li, Wenhai Wang, Xiaolin Hu, Jun Li, Jinhui Tang, Jian Yang
- **🏷️ 机构**: Shanghai AI Lab
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Localization Quality Estimation (LQE) is crucial and popular in the recent advancement of dense object detectors since it can provide accurate ranking scores that benefit the Non-Maximum Suppression processing and improve detection performance. As a common practice, most existing methods predict LQE scores through vanilla convolutional features shared with object classification or bounding box regression. In this paper, we explore a completely novel and different perspective to perform LQE -- based on the learned distributions of the four parameters of the bounding box. The bounding box distributions are inspired and introduced as "General Distribution" in GFLV1, which describes the uncertainty of the predicted bounding boxes well. Such a property makes the distribution statistics of a bounding box highly correlated to its real localization quality. Specifically, a bounding box distribution with a sharp peak usually corresponds to high localization quality, and vice versa. By leveraging the close correlation between distribution statistics and the real localization quality, we develop a considerably lightweight Distribution-Guided Quality Predictor (DGQP) for reliable LQE based on GFLV1, thus producing GFLV2. To our best knowledge, it is the first attempt in object detection to use a highly relevant, statistical representation to facilitate LQE. Extensive experiments demonstrate the effectiveness of our method. Notably, GFLV2 (ResNet-101) achieves 46.2 AP at 14.6 FPS, surpassing the previous state-of-the-art ATSS baseline (43.6 AP at 14.6 FPS) by absolute 2.6 AP on COCO {\tt test-dev}, without sacrificing the efficiency both in training and inference. Code will be available at https://github.com/implus/GFocalV2.

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Few-shot object detection has made substantial progressby representing novel class objects using the feature representation learned upon a set of base class objects. However,an implicit contradiction between novel class classification and representation is unfortunately ignored. On the one hand, to achieve accurate novel class classification, the distributions of either two base classes must be far away fromeach other (max-margin). On the other hand, to precisely represent novel classes, the distributions of base classes should be close to each other to reduce the intra-class distance of novel classes (min-margin). In this paper, we propose a class margin equilibrium (CME) approach, with the aim to optimize both feature space partition and novel class reconstruction in a systematic way. CME first converts the few-shot detection problem to the few-shot classification problem by using a fully connected layer to decouple localization features. CME then reserves adequate margin space for novel classes by introducing simple-yet-effective class margin loss during feature learning. Finally, CME pursues margin equilibrium by disturbing the features of novel class instances in an adversarial min-max fashion. Experiments on Pascal VOC and MS-COCO datasets show that CME significantly improves upon two baseline detectors (up to $3\sim 5\%$ in average), achieving state-of-the-art performance. Code is available at https://github.com/Bohao-Lee/CME .

</details>

### Dynamic Context-Sensitive Filtering Network for Video Salient Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00158)
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

### Improved Handling of Motion Blur in Online Object Detection.
- **链接**: [arXiv:2011.14448](https://arxiv.org/abs/2011.14448) · 📚 被引 42
- **作者**: Mohamed Sayed, Gabriel J. Brostow
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We wish to detect specific categories of objects, for online vision systems that will run in the real world. Object detection is already very challenging. It is even harder when the images are blurred, from the camera being in a car or a hand-held phone. Most existing efforts either focused on sharp images, with easy to label ground truth, or they have treated motion blur as one of many generic corruptions. Instead, we focus especially on the details of egomotion induced blur. We explore five classes of remedies, where each targets different potential causes for the performance gap between sharp and blurred images. For example, first deblurring an image changes its human interpretability, but at present, only partly improves object detection. The other four classes of remedies address multi-scale texture, out-of-distribution testing, label generation, and conditioning by blur-type. Surprisingly, we discover that custom label generation aimed at resolving spatial ambiguity, ahead of all others, markedly improves object detection. Also, in contrast to findings from classification, we see a noteworthy boost by conditioning our model on bespoke categories of motion blur. We validate and cross-breed the different remedies experimentally on blurred COCO images and real-world blur datasets, producing an easy and practical favorite model with superior detection rates.

</details>

### FSCE: Few-Shot Object Detection via Contrastive Proposal Encoding.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Sun_FSCE_Few-Shot_Object_Detection_via_Contrastive_Proposal_Encoding_CVPR_2021_paper.html) · 📚 被引 505
- **作者**: Bo Sun, Banghuai Li, Shengcai Cai, Ye Yuan, Chi Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Sparse R-CNN: End-to-End Object Detection With Learnable Proposals.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Sun_Sparse_R-CNN_End-to-End_Object_Detection_With_Learnable_Proposals_CVPR_2021_paper.html) · 📚 被引 1310
- **作者**: Peize Sun, Rufeng Zhang, Yi Jiang, Tao Kong, Chenfeng Xu, Wei Zhan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Equalization Loss v2: A New Gradient Balance Approach for Long-Tailed Object Detection.
- **链接**: [arXiv:2012.08548](https://arxiv.org/abs/2012.08548) · [代码](https://github.com/tztztztztz/eqlv2) · 📚 被引 179
- **作者**: Jingru Tan, Xin Lu, Gang Zhang, Changqing Yin, Quanquan Li
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently proposed decoupled training methods emerge as a dominant paradigm for long-tailed object detection. But they require an extra fine-tuning stage, and the disjointed optimization of representation and classifier might lead to suboptimal results. However, end-to-end training methods, like equalization loss (EQL), still perform worse than decoupled training methods. In this paper, we reveal the main issue in long-tailed object detection is the imbalanced gradients between positives and negatives, and find that EQL does not solve it well. To address the problem of imbalanced gradients, we introduce a new version of equalization loss, called equalization loss v2 (EQL v2), a novel gradient guided reweighing mechanism that re-balances the training process for each category independently and equally. Extensive experiments are performed on the challenging LVIS benchmark. EQL v2 outperforms origin EQL by about 4 points overall AP with 14-18 points improvements on the rare categories. More importantly, it also surpasses decoupled training methods. Without further tuning for the Open Images dataset, EQL v2 improves EQL by 7.3 points AP, showing strong generalization ability. Codes have been released at https://github.com/tztztztztz/eqlv2

</details>

### Humble Teachers Teach Better Students for Semi-Supervised Object Detection.
- **链接**: [arXiv:2106.10456](https://arxiv.org/abs/2106.10456) · 📚 被引 180
- **作者**: Yihe Tang, Weifeng Chen, Yijun Luo, Yuting Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose a semi-supervised approach for contemporary object detectors following the teacher-student dual model framework. Our method is featured with 1) the exponential moving averaging strategy to update the teacher from the student online, 2) using plenty of region proposals and soft pseudo-labels as the student's training targets, and 3) a light-weighted detection-specific data ensemble for the teacher to generate more reliable pseudo-labels. Compared to the recent state-of-the-art -- STAC, which uses hard labels on sparsely selected hard pseudo samples, the teacher in our model exposes richer information to the student with soft-labels on many proposals. Our model achieves COCO-style AP of 53.04% on VOC07 val set, 8.4% better than STAC, when using VOC12 as unlabeled data. On MS-COCO, it outperforms prior work when only a small percentage of data is taken as labeled. It also reaches 53.8% AP on MS-COCO test-dev with 3.1% gain over the fully supervised ResNet-152 Cascaded R-CNN, by tapping into unlabeled data of a similar size to the labeled data.

</details>

### Unsupervised Object Detection With LIDAR Clues.
- **链接**: [arXiv:2011.12953](https://arxiv.org/abs/2011.12953) · 📚 被引 26
- **作者**: Hao Tian, Yuntao Chen, Jifeng Dai, Zhaoxiang Zhang, Xizhou Zhu
- **🏷️ 机构**: Tsinghua / Shanghai AI Lab
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite the importance of unsupervised object detection, to the best of our knowledge, there is no previous work addressing this problem. One main issue, widely known to the community, is that object boundaries derived only from 2D image appearance are ambiguous and unreliable. To address this, we exploit LiDAR clues to aid unsupervised object detection. By exploiting the 3D scene structure, the issue of localization can be considerably mitigated. We further identify another major issue, seldom noticed by the community, that the long-tailed and open-ended (sub-)category distribution should be accommodated. In this paper, we present the first practical method for unsupervised object detection with the aid of LiDAR clues. In our approach, candidate object segments based on 3D point clouds are firstly generated. Then, an iterative segment labeling process is conducted to assign segment labels and to train a segment labeling network, which is based on features from both 2D images and 3D point clouds. The labeling process is carefully designed so as to mitigate the issue of long-tailed and open-ended distribution. The final segment labels are set as pseudo annotations for object detection network training. Extensive experiments on the large-scale Waymo Open dataset suggest that the derived unsupervised object detection method achieves reasonable accuracy compared with that of strong supervision within the LiDAR visible range. Code shall be released.

</details>

### MeGA-CDA: Memory Guided Attention for Category-Aware Unsupervised Domain Adaptive Object Detection.
- **链接**: [arXiv:2103.04224](https://arxiv.org/abs/2103.04224) · 📚 被引 160
- **作者**: Vibashan VS, Vikram Gupta, Poojan Oza, Vishwanath A. Sindagi, Vishal M. Patel
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing approaches for unsupervised domain adaptive object detection perform feature alignment via adversarial training. While these methods achieve reasonable improvements in performance, they typically perform category-agnostic domain alignment, thereby resulting in negative transfer of features. To overcome this issue, in this work, we attempt to incorporate category information into the domain adaptation process by proposing Memory Guided Attention for Category-Aware Domain Adaptation (MeGA-CDA). The proposed method consists of employing category-wise discriminators to ensure category-aware feature alignment for learning domain-invariant discriminative features. However, since the category information is not available for the target samples, we propose to generate memory-guided category-specific attention maps which are then used to route the features appropriately to the corresponding category discriminator. The proposed method is evaluated on several benchmark datasets and is shown to outperform existing approaches.

</details>

### Data-Uncertainty Guided Multi-Phase Learning for Semi-Supervised Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Wang_Data-Uncertainty_Guided_Multi-Phase_Learning_for_Semi-Supervised_Object_Detection_CVPR_2021_paper.html) · 📚 被引 83
- **作者**: Zhenyu Wang, Yali Li, Ye Guo, Lu Fang, Shengjin Wang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### End-to-End Object Detection With Fully Convolutional Network.
- **链接**: [arXiv:2012.03544](https://arxiv.org/abs/2012.03544) · [代码](https://github.com/Megvii-BaseDetection/DeFCN)
- **作者**: Jianfeng Wang, Lin Song, Zeming Li, Hongbin Sun, Jian Sun, Nanning Zheng
- **🏷️ 机构**: MEGVII, XJTU
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Mainstream object detectors based on the fully convolutional network has achieved impressive performance. While most of them still need a hand-designed non-maximum suppression (NMS) post-processing, which impedes fully end-to-end training. In this paper, we give the analysis of discarding NMS, where the results reveal that a proper label assignment plays a crucial role. To this end, for fully convolutional detectors, we introduce a Prediction-aware One-To-One (POTO) label assignment for classification to enable end-to-end detection, which obtains comparable performance with NMS. Besides, a simple 3D Max Filtering (3DMF) is proposed to utilize the multi-scale features and improve the discriminability of convolutions in the local region. With these techniques, our end-to-end framework achieves competitive performance against many state-of-the-art detectors with NMS on COCO and CrowdHuman datasets. The code is available at https://github.com/Megvii-BaseDetection/DeFCN .

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
