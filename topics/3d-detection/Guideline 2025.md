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

> Recent advances in LiDAR 3D detection have demonstrated the effectiveness of Transformer-based frameworks in capturing the global dependencies from point cloud spaces, which serialize the 3D voxels into the flattened 1D sequence for iterative self-attention. However, the spatial structure of 3D voxels will be inevitably destroyed during the serialization process. Besides, due to the considerable number of 3D voxels and quadratic complexity of Transformers, multiple sequences are grouped before feeding to Transformers, leading to a limited receptive field. Inspired by the impressive performance of State Space Models (SSM) achieved in the field of 2D vision tasks, in this paper, we propose a novel Unified Mamba (UniMamba), which seamlessly integrates the merits of 3D convolution and SSM in a concise multi-head manner, aiming to perform "local and global" spatial context aggregation efficiently and simultaneously. Specifically, a UniMamba block is designed which mainly consists of spatial locality modeling, complementary Z-order serialization and local-global sequential aggregator. The spatial locality modeling module integrates 3D submanifold convolution to capture the dynamic spatial position embedding before serialization. Then the efficient Z-order curve is adopted for serialization both horizontally and vertically. Furthermore, the local-global sequential aggregator adopts the channel grouping strategy to efficiently encode both "local and global" spatial inter-dependencies using multi-head SSM. Additionally, an encoder-decoder architecture with stacked UniMamba blocks is formed to facilitate multi-scale spatial learning hierarchically. Extensive experiments are conducted on three popular datasets: nuScenes, Waymo and Argoverse 2. Particularly, our UniMamba achieves 70.2 mAP on the nuScenes dataset.

</details>

### Ev-3DOD: Pushing the Temporal Boundaries of 3D Object Detection with Event Cameras.
- **链接**: [arXiv:2502.19630](https://arxiv.org/abs/2502.19630) · [代码](https://github.com/mickeykang16/Ev3DOD) · 📚 被引 3
- **作者**: Hoonhee Cho, Jae-Young Kang, Youngho Kim, Kuk-Jin Yoon
- **🏷️ 机构**: KAIST
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Detecting 3D objects in point clouds plays a crucial role in autonomous driving systems. Recently, advanced multi-modal methods incorporating camera information have achieved notable performance. For a safe and effective autonomous driving system, algorithms that excel not only in accuracy but also in speed and low latency are essential. However, existing algorithms fail to meet these requirements due to the latency and bandwidth limitations of fixed frame rate sensors, e.g., LiDAR and camera. To address this limitation, we introduce asynchronous event cameras into 3D object detection for the first time. We leverage their high temporal resolution and low bandwidth to enable high-speed 3D object detection. Our method enables detection even during inter-frame intervals when synchronized data is unavailable, by retrieving previous 3D information through the event camera. Furthermore, we introduce the first event-based 3D object detection dataset, DSEC-3DOD, which includes ground-truth 3D bounding boxes at 100 FPS, establishing the first benchmark for event-based 3D detectors. The code and dataset are available at https://github.com/mickeykang16/Ev3DOD.

</details>

### RaCFormer: Towards High-Quality 3D Object Detection via Query-based Radar-Camera Fusion.
- **链接**: [arXiv:2412.12725](https://arxiv.org/abs/2412.12725) · [代码](https://github.com/cxmomo/RaCFormer) · 📚 被引 12
- **作者**: Xiaomeng Chu, Jiajun Deng, Guoliang You, Yifan Duan, Houqiang Li, Yanyong Zhang
- **🏷️ 机构**: University of Science and Technology of China, The University of Adelaide
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose Radar-Camera fusion transformer (RaCFormer) to boost the accuracy of 3D object detection by the following insight. The Radar-Camera fusion in outdoor 3D scene perception is capped by the image-to-BEV transformation--if the depth of pixels is not accurately estimated, the naive combination of BEV features actually integrates unaligned visual content. To avoid this problem, we propose a query-based framework that enables adaptive sampling of instance-relevant features from both the bird's-eye view (BEV) and the original image view. Furthermore, we enhance system performance by two key designs: optimizing query initialization and strengthening the representational capacity of BEV. For the former, we introduce an adaptive circular distribution in polar coordinates to refine the initialization of object queries, allowing for a distance-based adjustment of query density. For the latter, we initially incorporate a radar-guided depth head to refine the transformation from image view to BEV. Subsequently, we focus on leveraging the Doppler effect of radar and introduce an implicit dynamic catcher to capture the temporal elements within the BEV. Extensive experiments on nuScenes and View-of-Delft (VoD) datasets validate the merits of our design. Remarkably, our method achieves superior results of 64.9% mAP and 70.2% NDS on nuScenes. RaCFormer also secures the state-of-the-art performance on the VoD dataset. Code is available at https://github.com/cxmomo/RaCFormer.

</details>

### V2X-R: Cooperative LiDAR-4D Radar Fusion with Denoising Diffusion for 3D Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Huang_V2X-R_Cooperative_LiDAR-4D_Radar_Fusion_with_Denoising_Diffusion_for_3D_CVPR_2025_paper.html)
- **作者**: Xun Huang, Jinlong Wang, Qiming Xia, Siheng Chen, Bisheng Yang, Xin Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### Cubify Anything: Scaling Indoor 3D Object Detection.
- **链接**: [arXiv:2412.04458](https://arxiv.org/abs/2412.04458) · 📚 被引 10
- **作者**: Justin Lazarow, David Griffiths, Gefen Kohavi, Francisco Crespo, Afshin Dehghan
- **🏷️ 机构**: Apple
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We consider indoor 3D object detection with respect to a single RGB(-D) frame acquired from a commodity handheld device. We seek to significantly advance the status quo with respect to both data and modeling. First, we establish that existing datasets have significant limitations to scale, accuracy, and diversity of objects. As a result, we introduce the Cubify-Anything 1M (CA-1M) dataset, which exhaustively labels over 400K 3D objects on over 1K highly accurate laser-scanned scenes with near-perfect registration to over 3.5K handheld, egocentric captures. Next, we establish Cubify Transformer (CuTR), a fully Transformer 3D object detection baseline which rather than operating in 3D on point or voxel-based representations, predicts 3D boxes directly from 2D features derived from RGB(-D) inputs. While this approach lacks any 3D inductive biases, we show that paired with CA-1M, CuTR outperforms point-based methods - accurately recalling over 62% of objects in 3D, and is significantly more capable at handling noise and uncertainty present in commodity LiDAR-derived depth maps while also providing promising RGB only performance without architecture changes. Furthermore, by pre-training on CA-1M, CuTR can outperform point-based methods on a more diverse variant of SUN RGB-D - supporting the notion that while inductive biases in 3D are useful at the smaller sizes of existing datasets, they fail to scale to the data-rich regime of CA-1M. Overall, this dataset and baseline model provide strong evidence that we are moving towards models which can effectively Cubify Anything.

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
