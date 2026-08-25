# BEV — 2024 Guideline

> 领域: 鸟瞰图感知（BEV 特征、BEV 检测/分割/预测）
> 论文数: 9 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### CLIP-BEVFormer: Enhancing Multi-View Image-Based BEV Detector with Ground Truth Flow.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01441)
- **作者**: Chenbin Pan, Burhaneddin Yaman, Senem Velipasalar, Liu Ren
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### From a Bird's Eye View to See: Joint Camera and Subject Registration without the Camera Calibration.
- **链接**: [arXiv:2212.09298](https://arxiv.org/abs/2212.09298) · 📚 被引 10
- **作者**: Zekun Qian, Ruize Han, Wei Feng, Song Wang
- **🏷️ 机构**: College of Intelligence and Computing, Tianjin University, Shenzhen Institute of Advanced Technology, Chinese Academy of Sciences, University of South Carolina
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > We tackle a new problem of multi-view camera and subject registration in the bird's eye view (BEV) without pre-given camera calibration. This is a very challenging problem since its only input is several RGB images from different first-person views (FPVs) for a multi-person scene, without the BEV image and the calibration of the FPVs, while the output is a unified plane with the localization and orientation of both the subjects and cameras in a BEV. We propose an end-to-end framework solving this problem, whose main idea can be divided into following parts: i) creating a view-transform subject detection module to transform the FPV to a virtual BEV including localization and orientation of each pedestrian, ii) deriving a geometric transformation based method to estimate camera localization and view direction, i.e., the camera registration in a unified BEV, iii) making use of spatial and appearance information to aggregate the subjects into the unified BEV. We collect a new large-scale synthetic dataset with rich annotations for evaluation. The experimental results show the remarkable effectiveness of our proposed method.

### Improving Bird's Eye View Semantic Segmentation by Task Decomposition.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01469) · 📚 被引 14
- **作者**: Tianhao Zhao, Yongcan Chen, Yu Wu, Tianyang Liu, Bo Du, Peilun Xiao et al.
- **🏷️ 机构**: Institute of Artificial Intelligence, School of Computer Science, Hubei Luojia Laboratory, Wuhan University,Wuhan,China, Didi Chuxing,China
- **会议**: CVPR 2024

### SG-BEV: Satellite-Guided BEV Fusion for Cross-View Semantic Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02621) · 📚 被引 26
- **作者**: Junyan Ye, Qiyan Luo, Jinhua Yu, Huaping Zhong, Zhimeng Zheng, Conghui He et al.
- **🏷️ 机构**: Sun Yat-Sen University, SenseTime Research, Shanghai AI Laboratory
- **会议**: CVPR 2024

### PointBeV: A Sparse Approach to BeV Predictions.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01439) · 📚 被引 22
- **作者**: Loïck Chambon, Éloi Zablocki, Mickaël Chen, Florent Bartoccioni, Patrick Pérez, Matthieu Cord
- **🏷️ 机构**: Valeo.ai,Paris,France, Kyutai,Paris,France
- **会议**: CVPR 2024

### BerfScene: Bev-conditioned Equivariant Radiance Fields for Infinite 3D Scene Generation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00653) · 📚 被引 1
- **作者**: Qihang Zhang, Yinghao Xu, Yujun Shen, Bo Dai, Bolei Zhou, Ceyuan Yang
- **🏷️ 机构**: CUHK, Stanford, Ant Group
- **会议**: CVPR 2024

## 跨领域论文（完整笔记在其他领域）

- BEVNeXt: Reviving Dense BEV Frameworks for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- RCBEVDet: Radar-Camera Fusion in Bird's Eye View for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- BEVSpread: Spread Voxel Pooling for Bird's-Eye-View Representation in Vision-Based Roadside 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
