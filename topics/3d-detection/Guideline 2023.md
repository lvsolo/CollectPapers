# 3D Detection — 2023 Guideline

> 领域: 3D 目标检测（LiDAR / 相机 / 多模态融合）
> 论文数: 36 · 按重要性排序（引用数/标题信号启发式）

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

- **摘要（英，原文）**:

  > Although DETR-based 3D detectors can simplify the detection pipeline and achieve direct sparse predictions, their performance still lags behind dense detectors with post-processing for 3D object detection from point clouds. DETRs usually adopt a larger number of queries than GTs (e.g., 300 queries v.s. 40 objects in Waymo) in a scene, which inevitably incur many false positives during inference. In this paper, we propose a simple yet effective sparse 3D detector, named Query Contrast Voxel-DETR (ConQueR), to eliminate the challenging false positives, and achieve more accurate and sparser predictions. We observe that most false positives are highly overlapping in local regions, caused by the lack of explicit supervision to discriminate locally similar queries. We thus propose a Query Contrast mechanism to explicitly enhance queries towards their best-matched GTs over all unmatched query predictions. This is achieved by the construction of positive and negative GT-query pairs for each GT, and a contrastive loss to enhance positive GT-query pairs against negative ones based on feature similarities. ConQueR closes the gap of sparse and dense 3D detectors, and reduces up to ~60% false positives. Our single-frame ConQueR achieves new state-of-the-art (sota) 71.6 mAPH/L2 on the challenging Waymo Open Dataset validation set, outperforming previous sota methods (e.g., PV-RCNN++) by over 2.0 mAPH/L2.

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
- **🏷️ 机构**: The Chinese University of Hong Kong, The University of Hong Kong, MEGVII
- **会议**: CVPR 2023

