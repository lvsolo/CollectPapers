# Self-supervised Vision — 2023 Guideline

> 领域: 视觉自监督学习（对比学习、MAE、DINO 系）
> 论文数: 98 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Forecast-MAE: Self-supervised Pre-training for Motion Forecasting with Masked Autoencoders.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00797) · 📚 被引 104
- **作者**: Jie Cheng, Xiaodong Mei, Ming Liu
- **🏷️ 机构**: HKUST
- **会议**: ICCV 2023

### Temporal DINO: A Self-supervised Video Strategy to Enhance Action Prediction.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00352) · 📚 被引 3
- **作者**: Izzeddin Teeti, Rongali Sai Bhargav, Vivek Singh, Andrew Bradley, Biplab Banerjee, Fabio Cuzzolin
- **🏷️ 机构**: Oxford Brookes University,VAIL, Indian Institute of Technology,Bombay
- **会议**: ICCV 2023

### P2C: Self-Supervised Point Cloud Completion from Single Partial Clouds.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01320) · 📚 被引 43
- **作者**: Ruikai Cui, Shi Qiu, Saeed Anwar, Jiawei Liu, Chaoyue Xing, Jing Zhang et al.
- **🏷️ 机构**: Australian National University, King Fahd University of Petroleum and Minerals
- **会议**: ICCV 2023

### Point Contrastive Prediction with Semantic Clustering for Self-Supervised Learning on Point Cloud Videos.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01514) · 📚 被引 20
- **作者**: Xiaoxiao Sheng, Zhiqiang Shen, Gang Xiao, Longguang Wang, Yulan Guo, Hehe Fan
- **🏷️ 机构**: Shanghai Jiao Tong University, Aviation University of Air Force, Sun Yat-Sen University
- **会议**: ICCV 2023

### Masked Spatio-Temporal Structure Prediction for Self-supervised Learning on Point Cloud Videos.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01520) · 📚 被引 23
- **作者**: Zhiqiang Shen, Xiaoxiao Sheng, Hehe Fan, Longguang Wang, Yulan Guo, Qiong Liu et al.
- **🏷️ 机构**: Shanghai Jiao Tong University, Zhejiang University, Aviation University of Air Force
- **会议**: ICCV 2023

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

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We address the task of weakly-supervised few-shot image classification and segmentation, by leveraging a Vision Transformer (ViT) pretrained with self-supervision. Our proposed method takes token representations from the self-supervised ViT and leverages their correlations, via self-attention, to produce classification and segmentation predictions through separate task heads. Our model is able to effectively learn to perform classification and segmentation in the absence of pixel-level labels during training, using only image-level labels. To do this it uses attention maps, created from tokens generated by the self-supervised ViT backbone, as pixel-level pseudo-labels. We also explore a practical setup with ``mixed" supervision, where a small number of training images contains ground-truth pixel-level labels and the remaining images have only image-level labels. For this mixed setup, we propose to improve the pseudo-labels using a pseudo-label enhancer that was trained using the available ground-truth pixel-level labels. Experiments on Pascal-5i and COCO-20i demonstrate significant performance gains in a variety of supervision settings, and in particular when little-to-no pixel-level labels are available.

</details>

### MixMAE: Mixed and Masked Autoencoder for Efficient Pretraining of Hierarchical Vision Transformers.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00605) · 📚 被引 69
- **作者**: Jihao Liu, Xin Huang, Jinliang Zheng, Yu Liu, Hongsheng Li
- **🏷️ 机构**: CUHK MMLab, SenseTime Research
- **会议**: CVPR 2023

</details>

### Randomized Quantization: A Generic Augmentation for Data Agnostic Self-supervised Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01494) · 📚 被引 10
- **作者**: Huimin Wu, Chenyang Lei, Xiao Sun, Peng-Shuai Wang, Qifeng Chen, Kwang-Ting Cheng et al.
- **🏷️ 机构**: HKUST, CAIR, HKISI CAS, Shanghai AI Lab
- **会议**: ICCV 2023

### Self-Supervised Burst Super-Resolution.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00973)
- **作者**: Goutam Bhat, Michaël Gharbi, Jiawen Chen, Luc Van Gool, Zhihao Xia
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### Active Self-Supervised Learning: A Few Low-Cost Relationships Are All You Need.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01491) · 📚 被引 9
- **作者**: Vivien Cabannes, Léon Bottou, Yann LeCun, Randall Balestriero
- **🏷️ 机构**: Meta AI
- **会议**: ICCV 2023

### Contrastive Continuity on Augmentation Stability Rehearsal for Continual Self-Supervised Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00525) · 📚 被引 10
- **作者**: Haoyang Cheng, Haitao Wen, Xiaoliang Zhang, Heqian Qiu, Lanxiao Wang, Hongliang Li
- **🏷️ 机构**: University of Electronic Science and Technology of China,Chengdu,China
- **会议**: ICCV 2023

### Identity-Seeking Self-Supervised Representation Learning for Generalizable Person Re-identification.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01452) · 📚 被引 27
- **作者**: Zhaopeng Dou, Zhongdao Wang, Yali Li, Shengjin Wang
- **🏷️ 机构**: Tsinghua University,Department of Electronic Engineering,China
- **会议**: ICCV 2023

### SimFIR: A Simple Framework for Fisheye Image Rectification with Self-supervised Representation Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01141) · 📚 被引 27
- **作者**: Hao Feng, Wendi Wang, Jiajun Deng, Wengang Zhou, Li Li, Houqiang Li
- **🏷️ 机构**: University of Science and Technology of China,CAS Key Laboratory of Technology in GIPAS,EEIS Department, The University of Sydney
- **会议**: ICCV 2023

### TeD-SPAD: Temporal Distinctiveness for Self-supervised Privacy-preservation for video Anomaly Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01251)
- **作者**: Joseph Fioresi, Ishan Rajendrakumar Dave, Mubarak Shah
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### Self-supervised Character-to-Character Distillation for Text Recognition.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01784) · 📚 被引 40
- **作者**: Tongkun Guan, Wei Shen, Xue Yang, Qi Feng, Zekun Jiang, Xiaokang Yang
- **🏷️ 机构**: Shanghai Jiao Tong University,MoE Key Lab of Artificial Intelligence, AI Institute, Shanghai Jiao Tong University,Department of Automation
- **会议**: ICCV 2023

