# Self-supervised Vision — 2024 Guideline

> 领域: 视觉自监督学习（对比学习、MAE、DINO 系）
> 论文数: 67 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### ViC-MAE: Self-supervised Representation Learning from Images and Video with Contrastive Masked Autoencoders.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73235-5_25) · 📚 被引 10
- **作者**: Jefferson Hernandez, Ruben Villegas, Vicente Ordonez
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### NeRF-MAE: Masked AutoEncoders for Self-supervised 3D Representation Learning for Neural Radiance Fields.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73223-2_24) · 📚 被引 12
- **作者**: Muhammad Zubair Irshad, Sergey Zakharov, Vitor Guizilini, Adrien Gaidon, Zsolt Kira, Rares Ambrus
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### DINO-Tracker: Taming DINO for Self-supervised Point Tracking in a Single Video.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73347-5_21) · 📚 被引 34
- **作者**: Narek Tumanyan, Assaf Singer, Shai Bagon, Tali Dekel
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Ex2Eg-MAE: A Framework for Adaptation of Exocentric Video Masked Autoencoders for Egocentric Social Role Understanding.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72989-8_1) · 📚 被引 3
- **作者**: Minh Tran, Yelin Kim, Che-Chun Su, Cheng-Hao Kuo, Min Sun, Mohammad Soleymani
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Towards Open-World Object-Based Anomaly Detection via Self-Supervised Outlier Synthesis.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73209-6_12) · 📚 被引 6
- **作者**: Brian K. S. Isaac-Medina, Yona Falinie A. Gaus, Neelanjan Bhowmik, Toby P. Breckon
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### GroCo: Ground Constraint for Metric Self-supervised Monocular Depth.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73021-4_4) · 📚 被引 6
- **作者**: Aurélien Cecille, Stefan Duffner, Franck Davoine, Thibault Neveu, Rémi Agier
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### ProDepth: Boosting Self-supervised Multi-frame Monocular Depth with Probabilistic Fusion.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72646-0_12) · 📚 被引 9
- **作者**: Sungmin Woo, Wonjoon Lee, Woo Jin Kim, Dogyoon Lee, Sangyoun Lee
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Walker: Self-supervised Multiple Object Tracking by Walking on Temporal Appearance Graphs.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73242-3_1)
- **作者**: Mattia Segù, Luigi Piccinelli, Siyuan Li, Luc Van Gool, Fisher Yu, Bernt Schiele
- **🏷️ 机构**: ETH Zurich
- **会议**: ECCV 2024

### SelfSwapper: Self-supervised Face Swapping via Shape Agnostic Masked AutoEncoder.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73001-6_22) · 📚 被引 3
- **作者**: Jaeseong Lee, Junha Hyung, Sohyun Jung, Jaegul Choo
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Exploiting Supervised Poison Vulnerability to Strengthen Self-supervised Defense.
- **链接**: [arXiv:2409.08509](https://arxiv.org/abs/2409.08509) · 📚 被引 0
- **作者**: Jeremy Styborski, Mingzhi Lyu, Yi Huang, Adams Wai-Kin Kong
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

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

### OmniSat: Self-supervised Modality Fusion for Earth Observation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73390-1_24) · 📚 被引 41
- **作者**: Guillaume Astruc, Nicolas Gonthier, Clément Mallet, Loïc Landrieu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Self-supervised Visual Learning from Interactions with Objects.
- **链接**: [arXiv:2407.06704](https://arxiv.org/abs/2407.06704)
- **作者**: Arthur Aubret, Céline Teulière, Jochen Triesch
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning (SSL) has revolutionized visual representation learning, but has not achieved the robustness of human vision. A reason for this could be that SSL does not leverage all the data available to humans during learning. When learning about an object, humans often purposefully turn or move around objects and research suggests that these interactions can substantially enhance their learning. Here we explore whether such object-related actions can boost SSL. For this, we extract the actions performed to change from one ego-centric view of an object to another in four video datasets. We then introduce a new loss function to learn visual and action embeddings by aligning the performed action with the representations of two images extracted from the same clip. This permits the performed actions to structure the latent visual representation. Our experiments show that our method consistently outperforms previous methods on downstream category recognition. In our analysis, we find that the observed improvement is associated with a better viewpoint-wise alignment of different objects from the same category. Overall, our work demonstrates that embodied interactions with objects can improve SSL of object categories.

</details>

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

### Self-Supervised Underwater Caustics Removal and Descattering via Deep Monocular SLAM.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72907-2_13) · 📚 被引 3
- **作者**: Jonathan Sauder, Devis Tuia
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Learning Representation for Multitask Learning Through Self-supervised Auxiliary Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72989-8_14) · 📚 被引 2
- **作者**: Seokwon Shin, Hyungrok Do, Youngdoo Son
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Self-supervised Any-Point Tracking by Contrastive Random Walks.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72630-9_16) · 📚 被引 3
- **作者**: Ayush Shrivastava, Andrew Owens
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

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

### SAH-SCI: Self-supervised Adapter for Efficient Hyperspectral Snapshot Compressive Imaging.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73039-9_18) · 📚 被引 2
- **作者**: Haijin Zeng, Yuxi Liu, Yongyong Chen, Youfa Liu, Chong Peng, Jingyong Su
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

