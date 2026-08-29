# Multi-camera Perception — 2023 Guideline

> 领域: 多相机 / 多视角感知（环视、深度估计与 3D 预测）
> 论文数: 58 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Are We Ready for Vision-Centric Driving Streaming Perception? The ASAP Benchmark.
- **链接**: [arXiv:2212.08914](https://arxiv.org/abs/2212.08914) · [代码](https://github.com/JeffWang987/ASAP) · 📚 被引 21
- **作者**: Xiaofeng Wang, Zheng Zhu, Yunpeng Zhang, Guan Huang, Yun Ye, Wenbo Xu et al.
- **🏷️ 机构**: Institute of Automation, Chinese Academy of Sciences, PhiGent Robotics, Southeast University
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In recent years, vision-centric perception has flourished in various autonomous driving tasks, including 3D detection, semantic map construction, motion forecasting, and depth estimation. Nevertheless, the latency of vision-centric approaches is too high for practical deployment (e.g., most camera-based 3D detectors have a runtime greater than 300ms). To bridge the gap between ideal research and real-world applications, it is necessary to quantify the trade-off between performance and efficiency. Traditionally, autonomous-driving perception benchmarks perform the offline evaluation, neglecting the inference time delay. To mitigate the problem, we propose the Autonomous-driving StreAming Perception (ASAP) benchmark, which is the first benchmark to evaluate the online performance of vision-centric perception in autonomous driving. On the basis of the 2Hz annotated nuScenes dataset, we first propose an annotation-extending pipeline to generate high-frame-rate labels for the 12Hz raw images. Referring to the practical deployment, the Streaming Perception Under constRained-computation (SPUR) evaluation protocol is further constructed, where the 12Hz inputs are utilized for streaming evaluation under the constraints of different computational resources. In the ASAP benchmark, comprehensive experiment results reveal that the model rank alters under different constraints, suggesting that the model latency and computation budget should be considered as design choices to optimize the practical deployment. To facilitate further research, we establish baselines for camera-based streaming 3D detection, which consistently enhance the streaming performance across various hardware. ASAP project page: https://github.com/JeffWang987/ASAP.

</details>

### Multi-view Adversarial Discriminator: Mine the Non-causal Factors for Object Detection in Unseen Domains.
- **链接**: [arXiv:2304.02950](https://arxiv.org/abs/2304.02950) · 📚 被引 56
- **作者**: Mingjun Xu, Lingyun Qin, Weijie Chen, Shiliang Pu, Lei Zhang
- **🏷️ 机构**: School of Microelectronics and Communication Engineering, Chongqing University, China Hikvision Research Institute,Hangzhou,China
- **会议**: CVPR 2023

### AIDE: A Vision-Driven Multi-View, Multi-Modal, Multi-Tasking Dataset for Assistive Driving Perception.
- **链接**: [arXiv:2307.13933](https://arxiv.org/abs/2307.13933) · 📚 被引 67
- **作者**: Dingkang Yang, Shuai Huang, Zhi Xu, Zhenpeng Li, Shunli Wang, Mingcheng Li et al.
- **🏷️ 机构**: Academy for Engineering and Technology, Fudan University
- **会议**: ICCV 2023

### Cross-view Topology Based Consistent and Complementary Information for Deep Multi-view Clustering.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01781) · 📚 被引 32
- **作者**: Zhibin Dong, Siwei Wang, Jiaqi Jin, Xinwang Liu, En Zhu
- **🏷️ 机构**: National University of Defense Technology,School of Computer,Changsha,China, Intelligent Game and Decision Lab,Beijing,China
- **会议**: ICCV 2023

</details>

### Robust Multiview Point Cloud Registration with Reliable Pose Graph Initialization and History Reweighting.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00917) · 📚 被引 45
- **作者**: Haiping Wang, Yuan Liu, Zhen Dong, Yulan Guo, Yu-Shen Liu, Wenping Wang et al.
- **🏷️ 机构**: Wuhan University, The University of Hong Kong, Sun Yat-sen University
- **会议**: CVPR 2023

### Neural Pixel Composition for 3D-4D View Synthesis from Multi-Views.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00036) · 📚 被引 8
- **作者**: Aayush Bansal, Michael Zollhöfer
- **🏷️ 机构**: Reality Labs Research,Pittsburgh,USA
- **会议**: CVPR 2023

### Deep Incomplete Multi-View Clustering with Cross-View Partial Sample and Prototype Alignment.
- **链接**: [arXiv:2303.15689](https://arxiv.org/abs/2303.15689) · 📚 被引 102
- **作者**: Jiaqi Jin, Siwei Wang, Zhibin Dong, Xinwang Liu, En Zhu
- **🏷️ 机构**: School of Computer, National University of Defense Technology,Changsha,China
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The success of existing multi-view clustering relies on the assumption of sample integrity across multiple views. However, in real-world scenarios, samples of multi-view are partially available due to data corruption or sensor failure, which leads to incomplete multi-view clustering study (IMVC). Although several attempts have been proposed to address IMVC, they suffer from the following drawbacks: i) Existing methods mainly adopt cross-view contrastive learning forcing the representations of each sample across views to be exactly the same, which might ignore view discrepancy and flexibility in representations; ii) Due to the absence of non-observed samples across multiple views, the obtained prototypes of clusters might be unaligned and biased, leading to incorrect fusion. To address the above issues, we propose a Cross-view Partial Sample and Prototype Alignment Network (CPSPAN) for Deep Incomplete Multi-view Clustering. Firstly, unlike existing contrastive-based methods, we adopt pair-observed data alignment as 'proxy supervised signals' to guide instance-to-instance correspondence construction among views. Then, regarding of the shifted prototypes in IMVC, we further propose a prototype alignment module to achieve incomplete distribution calibration across views. Extensive experimental results showcase the effectiveness of our proposed modules, attaining noteworthy performance improvements when compared to existing IMVC competitors on benchmark datasets.

</details>

### Learning to Fuse Monocular and Multi-view Cues for Multi-frame Depth Estimation in Dynamic Scenes.
- **链接**: [arXiv:2304.08993](https://arxiv.org/abs/2304.08993) · 📚 被引 41
- **作者**: Rui Li, Dong Gong, Wei Yin, Hao Chen, Yu Zhu, Kaixuan Wang et al.
- **🏷️ 机构**: Northwestern Polytechnical University, The University of New South Wales, DJI
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-frame depth estimation generally achieves high accuracy relying on the multi-view geometric consistency. When applied in dynamic scenes, e.g., autonomous driving, this consistency is usually violated in the dynamic areas, leading to corrupted estimations. Many multi-frame methods handle dynamic areas by identifying them with explicit masks and compensating the multi-view cues with monocular cues represented as local monocular depth or features. The improvements are limited due to the uncontrolled quality of the masks and the underutilized benefits of the fusion of the two types of cues. In this paper, we propose a novel method to learn to fuse the multi-view and monocular cues encoded as volumes without needing the heuristically crafted masks. As unveiled in our analyses, the multi-view cues capture more accurate geometric information in static areas, and the monocular cues capture more useful contexts in dynamic areas. To let the geometric perception learned from multi-view cues in static areas propagate to the monocular representation in dynamic areas and let monocular cues enhance the representation of multi-view cost volume, we propose a cross-cue fusion (CCF) module, which includes the cross-cue attention (CCA) to encode the spatially non-local relative intra-relations from each source to enhance the representation of the other. Experiments on real-world datasets prove the significant effectiveness and generalization ability of the proposed method.

</details>

### OmniCity: Omnipotent City Understanding with Multi-Level and Multi-View Images.
- **链接**: [arXiv:2208.00928](https://arxiv.org/abs/2208.00928) · 📚 被引 30
- **作者**: Weijia Li, Yawen Lai, Linning Xu, Yuanbo Xiangli, Jinhua Yu, Conghui He et al.
- **🏷️ 机构**: Sun Yat-Sen University, SenseTime Research, The Chinese University of Hong Kong
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper presents OmniCity, a new dataset for omnipotent city understanding from multi-level and multi-view images. More precisely, the OmniCity contains multi-view satellite images as well as street-level panorama and mono-view images, constituting over 100K pixel-wise annotated images that are well-aligned and collected from 25K geo-locations in New York City. To alleviate the substantial pixel-wise annotation efforts, we propose an efficient street-view image annotation pipeline that leverages the existing label maps of satellite view and the transformation relations between different views (satellite, panorama, and mono-view). With the new OmniCity dataset, we provide benchmarks for a variety of tasks including building footprint extraction, height estimation, and building plane/instance/fine-grained segmentation. Compared with the existing multi-level and multi-view benchmarks, OmniCity contains a larger number of images with richer annotation types and more views, provides more benchmark results of state-of-the-art models, and introduces a novel task for fine-grained building instance segmentation on street-level panorama images. Moreover, OmniCity provides new problem settings for existing tasks, such as cross-view image matching, synthesis, segmentation, detection, etc., and facilitates the developing of new methods for large-scale city understanding, reconstruction, and simulation. The OmniCity dataset as well as the benchmarks will be available at https://city-super.github.io/omnicity.

</details>

### Multi-Sensor Large-Scale Dataset for Multi-View 3D Reconstruction.
- **链接**: [arXiv:2203.06111](https://arxiv.org/abs/2203.06111) · 📚 被引 14
- **作者**: Oleg Voynov, Gleb Bobrovskikh, Pavel A. Karpyshev, Saveliy Galochkin, Andrei-Timotei Ardelean, Arseniy Bozhenko et al.
- **🏷️ 机构**: Skolkovo Institute of Science and Technology
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a new multi-sensor dataset for multi-view 3D surface reconstruction. It includes registered RGB and depth data from sensors of different resolutions and modalities: smartphones, Intel RealSense, Microsoft Kinect, industrial cameras, and structured-light scanner. The scenes are selected to emphasize a diverse set of material properties challenging for existing algorithms. We provide around 1.4 million images of 107 different scenes acquired from 100 viewing directions under 14 lighting conditions. We expect our dataset will be useful for evaluation and training of 3D reconstruction algorithms and for related tasks. The dataset is available at skoltech3d.appliedai.tech.

</details>

### GCFAgg: Global and Cross-View Feature Aggregation for Multi-View Clustering.
- **链接**: [arXiv:2305.06799](https://arxiv.org/abs/2305.06799) · 📚 被引 186
- **作者**: Weiqing Yan, Yuanyang Zhang, Chenlei Lv, Chang Tang, Guanghui Yue, Liang Liao et al.
- **🏷️ 机构**: School of Computer and Control Engineering, Yantai University,Yantai,China,264005, College of Computer Science and Software Engineering, Shenzhen University,Shenzhen,China,518060, School of Computer, China University of Geosciences,Wuhan,China,430074
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-view clustering can partition data samples into their categories by learning a consensus representation in unsupervised way and has received more and more attention in recent years. However, most existing deep clustering methods learn consensus representation or view-specific representations from multiple views via view-wise aggregation way, where they ignore structure relationship of all samples. In this paper, we propose a novel multi-view clustering network to address these problems, called Global and Cross-view Feature Aggregation for Multi-View Clustering (GCFAggMVC). Specifically, the consensus data presentation from multiple views is obtained via cross-sample and cross-view feature aggregation, which fully explores the complementary ofsimilar samples. Moreover, we align the consensus representation and the view-specific representation by the structure-guided contrastive learning module, which makes the view-specific representations from different samples with high structure relationship similar. The proposed module is a flexible multi-view data representation module, which can be also embedded to the incomplete multi-view data clustering task via plugging our module into other frameworks. Extensive experiments show that the proposed method achieves excellent performance in both complete multi-view data clustering tasks and incomplete multi-view data clustering tasks.

</details>

### Cross-Guided Optimization of Radiance Fields with Multi-View Image Super-Resolution for High-Resolution Novel View Synthesis.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01196) · 📚 被引 14
- **作者**: Youngho Yoon, Kuk-Jin Yoon
- **🏷️ 机构**: Visual Intelligence Lab., KAIST,Korea
- **会议**: CVPR 2023

### POEM: Reconstructing Hand in a Point Embedded Multi-view Stereo.
- **链接**: [arXiv:2304.04038](https://arxiv.org/abs/2304.04038) · [代码](https://github.com/lixiny/POEM) · 📚 被引 14
- **作者**: Lixin Yang, Jian Xu, Licheng Zhong, Xinyu Zhan, Zhicheng Wang, Kejian Wu et al.
- **🏷️ 机构**: Shanghai Jiao Tong University, Nreal
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Enable neural networks to capture 3D geometrical-aware features is essential in multi-view based vision tasks. Previous methods usually encode the 3D information of multi-view stereo into the 2D features. In contrast, we present a novel method, named POEM, that directly operates on the 3D POints Embedded in the Multi-view stereo for reconstructing hand mesh in it. Point is a natural form of 3D information and an ideal medium for fusing features across views, as it has different projections on different views. Our method is thus in light of a simple yet effective idea, that a complex 3D hand mesh can be represented by a set of 3D points that 1) are embedded in the multi-view stereo, 2) carry features from the multi-view images, and 3) encircle the hand. To leverage the power of points, we design two operations: point-based feature fusion and cross-set point attention mechanism. Evaluation on three challenging multi-view datasets shows that POEM outperforms the state-of-the-art in hand mesh reconstruction. Code and models are available for research at https://github.com/lixiny/POEM.

</details>

### Adaptive Patch Deformation for Textureless-Resilient Multi-View Stereo.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00162) · 📚 被引 35
- **作者**: Yuesong Wang, Zhaojie Zeng, Tao Guan, Wei Yang, Zhuo Chen, Wenkai Liu et al.
- **🏷️ 机构**: School of Computer Science &#x0026; Technology, Huazhong University of Science &#x0026; Technology, School of Computer Science &#x0026; Technology, Zhejiang University
- **会议**: CVPR 2023

### MetaViewer: Towards A Unified Multi-View Representation.
- **链接**: [arXiv:2303.06329](https://arxiv.org/abs/2303.06329) · 📚 被引 14
- **作者**: Ren Wang, Haoliang Sun, Yuling Ma, Xiaoming Xi, Yilong Yin
- **🏷️ 机构**: Shandong University, Shandong Jianzhu University
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing multi-view representation learning methods typically follow a specific-to-uniform pipeline, extracting latent features from each view and then fusing or aligning them to obtain the unified object representation. However, the manually pre-specify fusion functions and view-private redundant information mixed in features potentially degrade the quality of the derived representation. To overcome them, we propose a novel bi-level-optimization-based multi-view learning framework, where the representation is learned in a uniform-to-specific manner. Specifically, we train a meta-learner, namely MetaViewer, to learn fusion and model the view-shared meta representation in outer-level optimization. Start with this meta representation, view-specific base-learners are then required to rapidly reconstruct the corresponding view in inner-level. MetaViewer eventually updates by observing reconstruction processes from uniform to specific over all views, and learns an optimal fusion scheme that separates and filters out view-private information. Extensive experimental results in downstream tasks such as classification and clustering demonstrate the effectiveness of our method.

</details>

### A Light Touch Approach to Teaching Transformers Multi-view Geometry.
- **链接**: [arXiv:2211.15107](https://arxiv.org/abs/2211.15107) · 📚 被引 10
- **作者**: Yash Bhalgat, João F. Henriques, Andrew Zisserman
- **🏷️ 机构**: University of Oxford,Visual Geometry Group
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Transformers are powerful visual learners, in large part due to their conspicuous lack of manually-specified priors. This flexibility can be problematic in tasks that involve multiple-view geometry, due to the near-infinite possible variations in 3D shapes and viewpoints (requiring flexibility), and the precise nature of projective geometry (obeying rigid laws). To resolve this conundrum, we propose a "light touch" approach, guiding visual Transformers to learn multiple-view geometry but allowing them to break free when needed. We achieve this by using epipolar lines to guide the Transformer's cross-attention maps, penalizing attention values outside the epipolar lines and encouraging higher attention along these lines since they contain geometrically plausible matches. Unlike previous methods, our proposal does not require any camera pose information at test-time. We focus on pose-invariant object instance retrieval, where standard Transformer networks struggle, due to the large differences in viewpoint between query and retrieved images. Experimentally, our method outperforms state-of-the-art approaches at object retrieval, without needing pose information at test-time.

</details>

### Instant Multi-View Head Capture through Learnable Registration.
- **链接**: [arXiv:2306.07437](https://arxiv.org/abs/2306.07437) · 📚 被引 25
- **作者**: Timo Bolkart, Tianye Li, Michael J. Black
- **🏷️ 机构**: MPI for Intelligent Systems,T&#x00FC;bingen, University of Southern California
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing methods for capturing datasets of 3D heads in dense semantic correspondence are slow, and commonly address the problem in two separate steps; multi-view stereo (MVS) reconstruction followed by non-rigid registration. To simplify this process, we introduce TEMPEH (Towards Estimation of 3D Meshes from Performances of Expressive Heads) to directly infer 3D heads in dense correspondence from calibrated multi-view images. Registering datasets of 3D scans typically requires manual parameter tuning to find the right balance between accurately fitting the scans surfaces and being robust to scanning noise and outliers. Instead, we propose to jointly register a 3D head dataset while training TEMPEH. Specifically, during training we minimize a geometric loss commonly used for surface registration, effectively leveraging TEMPEH as a regularizer. Our multi-view head inference builds on a volumetric feature representation that samples and fuses features from each view using camera calibration information. To account for partial occlusions and a large capture volume that enables head movements, we use view- and surface-aware feature fusion, and a spatial transformer-based head localization module, respectively. We use raw MVS scans as supervision during training, but, once trained, TEMPEH directly predicts 3D heads in dense correspondence without requiring scans. Predicting one head takes about 0.3 seconds with a median reconstruction error of 0.26 mm, 64% lower than the current state-of-the-art. This enables the efficient capture of large datasets containing multiple people and diverse facial motions. Code, model, and data are publicly available at https://tempeh.is.tue.mpg.de.

</details>

### RIAV-MVS: Recurrent-Indexing an Asymmetric Volume for Multi-View Stereo.
- **链接**: [arXiv:2205.14320](https://arxiv.org/abs/2205.14320) · [代码](https://github.com/oppo-us-research/riav-mvs) · 📚 被引 12
- **作者**: Changjiang Cai, Pan Ji, Qingan Yan, Yi Xu
- **🏷️ 机构**: OPPO US Research Center, InnoPeak Technology, Inc.
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper presents a learning-based method for multi-view depth estimation from posed images. Our core idea is a "learning-to-optimize" paradigm that iteratively indexes a plane-sweeping cost volume and regresses the depth map via a convolutional Gated Recurrent Unit (GRU). Since the cost volume plays a paramount role in encoding the multi-view geometry, we aim to improve its construction both at pixel- and frame- levels. At the pixel level, we propose to break the symmetry of the Siamese network (which is typically used in MVS to extract image features) by introducing a transformer block to the reference image (but not to the source images). Such an asymmetric volume allows the network to extract global features from the reference image to predict its depth map. Given potential inaccuracies in the poses between reference and source images, we propose to incorporate a residual pose network to correct the relative poses. This essentially rectifies the cost volume at the frame level. We conduct extensive experiments on real-world MVS datasets and show that our method achieves state-of-the-art performance in terms of both within-dataset evaluation and cross-dataset generalization. Code available: https://github.com/oppo-us-research/riav-mvs.

</details>

### Multi-View Azimuth Stereo via Tangent Space Consistency.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00086) · 📚 被引 14
- **作者**: Xu Cao, Hiroaki Santo, Fumio Okura, Yasuyuki Matsushita
- **🏷️ 机构**: Osaka University
- **会议**: CVPR 2023

### GM-NeRF: Learning Generalizable Model-Based Neural Radiance Fields from Multi-View Images.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01978) · 📚 被引 33
- **作者**: Jianchuan Chen, Wentao Yi, Liqian Ma, Xu Jia, Huchuan Lu
- **🏷️ 机构**: Dalian University of Technology,China, ZMO AI Inc.
- **会议**: CVPR 2023

### MAIR: Multi-View Attention Inverse Rendering with 3D Spatially-Varying Lighting Estimation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00811) · 📚 被引 12
- **作者**: Junyong Choi, SeokYeong Lee, Haesol Park, Seung-Won Jung, Ig-Jae Kim, Junghyun Cho
- **🏷️ 机构**: Korea Institute of Science and Technology(KIST), Korea University
- **会议**: CVPR 2023

### 3D Concept Learning and Reasoning from Multi-View Images.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00888) · 📚 被引 42
- **作者**: Yining Hong, Chunru Lin, Yilun Du, Zhenfang Chen, Joshua B. Tenenbaum, Chuang Gan
- **🏷️ 机构**: UCLA, Shanghai Jiaotong University, MIT CSAIL
- **会议**: CVPR 2023

### StyleGAN Salon: Multi-View Latent Optimization for Pose-Invariant Hairstyle Transfer.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00832) · 📚 被引 10
- **作者**: Sasikarn Khwanmuang, Pakkapon Phongthawee, Patsorn Sangkloy, Supasorn Suwajanakorn
- **🏷️ 机构**: VISTEC,Thailand, Phranakhon Rajabhat University,Thailand
- **会议**: CVPR 2023

### Multi-view Inverse Rendering for Large-scale Real-world Indoor Scenes.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01203) · 📚 被引 25
- **作者**: Zhen Li, Lingli Wang, Mofang Cheng, Cihui Pan, Jiaqi Yang
- **🏷️ 机构**: Realsee, Northwestern Polytechnical University
- **会议**: CVPR 2023

### NeuralUDF: Learning Unsigned Distance Fields for Multi-View Reconstruction of Surfaces with Arbitrary Topologies.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01996) · 📚 被引 67
- **作者**: Xiaoxiao Long, Cheng Lin, Lingjie Liu, Yuan Liu, Peng Wang, Christian Theobalt et al.
- **🏷️ 机构**: The University of Hong Kong, Tencent Games, Max Planck Institute for Informatics
- **会议**: CVPR 2023

### NeAT: Learning Neural Implicit Surfaces with Arbitrary Topologies from Multi-View Images.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00032) · 📚 被引 42
- **作者**: Xiaoxu Meng, Weikai Chen, Bo Yang
- **🏷️ 机构**: Digital Content Technology Center, Tencent Games
- **会议**: CVPR 2023

### I2MVFormer: Large Language Model Generated Multi-View Document Supervision for Zero-Shot Image Classification.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01456) · 📚 被引 77
- **作者**: Muhammad Ferjad Naeem, Muhammad Gul Zain Ali Khan, Yongqin Xian, Muhammad Zeshan Afzal, Didier Stricker, Luc Van Gool et al.
- **🏷️ 机构**: ETH Z&#x00FC;rich, TUKL, Google
- **会议**: CVPR 2023

### VolRecon: Volume Rendering of Signed Ray Distance Functions for Generalizable Multi-View Reconstruction.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01601) · 📚 被引 52
- **作者**: Yufan Ren, Fangjinhua Wang, Tong Zhang, Marc Pollefeys, Sabine Süsstrunk
- **🏷️ 机构**: IVRL IC EPFL, ETH Zurich,Department of Computer Science
- **会议**: CVPR 2023

### PermutoSDF: Fast Multi-View Reconstruction with Implicit Surfaces Using Permutohedral Lattices.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00818) · 📚 被引 72
- **作者**: Radu Alexandru Rosu, Sven Behnke
- **🏷️ 机构**: University of Bonn,Germany
- **会议**: CVPR 2023

### BKinD-3D: Self-Supervised 3D Keypoint Discovery from Multi-View Videos.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00869)
- **作者**: Jennifer J. Sun, Lili Karashchuk, Amil Dravid, Serim Ryou, Sonia Fereidooni, John C. Tuthill et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### Replay: Multi-modal Multi-view Acted Videos for Casual Holography.
- **链接**: [arXiv:2307.12067](https://arxiv.org/abs/2307.12067) · 📚 被引 7
- **作者**: Roman Shapovalov, Yanir Kleiman, Ignacio Rocco, David Novotný, Andrea Vedaldi, Changan Chen et al.
- **🏷️ 机构**: Meta
- **会议**: ICCV 2023

### On the Effects of Self-supervision and Contrastive Alignment in Deep Multi-view Clustering.
- **链接**: [arXiv:2303.09877](https://arxiv.org/abs/2303.09877) · 📚 被引 57
- **作者**: Daniel J. Trosten, Sigurd Løkse, Robert Jenssen, Michael C. Kampffmeyer
- **🏷️ 机构**: UiT The Arctic University of Norway,Department of Physics and Technology
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-view image generation attracts particular attention these days due to its promising 3D-related applications, e.g., image viewpoint editing. Most existing methods follow a paradigm where a 3D representation is first synthesized, and then rendered into 2D images to ensure photo-consistency across viewpoints. However, such explicit bias for photo-consistency sacrifices photo-realism, causing geometry artifacts and loss of fine-scale details when these methods are applied to edit real images. To address this issue, we propose ray conditioning, a geometry-free alternative that relaxes the photo-consistency constraint. Our method generates multi-view images by conditioning a 2D GAN on a light field prior. With explicit viewpoint control, state-of-the-art photo-realism and identity consistency, our method is particularly suited for the viewpoint editing task.

</details>

### Multi-view Self-supervised Disentanglement for General Image Denoising.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01128)
- **作者**: Hao Chen, Chenyuan Qu, Yu Zhang, Chen Chen, Jianbo Jiao
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### Trap Attention: Monocular Depth Estimation with Manual Traps.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00487) · 📚 被引 21
- **作者**: Chao Ning, Hongping Gan
- **🏷️ 机构**: Northwestern Polytechnical University,Xi&#x0027;an,China,710072
- **会议**: CVPR 2023

### iDisc: Internal Discretization for Monocular Depth Estimation.
- **链接**: [arXiv:2304.06334](https://arxiv.org/abs/2304.06334) · 📚 被引 120
- **作者**: Luigi Piccinelli, Christos Sakaridis, Fisher Yu
- **🏷️ 机构**: ETH Z&#x00FC;rich,Computer Vision Lab
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular depth estimation is fundamental for 3D scene understanding and downstream applications. However, even under the supervised setup, it is still challenging and ill-posed due to the lack of full geometric constraints. Although a scene can consist of millions of pixels, there are fewer high-level patterns. We propose iDisc to learn those patterns with internal discretized representations. The method implicitly partitions the scene into a set of high-level patterns. In particular, our new module, Internal Discretization (ID), implements a continuous-discrete-continuous bottleneck to learn those concepts without supervision. In contrast to state-of-the-art methods, the proposed model does not enforce any explicit constraints or priors on the depth output. The whole network with the ID module can be trained end-to-end, thanks to the bottleneck module based on attention. Our method sets the new state of the art with significant improvements on NYU-Depth v2 and KITTI, outperforming all published methods on the official KITTI benchmark. iDisc can also achieve state-of-the-art results on surface normal estimation. Further, we explore the model generalization capability via zero-shot testing. We observe the compelling need to promote diversification in the outdoor scenario. Hence, we introduce splits of two autonomous driving datasets, DDAD and Argoverse. Code is available at http://vis.xyz/pub/idisc .

</details>

### Lite-Mono: A Lightweight CNN and Transformer Architecture for Self-Supervised Monocular Depth Estimation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01778)
- **作者**: Ning Zhang, Francesco Nex, George Vosselman, Norman Kerle
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### PlaneDepth: Self-Supervised Depth Estimation via Orthogonal Planes.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02052)
- **作者**: Ruoyu Wang, Zehao Yu, Shenghua Gao
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### DualRefine: Self-Supervised Depth and Pose Estimation Through Iterative Epipolar Sampling and Refinement Toward Equilibrium.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00077)
- **作者**: Antyanta Bangunharcana, Ahmed Magd, Kyung-Soo Kim
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### Fully Self-Supervised Depth Estimation from Defocus Clue.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00882)
- **作者**: Haozhe Si, Bin Zhao, Dong Wang, Yunpeng Gao, Mulin Chen, Zhigang Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

## 跨领域论文（完整笔记在其他领域）

- Viewpoint Equivariance for Multi-View 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- AeDet: Azimuth-Invariant Multi-View 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- X3KD: Knowledge Distillation Across Modalities, Tasks and Stages for Multi-Camera 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Weakly Supervised Monocular 3D Object Detection Using Multi-View Projection and Direction Consistency. → [3d-detection](../3d-detection/Guideline%202023.md)
- Towards Domain Generalization for Multi-view 3D Object Detection in Bird-Eye-View. → [3d-detection](../3d-detection/Guideline%202023.md)
- CAPE: Camera View Position Embedding for Multi-View 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- TBP-Former: Learning Temporal Bird's-Eye-View Pyramid for Joint Perception and Prediction in Vision-Centric Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202023.md)
- FrustumFormer: Adaptive Instance-aware Resampling for Multi-view 3D Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
