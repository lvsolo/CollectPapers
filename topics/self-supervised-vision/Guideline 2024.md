# Self-supervised Vision — 2024 Guideline

> 领域: 视觉自监督学习（对比学习、MAE、DINO 系）
> 论文数: 64 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份:

### T-MAE : Temporal Masked Autoencoders for Point Cloud Representation Learning. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73247-8_11) · 📚 被引 6
- **作者**: Weijie Wei, Fatemeh Karimi Nejadasl, Theo Gevers, Martin R. Oswald
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024
- **摘要（中）**: 针对点云表示学习中时间信息利用不足的问题，该论文提出T-MAE，一种时间掩码自编码器。方法在预训练时同时掩蔽空间和时间维度的点云块，迫使模型学习时空一致性特征。相比仅空间MAE，T-MAE能捕捉动态场景中的时序依赖。实验表明在多个点云下游任务（如分类、分割）上显著提升性能。
- **摘要（英）**: This paper addresses insufficient temporal information in point cloud representation learning by proposing T-MAE, a temporal masked autoencoder that masks both spatial and temporal patches during pretraining. It learns spatiotemporal consistency, outperforming spatial-only MAE on downstream tasks like classification and segmentation.
- **核心贡献**: 提出时间掩码自编码器用于点云表示学习。
- **创新点**: 联合掩蔽空间与时间维度。
- **结果**: 在点云下游任务上显著提升性能。

### DINO-Tracker: Taming DINO for Self-supervised Point Tracking in a Single Video. **⭐⭐⭐⭐** (相关度: 65%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73347-5_21) · 📚 被引 34
- **作者**: Narek Tumanyan, Assaf Singer, Shai Bagon, Tali Dekel
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024
- **摘要（中）**: 针对单视频中无监督点跟踪的挑战，该论文提出DINO-Tracker，利用DINO预训练特征进行自监督点跟踪。方法通过特征匹配和时序一致性约束，无需标注即可跟踪任意点。相比传统光流或监督方法，DINO-Tracker在遮挡和复杂运动下更鲁棒。实验表明在多个视频跟踪基准上达到最先进性能。
- **摘要（英）**: This paper addresses unsupervised point tracking in a single video by proposing DINO-Tracker, which leverages DINO pretrained features for self-supervised tracking. It uses feature matching and temporal consistency without annotations, showing robustness to occlusion and complex motion, achieving state-of-the-art on tracking benchmarks.
- **核心贡献**: 提出基于DINO的自监督点跟踪方法。
- **创新点**: 利用预训练视觉特征实现无监督跟踪。
- **结果**: 在多个跟踪基准上达到最先进性能。

### Towards Open-World Object-Based Anomaly Detection via Self-Supervised Outlier Synthesis.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73209-6_12) · 📚 被引 6
- **作者**: Brian K. S. Isaac-Medina, Yona Falinie A. Gaus, Neelanjan Bhowmik, Toby P. Breckon
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Face swapping has gained significant attention for its varied applications. Most previous face swapping approaches have relied on the seesaw game training scheme, also known as the target-oriented approach. However, this often leads to instability in model training and results in undesired samples with blended identities due to the target identity leakage problem. Source-oriented methods achieve more stable training with self-reconstruction objective but often fail to accurately reflect target image's skin color and illumination. This paper introduces the Shape Agnostic Masked AutoEncoder (SAMAE) training scheme, a novel self-supervised approach that combines the strengths of both target-oriented and source-oriented approaches. Our training scheme addresses the limitations of traditional training methods by circumventing the conventional seesaw game and introducing clear ground truth through its self-reconstruction training regime. Our model effectively mitigates identity leakage and reflects target albedo and illumination through learned disentangled identity and non-identity features. Additionally, we closely tackle the shape misalignment and volume discrepancy problems with new techniques, including perforation confusion and random mesh scaling. SAMAE establishes a new state-of-the-art, surpassing other baseline methods, preserving both identity and non-identity attributes without sacrificing on either aspect.

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Availability poisons exploit supervised learning (SL) algorithms by introducing class-related shortcut features in images such that models trained on poisoned data are useless for real-world datasets. Self-supervised learning (SSL), which utilizes augmentations to learn instance discrimination, is regarded as a strong defense against poisoned data. However, by extending the study of SSL across multiple poisons on the CIFAR-10 and ImageNet-100 datasets, we demonstrate that it often performs poorly, far below that of training on clean data. Leveraging the vulnerability of SL to poison attacks, we introduce adversarial training (AT) on SL to obfuscate poison features and guide robust feature learning for SSL. Our proposed defense, designated VESPR (Vulnerability Exploitation of Supervised Poisoning for Robust SSL), surpasses the performance of six previous defenses across seven popular availability poisons. VESPR displays superior performance over all previous defenses, boosting the minimum and average ImageNet-100 test accuracies of poisoned models by 16% and 9%, respectively. Through analysis and ablation studies, we elucidate the mechanisms by which VESPR learns robust class features.

</details>

