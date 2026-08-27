# 3D Detection — 2022 Guideline

> 领域: 3D 目标检测（LiDAR / 相机 / 多模态融合）
> 论文数: 24 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Deformable Feature Aggregation for Dynamic Multi-modal 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20074-8_36)
- **作者**: Zehui Chen, Zhenyu Li, Shiquan Zhang, Liangji Fang, Qinhong Jiang, Feng Zhao
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### SpatialDETR: Robust Scalable Transformer-Based 3D Object Detection From Multi-view Camera Images With Global Cross-Sensor Attention.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19842-7_14)
- **作者**: Simon Doll, Richard Schulz, Lukas Schneider, Viviane Benzin, Markus Enzweiler, Hendrik P. A. Lensch
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### 3D Object Detection with a Self-supervised Lidar Scene Flow Backbone.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20080-9_15) · 📚 被引 25
- **作者**: Emeç Erçelik, Ekim Yurtsever, Mingyu Liu, Zhijie Yang, Hanzhen Zhang, Pinar Topçam et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Cross-Modality Knowledge Distillation Network for Monocular 3D Object Detection.
- **链接**: [arXiv:2211.07171](https://arxiv.org/abs/2211.07171)
- **作者**: Yu Hong, Hang Dai, Yong Ding
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

- **摘要（英，原文）**:

  > Leveraging LiDAR-based detectors or real LiDAR point data to guide monocular 3D detection has brought significant improvement, e.g., Pseudo-LiDAR methods. However, the existing methods usually apply non-end-to-end training strategies and insufficiently leverage the LiDAR information, where the rich potential of the LiDAR data has not been well exploited. In this paper, we propose the Cross-Modality Knowledge Distillation (CMKD) network for monocular 3D detection to efficiently and directly transfer the knowledge from LiDAR modality to image modality on both features and responses. Moreover, we further extend CMKD as a semi-supervised training framework by distilling knowledge from large-scale unlabeled data and significantly boost the performance. Until submission, CMKD ranks $1^{st}$ among the monocular 3D detectors with publications on both KITTI $test$ set and Waymo $val$ set with significant performance gains compared to previous state-of-the-art methods.

### CramNet: Camera-Radar Fusion with Ray-Constrained Cross-Attention for Robust 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19839-7_23) · 📚 被引 57
- **作者**: Jyh-Jing Hwang, Henrik Kretzschmar, Joshua Manela, Sean Rafferty, Nicholas Armstrong-Crews, Tiffany L. Chen et al.
- **🏷️ 机构**: Waymo
- **会议**: ECCV 2022

### DEVIANT: Depth EquiVarIAnt NeTwork for Monocular 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20077-9_39) · 📚 被引 69
- **作者**: Abhinav Kumar, Garrick Brazil, Enrique Corona, Armin Parchami, Xiaoming Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Densely Constrained Depth Estimator for Monocular 3D Object Detection.
- **链接**: [arXiv:2207.10047](https://arxiv.org/abs/2207.10047) · [代码](https://github.com/BraveGroup/DCD)
- **作者**: Yingyan Li, Yuntao Chen, Jiawei He, Zhaoxiang Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

- **摘要（英，原文）**:

  > Estimating accurate 3D locations of objects from monocular images is a challenging problem because of lacking depth. Previous work shows that utilizing the object's keypoint projection constraints to estimate multiple depth candidates boosts the detection performance. However, the existing methods can only utilize vertical edges as projection constraints for depth estimation. So these methods only use a small number of projection constraints and produce insufficient depth candidates, leading to inaccurate depth estimation. In this paper, we propose a method that utilizes dense projection constraints from edges of any direction. In this way, we employ much more projection constraints and produce considerable depth candidates. Besides, we present a graph matching weighting module to merge the depth candidates. The proposed method DCD (Densely Constrained Detector) achieves state-of-the-art performance on the KITTI and WOD benchmarks. Code is released at https://github.com/BraveGroup/DCD.

### Unsupervised Domain Adaptation for Monocular 3D Object Detection via Self-training.
- **链接**: [arXiv:2204.11590](https://arxiv.org/abs/2204.11590)
- **作者**: Zhenyu Li, Zehui Chen, Ang Li, Liangji Fang, Qinhong Jiang, Xianming Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

- **摘要（英，原文）**:

  > Monocular 3D object detection (Mono3D) has achieved unprecedented success with the advent of deep learning techniques and emerging large-scale autonomous driving datasets. However, drastic performance degradation remains an unwell-studied challenge for practical cross-domain deployment as the lack of labels on the target domain. In this paper, we first comprehensively investigate the significant underlying factor of the domain gap in Mono3D, where the critical observation is a depth-shift issue caused by the geometric misalignment of domains. Then, we propose STMono3D, a new self-teaching framework for unsupervised domain adaptation on Mono3D. To mitigate the depth-shift, we introduce the geometry-aligned multi-scale training strategy to disentangle the camera parameters and guarantee the geometry consistency of domains. Based on this, we develop a teacher-student paradigm to generate adaptive pseudo labels on the target domain. Benefiting from the end-to-end framework that provides richer information of the pseudo labels, we propose the quality-aware supervision strategy to take instance-level pseudo confidences into account and improve the effectiveness of the target-domain training process. Moreover, the positive focusing training strategy and dynamic threshold are proposed to handle tremendous FN and FP pseudo samples. STMono3D achieves remarkable performance on all evaluated datasets and even surpasses fully supervised results on the KITTI 3D object detection dataset. To the best of our knowledge, this is the first study to explore effective UDA methods for Mono3D.

### Homogeneous Multi-modal Feature Fusion and Interaction for 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19839-7_40)
- **作者**: Xin Li, Botian Shi, Yuenan Hou, Xingjiao Wu, Tianlong Ma, Yikang Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Enhancing Multi-modal Features Using Local Self-attention for 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20080-9_31)
- **作者**: Hao Li, Zehan Zhang, Xian Zhao, Yulong Wang, Yuxi Shen, Shiliang Pu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Semi-supervised Monocular 3D Object Detection by Multi-view Consistency.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20074-8_41)
- **作者**: Qing Lian, Yanbo Xu, Weilong Yao, Yingcong Chen, Tong Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### PETR: Position Embedding Transformation for Multi-view 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19812-0_31)
- **作者**: Yingfei Liu, Tiancai Wang, Xiangyu Zhang, Jian Sun
- **🏷️ 机构**: MEGVII
- **会议**: ECCV 2022

### Lidar Point Cloud Guided Monocular 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19769-7_8)
- **作者**: Liang Peng, Fei Liu, Zhengxu Yu, Senbo Yan, Dan Deng, Zheng Yang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### DID-M3D: Decoupling Instance Depth for Monocular 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19769-7_5) · 📚 被引 78
- **作者**: Liang Peng, Xiaopei Wu, Zheng Yang, Haifeng Liu, Deng Cai
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### FCAF3D: Fully Convolutional Anchor-Free 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20080-9_28) · 📚 被引 125
- **作者**: Danila Rukhovich, Anna Vorontsova, Anton Konushin
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Rethinking IoU-based Optimization for Single-stage 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20077-9_32)
- **作者**: Hualian Sheng, Sijia Cai, Na Zhao, Bing Deng, Jianqiang Huang, Xian-Sheng Hua et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### PillarNet: Real-Time and High-Performance Pillar-Based 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20080-9_3) · 📚 被引 210
- **作者**: Guangsheng Shi, Ruifeng Li, Chao Ma
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### SWFormer: Sparse Window Transformer for 3D Object Detection in Point Clouds.
- **链接**: [arXiv:2210.07372](https://arxiv.org/abs/2210.07372) · 📚 被引 129
- **作者**: Pei Sun, Mingxing Tan, Weiyue Wang, Chenxi Liu, Fei Xia, Zhaoqi Leng et al.
- **🏷️ 机构**: Waymo
- **会议**: ECCV 2022

- **摘要（英，原文）**:

  > 3D object detection in point clouds is a core component for modern robotics and autonomous driving systems. A key challenge in 3D object detection comes from the inherent sparse nature of point occupancy within the 3D scene. In this paper, we propose Sparse Window Transformer (SWFormer ), a scalable and accurate model for 3D object detection, which can take full advantage of the sparsity of point clouds. Built upon the idea of window-based Transformers, SWFormer converts 3D points into sparse voxels and windows, and then processes these variable-length sparse windows efficiently using a bucketing scheme. In addition to self-attention within each spatial window, our SWFormer also captures cross-window correlation with multi-scale feature fusion and window shifting operations. To further address the unique challenge of detecting 3D objects accurately from sparse features, we propose a new voxel diffusion technique. Experimental results on the Waymo Open Dataset show our SWFormer achieves state-of-the-art 73.36 L2 mAPH on vehicle and pedestrian for 3D object detection on the official test set, outperforming all previous single-stage and two-stage models, while being much more efficient.

### Monocular 3D Object Detection with Depth from Motion.
- **链接**: [arXiv:2207.12988](https://arxiv.org/abs/2207.12988) · [代码](https://github.com/Tai-Wang/Depth-from-Motion)
- **作者**: Tai Wang, Jiangmiao Pang, Dahua Lin
- **🏷️ 机构**: CUHK
- **会议**: ECCV 2022

- **摘要（英，原文）**:

  > Perceiving 3D objects from monocular inputs is crucial for robotic systems, given its economy compared to multi-sensor settings. It is notably difficult as a single image can not provide any clues for predicting absolute depth values. Motivated by binocular methods for 3D object detection, we take advantage of the strong geometry structure provided by camera ego-motion for accurate object depth estimation and detection. We first make a theoretical analysis on this general two-view case and notice two challenges: 1) Cumulative errors from multiple estimations that make the direct prediction intractable; 2) Inherent dilemmas caused by static cameras and matching ambiguity. Accordingly, we establish the stereo correspondence with a geometry-aware cost volume as the alternative for depth estimation and further compensate it with monocular understanding to address the second problem. Our framework, named Depth from Motion (DfM), then uses the established geometry to lift 2D image features to the 3D space and detects 3D objects thereon. We also present a pose-free DfM to make it usable when the camera pose is unavailable. Our framework outperforms state-of-the-art methods by a large margin on the KITTI benchmark. Detailed quantitative and qualitative analyses also validate our theoretical conclusions. The code will be released at https://github.com/Tai-Wang/Depth-from-Motion.

