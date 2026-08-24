# Object Detection — 2023 Guideline

> 领域: 通用 2D 目标检测（检测器架构、密集预测、小物体/旋转框/NMS 等）
> 论文数: 101 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Semi-DETR: Semi-Supervised Object Detection with Detection Transformers.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02280) · 📚 被引 77
- **作者**: Jiacheng Zhang, Xiangru Lin, Wei Zhang, Kuo Wang, Xiao Tan, Junyu Han et al.
- **🏷️ 机构**: School of Computer Science and Engineering, Sun Yat-sen University,Guangzhou,China, Baidu Inc.,Department of Computer Vision Technology (VIS),China
- **会议**: CVPR 2023

### Mask DINO: Towards A Unified Transformer-based Framework for Object Detection and Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00297)
- **作者**: Feng Li, Hao Zhang, Huaizhe Xu, Shilong Liu, Lei Zhang, Lionel M. Ni et al.
- **🏷️ 机构**: PolyU / OPPO
- **会议**: CVPR 2023

### DETR with Additional Global Aggregation for Cross-domain Weakly Supervised Object Detection.
- **链接**: [arXiv:2304.07082](https://arxiv.org/abs/2304.07082) · [出版页](https://doi.org/10.1109/CVPR52729.2023.01099) · 📚 被引 15
- **作者**: Zongheng Tang, Yifan Sun, Si Liu, Yi Yang
- **🏷️ 机构**: Institute of Artificial Intelligence, Beihang University, Baidu Inc, CCAI, Zhejiang University
- **会议**: CVPR 2023

- **摘要（英，原文）**:

  > This paper presents a DETR-based method for cross-domain weakly supervised object detection (CDWSOD), aiming at adapting the detector from source to target domain through weak supervision. We think DETR has strong potential for CDWSOD due to an insight: the encoder and the decoder in DETR are both based on the attention mechanism and are thus capable of aggregating semantics across the entire image. The aggregation results, i.e., image-level predictions, can naturally exploit the weak supervision for domain alignment. Such motivated, we propose DETR with additional Global Aggregation (DETR-GA), a CDWSOD detector that simultaneously makes "instance-level + image-level" predictions and utilizes "strong + weak" supervisions. The key point of DETR-GA is very simple: for the encoder / decoder, we respectively add multiple class queries / a foreground query to aggregate the semantics into image-level predictions. Our query-based aggregation has two advantages. First, in the encoder, the weakly-supervised class queries are capable of roughly locating the corresponding positions and excluding the distraction from non-relevant regions. Second, through our design, the object queries and the foreground query in the decoder share consensus on the class semantics, therefore making the strong and weak supervision mutually benefit each other for domain alignment. Extensive experiments on four popular cross-domain benchmarks show that DETR-GA significantly improves CSWSOD and advances the states of the art (e.g., 29.0% --> 79.4% mAP on PASCAL VOC --> Clipart_all dataset).

### Toward RAW Object Detection: A New Benchmark and A New Model.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01286) · 📚 被引 31
- **作者**: Ruikang Xu, Chang Chen, Jingyang Peng, Cheng Li, Yibin Huang, Fenglong Song et al.
- **🏷️ 机构**: University of Science and Technology of China, Huawei Noah&#x0027;s Ark Lab
- **会议**: CVPR 2023

### Object-Aware Distillation Pyramid for Open-Vocabulary Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01076)
- **作者**: Luting Wang, Yi Liu, Penghui Du, Zihan Ding, Yue Liao, Qiaosong Qi et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### Continual Detection Transformer for Incremental Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02279) · 📚 被引 93
- **作者**: Yaoyao Liu, Bernt Schiele, Andrea Vedaldi, Christian Rupprecht
- **🏷️ 机构**: Max Planck Institute for Informatics, Saarland Informatics Campus, University of Oxford,Visual Geometry Group,Department of Engineering Science
- **会议**: CVPR 2023

### 3D Video Object Detection with Learnable Object-Centric Global Optimization.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00494) · 📚 被引 10
- **作者**: Jiawei He, Yuntao Chen, Naiyan Wang, Zhaoxiang Zhang
- **🏷️ 机构**: Institute of Automation, Chinese Academy of Sciences (CASIA),CRIPAC, HKISI_CAS,Centre for Artificial Intelligence and Robotics, TuSimple
- **会议**: CVPR 2023

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
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01097) · 📚 被引 10
- **作者**: Lingchen Meng, Xiyang Dai, Yinpeng Chen, Pengchuan Zhang, Dongdong Chen, Mengchen Liu et al.
- **🏷️ 机构**: School of CS, Fudan University,Shanghai Key Lab of Intell. Info. Processing, Microsoft
- **会议**: CVPR 2023

