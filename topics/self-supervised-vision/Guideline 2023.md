# Self-supervised Vision — 2023 Guideline

> 领域: 视觉自监督学习（对比学习、MAE、DINO 系）
> 论文数: 60 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### GD-MAE: Generative Decoder for MAE Pre-Training on LiDAR Point Clouds.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00907) · 📚 被引 71
- **作者**: Honghui Yang, Tong He, Jiaheng Liu, Hua Chen, Boxi Wu, Binbin Lin et al.
- **🏷️ 机构**: Zhejiang University,State Key Lab of CAD&#x0026;CG, Shanghai AI Laboratory, COMAC Beijing Aircraft Technology Research Institute
- **会议**: CVPR 2023

### DeepMapping2: Self-Supervised Large-Scale LiDAR Map Optimization.
- **链接**: [arXiv:2212.06331](https://arxiv.org/abs/2212.06331) · 📚 被引 13
- **作者**: Chao Chen, Xinhao Liu, Yiming Li, Li Ding, Chen Feng
- **🏷️ 机构**: New York University, University of Rochester
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> LiDAR mapping is important yet challenging in self-driving and mobile robotics. To tackle such a global point cloud registration problem, DeepMapping converts the complex map estimation into a self-supervised training of simple deep networks. Despite its broad convergence range on small datasets, DeepMapping still cannot produce satisfactory results on large-scale datasets with thousands of frames. This is due to the lack of loop closures and exact cross-frame point correspondences, and the slow convergence of its global localization network. We propose DeepMapping2 by adding two novel techniques to address these issues: (1) organization of training batch based on map topology from loop closing, and (2) self-supervised local-to-global point consistency loss leveraging pairwise registration. Our experiments and ablation studies on public datasets (KITTI, NCLT, and Nebula) demonstrate the effectiveness of our method.

</details>

### PointCMP: Contrastive Mask Prediction for Self-supervised Learning on Point Cloud Videos.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00123) · 📚 被引 26
- **作者**: Zhiqiang Shen, Xiaoxiao Sheng, Longguang Wang, Yulan Guo, Qiong Liu, Xi Zhou
- **🏷️ 机构**: Shanghai Jiao Tong University, Aviation University of Air Force, Sun Yat-sen University
- **会议**: CVPR 2023

### ACL-SPC: Adaptive Closed-Loop System for Self-Supervised Point Cloud Completion.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00910) · 📚 被引 27
- **作者**: Sangmin Hong, Mohsen Yavartanoo, Reyhaneh Neshatavar, Kyoung Mu Lee
- **🏷️ 机构**: IPAI, Seoul National University,Dept. of ECE &#x0026; ASRI,Seoul,Korea
- **会议**: CVPR 2023

### ToThePoint: Efficient Contrastive Learning of 3D Point Clouds via Recycling.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02086) · 📚 被引 14
- **作者**: Xinglin Li, Jiajing Chen, Jinhui Ouyang, Hanhui Deng, Senem Velipasalar, Di Wu
- **🏷️ 机构**: Hunan University,China, Syracuse University,NY,USA
- **会议**: CVPR 2023

### GeoMAE: Masked Geometric Target Prediction for Self-supervised Point Cloud Pre-Training.
- **链接**: [arXiv:2305.08808](https://arxiv.org/abs/2305.08808) · 📚 被引 45
- **作者**: Xiaoyu Tian, Haoxi Ran, Yue Wang, Hang Zhao
- **🏷️ 机构**: IIIS, Tsinghua University, CMU, NVIDIA
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper tries to address a fundamental question in point cloud self-supervised learning: what is a good signal we should leverage to learn features from point clouds without annotations? To answer that, we introduce a point cloud representation learning framework, based on geometric feature reconstruction. In contrast to recent papers that directly adopt masked autoencoder (MAE) and only predict original coordinates or occupancy from masked point clouds, our method revisits differences between images and point clouds and identifies three self-supervised learning objectives peculiar to point clouds, namely centroid prediction, normal estimation, and curvature prediction. Combined with occupancy prediction, these four objectives yield an nontrivial self-supervised learning task and mutually facilitate models to better reason fine-grained geometry of point clouds. Our pipeline is conceptually simple and it consists of two major steps: first, it randomly masks out groups of points, followed by a Transformer-based point cloud encoder; second, a lightweight Transformer decoder predicts centroid, normal, and curvature for points in each voxel. We transfer the pre-trained Transformer encoder to a downstream peception model. On the nuScene Datset, our model achieves 3.38 mAP improvment for object detection, 2.1 mIoU gain for segmentation, and 1.7 AMOTA gain for multi-object tracking. We also conduct experiments on the Waymo Open Dataset and achieve significant performance improvements over baselines as well.

</details>

### Spatiotemporal Self-Supervised Learning for Point Clouds in the Wild.
- **链接**: [arXiv:2303.16235](https://arxiv.org/abs/2303.16235) · 📚 被引 26
- **作者**: Yanhao Wu, Tong Zhang, Wei Ke, Sabine Süsstrunk, Mathieu Salzmann
- **🏷️ 机构**: School of Software Engineering, Xi&#x0027;an Jiaotong University,China, School of Computer and Communication Sciences, EPFL,Switzerland
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning (SSL) has the potential to benefit many applications, particularly those where manually annotating data is cumbersome. One such situation is the semantic segmentation of point clouds. In this context, existing methods employ contrastive learning strategies and define positive pairs by performing various augmentation of point clusters in a single frame. As such, these methods do not exploit the temporal nature of LiDAR data. In this paper, we introduce an SSL strategy that leverages positive pairs in both the spatial and temporal domain. To this end, we design (i) a point-to-cluster learning strategy that aggregates spatial information to distinguish objects; and (ii) a cluster-to-cluster learning strategy based on unsupervised object tracking that exploits temporal correspondences. We demonstrate the benefits of our approach via extensive experiments performed by self-supervised training on two large-scale LiDAR datasets and transferring the resulting models to other point cloud segmentation benchmarks. Our results evidence that our method outperforms the state-of-the-art point cloud SSL methods.

</details>

### Complete-to-Partial 4D Distillation for Self-Supervised Point Cloud Sequence Representation Learning.
- **链接**: [arXiv:2212.05330](https://arxiv.org/abs/2212.05330) · 📚 被引 23
- **作者**: Zhuoyang Zhang, Yuhao Dong, Yunze Liu, Li Yi
- **🏷️ 机构**: IIIS, Tsinghua University
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent work on 4D point cloud sequences has attracted a lot of attention. However, obtaining exhaustively labeled 4D datasets is often very expensive and laborious, so it is especially important to investigate how to utilize raw unlabeled data. However, most existing self-supervised point cloud representation learning methods only consider geometry from a static snapshot omitting the fact that sequential observations of dynamic scenes could reveal more comprehensive geometric details. And the video representation learning frameworks mostly model motion as image space flows, let alone being 3D-geometric-aware. To overcome such issues, this paper proposes a new 4D self-supervised pre-training method called Complete-to-Partial 4D Distillation. Our key idea is to formulate 4D self-supervised representation learning as a teacher-student knowledge distillation framework and let the student learn useful 4D representations with the guidance of the teacher. Experiments show that this approach significantly outperforms previous pre-training approaches on a wide range of 4D point cloud sequence understanding tasks including indoor and outdoor scenarios.

</details>

### SkyEye: Self-Supervised Bird's-Eye-View Semantic Mapping Using Monocular Frontal View Images.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01431) · 📚 被引 39
- **作者**: Nikhil Gosala, Kürsat Petek, Paulo L. J. Drews-Jr, Wolfram Burgard, Abhinav Valada
- **🏷️ 机构**: University of Freiburg, Federal University of Rio Grande
- **会议**: CVPR 2023

### Distilling Self-Supervised Vision Transformers for Weakly-Supervised Few-Shot Classification & Segmentation.
- **链接**: [arXiv:2307.03407](https://arxiv.org/abs/2307.03407) · 📚 被引 42
- **作者**: Dahyun Kang, Piotr Koniusz, Minsu Cho, Naila Murray
- **🏷️ 机构**: Meta AI, Data61 &#x2665; CSIRO, POSTECH
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We address the task of weakly-supervised few-shot image classification and segmentation, by leveraging a Vision Transformer (ViT) pretrained with self-supervision. Our proposed method takes token representations from the self-supervised ViT and leverages their correlations, via self-attention, to produce classification and segmentation predictions through separate task heads. Our model is able to effectively learn to perform classification and segmentation in the absence of pixel-level labels during training, using only image-level labels. To do this it uses attention maps, created from tokens generated by the self-supervised ViT backbone, as pixel-level pseudo-labels. We also explore a practical setup with ``mixed" supervision, where a small number of training images contains ground-truth pixel-level labels and the remaining images have only image-level labels. For this mixed setup, we propose to improve the pseudo-labels using a pseudo-label enhancer that was trained using the available ground-truth pixel-level labels. Experiments on Pascal-5i and COCO-20i demonstrate significant performance gains in a variety of supervision settings, and in particular when little-to-no pixel-level labels are available.

</details>

### MixMAE: Mixed and Masked Autoencoder for Efficient Pretraining of Hierarchical Vision Transformers.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00605) · 📚 被引 69
- **作者**: Jihao Liu, Xin Huang, Jinliang Zheng, Yu Liu, Hongsheng Li
- **🏷️ 机构**: CUHK MMLab, SenseTime Research
- **会议**: CVPR 2023

### Multiple Instance Learning via Iterative Self-Paced Supervised Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00327) · 📚 被引 35
- **作者**: Kangning Liu, Weicheng Zhu, Yiqiu Shen, Sheng Liu, Narges Razavian, Krzysztof J. Geras et al.
- **🏷️ 机构**: NYU Center for Data Science, NYU Grossman School of Medicine
- **会议**: CVPR 2023

### CiCo: Domain-Aware Sign Language Retrieval via Cross-Lingual Contrastive Learning.
- **链接**: [arXiv:2303.12793](https://arxiv.org/abs/2303.12793) · [代码](https://github.com/FangyunWei/SLRT) · 📚 被引 33
- **作者**: Yiting Cheng, Fangyun Wei, Jianmin Bao, Dong Chen, Wenqiang Zhang
- **🏷️ 机构**: School of Computer Science, Fudan University, Microsoft Research Asia
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This work focuses on sign language retrieval-a recently proposed task for sign language understanding. Sign language retrieval consists of two sub-tasks: text-to-sign-video (T2V) retrieval and sign-video-to-text (V2T) retrieval. Different from traditional video-text retrieval, sign language videos, not only contain visual signals but also carry abundant semantic meanings by themselves due to the fact that sign languages are also natural languages. Considering this character, we formulate sign language retrieval as a cross-lingual retrieval problem as well as a video-text retrieval task. Concretely, we take into account the linguistic properties of both sign languages and natural languages, and simultaneously identify the fine-grained cross-lingual (i.e., sign-to-word) mappings while contrasting the texts and the sign videos in a joint embedding space. This process is termed as cross-lingual contrastive learning. Another challenge is raised by the data scarcity issue-sign language datasets are orders of magnitude smaller in scale than that of speech recognition. We alleviate this issue by adopting a domain-agnostic sign encoder pre-trained on large-scale sign videos into the target domain via pseudo-labeling. Our framework, termed as domain-aware sign language retrieval via Cross-lingual Contrastive learning or CiCo for short, outperforms the pioneering method by large margins on various datasets, e.g., +22.4 T2V and +28.0 V2T R@1 improvements on How2Sign dataset, and +13.7 T2V and +17.1 V2T R@1 improvements on PHOENIX-2014T dataset. Code and models are available at: https://github.com/FangyunWei/SLRT.

</details>

### Dynamic Graph Enhanced Contrastive Learning for Chest X-Ray Report Generation.
- **链接**: [arXiv:2303.10323](https://arxiv.org/abs/2303.10323) · 📚 被引 176
- **作者**: Mingjie Li, Bingqian Lin, Zicong Chen, Haokun Lin, Xiaodan Liang, Xiaojun Chang
- **🏷️ 机构**: AAII, University of Technology Sydney,ReLER, School of ISE, Sun Yat-Sen University, The University of Hong Kong
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Automatic radiology reporting has great clinical potential to relieve radiologists from heavy workloads and improve diagnosis interpretation. Recently, researchers have enhanced data-driven neural networks with medical knowledge graphs to eliminate the severe visual and textual bias in this task. The structures of such graphs are exploited by using the clinical dependencies formed by the disease topic tags via general knowledge and usually do not update during the training process. Consequently, the fixed graphs can not guarantee the most appropriate scope of knowledge and limit the effectiveness. To address the limitation, we propose a knowledge graph with Dynamic structure and nodes to facilitate medical report generation with Contrastive Learning, named DCL. In detail, the fundamental structure of our graph is pre-constructed from general knowledge. Then we explore specific knowledge extracted from the retrieved reports to add additional nodes or redefine their relations in a bottom-up manner. Each image feature is integrated with its very own updated graph before being fed into the decoder module for report generation. Finally, this paper introduces Image-Report Contrastive and Image-Report Matching losses to better represent visual features and textual information. Evaluated on IU-Xray and MIMIC-CXR datasets, our DCL outperforms previous state-of-the-art models on these two benchmarks.

</details>

### Promoting Semantic Connectivity: Dual Nearest Neighbors Contrastive Learning for Unsupervised Domain Generalization.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00342) · 📚 被引 12
- **作者**: Yuchen Liu, Yaoming Wang, Yabo Chen, Wenrui Dai, Chenglin Li, Junni Zou et al.
- **🏷️ 机构**: Shanghai Jiao Tong University,Department of Electronic Engineering,China, Shanghai Jiao Tong University,Department of Computer Science and Engineering,China
- **会议**: CVPR 2023

### Class Prototypes based Contrastive Learning for Classifying Multi-Label and Fine-Grained Educational Videos.
- **链接**: [arXiv:2510.11204](https://arxiv.org/abs/2510.11204) · [代码](https://github.com/rohit-gupta/MMContrast) · 📚 被引 16
- **作者**: Rohit Gupta, Anirban Roy, Claire Christensen, Sujeong Kim, Sarah Gerard, Madeline Cincebeaux et al.
- **🏷️ 机构**: University of Central Florida,Center for Research in Computer Vision, SRI International
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The recent growth in the consumption of online media by children during early childhood necessitates data-driven tools enabling educators to filter out appropriate educational content for young learners. This paper presents an approach for detecting educational content in online videos. We focus on two widely used educational content classes: literacy and math. For each class, we choose prominent codes (sub-classes) based on the Common Core Standards. For example, literacy codes include `letter names', `letter sounds', and math codes include `counting', `sorting'. We pose this as a fine-grained multilabel classification problem as videos can contain multiple types of educational content and the content classes can get visually similar (e.g., `letter names' vs `letter sounds'). We propose a novel class prototypes based supervised contrastive learning approach that can handle fine-grained samples associated with multiple labels. We learn a class prototype for each class and a loss function is employed to minimize the distances between a class prototype and the samples from the class. Similarly, distances between a class prototype and the samples from other classes are maximized. As the alignment between visual and audio cues are crucial for effective comprehension, we consider a multimodal transformer network to capture the interaction between visual and audio cues in videos while learning the embedding for videos. For evaluation, we present a dataset, APPROVE, employing educational videos from YouTube labeled with fine-grained education classes by education researchers. APPROVE consists of 193 hours of expert-annotated videos with 19 classes. The proposed approach outperforms strong baselines on APPROVE and other benchmarks such as Youtube-8M, and COIN. The dataset is available at https://github.com/rohit-gupta/MMContrast/tree/main/APPROVE

</details>

### Pseudo-Label Guided Contrastive Learning for Semi-Supervised Medical Image Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01895) · 📚 被引 187
- **作者**: Hritam Basak, Zhaozheng Yin
- **🏷️ 机构**: Stony Brook University,NY,USA
- **会议**: CVPR 2023

### Weakly-Supervised Domain Adaptive Semantic Segmentation with Prototypical Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01481) · 📚 被引 30
- **作者**: Anurag Das, Yongqin Xian, Dengxin Dai, Bernt Schiele
- **🏷️ 机构**: Saarland Informatics Campus,MPI for Informatics, ETH Zurich
- **会议**: CVPR 2023

### MaskCon: Masked Contrastive Learning for Coarse-Labelled Dataset.
- **链接**: [arXiv:2303.12756](https://arxiv.org/abs/2303.12756) · [代码](https://github.com/MrChenFeng/MaskCon_CVPR2023) · 📚 被引 18
- **作者**: Chen Feng, Ioannis Patras
- **🏷️ 机构**: Queen Mary University of London,UK
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep learning has achieved great success in recent years with the aid of advanced neural network structures and large-scale human-annotated datasets. However, it is often costly and difficult to accurately and efficiently annotate large-scale datasets, especially for some specialized domains where fine-grained labels are required. In this setting, coarse labels are much easier to acquire as they do not require expert knowledge. In this work, we propose a contrastive learning method, called $\textbf{Mask}$ed $\textbf{Con}$trastive learning~($\textbf{MaskCon}$) to address the under-explored problem setting, where we learn with a coarse-labelled dataset in order to address a finer labelling problem. More specifically, within the contrastive learning framework, for each sample our method generates soft-labels with the aid of coarse labels against other samples and another augmented view of the sample in question. By contrast to self-supervised contrastive learning where only the sample's augmentations are considered hard positives, and in supervised contrastive learning where only samples with the same coarse labels are considered hard positives, we propose soft labels based on sample distances, that are masked by the coarse labels. This allows us to utilize both inter-sample relations and coarse labels. We demonstrate that our method can obtain as special cases many existing state-of-the-art works and that it provides tighter bounds on the generalization error. Experimentally, our method achieves significant improvement over the current state-of-the-art in various datasets, including CIFAR10, CIFAR100, ImageNet-1K, Standford Online Products and Stanford Cars196 datasets. Code and annotations are available at https://github.com/MrChenFeng/MaskCon_CVPR2023.

</details>

### Hyperbolic Contrastive Learning for Visual Representations beyond Objects.
- **链接**: [arXiv:2212.00653](https://arxiv.org/abs/2212.00653) · [代码](https://github.com/shlokk/HCL) · 📚 被引 50
- **作者**: Songwei Ge, Shlok Mishra, Simon Kornblith, Chun-Liang Li, David Jacobs
- **🏷️ 机构**: University of Maryland,College Park, Google Research
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Although self-/un-supervised methods have led to rapid progress in visual representation learning, these methods generally treat objects and scenes using the same lens. In this paper, we focus on learning representations for objects and scenes that preserve the structure among them. Motivated by the observation that visually similar objects are close in the representation space, we argue that the scenes and objects should instead follow a hierarchical structure based on their compositionality. To exploit such a structure, we propose a contrastive learning framework where a Euclidean loss is used to learn object representations and a hyperbolic loss is used to encourage representations of scenes to lie close to representations of their constituent objects in a hyperbolic space. This novel hyperbolic objective encourages the scene-object hypernymy among the representations by optimizing the magnitude of their norms. We show that when pretraining on the COCO and OpenImages datasets, the hyperbolic loss improves downstream performance of several baselines across multiple datasets and tasks, including image classification, object detection, and semantic segmentation. We also show that the properties of the learned representations allow us to solve various vision tasks that involve the interaction between scenes and objects in a zero-shot fashion. Our code can be found at \url{https://github.com/shlokk/HCL/tree/main/HCL}.

</details>

### Twin Contrastive Learning with Noisy Labels.
- **链接**: [arXiv:2303.06930](https://arxiv.org/abs/2303.06930) · [代码](https://github.com/Hzzone/TCL) · 📚 被引 108
- **作者**: Zhizhong Huang, Junping Zhang, Hongming Shan
- **🏷️ 机构**: School of Computer Science, Fudan University,Shanghai Key Lab of Intelligent Information Processing,Shanghai,China,200433, Institute of Science and Technology for Brain-inspired Intelligence and MOE Frontiers Center for Brain Science, Fudan University,Shanghai,China,200433
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Learning from noisy data is a challenging task that significantly degenerates the model performance. In this paper, we present TCL, a novel twin contrastive learning model to learn robust representations and handle noisy labels for classification. Specifically, we construct a Gaussian mixture model (GMM) over the representations by injecting the supervised model predictions into GMM to link label-free latent variables in GMM with label-noisy annotations. Then, TCL detects the examples with wrong labels as the out-of-distribution examples by another two-component GMM, taking into account the data distribution. We further propose a cross-supervision with an entropy regularization loss that bootstraps the true targets from model predictions to handle the noisy labels. As a result, TCL can learn discriminative representations aligned with estimated labels through mixup and contrastive learning. Extensive experimental results on several standard benchmarks and real-world datasets demonstrate the superior performance of TCL. In particular, TCL achieves 7.5\% improvements on CIFAR-10 with 90\% noisy label -- an extremely noisy scenario. The source code is available at \url{https://github.com/Hzzone/TCL}.

</details>

### Actionlet-Dependent Contrastive Learning for Unsupervised Skeleton-Based Action Recognition.
- **链接**: [arXiv:2303.10904](https://arxiv.org/abs/2303.10904) · 📚 被引 92
- **作者**: Lilang Lin, Jiahang Zhang, Jiaying Liu
- **🏷️ 机构**: Wangxuan Institute of Computer Technology, Peking University,Beijing,China
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The self-supervised pretraining paradigm has achieved great success in skeleton-based action recognition. However, these methods treat the motion and static parts equally, and lack an adaptive design for different parts, which has a negative impact on the accuracy of action recognition. To realize the adaptive action modeling of both parts, we propose an Actionlet-Dependent Contrastive Learning method (ActCLR). The actionlet, defined as the discriminative subset of the human skeleton, effectively decomposes motion regions for better action modeling. In detail, by contrasting with the static anchor without motion, we extract the motion region of the skeleton data, which serves as the actionlet, in an unsupervised manner. Then, centering on actionlet, a motion-adaptive data transformation method is built. Different data transformations are applied to actionlet and non-actionlet regions to introduce more diversity while maintaining their own characteristics. Meanwhile, we propose a semantic-aware feature pooling method to build feature representations among motion and static regions in a distinguished manner. Extensive experiments on NTU RGB+D and PKUMMD show that the proposed method achieves remarkable action recognition performance. More visualization and quantitative experiments demonstrate the effectiveness of our method. Our project website is available at https://langlandslin.github.io/projects/ActCLR/

</details>

### Pose-disentangled Contrastive Learning for Self-supervised Facial Representation.
- **链接**: [arXiv:2211.13490](https://arxiv.org/abs/2211.13490) · [代码](https://github.com/DreamMr/PCL) · 📚 被引 29
- **作者**: Yuanyuan Liu, Wenbin Wang, Yibing Zhan, Shaoze Feng, Kejun Liu, Zhe Chen
- **🏷️ 机构**: School of Computer Science, China University of Geosciences,Wuhan,China, JD Explore Academy,China, The University of Sydney,Australia
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised facial representation has recently attracted increasing attention due to its ability to perform face understanding without relying on large-scale annotated datasets heavily. However, analytically, current contrastive-based self-supervised learning (SSL) still performs unsatisfactorily for learning facial representation. More specifically, existing contrastive learning (CL) tends to learn pose-invariant features that cannot depict the pose details of faces, compromising the learning performance. To conquer the above limitation of CL, we propose a novel Pose-disentangled Contrastive Learning (PCL) method for general self-supervised facial representation. Our PCL first devises a pose-disentangled decoder (PDD) with a delicately designed orthogonalizing regulation, which disentangles the pose-related features from the face-aware features; therefore, pose-related and other pose-unrelated facial information could be performed in individual subnetworks and do not affect each other's training. Furthermore, we introduce a pose-related contrastive learning scheme that learns pose-related information based on data augmentation of the same image, which would deliver more effective face-aware representation for various downstream tasks. We conducted linear evaluation on four challenging downstream facial understanding tasks, ie, facial expression recognition, face recognition, AU detection and head pose estimation. Experimental results demonstrate that our method significantly outperforms state-of-the-art SSL methods. Code is available at https://github.com/DreamMr/PCL}{https://github.com/DreamMr/PCL

</details>

### Spatio-Temporal Pixel-Level Contrastive Learning-based Source-Free Domain Adaptation for Video Semantic Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01015)
- **作者**: Shao-Yuan Lo, Poojan Oza, Sumanth Chennupati, Alejandro Galindo, Vishal M. Patel
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### Change-Aware Sampling and Contrastive Learning for Satellite Images.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00509) · 📚 被引 96
- **作者**: Utkarsh Mall, Bharath Hariharan, Kavita Bala
- **🏷️ 机构**: Cornell University
- **会议**: CVPR 2023

### MobileVOS: Real-Time Video Object Segmentation Contrastive Learning meets Knowledge Distillation.
- **链接**: [arXiv:2303.07815](https://arxiv.org/abs/2303.07815) · 📚 被引 36
- **作者**: Roy Miles, Mehmet Kerim Yucel, Bruno Manganelli, Albert Saà-Garriga
- **🏷️ 机构**: Samsung Research,UK
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper tackles the problem of semi-supervised video object segmentation on resource-constrained devices, such as mobile phones. We formulate this problem as a distillation task, whereby we demonstrate that small space-time-memory networks with finite memory can achieve competitive results with state of the art, but at a fraction of the computational cost (32 milliseconds per frame on a Samsung Galaxy S22). Specifically, we provide a theoretically grounded framework that unifies knowledge distillation with supervised contrastive representation learning. These models are able to jointly benefit from both pixel-wise contrastive learning and distillation from a pre-trained teacher. We validate this loss by achieving competitive J&F to state of the art on both the standard DAVIS and YouTube benchmarks, despite running up to 5x faster, and with 32x fewer parameters.

</details>

### Dynamic Conceptional Contrastive Learning for Generalized Category Discovery.
- **链接**: [arXiv:2303.17393](https://arxiv.org/abs/2303.17393) · [代码](https://github.com/TPCD/DCCL) · 📚 被引 94
- **作者**: Nan Pu, Zhun Zhong, Nicu Sebe
- **🏷️ 机构**: University of Trento,The Department of Information Engineering and Computer Science,Trento,Italy
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Generalized category discovery (GCD) is a recently proposed open-world problem, which aims to automatically cluster partially labeled data. The main challenge is that the unlabeled data contain instances that are not only from known categories of the labeled data but also from novel categories. This leads traditional novel category discovery (NCD) methods to be incapacitated for GCD, due to their assumption of unlabeled data are only from novel categories. One effective way for GCD is applying self-supervised learning to learn discriminate representation for unlabeled data. However, this manner largely ignores underlying relationships between instances of the same concepts (e.g., class, super-class, and sub-class), which results in inferior representation learning. In this paper, we propose a Dynamic Conceptional Contrastive Learning (DCCL) framework, which can effectively improve clustering accuracy by alternately estimating underlying visual conceptions and learning conceptional representation. In addition, we design a dynamic conception generation and update mechanism, which is able to ensure consistent conception learning and thus further facilitate the optimization of DCCL. Extensive experiments show that DCCL achieves new state-of-the-art performances on six generic and fine-grained visual recognition datasets, especially on fine-grained ones. For example, our method significantly surpasses the best competitor by 16.2% on the new classes for the CUB-200 dataset. Code is available at https://github.com/TPCD/DCCL.

</details>

### TranSG: Transformer-Based Skeleton Graph Prototype Contrastive Learning with Structure-Trajectory Prompted Reconstruction for Person Re-Identification.
- **链接**: [arXiv:2303.06819](https://arxiv.org/abs/2303.06819) · 📚 被引 51
- **作者**: Haocong Rao, Chunyan Miao
- **🏷️ 机构**: LILY Research Center, Nanyang Technological University, Singapore School of Computer Science and Engineering, Nanyang Technological University,Singapore
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Person re-identification (re-ID) via 3D skeleton data is an emerging topic with prominent advantages. Existing methods usually design skeleton descriptors with raw body joints or perform skeleton sequence representation learning. However, they typically cannot concurrently model different body-component relations, and rarely explore useful semantics from fine-grained representations of body joints. In this paper, we propose a generic Transformer-based Skeleton Graph prototype contrastive learning (TranSG) approach with structure-trajectory prompted reconstruction to fully capture skeletal relations and valuable spatial-temporal semantics from skeleton graphs for person re-ID. Specifically, we first devise the Skeleton Graph Transformer (SGT) to simultaneously learn body and motion relations within skeleton graphs, so as to aggregate key correlative node features into graph representations. Then, we propose the Graph Prototype Contrastive learning (GPC) to mine the most typical graph features (graph prototypes) of each identity, and contrast the inherent similarity between graph representations and different prototypes from both skeleton and sequence levels to learn discriminative graph representations. Last, a graph Structure-Trajectory Prompted Reconstruction (STPR) mechanism is proposed to exploit the spatial and temporal contexts of graph nodes to prompt skeleton graph reconstruction, which facilitates capturing more valuable patterns and graph semantics for person re-ID. Empirical evaluations demonstrate that TranSG significantly outperforms existing state-of-the-art methods. We further show its generality under different graph modeling, RGB-estimated skeletons, and unsupervised scenarios.

</details>

### Positive-Augmented Contrastive Learning for Image and Video Captioning Evaluation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00668) · 📚 被引 46
- **作者**: Sara Sarto, Manuele Barraco, Marcella Cornia, Lorenzo Baraldi, Rita Cucchiara
- **🏷️ 机构**: University of Modena and Reggio Emilia,Modena,Italy
- **会议**: CVPR 2023

### FEND: A Future Enhanced Distribution-Aware Contrastive Learning Framework for Long-Tail Trajectory Prediction.
- **链接**: [arXiv:2303.16574](https://arxiv.org/abs/2303.16574) · 📚 被引 44
- **作者**: Yuning Wang, Pu Zhang, Lei Bai, Jianru Xue
- **🏷️ 机构**: Institute of Artificial Intelligence and Robotics, Xi&#x0027;an Jiaotong University,China, DiDi Chuxing,China, Shanghai AI Laboratory,China
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Predicting the future trajectories of the traffic agents is a gordian technique in autonomous driving. However, trajectory prediction suffers from data imbalance in the prevalent datasets, and the tailed data is often more complicated and safety-critical. In this paper, we focus on dealing with the long-tail phenomenon in trajectory prediction. Previous methods dealing with long-tail data did not take into account the variety of motion patterns in the tailed data. In this paper, we put forward a future enhanced contrastive learning framework to recognize tail trajectory patterns and form a feature space with separate pattern clusters. Furthermore, a distribution aware hyper predictor is brought up to better utilize the shaped feature space. Our method is a model-agnostic framework and can be plugged into many well-known baselines. Experimental results show that our framework outperforms the state-of-the-art long-tail prediction method on tailed samples by 9.5% on ADE and 8.5% on FDE, while maintaining or slightly improving the averaged performance. Our method also surpasses many long-tail techniques on trajectory prediction task.

</details>

### MoLo: Motion-Augmented Long-Short Contrastive Learning for Few-Shot Action Recognition.
- **链接**: [arXiv:2304.00946](https://arxiv.org/abs/2304.00946) · [代码](https://github.com/alibaba-mmai-research/MoLo) · 📚 被引 92
- **作者**: Xiang Wang, Shiwei Zhang, Zhiwu Qing, Changxin Gao, Yingya Zhang, Deli Zhao et al.
- **🏷️ 机构**: School of Artificial Intelligence and Automation, Huazhong University of Science and Technology,Key Laboratory of Image Processing and Intelligent Control, Alibaba Group
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Current state-of-the-art approaches for few-shot action recognition achieve promising performance by conducting frame-level matching on learned visual features. However, they generally suffer from two limitations: i) the matching procedure between local frames tends to be inaccurate due to the lack of guidance to force long-range temporal perception; ii) explicit motion learning is usually ignored, leading to partial information loss. To address these issues, we develop a Motion-augmented Long-short Contrastive Learning (MoLo) method that contains two crucial components, including a long-short contrastive objective and a motion autodecoder. Specifically, the long-short contrastive objective is to endow local frame features with long-form temporal awareness by maximizing their agreement with the global token of videos belonging to the same class. The motion autodecoder is a lightweight architecture to reconstruct pixel motions from the differential features, which explicitly embeds the network with motion dynamics. By this means, MoLo can simultaneously learn long-range temporal context and motion cues for comprehensive few-shot matching. To demonstrate the effectiveness, we evaluate MoLo on five standard benchmarks, and the results show that MoLo favorably outperforms recent advanced methods. The source code is available at https://github.com/alibaba-mmai-research/MoLo.

</details>

### ContraNeRF: Generalizable Neural Radiance Fields for Synthetic-to-real Novel View Synthesis via Contrastive Learning.
- **链接**: [arXiv:2303.11052](https://arxiv.org/abs/2303.11052) · 📚 被引 21
- **作者**: Hao Yang, Lanqing Hong, Aoxue Li, Tianyang Hu, Zhenguo Li, Gim Hee Lee et al.
- **🏷️ 机构**: Peking University,Center for Data Science, Huawei Noah&#x0027;s Ark Lab, School of Computing, National University of Singapore
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Although many recent works have investigated generalizable NeRF-based novel view synthesis for unseen scenes, they seldom consider the synthetic-to-real generalization, which is desired in many practical applications. In this work, we first investigate the effects of synthetic data in synthetic-to-real novel view synthesis and surprisingly observe that models trained with synthetic data tend to produce sharper but less accurate volume densities. For pixels where the volume densities are correct, fine-grained details will be obtained. Otherwise, severe artifacts will be produced. To maintain the advantages of using synthetic data while avoiding its negative effects, we propose to introduce geometry-aware contrastive learning to learn multi-view consistent features with geometric constraints. Meanwhile, we adopt cross-view attention to further enhance the geometry perception of features by querying features across input views. Experiments demonstrate that under the synthetic-to-real setting, our method can render images with higher quality and better fine-grained details, outperforming existing generalizable novel view synthesis methods in terms of PSNR, SSIM, and LPIPS. When trained on real data, our method also achieves state-of-the-art results.

</details>

### Explicit Boundary Guided Semi-Push-Pull Contrastive Learning for Supervised Anomaly Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02346) · 📚 被引 108
- **作者**: Xincheng Yao, Ruoqi Li, Jing Zhang, Jun Sun, Chongyang Zhang
- **🏷️ 机构**: School of Electronic Information and Electrical Engineering, Shanghai Jiao Tong University, Research Institute of Systems Engineering, Academy Military Science,Beijing,China
- **会议**: CVPR 2023

### CLAMP: Prompt-based Contrastive Learning for Connecting Language and Animal Pose.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02229) · 📚 被引 29
- **作者**: Xu Zhang, Wen Wang, Zhe Chen, Yufei Xu, Jing Zhang, Dacheng Tao
- **🏷️ 机构**: The University of Sydney,Australia, Zhejiang University,China
- **会议**: CVPR 2023

### Non-Contrastive Learning Meets Language-Image Pre-Training.
- **链接**: [arXiv:2210.09304](https://arxiv.org/abs/2210.09304) · 📚 被引 19
- **作者**: Jinghao Zhou, Li Dong, Zhe Gan, Lijuan Wang, Furu Wei
- **🏷️ 机构**: Microsoft
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Contrastive language-image pre-training (CLIP) serves as a de-facto standard to align images and texts. Nonetheless, the loose correlation between images and texts of web-crawled data renders the contrastive objective data inefficient and craving for a large training batch size. In this work, we explore the validity of non-contrastive language-image pre-training (nCLIP), and study whether nice properties exhibited in visual self-supervised models can emerge. We empirically observe that the non-contrastive objective nourishes representation learning while sufficiently underperforming under zero-shot recognition. Based on the above study, we further introduce xCLIP, a multi-tasking framework combining CLIP and nCLIP, and show that nCLIP aids CLIP in enhancing feature semantics. The synergy between two objectives lets xCLIP enjoy the best of both worlds: superior performance in both zero-shot transfer and representation learning. Systematic evaluation is conducted spanning a wide variety of downstream tasks including zero-shot classification, out-of-domain classification, retrieval, visual representation learning, and textual representation learning, showcasing a consistent performance gain and validating the effectiveness of xCLIP.

</details>

### Masked Image Training for Generalizable Deep Image Denoising.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00169) · 📚 被引 106
- **作者**: Haoyu Chen, Jinjin Gu, Yihao Liu, Salma Abdel Magid, Chao Dong, Qiong Wang et al.
- **🏷️ 机构**: The Hong Kong University of Science and Technology (Guangzhou), Shanghai AI Lab, Harvard University
- **会议**: CVPR 2023

### MaskSketch: Unpaired Structure-guided Masked Image Generation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00187) · 📚 被引 35
- **作者**: Dina Bashkirova, José Lezama, Kihyuk Sohn, Kate Saenko, Irfan Essa
- **🏷️ 机构**: Boston University, Google Research
- **会议**: CVPR 2023

### MIC: Masked Image Consistency for Context-Enhanced Domain Adaptation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01128) · 📚 被引 329
- **作者**: Lukas Hoyer, Dengxin Dai, Haoran Wang, Luc Van Gool
- **🏷️ 机构**: ETH Zurich, Max Planck Institute for Informatics, Saarland Informatics Campus
- **会议**: CVPR 2023

### Understanding Masked Image Modeling via Learning Occlusion Invariant Feature.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00604) · 📚 被引 40
- **作者**: Xiangwen Kong, Xiangyu Zhang
- **🏷️ 机构**: MEGVII Technology
- **会议**: CVPR 2023

### Rethinking Out-of-distribution (OOD) Detection: Masked Image Modeling is All You Need.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01114) · 📚 被引 58
- **作者**: Jingyao Li, Pengguang Chen, Zexin He, Shaozuo Yu, Shu Liu, Jiaya Jia
- **🏷️ 机构**: The Chinese University of Hong Kong, SmartMore
- **会议**: CVPR 2023

### Hard Patches Mining for Masked Image Modeling.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01000) · 📚 被引 71
- **作者**: Haochen Wang, Kaiyou Song, Junsong Fan, Yuxi Wang, Jin Xie, Zhaoxiang Zhang
- **🏷️ 机构**: Institute of Automation, Chinese Academy of Sciences,Center for Research on Intelligent Perception and Computing, National Laboratory of Pattern Recognition, Megvii Technology
- **会议**: CVPR 2023

### Masked Image Modeling with Local Multi-Scale Reconstruction.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00211) · 📚 被引 58
- **作者**: Haoqing Wang, Yehui Tang, Yunhe Wang, Jianyuan Guo, Zhi-Hong Deng, Kai Han
- **🏷️ 机构**: School of Intelligence Science and Technology, Peking University, Huawei Noah&#x0027;s Ark Lab
- **会议**: CVPR 2023

### Revealing the Dark Secrets of Masked Image Modeling.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01391) · 📚 被引 95
- **作者**: Zhenda Xie, Zigang Geng, Jingcheng Hu, Zheng Zhang, Han Hu, Yue Cao
- **🏷️ 机构**: Tsinghua University, University of Science and Technology of China, Microsoft Research Asia
- **会议**: CVPR 2023

### On Data Scaling in Masked Image Modeling.
- **链接**: [arXiv:2206.04664](https://arxiv.org/abs/2206.04664) · 📚 被引 52
- **作者**: Zhenda Xie, Zheng Zhang, Yue Cao, Yutong Lin, Yixuan Wei, Qi Dai et al.
- **🏷️ 机构**: Tsinghua University, Xi&#x0027;an Jiaotong University, Microsoft Research Asia
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> An important goal of self-supervised learning is to enable model pre-training to benefit from almost unlimited data. However, one method that has recently become popular, namely masked image modeling (MIM), is suspected to be unable to benefit from larger data. In this work, we break this misconception through extensive experiments, with data scales ranging from 10\% of ImageNet-1K to full ImageNet-22K, model sizes ranging from 49 million to 1 billion, and training lengths ranging from 125K iterations to 500K iterations. Our study reveals that: (i) Masked image modeling is also demanding on larger data. We observed that very large models got over-fitted with relatively small data; (ii) The length of training matters. Large models trained with masked image modeling can benefit from more data with longer training; (iii) The validation loss in pre-training is a good indicator to measure how well the model performs for fine-tuning on multiple tasks. This observation allows us to pre-evaluate pre-trained models in advance without having to make costly trial-and-error assessments of downstream tasks. We hope that our findings will advance the understanding of masked image modeling in terms of scaling ability.

</details>

### Stare at What You See: Masked Image Modeling without Reconstruction.
- **链接**: [arXiv:2211.08887](https://arxiv.org/abs/2211.08887) · [代码](https://github.com/OpenPerceptionX/maskalign) · 📚 被引 22
- **作者**: Hongwei Xue, Peng Gao, Hongyang Li, Yu Qiao, Hao Sun, Houqiang Li et al.
- **🏷️ 机构**: University of Science and Technology of China, Shanghai Artificial Intelligence Laboratory, China Telecom Corporation Ltd., Data&#x0026;AI Technology Company
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Masked Autoencoders (MAE) have been prevailing paradigms for large-scale vision representation pre-training. By reconstructing masked image patches from a small portion of visible image regions, MAE forces the model to infer semantic correlation within an image. Recently, some approaches apply semantic-rich teacher models to extract image features as the reconstruction target, leading to better performance. However, unlike the low-level features such as pixel values, we argue the features extracted by powerful teacher models already encode rich semantic correlation across regions in an intact image.This raises one question: is reconstruction necessary in Masked Image Modeling (MIM) with a teacher model? In this paper, we propose an efficient MIM paradigm named MaskAlign. MaskAlign simply learns the consistency of visible patch features extracted by the student model and intact image features extracted by the teacher model. To further advance the performance and tackle the problem of input inconsistency between the student and teacher model, we propose a Dynamic Alignment (DA) module to apply learnable alignment. Our experimental results demonstrate that masked modeling does not lose effectiveness even without reconstruction on masked regions. Combined with Dynamic Alignment, MaskAlign can achieve state-of-the-art performance with much higher efficiency. Code and models will be available at https://github.com/OpenPerceptionX/maskalign.

</details>

### PMatch: Paired Masked Image Modeling for Dense Geometric Matching.
- **链接**: [arXiv:2303.17342](https://arxiv.org/abs/2303.17342) · [代码](https://github.com/ShngJZ/PMatch) · 📚 被引 43
- **作者**: Shengjie Zhu, Xiaoming Liu
- **🏷️ 机构**: Michigan State University,Department of Computer Science and Engineering,East Lansing,MI,48824
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Dense geometric matching determines the dense pixel-wise correspondence between a source and support image corresponding to the same 3D structure. Prior works employ an encoder of transformer blocks to correlate the two-frame features. However, existing monocular pretraining tasks, e.g., image classification, and masked image modeling (MIM), can not pretrain the cross-frame module, yielding less optimal performance. To resolve this, we reformulate the MIM from reconstructing a single masked image to reconstructing a pair of masked images, enabling the pretraining of transformer module. Additionally, we incorporate a decoder into pretraining for improved upsampling results. Further, to be robust to the textureless area, we propose a novel cross-frame global matching module (CFGM). Since the most textureless area is planar surfaces, we propose a homography loss to further regularize its learning. Combined together, we achieve the State-of-The-Art (SoTA) performance on geometric matching. Codes and models are available at https://github.com/ShngJZ/PMatch.

</details>

### Self-Supervised Image-to-Point Distillation via Semantically Tolerant Contrastive Loss.
- **链接**: [arXiv:2301.05709](https://arxiv.org/abs/2301.05709) · 📚 被引 29
- **作者**: Anas Mahmoud, Jordan S. K. Hu, Tianshu Kuai, Ali Harakeh, Liam Paull, Steven L. Waslander
- **🏷️ 机构**: University of Toronto Robotics Institute, Mila, Universit&#x00E9; de Montr&#x00E9;al
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> An effective framework for learning 3D representations for perception tasks is distilling rich self-supervised image features via contrastive learning. However, image-to point representation learning for autonomous driving datasets faces two main challenges: 1) the abundance of self-similarity, which results in the contrastive losses pushing away semantically similar point and image regions and thus disturbing the local semantic structure of the learned representations, and 2) severe class imbalance as pretraining gets dominated by over-represented classes. We propose to alleviate the self-similarity problem through a novel semantically tolerant image-to-point contrastive loss that takes into consideration the semantic distance between positive and negative image regions to minimize contrasting semantically similar point and image regions. Additionally, we address class imbalance by designing a class-agnostic balanced loss that approximates the degree of class imbalance through an aggregate sample-to-samples semantic similarity measure. We demonstrate that our semantically-tolerant contrastive loss with class balancing improves state-of-the art 2D-to-3D representation learning in all evaluation settings on 3D semantic segmentation. Our method consistently outperforms state-of-the-art 2D-to-3D representation learning frameworks across a wide range of 2D self-supervised pretrained models.

</details>

### Multi-Mode Online Knowledge Distillation for Self-Supervised Visual Representation Learning.
- **链接**: [arXiv:2304.06461](https://arxiv.org/abs/2304.06461) · 📚 被引 38
- **作者**: Kaiyou Song, Jin Xie, Shan Zhang, Zimeng Luo
- **🏷️ 机构**: Megvii Technology
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning (SSL) has made remarkable progress in visual representation learning. Some studies combine SSL with knowledge distillation (SSL-KD) to boost the representation learning performance of small models. In this study, we propose a Multi-mode Online Knowledge Distillation method (MOKD) to boost self-supervised visual representation learning. Different from existing SSL-KD methods that transfer knowledge from a static pre-trained teacher to a student, in MOKD, two different models learn collaboratively in a self-supervised manner. Specifically, MOKD consists of two distillation modes: self-distillation and cross-distillation modes. Among them, self-distillation performs self-supervised learning for each model independently, while cross-distillation realizes knowledge interaction between different models. In cross-distillation, a cross-attention feature search strategy is proposed to enhance the semantic feature alignment between different models. As a result, the two models can absorb knowledge from each other to boost their representation learning performance. Extensive experimental results on different backbones and datasets demonstrate that two heterogeneous models can benefit from MOKD and outperform their independently trained baseline. In addition, MOKD also outperforms existing SSL-KD methods for both the student and teacher models.

</details>

### Masked Video Distillation: Rethinking Masked Feature Modeling for Self-supervised Video Representation Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00611)
- **作者**: Rui Wang, Dongdong Chen, Zuxuan Wu, Yinpeng Chen, Xiyang Dai, Mengchen Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

## 跨领域论文（完整笔记在其他领域）

- Mask DINO: Towards A Unified Transformer-based Framework for Object Detection and Segmentation. → [object-detection](../object-detection/Guideline%202023.md)
- Object Detection with Self-Supervised Scene Adaptation. → [object-detection](../object-detection/Guideline%202023.md)
- MV-JAR: Masked Voxel Jigsaw and Reconstruction for LiDAR-Based Self-Supervised Pre-Training. → [3d-detection](../3d-detection/Guideline%202023.md)
- BKinD-3D: Self-Supervised 3D Keypoint Discovery from Multi-View Videos. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- Lite-Mono: A Lightweight CNN and Transformer Architecture for Self-Supervised Monocular Depth Estimation. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- Open Vocabulary Semantic Segmentation with Patch Aligned Contrastive Learning. → [open-set-detection](../open-set-detection/Guideline%202023.md)
- Revisiting Multimodal Representation in Contrastive Learning: From Patch and Token Embeddings to Finite Discrete Tokens. → [multimodal](../multimodal/Guideline%202023.md)
- Self-Supervised Learning for Multimodal Non-Rigid 3D Shape Matching. → [multimodal](../multimodal/Guideline%202023.md)
- Best of Both Worlds: Multimodal Contrastive Learning with Tabular and Imaging Data. → [multimodal](../multimodal/Guideline%202023.md)
- Learning Audio-Visual Source Localization via False Negative Aware Contrastive Learning. → [multimodal](../multimodal/Guideline%202023.md)
- Hunting Sparsity: Density-Guided Contrastive Learning for Semi-Supervised Semantic Segmentation. → [network-pruning](../network-pruning/Guideline%202023.md)