### LiDAR Distillation: Bridging the Beam-Induced Domain Gap for 3D Object Detection.
- **链接**: [arXiv:2203.14956](https://arxiv.org/abs/2203.14956)
- **作者**: Yi Wei, Zibu Wei, Yongming Rao, Jiaxin Li, Jie Zhou, Jiwen Lu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

- **摘要（英，原文）**:

  > In this paper, we propose the LiDAR Distillation to bridge the domain gap induced by different LiDAR beams for 3D object detection. In many real-world applications, the LiDAR points used by mass-produced robots and vehicles usually have fewer beams than that in large-scale public datasets. Moreover, as the LiDARs are upgraded to other product models with different beam amount, it becomes challenging to utilize the labeled data captured by previous versions' high-resolution sensors. Despite the recent progress on domain adaptive 3D detection, most methods struggle to eliminate the beam-induced domain gap. We find that it is essential to align the point cloud density of the source domain with that of the target domain during the training process. Inspired by this discovery, we propose a progressive framework to mitigate the beam-induced domain shift. In each iteration, we first generate low-beam pseudo LiDAR by downsampling the high-beam point clouds. Then the teacher-student framework is employed to distill rich information from the data with more beams. Extensive experiments on Waymo, nuScenes and KITTI datasets with three different LiDAR-based detectors demonstrate the effectiveness of our LiDAR Distillation. Notably, our approach does not increase any additional computation cost for inference.

### Graph R-CNN: Towards Accurate 3D Object Detection with Semantic-Decorated Local Graph.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20074-8_38) · 📚 被引 83
- **作者**: Honghui Yang, Zili Liu, Xiaopei Wu, Wenxiao Wang, Wei Qian, Xiaofei He et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Semi-supervised 3D Object Detection with Proficient Teachers.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19839-7_42) · 📚 被引 73
- **作者**: Junbo Yin, Jin Fang, Dingfu Zhou, Liangjun Zhang, Cheng-Zhong Xu, Jianbing Shen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### ProposalContrast: Unsupervised Pre-training for LiDAR-Based 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19842-7_2) · 📚 被引 85
- **作者**: Junbo Yin, Dingfu Zhou, Liangjun Zhang, Jin Fang, Cheng-Zhong Xu, Jianbing Shen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### CenterFormer: Center-Based Transformer for 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19839-7_29) · 📚 被引 162
- **作者**: Zixiang Zhou, Xiangchen Zhao, Yu Wang, Panqu Wang, Hassan Foroosh
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
