# Occupancy — 2024 Guideline

> 领域: 占用栅格 / 占用网络（Occupancy Prediction / Occ3D）
> 论文数: 7 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### COTR: Compact Occupancy TRansformer for Vision-Based 3D Occupancy Prediction.
- **链接**: [arXiv:2312.01919](https://arxiv.org/abs/2312.01919) · 📚 被引 49
- **作者**: Qihang Ma, Xin Tan, Yanyun Qu, Lizhuang Ma, Zhizhong Zhang, Yuan Xie
- **🏷️ 机构**: East China Normal University,Shanghai,China, Xiamen University,Fujian,China
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > The autonomous driving community has shown significant interest in 3D occupancy prediction, driven by its exceptional geometric perception and general object recognition capabilities. To achieve this, current works try to construct a Tri-Perspective View (TPV) or Occupancy (OCC) representation extending from the Bird-Eye-View perception. However, compressed views like TPV representation lose 3D geometry information while raw and sparse OCC representation requires heavy but redundant computational costs. To address the above limitations, we propose Compact Occupancy TRansformer (COTR), with a geometry-aware occupancy encoder and a semantic-aware group decoder to reconstruct a compact 3D OCC representation. The occupancy encoder first generates a compact geometrical OCC feature through efficient explicit-implicit view transformation. Then, the occupancy decoder further enhances the semantic discriminability of the compact OCC representation by a coarse-to-fine semantic grouping strategy. Empirical experiments show that there are evident performance gains across multiple baselines, e.g., COTR outperforms baselines with a relative improvement of 8%-15%, demonstrating the superiority of our method.

### Collaborative Semantic Occupancy Prediction with Hybrid Feature Fusion in Connected Automated Vehicles.
- **链接**: [arXiv:2402.07635](https://arxiv.org/abs/2402.07635) · 📚 被引 40
- **作者**: Rui Song, Chenwei Liang, Hu Cao, Zhiran Yan, Walter Zimmer, Markus Gross et al.
- **🏷️ 机构**: Fraunhofer IVI, Technical University of Munich, Technische Hochschule Ingolstadt
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Collaborative perception in automated vehicles leverages the exchange of information between agents, aiming to elevate perception results. Previous camera-based collaborative 3D perception methods typically employ 3D bounding boxes or bird's eye views as representations of the environment. However, these approaches fall short in offering a comprehensive 3D environmental prediction. To bridge this gap, we introduce the first method for collaborative 3D semantic occupancy prediction. Particularly, it improves local 3D semantic occupancy predictions by hybrid fusion of (i) semantic and occupancy task features, and (ii) compressed orthogonal attention features shared between vehicles. Additionally, due to the lack of a collaborative perception dataset designed for semantic occupancy prediction, we augment a current collaborative perception dataset to include 3D collaborative semantic occupancy labels for a more robust evaluation. The experimental findings highlight that: (i) our collaborative semantic occupancy predictions excel above the results from single vehicles by over 30%, and (ii) models anchored on semantic occupancy outpace state-of-the-art collaborative 3D detection techniques in subsequent perception applications, showcasing enhanced accuracy and enriched semantic-awareness in road environments.

### UnO: Unsupervised Occupancy Fields for Perception and Forecasting.
- **链接**: [arXiv:2406.08691](https://arxiv.org/abs/2406.08691) · 📚 被引 19
- **作者**: Ben Agro, Quinlan Sykora, Sergio Casas, Thomas Gilles, Raquel Urtasun
- **🏷️ 机构**: Waabi, University of Toronto
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Perceiving the world and forecasting its future state is a critical task for self-driving. Supervised approaches leverage annotated object labels to learn a model of the world -- traditionally with object detections and trajectory predictions, or temporal bird's-eye-view (BEV) occupancy fields. However, these annotations are expensive and typically limited to a set of predefined categories that do not cover everything we might encounter on the road. Instead, we learn to perceive and forecast a continuous 4D (spatio-temporal) occupancy field with self-supervision from LiDAR data. This unsupervised world model can be easily and effectively transferred to downstream tasks. We tackle point cloud forecasting by adding a lightweight learned renderer and achieve state-of-the-art performance in Argoverse 2, nuScenes, and KITTI. To further showcase its transferability, we fine-tune our model for BEV semantic occupancy forecasting and show that it outperforms the fully supervised state-of-the-art, especially when labeled data is scarce. Finally, when compared to prior state-of-the-art on spatio-temporal geometric occupancy prediction, our 4D world model achieves a much higher recall of objects from classes relevant to self-driving.

### SelfOcc: Self-Supervised Vision-Based 3D Occupancy Prediction.
- **链接**: [arXiv:2311.12754](https://arxiv.org/abs/2311.12754) · [代码](https://github.com/huang-yh/SelfOcc) · 📚 被引 79
- **作者**: Yuanhui Huang, Wenzhao Zheng, Borui Zhang, Jie Zhou, Jiwen Lu
- **🏷️ 机构**: Beijing National Research Center for Information Science and Technology,China, Tsinghua University,Department of Automation,China
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > 3D occupancy prediction is an important task for the robustness of vision-centric autonomous driving, which aims to predict whether each point is occupied in the surrounding 3D space. Existing methods usually require 3D occupancy labels to produce meaningful results. However, it is very laborious to annotate the occupancy status of each voxel. In this paper, we propose SelfOcc to explore a self-supervised way to learn 3D occupancy using only video sequences. We first transform the images into the 3D space (e.g., bird's eye view) to obtain 3D representation of the scene. We directly impose constraints on the 3D representations by treating them as signed distance fields. We can then render 2D images of previous and future frames as self-supervision signals to learn the 3D representations. We propose an MVS-embedded strategy to directly optimize the SDF-induced weights with multiple depth proposals. Our SelfOcc outperforms the previous best method SceneRF by 58.7% using a single frame as input on SemanticKITTI and is the first self-supervised work that produces reasonable 3D occupancy for surround cameras on nuScenes. SelfOcc produces high-quality depth and achieves state-of-the-art results on novel depth synthesis, monocular depth estimation, and surround-view depth estimation on the SemanticKITTI, KITTI-2015, and nuScenes, respectively. Code: https://github.com/huang-yh/SelfOcc.

### Diffusion-FOF: Single-View Clothed Human Reconstruction via Diffusion-Based Fourier Occupancy Field.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00910) · 📚 被引 13
- **作者**: Yuanzhen Li, Fei Luo, Chunxia Xiao
- **🏷️ 机构**: School of Computer Science, Wuhan University,China
- **会议**: CVPR 2024

### SparseOcc: Rethinking Sparse Latent Representation for Vision-Based Semantic Occupancy Prediction.
- **链接**: [arXiv:2404.09502](https://arxiv.org/abs/2404.09502) · 📚 被引 51
- **作者**: Pin Tang, Zhongdao Wang, Guoqing Wang, Jilai Zheng, Xiangxuan Ren, Bailan Feng et al.
- **🏷️ 机构**: MoE Key Lab of Artificial Intelligence, AI Institute, Shanghai Jiao Tong University, Huawei Noah&#x0027;s Ark Lab
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Vision-based perception for autonomous driving requires an explicit modeling of a 3D space, where 2D latent representations are mapped and subsequent 3D operators are applied. However, operating on dense latent spaces introduces a cubic time and space complexity, which limits scalability in terms of perception range or spatial resolution. Existing approaches compress the dense representation using projections like Bird's Eye View (BEV) or Tri-Perspective View (TPV). Although efficient, these projections result in information loss, especially for tasks like semantic occupancy prediction. To address this, we propose SparseOcc, an efficient occupancy network inspired by sparse point cloud processing. It utilizes a lossless sparse latent representation with three key innovations. Firstly, a 3D sparse diffuser performs latent completion using spatially decomposed 3D sparse convolutional kernels. Secondly, a feature pyramid and sparse interpolation enhance scales with information from others. Finally, the transformer head is redesigned as a sparse variant. SparseOcc achieves a remarkable 74.9% reduction on FLOPs over the dense baseline. Interestingly, it also improves accuracy, from 12.8% to 14.1% mIOU, which in part can be attributed to the sparse representation's ability to avoid hallucinations on empty voxels.

### LowRankOcc: Tensor Decomposition and Low-Rank Recovery for Vision-Based 3D Semantic Occupancy Prediction.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00936) · 📚 被引 20
- **作者**: Linqing Zhao, Xiuwei Xu, Ziwei Wang, Yunpeng Zhang, Borui Zhang, Wenzhao Zheng et al.
- **🏷️ 机构**: Tsinghua University,Department of Automation,China, PhiGent Robotics
- **会议**: CVPR 2024
