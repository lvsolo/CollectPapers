# Self-supervised Vision — 2023 Guideline

> 领域: 视觉自监督学习（对比学习、MAE、DINO 系）
> 论文数: 110 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### GD-MAE: Generative Decoder for MAE Pre-Training on LiDAR Point Clouds.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00907) · 📚 被引 71
- **作者**: Honghui Yang, Tong He, Jiaheng Liu, Hua Chen, Boxi Wu, Binbin Lin et al.
- **🏷️ 机构**: Zhejiang University,State Key Lab of CAD&#x0026;CG, Shanghai AI Laboratory, COMAC Beijing Aircraft Technology Research Institute
- **会议**: CVPR 2023

### DeepMapping2: Self-Supervised Large-Scale LiDAR Map Optimization.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00898)
- **作者**: Chao Chen, Xinhao Liu, Yiming Li, Li Ding, Chen Feng
- **🏷️ 机构**: New York University, University of Rochester
- **会议**: CVPR 2023

### PointCMP: Contrastive Mask Prediction for Self-supervised Learning on Point Cloud Videos.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00123) · 📚 被引 25
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
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01304) · 📚 被引 45
- **作者**: Xiaoyu Tian, Haoxi Ran, Yue Wang, Hang Zhao
- **🏷️ 机构**: IIIS, Tsinghua University, CMU, NVIDIA
- **会议**: CVPR 2023

### Spatiotemporal Self-Supervised Learning for Point Clouds in the Wild.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00508) · 📚 被引 26
- **作者**: Yanhao Wu, Tong Zhang, Wei Ke, Sabine Süsstrunk, Mathieu Salzmann
- **🏷️ 机构**: School of Software Engineering, Xi&#x0027;an Jiaotong University,China, School of Computer and Communication Sciences, EPFL,Switzerland
- **会议**: CVPR 2023

