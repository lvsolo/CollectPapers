# 3D Detection — 2025 Guideline

> 领域: 3D 目标检测（LiDAR / 相机 / 多模态融合）
> 论文数: 18 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### UniMamba: Unified Spatial-Channel Representation Learning with Group-Efficient Mamba for LiDAR-based 3D Object Detection.
- **链接**: [arXiv:2503.12009](https://arxiv.org/abs/2503.12009) · 📚 被引 18
- **作者**: Xin Jin, Haisheng Su, Kai Liu, Cong Ma, Wei Wu, Fei Hui et al.
- **🏷️ 机构**: Chang&#x2019;an University, Shanghai Jiao Tong University,School of Computer Science, SenseAuto Research
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We revisit scene-level 3D object detection as the output of an object-centric framework capable of both localization and mapping using 3D oriented boxes as the underlying geometric primitive. While existing 3D object detection approaches operate globally and implicitly rely on the a priori existence of metric camera poses, our method, Rooms from Motion (RfM) operates on a collection of un-posed images. By replacing the standard 2D keypoint-based matcher of structure-from-motion with an object-centric matcher based on image-derived 3D boxes, we estimate metric camera poses, object tracks, and finally produce a global, semantic 3D object map. When a priori pose is available, we can significantly improve map quality through optimization of global 3D boxes against individual observations. RfM shows strong localization performance and subsequently produces maps of higher quality than leading point-based and multi-view 3D object detection methods on CA-1M and ScanNet++, despite these global methods relying on overparameterization through point clouds or dense volumes. Rooms from Motion achieves a general, object-centric representation which not only extends the work of Cubify Anything to full scenes but also allows for inherently sparse localization and parametric mapping proportional to the number of objects in a scene.

</details>

### Ev-3DOD: Pushing the Temporal Boundaries of 3D Object Detection with Event Cameras.
- **链接**: [arXiv:2502.19630](https://arxiv.org/abs/2502.19630) · [代码](https://github.com/mickeykang16/Ev3DOD) · 📚 被引 3
- **作者**: Hoonhee Cho, Jae-Young Kang, Youngho Kim, Kuk-Jin Yoon
- **🏷️ 机构**: KAIST
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D object detection is essential for autonomous systems, enabling precise localization and dimension estimation. While LiDAR and RGB cameras are widely used, their fixed frame rates create perception gaps in high-speed scenarios. Event cameras, with their asynchronous nature and high temporal resolution, offer a solution by capturing motion continuously. The recent approach, which integrates event cameras with conventional sensors for continuous-time detection, struggles in fast-motion scenarios due to its dependency on synchronized sensors. We propose a novel stereo 3D object detection framework that relies solely on event cameras, eliminating the need for conventional 3D sensors. To compensate for the lack of semantic and geometric information in event data, we introduce a dual filter mechanism that extracts both. Additionally, we enhance regression by aligning bounding boxes with object-centric information. Experiments show that our method outperforms prior approaches in dynamic environments, demonstrating the potential of event cameras for robust, continuous-time 3D perception. The code is available at https://github.com/mickeykang16/Ev-Stereo3D.

</details>

### MemDistill: Distilling LiDAR Knowledge into Memory for Camera-Only 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00642)
- **作者**: Donghyeon Kwon, Youngseok Yoon, Hyeongseok Son, Suha Kwak
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### EVT: Efficient View Transformation for Multi-Modal 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02472)
- **作者**: Yongjin Lee, Hyeon Mun Jeong, Yurim Jeon, Sanghyun Kim
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### Perspective-Invariant 3D Object Detection.
- **链接**: [arXiv:2507.17665](https://arxiv.org/abs/2507.17665) · 📚 被引 1
- **作者**: Ao Liang, Lingdong Kong, Dongyue Lu, Youquan Liu, Jian Fang, Huaici Zhao et al.
- **🏷️ 机构**: National University of Singapore, Fudan University, Shenyang Institute of Automation, Chinese Academy of Sciences
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> With the rise of robotics, LiDAR-based 3D object detection has garnered significant attention in both academia and industry. However, existing datasets and methods predominantly focus on vehicle-mounted platforms, leaving other autonomous platforms underexplored. To bridge this gap, we introduce Pi3DET, the first benchmark featuring LiDAR data and 3D bounding box annotations collected from multiple platforms: vehicle, quadruped, and drone, thereby facilitating research in 3D object detection for non-vehicle platforms as well as cross-platform 3D detection. Based on Pi3DET, we propose a novel cross-platform adaptation framework that transfers knowledge from the well-studied vehicle platform to other platforms. This framework achieves perspective-invariant 3D detection through robust alignment at both geometric and feature levels. Additionally, we establish a benchmark to evaluate the resilience and robustness of current 3D detectors in cross-platform scenarios, providing valuable insights for developing adaptive 3D perception systems. Extensive experiments validate the effectiveness of our approach on challenging cross-platform tasks, demonstrating substantial gains over existing adaptation methods. We hope this work paves the way for generalizable and unified 3D perception systems across diverse and complex environments. Our Pi3DET dataset, cross-platform benchmark suite, and annotation toolkit have been made publicly available.

</details>

### Towards Accurate and Efficient 3D Object Detection for Autonomous Driving: A Mixture of Experts Computing System on Edge.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02403)
- **作者**: Linshen Liu, Boyan Su, Junyue Jiang, Guanlin Wu, Cong Guo, Ceyu Xu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### FreqPDE: Rethinking Positional Depth Embedding for Multi-View 3D Object Detection Transformers.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02613)
- **作者**: Haisheng Su, Junjie Zhang, Feixiang Song, Sanping Zhou, Wei Wu, Junchi Yan et al.
- **🏷️ 机构**: XJTU
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Skins wrapping around our bodies, leathers covering over the sofa, sheet metal coating the car - it suggests that objects are enclosed by a series of continuous surfaces, which provides us with informative geometry prior for objectness deduction. In this paper, we propose Gaussian-Det which leverages Gaussian Splatting as surface representation for multi-view based 3D object detection. Unlike existing monocular or NeRF-based methods which depict the objects via discrete positional data, Gaussian-Det models the objects in a continuous manner by formulating the input Gaussians as feature descriptors on a mass of partial surfaces. Furthermore, to address the numerous outliers inherently introduced by Gaussian splatting, we accordingly devise a Closure Inferring Module (CIM) for the comprehensive surface-based objectness deduction. CIM firstly estimates the probabilistic feature residuals for partial surfaces given the underdetermined nature of Gaussian Splatting, which are then coalesced into a holistic representation on the overall surface closure of the object proposal. In this way, the surface information Gaussian-Det exploits serves as the prior on the quality and reliability of objectness and the information basis of proposal refinement. Experiments on both synthetic and real-world datasets demonstrate that Gaussian-Det outperforms various existing approaches, in terms of both average precision and recall.

</details>

### FSHNet: Fully Sparse Hybrid Network for 3D Object Detection.
- **链接**: [arXiv:2506.03714](https://arxiv.org/abs/2506.03714) · [代码](https://github.com/Say2L/FSHNet) · 📚 被引 3
- **作者**: Shuai Liu, Mingyue Cui, Boyang Li, Quanmin Liang, Tinghe Hong, Yunxiao Shan et al.
- **🏷️ 机构**: Sun Yat-sen University,School of Computer Science and Engineering, Sun Yat-sen University,School of Artificial Intelligence
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Fully sparse 3D detectors have recently gained significant attention due to their efficiency in long-range detection. However, sparse 3D detectors extract features only from non-empty voxels, which impairs long-range interactions and causes the center feature missing. The former weakens the feature extraction capability, while the latter hinders network optimization. To address these challenges, we introduce the Fully Sparse Hybrid Network (FSHNet). FSHNet incorporates a proposed SlotFormer block to enhance the long-range feature extraction capability of existing sparse encoders. The SlotFormer divides sparse voxels using a slot partition approach, which, compared to traditional window partition, provides a larger receptive field. Additionally, we propose a dynamic sparse label assignment strategy to deeply optimize the network by providing more high-quality positive samples. To further enhance performance, we introduce a sparse upsampling module to refine downsampled voxels, preserving fine-grained details crucial for detecting small objects. Extensive experiments on the Waymo, nuScenes, and Argoverse2 benchmarks demonstrate the effectiveness of FSHNet. The code is available at https://github.com/Say2L/FSHNet.

</details>

### MonoTAKD: Teaching Assistant Knowledge Distillation for Monocular 3D Object Detection.
- **链接**: [arXiv:2404.04910](https://arxiv.org/abs/2404.04910) · [代码](https://github.com/hoiliu-0801/MonoTAKD) · 📚 被引 6
- **作者**: Hou-I Liu, Christine Wu, Jen-Hao Cheng, Wenhao Chai, Shian-Yun Wang, Gaowen Liu et al.
- **🏷️ 机构**: National Yang Ming Chiao Tung University, University of Washington, University of Southern California
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular 3D object detection (Mono3D) holds noteworthy promise for autonomous driving applications owing to the cost-effectiveness and rich visual context of monocular camera sensors. However, depth ambiguity poses a significant challenge, as it requires extracting precise 3D scene geometry from a single image, resulting in suboptimal performance when transferring knowledge from a LiDAR-based teacher model to a camera-based student model. To facilitate effective distillation, we introduce Monocular Teaching Assistant Knowledge Distillation (MonoTAKD), which proposes a camera-based teaching assistant (TA) model to transfer robust 3D visual knowledge to the student model, leveraging the smaller feature representation gap. Additionally, we define 3D spatial cues as residual features that capture the differences between the teacher and the TA models. We then leverage these cues to improve the student model's 3D perception capabilities. Experimental results show that our MonoTAKD achieves state-of-the-art performance on the KITTI3D dataset. Furthermore, we evaluate the performance on nuScenes and KITTI raw datasets to demonstrate the generalization of our model to multi-view 3D and unsupervised data settings. Our code is available at https://github.com/hoiliu-0801/MonoTAKD.

</details>

### RICCARDO: Radar Hit Prediction and Convolution for Camera-Radar 3D Object Detection.
- **链接**: [arXiv:2504.09086](https://arxiv.org/abs/2504.09086) · [代码](https://github.com/longyunf/riccardo) · 📚 被引 5
- **作者**: Yunfei Long, Abhinav Kumar, Xiaoming Liu, Daniel D. Morris
- **🏷️ 机构**: Michigan State University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Radar hits reflect from points on both the boundary and internal to object outlines. This results in a complex distribution of radar hits that depends on factors including object category, size, and orientation. Current radar-camera fusion methods implicitly account for this with a black-box neural network. In this paper, we explicitly utilize a radar hit distribution model to assist fusion. First, we build a model to predict radar hit distributions conditioned on object properties obtained from a monocular detector. Second, we use the predicted distribution as a kernel to match actual measured radar points in the neighborhood of the monocular detections, generating matching scores at nearby positions. Finally, a fusion stage combines context with the kernel detector to refine the matching scores. Our method achieves the state-of-the-art radar-camera detection performance on nuScenes. Our source code is available at https://github.com/longyunf/riccardo.

</details>

### GBlobs: Explicit Local Structure via Gaussian Blobs for Improved Cross-Domain LiDAR-based 3D Object Detection.
- **链接**: [arXiv:2503.08639](https://arxiv.org/abs/2503.08639) · 📚 被引 2
- **作者**: Dusan Malic, Christian Fruhwirth-Reisinger, Samuel Schulter, Horst Possegger
- **🏷️ 机构**: Christian Doppler Laboratory for Embedded Machine Learning, Amazon
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> LiDAR-based 3D detectors need large datasets for training, yet they struggle to generalize to novel domains. Domain Generalization (DG) aims to mitigate this by training detectors that are invariant to such domain shifts. Current DG approaches exclusively rely on global geometric features (point cloud Cartesian coordinates) as input features. Over-reliance on these global geometric features can, however, cause 3D detectors to prioritize object location and absolute position, resulting in poor cross-domain performance. To mitigate this, we propose to exploit explicit local point cloud structure for DG, in particular by encoding point cloud neighborhoods with Gaussian blobs, GBlobs. Our proposed formulation is highly efficient and requires no additional parameters. Without any bells and whistles, simply by integrating GBlobs in existing detectors, we beat the current state-of-the-art in challenging single-source DG benchmarks by over 21 mAP (Waymo->KITTI), 13 mAP (KITTI->Waymo), and 12 mAP (nuScenes->KITTI), without sacrificing in-domain performance. Additionally, GBlobs demonstrate exceptional performance in multi-source DG, surpassing the current state-of-the-art by 17, 12, and 5 mAP on Waymo, KITTI, and ONCE, respectively.

</details>

### Leveraging Temporal Cues for Semi-Supervised Multi-View 3D Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Park_Leveraging_Temporal_Cues_for_Semi-Supervised_Multi-View_3D_Object_Detection_CVPR_2025_paper.html) · 📚 被引 2
- **作者**: Jinhyung Park, Navyata Sanghvi, Hiroki Adachi, Yoshihisa Shibata, Shawn Hunt, Shinya Tanaka et al.
- **🏷️ 机构**: Carnegie Mellon University, DENSO Corporation, DENSO International America, Inc.
- **会议**: CVPR 2025

### MonoDGP: Monocular 3D Object Detection with Decoupled-Query and Geometry-Error Priors.
- **链接**: [arXiv:2410.19590](https://arxiv.org/abs/2410.19590) · [代码](https://github.com/PuFanqi23/MonoDGP) · 📚 被引 25
- **作者**: Fanqi Pu, Yifan Wang, Jiru Deng, Wenming Yang
- **🏷️ 机构**: Tsinghua University,Shenzhen International Graduate School
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Perspective projection has been extensively utilized in monocular 3D object detection methods. It introduces geometric priors from 2D bounding boxes and 3D object dimensions to reduce the uncertainty of depth estimation. However, due to depth errors originating from the object's visual surface, the height of the bounding box often fails to represent the actual projected central height, which undermines the effectiveness of geometric depth. Direct prediction for the projected height unavoidably results in a loss of 2D priors, while multi-depth prediction with complex branches does not fully leverage geometric depth. This paper presents a Transformer-based monocular 3D object detection method called MonoDGP, which adopts perspective-invariant geometry errors to modify the projection formula. We also try to systematically discuss and explain the mechanisms and efficacy behind geometry errors, which serve as a simple but effective alternative to multi-depth prediction. Additionally, MonoDGP decouples the depth-guided decoder and constructs a 2D decoder only dependent on visual features, providing 2D priors and initializing object queries without the disturbance of 3D detection. To further optimize and fine-tune input tokens of the transformer decoder, we also introduce a Region Segment Head (RSH) that generates enhanced features and segment embeddings. Our monocular method demonstrates state-of-the-art performance on the KITTI benchmark without extra data. Code is available at https://github.com/PuFanqi23/MonoDGP.

</details>

### Uncertainty Meets Diversity: A Comprehensive Active Learning Framework for Indoor 3D Object Detection.
- **链接**: [arXiv:2503.16125](https://arxiv.org/abs/2503.16125) · 📚 被引 3
- **作者**: Jiangyi Wang, Na Zhao
- **🏷️ 机构**: Singapore University of Technology and Design (SUTD)
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Active learning has emerged as a promising approach to reduce the substantial annotation burden in 3D object detection tasks, spurring several initiatives in outdoor environments. However, its application in indoor environments remains unexplored. Compared to outdoor 3D datasets, indoor datasets face significant challenges, including fewer training samples per class, a greater number of classes, more severe class imbalance, and more diverse scene types and intra-class variances. This paper presents the first study on active learning for indoor 3D object detection, where we propose a novel framework tailored for this task. Our method incorporates two key criteria - uncertainty and diversity - to actively select the most ambiguous and informative unlabeled samples for annotation. The uncertainty criterion accounts for both inaccurate detections and undetected objects, ensuring that the most ambiguous samples are prioritized. Meanwhile, the diversity criterion is formulated as a joint optimization problem that maximizes the diversity of both object class distributions and scene types, using a new Class-aware Adaptive Prototype (CAP) bank. The CAP bank dynamically allocates representative prototypes to each class, helping to capture varying intra-class diversity across different categories. We evaluate our method on SUN RGB-D and ScanNetV2, where it outperforms baselines by a significant margin, achieving over 85% of fully-supervised performance with just 10% of the annotation budget.

</details>

### CorrBEV: Multi-View 3D Object Detection by Correlation Learning with Multi-modal Prototypes.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Xue_CorrBEV_Multi-View_3D_Object_Detection_by_Correlation_Learning_with_Multi-modal_CVPR_2025_paper.html)
- **作者**: Ziteng Xue, Mingzhe Guo, Heng Fan, Shihui Zhang, Zhipeng Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### ViKIENet: Towards Efficient 3D Object Detection with Virtual Key Instance Enhanced Network.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Yu_ViKIENet_Towards_Efficient_3D_Object_Detection_with_Virtual_Key_Instance_CVPR_2025_paper.html) · 📚 被引 9
- **作者**: Zhuochen Yu, Bijie Qiu, Andy W. H. Khong
- **🏷️ 机构**: Nanyang Technological University,School of Electrical and Electronic Engineering,Singapore
- **会议**: CVPR 2025

### SP3D: Boosting Sparsely-Supervised 3D Object Detection via Accurate Cross-Modal Semantic Prompts.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhao_SP3D_Boosting_Sparsely-Supervised_3D_Object_Detection_via_Accurate_Cross-Modal_Semantic_CVPR_2025_paper.html)
- **作者**: Shijia Zhao, Qiming Xia, Xusheng Guo, Pufan Zou, Maoji Zheng, Hai Wu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### Learning Class Prototypes for Unified Sparse-Supervised 3D Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhu_Learning_Class_Prototypes_for_Unified_Sparse-Supervised_3D_Object_Detection_CVPR_2025_paper.html) · 📚 被引 6
- **作者**: Yun Zhu, Le Hui, Hang Yang, Jianjun Qian, Jin Xie, Jian Yang
- **🏷️ 机构**: Nanjing University of Science and Technology,PCA Lab,Nanjing,China, Northwestern Polytechnical University,School of Electronics and Information,Xi&#x2019;an,China, Nanjing University,State Key Laboratory for Novel Software Technology,Nanjing,China
- **会议**: CVPR 2025

### DriveGEN: Generalized and Robust 3D Detection in Driving via Controllable Text-to-Image Diffusion Generation.
- **链接**: [arXiv:2503.11122](https://arxiv.org/abs/2503.11122) · [代码](https://github.com/Hongbin98/DriveGEN) · 📚 被引 4
- **作者**: Hongbin Lin, Zilu Guo, Yifan Zhang, Shuaicheng Niu, Yafeng Li, Ruimao Zhang et al.
- **🏷️ 机构**: FNii-Shenzhen, National University of Singapore, Nanyang Technological University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In autonomous driving, vision-centric 3D detection aims to identify 3D objects from images. However, high data collection costs and diverse real-world scenarios limit the scale of training data. Once distribution shifts occur between training and test data, existing methods often suffer from performance degradation, known as Out-of-Distribution (OOD) problems. To address this, controllable Text-to-Image (T2I) diffusion offers a potential solution for training data enhancement, which is required to generate diverse OOD scenarios with precise 3D object geometry. Nevertheless, existing controllable T2I approaches are restricted by the limited scale of training data or struggle to preserve all annotated 3D objects. In this paper, we present DriveGEN, a method designed to improve the robustness of 3D detectors in Driving via Training-Free Controllable Text-to-Image Diffusion Generation. Without extra diffusion model training, DriveGEN consistently preserves objects with precise 3D geometry across diverse OOD generations, consisting of 2 stages: 1) Self-Prototype Extraction: We empirically find that self-attention features are semantic-aware but require accurate region selection for 3D objects. Thus, we extract precise object features via layouts to capture 3D object geometry, termed self-prototypes. 2) Prototype-Guided Diffusion: To preserve objects across various OOD scenarios, we perform semantic-aware feature alignment and shallow feature alignment during denoising. Extensive experiments demonstrate the effectiveness of DriveGEN in improving 3D detection. The code is available at https://github.com/Hongbin98/DriveGEN.

</details>

### Text-guided Sparse Voxel Pruning for Efficient 3D Visual Grounding.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Guo_Text-guided_Sparse_Voxel_Pruning_for_Efficient_3D_Visual_Grounding_CVPR_2025_paper.html)
- **作者**: Wenxuan Guo, Xiuwei Xu, Ziwei Wang, Jianjiang Feng, Jie Zhou, Jiwen Lu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025
