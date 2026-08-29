# Object Detection — 2023 Guideline

> 领域: 通用 2D 目标检测（检测器架构、密集预测、小物体/旋转框/NMS 等）
> 论文数: 101 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### DINO: DETR with Improved DeNoising Anchor Boxes for End-to-End Object Detection.
- **链接**: [出版页](https://openreview.net/forum?id=3mRwyG5one)
- **作者**: Hao Zhang, Feng Li, Shilong Liu, Lei Zhang, Hang Su, Jun Zhu et al.
- **🏷️ 机构**: PolyU / OPPO
- **会议**: CVPR 2023

### Learning Object-Language Alignments for Open-Vocabulary Object Detection.
- **链接**: [出版页](https://openreview.net/forum?id=mjHlitXvReu)
- **作者**: Chuang Lin, Peize Sun, Yi Jiang, Ping Luo, Lizhen Qu, Gholamreza Haffari et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### Continual Detection Transformer for Incremental Object Detection.
- **链接**: [arXiv:2304.03110](https://arxiv.org/abs/2304.03110) · 📚 被引 93
- **作者**: Yaoyao Liu, Bernt Schiele, Andrea Vedaldi, Christian Rupprecht
- **🏷️ 机构**: Max Planck Institute for Informatics, Saarland Informatics Campus, University of Oxford,Visual Geometry Group,Department of Engineering Science
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Language-based object detection is a promising direction towards building a natural interface to describe objects in images that goes far beyond plain category names. While recent methods show great progress in that direction, proper evaluation is lacking. With OmniLabel, we propose a novel task definition, dataset, and evaluation metric. The task subsumes standard- and open-vocabulary detection as well as referring expressions. With more than 28K unique object descriptions on over 25K images, OmniLabel provides a challenging benchmark with diverse and complex object descriptions in a naturally open-vocabulary setting. Moreover, a key differentiation to existing benchmarks is that our object descriptions can refer to one, multiple or even no object, hence, providing negative examples in free-form text. The proposed evaluation handles the large label space and judges performance via a modified average precision metric, which we validate by evaluating strong language-based baselines. OmniLabel indeed provides a challenging test bed for future research on language-based detection.

</details>

### 3D Video Object Detection with Learnable Object-Centric Global Optimization.
- **链接**: [arXiv:2303.15416](https://arxiv.org/abs/2303.15416) · [代码](https://github.com/jiaweihe1996/BA-Det) · 📚 被引 10
- **作者**: Jiawei He, Yuntao Chen, Naiyan Wang, Zhaoxiang Zhang
- **🏷️ 机构**: Institute of Automation, Chinese Academy of Sciences (CASIA),CRIPAC, HKISI_CAS,Centre for Artificial Intelligence and Robotics, TuSimple
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Object localization in general environments is a fundamental part of vision systems. While dominating on the COCO benchmark, recent Transformer-based detection methods are not competitive in diverse domains. Moreover, these methods still struggle to very accurately estimate the object bounding boxes in complex environments. We introduce Cascade-DETR for high-quality universal object detection. We jointly tackle the generalization to diverse domains and localization accuracy by proposing the Cascade Attention layer, which explicitly integrates object-centric information into the detection decoder by limiting the attention to the previous box prediction. To further enhance accuracy, we also revisit the scoring of queries. Instead of relying on classification scores, we predict the expected IoU of the query, leading to substantially more well-calibrated confidences. Lastly, we introduce a universal object detection benchmark, UDB10, that contains 10 datasets from diverse domains. While also advancing the state-of-the-art on COCO, Cascade-DETR substantially improves DETR-based detectors on all datasets in UDB10, even by over 10 mAP in some cases. The improvements under stringent quality requirements are even more pronounced. Our code and models will be released at https://github.com/SysCV/cascade-detr.

</details>

### Unknown Sniffer for Object Detection: Don't Turn a Blind Eye to Unknown Objects.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00315)
- **作者**: Wenteng Liang, Feng Xue, Yihao Liu, Guofeng Zhong, Anlong Ming
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### CAT: LoCalization and IdentificAtion Cascade Detection Transformer for Open-World Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01885)
- **作者**: Shuailei Ma, Yuefeng Wang, Ying Wei, Jiaqi Fan, Thomas H. Li, Hongli Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### Detection Hub: Unifying Object Detection Datasets via Query Adaptation on Language Embedding.
- **链接**: [arXiv:2206.03484](https://arxiv.org/abs/2206.03484) · 📚 被引 10
- **作者**: Lingchen Meng, Xiyang Dai, Yinpeng Chen, Pengchuan Zhang, Dongdong Chen, Mengchen Liu et al.
- **🏷️ 机构**: School of CS, Fudan University,Shanghai Key Lab of Intell. Info. Processing, Microsoft
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose DiffusionDet, a new framework that formulates object detection as a denoising diffusion process from noisy boxes to object boxes. During the training stage, object boxes diffuse from ground-truth boxes to random distribution, and the model learns to reverse this noising process. In inference, the model refines a set of randomly generated boxes to the output results in a progressive way. Our work possesses an appealing property of flexibility, which enables the dynamic number of boxes and iterative evaluation. The extensive experiments on the standard benchmarks show that DiffusionDet achieves favorable performance compared to previous well-established detectors. For example, DiffusionDet achieves 5.3 AP and 4.8 AP gains when evaluated with more boxes and iteration steps, under a zero-shot transfer setting from COCO to CrowdHuman. Our code is available at https://github.com/ShoufaChen/DiffusionDet.

</details>

### Pixels, Regions, and Objects: Multiple Enhancement for Salient Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00967) · 📚 被引 132
- **作者**: Yi Wang, Ruili Wang, Xin Fan, Tianzhu Wang, Xiangjian He
- **🏷️ 机构**: DUT-RU International School of Information Science and Engineering, Dalian University of Technology,China, School of Mathematical and Computational Sciences, Massey University,New Zealand, School of Computer Science, University of Nottingham Ningbo China,Ningbo,China
- **会议**: CVPR 2023

### Curricular Object Manipulation in LiDAR-based Object Detection.
- **链接**: [arXiv:2304.04248](https://arxiv.org/abs/2304.04248) · [代码](https://github.com/ZZY816/COM) · 📚 被引 15
- **作者**: Ziyue Zhu, Qiang Meng, Xiao Wang, Ke Wang, Liujiang Yan, Jian Yang
- **🏷️ 机构**: College of Computer Science, Nankai University,Tianjin Key Laboratory of Visual Computing and Intelligent Perception, Didi Chuxing
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In Video Object Detection (VID), a common practice is to leverage the rich temporal contexts from the video to enhance the object representations in each frame. Existing methods treat the temporal contexts obtained from different objects indiscriminately and ignore their different identities. While intuitively, aggregating local views of the same object in different frames may facilitate a better understanding of the object. Thus, in this paper, we aim to enable the model to focus on the identity-consistent temporal contexts of each object to obtain more comprehensive object representations and handle the rapid object appearance variations such as occlusion, motion blur, etc. However, realizing this goal on top of existing VID models faces low-efficiency problems due to their redundant region proposals and nonparallel frame-wise prediction manner. To aid this, we propose ClipVID, a VID model equipped with Identity-Consistent Aggregation (ICA) layers specifically designed for mining fine-grained and identity-consistent temporal contexts. It effectively reduces the redundancies through the set prediction strategy, making the ICA layers very efficient and further allowing us to design an architecture that makes parallel clip-wise predictions for the whole video clip. Extensive experimental results demonstrate the superiority of our method: a state-of-the-art (SOTA) performance (84.7% mAP) on the ImageNet VID dataset while running at a speed about 7x faster (39.3 fps) than previous SOTAs.

</details>

### PROB: Probabilistic Objectness for Open World Object Detection.
- **链接**: [arXiv:2212.01424](https://arxiv.org/abs/2212.01424) · [代码](https://github.com/orrzohar/PROB) · 📚 被引 110
- **作者**: Orr Zohar, Kuan-Chieh Wang, Serena Yeung
- **🏷️ 机构**: Stanford University
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open World Object Detection (OWOD) is a new and challenging computer vision task that bridges the gap between classic object detection (OD) benchmarks and object detection in the real world. In addition to detecting and classifying seen/labeled objects, OWOD algorithms are expected to detect novel/unknown objects - which can be classified and incrementally learned. In standard OD, object proposals not overlapping with a labeled object are automatically classified as background. Therefore, simply applying OD methods to OWOD fails as unknown objects would be predicted as background. The challenge of detecting unknown objects stems from the lack of supervision in distinguishing unknown objects and background object proposals. Previous OWOD methods have attempted to overcome this issue by generating supervision using pseudo-labeling - however, unknown object detection has remained low. Probabilistic/generative models may provide a solution for this challenge. Herein, we introduce a novel probabilistic framework for objectness estimation, where we alternate between probability distribution estimation and objectness likelihood maximization of known objects in the embedded feature space - ultimately allowing us to estimate the objectness probability of different proposals. The resulting Probabilistic Objectness transformer-based open-world detector, PROB, integrates our framework into traditional object detection models, adapting them for the open-world setting. Comprehensive experiments on OWOD benchmarks show that PROB outperforms all existing OWOD methods in both unknown object detection ($\sim 2\times$ unknown recall) and known object detection ($\sim 10\%$ mAP). Our code will be made available upon publication at https://github.com/orrzohar/PROB.

</details>

### Detecting Everything in the Open World: Towards Universal Object Detection.
- **链接**: [arXiv:2303.11749](https://arxiv.org/abs/2303.11749) · 📚 被引 96
- **作者**: Zhenyu Wang, Yali Li, Xi Chen, Ser-Nam Lim, Antonio Torralba, Hengshuang Zhao et al.
- **🏷️ 机构**: Tsinghua University,Department of Electronic Engineering, The University of Hong Kong, Meta AI
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we formally address universal object detection, which aims to detect every scene and predict every category. The dependence on human annotations, the limited visual information, and the novel categories in the open world severely restrict the universality of traditional detectors. We propose UniDetector, a universal object detector that has the ability to recognize enormous categories in the open world. The critical points for the universality of UniDetector are: 1) it leverages images of multiple sources and heterogeneous label spaces for training through the alignment of image and text spaces, which guarantees sufficient information for universal representations. 2) it generalizes to the open world easily while keeping the balance between seen and unseen classes, thanks to abundant information from both vision and language modalities. 3) it further promotes the generalization ability to novel categories through our proposed decoupling training manner and probability calibration. These contributions allow UniDetector to detect over 7k categories, the largest measurable category size so far, with only about 500 classes participating in training. Our UniDetector behaves the strong zero-shot generalization ability on large-vocabulary datasets like LVIS, ImageNetBoxes, and VisualGenome - it surpasses the traditional supervised baselines by more than 4\% on average without seeing any corresponding images. On 13 public detection datasets with various scenes, UniDetector also achieves state-of-the-art performance with only a 3\% amount of training data.

</details>

### Bi-LRFusion: Bi-Directional LiDAR-Radar Fusion for 3D Dynamic Object Detection.
- **链接**: [arXiv:2306.01438](https://arxiv.org/abs/2306.01438) · [代码](https://github.com/JessieW0806/BiLRFusion) · 📚 被引 48
- **作者**: Yingjie Wang, Jiajun Deng, Yao Li, Jinshui Hu, Cong Liu, Yu Zhang et al.
- **🏷️ 机构**: University of Science and Technology of China, University of Sydney, iFLYTEK
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> LiDAR and Radar are two complementary sensing approaches in that LiDAR specializes in capturing an object's 3D shape while Radar provides longer detection ranges as well as velocity hints. Though seemingly natural, how to efficiently combine them for improved feature representation is still unclear. The main challenge arises from that Radar data are extremely sparse and lack height information. Therefore, directly integrating Radar features into LiDAR-centric detection networks is not optimal. In this work, we introduce a bi-directional LiDAR-Radar fusion framework, termed Bi-LRFusion, to tackle the challenges and improve 3D detection for dynamic objects. Technically, Bi-LRFusion involves two steps: first, it enriches Radar's local features by learning important details from the LiDAR branch to alleviate the problems caused by the absence of height information and extreme sparsity; second, it combines LiDAR features with the enhanced Radar features in a unified bird's-eye-view representation. We conduct extensive experiments on nuScenes and ORR datasets, and show that our Bi-LRFusion achieves state-of-the-art performance for detecting dynamic objects. Notably, Radar data in these two datasets have different formats, which demonstrates the generalizability of our method. Codes are available at https://github.com/JessieW0806/BiLRFusion.

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> LiDAR and Radar are two complementary sensing approaches in that LiDAR specializes in capturing an object's 3D shape while Radar provides longer detection ranges as well as velocity hints. Though seemingly natural, how to efficiently combine them for improved feature representation is still unclear. The main challenge arises from that Radar data are extremely sparse and lack height information. Therefore, directly integrating Radar features into LiDAR-centric detection networks is not optimal. In this work, we introduce a bi-directional LiDAR-Radar fusion framework, termed Bi-LRFusion, to tackle the challenges and improve 3D detection for dynamic objects. Technically, Bi-LRFusion involves two steps: first, it enriches Radar's local features by learning important details from the LiDAR branch to alleviate the problems caused by the absence of height information and extreme sparsity; second, it combines LiDAR features with the enhanced Radar features in a unified bird's-eye-view representation. We conduct extensive experiments on nuScenes and ORR datasets, and show that our Bi-LRFusion achieves state-of-the-art performance for detecting dynamic objects. Notably, Radar data in these two datasets have different formats, which demonstrates the generalizability of our method. Codes are available at https://github.com/JessieW0806/BiLRFusion.

</details>

### Normalizing Flow based Feature Synthesis for Outlier-Aware Object Detection.
- **链接**: [arXiv:2302.07106](https://arxiv.org/abs/2302.07106) · [代码](https://github.com/nish03/FFS) · 📚 被引 14
- **作者**: Nishant Kumar, Sinisa Segvic, Abouzar Eslami, Stefan Gumhold
- **🏷️ 机构**: TU Dresden, University of Zagreb - FER, Carl Zeiss Meditec AG
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Real-world deployment of reliable object detectors is crucial for applications such as autonomous driving. However, general-purpose object detectors like Faster R-CNN are prone to providing overconfident predictions for outlier objects. Recent outlier-aware object detection approaches estimate the density of instance-wide features with class-conditional Gaussians and train on synthesized outlier features from their low-likelihood regions. However, this strategy does not guarantee that the synthesized outlier features will have a low likelihood according to the other class-conditional Gaussians. We propose a novel outlier-aware object detection framework that distinguishes outliers from inlier objects by learning the joint data distribution of all inlier classes with an invertible normalizing flow. The appropriate sampling of the flow model ensures that the synthesized outliers have a lower likelihood than inliers of all object classes, thereby modeling a better decision boundary between inlier and outlier objects. Our approach significantly outperforms the state-of-the-art for outlier-aware object detection on both image and video datasets. Code available at https://github.com/nish03/FFS

</details>

### Cut and Learn for Unsupervised Object Detection and Instance Segmentation.
- **链接**: [arXiv:2301.11320](https://arxiv.org/abs/2301.11320) · 📚 被引 182
- **作者**: Xudong Wang, Rohit Girdhar, Stella X. Yu, Ishan Misra
- **🏷️ 机构**: FAIR, Meta AI, UC Berkeley / ICSI
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose Cut-and-LEaRn (CutLER), a simple approach for training unsupervised object detection and segmentation models. We leverage the property of self-supervised models to 'discover' objects without supervision and amplify it to train a state-of-the-art localization model without any human labels. CutLER first uses our proposed MaskCut approach to generate coarse masks for multiple objects in an image and then learns a detector on these masks using our robust loss function. We further improve the performance by self-training the model on its predictions. Compared to prior work, CutLER is simpler, compatible with different detection architectures, and detects multiple objects. CutLER is also a zero-shot unsupervised detector and improves detection performance AP50 by over 2.7 times on 11 benchmarks across domains like video frames, paintings, sketches, etc. With finetuning, CutLER serves as a low-shot detector surpassing MoCo-v2 by 7.3% APbox and 6.6% APmask on COCO when training with 5% labels.

</details>

### Phase-Shifting Coder: Predicting Accurate Orientation in Oriented Object Detection.
- **链接**: [arXiv:2211.06368](https://arxiv.org/abs/2211.06368) · [代码](https://github.com/open-mmlab/mmrotate) · 📚 被引 173
- **作者**: Yi Yu, Feipeng Da
- **🏷️ 机构**: School of Automation, Southeast University,Nanjing,China
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> With the vigorous development of computer vision, oriented object detection has gradually been featured. In this paper, a novel differentiable angle coder named phase-shifting coder (PSC) is proposed to accurately predict the orientation of objects, along with a dual-frequency version (PSCD). By mapping the rotational periodicity of different cycles into the phase of different frequencies, we provide a unified framework for various periodic fuzzy problems caused by rotational symmetry in oriented object detection. Upon such a framework, common problems in oriented object detection such as boundary discontinuity and square-like problems are elegantly solved in a unified form. Visual analysis and experiments on three datasets prove the effectiveness and the potentiality of our approach. When facing scenarios requiring high-quality bounding boxes, the proposed methods are expected to give a competitive performance. The codes are publicly available at https://github.com/open-mmlab/mmrotate.

</details>

### Enhanced Training of Query-Based Object Detection via Selective Query Recollection.
- **链接**: [arXiv:2212.07593](https://arxiv.org/abs/2212.07593) · 📚 被引 64
- **作者**: Fangyi Chen, Han Zhang, Kai Hu, Yu-Kai Huang, Chenchen Zhu, Marios Savvides
- **🏷️ 机构**: Carnegie Mellon University, Meta AI
- **会议**: CVPR 2023

### STDLens: Model Hijacking-Resilient Federated Learning for Object Detection.
- **链接**: [arXiv:2303.11511](https://arxiv.org/abs/2303.11511) · 📚 被引 13
- **作者**: Ka-Ho Chow, Ling Liu, Wenqi Wei, Fatih Ilhan, Yanzhao Wu
- **🏷️ 机构**: Georgia Instutite of Technology,Atlanta,GA,USA
- **会议**: CVPR 2023

### What Can Human Sketches Do for Object Detection?
- **链接**: [arXiv:2303.15149](https://arxiv.org/abs/2303.15149) · 📚 被引 41
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
- **链接**: [arXiv:2303.14488](https://arxiv.org/abs/2303.14488) · [代码](https://github.com/Cuogeihong/CEASC) · 📚 被引 238
- **作者**: Bowei Du, Yecheng Huang, Jiaxin Chen, Di Huang
- **🏷️ 机构**: Beihang University,State Key Laboratory of Software Development Environment,Beijing,China, School of Computer Science and Engineering, Beihang University,Beijing,China
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Object detection on drone images with low-latency is an important but challenging task on the resource-constrained unmanned aerial vehicle (UAV) platform. This paper investigates optimizing the detection head based on the sparse convolution, which proves effective in balancing the accuracy and efficiency. Nevertheless, it suffers from inadequate integration of contextual information of tiny objects as well as clumsy control of the mask ratio in the presence of foreground with varying scales. To address the issues above, we propose a novel global context-enhanced adaptive sparse convolutional network (CEASC). It first develops a context-enhanced group normalization (CE-GN) layer, by replacing the statistics based on sparsely sampled features with the global contextual ones, and then designs an adaptive multi-layer masking strategy to generate optimal mask ratios at distinct scales for compact foreground coverage, promoting both the accuracy and efficiency. Extensive experimental results on two major benchmarks, i.e. VisDrone and UAVDT, demonstrate that CEASC remarkably reduces the GFLOPs and accelerates the inference procedure when plugging into the typical state-of-the-art detection frameworks (e.g. RetinaNet and GFL V1) with competitive performance. Code is available at https://github.com/Cuogeihong/CEASC.

</details>

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
- **链接**: [arXiv:2303.14311](https://arxiv.org/abs/2303.14311) · 📚 被引 6
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
- **链接**: [arXiv:2304.04515](https://arxiv.org/abs/2304.04515) · 📚 被引 70
- **作者**: Wei Hua, Dingkang Liang, Jingyu Li, Xiaolong Liu, Zhikang Zou, Xiaoqing Ye et al.
- **🏷️ 机构**: Huazhong University of Science and Technology, Baidu Inc.,China
- **会议**: CVPR 2023

### T-SEA: Transfer-Based Self-Ensemble Attack on Object Detection.
- **链接**: [arXiv:2211.09773](https://arxiv.org/abs/2211.09773) · 📚 被引 72
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
- **会议**: CVPR 2023

### Discriminative Co-Saliency and Background Mining Transformer for Co-Salient Object Detection.
- **链接**: [arXiv:2305.00514](https://arxiv.org/abs/2305.00514) · [代码](https://github.com/dragonlee258079/DMT) · 📚 被引 42
- **作者**: Long Li, Junwei Han, Ni Zhang, Nian Liu, Salman H. Khan, Hisham Cholakkal et al.
- **🏷️ 机构**: Northwestern Polytechnical University, Mohamed bin Zayed University of Artificial Intelligence
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent research on remote sensing object detection has largely focused on improving the representation of oriented bounding boxes but has overlooked the unique prior knowledge presented in remote sensing scenarios. Such prior knowledge can be useful because tiny remote sensing objects may be mistakenly detected without referencing a sufficiently long-range context, and the long-range context required by different types of objects can vary. In this paper, we take these priors into account and propose the Large Selective Kernel Network (LSKNet). LSKNet can dynamically adjust its large spatial receptive field to better model the ranging context of various objects in remote sensing scenarios. To the best of our knowledge, this is the first time that large and selective kernel mechanisms have been explored in the field of remote sensing object detection. Without bells and whistles, LSKNet sets new state-of-the-art scores on standard benchmarks, i.e., HRSC2016 (98.46\% mAP), DOTA-v1.0 (81.85\% mAP) and FAIR1M-v1.0 (47.87\% mAP). Based on a similar technique, we rank 2nd place in 2022 the Greater Bay Area International Algorithm Competition. Code is available at https://github.com/zcablii/Large-Selective-Kernel-Network.

</details>

### DynamicDet: A Unified Dynamic Architecture for Object Detection.
- **链接**: [arXiv:2304.05552](https://arxiv.org/abs/2304.05552) · 📚 被引 53
- **作者**: Zhihao Lin, Yongtao Wang, Jinhe Zhang, Xiaojie Chu
- **🏷️ 机构**: Wangxuan Institute of Computer Technology, Peking University
- **会议**: CVPR 2023

### Hierarchical Supervision and Shuffle Data Augmentation for 3D Semi-Supervised Object Detection.
- **链接**: [arXiv:2304.01464](https://arxiv.org/abs/2304.01464) · 📚 被引 31
- **作者**: Chuandong Liu, Chenqiang Gao, Fangcen Liu, Pengcheng Li, Deyu Meng, Xinbo Gao
- **🏷️ 机构**: School of Communication and Information Engineering, Chongqing University of Posts and Telecommunications,Chongqing,China, Xi&#x0027;an Jiaotong University,Xi&#x0027;an,China
- **会议**: CVPR 2023

### CIGAR: Cross-Modality Graph Reasoning for Domain Adaptive Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02277) · 📚 被引 47
- **作者**: Yabo Liu, Jinghua Wang, Chao Huang, Yaowei Wang, Yong Xu
- **🏷️ 机构**: Harbin Institute of Technology,Shenzhen, School of Cyber Science and Technology, Shenzhen Campus of Sun Yat-sen University, Peng Cheng Laboratory
- **会议**: CVPR 2023

### Ambiguity-Resistant Semi-Supervised Learning for Dense Object Detection.
- **链接**: [arXiv:2303.14960](https://arxiv.org/abs/2303.14960) · [代码](https://github.com/PaddlePaddle/PaddleDetection) · 📚 被引 67
- **作者**: Chang Liu, Weiming Zhang, Xiangru Lin, Wei Zhang, Xiao Tan, Junyu Han et al.
- **🏷️ 机构**: Shanghai University, Baidu Inc
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> With basic Semi-Supervised Object Detection (SSOD) techniques, one-stage detectors generally obtain limited promotions compared with two-stage clusters. We experimentally find that the root lies in two kinds of ambiguities: (1) Selection ambiguity that selected pseudo labels are less accurate, since classification scores cannot properly represent the localization quality. (2) Assignment ambiguity that samples are matched with improper labels in pseudo-label assignment, as the strategy is misguided by missed objects and inaccurate pseudo boxes. To tackle these problems, we propose a Ambiguity-Resistant Semi-supervised Learning (ARSL) for one-stage detectors. Specifically, to alleviate the selection ambiguity, Joint-Confidence Estimation (JCE) is proposed to jointly quantifies the classification and localization quality of pseudo labels. As for the assignment ambiguity, Task-Separation Assignment (TSA) is introduced to assign labels based on pixel-level predictions rather than unreliable pseudo boxes. It employs a "divide-and-conquer" strategy and separately exploits positives for the classification and localization task, which is more robust to the assignment ambiguity. Comprehensive experiments demonstrate that ARSL effectively mitigates the ambiguities and achieves state-of-the-art SSOD performance on MS COCO and PASCAL VOC. Codes can be found at https://github.com/PaddlePaddle/PaddleDetection.

</details>

### MixTeacher: Mining Promising Labels with Mixed Scale Teacher for Semi-Supervised Object Detection.
- **链接**: [arXiv:2303.09061](https://arxiv.org/abs/2303.09061) · [代码](https://github.com/lliuz/MixTeacher) · 📚 被引 58
- **作者**: Liang Liu, Boshen Zhang, Jiangning Zhang, Wuhao Zhang, Zhenye Gan, Guanzhong Tian et al.
- **🏷️ 机构**: Youtu Lab,Tencent, Ningbo Research Institute, Zhejiang University, Rongcheer Co., Ltd
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Scale variation across object instances remains a key challenge in object detection task. Despite the remarkable progress made by modern detection models, this challenge is particularly evident in the semi-supervised case. While existing semi-supervised object detection methods rely on strict conditions to filter high-quality pseudo labels from network predictions, we observe that objects with extreme scale tend to have low confidence, resulting in a lack of positive supervision for these objects. In this paper, we propose a novel framework that addresses the scale variation problem by introducing a mixed scale teacher to improve pseudo label generation and scale-invariant learning. Additionally, we propose mining pseudo labels using score promotion of predictions across scales, which benefits from better predictions from mixed scale features. Our extensive experiments on MS COCO and PASCAL VOC benchmarks under various semi-supervised settings demonstrate that our method achieves new state-of-the-art performance. The code and models are available at \url{https://github.com/lliuz/MixTeacher}.

</details>

### Open-Vocabulary Point-Cloud Object Detection without 3D Annotation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00121)
- **作者**: Yuheng Lu, Chenfeng Xu, Xiaobao Wei, Xiaodong Xie, Masayoshi Tomizuka, Kurt Keutzer et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### Annealing-based Label-Transfer Learning for Open World Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01102) · 📚 被引 34
- **作者**: Yuqing Ma, Hainan Li, Zhange Zhang, Jinyang Guo, Shanghang Zhang, Ruihao Gong et al.
- **🏷️ 机构**: Beihang University,SKLSDE Lab, Institute of Data Space,Hefei Comprehensive National Science Center, Peking University,National Key Laboratory for Multimedia Information Processing
- **会议**: CVPR 2023

### DiGeo: Discriminative Geometry-Aware Learning for Generalized Few-Shot Object Detection.
- **链接**: [arXiv:2303.09674](https://arxiv.org/abs/2303.09674) · 📚 被引 68
- **作者**: Jiawei Ma, Yulei Niu, Jincheng Xu, Shiyuan Huang, Guangxing Han, Shih-Fu Chang
- **🏷️ 机构**: Columbia University
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Current semi-supervised object detection (SSOD) algorithms typically assume class balanced datasets (PASCAL VOC etc.) or slightly class imbalanced datasets (MS-COCO, etc). This assumption can be easily violated since real world datasets can be extremely class imbalanced in nature, thus making the performance of semi-supervised object detectors far from satisfactory. Besides, the research for this problem in SSOD is severely under-explored. To bridge this research gap, we comprehensively study the class imbalance problem for SSOD under more challenging scenarios, thus forming the first experimental setting for class imbalanced SSOD (CI-SSOD). Moreover, we propose a simple yet effective gradient-based sampling framework that tackles the class imbalance problem from the perspective of two types of confirmation biases. To tackle confirmation bias towards majority classes, the gradient-based reweighting and gradient-based thresholding modules leverage the gradients from each class to fully balance the influence of the majority and minority classes. To tackle the confirmation bias from incorrect pseudo labels of minority classes, the class-rebalancing sampling module resamples unlabeled data following the guidance of the gradient-based reweighting module. Experiments on three proposed sub-tasks, namely MS-COCO, MS-COCO to Object365 and LVIS, suggest that our method outperforms current class imbalanced object detectors by clear margins, serving as a baseline for future research in CI-SSOD. Code will be available at https://github.com/nightkeepers/CI-SSOD.

</details>

### Bridging Precision and Confidence: A Train-Time Loss for Calibrating Object Detection.
- **链接**: [arXiv:2303.14404](https://arxiv.org/abs/2303.14404) · [代码](https://github.com/akhtarvision/bpc_calibration) · 📚 被引 18
- **作者**: Muhammad Akhtar Munir, Muhammad Haris Khan, Salman H. Khan, Fahad Shahbaz Khan
- **🏷️ 机构**: Mohamed bin Zayed University of AI
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep neural networks (DNNs) have enabled astounding progress in several vision-based problems. Despite showing high predictive accuracy, recently, several works have revealed that they tend to provide overconfident predictions and thus are poorly calibrated. The majority of the works addressing the miscalibration of DNNs fall under the scope of classification and consider only in-domain predictions. However, there is little to no progress in studying the calibration of DNN-based object detection models, which are central to many vision-based safety-critical applications. In this paper, inspired by the train-time calibration methods, we propose a novel auxiliary loss formulation that explicitly aims to align the class confidence of bounding boxes with the accurateness of predictions (i.e. precision). Since the original formulation of our loss depends on the counts of true positives and false positives in a minibatch, we develop a differentiable proxy of our loss that can be used during training with other application-specific loss functions. We perform extensive experiments on challenging in-domain and out-domain scenarios with six benchmark datasets including MS-COCO, Cityscapes, Sim10k, and BDD100k. Our results reveal that our train-time loss surpasses strong calibration baselines in reducing calibration error for both in and out-domain scenarios. Our source code and pre-trained models are available at https://github.com/akhtarvision/bpc_calibration

</details>

### Multiclass Confidence and Localization Calibration for Object Detection.
- **链接**: [arXiv:2306.08271](https://arxiv.org/abs/2306.08271) · [代码](https://github.com/bimsarapathiraja/MCCL) · 📚 被引 25
- **作者**: Bimsara Pathiraja, Malitha Gunawardhana, Muhammad Haris Khan
- **🏷️ 机构**: Mohamed bin Zayed University of Artificial Intelligence,UAE
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Albeit achieving high predictive accuracy across many challenging computer vision problems, recent studies suggest that deep neural networks (DNNs) tend to make overconfident predictions, rendering them poorly calibrated. Most of the existing attempts for improving DNN calibration are limited to classification tasks and restricted to calibrating in-domain predictions. Surprisingly, very little to no attempts have been made in studying the calibration of object detection methods, which occupy a pivotal space in vision-based security-sensitive, and safety-critical applications. In this paper, we propose a new train-time technique for calibrating modern object detection methods. It is capable of jointly calibrating multiclass confidence and box localization by leveraging their predictive uncertainties. We perform extensive experiments on several in-domain and out-of-domain detection benchmarks. Results demonstrate that our proposed train-time calibration method consistently outperforms several baselines in reducing calibration error for both in-domain and out-of-domain predictions. Our code and models are available at https://github.com/bimsarapathiraja/MCCL.

</details>

### Unbalanced Optimal Transport: A Unified Framework for Object Detection.
- **链接**: [arXiv:2307.02402](https://arxiv.org/abs/2307.02402) · 📚 被引 12
- **作者**: Henri De Plaen, Pierre-François De Plaen, Johan A. K. Suykens, Marc Proesmans, Tinne Tuytelaars, Luc Van Gool
- **🏷️ 机构**: ESAT-STADIUS, KU,Leuven,Belgium, ESAT-PSI, KU,Leuven,Belgium
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The paradigm of large-scale pre-training followed by downstream fine-tuning has been widely employed in various object detection algorithms. In this paper, we reveal discrepancies in data, model, and task between the pre-training and fine-tuning procedure in existing practices, which implicitly limit the detector's performance, generalization ability, and convergence speed. To this end, we propose AlignDet, a unified pre-training framework that can be adapted to various existing detectors to alleviate the discrepancies. AlignDet decouples the pre-training process into two stages, i.e., image-domain and box-domain pre-training. The image-domain pre-training optimizes the detection backbone to capture holistic visual abstraction, and box-domain pre-training learns instance-level semantics and task-aware concepts to initialize the parts out of the backbone. By incorporating the self-supervised pre-trained backbones, we can pre-train all modules for various detectors in an unsupervised paradigm. As depicted in Figure 1, extensive experiments demonstrate that AlignDet can achieve significant improvements across diverse protocols, such as detection algorithm, model backbone, data setting, and training schedule. For example, AlignDet improves FCOS by 5.3 mAP, RetinaNet by 2.1 mAP, Faster R-CNN by 3.3 mAP, and DETR by 2.3 mAP under fewer epochs.

</details>

### Modeling the Distributional Uncertainty for Salient Object Detection Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01883) · 📚 被引 32
- **作者**: Xinyu Tian, Jing Zhang, Mochu Xiang, Yuchao Dai
- **🏷️ 机构**: Northwestern Polytechnical University,China, Australian National University,Australia
- **会议**: CVPR 2023

### Instance Relation Graph Guided Source-Free Domain Adaptive Object Detection.
- **链接**: [arXiv:2203.15793](https://arxiv.org/abs/2203.15793) · 📚 被引 94
- **作者**: Vibashan VS, Poojan Oza, Vishal M. Patel
- **🏷️ 机构**: Johns Hopkins University,Baltimore,MD,USA
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Unsupervised Domain Adaptation (UDA) is an effective approach to tackle the issue of domain shift. Specifically, UDA methods try to align the source and target representations to improve the generalization on the target domain. Further, UDA methods work under the assumption that the source data is accessible during the adaptation process. However, in real-world scenarios, the labelled source data is often restricted due to privacy regulations, data transmission constraints, or proprietary data concerns. The Source-Free Domain Adaptation (SFDA) setting aims to alleviate these concerns by adapting a source-trained model for the target domain without requiring access to the source data. In this paper, we explore the SFDA setting for the task of adaptive object detection. To this end, we propose a novel training strategy for adapting a source-trained object detector to the target domain without source data. More precisely, we design a novel contrastive loss to enhance the target representations by exploiting the objects relations for a given target domain input. These object instance relations are modelled using an Instance Relation Graph (IRG) network, which are then used to guide the contrastive representation learning. In addition, we utilize a student-teacher based knowledge distillation strategy to avoid overfitting to the noisy pseudo-labels generated by the source-trained model. Extensive experiments on multiple object detection benchmark datasets show that the proposed approach is able to efficiently adapt source-trained object detectors to the target domain, outperforming previous state-of-the-art domain adaptive detection methods. Code and models are provided in \href{https://viudomain.github.io/irg-sfda-web/}{https://viudomain.github.io/irg-sfda-web/}.

</details>

### Test Time Adaptation with Regularized Loss for Weakly Supervised Salient Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00711) · 📚 被引 16
- **作者**: Olga Veksler
- **🏷️ 机构**: University of Waterloo,Canada
- **会议**: CVPR 2023

### CLIP the Gap: A Single Domain Generalization Approach for Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00314)
- **作者**: Vidit Vidit, Martin Engilberge, Mathieu Salzmann
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### Learning Transformations to Reduce the Geometric Shift in Object Detection.
- **链接**: [arXiv:2301.05496](https://arxiv.org/abs/2301.05496) · 📚 被引 2
- **作者**: Vidit Vidit, Martin Engilberge, Mathieu Salzmann
- **🏷️ 机构**: EPFL,CVLab
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In incremental learning, replaying stored samples from previous tasks together with current task samples is one of the most efficient approaches to address catastrophic forgetting. However, unlike incremental classification, image replay has not been successfully applied to incremental object detection (IOD). In this paper, we identify the overlooked problem of foreground shift as the main reason for this. Foreground shift only occurs when replaying images of previous tasks and refers to the fact that their background might contain foreground objects of the current task. To overcome this problem, a novel and efficient Augmented Box Replay (ABR) method is developed that only stores and replays foreground objects and thereby circumvents the foreground shift problem. In addition, we propose an innovative Attentive RoI Distillation loss that uses spatial attention from region-of-interest (RoI) features to constrain current model to focus on the most important information from old model. ABR significantly reduces forgetting of previous classes while maintaining high plasticity in current classes. Moreover, it considerably reduces the storage requirements when compared to standard image replay. Comprehensive experiments on Pascal-VOC and COCO datasets support the state-of-the-art performance of our model.

</details>

### Learning to Detect and Segment for Open Vocabulary Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00681)
- **作者**: Tao Wang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### Generalized UAV Object Detection via Frequency Domain Disentanglement.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00109) · 📚 被引 74
- **作者**: Kunyu Wang, Xueyang Fu, Yukun Huang, Chengzhi Cao, Gege Shi, Zheng-Jun Zha
- **🏷️ 机构**: University of Science and Technology of China,China
- **会议**: CVPR 2023

### Consistent-Teacher: Towards Reducing Inconsistent Pseudo-Targets in Semi-Supervised Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00316) · 📚 被引 115
- **作者**: Xinjiang Wang, Xingyi Yang, Shilong Zhang, Yijiang Li, Litong Feng, Shijie Fang et al.
- **🏷️ 机构**: SenseTime Research, National University of Singapore, Shanghai AI Laboratory
- **会议**: CVPR 2023

### Co-Salient Object Detection with Uncertainty-Aware Group Exchange-Masking.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01881) · 📚 被引 24
- **作者**: Yang Wu, Huihui Song, Bo Liu, Kaihua Zhang, Dong Liu
- **🏷️ 机构**: Nanjing University of Information Science and Technology,B-DAT and CICAEET,Nanjing,China, Walmart Global Tech,Sunnyvale,CA,USA,94086, Netflix Inc,Los Gatos,CA,USA,95032
- **会议**: CVPR 2023

### Aligning Bag of Regions for Open-Vocabulary Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01464)
- **作者**: Size Wu, Wenwei Zhang, Sheng Jin, Wentao Liu, Chen Change Loy
- **🏷️ 机构**: NTU S-Lab
- **会议**: CVPR 2023

### LSTFE-Net: Long Short-Term Feature Enhancement Network for Video Small Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01404) · 📚 被引 36
- **作者**: Jinsheng Xiao, Yuanxu Wu, Yunhua Chen, Shurui Wang, Zhongyuan Wang, Jiayi Ma
- **🏷️ 机构**: Wuhan University,China, Guangdong University of Technology,China
- **会议**: CVPR 2023

### Dynamic Coarse-to-Fine Learning for Oriented Tiny Object Detection.
- **链接**: [arXiv:2304.08876](https://arxiv.org/abs/2304.08876) · [代码](https://github.com/Chasel-Tsui/mmrotate-dcfl) · 📚 被引 166
- **作者**: Chang Xu, Jian Ding, Jinwang Wang, Wen Yang, Huai Yu, Lei Yu et al.
- **🏷️ 机构**: School of Electronic Information, Wuhan University, School of Computer Science, Wuhan University
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Detecting arbitrarily oriented tiny objects poses intense challenges to existing detectors, especially for label assignment. Despite the exploration of adaptive label assignment in recent oriented object detectors, the extreme geometry shape and limited feature of oriented tiny objects still induce severe mismatch and imbalance issues. Specifically, the position prior, positive sample feature, and instance are mismatched, and the learning of extreme-shaped objects is biased and unbalanced due to little proper feature supervision. To tackle these issues, we propose a dynamic prior along with the coarse-to-fine assigner, dubbed DCFL. For one thing, we model the prior, label assignment, and object representation all in a dynamic manner to alleviate the mismatch issue. For another, we leverage the coarse prior matching and finer posterior constraint to dynamically assign labels, providing appropriate and relatively balanced supervision for diverse instances. Extensive experiments on six datasets show substantial improvements to the baseline. Notably, we obtain the state-of-the-art performance for one-stage detectors on the DOTA-v1.5, DOTA-v2.0, and DIOR-R datasets under single-scale training and testing. Codes are available at https://github.com/Chasel-Tsui/mmrotate-dcfl.

</details>

### Gaussian Label Distribution Learning for Spherical Image Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00106) · 📚 被引 10
- **作者**: Hang Xu, Xinyuan Liu, Qiang Zhao, Yike Ma, Chenggang Yan, Feng Dai
- **🏷️ 机构**: Hangzhou Dianzi University,Hangzhou,China, Institute of Computing Technology, Chinese Academy of Sciences,Key Laboratory of Intelligent Information Processing of Chinese Academy of Sciences,Beijing,China
- **会议**: CVPR 2023

### Generating Features with Increased Crop-Related Diversity for Few-Shot Object Detection.
- **链接**: [arXiv:2304.05096](https://arxiv.org/abs/2304.05096) · 📚 被引 50
- **作者**: Jingyi Xu, Hieu Le, Dimitris Samaras
- **🏷️ 机构**: Stony Brook University, EPFL
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Anchor-based detectors have been continuously developed for object detection. However, the individual anchor box makes it difficult to predict the boundary's offset accurately. Instead of taking each bounding box as a closed individual, we consider using multiple boxes together to get prediction boxes. To this end, this paper proposes the \textbf{Box Decouple-Couple(BDC) strategy} in the inference, which no longer discards the overlapping boxes, but decouples the corner points of these boxes. Then, according to each corner's score, we couple the corner points to select the most accurate corner pairs. To meet the BDC strategy, a simple but novel model is designed named the \textbf{Anchor-Intermediate Detector(AID)}, which contains two head networks, i.e., an anchor-based head and an anchor-free \textbf{Corner-aware head}. The corner-aware head is able to score the corners of each bounding box to facilitate the coupling between corner points. Extensive experiments on MS COCO show that the proposed anchor-intermediate detector respectively outperforms their baseline RetinaNet and GFL method by $\sim$2.4 and $\sim$1.2 AP on the MS COCO test-dev dataset without any bells and whistles. Code is available at: https://github.com/YilongLv/AID.

</details>

### DetCLIPv2: Scalable Open-Vocabulary Object Detection Pre-training via Word-Region Alignment.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02250)
- **作者**: Lewei Yao, Jianhua Han, Xiaodan Liang, Dan Xu, Wei Zhang, Zhenguo Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### Object Detection with Self-Supervised Scene Adaptation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02068)
- **作者**: Zekun Zhang, Minh Hoai
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### Dense Distinct Query for End-to-End Object Detection.
- **链接**: [arXiv:2303.12776](https://arxiv.org/abs/2303.12776) · [代码](https://github.com/jshilong/DDQ) · 📚 被引 311
- **作者**: Shilong Zhang, Xinjiang Wang, Jiaqi Wang, Jiangmiao Pang, Chengqi Lyu, Wenwei Zhang et al.
- **🏷️ 机构**: Shanghai AI Laboratory, SenseTime Research, The University of Hong Kong
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> One-to-one label assignment in object detection has successfully obviated the need for non-maximum suppression (NMS) as postprocessing and makes the pipeline end-to-end. However, it triggers a new dilemma as the widely used sparse queries cannot guarantee a high recall, while dense queries inevitably bring more similar queries and encounter optimization difficulties. As both sparse and dense queries are problematic, then what are the expected queries in end-to-end object detection? This paper shows that the solution should be Dense Distinct Queries (DDQ). Concretely, we first lay dense queries like traditional detectors and then select distinct ones for one-to-one assignments. DDQ blends the advantages of traditional and recent end-to-end detectors and significantly improves the performance of various detectors including FCN, R-CNN, and DETRs. Most impressively, DDQ-DETR achieves 52.1 AP on MS-COCO dataset within 12 epochs using a ResNet-50 backbone, outperforming all existing detectors in the same setting. DDQ also shares the benefit of end-to-end detectors in crowded scenes and achieves 93.8 AP on CrowdHuman. We hope DDQ can inspire researchers to consider the complementarity between traditional methods and end-to-end detectors. The source code can be found at \url{https://github.com/jshilong/DDQ}.

</details>

### Towards Unsupervised Object Detection from LiDAR Point Clouds.
- **链接**: [arXiv:2311.02007](https://arxiv.org/abs/2311.02007) · 📚 被引 39
- **作者**: Lunjun Zhang, Anqi Joyce Yang, Yuwen Xiong, Sergio Casas, Bin Yang, Mengye Ren et al.
- **🏷️ 机构**: Waabi, University of Toronto
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we study the problem of unsupervised object detection from 3D point clouds in self-driving scenes. We present a simple yet effective method that exploits (i) point clustering in near-range areas where the point clouds are dense, (ii) temporal consistency to filter out noisy unsupervised detections, (iii) translation equivariance of CNNs to extend the auto-labels to long range, and (iv) self-supervision for improving on its own. Our approach, OYSTER (Object Discovery via Spatio-Temporal Refinement), does not impose constraints on data collection (such as repeated traversals of the same location), is able to detect objects in a zero-shot manner without supervised finetuning (even in sparse, distant regions), and continues to self-improve given more rounds of iterative self-training. To better measure model performance in self-driving scenarios, we propose a new planning-centric perception metric based on distance-to-collision. We demonstrate that our unsupervised object detector significantly outperforms unsupervised baselines on PandaSet and Argoverse 2 Sensor dataset, showing promise that self-supervision combined with object priors can enable object discovery in the wild. For more information, visit the project website: https://waabi.ai/research/oyster

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

### Prototypical Variational Autoencoder for 3D Few-shot Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/076a93fd42aa85f5ccee921a01d77dd5-Abstract-Conference.html) · 📚 被引 0
- **作者**: Weiliang Tang, Biqi Yang, Xianzhi Li, Yun-Hui Liu, Pheng-Ann Heng, Chi-Wing Fu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we study the problem of unsupervised object detection from 3D point clouds in self-driving scenes. We present a simple yet effective method that exploits (i) point clustering in near-range areas where the point clouds are dense, (ii) temporal consistency to filter out noisy unsupervised detections, (iii) translation equivariance of CNNs to extend the auto-labels to long range, and (iv) self-supervision for improving on its own. Our approach, OYSTER (Object Discovery via Spatio-Temporal Refinement), does not impose constraints on data collection (such as repeated traversals of the same location), is able to detect objects in a zero-shot manner without supervised finetuning (even in sparse, distant regions), and continues to self-improve given more rounds of iterative self-training. To better measure model performance in self-driving scenarios, we propose a new planning-centric perception metric based on distance-to-collision. We demonstrate that our unsupervised object detector significantly outperforms unsupervised baselines on PandaSet and Argoverse 2 Sensor dataset, showing promise that self-supervision combined with object priors can enable object discovery in the wild. For more information, visit the project website: https://waabi.ai/research/oyster

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Object detection via inaccurate bounding boxes supervision has boosted a broad interest due to the expensive high-quality annotation data or the occasional inevitability of low annotation quality (\eg tiny objects). The previous works usually utilize multiple instance learning (MIL), which highly depends on category information, to select and refine a low-quality box. Those methods suffer from object drift, group prediction and part domination problems without exploring spatial information. In this paper, we heuristically propose a \textbf{Spatial Self-Distillation based Object Detector (SSD-Det)} to mine spatial information to refine the inaccurate box in a self-distillation fashion. SSD-Det utilizes a Spatial Position Self-Distillation \textbf{(SPSD)} module to exploit spatial information and an interactive structure to combine spatial information and category information, thus constructing a high-quality proposal bag. To further improve the selection procedure, a Spatial Identity Self-Distillation \textbf{(SISD)} module is introduced in SSD-Det to obtain spatial confidence to help select the best proposals. Experiments on MS-COCO and VOC datasets with noisy box annotation verify our method's effectiveness and achieve state-of-the-art performance. The code is available at https://github.com/ucas-vg/PointTinyBenchmark/tree/SSD-Det.

</details>

### Bridging Cross-task Protocol Inconsistency for Distillation in Dense Object Detection.
- **链接**: [arXiv:2308.14286](https://arxiv.org/abs/2308.14286) · [代码](https://github.com/TinyTigerPan/BCKD) · 📚 被引 68
- **作者**: Longrong Yang, Xianpan Zhou, Xuewei Li, Liang Qiao, Zheyang Li, Ziwei Yang et al.
- **🏷️ 机构**: Zhejiang University,College of Computer Science &#x0026; Technology, Zhejiang University,Polytechnic Institute, Hikvision Research Institute
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Knowledge distillation (KD) has shown potential for learning compact models in dense object detection. However, the commonly used softmax-based distillation ignores the absolute classification scores for individual categories. Thus, the optimum of the distillation loss does not necessarily lead to the optimal student classification scores for dense object detectors. This cross-task protocol inconsistency is critical, especially for dense object detectors, since the foreground categories are extremely imbalanced. To address the issue of protocol differences between distillation and classification, we propose a novel distillation method with cross-task consistent protocols, tailored for the dense object detection. For classification distillation, we address the cross-task protocol inconsistency problem by formulating the classification logit maps in both teacher and student models as multiple binary-classification maps and applying a binary-classification distillation loss to each map. For localization distillation, we design an IoU-based Localization Distillation Loss that is free from specific network structures and can be compared with existing localization distillation losses. Our proposed method is simple but effective, and experimental results demonstrate its superiority over existing methods. Code is available at https://github.com/TinyTigerPan/BCKD.

</details>

### Cyclic-Bootstrap Labeling for Weakly Supervised Object Detection.
- **链接**: [arXiv:2308.05991](https://arxiv.org/abs/2308.05991) · [代码](https://github.com/Yinyf0804/WSOD-CBL) · 📚 被引 17
- **作者**: Yufei Yin, Jiajun Deng, Wengang Zhou, Li Li, Houqiang Li
- **🏷️ 机构**: University of Science and Technology of China,CAS Key Laboratory of Technology in GIPAS,EEIS Department, The University of Sydney
- **会议**: ICCV 2023

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

### Introspection of 2D Object Detection using Processed Neural Activation Patterns in Automated Driving Systems.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00437) · 📚 被引 3
- **作者**: Hakan Yekta Yatbaz, Mehrdad Dianati, Konstantinos Koufos, Roger Woodman
- **🏷️ 机构**: University of Warwick,WMG
- **会议**: ICCV 2023

## 跨领域论文（完整笔记在其他领域）

- Omni3D: A Large Benchmark and Model for 3D Object Detection in the Wild. → [3d-detection](../3d-detection/Guideline%202023.md)
- ConQueR: Query Contrast Voxel-DETR for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- AShapeFormer : Semantics-Guided Object-Level Active Shape Encoding for 3D Object Detection via Transformers. → [3d-detection](../3d-detection/Guideline%202023.md)
- Viewpoint Equivariance for Multi-View 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- VoxelNeXt: Fully Sparse VoxelNet for 3D Object Detection and Tracking. → [3d-detection](../3d-detection/Guideline%202023.md)
- PiMAE: Point Cloud and Image Interactive Masked Autoencoders for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- BEV-SAN: Accurate BEV 3D Object Detection via Slice Attention Networks. → [3d-detection](../3d-detection/Guideline%202023.md)
- itKD: Interchange Transfer-based Knowledge Distillation for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Benchmarking Robustness of 3D Object Detection to Common Corruptions in Autonomous Driving. → [3d-detection](../3d-detection/Guideline%202023.md)
- AeDet: Azimuth-Invariant Multi-View 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- MSF: Motion-guided Sequential Fusion for Efficient 3D Object Detection from Point Cloud Sequences. → [3d-detection](../3d-detection/Guideline%202023.md)
- Density-Insensitive Unsupervised Domain Adaption on 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- MSMDFusion: Fusing LiDAR and Camera at Multiple Scales with Multi-Depth Seeds for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- X3KD: Knowledge Distillation Across Modalities, Tasks and Stages for Multi-Camera 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- LoGoNet: Towards Accurate 3D Object Detection with Local-to-Global Cross- Modal Fusion. → [3d-detection](../3d-detection/Guideline%202023.md)
- PillarNeXt: Rethinking Network Designs for 3D Object Detection in LiDAR Point Clouds. → [3d-detection](../3d-detection/Guideline%202023.md)
- MoDAR: Using Motion Forecasting for 3D Object Detection in Point Cloud Sequences. → [3d-detection](../3d-detection/Guideline%202023.md)
- Deep Dive into Gradients: Better Optimization for 3D Object Detection with Gradient-Corrected IoU Supervision. → [3d-detection](../3d-detection/Guideline%202023.md)
- Weakly Supervised Monocular 3D Object Detection Using Multi-View Projection and Direction Consistency. → [3d-detection](../3d-detection/Guideline%202023.md)
- Towards Domain Generalization for Multi-view 3D Object Detection in Bird-Eye-View. → [3d-detection](../3d-detection/Guideline%202023.md)
- Semi-Supervised Stereo-Based 3D Object Detection via Cross-View Consensus. → [3d-detection](../3d-detection/Guideline%202023.md)
- Virtual Sparse Convolution for Multimodal 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- CAPE: Camera View Position Embedding for Multi-View 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Multi-view Adversarial Discriminator: Mine the Non-causal Factors for Object Detection in Unseen Domains. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- BEVHeight: A Robust Framework for Vision-based Roadside 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Bi3D: Bi-Domain Active Learning for Cross-Domain 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Distilling Focal Knowledge from Imperfect Expert for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Uni3D: A Unified Baseline for Multi-Dataset 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- OcTr: Octree-Based Transformer for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- UniDistill: A Universal Cross-Modality Knowledge Distillation Framework for 3D Object Detection in Bird's-Eye View. → [3d-detection](../3d-detection/Guideline%202023.md)
- MonoATT: Online Monocular 3D Object Detection with Adaptive Token Transformer. → [3d-detection](../3d-detection/Guideline%202023.md)
- Understanding the Robustness of 3D Object Detection with Bird'View Representations in Autonomous Driving. → [3d-detection](../3d-detection/Guideline%202023.md)