### Pixels, Regions, and Objects: Multiple Enhancement for Salient Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00967) · 📚 被引 132
- **作者**: Yi Wang, Ruili Wang, Xin Fan, Tianzhu Wang, Xiangjian He
- **🏷️ 机构**: DUT-RU International School of Information Science and Engineering, Dalian University of Technology,China, School of Mathematical and Computational Sciences, Massey University,New Zealand, School of Computer Science, University of Nottingham Ningbo China,Ningbo,China
- **会议**: CVPR 2023

### Curricular Object Manipulation in LiDAR-based Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00115) · 📚 被引 15
- **作者**: Ziyue Zhu, Qiang Meng, Xiao Wang, Ke Wang, Liujiang Yan, Jian Yang
- **🏷️ 机构**: College of Computer Science, Nankai University,Tianjin Key Laboratory of Visual Computing and Intelligent Perception, Didi Chuxing
- **会议**: CVPR 2023

### PROB: Probabilistic Objectness for Open World Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01101) · 📚 被引 110
- **作者**: Orr Zohar, Kuan-Chieh Wang, Serena Yeung
- **🏷️ 机构**: Stanford University
- **会议**: CVPR 2023

### Detecting Everything in the Open World: Towards Universal Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01100) · 📚 被引 96
- **作者**: Zhenyu Wang, Yali Li, Xi Chen, Ser-Nam Lim, Antonio Torralba, Hengshuang Zhao et al.
- **🏷️ 机构**: Tsinghua University,Department of Electronic Engineering, The University of Hong Kong, Meta AI
- **会议**: CVPR 2023

### Bi-LRFusion: Bi-Directional LiDAR-Radar Fusion for 3D Dynamic Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01287) · 📚 被引 48
- **作者**: Yingjie Wang, Jiajun Deng, Yao Li, Jinshui Hu, Cong Liu, Yu Zhang et al.
- **🏷️ 机构**: University of Science and Technology of China, University of Sydney, iFLYTEK
- **会议**: CVPR 2023

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
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01283) · 📚 被引 172
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
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01993) · 📚 被引 18
- **作者**: Geoffroi Côté, Fahim Mannan, Simon Thibault, Jean-François Lalonde, Felix Heide
- **🏷️ 机构**: Universit&#x00E9; Laval, Algolux, Princeton University
- **会议**: CVPR 2023

### Meta-Tuning Loss Functions and Data Augmentation for Few-Shot Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00709) · 📚 被引 32
- **作者**: Berkan Demirel, Orhun Bugra Baran, Ramazan Gokberk Cinbis
- **🏷️ 机构**: Middle East Technical University
- **会议**: CVPR 2023

### Harmonious Teacher for Cross-Domain Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02282) · 📚 被引 71
- **作者**: Jinhong Deng, Dongli Xu, Wen Li, Lixin Duan
- **🏷️ 机构**: University of Electronic Science and Technology of China, University of Sydney, Shenzhen Institute for Advanced Study, UESTC
- **会议**: CVPR 2023

### Adaptive Sparse Convolutional Networks with Global Context Enhancement for Faster Object Detection on Drone Images.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01291) · 📚 被引 236
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
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01334) · 📚 被引 188
- **作者**: Mathias Gehrig, Davide Scaramuzza
- **🏷️ 机构**: Robotics and Perception Group, University of Zurich,Switzerland
- **会议**: CVPR 2023

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
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02111) · 📚 被引 363
- **作者**: Chunming He, Kai Li, Yachao Zhang, Longxiang Tang, Yulun Zhang, Zhenhua Guo et al.
- **🏷️ 机构**: Shenzhen International Graduate School, Tsinghua University, NEC Laboratories America, ETH Z&#x00FC;rich
- **会议**: CVPR 2023

### NeRF-RPN: A general framework for object detection in NeRFs.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02253) · 📚 被引 54
- **作者**: Benran Hu, Junkai Huang, Yichen Liu, Yu-Wing Tai, Chi-Keung Tang
- **🏷️ 机构**: The Hong Kong University of Science and Technology
- **会议**: CVPR 2023

### SOOD: Towards Semi-Supervised Oriented Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01493) · 📚 被引 70
- **作者**: Wei Hua, Dingkang Liang, Jingyu Li, Xiaolong Liu, Zhikang Zou, Xiaoqing Ye et al.
- **🏷️ 机构**: HUAST
- **会议**: CVPR 2023