### Pseudo Flow Consistency for Self-Supervised 6D Object Pose Estimation.
- **链接**: [arXiv:2308.10016](https://arxiv.org/abs/2308.10016) · 📚 被引 17
- **作者**: Yang Hai, Rui Song, Jiaojiao Li, David Ferstl, Yinlin Hu
- **🏷️ 机构**: State Key Laboratory of ISN, Xidian University, MagicLeap
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Most self-supervised 6D object pose estimation methods can only work with additional depth information or rely on the accurate annotation of 2D segmentation masks, limiting their application range. In this paper, we propose a 6D object pose estimation method that can be trained with pure RGB images without any auxiliary information. We first obtain a rough pose initialization from networks trained on synthetic images rendered from the target's 3D mesh. Then, we introduce a refinement strategy leveraging the geometry constraint in synthetic-to-real image pairs from multiple different views. We formulate this geometry constraint as pixel-level flow consistency between the training images with dynamically generated pseudo labels. We evaluate our method on three challenging datasets and demonstrate that it outperforms state-of-the-art self-supervised methods significantly, with neither 2D annotations nor additional depth images.

</details>

### Self-supervised Image Denoising with Downsampled Invariance Loss and Conditional Blind-Spot Network.
- **链接**: [arXiv:2304.09507](https://arxiv.org/abs/2304.09507) · 📚 被引 15
- **作者**: Yeong Il Jang, Keuntek Lee, Gu Yong Park, Seyun Kim, Nam Ik Cho
- **🏷️ 机构**: Seoul National University,INMC,Department of ECE,Seoul,Korea, Gauss Labs Inc.
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> There have been many image denoisers using deep neural networks, which outperform conventional model-based methods by large margins. Recently, self-supervised methods have attracted attention because constructing a large real noise dataset for supervised training is an enormous burden. The most representative self-supervised denoisers are based on blind-spot networks, which exclude the receptive field's center pixel. However, excluding any input pixel is abandoning some information, especially when the input pixel at the corresponding output position is excluded. In addition, a standard blind-spot network fails to reduce real camera noise due to the pixel-wise correlation of noise, though it successfully removes independently distributed synthetic noise. Hence, to realize a more practical denoiser, we propose a novel self-supervised training framework that can remove real noise. For this, we derive the theoretic upper bound of a supervised loss where the network is guided by the downsampled blinded output. Also, we design a conditional blind-spot network (C-BSN), which selectively controls the blindness of the network to use the center pixel information. Furthermore, we exploit a random subsampler to decorrelate noise spatially, making the C-BSN free of visual artifacts that were often seen in downsample-based methods. Extensive experiments show that the proposed C-BSN achieves state-of-the-art performance on real-world datasets as a self-supervised denoiser and shows qualitatively pleasing results without any post-processing or refinement.

</details>

### EMR-MSF: Self-Supervised Recurrent Monocular Scene Flow Exploiting Ego-Motion Rigidity.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00013) · 📚 被引 0
- **作者**: Zijie Jiang, Masatoshi Okutomi
- **🏷️ 机构**: Tokyo Institute of Technology
- **会议**: ICCV 2023

### Anatomical Invariance Modeling and Semantic Alignment for Self-supervised Learning in 3D Medical Image Analysis.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01453) · 📚 被引 27
- **作者**: Yankai Jiang, Mingze Sun, Heng Guo, Xiaoyu Bai, Ke Yan, Le Lu et al.
- **🏷️ 机构**: Alibaba Group,DAMO Academy
- **会议**: ICCV 2023

### An Embarrassingly Simple Backdoor Attack on Self-supervised Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00403) · 📚 被引 48
- **作者**: Changjiang Li, Ren Pang, Zhaohan Xi, Tianyu Du, Shouling Ji, Yuan Yao et al.
- **🏷️ 机构**: Pennsylvania State University, Zhejiang University, Nanjing University
- **会议**: ICCV 2023

### Self-supervised Pre-training for Mirror Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01123) · 📚 被引 7
- **作者**: Jiaying Lin, Rynson W. H. Lau
- **🏷️ 机构**: City University of Hong Kong
- **会议**: ICCV 2023

### Geometrized Transformer for Self-Supervised Homography Estimation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00876) · 📚 被引 33
- **作者**: Jiazhen Liu, Xirong Li
- **🏷️ 机构**: Renmin University of China,Key Lab of DEKE
- **会议**: ICCV 2023

### DDS2M: Self-Supervised Denoising Diffusion Spatio-Spectral Model for Hyperspectral Image Restoration.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01110) · 📚 被引 74
- **作者**: Yuchun Miao, Lefei Zhang, Liangpei Zhang, Dacheng Tao
- **🏷️ 机构**: Wuhan University,National Engineering Research Center for Multimedia Software, School of Computer Science, Wuhan University,State Key Lab. of Information Engineering in Surveying, Mapping and Remote Sensing, The University of Sydney,Sydney AI Centre, School of Computer Science
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Coordinate-based implicit neural networks, or neural fields, have emerged as useful representations of shape and appearance in 3D computer vision. Despite advances, however, it remains challenging to build neural fields for categories of objects without datasets like ShapeNet that provide "canonicalized" object instances that are consistently aligned for their 3D position and orientation (pose). We present Canonical Field Network (CaFi-Net), a self-supervised method to canonicalize the 3D pose of instances from an object category represented as neural fields, specifically neural radiance fields (NeRFs). CaFi-Net directly learns from continuous and noisy radiance fields using a Siamese network architecture that is designed to extract equivariant field features for category-level canonicalization. During inference, our method takes pre-trained neural radiance fields of novel object instances at arbitrary 3D pose and estimates a canonical field with consistent 3D pose across the entire category. Extensive experiments on a new dataset of 1300 NeRF models across 13 object categories show that our method matches or exceeds the performance of 3D point cloud-based methods.

</details>

### Look, Radiate, and Learn: Self-Supervised Localisation via Radio-Visual Correspondence.
- **链接**: [arXiv:2206.06424](https://arxiv.org/abs/2206.06424) · 📚 被引 3
- **作者**: Mohammed Alloulah, Maximilian Arnold
- **🏷️ 机构**: Nokia Bell Labs
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Next generation cellular networks will implement radio sensing functions alongside customary communications, thereby enabling unprecedented worldwide sensing coverage outdoors. Deep learning has revolutionised computer vision but has had limited application to radio perception tasks, in part due to lack of systematic datasets and benchmarks dedicated to the study of the performance and promise of radio sensing. To address this gap, we present MaxRay: a synthetic radio-visual dataset and benchmark that facilitate precise target localisation in radio. We further propose to learn to localise targets in radio without supervision by extracting self-coordinates from radio-visual correspondence. We use such self-supervised coordinates to train a radio localiser network. We characterise our performance against a number of state-of-the-art baselines. Our results indicate that accurate radio target localisation can be automatically learned from paired radio-visual data without labels, which is important for empirical data. This opens the door for vast data scalability and may prove key to realising the promise of robust radio sensing atop a unified communication-perception cellular infrastructure. Dataset will be hosted on IEEE DataPort.

</details>

### Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture.
- **链接**: [arXiv:2301.08243](https://arxiv.org/abs/2301.08243)
- **作者**: Mahmoud Assran, Quentin Duval, Ishan Misra, Piotr Bojanowski, Pascal Vincent, Michael G. Rabbat et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper demonstrates an approach for learning highly semantic image representations without relying on hand-crafted data-augmentations. We introduce the Image-based Joint-Embedding Predictive Architecture (I-JEPA), a non-generative approach for self-supervised learning from images. The idea behind I-JEPA is simple: from a single context block, predict the representations of various target blocks in the same image. A core design choice to guide I-JEPA towards producing semantic representations is the masking strategy; specifically, it is crucial to (a) sample target blocks with sufficiently large scale (semantic), and to (b) use a sufficiently informative (spatially distributed) context block. Empirically, when combined with Vision Transformers, we find I-JEPA to be highly scalable. For instance, we train a ViT-Huge/14 on ImageNet using 16 A100 GPUs in under 72 hours to achieve strong downstream performance across a wide range of tasks, from linear classification to object counting and depth prediction.

</details>

### Three Guidelines You Should Know for Universally Slimmable Self-Supervised Learning.
- **链接**: [arXiv:2303.06870](https://arxiv.org/abs/2303.06870) · [代码](https://github.com/megvii-research/US3L-CVPR2023) · 📚 被引 6
- **作者**: Yun-Hao Cao, Peiqin Sun, Shuchang Zhou
- **🏷️ 机构**: Nanjing University,State Key Laboratory for Novel Software Technology, MEGVII Technology
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose universally slimmable self-supervised learning (dubbed as US3L) to achieve better accuracy-efficiency trade-offs for deploying self-supervised models across different devices. We observe that direct adaptation of self-supervised learning (SSL) to universally slimmable networks misbehaves as the training process frequently collapses. We then discover that temporal consistent guidance is the key to the success of SSL for universally slimmable networks, and we propose three guidelines for the loss design to ensure this temporal consistency from a unified gradient perspective. Moreover, we propose dynamic sampling and group regularization strategies to simultaneously improve training efficiency and accuracy. Our US3L method has been empirically validated on both convolutional neural networks and vision transformers. With only once training and one copy of weights, our method outperforms various state-of-the-art methods (individually trained or not) on benchmarks including recognition, object detection and instance segmentation. Our code is available at https://github.com/megvii-research/US3L-CVPR2023.

</details>

### Mixed Autoencoder for Self-Supervised Visual Representation Learning.
- **链接**: [arXiv:2303.17152](https://arxiv.org/abs/2303.17152) · 📚 被引 35
- **作者**: Kai Chen, Zhili Liu, Lanqing Hong, Hang Xu, Zhenguo Li, Dit-Yan Yeung
- **🏷️ 机构**: Hong Kong University of Science and Technology, Huawei Noah&#x0027;s Ark Lab
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Masked Autoencoder (MAE) has demonstrated superior performance on various vision tasks via randomly masking image patches and reconstruction. However, effective data augmentation strategies for MAE still remain open questions, different from those in contrastive learning that serve as the most important part. This paper studies the prevailing mixing augmentation for MAE. We first demonstrate that naive mixing will in contrast degenerate model performance due to the increase of mutual information (MI). To address, we propose homologous recognition, an auxiliary pretext task, not only to alleviate the MI increasement by explicitly requiring each patch to recognize homologous patches, but also to perform object-aware self-supervised pre-training for better downstream dense perception performance. With extensive experiments, we demonstrate that our proposed Mixed Autoencoder (MixedAE) achieves the state-of-the-art transfer results among masked image modeling (MIM) augmentations on different downstream tasks with significant efficiency. Specifically, our MixedAE outperforms MAE by +0.3% accuracy, +1.7 mIoU and +0.9 AP on ImageNet-1K, ADE20K and COCO respectively with a standard ViT-Base. Moreover, MixedAE surpasses iBOT, a strong MIM method combined with instance discrimination, while accelerating training by 2x. To our best knowledge, this is the very first work to consider mixing for MIM from the perspective of pretext task design. Code will be made available.

</details>

### TexPose: Neural Texture Learning for Self-Supervised 6D Object Pose Estimation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00469) · 📚 被引 45
- **作者**: Hanzhi Chen, Fabian Manhardt, Nassir Navab, Benjamin Busam
- **🏷️ 机构**: Technical University of Munich, Google Inc.
- **会议**: CVPR 2023

### Beyond Appearance: A Semantic Controllable Self-Supervised Learning Framework for Human-Centric Visual Tasks.
- **链接**: [arXiv:2303.17602](https://arxiv.org/abs/2303.17602) · [代码](https://github.com/tinyvision/SOLIDER) · 📚 被引 144
- **作者**: Weihua Chen, Xianzhe Xu, Jian Jia, Hao Luo, Yaohua Wang, Fan Wang et al.
- **🏷️ 机构**: Alibaba Group
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Human-centric visual tasks have attracted increasing research attention due to their widespread applications. In this paper, we aim to learn a general human representation from massive unlabeled human images which can benefit downstream human-centric tasks to the maximum extent. We call this method SOLIDER, a Semantic cOntrollable seLf-supervIseD lEaRning framework. Unlike the existing self-supervised learning methods, prior knowledge from human images is utilized in SOLIDER to build pseudo semantic labels and import more semantic information into the learned representation. Meanwhile, we note that different downstream tasks always require different ratios of semantic information and appearance information. For example, human parsing requires more semantic information, while person re-identification needs more appearance information for identification purpose. So a single learned representation cannot fit for all requirements. To solve this problem, SOLIDER introduces a conditional network with a semantic controller. After the model is trained, users can send values to the controller to produce representations with different ratios of semantic information, which can fit different needs of downstream tasks. Finally, SOLIDER is verified on six downstream human-centric visual tasks. It outperforms state of the arts and builds new baselines for these tasks. The code is released in https://github.com/tinyvision/SOLIDER.

</details>

### StepFormer: Self-Supervised Step Discovery and Localization in Instructional Videos.
- **链接**: [arXiv:2304.13265](https://arxiv.org/abs/2304.13265) · 📚 被引 22
- **作者**: Nikita Dvornik, Isma Hadji, Ran Zhang, Konstantinos G. Derpanis, Richard P. Wildes, Allan D. Jepson
- **🏷️ 机构**: Samsung AI Centre Toronto
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Instructional videos are an important resource to learn procedural tasks from human demonstrations. However, the instruction steps in such videos are typically short and sparse, with most of the video being irrelevant to the procedure. This motivates the need to temporally localize the instruction steps in such videos, i.e. the task called key-step localization. Traditional methods for key-step localization require video-level human annotations and thus do not scale to large datasets. In this work, we tackle the problem with no human supervision and introduce StepFormer, a self-supervised model that discovers and localizes instruction steps in a video. StepFormer is a transformer decoder that attends to the video with learnable queries, and produces a sequence of slots capturing the key-steps in the video. We train our system on a large dataset of instructional videos, using their automatically-generated subtitles as the only source of supervision. In particular, we supervise our system with a sequence of text narrations using an order-aware loss function that filters out irrelevant phrases. We show that our model outperforms all previous unsupervised and weakly-supervised approaches on step detection and localization by a large margin on three challenging benchmarks. Moreover, our model demonstrates an emergent property to solve zero-shot multi-step localization and outperforms all relevant baselines at this task.

</details>

### Self-supervised Non-uniform Kernel Estimation with Flow-based Motion Prior for Blind Image Deblurring.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01736) · 📚 被引 60
- **作者**: Zhenxuan Fang, Fangfang Wu, Weisheng Dong, Xin Li, Jinjian Wu, Guangming Shi
- **🏷️ 机构**: Xidian University, West Virginia University
- **会议**: CVPR 2023

### MOST: Multiple Object localization with Self-supervised Transformers for object discovery.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01450) · 📚 被引 15
- **作者**: Sai Saketh Rambhatla, Ishan Misra, Rama Chellappa, Abhinav Shrivastava
- **🏷️ 机构**: Meta, Johns Hopkins University, University of Maryland,College Park
- **会议**: ICCV 2023

### Sempart: Self-supervised Multi-resolution Partitioning of Image Semantics.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00073) · 📚 被引 4
- **作者**: Sriram Ravindran, Debraj Basu
- **🏷️ 机构**: Adobe
- **会议**: ICCV 2023

### L-DAWA: Layer-wise Divergence Aware Weight Aggregation in Federated Self-Supervised Visual Representation Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01509) · 📚 被引 23
- **作者**: Yasar Abbas Ur Rehman, Yan Gao, Pedro Porto Buarque de Gusmão, Mina Alibeigi, Jiajun Shen, Nicholas D. Lane
- **🏷️ 机构**: TCL AI Lab,Hong Kong, University of Cambridge,United Kingdom
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present Vid2Avatar, a method to learn human avatars from monocular in-the-wild videos. Reconstructing humans that move naturally from monocular in-the-wild videos is difficult. Solving it requires accurately separating humans from arbitrary backgrounds. Moreover, it requires reconstructing detailed 3D surface from short video sequences, making it even more challenging. Despite these challenges, our method does not require any groundtruth supervision or priors extracted from large datasets of clothed human scans, nor do we rely on any external segmentation modules. Instead, it solves the tasks of scene decomposition and surface reconstruction directly in 3D by modeling both the human and the background in the scene jointly, parameterized via two separate neural fields. Specifically, we define a temporally consistent human representation in canonical space and formulate a global optimization over the background model, the canonical human shape and texture, and per-frame human pose parameters. A coarse-to-fine sampling strategy for volume rendering and novel objectives are introduced for a clean separation of dynamic human and static background, yielding detailed and robust 3D human geometry reconstructions. We evaluate our methods on publicly available datasets and show improvements over prior art.

</details>

### CLIP-S4: Language-Guided Self-Supervised Semantic Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01078)
- **作者**: Wenbin He, Suphanut Jamonnak, Liang Gou, Liu Ren
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### STEPs: Self-Supervised Key Step Extraction and Localization from Unlabeled Procedural Videos.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00952) · 📚 被引 11
- **作者**: Anshul Shah, Benjamin Lundell, Harpreet Sawhney, Rama Chellappa
- **🏷️ 机构**: Johns Hopkins University, Microsoft Mixed Reality
- **会议**: ICCV 2023

### Self-supervised Learning to Bring Dual Reversed Rolling Shutter Images Alive.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01203) · 📚 被引 9
- **作者**: Wei Shang, Dongwei Ren, Chaoyu Feng, Xiaotao Wang, Lei Lei, Wangmeng Zuo
- **🏷️ 机构**: Harbin Institute of Technology,School of Computer Science and Technology
- **会议**: ICCV 2023

### FreeCOS: Self-Supervised Learning from Fractals and Unlabeled Images for Curvilinear Object Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00087) · 📚 被引 18
- **作者**: Tianyi Shi, Xiaohuan Ding, Liang Zhang, Xin Yang
- **🏷️ 机构**: Huazhong University of Science &#x0026; Technology,School of EIC
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, AutoFlow has shown promising results on learning a training set for optical flow, but requires ground truth labels in the target domain to compute its search metric. Observing a strong correlation between the ground truth search metric and self-supervised losses, we introduce self-supervised AutoFlow to handle real-world videos without ground truth labels. Using self-supervised loss as the search metric, our self-supervised AutoFlow performs on par with AutoFlow on Sintel and KITTI where ground truth is available, and performs better on the real-world DAVIS dataset. We further explore using self-supervised AutoFlow in the (semi-)supervised setting and obtain competitive results against the state of the art.

</details>

### Self-Supervised Pre-Training with Masked Shape Prediction for 3D Scene Understanding.
- **链接**: [arXiv:2305.05026](https://arxiv.org/abs/2305.05026) · 📚 被引 14
- **作者**: Li Jiang, Zetong Yang, Shaoshuai Shi, Vladislav Golyanik, Dengxin Dai, Bernt Schiele
- **🏷️ 机构**: Max Planck Institute for Informatics,Saarland Informatics Campus, CUHK
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Masked signal modeling has greatly advanced self-supervised pre-training for language and 2D images. However, it is still not fully explored in 3D scene understanding. Thus, this paper introduces Masked Shape Prediction (MSP), a new framework to conduct masked signal modeling in 3D scenes. MSP uses the essential 3D semantic cue, i.e., geometric shape, as the prediction target for masked points. The context-enhanced shape target consisting of explicit shape context and implicit deep shape feature is proposed to facilitate exploiting contextual cues in shape prediction. Meanwhile, the pre-training architecture in MSP is carefully designed to alleviate the masked shape leakage from point coordinates. Experiments on multiple 3D understanding tasks on both indoor and outdoor datasets demonstrate the effectiveness of MSP in learning good feature representations to consistently boost downstream performance.

</details>

### Self-Supervised Representation Learning for CAD.
- **链接**: [arXiv:2210.10807](https://arxiv.org/abs/2210.10807)
- **作者**: Benjamin T. Jones, Michael Hu, Milin Kodnongbua, Vladimir G. Kim, Adriana Schulz
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The design of man-made objects is dominated by computer aided design (CAD) tools. Assisting design with data-driven machine learning methods is hampered by lack of labeled data in CAD's native format; the parametric boundary representation (B-Rep). Several data sets of mechanical parts in B-Rep format have recently been released for machine learning research. However, large scale databases are largely unlabeled, and labeled datasets are small. Additionally, task specific label sets are rare, and costly to annotate. This work proposes to leverage unlabeled CAD geometry on supervised learning tasks. We learn a novel, hybrid implicit/explicit surface representation for B-Rep geometry, and show that this pre-training significantly improves few-shot learning performance and also achieves state-of-the-art performance on several existing B-Rep benchmarks.

</details>

### Benchmarking Self-Supervised Learning on Diverse Pathology Datasets.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00326) · 📚 被引 174
- **作者**: Mingu Kang, Heon Song, Seonwook Park, Donggeun Yoo, Sérgio Pereira
- **🏷️ 机构**: Lunit Inc.
- **会议**: CVPR 2023

> Recent Self-Supervised Learning (SSL) methods are able to learn feature representations that are invariant to different data augmentations, which can then be transferred to downstream tasks of interest. However, different downstream tasks require different invariances for their best performance, so the optimal choice of augmentations for SSL depends on the target task. In this paper, we aim to learn self-supervised features that generalize well across a variety of downstream tasks (e.g., object classification, detection and instance segmentation) without knowing any task information beforehand. We do so by Masked Augmentation Subspace Training (or MAST) to encode in the single feature space the priors from different data augmentations in a factorized way. Specifically, we disentangle the feature space into separate subspaces, each induced by a learnable mask that selects relevant feature dimensions to model invariance to a specific augmentation. We show the success of MAST in jointly capturing generalizable priors from different augmentations, using both unique and shared features across the subspaces. We further show that MAST benefits from uncertainty modeling to reweight ambiguous samples from strong augmentations that may cause similarity mismatch in each subspace. Experiments demonstrate that MAST consistently improves generalization on various downstream tasks, while being task-agnostic and efficient during SSL. We also provide interesting insights about how different augmentations are related and how uncertainty reflects learning difficulty.

</details>

### Towards the Generalization of Contrastive Self-Supervised Learning.
- **链接**: [arXiv:2111.00743](https://arxiv.org/abs/2111.00743)
- **作者**: Weiran Huang, Mingyang Yi, Xuyang Zhao, Zihao Jiang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Masked Frequency Modeling for Self-Supervised Visual Pre-Training.
- **链接**: [arXiv:2206.07706](https://arxiv.org/abs/2206.07706)
- **作者**: Jiahao Xie, Wei Li, Xiaohang Zhan, Ziwei Liu, Yew-Soon Ong, Chen Change Loy
- **🏷️ 机构**: NTU S-Lab
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present Masked Frequency Modeling (MFM), a unified frequency-domain-based approach for self-supervised pre-training of visual models. Instead of randomly inserting mask tokens to the input embeddings in the spatial domain, in this paper, we shift the perspective to the frequency domain. Specifically, MFM first masks out a portion of frequency components of the input image and then predicts the missing frequencies on the frequency spectrum. Our key insight is that predicting masked components in the frequency domain is more ideal to reveal underlying image patterns rather than predicting masked patches in the spatial domain, due to the heavy spatial redundancy. Our findings suggest that with the right configuration of mask-and-predict strategy, both the structural information within high-frequency components and the low-level statistics among low-frequency counterparts are useful in learning good representations. For the first time, MFM demonstrates that, for both ViT and CNN, a simple non-Siamese framework can learn meaningful representations even using none of the following: (i) extra data, (ii) extra model, (iii) mask token. Experimental results on image classification and semantic segmentation, as well as several robustness benchmarks show the competitive performance and advanced robustness of MFM compared with recent masked image modeling approaches. Furthermore, we also comprehensively investigate the effectiveness of classical image restoration tasks for representation learning from a unified frequency perspective and reveal their intriguing relations with our MFM approach.

</details>

### The hidden uniform cluster prior in self-supervised learning.
- **链接**: [arXiv:2210.07277](https://arxiv.org/abs/2210.07277)
- **作者**: Mido Assran, Randall Balestriero, Quentin Duval, Florian Bordes, Ishan Misra, Piotr Bojanowski et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> A successful paradigm in representation learning is to perform self-supervised pretraining using tasks based on mini-batch statistics (e.g., SimCLR, VICReg, SwAV, MSN). We show that in the formulation of all these methods is an overlooked prior to learn features that enable uniform clustering of the data. While this prior has led to remarkably semantic representations when pretraining on class-balanced data, such as ImageNet, we demonstrate that it can hamper performance when pretraining on class-imbalanced data. By moving away from conventional uniformity priors and instead preferring power-law distributed feature clusters, we show that one can improve the quality of the learned representations on real-world class-imbalanced datasets. To demonstrate this, we develop an extension of the Masked Siamese Networks (MSN) method to support the use of arbitrary features priors.

</details>

### Time to augment self-supervised visual representation learning.
- **链接**: [出版页](https://openreview.net/forum?id=o8xdgmwCP8l)
- **作者**: Arthur Aubret, Markus Roland Ernst, Céline Teulière, Jochen Triesch
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### On the Effectiveness of Out-of-Distribution Data in Self-Supervised Long-Tail Learning.
- **链接**: [arXiv:2306.04934](https://arxiv.org/abs/2306.04934) · [代码](https://github.com/JianhongBai/COLT)
- **作者**: Jianhong Bai, Zuozhu Liu, Hualiang Wang, Jin Hao, Yang Feng, Huanpeng Chu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Though Self-supervised learning (SSL) has been widely studied as a promising technique for representation learning, it doesn't generalize well on long-tailed datasets due to the majority classes dominating the feature space. Recent work shows that the long-tailed learning performance could be boosted by sampling extra in-domain (ID) data for self-supervised training, however, large-scale ID data which can rebalance the minority classes are expensive to collect. In this paper, we propose an alternative but easy-to-use and effective solution, Contrastive with Out-of-distribution (OOD) data for Long-Tail learning (COLT), which can effectively exploit OOD data to dynamically re-balance the feature space. We empirically identify the counter-intuitive usefulness of OOD samples in SSL long-tailed learning and principally design a novel SSL method. Concretely, we first localize the `head' and `tail' samples by assigning a tailness score to each OOD sample based on its neighborhoods in the feature space. Then, we propose an online OOD sampling strategy to dynamically re-balance the feature space. Finally, we enforce the model to be capable of distinguishing ID and OOD samples by a distribution-level supervised contrastive loss. Extensive experiments are conducted on various datasets and several state-of-the-art SSL frameworks to verify the effectiveness of the proposed method. The results show that our method significantly improves the performance of SSL on long-tailed datasets by a large margin, and even outperforms previous work which uses external ID data. Our code is available at https://github.com/JianhongBai/COLT.

</details>

### Rethinking Self-Supervised Visual Representation Learning in Pre-training for 3D Human Pose and Shape Estimation.
- **链接**: [arXiv:2303.05370](https://arxiv.org/abs/2303.05370)
- **作者**: Hongsuk Choi, Hyeongjin Nam, Taeryung Lee, Gyeongsik Moon, Kyoung Mu Lee
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, a few self-supervised representation learning (SSL) methods have outperformed the ImageNet classification pre-training for vision tasks such as object detection. However, its effects on 3D human body pose and shape estimation (3DHPSE) are open to question, whose target is fixed to a unique class, the human, and has an inherent task gap with SSL. We empirically study and analyze the effects of SSL and further compare it with other pre-training alternatives for 3DHPSE. The alternatives are 2D annotation-based pre-training and synthetic data pre-training, which share the motivation of SSL that aims to reduce the labeling cost. They have been widely utilized as a source of weak-supervision or fine-tuning, but have not been remarked as a pre-training source. SSL methods underperform the conventional ImageNet classification pre-training on multiple 3DHPSE benchmarks by 7.7% on average. In contrast, despite a much less amount of pre-training data, the 2D annotation-based pre-training improves accuracy on all benchmarks and shows faster convergence during fine-tuning. Our observations challenge the naive application of the current SSL pre-training to 3DHPSE and relight the value of other data types in the pre-training aspect.

</details>

### NeRF-SOS: Any-View Self-supervised Object Segmentation on Complex Scenes.
- **链接**: [arXiv:2209.08776](https://arxiv.org/abs/2209.08776)
- **作者**: Zhiwen Fan, Peihao Wang, Yifan Jiang, Xinyu Gong, Dejia Xu, Zhangyang Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural volumetric representations have shown the potential that Multi-layer Perceptrons (MLPs) can be optimized with multi-view calibrated images to represent scene geometry and appearance, without explicit 3D supervision. Object segmentation can enrich many downstream applications based on the learned radiance field. However, introducing hand-crafted segmentation to define regions of interest in a complex real-world scene is non-trivial and expensive as it acquires per view annotation. This paper carries out the exploration of self-supervised learning for object segmentation using NeRF for complex real-world scenes. Our framework, called NeRF with Self-supervised Object Segmentation NeRF-SOS, couples object segmentation and neural radiance field to segment objects in any view within a scene. By proposing a novel collaborative contrastive loss in both appearance and geometry levels, NeRF-SOS encourages NeRF models to distill compact geometry-aware segmentation clusters from their density fields and the self-supervised pre-trained 2D visual features. The self-supervised object segmentation framework can be applied to various NeRF models that both lead to photo-realistic rendering results and convincing segmentation maps for both indoor and outdoor scenarios. Extensive results on the LLFF, Tank & Temple, and BlendedMVS datasets validate the effectiveness of NeRF-SOS. It consistently surpasses other 2D-based self-supervised baselines and predicts finer semantics masks than existing supervised counterparts. Please refer to the video on our project page for more details:https://zhiwenfan.github.io/NeRF-SOS.

</details>

### Corrupted Image Modeling for Self-Supervised Visual Pre-Training.
- **链接**: [arXiv:2202.03382](https://arxiv.org/abs/2202.03382)
- **作者**: Yuxin Fang, Li Dong, Hangbo Bao, Xinggang Wang, Furu Wei
- **🏷️ 机构**: Nanyang Technological University,S-Lab
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce Corrupted Image Modeling (CIM) for self-supervised visual pre-training. CIM uses an auxiliary generator with a small trainable BEiT to corrupt the input image instead of using artificial [MASK] tokens, where some patches are randomly selected and replaced with plausible alternatives sampled from the BEiT output distribution. Given this corrupted image, an enhancer network learns to either recover all the original image pixels, or predict whether each visual token is replaced by a generator sample or not. The generator and the enhancer are simultaneously trained and synergistically updated. After pre-training, the enhancer can be used as a high-capacity visual encoder for downstream tasks. CIM is a general and flexible visual pre-training framework that is suitable for various network architectures. For the first time, CIM demonstrates that both ViT and CNN can learn rich visual representations using a unified, non-Siamese framework. Experimental results show that our approach achieves compelling results in vision benchmarks, such as ImageNet classification and ADE20K semantic segmentation.

</details>

### On the duality between contrastive and non-contrastive self-supervised learning.
- **链接**: [arXiv:2206.02574](https://arxiv.org/abs/2206.02574)
- **作者**: Quentin Garrido, Yubei Chen, Adrien Bardes, Laurent Najman, Yann LeCun
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Spatially Adaptive Self-Supervised Learning for Real-World Image Denoising.
- **链接**: [arXiv:2303.14934](https://arxiv.org/abs/2303.14934) · [代码](https://github.com/nagejacob/SpatiallyAdaptiveSSID) · 📚 被引 58
- **作者**: Junyi Li, Zhilu Zhang, Xiaoyu Liu, Chaoyu Feng, Xiaotao Wang, Lei Lei et al.
- **🏷️ 机构**: School of Computer Science and Technology, Harbin Institute of Technology,China
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Significant progress has been made in self-supervised image denoising (SSID) in the recent few years. However, most methods focus on dealing with spatially independent noise, and they have little practicality on real-world sRGB images with spatially correlated noise. Although pixel-shuffle downsampling has been suggested for breaking the noise correlation, it breaks the original information of images, which limits the denoising performance. In this paper, we propose a novel perspective to solve this problem, i.e., seeking for spatially adaptive supervision for real-world sRGB image denoising. Specifically, we take into account the respective characteristics of flat and textured regions in noisy images, and construct supervisions for them separately. For flat areas, the supervision can be safely derived from non-adjacent pixels, which are much far from the current pixel for excluding the influence of the noise-correlated ones. And we extend the blind-spot network to a blind-neighborhood network (BNN) for providing supervision on flat areas. For textured regions, the supervision has to be closely related to the content of adjacent pixels. And we present a locally aware network (LAN) to meet the requirement, while LAN itself is selectively supervised with the output of BNN. Combining these two supervisions, a denoising network (e.g., U-Net) can be well-trained. Extensive experiments show that our method performs favorably against state-of-the-art SSID methods on real-world sRGB photographs. The code is available at https://github.com/nagejacob/SpatiallyAdaptiveSSID.

</details>

### Pose-disentangled Contrastive Learning for Self-supervised Facial Representation.
- **链接**: [arXiv:2211.13490](https://arxiv.org/abs/2211.13490) · [代码](https://github.com/DreamMr/PCL) · 📚 被引 29
- **作者**: Yuanyuan Liu, Wenbin Wang, Yibing Zhan, Shaoze Feng, Kejun Liu, Zhe Chen
- **🏷️ 机构**: School of Computer Science, China University of Geosciences,Wuhan,China, JD Explore Academy,China, The University of Sydney,Australia
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised facial representation has recently attracted increasing attention due to its ability to perform face understanding without relying on large-scale annotated datasets heavily. However, analytically, current contrastive-based self-supervised learning (SSL) still performs unsatisfactorily for learning facial representation. More specifically, existing contrastive learning (CL) tends to learn pose-invariant features that cannot depict the pose details of faces, compromising the learning performance. To conquer the above limitation of CL, we propose a novel Pose-disentangled Contrastive Learning (PCL) method for general self-supervised facial representation. Our PCL first devises a pose-disentangled decoder (PDD) with a delicately designed orthogonalizing regulation, which disentangles the pose-related features from the face-aware features; therefore, pose-related and other pose-unrelated facial information could be performed in individual subnetworks and do not affect each other's training. Furthermore, we introduce a pose-related contrastive learning scheme that learns pose-related information based on data augmentation of the same image, which would deliver more effective face-aware representation for various downstream tasks. We conducted linear evaluation on four challenging downstream facial understanding tasks, ie, facial expression recognition, face recognition, AU detection and head pose estimation. Experimental results demonstrate that our method significantly outperforms state-of-the-art SSL methods. Code is available at https://github.com/DreamMr/PCL}{https://github.com/DreamMr/PCL

</details>

### Multiple Instance Learning via Iterative Self-Paced Supervised Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00327) · 📚 被引 35
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
- **链接**: [arXiv:2301.05709](https://arxiv.org/abs/2301.05709) · 📚 被引 29
- **作者**: Anas Mahmoud, Jordan S. K. Hu, Tianshu Kuai, Ali Harakeh, Liam Paull, Steven L. Waslander
- **🏷️ 机构**: University of Toronto Robotics Institute, Mila, Universit&#x00E9; de Montr&#x00E9;al
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> An effective framework for learning 3D representations for perception tasks is distilling rich self-supervised image features via contrastive learning. However, image-to point representation learning for autonomous driving datasets faces two main challenges: 1) the abundance of self-similarity, which results in the contrastive losses pushing away semantically similar point and image regions and thus disturbing the local semantic structure of the learned representations, and 2) severe class imbalance as pretraining gets dominated by over-represented classes. We propose to alleviate the self-similarity problem through a novel semantically tolerant image-to-point contrastive loss that takes into consideration the semantic distance between positive and negative image regions to minimize contrasting semantically similar point and image regions. Additionally, we address class imbalance by designing a class-agnostic balanced loss that approximates the degree of class imbalance through an aggregate sample-to-samples semantic similarity measure. We demonstrate that our semantically-tolerant contrastive loss with class balancing improves state-of-the art 2D-to-3D representation learning in all evaluation settings on 3D semantic segmentation. Our method consistently outperforms state-of-the-art 2D-to-3D representation learning frameworks across a wide range of 2D self-supervised pretrained models.

</details>

### HaLP: Hallucinating Latent Positives for Skeleton-based Self-Supervised Learning of Actions.
- **链接**: [arXiv:2304.00387](https://arxiv.org/abs/2304.00387) · [代码](https://github.com/anshulbshah/HaLP) · 📚 被引 41
- **作者**: Anshul Shah, Aniket Roy, Ketul Shah, Shlok Mishra, David Jacobs, Anoop Cherian et al.
- **🏷️ 机构**: Johns Hopkins University, University of Maryland,College Park, MERL
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Supervised learning of skeleton sequence encoders for action recognition has received significant attention in recent times. However, learning such encoders without labels continues to be a challenging problem. While prior works have shown promising results by applying contrastive learning to pose sequences, the quality of the learned representations is often observed to be closely tied to data augmentations that are used to craft the positives. However, augmenting pose sequences is a difficult task as the geometric constraints among the skeleton joints need to be enforced to make the augmentations realistic for that action. In this work, we propose a new contrastive learning approach to train models for skeleton-based action recognition without labels. Our key contribution is a simple module, HaLP - to Hallucinate Latent Positives for contrastive learning. Specifically, HaLP explores the latent space of poses in suitable directions to generate new positives. To this end, we present a novel optimization formulation to solve for the synthetic positives with an explicit control on their hardness. We propose approximations to the objective, making them solvable in closed form with minimal overhead. We show via experiments that using these generated positives within a standard contrastive learning framework leads to consistent improvements across benchmarks such as NTU-60, NTU-120, and PKU-II on tasks like linear evaluation, transfer learning, and kNN evaluation. Our code will be made available at https://github.com/anshulbshah/HaLP.

</details>

### Self-Supervised 3D Scene Flow Estimation Guided by Superpoints.
- **链接**: [arXiv:2305.02528](https://arxiv.org/abs/2305.02528) · 📚 被引 33
- **作者**: Yaqi Shen, Le Hui, Jin Xie, Jian Yang
- **🏷️ 机构**: Nanjing University of Science and Technology,PCA Lab,Nanjing,China
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D scene flow estimation aims to estimate point-wise motions between two consecutive frames of point clouds. Superpoints, i.e., points with similar geometric features, are usually employed to capture similar motions of local regions in 3D scenes for scene flow estimation. However, in existing methods, superpoints are generated with the offline clustering methods, which cannot characterize local regions with similar motions for complex 3D scenes well, leading to inaccurate scene flow estimation. To this end, we propose an iterative end-to-end superpoint based scene flow estimation framework, where the superpoints can be dynamically updated to guide the point-level flow prediction. Specifically, our framework consists of a flow guided superpoint generation module and a superpoint guided flow refinement module. In our superpoint generation module, we utilize the bidirectional flow information at the previous iteration to obtain the matching points of points and superpoint centers for soft point-to-superpoint association construction, in which the superpoints are generated for pairwise point clouds. With the generated superpoints, we first reconstruct the flow for each point by adaptively aggregating the superpoint-level flow, and then encode the consistency between the reconstructed flow of pairwise point clouds. Finally, we feed the consistency encoding along with the reconstructed flow into GRU to refine point-level flow. Extensive experiments on several different datasets show that our method can achieve promising performance.

</details>

### Learning Common Rationale to Improve Self-Supervised Representation for Fine-Grained Visual Recognition Problems.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01096) · 📚 被引 25
- **作者**: Yangyang Shu, Anton van den Hengel, Lingqiao Liu
- **🏷️ 机构**: School of Computer Science, The University of Adelaide
- **会议**: CVPR 2023

### Multi-Mode Online Knowledge Distillation for Self-Supervised Visual Representation Learning.
- **链接**: [arXiv:2304.06461](https://arxiv.org/abs/2304.06461) · 📚 被引 38
- **作者**: Kaiyou Song, Jin Xie, Shan Zhang, Zimeng Luo
- **🏷️ 机构**: Megvii Technology
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning (SSL) has made remarkable progress in visual representation learning. Some studies combine SSL with knowledge distillation (SSL-KD) to boost the representation learning performance of small models. In this study, we propose a Multi-mode Online Knowledge Distillation method (MOKD) to boost self-supervised visual representation learning. Different from existing SSL-KD methods that transfer knowledge from a static pre-trained teacher to a student, in MOKD, two different models learn collaboratively in a self-supervised manner. Specifically, MOKD consists of two distillation modes: self-distillation and cross-distillation modes. Among them, self-distillation performs self-supervised learning for each model independently, while cross-distillation realizes knowledge interaction between different models. In cross-distillation, a cross-attention feature search strategy is proposed to enhance the semantic feature alignment between different models. As a result, the two models can absorb knowledge from each other to boost their representation learning performance. Extensive experimental results on different backbones and datasets demonstrate that two heterogeneous models can benefit from MOKD and outperform their independently trained baseline. In addition, MOKD also outperforms existing SSL-KD methods for both the student and teacher models.

</details>

### Masked Motion Encoding for Self-Supervised Video Representation Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00222)
- **作者**: Xinyu Sun, Peihao Chen, Liangwei Chen, Changhao Li, Thomas H. Li, Mingkui Tan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### Scene Graph Contrastive Learning for Embodied Navigation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00999) · 📚 被引 21
- **作者**: Kunal Pratap Singh, Jordi Salvador, Luca Weihs, Aniruddha Kembhavi
- **🏷️ 机构**: Allen Institute for AI
- **会议**: ICCV 2023

### Siamese Image Modeling for Self-Supervised Vision Representation Learning.
- **链接**: [arXiv:2206.01204](https://arxiv.org/abs/2206.01204) · [代码](https://github.com/fundamentalvision/Siamese-Image-Modeling) · 📚 被引 78
- **作者**: Chenxin Tao, Xizhou Zhu, Weijie Su, Gao Huang, Bin Li, Jie Zhou et al.
- **🏷️ 机构**: Tsinghua University, SenseTime Research, University of Science and Technology of China
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning (SSL) has delivered superior performance on a variety of downstream vision tasks. Two main-stream SSL frameworks have been proposed, i.e., Instance Discrimination (ID) and Masked Image Modeling (MIM). ID pulls together representations from different views of the same image, while avoiding feature collapse. It lacks spatial sensitivity, which requires modeling the local structure within each image. On the other hand, MIM reconstructs the original content given a masked image. It instead does not have good semantic alignment, which requires projecting semantically similar views into nearby representations. To address this dilemma, we observe that (1) semantic alignment can be achieved by matching different image views with strong augmentations; (2) spatial sensitivity can benefit from predicting dense representations with masked images. Driven by these analysis, we propose Siamese Image Modeling (SiameseIM), which predicts the dense representations of an augmented view, based on another masked view from the same image but with different augmentations. SiameseIM uses a Siamese network with two branches. The online branch encodes the first view, and predicts the second view's representation according to the relative positions between these two views. The target branch produces the target by encoding the second view. SiameseIM can surpass both ID and MIM on a wide range of downstream tasks, including ImageNet finetuning and linear probing, COCO and LVIS detection, and ADE20k semantic segmentation. The improvement is more significant in few-shot, long-tail and robustness-concerned scenarios. Code shall be released at https://github.com/fundamentalvision/Siamese-Image-Modeling.

</details>

### Defending Against Patch-based Backdoor Attacks on Self-Supervised Learning.
- **链接**: [arXiv:2304.01482](https://arxiv.org/abs/2304.01482) · [代码](https://github.com/UCDvision/PatchSearch) · 📚 被引 23
- **作者**: Ajinkya Tejankar, Maziar Sanjabi, Qifan Wang, Sinong Wang, Hamed Firooz, Hamed Pirsiavash et al.
- **🏷️ 机构**: University of California,Davis, Meta AI
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, self-supervised learning (SSL) was shown to be vulnerable to patch-based data poisoning backdoor attacks. It was shown that an adversary can poison a small part of the unlabeled data so that when a victim trains an SSL model on it, the final model will have a backdoor that the adversary can exploit. This work aims to defend self-supervised learning against such attacks. We use a three-step defense pipeline, where we first train a model on the poisoned data. In the second step, our proposed defense algorithm (PatchSearch) uses the trained model to search the training data for poisoned samples and removes them from the training set. In the third step, a final model is trained on the cleaned-up training set. Our results show that PatchSearch is an effective defense. As an example, it improves a model's accuracy on images containing the trigger from 38.2% to 63.7% which is very close to the clean model's accuracy, 64.6%. Moreover, we show that PatchSearch outperforms baselines and state-of-the-art defense approaches including those using additional clean, trusted data. Our code is available at https://github.com/UCDvision/PatchSearch

</details>

### Learning with Noisy labels via Self-supervised Adversarial Noisy Masking.
- **链接**: [arXiv:2302.06805](https://arxiv.org/abs/2302.06805) · 📚 被引 27
- **作者**: Yuanpeng Tu, Boshen Zhang, Yuxi Li, Liang Liu, Jian Li, Jiangning Zhang et al.
- **🏷️ 机构**: Tongji Univeristy,Dept. of Electronic and Information Engineering,Shanghai, Tencent,YouTu Lab,Shanghai
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Collecting large-scale datasets is crucial for training deep models, annotating the data, however, inevitably yields noisy labels, which poses challenges to deep learning algorithms. Previous efforts tend to mitigate this problem via identifying and removing noisy samples or correcting their labels according to the statistical properties (e.g., loss values) among training samples. In this paper, we aim to tackle this problem from a new perspective, delving into the deep feature maps, we empirically find that models trained with clean and mislabeled samples manifest distinguishable activation feature distributions. From this observation, a novel robust training approach termed adversarial noisy masking is proposed. The idea is to regularize deep features with a label quality guided masking scheme, which adaptively modulates the input data and label simultaneously, preventing the model to overfit noisy samples. Further, an auxiliary task is designed to reconstruct input data, it naturally provides noise-free self-supervised signals to reinforce the generalization ability of deep models. The proposed method is simple and flexible, it is tested on both synthetic and real-world noisy datasets, where significant improvements are achieved over previous state-of-the-art methods.

</details>

### PatchCraft Self-Supervised Training for Correlated Image Denoising.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00561) · 📚 被引 13
- **作者**: Gregory Vaksman, Michael Elad
- **🏷️ 机构**: CS Department - The Technion,Haifa,Israel
- **会议**: CVPR 2023

### Boosting Novel Category Discovery Over Domains with Soft Contrastive Learning and All in One Classifier.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01089) · 📚 被引 18
- **作者**: Zelin Zang, Lei Shang, Senqiao Yang, Fei Wang, Baigui Sun, Xuansong Xie et al.
- **🏷️ 机构**: Westlake University, Alibaba Group
- **会议**: ICCV 2023

### Weakly-Supervised Text-driven Contrastive Learning for Facial Behavior Understanding.
- **链接**: [arXiv:2304.00058](https://arxiv.org/abs/2304.00058) · 📚 被引 23
- **作者**: Xiang Zhang, Taoyue Wang, Xiaotian Li, Huiyuan Yang, Lijun Yin
- **🏷️ 机构**: State University of New York,Binghamton, Rice University
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Contrastive learning has shown promising potential for learning robust representations by utilizing unlabeled data. However, constructing effective positive-negative pairs for contrastive learning on facial behavior datasets remains challenging. This is because such pairs inevitably encode the subject-ID information, and the randomly constructed pairs may push similar facial images away due to the limited number of subjects in facial behavior datasets. To address this issue, we propose to utilize activity descriptions, coarse-grained information provided in some datasets, which can provide high-level semantic information about the image sequences but is often neglected in previous studies. More specifically, we introduce a two-stage Contrastive Learning with Text-Embeded framework for Facial behavior understanding (CLEF). The first stage is a weakly-supervised contrastive learning method that learns representations from positive-negative pairs constructed using coarse-grained activity information. The second stage aims to train the recognition of facial expressions or facial action units by maximizing the similarity between image and the corresponding text label names. The proposed CLEF achieves state-of-the-art performance on three in-the-lab datasets for AU recognition and three in-the-wild datasets for facial expression recognition.

</details>

### Pre-training-free Image Manipulation Localization through Non-Mutually Exclusive Contrastive Learning.
- **链接**: [arXiv:2309.14900](https://arxiv.org/abs/2309.14900) · [代码](https://github.com/Knightzjz/NCL-IML) · 📚 被引 49
- **作者**: Jizhe Zhou, Xiaochen Ma, Xia Du, Ahmed Y. Al Hammadi, Wentao Feng
- **🏷️ 机构**: Sichuan University,College of Computer Science, Xiamen University of Technology,School of Computer and Information Engineering, Mohamed Bin Zayed University for Humanities,Strategy Affairs Office
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep Image Manipulation Localization (IML) models suffer from training data insufficiency and thus heavily rely on pre-training. We argue that contrastive learning is more suitable to tackle the data insufficiency problem for IML. Crafting mutually exclusive positives and negatives is the prerequisite for contrastive learning. However, when adopting contrastive learning in IML, we encounter three categories of image patches: tampered, authentic, and contour patches. Tampered and authentic patches are naturally mutually exclusive, but contour patches containing both tampered and authentic pixels are non-mutually exclusive to them. Simply abnegating these contour patches results in a drastic performance loss since contour patches are decisive to the learning outcomes. Hence, we propose the Non-mutually exclusive Contrastive Learning (NCL) framework to rescue conventional contrastive learning from the above dilemma. In NCL, to cope with the non-mutually exclusivity, we first establish a pivot structure with dual branches to constantly switch the role of contour patches between positives and negatives while training. Then, we devise a pivot-consistent loss to avoid spatial corruption caused by the role-switching process. In this manner, NCL both inherits the self-supervised merits to address the data insufficiency and retains a high manipulation localization accuracy. Extensive experiments verify that our NCL achieves state-of-the-art performance on all five benchmarks without any pre-training and is more robust on unseen real-life samples. The code is available at: https://github.com/Knightzjz/NCL-IML.

</details>

### Geometric Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00028)
- **作者**: Yeskendir Koishekenov, Sharvaree P. Vadgama, Riccardo Valperga, Erik J. Bekkers
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### LG-BPN: Local and Global Blind-Patch Network for Self-Supervised Real-World Denoising.
- **链接**: [arXiv:2304.00534](https://arxiv.org/abs/2304.00534) · [代码](https://github.com/Wang-XIaoDingdd/LGBPN) · 📚 被引 74
- **作者**: Zichun Wang, Ying Fu, Ji Liu, Yulun Zhang
- **🏷️ 机构**: Beijing Institute of Technology, Baidu Inc.,Beijing,China, ETH Z&#x00FC;rich
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite the significant results on synthetic noise under simplified assumptions, most self-supervised denoising methods fail under real noise due to the strong spatial noise correlation, including the advanced self-supervised blind-spot networks (BSNs). For recent methods targeting real-world denoising, they either suffer from ignoring this spatial correlation, or are limited by the destruction of fine textures for under-considering the correlation. In this paper, we present a novel method called LG-BPN for self-supervised real-world denoising, which takes the spatial correlation statistic into our network design for local detail restoration, and also brings the long-range dependencies modeling ability to previously CNN-based BSN methods. First, based on the correlation statistic, we propose a densely-sampled patch-masked convolution module. By taking more neighbor pixels with low noise correlation into account, we enable a denser local receptive field, preserving more useful information for enhanced fine structure recovery. Second, we propose a dilated Transformer block to allow distant context exploitation in BSN. This global perception addresses the intrinsic deficiency of BSN, whose receptive field is constrained by the blind spot requirement, which can not be fully resolved by the previous CNN-based BSNs. These two designs enable LG-BPN to fully exploit both the detailed structure and the global interaction in a blind manner. Extensive results on real-world datasets demonstrate the superior performance of our method. https://github.com/Wang-XIaoDingdd/LGBPN

</details>

### DLBD: A Self-Supervised Direct-Learned Binary Descriptor.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01521) · 📚 被引 7
- **作者**: Bin Xiao, Yang Hu, Bo Liu, Xiuli Bi, Weisheng Li, Xinbo Gao
- **🏷️ 机构**: Chongqing University of Posts and Telecommunications,Chongqing,China
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We develop techniques for refining representations for fine-grained classification and segmentation tasks in a self-supervised manner. We find that fine-tuning methods based on instance-discriminative contrastive learning are not as effective, and posit that recognizing part-specific variations is crucial for fine-grained categorization. We present an iterative learning approach that incorporates part-centric equivariance and invariance objectives. First, pixel representations are clustered to discover parts. We analyze the representations from convolutional and vision transformer networks that are best suited for this task. Then, a part-centric learning step aggregates and contrasts representations of parts within an image. We show that this improves the performance on image classification and part segmentation tasks across datasets. For example, under a linear-evaluation scheme, the classification accuracy of a ResNet50 trained on ImageNet using DetCon, a self-supervised learning approach, improves from 35.4% to 42.0% on the Caltech-UCSD Birds, from 35.5% to 44.1% on the FGVC Aircraft, and from 29.7% to 37.4% on the Stanford Cars. We also observe significant gains in few-shot part segmentation tasks using the proposed technique, while instance-discriminative learning was not as effective. Smaller, yet consistent, improvements are also observed for stronger networks based on transformers.

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
- **会议**: NeurIPS 2023

### Reverse Engineering Self-Supervised Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/b63ad8c24354b0e5bcb7aea16490beab-Abstract-Conference.html)
- **作者**: Ido Ben-Shaul, Ravid Shwartz-Ziv, Tomer Galanti, Shai Dekel, Yann LeCun
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Bridging the Domain Gap: Self-Supervised 3D Scene Understanding with Foundation Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/fa5b423e24b442180bcd4e13ae75a27f-Abstract-Conference.html) · 📚 被引 6
- **作者**: Zhimin Chen, Longlong Jing, Yingwei Li, Bing Li
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

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

> Although supervised image denoising networks have shown remarkable performance on synthesized noisy images, they often fail in practice due to the difference between real and synthesized noise. Since clean-noisy image pairs from the real world are extremely costly to gather, self-supervised learning, which utilizes noisy input itself as a target, has been studied. To prevent a self-supervised denoising model from learning identical mapping, each output pixel should not be influenced by its corresponding input pixel; This requirement is known as J-invariance. Blind-spot networks (BSNs) have been a prevalent choice to ensure J-invariance in self-supervised image denoising. However, constructing variations of BSNs by injecting additional operations such as downsampling can expose blinded information, thereby violating J-invariance. Consequently, convolutions designed specifically for BSNs have been allowed only, limiting architectural flexibility. To overcome this limitation, we propose PUCA, a novel J-invariant U-Net architecture, for self-supervised denoising. PUCA leverages patch-unshuffle/shuffle to dramatically expand receptive fields while maintaining J-invariance and dilated attention blocks (DABs) for global context incorporation. Experimental results demonstrate that PUCA achieves state-of-the-art performance, outperforming existing methods in self-supervised image denoising.

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Contrastive language-image pre-training (CLIP) serves as a de-facto standard to align images and texts. Nonetheless, the loose correlation between images and texts of web-crawled data renders the contrastive objective data inefficient and craving for a large training batch size. In this work, we explore the validity of non-contrastive language-image pre-training (nCLIP), and study whether nice properties exhibited in visual self-supervised models can emerge. We empirically observe that the non-contrastive objective nourishes representation learning while sufficiently underperforming under zero-shot recognition. Based on the above study, we further introduce xCLIP, a multi-tasking framework combining CLIP and nCLIP, and show that nCLIP aids CLIP in enhancing feature semantics. The synergy between two objectives lets xCLIP enjoy the best of both worlds: superior performance in both zero-shot transfer and representation learning. Systematic evaluation is conducted spanning a wide variety of downstream tasks including zero-shot classification, out-of-domain classification, retrieval, visual representation learning, and textual representation learning, showcasing a consistent performance gain and validating the effectiveness of xCLIP.

</details>

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite its practical importance across a wide range of modalities, recent advances in self-supervised learning (SSL) have been primarily focused on a few well-curated domains, e.g., vision and language, often relying on their domain-specific knowledge. For example, Masked Auto-Encoder (MAE) has become one of the popular architectures in these domains, but less has explored its potential in other modalities. In this paper, we develop MAE as a unified, modality-agnostic SSL framework. In turn, we argue meta-learning as a key to interpreting MAE as a modality-agnostic learner, and propose enhancements to MAE from the motivation to jointly improve its SSL across diverse modalities, coined MetaMAE as a result. Our key idea is to view the mask reconstruction of MAE as a meta-learning task: masked tokens are predicted by adapting the Transformer meta-learner through the amortization of unmasked tokens. Based on this novel interpretation, we propose to integrate two advanced meta-learning techniques. First, we adapt the amortized latent of the Transformer encoder using gradient-based meta-learning to enhance the reconstruction. Then, we maximize the alignment between amortized and adapted latents through task contrastive learning which guides the Transformer encoder to better encode the task-specific knowledge. Our experiment demonstrates the superiority of MetaMAE in the modality-agnostic SSL benchmark (called DABS), significantly outperforming prior baselines. Code is available at https://github.com/alinlab/MetaMAE.

</details>

### Effective Targeted Attacks for Adversarial Self-Supervised Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/b28ae1166e1035c26b89d20f0286c9eb-Abstract-Conference.html) · 📚 被引 0
- **作者**: Minseon Kim, Hyeonjeong Ha, Sooel Son, Sung Ju Hwang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Analyzing the Sample Complexity of Self-Supervised Image Reconstruction Methods.
- **链接**: [arXiv:2305.19079](https://arxiv.org/abs/2305.19079) · 📚 被引 1
- **作者**: Tobit Klug, Dogukan Atik, Reinhard Heckel
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Supervised training of deep neural networks on pairs of clean image and noisy measurement achieves state-of-the-art performance for many image reconstruction tasks, but such training pairs are difficult to collect. Self-supervised methods enable training based on noisy measurements only, without clean images. In this work, we investigate the cost of self-supervised training in terms of sample complexity for a class of self-supervised methods that enable the computation of unbiased estimates of gradients of the supervised loss, including noise2noise methods. We analytically show that a model trained with such self-supervised training is as good as the same model trained in a supervised fashion, but self-supervised training requires more examples than supervised training. We then study self-supervised denoising and accelerated MRI empirically and characterize the cost of self-supervised training in terms of the number of additional samples required, and find that the performance gap between self-supervised and supervised training vanishes as a function of the training examples, at a problem-dependent rate, as predicted by our theory.

</details>

### Improving Self-supervised Molecular Representation Learning using Persistent Homology.
- **链接**: [arXiv:2311.17327](https://arxiv.org/abs/2311.17327) · 📚 被引 2
- **作者**: Yuankai Luo, Lei Shi, Veronika Thost
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

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

- Self-Supervised Object Detection from Egocentric Videos. → [object-detection](../object-detection/Guideline%202023.md)
- Unleashing Vanilla Vision Transformer with Masked Image Modeling for Object Detection. → [object-detection](../object-detection/Guideline%202023.md)
- CleanCLIP: Mitigating Data Poisoning Attacks in Multimodal Contrastive Learning. → [multimodal](../multimodal/Guideline%202023.md)
- Multimodal Contrastive Learning and Tabular Attention for Automated Alzheimer's Disease Prediction. → [multimodal](../multimodal/Guideline%202023.md)
- SceneRF: Self-Supervised Monocular 3D Scene Reconstruction with Radiance Fields. → [3d-detection](../3d-detection/Guideline%202023.md)
- Multi-view Self-supervised Disentanglement for General Image Denoising. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- DeLiRa: Self-Supervised Depth, Light, and Radiance Fields. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- Self-Supervised Monocular Depth Estimation by Direction-aware Cumulative Convolution Network. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- Self-supervised Monocular Depth Estimation: Let's Talk About The Weather. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- 3D Distillation: Improving Self-Supervised Monocular Depth Estimation on Reflective Surfaces. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- GasMono: Geometry-Aided Self-Supervised Monocular Depth Estimation for Indoor Scenes. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- HaMuCo: Hand Pose Estimation via Multiview Collaborative Self-Supervised Learning. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- Two-in-One Depth: Bridging the Gap Between Monocular and Binocular Self-supervised Depth Estimation. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- Margin Contrastive Learning with Learnable-Vector for Continual Learning. → [continual-learning](../continual-learning/Guideline%202023.md)
- CL-MVSNet: Unsupervised Multi-view Stereo with Dual-level Contrastive Learning. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- GeoMIM: Towards Better 3D Knowledge Transfer via Masked Image Modeling for Multi-view 3D Understanding. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
