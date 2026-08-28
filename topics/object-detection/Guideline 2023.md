# Object Detection — 2023 Guideline

> 领域: 通用 2D 目标检测（检测器架构、密集预测、小物体/旋转框/NMS 等）
> 论文数: 95 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Semi-DETR: Semi-Supervised Object Detection with Detection Transformers.
- **链接**: [arXiv:2307.08095](https://arxiv.org/abs/2307.08095) · [代码](https://github.com/PaddlePaddle/PaddleDetection) · 📚 被引 78
- **作者**: Jiacheng Zhang, Xiangru Lin, Wei Zhang, Kuo Wang, Xiao Tan, Junyu Han et al.
- **🏷️ 机构**: School of Computer Science and Engineering, Sun Yat-sen University,Guangzhou,China, Baidu Inc.,Department of Computer Vision Technology (VIS),China
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We analyze the DETR-based framework on semi-supervised object detection (SSOD) and observe that (1) the one-to-one assignment strategy generates incorrect matching when the pseudo ground-truth bounding box is inaccurate, leading to training inefficiency; (2) DETR-based detectors lack deterministic correspondence between the input query and its prediction output, which hinders the applicability of the consistency-based regularization widely used in current SSOD methods. We present Semi-DETR, the first transformer-based end-to-end semi-supervised object detector, to tackle these problems. Specifically, we propose a Stage-wise Hybrid Matching strategy that combines the one-to-many assignment and one-to-one assignment strategies to improve the training efficiency of the first stage and thus provide high-quality pseudo labels for the training of the second stage. Besides, we introduce a Crossview Query Consistency method to learn the semantic feature invariance of object queries from different views while avoiding the need to find deterministic query correspondence. Furthermore, we propose a Cost-based Pseudo Label Mining module to dynamically mine more pseudo boxes based on the matching cost of pseudo ground truth bounding boxes for consistency training. Extensive experiments on all SSOD settings of both COCO and Pascal VOC benchmark datasets show that our Semi-DETR method outperforms all state-of-the-art methods by clear margins. The PaddlePaddle version code1 is at https://github.com/PaddlePaddle/PaddleDetection/tree/develop/configs/semi_det/semi_detr.

</details>

### Mask DINO: Towards A Unified Transformer-based Framework for Object Detection and Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00297)
- **作者**: Feng Li, Hao Zhang, Huaizhe Xu, Shilong Liu, Lei Zhang, Lionel M. Ni et al.
- **🏷️ 机构**: PolyU / OPPO
- **会议**: CVPR 2023

### DETR with Additional Global Aggregation for Cross-domain Weakly Supervised Object Detection.
- **链接**: [arXiv:2304.07082](https://arxiv.org/abs/2304.07082) · 📚 被引 15
- **作者**: Zongheng Tang, Yifan Sun, Si Liu, Yi Yang
- **🏷️ 机构**: Institute of Artificial Intelligence, Beihang University, Baidu Inc, CCAI, Zhejiang University
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper presents a DETR-based method for cross-domain weakly supervised object detection (CDWSOD), aiming at adapting the detector from source to target domain through weak supervision. We think DETR has strong potential for CDWSOD due to an insight: the encoder and the decoder in DETR are both based on the attention mechanism and are thus capable of aggregating semantics across the entire image. The aggregation results, i.e., image-level predictions, can naturally exploit the weak supervision for domain alignment. Such motivated, we propose DETR with additional Global Aggregation (DETR-GA), a CDWSOD detector that simultaneously makes "instance-level + image-level" predictions and utilizes "strong + weak" supervisions. The key point of DETR-GA is very simple: for the encoder / decoder, we respectively add multiple class queries / a foreground query to aggregate the semantics into image-level predictions. Our query-based aggregation has two advantages. First, in the encoder, the weakly-supervised class queries are capable of roughly locating the corresponding positions and excluding the distraction from non-relevant regions. Second, through our design, the object queries and the foreground query in the decoder share consensus on the class semantics, therefore making the strong and weak supervision mutually benefit each other for domain alignment. Extensive experiments on four popular cross-domain benchmarks show that DETR-GA significantly improves CSWSOD and advances the states of the art (e.g., 29.0% --> 79.4% mAP on PASCAL VOC --> Clipart_all dataset).

</details>

### Toward RAW Object Detection: A New Benchmark and A New Model.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01286) · 📚 被引 31
- **作者**: Ruikang Xu, Chang Chen, Jingyang Peng, Cheng Li, Yibin Huang, Fenglong Song et al.
- **🏷️ 机构**: University of Science and Technology of China, Huawei Noah&#x0027;s Ark Lab
- **会议**: CVPR 2023

### Object-Aware Distillation Pyramid for Open-Vocabulary Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01076)
- **作者**: Luting Wang, Yi Liu, Penghui Du, Zihan Ding, Yue Liao, Qiaosong Qi et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### OmniLabel: A Challenging Benchmark for Language-Based Object Detection.
- **链接**: [arXiv:2304.11463](https://arxiv.org/abs/2304.11463) · 📚 被引 12
- **作者**: Samuel Schulter, Vijay Kumar B. G, Yumin Suh, Konstantinos M. Dafnis, Zhixing Zhang, Shiyu Zhao et al.
- **🏷️ 机构**: NEC Laboratories America, Rutgers University
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Incremental object detection (IOD) aims to train an object detector in phases, each with annotations for new object categories. As other incremental settings, IOD is subject to catastrophic forgetting, which is often addressed by techniques such as knowledge distillation (KD) and exemplar replay (ER). However, KD and ER do not work well if applied directly to state-of-the-art transformer-based object detectors such as Deformable DETR and UP-DETR. In this paper, we solve these issues by proposing a ContinuaL DEtection TRansformer (CL-DETR), a new method for transformer-based IOD which enables effective usage of KD and ER in this context. First, we introduce a Detector Knowledge Distillation (DKD) loss, focusing on the most informative and reliable predictions from old versions of the model, ignoring redundant background predictions, and ensuring compatibility with the available ground-truth labels. We also improve ER by proposing a calibration strategy to preserve the label distribution of the training set, therefore better matching training and testing statistics. We conduct extensive experiments on COCO 2017 and demonstrate that CL-DETR achieves state-of-the-art results in the IOD setting.

</details>

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We explore long-term temporal visual correspondence-based optimization for 3D video object detection in this work. Visual correspondence refers to one-to-one mappings for pixels across multiple images. Correspondence-based optimization is the cornerstone for 3D scene reconstruction but is less studied in 3D video object detection, because moving objects violate multi-view geometry constraints and are treated as outliers during scene reconstruction. We address this issue by treating objects as first-class citizens during correspondence-based optimization. In this work, we propose BA-Det, an end-to-end optimizable object detector with object-centric temporal correspondence learning and featuremetric object bundle adjustment. Empirically, we verify the effectiveness and efficiency of BA-Det for multiple baseline 3D detectors under various setups. Our BA-Det achieves SOTA performance on the large-scale Waymo Open Dataset (WOD) with only marginal computation cost. Our code is available at https://github.com/jiaweihe1996/BA-Det.

</details>

> Object localization in general environments is a fundamental part of vision systems. While dominating on the COCO benchmark, recent Transformer-based detection methods are not competitive in diverse domains. Moreover, these methods still struggle to very accurately estimate the object bounding boxes in complex environments. We introduce Cascade-DETR for high-quality universal object detection. We jointly tackle the generalization to diverse domains and localization accuracy by proposing the Cascade Attention layer, which explicitly integrates object-centric information into the detection decoder by limiting the attention to the previous box prediction. To further enhance accuracy, we also revisit the scoring of queries. Instead of relying on classification scores, we predict the expected IoU of the query, leading to substantially more well-calibrated confidences. Lastly, we introduce a universal object detection benchmark, UDB10, that contains 10 datasets from diverse domains. While also advancing the state-of-the-art on COCO, Cascade-DETR substantially improves DETR-based detectors on all datasets in UDB10, even by over 10 mAP in some cases. The improvements under stringent quality requirements are even more pronounced. Our code and models will be released at https://github.com/SysCV/cascade-detr.

</details>

### Decoupled DETR: Spatially Disentangling Localization and Classification for Improved End-to-End Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00607) · 📚 被引 28
- **作者**: Manyuan Zhang, Guanglu Song, Yu Liu, Hongsheng Li
- **🏷️ 机构**: The Chinese University of HongKong,Multimedia Laboratory, SenseTime Research
- **会议**: ICCV 2023

### T-FFTRadNet: Object Detection with Swin Vision Transformers from Raw ADC Radar Signals.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00435)
- **作者**: James Giroux, Martin Bouchard, Robert Laganière
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### DETRDistill: A Universal Knowledge Distillation Framework for DETR-families.
- **链接**: [arXiv:2211.10156](https://arxiv.org/abs/2211.10156) · 📚 被引 39
- **作者**: Jiahao Chang, Shuo Wang, Hai-Ming Xu, Zehui Chen, Chenhongyi Yang, Feng Zhao
- **🏷️ 机构**: University of Science and Technology of China, University of Adelaide, University of Edinburgh
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Transformer-based detectors (DETRs) are becoming popular for their simple framework, but the large model size and heavy time consumption hinder their deployment in the real world. While knowledge distillation (KD) can be an appealing technique to compress giant detectors into small ones for comparable detection performance and low inference cost. Since DETRs formulate object detection as a set prediction problem, existing KD methods designed for classic convolution-based detectors may not be directly applicable. In this paper, we propose DETRDistill, a novel knowledge distillation method dedicated to DETR-families. Specifically, we first design a Hungarian-matching logits distillation to encourage the student model to have the exact predictions as that of teacher DETRs. Next, we propose a target-aware feature distillation to help the student model learn from the object-centric features of the teacher model. Finally, in order to improve the convergence rate of the student DETR, we introduce a query-prior assignment distillation to speed up the student model learning from well-trained queries and stable assignment of the teacher model. Extensive experimental results on the COCO dataset validate the effectiveness of our approach. Notably, DETRDistill consistently improves various DETRs by more than 2.0 mAP, even surpassing their teacher models.

</details>

### Objects do not disappear: Video object detection by single-frame object location anticipation.
- **链接**: [arXiv:2308.04770](https://arxiv.org/abs/2308.04770) · [代码](https://github.com/L-KID/Videoobject-detection-by-location-anticipation) · 📚 被引 11
- **作者**: Xin Liu, Fatemeh Karimi Nejadasl, Jan C. van Gemert, Olaf Booij, Silvia L. Pintea
- **🏷️ 机构**: Delft University of Technology,Computer Vision Lab, University of Amsterdam,Institute for Biodiversity and Ecosystem Dynamics
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Objects in videos are typically characterized by continuous smooth motion. We exploit continuous smooth motion in three ways. 1) Improved accuracy by using object motion as an additional source of supervision, which we obtain by anticipating object locations from a static keyframe. 2) Improved efficiency by only doing the expensive feature computations on a small subset of all frames. Because neighboring video frames are often redundant, we only compute features for a single static keyframe and predict object locations in subsequent frames. 3) Reduced annotation cost, where we only annotate the keyframe and use smooth pseudo-motion between keyframes. We demonstrate computational efficiency, annotation efficiency, and improved mean average precision compared to the state-of-the-art on four datasets: ImageNet VID, EPIC KITCHENS-55, YouTube-BoundingBoxes, and Waymo Open dataset. Our source code is available at https://github.com/L-KID/Videoobject-detection-by-location-anticipation.

</details>

### Self-Supervised Object Detection from Egocentric Videos.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00482)
- **作者**: Peri Akiva, Jing Huang, Kevin J. Liang, Rama Kovvuri, Xingyu Chen, Matt Feiszli et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### DiffusionDet: Diffusion Model for Object Detection.
- **链接**: [arXiv:2211.09788](https://arxiv.org/abs/2211.09788) · [代码](https://github.com/ShoufaChen/DiffusionDet) · 📚 被引 560
- **作者**: Shoufa Chen, Peize Sun, Yibing Song, Ping Luo
- **🏷️ 机构**: The University of Hong Kong, Tencent AI Lab
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Combining multiple datasets enables performance boost on many computer vision tasks. But similar trend has not been witnessed in object detection when combining multiple datasets due to two inconsistencies among detection datasets: taxonomy difference and domain gap. In this paper, we address these challenges by a new design (named Detection Hub) that is dataset-aware and category-aligned. It not only mitigates the dataset inconsistency but also provides coherent guidance for the detector to learn across multiple datasets. In particular, the dataset-aware design is achieved by learning a dataset embedding that is used to adapt object queries as well as convolutional kernels in detection heads. The categories across datasets are semantically aligned into a unified space by replacing one-hot category representations with word embedding and leveraging the semantic coherence of language embedding. Detection Hub fulfills the benefits of large data on object detection. Experiments demonstrate that joint training on multiple datasets achieves significant performance gains over training on each dataset alone. Detection Hub further achieves SoTA performance on UODB benchmark with wide variety of datasets.

</details>

</details>

### Identity-Consistent Aggregation for Video Object Detection.
- **链接**: [arXiv:2308.07737](https://arxiv.org/abs/2308.07737) · 📚 被引 10
- **作者**: Chaorui Deng, Da Chen, Qi Wu
- **🏷️ 机构**: University of Adelaide,Australia Institute of Machine Learning, University of Bath,Department of Computer Science
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper explores the potential of curriculum learning in LiDAR-based 3D object detection by proposing a curricular object manipulation (COM) framework. The framework embeds the curricular training strategy into both the loss design and the augmentation process. For the loss design, we propose the COMLoss to dynamically predict object-level difficulties and emphasize objects of different difficulties based on training stages. On top of the widely-used augmentation technique called GT-Aug in LiDAR detection tasks, we propose a novel COMAug strategy which first clusters objects in ground-truth database based on well-designed heuristics. Group-level difficulties rather than individual ones are then predicted and updated during training for stable results. Model performance and generalization capabilities can be improved by sampling and augmenting progressively more difficult objects into the training samples. Extensive experiments and ablation studies reveal the superior and generality of the proposed framework. The code is available at https://github.com/ZZY816/COM.

</details>

</details>

### Boosting Long-tailed Object Detection via Step-wise Learning on Smooth-tail Data.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00639) · 📚 被引 5
- **作者**: Na Dong, Yongqiang Zhang, Mingli Ding, Gim Hee Lee
- **🏷️ 机构**: National University of Singapore,Department of Computer Science, Harbin Institute of Technology,School of Instrument Science and Engineering
- **会议**: ICCV 2023

### σ-Adaptive Decoupled Prototype for Few-Shot Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01737) · 📚 被引 19
- **作者**: Jinhao Du, Shan Zhang, Qiang Chen, Haifeng Le, Yanpeng Sun, Yao Ni et al.
- **🏷️ 机构**: Baidu VIS, Australian National University, Beijing Union University
- **会议**: ICCV 2023

### Normalizing Flow based Feature Synthesis for Outlier-Aware Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00499) · 📚 被引 14
- **作者**: Nishant Kumar, Sinisa Segvic, Abouzar Eslami, Stefan Gumhold
- **🏷️ 机构**: TU Dresden, University of Zagreb - FER, Carl Zeiss Meditec AG
- **会议**: CVPR 2023

### Cut and Learn for Unsupervised Object Detection and Instance Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00305) · 📚 被引 182
- **作者**: Xudong Wang, Rohit Girdhar, Stella X. Yu, Ishan Misra
- **🏷️ 机构**: FAIR, Meta AI, UC Berkeley / ICSI
- **会议**: CVPR 2023

### Phase-Shifting Coder: Predicting Accurate Orientation in Oriented Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01283) · 📚 被引 173
- **作者**: Yi Yu, Feipeng Da
- **🏷️ 机构**: School of Automation, Southeast University,Nanjing,China
- **会议**: CVPR 2023

### Enhanced Training of Query-Based Object Detection via Selective Query Recollection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02275) · 📚 被引 64
- **作者**: Fangyi Chen, Han Zhang, Kai Hu, Yu-Kai Huang, Chenchen Zhu, Marios Savvides
- **🏷️ 机构**: Carnegie Mellon University, Meta AI
- **会议**: CVPR 2023

### STDLens: Model Hijacking-Resilient Federated Learning for Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01568) · 📚 被引 13
- **作者**: Ka-Ho Chow, Ling Liu, Wenqi Wei, Fatih Ilhan, Yanzhao Wu
- **🏷️ 机构**: Georgia Instutite of Technology,Atlanta,GA,USA
- **会议**: CVPR 2023

### What Can Human Sketches Do for Object Detection?
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01448) · 📚 被引 41
- **作者**: Pinaki Nath Chowdhury, Ayan Kumar Bhunia, Aneeshan Sain, Subhadeep Koley, Tao Xiang, Yi-Zhe Song
- **🏷️ 机构**: SketchX, CVSSP, University of Surrey,United Kingdom
- **会议**: CVPR 2023

### The Differentiable Lens: Compound Lens Search over Glass Surfaces and Materials for Object Detection.
- **链接**: [arXiv:2212.04441](https://arxiv.org/abs/2212.04441) · 📚 被引 18
- **作者**: Geoffroi Côté, Fahim Mannan, Simon Thibault, Jean-François Lalonde, Felix Heide
- **🏷️ 机构**: Universit&#x00E9; Laval, Algolux, Princeton University
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Most camera lens systems are designed in isolation, separately from downstream computer vision methods. Recently, joint optimization approaches that design lenses alongside other components of the image acquisition and processing pipeline -- notably, downstream neural networks -- have achieved improved imaging quality or better performance on vision tasks. However, these existing methods optimize only a subset of lens parameters and cannot optimize glass materials given their categorical nature. In this work, we develop a differentiable spherical lens simulation model that accurately captures geometrical aberrations. We propose an optimization strategy to address the challenges of lens design -- notorious for non-convex loss function landscapes and many manufacturing constraints -- that are exacerbated in joint optimization tasks. Specifically, we introduce quantized continuous glass variables to facilitate the optimization and selection of glass materials in an end-to-end design context, and couple this with carefully designed constraints to support manufacturability. In automotive object detection, we report improved detection performance over existing designs even when simplifying designs to two- or three-element lenses, despite significantly degrading the image quality.

</details>

### Meta-Tuning Loss Functions and Data Augmentation for Few-Shot Object Detection.
- **链接**: [arXiv:2304.12161](https://arxiv.org/abs/2304.12161) · 📚 被引 32
- **作者**: Berkan Demirel, Orhun Bugra Baran, Ramazan Gokberk Cinbis
- **🏷️ 机构**: Middle East Technical University
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Few-shot object detection, the problem of modelling novel object detection categories with few training instances, is an emerging topic in the area of few-shot learning and object detection. Contemporary techniques can be divided into two groups: fine-tuning based and meta-learning based approaches. While meta-learning approaches aim to learn dedicated meta-models for mapping samples to novel class models, fine-tuning approaches tackle few-shot detection in a simpler manner, by adapting the detection model to novel classes through gradient based optimization. Despite their simplicity, fine-tuning based approaches typically yield competitive detection results. Based on this observation, we focus on the role of loss functions and augmentations as the force driving the fine-tuning process, and propose to tune their dynamics through meta-learning principles. The proposed training scheme, therefore, allows learning inductive biases that can boost few-shot detection, while keeping the advantages of fine-tuning based approaches. In addition, the proposed approach yields interpretable loss functions, as opposed to highly parametric and complex few-shot meta-models. The experimental results highlight the merits of the proposed scheme, with significant improvements over the strong fine-tuning based few-shot detection baselines on benchmark Pascal VOC and MS-COCO datasets, in terms of both standard and generalized few-shot performance metrics.

</details>

### Harmonious Teacher for Cross-Domain Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02282) · 📚 被引 71
- **作者**: Jinhong Deng, Dongli Xu, Wen Li, Lixin Duan
- **🏷️ 机构**: University of Electronic Science and Technology of China, University of Sydney, Shenzhen Institute for Advanced Study, UESTC
- **会议**: CVPR 2023

### Adaptive Sparse Convolutional Networks with Global Context Enhancement for Faster Object Detection on Drone Images.
- **链接**: [arXiv:2303.14488](https://arxiv.org/abs/2303.14488) · 📚 被引 238
- **作者**: Bowei Du, Yecheng Huang, Jiaxin Chen, Di Huang
- **🏷️ 机构**: Beihang University,State Key Laboratory of Software Development Environment,Beijing,China, School of Computer Science and Engineering, Beihang University,Beijing,China
- **会议**: CVPR 2023

### Weak-shot Object Detection through Mutual Knowledge Transfer.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01884) · 📚 被引 1
- **作者**: Xuanyi Du, Weitao Wan, Chong Sun, Chen Li
- **🏷️ 机构**: WeChat, Tencent
- **会议**: CVPR 2023

### AsyFOD: An Asymmetric Adaptation Paradigm for Few-Shot Domain Adaptive Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00318) · 📚 被引 30
- **作者**: Yipeng Gao, Kun-Yu Lin, Junkai Yan, Yaowei Wang, Wei-Shi Zheng
- **🏷️ 机构**: School of Computer Science and Engineering, Sun Yat-sen University,China, Pengcheng Lab
- **会议**: CVPR 2023

### Recurrent Vision Transformers for Object Detection with Event Cameras.
- **链接**: [arXiv:2212.05598](https://arxiv.org/abs/2212.05598) · 📚 被引 188
- **作者**: Mathias Gehrig, Davide Scaramuzza
- **🏷️ 机构**: Robotics and Perception Group, University of Zurich,Switzerland
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present Recurrent Vision Transformers (RVTs), a novel backbone for object detection with event cameras. Event cameras provide visual information with sub-millisecond latency at a high-dynamic range and with strong robustness against motion blur. These unique properties offer great potential for low-latency object detection and tracking in time-critical scenarios. Prior work in event-based vision has achieved outstanding detection performance but at the cost of substantial inference time, typically beyond 40 milliseconds. By revisiting the high-level design of recurrent vision backbones, we reduce inference time by a factor of 6 while retaining similar performance. To achieve this, we explore a multi-stage design that utilizes three key concepts in each stage: First, a convolutional prior that can be regarded as a conditional positional embedding. Second, local and dilated global self-attention for spatial feature interaction. Third, recurrent temporal feature aggregation to minimize latency while retaining temporal information. RVTs can be trained from scratch to reach state-of-the-art performance on event-based object detection - achieving an mAP of 47.2% on the Gen1 automotive dataset. At the same time, RVTs offer fast inference (<12 ms on a T4 GPU) and favorable parameter efficiency (5 times fewer than prior art). Our study brings new insights into effective design choices that can be fruitful for research beyond event-based vision.

</details>

### Learned Two-Plane Perspective Prior based Image Resampling for Efficient Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01284) · 📚 被引 6
- **作者**: Anurag Ghosh, N. Dinesh Reddy, Christoph Mertz, Srinivasa G. Narasimhan
- **🏷️ 机构**: Carnegie Mellon University
- **会议**: CVPR 2023

### NIFF: Alleviating Forgetting in Generalized Few-Shot Object Detection via Neural Instance Feature Forging.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02317) · 📚 被引 23
- **作者**: Karim Guirguis, Johannes Meier, George Eskandar, Matthias Kayser, Bin Yang, Jürgen Beyerer
- **🏷️ 机构**: Robert Bosch GmbH, University of Stuttgart, Karlsruhe Institute of Technology
- **会议**: CVPR 2023

### Camouflaged Object Detection with Feature Decomposition and Edge Reconstruction.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02111) · 📚 被引 364
- **作者**: Chunming He, Kai Li, Yachao Zhang, Longxiang Tang, Yulun Zhang, Zhenhua Guo et al.
- **🏷️ 机构**: Shenzhen International Graduate School, Tsinghua University, NEC Laboratories America, ETH Z&#x00FC;rich
- **会议**: CVPR 2023

### NeRF-RPN: A general framework for object detection in NeRFs.
- **链接**: [arXiv:2211.11646](https://arxiv.org/abs/2211.11646) · [代码](https://github.com/lyclyc52/NeRF_RPN) · 📚 被引 54
- **作者**: Benran Hu, Junkai Huang, Yichen Liu, Yu-Wing Tai, Chi-Keung Tang
- **🏷️ 机构**: The Hong Kong University of Science and Technology
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper presents the first significant object detection framework, NeRF-RPN, which directly operates on NeRF. Given a pre-trained NeRF model, NeRF-RPN aims to detect all bounding boxes of objects in a scene. By exploiting a novel voxel representation that incorporates multi-scale 3D neural volumetric features, we demonstrate it is possible to regress the 3D bounding boxes of objects in NeRF directly without rendering the NeRF at any viewpoint. NeRF-RPN is a general framework and can be applied to detect objects without class labels. We experimented NeRF-RPN with various backbone architectures, RPN head designs and loss functions. All of them can be trained in an end-to-end manner to estimate high quality 3D bounding boxes. To facilitate future research in object detection for NeRF, we built a new benchmark dataset which consists of both synthetic and real-world data with careful labeling and clean up. Code and dataset are available at https://github.com/lyclyc52/NeRF_RPN.

</details>

### SOOD: Towards Semi-Supervised Oriented Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01493) · 📚 被引 70
- **作者**: Wei Hua, Dingkang Liang, Jingyu Li, Xiaolong Liu, Zhikang Zou, Xiaoqing Ye et al.
- **🏷️ 机构**: Huazhong University of Science and Technology, Baidu Inc.,China
- **会议**: CVPR 2023

### T-SEA: Transfer-Based Self-Ensemble Attack on Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01965) · 📚 被引 72
- **作者**: Hao Huang, Ziyan Chen, Huanran Chen, Yongtao Wang, Kevin Zhang
- **🏷️ 机构**: Peking University,Beijing,China
- **会议**: CVPR 2023

### Feature Shrinkage Pyramid for Camouflaged Object Detection with Transformers.
- **链接**: [arXiv:2303.14816](https://arxiv.org/abs/2303.14816) · [代码](https://github.com/ZhouHuang23/FSPNet) · 📚 被引 273
- **作者**: Zhou Huang, Hang Dai, Tian-Zhu Xiang, Shuo Wang, Huai-Xin Chen, Jie Qin et al.
- **🏷️ 机构**: Sichuan Changhong Electric Co., Ltd, University of Glasgow, G42
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision transformers have recently shown strong global context modeling capabilities in camouflaged object detection. However, they suffer from two major limitations: less effective locality modeling and insufficient feature aggregation in decoders, which are not conducive to camouflaged object detection that explores subtle cues from indistinguishable backgrounds. To address these issues, in this paper, we propose a novel transformer-based Feature Shrinkage Pyramid Network (FSPNet), which aims to hierarchically decode locality-enhanced neighboring transformer features through progressive shrinking for camouflaged object detection. Specifically, we propose a nonlocal token enhancement module (NL-TEM) that employs the non-local mechanism to interact neighboring tokens and explore graph-based high-order relations within tokens to enhance local representations of transformers. Moreover, we design a feature shrinkage decoder (FSD) with adjacent interaction modules (AIM), which progressively aggregates adjacent transformer features through a layer-bylayer shrinkage pyramid to accumulate imperceptible but effective cues as much as possible for object information decoding. Extensive quantitative and qualitative experiments demonstrate that the proposed model significantly outperforms the existing 24 competitors on three challenging COD benchmark datasets under six widely-used evaluation metrics. Our code is publicly available at https://github.com/ZhouHuang23/FSPNet.

</details>

### 2PCNet: Two-Phase Consistency Training for Day-to-Night Unsupervised Domain Adaptive Object Detection.
- **链接**: [arXiv:2303.13853](https://arxiv.org/abs/2303.13853) · 📚 被引 73
- **作者**: Mikhail Kennerley, Jian-Gang Wang, Bharadwaj Veeravalli, Robby T. Tan
- **🏷️ 机构**: National University of Singapore,Department of Electrical and Computer Engineering, Institute for Infocomm Research, A*STAR
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Object detection at night is a challenging problem due to the absence of night image annotations. Despite several domain adaptation methods, achieving high-precision results remains an issue. False-positive error propagation is still observed in methods using the well-established student-teacher framework, particularly for small-scale and low-light objects. This paper proposes a two-phase consistency unsupervised domain adaptation network, 2PCNet, to address these issues. The network employs high-confidence bounding-box predictions from the teacher in the first phase and appends them to the student's region proposals for the teacher to re-evaluate in the second phase, resulting in a combination of high and low confidence pseudo-labels. The night images and pseudo-labels are scaled-down before being used as input to the student, providing stronger small-scale pseudo-labels. To address errors that arise from low-light regions and other night-related attributes in images, we propose a night-specific augmentation pipeline called NightAug. This pipeline involves applying random augmentations, such as glare, blur, and noise, to daytime images. Experiments on publicly available datasets demonstrate that our method achieves superior results to state-of-the-art methods by 20\%, and to supervised models trained directly on the target data.

</details>

### Region-Aware Pretraining for Open-Vocabulary Object Detection with Vision Transformers.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01072)
- **作者**: Dahun Kim, Anelia Angelova, Weicheng Kuo
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### CSDA: Learning Category-Scale Joint Feature for Domain Adaptive Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01049) · 📚 被引 25
- **作者**: Changlong Gao, Chengxu Liu, Yujie Dun, Xueming Qian
- **🏷️ 机构**: Xi&#x2019;an Jiaotong University
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Most previous co-salient object detection works mainly focus on extracting co-salient cues via mining the consistency relations across images while ignoring explicit exploration of background regions. In this paper, we propose a Discriminative co-saliency and background Mining Transformer framework (DMT) based on several economical multi-grained correlation modules to explicitly mine both co-saliency and background information and effectively model their discrimination. Specifically, we first propose a region-to-region correlation module for introducing inter-image relations to pixel-wise segmentation features while maintaining computational efficiency. Then, we use two types of pre-defined tokens to mine co-saliency and background information via our proposed contrast-induced pixel-to-token correlation and co-saliency token-to-token correlation modules. We also design a token-guided feature refinement module to enhance the discriminability of the segmentation features under the guidance of the learned tokens. We perform iterative mutual promotion for the segmentation feature extraction and token construction. Experimental results on three benchmark datasets demonstrate the effectiveness of our proposed method. The source code is available at: https://github.com/dragonlee258079/DMT.

</details>

### Novel Scenes & Classes: Towards Adaptive Open-set Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01446)
- **作者**: Wuyang Li, Xiaoqing Guo, Yixuan Yuan
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### Large Selective Kernel Network for Remote Sensing Object Detection.
- **链接**: [arXiv:2303.09030](https://arxiv.org/abs/2303.09030) · [代码](https://github.com/zcablii/Large-Selective-Kernel-Network) · 📚 被引 807
- **作者**: Yuxuan Li, Qibin Hou, Zhaohui Zheng, Ming-Ming Cheng, Jian Yang, Xiang Li
- **🏷️ 机构**: Nankai University,VCIP, CS
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Generalized few-shot object detection aims to achieve precise detection on both base classes with abundant annotations and novel classes with limited training data. Existing approaches enhance few-shot generalization with the sacrifice of base-class performance, or maintain high precision in base-class detection with limited improvement in novel-class adaptation. In this paper, we point out the reason is insufficient Discriminative feature learning for all of the classes. As such, we propose a new training framework, DiGeo, to learn Geometry-aware features of inter-class separation and intra-class compactness. To guide the separation of feature clusters, we derive an offline simplex equiangular tight frame (ETF) classifier whose weights serve as class centers and are maximally and equally separated. To tighten the cluster for each class, we include adaptive class-specific margins into the classification loss and encourage the features close to the class centers. Experimental studies on two few-shot benchmark datasets (VOC, COCO) and one long-tail dataset (LVIS) demonstrate that, with a single model, our method can effectively improve generalization on novel classes without hurting the detection of base classes.

</details>

### Gradient-based Sampling for Class Imbalanced Semi-supervised Object Detection.
- **链接**: [arXiv:2403.15127](https://arxiv.org/abs/2403.15127) · [代码](https://github.com/nightkeepers/CI-SSOD) · 📚 被引 11
- **作者**: Jiaming Li, Xiangru Lin, Wei Zhang, Xiao Tan, Yingying Li, Junyu Han et al.
- **🏷️ 机构**: Sun Yat-sen University,School of Computer Science and Engineering,Guangzhou,China, Baidu Inc.,Department of Computer Vision Technology (VIS),China
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Current semi-supervised object detection (SSOD) algorithms typically assume class balanced datasets (PASCAL VOC etc.) or slightly class imbalanced datasets (MS-COCO, etc). This assumption can be easily violated since real world datasets can be extremely class imbalanced in nature, thus making the performance of semi-supervised object detectors far from satisfactory. Besides, the research for this problem in SSOD is severely under-explored. To bridge this research gap, we comprehensively study the class imbalance problem for SSOD under more challenging scenarios, thus forming the first experimental setting for class imbalanced SSOD (CI-SSOD). Moreover, we propose a simple yet effective gradient-based sampling framework that tackles the class imbalance problem from the perspective of two types of confirmation biases. To tackle confirmation bias towards majority classes, the gradient-based reweighting and gradient-based thresholding modules leverage the gradients from each class to fully balance the influence of the majority and minority classes. To tackle the confirmation bias from incorrect pseudo labels of minority classes, the class-rebalancing sampling module resamples unlabeled data following the guidance of the gradient-based reweighting module. Experiments on three proposed sub-tasks, namely MS-COCO, MS-COCO to Object365 and LVIS, suggest that our method outperforms current class imbalanced object detectors by clear margins, serving as a baseline for future research in CI-SSOD. Code will be available at https://github.com/nightkeepers/CI-SSOD.

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> During training, supervised object detection tries to correctly match the predicted bounding boxes and associated classification scores to the ground truth. This is essential to determine which predictions are to be pushed towards which solutions, or to be discarded. Popular matching strategies include matching to the closest ground truth box (mostly used in combination with anchors), or matching via the Hungarian algorithm (mostly used in anchor-free methods). Each of these strategies comes with its own properties, underlying losses, and heuristics. We show how Unbalanced Optimal Transport unifies these different approaches and opens a whole continuum of methods in between. This allows for a finer selection of the desired properties. Experimentally, we show that training an object detection model with Unbalanced Optimal Transport is able to reach the state-of-the-art both in terms of Average Precision and Average Recall as well as to provide a faster initial convergence. The approach is well suited for GPU implementation, which proves to be an advantage for large-scale models.

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

### Instance Relation Graph Guided Source-Free Domain Adaptive Object Detection.
- **链接**: [arXiv:2203.15793](https://arxiv.org/abs/2203.15793) · 📚 被引 94
- **作者**: Vibashan VS, Poojan Oza, Vishal M. Patel
- **🏷️ 机构**: Johns Hopkins University,Baltimore,MD,USA
- **会议**: CVPR 2023

</details>

### Augmented Box Replay: Overcoming Foreground Shift for Incremental Object Detection.
- **链接**: [arXiv:2307.12427](https://arxiv.org/abs/2307.12427) · 📚 被引 39
- **作者**: Yuyang Liu, Yang Cong, Dipam Goswami, Xialei Liu, Joost van de Weijer
- **🏷️ 机构**: Chinese Academy of Sciences,State Key Laboratory of Robotics, Shenyang Institute of Automation, South China University of Technology, Computer Vision Center, Barcelona
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In incremental learning, replaying stored samples from previous tasks together with current task samples is one of the most efficient approaches to address catastrophic forgetting. However, unlike incremental classification, image replay has not been successfully applied to incremental object detection (IOD). In this paper, we identify the overlooked problem of foreground shift as the main reason for this. Foreground shift only occurs when replaying images of previous tasks and refers to the fact that their background might contain foreground objects of the current task. To overcome this problem, a novel and efficient Augmented Box Replay (ABR) method is developed that only stores and replays foreground objects and thereby circumvents the foreground shift problem. In addition, we propose an innovative Attentive RoI Distillation loss that uses spatial attention from region-of-interest (RoI) features to constrain current model to focus on the most important information from old model. ABR significantly reduces forgetting of previous classes while maintaining high plasticity in current classes. Moreover, it considerably reduces the storage requirements when compared to standard image replay. Comprehensive experiments on Pascal-VOC and COCO datasets support the state-of-the-art performance of our model.

</details>

### Integrally Migrating Pre-trained Transformer Encoder-decoders for Visual Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00628) · 📚 被引 26
- **作者**: Feng Liu, Xiaosong Zhang, Zhiliang Peng, Zonghao Guo, Fang Wan, Xiangyang Ji et al.
- **🏷️ 机构**: University of Chinese Academy of Sciences, Tsinghua University
- **会议**: ICCV 2023

### Anchor-Intermediate Detector: Decoupling and Coupling Bounding Boxes for Accurate Object Detection.
- **链接**: [arXiv:2310.05666](https://arxiv.org/abs/2310.05666) · [代码](https://github.com/YilongLv/AID) · 📚 被引 7
- **作者**: Yilong Lv, Min Li, Yujie He, Zhuzhen He, Shaopeng Li, Aitao Yang
- **🏷️ 机构**: Xi&#x2019;an Institute of High Technology, National University of Defense Technology, Tsinghua University,Department of Automation
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Anchor-based detectors have been continuously developed for object detection. However, the individual anchor box makes it difficult to predict the boundary's offset accurately. Instead of taking each bounding box as a closed individual, we consider using multiple boxes together to get prediction boxes. To this end, this paper proposes the \textbf{Box Decouple-Couple(BDC) strategy} in the inference, which no longer discards the overlapping boxes, but decouples the corner points of these boxes. Then, according to each corner's score, we couple the corner points to select the most accurate corner pairs. To meet the BDC strategy, a simple but novel model is designed named the \textbf{Anchor-Intermediate Detector(AID)}, which contains two head networks, i.e., an anchor-based head and an anchor-free \textbf{Corner-aware head}. The corner-aware head is able to score the corners of each bounding box to facilitate the coupling between corner points. Extensive experiments on MS COCO show that the proposed anchor-intermediate detector respectively outperforms their baseline RetinaNet and GFL method by $\sim$2.4 and $\sim$1.2 AP on the MS COCO test-dev dataset without any bells and whistles. Code is available at: https://github.com/YilongLv/AID.

</details>

### Adaptive Rotated Convolution for Rotated Object Detection.
- **链接**: [arXiv:2303.07820](https://arxiv.org/abs/2303.07820) · [代码](https://github.com/LeapLabTHU/ARC) · 📚 被引 191
- **作者**: Yifan Pu, Yiru Wang, Zhuofan Xia, Yizeng Han, Yulin Wang, Weihao Gan et al.
- **🏷️ 机构**: Tsinghua University,BNRist,Department of Automation, SenseTime Research, Mashang Consumer Finance Co., Ltd.
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Rotated object detection aims to identify and locate objects in images with arbitrary orientation. In this scenario, the oriented directions of objects vary considerably across different images, while multiple orientations of objects exist within an image. This intrinsic characteristic makes it challenging for standard backbone networks to extract high-quality features of these arbitrarily orientated objects. In this paper, we present Adaptive Rotated Convolution (ARC) module to handle the aforementioned challenges. In our ARC module, the convolution kernels rotate adaptively to extract object features with varying orientations in different images, and an efficient conditional computation mechanism is introduced to accommodate the large orientation variations of objects within an image. The two designs work seamlessly in rotated object detection problem. Moreover, ARC can conveniently serve as a plug-and-play module in various vision backbones to boost their representation ability to detect oriented objects accurately. Experiments on commonly used benchmarks (DOTA and HRSC2016) demonstrate that equipped with our proposed ARC module in the backbone network, the performance of multiple popular oriented object detectors is significantly improved (\eg +3.03\% mAP on Rotated RetinaNet and +4.16\% on CFA). Combined with the highly competitive method Oriented R-CNN, the proposed approach achieves state-of-the-art performance on the DOTA dataset with 81.77\% mAP. Code is available at \url{https://github.com/LeapLabTHU/ARC}.

</details>

### EdaDet: Open-Vocabulary Object Detection Using Early Dense Alignment.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01441)
- **作者**: Cheng Shi, Sibei Yang
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### Deep Directly-Trained Spiking Neural Networks for Object Detection.
- **链接**: [arXiv:2307.11411](https://arxiv.org/abs/2307.11411) · 📚 被引 129
- **作者**: Qiaoyi Su, Yuhong Chou, Yifan Hu, Jianing Li, Shijie Mei, Ziyang Zhang et al.
- **🏷️ 机构**: University of Chinese Academy of Sciences,School of Artificial Intelligence, Xi&#x2019;an Jiaotong University,College of Artificial Intelligence, Tsinghua University,Department of Precision Instrument
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The performance of modern object detectors drops when the test distribution differs from the training one. Most of the methods that address this focus on object appearance changes caused by, e.g., different illumination conditions, or gaps between synthetic and real images. Here, by contrast, we tackle geometric shifts emerging from variations in the image capture process, or due to the constraints of the environment causing differences in the apparent geometry of the content itself. We introduce a self-training approach that learns a set of geometric transformations to minimize these shifts without leveraging any labeled data in the new domain, nor any information about the cameras. We evaluate our method on two different shifts, i.e., a camera's field of view (FoV) change and a viewpoint change. Our results evidence that learning geometric transformations helps detectors to perform better in the target domains.

</details>

</details>

### SparseDet: Improving Sparsely Annotated Object Detection with Pseudo-positive Mining.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00623) · 📚 被引 15
- **作者**: Saksham Suri, Sai Saketh Rambhatla, Rama Chellappa, Abhinav Shrivastava
- **🏷️ 机构**: University of Maryland,College Park, Johns Hopkins University
- **会议**: ICCV 2023

### CoTDet: Affordance Knowledge Prompting for Task Driven Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00285) · 📚 被引 27
- **作者**: Jiajin Tang, Ge Zheng, Jingyi Yu, Sibei Yang
- **🏷️ 机构**: ShanghaiTech University,School of Information Science and Technology
- **会议**: ICCV 2023

### FemtoDet: An Object Detection Baseline for Energy Versus Performance Tradeoffs.
- **链接**: [arXiv:2301.06719](https://arxiv.org/abs/2301.06719) · 📚 被引 14
- **作者**: Peng Tu, Xu Xie, Guo Ai, Yuexiang Li, Yawen Huang, Yefeng Zheng
- **🏷️ 机构**: MicroBT Inc., Jarvis Lab Tencent
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Efficient detectors for edge devices are often optimized for parameters or speed count metrics, which remain in weak correlation with the energy of detectors. However, some vision applications of convolutional neural networks, such as always-on surveillance cameras, are critical for energy constraints. This paper aims to serve as a baseline by designing detectors to reach tradeoffs between energy and performance from two perspectives: 1) We extensively analyze various CNNs to identify low-energy architectures, including selecting activation functions, convolutions operators, and feature fusion structures on necks. These underappreciated details in past work seriously affect the energy consumption of detectors; 2) To break through the dilemmatic energy-performance problem, we propose a balanced detector driven by energy using discovered low-energy components named \textit{FemtoDet}. In addition to the novel construction, we improve FemtoDet by considering convolutions and training strategy optimizations. Specifically, we develop a new instance boundary enhancement (IBE) module for convolution optimization to overcome the contradiction between the limited capacity of CNNs and detection tasks in diverse spatial representations, and propose a recursive warm-restart (RecWR) for optimizing training strategy to escape the sub-optimization of light-weight detectors by considering the data shift produced in popular augmentations. As a result, FemtoDet with only 68.77k parameters achieves a competitive score of 46.3 AP50 on PASCAL VOC and 1.11 W $\&$ 64.47 FPS on Qualcomm Snapdragon 865 CPU platforms. Extensive experiments on COCO and TJU-DHD datasets indicate that the proposed method achieves competitive results in diverse scenes.

</details>

### ALWOD: Active Learning for Weakly-Supervised Object Detection.
- **链接**: [arXiv:2309.07914](https://arxiv.org/abs/2309.07914) · [代码](https://github.com/seqam-lab/ALWOD) · 📚 被引 28
- **作者**: Yuting Wang, Velibor Ilic, Jiatong Li, Branislav Kisacanin, Vladimir Pavlovic
- **🏷️ 机构**: Rutgers University,NJ,USA, The Institute for Artificial Intelligence Research and Development of Serbia,Novi Sad,Serbia, Nvidia Corporation,TX,USA
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Object detection (OD), a crucial vision task, remains challenged by the lack of large training datasets with precise object localization labels. In this work, we propose ALWOD, a new framework that addresses this problem by fusing active learning (AL) with weakly and semi-supervised object detection paradigms. Because the performance of AL critically depends on the model initialization, we propose a new auxiliary image generator strategy that utilizes an extremely small labeled set, coupled with a large weakly tagged set of images, as a warm-start for AL. We then propose a new AL acquisition function, another critical factor in AL success, that leverages the student-teacher OD pair disagreement and uncertainty to effectively propose the most informative images to annotate. Finally, to complete the AL loop, we introduce a new labeling task delegated to human annotators, based on selection and correction of model-proposed detections, which is both rapid and effective in labeling the informative images. We demonstrate, across several challenging benchmarks, that ALWOD significantly narrows the gap between the ODs trained on few partially labeled but strategically selected image instances and those that rely on the fully-labeled data. Our code is publicly available on https://github.com/seqam-lab/ALWOD.

</details>

### Deep Equilibrium Object Detection.
- **链接**: [arXiv:2308.09564](https://arxiv.org/abs/2308.09564) · 📚 被引 7
- **作者**: Shuai Wang, Yao Teng, Limin Wang
- **🏷️ 机构**: Nanjing University,State Key Laboratory for Novel Software Technology
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Query-based object detectors directly decode image features into object instances with a set of learnable queries. These query vectors are progressively refined to stable meaningful representations through a sequence of decoder layers, and then used to directly predict object locations and categories with simple FFN heads. In this paper, we present a new query-based object detector (DEQDet) by designing a deep equilibrium decoder. Our DEQ decoder models the query vector refinement as the fixed point solving of an {implicit} layer and is equivalent to applying {infinite} steps of refinement. To be more specific to object decoding, we use a two-step unrolled equilibrium equation to explicitly capture the query vector refinement. Accordingly, we are able to incorporate refinement awareness into the DEQ training with the inexact gradient back-propagation (RAG). In addition, to stabilize the training of our DEQDet and improve its generalization ability, we devise the deep supervision scheme on the optimization path of DEQ with refinement-aware perturbation~(RAP). Our experiments demonstrate DEQDet converges faster, consumes less memory, and achieves better results than the baseline counterpart (AdaMixer). In particular, our DEQDet with ResNet50 backbone and 300 queries achieves the $49.5$ mAP and $33.0$ AP$_s$ on the MS COCO benchmark under $2\times$ training scheme (24 epochs).

</details>

### Open-Vocabulary Object Detection With an Open Corpus.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00622)
- **作者**: Jiong Wang, Huiming Zhang, Haiwen Hong, Xuan Jin, Yuan He, Hui Xue et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### Generalized UAV Object Detection via Frequency Domain Disentanglement.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00109) · 📚 被引 74
- **作者**: Kunyu Wang, Xueyang Fu, Yukun Huang, Chengzhi Cao, Gege Shi, Zheng-Jun Zha
- **🏷️ 机构**: University of Science and Technology of China,China
- **会议**: CVPR 2023

### Spatial Self-Distillation for Object Detection with Inaccurate Bounding Boxes.
- **链接**: [arXiv:2307.12101](https://arxiv.org/abs/2307.12101) · [代码](https://github.com/ucas-vg/PointTinyBenchmark) · 📚 被引 20
- **作者**: Di Wu, Pengfei Chen, Xuehui Yu, Guorong Li, Zhenjun Han, Jianbin Jiao
- **🏷️ 机构**: University of Chinese Academy of Sciences
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Object detection via inaccurate bounding boxes supervision has boosted a broad interest due to the expensive high-quality annotation data or the occasional inevitability of low annotation quality (\eg tiny objects). The previous works usually utilize multiple instance learning (MIL), which highly depends on category information, to select and refine a low-quality box. Those methods suffer from object drift, group prediction and part domination problems without exploring spatial information. In this paper, we heuristically propose a \textbf{Spatial Self-Distillation based Object Detector (SSD-Det)} to mine spatial information to refine the inaccurate box in a self-distillation fashion. SSD-Det utilizes a Spatial Position Self-Distillation \textbf{(SPSD)} module to exploit spatial information and an interactive structure to combine spatial information and category information, thus constructing a high-quality proposal bag. To further improve the selection procedure, a Spatial Identity Self-Distillation \textbf{(SISD)} module is introduced in SSD-Det to obtain spatial confidence to help select the best proposals. Experiments on MS-COCO and VOC datasets with noisy box annotation verify our method's effectiveness and achieve state-of-the-art performance. The code is available at https://github.com/ucas-vg/PointTinyBenchmark/tree/SSD-Det.

</details>

### Bridging Cross-task Protocol Inconsistency for Distillation in Dense Object Detection.
- **链接**: [arXiv:2308.14286](https://arxiv.org/abs/2308.14286) · [代码](https://github.com/TinyTigerPan/BCKD) · 📚 被引 67
- **作者**: Longrong Yang, Xianpan Zhou, Xuewei Li, Liang Qiao, Zheyang Li, Ziwei Yang et al.
- **🏷️ 机构**: Zhejiang University,College of Computer Science &#x0026; Technology, Zhejiang University,Polytechnic Institute, Hikvision Research Institute
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Knowledge distillation (KD) has shown potential for learning compact models in dense object detection. However, the commonly used softmax-based distillation ignores the absolute classification scores for individual categories. Thus, the optimum of the distillation loss does not necessarily lead to the optimal student classification scores for dense object detectors. This cross-task protocol inconsistency is critical, especially for dense object detectors, since the foreground categories are extremely imbalanced. To address the issue of protocol differences between distillation and classification, we propose a novel distillation method with cross-task consistent protocols, tailored for the dense object detection. For classification distillation, we address the cross-task protocol inconsistency problem by formulating the classification logit maps in both teacher and student models as multiple binary-classification maps and applying a binary-classification distillation loss to each map. For localization distillation, we design an IoU-based Localization Distillation Loss that is free from specific network structures and can be compared with existing localization distillation losses. Our proposed method is simple but effective, and experimental results demonstrate its superiority over existing methods. Code is available at https://github.com/TinyTigerPan/BCKD.

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Two-stage object detectors generate object proposals and classify them to detect objects in images. These proposals often do not contain the objects perfectly but overlap with them in many possible ways, exhibiting great variability in the difficulty levels of the proposals. Training a robust classifier against this crop-related variability requires abundant training data, which is not available in few-shot settings. To mitigate this issue, we propose a novel variational autoencoder (VAE) based data generation model, which is capable of generating data with increased crop-related diversity. The main idea is to transform the latent space such latent codes with different norms represent different crop-related variations. This allows us to generate features with increased crop-related diversity in difficulty levels by simply varying the latent norm. In particular, each latent code is rescaled such that its norm linearly correlates with the IoU score of the input crop w.r.t. the ground-truth box. Here the IoU score is a proxy that represents the difficulty level of the crop. We train this VAE model on base classes conditioned on the semantic code of each class and then use the trained model to generate features for novel classes. In our experiments our generated features consistently improve state-of-the-art few-shot object detection methods on the PASCAL VOC and MS COCO datasets.

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent progress in weakly supervised object detection is featured by a combination of multiple instance detection networks (MIDN) and ordinal online refinement. However, with only image-level annotation, MIDN inevitably assigns high scores to some unexpected region proposals when generating pseudo labels. These inaccurate high-scoring region proposals will mislead the training of subsequent refinement modules and thus hamper the detection performance. In this work, we explore how to ameliorate the quality of pseudo-labeling in MIDN. Formally, we devise Cyclic-Bootstrap Labeling (CBL), a novel weakly supervised object detection pipeline, which optimizes MIDN with rank information from a reliable teacher network. Specifically, we obtain this teacher network by introducing a weighted exponential moving average strategy to take advantage of various refinement modules. A novel class-specific ranking distillation algorithm is proposed to leverage the output of weighted ensembled teacher network for distilling MIDN with rank information. As a result, MIDN is guided to assign higher scores to accurate proposals among their neighboring ones, thus benefiting the subsequent pseudo labeling. Extensive experiments on the prevalent PASCAL VOC 2007 \& 2012 and COCO datasets demonstrate the superior performance of our CBL framework. Code will be available at https://github.com/Yinyf0804/WSOD-CBL/.

</details>

### Small Object Detection via Coarse-to-fine Proposal Generation and Imitation Learning.
- **链接**: [arXiv:2308.09534](https://arxiv.org/abs/2308.09534) · 📚 被引 135
- **作者**: Xiang Yuan, Gong Cheng, Kebing Yan, Qinghua Zeng, Junwei Han
- **🏷️ 机构**: Northwestern Polytechnical University,School of Automation,Xi&#x2019;an,China
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The past few years have witnessed the immense success of object detection, while current excellent detectors struggle on tackling size-limited instances. Concretely, the well-known challenge of low overlaps between the priors and object regions leads to a constrained sample pool for optimization, and the paucity of discriminative information further aggravates the recognition. To alleviate the aforementioned issues, we propose CFINet, a two-stage framework tailored for small object detection based on the Coarse-to-fine pipeline and Feature Imitation learning. Firstly, we introduce Coarse-to-fine RPN (CRPN) to ensure sufficient and high-quality proposals for small objects through the dynamic anchor selection strategy and cascade regression. Then, we equip the conventional detection head with a Feature Imitation (FI) branch to facilitate the region representations of size-limited instances that perplex the model in an imitation manner. Moreover, an auxiliary imitation loss following supervised contrastive learning paradigm is devised to optimize this branch. When integrated with Faster RCNN, CFINet achieves state-of-the-art performance on the large-scale small object detection benchmarks, SODA-D and SODA-A, underscoring its superiority over baseline detector and other mainstream detection approaches.

</details>

### A Dynamic Dual-Processing Object Detection Framework Inspired by the Brain's Recognition Mechanism.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00576) · 📚 被引 3
- **作者**: Minying Zhang, Tianpeng Bu, Lulu Hu
- **🏷️ 机构**: Alibaba Group,Hangzhou,China
- **会议**: ICCV 2023

### RecursiveDet: End-to-End Region-based Recursive Object Detection.
- **链接**: [arXiv:2307.13619](https://arxiv.org/abs/2307.13619) · [代码](https://github.com/bravezzzzzz/RecursiveDet) · 📚 被引 7
- **作者**: Jing Zhao, Li Sun, Qingli Li
- **🏷️ 机构**: East China Normal University,Shanghai Key Laboratory of Multidimensional Information Processing,Shanghai,China
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> End-to-end region-based object detectors like Sparse R-CNN usually have multiple cascade bounding box decoding stages, which refine the current predictions according to their previous results. Model parameters within each stage are independent, evolving a huge cost. In this paper, we find the general setting of decoding stages is actually redundant. By simply sharing parameters and making a recursive decoder, the detector already obtains a significant improvement. The recursive decoder can be further enhanced by positional encoding (PE) of the proposal box, which makes it aware of the exact locations and sizes of input bounding boxes, thus becoming adaptive to proposals from different stages during the recursion. Moreover, we also design centerness-based PE to distinguish the RoI feature element and dynamic convolution kernels at different positions within the bounding box. To validate the effectiveness of the proposed method, we conduct intensive ablations and build the full model on three recent mainstream region-based detectors. The RecusiveDet is able to achieve obvious performance boosts with even fewer model parameters and slightly increased computation cost. Codes are available at https://github.com/bravezzzzzz/RecursiveDet.

</details>

### Class-aware Memory Guided Unbiased Weighting for Universal Domain Adaptive Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00469) · 📚 被引 2
- **作者**: Qinghai Lang, Zhenwei He, Xiaowei Fu, Lei Zhang
- **🏷️ 机构**: Chongqing University,School of Microelectronics and Communication Engineering,China
- **会议**: ICCV 2023

### Self-training and multi-task learning for limited data: evaluation study on object detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00107) · 📚 被引 1
- **作者**: Hoàng-Ân Lê, Minh-Tan Pham
- **🏷️ 机构**: Universit&#x00E9; Bretagne Sud, UMR 6074,IRISA,Vannes,France,56000
- **会议**: ICCV 2023

### DetOFA: Efficient Training of Once-for-All Networks for Object Detection using Path Filter.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00143) · 📚 被引 3
- **作者**: Yuiko Sakuma, Masato Ishii, Takuya Narihira
- **🏷️ 机构**: Sony Group Corporation,Tokyo,Japan
- **会议**: ICCV 2023

### Identification of Novel Classes for Improving Few-Shot Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00360)
- **作者**: Zeyu Shangguan, Mohammad Rostami
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### InterAug: A Tuning-Free Augmentation Policy for Data-Efficient and Robust Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00033) · 📚 被引 0
- **作者**: Kowshik Thopalli, Devi S, Jayaraman J. Thiagarajan
- **🏷️ 机构**: Lawrence Livermore National Labs,USA, SRM Institute of Science and Technology,India
- **会议**: ICCV 2023

### Fast Object Detection in High-Resolution Videos.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00159) · 📚 被引 0
- **作者**: Ryan Tran, Atul Kanaujia, Vasu Parameswaran
- **🏷️ 机构**: Percipient.ai,Santa Clara,CA
- **会议**: ICCV 2023

### Adaptive Self-Training for Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00098)
- **作者**: Renaud Vandeghen, Gilles Louppe, Marc Van Droogenbroeck
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### Comparative Study of Natural Replay and Experience Replay in Online Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00386) · 📚 被引 0
- **作者**: Baptiste Wagner, Denis Pellerin, Sylvain Huet
- **🏷️ 机构**: Univ. Grenoble Alpes,CNRS, Grenoble INP, GIPSA-lab,Grenoble,France,38000
- **会议**: ICCV 2023

### Towards Unsupervised Object Detection from LiDAR Point Clouds.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00899) · 📚 被引 39
- **作者**: Lunjun Zhang, Anqi Joyce Yang, Yuwen Xiong, Sergio Casas, Bin Yang, Mengye Ren et al.
- **🏷️ 机构**: Waabi, University of Toronto
- **会议**: CVPR 2023

### MetaFusion: Infrared and Visible Image Fusion via Meta-Feature Embedding from Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01341) · 📚 被引 241
- **作者**: Wenda Zhao, Shigeng Xie, Fan Zhao, You He, Huchuan Lu
- **🏷️ 机构**: Dalian University of Technology,China, Liaoning Normal University,China, Tsinghua University,China
- **会议**: CVPR 2023

### Texture-Guided Saliency Distilling for Unsupervised Salient Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00701) · 📚 被引 74
- **作者**: Huajun Zhou, Bo Qiao, Lingxiao Yang, Jianhuang Lai, Xiaohua Xie
- **🏷️ 机构**: School of Computer Science and Engineering, Sun Yat-sen University,China
- **会议**: CVPR 2023

## 跨领域论文（完整笔记在其他领域）

- ObjectFusion: Multi-modal 3D Object Detection with Object-Centric Fusion. → [3d-detection](../3d-detection/Guideline%202023.md)
- Object as Query: Lifting any 2D Object Detector to 3D Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Exploring Object-Centric Temporal Modeling for Efficient Multi-View 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Periodically Exchange Teacher-Student for Source-Free Object Detection. → [knowledge-distillation](../knowledge-distillation/Guideline%202023.md)
- Efficient Transformer-based 3D Object Detection with Dynamic Token Halting. → [3d-detection](../3d-detection/Guideline%202023.md)
- DistillBEV: Boosting Multi-Camera 3D Object Detection with Cross-Modal Knowledge Distillation. → [3d-detection](../3d-detection/Guideline%202023.md)
- Revisiting Domain-Adaptive 3D Object Detection by Reliable, Diverse and Class-balanced Pseudo-Labeling. → [3d-detection](../3d-detection/Guideline%202023.md)
- Learning with Noisy Data for Semi-Supervised 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- FocalFormer3D : Focusing on Hard Instance for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Once Detected, Never Lost: Surpassing Human Performance in Offline LiDAR based 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- A Fast Unified System for 3D Object Detection and Tracking. → [3d-detection](../3d-detection/Guideline%202023.md)
- UpCycling: Semi-supervised 3D Object Detection without Sharing Raw-level Unlabeled Scenes. → [3d-detection](../3d-detection/Guideline%202023.md)
- Alleviating Catastrophic Forgetting of Incremental Object Detection via Within-Class and Between-Class Knowledge Distillation. → [continual-learning](../continual-learning/Guideline%202023.md)
- Predict to Detect: Prediction-guided 3D Object Detection using Sequential Images. → [3d-detection](../3d-detection/Guideline%202023.md)
- PG-RCNN: Semantic Surface Point Generation for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- GPA-3D: Geometry-aware Prototype Alignment for Unsupervised Domain Adaptive 3D Object Detection from Point Clouds. → [3d-detection](../3d-detection/Guideline%202023.md)
- Representation Disparity-aware Distillation for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- SparseBEV: High-Performance Sparse 3D Object Detection from Multi-Camera Videos. → [3d-detection](../3d-detection/Guideline%202023.md)
- Monocular 3D Object Detection with Bounding Box Denoising in 3D by Perceiver. → [3d-detection](../3d-detection/Guideline%202023.md)
- Kecor: Kernel Coding Rate Maximization for Active 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Towards Fair and Comprehensive Comparisons for Image-Based 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- DetZero: Rethinking Offboard 3D Object Detection with Long-term Sequential Point Clouds. → [3d-detection](../3d-detection/Guideline%202023.md)
- PARTNER: Level up the Polar Representation for LiDAR 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Clusterformer: Cluster-based Transformer for 3D Object Detection in Point Clouds. → [3d-detection](../3d-detection/Guideline%202023.md)
- SupFusion: Supervised LiDAR-Camera Fusion for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- 3DPPE: 3D Point Positional Encoding for Transformer-based Multi-Camera 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- GraphAlign: Enhancing Accurate Feature Alignment by Graph matching for Multi-Modal 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- ImGeoNet: Image-induced Geometry-aware Voxel Representation for Multi-view 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Not Every Side Is Equal: Localization Uncertainty Estimation for Semi-Supervised 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Towards Universal LiDAR-Based 3D Object Detection by Multi-Domain Knowledge Transfer. → [3d-detection](../3d-detection/Guideline%202023.md)
- Label-Efficient Online Continual Object Detection in Streaming Video. → [continual-learning](../continual-learning/Guideline%202023.md)
- CoIn: Contrastive Instance Feature Mining for Outdoor 3D Object Detection with Very Limited Annotations. → [3d-detection](../3d-detection/Guideline%202023.md)
- Pixel-Aligned Recurrent Queries for Multi-View 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- SparseFusion: Fusing Multi-Modal Sparse Representations for Multi-Sensor 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- MonoNeRD: NeRF-like Representations for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- NeRF-Det: Learning Geometry-Aware Volumetric Representation for Multi-View 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Cross Modal Transformer: Towards Fast and Robust 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Parametric Depth Based Feature Representation Learning for Object Detection and Segmentation in Bird's-Eye View. → [bev](../bev/Guideline%202023.md)
- MonoDETR: Depth-guided Transformer for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- QD-BEV : Quantization-aware View-guided Distillation for Multi-view 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- A Simple Vision Transformer for Weakly Semi-supervised 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- SA-BEV: Generating Semantic-Aware Bird's-Eye-View Feature for Multi-view 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Ada3D : Exploiting the Spatial Redundancy with Adaptive Inference for Efficient 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Masked Retraining Teacher-Student Framework for Domain Adaptive Object Detection. → [knowledge-distillation](../knowledge-distillation/Guideline%202023.md)
- An Empirical Analysis of Range for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- On Offline Evaluation of 3D Object Detection for Autonomous Driving. → [3d-detection](../3d-detection/Guideline%202023.md)
- Tensor Factorization for Leveraging Cross-Modal Knowledge in Data-Constrained Infrared Object Detection. → [multimodal](../multimodal/Guideline%202023.md)
