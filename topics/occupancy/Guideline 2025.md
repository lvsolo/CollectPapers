# Occupancy — 2025 Guideline

> 领域: 占用栅格 / 占用网络（Occupancy Prediction / Occ3D）
> 论文数: 9 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Rethinking Temporal Fusion with a Unified Gradient Descent View for 3D Semantic Occupancy Prediction.
- **链接**: [arXiv:2504.12959](https://arxiv.org/abs/2504.12959) · 📚 被引 4
- **作者**: Dubing Chen, Huan Zheng, Jin Fang, Xingping Dong, Xianfei Li, Wenlong Liao et al.
- **🏷️ 机构**: SKL-IOTSC, CIS, University of Macau, Wuhan University, Cowarobot Co. Ltd.
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce GaussianOcc, a systematic method that investigates the two usages of Gaussian splatting for fully self-supervised and efficient 3D occupancy estimation in surround views. First, traditional methods for self-supervised 3D occupancy estimation still require ground truth 6D poses from sensors during training. To address this limitation, we propose Gaussian Splatting for Projection (GSP) module to provide accurate scale information for fully self-supervised training from adjacent view projection. Additionally, existing methods rely on volume rendering for final 3D voxel representation learning using 2D signals (depth maps, semantic maps), which is both time-consuming and less effective. We propose Gaussian Splatting from Voxel space (GSV) to leverage the fast rendering properties of Gaussian splatting. As a result, the proposed GaussianOcc method enables fully self-supervised (no ground truth pose) 3D occupancy estimation in competitive performance with low computational cost (2.7 times faster in training and 5 times faster in rendering). The relevant code is available in https://github.com/GANWANSHUI/GaussianOcc.git.

</details>

### QuadricFormer: Scene as Superquadrics for 3D Semantic Occupancy Prediction.
- **链接**: [arXiv:2506.10977](https://arxiv.org/abs/2506.10977) · 📚 被引 0
- **作者**: Sicheng Zuo, Wenzhao Zheng, Xiaoyong Han, Longchao Yang, Yong Pan, Jiwen Lu
- **🏷️ 机构**: Tsinghua University, University of California, Berkeley, Li Auto Inc.
- **会议**: NeurIPS 2025

### EvOcc: Accurate Semantic Occupancy for Automated Driving Using Evidence Theory.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Kalble_EvOcc_Accurate_Semantic_Occupancy_for_Automated_Driving_Using_Evidence_Theory_CVPR_2025_paper.html) · 📚 被引 1
- **作者**: Jonas Kälble, Sascha Wirges, Maxim Tatarchenko, Eddy Ilg
- **🏷️ 机构**: Bosch Center for Artificial Intelligence, University of Technology Nuremberg
- **会议**: CVPR 2025

### OccMamba: Semantic Occupancy Prediction with State Space Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Li_OccMamba_Semantic_Occupancy_Prediction_with_State_Space_Models_CVPR_2025_paper.html) · 📚 被引 11
- **作者**: Heng Li, Yuenan Hou, Xiaohan Xing, Yuexin Ma, Xiao Sun, Yanyong Zhang
- **🏷️ 机构**: University of Science and Technology of China, Shanghai AI Laboratory, Stanford University
- **会议**: CVPR 2025

### STCOcc: Sparse Spatial-Temporal Cascade Renovation for 3D Occupancy and Scene Flow Prediction.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Liao_STCOcc_Sparse_Spatial-Temporal_Cascade_Renovation_for_3D_Occupancy_and_Scene_CVPR_2025_paper.html) · 📚 被引 5
- **作者**: Zhimin Liao, Ping Wei, Shuaijia Chen, Haoxuan Wang, Ziyang Ren
- **🏷️ 机构**: Xi&#x2019;an Jiaotong University,National Key Laboratory of Human-Machine Hybrid Augmented Intelligence Institute of Artificial Intelligence and Robotics
- **会议**: CVPR 2025

### 3D Occupancy Prediction with Low-Resolution Queries via Prototype-aware View Transformation.
- **链接**: [arXiv:2503.15185](https://arxiv.org/abs/2503.15185) · 📚 被引 1
- **作者**: Gyeongrok Oh, Sungjune Kim, Heeju Ko, Hyung-gun Chi, Jinkyu Kim, Dongwook Lee et al.
- **🏷️ 机构**: Korea University, Purdue University, Samsung Electronics,AI Center, DS Division
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The resolution of voxel queries significantly influences the quality of view transformation in camera-based 3D occupancy prediction. However, computational constraints and the practical necessity for real-time deployment require smaller query resolutions, which inevitably leads to an information loss. Therefore, it is essential to encode and preserve rich visual details within limited query sizes while ensuring a comprehensive representation of 3D occupancy. To this end, we introduce ProtoOcc, a novel occupancy network that leverages prototypes of clustered image segments in view transformation to enhance low-resolution context. In particular, the mapping of 2D prototypes onto 3D voxel queries encodes high-level visual geometries and complements the loss of spatial information from reduced query resolutions. Additionally, we design a multi-perspective decoding strategy to efficiently disentangle the densely compressed visual cues into a high-dimensional 3D occupancy scene. Experimental results on both Occ3D and SemanticKITTI benchmarks demonstrate the effectiveness of the proposed method, showing clear improvements over the baselines. More importantly, ProtoOcc achieves competitive performance against the baselines even with 75\% reduced voxel resolution.

</details>

### GaussianWorld: Gaussian World Model for Streaming 3D Occupancy Prediction.
- **链接**: [arXiv:2412.10373](https://arxiv.org/abs/2412.10373) · 📚 被引 13
- **作者**: Sicheng Zuo, Wenzhao Zheng, Yuanhui Huang, Jie Zhou, Jiwen Lu
- **🏷️ 机构**: Tsinghua University,Department of Automation,China
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D occupancy prediction is important for autonomous driving due to its comprehensive perception of the surroundings. To incorporate sequential inputs, most existing methods fuse representations from previous frames to infer the current 3D occupancy. However, they fail to consider the continuity of driving scenarios and ignore the strong prior provided by the evolution of 3D scenes (e.g., only dynamic objects move). In this paper, we propose a world-model-based framework to exploit the scene evolution for perception. We reformulate 3D occupancy prediction as a 4D occupancy forecasting problem conditioned on the current sensor input. We decompose the scene evolution into three factors: 1) ego motion alignment of static scenes; 2) local movements of dynamic objects; and 3) completion of newly-observed scenes. We then employ a Gaussian world model (GaussianWorld) to explicitly exploit these priors and infer the scene evolution in the 3D Gaussian space considering the current RGB observation. We evaluate the effectiveness of our framework on the widely used nuScenes dataset. Our GaussianWorld improves the performance of the single-frame counterpart by over 2% in mIoU without introducing additional computations. Code: https://github.com/zuosc19/GaussianWorld.

</details>

## 跨领域论文（完整笔记在其他领域）

- TopNet: Transformer-Efficient Occupancy Prediction Network for Octree-Structured Point Cloud Geometry Compression. → [network-pruning](../network-pruning/Guideline%202025.md)
- SDGOCC: Semantic and Depth-Guided Bird's-Eye View Transformation for 3D Multimodal Occupancy Prediction. → [bev](../bev/Guideline%202025.md)