### PiMAE: Point Cloud and Image Interactive Masked Autoencoders for 3D Object Detection.
- **链接**: [arXiv:2303.08129](https://arxiv.org/abs/2303.08129) · [代码](https://github.com/BLVLab/PiMAE) · 📚 被引 78
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
- **链接**: [arXiv:2205.15531](https://arxiv.org/abs/2205.15531) · 📚 被引 34
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
- **链接**: [arXiv:2303.08316](https://arxiv.org/abs/2303.08316) · [代码](https://github.com/skyhehe123/MSF) · 📚 被引 33
- **作者**: Chenhang He, Ruihuang Li, Yabin Zhang, Shuai Li, Lei Zhang
- **🏷️ 机构**: The Hong Kong Polytechnic University
- **会议**: CVPR 2023

- **摘要（英，原文）**:

  > Point cloud sequences are commonly used to accurately detect 3D objects in applications such as autonomous driving. Current top-performing multi-frame detectors mostly follow a Detect-and-Fuse framework, which extracts features from each frame of the sequence and fuses them to detect the objects in the current frame. However, this inevitably leads to redundant computation since adjacent frames are highly correlated. In this paper, we propose an efficient Motion-guided Sequential Fusion (MSF) method, which exploits the continuity of object motion to mine useful sequential contexts for object detection in the current frame. We first generate 3D proposals on the current frame and propagate them to preceding frames based on the estimated velocities. The points-of-interest are then pooled from the sequence and encoded as proposal features. A novel Bidirectional Feature Aggregation (BiFA) module is further proposed to facilitate the interactions of proposal features across frames. Besides, we optimize the point cloud pooling by a voxel-based sampling technique so that millions of points can be processed in several milliseconds. The proposed MSF method achieves not only better efficiency than other multi-frame detectors but also leading accuracy, with 83.12% and 78.30% mAP on the LEVEL1 and LEVEL2 test sets of Waymo Open Dataset, respectively. Codes can be found at \url{https://github.com/skyhehe123/MSF}.

### Density-Insensitive Unsupervised Domain Adaption on 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01684) · 📚 被引 40
- **作者**: Qianjiang Hu, Daizong Liu, Wei Hu
- **🏷️ 机构**: Wangxuan Institute of Computer Technology, Peking University,Beijing,China
- **会议**: CVPR 2023

### MSMDFusion: Fusing LiDAR and Camera at Multiple Scales with Multi-Depth Seeds for 3D Object Detection.
- **链接**: [arXiv:2209.03102](https://arxiv.org/abs/2209.03102) · [代码](https://github.com/SxJyJay/MSMDFusion) · 📚 被引 144
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
- **链接**: [arXiv:2305.04925](https://arxiv.org/abs/2305.04925) · 📚 被引 180
- **作者**: Jinyu Li, Chenxu Luo, Xiaodong Yang
- **🏷️ 机构**: QCraft
- **会议**: CVPR 2023

- **摘要（英，原文）**:

  > In order to deal with the sparse and unstructured raw point clouds, LiDAR based 3D object detection research mostly focuses on designing dedicated local point aggregators for fine-grained geometrical modeling. In this paper, we revisit the local point aggregators from the perspective of allocating computational resources. We find that the simplest pillar based models perform surprisingly well considering both accuracy and latency. Additionally, we show that minimal adaptions from the success of 2D object detection, such as enlarging receptive field, significantly boost the performance. Extensive experiments reveal that our pillar based networks with modernized designs in terms of architecture and training render the state-of-the-art performance on the two popular benchmarks: Waymo Open Dataset and nuScenes. Our results challenge the common intuition that the detailed geometry modeling is essential to achieve high performance for 3D object detection.

### MoDAR: Using Motion Forecasting for 3D Object Detection in Point Cloud Sequences.
- **链接**: [arXiv:2306.03206](https://arxiv.org/abs/2306.03206) · 📚 被引 17
- **作者**: Yingwei Li, Charles R. Qi, Yin Zhou, Chenxi Liu, Dragomir Anguelov
- **🏷️ 机构**: Waymo LLC
- **会议**: CVPR 2023

- **摘要（英，原文）**:

  > Occluded and long-range objects are ubiquitous and challenging for 3D object detection. Point cloud sequence data provide unique opportunities to improve such cases, as an occluded or distant object can be observed from different viewpoints or gets better visibility over time. However, the efficiency and effectiveness in encoding long-term sequence data can still be improved. In this work, we propose MoDAR, using motion forecasting outputs as a type of virtual modality, to augment LiDAR point clouds. The MoDAR modality propagates object information from temporal contexts to a target frame, represented as a set of virtual points, one for each object from a waypoint on a forecasted trajectory. A fused point cloud of both raw sensor points and the virtual points can then be fed to any off-the-shelf point-cloud based 3D object detector. Evaluated on the Waymo Open Dataset, our method significantly improves prior art detectors by using motion forecasting from extra-long sequences (e.g. 18 seconds), achieving new state of the arts, while not adding much computation overhead.

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
- **链接**: [arXiv:2303.08498](https://arxiv.org/abs/2303.08498) · [代码](https://github.com/ADLab-AutoDrive/BEVHeight) · 📚 被引 122
- **作者**: Lei Yang, Kaicheng Yu, Tao Tang, Jun Li, Kun Yuan, Li Wang et al.
- **🏷️ 机构**: Tsinghua University,State Key Laboratory of Automotive Safety and Energy, Autonomous Driving Lab, Alibaba Group, Sun Yat-sen University,Shenzhen Campus
- **会议**: CVPR 2023

- **摘要（英，原文）**:

  > While most recent autonomous driving system focuses on developing perception methods on ego-vehicle sensors, people tend to overlook an alternative approach to leverage intelligent roadside cameras to extend the perception ability beyond the visual range. We discover that the state-of-the-art vision-centric bird's eye view detection methods have inferior performances on roadside cameras. This is because these methods mainly focus on recovering the depth regarding the camera center, where the depth difference between the car and the ground quickly shrinks while the distance increases. In this paper, we propose a simple yet effective approach, dubbed BEVHeight, to address this issue. In essence, instead of predicting the pixel-wise depth, we regress the height to the ground to achieve a distance-agnostic formulation to ease the optimization process of camera-only perception methods. On popular 3D detection benchmarks of roadside cameras, our method surpasses all previous vision-centric methods by a significant margin. The code is available at {\url{https://github.com/ADLab-AutoDrive/BEVHeight}}.

### Bi3D: Bi-Domain Active Learning for Cross-Domain 3D Object Detection.
- **链接**: [arXiv:2303.05886](https://arxiv.org/abs/2303.05886) · [代码](https://github.com/PJLabADG/3DTrans) · 📚 被引 0
- **作者**: Jiakang Yuan, Bo Zhang, Xiangchao Yan, Tao Chen, Botian Shi, Yikang Li et al.
- **🏷️ 机构**: Shanghai AI Lab
- **会议**: CVPR 2023

- **摘要（英，原文）**:

  > Unsupervised Domain Adaptation (UDA) technique has been explored in 3D cross-domain tasks recently. Though preliminary progress has been made, the performance gap between the UDA-based 3D model and the supervised one trained with fully annotated target domain is still large. This motivates us to consider selecting partial-yet-important target data and labeling them at a minimum cost, to achieve a good trade-off between high performance and low annotation cost. To this end, we propose a Bi-domain active learning approach, namely Bi3D, to solve the cross-domain 3D object detection task. The Bi3D first develops a domainness-aware source sampling strategy, which identifies target-domain-like samples from the source domain to avoid the model being interfered by irrelevant source data. Then a diversity-based target sampling strategy is developed, which selects the most informative subset of target domain to improve the model adaptability to the target domain using as little annotation budget as possible. Experiments are conducted on typical cross-domain adaptation scenarios including cross-LiDAR-beam, cross-country, and cross-sensor, where Bi3D achieves a promising target-domain detection accuracy (89.63% on KITTI) compared with UDAbased work (84.29%), even surpassing the detector trained on the full set of the labeled target domain (88.98%). Our code is available at: https://github.com/PJLabADG/3DTrans.

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
- **会议**: CVPR 2023

### MonoATT: Online Monocular 3D Object Detection with Adaptive Token Transformer.
- **链接**: [arXiv:2303.13018](https://arxiv.org/abs/2303.13018) · 📚 被引 45
- **作者**: Yunsong Zhou, Hongzi Zhu, Quan Liu, Shan Chang, Minyi Guo
- **🏷️ 机构**: Shanghai Jiao Tong University, Donghua University
- **会议**: CVPR 2023

- **摘要（英，原文）**:

  > Mobile monocular 3D object detection (Mono3D) (e.g., on a vehicle, a drone, or a robot) is an important yet challenging task. Existing transformer-based offline Mono3D models adopt grid-based vision tokens, which is suboptimal when using coarse tokens due to the limited available computational power. In this paper, we propose an online Mono3D framework, called MonoATT, which leverages a novel vision transformer with heterogeneous tokens of varying shapes and sizes to facilitate mobile Mono3D. The core idea of MonoATT is to adaptively assign finer tokens to areas of more significance before utilizing a transformer to enhance Mono3D. To this end, we first use prior knowledge to design a scoring network for selecting the most important areas of the image, and then propose a token clustering and merging network with an attention mechanism to gradually merge tokens around the selected areas in multiple stages. Finally, a pixel-level feature map is reconstructed from heterogeneous tokens before employing a SOTA Mono3D detector as the underlying detection core. Experiment results on the real-world KITTI dataset demonstrate that MonoATT can effectively improve the Mono3D accuracy for both near and far objects and guarantee low latency. MonoATT yields the best performance compared with the state-of-the-art methods by a large margin and is ranked number one on the KITTI 3D benchmark.

### Understanding the Robustness of 3D Object Detection with Bird'View Representations in Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02069)
- **作者**: Zijian Zhu, Yichi Zhang, Hai Chen, Yinpeng Dong, Shu Zhao, Wenbo Ding et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### Collaboration Helps Camera Overtake LiDAR in 3D Detection.
- **链接**: [arXiv:2303.13560](https://arxiv.org/abs/2303.13560) · [代码](https://github.com/MediaBrain-SJTU/CoCa3D) · 📚 被引 108
- **作者**: Yue Hu, Yifan Lu, Runsheng Xu, Weidi Xie, Siheng Chen, Yanfeng Wang
- **🏷️ 机构**: Shanghai Jiao Tong University,Cooperative Medianet Innovation Center, University of California,Los Angeles, Shanghai AI Laboratory
- **会议**: CVPR 2023

- **摘要（英，原文）**:

  > Camera-only 3D detection provides an economical solution with a simple configuration for localizing objects in 3D space compared to LiDAR-based detection systems. However, a major challenge lies in precise depth estimation due to the lack of direct 3D measurements in the input. Many previous methods attempt to improve depth estimation through network designs, e.g., deformable layers and larger receptive fields. This work proposes an orthogonal direction, improving the camera-only 3D detection by introducing multi-agent collaborations. Our proposed collaborative camera-only 3D detection (CoCa3D) enables agents to share complementary information with each other through communication. Meanwhile, we optimize communication efficiency by selecting the most informative cues. The shared messages from multiple viewpoints disambiguate the single-agent estimated depth and complement the occluded and long-range regions in the single-agent view. We evaluate CoCa3D in one real-world dataset and two new simulation datasets. Results show that CoCa3D improves previous SOTA performances by 44.21% on DAIR-V2X, 30.60% on OPV2V+, 12.59% on CoPerception-UAVs+ for AP@70. Our preliminary results show a potential that with sufficient collaboration, the camera might overtake LiDAR in some practical scenarios. We released the dataset and code at https://siheng-chen.github.io/dataset/CoPerception+ and https://github.com/MediaBrain-SJTU/CoCa3D.

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

### PointDistiller: Structured Knowledge Distillation Towards Efficient and Compact 3D Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02087) · 📚 被引 59
- **作者**: Linfeng Zhang, Runpei Dong, Hung-Shuo Tai, Kaisheng Ma
- **🏷️ 机构**: Tsinghua University, Xi&#x0027;an Jiaotong University, DIDI
- **会议**: CVPR 2023
