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

## 🆕 增量新增

### V2X-R: Cooperative LiDAR-4D Radar Fusion with Denoising Diffusion for 3D Object Detection. **⭐⭐⭐** (相关度: 85%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Huang_V2X-R_Cooperative_LiDAR-4D_Radar_Fusion_with_Denoising_Diffusion_for_3D_CVPR_2025_paper.html) · 📚 被引 20
- **作者**: Xun Huang, Jinlong Wang, Qiming Xia, Siheng Chen, Bisheng Yang, Xin Li et al.
- **🏷️ 机构**: Xiamen University,Fujian Key Laboratory of Sensing and Computing for Smart Cities, Shanghai Jiao Tong University, Wuhan University
- **会议**: CVPR 2025
- **摘要（中）**: ①针对车联网（V2X）场景下LiDAR与4D雷达融合的3D检测问题，摘要缺失，但标题表明利用去噪扩散模型进行协同融合。②提出V2X-R方法，结合LiDAR和4D雷达数据，通过去噪扩散模型生成或增强特征，实现鲁棒的3D目标检测。③相比传统融合方法，扩散模型能更好地处理多传感器噪声和不确定性。④具体效果未在摘要中提供。
- **摘要（英）**: This paper tackles cooperative LiDAR-4D radar fusion for 3D detection in V2X scenarios. It proposes V2X-R, which leverages denoising diffusion models to fuse multi-modal data, enhancing robustness against sensor noise. The approach aims to improve detection accuracy in cooperative settings, though specific results are not detailed in the abstract.
- **核心贡献**: 提出基于去噪扩散的LiDAR-4D雷达协同融合方法，用于V2X 3D检测。
- **创新点**: 将扩散模型引入多传感器融合，处理噪声和不确定性。
- **结果**: 摘要未提供具体数据，但预期提升V2X场景检测鲁棒性。

### Cubify Anything: Scaling Indoor 3D Object Detection. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2412.04458](https://arxiv.org/abs/2412.04458) · 📚 被引 10
- **作者**: Justin Lazarow, David Griffiths, Gefen Kohavi, Francisco Crespo, Afshin Dehghan
- **🏷️ 机构**: Apple
- **会议**: CVPR 2025
- **摘要（中）**: ①针对室内3D检测中现有数据集规模、精度和物体多样性不足的问题。②引入Cubify-Anything 1M (CA-1M)数据集，包含40万+3D物体和3500+手持捕获，并提出Cubify Transformer (CuTR)，直接从2D特征预测3D框，无需3D点或体素表示。③相比基于点的方法，CuTR在CA-1M上训练后，3D召回率超过62%，且对噪声和深度不确定性更鲁棒，支持纯RGB输入。④预训练进一步提升了性能。
- **摘要（英）**: This paper addresses limitations in indoor 3D detection datasets regarding scale, accuracy, and diversity. It introduces the CA-1M dataset with over 400K labeled 3D objects and proposes CuTR, a fully Transformer baseline that predicts 3D boxes directly from 2D features. CuTR outperforms point-based methods with over 62% 3D recall and handles noisy depth better, also supporting RGB-only input.
- **核心贡献**: 构建CA-1M大规模室内3D检测数据集，并提出无需3D归纳偏置的CuTR模型。
- **创新点**: 直接从2D特征预测3D框，摆脱对点云或体素表示的依赖。
- **结果**: CuTR在CA-1M上3D召回率超62%，优于基于点的方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We consider indoor 3D object detection with respect to a single RGB(-D) frame acquired from a commodity handheld device. We seek to significantly advance the status quo with respect to both data and modeling. First, we establish that existing datasets have significant limitations to scale, accuracy, and diversity of objects. As a result, we introduce the Cubify-Anything 1M (CA-1M) dataset, which exhaustively labels over 400K 3D objects on over 1K highly accurate laser-scanned scenes with near-perfect registration to over 3.5K handheld, egocentric captures. Next, we establish Cubify Transformer (CuTR), a fully Transformer 3D object detection baseline which rather than operating in 3D on point or voxel-based representations, predicts 3D boxes directly from 2D features derived from RGB(-D) inputs. While this approach lacks any 3D inductive biases, we show that paired with CA-1M, CuTR outperforms point-based methods - accurately recalling over 62% of objects in 3D, and is significantly more capable at handling noise and uncertainty present in commodity LiDAR-derived depth maps while also providing promising RGB only performance without architecture changes. Furthermore, by pre-training on CA-1M, CuTR can outperform point-based methods on a more diverse variant of SUN RGB-D - supporting the notion that while inductive biases in 3D are useful at the smaller sizes of existing datasets, they fail to scale to the data-rich regime of CA-1M. Overall, this dataset and baseline model provide strong evidence that we are moving towards models which can effectively Cubify Anything.