### SelfGeo: Self-supervised and Geodesic-Consistent Estimation of Keypoints on Deformable Shapes.
- **链接**: [arXiv:2408.02291](https://arxiv.org/abs/2408.02291) · [代码](https://github.com/IIT-PAVIS/SelfGeo) · 📚 被引 5
- **作者**: Mohammad Zohaib, Luca Cosmo, Alessio Del Bue
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Unsupervised 3D keypoints estimation from Point Cloud Data (PCD) is a complex task, even more challenging when an object shape is deforming. As keypoints should be semantically and geometrically consistent across all the 3D frames - each keypoint should be anchored to a specific part of the deforming shape irrespective of intrinsic and extrinsic motion. This paper presents, "SelfGeo", a self-supervised method that computes persistent 3D keypoints of non-rigid objects from arbitrary PCDs without the need of human annotations. The gist of SelfGeo is to estimate keypoints between frames that respect invariant properties of deforming bodies. Our main contribution is to enforce that keypoints deform along with the shape while keeping constant geodesic distances among them. This principle is then propagated to the design of a set of losses which minimization let emerge repeatable keypoints in specific semantic locations of the non-rigid shape. We show experimentally that the use of geodesic has a clear advantage in challenging dynamic scenes and with different classes of deforming shapes (humans and animals). Code and data are available at: https://github.com/IIT-PAVIS/SelfGeo

</details>

</details>

### Self-supervised Visual Learning from Interactions with Objects.
- **链接**: [arXiv:2407.06704](https://arxiv.org/abs/2407.06704)
- **作者**: Arthur Aubret, Céline Teulière, Jochen Triesch
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning (SSL) has revolutionized visual representation learning, but has not achieved the robustness of human vision. A reason for this could be that SSL does not leverage all the data available to humans during learning. When learning about an object, humans often purposefully turn or move around objects and research suggests that these interactions can substantially enhance their learning. Here we explore whether such object-related actions can boost SSL. For this, we extract the actions performed to change from one ego-centric view of an object to another in four video datasets. We then introduce a new loss function to learn visual and action embeddings by aligning the performed action with the representations of two images extracted from the same clip. This permits the performed actions to structure the latent visual representation. Our experiments show that our method consistently outperforms previous methods on downstream category recognition. In our analysis, we find that the observed improvement is associated with a better viewpoint-wise alignment of different objects from the same category. Overall, our work demonstrates that embodied interactions with objects can improve SSL of object categories.

</details>

### GroCo: Ground Constraint for Metric Self-supervised Monocular Depth.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73021-4_4) · 📚 被引 6
- **作者**: Aurélien Cecille, Stefan Duffner, Franck Davoine, Thibault Neveu, Rémi Agier
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### OP-Align: Object-Level and Part-Level Alignment for Self-supervised Category-Level Articulated Object Pose Estimation.
- **链接**: [arXiv:2408.16547](https://arxiv.org/abs/2408.16547) · 📚 被引 2
- **作者**: Yuchen Che, Ryo Furukawa, Asako Kanezaki
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Category-level articulated object pose estimation focuses on the pose estimation of unknown articulated objects within known categories. Despite its significance, this task remains challenging due to the varying shapes and poses of objects, expensive dataset annotation costs, and complex real-world environments. In this paper, we propose a novel self-supervised approach that leverages a single-frame point cloud to solve this task. Our model consistently generates reconstruction with a canonical pose and joint state for the entire input object, and it estimates object-level poses that reduce overall pose variance and part-level poses that align each part of the input with its corresponding part of the reconstruction. Experimental results demonstrate that our approach significantly outperforms previous self-supervised methods and is comparable to the state-of-the-art supervised methods. To assess the performance of our model in real-world scenarios, we also introduce a new real-world articulated object benchmark dataset.

</details>

### Betrayed by Attention: A Simple yet Effective Approach for Self-supervised Video Object Segmentation.
- **链接**: [arXiv:2311.17893](https://arxiv.org/abs/2311.17893) · [代码](https://github.com/shvdiwnkozbw/SSL-UVOS) · 📚 被引 7
- **作者**: Shuangrui Ding, Rui Qian, Haohang Xu, Dahua Lin, Hongkai Xiong
- **🏷️ 机构**: CUHK
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we propose a simple yet effective approach for self-supervised video object segmentation (VOS). Our key insight is that the inherent structural dependencies present in DINO-pretrained Transformers can be leveraged to establish robust spatio-temporal correspondences in videos. Furthermore, simple clustering on this correspondence cue is sufficient to yield competitive segmentation results. Previous self-supervised VOS techniques majorly resort to auxiliary modalities or utilize iterative slot attention to assist in object discovery, which restricts their general applicability and imposes higher computational requirements. To deal with these challenges, we develop a simplified architecture that capitalizes on the emerging objectness from DINO-pretrained Transformers, bypassing the need for additional modalities or slot attention. Specifically, we first introduce a single spatio-temporal Transformer block to process the frame-wise DINO features and establish spatio-temporal dependencies in the form of self-attention. Subsequently, utilizing these attention maps, we implement hierarchical clustering to generate object segmentation masks. To train the spatio-temporal block in a fully self-supervised manner, we employ semantic and dynamic motion consistency coupled with entropy normalization. Our method demonstrates state-of-the-art performance across multiple unsupervised VOS benchmarks and particularly excels in complex real-world multi-object video segmentation tasks such as DAVIS-17-Unsupervised and YouTube-VIS-19. The code and model checkpoints will be released at https://github.com/shvdiwnkozbw/SSL-UVOS.

</details>

### Learning Where to Look: Self-supervised Viewpoint Selection for Active Localization Using Geometrical Information.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73016-0_12) · 📚 被引 1
- **作者**: Luca Di Giammarino, Boyang Sun, Giorgio Grisetti, Marc Pollefeys, Hermann Blum, Daniel Barath
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### TreeSBA: Tree-Transformer for Self-supervised Sequential Brick Assembly.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73016-0_3) · 📚 被引 0
- **作者**: Mengqi Guo, Chen Li, Yuyang Zhao, Gim Hee Lee
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### On Pretraining Data Diversity for Self-Supervised Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72992-8_4)
- **作者**: Hasan Abed Al Kader Hammoud, Tuhin Das, Fabio Pizzati, Philip H. S. Torr, Adel Bibi, Bernard Ghanem
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Self-supervised Representation Learning for Adversarial Attack Detection.
- **链接**: [arXiv:2407.04382](https://arxiv.org/abs/2407.04382) · 📚 被引 12
- **作者**: Yi Li, Plamen Angelov, Neeraj Suri
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Supervised learning-based adversarial attack detection methods rely on a large number of labeled data and suffer significant performance degradation when applying the trained model to new domains. In this paper, we propose a self-supervised representation learning framework for the adversarial attack detection task to address this drawback. Firstly, we map the pixels of augmented input images into an embedding space. Then, we employ the prototype-wise contrastive estimation loss to cluster prototypes as latent variables. Additionally, drawing inspiration from the concept of memory banks, we introduce a discrimination bank to distinguish and learn representations for each individual instance that shares the same or a similar prototype, establishing a connection between instances and their associated prototypes. We propose a parallel axial-attention (PAA)-based encoder to facilitate the training process by parallel training over height- and width-axis of attention maps. Experimental results show that, compared to various benchmark self-supervised vision learning models and supervised adversarial attack detection methods, the proposed model achieves state-of-the-art performance on the adversarial attack detection task across a wide range of images.

</details>

### GenView: Enhancing View Quality with Pretrained Generative Model for Self-Supervised Learning.
- **链接**: [arXiv:2403.12003](https://arxiv.org/abs/2403.12003) · [代码](https://github.com/xiaojieli0903/genview) · 📚 被引 3
- **作者**: Xiaojie Li, Yibo Yang, Xiangtai Li, Jianlong Wu, Yue Yu, Bernard Ghanem et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning has achieved remarkable success in acquiring high-quality representations from unlabeled data. The widely adopted contrastive learning framework aims to learn invariant representations by minimizing the distance between positive views originating from the same image. However, existing techniques to construct positive views highly rely on manual transformations, resulting in limited diversity and potentially false positive pairs. To tackle these challenges, we present GenView, a controllable framework that augments the diversity of positive views leveraging the power of pretrained generative models while preserving semantics. We develop an adaptive view generation method that dynamically adjusts the noise level in sampling to ensure the preservation of essential semantic meaning while introducing variability. Additionally, we introduce a quality-driven contrastive loss, which assesses the quality of positive pairs by considering both foreground similarity and background diversity. This loss prioritizes the high-quality positive pairs we construct while reducing the influence of low-quality pairs, thereby mitigating potential semantic inconsistencies introduced by generative models and aggressive data augmentation. Thanks to the improved positive view quality and the quality-driven contrastive loss, GenView significantly improves self-supervised learning across various tasks. For instance, GenView improves MoCov2 performance by 2.5%/2.2% on ImageNet linear/semi-supervised classification. Moreover, GenView even performs much better than naively augmenting the ImageNet dataset with Laion400M or ImageNet21K. Code: https://github.com/xiaojieli0903/genview.

</details>

### Asymmetric Mask Scheme for Self-supervised Real Image Denoising.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72698-9_12) · 📚 被引 11
- **作者**: Xiangyu Liao, Tianheng Zheng, Jiayu Zhong, Pingping Zhang, Chao Ren
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Self-supervised Shape Completion via Involution and Implicit Correspondences.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73636-0_13) · 📚 被引 1
- **作者**: Mengya Liu, Ajad Chhatkuli, Janis Postels, Luc Van Gool, Federico Tombari
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Self-supervised Video Copy Localization with Regional Token Representation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73254-6_2) · 📚 被引 3
- **作者**: Minlong Lu, Yichen Lu, Siwei Nie, Xudong Yang, Xiaobo Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### CroMo-Mixup: Augmenting Cross-Model Representations for Continual Self-Supervised Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72989-8_18) · 📚 被引 3
- **作者**: Erum Mushtaq, Duygu Nur Yaldiz, Yavuz Faruk Bakman, Jie Ding, Chenyang Tao, Dimitrios Dimitriadis et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Walker: Self-supervised Multiple Object Tracking by Walking on Temporal Appearance Graphs.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73242-3_1)
- **作者**: Mattia Segù, Luigi Piccinelli, Siyuan Li, Luc Van Gool, Fisher Yu, Bernt Schiele
- **🏷️ 机构**: ETH Zurich
- **会议**: ECCV 2024

### Learning Representation for Multitask Learning Through Self-supervised Auxiliary Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72989-8_14) · 📚 被引 2
- **作者**: Seokwon Shin, Hyungrok Do, Youngdoo Son
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Self-supervised Any-Point Tracking by Contrastive Random Walks.
- **链接**: [arXiv:2409.16288](https://arxiv.org/abs/2409.16288) · 📚 被引 3
- **作者**: Ayush Shrivastava, Andrew Owens
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a simple, self-supervised approach to the Tracking Any Point (TAP) problem. We train a global matching transformer to find cycle consistent tracks through video via contrastive random walks, using the transformer's attention-based global matching to define the transition matrices for a random walk on a space-time graph. The ability to perform "all pairs" comparisons between points allows the model to obtain high spatial precision and to obtain a strong contrastive learning signal, while avoiding many of the complexities of recent approaches (such as coarse-to-fine matching). To do this, we propose a number of design decisions that allow global matching architectures to be trained through self-supervision using cycle consistency. For example, we identify that transformer-based methods are sensitive to shortcut solutions, and propose a data augmentation scheme to address them. Our method achieves strong performance on the TapVid benchmarks, outperforming previous self-supervised tracking methods, such as DIFT, and is competitive with several supervised methods.

</details>

### Self-supervised Feature Adaptation for 3D Industrial Anomaly Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72627-9_5)
- **作者**: Yuanpeng Tu, Boshen Zhang, Liang Liu, Yuxi Li, Jiangning Zhang, Yabiao Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### VideoClusterNet: Self-supervised and Adaptive Face Clustering for Videos.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73404-5_22) · 📚 被引 2
- **作者**: Devesh Walawalkar, Pablo Garrido
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Pose-Aware Self-supervised Learning with Viewpoint Trajectory Regularization.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72664-4_2) · 📚 被引 3
- **作者**: Jiayun Wang, Yubei Chen, Stella X. Yu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Revisit Event Generation Model: Self-supervised Learning of Event-to-Video Reconstruction with Implicit Neural Representations.
- **链接**: [arXiv:2407.18500](https://arxiv.org/abs/2407.18500) · 📚 被引 4
- **作者**: Zipeng Wang, Yunfan Lu, Lin Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Reconstructing intensity frames from event data while maintaining high temporal resolution and dynamic range is crucial for bridging the gap between event-based and frame-based computer vision. Previous approaches have depended on supervised learning on synthetic data, which lacks interpretability and risk over-fitting to the setting of the event simulator. Recently, self-supervised learning (SSL) based methods, which primarily utilize per-frame optical flow to estimate intensity via photometric constancy, has been actively investigated. However, they are vulnerable to errors in the case of inaccurate optical flow. This paper proposes a novel SSL event-to-video reconstruction approach, dubbed EvINR, which eliminates the need for labeled data or optical flow estimation. Our core idea is to reconstruct intensity frames by directly addressing the event generation model, essentially a partial differential equation (PDE) that describes how events are generated based on the time-varying brightness signals. Specifically, we utilize an implicit neural representation (INR), which takes in spatiotemporal coordinate $(x, y, t)$ and predicts intensity values, to represent the solution of the event generation equation. The INR, parameterized as a fully-connected Multi-layer Perceptron (MLP), can be optimized with its temporal derivatives supervised by events. To make EvINR feasible for online requisites, we propose several acceleration techniques that substantially expedite the training process. Comprehensive experiments demonstrate that our EvINR surpasses previous SSL methods by 38% w.r.t. Mean Squared Error (MSE) and is comparable or superior to SoTA supervised methods. Project page: https://vlislab22.github.io/EvINR/.

</details>

### On Learning Discriminative Features from Synthesized Data for Self-supervised Fine-Grained Visual Recognition.
- **链接**: [arXiv:2407.14676](https://arxiv.org/abs/2407.14676) · 📚 被引 4
- **作者**: Zihu Wang, Lingqiao Liu, Scott Ricardo Figueroa Weston, Samuel Tian, Peng Li
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-Supervised Learning (SSL) has become a prominent approach for acquiring visual representations across various tasks, yet its application in fine-grained visual recognition (FGVR) is challenged by the intricate task of distinguishing subtle differences between categories. To overcome this, we introduce an novel strategy that boosts SSL's ability to extract critical discriminative features vital for FGVR. This approach creates synthesized data pairs to guide the model to focus on discriminative features critical for FGVR during SSL. We start by identifying non-discriminative features using two main criteria: features with low variance that fail to effectively separate data and those deemed less important by Grad-CAM induced from the SSL loss. We then introduce perturbations to these non-discriminative features while preserving discriminative ones. A decoder is employed to reconstruct images from both perturbed and original feature vectors to create data pairs. An encoder is trained on such generated data pairs to become invariant to variations in non-discriminative dimensions while focusing on discriminative features, thereby improving the model's performance in FGVR tasks. We demonstrate the promising FGVR performance of the proposed approach through extensive evaluation on a wide variety of datasets.

</details>

### Towards Latent Masked Image Modeling for Self-supervised Visual Representation Learning.
- **链接**: [arXiv:2407.15837](https://arxiv.org/abs/2407.15837) · 📚 被引 8
- **作者**: Yibing Wei, Abhinav Gupta, Pedro Morgado
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Masked Image Modeling (MIM) has emerged as a promising method for deriving visual representations from unlabeled image data by predicting missing pixels from masked portions of images. It excels in region-aware learning and provides strong initializations for various tasks, but struggles to capture high-level semantics without further supervised fine-tuning, likely due to the low-level nature of its pixel reconstruction objective. A promising yet unrealized framework is learning representations through masked reconstruction in latent space, combining the locality of MIM with the high-level targets. However, this approach poses significant training challenges as the reconstruction targets are learned in conjunction with the model, potentially leading to trivial or suboptimal solutions.Our study is among the first to thoroughly analyze and address the challenges of such framework, which we refer to as Latent MIM. Through a series of carefully designed experiments and extensive analysis, we identify the source of these challenges, including representation collapsing for joint online/target optimization, learning objectives, the high region correlation in latent space and decoding conditioning. By sequentially addressing these issues, we demonstrate that Latent MIM can indeed learn high-level representations while retaining the benefits of MIM models.

</details>

### ProDepth: Boosting Self-supervised Multi-frame Monocular Depth with Probabilistic Fusion.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72646-0_12) · 📚 被引 9
- **作者**: Sungmin Woo, Wonjoon Lee, Woo Jin Kim, Dogyoon Lee, Sangyoun Lee
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Pseudo-Keypoint RKHS Learning for Self-supervised 6DoF Pose Estimation.
- **链接**: [arXiv:2311.09500](https://arxiv.org/abs/2311.09500) · 📚 被引 4
- **作者**: Yangzheng Wu, Michael A. Greenspan
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We address the simulation-to-real domain gap in six degree-of-freedom pose estimation (6DoF PE), and propose a novel self-supervised keypoint voting-based 6DoF PE framework, effectively narrowing this gap using a learnable kernel in RKHS. We formulate this domain gap as a distance in high-dimensional feature space, distinct from previous iterative matching methods. We propose an adapter network, which is pre-trained on purely synthetic data with synthetic ground truth poses, and which evolves the network parameters from this source synthetic domain to the target real domain. Importantly, the real data training only uses pseudo-poses estimated by pseudo-keypoints, and thereby requires no real ground truth data annotations. Our proposed method is called RKHSPose, and achieves state-of-the-art performance among self-supervised methods on three commonly used 6DoF PE datasets including LINEMOD (+4.2%), Occlusion LINEMOD (+2%), and YCB-Video (+3%). It also compares favorably to fully supervised methods on all six applicable BOP core datasets, achieving within -11.3% to +0.2% of the top fully supervised results.

</details>

### Self-Supervised Video Desmoking for Laparoscopic Surgery.
- **链接**: [arXiv:2403.11192](https://arxiv.org/abs/2403.11192) · [代码](https://github.com/ZcsrenlongZ/SelfSVD) · 📚 被引 12
- **作者**: Renlong Wu, Zhilu Zhang, Shuohao Zhang, Longfei Gou, Haobin Chen, Lei Zhang et al.
- **🏷️ 机构**: PolyU / OPPO
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Due to the difficulty of collecting real paired data, most existing desmoking methods train the models by synthesizing smoke, generalizing poorly to real surgical scenarios. Although a few works have explored single-image real-world desmoking in unpaired learning manners, they still encounter challenges in handling dense smoke. In this work, we address these issues together by introducing the self-supervised surgery video desmoking (SelfSVD). On the one hand, we observe that the frame captured before the activation of high-energy devices is generally clear (named pre-smoke frame, PS frame), thus it can serve as supervision for other smoky frames, making real-world self-supervised video desmoking practically feasible. On the other hand, in order to enhance the desmoking performance, we further feed the valuable information from PS frame into models, where a masking strategy and a regularization term are presented to avoid trivial solutions. In addition, we construct a real surgery video dataset for desmoking, which covers a variety of smoky scenes. Extensive experiments on the dataset show that our SelfSVD can remove smoke more effectively and efficiently while recovering more photo-realistic details than the state-of-the-art methods. The dataset, codes, and pre-trained models are available at \url{https://github.com/ZcsrenlongZ/SelfSVD}.

</details>

### Made to Order: Discovering Monotonic Temporal Changes via Self-supervised Video Ordering.
- **链接**: [arXiv:2404.16828](https://arxiv.org/abs/2404.16828) · 📚 被引 3
- **作者**: Charig Yang, Weidi Xie, Andrew Zisserman
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Our objective is to discover and localize monotonic temporal changes in a sequence of images. To achieve this, we exploit a simple proxy task of ordering a shuffled image sequence, with `time' serving as a supervisory signal, since only changes that are monotonic with time can give rise to the correct ordering. We also introduce a transformer-based model for ordering of image sequences of arbitrary length with built-in attribution maps. After training, the model successfully discovers and localizes monotonic changes while ignoring cyclic and stochastic ones. We demonstrate applications of the model in multiple domains covering different scene and object types, discovering both object-level and environmental changes in unseen sequences. We also demonstrate that the attention-based attribution maps function as effective prompts for segmenting the changing regions, and that the learned representations can be used for downstream applications. Finally, we show that the model achieves the state-of-the-art on standard benchmarks for image ordering.

</details>

### Rotated Orthographic Projection for Self-supervised 3D Human Pose Estimation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72890-7_26) · 📚 被引 1
- **作者**: Yao Yao, Yixuan Pan, Wenjun Shi, Dongchen Zhu, Lei Wang, Jiamao Li
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Test-Time Model Adaptation for Image Reconstruction Using Self-supervised Adaptive Layers.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72913-3_7) · 📚 被引 3
- **作者**: Yutian Zhao, Tianjing Zhang, Hui Ji
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### SSL-Cleanse: Trojan Detection and Mitigation in Self-Supervised Learning.
- **链接**: [arXiv:2303.09079](https://arxiv.org/abs/2303.09079) · [代码](https://github.com/UCF-ML-Research/SSL-Cleanse) · 📚 被引 12
- **作者**: Mengxin Zheng, Jiaqi Xue, Zihao Wang, Xun Chen, Qian Lou, Lei Jiang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning (SSL) is a prevalent approach for encoding data representations. Using a pre-trained SSL image encoder and subsequently training a downstream classifier, impressive performance can be achieved on various tasks with very little labeled data. The growing adoption of SSL has led to an increase in security research on SSL encoders and associated Trojan attacks. Trojan attacks embedded in SSL encoders can operate covertly, spreading across multiple users and devices. The presence of backdoor behavior in Trojaned encoders can inadvertently be inherited by downstream classifiers, making it even more difficult to detect and mitigate the threat. Although current Trojan detection methods in supervised learning can potentially safeguard SSL downstream classifiers, identifying and addressing triggers in the SSL encoder before its widespread dissemination is a challenging task. This challenge arises because downstream tasks might be unknown, dataset labels may be unavailable, and the original unlabeled training dataset might be inaccessible during Trojan detection in SSL encoders. We introduce SSL-Cleanse as a solution to identify and mitigate backdoor threats in SSL encoders. We evaluated SSL-Cleanse on various datasets using 1200 encoders, achieving an average detection success rate of 82.2% on ImageNet-100. After mitigating backdoors, on average, backdoored encoders achieve 0.3% attack success rate without great accuracy loss, proving the effectiveness of SSL-Cleanse. The source code of SSL-Cleanse is available at https://github.com/UCF-ML-Research/SSL-Cleanse.

</details>

### Learning the Unlearned: Mitigating Feature Suppression in Contrastive Learning.
- **链接**: [arXiv:2402.11816](https://arxiv.org/abs/2402.11816) · 📚 被引 3
- **作者**: Jihai Zhang, Xiang Lan, Xiaoye Qu, Yu Cheng, Mengling Feng, Bryan Hooi
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-Supervised Contrastive Learning has proven effective in deriving high-quality representations from unlabeled data. However, a major challenge that hinders both unimodal and multimodal contrastive learning is feature suppression, a phenomenon where the trained model captures only a limited portion of the information from the input data while overlooking other potentially valuable content. This issue often leads to indistinguishable representations for visually similar but semantically different inputs, adversely affecting downstream task performance, particularly those requiring rigorous semantic comprehension. To address this challenge, we propose a novel model-agnostic Multistage Contrastive Learning (MCL) framework. Unlike standard contrastive learning which inherently captures one single biased feature distribution, MCL progressively learns previously unlearned features through feature-aware negative sampling at each stage, where the negative samples of an anchor are exclusively selected from the cluster it was assigned to in preceding stages. Meanwhile, MCL preserves the previously well-learned features by cross-stage representation integration, integrating features across all stages to form final representations. Our comprehensive evaluation demonstrates MCL's effectiveness and superiority across both unimodal and multimodal contrastive learning, spanning a range of model architectures from ResNet to Vision Transformers (ViT). Remarkably, in tasks where the original CLIP model has shown limitations, MCL dramatically enhances performance, with improvements up to threefold on specific attributes in the recently proposed MMVP benchmark.

</details>

### FlowCon: Out-of-Distribution Detection Using Flow-Based Contrastive Learning.
- **链接**: [arXiv:2407.03489](https://arxiv.org/abs/2407.03489) · 📚 被引 1
- **作者**: Saandeep Aathreya, Shaun J. Canavan
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Identifying Out-of-distribution (OOD) data is becoming increasingly critical as the real-world applications of deep learning methods expand. Post-hoc methods modify softmax scores fine-tuned on outlier data or leverage intermediate feature layers to identify distinctive patterns between In-Distribution (ID) and OOD samples. Other methods focus on employing diverse OOD samples to learn discrepancies between ID and OOD. These techniques, however, are typically dependent on the quality of the outlier samples assumed. Density-based methods explicitly model class-conditioned distributions but this requires long training time or retraining the classifier. To tackle these issues, we introduce \textit{FlowCon}, a new density-based OOD detection technique. Our main innovation lies in efficiently combining the properties of normalizing flow with supervised contrastive learning, ensuring robust representation learning with tractable density estimation. Empirical evaluation shows the enhanced performance of our method across common vision datasets such as CIFAR-10 and CIFAR-100 pretrained on ResNet18 and WideResNet classifiers. We also perform quantitative analysis using likelihood plots and qualitative visualization using UMAP embeddings and demonstrate the robustness of the proposed method under various OOD contexts. Code will be open-sourced post decision.

</details>

### Contrasting Deepfakes Diffusion via Contrastive Learning and Global-Local Similarities.
- **链接**: [arXiv:2407.20337](https://arxiv.org/abs/2407.20337) · [代码](https://github.com/aimagelab/CoDE) · 📚 被引 18
- **作者**: Federico Cocchi, Marcella Cornia, Lorenzo Baraldi, Alessandro Nicolosi, Rita Cucchiara
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Discerning between authentic content and that generated by advanced AI methods has become increasingly challenging. While previous research primarily addresses the detection of fake faces, the identification of generated natural images has only recently surfaced. This prompted the recent exploration of solutions that employ foundation vision-and-language models, like CLIP. However, the CLIP embedding space is optimized for global image-to-text alignment and is not inherently designed for deepfake detection, neglecting the potential benefits of tailored training and local image features. In this study, we propose CoDE (Contrastive Deepfake Embeddings), a novel embedding space specifically designed for deepfake detection. CoDE is trained via contrastive learning by additionally enforcing global-local similarities. To sustain the training of our model, we generate a comprehensive dataset that focuses on images generated by diffusion models and encompasses a collection of 9.2 million images produced by using four different generators. Experimental results demonstrate that CoDE achieves state-of-the-art accuracy on the newly collected dataset, while also showing excellent generalization capabilities to unseen image generators. Our source code, trained models, and collected dataset are publicly available at: https://github.com/aimagelab/CoDE.

</details>

### CLAP: Isolating Content from Style Through Contrastive Learning with Augmented Prompts.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72664-4_8) · 📚 被引 8
- **作者**: Yichao Cai, Yuhang Liu, Zhen Zhang, Javen Qinfeng Shi
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Understanding and Mitigating Human-Labelling Errors in Supervised Contrastive Learning.
- **链接**: [arXiv:2403.06289](https://arxiv.org/abs/2403.06289) · 📚 被引 1
- **作者**: Zijun Long, Lipeng Zhuang, George Killick, Richard McCreadie, Gerardo Aragon-Camarasa, Paul Henderson
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Human-annotated vision datasets inevitably contain a fraction of human mislabelled examples. While the detrimental effects of such mislabelling on supervised learning are well-researched, their influence on Supervised Contrastive Learning (SCL) remains largely unexplored. In this paper, we show that human-labelling errors not only differ significantly from synthetic label errors, but also pose unique challenges in SCL, different to those in traditional supervised learning methods. Specifically, our results indicate they adversely impact the learning process in the ~99% of cases when they occur as false positive samples. Existing noise-mitigating methods primarily focus on synthetic label errors and tackle the unrealistic setting of very high synthetic noise rates (40-80%), but they often underperform on common image datasets due to overfitting. To address this issue, we introduce a novel SCL objective with robustness to human-labelling errors, SCL-RHE. SCL-RHE is designed to mitigate the effects of real-world mislabelled examples, typically characterized by much lower noise rates (<5%). We demonstrate that SCL-RHE consistently outperforms state-of-the-art representation learning and noise-mitigating methods across various vision benchmarks, by offering improved resilience against human-labelling errors.

</details>

### Adaptive Multi-head Contrastive Learning.
- **链接**: [arXiv:2310.05615](https://arxiv.org/abs/2310.05615)
- **作者**: Lei Wang, Piotr Koniusz, Tom Gedeon, Liang Zheng
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In contrastive learning, two views of an original image, generated by different augmentations, are considered a positive pair, and their similarity is required to be high. Similarly, two views of distinct images form a negative pair, with encouraged low similarity. Typically, a single similarity measure, provided by a lone projection head, evaluates positive and negative sample pairs. However, due to diverse augmentation strategies and varying intra-sample similarity, views from the same image may not always be similar. Additionally, owing to inter-sample similarity, views from different images may be more akin than those from the same image. Consequently, enforcing high similarity for positive pairs and low similarity for negative pairs may be unattainable, and in some cases, such enforcement could detrimentally impact performance. To address this challenge, we propose using multiple projection heads, each producing a distinct set of features. Our pre-training loss function emerges from a solution to the maximum likelihood estimation over head-wise posterior distributions of positive samples given observations. This loss incorporates the similarity measure over positive and negative pairs, each re-weighted by an individual adaptive temperature, regulated to prevent ill solutions. Our approach, Adaptive Multi-Head Contrastive Learning (AMCL), can be applied to and experimentally enhances several popular contrastive learning methods such as SimCLR, MoCo, and Barlow Twins. The improvement remains consistent across various backbones and linear probing epochs, and becomes more significant when employing multiple augmentation methods.

</details>

### WeCromCL: Weakly Supervised Cross-Modality Contrastive Learning for Transcription-Only Supervised Text Spotting.
- **链接**: [arXiv:2407.19507](https://arxiv.org/abs/2407.19507) · 📚 被引 2
- **作者**: Jingjing Wu, Zhengyao Fang, Pengyuan Lyu, Chengquan Zhang, Fanglin Chen, Guangming Lu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Transcription-only Supervised Text Spotting aims to learn text spotters relying only on transcriptions but no text boundaries for supervision, thus eliminating expensive boundary annotation. The crux of this task lies in locating each transcription in scene text images without location annotations. In this work, we formulate this challenging problem as a Weakly Supervised Cross-modality Contrastive Learning problem, and design a simple yet effective model dubbed WeCromCL that is able to detect each transcription in a scene image in a weakly supervised manner. Unlike typical methods for cross-modality contrastive learning that focus on modeling the holistic semantic correlation between an entire image and a text description, our WeCromCL conducts atomistic contrastive learning to model the character-wise appearance consistency between a text transcription and its correlated region in a scene image to detect an anchor point for the transcription in a weakly supervised manner. The detected anchor points by WeCromCL are further used as pseudo location labels to guide the learning of text spotting. Extensive experiments on four challenging benchmarks demonstrate the superior performance of our model over other methods. Code will be released.

</details>

### Prompt-Driven Contrastive Learning for Transferable Adversarial Attacks.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72775-7_3) · 📚 被引 4
- **作者**: Hunmin Yang, Jongoh Jeong, Kuk-Jin Yoon
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Contrastive Learning with Synthetic Positives.
- **链接**: [arXiv:2408.16965](https://arxiv.org/abs/2408.16965)
- **作者**: Dewen Zeng, Yawen Wu, Xinrong Hu, Xiaowei Xu, Yiyu Shi
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Contrastive learning with the nearest neighbor has proved to be one of the most efficient self-supervised learning (SSL) techniques by utilizing the similarity of multiple instances within the same class. However, its efficacy is constrained as the nearest neighbor algorithm primarily identifies "easy" positive pairs, where the representations are already closely located in the embedding space. In this paper, we introduce a novel approach called Contrastive Learning with Synthetic Positives (CLSP) that utilizes synthetic images, generated by an unconditional diffusion model, as the additional positives to help the model learn from diverse positives. Through feature interpolation in the diffusion model sampling process, we generate images with distinct backgrounds yet similar semantic content to the anchor image. These images are considered "hard" positives for the anchor image, and when included as supplementary positives in the contrastive loss, they contribute to a performance improvement of over 2% and 1% in linear evaluation compared to the previous NNCLR and All4One methods across multiple benchmark datasets such as CIFAR10, achieving state-of-the-art methods. On transfer learning benchmarks, CLSP outperforms existing SSL frameworks on 6 out of 8 downstream datasets. We believe CLSP establishes a valuable baseline for future SSL studies incorporating synthetic data in the training process.

</details>

## 跨领域论文（完整笔记在其他领域）

- Grounding DINO: Marrying DINO with Grounded Pre-training for Open-Set Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- LISO: Lidar-Only Self-supervised 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- Self-supervised Co-salient Object Detection via Feature Correspondences at Multiple Scales. → [object-detection](../object-detection/Guideline%202024.md)
- Decoupling Common and Unique Representations for Multimodal Self-supervised Learning. → [multimodal](../multimodal/Guideline%202024.md)
- High-Precision Self-supervised Monocular Depth Estimation with Rich-Resource Prior. → [multi-camera-perception](../multi-camera-perception/Guideline%202024.md)
- Self-Supervised Audio-Visual Soundscape Stylization. → [multimodal](../multimodal/Guideline%202024.md)
- Mono-ViFI: A Unified Learning Framework for Self-supervised Single and Multi-frame Monocular Depth Estimation. → [multi-camera-perception](../multi-camera-perception/Guideline%202024.md)
- FroSSL: Frobenius Norm Minimization for Efficient Multiview Self-supervised Learning. → [multi-camera-perception](../multi-camera-perception/Guideline%202024.md)
- Improving Domain Generalization in Self-supervised Monocular Depth Estimation via Stabilized Adversarial Training. → [multi-camera-perception](../multi-camera-perception/Guideline%202024.md)
- SCPNet: Unsupervised Cross-Modal Homography Estimation via Intra-modal Self-supervised Learning. → [multimodal](../multimodal/Guideline%202024.md)
- SeFlow: A Self-supervised Scene Flow Method in Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202024.md)
- Revisit Self-supervised Depth Estimation with Local Structure-from-Motion. → [multi-camera-perception](../multi-camera-perception/Guideline%202024.md)
- M2Depth: Self-supervised Two-Frame Multi-camera Metric Depth Estimation. → [multi-camera-perception](../multi-camera-perception/Guideline%202024.md)
- Improving Medical Multi-modal Contrastive Learning with Expert Annotations. → [multimodal](../multimodal/Guideline%202024.md)

## 🆕 增量新增

### Towards Scalable 3D Anomaly Detection and Localization: A Benchmark via 3D Anomaly Synthesis and A Self-Supervised Learning Network. **⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2311.14897](https://arxiv.org/abs/2311.14897) · 📚 被引 50
- **作者**: Wenqiao Li, Xiaohao Xu, Yao Gu, Bozhong Zheng, Shenghua Gao, Yingna Wu
- **🏷️ 机构**: ShanghaiTech University, University of Michigan, Ann Arbor
- **会议**: CVPR 2024
- **摘要（中）**: 这篇论文针对3D异常检测中真实异常数据稀缺、限制模型可扩展性的问题。作者提出了一种3D异常合成流程，基于ShapeNet构建了包含40类1600个点云样本的Anomaly-ShapeNet数据集，并设计了一种自监督方法IMRNet，通过几何感知采样模块保留潜在异常区域，并利用掩码重建进行表示学习。相比现有方法，该方法提供了丰富多样的合成数据，增强了模型对工业场景的适应性。实验表明，该方法能有效训练模型并提升3D异常定位性能。
- **摘要（英）**: This paper addresses the scarcity of real 3D anomaly data that limits model scalability. It proposes a 3D anomaly synthesis pipeline to create Anomaly-ShapeNet with 1600 samples across 40 categories, and a self-supervised IMRNet with geometry-aware sampling and mask reconstruction. This approach provides rich training data and improves adaptability to industrial scenarios, with experiments showing effective anomaly localization.
- **核心贡献**: 提出了Anomaly-ShapeNet合成数据集和IMRNet自监督网络，用于可扩展的3D异常检测与定位。
- **创新点**: 利用几何感知采样和掩码重建实现自监督3D异常表示学习。
- **结果**: 在合成数据集上实现了有效的3D异常检测和定位，增强了模型泛化能力。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, 3D anomaly detection, a crucial problem involving fine-grained geometry discrimination, is getting more attention. However, the lack of abundant real 3D anomaly data limits the scalability of current models. To enable scalable anomaly data collection, we propose a 3D anomaly synthesis pipeline to adapt existing large-scale 3Dmodels for 3D anomaly detection. Specifically, we construct a synthetic dataset, i.e., Anomaly-ShapeNet, basedon ShapeNet. Anomaly-ShapeNet consists of 1600 point cloud samples under 40 categories, which provides a rich and varied collection of data, enabling efficient training and enhancing adaptability to industrial scenarios. Meanwhile,to enable scalable representation learning for 3D anomaly localization, we propose a self-supervised method, i.e., Iterative Mask Reconstruction Network (IMRNet). During training, we propose a geometry-aware sample module to preserve potentially anomalous local regions during point cloud down-sampling. Then, we randomly mask out point patches and sent the visible patches to a transformer for reconstruction-based self-supervision. During testing, the point cloud repeatedly goes through the Mask Reconstruction Network, with each iteration's output becoming the next input. By merging and contrasting the final reconstructed point cloud with the initial input, our method successfully locates anomalies. Experiments show that IMRNet outperforms previous state-of-the-art methods, achieving 66.1% in I-AUC on Anomaly-ShapeNet dataset and 72.5% in I-AUC on Real3D-AD dataset. Our dataset will be released at https://github.com/Chopper-233/Anomaly-ShapeNet

</details>

### SCE-MAE: Selective Correspondence Enhancement with Masked Autoencoder for Self-Supervised Landmark Estimation. **⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2405.18322](https://arxiv.org/abs/2405.18322) · 📚 被引 3
- **作者**: Kejia Yin, Varshanth S. Rao, Ruowei Jiang, Xudong Liu, Parham Aarabi, David B. Lindell
- **🏷️ 机构**: University of Toronto, ModiFace
- **会议**: CVPR 2024
- **摘要（中）**: 针对自监督关键点估计中特征表示粗糙和计算开销大的问题，提出了SCE-MAE框架。该方法利用MAE进行区域级自监督学习，在普通特征图上操作，并通过对应近似与精炼块选择局部对应关系。相比现有方法，提高了效率和鲁棒性。实验证明SCE-MAE在关键点估计任务上表现优异。
- **摘要（英）**: This paper introduces SCE-MAE for self-supervised landmark estimation, leveraging MAE for region-level SSL and a Correspondence Approximation and Refinement Block to hone select local correspondences. The method operates on vanilla feature maps, reducing memory overhead while improving robustness. Extensive experiments demonstrate its effectiveness and efficiency.
- **核心贡献**: 提出了SCE-MAE框架，结合MAE和选择性对应增强提升自监督关键点估计。
- **创新点**: 利用MAE的区域级SSL和密度峰值聚类实现高效局部对应学习。
- **结果**: 实验证明SCE-MAE在关键点估计任务上高效且鲁棒。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised landmark estimation is a challenging task that demands the formation of locally distinct feature representations to identify sparse facial landmarks in the absence of annotated data. To tackle this task, existing state-of-the-art (SOTA) methods (1) extract coarse features from backbones that are trained with instance-level self-supervised learning (SSL) paradigms, which neglect the dense prediction nature of the task, (2) aggregate them into memory-intensive hypercolumn formations, and (3) supervise lightweight projector networks to naively establish full local correspondences among all pairs of spatial features. In this paper, we introduce SCE-MAE, a framework that (1) leverages the MAE, a region-level SSL method that naturally better suits the landmark prediction task, (2) operates on the vanilla feature map instead of on expensive hypercolumns, and (3) employs a Correspondence Approximation and Refinement Block (CARB) that utilizes a simple density peak clustering algorithm and our proposed Locality-Constrained Repellence Loss to directly hone only select local correspondences. We demonstrate through extensive experiments that SCE-MAE is highly effective and robust, outperforming existing SOTA methods by large margins of approximately 20%-44% on the landmark matching and approximately 9%-15% on the landmark detection tasks.

</details>

### ViC-MAE: Self-supervised Representation Learning from Images and Video with Contrastive Masked Autoencoders. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73235-5_25) · 📚 被引 10
- **作者**: Jefferson Hernandez, Ruben Villegas, Vicente Ordonez
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024
- **摘要（中）**: ①针对图像和视频联合自监督表示学习中，现有方法未能充分融合对比学习和掩码重建优势的问题。②提出ViC-MAE，结合对比学习与掩码自编码器，在图像和视频数据上联合训练，通过共享编码器学习跨模态特征。③相比单一MAE或对比方法，ViC-MAE利用对比损失增强判别性，同时通过重建保留细节信息。④在视频动作识别和图像分类任务上，如Kinetics-400上达到85.1% top-1准确率，优于现有自监督方法。
- **摘要（英）**: This paper tackles the challenge of jointly learning self-supervised representations from images and videos by combining contrastive learning and masked autoencoding. It proposes ViC-MAE, which trains a shared encoder with both contrastive and reconstruction losses, capturing discriminative and detailed features. Compared to single-modality MAE or contrastive methods, ViC-MAE improves cross-modal generalization. It achieves 85.1% top-1 accuracy on Kinetics-400, outperforming prior self-supervised approaches.
- **核心贡献**: 提出ViC-MAE，统一图像和视频的对比掩码自编码框架。
- **创新点**: 在共享编码器中联合优化对比损失和重建损失。
- **结果**: 在视频和图像基准上达到领先性能。

### NeRF-MAE: Masked AutoEncoders for Self-supervised 3D Representation Learning for Neural Radiance Fields. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73223-2_24) · 📚 被引 12
- **作者**: Muhammad Zubair Irshad, Sergey Zakharov, Vitor Guizilini, Adrien Gaidon, Zsolt Kira, Rares Ambrus
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024
- **摘要（中）**: ①针对NeRF场景表示中缺乏自监督预训练方法的问题。②提出NeRF-MAE，将掩码自编码器应用于NeRF的3D特征场，通过掩码部分空间位置并重建特征来学习3D表示。③相比基于2D图像的MAE，NeRF-MAE直接在3D空间中操作，更好地捕获几何和外观信息。④在3D分类和分割任务上，如ModelNet40分类达到92.3%准确率，显著优于从零训练和2D预训练基线。
- **摘要（英）**: This paper addresses the lack of self-supervised pretraining for NeRF-based 3D representations. It proposes NeRF-MAE, which applies masked autoencoding to NeRF's 3D feature fields by masking spatial locations and reconstructing features. Unlike 2D image MAEs, NeRF-MAE operates directly in 3D space, capturing geometry and appearance better. It achieves 92.3% accuracy on ModelNet40 classification, outperforming from-scratch and 2D-pretrained baselines.
- **核心贡献**: 首次提出NeRF-MAE，用于NeRF特征场的自监督学习。
- **创新点**: 在3D特征场上执行掩码重建，利用NeRF的隐式表示。
- **结果**: 在多个3D任务上超越现有方法。

### SPU-PMD: Self-Supervised Point Cloud Upsampling via Progressive Mesh Deformation. **⭐⭐** (相关度: 40%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00496) · 📚 被引 16
- **作者**: Yanzhe Liu, Rong Chen, Yushi Li, Yixi Li, Xuehou Tan
- **🏷️ 机构**: Dalian Maritime University, Xi&#x0027;an Jiaotong-Liverpool University, Tokai University
- **会议**: CVPR 2024
- **摘要（中）**: 该论文摘要为空，无法获取具体内容。根据标题推测，它可能针对点云上采样问题，提出了一种基于渐进网格变形的自监督方法。由于缺乏详细信息，无法评估其方法质量和效果。
- **摘要（英）**: The abstract is empty, so details are unavailable. Based on the title, it likely addresses point cloud upsampling via a self-supervised progressive mesh deformation approach. Quality and results cannot be assessed due to missing information.
- **核心贡献**: 未知，因摘要缺失。
- **创新点**: 未知，因摘要缺失。
- **结果**: 未知，因摘要缺失。

### Mitigating Object Dependencies: Improving Point Cloud Self-Supervised Learning Through Object Exchange. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2404.07504](https://arxiv.org/abs/2404.07504) · 📚 被引 5
- **作者**: Yanhao Wu, Tong Zhang, Wei Ke, Congpei Qiu, Sabine Süsstrunk, Mathieu Salzmann
- **🏷️ 机构**: School of Software Engineering, Xi&#x0027;an Jiaotong University,China, School of Computer and Communication Sciences, EPFL,Switzerland
- **会议**: CVPR 2024
- **摘要（中）**: 这篇论文针对室内点云场景中物体间强依赖关系导致网络忽略个体模式的问题。作者提出了一种新的自监督学习策略，通过物体交换策略在不同场景间交换相似大小的物体对，以解耦上下文依赖，并引入上下文感知特征学习，聚合跨场景物体特征以编码物体模式。相比现有SSL方法，该方法在特征鲁棒性和环境变化适应性上表现更优。实验表明，该方法在点云场景理解任务上超越了现有技术，并展示了良好的迁移能力。
- **摘要（英）**: This paper addresses the issue of strong inter-object dependencies in indoor point clouds that cause networks to bypass individual patterns. It proposes an SSL strategy with object exchange to disentangle context and context-aware feature learning to encode object patterns. The method outperforms existing SSL techniques in robustness and transferability, as shown in experiments.
- **核心贡献**: 提出了基于物体交换和上下文感知特征学习的自监督策略，提升点云特征鲁棒性。
- **创新点**: 通过物体交换解耦上下文依赖，并聚合跨场景特征学习物体模式。
- **结果**: 在点云场景理解任务上超越了现有SSL方法，并展现出更强的环境鲁棒性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In the realm of point cloud scene understanding, particularly in indoor scenes, objects are arranged following human habits, resulting in objects of certain semantics being closely positioned and displaying notable inter-object correlations. This can create a tendency for neural networks to exploit these strong dependencies, bypassing the individual object patterns. To address this challenge, we introduce a novel self-supervised learning (SSL) strategy. Our approach leverages both object patterns and contextual cues to produce robust features. It begins with the formulation of an object-exchanging strategy, where pairs of objects with comparable sizes are exchanged across different scenes, effectively disentangling the strong contextual dependencies. Subsequently, we introduce a context-aware feature learning strategy, which encodes object patterns without relying on their specific context by aggregating object features across various scenes. Our extensive experiments demonstrate the superiority of our method over existing SSL techniques, further showing its better robustness to environmental changes. Moreover, we showcase the applicability of our approach by transferring pre-trained models to diverse point cloud datasets.

</details>

### SelfOcc: Self-Supervised Vision-Based 3D Occupancy Prediction. **⭐⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2311.12754](https://arxiv.org/abs/2311.12754) · 📚 被引 79
- **作者**: Yuanhui Huang, Wenzhao Zheng, Borui Zhang, Jie Zhou, Jiwen Lu
- **🏷️ 机构**: Beijing National Research Center for Information Science and Technology,China, Tsinghua University,Department of Automation,China
- **会议**: CVPR 2024
- **摘要（中）**: ①针对自动驾驶中3D占用预测依赖昂贵体素标注的问题，提出自监督方法。②将图像转换到3D空间（如BEV）获得场景表示，将其视为符号距离场（SDF），通过渲染前后帧2D图像作为自监督信号进行学习，并采用MVS嵌入策略优化SDF权重。③相比现有方法，首次实现仅用视频序列进行自监督3D占用预测，无需任何3D标签。④在SemanticKITTI上，单帧输入比之前最优方法SceneRF提升58.7%，且是首个在nuScenes上为环视相机生成合理3D占用的自监督工作，同时产生高质量深度图。
- **摘要（英）**: This paper addresses the challenge of expensive 3D occupancy labeling in autonomous driving by proposing SelfOcc, a self-supervised method that learns 3D occupancy from video sequences only. It transforms images into 3D space, treats representations as signed distance fields, and uses rendering of previous/future frames as supervision, with an MVS-embedded strategy for optimization. SelfOcc outperforms SceneRF by 58.7% on SemanticKITTI with single-frame input and is the first self-supervised work to produce reasonable 3D occupancy for surround cameras on nuScenes.
- **核心贡献**: 提出首个自监督3D占用预测框架，仅需视频序列即可学习场景占用。
- **创新点**: 利用SDF和神经渲染实现自监督，并嵌入MVS策略优化多深度提议。
- **结果**: 在SemanticKITTI上提升58.7%，并在nuScenes上首次实现自监督环视占用预测。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D occupancy prediction is an important task for the robustness of vision-centric autonomous driving, which aims to predict whether each point is occupied in the surrounding 3D space. Existing methods usually require 3D occupancy labels to produce meaningful results. However, it is very laborious to annotate the occupancy status of each voxel. In this paper, we propose SelfOcc to explore a self-supervised way to learn 3D occupancy using only video sequences. We first transform the images into the 3D space (e.g., bird's eye view) to obtain 3D representation of the scene. We directly impose constraints on the 3D representations by treating them as signed distance fields. We can then render 2D images of previous and future frames as self-supervision signals to learn the 3D representations. We propose an MVS-embedded strategy to directly optimize the SDF-induced weights with multiple depth proposals. Our SelfOcc outperforms the previous best method SceneRF by 58.7% using a single frame as input on SemanticKITTI and is the first self-supervised work that produces reasonable 3D occupancy for surround cameras on nuScenes. SelfOcc produces high-quality depth and achieves state-of-the-art results on novel depth synthesis, monocular depth estimation, and surround-view depth estimation on the SemanticKITTI, KITTI-2015, and nuScenes, respectively. Code: https://github.com/huang-yh/SelfOcc.

</details>

### Self-Supervised Multi-Object Tracking with Path Consistency. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2404.05136](https://arxiv.org/abs/2404.05136) · 📚 被引 15
- **作者**: Zijia Lu, Bing Shuai, Yanbei Chen, Zhenlin Xu, Davide Modolo
- **🏷️ 机构**: AWS AI Labs
- **会议**: CVPR 2024
- **摘要（中）**: 针对无监督多目标跟踪中缺乏身份监督导致目标匹配学习困难的问题，提出了路径一致性概念，通过让模型在不同帧跳过组合下生成多个关联结果，并强制这些结果一致来训练匹配模型。设计了路径一致性损失，仅用自监督信号训练，无需人工身份标注。在MOT17、PersonPath22和KITTI三个数据集上，该方法显著优于现有无监督方法，并接近监督方法的性能。
- **摘要（英）**: To learn robust object matching without identity supervision, this paper introduces path consistency, enforcing consistent association results across different frame-skipping observation paths. A path consistency loss trains the matching model purely self-supervised, outperforming existing unsupervised methods on MOT17, PersonPath22, and KITTI, approaching supervised performance.
- **核心贡献**: 提出路径一致性损失，实现无需身份标注的自监督多目标跟踪训练。
- **创新点**: 通过帧跳过生成多观测路径并强制关联一致性，创新性地利用观测不变性。
- **结果**: 在三个跟踪数据集上超越现有无监督方法，接近监督方法性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we propose a novel concept of path consistency to learn robust object matching without using manual object identity supervision. Our key idea is that, to track a object through frames, we can obtain multiple different association results from a model by varying the frames it can observe, i.e., skipping frames in observation. As the differences in observations do not alter the identities of objects, the obtained association results should be consistent. Based on this rationale, we generate multiple observation paths, each specifying a different set of frames to be skipped, and formulate the Path Consistency Loss that enforces the association results are consistent across different observation paths. We use the proposed loss to train our object matching model with only self-supervision. By extensive experiments on three tracking datasets (MOT17, PersonPath22, KITTI), we demonstrate that our method outperforms existing unsupervised methods with consistent margins on various evaluation metrics, and even achieves performance close to supervised methods.

</details>

### RegionPLC: Regional Point-Language Contrastive Learning for Open-World 3D Scene Understanding. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2304.00962](https://arxiv.org/abs/2304.00962) · 📚 被引 64
- **作者**: Jihan Yang, Runyu Ding, Weipeng Deng, Zhe Wang, Xiaojuan Qi
- **🏷️ 机构**: The University of Hong Kong, SenseTime Research
- **会议**: CVPR 2024
- **摘要（中）**: 针对开放世界3D场景理解中缺乏3D人工标注、难以识别开放集物体和类别的问题，提出了RegionPLC框架。该方法通过3D感知的SFusion策略融合多个2D基础模型生成的视觉-语言对，获得高质量的密集区域级语言描述，并设计区域感知的点判别对比学习目标，实现无需3D标注的开放世界3D学习。相比已有方法，在ScanNet、ScanNet200和nuScenes数据集上，语义分割和实例分割平均提升17.2%和9.1%，且具有更好的可扩展性和更低的资源需求。此外，该方法可无缝集成语言模型，实现开放式的3D接地推理。
- **摘要（英）**: To address the challenge of open-world 3D scene understanding without human 3D annotations, we propose RegionPLC, a lightweight and scalable framework that fuses 3D vision-language pairs from multiple 2D foundation models via a 3D-aware SFusion strategy, generating dense region-level language descriptions. A region-aware point-discriminative contrastive learning objective enables robust 3D learning, outperforming prior methods by 17.2% and 9.1% on semantic and instance segmentation across ScanNet, ScanNet200, and nuScenes, while offering greater scalability and lower resource demands. The method also integrates with language models for open-ended grounded 3D reasoning.
- **核心贡献**: 提出RegionPLC框架，利用2D基础模型和对比学习实现开放世界3D场景理解，显著提升语义和实例分割性能。
- **创新点**: 引入3D感知的SFusion策略和区域感知对比学习，实现高质量密集区域语言描述和无需3D标注的开放集识别。
- **结果**: 在多个数据集上平均提升17.2%和9.1%的语义和实例分割性能，并支持开放式3D推理。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose a lightweight and scalable Regional Point-Language Contrastive learning framework, namely \textbf{RegionPLC}, for open-world 3D scene understanding, aiming to identify and recognize open-set objects and categories. Specifically, based on our empirical studies, we introduce a 3D-aware SFusion strategy that fuses 3D vision-language pairs derived from multiple 2D foundation models, yielding high-quality, dense region-level language descriptions without human 3D annotations. Subsequently, we devise a region-aware point-discriminative contrastive learning objective to enable robust and effective 3D learning from dense regional language supervision. We carry out extensive experiments on ScanNet, ScanNet200, and nuScenes datasets, and our model outperforms prior 3D open-world scene understanding approaches by an average of 17.2\% and 9.1\% for semantic and instance segmentation, respectively, while maintaining greater scalability and lower resource demands. Furthermore, our method has the flexibility to be effortlessly integrated with language models to enable open-ended grounded 3D reasoning without extra task-specific training. Code is available at https://github.com/CVMI-Lab/PLA.

</details>

### Bootstrapping Autonomous Driving Radars with Self-Supervised Learning. **⭐⭐⭐** (相关度: 80%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01422) · 📚 被引 17
- **作者**: Yiduo Hao, Sohrab Madani, Junfeng Guan, Mohammed Alloulah, Saurabh Gupta, Haitham Hassanieh
- **🏷️ 机构**: University of Cambridge, UIUC, EPFL
- **会议**: CVPR 2024
- **摘要（中）**: 该论文针对自动驾驶雷达数据标注成本高、难以利用大量未标注数据的问题，提出了一种基于自监督学习的雷达数据引导方法。通过自监督预训练，模型能够从雷达数据中学习有效的特征表示，从而提升下游任务性能。具体方法可能涉及对比学习或掩码重建等技术，但摘要内容不完整，无法提供详细细节。相比已有工作，该方法专注于雷达模态，填补了自监督学习在自动驾驶雷达领域的空白。实验效果未在摘要中给出具体数据。
- **摘要（英）**: This paper addresses the challenge of high annotation costs and underutilization of unlabeled data in autonomous driving radar perception by proposing a self-supervised learning approach to bootstrap radar data. The method learns effective feature representations from radar data through self-supervised pre-training, potentially using contrastive or reconstruction-based techniques, though details are incomplete in the abstract. It focuses on the radar modality, filling a gap in self-supervised learning for this domain, but specific experimental results are not provided.
- **核心贡献**: 提出自监督学习方法用于自动驾驶雷达数据，提升特征学习效率。
- **创新点**: 将自监督学习应用于雷达模态，解决标注稀缺问题。
- **结果**: 摘要未提供具体性能数据。

### What, When, and Where? Self-Supervised Spatio- Temporal Grounding in Untrimmed Multi-Action Videos from Narrated Instructions. **⭐⭐⭐** (相关度: 40%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01743)
- **作者**: Brian Chen, Nina Shvetsova, Andrew Rouditchenko, Daniel Kondermann, Samuel Thomas, Shih-Fu Chang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024
- **摘要（中）**: ①针对未修剪多动作视频中时空定位的挑战，现有方法依赖密集标注。②提出自监督方法，利用叙述指令作为监督信号，学习视频片段与文本指令的对应关系，实现动作的时空定位。③通过联合建模时间顺序和空间位置，改进了对多动作视频的理解。④在多个基准数据集上验证了方法的有效性，但未提供具体数值。
- **摘要（英）**: This paper tackles spatio-temporal grounding in untrimmed multi-action videos, which typically requires dense annotations. It proposes a self-supervised method that leverages narrated instructions as supervision to learn correspondences between video segments and text, enabling action localization. By jointly modeling temporal order and spatial positions, it improves video understanding, with effectiveness validated on multiple benchmarks.
- **核心贡献**: 提出利用叙述指令进行自监督时空定位的方法。
- **创新点**: 联合建模时间顺序和空间位置，无需密集标注。
- **结果**: 在多个基准上验证了有效性。

### Low-Res Leads the Way: Improving Generalization for Super-Resolution by Self-Supervised Learning. **⭐⭐⭐** (相关度: 30%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02443)
- **作者**: Haoyu Chen, Wenbo Li, Jinjin Gu, Jingjing Ren, Haoze Sun, Xueyi Zou et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024
- **摘要（中）**: ①针对超分辨率模型在低分辨率输入上泛化能力差的问题。②提出自监督学习策略，利用低分辨率图像作为引导，增强模型对未知退化模式的鲁棒性。③通过预训练和微调阶段的自监督任务，改进了超分辨率模型的泛化性能。④在多个超分辨率基准上，该方法在低分辨率测试集上显著提升了PSNR和SSIM。
- **摘要（英）**: This paper addresses poor generalization of super-resolution models on low-resolution inputs. It proposes a self-supervised learning strategy that uses low-resolution images as guidance to enhance robustness to unknown degradation patterns. Through self-supervised tasks in pretraining and fine-tuning, it improves generalization, achieving significant PSNR and SSIM gains on low-resolution test sets.
- **核心贡献**: 提出利用低分辨率图像引导的自监督超分辨率泛化方法。
- **创新点**: 自监督预训练和微调策略增强退化鲁棒性。
- **结果**: 在低分辨率测试集上显著提升PSNR和SSIM。

### Self-Supervised Facial Representation Learning with Facial Region Awareness. **⭐⭐⭐** (相关度: 35%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00203)
- **作者**: Zheng Gao, Ioannis Patras
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024
- **摘要（中）**: ①针对人脸表示学习中缺乏区域感知的问题。②提出区域感知的自监督人脸表示学习方法，通过显式建模面部区域（如眼睛、鼻子）来增强特征判别力。③相比通用自监督方法，该方法利用人脸结构先验，提升了细粒度特征学习。④在多个下游人脸任务上（如识别、属性分析）取得了改进，但未提供具体数值。
- **摘要（英）**: This paper addresses the lack of region awareness in facial representation learning. It proposes a region-aware self-supervised method that explicitly models facial regions (e.g., eyes, nose) to enhance feature discriminability. By leveraging facial structure priors, it improves fine-grained feature learning over generic self-supervised methods, with gains on downstream tasks like recognition and attribute analysis.
- **核心贡献**: 提出区域感知的自监督人脸表示学习方法。
- **创新点**: 显式建模面部区域先验。
- **结果**: 在多个下游人脸任务上取得改进。

### CuVLER: Enhanced Unsupervised Object Discoveries through Exhaustive Self-Supervised Transformers. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02180)
- **作者**: Shahaf Arica, Or Rubin, Sapir Gershov, Shlomi Laufer
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024
- **摘要（中）**: ①针对无监督目标发现中现有方法对目标覆盖不完整的问题。②提出CuVLER，利用自监督Transformer进行穷举式目标发现，通过增强特征提取和候选生成，提高召回率。③相比现有无监督方法，CuVLER在多个数据集上发现了更多且更准确的目标。④在PASCAL VOC和COCO等基准上，CuVLER显著提升了目标发现的准确率和召回率。
- **摘要（英）**: This paper addresses incomplete object coverage in unsupervised object discovery. It proposes CuVLER, which uses self-supervised Transformers for exhaustive discovery by enhancing feature extraction and candidate generation, improving recall. CuVLER finds more accurate objects than existing methods on PASCAL VOC and COCO, with significant gains in precision and recall.
- **核心贡献**: 提出CuVLER，利用自监督Transformer实现穷举式目标发现。
- **创新点**: 增强特征提取和候选生成，提高目标召回率。
- **结果**: 在PASCAL VOC和COCO上显著提升准确率和召回率。

### Prompt Augmentation for Self-supervised Text-guided Image Manipulation. **⭐⭐** (相关度: 20%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00843)
- **作者**: Rumeysa Bodur, Binod Bhattarai, Tae-Kyun Kim
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024
- **摘要（中）**: ①针对文本引导图像编辑中提示词不足导致编辑效果不佳的问题。②提出提示增强方法，通过自监督方式生成更丰富的文本提示，提升编辑的语义一致性。③相比固定提示，该方法动态调整提示，增强了编辑的灵活性和准确性。④在多个图像编辑基准上验证了改进，但未提供具体数值。
- **摘要（英）**: This paper addresses insufficient prompts in text-guided image manipulation. It proposes a prompt augmentation method that generates richer text prompts in a self-supervised manner, improving semantic consistency. Compared to fixed prompts, it dynamically adjusts prompts, enhancing flexibility and accuracy, with improvements on editing benchmarks.
- **核心贡献**: 提出自监督提示增强方法提升文本引导图像编辑。
- **创新点**: 动态生成丰富提示。
- **结果**: 在图像编辑基准上验证了改进。

### Exploring Efficient Asymmetric Blind-Spots for Self-Supervised Denoising in Real-World Scenarios.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00272) · 📚 被引 16
- **作者**: Shiyan Chen, Jiyuan Zhang, Zhaofei Yu, Tiejun Huang
- **🏷️ 机构**: School of Computer Science, Peking University
- **会议**: CVPR 2024

### ShapeMatcher: Self-Supervised Joint Shape Canonicalization, Segmentation, Retrieval and Deformation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01986) · 📚 被引 10
- **作者**: Yan Di, Chenyangguang Zhang, Chaowei Wang, Ruida Zhang, Guangyao Zhai, Yanyan Li et al.
- **🏷️ 机构**: Technical University of Munich, Tsinghua University, Northwestern Polytechnical University
- **会议**: CVPR 2024

### Learning to Predict Activity Progress by Self-Supervised Video Alignment.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01766) · 📚 被引 25
- **作者**: Gerard Donahue, Ehsan Elhamifar
- **🏷️ 机构**: Northeastern University Northeastern University,Boston,MA,USA
- **会议**: CVPR 2024

### Patch2Self2: Self-Supervised Denoising on Coresets via Matrix Sketching.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02610) · 📚 被引 2
- **作者**: Shreyas Fadnavis, Agniva Chowdhury, Joshua Batson, Petros Drineas, Eleftherios Garyfallidis
- **🏷️ 机构**: Johnson and Johnson R&#x0026;D,Cambridge,MA, Oak Ridge National Laboratory,Oak Ridge,TN, Anthropic,San Francisco,CA
- **会议**: CVPR 2024

### SD2Event: Self-Supervised Learning of Dynamic Detectors and Contextual Descriptors for Event Cameras.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00295) · 📚 被引 10
- **作者**: Yuan Gao, Yuqing Zhu, Xinjun Li, Yimin Du, Tianzhu Zhang
- **🏷️ 机构**: University of Science and Technology of China
- **会议**: CVPR 2024

### Separating the "Chirp" from the "Chat": Self-supervised Visual Grounding of Sound and Language.
- **链接**: [arXiv:2406.05629](https://arxiv.org/abs/2406.05629) · 📚 被引 9
- **作者**: Mark Hamilton, Andrew Zisserman, John R. Hershey, William T. Freeman
- **🏷️ 机构**: MIT, Microsoft, Oxford, Google, Google
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present DenseAV, a novel dual encoder grounding architecture that learns high-resolution, semantically meaningful, and audio-visually aligned features solely through watching videos. We show that DenseAV can discover the ``meaning'' of words and the ``location'' of sounds without explicit localization supervision. Furthermore, it automatically discovers and distinguishes between these two types of associations without supervision. We show that DenseAV's localization abilities arise from a new multi-head feature aggregation operator that directly compares dense image and audio representations for contrastive learning. In contrast, many other systems that learn ``global'' audio and video representations cannot localize words and sound. Finally, we contribute two new datasets to improve the evaluation of AV representations through speech and sound prompted semantic segmentation. On these and other datasets we show DenseAV dramatically outperforms the prior art on speech and sound prompted semantic segmentation. DenseAV outperforms the previous state-of-the-art, ImageBind, on cross-modal retrieval using fewer than half of the parameters. Project Page: \href{https://aka.ms/denseav}{https://aka.ms/denseav}

</details>

### An Asymmetric Augmented Self-Supervised Learning Method for Unsupervised Fine-Grained Image Hashing.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01671) · 📚 被引 15
- **作者**: Feiran Hu, Chen-Lin Zhang, Jiangliang Guo, Xiu-Shen Wei, Lin Zhao, Anqi Xu et al.
- **🏷️ 机构**: School of Computer Science and Engineering, Nanjing University of Science and Technology, 4Paradigm Inc., A Innovation Technology Group Co., Ltd
- **会议**: CVPR 2024

### Self-Supervised Representation Learning from Arbitrary Scenarios.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02167) · 📚 被引 5
- **作者**: Zhaowen Li, Yousong Zhu, Zhiyang Chen, Zongxin Gao, Rui Zhao, Chaoyang Zhao et al.
- **🏷️ 机构**: Foundation Model Research Center, Institute of Automation, Chinese Academy of Science1, Independent Researcher, Qing Yuan Research Institute, Shanghai Jiao Tong University
- **会议**: CVPR 2024

### Self-Supervised Debiasing Using Low Rank Regularization.
- **链接**: [arXiv:2210.05248](https://arxiv.org/abs/2210.05248) · 📚 被引 2
- **作者**: Geon Yeong Park, Chanyong Jung, Sangmin Lee, Jong Chul Ye, Sang Wan Lee
- **🏷️ 机构**: Bio and Brain Engineering, Mathematical Sciences
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Spurious correlations can cause strong biases in deep neural networks, impairing generalization ability. While most existing debiasing methods require full supervision on either spurious attributes or target labels, training a debiased model from a limited amount of both annotations is still an open question. To address this issue, we investigate an interesting phenomenon using the spectral analysis of latent representations: spuriously correlated attributes make neural networks inductively biased towards encoding lower effective rank representations. We also show that a rank regularization can amplify this bias in a way that encourages highly correlated features. Leveraging these findings, we propose a self-supervised debiasing framework potentially compatible with unlabeled samples. Specifically, we first pretrain a biased encoder in a self-supervised manner with the rank regularization, serving as a semantic bottleneck to enforce the encoder to learn the spuriously correlated attributes. This biased encoder is then used to discover and upweight bias-conflicting samples in a downstream task, serving as a boosting to effectively debias the main model. Remarkably, the proposed debiasing framework significantly improves the generalization performance of self-supervised learning baselines and, in some cases, even outperforms state-of-the-art supervised debiasing approaches.

</details>

### Parameter Efficient Self-Supervised Geospatial Domain Adaptation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02630) · 📚 被引 21
- **作者**: Linus Scheibenreif, Michael Mommert, Damian Borth
- **🏷️ 机构**: University of St. Gallen,Switzerland
- **会议**: CVPR 2024

### LAFS: Landmark-Based Facial Self-Supervised Learning for Face Recognition.
- **链接**: [arXiv:2403.08161](https://arxiv.org/abs/2403.08161) · 📚 被引 26
- **作者**: Zhonglin Sun, Chen Feng, Ioannis Patras, Georgios Tzimiropoulos
- **🏷️ 机构**: Queen Mary University of London,London,UK
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this work we focus on learning facial representations that can be adapted to train effective face recognition models, particularly in the absence of labels. Firstly, compared with existing labelled face datasets, a vastly larger magnitude of unlabeled faces exists in the real world. We explore the learning strategy of these unlabeled facial images through self-supervised pretraining to transfer generalized face recognition performance. Moreover, motivated by one recent finding, that is, the face saliency area is critical for face recognition, in contrast to utilizing random cropped blocks of images for constructing augmentations in pretraining, we utilize patches localized by extracted facial landmarks. This enables our method - namely LAndmark-based Facial Self-supervised learning LAFS), to learn key representation that is more critical for face recognition. We also incorporate two landmark-specific augmentations which introduce more diversity of landmark information to further regularize the learning. With learned landmark-based facial representations, we further adapt the representation for face recognition with regularization mitigating variations in landmark positions. Our method achieves significant improvement over the state-of-the-art on multiple face recognition benchmarks, especially on more challenging few-shot scenarios.

</details>

### Self-Supervised Dual Contouring.
- **链接**: [arXiv:2405.18131](https://arxiv.org/abs/2405.18131)
- **作者**: Ramana Sundararaman, Roman Klokov, Maks Ovsjanikov
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Learning-based isosurface extraction methods have recently emerged as a robust and efficient alternative to axiomatic techniques. However, the vast majority of such approaches rely on supervised training with axiomatically computed ground truths, thus potentially inheriting biases and data artifacts of the corresponding axiomatic methods. Steering away from such dependencies, we propose a self-supervised training scheme for the Neural Dual Contouring meshing framework, resulting in our method: Self-Supervised Dual Contouring (SDC). Instead of optimizing predicted mesh vertices with supervised training, we use two novel self-supervised loss functions that encourage the consistency between distances to the generated mesh up to the first order. Meshes reconstructed by SDC surpass existing data-driven methods in capturing intricate details while being more robust to possible irregularities in the input. Furthermore, we use the same self-supervised training objective linking inferred mesh and input SDF, to regularize the training process of Deep Implicit Networks (DINs). We demonstrate that the resulting DINs produce higher-quality implicit functions, ultimately leading to more accurate and detail-preserving surfaces compared to prior baselines for different input modalities. Finally, we demonstrate that our self-supervised losses improve meshing performance in the single-view reconstruction task by enabling joint training of predicted SDF and resulting output mesh. We open-source our code at https://github.com/Sentient07/SDC

</details>

### PanoPose: Self-supervised Relative Pose Estimation for Panoramic Images.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01891) · 📚 被引 9
- **作者**: Diantao Tu, Hainan Cui, Xianwei Zheng, Shuhan Shen
- **🏷️ 机构**: Institute of Automation, Chinese Academy of Sciences, Wuhan University,The State Key Lab. LIESMARS
- **会议**: CVPR 2024

### GroupContrast: Semantic-Aware Self-Supervised Representation Learning for 3D Understanding.
- **链接**: [arXiv:2403.09639](https://arxiv.org/abs/2403.09639) · 📚 被引 28
- **作者**: Chengyao Wang, Li Jiang, Xiaoyang Wu, Zhuotao Tian, Bohao Peng, Hengshuang Zhao et al.
- **🏷️ 机构**: CUHK, CUHK(SZ), HKU
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised 3D representation learning aims to learn effective representations from large-scale unlabeled point clouds. Most existing approaches adopt point discrimination as the pretext task, which assigns matched points in two distinct views as positive pairs and unmatched points as negative pairs. However, this approach often results in semantically identical points having dissimilar representations, leading to a high number of false negatives and introducing a "semantic conflict" problem. To address this issue, we propose GroupContrast, a novel approach that combines segment grouping and semantic-aware contrastive learning. Segment grouping partitions points into semantically meaningful regions, which enhances semantic coherence and provides semantic guidance for the subsequent contrastive representation learning. Semantic-aware contrastive learning augments the semantic information extracted from segment grouping and helps to alleviate the issue of "semantic conflict". We conducted extensive experiments on multiple 3D scene understanding tasks. The results demonstrate that GroupContrast learns semantically meaningful representations and achieves promising transfer learning performance.

</details>

### Neural Modes: Self-supervised Learning of Nonlinear Modal Subspaces.
- **链接**: [arXiv:2404.17620](https://arxiv.org/abs/2404.17620) · 📚 被引 6
- **作者**: Jiahong Wang, Yinwei Du, Stelian Coros, Bernhard Thomaszewski
- **🏷️ 机构**: ETH Z&#x00FC;rich
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose a self-supervised approach for learning physics-based subspaces for real-time simulation. Existing learning-based methods construct subspaces by approximating pre-defined simulation data in a purely geometric way. However, this approach tends to produce high-energy configurations, leads to entangled latent space dimensions, and generalizes poorly beyond the training set. To overcome these limitations, we propose a self-supervised approach that directly minimizes the system's mechanical energy during training. We show that our method leads to learned subspaces that reflect physical equilibrium constraints, resolve overfitting issues of previous methods, and offer interpretable latent space parameters.

</details>

### CNC-Net: Self-Supervised Learning for CNC Machining Operations.
- **链接**: [arXiv:2312.09925](https://arxiv.org/abs/2312.09925) · 📚 被引 3
- **作者**: Mohsen Yavartanoo, Sangmin Hong, Reyhaneh Neshatavar, Kyoung Mu Lee
- **🏷️ 机构**: Dept. of ECE &#x0026; ASRI, Seoul National University,IPAI,Seoul,Korea
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> CNC manufacturing is a process that employs computer numerical control (CNC) machines to govern the movements of various industrial tools and machinery, encompassing equipment ranging from grinders and lathes to mills and CNC routers. However, the reliance on manual CNC programming has become a bottleneck, and the requirement for expert knowledge can result in significant costs. Therefore, we introduce a pioneering approach named CNC-Net, representing the use of deep neural networks (DNNs) to simulate CNC machines and grasp intricate operations when supplied with raw materials. CNC-Net constitutes a self-supervised framework that exclusively takes an input 3D model and subsequently generates the essential operation parameters required by the CNC machine to construct the object. Our method has the potential to transformative automation in manufacturing by offering a cost-effective alternative to the high costs of manual CNC programming while maintaining exceptional precision in 3D object production. Our experiments underscore the effectiveness of our CNC-Net in constructing the desired 3D objects through the utilization of CNC operations. Notably, it excels in preserving finer local details, exhibiting a marked enhancement in precision compared to the state-of-the-art 3D CAD reconstruction approaches.

</details>

### ES3: Evolving Self-Supervised Learning of Robust Audio-Visual Speech Representations.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02556) · 📚 被引 8
- **作者**: Yuanhang Zhang, Shuang Yang, Shiguang Shan, Xilin Chen
- **🏷️ 机构**: Institute of Computing Technology, CAS,Key Laboratory of Intelligent Information Processing of Chinese Academy of Sciences (CAS),Beijing,China,100190
- **会议**: CVPR 2024

### Imagine Before Go: Self-Supervised Generative Map for Object Goal Navigation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01553) · 📚 被引 21
- **作者**: Sixian Zhang, Xinyao Yu, Xinhang Song, Xiaohan Wang, Shuqiang Jiang
- **🏷️ 机构**: Institute of Computing Technology,Key Lab of Intelligent Information Processing Laboratory of the Chinese Academy of Sciences (CAS),Beijing
- **会议**: CVPR 2024

### SD-DiT: Unleashing the Power of Self-Supervised Discrimination in Diffusion Transformer*.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00806) · 📚 被引 18
- **作者**: Rui Zhu, Yingwei Pan, Yehao Li, Ting Yao, Zhenglong Sun, Tao Mei et al.
- **🏷️ 机构**: The Chinese University of HongKong,Shenzhen, HiDream.ai Inc, The Hong Kong Polytechnic University
- **会议**: CVPR 2024

### MaskCLR: Attention-Guided Contrastive Learning for Robust Action Representation Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01767) · 📚 被引 23
- **作者**: Mohamed Abdelfattah, Mariam Hassan, Alexandre Alahi
- **🏷️ 机构**: &#x00C9;cole Poly technique F&#x00E9;d&#x00E9;rale de Lausanne (EPFL)
- **会议**: CVPR 2024

### Relaxed Contrastive Learning for Federated Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01167) · 📚 被引 40
- **作者**: Seonguk Seo, Jinkyu Kim, Geeho Kim, Bohyung Han
- **🏷️ 机构**: Seoul National University,ECE
- **会议**: CVPR 2024

### Style Blind Domain Generalized Semantic Segmentation via Covariance Alignment and Semantic Consistence Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00347) · 📚 被引 31
- **作者**: Woo-Jin Ahn, Geun-Yeong Yang, Hyun Duck Choi, Myo-Taeg Lim
- **🏷️ 机构**: Korea University, Chonnam National University
- **会议**: CVPR 2024

### NoiseCLR: A Contrastive Learning Approach for Unsupervised Discovery of Interpretable Directions in Diffusion Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02285) · 📚 被引 18
- **作者**: Yusuf Dalva, Pinar Yanardag
- **🏷️ 机构**: Virginia Tech
- **会议**: CVPR 2024

### Instance-Aware Contrastive Learning for Occluded Human Mesh Reconstruction.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01004) · 📚 被引 4
- **作者**: Mi-Gyeong Gwon, Gi-Mun Um, Won-Sik Cheong, Wonjun Kim
- **🏷️ 机构**: Konkuk University, Electronics and Telecommunications Research Institute
- **会议**: CVPR 2024

### Contrastive Learning for DeepFake Classification and Localization via Multi-Label Ranking.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01669) · 📚 被引 20
- **作者**: Cheng-Yao Hong, Yen-Chi Hsu, Tyng-Luh Liu
- **🏷️ 机构**: Institute of Information Science, Academia Sinica,Taiwan
- **会议**: CVPR 2024

### Enhancing Visual Document Understanding with Contrastive Learning in Large Visual-Language Models.
- **链接**: [arXiv:2402.19014](https://arxiv.org/abs/2402.19014) · 📚 被引 28
- **作者**: Xin Li, Yunfei Wu, Xinghua Jiang, Zhihao Guo, Mingming Gong, Haoyu Cao et al.
- **🏷️ 机构**: Tencent YouTu Lab
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, the advent of Large Visual-Language Models (LVLMs) has received increasing attention across various domains, particularly in the field of visual document understanding (VDU). Different from conventional vision-language tasks, VDU is specifically concerned with text-rich scenarios containing abundant document elements. Nevertheless, the importance of fine-grained features remains largely unexplored within the community of LVLMs, leading to suboptimal performance in text-rich scenarios. In this paper, we abbreviate it as the fine-grained feature collapse issue. With the aim of filling this gap, we propose a contrastive learning framework, termed Document Object COntrastive learning (DoCo), specifically tailored for the downstream tasks of VDU. DoCo leverages an auxiliary multimodal encoder to obtain the features of document objects and align them to the visual features generated by the vision encoder of LVLM, which enhances visual representation in text-rich scenarios. It can represent that the contrastive learning between the visual holistic representations and the multimodal fine-grained features of document objects can assist the vision encoder in acquiring more effective visual cues, thereby enhancing the comprehension of text-rich documents in LVLMs. We also demonstrate that the proposed DoCo serves as a plug-and-play pre-training method, which can be employed in the pre-training of various LVLMs without inducing any increase in computational complexity during the inference process. Extensive experimental results on multiple benchmarks of VDU reveal that LVLMs equipped with our proposed DoCo can achieve superior performance and mitigate the gap between VDU and generic vision-language tasks.

</details>

### Universal Novelty Detection Through Adaptive Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02162) · 📚 被引 10
- **作者**: Hossein Mirzaei, Mojtaba Nafez, Mohammad Jafari, Mohammad Bagher Soltani, Mohammad Azizmalayeri, Jafar Habibi et al.
- **🏷️ 机构**: Sharif University of Technology,Iran, Okinawa Institute of Science and Technology,Japan
- **会议**: CVPR 2024

### Enhancing Post-Training Quantization Calibration Through Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01507) · 📚 被引 13
- **作者**: Yuzhang Shang, Gaowen Liu, Ramana Rao Kompella, Yan Yan
- **🏷️ 机构**: Illinois Institute of Technology, Cisco Research
- **会议**: CVPR 2024

### Contextrast: Contextual Contrastive Learning for Semantic Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00358) · 📚 被引 41
- **作者**: Changki Sung, Wanhee Kim, Jungho An, Wooju Lee, Hyungtae Lim, Hyun Myung
- **🏷️ 机构**: School of Electrical Engineering, KI-Robotics, Korea Advanced Institute of Science and Technology,Republic of Korea, Department of Automotive Engineering Kookmin University,Republic of Korea
- **会议**: CVPR 2024

### OmniSeg3D: Omniversal 3D Segmentation via Hierarchical Contrastive Learning.
- **链接**: [arXiv:2311.11666](https://arxiv.org/abs/2311.11666) · 📚 被引 52
- **作者**: Haiyang Ying, Yixuan Yin, Jinzhi Zhang, Fan Wang, Tao Yu, Ruqi Huang et al.
- **🏷️ 机构**: Tsinghua University, Alibaba Group
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Towards holistic understanding of 3D scenes, a general 3D segmentation method is needed that can segment diverse objects without restrictions on object quantity or categories, while also reflecting the inherent hierarchical structure. To achieve this, we propose OmniSeg3D, an omniversal segmentation method aims for segmenting anything in 3D all at once. The key insight is to lift multi-view inconsistent 2D segmentations into a consistent 3D feature field through a hierarchical contrastive learning framework, which is accomplished by two steps. Firstly, we design a novel hierarchical representation based on category-agnostic 2D segmentations to model the multi-level relationship among pixels. Secondly, image features rendered from the 3D feature field are clustered at different levels, which can be further drawn closer or pushed apart according to the hierarchical relationship between different levels. In tackling the challenges posed by inconsistent 2D segmentations, this framework yields a global consistent 3D feature field, which further enables hierarchical segmentation, multi-object selection, and global discretization. Extensive experiments demonstrate the effectiveness of our method on high-quality 3D segmentation and accurate hierarchical structure understanding. A graphical user interface further facilitates flexible interaction for omniversal 3D segmentation.

</details>

### Data Poisoning Based Backdoor Attacks to Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02299) · 📚 被引 18
- **作者**: Jinghuai Zhang, Hongbin Liu, Jinyuan Jia, Neil Zhenqiang Gong
- **🏷️ 机构**: University of California,Los Angeles, Duke University, Penn State
- **会议**: CVPR 2024

### Improving Graph Contrastive Learning via Adaptive Positive Sampling.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02187) · 📚 被引 9
- **作者**: Jiaming Zhuo, Feiyang Qin, Can Cui, Kun Fu, Bingxin Niu, Mengzhu Wang et al.
- **🏷️ 机构**: School of Artificial Intelligence, Hebei University of Technology,Tianjin,China, School of Computer Science and Engineering, Beihang University,Beijing,China, Institute of Information Engineering Chinese Academy of Sciences,Beijing,China
- **会议**: CVPR 2024

### EfficientSAM: Leveraged Masked Image Pretraining for Efficient Segment Anything.
- **链接**: [arXiv:2312.00863](https://arxiv.org/abs/2312.00863) · 📚 被引 227
- **作者**: Yunyang Xiong, Bala Varadarajan, Lemeng Wu, Xiaoyu Xiang, Fanyi Xiao, Chenchen Zhu et al.
- **🏷️ 机构**: Meta AI Research
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Segment Anything Model (SAM) has emerged as a powerful tool for numerous vision applications. A key component that drives the impressive performance for zero-shot transfer and high versatility is a super large Transformer model trained on the extensive high-quality SA-1B dataset. While beneficial, the huge computation cost of SAM model has limited its applications to wider real-world applications. To address this limitation, we propose EfficientSAMs, light-weight SAM models that exhibits decent performance with largely reduced complexity. Our idea is based on leveraging masked image pretraining, SAMI, which learns to reconstruct features from SAM image encoder for effective visual representation learning. Further, we take SAMI-pretrained light-weight image encoders and mask decoder to build EfficientSAMs, and finetune the models on SA-1B for segment anything task. We perform evaluations on multiple vision tasks including image classification, object detection, instance segmentation, and semantic object detection, and find that our proposed pretraining method, SAMI, consistently outperforms other masked image pretraining methods. On segment anything task such as zero-shot instance segmentation, our EfficientSAMs with SAMI-pretrained lightweight image encoders perform favorably with a significant gain (e.g., ~4 AP on COCO/LVIS) over other fast SAM models.

</details>

### Weak-to-Strong Compositional Learning from Generative Models for Language-Based Object Detection.
- **链接**: [arXiv:2407.15296](https://arxiv.org/abs/2407.15296) · 📚 被引 3
- **作者**: Kwanyong Park, Kuniaki Saito, Donghyun Kim
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-language (VL) models often exhibit a limited understanding of complex expressions of visual objects (e.g., attributes, shapes, and their relations), given complex and diverse language queries. Traditional approaches attempt to improve VL models using hard negative synthetic text, but their effectiveness is limited. In this paper, we harness the exceptional compositional understanding capabilities of generative foundational models. We introduce a novel method for structured synthetic data generation aimed at enhancing the compositional understanding of VL models in language-based object detection. Our framework generates densely paired positive and negative triplets (image, text descriptions, and bounding boxes) in both image and text domains. By leveraging these synthetic triplets, we transform 'weaker' VL models into 'stronger' models in terms of compositional understanding, a process we call "Weak-to-Strong Compositional Learning" (WSCL). To achieve this, we propose a new compositional contrastive learning formulation that discovers semantics and structures in complex descriptions from synthetic triplets. As a result, VL models trained with our synthetic data generation exhibit a significant performance boost in the Omnilabel benchmark by up to +5AP and the D3 benchmark by +6.9AP upon existing baselines.

</details>

### TIP: Tabular-Image Pre-training for Multimodal Classification with Incomplete Data.
- **链接**: [arXiv:2407.07582](https://arxiv.org/abs/2407.07582) · 📚 被引 16
- **作者**: Siyi Du, Shaoming Zheng, Yinsong Wang, Wenjia Bai, Declan P. O'Regan, Chen Qin
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Images and structured tables are essential parts of real-world databases. Though tabular-image representation learning is promising to create new insights, it remains a challenging task, as tabular data is typically heterogeneous and incomplete, presenting significant modality disparities with images. Earlier works have mainly focused on simple modality fusion strategies in complete data scenarios, without considering the missing data issue, and thus are limited in practice. In this paper, we propose TIP, a novel tabular-image pre-training framework for learning multimodal representations robust to incomplete tabular data. Specifically, TIP investigates a novel self-supervised learning (SSL) strategy, including a masked tabular reconstruction task for tackling data missingness, and image-tabular matching and contrastive learning objectives to capture multimodal information. Moreover, TIP proposes a versatile tabular encoder tailored for incomplete, heterogeneous tabular data and a multimodal interaction module for inter-modality representation learning. Experiments are performed on downstream multimodal classification tasks using both natural and medical image datasets. The results show that TIP outperforms state-of-the-art supervised/SSL image/multimodal algorithms in both complete and incomplete data scenarios. Our code is available at https://github.com/siyi-wind/TIP.

</details>

### Missing Modality Prediction for Unpaired Multimodal Learning via Joint Embedding of Unimodal Models.
- **链接**: [arXiv:2407.12616](https://arxiv.org/abs/2407.12616) · 📚 被引 9
- **作者**: Donggeun Kim, Taesup Kim
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal learning typically relies on the assumption that all modalities are fully available during both the training and inference phases. However, in real-world scenarios, consistently acquiring complete multimodal data presents significant challenges due to various factors. This often leads to the issue of missing modalities, where data for certain modalities are absent, posing considerable obstacles not only for the availability of multimodal pretrained models but also for their fine-tuning and the preservation of robustness in downstream tasks. To address these challenges, we propose a novel framework integrating parameter-efficient fine-tuning of unimodal pretrained models with a self-supervised joint-embedding learning method. This framework enables the model to predict the embedding of a missing modality in the representation space during inference. Our method effectively predicts the missing embedding through prompt tuning, leveraging information from available modalities. We evaluate our approach on several multimodal benchmark datasets and demonstrate its effectiveness and robustness across various scenarios of missing modalities.

</details>

### Decoupling Common and Unique Representations for Multimodal Self-supervised Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73397-0_17) · 📚 被引 46
- **作者**: Yi Wang, Conrad M. Albrecht, Nassim Ait Ali Braham, Chenying Liu, Zhitong Xiong, Xiao Xiang Zhu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### SelfSwapper: Self-supervised Face Swapping via Shape Agnostic Masked AutoEncoder.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73001-6_22) · 📚 被引 3
- **作者**: Jaeseong Lee, Junha Hyung, Sohyun Jung, Jaegul Choo
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Exploiting Supervised Poison Vulnerability to Strengthen Self-supervised Defense.
- **链接**: [arXiv:2409.08509](https://arxiv.org/abs/2409.08509)
- **作者**: Jeremy Styborski, Mingzhi Lyu, Yi Huang, Adams Wai-Kin Kong
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Availability poisons exploit supervised learning (SL) algorithms by introducing class-related shortcut features in images such that models trained on poisoned data are useless for real-world datasets. Self-supervised learning (SSL), which utilizes augmentations to learn instance discrimination, is regarded as a strong defense against poisoned data. However, by extending the study of SSL across multiple poisons on the CIFAR-10 and ImageNet-100 datasets, we demonstrate that it often performs poorly, far below that of training on clean data. Leveraging the vulnerability of SL to poison attacks, we introduce adversarial training (AT) on SL to obfuscate poison features and guide robust feature learning for SSL. Our proposed defense, designated VESPR (Vulnerability Exploitation of Supervised Poisoning for Robust SSL), surpasses the performance of six previous defenses across seven popular availability poisons. VESPR displays superior performance over all previous defenses, boosting the minimum and average ImageNet-100 test accuracies of poisoned models by 16% and 9%, respectively. Through analysis and ablation studies, we elucidate the mechanisms by which VESPR learns robust class features.

</details>

### Self-Supervised Audio-Visual Soundscape Stylization.
- **链接**: [arXiv:2409.14340](https://arxiv.org/abs/2409.14340) · 📚 被引 4
- **作者**: Tingle Li, Renhao Wang, Po-Yao Huang, Andrew Owens, Gopala Anumanchipalli
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Speech sounds convey a great deal of information about the scenes, resulting in a variety of effects ranging from reverberation to additional ambient sounds. In this paper, we manipulate input speech to sound as though it was recorded within a different scene, given an audio-visual conditional example recorded from that scene. Our model learns through self-supervision, taking advantage of the fact that natural video contains recurring sound events and textures. We extract an audio clip from a video and apply speech enhancement. We then train a latent diffusion model to recover the original speech, using another audio-visual clip taken from elsewhere in the video as a conditional hint. Through this process, the model learns to transfer the conditional example's sound properties to the input speech. We show that our model can be successfully trained using unlabeled, in-the-wild videos, and that an additional visual signal can improve its sound prediction abilities. Please see our project webpage for video results: https://tinglok.netlify.app/files/avsoundscape/

</details>

### FroSSL: Frobenius Norm Minimization for Efficient Multiview Self-supervised Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73024-5_5) · 📚 被引 3
- **作者**: Oscar Skean, Aayush Dhakal, Nathan Jacobs, Luis Gonzalo Sánchez Giraldo
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### SCPNet: Unsupervised Cross-Modal Homography Estimation via Intra-modal Self-supervised Learning.
- **链接**: [arXiv:2407.08148](https://arxiv.org/abs/2407.08148) · 📚 被引 5
- **作者**: Runmin Zhang, Jun Ma, Si-Yuan Cao, Lun Luo, Beinan Yu, Shu-Jie Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose a novel unsupervised cross-modal homography estimation framework based on intra-modal Self-supervised learning, Correlation, and consistent feature map Projection, namely SCPNet. The concept of intra-modal self-supervised learning is first presented to facilitate the unsupervised cross-modal homography estimation. The correlation-based homography estimation network and the consistent feature map projection are combined to form the learnable architecture of SCPNet, boosting the unsupervised learning framework. SCPNet is the first to achieve effective unsupervised homography estimation on the satellite-map image pair cross-modal dataset, GoogleMap, under [-32,+32] offset on a 128x128 image, leading the supervised approach MHN by 14.0% of mean average corner error (MACE). We further conduct extensive experiments on several cross-modal/spectral and manually-made inconsistent datasets, on which SCPNet achieves the state-of-the-art (SOTA) performance among unsupervised approaches, and owns 49.0%, 25.2%, 36.4%, and 10.7% lower MACEs than the supervised approach MHN. Source code is available at https://github.com/RM-Zhang/SCPNet.

</details>

<!-- COMPLETE v1 papers=99 -->
