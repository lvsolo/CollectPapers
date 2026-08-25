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
- **链接**: [arXiv:2404.01925](https://arxiv.org/abs/2404.01925) · [代码](https://github.com/happytianhao/TaDe) · 📚 被引 14
- **作者**: Tianhao Zhao, Yongcan Chen, Yu Wu, Tianyang Liu, Bo Du, Peilun Xiao et al.
- **🏷️ 机构**: Institute of Artificial Intelligence, School of Computer Science, Hubei Luojia Laboratory, Wuhan University,Wuhan,China, Didi Chuxing,China
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Semantic segmentation in bird's eye view (BEV) plays a crucial role in autonomous driving. Previous methods usually follow an end-to-end pipeline, directly predicting the BEV segmentation map from monocular RGB inputs. However, the challenge arises when the RGB inputs and BEV targets from distinct perspectives, making the direct point-to-point predicting hard to optimize. In this paper, we decompose the original BEV segmentation task into two stages, namely BEV map reconstruction and RGB-BEV feature alignment. In the first stage, we train a BEV autoencoder to reconstruct the BEV segmentation maps given corrupted noisy latent representation, which urges the decoder to learn fundamental knowledge of typical BEV patterns. The second stage involves mapping RGB input images into the BEV latent space of the first stage, directly optimizing the correlations between the two views at the feature level. Our approach simplifies the complexity of combining perception and generation into distinct steps, equipping the model to handle intricate and challenging scenes effectively. Besides, we propose to transform the BEV segmentation map from the Cartesian to the polar coordinate system to establish the column-wise correspondence between RGB images and BEV maps. Moreover, our method requires neither multi-scale features nor camera intrinsic parameters for depth estimation and saves computational overhead. Extensive experiments on nuScenes and Argoverse show the effectiveness and efficiency of our method. Code is available at https://github.com/happytianhao/TaDe.

### SG-BEV: Satellite-Guided BEV Fusion for Cross-View Semantic Segmentation.
- **链接**: [arXiv:2404.02638](https://arxiv.org/abs/2404.02638) · [代码](https://github.com/yejy53/SG-BEV) · 📚 被引 26
- **作者**: Junyan Ye, Qiyan Luo, Jinhua Yu, Huaping Zhong, Zhimeng Zheng, Conghui He et al.
- **🏷️ 机构**: Sun Yat-Sen University, SenseTime Research, Shanghai AI Laboratory
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > This paper aims at achieving fine-grained building attribute segmentation in a cross-view scenario, i.e., using satellite and street-view image pairs. The main challenge lies in overcoming the significant perspective differences between street views and satellite views. In this work, we introduce SG-BEV, a novel approach for satellite-guided BEV fusion for cross-view semantic segmentation. To overcome the limitations of existing cross-view projection methods in capturing the complete building facade features, we innovatively incorporate Bird's Eye View (BEV) method to establish a spatially explicit mapping of street-view features. Moreover, we fully leverage the advantages of multiple perspectives by introducing a novel satellite-guided reprojection module, optimizing the uneven feature distribution issues associated with traditional BEV methods. Our method demonstrates significant improvements on four cross-view datasets collected from multiple cities, including New York, San Francisco, and Boston. On average across these datasets, our method achieves an increase in mIOU by 10.13% and 5.21% compared with the state-of-the-art satellite-based and cross-view methods. The code and datasets of this work will be released at https://github.com/yejy53/SG-BEV.

### PointBeV: A Sparse Approach to BeV Predictions.
- **链接**: [arXiv:2312.00703](https://arxiv.org/abs/2312.00703) · [代码](https://github.com/valeoai/PointBeV) · 📚 被引 22
- **作者**: Loïck Chambon, Éloi Zablocki, Mickaël Chen, Florent Bartoccioni, Patrick Pérez, Matthieu Cord
- **🏷️ 机构**: Valeo.ai,Paris,France, Kyutai,Paris,France
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Bird's-eye View (BeV) representations have emerged as the de-facto shared space in driving applications, offering a unified space for sensor data fusion and supporting various downstream tasks. However, conventional models use grids with fixed resolution and range and face computational inefficiencies due to the uniform allocation of resources across all cells. To address this, we propose PointBeV, a novel sparse BeV segmentation model operating on sparse BeV cells instead of dense grids. This approach offers precise control over memory usage, enabling the use of long temporal contexts and accommodating memory-constrained platforms. PointBeV employs an efficient two-pass strategy for training, enabling focused computation on regions of interest. At inference time, it can be used with various memory/performance trade-offs and flexibly adjusts to new specific use cases. PointBeV achieves state-of-the-art results on the nuScenes dataset for vehicle, pedestrian, and lane segmentation, showcasing superior performance in static and temporal settings despite being trained solely with sparse signals. We will release our code along with two new efficient modules used in the architecture: Sparse Feature Pulling, designed for the effective extraction of features from images to BeV, and Submanifold Attention, which enables efficient temporal modeling. Our code is available at https://github.com/valeoai/PointBeV.

### BerfScene: Bev-conditioned Equivariant Radiance Fields for Infinite 3D Scene Generation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00653) · 📚 被引 1
- **作者**: Qihang Zhang, Yinghao Xu, Yujun Shen, Bo Dai, Bolei Zhou, Ceyuan Yang
- **🏷️ 机构**: CUHK, Stanford, Ant Group
- **会议**: CVPR 2024

## 跨领域论文（完整笔记在其他领域）

- BEVNeXt: Reviving Dense BEV Frameworks for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- RCBEVDet: Radar-Camera Fusion in Bird's Eye View for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- BEVSpread: Spread Voxel Pooling for Bird's-Eye-View Representation in Vision-Based Roadside 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