### T-SEA: Transfer-Based Self-Ensemble Attack on Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01965) · 📚 被引 72
- **作者**: Hao Huang, Ziyan Chen, Huanran Chen, Yongtao Wang, Kevin Zhang
- **🏷️ 机构**: Peking University,Beijing,China
- **会议**: CVPR 2023

### Feature Shrinkage Pyramid for Camouflaged Object Detection with Transformers.
- **链接**: [arXiv:2303.14816](https://arxiv.org/abs/2303.14816) · [出版页](https://doi.org/10.1109/CVPR52729.2023.00538) · [代码](https://github.com/ZhouHuang23/FSPNet) · 📚 被引 273
- **作者**: Zhou Huang, Hang Dai, Tian-Zhu Xiang, Shuo Wang, Huai-Xin Chen, Jie Qin et al.
- **🏷️ 机构**: Sichuan Changhong Electric Co., Ltd, University of Glasgow, G42
- **会议**: CVPR 2023

- **摘要（英，原文）**:

  > Vision transformers have recently shown strong global context modeling capabilities in camouflaged object detection. However, they suffer from two major limitations: less effective locality modeling and insufficient feature aggregation in decoders, which are not conducive to camouflaged object detection that explores subtle cues from indistinguishable backgrounds. To address these issues, in this paper, we propose a novel transformer-based Feature Shrinkage Pyramid Network (FSPNet), which aims to hierarchically decode locality-enhanced neighboring transformer features through progressive shrinking for camouflaged object detection. Specifically, we propose a nonlocal token enhancement module (NL-TEM) that employs the non-local mechanism to interact neighboring tokens and explore graph-based high-order relations within tokens to enhance local representations of transformers. Moreover, we design a feature shrinkage decoder (FSD) with adjacent interaction modules (AIM), which progressively aggregates adjacent transformer features through a layer-bylayer shrinkage pyramid to accumulate imperceptible but effective cues as much as possible for object information decoding. Extensive quantitative and qualitative experiments demonstrate that the proposed model significantly outperforms the existing 24 competitors on three challenging COD benchmark datasets under six widely-used evaluation metrics. Our code is publicly available at https://github.com/ZhouHuang23/FSPNet.

### 2PCNet: Two-Phase Consistency Training for Day-to-Night Unsupervised Domain Adaptive Object Detection.
- **链接**: [arXiv:2303.13853](https://arxiv.org/abs/2303.13853) · [出版页](https://doi.org/10.1109/CVPR52729.2023.01105) · 📚 被引 72
- **作者**: Mikhail Kennerley, Jian-Gang Wang, Bharadwaj Veeravalli, Robby T. Tan
- **🏷️ 机构**: National University of Singapore,Department of Electrical and Computer Engineering, Institute for Infocomm Research, A*STAR
- **会议**: CVPR 2023

- **摘要（英，原文）**:

  > Object detection at night is a challenging problem due to the absence of night image annotations. Despite several domain adaptation methods, achieving high-precision results remains an issue. False-positive error propagation is still observed in methods using the well-established student-teacher framework, particularly for small-scale and low-light objects. This paper proposes a two-phase consistency unsupervised domain adaptation network, 2PCNet, to address these issues. The network employs high-confidence bounding-box predictions from the teacher in the first phase and appends them to the student's region proposals for the teacher to re-evaluate in the second phase, resulting in a combination of high and low confidence pseudo-labels. The night images and pseudo-labels are scaled-down before being used as input to the student, providing stronger small-scale pseudo-labels. To address errors that arise from low-light regions and other night-related attributes in images, we propose a night-specific augmentation pipeline called NightAug. This pipeline involves applying random augmentations, such as glare, blur, and noise, to daytime images. Experiments on publicly available datasets demonstrate that our method achieves superior results to state-of-the-art methods by 20\%, and to supervised models trained directly on the target data.

### Region-Aware Pretraining for Open-Vocabulary Object Detection with Vision Transformers.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01072)
- **作者**: Dahun Kim, Anelia Angelova, Weicheng Kuo
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### Discriminative Co-Saliency and Background Mining Transformer for Co-Salient Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00700) · 📚 被引 42
- **作者**: Long Li, Junwei Han, Ni Zhang, Nian Liu, Salman H. Khan, Hisham Cholakkal et al.
- **🏷️ 机构**: Northwestern Polytechnical University, Mohamed bin Zayed University of Artificial Intelligence
- **会议**: CVPR 2023

### DynamicDet: A Unified Dynamic Architecture for Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00608) · 📚 被引 53
- **作者**: Zhihao Lin, Yongtao Wang, Jinhe Zhang, Xiaojie Chu
- **🏷️ 机构**: Wangxuan Institute of Computer Technology, Peking University
- **会议**: CVPR 2023

### Hierarchical Supervision and Shuffle Data Augmentation for 3D Semi-Supervised Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02281) · 📚 被引 30
- **作者**: Chuandong Liu, Chenqiang Gao, Fangcen Liu, Pengcheng Li, Deyu Meng, Xinbo Gao
- **🏷️ 机构**: School of Communication and Information Engineering, Chongqing University of Posts and Telecommunications,Chongqing,China, Xi&#x0027;an Jiaotong University,Xi&#x0027;an,China
- **会议**: CVPR 2023

### CIGAR: Cross-Modality Graph Reasoning for Domain Adaptive Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02277) · 📚 被引 47
- **作者**: Yabo Liu, Jinghua Wang, Chao Huang, Yaowei Wang, Yong Xu
- **🏷️ 机构**: Harbin Institute of Technology,Shenzhen, School of Cyber Science and Technology, Shenzhen Campus of Sun Yat-sen University, Peng Cheng Laboratory
- **会议**: CVPR 2023

### Ambiguity-Resistant Semi-Supervised Learning for Dense Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01495) · 📚 被引 67
- **作者**: Chang Liu, Weiming Zhang, Xiangru Lin, Wei Zhang, Xiao Tan, Junyu Han et al.
- **🏷️ 机构**: Shanghai University, Baidu Inc
- **会议**: CVPR 2023

### MixTeacher: Mining Promising Labels with Mixed Scale Teacher for Semi-Supervised Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00712) · 📚 被引 57
- **作者**: Liang Liu, Boshen Zhang, Jiangning Zhang, Wuhao Zhang, Zhenye Gan, Guanzhong Tian et al.
- **🏷️ 机构**: Youtu Lab,Tencent, Ningbo Research Institute, Zhejiang University, Rongcheer Co., Ltd
- **会议**: CVPR 2023

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
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00313) · 📚 被引 68
- **作者**: Jiawei Ma, Yulei Niu, Jincheng Xu, Shiyuan Huang, Guangxing Han, Shih-Fu Chang
- **🏷️ 机构**: Columbia University
- **会议**: CVPR 2023

### Bridging Precision and Confidence: A Train-Time Loss for Calibrating Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01104) · 📚 被引 18
- **作者**: Muhammad Akhtar Munir, Muhammad Haris Khan, Salman H. Khan, Fahad Shahbaz Khan
- **🏷️ 机构**: Mohamed bin Zayed University of AI
- **会议**: CVPR 2023

### Multiclass Confidence and Localization Calibration for Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01890) · 📚 被引 25
- **作者**: Bimsara Pathiraja, Malitha Gunawardhana, Muhammad Haris Khan
- **🏷️ 机构**: Mohamed bin Zayed University of Artificial Intelligence,UAE
- **会议**: CVPR 2023

### Unbalanced Optimal Transport: A Unified Framework for Object Detection.
- **链接**: [arXiv:2307.02402](https://arxiv.org/abs/2307.02402) · [出版页](https://doi.org/10.1109/CVPR52729.2023.00312) · 📚 被引 12
- **作者**: Henri De Plaen, Pierre-François De Plaen, Johan A. K. Suykens, Marc Proesmans, Tinne Tuytelaars, Luc Van Gool
- **🏷️ 机构**: ESAT-STADIUS, KU,Leuven,Belgium, ESAT-PSI, KU,Leuven,Belgium
- **会议**: CVPR 2023

- **摘要（英，原文）**:

  > During training, supervised object detection tries to correctly match the predicted bounding boxes and associated classification scores to the ground truth. This is essential to determine which predictions are to be pushed towards which solutions, or to be discarded. Popular matching strategies include matching to the closest ground truth box (mostly used in combination with anchors), or matching via the Hungarian algorithm (mostly used in anchor-free methods). Each of these strategies comes with its own properties, underlying losses, and heuristics. We show how Unbalanced Optimal Transport unifies these different approaches and opens a whole continuum of methods in between. This allows for a finer selection of the desired properties. Experimentally, we show that training an object detection model with Unbalanced Optimal Transport is able to reach the state-of-the-art both in terms of Average Precision and Average Recall as well as to provide a faster initial convergence. The approach is well suited for GPU implementation, which proves to be an advantage for large-scale models.

### Modeling the Distributional Uncertainty for Salient Object Detection Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01883) · 📚 被引 32
- **作者**: Xinyu Tian, Jing Zhang, Mochu Xiang, Yuchao Dai
- **🏷️ 机构**: Northwestern Polytechnical University,China, Australian National University,Australia
- **会议**: CVPR 2023

### Instance Relation Graph Guided Source-Free Domain Adaptive Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00343) · 📚 被引 94
- **作者**: Vibashan VS, Poojan Oza, Vishal M. Patel
- **🏷️ 机构**: Johns Hopkins University,Baltimore,MD,USA
- **会议**: CVPR 2023

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
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01673) · 📚 被引 2
- **作者**: Vidit Vidit, Martin Engilberge, Mathieu Salzmann
- **🏷️ 机构**: EPFL,CVLab
- **会议**: CVPR 2023

### Learning to Detect and Segment for Open Vocabulary Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00681)
- **作者**: Tao Wang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### Generalized UAV Object Detection via Frequency Domain Disentanglement.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00109) · 📚 被引 72
- **作者**: Kunyu Wang, Xueyang Fu, Yukun Huang, Chengzhi Cao, Gege Shi, Zheng-Jun Zha
- **🏷️ 机构**: University of Science and Technology of China,China
- **会议**: CVPR 2023

### Consistent-Teacher: Towards Reducing Inconsistent Pseudo-Targets in Semi-Supervised Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00316) · 📚 被引 113
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
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01404) · 📚 被引 33
- **作者**: Jinsheng Xiao, Yuanxu Wu, Yunhua Chen, Shurui Wang, Zhongyuan Wang, Jiayi Ma
- **🏷️ 机构**: Wuhan University,China, Guangdong University of Technology,China
- **会议**: CVPR 2023

