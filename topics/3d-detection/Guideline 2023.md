# 3D Detection — 2023 Guideline

> 领域: 3D 目标检测（LiDAR / 相机 / 多模态融合）
> 论文数: 34 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Omni3D: A Large Benchmark and Model for 3D Object Detection in the Wild.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01264) · 📚 被引 106
- **作者**: Garrick Brazil, Abhinav Kumar, Julian Straub, Nikhila Ravi, Justin Johnson, Georgia Gkioxari
- **🏷️ 机构**: Meta AI, Michigan State University, Caltech
- **会议**: CVPR 2023

### ConQueR: Query Contrast Voxel-DETR for 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00897) · 📚 被引 30
- **作者**: Benjin Zhu, Zhe Wang, Shaoshuai Shi, Hang Xu, Lanqing Hong, Hongsheng Li
- **🏷️ 机构**: CUHK
- **会议**: CVPR 2023

### AShapeFormer : Semantics-Guided Object-Level Active Shape Encoding for 3D Object Detection via Transformers.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00104) · 📚 被引 19
- **作者**: Zechuan Li, Hongshan Yu, Zhengeng Yang, Tom Tongjia Chen, Naveed Akhtar
- **🏷️ 机构**: Hunan University, The University of Western Australia
- **会议**: CVPR 2023

### Viewpoint Equivariance for Multi-View 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00889)
- **作者**: Dian Chen, Jie Li, Vitor Guizilini, Rares Ambrus, Adrien Gaidon
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### VoxelNeXt: Fully Sparse VoxelNet for 3D Object Detection and Tracking.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02076) · 📚 被引 448
- **作者**: Yukang Chen, Jianhui Liu, Xiangyu Zhang, Xiaojuan Qi, Jiaya Jia
- **🏷️ 机构**: MEGVII, CUHK / SmartMore
- **会议**: CVPR 2023

