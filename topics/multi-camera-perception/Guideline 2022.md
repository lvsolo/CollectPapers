# Multi-camera Perception — 2022 Guideline

> 领域: 多相机 / 多视角感知（环视、深度估计与 3D 预测）
> 论文数: 33 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### MVSalNet: Multi-view Augmentation for RGB-D Salient Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19818-2_16) · 📚 被引 29
- **作者**: Jiayuan Zhou, Lijun Wang, Huchuan Lu, Kaining Huang, Xinchu Shi, Bocong Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Sequential Multi-view Fusion Network for Fast LiDAR Point Motion Estimation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20047-2_17) · 📚 被引 3
- **作者**: Gang Zhang, Xiaoyan Li, Zhenhua Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### RC-MVSNet: Unsupervised Multi-View Stereo with Neural Rendering.
- **链接**: [arXiv:2203.03949](https://arxiv.org/abs/2203.03949) · [代码](https://github.com/Boese0601/RC-MVSNet) · 📚 被引 54
- **作者**: Di Chang, Aljaz Bozic, Tong Zhang, Qingsong Yan, Yingcong Chen, Sabine Süsstrunk et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

- **摘要（英，原文）**:

  > Finding accurate correspondences among different views is the Achilles' heel of unsupervised Multi-View Stereo (MVS). Existing methods are built upon the assumption that corresponding pixels share similar photometric features. However, multi-view images in real scenarios observe non-Lambertian surfaces and experience occlusions. In this work, we propose a novel approach with neural rendering (RC-MVSNet) to solve such ambiguity issues of correspondences among views. Specifically, we impose a depth rendering consistency loss to constrain the geometry features close to the object surface to alleviate occlusions. Concurrently, we introduce a reference view synthesis loss to generate consistent supervision, even for non-Lambertian surfaces. Extensive experiments on DTU and Tanks\&Temples benchmarks demonstrate that our RC-MVSNet approach achieves state-of-the-art performance over unsupervised MVS frameworks and competitive performance to many supervised methods.The code is released at https://github.com/Boese0601/RC-MVSNet

### KD-MVS: Knowledge Distillation Based Self-supervised Learning for Multi-view Stereo.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19821-2_36) · 📚 被引 31
- **作者**: Yikang Ding, Qingtian Zhu, Xiangyue Liu, Wentao Yuan, Haotian Zhang, Chi Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### FLEX: Extrinsic Parameters-free Multi-view 3D Human Motion Reconstruction.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19827-4_11) · 📚 被引 31
- **作者**: Brian Gordon, Sigal Raab, Guy Azov, Raja Giryes, Daniel Cohen-Or
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Depth Field Networks For Generalizable Multi-view Scene Representation.
- **链接**: [arXiv:2207.14287](https://arxiv.org/abs/2207.14287) · 📚 被引 13
- **作者**: Vitor Guizilini, Igor Vasiljevic, Jiading Fang, Rare Ambru, Greg Shakhnarovich, Matthew R. Walter et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

- **摘要（英，原文）**:

  > Modern 3D computer vision leverages learning to boost geometric reasoning, mapping image data to classical structures such as cost volumes or epipolar constraints to improve matching. These architectures are specialized according to the particular problem, and thus require significant task-specific tuning, often leading to poor domain generalization performance. Recently, generalist Transformer architectures have achieved impressive results in tasks such as optical flow and depth estimation by encoding geometric priors as inputs rather than as enforced constraints. In this paper, we extend this idea and propose to learn an implicit, multi-view consistent scene representation, introducing a series of 3D data augmentation techniques as a geometric inductive prior to increase view diversity. We also show that introducing view synthesis as an auxiliary task further improves depth estimation. Our Depth Field Networks (DeFiNe) achieve state-of-the-art results in stereo and video depth estimation without explicit geometric constraints, and improve on zero-shot domain generalization by a wide margin.

### Emotion-aware Multi-view Contrastive Learning for Facial Emotion Recognition.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19778-9_11) · 📚 被引 16
- **作者**: Dae Ha Kim, Byung Cheol Song
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### MODE: Multi-view Omnidirectional Depth Estimation with 360$\circ $ Cameras.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19827-4_12)
- **作者**: Ming Li, Xueqian Jin, Xuejiao Hu, Jingzhao Dai, Sidan Du, Yang Li
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### PPT: Token-Pruned Pose Transformer for Monocular and Multi-view Human Pose Estimation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20065-6_25)
- **作者**: Haoyu Ma, Zhe Wang, Yifei Chen, Deying Kong, Liangjian Chen, Xingwei Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Neural Strands: Learning Hair Geometry and Appearance from Multi-view Images.
- **链接**: [arXiv:2207.14067](https://arxiv.org/abs/2207.14067) · 📚 被引 42
- **作者**: Radu Alexandru Rosu, Shunsuke Saito, Ziyan Wang, Chenglei Wu, Sven Behnke, Giljoo Nam
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

- **摘要（英，原文）**:

  > We present Neural Strands, a novel learning framework for modeling accurate hair geometry and appearance from multi-view image inputs. The learned hair model can be rendered in real-time from any viewpoint with high-fidelity view-dependent effects. Our model achieves intuitive shape and style control unlike volumetric counterparts. To enable these properties, we propose a novel hair representation based on a neural scalp texture that encodes the geometry and appearance of individual strands at each texel location. Furthermore, we introduce a novel neural rendering framework based on rasterization of the learned hair strands. Our neural rendering is strand-accurate and anti-aliased, making the rendering view-consistent and photorealistic. Combining appearance with a multi-view geometric prior, we enable, for the first time, the joint learning of appearance and explicit hair geometry from a multi-view setup. We demonstrate the efficacy of our approach in terms of fidelity and efficiency for various hairstyles.

### MvDeCor: Multi-view Dense Correspondence Learning for Fine-Grained 3D Segmentation.
- **链接**: [arXiv:2208.08580](https://arxiv.org/abs/2208.08580) · 📚 被引 10
- **作者**: Gopal Sharma, Kangxue Yin, Subhransu Maji, Evangelos Kalogerakis, Or Litany, Sanja Fidler
- **🏷️ 机构**: NVIDIA / University of Toronto
- **会议**: ECCV 2022

- **摘要（英，原文）**:

  > We propose to utilize self-supervised techniques in the 2D domain for fine-grained 3D shape segmentation tasks. This is inspired by the observation that view-based surface representations are more effective at modeling high-resolution surface details and texture than their 3D counterparts based on point clouds or voxel occupancy. Specifically, given a 3D shape, we render it from multiple views, and set up a dense correspondence learning task within the contrastive learning framework. As a result, the learned 2D representations are view-invariant and geometrically consistent, leading to better generalization when trained on a limited number of labeled shapes compared to alternatives that utilize self-supervision in 2D or 3D alone. Experiments on textured (RenderPeople) and untextured (PartNet) 3D datasets show that our method outperforms state-of-the-art alternatives in fine-grained part segmentation. The improvements over baselines are greater when only a sparse set of views is available for training or when shapes are textured, indicating that MvDeCor benefits from both 2D processing and 3D geometric reasoning.

### A Real World Dataset for Multi-view 3D Reconstruction.
- **链接**: [arXiv:2203.11397](https://arxiv.org/abs/2203.11397) · 📚 被引 10
- **作者**: Rakesh Shrestha, Siqi Hu, Minghao Gou, Ziyuan Liu, Ping Tan
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

- **摘要（英，原文）**:

  > We present a dataset of 998 3D models of everyday tabletop objects along with their 847,000 real world RGB and depth images. Accurate annotations of camera poses and object poses for each image are performed in a semi-automated fashion to facilitate the use of the dataset for myriad 3D applications like shape reconstruction, object pose estimation, shape retrieval etc. We primarily focus on learned multi-view 3D reconstruction due to the lack of appropriate real world benchmark for the task and demonstrate that our dataset can fill that gap. The entire annotated dataset along with the source code for the annotation tools and evaluation baselines is available at http://www.ocrtoc.org/3d-reconstruction.html.

### MVSTER: Epipolar Transformer for Efficient Multi-view Stereo.
- **链接**: [arXiv:2204.07346](https://arxiv.org/abs/2204.07346) · 📚 被引 115
- **作者**: Xiaofeng Wang, Zheng Zhu, Guan Huang, Fangbo Qin, Yun Ye, Yijia He et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

- **摘要（英，原文）**:

  > Learning-based Multi-View Stereo (MVS) methods warp source images into the reference camera frustum to form 3D volumes, which are fused as a cost volume to be regularized by subsequent networks. The fusing step plays a vital role in bridging 2D semantics and 3D spatial associations. However, previous methods utilize extra networks to learn 2D information as fusing cues, underusing 3D spatial correlations and bringing additional computation costs. Therefore, we present MVSTER, which leverages the proposed epipolar Transformer to learn both 2D semantics and 3D spatial associations efficiently. Specifically, the epipolar Transformer utilizes a detachable monocular depth estimator to enhance 2D semantics and uses cross-attention to construct data-dependent 3D associations along epipolar line. Additionally, MVSTER is built in a cascade structure, where entropy-regularized optimal transport is leveraged to propagate finer depth estimations in each stage. Extensive experiments show MVSTER achieves state-of-the-art reconstruction performance with significantly higher efficiency: Compared with MVSNet and CasMVSNet, our MVSTER achieves 34% and 14% relative improvements on the DTU benchmark, with 80% and 51% relative reductions in running time. MVSTER also ranks first on Tanks&Temples-Advanced among all published works. Code is released at https://github.com/JeffWang987.

### Incomplete Multi-view Domain Adaptation via Channel Enhancement and Knowledge Transfer.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19830-4_12) · 📚 被引 5
- **作者**: Haifeng Xia, Pu Wang, Zhengming Ding
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### PS-NeRF: Neural Inverse Rendering for Multi-view Photometric Stereo.
- **链接**: [arXiv:2207.11406](https://arxiv.org/abs/2207.11406) · 📚 被引 69
- **作者**: Wenqi Yang, Guanying Chen, Chaofeng Chen, Zhenfang Chen, Kwan-Yee K. Wong
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

- **摘要（英，原文）**:

  > Traditional multi-view photometric stereo (MVPS) methods are often composed of multiple disjoint stages, resulting in noticeable accumulated errors. In this paper, we present a neural inverse rendering method for MVPS based on implicit representation. Given multi-view images of a non-Lambertian object illuminated by multiple unknown directional lights, our method jointly estimates the geometry, materials, and lights. Our method first employs multi-light images to estimate per-view surface normal maps, which are used to regularize the normals derived from the neural radiance field. It then jointly optimizes the surface normals, spatially-varying BRDFs, and lights based on a shadow-aware differentiable rendering layer. After optimization, the reconstructed object can be used for novel-view rendering, relighting, and material editing. Experiments on both synthetic and real datasets demonstrate that our method achieves far more accurate shape reconstruction than existing MVPS and neural rendering methods. Our code and model can be found at https://ywq.github.io/psnerf.

### MVDG: A Unified Multi-view Framework for Domain Generalization.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19812-0_10) · 📚 被引 0
- **作者**: Jian Zhang, Lei Qi, Yinghuan Shi, Yang Gao
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Calibration-Free Multi-view Crowd Counting.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20077-9_14) · 📚 被引 13
- **作者**: Qi Zhang, Antoni B. Chan
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### 3D Random Occlusion and Multi-layer Projection for Deep Multi-camera Pedestrian Localization.
- **链接**: [arXiv:2207.10895](https://arxiv.org/abs/2207.10895) · 📚 被引 35
- **作者**: Rui Qiu, Ming Xu, Yuyao Yan, Jeremy S. Smith, Xi Yang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

- **摘要（英，原文）**:

  > Although deep-learning based methods for monocular pedestrian detection have made great progress, they are still vulnerable to heavy occlusions. Using multi-view information fusion is a potential solution but has limited applications, due to the lack of annotated training samples in existing multi-view datasets, which increases the risk of overfitting. To address this problem, a data augmentation method is proposed to randomly generate 3D cylinder occlusions, on the ground plane, which are of the average size of pedestrians and projected to multiple views, to relieve the impact of overfitting in the training. Moreover, the feature map of each view is projected to multiple parallel planes at different heights, by using homographies, which allows the CNNs to fully utilize the features across the height of each pedestrian to infer the locations of pedestrians on the ground plane. The proposed 3DROM method has a greatly improved performance in comparison with the state-of-the-art deep-learning based methods for multi-view pedestrian detection.

### Affine Correspondences Between Multi-camera Systems for 6DOF Relative Pose Estimation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19824-3_37) · 📚 被引 0
- **作者**: Banglei Guan, Ji Zhao
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### RA-Depth: Resolution Adaptive Self-supervised Monocular Depth Estimation.
- **链接**: [arXiv:2207.11984](https://arxiv.org/abs/2207.11984)
- **作者**: Mu He, Le Hui, Yikai Bian, Jian Ren, Jin Xie, Jian Yang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

- **摘要（英，原文）**:

  > Existing self-supervised monocular depth estimation methods can get rid of expensive annotations and achieve promising results. However, these methods suffer from severe performance degradation when directly adopting a model trained on a fixed resolution to evaluate at other different resolutions. In this paper, we propose a resolution adaptive self-supervised monocular depth estimation method (RA-Depth) by learning the scale invariance of the scene depth. Specifically, we propose a simple yet efficient data augmentation method to generate images with arbitrary scales for the same scene. Then, we develop a dual high-resolution network that uses the multi-path encoder and decoder with dense interactions to aggregate multi-scale features for accurate depth inference. Finally, to explicitly learn the scale invariance of the scene depth, we formulate a cross-scale depth consistency loss on depth predictions with different scales. Extensive experiments on the KITTI, Make3D and NYU-V2 datasets demonstrate that RA-Depth not only achieves state-of-the-art performance, but also exhibits a good ability of resolution adaptation.

### Depth Map Decomposition for Monocular Depth Estimation.
- **链接**: [arXiv:2208.10762](https://arxiv.org/abs/2208.10762)
- **作者**: Jinyoung Jun, Jaehan Lee, Chul Lee, Chang-Su Kim
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

- **摘要（英，原文）**:

  > We propose a novel algorithm for monocular depth estimation that decomposes a metric depth map into a normalized depth map and scale features. The proposed network is composed of a shared encoder and three decoders, called G-Net, N-Net, and M-Net, which estimate gradient maps, a normalized depth map, and a metric depth map, respectively. M-Net learns to estimate metric depths more accurately using relative depth features extracted by G-Net and N-Net. The proposed algorithm has the advantage that it can use datasets without metric depth labels to improve the performance of metric depth estimation. Experimental results on various datasets demonstrate that the proposed algorithm not only provides competitive performance to state-of-the-art algorithms but also yields acceptable results even when only a small amount of metric depth data is available for its training.

### Physical Attack on Monocular Depth Estimation with Optimal Adversarial Patches.
- **链接**: [arXiv:2207.04718](https://arxiv.org/abs/2207.04718) · 📚 被引 11
- **作者**: Zhiyuan Cheng, James Liang, Hongjun Choi, Guanhong Tao, Zhiwen Cao, Dongfang Liu et al.
- **🏷️ 机构**: School of Automation, Northwestern Polytechnical University, Xi&#x2019;an, Shaanxi, China
- **会议**: ECCV 2022

- **摘要（英，原文）**:

  > Deep learning has substantially boosted the performance of Monocular Depth Estimation (MDE), a critical component in fully vision-based autonomous driving (AD) systems (e.g., Tesla and Toyota). In this work, we develop an attack against learning-based MDE. In particular, we use an optimization-based method to systematically generate stealthy physical-object-oriented adversarial patches to attack depth estimation. We balance the stealth and effectiveness of our attack with object-oriented adversarial design, sensitive region localization, and natural style camouflage. Using real-world driving scenarios, we evaluate our attack on concurrent MDE models and a representative downstream task for AD (i.e., 3D object detection). Experimental results show that our method can generate stealthy, effective, and robust adversarial patches for different target objects and models and achieves more than 6 meters mean depth estimation error and 93% attack success rate (ASR) in object detection with a patch of 1/9 of the vehicle's rear area. Field tests on three different driving routes with a real vehicle indicate that we cause over 6 meters mean depth estimation error and reduce the object detection rate from 90.70% to 5.16% in continuous video frames.

### BRNet: Exploring Comprehensive Features for Monocular Depth Estimation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19839-7_34) · 📚 被引 40
- **作者**: Wencheng Han, Junbo Yin, Xiaogang Jin, Xiangdong Dai, Jianbing Shen
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Gradient-Based Uncertainty for Monocular Depth Estimation.
- **链接**: [arXiv:2208.02005](https://arxiv.org/abs/2208.02005) · [代码](https://github.com/jhornauer/GrUMoDepth)
- **作者**: Julia Hornauer, Vasileios Belagiannis
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

- **摘要（英，原文）**:

  > In monocular depth estimation, disturbances in the image context, like moving objects or reflecting materials, can easily lead to erroneous predictions. For that reason, uncertainty estimates for each pixel are necessary, in particular for safety-critical applications such as automated driving. We propose a post hoc uncertainty estimation approach for an already trained and thus fixed depth estimation model, represented by a deep neural network. The uncertainty is estimated with the gradients which are extracted with an auxiliary loss function. To avoid relying on ground-truth information for the loss definition, we present an auxiliary loss function based on the correspondence of the depth prediction for an image and its horizontally flipped counterpart. Our approach achieves state-of-the-art uncertainty estimation results on the KITTI and NYU Depth V2 benchmarks without the need to retrain the neural network. Models and code are publicly available at https://github.com/jhornauer/GrUMoDepth.

### Towards Comprehensive Representation Enhancement in Semantics-Guided Self-supervised Monocular Depth Estimation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19769-7_18) · 📚 被引 21
- **作者**: Jingyuan Ma, Xiangyu Lei, Nan Liu, Xian Zhao, Shiliang Pu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Adaptive Co-teaching for Unsupervised Monocular Depth Estimation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19769-7_6)
- **作者**: Weisong Ren, Lijun Wang, Yongri Piao, Miao Zhang, Huchuan Lu, Ting Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Spike Transformer: Monocular Depth Estimation for Spiking Camera.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20071-7_3) · 📚 被引 28
- **作者**: Jiyuan Zhang, Lulu Tang, Zhaofei Yu, Jiwen Lu, Tie-Jun Huang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Towards Scale-Aware, Robust, and Generalizable Unsupervised Monocular Depth Estimation by Integrating IMU Motion Dynamics.
- **链接**: [arXiv:2207.04680](https://arxiv.org/abs/2207.04680) · 📚 被引 38
- **作者**: Sen Zhang, Jing Zhang, Dacheng Tao
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

- **摘要（英，原文）**:

  > Unsupervised monocular depth and ego-motion estimation has drawn extensive research attention in recent years. Although current methods have reached a high up-to-scale accuracy, they usually fail to learn the true scale metric due to the inherent scale ambiguity from training with monocular sequences. In this work, we tackle this problem and propose DynaDepth, a novel scale-aware framework that integrates information from vision and IMU motion dynamics. Specifically, we first propose an IMU photometric loss and a cross-sensor photometric consistency loss to provide dense supervision and absolute scales. To fully exploit the complementary information from both sensors, we further drive a differentiable camera-centric extended Kalman filter (EKF) to update the IMU preintegrated motions when observing visual measurements. In addition, the EKF formulation enables learning an ego-motion uncertainty measure, which is non-trivial for unsupervised methods. By leveraging IMU during training, DynaDepth not only learns an absolute scale, but also provides a better generalization ability and robustness against vision degradation such as illumination change and moving objects. We validate the effectiveness of DynaDepth by conducting extensive experiments and simulations on the KITTI and Make3D datasets.

### Self-distilled Feature Aggregation for Self-supervised Monocular Depth Estimation.
- **链接**: [arXiv:2209.07088](https://arxiv.org/abs/2209.07088) · [代码](https://github.com/ZM-Zhou/SDFA-Net_pytorch)
- **作者**: Zhengming Zhou, Qiulei Dong
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

- **摘要（英，原文）**:

  > Self-supervised monocular depth estimation has received much attention recently in computer vision. Most of the existing works in literature aggregate multi-scale features for depth prediction via either straightforward concatenation or element-wise addition, however, such feature aggregation operations generally neglect the contextual consistency between multi-scale features. Addressing this problem, we propose the Self-Distilled Feature Aggregation (SDFA) module for simultaneously aggregating a pair of low-scale and high-scale features and maintaining their contextual consistency. The SDFA employs three branches to learn three feature offset maps respectively: one offset map for refining the input low-scale feature and the other two for refining the input high-scale feature under a designed self-distillation manner. Then, we propose an SDFA-based network for self-supervised monocular depth estimation, and design a self-distilled training strategy to train the proposed network with the SDFA module. Experimental results on the KITTI dataset demonstrate that the proposed method outperforms the comparative state-of-the-art methods in most cases. The code is available at https://github.com/ZM-Zhou/SDFA-Net_pytorch.

## 跨领域论文（完整笔记在其他领域）

- BEVFormer: Learning Bird's-Eye-View Representation from Multi-camera Images via Spatiotemporal Transformers. → [bev](../bev/Guideline%202022.md)
- SpatialDETR: Robust Scalable Transformer-Based 3D Object Detection From Multi-view Camera Images With Global Cross-Sensor Attention. → [3d-detection](../3d-detection/Guideline%202022.md)
- Semi-supervised Monocular 3D Object Detection by Multi-view Consistency. → [3d-detection](../3d-detection/Guideline%202022.md)
- PETR: Position Embedding Transformation for Multi-view 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
