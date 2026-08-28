# 3D Detection — 2023 Guideline

> 领域: 3D 目标检测（LiDAR / 相机 / 多模态融合）
> 论文数: 35 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Omni3D: A Large Benchmark and Model for 3D Object Detection in the Wild.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01264) · 📚 被引 106
- **作者**: Garrick Brazil, Abhinav Kumar, Julian Straub, Nikhila Ravi, Justin Johnson, Georgia Gkioxari
- **🏷️ 机构**: Meta AI, Michigan State University, Caltech
- **会议**: CVPR 2023

### ConQueR: Query Contrast Voxel-DETR for 3D Object Detection.
- **链接**: [arXiv:2212.07289](https://arxiv.org/abs/2212.07289) · 📚 被引 30
- **作者**: Benjin Zhu, Zhe Wang, Shaoshuai Shi, Hang Xu, Lanqing Hong, Hongsheng Li
- **🏷️ 机构**: The Chinese University of Hong Kong,Multimedia Laboratory, Max Planck Institute for Informatics, Huawei Noah&#x0027;s Ark Lab
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Although DETR-based 3D detectors can simplify the detection pipeline and achieve direct sparse predictions, their performance still lags behind dense detectors with post-processing for 3D object detection from point clouds. DETRs usually adopt a larger number of queries than GTs (e.g., 300 queries v.s. 40 objects in Waymo) in a scene, which inevitably incur many false positives during inference. In this paper, we propose a simple yet effective sparse 3D detector, named Query Contrast Voxel-DETR (ConQueR), to eliminate the challenging false positives, and achieve more accurate and sparser predictions. We observe that most false positives are highly overlapping in local regions, caused by the lack of explicit supervision to discriminate locally similar queries. We thus propose a Query Contrast mechanism to explicitly enhance queries towards their best-matched GTs over all unmatched query predictions. This is achieved by the construction of positive and negative GT-query pairs for each GT, and a contrastive loss to enhance positive GT-query pairs against negative ones based on feature similarities. ConQueR closes the gap of sparse and dense 3D detectors, and reduces up to ~60% false positives. Our single-frame ConQueR achieves new state-of-the-art (sota) 71.6 mAPH/L2 on the challenging Waymo Open Dataset validation set, outperforming previous sota methods (e.g., PV-RCNN++) by over 2.0 mAPH/L2.

</details>

### AShapeFormer : Semantics-Guided Object-Level Active Shape Encoding for 3D Object Detection via Transformers.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00104) · 📚 被引 19
- **作者**: Zechuan Li, Hongshan Yu, Zhengeng Yang, Tom Tongjia Chen, Naveed Akhtar
- **🏷️ 机构**: Hunan University, The University of Western Australia
- **会议**: CVPR 2023

### Viewpoint Equivariance for Multi-View 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00889)
- **作者**: Dian Chen, Jie Li, Vitor Guizilini, Rares Ambrus, Adrien Gaidon
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### VoxelNeXt: Fully Sparse VoxelNet for 3D Object Detection and Tracking.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02076) · 📚 被引 449
- **作者**: Yukang Chen, Jianhui Liu, Xiangyu Zhang, Xiaojuan Qi, Jiaya Jia
- **🏷️ 机构**: The Chinese University of Hong Kong, The University of Hong Kong, MEGVII
- **会议**: CVPR 2023

### PiMAE: Point Cloud and Image Interactive Masked Autoencoders for 3D Object Detection.
- **链接**: [arXiv:2303.08129](https://arxiv.org/abs/2303.08129) · [代码](https://github.com/BLVLab/PiMAE) · 📚 被引 78
- **作者**: Anthony Chen, Kevin Zhang, Renrui Zhang, Zihan Wang, Yuheng Lu, Yandong Guo et al.
- **🏷️ 机构**: School of Computer Science, Peking University,National Key Laboratory for Multimedia Information Processing, The Chinese University of Hong Kong, Beijing University of Posts and Telecommunications
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Masked Autoencoders learn strong visual representations and achieve state-of-the-art results in several independent modalities, yet very few works have addressed their capabilities in multi-modality settings. In this work, we focus on point cloud and RGB image data, two modalities that are often presented together in the real world, and explore their meaningful interactions. To improve upon the cross-modal synergy in existing works, we propose PiMAE, a self-supervised pre-training framework that promotes 3D and 2D interaction through three aspects. Specifically, we first notice the importance of masking strategies between the two sources and utilize a projection module to complementarily align the mask and visible tokens of the two modalities. Then, we utilize a well-crafted two-branch MAE pipeline with a novel shared decoder to promote cross-modality interaction in the mask tokens. Finally, we design a unique cross-modal reconstruction module to enhance representation learning for both modalities. Through extensive experiments performed on large-scale RGB-D scene understanding benchmarks (SUN RGB-D and ScannetV2), we discover it is nontrivial to interactively learn point-image features, where we greatly improve multiple 3D detectors, 2D detectors, and few-shot classifiers by 2.9%, 6.7%, and 2.4%, respectively. Code is available at https://github.com/BLVLab/PiMAE.

</details>

### BEV-SAN: Accurate BEV 3D Object Detection via Slice Attention Networks.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01675)
- **作者**: Xiaowei Chi, Jiaming Liu, Ming Lu, Rongyu Zhang, Zhaoqing Wang, Yandong Guo et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### Object as Query: Lifting any 2D Object Detector to 3D Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00351) · 📚 被引 47
- **作者**: Zitian Wang, Zehao Huang, Jiahui Fu, Naiyan Wang, Si Liu
- **🏷️ 机构**: Institute of Artificial Intelligence, Beihang University, TuSimple
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Point-cloud based 3D object detectors recently have achieved remarkable progress. However, most studies are limited to the development of network architectures for improving only their accuracy without consideration of the computational efficiency. In this paper, we first propose an autoencoder-style framework comprising channel-wise compression and decompression via interchange transfer-based knowledge distillation. To learn the map-view feature of a teacher network, the features from teacher and student networks are independently passed through the shared autoencoder; here, we use a compressed representation loss that binds the channel-wised compression knowledge from both student and teacher networks as a kind of regularization. The decompressed features are transferred in opposite directions to reduce the gap in the interchange reconstructions. Lastly, we present an head attention loss to match the 3D object detection information drawn by the multi-head self-attention mechanism. Through extensive experiments, we verify that our method can train the lightweight model that is well-aligned with the 3D point cloud detection task and we demonstrate its superiority using the well-known public datasets; e.g., Waymo and nuScenes.

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Balancing efficiency and accuracy is a long-standing problem for deploying deep learning models. The trade-off is even more important for real-time safety-critical systems like autonomous vehicles. In this paper, we propose an effective approach for accelerating transformer-based 3D object detectors by dynamically halting tokens at different layers depending on their contribution to the detection task. Although halting a token is a non-differentiable operation, our method allows for differentiable end-to-end learning by leveraging an equivalent differentiable forward-pass. Furthermore, our framework allows halted tokens to be reused to inform the model's predictions through a straightforward token recycling mechanism. Our method significantly improves the Pareto frontier of efficiency versus accuracy when compared with the existing approaches. By halting tokens and increasing model capacity, we are able to improve the baseline model's performance without increasing the model's latency on the Waymo Open Dataset.

</details>

### DistillBEV: Boosting Multi-Camera 3D Object Detection with Cross-Modal Knowledge Distillation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00793)
- **作者**: Zeyu Wang, Dingwen Li, Chenxu Luo, Cihang Xie, Xiaodong Yang
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### Revisiting Domain-Adaptive 3D Object Detection by Reliable, Diverse and Class-balanced Pseudo-Labeling.
- **链接**: [arXiv:2307.07944](https://arxiv.org/abs/2307.07944) · [代码](https://github.com/zhuoxiao-chen/ReDB-DA-3Ddet) · 📚 被引 26
- **作者**: Zhuoxiao Chen, Yadan Luo, Zheng Wang, Mahsa Baktashmotlagh, Zi Huang
- **🏷️ 机构**: The University of Queensland, University of Electronic Science and Technology of China
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Unsupervised domain adaptation (DA) with the aid of pseudo labeling techniques has emerged as a crucial approach for domain-adaptive 3D object detection. While effective, existing DA methods suffer from a substantial drop in performance when applied to a multi-class training setting, due to the co-existence of low-quality pseudo labels and class imbalance issues. In this paper, we address this challenge by proposing a novel ReDB framework tailored for learning to detect all classes at once. Our approach produces Reliable, Diverse, and class-Balanced pseudo 3D boxes to iteratively guide the self-training on a distributionally different target domain. To alleviate disruptions caused by the environmental discrepancy (e.g., beam numbers), the proposed cross-domain examination (CDE) assesses the correctness of pseudo labels by copy-pasting target instances into a source environment and measuring the prediction consistency. To reduce computational overhead and mitigate the object shift (e.g., scales and point densities), we design an overlapped boxes counting (OBC) metric that allows to uniformly downsample pseudo-labeled objects across different geometric characteristics. To confront the issue of inter-class imbalance, we progressively augment the target point clouds with a class-balanced set of pseudo-labeled target instances and source objects, which boosts recognition accuracies on both frequently appearing and rare classes. Experimental results on three benchmark datasets using both voxel-based (i.e., SECOND) and point-based 3D detectors (i.e., PointRCNN) demonstrate that our proposed ReDB approach outperforms existing 3D domain adaptation methods by a large margin, improving 23.15% mAP on the nuScenes $\rightarrow$ KITTI task. The code is available at https://github.com/zhuoxiao-chen/ReDB-DA-3Ddet.

</details>

### Learning with Noisy Data for Semi-Supervised 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00638) · 📚 被引 15
- **作者**: Zehui Chen, Zhenyu Li, Shuo Wang, Dengpan Fu, Feng Zhao
- **🏷️ 机构**: University of Science and Technology of China, Harbin Institute of Technology, NIO
- **会议**: ICCV 2023

### FocalFormer3D : Focusing on Hard Instance for 3D Object Detection.
- **链接**: [arXiv:2308.04556](https://arxiv.org/abs/2308.04556) · [代码](https://github.com/NVlabs/FocalFormer3D) · 📚 被引 112
- **作者**: Yilun Chen, Zhiding Yu, Yukang Chen, Shiyi Lan, Anima Anandkumar, Jiaya Jia et al.
- **🏷️ 机构**: The Chinese University of Hong Kong, NVIDIA, Caltech
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> False negatives (FN) in 3D object detection, {\em e.g.}, missing predictions of pedestrians, vehicles, or other obstacles, can lead to potentially dangerous situations in autonomous driving. While being fatal, this issue is understudied in many current 3D detection methods. In this work, we propose Hard Instance Probing (HIP), a general pipeline that identifies \textit{FN} in a multi-stage manner and guides the models to focus on excavating difficult instances. For 3D object detection, we instantiate this method as FocalFormer3D, a simple yet effective detector that excels at excavating difficult objects and improving prediction recall. FocalFormer3D features a multi-stage query generation to discover hard objects and a box-level transformer decoder to efficiently distinguish objects from massive object candidates. Experimental results on the nuScenes and Waymo datasets validate the superior performance of FocalFormer3D. The advantage leads to strong performance on both detection and tracking, in both LiDAR and multi-modal settings. Notably, FocalFormer3D achieves a 70.5 mAP and 73.9 NDS on nuScenes detection benchmark, while the nuScenes tracking benchmark shows 72.1 AMOTA, both ranking 1st place on the nuScenes LiDAR leaderboard. Our code is available at \url{https://github.com/NVlabs/FocalFormer3D}.

</details>

### Once Detected, Never Lost: Surpassing Human Performance in Offline LiDAR based 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01815) · 📚 被引 28
- **作者**: Lue Fan, Yuxue Yang, Yiming Mao, Feng Wang, Yuntao Chen, Naiyan Wang et al.
- **🏷️ 机构**: Chinese Academy of Sciences,Institute of Automation, Hunan University, TuSimple
- **会议**: ICCV 2023

### A Fast Unified System for 3D Object Detection and Tracking.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01563) · 📚 被引 3
- **作者**: Thomas Heitzinger, Martin Kampel
- **🏷️ 机构**: TU Wien,Computer Vision Lab,Vienna,Austria
- **会议**: ICCV 2023

### UpCycling: Semi-supervised 3D Object Detection without Sharing Raw-level Unlabeled Scenes.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.02134) · 📚 被引 4
- **作者**: Sunwook Hwang, Youngseok Kim, Seongwon Kim, Saewoong Bahk, Hyung-Sin Kim
- **🏷️ 机构**: Seoul National University,Department of Electrical and Computer Engineering, SK Telecom,Seoul,Korea, Seoul National University,Graduate School of Data Science
- **会议**: ICCV 2023

### Predict to Detect: Prediction-guided 3D Object Detection using Sequential Images.
- **链接**: [arXiv:2306.08528](https://arxiv.org/abs/2306.08528) · 📚 被引 13
- **作者**: Sanmin Kim, Youngseok Kim, In-Jae Lee, Dongsuk Kum
- **🏷️ 机构**: KAIST
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent camera-based 3D object detection methods have introduced sequential frames to improve the detection performance hoping that multiple frames would mitigate the large depth estimation error. Despite improved detection performance, prior works rely on naive fusion methods (e.g., concatenation) or are limited to static scenes (e.g., temporal stereo), neglecting the importance of the motion cue of objects. These approaches do not fully exploit the potential of sequential images and show limited performance improvements. To address this limitation, we propose a novel 3D object detection model, P2D (Predict to Detect), that integrates a prediction scheme into a detection framework to explicitly extract and leverage motion features. P2D predicts object information in the current frame using solely past frames to learn temporal motion features. We then introduce a novel temporal feature aggregation method that attentively exploits Bird's-Eye-View (BEV) features based on predicted object information, resulting in accurate 3D object detection. Experimental results demonstrate that P2D improves mAP and NDS by 3.0% and 3.7% compared to the sequential image-based baseline, illustrating that incorporating a prediction scheme can significantly improve detection accuracy.

</details>

### PG-RCNN: Semantic Surface Point Generation for 3D Object Detection.
- **链接**: [arXiv:2307.12637](https://arxiv.org/abs/2307.12637) · [代码](https://github.com/quotation2520/PG-RCNN) · 📚 被引 49
- **作者**: Inyong Koo, Inyoung Lee, Se-Ho Kim, Hee-Seon Kim, Woo-Jin Jeon, Changick Kim
- **🏷️ 机构**: KAIST Daejeon,South Korea
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> One of the main challenges in LiDAR-based 3D object detection is that the sensors often fail to capture the complete spatial information about the objects due to long distance and occlusion. Two-stage detectors with point cloud completion approaches tackle this problem by adding more points to the regions of interest (RoIs) with a pre-trained network. However, these methods generate dense point clouds of objects for all region proposals, assuming that objects always exist in the RoIs. This leads to the indiscriminate point generation for incorrect proposals as well. Motivated by this, we propose Point Generation R-CNN (PG-RCNN), a novel end-to-end detector that generates semantic surface points of foreground objects for accurate detection. Our method uses a jointly trained RoI point generation module to process the contextual information of RoIs and estimate the complete shape and displacement of foreground objects. For every generated point, PG-RCNN assigns a semantic feature that indicates the estimated foreground probability. Extensive experiments show that the point clouds generated by our method provide geometrically and semantically rich information for refining false positive and misaligned proposals. PG-RCNN achieves competitive performance on the KITTI benchmark, with significantly fewer parameters than state-of-the-art models. The code is available at https://github.com/quotation2520/PG-RCNN.

</details>

### GPA-3D: Geometry-aware Prototype Alignment for Unsupervised Domain Adaptive 3D Object Detection from Point Clouds.
- **链接**: [arXiv:2308.08140](https://arxiv.org/abs/2308.08140) · [代码](https://github.com/Liz66666/GPA3D) · 📚 被引 14
- **作者**: Ziyu Li, Jingming Guo, Tongtong Cao, Bingbing Liu, Wankou Yang
- **🏷️ 机构**: School of Automation, Southeast University, Huawei Noah&#x2019;s Ark Lab
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> LiDAR-based 3D detection has made great progress in recent years. However, the performance of 3D detectors is considerably limited when deployed in unseen environments, owing to the severe domain gap problem. Existing domain adaptive 3D detection methods do not adequately consider the problem of the distributional discrepancy in feature space, thereby hindering generalization of detectors across domains. In this work, we propose a novel unsupervised domain adaptive \textbf{3D} detection framework, namely \textbf{G}eometry-aware \textbf{P}rototype \textbf{A}lignment (\textbf{GPA-3D}), which explicitly leverages the intrinsic geometric relationship from point cloud objects to reduce the feature discrepancy, thus facilitating cross-domain transferring. Specifically, GPA-3D assigns a series of tailored and learnable prototypes to point cloud objects with distinct geometric structures. Each prototype aligns BEV (bird's-eye-view) features derived from corresponding point cloud objects on source and target domains, reducing the distributional discrepancy and achieving better adaptation. The evaluation results obtained on various benchmarks, including Waymo, nuScenes and KITTI, demonstrate the superiority of our GPA-3D over the state-of-the-art approaches for different adaptation scenarios. The MindSpore version code will be publicly available at \url{https://github.com/Liz66666/GPA3D}.

</details>

### Representation Disparity-aware Distillation for 3D Object Detection.
- **链接**: [arXiv:2308.10308](https://arxiv.org/abs/2308.10308) · 📚 被引 7
- **作者**: Yanjing Li, Sheng Xu, Mingbao Lin, Jihao Yin, Baochang Zhang, Xianbin Cao
- **🏷️ 机构**: Beihang University, Tencent
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we focus on developing knowledge distillation (KD) for compact 3D detectors. We observe that off-the-shelf KD methods manifest their efficacy only when the teacher model and student counterpart share similar intermediate feature representations. This might explain why they are less effective in building extreme-compact 3D detectors where significant representation disparity arises due primarily to the intrinsic sparsity and irregularity in 3D point clouds. This paper presents a novel representation disparity-aware distillation (RDD) method to address the representation disparity issue and reduce performance gap between compact students and over-parameterized teachers. This is accomplished by building our RDD from an innovative perspective of information bottleneck (IB), which can effectively minimize the disparity of proposal region pairs from student and teacher in features and logits. Extensive experiments are performed to demonstrate the superiority of our RDD over existing KD methods. For example, our RDD increases mAP of CP-Voxel-S to 57.1% on nuScenes dataset, which even surpasses teacher performance while taking up only 42% FLOPs.

</details>

### SparseBEV: High-Performance Sparse 3D Object Detection from Multi-Camera Videos.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01703)
- **作者**: Haisong Liu, Yao Teng, Tao Lu, Haiguang Wang, Limin Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### Monocular 3D Object Detection with Bounding Box Denoising in 3D by Perceiver.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00592) · 📚 被引 16
- **作者**: Xianpeng Liu, Ce Zheng, Kelvin Cheng, Nan Xue, Guo-Jun Qi, Tianfu Wu
- **🏷️ 机构**: North Carolina State University, University of Central Florida, Ant Group
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Point cloud sequences are commonly used to accurately detect 3D objects in applications such as autonomous driving. Current top-performing multi-frame detectors mostly follow a Detect-and-Fuse framework, which extracts features from each frame of the sequence and fuses them to detect the objects in the current frame. However, this inevitably leads to redundant computation since adjacent frames are highly correlated. In this paper, we propose an efficient Motion-guided Sequential Fusion (MSF) method, which exploits the continuity of object motion to mine useful sequential contexts for object detection in the current frame. We first generate 3D proposals on the current frame and propagate them to preceding frames based on the estimated velocities. The points-of-interest are then pooled from the sequence and encoded as proposal features. A novel Bidirectional Feature Aggregation (BiFA) module is further proposed to facilitate the interactions of proposal features across frames. Besides, we optimize the point cloud pooling by a voxel-based sampling technique so that millions of points can be processed in several milliseconds. The proposed MSF method achieves not only better efficiency than other multi-frame detectors but also leading accuracy, with 83.12% and 78.30% mAP on the LEVEL1 and LEVEL2 test sets of Waymo Open Dataset, respectively. Codes can be found at \url{https://github.com/skyhehe123/MSF}.

</details>

> Achieving a reliable LiDAR-based object detector in autonomous driving is paramount, but its success hinges on obtaining large amounts of precise 3D annotations. Active learning (AL) seeks to mitigate the annotation burden through algorithms that use fewer labels and can attain performance comparable to fully supervised learning. Although AL has shown promise, current approaches prioritize the selection of unlabeled point clouds with high uncertainty and/or diversity, leading to the selection of more instances for labeling and reduced computational efficiency. In this paper, we resort to a novel kernel coding rate maximization (KECOR) strategy which aims to identify the most informative point clouds to acquire labels through the lens of information theory. Greedy search is applied to seek desired point clouds that can maximize the minimal number of bits required to encode the latent features. To determine the uniqueness and informativeness of the selected samples from the model perspective, we construct a proxy network of the 3D detector head and compute the outer product of Jacobians from all proxy layers to form the empirical neural tangent kernel (NTK) matrix. To accommodate both one-stage (i.e., SECOND) and two-stage detectors (i.e., PVRCNN), we further incorporate the classification entropy maximization and well trade-off between detection performance and the total number of bounding boxes selected for annotation. Extensive experiments conducted on two 3D benchmarks and a 2D detection dataset evidence the superiority and versatility of the proposed approach. Our results show that approximately 44% box-level annotation costs and 26% computational time are reduced compared to the state-of-the-art AL method, without compromising detection performance.

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Fusing LiDAR and camera information is essential for achieving accurate and reliable 3D object detection in autonomous driving systems. This is challenging due to the difficulty of combining multi-granularity geometric and semantic features from two drastically different modalities. Recent approaches aim at exploring the semantic densities of camera features through lifting points in 2D camera images (referred to as seeds) into 3D space, and then incorporate 2D semantics via cross-modal interaction or fusion techniques. However, depth information is under-investigated in these approaches when lifting points into 3D space, thus 2D semantics can not be reliably fused with 3D points. Moreover, their multi-modal fusion strategy, which is implemented as concatenation or attention, either can not effectively fuse 2D and 3D information or is unable to perform fine-grained interactions in the voxel space. To this end, we propose a novel framework with better utilization of the depth information and fine-grained cross-modal interaction between LiDAR and camera, which consists of two important components. First, a Multi-Depth Unprojection (MDU) method with depth-aware designs is used to enhance the depth quality of the lifted points at each interaction level. Second, a Gated Modality-Aware Convolution (GMA-Conv) block is applied to modulate voxels involved with the camera modality in a fine-grained manner and then aggregate multi-modal features into a unified space. Together they provide the detection head with more comprehensive features from LiDAR and camera. On the nuScenes test benchmark, our proposed method, abbreviated as MSMDFusion, achieves state-of-the-art 3D object detection results with 71.5% mAP and 74.0% NDS, and strong tracking results with 74.0% AMOTA without using test-time-augmentation and ensemble techniques. The code is available at https://github.com/SxJyJay/MSMDFusion.

</details>

> In this work, we build a modular-designed codebase, formulate strong training recipes, design an error diagnosis toolbox, and discuss current methods for image-based 3D object detection. In particular, different from other highly mature tasks, e.g., 2D object detection, the community of image-based 3D object detection is still evolving, where methods often adopt different training recipes and tricks resulting in unfair evaluations and comparisons. What is worse, these tricks may overwhelm their proposed designs in performance, even leading to wrong conclusions. To address this issue, we build a module-designed codebase and formulate unified training standards for the community. Furthermore, we also design an error diagnosis toolbox to measure the detailed characterization of detection models. Using these tools, we analyze current methods in-depth under varying settings and provide discussions for some open questions, e.g., discrepancies in conclusions on KITTI-3D and nuScenes datasets, which have led to different dominant methods for these datasets. We hope that this work will facilitate future research in image-based 3D object detection. Our codes will be released at \url{https://github.com/OpenGVLab/3dodi}

</details>

### DetZero: Rethinking Offboard 3D Object Detection with Long-term Sequential Point Clouds.
- **链接**: [arXiv:2306.06023](https://arxiv.org/abs/2306.06023) · 📚 被引 42
- **作者**: Tao Ma, Xuemeng Yang, Hongbin Zhou, Xin Li, Botian Shi, Junjie Liu et al.
- **🏷️ 机构**: The Chinese University of Hong Kong,Multimedia Laboratory, Shanghai Artificial Intelligence Laboratory, East China Normal University
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing offboard 3D detectors always follow a modular pipeline design to take advantage of unlimited sequential point clouds. We have found that the full potential of offboard 3D detectors is not explored mainly due to two reasons: (1) the onboard multi-object tracker cannot generate sufficient complete object trajectories, and (2) the motion state of objects poses an inevitable challenge for the object-centric refining stage in leveraging the long-term temporal context representation. To tackle these problems, we propose a novel paradigm of offboard 3D object detection, named DetZero. Concretely, an offline tracker coupled with a multi-frame detector is proposed to focus on the completeness of generated object tracks. An attention-mechanism refining module is proposed to strengthen contextual information interaction across long-term sequential point clouds for object refining with decomposed regression methods. Extensive experiments on Waymo Open Dataset show our DetZero outperforms all state-of-the-art onboard and offboard 3D detection methods. Notably, DetZero ranks 1st place on Waymo 3D object detection leaderboard with 85.15 mAPH (L2) detection performance. Further experiments validate the application of taking the place of human labels with such high-quality results. Our empirical study leads to rethinking conventions and interesting findings that can guide future research on offboard 3D object detection.

</details>

### PARTNER: Level up the Polar Representation for LiDAR 3D Object Detection.
- **链接**: [arXiv:2308.03982](https://arxiv.org/abs/2308.03982) · 📚 被引 20
- **作者**: Ming Nie, Yujing Xue, Chunwei Wang, Chaoqiang Ye, Hang Xu, Xinge Zhu et al.
- **🏷️ 机构**: Fudan University,School of Data Science, National University of Singapore, Huawei Noah&#x2019;s Ark Lab
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, polar-based representation has shown promising properties in perceptual tasks. In addition to Cartesian-based approaches, which separate point clouds unevenly, representing point clouds as polar grids has been recognized as an alternative due to (1) its advantage in robust performance under different resolutions and (2) its superiority in streaming-based approaches. However, state-of-the-art polar-based detection methods inevitably suffer from the feature distortion problem because of the non-uniform division of polar representation, resulting in a non-negligible performance gap compared to Cartesian-based approaches. To tackle this issue, we present PARTNER, a novel 3D object detector in the polar coordinate. PARTNER alleviates the dilemma of feature distortion with global representation re-alignment and facilitates the regression by introducing instance-level geometric information into the detection head. Extensive experiments show overwhelming advantages in streaming-based detection and different resolutions. Furthermore, our method outperforms the previous polar-based works with remarkable margins of 3.68% and 9.15% on Waymo and ONCE validation set, thus achieving competitive results over the state-of-the-art methods.

</details>

### Clusterformer: Cluster-based Transformer for 3D Object Detection in Point Clouds.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00613) · 📚 被引 14
- **作者**: Yu Pei, Xian Zhao, Hao Li, Jingyuan Ma, Jingwei Zhang, Shiliang Pu
- **🏷️ 机构**: HikVision Research Institute
- **会议**: ICCV 2023

### SupFusion: Supervised LiDAR-Camera Fusion for 3D Object Detection.
- **链接**: [arXiv:2309.07084](https://arxiv.org/abs/2309.07084) · 📚 被引 34
- **作者**: Yiran Qin, Chaoqun Wang, Zijian Kang, Ningning Ma, Zhen Li, Ruimao Zhang
- **🏷️ 机构**: The Chinese University of Hong Kong, Shenzhen (CUHK-Shenzhen),School of Data Science, Shenzhen Research Institute of Big Data,China, NIO, The Chinese University of Hong Kong, Shenzhen (CUHK-Shenzhen),School of Science and Engineering, Future Intelligent Network Research Institute,China
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we propose a novel training strategy called SupFusion, which provides an auxiliary feature level supervision for effective LiDAR-Camera fusion and significantly boosts detection performance. Our strategy involves a data enhancement method named Polar Sampling, which densifies sparse objects and trains an assistant model to generate high-quality features as the supervision. These features are then used to train the LiDAR-Camera fusion model, where the fusion feature is optimized to simulate the generated high-quality features. Furthermore, we propose a simple yet effective deep fusion module, which contiguously gains superior performance compared with previous fusion methods with SupFusion strategy. In such a manner, our proposal shares the following advantages. Firstly, SupFusion introduces auxiliary feature-level supervision which could boost LiDAR-Camera detection performance without introducing extra inference costs. Secondly, the proposed deep fusion could continuously improve the detector's abilities. Our proposed SupFusion and deep fusion module is plug-and-play, we make extensive experiments to demonstrate its effectiveness. Specifically, we gain around 2% 3D mAP improvements on KITTI benchmark based on multiple LiDAR-Camera 3D detectors.

</details>

### 3DPPE: 3D Point Positional Encoding for Transformer-based Multi-Camera 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00331)
- **作者**: Changyong Shu, Jiajun Deng, Fisher Yu, Yifan Liu
- **🏷️ 机构**: ETH Zurich
- **会议**: ICCV 2023

### GraphAlign: Enhancing Accurate Feature Alignment by Graph matching for Multi-Modal 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00311)
- **作者**: Ziying Song, Haiyue Wei, Lin Bai, Lei Yang, Caiyan Jia
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### LoGoNet: Towards Accurate 3D Object Detection with Local-to-Global Cross- Modal Fusion.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01681) · 📚 被引 181
- **作者**: Xin Li, Tao Ma, Yuenan Hou, Botian Shi, Yuchen Yang, Youquan Liu et al.
- **🏷️ 机构**: The Chinese University of Hong Kong, Shanghai AI Laboratory, Fudan University
- **会议**: CVPR 2023

### PillarNeXt: Rethinking Network Designs for 3D Object Detection in LiDAR Point Clouds.
- **链接**: [arXiv:2305.04925](https://arxiv.org/abs/2305.04925) · 📚 被引 182
- **作者**: Jinyu Li, Chenxu Luo, Xiaodong Yang
- **🏷️ 机构**: QCraft
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In order to deal with the sparse and unstructured raw point clouds, LiDAR based 3D object detection research mostly focuses on designing dedicated local point aggregators for fine-grained geometrical modeling. In this paper, we revisit the local point aggregators from the perspective of allocating computational resources. We find that the simplest pillar based models perform surprisingly well considering both accuracy and latency. Additionally, we show that minimal adaptions from the success of 2D object detection, such as enlarging receptive field, significantly boost the performance. Extensive experiments reveal that our pillar based networks with modernized designs in terms of architecture and training render the state-of-the-art performance on the two popular benchmarks: Waymo Open Dataset and nuScenes. Our results challenge the common intuition that the detailed geometry modeling is essential to achieve high performance for 3D object detection.

</details>

### MoDAR: Using Motion Forecasting for 3D Object Detection in Point Cloud Sequences.
- **链接**: [arXiv:2306.03206](https://arxiv.org/abs/2306.03206) · 📚 被引 17
- **作者**: Yingwei Li, Charles R. Qi, Yin Zhou, Chenxi Liu, Dragomir Anguelov
- **🏷️ 机构**: Waymo LLC
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Occluded and long-range objects are ubiquitous and challenging for 3D object detection. Point cloud sequence data provide unique opportunities to improve such cases, as an occluded or distant object can be observed from different viewpoints or gets better visibility over time. However, the efficiency and effectiveness in encoding long-term sequence data can still be improved. In this work, we propose MoDAR, using motion forecasting outputs as a type of virtual modality, to augment LiDAR point clouds. The MoDAR modality propagates object information from temporal contexts to a target frame, represented as a set of virtual points, one for each object from a waypoint on a forecasted trajectory. A fused point cloud of both raw sensor points and the virtual points can then be fed to any off-the-shelf point-cloud based 3D object detector. Evaluated on the Waymo Open Dataset, our method significantly improves prior art detectors by using motion forecasting from extra-long sequences (e.g. 18 seconds), achieving new state of the arts, while not adding much computation overhead.

</details>

### Deep Dive into Gradients: Better Optimization for 3D Object Detection with Gradient-Corrected IoU Supervision.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00497) · 📚 被引 15
- **作者**: Qi Ming, Lingjuan Miao, Zhe Ma, Lin Zhao, Zhiqiang Zhou, Xuhui Huang et al.
- **🏷️ 机构**: School of Automation, Beijing Institute of Technology,China
- **会议**: CVPR 2023

### Weakly Supervised Monocular 3D Object Detection Using Multi-View Projection and Direction Consistency.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01677)
- **作者**: Runzhou Tao, Wencheng Han, Zhongying Qiu, Cheng-Zhong Xu, Jianbing Shen
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### Not Every Side Is Equal: Localization Uncertainty Estimation for Semi-Supervised 3D Object Detection.
- **链接**: [arXiv:2312.10390](https://arxiv.org/abs/2312.10390) · 📚 被引 10
- **作者**: Chuxin Wang, Wenfei Yang, Tianzhu Zhang
- **🏷️ 机构**: University of Science and Technology of China
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Semi-supervised 3D object detection from point cloud aims to train a detector with a small number of labeled data and a large number of unlabeled data. The core of existing methods lies in how to select high-quality pseudo-labels using the designed quality evaluation criterion. However, these methods treat each pseudo bounding box as a whole and assign equal importance to each side during training, which is detrimental to model performance due to many sides having poor localization quality. Besides, existing methods filter out a large number of low-quality pseudo-labels, which also contain some correct regression values that can help with model training. To address the above issues, we propose a side-aware framework for semi-supervised 3D object detection consisting of three key designs: a 3D bounding box parameterization method, an uncertainty estimation module, and a pseudo-label selection strategy. These modules work together to explicitly estimate the localization quality of each side and assign different levels of importance during the training phase. Extensive experiment results demonstrate that the proposed method can consistently outperform baseline models under different scenes and evaluation criteria. Moreover, our method achieves state-of-the-art performance on three datasets with different labeled ratios.

</details>

### Towards Universal LiDAR-Based 3D Object Detection by Multi-Domain Knowledge Transfer.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00796) · 📚 被引 9
- **作者**: Guile Wu, Tongtong Cao, Bingbing Liu, Xingxin Chen, Yuan Ren
- **🏷️ 机构**: Huawei Noah&#x2019;s Ark Lab
- **会议**: ICCV 2023

### CoIn: Contrastive Instance Feature Mining for Outdoor 3D Object Detection with Very Limited Annotations.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00575) · 📚 被引 31
- **作者**: Qiming Xia, Jinhao Deng, Chenglu Wen, Hai Wu, Shaoshuai Shi, Xin Li et al.
- **🏷️ 机构**: Xiamen University, Max-Planck Institute, Texas A&#x0026;M University
- **会议**: ICCV 2023

### Pixel-Aligned Recurrent Queries for Multi-View 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01684)
- **作者**: Yiming Xie, Huaizu Jiang, Georgia Gkioxari, Julian Straub
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### SparseFusion: Fusing Multi-Modal Sparse Representations for Multi-Sensor 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01613)
- **作者**: Yichen Xie, Chenfeng Xu, Marie-Julie Rakotosaona, Patrick Rim, Federico Tombari, Kurt Keutzer et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### MonoNeRD: NeRF-like Representations for Monocular 3D Object Detection.
- **链接**: [arXiv:2308.09421](https://arxiv.org/abs/2308.09421) · [代码](https://github.com/cskkxjk/MonoNeRD) · 📚 被引 40
- **作者**: Junkai Xu, Liang Peng, Haoran Chen, Hao Li, Wei Qian, Ke Li et al.
- **🏷️ 机构**: Zhejiang University,State Key Lab of CAD &#x0026; CG, FABU Inc, Fullong Inc
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In the field of monocular 3D detection, it is common practice to utilize scene geometric clues to enhance the detector's performance. However, many existing works adopt these clues explicitly such as estimating a depth map and back-projecting it into 3D space. This explicit methodology induces sparsity in 3D representations due to the increased dimensionality from 2D to 3D, and leads to substantial information loss, especially for distant and occluded objects. To alleviate this issue, we propose MonoNeRD, a novel detection framework that can infer dense 3D geometry and occupancy. Specifically, we model scenes with Signed Distance Functions (SDF), facilitating the production of dense 3D representations. We treat these representations as Neural Radiance Fields (NeRF) and then employ volume rendering to recover RGB images and depth maps. To the best of our knowledge, this work is the first to introduce volume rendering for M3D, and demonstrates the potential of implicit reconstruction for image-based 3D perception. Extensive experiments conducted on the KITTI-3D benchmark and Waymo Open Dataset demonstrate the effectiveness of MonoNeRD. Codes are available at https://github.com/cskkxjk/MonoNeRD.

</details>

### NeRF-Det: Learning Geometry-Aware Volumetric Representation for Multi-View 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.02131)
- **作者**: Chenfeng Xu, Bichen Wu, Ji Hou, Sam S. Tsai, Ruilong Li, Jialiang Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### Cross Modal Transformer: Towards Fast and Robust 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01675) · 📚 被引 173
- **作者**: Junjie Yan, Yingfei Liu, Jianjian Sun, Fan Jia, Shuailin Li, Tiancai Wang et al.
- **🏷️ 机构**: MEGVII Technology
- **会议**: ICCV 2023

### MonoDETR: Depth-guided Transformer for Monocular 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00840) · 📚 被引 190
- **作者**: Renrui Zhang, Han Qiu, Tai Wang, Ziyu Guo, Ziteng Cui, Yu Qiao et al.
- **🏷️ 机构**: CUHK MMLab, Shanghai Artificial Intelligence Laboratory
- **会议**: ICCV 2023

### QD-BEV : Quantization-aware View-guided Distillation for Multi-view 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00354)
- **作者**: Yifan Zhang, Zhen Dong, Huanrui Yang, Ming Lu, Cheng-Ching Tseng, Yuan Du et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### A Simple Vision Transformer for Weakly Semi-supervised 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00769)
- **作者**: Dingyuan Zhang, Dingkang Liang, Zhikang Zou, Jingyu Li, Xiaoqing Ye, Zhe Liu et al.
- **🏷️ 机构**: HUAST
- **会议**: ICCV 2023

### BEVHeight: A Robust Framework for Vision-based Roadside 3D Object Detection.
- **链接**: [arXiv:2303.08498](https://arxiv.org/abs/2303.08498) · [代码](https://github.com/ADLab-AutoDrive/BEVHeight) · 📚 被引 122
- **作者**: Lei Yang, Kaicheng Yu, Tao Tang, Jun Li, Kun Yuan, Li Wang et al.
- **🏷️ 机构**: Tsinghua University,State Key Laboratory of Automotive Safety and Energy, Autonomous Driving Lab, Alibaba Group, Sun Yat-sen University,Shenzhen Campus
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While most recent autonomous driving system focuses on developing perception methods on ego-vehicle sensors, people tend to overlook an alternative approach to leverage intelligent roadside cameras to extend the perception ability beyond the visual range. We discover that the state-of-the-art vision-centric bird's eye view detection methods have inferior performances on roadside cameras. This is because these methods mainly focus on recovering the depth regarding the camera center, where the depth difference between the car and the ground quickly shrinks while the distance increases. In this paper, we propose a simple yet effective approach, dubbed BEVHeight, to address this issue. In essence, instead of predicting the pixel-wise depth, we regress the height to the ground to achieve a distance-agnostic formulation to ease the optimization process of camera-only perception methods. On popular 3D detection benchmarks of roadside cameras, our method surpasses all previous vision-centric methods by a significant margin. The code is available at {\url{https://github.com/ADLab-AutoDrive/BEVHeight}}.

</details>

### Bi3D: Bi-Domain Active Learning for Cross-Domain 3D Object Detection.
- **链接**: [arXiv:2303.05886](https://arxiv.org/abs/2303.05886) · [代码](https://github.com/PJLabADG/3DTrans) · 📚 被引 0
- **作者**: Jiakang Yuan, Bo Zhang, Xiangchao Yan, Tao Chen, Botian Shi, Yikang Li et al.
- **🏷️ 机构**: Shanghai AI Lab
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Unsupervised Domain Adaptation (UDA) technique has been explored in 3D cross-domain tasks recently. Though preliminary progress has been made, the performance gap between the UDA-based 3D model and the supervised one trained with fully annotated target domain is still large. This motivates us to consider selecting partial-yet-important target data and labeling them at a minimum cost, to achieve a good trade-off between high performance and low annotation cost. To this end, we propose a Bi-domain active learning approach, namely Bi3D, to solve the cross-domain 3D object detection task. The Bi3D first develops a domainness-aware source sampling strategy, which identifies target-domain-like samples from the source domain to avoid the model being interfered by irrelevant source data. Then a diversity-based target sampling strategy is developed, which selects the most informative subset of target domain to improve the model adaptability to the target domain using as little annotation budget as possible. Experiments are conducted on typical cross-domain adaptation scenarios including cross-LiDAR-beam, cross-country, and cross-sensor, where Bi3D achieves a promising target-domain detection accuracy (89.63% on KITTI) compared with UDAbased work (84.29%), even surpassing the detector trained on the full set of the labeled target domain (88.98%). Our code is available at: https://github.com/PJLabADG/3DTrans.

</details>

### Distilling Focal Knowledge from Imperfect Expert for 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00102) · 📚 被引 13
- **作者**: Jia Zeng, Li Chen, Hanming Deng, Lewei Lu, Junchi Yan, Yu Qiao et al.
- **🏷️ 机构**: OpenDrivel.ab, Shanghai AI Lab, SenseTime Research
- **会议**: CVPR 2023

### Uni3D: A Unified Baseline for Multi-Dataset 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00893) · 📚 被引 43
- **作者**: Bo Zhang, Jiakang Yuan, Botian Shi, Tao Chen, Yikang Li, Yu Qiao
- **🏷️ 机构**: Shanghai AI Laboratory, School of Information Science and Technology, Fudan University
- **会议**: CVPR 2023

### OcTr: Octree-Based Transformer for 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00500) · 📚 被引 79
- **作者**: Chao Zhou, Yanan Zhang, Jiaxin Chen, Di Huang
- **🏷️ 机构**: Beihang University,State Key Laboratory of Software Development Environment,Beijing,China, School of Computer Science and Engineering, Beihang University,Beijing,China
- **会议**: CVPR 2023

### UniDistill: A Universal Cross-Modality Knowledge Distillation Framework for 3D Object Detection in Bird's-Eye View.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00495)
- **作者**: Shengchao Zhou, Weizhou Liu, Chen Hu, Shuchang Zhou, Chao Ma
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### MonoATT: Online Monocular 3D Object Detection with Adaptive Token Transformer.
- **链接**: [arXiv:2303.13018](https://arxiv.org/abs/2303.13018) · 📚 被引 46
- **作者**: Yunsong Zhou, Hongzi Zhu, Quan Liu, Shan Chang, Minyi Guo
- **🏷️ 机构**: Shanghai Jiao Tong University, Donghua University
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Mobile monocular 3D object detection (Mono3D) (e.g., on a vehicle, a drone, or a robot) is an important yet challenging task. Existing transformer-based offline Mono3D models adopt grid-based vision tokens, which is suboptimal when using coarse tokens due to the limited available computational power. In this paper, we propose an online Mono3D framework, called MonoATT, which leverages a novel vision transformer with heterogeneous tokens of varying shapes and sizes to facilitate mobile Mono3D. The core idea of MonoATT is to adaptively assign finer tokens to areas of more significance before utilizing a transformer to enhance Mono3D. To this end, we first use prior knowledge to design a scoring network for selecting the most important areas of the image, and then propose a token clustering and merging network with an attention mechanism to gradually merge tokens around the selected areas in multiple stages. Finally, a pixel-level feature map is reconstructed from heterogeneous tokens before employing a SOTA Mono3D detector as the underlying detection core. Experiment results on the real-world KITTI dataset demonstrate that MonoATT can effectively improve the Mono3D accuracy for both near and far objects and guarantee low latency. MonoATT yields the best performance compared with the state-of-the-art methods by a large margin and is ranked number one on the KITTI 3D benchmark.

</details>

</details>

### An Empirical Analysis of Range for 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00440) · 📚 被引 10
- **作者**: Neehar Peri, Mengtian Li, Benjamin Wilson, Yu-Xiong Wang, James Hays, Deva Ramanan
- **🏷️ 机构**: Carnegie Mellon University, Georgia Institute of Technology, University of Illinois Urbana-Champaign
- **会议**: ICCV 2023

### On Offline Evaluation of 3D Object Detection for Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00441)
- **作者**: Tim Schreier, Katrin Renz, Andreas Geiger, Kashyap Chitta
- **🏷️ 机构**: University of Tübingen
- **会议**: ICCV 2023

### SVQNet: Sparse Voxel-Adjacent Query Network for 4D Spatio-Temporal LiDAR Semantic Segmentation.
- **链接**: [arXiv:2308.13323](https://arxiv.org/abs/2308.13323) · 📚 被引 10
- **作者**: Xuechao Chen, Shuangjie Xu, Xiaoyi Zou, Tongyi Cao, Dit-Yan Yeung, Lu Fang
- **🏷️ 机构**: Tsinghua University, Hong Kong University of Science and Technology, Deeproute.ai
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> LiDAR-based semantic perception tasks are critical yet challenging for autonomous driving. Due to the motion of objects and static/dynamic occlusion, temporal information plays an essential role in reinforcing perception by enhancing and completing single-frame knowledge. Previous approaches either directly stack historical frames to the current frame or build a 4D spatio-temporal neighborhood using KNN, which duplicates computation and hinders realtime performance. Based on our observation that stacking all the historical points would damage performance due to a large amount of redundant and misleading information, we propose the Sparse Voxel-Adjacent Query Network (SVQNet) for 4D LiDAR semantic segmentation. To take full advantage of the historical frames high-efficiently, we shunt the historical points into two groups with reference to the current points. One is the Voxel-Adjacent Neighborhood carrying local enhancing knowledge. The other is the Historical Context completing the global knowledge. Then we propose new modules to select and extract the instructive features from the two groups. Our SVQNet achieves state-of-the-art performance in LiDAR semantic segmentation of the SemanticKITTI benchmark and the nuScenes dataset.

</details>

### PointDC: Unsupervised Semantic Segmentation of 3D Point Clouds via Cross-modal Distillation and Super-Voxel Clustering.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01314)
- **作者**: Zisheng Chen, Hongbin Xu, Weitao Chen, Zhipeng Zhou, Haihong Xiao, Baigui Sun et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### Collaboration Helps Camera Overtake LiDAR in 3D Detection.
- **链接**: [arXiv:2303.13560](https://arxiv.org/abs/2303.13560) · [代码](https://github.com/MediaBrain-SJTU/CoCa3D) · 📚 被引 108
- **作者**: Yue Hu, Yifan Lu, Runsheng Xu, Weidi Xie, Siheng Chen, Yanfeng Wang
- **🏷️ 机构**: Shanghai Jiao Tong University,Cooperative Medianet Innovation Center, University of California,Los Angeles, Shanghai AI Laboratory
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Camera-only 3D detection provides an economical solution with a simple configuration for localizing objects in 3D space compared to LiDAR-based detection systems. However, a major challenge lies in precise depth estimation due to the lack of direct 3D measurements in the input. Many previous methods attempt to improve depth estimation through network designs, e.g., deformable layers and larger receptive fields. This work proposes an orthogonal direction, improving the camera-only 3D detection by introducing multi-agent collaborations. Our proposed collaborative camera-only 3D detection (CoCa3D) enables agents to share complementary information with each other through communication. Meanwhile, we optimize communication efficiency by selecting the most informative cues. The shared messages from multiple viewpoints disambiguate the single-agent estimated depth and complement the occluded and long-range regions in the single-agent view. We evaluate CoCa3D in one real-world dataset and two new simulation datasets. Results show that CoCa3D improves previous SOTA performances by 44.21% on DAIR-V2X, 30.60% on OPV2V+, 12.59% on CoPerception-UAVs+ for AP@70. Our preliminary results show a potential that with sufficient collaboration, the camera might overtake LiDAR in some practical scenarios. We released the dataset and code at https://siheng-chen.github.io/dataset/CoPerception+ and https://github.com/MediaBrain-SJTU/CoCa3D.

</details>

### MV-JAR: Masked Voxel Jigsaw and Reconstruction for LiDAR-Based Self-Supervised Pre-Training.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01292)
- **作者**: Runsen Xu, Tai Wang, Wenwei Zhang, Runjian Chen, Jinkun Cao, Jiangmiao Pang et al.
- **🏷️ 机构**: CUHK
- **会议**: CVPR 2023

### GraVoS: Voxel Selection for 3D Point-Cloud Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02077) · 📚 被引 15
- **作者**: Oren Shrout, Yizhak Ben-Shabat, Ayellet Tal
- **🏷️ 机构**: Technion,Israel
- **会议**: CVPR 2023

### FrustumFormer: Adaptive Instance-aware Resampling for Multi-view 3D Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00493)
- **作者**: Yuqi Wang, Yuntao Chen, Zhaoxiang Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023