</details>

### Robust 3D Object Detection Using Probabilistic Point Clouds From Single-Photon Lidars.
- **链接**: [arXiv:2508.00169](https://arxiv.org/abs/2508.00169)
- **作者**: Bhavya Goyal, Felipe Gutierrez-Barragan, Wei Lin, Andreas Velten, Yin Li, Mohit Gupta
- **🏷️ 机构**: University of Wisconsin-Madison
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> LiDAR-based 3D sensors provide point clouds, a canonical 3D representation used in various scene understanding tasks. Modern LiDARs face key challenges in several real-world scenarios, such as long-distance or low-albedo objects, producing sparse or erroneous point clouds. These errors, which are rooted in the noisy raw LiDAR measurements, get propagated to downstream perception models, resulting in potentially severe loss of accuracy. This is because conventional 3D processing pipelines do not retain any uncertainty information from the raw measurements when constructing point clouds. We propose Probabilistic Point Clouds (PPC), a novel 3D scene representation where each point is augmented with a probability attribute that encapsulates the measurement uncertainty (or confidence) in the raw data. We further introduce inference approaches that leverage PPC for robust 3D object detection; these methods are versatile and can be used as computationally lightweight drop-in modules in 3D inference pipelines. We demonstrate, via both simulations and real captures, that PPC-based 3D inference methods outperform several baselines using LiDAR as well as camera-LiDAR fusion models, across challenging indoor and outdoor scenarios involving small, distant, and low-albedo objects, as well as strong ambient light. Our project webpage is at https://bhavyagoyal.github.io/ppc .

</details>

### Adaptive Dual Uncertainty Optimization: Boosting Monocular 3D Object Detection under Test-Time Shifts.
- **链接**: [arXiv:2508.20488](https://arxiv.org/abs/2508.20488)
- **作者**: Zixuan Hu, Dongxiao Li, Xinzhu Ma, Shixiang Tang, Xiaotong Li, Wenhan Yang et al.
- **🏷️ 机构**: School of Computer Science, Peking University,Beijing,China, The Chinese University of Hong Kong,Hongkong,China, Peng Cheng Laboratory,Shenzhen,China
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Accurate monocular 3D object detection (M3OD) is pivotal for safety-critical applications like autonomous driving, yet its reliability deteriorates significantly under real-world domain shifts caused by environmental or sensor variations. To address these shifts, Test-Time Adaptation (TTA) methods have emerged, enabling models to adapt to target distributions during inference. While prior TTA approaches recognize the positive correlation between low uncertainty and high generalization ability, they fail to address the dual uncertainty inherent to M3OD: semantic uncertainty (ambiguous class predictions) and geometric uncertainty (unstable spatial localization). To bridge this gap, we propose Dual Uncertainty Optimization (DUO), the first TTA framework designed to jointly minimize both uncertainties for robust M3OD. Through a convex optimization lens, we introduce an innovative convex structure of the focal loss and further derive a novel unsupervised version, enabling label-agnostic uncertainty weighting and balanced learning for high-uncertainty objects. In parallel, we design a semantic-aware normal field constraint that preserves geometric coherence in regions with clear semantic cues, reducing uncertainty from the unstable 3D representation. This dual-branch mechanism forms a complementary loop: enhanced spatial perception improves semantic classification, and robust semantic predictions further refine spatial understanding. Extensive experiments demonstrate the superiority of DUO over existing methods across various datasets and domain shift types.

</details>

### GeoFormer: Geometry Point Encoder for 3D Object Detection with Graph-Based Transformer.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02495) · 📚 被引 1
- **作者**: Xin Jin, Haisheng Su, Cong Ma, Kai Liu, Wei Wu, Fei Hui et al.
- **🏷️ 机构**: Chang&#x0027; an University, Shanghai Jiao Tong University, SenseAuto Research
- **会议**: ICCV 2025

### Height-Fidelity Dense Global Fusion for Multi-Modal 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02475) · 📚 被引 3
- **作者**: Hanshi Wang, Jin Gao, Weiming Hu, Zhipeng Zhang
- **🏷️ 机构**: State Key Laboratory of Multimodal Artificial Intelligence Systems (MAIS), CASIA, School of Artificial Intelligence, Shanghai Jiao Tong University
- **会议**: ICCV 2025

### Motal: Unsupervised 3D Object Detection by Modality and Task-Specific Knowledge Transfer.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00593)
- **作者**: Hai Wu, Hongwei Lin, Xusheng Guo, Xin Li, Mingming Wang, Cheng Wang et al.
- **🏷️ 机构**: Xiamen University, Texas A&#x0026;M University, Tsinghua University
- **会议**: ICCV 2025

### 3D-MOOD: Lifting 2D to 3D for Monocular Open-Set Object Detection.
- **链接**: [arXiv:2507.23567](https://arxiv.org/abs/2507.23567)
- **作者**: Yung-Hsu Yang, Luigi Piccinelli, Mattia Segù, Siyuan Li, Rui Huang, Yuqian Fu et al.
- **🏷️ 机构**: ETH Z&#x00FC;rich, INSAIT
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular 3D object detection is valuable for various applications such as robotics and AR/VR. Existing methods are confined to closed-set settings, where the training and testing sets consist of the same scenes and/or object categories. However, real-world applications often introduce new environments and novel object categories, posing a challenge to these methods. In this paper, we address monocular 3D object detection in an open-set setting and introduce the first end-to-end 3D Monocular Open-set Object Detector (3D-MOOD). We propose to lift the open-set 2D detection into 3D space through our designed 3D bounding box head, enabling end-to-end joint training for both 2D and 3D tasks to yield better overall performance. We condition the object queries with geometry prior and overcome the generalization for 3D estimation across diverse scenes. To further improve performance, we design the canonical image space for more efficient cross-dataset training. We evaluate 3D-MOOD on both closed-set settings (Omni3D) and open-set settings (Omni3D to Argoverse 2, ScanNet), and achieve new state-of-the-art results. Code and models are available at royyang0714.github.io/3D-MOOD.

</details>

### Harnessing Uncertainty-Aware Bounding Boxes for Unsupervised 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00862) · 📚 被引 1
- **作者**: Ruiyang Zhang, Hu Zhang, Zhedong Zheng
- **🏷️ 机构**: FST and ICI, University of Macau,China, CSIRO Data61,Australia
- **会议**: ICCV 2025

### CVFusion: Cross-View Fusion of 4D Radar and Camera for 3D Object Detection.
- **链接**: [arXiv:2507.04587](https://arxiv.org/abs/2507.04587) · 📚 被引 4
- **作者**: Hanzhi Zhong, Zhiyu Xiang, Ruoyu Xu, Jingyun Fu, Peng Xu, Shaohong Wang et al.
- **🏷️ 机构**: Zhejiang University,China
- **会议**: ICCV 2025

### Doppler-Aware LiDAR-RADAR Fusion for Weather-Robust 3D Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02525) · 📚 被引 2
- **作者**: Yujeong Chae, Heejun Park, Hyeonseong Kim, Kuk-Jin Yoon
- **🏷️ 机构**: Korea Advanced Institute of Science and Technology
- **会议**: ICCV 2025

### VoxelKP: A Voxel-Based Network Architecture for Human Keypoint Estimation in LiDAR Data.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02626)
- **作者**: Jian Shi, Peter Wonka
- **🏷️ 机构**: KAUST
- **会议**: ICCV 2025

### HVPUNet: Hybrid-Voxel Point-Cloud Upsampling Network.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02707)
- **作者**: Juhyung Ha, Vibhas K. Vats, Soon-Heung Jung, Md. Alimoor Reza, David J. Crandall
- **🏷️ 机构**: Luddy School of Informatics, Computing, and Engineering, Indiana University,Bloomington,IN,USA, Electronics and Telecommunications Research Institute,Daejeon,Republic of Korea, Drake University,Department of Mathematics and Computer Science,Des Moines,IA,USA
- **会议**: ICCV 2025

### SDFormer: Vision-Based 3D Semantic Scene Completion via SAM-Assisted Dual-Channel Voxel Transformer.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02491)
- **作者**: Yujie Xue, Huilong Pi, Jiapeng Zhang, Yunchuan Qin, Zhuo Tang, Kenli Li et al.
- **🏷️ 机构**: College of Computer Science and Electronic Engineering, Hunan University
- **会议**: ICCV 2025

### MOS: Model Synergy for Test-Time Adaptation on LiDAR-Based 3D Object Detection.
- **链接**: [arXiv:2406.14878](https://arxiv.org/abs/2406.14878)
- **作者**: Zhuoxiao Chen, Junjie Meng, Mahsa Baktashmotlagh, Yonggang Zhang, Zi Huang, Yadan Luo
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> LiDAR-based 3D object detection is crucial for various applications but often experiences performance degradation in real-world deployments due to domain shifts. While most studies focus on cross-dataset shifts, such as changes in environments and object geometries, practical corruptions from sensor variations and weather conditions remain underexplored. In this work, we propose a novel online test-time adaptation framework for 3D detectors that effectively tackles these shifts, including a challenging cross-corruption scenario where cross-dataset shifts and corruptions co-occur. By leveraging long-term knowledge from previous test batches, our approach mitigates catastrophic forgetting and adapts effectively to diverse shifts. Specifically, we propose a Model Synergy (MOS) strategy that dynamically selects historical checkpoints with diverse knowledge and assembles them to best accommodate the current test batch. This assembly is directed by our proposed Synergy Weights (SW), which perform a weighted averaging of the selected checkpoints, minimizing redundancy in the composite model. The SWs are computed by evaluating the similarity of predicted bounding boxes on the test data and the independence of features between checkpoint pairs in the model bank. To maintain an efficient and informative model bank, we discard checkpoints with the lowest average SW scores, replacing them with newly updated models. Our method was rigorously tested against existing test-time adaptation strategies across three datasets and eight types of corruptions, demonstrating superior adaptability to dynamic scenes and conditions. Notably, it achieved a 67.3% improvement in a challenging cross-corruption scenario, offering a more comprehensive benchmark for adaptation. Source code: https://github.com/zhuoxiao-chen/MOS.

</details>

### Intent3D: 3D Object Detection in RGB-D Scans Based on Human Intention.
- **链接**: [arXiv:2405.18295](https://arxiv.org/abs/2405.18295)
- **作者**: Weitai Kang, Mengxue Qu, Jyoti Kini, Yunchao Wei, Mubarak Shah, Yan Yan
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In real-life scenarios, humans seek out objects in the 3D world to fulfill their daily needs or intentions. This inspires us to introduce 3D intention grounding, a new task in 3D object detection employing RGB-D, based on human intention, such as "I want something to support my back". Closely related, 3D visual grounding focuses on understanding human reference. To achieve detection based on human intention, it relies on humans to observe the scene, reason out the target that aligns with their intention ("pillow" in this case), and finally provide a reference to the AI system, such as "A pillow on the couch". Instead, 3D intention grounding challenges AI agents to automatically observe, reason and detect the desired target solely based on human intention. To tackle this challenge, we introduce the new Intent3D dataset, consisting of 44,990 intention texts associated with 209 fine-grained classes from 1,042 scenes of the ScanNet dataset. We also establish several baselines based on different language-based 3D object detection models on our benchmark. Finally, we propose IntentNet, our unique approach, designed to tackle this intention-based detection problem. It focuses on three key aspects: intention understanding, reasoning to identify object candidates, and cascaded adaptive learning that leverages the intrinsic priority logic of different losses for multiple objective optimization. Project Page: https://weitaikang.github.io/Intent3D-webpage/

</details>

### State Space Model Meets Transformer: A New Paradigm for 3D Object Detection.
- **链接**: [arXiv:2503.14493](https://arxiv.org/abs/2503.14493)
- **作者**: Chuxin Wang, Wenfei Yang, Xiang Liu, Tianzhu Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> DETR-based methods, which use multi-layer transformer decoders to refine object queries iteratively, have shown promising performance in 3D indoor object detection. However, the scene point features in the transformer decoder remain fixed, leading to minimal contributions from later decoder layers, thereby limiting performance improvement. Recently, State Space Models (SSM) have shown efficient context modeling ability with linear complexity through iterative interactions between system states and inputs. Inspired by SSMs, we propose a new 3D object DEtection paradigm with an interactive STate space model (DEST). In the interactive SSM, we design a novel state-dependent SSM parameterization method that enables system states to effectively serve as queries in 3D indoor detection tasks. In addition, we introduce four key designs tailored to the characteristics of point cloud and SSM: The serialization and bidirectional scanning strategies enable bidirectional feature interaction among scene points within the SSM. The inter-state attention mechanism models the relationships between state points, while the gated feed-forward network enhances inter-channel correlations. To the best of our knowledge, this is the first method to model queries as system states and scene points as system inputs, which can simultaneously update scene point features and query features with linear complexity. Extensive experiments on two challenging datasets demonstrate the effectiveness of our DEST-based method. Our method improves the GroupFree baseline in terms of AP50 on ScanNet V2 (+5.3) and SUN RGB-D (+3.2) datasets. Based on the VDETR baseline, Our method sets a new SOTA on the ScanNetV2 and SUN RGB-D datasets.

</details>

### Rooms from Motion: Un-posed Indoor 3D Object Detection as Localization and Mapping.
- **链接**: [arXiv:2505.23756](https://arxiv.org/abs/2505.23756)
- **作者**: Justin Lazarow, Kai Kang, Afshin Dehghan
- **🏷️ 机构**: Apple, Apple Inc.
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We revisit scene-level 3D object detection as the output of an object-centric framework capable of both localization and mapping using 3D oriented boxes as the underlying geometric primitive. While existing 3D object detection approaches operate globally and implicitly rely on the a priori existence of metric camera poses, our method, Rooms from Motion (RfM) operates on a collection of un-posed images. By replacing the standard 2D keypoint-based matcher of structure-from-motion with an object-centric matcher based on image-derived 3D boxes, we estimate metric camera poses, object tracks, and finally produce a global, semantic 3D object map. When a priori pose is available, we can significantly improve map quality through optimization of global 3D boxes against individual observations. RfM shows strong localization performance and subsequently produces maps of higher quality than leading point-based and multi-view 3D object detection methods on CA-1M and ScanNet++, despite these global methods relying on overparameterization through point clouds or dense volumes. Rooms from Motion achieves a general, object-centric representation which not only extends the work of Cubify Anything to full scenes but also allows for inherently sparse localization and parametric mapping proportional to the number of objects in a scene.

</details>

### Point4Bit: Post Training 4-bit Quantization for Point Cloud 3D Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/f1922bd718528ac3eab114eabbbfa7a0-Abstract-Conference.html)
- **作者**: Jianyu Wang, Yu Wang, Shengjie Zhao, Sifan Zhou
- **🏷️ 机构**: Tongji University, Tsinghua University, Southeast University &amp; Carnegie Mellon University
- **会议**: NeurIPS 2025

## 跨领域论文（完整笔记在其他领域）

- OpenAD: Open-World Autonomous Driving Benchmark for 3D Object Detection. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
- RaCFormer: Towards High-Quality 3D Object Detection via Query-based Radar-Camera Fusion. → [object-detection](../object-detection/Guideline%202025.md)
- Leveraging Temporal Cues for Semi-Supervised Multi-View 3D Object Detection. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
- CorrBEV: Multi-View 3D Object Detection by Correlation Learning with Multi-modal Prototypes. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
- Multi-Scale Neighborhood Occupancy Masked Autoencoder for Self-Supervised Learning in LiDAR Point Clouds. → [self-supervised-vision](../self-supervised-vision/Guideline%202025.md)
- PSA-SSL: Pose and Size-aware Self-Supervised Learning on LiDAR Point Clouds. → [self-supervised-vision](../self-supervised-vision/Guideline%202025.md)
- RENO: Real-Time Neural Compression for 3D LiDAR Point Clouds. → [network-pruning](../network-pruning/Guideline%202025.md)
- 3D Occupancy Prediction with Low-Resolution Queries via Prototype-aware View Transformation. → [occupancy](../occupancy/Guideline%202025.md)
- Zero-Shot Novel View and Depth Synthesis with Multi-View Geometric Diffusion. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
- RoGSplat: Learning Robust Generalizable Human Gaussian Splatting from Sparse Multi-View Images. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
- VisionPAD: A Vision-Centric Pre-training Paradigm for Autonomous Driving. → [object-detection](../object-detection/Guideline%202025.md)
- SplatFlow: Self-Supervised Dynamic Gaussian Splatting in Neural Motion Flow Field for Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202025.md)
- DriveGEN: Generalized and Robust 3D Detection in Driving via Controllable Text-to-Image Diffusion Generation. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
- GaussTR: Foundation Model-Aligned Gaussian Transformer for Self-Supervised 3D Spatial Understanding. → [self-supervised-vision](../self-supervised-vision/Guideline%202025.md)
- VoteFlow: Enforcing Local Rigidity in Self-Supervised Scene Flow. → [autonomous-driving](../autonomous-driving/Guideline%202025.md)
- Text-guided Sparse Voxel Pruning for Efficient 3D Visual Grounding. → [network-pruning](../network-pruning/Guideline%202025.md)
- OV-SCAN: Semantically Consistent Alignment for Novel Object Discovery in Open-Vocabulary 3D Object Detection. → [open-set-detection](../open-set-detection/Guideline%202025.md)
- OcRFDet: Object-Centric Radiance Fields for Multi-View 3D Object Detection in Autonomous Driving. → [object-detection](../object-detection/Guideline%202025.md)
- RCTDistill: Cross-Modal Knowledge Distillation Framework for Radar-Camera 3D Object Detection with Temporal Fusion. → [object-detection](../object-detection/Guideline%202025.md)
- OpenM3D: Open Vocabulary Multi-View Indoor 3D Object Detection without Human Annotations. → [open-set-detection](../open-set-detection/Guideline%202025.md)
- Unleashing the Temporal Potential of Stereo Event Cameras for Continuous-Time 3D Object Detection. → [object-detection](../object-detection/Guideline%202025.md)
- MemDistill: Distilling LiDAR Knowledge into Memory for Camera-Only 3D Object Detection. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
- EVT: Efficient View Transformation for Multi-Modal 3D Object Detection. → [object-detection](../object-detection/Guideline%202025.md)
- FreqPDE: Rethinking Positional Depth Embedding for Multi-View 3D Object Detection Transformers. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
- Accelerate 3D Object Detection Models via Zero-Shot Attention Key Pruning. → [network-pruning](../network-pruning/Guideline%202025.md)
- Boosting Multi-View Indoor 3D Object Detection Via Adaptive 3D Volume Construction. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
- GaussianOcc: Fully Self-Supervised and Efficient 3D Occupancy Estimation with Gaussian Splatting. → [self-supervised-vision](../self-supervised-vision/Guideline%202025.md)
- Gaussian-Det: Learning Closed-Surface Gaussians for 3D Object Detection. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
- RobuRCDet: Enhancing Robustness of Radar-Camera Fusion in Bird's Eye View for 3D Object Detection. → [bev](../bev/Guideline%202025.md)
- Generalizable Multi-Camera 3D Object Detection from a Single Source via Fourier Cross-View Learning. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
- QuadricFormer: Scene as Superquadrics for 3D Semantic Occupancy Prediction. → [occupancy](../occupancy/Guideline%202025.md)
- TrackingWorld: World-centric Monocular 3D Tracking of Almost All Pixels. → [tracking](../tracking/Guideline%202025.md)
- RLGF: Reinforcement Learning with Geometric Feedback for Autonomous Driving Video Generation. → [occupancy](../occupancy/Guideline%202025.md)
- CodeMerge: Codebook-Guided Model Merging for Robust Test-Time Adaptation in Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202025.md)
- SQS: Enhancing Sparse Perception Models via Query-based Splatting in Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202025.md)
- Genesis: Multimodal Driving Scene Generation with Spatio-Temporal and Cross-Modal Consistency. → [video-understanding](../video-understanding/Guideline%202025.md)
<!-- COMPLETE v1 papers=39 -->