### Complete-to-Partial 4D Distillation for Self-Supervised Point Cloud Sequence Representation Learning.
- **链接**: [arXiv:2212.05330](https://arxiv.org/abs/2212.05330)
- **作者**: Zhuoyang Zhang, Yuhao Dong, Yunze Liu, Li Yi
- **🏷️ 机构**: IIIS, Tsinghua University
- **会议**: CVPR 2023

- **摘要（英，原文）**:

  > Recent work on 4D point cloud sequences has attracted a lot of attention. However, obtaining exhaustively labeled 4D datasets is often very expensive and laborious, so it is especially important to investigate how to utilize raw unlabeled data. However, most existing self-supervised point cloud representation learning methods only consider geometry from a static snapshot omitting the fact that sequential observations of dynamic scenes could reveal more comprehensive geometric details. And the video representation learning frameworks mostly model motion as image space flows, let alone being 3D-geometric-aware. To overcome such issues, this paper proposes a new 4D self-supervised pre-training method called Complete-to-Partial 4D Distillation. Our key idea is to formulate 4D self-supervised representation learning as a teacher-student knowledge distillation framework and let the student learn useful 4D representations with the guidance of the teacher. Experiments show that this approach significantly outperforms previous pre-training approaches on a wide range of 4D point cloud sequence understanding tasks including indoor and outdoor scenarios.

### SkyEye: Self-Supervised Bird's-Eye-View Semantic Mapping Using Monocular Frontal View Images.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01431) · 📚 被引 39
- **作者**: Nikhil Gosala, Kürsat Petek, Paulo L. J. Drews-Jr, Wolfram Burgard, Abhinav Valada
- **🏷️ 机构**: University of Freiburg, Federal University of Rio Grande
- **会议**: CVPR 2023

### Distilling Self-Supervised Vision Transformers for Weakly-Supervised Few-Shot Classification & Segmentation.
- **链接**: [arXiv:2307.03407](https://arxiv.org/abs/2307.03407)
- **作者**: Dahyun Kang, Piotr Koniusz, Minsu Cho, Naila Murray
- **🏷️ 机构**: Meta AI, Data61 &#x2665; CSIRO, POSTECH
- **会议**: CVPR 2023

- **摘要（英，原文）**:

  > We address the task of weakly-supervised few-shot image classification and segmentation, by leveraging a Vision Transformer (ViT) pretrained with self-supervision. Our proposed method takes token representations from the self-supervised ViT and leverages their correlations, via self-attention, to produce classification and segmentation predictions through separate task heads. Our model is able to effectively learn to perform classification and segmentation in the absence of pixel-level labels during training, using only image-level labels. To do this it uses attention maps, created from tokens generated by the self-supervised ViT backbone, as pixel-level pseudo-labels. We also explore a practical setup with ``mixed" supervision, where a small number of training images contains ground-truth pixel-level labels and the remaining images have only image-level labels. For this mixed setup, we propose to improve the pseudo-labels using a pseudo-label enhancer that was trained using the available ground-truth pixel-level labels. Experiments on Pascal-5i and COCO-20i demonstrate significant performance gains in a variety of supervision settings, and in particular when little-to-no pixel-level labels are available.

### MixMAE: Mixed and Masked Autoencoder for Efficient Pretraining of Hierarchical Vision Transformers.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00605) · 📚 被引 69
- **作者**: Jihao Liu, Xin Huang, Jinliang Zheng, Yu Liu, Hongsheng Li
- **🏷️ 机构**: CUHK MMLab, SenseTime Research
- **会议**: CVPR 2023

### SelfME: Self-Supervised Motion Learning for Micro-Expression Recognition.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01329) · 📚 被引 56
- **作者**: Xinqi Fan, Xueli Chen, Mingjie Jiang, Ali Raza Shahid, Hong Yan
- **🏷️ 机构**: City University of Hong Kong
- **会议**: CVPR 2023

### Semi-supervised learning made simple with self-supervised clustering.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00311) · 📚 被引 38
- **作者**: Enrico Fini, Pietro Astolfi, Karteek Alahari, Xavier Alameda-Pineda, Julien Mairal, Moin Nabi et al.
- **🏷️ 机构**: University of Trento, Inria, SAP AI Research
- **会议**: CVPR 2023

### Canonical Fields: Self-Supervised Learning of Pose-Canonicalized Neural Fields.
- **链接**: [arXiv:2212.02493](https://arxiv.org/abs/2212.02493) · 📚 被引 8
- **作者**: Rohith Agaram, Shaurya Dewan, Rahul Sajnani, Adrien Poulenard, K. Madhava Krishna, Srinath Sridhar
- **🏷️ 机构**: IIIT-Hyderabad,RRC, Brown University, Stanford University
- **会议**: CVPR 2023

- **摘要（英，原文）**:

  > Coordinate-based implicit neural networks, or neural fields, have emerged as useful representations of shape and appearance in 3D computer vision. Despite advances, however, it remains challenging to build neural fields for categories of objects without datasets like ShapeNet that provide "canonicalized" object instances that are consistently aligned for their 3D position and orientation (pose). We present Canonical Field Network (CaFi-Net), a self-supervised method to canonicalize the 3D pose of instances from an object category represented as neural fields, specifically neural radiance fields (NeRFs). CaFi-Net directly learns from continuous and noisy radiance fields using a Siamese network architecture that is designed to extract equivariant field features for category-level canonicalization. During inference, our method takes pre-trained neural radiance fields of novel object instances at arbitrary 3D pose and estimates a canonical field with consistent 3D pose across the entire category. Extensive experiments on a new dataset of 1300 NeRF models across 13 object categories show that our method matches or exceeds the performance of 3D point cloud-based methods.

### Look, Radiate, and Learn: Self-Supervised Localisation via Radio-Visual Correspondence.
- **链接**: [arXiv:2206.06424](https://arxiv.org/abs/2206.06424) · 📚 被引 3
- **作者**: Mohammed Alloulah, Maximilian Arnold
- **🏷️ 机构**: Nokia Bell Labs
- **会议**: CVPR 2023

- **摘要（英，原文）**:

  > Next generation cellular networks will implement radio sensing functions alongside customary communications, thereby enabling unprecedented worldwide sensing coverage outdoors. Deep learning has revolutionised computer vision but has had limited application to radio perception tasks, in part due to lack of systematic datasets and benchmarks dedicated to the study of the performance and promise of radio sensing. To address this gap, we present MaxRay: a synthetic radio-visual dataset and benchmark that facilitate precise target localisation in radio. We further propose to learn to localise targets in radio without supervision by extracting self-coordinates from radio-visual correspondence. We use such self-supervised coordinates to train a radio localiser network. We characterise our performance against a number of state-of-the-art baselines. Our results indicate that accurate radio target localisation can be automatically learned from paired radio-visual data without labels, which is important for empirical data. This opens the door for vast data scalability and may prove key to realising the promise of robust radio sensing atop a unified communication-perception cellular infrastructure. Dataset will be hosted on IEEE DataPort.

### Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture.
- **链接**: [arXiv:2301.08243](https://arxiv.org/abs/2301.08243)
- **作者**: Mahmoud Assran, Quentin Duval, Ishan Misra, Piotr Bojanowski, Pascal Vincent, Michael G. Rabbat et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

- **摘要（英，原文）**:

  > This paper demonstrates an approach for learning highly semantic image representations without relying on hand-crafted data-augmentations. We introduce the Image-based Joint-Embedding Predictive Architecture (I-JEPA), a non-generative approach for self-supervised learning from images. The idea behind I-JEPA is simple: from a single context block, predict the representations of various target blocks in the same image. A core design choice to guide I-JEPA towards producing semantic representations is the masking strategy; specifically, it is crucial to (a) sample target blocks with sufficiently large scale (semantic), and to (b) use a sufficiently informative (spatially distributed) context block. Empirically, when combined with Vision Transformers, we find I-JEPA to be highly scalable. For instance, we train a ViT-Huge/14 on ImageNet using 16 A100 GPUs in under 72 hours to achieve strong downstream performance across a wide range of tasks, from linear classification to object counting and depth prediction.

### Three Guidelines You Should Know for Universally Slimmable Self-Supervised Learning.
- **链接**: [arXiv:2303.06870](https://arxiv.org/abs/2303.06870) · [代码](https://github.com/megvii-research/US3L-CVPR2023) · 📚 被引 6
- **作者**: Yun-Hao Cao, Peiqin Sun, Shuchang Zhou
- **🏷️ 机构**: Nanjing University,State Key Laboratory for Novel Software Technology, MEGVII Technology
- **会议**: CVPR 2023

- **摘要（英，原文）**:

  > We propose universally slimmable self-supervised learning (dubbed as US3L) to achieve better accuracy-efficiency trade-offs for deploying self-supervised models across different devices. We observe that direct adaptation of self-supervised learning (SSL) to universally slimmable networks misbehaves as the training process frequently collapses. We then discover that temporal consistent guidance is the key to the success of SSL for universally slimmable networks, and we propose three guidelines for the loss design to ensure this temporal consistency from a unified gradient perspective. Moreover, we propose dynamic sampling and group regularization strategies to simultaneously improve training efficiency and accuracy. Our US3L method has been empirically validated on both convolutional neural networks and vision transformers. With only once training and one copy of weights, our method outperforms various state-of-the-art methods (individually trained or not) on benchmarks including recognition, object detection and instance segmentation. Our code is available at https://github.com/megvii-research/US3L-CVPR2023.

### Mixed Autoencoder for Self-Supervised Visual Representation Learning.
- **链接**: [arXiv:2303.17152](https://arxiv.org/abs/2303.17152) · 📚 被引 35
- **作者**: Kai Chen, Zhili Liu, Lanqing Hong, Hang Xu, Zhenguo Li, Dit-Yan Yeung
- **🏷️ 机构**: Hong Kong University of Science and Technology, Huawei Noah&#x0027;s Ark Lab
- **会议**: CVPR 2023

- **摘要（英，原文）**:

  > Masked Autoencoder (MAE) has demonstrated superior performance on various vision tasks via randomly masking image patches and reconstruction. However, effective data augmentation strategies for MAE still remain open questions, different from those in contrastive learning that serve as the most important part. This paper studies the prevailing mixing augmentation for MAE. We first demonstrate that naive mixing will in contrast degenerate model performance due to the increase of mutual information (MI). To address, we propose homologous recognition, an auxiliary pretext task, not only to alleviate the MI increasement by explicitly requiring each patch to recognize homologous patches, but also to perform object-aware self-supervised pre-training for better downstream dense perception performance. With extensive experiments, we demonstrate that our proposed Mixed Autoencoder (MixedAE) achieves the state-of-the-art transfer results among masked image modeling (MIM) augmentations on different downstream tasks with significant efficiency. Specifically, our MixedAE outperforms MAE by +0.3% accuracy, +1.7 mIoU and +0.9 AP on ImageNet-1K, ADE20K and COCO respectively with a standard ViT-Base. Moreover, MixedAE surpasses iBOT, a strong MIM method combined with instance discrimination, while accelerating training by 2x. To our best knowledge, this is the very first work to consider mixing for MIM from the perspective of pretext task design. Code will be made available.

### TexPose: Neural Texture Learning for Self-Supervised 6D Object Pose Estimation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00469) · 📚 被引 45
- **作者**: Hanzhi Chen, Fabian Manhardt, Nassir Navab, Benjamin Busam
- **🏷️ 机构**: Technical University of Munich, Google Inc.
- **会议**: CVPR 2023

### Beyond Appearance: A Semantic Controllable Self-Supervised Learning Framework for Human-Centric Visual Tasks.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01445) · 📚 被引 144
- **作者**: Weihua Chen, Xianzhe Xu, Jian Jia, Hao Luo, Yaohua Wang, Fan Wang et al.
- **🏷️ 机构**: Alibaba Group
- **会议**: CVPR 2023

### StepFormer: Self-Supervised Step Discovery and Localization in Instructional Videos.
- **链接**: [arXiv:2304.13265](https://arxiv.org/abs/2304.13265) · 📚 被引 22
- **作者**: Nikita Dvornik, Isma Hadji, Ran Zhang, Konstantinos G. Derpanis, Richard P. Wildes, Allan D. Jepson
- **🏷️ 机构**: Samsung AI Centre Toronto
- **会议**: CVPR 2023

- **摘要（英，原文）**:

  > Instructional videos are an important resource to learn procedural tasks from human demonstrations. However, the instruction steps in such videos are typically short and sparse, with most of the video being irrelevant to the procedure. This motivates the need to temporally localize the instruction steps in such videos, i.e. the task called key-step localization. Traditional methods for key-step localization require video-level human annotations and thus do not scale to large datasets. In this work, we tackle the problem with no human supervision and introduce StepFormer, a self-supervised model that discovers and localizes instruction steps in a video. StepFormer is a transformer decoder that attends to the video with learnable queries, and produces a sequence of slots capturing the key-steps in the video. We train our system on a large dataset of instructional videos, using their automatically-generated subtitles as the only source of supervision. In particular, we supervise our system with a sequence of text narrations using an order-aware loss function that filters out irrelevant phrases. We show that our model outperforms all previous unsupervised and weakly-supervised approaches on step detection and localization by a large margin on three challenging benchmarks. Moreover, our model demonstrates an emergent property to solve zero-shot multi-step localization and outperforms all relevant baselines at this task.

### Self-supervised Non-uniform Kernel Estimation with Flow-based Motion Prior for Blind Image Deblurring.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01736) · 📚 被引 60
- **作者**: Zhenxuan Fang, Fangfang Wu, Weisheng Dong, Xin Li, Jinjian Wu, Guangming Shi
- **🏷️ 机构**: Xidian University, West Virginia University
- **会议**: CVPR 2023

### Evolved Part Masking for Self-Supervised Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01001) · 📚 被引 24
- **作者**: Zhanzhou Feng, Shiliang Zhang
- **🏷️ 机构**: School of Computer Science, Peking University,National Key Laboratory for Multimedia Information Processing
- **会议**: CVPR 2023

### Self-Supervised Implicit Glyph Attention for Text Recognition.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01467) · 📚 被引 25
- **作者**: Tongkun Guan, Chaochen Gu, Jingzheng Tu, Xue Yang, Qi Feng, Yudi Zhao et al.
- **🏷️ 机构**: AI Institute, Shanghai Jiao Tong University,MoE Key Lab of Artificial Intelligence, Shanghai Jiao Tong University,Department of Automation
- **会议**: CVPR 2023

### Vid2Avatar: 3D Avatar Reconstruction from Videos in the Wild via Self-supervised Scene Decomposition.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01236) · 📚 被引 121
- **作者**: Chen Guo, Tianjian Jiang, Xu Chen, Jie Song, Otmar Hilliges
- **🏷️ 机构**: ETH Z&#x00FC;rich
- **会议**: CVPR 2023

### CLIP-S4: Language-Guided Self-Supervised Semantic Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01078)
- **作者**: Wenbin He, Suphanut Jamonnak, Liang Gou, Liu Ren
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### Geometric Visual Similarity Learning in 3D Medical Image Self-Supervised Pre-training.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00920) · 📚 被引 54
- **作者**: Yuting He, Guanyu Yang, Rongjun Ge, Yang Chen, Jean-Louis Coatrieux, Boyu Wang et al.
- **🏷️ 机构**: Southeast University, Nanjing University of Aeronautics and Astronautics, University of Rennes 1
- **会议**: CVPR 2023

### ReVISE: Self-Supervised Speech Resynthesis with Visual Input for Universal and Generalized Speech Regeneration.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01802) · 📚 被引 18
- **作者**: Wei-Ning Hsu, Tal Remez, Bowen Shi, Jacob Donley, Yossi Adi
- **🏷️ 机构**: FAIR, Meta AI Research, Meta Reality Labs Research
- **会议**: CVPR 2023

### Self-supervised AutoFlow.
- **链接**: [arXiv:2212.01762](https://arxiv.org/abs/2212.01762)
- **作者**: Hsin-Ping Huang, Charles Herrmann, Junhwa Hur, Erika Lu, Kyle Sargent, Austin Stone et al.
- **🏷️ 机构**: UC Merced
- **会议**: CVPR 2023

- **摘要（英，原文）**:

  > Recently, AutoFlow has shown promising results on learning a training set for optical flow, but requires ground truth labels in the target domain to compute its search metric. Observing a strong correlation between the ground truth search metric and self-supervised losses, we introduce self-supervised AutoFlow to handle real-world videos without ground truth labels. Using self-supervised loss as the search metric, our self-supervised AutoFlow performs on par with AutoFlow on Sintel and KITTI where ground truth is available, and performs better on the real-world DAVIS dataset. We further explore using self-supervised AutoFlow in the (semi-)supervised setting and obtain competitive results against the state of the art.

### Self-Supervised Pre-Training with Masked Shape Prediction for 3D Scene Understanding.
- **链接**: [arXiv:2305.05026](https://arxiv.org/abs/2305.05026) · 📚 被引 14
- **作者**: Li Jiang, Zetong Yang, Shaoshuai Shi, Vladislav Golyanik, Dengxin Dai, Bernt Schiele
- **🏷️ 机构**: Max Planck Institute for Informatics,Saarland Informatics Campus, CUHK
- **会议**: CVPR 2023

- **摘要（英，原文）**:

  > Masked signal modeling has greatly advanced self-supervised pre-training for language and 2D images. However, it is still not fully explored in 3D scene understanding. Thus, this paper introduces Masked Shape Prediction (MSP), a new framework to conduct masked signal modeling in 3D scenes. MSP uses the essential 3D semantic cue, i.e., geometric shape, as the prediction target for masked points. The context-enhanced shape target consisting of explicit shape context and implicit deep shape feature is proposed to facilitate exploiting contextual cues in shape prediction. Meanwhile, the pre-training architecture in MSP is carefully designed to alleviate the masked shape leakage from point coordinates. Experiments on multiple 3D understanding tasks on both indoor and outdoor datasets demonstrate the effectiveness of MSP in learning good feature representations to consistently boost downstream performance.

### Self-Supervised Representation Learning for CAD.
- **链接**: [arXiv:2210.10807](https://arxiv.org/abs/2210.10807)
- **作者**: Benjamin T. Jones, Michael Hu, Milin Kodnongbua, Vladimir G. Kim, Adriana Schulz
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

- **摘要（英，原文）**:

  > The design of man-made objects is dominated by computer aided design (CAD) tools. Assisting design with data-driven machine learning methods is hampered by lack of labeled data in CAD's native format; the parametric boundary representation (B-Rep). Several data sets of mechanical parts in B-Rep format have recently been released for machine learning research. However, large scale databases are largely unlabeled, and labeled datasets are small. Additionally, task specific label sets are rare, and costly to annotate. This work proposes to leverage unlabeled CAD geometry on supervised learning tasks. We learn a novel, hybrid implicit/explicit surface representation for B-Rep geometry, and show that this pre-training significantly improves few-shot learning performance and also achieves state-of-the-art performance on several existing B-Rep benchmarks.

### Benchmarking Self-Supervised Learning on Diverse Pathology Datasets.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00326) · 📚 被引 173
- **作者**: Mingu Kang, Heon Song, Seonwook Park, Donggeun Yoo, Sérgio Pereira
- **🏷️ 机构**: Lunit Inc.
- **会议**: CVPR 2023

### Self-Supervised Geometry-Aware Encoder for Style-Based 3D GAN Inversion.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02006) · 📚 被引 27
- **作者**: Yushi Lan, Xuyi Meng, Shuai Yang, Chen Change Loy, Bo Dai
- **🏷️ 机构**: Nanyang Technological University,S-Lab,Singapore, Shanghai AI Laboratory
- **会议**: CVPR 2023

### SCOOP: Self-Supervised Correspondence and Optimization-Based Scene Flow.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00511) · 📚 被引 34
- **作者**: Itai Lang, Dror Aiger, Forrester Cole, Shai Avidan, Michael Rubinstein
- **🏷️ 机构**: Tel Aviv University, Google Research
- **会议**: CVPR 2023

### Correlational Image Modeling for Self-Supervised Visual Pre-Training.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01450) · 📚 被引 13
- **作者**: Wei Li, Jiahao Xie, Chen Change Loy
- **🏷️ 机构**: Nanyang Technological University,S-Lab
- **会议**: CVPR 2023

### Token Boosting for Robust Self-Supervised Visual Transformer Pre-training.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02301) · 📚 被引 6
- **作者**: Tianjiao Li, Lin Geng Foo, Ping Hu, Xindi Shang, Hossein Rahmani, Zehuan Yuan et al.
- **🏷️ 机构**: Singapore University of Technology and Design, Boston University, ByteDance
- **会议**: CVPR 2023

### SECAD-Net: Self-Supervised CAD Reconstruction by Learning Sketch-Extrude Operations.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01613) · 📚 被引 50
- **作者**: Pu Li, Jianwei Guo, Xiaopeng Zhang, Dong-Ming Yan
- **🏷️ 机构**: Institute of Automation, Chinese Academy of Sciences,MAIS
- **会议**: CVPR 2023

### Spatial-then-Temporal Self-Supervised Learning for Video Correspondence.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00226) · 📚 被引 10
- **作者**: Rui Li, Dong Liu
- **🏷️ 机构**: University of Science and Technology of China,Hefei,China
- **会议**: CVPR 2023

### Self-Supervised Blind Motion Deblurring with Deep Expectation Maximization.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01344) · 📚 被引 15
- **作者**: Ji Li, Weixi Wang, Yuesong Nan, Hui Ji
- **🏷️ 机构**: National University of Singapore,Department of Mathematics,Singapore,119076
- **会议**: CVPR 2023

### Unified Mask Embedding and Correspondence Learning for Self-Supervised Video Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01794)
- **作者**: Liulei Li, Wenguan Wang, Tianfei Zhou, Jianwu Li, Yi Yang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### Spatially Adaptive Self-Supervised Learning for Real-World Image Denoising.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00956) · 📚 被引 58
- **作者**: Junyi Li, Zhilu Zhang, Xiaoyu Liu, Chaoyu Feng, Xiaotao Wang, Lei Lei et al.
- **🏷️ 机构**: School of Computer Science and Technology, Harbin Institute of Technology,China
- **会议**: CVPR 2023

### Pose-disentangled Contrastive Learning for Self-supervised Facial Representation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00937) · 📚 被引 29
- **作者**: Yuanyuan Liu, Wenbin Wang, Yibing Zhan, Shaoze Feng, Kejun Liu, Zhe Chen
- **🏷️ 机构**: School of Computer Science, China University of Geosciences,Wuhan,China, JD Explore Academy,China, The University of Sydney,Australia
- **会议**: CVPR 2023

### Multiple Instance Learning via Iterative Self-Paced Supervised Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00327) · 📚 被引 34
- **作者**: Kangning Liu, Weicheng Zhu, Yiqiu Shen, Sheng Liu, Narges Razavian, Krzysztof J. Geras et al.
- **🏷️ 机构**: NYU Center for Data Science, NYU Grossman School of Medicine
- **会议**: CVPR 2023

### Markerless Camera-to-Robot Pose Estimation via Self-Supervised Sim-to-Real Transfer.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02040) · 📚 被引 29
- **作者**: Jingpei Lu, Florian Richter, Michael C. Yip
- **🏷️ 机构**: University of California,San Diego
- **会议**: CVPR 2023

### DrapeNet: Garment Generation and Self-Supervised Draping.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00146) · 📚 被引 51
- **作者**: Luca De Luigi, Ren Li, Benoît Guillard, Mathieu Salzmann, Pascal Fua
- **🏷️ 机构**: University of Bologna, EPFL,CVLab
- **会议**: CVPR 2023

### Self-Supervised Image-to-Point Distillation via Semantically Tolerant Contrastive Loss.
- **链接**: [arXiv:2301.05709](https://arxiv.org/abs/2301.05709)
- **作者**: Anas Mahmoud, Jordan S. K. Hu, Tianshu Kuai, Ali Harakeh, Liam Paull, Steven L. Waslander
- **🏷️ 机构**: University of Toronto Robotics Institute, Mila, Universit&#x00E9; de Montr&#x00E9;al
- **会议**: CVPR 2023

- **摘要（英，原文）**:

  > An effective framework for learning 3D representations for perception tasks is distilling rich self-supervised image features via contrastive learning. However, image-to point representation learning for autonomous driving datasets faces two main challenges: 1) the abundance of self-similarity, which results in the contrastive losses pushing away semantically similar point and image regions and thus disturbing the local semantic structure of the learned representations, and 2) severe class imbalance as pretraining gets dominated by over-represented classes. We propose to alleviate the self-similarity problem through a novel semantically tolerant image-to-point contrastive loss that takes into consideration the semantic distance between positive and negative image regions to minimize contrasting semantically similar point and image regions. Additionally, we address class imbalance by designing a class-agnostic balanced loss that approximates the degree of class imbalance through an aggregate sample-to-samples semantic similarity measure. We demonstrate that our semantically-tolerant contrastive loss with class balancing improves state-of-the art 2D-to-3D representation learning in all evaluation settings on 3D semantic segmentation. Our method consistently outperforms state-of-the-art 2D-to-3D representation learning frameworks across a wide range of 2D self-supervised pretrained models.

### HaLP: Hallucinating Latent Positives for Skeleton-based Self-Supervised Learning of Actions.
- **链接**: [arXiv:2304.00387](https://arxiv.org/abs/2304.00387) · [代码](https://github.com/anshulbshah/HaLP) · 📚 被引 41
- **作者**: Anshul Shah, Aniket Roy, Ketul Shah, Shlok Mishra, David Jacobs, Anoop Cherian et al.
- **🏷️ 机构**: Johns Hopkins University, University of Maryland,College Park, MERL
- **会议**: CVPR 2023

- **摘要（英，原文）**:

  > Supervised learning of skeleton sequence encoders for action recognition has received significant attention in recent times. However, learning such encoders without labels continues to be a challenging problem. While prior works have shown promising results by applying contrastive learning to pose sequences, the quality of the learned representations is often observed to be closely tied to data augmentations that are used to craft the positives. However, augmenting pose sequences is a difficult task as the geometric constraints among the skeleton joints need to be enforced to make the augmentations realistic for that action. In this work, we propose a new contrastive learning approach to train models for skeleton-based action recognition without labels. Our key contribution is a simple module, HaLP - to Hallucinate Latent Positives for contrastive learning. Specifically, HaLP explores the latent space of poses in suitable directions to generate new positives. To this end, we present a novel optimization formulation to solve for the synthetic positives with an explicit control on their hardness. We propose approximations to the objective, making them solvable in closed form with minimal overhead. We show via experiments that using these generated positives within a standard contrastive learning framework leads to consistent improvements across benchmarks such as NTU-60, NTU-120, and PKU-II on tasks like linear evaluation, transfer learning, and kNN evaluation. Our code will be made available at https://github.com/anshulbshah/HaLP.

### Self-Supervised 3D Scene Flow Estimation Guided by Superpoints.
- **链接**: [arXiv:2305.02528](https://arxiv.org/abs/2305.02528) · 📚 被引 33
- **作者**: Yaqi Shen, Le Hui, Jin Xie, Jian Yang
- **🏷️ 机构**: Nanjing University of Science and Technology,PCA Lab,Nanjing,China
- **会议**: CVPR 2023

- **摘要（英，原文）**:

  > 3D scene flow estimation aims to estimate point-wise motions between two consecutive frames of point clouds. Superpoints, i.e., points with similar geometric features, are usually employed to capture similar motions of local regions in 3D scenes for scene flow estimation. However, in existing methods, superpoints are generated with the offline clustering methods, which cannot characterize local regions with similar motions for complex 3D scenes well, leading to inaccurate scene flow estimation. To this end, we propose an iterative end-to-end superpoint based scene flow estimation framework, where the superpoints can be dynamically updated to guide the point-level flow prediction. Specifically, our framework consists of a flow guided superpoint generation module and a superpoint guided flow refinement module. In our superpoint generation module, we utilize the bidirectional flow information at the previous iteration to obtain the matching points of points and superpoint centers for soft point-to-superpoint association construction, in which the superpoints are generated for pairwise point clouds. With the generated superpoints, we first reconstruct the flow for each point by adaptively aggregating the superpoint-level flow, and then encode the consistency between the reconstructed flow of pairwise point clouds. Finally, we feed the consistency encoding along with the reconstructed flow into GRU to refine point-level flow. Extensive experiments on several different datasets show that our method can achieve promising performance.

### Learning Common Rationale to Improve Self-Supervised Representation for Fine-Grained Visual Recognition Problems.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01096) · 📚 被引 25
- **作者**: Yangyang Shu, Anton van den Hengel, Lingqiao Liu
- **🏷️ 机构**: School of Computer Science, The University of Adelaide
- **会议**: CVPR 2023

### Multi-Mode Online Knowledge Distillation for Self-Supervised Visual Representation Learning.
- **链接**: [arXiv:2304.06461](https://arxiv.org/abs/2304.06461)
- **作者**: Kaiyou Song, Jin Xie, Shan Zhang, Zimeng Luo
- **🏷️ 机构**: Megvii Technology
- **会议**: CVPR 2023

- **摘要（英，原文）**:

  > Self-supervised learning (SSL) has made remarkable progress in visual representation learning. Some studies combine SSL with knowledge distillation (SSL-KD) to boost the representation learning performance of small models. In this study, we propose a Multi-mode Online Knowledge Distillation method (MOKD) to boost self-supervised visual representation learning. Different from existing SSL-KD methods that transfer knowledge from a static pre-trained teacher to a student, in MOKD, two different models learn collaboratively in a self-supervised manner. Specifically, MOKD consists of two distillation modes: self-distillation and cross-distillation modes. Among them, self-distillation performs self-supervised learning for each model independently, while cross-distillation realizes knowledge interaction between different models. In cross-distillation, a cross-attention feature search strategy is proposed to enhance the semantic feature alignment between different models. As a result, the two models can absorb knowledge from each other to boost their representation learning performance. Extensive experimental results on different backbones and datasets demonstrate that two heterogeneous models can benefit from MOKD and outperform their independently trained baseline. In addition, MOKD also outperforms existing SSL-KD methods for both the student and teacher models.

### Masked Motion Encoding for Self-Supervised Video Representation Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00222)
- **作者**: Xinyu Sun, Peihao Chen, Liangwei Chen, Changhao Li, Thomas H. Li, Mingkui Tan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### SMOC-Net: Leveraging Camera Pose for Self-Supervised Monocular Object Pose Estimation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02041) · 📚 被引 18
- **作者**: Tao Tan, Qiulei Dong
- **🏷️ 机构**: School of Artificial Intelligence, UCAS
- **会议**: CVPR 2023

### Siamese Image Modeling for Self-Supervised Vision Representation Learning.
- **链接**: [arXiv:2206.01204](https://arxiv.org/abs/2206.01204) · [代码](https://github.com/fundamentalvision/Siamese-Image-Modeling) · 📚 被引 78
- **作者**: Chenxin Tao, Xizhou Zhu, Weijie Su, Gao Huang, Bin Li, Jie Zhou et al.
- **🏷️ 机构**: Tsinghua University, SenseTime Research, University of Science and Technology of China
- **会议**: CVPR 2023

- **摘要（英，原文）**:

  > Self-supervised learning (SSL) has delivered superior performance on a variety of downstream vision tasks. Two main-stream SSL frameworks have been proposed, i.e., Instance Discrimination (ID) and Masked Image Modeling (MIM). ID pulls together representations from different views of the same image, while avoiding feature collapse. It lacks spatial sensitivity, which requires modeling the local structure within each image. On the other hand, MIM reconstructs the original content given a masked image. It instead does not have good semantic alignment, which requires projecting semantically similar views into nearby representations. To address this dilemma, we observe that (1) semantic alignment can be achieved by matching different image views with strong augmentations; (2) spatial sensitivity can benefit from predicting dense representations with masked images. Driven by these analysis, we propose Siamese Image Modeling (SiameseIM), which predicts the dense representations of an augmented view, based on another masked view from the same image but with different augmentations. SiameseIM uses a Siamese network with two branches. The online branch encodes the first view, and predicts the second view's representation according to the relative positions between these two views. The target branch produces the target by encoding the second view. SiameseIM can surpass both ID and MIM on a wide range of downstream tasks, including ImageNet finetuning and linear probing, COCO and LVIS detection, and ADE20k semantic segmentation. The improvement is more significant in few-shot, long-tail and robustness-concerned scenarios. Code shall be released at https://github.com/fundamentalvision/Siamese-Image-Modeling.

### Defending Against Patch-based Backdoor Attacks on Self-Supervised Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01178) · 📚 被引 23
- **作者**: Ajinkya Tejankar, Maziar Sanjabi, Qifan Wang, Sinong Wang, Hamed Firooz, Hamed Pirsiavash et al.
- **🏷️ 机构**: University of California,Davis, Meta AI
- **会议**: CVPR 2023

### Learning with Noisy labels via Self-supervised Adversarial Noisy Masking.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01553) · 📚 被引 27
- **作者**: Yuanpeng Tu, Boshen Zhang, Yuxi Li, Liang Liu, Jian Li, Jiangning Zhang et al.
- **🏷️ 机构**: Tongji Univeristy,Dept. of Electronic and Information Engineering,Shanghai, Tencent,YouTu Lab,Shanghai
- **会议**: CVPR 2023

### PatchCraft Self-Supervised Training for Correlated Image Denoising.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00561) · 📚 被引 13
- **作者**: Gregory Vaksman, Michael Elad
- **🏷️ 机构**: CS Department - The Technion,Haifa,Israel
- **会议**: CVPR 2023

### Masked Video Distillation: Rethinking Masked Feature Modeling for Self-supervised Video Representation Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00611)
- **作者**: Rui Wang, Dongdong Chen, Zuxuan Wu, Yinpeng Chen, Xiyang Dai, Mengchen Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### LG-BPN: Local and Global Blind-Patch Network for Self-Supervised Real-World Denoising.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01741) · 📚 被引 74
- **作者**: Zichun Wang, Ying Fu, Ji Liu, Yulun Zhang
- **🏷️ 机构**: Beijing Institute of Technology, Baidu Inc.,Beijing,China, ETH Z&#x00FC;rich
- **会议**: CVPR 2023

### DLBD: A Self-Supervised Direct-Learned Binary Descriptor.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01521) · 📚 被引 7
- **作者**: Bin Xiao, Yang Hu, Bo Liu, Xiuli Bi, Weisheng Li, Xinbo Gao
- **🏷️ 机构**: Chongqing University of Posts and Telecommunications,Chongqing,China
- **会议**: CVPR 2023

### MAESTER: Masked Autoencoder Guided Segmentation at Pixel Resolution for Accurate, Self-Supervised Subcellular Structure Recognition.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00321) · 📚 被引 18
- **作者**: Ronald Xie, Kuan Pang, Gary D. Bader, Bo Wang
- **🏷️ 机构**: University of Toronto
- **会议**: CVPR 2023

### Self-Supervised Super-Plane for Neural 3D Reconstruction.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02051) · 📚 被引 13
- **作者**: Botao Ye, Sifei Liu, Xueting Li, Ming-Hsuan Yang
- **🏷️ 机构**: University of Chinese Academy of Sciences, NVIDIA, University of California,Merced
- **会议**: CVPR 2023

### CiCo: Domain-Aware Sign Language Retrieval via Cross-Lingual Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01823) · 📚 被引 32
- **作者**: Yiting Cheng, Fangyun Wei, Jianmin Bao, Dong Chen, Wenqiang Zhang
- **🏷️ 机构**: School of Computer Science, Fudan University, Microsoft Research Asia
- **会议**: CVPR 2023

### Dynamic Graph Enhanced Contrastive Learning for Chest X-Ray Report Generation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00325) · 📚 被引 173
- **作者**: Mingjie Li, Bingqian Lin, Zicong Chen, Haokun Lin, Xiaodan Liang, Xiaojun Chang
- **🏷️ 机构**: AAII, University of Technology Sydney,ReLER, School of ISE, Sun Yat-Sen University, The University of Hong Kong
- **会议**: CVPR 2023

### Promoting Semantic Connectivity: Dual Nearest Neighbors Contrastive Learning for Unsupervised Domain Generalization.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00342) · 📚 被引 12
- **作者**: Yuchen Liu, Yaoming Wang, Yabo Chen, Wenrui Dai, Chenglin Li, Junni Zou et al.
- **🏷️ 机构**: Shanghai Jiao Tong University,Department of Electronic Engineering,China, Shanghai Jiao Tong University,Department of Computer Science and Engineering,China
- **会议**: CVPR 2023

### Class Prototypes based Contrastive Learning for Classifying Multi-Label and Fine-Grained Educational Videos.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01908) · 📚 被引 16
- **作者**: Rohit Gupta, Anirban Roy, Claire Christensen, Sujeong Kim, Sarah Gerard, Madeline Cincebeaux et al.
- **🏷️ 机构**: University of Central Florida,Center for Research in Computer Vision, SRI International
- **会议**: CVPR 2023

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
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01907) · 📚 被引 18
- **作者**: Chen Feng, Ioannis Patras
- **🏷️ 机构**: Queen Mary University of London,UK
- **会议**: CVPR 2023

### Hyperbolic Contrastive Learning for Visual Representations beyond Objects.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00661) · 📚 被引 49
- **作者**: Songwei Ge, Shlok Mishra, Simon Kornblith, Chun-Liang Li, David Jacobs
- **🏷️ 机构**: University of Maryland,College Park, Google Research
- **会议**: CVPR 2023

### Twin Contrastive Learning with Noisy Labels.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01122) · 📚 被引 107
- **作者**: Zhizhong Huang, Junping Zhang, Hongming Shan
- **🏷️ 机构**: School of Computer Science, Fudan University,Shanghai Key Lab of Intelligent Information Processing,Shanghai,China,200433, Institute of Science and Technology for Brain-inspired Intelligence and MOE Frontiers Center for Brain Science, Fudan University,Shanghai,China,200433
- **会议**: CVPR 2023

### Actionlet-Dependent Contrastive Learning for Unsupervised Skeleton-Based Action Recognition.
- **链接**: [arXiv:2303.10904](https://arxiv.org/abs/2303.10904) · 📚 被引 92
- **作者**: Lilang Lin, Jiahang Zhang, Jiaying Liu
- **🏷️ 机构**: Wangxuan Institute of Computer Technology, Peking University,Beijing,China
- **会议**: CVPR 2023

- **摘要（英，原文）**:

  > The self-supervised pretraining paradigm has achieved great success in skeleton-based action recognition. However, these methods treat the motion and static parts equally, and lack an adaptive design for different parts, which has a negative impact on the accuracy of action recognition. To realize the adaptive action modeling of both parts, we propose an Actionlet-Dependent Contrastive Learning method (ActCLR). The actionlet, defined as the discriminative subset of the human skeleton, effectively decomposes motion regions for better action modeling. In detail, by contrasting with the static anchor without motion, we extract the motion region of the skeleton data, which serves as the actionlet, in an unsupervised manner. Then, centering on actionlet, a motion-adaptive data transformation method is built. Different data transformations are applied to actionlet and non-actionlet regions to introduce more diversity while maintaining their own characteristics. Meanwhile, we propose a semantic-aware feature pooling method to build feature representations among motion and static regions in a distinguished manner. Extensive experiments on NTU RGB+D and PKUMMD show that the proposed method achieves remarkable action recognition performance. More visualization and quantitative experiments demonstrate the effectiveness of our method. Our project website is available at https://langlandslin.github.io/projects/ActCLR/

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
- **链接**: [arXiv:2303.07815](https://arxiv.org/abs/2303.07815)
- **作者**: Roy Miles, Mehmet Kerim Yucel, Bruno Manganelli, Albert Saà-Garriga
- **🏷️ 机构**: Samsung Research,UK
- **会议**: CVPR 2023

- **摘要（英，原文）**:

  > This paper tackles the problem of semi-supervised video object segmentation on resource-constrained devices, such as mobile phones. We formulate this problem as a distillation task, whereby we demonstrate that small space-time-memory networks with finite memory can achieve competitive results with state of the art, but at a fraction of the computational cost (32 milliseconds per frame on a Samsung Galaxy S22). Specifically, we provide a theoretically grounded framework that unifies knowledge distillation with supervised contrastive representation learning. These models are able to jointly benefit from both pixel-wise contrastive learning and distillation from a pre-trained teacher. We validate this loss by achieving competitive J&F to state of the art on both the standard DAVIS and YouTube benchmarks, despite running up to 5x faster, and with 32x fewer parameters.

### Dynamic Conceptional Contrastive Learning for Generalized Category Discovery.
- **链接**: [arXiv:2303.17393](https://arxiv.org/abs/2303.17393) · [代码](https://github.com/TPCD/DCCL) · 📚 被引 94
- **作者**: Nan Pu, Zhun Zhong, Nicu Sebe
- **🏷️ 机构**: University of Trento,The Department of Information Engineering and Computer Science,Trento,Italy
- **会议**: CVPR 2023

- **摘要（英，原文）**:

  > Generalized category discovery (GCD) is a recently proposed open-world problem, which aims to automatically cluster partially labeled data. The main challenge is that the unlabeled data contain instances that are not only from known categories of the labeled data but also from novel categories. This leads traditional novel category discovery (NCD) methods to be incapacitated for GCD, due to their assumption of unlabeled data are only from novel categories. One effective way for GCD is applying self-supervised learning to learn discriminate representation for unlabeled data. However, this manner largely ignores underlying relationships between instances of the same concepts (e.g., class, super-class, and sub-class), which results in inferior representation learning. In this paper, we propose a Dynamic Conceptional Contrastive Learning (DCCL) framework, which can effectively improve clustering accuracy by alternately estimating underlying visual conceptions and learning conceptional representation. In addition, we design a dynamic conception generation and update mechanism, which is able to ensure consistent conception learning and thus further facilitate the optimization of DCCL. Extensive experiments show that DCCL achieves new state-of-the-art performances on six generic and fine-grained visual recognition datasets, especially on fine-grained ones. For example, our method significantly surpasses the best competitor by 16.2% on the new classes for the CUB-200 dataset. Code is available at https://github.com/TPCD/DCCL.

### TranSG: Transformer-Based Skeleton Graph Prototype Contrastive Learning with Structure-Trajectory Prompted Reconstruction for Person Re-Identification.
- **链接**: [arXiv:2303.06819](https://arxiv.org/abs/2303.06819) · 📚 被引 51
- **作者**: Haocong Rao, Chunyan Miao
- **🏷️ 机构**: LILY Research Center, Nanyang Technological University, Singapore School of Computer Science and Engineering, Nanyang Technological University,Singapore
- **会议**: CVPR 2023

- **摘要（英，原文）**:

  > Person re-identification (re-ID) via 3D skeleton data is an emerging topic with prominent advantages. Existing methods usually design skeleton descriptors with raw body joints or perform skeleton sequence representation learning. However, they typically cannot concurrently model different body-component relations, and rarely explore useful semantics from fine-grained representations of body joints. In this paper, we propose a generic Transformer-based Skeleton Graph prototype contrastive learning (TranSG) approach with structure-trajectory prompted reconstruction to fully capture skeletal relations and valuable spatial-temporal semantics from skeleton graphs for person re-ID. Specifically, we first devise the Skeleton Graph Transformer (SGT) to simultaneously learn body and motion relations within skeleton graphs, so as to aggregate key correlative node features into graph representations. Then, we propose the Graph Prototype Contrastive learning (GPC) to mine the most typical graph features (graph prototypes) of each identity, and contrast the inherent similarity between graph representations and different prototypes from both skeleton and sequence levels to learn discriminative graph representations. Last, a graph Structure-Trajectory Prompted Reconstruction (STPR) mechanism is proposed to exploit the spatial and temporal contexts of graph nodes to prompt skeleton graph reconstruction, which facilitates capturing more valuable patterns and graph semantics for person re-ID. Empirical evaluations demonstrate that TranSG significantly outperforms existing state-of-the-art methods. We further show its generality under different graph modeling, RGB-estimated skeletons, and unsupervised scenarios.

### Positive-Augmented Contrastive Learning for Image and Video Captioning Evaluation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00668) · 📚 被引 46
- **作者**: Sara Sarto, Manuele Barraco, Marcella Cornia, Lorenzo Baraldi, Rita Cucchiara
- **🏷️ 机构**: University of Modena and Reggio Emilia,Modena,Italy
- **会议**: CVPR 2023

### FEND: A Future Enhanced Distribution-Aware Contrastive Learning Framework for Long-Tail Trajectory Prediction.
- **链接**: [arXiv:2303.16574](https://arxiv.org/abs/2303.16574) · 📚 被引 43
- **作者**: Yuning Wang, Pu Zhang, Lei Bai, Jianru Xue
- **🏷️ 机构**: Institute of Artificial Intelligence and Robotics, Xi&#x0027;an Jiaotong University,China, DiDi Chuxing,China, Shanghai AI Laboratory,China
- **会议**: CVPR 2023

- **摘要（英，原文）**:

  > Predicting the future trajectories of the traffic agents is a gordian technique in autonomous driving. However, trajectory prediction suffers from data imbalance in the prevalent datasets, and the tailed data is often more complicated and safety-critical. In this paper, we focus on dealing with the long-tail phenomenon in trajectory prediction. Previous methods dealing with long-tail data did not take into account the variety of motion patterns in the tailed data. In this paper, we put forward a future enhanced contrastive learning framework to recognize tail trajectory patterns and form a feature space with separate pattern clusters. Furthermore, a distribution aware hyper predictor is brought up to better utilize the shaped feature space. Our method is a model-agnostic framework and can be plugged into many well-known baselines. Experimental results show that our framework outperforms the state-of-the-art long-tail prediction method on tailed samples by 9.5% on ADE and 8.5% on FDE, while maintaining or slightly improving the averaged performance. Our method also surpasses many long-tail techniques on trajectory prediction task.

### MoLo: Motion-Augmented Long-Short Contrastive Learning for Few-Shot Action Recognition.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01727) · 📚 被引 92
- **作者**: Xiang Wang, Shiwei Zhang, Zhiwu Qing, Changxin Gao, Yingya Zhang, Deli Zhao et al.
- **🏷️ 机构**: School of Artificial Intelligence and Automation, Huazhong University of Science and Technology,Key Laboratory of Image Processing and Intelligent Control, Alibaba Group
- **会议**: CVPR 2023

### ContraNeRF: Generalizable Neural Radiance Fields for Synthetic-to-real Novel View Synthesis via Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01584) · 📚 被引 21
- **作者**: Hao Yang, Lanqing Hong, Aoxue Li, Tianyang Hu, Zhenguo Li, Gim Hee Lee et al.
- **🏷️ 机构**: Peking University,Center for Data Science, Huawei Noah&#x0027;s Ark Lab, School of Computing, National University of Singapore
- **会议**: CVPR 2023

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
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01061) · 📚 被引 19
- **作者**: Jinghao Zhou, Li Dong, Zhe Gan, Lijuan Wang, Furu Wei
- **🏷️ 机构**: Microsoft
- **会议**: CVPR 2023

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
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00999) · 📚 被引 52
- **作者**: Zhenda Xie, Zheng Zhang, Yue Cao, Yutong Lin, Yixuan Wei, Qi Dai et al.
- **🏷️ 机构**: Tsinghua University, Xi&#x0027;an Jiaotong University, Microsoft Research Asia
- **会议**: CVPR 2023

### Stare at What You See: Masked Image Modeling without Reconstruction.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02177) · 📚 被引 22
- **作者**: Hongwei Xue, Peng Gao, Hongyang Li, Yu Qiao, Hao Sun, Houqiang Li et al.
- **🏷️ 机构**: University of Science and Technology of China, Shanghai Artificial Intelligence Laboratory, China Telecom Corporation Ltd., Data&#x0026;AI Technology Company
- **会议**: CVPR 2023

### PMatch: Paired Masked Image Modeling for Dense Geometric Matching.
- **链接**: [arXiv:2303.17342](https://arxiv.org/abs/2303.17342) · [代码](https://github.com/ShngJZ/PMatch) · 📚 被引 43
- **作者**: Shengjie Zhu, Xiaoming Liu
- **🏷️ 机构**: Michigan State University,Department of Computer Science and Engineering,East Lansing,MI,48824
- **会议**: CVPR 2023

- **摘要（英，原文）**:

  > Dense geometric matching determines the dense pixel-wise correspondence between a source and support image corresponding to the same 3D structure. Prior works employ an encoder of transformer blocks to correlate the two-frame features. However, existing monocular pretraining tasks, e.g., image classification, and masked image modeling (MIM), can not pretrain the cross-frame module, yielding less optimal performance. To resolve this, we reformulate the MIM from reconstructing a single masked image to reconstructing a pair of masked images, enabling the pretraining of transformer module. Additionally, we incorporate a decoder into pretraining for improved upsampling results. Further, to be robust to the textureless area, we propose a novel cross-frame global matching module (CFGM). Since the most textureless area is planar surfaces, we propose a homography loss to further regularize its learning. Combined together, we achieve the State-of-The-Art (SoTA) performance on geometric matching. Codes and models are available at https://github.com/ShngJZ/PMatch.

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
- PlaneDepth: Self-Supervised Depth Estimation via Orthogonal Planes. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- DualRefine: Self-Supervised Depth and Pose Estimation Through Iterative Epipolar Sampling and Refinement Toward Equilibrium. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- Self-Supervised Video Forensics by Audio-Visual Anomaly Detection. → [multimodal](../multimodal/Guideline%202023.md)
- Coreset Sampling from Open-Set for Fine-Grained Self-Supervised Learning. → [open-set-detection](../open-set-detection/Guideline%202023.md)
- Fully Self-Supervised Depth Estimation from Defocus Clue. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- Learning Audio-Visual Source Localization via False Negative Aware Contrastive Learning. → [multimodal](../multimodal/Guideline%202023.md)
- Hunting Sparsity: Density-Guided Contrastive Learning for Semi-Supervised Semantic Segmentation. → [network-pruning](../network-pruning/Guideline%202023.md)