### Contrastive Learning with Counterfactual Explanations for Radiology Report Generation.
- **链接**: [arXiv:2407.14474](https://arxiv.org/abs/2407.14474) · 📚 被引 21
- **作者**: Mingjie Li, Haokun Lin, Liang Qiu, Xiaodan Liang, Ling Chen, Abdulmotaleb Elsaddik et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Due to the common content of anatomy, radiology images with their corresponding reports exhibit high similarity. Such inherent data bias can predispose automatic report generation models to learn entangled and spurious representations resulting in misdiagnostic reports. To tackle these, we propose a novel \textbf{Co}unter\textbf{F}actual \textbf{E}xplanations-based framework (CoFE) for radiology report generation. Counterfactual explanations serve as a potent tool for understanding how decisions made by algorithms can be changed by asking ``what if'' scenarios. By leveraging this concept, CoFE can learn non-spurious visual representations by contrasting the representations between factual and counterfactual images. Specifically, we derive counterfactual images by swapping a patch between positive and negative samples until a predicted diagnosis shift occurs. Here, positive and negative samples are the most semantically similar but have different diagnosis labels. Additionally, CoFE employs a learnable prompt to efficiently fine-tune the pre-trained large language model, encapsulating both factual and counterfactual content to provide a more generalizable prompt representation. Extensive experiments on two benchmarks demonstrate that leveraging the counterfactual explanations enables CoFE to generate semantically coherent and factually complete reports and outperform in terms of language generation and clinical efficacy metrics.

</details>

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

### TTT-MIM: Test-Time Training with Masked Image Modeling for Denoising Distribution Shifts.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73254-6_20) · 📚 被引 9
- **作者**: Youssef Mansour, Xuyang Zhong, Serdar I. Caglar, Reinhard Heckel
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Leveraging Text Localization for Scene Text Removal via Text-Aware Masked Image Modeling.
- **链接**: [arXiv:2409.13431](https://arxiv.org/abs/2409.13431) · [代码](https://github.com/wzx99/TMIM) · 📚 被引 2
- **作者**: Zixiao Wang, Hongtao Xie, Yuxin Wang, Yadong Qu, Fengjun Guo, Pengwei Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing scene text removal (STR) task suffers from insufficient training data due to the expensive pixel-level labeling. In this paper, we aim to address this issue by introducing a Text-aware Masked Image Modeling algorithm (TMIM), which can pretrain STR models with low-cost text detection labels (e.g., text bounding box). Different from previous pretraining methods that use indirect auxiliary tasks only to enhance the implicit feature extraction ability, our TMIM first enables the STR task to be directly trained in a weakly supervised manner, which explores the STR knowledge explicitly and efficiently. In TMIM, first, a Background Modeling stream is built to learn background generation rules by recovering the masked non-text region. Meanwhile, it provides pseudo STR labels on the masked text region. Second, a Text Erasing stream is proposed to learn from the pseudo labels and equip the model with end-to-end STR ability. Benefiting from the two collaborative streams, our STR model can achieve impressive performance only with the public text detection datasets, which greatly alleviates the limitation of the high-cost STR labels. Experiments demonstrate that our method outperforms other pretrain methods and achieves state-of-the-art performance (37.35 PSNR on SCUT-EnsText). Code will be available at https://github.com/wzx99/TMIM.

</details>

## 跨领域论文（完整笔记在其他领域）

- Grounding DINO: Marrying DINO with Grounded Pre-training for Open-Set Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- CLIP-DINOiser: Teaching CLIP a Few DINO Tricks for Open-Vocabulary Semantic Segmentation. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- LISO: Lidar-Only Self-supervised 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- Self-supervised Co-salient Object Detection via Feature Correspondences at Multiple Scales. → [object-detection](../object-detection/Guideline%202024.md)
- M2Depth: Self-supervised Two-Frame Multi-camera Metric Depth Estimation. → [multi-camera-perception](../multi-camera-perception/Guideline%202024.md)
- High-Precision Self-supervised Monocular Depth Estimation with Rich-Resource Prior. → [multi-camera-perception](../multi-camera-perception/Guideline%202024.md)
- Mono-ViFI: A Unified Learning Framework for Self-supervised Single and Multi-frame Monocular Depth Estimation. → [multi-camera-perception](../multi-camera-perception/Guideline%202024.md)
- Improving Domain Generalization in Self-supervised Monocular Depth Estimation via Stabilized Adversarial Training. → [multi-camera-perception](../multi-camera-perception/Guideline%202024.md)
- SeFlow: A Self-supervised Scene Flow Method in Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202024.md)
- Decoupling Common and Unique Representations for Multimodal Self-supervised Learning. → [multimodal](../multimodal/Guideline%202024.md)
- Self-Supervised Audio-Visual Soundscape Stylization. → [multimodal](../multimodal/Guideline%202024.md)
- FroSSL: Frobenius Norm Minimization for Efficient Multiview Self-supervised Learning. → [multi-camera-perception](../multi-camera-perception/Guideline%202024.md)
- SCPNet: Unsupervised Cross-Modal Homography Estimation via Intra-modal Self-supervised Learning. → [multimodal](../multimodal/Guideline%202024.md)
- Revisit Self-supervised Depth Estimation with Local Structure-from-Motion. → [multi-camera-perception](../multi-camera-perception/Guideline%202024.md)
- Improving Medical Multi-modal Contrastive Learning with Expert Annotations. → [multimodal](../multimodal/Guideline%202024.md)
