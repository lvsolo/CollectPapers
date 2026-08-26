# Object Detection — 2024 Guideline

> 领域: 通用 2D 目标检测（检测器架构、密集预测、小物体/旋转框/NMS 等）
> 论文数: 70 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Sparse Semi-DETR: Sparse Learnable Queries for Semi-Supervised Object Detection.
- **链接**: [arXiv:2404.01819](https://arxiv.org/abs/2404.01819) · 📚 被引 49
- **作者**: Tahira Shehzadi, Khurram Azeem Hashmi, Didier Stricker, Muhammad Zeshan Afzal
- **🏷️ 机构**: DFKI
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > In this paper, we address the limitations of the DETR-based semi-supervised object detection (SSOD) framework, particularly focusing on the challenges posed by the quality of object queries. In DETR-based SSOD, the one-to-one assignment strategy provides inaccurate pseudo-labels, while the one-to-many assignments strategy leads to overlapping predictions. These issues compromise training efficiency and degrade model performance, especially in detecting small or occluded objects. We introduce Sparse Semi-DETR, a novel transformer-based, end-to-end semi-supervised object detection solution to overcome these challenges. Sparse Semi-DETR incorporates a Query Refinement Module to enhance the quality of object queries, significantly improving detection capabilities for small and partially obscured objects. Additionally, we integrate a Reliable Pseudo-Label Filtering Module that selectively filters high-quality pseudo-labels, thereby enhancing detection accuracy and consistency. On the MS-COCO and Pascal VOC object detection benchmarks, Sparse Semi-DETR achieves a significant improvement over current state-of-the-art methods that highlight Sparse Semi-DETR's effectiveness in semi-supervised object detection, particularly in challenging scenarios involving small or partially obscured objects.

### KD-DETR: Knowledge Distillation for Detection Transformer with Consistent Distillation Points Sampling.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01516) · 📚 被引 22
- **作者**: Yu Wang, Xin Li, Shengzhao Weng, Gang Zhang, Haixiao Yue, Haocheng Feng et al.
- **🏷️ 机构**: Baidu VIS
- **会议**: CVPR 2024

### YolOOD: Utilizing Object Detection Concepts for Multi-Label Out-of-Distribution Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00553) · 📚 被引 9
- **作者**: Alon Zolfi, Guy Amit, Amit Baras, Satoru Koda, Ikuya Morikawa, Yuval Elovici et al.
- **🏷️ 机构**: Ben-Gurion University of the Negev,Israel, Fujitsu Limited,Japan
- **会议**: CVPR 2024

### Exploring Orthogonality in Open World Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01638) · 📚 被引 20
- **作者**: Zhicheng Sun, Jinghan Li, Yadong Mu
- **🏷️ 机构**: Peking University,Beijing,China
- **会议**: CVPR 2024

### Generative Region-Language Pretraining for Open-Ended Object Detection.
- **链接**: [arXiv:2403.10191](https://arxiv.org/abs/2403.10191) · [代码](https://github.com/FoundationVision/GenerateU) · 📚 被引 15
- **作者**: Chuang Lin, Yi Jiang, Lizhen Qu, Zehuan Yuan, Jianfei Cai
- **🏷️ 机构**: Monash University, ByteDance Inc.
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > In recent research, significant attention has been devoted to the open-vocabulary object detection task, aiming to generalize beyond the limited number of classes labeled during training and detect objects described by arbitrary category names at inference. Compared with conventional object detection, open vocabulary object detection largely extends the object detection categories. However, it relies on calculating the similarity between image regions and a set of arbitrary category names with a pretrained vision-and-language model. This implies that, despite its open-set nature, the task still needs the predefined object categories during the inference stage. This raises the question: What if we do not have exact knowledge of object categories during inference? In this paper, we call such a new setting as generative open-ended object detection, which is a more general and practical problem. To address it, we formulate object detection as a generative problem and propose a simple framework named GenerateU, which can detect dense objects and generate their names in a free-form way. Particularly, we employ Deformable DETR as a region proposal generator with a language model translating visual regions to object names. To assess the free-form object detection task, we introduce an evaluation method designed to quantitatively measure the performance of generative outcomes. Extensive experiments demonstrate strong zero-shot detection performance of our GenerateU. For example, on the LVIS dataset, our GenerateU achieves comparable results to the open-vocabulary object detection method GLIP, even though the category names are not seen by GenerateU during inference. Code is available at: https:// github.com/FoundationVision/GenerateU .

### RadarDistill: Boosting Radar-Based Object Detection Performance via Knowledge Distillation from LiDAR Features.
- **链接**: [arXiv:2403.05061](https://arxiv.org/abs/2403.05061) · 📚 被引 49
- **作者**: Geonho Bang, Kwangjin Choi, Jisong Kim, Dongsuk Kum, Jun Won Choi
- **🏷️ 机构**: Hanyang University,Korea, KAIST,Korea, Seoul National University,Korea
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > The inherent noisy and sparse characteristics of radar data pose challenges in finding effective representations for 3D object detection. In this paper, we propose RadarDistill, a novel knowledge distillation (KD) method, which can improve the representation of radar data by leveraging LiDAR data. RadarDistill successfully transfers desirable characteristics of LiDAR features into radar features using three key components: Cross-Modality Alignment (CMA), Activation-based Feature Distillation (AFD), and Proposal-based Feature Distillation (PFD). CMA enhances the density of radar features by employing multiple layers of dilation operations, effectively addressing the challenge of inefficient knowledge transfer from LiDAR to radar. AFD selectively transfers knowledge based on regions of the LiDAR features, with a specific focus on areas where activation intensity exceeds a predefined threshold. PFD similarly guides the radar network to selectively mimic features from the LiDAR network within the object proposals. Our comparative analyses conducted on the nuScenes datasets demonstrate that RadarDistill achieves state-of-the-art (SOTA) performance for radar-only object detection task, recording 20.5% in mAP and 43.7% in NDS. Also, RadarDistill significantly improves the performance of the camera-radar fusion model.

### GLOW: Global Layout Aware Attacks on Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01146) · 📚 被引 1
- **作者**: Jun Bao, Buyu Liu, Kui Ren, Jun Yu
- **🏷️ 机构**: The State Key Laboratory of Blockchain and Data Security, Zhejiang University, Hangzhou Dianzi University
- **会议**: CVPR 2024

### RadSimReal: Bridging the Gap Between Synthetic and Real Data in Radar Object Detection With Simulation.
- **链接**: [arXiv:2404.18150](https://arxiv.org/abs/2404.18150) · 📚 被引 11
- **作者**: Oded Bialer, Yuval Haitman
- **🏷️ 机构**: General Motors, Technical Center Israel
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Object detection in radar imagery with neural networks shows great potential for improving autonomous driving. However, obtaining annotated datasets from real radar images, crucial for training these networks, is challenging, especially in scenarios with long-range detection and adverse weather and lighting conditions where radar performance excels. To address this challenge, we present RadSimReal, an innovative physical radar simulation capable of generating synthetic radar images with accompanying annotations for various radar types and environmental conditions, all without the need for real data collection. Remarkably, our findings demonstrate that training object detection models on RadSimReal data and subsequently evaluating them on real-world data produce performance levels comparable to models trained and tested on real data from the same dataset, and even achieves better performance when testing across different real datasets. RadSimReal offers advantages over other physical radar simulations that it does not necessitate knowledge of the radar design details, which are often not disclosed by radar suppliers, and has faster run-time. This innovative tool has the potential to advance the development of computer vision algorithms for radar-based autonomous driving applications.

### Overload: Latency Attacks on Object Detection for Edge Devices.
- **链接**: [arXiv:2304.05370](https://arxiv.org/abs/2304.05370) · 📚 被引 17
- **作者**: Erh-Chung Chen, Pin-Yu Chen, I-Hsin Chung, Che-Rung Lee
- **🏷️ 机构**: National Tsing Hua University, IBM Research
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Nowadays, the deployment of deep learning-based applications is an essential task owing to the increasing demands on intelligent services. In this paper, we investigate latency attacks on deep learning applications. Unlike common adversarial attacks for misclassification, the goal of latency attacks is to increase the inference time, which may stop applications from responding to the requests within a reasonable time. This kind of attack is ubiquitous for various applications, and we use object detection to demonstrate how such kind of attacks work. We also design a framework named Overload to generate latency attacks at scale. Our method is based on a newly formulated optimization problem and a novel technique, called spatial attention. This attack serves to escalate the required computing costs during the inference time, consequently leading to an extended inference time for object detection. It presents a significant threat, especially to systems with limited computing resources. We conducted experiments using YOLOv5 models on Nvidia NX. Compared to existing methods, our method is simpler and more effective. The experimental results show that with latency attacks, the inference time of a single image can be increased ten times longer in reference to the normal setting. Moreover, our findings pose a potential new threat to all object detection tasks requiring non-maximum suppression (NMS), as our attack is NMS-agnostic.

### YOLO-World: Real-Time Open-Vocabulary Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01599)
- **作者**: Tianheng Cheng, Lin Song, Yixiao Ge, Wenyu Liu, Xinggang Wang, Ying Shan
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### Improving Single Domain-Generalized Object Detection: A Focus on Diversification and Alignment.
- **链接**: [arXiv:2405.14497](https://arxiv.org/abs/2405.14497) · [代码](https://github.com/msohaildanish/DivAlign) · 📚 被引 27
- **作者**: Muhammad Sohail Danish, Muhammad Haris Khan, Muhammad Akhtar Munir, M. Saquib Sarfraz, Mohsen Ali
- **🏷️ 机构**: Mohamed bin Zayed University of Artificial Intelligence, Mercedes-Benz Tech Innovation, Information Technology, University of Punjab
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > In this work, we tackle the problem of domain generalization for object detection, specifically focusing on the scenario where only a single source domain is available. We propose an effective approach that involves two key steps: diversifying the source domain and aligning detections based on class prediction confidence and localization. Firstly, we demonstrate that by carefully selecting a set of augmentations, a base detector can outperform existing methods for single domain generalization by a good margin. This highlights the importance of domain diversification in improving the performance of object detectors. Secondly, we introduce a method to align detections from multiple views, considering both classification and localization outputs. This alignment procedure leads to better generalized and well-calibrated object detector models, which are crucial for accurate decision-making in safety-critical applications. Our approach is detector-agnostic and can be seamlessly applied to both single-stage and two-stage detectors. To validate the effectiveness of our proposed methods, we conduct extensive experiments and ablations on challenging domain-shift scenarios. The results consistently demonstrate the superiority of our approach compared to existing methods. Our code and models are available at: https://github.com/msohaildanish/DivAlign

### D3T: Distinctive Dual-Domain Teacher Zigzagging Across RGB-Thermal Gap for Domain-Adaptive Object Detection.
- **链接**: [arXiv:2403.09359](https://arxiv.org/abs/2403.09359) · [代码](https://github.com/EdwardDo69/D3T) · 📚 被引 18
- **作者**: Dinh Phat Do, Taehoon Kim, Jaemin Na, Jiwon Kim, Keonho Lee, Kyunghwan Cho et al.
- **🏷️ 机构**: Ajou University,Korea, Hyundai Motor Company,Robotics Lab
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Domain adaptation for object detection typically entails transferring knowledge from one visible domain to another visible domain. However, there are limited studies on adapting from the visible to the thermal domain, because the domain gap between the visible and thermal domains is much larger than expected, and traditional domain adaptation can not successfully facilitate learning in this situation. To overcome this challenge, we propose a Distinctive Dual-Domain Teacher (D3T) framework that employs distinct training paradigms for each domain. Specifically, we segregate the source and target training sets for building dual-teachers and successively deploy exponential moving average to the student model to individual teachers of each domain. The framework further incorporates a zigzag learning method between dual teachers, facilitating a gradual transition from the visible to thermal domains during training. We validate the superiority of our method through newly designed experimental protocols with well-known thermal datasets, i.e., FLIR and KAIST. Source code is available at https://github.com/EdwardDo69/D3T .

### Boosting Object Detection with Zero-Shot Day-Night Domain Adaptation.
- **链接**: [arXiv:2312.01220](https://arxiv.org/abs/2312.01220) · [代码](https://github.com/ZPDu/DAI-Net) · 📚 被引 70
- **作者**: Zhipeng Du, Miaojing Shi, Jiankang Deng
- **🏷️ 机构**: King&#x0027;s College,Department of Informatics,London, College of Electronic and Information Engineering, Tongji University, Imperial College,Department of Computing,London
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Detecting objects in low-light scenarios presents a persistent challenge, as detectors trained on well-lit data exhibit significant performance degradation on low-light data due to low visibility. Previous methods mitigate this issue by exploring image enhancement or object detection techniques with real low-light image datasets. However, the progress is impeded by the inherent difficulties about collecting and annotating low-light images. To address this challenge, we propose to boost low-light object detection with zero-shot day-night domain adaptation, which aims to generalize a detector from well-lit scenarios to low-light ones without requiring real low-light data. Revisiting Retinex theory in the low-level vision, we first design a reflectance representation learning module to learn Retinex-based illumination invariance in images with a carefully designed illumination invariance reinforcement strategy. Next, an interchange-redecomposition-coherence procedure is introduced to improve over the vanilla Retinex image decomposition process by performing two sequential image decompositions and introducing a redecomposition cohering loss. Extensive experiments on ExDark, DARK FACE, and CODaN datasets show strong low-light generalizability of our method. Our code is available at https://github.com/ZPDu/DAI-Net.

### InstaGen: Enhancing Object Detection by Training on Synthetic Dataset.
- **链接**: [arXiv:2402.05937](https://arxiv.org/abs/2402.05937) · 📚 被引 27
- **作者**: Chengjian Feng, Yujie Zhong, Zequn Jie, Weidi Xie, Lin Ma
- **🏷️ 机构**: Meituan Inc., CMIC, Shanghai Jiao Tong University
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > In this paper, we present a novel paradigm to enhance the ability of object detector, e.g., expanding categories or improving detection performance, by training on synthetic dataset generated from diffusion models. Specifically, we integrate an instance-level grounding head into a pre-trained, generative diffusion model, to augment it with the ability of localising instances in the generated images. The grounding head is trained to align the text embedding of category names with the regional visual feature of the diffusion model, using supervision from an off-the-shelf object detector, and a novel self-training scheme on (novel) categories not covered by the detector. We conduct thorough experiments to show that, this enhanced version of diffusion model, termed as InstaGen, can serve as a data synthesizer, to enhance object detectors by training on its generated samples, demonstrating superior performance over existing state-of-the-art methods in open-vocabulary (+4.5 AP) and data-sparse (+1.2 to 5.2 AP) scenarios. Project page with code: https://fcjian.github.io/InstaGen.

### Few-Shot Object Detection with Foundation Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02703) · 📚 被引 63
- **作者**: Guangxing Han, Ser-Nam Lim
- **🏷️ 机构**: Columbia University, University of Central Florida
- **会议**: CVPR 2024

### Endow SAM with Keen Eyes: Temporal-Spatial Prompt Learning for Video Camouflaged Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01803) · 📚 被引 22
- **作者**: Wenjun Hui, Zhenfeng Zhu, Shuai Zheng, Yao Zhao
- **🏷️ 机构**: Institute of Information Science, Beijing Jiaotong University
- **会议**: CVPR 2024

### CAT: Exploiting Inter-Class Dynamics for Domain Adaptive Object Detection.
- **链接**: [arXiv:2403.19278](https://arxiv.org/abs/2403.19278) · 📚 被引 46
- **作者**: Mikhail Kennerley, Jian-Gang Wang, Bharadwaj Veeravalli, Robby T. Tan
- **🏷️ 机构**: National University of Singapore,Department of Electrical and Computer Engineering, Institute for Infocomm Research,A*STAR, ASUS Intelligent Cloud Services
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Domain adaptive object detection aims to adapt detection models to domains where annotated data is unavailable. Existing methods have been proposed to address the domain gap using the semi-supervised student-teacher framework. However, a fundamental issue arises from the class imbalance in the labelled training set, which can result in inaccurate pseudo-labels. The relationship between classes, especially where one class is a majority and the other minority, has a large impact on class bias. We propose Class-Aware Teacher (CAT) to address the class bias issue in the domain adaptation setting. In our work, we approximate the class relationships with our Inter-Class Relation module (ICRm) and exploit it to reduce the bias within the model. In this way, we are able to apply augmentations to highly related classes, both inter- and intra-domain, to boost the performance of minority classes while having minimal impact on majority classes. We further reduce the bias by implementing a class-relation weight to our classification loss. Experiments conducted on various datasets and ablation studies show that our method is able to address the class bias in the domain adaptation setting. On the Cityscapes to Foggy Cityscapes dataset, we attained a 52.5 mAP, a substantial improvement over the 51.2 mAP achieved by the state-of-the-art method.

### Retrieval-Augmented Open-Vocabulary Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01650)
- **作者**: Jooyeon Kim, Eulrang Cho, Sehyung Kim, Hyunwoo J. Kim
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### SDDGR: Stable Diffusion-Based Deep Generative Replay for Class Incremental Object Detection.
- **链接**: [arXiv:2402.17323](https://arxiv.org/abs/2402.17323) · 📚 被引 44
- **作者**: Junsu Kim, Hoseong Cho, Jihyeon Kim, Yihalem Yimolal Tiruneh, Seungryul Baek
- **🏷️ 机构**: UNIST
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > In the field of class incremental learning (CIL), generative replay has become increasingly prominent as a method to mitigate the catastrophic forgetting, alongside the continuous improvements in generative models. However, its application in class incremental object detection (CIOD) has been significantly limited, primarily due to the complexities of scenes involving multiple labels. In this paper, we propose a novel approach called stable diffusion deep generative replay (SDDGR) for CIOD. Our method utilizes a diffusion-based generative model with pre-trained text-to-diffusion networks to generate realistic and diverse synthetic images. SDDGR incorporates an iterative refinement strategy to produce high-quality images encompassing old classes. Additionally, we adopt an L2 knowledge distillation technique to improve the retention of prior knowledge in synthetic images. Furthermore, our approach includes pseudo-labeling for old objects within new task images, preventing misclassification as background elements. Extensive experiments on the COCO 2017 dataset demonstrate that SDDGR significantly outperforms existing algorithms, achieving a new state-of-the-art in various CIOD scenarios. The source code will be made available to the public.

### Unleashing Channel Potential: Space-Frequency Selection Convolution for SAR Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01640) · 📚 被引 78
- **作者**: Ke Li, Di Wang, Zhangyuan Hu, Wenxuan Zhu, Shaofeng Li, Quan Wang
- **🏷️ 机构**: School of Computer Science and Technology, Xidian University,Xi&#x2019; an,China
- **会议**: CVPR 2024

### Learning Background Prompts to Discover Implicit Knowledge for Open Vocabulary Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01578)
- **作者**: Jiaming Li, Jiacheng Zhang, Jichang Li, Ge Li, Si Liu, Liang Lin et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### SHiNe: Semantic Hierarchy Nexus for Open-Vocabulary Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01574)
- **作者**: Mingxuan Liu, Tyler L. Hayes, Elisa Ricci, Gabriela Csurka, Riccardo Volpi
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### Unbiased Faster R-CNN for Single-source Domain Generalized Object Detection.
- **链接**: [arXiv:2405.15225](https://arxiv.org/abs/2405.15225) · 📚 被引 50
- **作者**: Yajing Liu, Shijun Zhou, Xiyao Liu, Chunhui Hao, Baojie Fan, Jiandong Tian
- **🏷️ 机构**: Shenyang Institute of Automation, Chinese Academy of Sciences,State Key Laboratory of Robotics, Nanjing University of Posts and Telecommunications
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Single-source domain generalization (SDG) for object detection is a challenging yet essential task as the distribution bias of the unseen domain degrades the algorithm performance significantly. However, existing methods attempt to extract domain-invariant features, neglecting that the biased data leads the network to learn biased features that are non-causal and poorly generalizable. To this end, we propose an Unbiased Faster R-CNN (UFR) for generalizable feature learning. Specifically, we formulate SDG in object detection from a causal perspective and construct a Structural Causal Model (SCM) to analyze the data bias and feature bias in the task, which are caused by scene confounders and object attribute confounders. Based on the SCM, we design a Global-Local Transformation module for data augmentation, which effectively simulates domain diversity and mitigates the data bias. Additionally, we introduce a Causal Attention Learning module that incorporates a designed attention invariance loss to learn image-level features that are robust to scene confounders. Moreover, we develop a Causal Prototype Learning module with an explicit instance constraint and an implicit prototype constraint, which further alleviates the negative impact of object attribute confounders. Experimental results on five scenes demonstrate the prominent generalization ability of our method, with an improvement of 3.9% mAP on the Night-Clear scene.

### PointOBB: Learning Oriented Object Detection via Single Point Supervision.
- **链接**: [arXiv:2311.14757](https://arxiv.org/abs/2311.14757) · 📚 被引 52
- **作者**: Junwei Luo, Xue Yang, Yi Yu, Qingyun Li, Junchi Yan, Yansheng Li
- **🏷️ 机构**: Wuhan University, Southeast University, Harbin Institute of Technology
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Single point-supervised object detection is gaining attention due to its cost-effectiveness. However, existing approaches focus on generating horizontal bounding boxes (HBBs) while ignoring oriented bounding boxes (OBBs) commonly used for objects in aerial images. This paper proposes PointOBB, the first single Point-based OBB generation method, for oriented object detection. PointOBB operates through the collaborative utilization of three distinctive views: an original view, a resized view, and a rotated/flipped (rot/flp) view. Upon the original view, we leverage the resized and rot/flp views to build a scale augmentation module and an angle acquisition module, respectively. In the former module, a Scale-Sensitive Consistency (SSC) loss is designed to enhance the deep network's ability to perceive the object scale. For accurate object angle predictions, the latter module incorporates self-supervised learning to predict angles, which is associated with a scale-guided Dense-to-Sparse (DS) matching strategy for aggregating dense angles corresponding to sparse objects. The resized and rot/flp views are switched using a progressive multi-view switching strategy during training to achieve coupled optimization of scale and angle. Experimental results on the DIOR-R and DOTA-v1.0 datasets demonstrate that PointOBB achieves promising performance, and significantly outperforms potential point-supervised baselines.

### VSCode: General Visual Salient and Camouflaged Object Detection with 2D Prompt Learning.
- **链接**: [arXiv:2311.15011](https://arxiv.org/abs/2311.15011) · [代码](https://github.com/Sssssuperior/VSCode) · 📚 被引 128
- **作者**: Ziyang Luo, Nian Liu, Wangbo Zhao, Xuguang Yang, Dingwen Zhang, Deng-Ping Fan et al.
- **🏷️ 机构**: Northwestern Polytechnical University, Mohamed bin Zayed University of Artificial Intelligence, National University of Singapore
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Salient object detection (SOD) and camouflaged object detection (COD) are related yet distinct binary mapping tasks. These tasks involve multiple modalities, sharing commonalities and unique cues. Existing research often employs intricate task-specific specialist models, potentially leading to redundancy and suboptimal results. We introduce VSCode, a generalist model with novel 2D prompt learning, to jointly address four SOD tasks and three COD tasks. We utilize VST as the foundation model and introduce 2D prompts within the encoder-decoder architecture to learn domain and task-specific knowledge on two separate dimensions. A prompt discrimination loss helps disentangle peculiarities to benefit model optimization. VSCode outperforms state-of-the-art methods across six tasks on 26 datasets and exhibits zero-shot generalization to unseen tasks by combining 2D prompts, such as RGB-D COD. Source code has been available at https://github.com/Sssssuperior/VSCode.

### Active Domain Adaptation with False Negative Prediction for Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02719) · 📚 被引 10
- **作者**: Yuzuru Nakamura, Yasunori Ishii, Takayoshi Yamashita
- **🏷️ 机构**: Panasonic Holdings Corporation, Chubu University
- **会议**: CVPR 2024

### Neural Exposure Fusion for High-Dynamic Range Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01663) · 📚 被引 12
- **作者**: Emmanuel Onzon, Maximilian Bömer, Fahim Mannan, Felix Heide
- **🏷️ 机构**: Torc Robotics
- **会议**: CVPR 2024

### Scene Adaptive Sparse Transformer for Event-based Object Detection.
- **链接**: [arXiv:2404.01882](https://arxiv.org/abs/2404.01882) · [代码](https://github.com/Peterande/SAST) · 📚 被引 42
- **作者**: Yansong Peng, Hebei Li, Yueyi Zhang, Xiaoyan Sun, Feng Wu
- **🏷️ 机构**: University of Science and Technology of China
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > While recent Transformer-based approaches have shown impressive performances on event-based object detection tasks, their high computational costs still diminish the low power consumption advantage of event cameras. Image-based works attempt to reduce these costs by introducing sparse Transformers. However, they display inadequate sparsity and adaptability when applied to event-based object detection, since these approaches cannot balance the fine granularity of token-level sparsification and the efficiency of window-based Transformers, leading to reduced performance and efficiency. Furthermore, they lack scene-specific sparsity optimization, resulting in information loss and a lower recall rate. To overcome these limitations, we propose the Scene Adaptive Sparse Transformer (SAST). SAST enables window-token co-sparsification, significantly enhancing fault tolerance and reducing computational overhead. Leveraging the innovative scoring and selection modules, along with the Masked Sparse Window Self-Attention, SAST showcases remarkable scene-aware adaptability: It focuses only on important objects and dynamically optimizes sparsity level according to scene complexity, maintaining a remarkable balance between performance and computational cost. The evaluation results show that SAST outperforms all other dense and sparse networks in both performance and efficiency on two large-scale event-based object detection datasets (1Mpx and Gen1). Code: https://github.com/Peterande/SAST

### CrossKD: Cross-Head Knowledge Distillation for Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01563) · 📚 被引 119
- **作者**: Jiabao Wang, Yuming Chen, Zhaohui Zheng, Xiang Li, Ming-Ming Cheng, Qibin Hou
- **🏷️ 机构**: College of Computer Science, Nankai University,VCIP, NKIARI,Shenzhen Futian
- **会议**: CVPR 2024

### A-Teacher: Asymmetric Network for 3D Semi-Supervised Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01419) · 📚 被引 8
- **作者**: Hanshi Wang, Zhipeng Zhang, Jin Gao, Weiming Hu
- **🏷️ 机构**: CASIA,State Key Laboratory of Multimodal Artificial Intelligence Systems (MAIS), KargoBot
- **会议**: CVPR 2024

### SNIDA: Unlocking Few-Shot Object Detection with Non-Linear Semantic Decoupling Augmentation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01192) · 📚 被引 31
- **作者**: Yanjie Wang, Xu Zou, Luxin Yan, Sheng Zhong, Jiahuan Zhou
- **🏷️ 机构**: Huazhong University of Science and Technology,Wuhan,China,430074, Wangxuan Institute of Computer Technology, Peking University,Beijing,China,100871
- **会议**: CVPR 2024

### LEOD: Label-Efficient Object Detection for Event Cameras.
- **链接**: [arXiv:2311.17286](https://arxiv.org/abs/2311.17286) · [代码](https://github.com/Wuziyi616/LEOD) · 📚 被引 17
- **作者**: Ziyi Wu, Mathias Gehrig, Qing Lyu, Xudong Liu, Igor Gilitschenski
- **🏷️ 机构**: University of Toronto, University of Zurich
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Object detection with event cameras benefits from the sensor's low latency and high dynamic range. However, it is costly to fully label event streams for supervised training due to their high temporal resolution. To reduce this cost, we present LEOD, the first method for label-efficient event-based detection. Our approach unifies weakly- and semi-supervised object detection with a self-training mechanism. We first utilize a detector pre-trained on limited labels to produce pseudo ground truth on unlabeled events. Then, the detector is re-trained with both real and generated labels. Leveraging the temporal consistency of events, we run bi-directional inference and apply tracking-based post-processing to enhance the quality of pseudo labels. To stabilize training against label noise, we further design a soft anchor assignment strategy. We introduce new experimental protocols to evaluate the task of label-efficient event-based detection on Gen1 and 1Mpx datasets. LEOD consistently outperforms supervised baselines across various labeling ratios. For example, on Gen1, it improves mAP by 8.6% and 7.8% for RVT-S trained with 1% and 2% labels. On 1Mpx, RVT-S with 10% labels even surpasses its fully-supervised counterpart using 100% labels. LEOD maintains its effectiveness even when all labeled data are available, reaching new state-of-the-art results. Finally, we show that our method readily scales to improve larger detectors as well. Code is released at https://github.com/Wuziyi616/LEOD

### Relational Matching for Weakly Semi-Supervised Oriented Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02626) · 📚 被引 13
- **作者**: Wenhao Wu, Hau-San Wong, Si Wu, Tianyou Zhang
- **🏷️ 机构**: City University of Hong Kong,Department of Computer Science, School of Computer Science and Engineering, South China University of Technology
- **会议**: CVPR 2024

### Rethinking Boundary Discontinuity Problem for Oriented Object Detection.
- **链接**: [arXiv:2305.10061](https://arxiv.org/abs/2305.10061) · [代码](https://github.com/hangxu-cv/cvpr24acm) · 📚 被引 43
- **作者**: Hang Xu, Xinyuan Liu, Haonan Xu, Yike Ma, Zunjie Zhu, Chenggang Yan et al.
- **🏷️ 机构**: Hangzhou Dianzi University,Hangzhou,China, Institute of Computing Technology, Chinese Academy of Sciences,Beijing,China
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Oriented object detection has been developed rapidly in the past few years, where rotation equivariance is crucial for detectors to predict rotated boxes. It is expected that the prediction can maintain the corresponding rotation when objects rotate, but severe mutation in angular prediction is sometimes observed when objects rotate near the boundary angle, which is well-known boundary discontinuity problem. The problem has been long believed to be caused by the sharp loss increase at the angular boundary, and widely used joint-optim IoU-like methods deal with this problem by loss-smoothing. However, we experimentally find that even state-of-the-art IoU-like methods actually fail to solve the problem. On further analysis, we find that the key to solution lies in encoding mode of the smoothing function rather than in joint or independent optimization. In existing IoU-like methods, the model essentially attempts to fit the angular relationship between box and object, where the break point at angular boundary makes the predictions highly unstable.To deal with this issue, we propose a dual-optimization paradigm for angles. We decouple reversibility and joint-optim from single smoothing function into two distinct entities, which for the first time achieves the objectives of both correcting angular boundary and blending angle with other parameters.Extensive experiments on multiple datasets show that boundary discontinuity problem is well-addressed. Moreover, typical IoU-like methods are improved to the same level without obvious performance gap. The code is available at https://github.com/hangxu-cv/cvpr24acm.

### Plug and Play Active Learning for Object Detection.
- **链接**: [arXiv:2211.11612](https://arxiv.org/abs/2211.11612) · [代码](https://github.com/ChenhongyiYang/PPAL) · 📚 被引 37
- **作者**: Chenhongyi Yang, Lichao Huang, Elliot J. Crowley
- **🏷️ 机构**: School of Engineering, University of Edinburgh, Horizon Robotics
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Annotating datasets for object detection is an expensive and time-consuming endeavor. To minimize this burden, active learning (AL) techniques are employed to select the most informative samples for annotation within a constrained "annotation budget". Traditional AL strategies typically rely on model uncertainty or sample diversity for query sampling, while more advanced methods have focused on developing AL-specific object detector architectures to enhance performance. However, these specialized approaches are not readily adaptable to different object detectors due to the significant engineering effort required for integration. To overcome this challenge, we introduce Plug and Play Active Learning (PPAL), a simple and effective AL strategy for object detection. PPAL is a two-stage method comprising uncertainty-based and diversity-based sampling phases. In the first stage, our Difficulty Calibrated Uncertainty Sampling leverage a category-wise difficulty coefficient that combines both classification and localisation difficulties to re-weight instance uncertainties, from which we sample a candidate pool for the subsequent diversity-based sampling. In the second stage, we propose Category Conditioned Matching Similarity to better compute the similarities of multi-instance images as ensembles of their instance similarities, which is used by the k-Means++ algorithm to sample the final AL queries. PPAL makes no change to model architectures or detector training pipelines; hence it can be easily generalized to different object detectors. We benchmark PPAL on the MS-COCO and Pascal VOC datasets using different detector architectures and show that our method outperforms prior work by a large margin. Code is available at https://github.com/ChenhongyiYang/PPAL

### Active Object Detection with Knowledge Aggregation and Distillation from Large Models.
- **链接**: [arXiv:2405.12509](https://arxiv.org/abs/2405.12509) · 📚 被引 9
- **作者**: Dejie Yang, Yang Liu
- **🏷️ 机构**: Wangxuan Institute of Computer Technology, Peking University
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Accurately detecting active objects undergoing state changes is essential for comprehending human interactions and facilitating decision-making. The existing methods for active object detection (AOD) primarily rely on visual appearance of the objects within input, such as changes in size, shape and relationship with hands. However, these visual changes can be subtle, posing challenges, particularly in scenarios with multiple distracting no-change instances of the same category. We observe that the state changes are often the result of an interaction being performed upon the object, thus propose to use informed priors about object related plausible interactions (including semantics and visual appearance) to provide more reliable cues for AOD. Specifically, we propose a knowledge aggregation procedure to integrate the aforementioned informed priors into oracle queries within the teacher decoder, offering more object affordance commonsense to locate the active object. To streamline the inference process and reduce extra knowledge inputs, we propose a knowledge distillation approach that encourages the student decoder to mimic the detection capabilities of the teacher decoder using the oracle query by replicating its predictions and attention. Our proposed framework achieves state-of-the-art performance on four datasets, namely Ego4D, Epic-Kitchens, MECCANO, and 100DOH, which demonstrates the effectiveness of our approach in improving AOD.

### DetCLIPv3: Towards Versatile Generative Open-Vocabulary Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02586)
- **作者**: Lewei Yao, Renjie Pi, Jianhua Han, Xiaodan Liang, Hang Xu, Wei Zhang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### Point2RBox: Combine Knowledge from Synthetic Visual Patterns for End-to-End Oriented Object Detection with Single Point Supervision.
- **链接**: [arXiv:2311.14758](https://arxiv.org/abs/2311.14758) · 📚 被引 41
- **作者**: Yi Yu, Xue Yang, Qingyun Li, Feipeng Da, Jifeng Dai, Yu Qiao et al.
- **🏷️ 机构**: Southeast University, Shanghai AI Laboratory, Harbin Institute of Technology
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > With the rapidly increasing demand for oriented object detection (OOD), recent research involving weakly-supervised detectors for learning rotated box (RBox) from the horizontal box (HBox) has attracted more and more attention. In this paper, we explore a more challenging yet label-efficient setting, namely single point-supervised OOD, and present our approach called Point2RBox. Specifically, we propose to leverage two principles: 1) Synthetic pattern knowledge combination: By sampling around each labeled point on the image, we spread the object feature to synthetic visual patterns with known boxes to provide the knowledge for box regression. 2) Transform self-supervision: With a transformed input image (e.g. scaled/rotated), the output RBoxes are trained to follow the same transformation so that the network can perceive the relative size/rotation between objects. The detector is further enhanced by a few devised techniques to cope with peripheral issues, e.g. the anchor/layer assignment as the size of the object is not available in our point supervision setting. To our best knowledge, Point2RBox is the first end-to-end solution for point-supervised OOD. In particular, our method uses a lightweight paradigm, yet it achieves a competitive performance among point-supervised alternatives, 41.05%/27.62%/80.01% on DOTA/DIOR/HRSC datasets.

### Exploring Region-Word Alignment in Built-in Detector for Open-Vocabulary Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01606)
- **作者**: Heng Zhang, Qiuyu Zhao, Linyu Zheng, Hao Zeng, Zhiwei Ge, Tianhao Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### DETRs Beat YOLOs on Real-time Object Detection.
- **链接**: [arXiv:2304.08069](https://arxiv.org/abs/2304.08069) · 📚 被引 4123
- **作者**: Yian Zhao, Wenyu Lv, Shangliang Xu, Jinman Wei, Guanzhong Wang, Qingqing Dang et al.
- **🏷️ 机构**: Baidu Inc,Beijing,China, School of Electronic and Computer Engineering, Peking University,Shenzhen,China
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > The YOLO series has become the most popular framework for real-time object detection due to its reasonable trade-off between speed and accuracy. However, we observe that the speed and accuracy of YOLOs are negatively affected by the NMS. Recently, end-to-end Transformer-based detectors (DETRs) have provided an alternative to eliminating NMS. Nevertheless, the high computational cost limits their practicality and hinders them from fully exploiting the advantage of excluding NMS. In this paper, we propose the Real-Time DEtection TRansformer (RT-DETR), the first real-time end-to-end object detector to our best knowledge that addresses the above dilemma. We build RT-DETR in two steps, drawing on the advanced DETR: first we focus on maintaining accuracy while improving speed, followed by maintaining speed while improving accuracy. Specifically, we design an efficient hybrid encoder to expeditiously process multi-scale features by decoupling intra-scale interaction and cross-scale fusion to improve speed. Then, we propose the uncertainty-minimal query selection to provide high-quality initial queries to the decoder, thereby improving accuracy. In addition, RT-DETR supports flexible speed tuning by adjusting the number of decoder layers to adapt to various scenarios without retraining. Our RT-DETR-R50 / R101 achieves 53.1% / 54.3% AP on COCO and 108 / 74 FPS on T4 GPU, outperforming previously advanced YOLOs in both speed and accuracy. We also develop scaled RT-DETRs that outperform the lighter YOLO detectors (S and M models). Furthermore, RT-DETR-R50 outperforms DINO-R50 by 2.2% AP in accuracy and about 21 times in FPS. After pre-training with Objects365, RT-DETR-R50 / R101 achieves 55.3% / 56.2% AP. The project page: https://zhao-yian.github.io/RTDETR.

### Taming Self-Training for Open-Vocabulary Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01322)
- **作者**: Shiyu Zhao, Samuel Schulter, Long Zhao, Zhixing Zhang, B. G. Vijay Kumar, Yumin Suh et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### CRKD: Enhanced Camera-Radar Object Detection with Cross-Modality Knowledge Distillation.
- **链接**: [arXiv:2403.19104](https://arxiv.org/abs/2403.19104) · 📚 被引 35
- **作者**: Lingjun Zhao, Jingyu Song, Katherine A. Skinner
- **🏷️ 机构**: University of Michigan,Ann Arbor,MI,USA
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > In the field of 3D object detection for autonomous driving, LiDAR-Camera (LC) fusion is the top-performing sensor configuration. Still, LiDAR is relatively high cost, which hinders adoption of this technology for consumer automobiles. Alternatively, camera and radar are commonly deployed on vehicles already on the road today, but performance of Camera-Radar (CR) fusion falls behind LC fusion. In this work, we propose Camera-Radar Knowledge Distillation (CRKD) to bridge the performance gap between LC and CR detectors with a novel cross-modality KD framework. We use the Bird's-Eye-View (BEV) representation as the shared feature space to enable effective knowledge distillation. To accommodate the unique cross-modality KD path, we propose four distillation losses to help the student learn crucial features from the teacher model. We present extensive evaluations on the nuScenes dataset to demonstrate the effectiveness of the proposed CRKD framework. The project page for CRKD is https://song-jingyu.github.io/CRKD.

## 跨领域论文（完整笔记在其他领域）

- Enhancing 3D Object Detection with 2D Detection-Guided Query Anchors. → [3d-detection](../3d-detection/Guideline%202024.md)
- Towards Robust 3D Object Detection with LiDAR and 4D Radar Fusion in Various Weather Conditions. → [3d-detection](../3d-detection/Guideline%202024.md)
- Weakly Misalignment-Free Adaptive Feature Alignment for UAVs-Based Multimodal Object Detection. → [multimodal](../multimodal/Guideline%202024.md)
- Weak-to-Strong 3D Object Detection with X-Ray Distillation. → [3d-detection](../3d-detection/Guideline%202024.md)
- PTT: Point-Trajectory Transformer for Efficient Temporal 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- GAFusion: Adaptive Fusing LiDAR and Camera with Multiple Guidance for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- BEVNeXt: Reviving Dense BEV Frameworks for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- UniMODE: Unified Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- AIDE: An Automatic Data Engine for Object Detection in Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202024.md)
- RCBEVDet: Radar-Camera Fusion in Bird's Eye View for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- VSRD: Instance-Aware Volumetric Silhouette Rendering for Weakly Supervised 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- Multi-View Attentive Contextualization for Multi-View 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- Learning Occupancy for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- MonoDiff: Monocular 3D Object Detection and Pose Estimation with Diffusion Models. → [3d-detection](../3d-detection/Guideline%202024.md)
- CN-RMA: Combined Network with Ray Marching Aggregation for 3D Indoor Object Detection from Multi-View Images. → [multi-camera-perception](../multi-camera-perception/Guideline%202024.md)
- BEVSpread: Spread Voxel Pooling for Bird's-Eye-View Representation in Vision-Based Roadside 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- Commonsense Prototype for Outdoor Unsupervised 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- HINTED: Hard Instance Enhanced Detector with Mixed-Density Feature Fusion for Sparsely-Supervised 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- 3DiffTection: 3D Object Detection with Geometry-Aware Diffusion Features. → [3d-detection](../3d-detection/Guideline%202024.md)
- MonoCD: Monocular 3D Object Detection with Complementary Depths. → [3d-detection](../3d-detection/Guideline%202024.md)
- Improving Distant 3D Object Detection Using 2D Box Supervision. → [3d-detection](../3d-detection/Guideline%202024.md)
- IS-Fusion: Instance-Scene Collaborative Fusion for Multimodal 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- Pseudo Label Refinery for Unsupervised Domain Adaptation on Cross-Dataset 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- SAFDNet: A Simple and Effective Network for Fully Sparse 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- CaKDP: Category-Aware Knowledge Distillation and Pruning Framework for Lightweight 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- Decoupled Pseudo-Labeling for Semi-Supervised Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- Prompt3D: Random Prompt Assisted Weakly-Supervised 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- Scene-adaptive and Region-aware Multi-modal Prompt for Open Vocabulary Object Detection. → [multimodal](../multimodal/Guideline%202024.md)