### PiMAE: Point Cloud and Image Interactive Masked Autoencoders for 3D Object Detection.
- **链接**: [arXiv:2303.08129](https://arxiv.org/abs/2303.08129) · [出版页](https://doi.org/10.1109/CVPR52729.2023.00512) · [代码](https://github.com/BLVLab/PiMAE) · 📚 被引 77
- **作者**: Anthony Chen, Kevin Zhang, Renrui Zhang, Zihan Wang, Yuheng Lu, Yandong Guo et al.
- **🏷️ 机构**: School of Computer Science, Peking University,National Key Laboratory for Multimedia Information Processing, The Chinese University of Hong Kong, Beijing University of Posts and Telecommunications
- **会议**: CVPR 2023

- **摘要（英，原文）**:

  > Masked Autoencoders learn strong visual representations and achieve state-of-the-art results in several independent modalities, yet very few works have addressed their capabilities in multi-modality settings. In this work, we focus on point cloud and RGB image data, two modalities that are often presented together in the real world, and explore their meaningful interactions. To improve upon the cross-modal synergy in existing works, we propose PiMAE, a self-supervised pre-training framework that promotes 3D and 2D interaction through three aspects. Specifically, we first notice the importance of masking strategies between the two sources and utilize a projection module to complementarily align the mask and visible tokens of the two modalities. Then, we utilize a well-crafted two-branch MAE pipeline with a novel shared decoder to promote cross-modality interaction in the mask tokens. Finally, we design a unique cross-modal reconstruction module to enhance representation learning for both modalities. Through extensive experiments performed on large-scale RGB-D scene understanding benchmarks (SUN RGB-D and ScannetV2), we discover it is nontrivial to interactively learn point-image features, where we greatly improve multiple 3D detectors, 2D detectors, and few-shot classifiers by 2.9%, 6.7%, and 2.4%, respectively. Code is available at https://github.com/BLVLab/PiMAE.

### BEV-SAN: Accurate BEV 3D Object Detection via Slice Attention Networks.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01675)
- **作者**: Xiaowei Chi, Jiaming Liu, Ming Lu, Rongyu Zhang, Zhaoqing Wang, Yandong Guo et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### itKD: Interchange Transfer-based Knowledge Distillation for 3D Object Detection.
- **链接**: [arXiv:2205.15531](https://arxiv.org/abs/2205.15531) · [出版页](https://doi.org/10.1109/CVPR52729.2023.01301) · 📚 被引 34
- **作者**: Hyeon Cho, Junyong Choi, Geonwoo Baek, Wonjun Hwang
- **🏷️ 机构**: Ajou University
- **会议**: CVPR 2023

- **摘要（英，原文）**:

  > Point-cloud based 3D object detectors recently have achieved remarkable progress. However, most studies are limited to the development of network architectures for improving only their accuracy without consideration of the computational efficiency. In this paper, we first propose an autoencoder-style framework comprising channel-wise compression and decompression via interchange transfer-based knowledge distillation. To learn the map-view feature of a teacher network, the features from teacher and student networks are independently passed through the shared autoencoder; here, we use a compressed representation loss that binds the channel-wised compression knowledge from both student and teacher networks as a kind of regularization. The decompressed features are transferred in opposite directions to reduce the gap in the interchange reconstructions. Lastly, we present an head attention loss to match the 3D object detection information drawn by the multi-head self-attention mechanism. Through extensive experiments, we verify that our method can train the lightweight model that is well-aligned with the 3D point cloud detection task and we demonstrate its superiority using the well-known public datasets; e.g., Waymo and nuScenes.

### Benchmarking Robustness of 3D Object Detection to Common Corruptions in Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00105)
- **作者**: Yinpeng Dong, Caixin Kang, Jinlai Zhang, Zijian Zhu, Yikai Wang, Xiao Yang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### AeDet: Azimuth-Invariant Multi-View 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02067)
- **作者**: Chengjian Feng, Zequn Jie, Yujie Zhong, Xiangxiang Chu, Lin Ma
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### MSF: Motion-guided Sequential Fusion for Efficient 3D Object Detection from Point Cloud Sequences.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00503) · 📚 被引 33
- **作者**: Chenhang He, Ruihuang Li, Yabin Zhang, Shuai Li, Lei Zhang
- **🏷️ 机构**: PolyU / OPPO
- **会议**: CVPR 2023

### Density-Insensitive Unsupervised Domain Adaption on 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01684) · 📚 被引 40
- **作者**: Qianjiang Hu, Daizong Liu, Wei Hu
- **🏷️ 机构**: Wangxuan Institute of Computer Technology, Peking University,Beijing,China
- **会议**: CVPR 2023

### MSMDFusion: Fusing LiDAR and Camera at Multiple Scales with Multi-Depth Seeds for 3D Object Detection.
- **链接**: [arXiv:2209.03102](https://arxiv.org/abs/2209.03102) · [出版页](https://doi.org/10.1109/CVPR52729.2023.02073) · [代码](https://github.com/SxJyJay/MSMDFusion) · 📚 被引 144
- **作者**: Yang Jiao, Zequn Jie, Shaoxiang Chen, Jingjing Chen, Lin Ma, Yu-Gang Jiang
- **🏷️ 机构**: School of CS, Fudan University,Shanghai Key Lab of Intell. Info. Processing, Meituan
- **会议**: CVPR 2023

- **摘要（英，原文）**:

  > Fusing LiDAR and camera information is essential for achieving accurate and reliable 3D object detection in autonomous driving systems. This is challenging due to the difficulty of combining multi-granularity geometric and semantic features from two drastically different modalities. Recent approaches aim at exploring the semantic densities of camera features through lifting points in 2D camera images (referred to as seeds) into 3D space, and then incorporate 2D semantics via cross-modal interaction or fusion techniques. However, depth information is under-investigated in these approaches when lifting points into 3D space, thus 2D semantics can not be reliably fused with 3D points. Moreover, their multi-modal fusion strategy, which is implemented as concatenation or attention, either can not effectively fuse 2D and 3D information or is unable to perform fine-grained interactions in the voxel space. To this end, we propose a novel framework with better utilization of the depth information and fine-grained cross-modal interaction between LiDAR and camera, which consists of two important components. First, a Multi-Depth Unprojection (MDU) method with depth-aware designs is used to enhance the depth quality of the lifted points at each interaction level. Second, a Gated Modality-Aware Convolution (GMA-Conv) block is applied to modulate voxels involved with the camera modality in a fine-grained manner and then aggregate multi-modal features into a unified space. Together they provide the detection head with more comprehensive features from LiDAR and camera. On the nuScenes test benchmark, our proposed method, abbreviated as MSMDFusion, achieves state-of-the-art 3D object detection results with 71.5% mAP and 74.0% NDS, and strong tracking results with 74.0% AMOTA without using test-time-augmentation and ensemble techniques. The code is available at https://github.com/SxJyJay/MSMDFusion.

### X3KD: Knowledge Distillation Across Modalities, Tasks and Stages for Multi-Camera 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01282)
- **作者**: Marvin Klingner, Shubhankar Borse, Varun Ravi Kumar, Behnaz Rezaei, Venkatraman Narayanan, Senthil Kumar Yogamani et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### LoGoNet: Towards Accurate 3D Object Detection with Local-to-Global Cross- Modal Fusion.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01681) · 📚 被引 181
- **作者**: Xin Li, Tao Ma, Yuenan Hou, Botian Shi, Yuchen Yang, Youquan Liu et al.
- **🏷️ 机构**: The Chinese University of Hong Kong, Shanghai AI Laboratory, Fudan University
- **会议**: CVPR 2023

### PillarNeXt: Rethinking Network Designs for 3D Object Detection in LiDAR Point Clouds.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01685) · 📚 被引 180
- **作者**: Jinyu Li, Chenxu Luo, Xiaodong Yang
- **🏷️ 机构**: QCraft
- **会议**: CVPR 2023

### MoDAR: Using Motion Forecasting for 3D Object Detection in Point Cloud Sequences.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00900) · 📚 被引 17
- **作者**: Yingwei Li, Charles R. Qi, Yin Zhou, Chenxi Liu, Dragomir Anguelov
- **🏷️ 机构**: Waymo
- **会议**: CVPR 2023

### Deep Dive into Gradients: Better Optimization for 3D Object Detection with Gradient-Corrected IoU Supervision.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00497) · 📚 被引 15
- **作者**: Qi Ming, Lingjuan Miao, Zhe Ma, Lin Zhao, Zhiqiang Zhou, Xuhui Huang et al.
- **🏷️ 机构**: School of Automation, Beijing Institute of Technology,China
- **会议**: CVPR 2023

### Weakly Supervised Monocular 3D Object Detection Using Multi-View Projection and Direction Consistency.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01677)
- **作者**: Runzhou Tao, Wencheng Han, Zhongying Qiu, Cheng-Zhong Xu, Jianbing Shen
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### Towards Domain Generalization for Multi-view 3D Object Detection in Bird-Eye-View.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01281)
- **作者**: Shuo Wang, Xinhai Zhao, Hai-Ming Xu, Zehui Chen, Dameng Yu, Jiahao Chang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### Semi-Supervised Stereo-Based 3D Object Detection via Cross-View Consensus.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01676) · 📚 被引 5
- **作者**: Wenhao Wu, Hau-San Wong, Si Wu
- **🏷️ 机构**: City University of Hong Kong,Department of Computer Science, School of Computer Science and Engineering, South China University of Technology
- **会议**: CVPR 2023

### Virtual Sparse Convolution for Multimodal 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02074)
- **作者**: Hai Wu, Chenglu Wen, Shaoshuai Shi, Xin Li, Cheng Wang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### CAPE: Camera View Position Embedding for Multi-View 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02066)
- **作者**: Kaixin Xiong, Shi Gong, Xiaoqing Ye, Xiao Tan, Ji Wan, Errui Ding et al.
- **🏷️ 机构**: HUAST
- **会议**: CVPR 2023

### BEVHeight: A Robust Framework for Vision-based Roadside 3D Object Detection.
- **链接**: [arXiv:2303.08498](https://arxiv.org/abs/2303.08498) · [出版页](https://doi.org/10.1109/CVPR52729.2023.02070) · [代码](https://github.com/ADLab-AutoDrive/BEVHeight) · 📚 被引 122
- **作者**: Lei Yang, Kaicheng Yu, Tao Tang, Jun Li, Kun Yuan, Li Wang et al.
- **🏷️ 机构**: Tsinghua University,State Key Laboratory of Automotive Safety and Energy, Autonomous Driving Lab, Alibaba Group, Sun Yat-sen University,Shenzhen Campus
- **会议**: CVPR 2023

- **摘要（英，原文）**:

  > While most recent autonomous driving system focuses on developing perception methods on ego-vehicle sensors, people tend to overlook an alternative approach to leverage intelligent roadside cameras to extend the perception ability beyond the visual range. We discover that the state-of-the-art vision-centric bird's eye view detection methods have inferior performances on roadside cameras. This is because these methods mainly focus on recovering the depth regarding the camera center, where the depth difference between the car and the ground quickly shrinks while the distance increases. In this paper, we propose a simple yet effective approach, dubbed BEVHeight, to address this issue. In essence, instead of predicting the pixel-wise depth, we regress the height to the ground to achieve a distance-agnostic formulation to ease the optimization process of camera-only perception methods. On popular 3D detection benchmarks of roadside cameras, our method surpasses all previous vision-centric methods by a significant margin. The code is available at {\url{https://github.com/ADLab-AutoDrive/BEVHeight}}.

### Bi3D: Bi-Domain Active Learning for Cross-Domain 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01497) · 📚 被引 0
- **作者**: Jiakang Yuan, Bo Zhang, Xiangchao Yan, Tao Chen, Botian Shi, Yikang Li et al.
- **🏷️ 机构**: Shanghai AI Lab
- **会议**: CVPR 2023

### Distilling Focal Knowledge from Imperfect Expert for 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00102) · 📚 被引 13
- **作者**: Jia Zeng, Li Chen, Hanming Deng, Lewei Lu, Junchi Yan, Yu Qiao et al.
- **🏷️ 机构**: Shanghai AI Lab
- **会议**: CVPR 2023

### Uni3D: A Unified Baseline for Multi-Dataset 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00893) · 📚 被引 43
- **作者**: Bo Zhang, Jiakang Yuan, Botian Shi, Tao Chen, Yikang Li, Yu Qiao
- **🏷️ 机构**: Shanghai AI Lab
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
- **会议**: CVPR 2023

### MonoATT: Online Monocular 3D Object Detection with Adaptive Token Transformer.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01678) · 📚 被引 45
- **作者**: Yunsong Zhou, Hongzi Zhu, Quan Liu, Shan Chang, Minyi Guo
- **🏷️ 机构**: Shanghai Jiao Tong University, Donghua University
- **会议**: CVPR 2023

### Understanding the Robustness of 3D Object Detection with Bird'View Representations in Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02069)
- **作者**: Zijian Zhu, Yichi Zhang, Hai Chen, Yinpeng Dong, Shu Zhao, Wenbo Ding et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### Collaboration Helps Camera Overtake LiDAR in 3D Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00892) · 📚 被引 108
- **作者**: Yue Hu, Yifan Lu, Runsheng Xu, Weidi Xie, Siheng Chen, Yanfeng Wang
- **🏷️ 机构**: Shanghai Jiao Tong University,Cooperative Medianet Innovation Center, University of California,Los Angeles, Shanghai AI Laboratory
- **会议**: CVPR 2023

### MV-JAR: Masked Voxel Jigsaw and Reconstruction for LiDAR-Based Self-Supervised Pre-Training.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01292)
- **作者**: Runsen Xu, Tai Wang, Wenwei Zhang, Runjian Chen, Jinkun Cao, Jiangmiao Pang et al.
- **🏷️ 机构**: CUHK
- **会议**: CVPR 2023

### PointDistiller: Structured Knowledge Distillation Towards Efficient and Compact 3D Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02087) · 📚 被引 59
- **作者**: Linfeng Zhang, Runpei Dong, Hung-Shuo Tai, Kaisheng Ma
- **🏷️ 机构**: Tsinghua University, Xi&#x0027;an Jiaotong University, DIDI
- **会议**: CVPR 2023