### Dynamic Coarse-to-Fine Learning for Oriented Tiny Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00707) · 📚 被引 165
- **作者**: Chang Xu, Jian Ding, Jinwang Wang, Wen Yang, Huai Yu, Lei Yu et al.
- **🏷️ 机构**: School of Electronic Information, Wuhan University, School of Computer Science, Wuhan University
- **会议**: CVPR 2023

### Gaussian Label Distribution Learning for Spherical Image Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00106) · 📚 被引 10
- **作者**: Hang Xu, Xinyuan Liu, Qiang Zhao, Yike Ma, Chenggang Yan, Feng Dai
- **🏷️ 机构**: Hangzhou Dianzi University,Hangzhou,China, Institute of Computing Technology, Chinese Academy of Sciences,Key Laboratory of Intelligent Information Processing of Chinese Academy of Sciences,Beijing,China
- **会议**: CVPR 2023

### Generating Features with Increased Crop-Related Diversity for Few-Shot Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01888) · 📚 被引 50
- **作者**: Jingyi Xu, Hieu Le, Dimitris Samaras
- **🏷️ 机构**: Stony Brook University, EPFL
- **会议**: CVPR 2023

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
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00708) · 📚 被引 309
- **作者**: Shilong Zhang, Xinjiang Wang, Jiaqi Wang, Jiangmiao Pang, Chengqi Lyu, Wenwei Zhang et al.
- **🏷️ 机构**: Shanghai AI Laboratory, SenseTime Research, The University of Hong Kong
- **会议**: CVPR 2023

### Towards Unsupervised Object Detection from LiDAR Point Clouds.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00899) · 📚 被引 39
- **作者**: Lunjun Zhang, Anqi Joyce Yang, Yuwen Xiong, Sergio Casas, Bin Yang, Mengye Ren et al.
- **🏷️ 机构**: Waabi / University of Toronto
- **会议**: CVPR 2023

### MetaFusion: Infrared and Visible Image Fusion via Meta-Feature Embedding from Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01341) · 📚 被引 239
- **作者**: Wenda Zhao, Shigeng Xie, Fan Zhao, You He, Huchuan Lu
- **🏷️ 机构**: Dalian University of Technology,China, Liaoning Normal University,China, Tsinghua University,China
- **会议**: CVPR 2023

### Texture-Guided Saliency Distilling for Unsupervised Salient Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00701) · 📚 被引 74
- **作者**: Huajun Zhou, Bo Qiao, Lingxiao Yang, Jianhuang Lai, Xiaohua Xie
- **🏷️ 机构**: School of Computer Science and Engineering, Sun Yat-sen University,China
- **会议**: CVPR 2023

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
