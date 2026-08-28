# BEV — 2024 Guideline

> 领域: 鸟瞰图感知（BEV 特征、BEV 检测/分割/预测）
> 论文数: 21 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: [2022](Guideline%202022.md)

### From a Bird's Eye View to See: Joint Camera and Subject Registration without the Camera Calibration. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2212.09298](https://arxiv.org/abs/2212.09298) · 📚 被引 10
- **作者**: Zekun Qian, Ruize Han, Wei Feng, Song Wang
- **🏷️ 机构**: College of Intelligence and Computing, Tianjin University, Shenzhen Institute of Advanced Technology, Chinese Academy of Sciences, University of South Carolina
- **会议**: CVPR 2024
- **摘要（中）**: 针对无相机标定情况下多视角相机和主体在鸟瞰图中的联合注册问题，该论文提出了一种端到端框架。它通过视图变换主体检测模块将第一视角转换为虚拟BEV，利用几何变换估计相机位置和方向，并结合空间和外观信息聚合主体。在合成数据集上验证了方法的有效性，为无标定BEV感知提供了新思路。
- **摘要（英）**: This paper tackles the challenging problem of joint camera and subject registration in BEV without pre-given calibration, by proposing an end-to-end framework with a view-transform detection module, geometric-based camera registration, and spatial-appearance aggregation. Experiments on a synthetic dataset demonstrate remarkable effectiveness, offering a novel approach for uncalibrated BEV perception.
- **核心贡献**: 提出无相机标定的BEV联合注册框架。
- **创新点**: 结合视图变换和几何估计实现相机与主体注册。
- **结果**: 在合成数据集上验证了方法的有效性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We tackle a new problem of multi-view camera and subject registration in the bird's eye view (BEV) without pre-given camera calibration. This is a very challenging problem since its only input is several RGB images from different first-person views (FPVs) for a multi-person scene, without the BEV image and the calibration of the FPVs, while the output is a unified plane with the localization and orientation of both the subjects and cameras in a BEV. We propose an end-to-end framework solving this problem, whose main idea can be divided into following parts: i) creating a view-transform subject detection module to transform the FPV to a virtual BEV including localization and orientation of each pedestrian, ii) deriving a geometric transformation based method to estimate camera localization and view direction, i.e., the camera registration in a unified BEV, iii) making use of spatial and appearance information to aggregate the subjects into the unified BEV. We collect a new large-scale synthetic dataset with rich annotations for evaluation. The experimental results show the remarkable effectiveness of our proposed method.

</details>

### SG-BEV: Satellite-Guided BEV Fusion for Cross-View Semantic Segmentation. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2404.02638](https://arxiv.org/abs/2404.02638) · 📚 被引 26
- **作者**: Junyan Ye, Qiyan Luo, Jinhua Yu, Huaping Zhong, Zhimeng Zheng, Conghui He et al.
- **🏷️ 机构**: Sun Yat-Sen University, SenseTime Research, Shanghai AI Laboratory
- **会议**: CVPR 2024
- **摘要（中）**: 针对跨视角（卫星与街景）语义分割中视角差异大、建筑立面特征捕获不完整的问题，提出SG-BEV方法，创新性地引入BEV建立街景特征的空间显式映射，并设计卫星引导的重投影模块以优化传统BEV方法的特征分布不均问题。在纽约、旧金山、波士顿等四个跨视角数据集上，平均mIOU相比最先进的卫星基和跨视角方法分别提升10.13%和5.21%。
- **摘要（英）**: This paper introduces SG-BEV for cross-view semantic segmentation, using BEV to map street-view features and a satellite-guided reprojection module to address feature distribution issues. It achieves average mIOU improvements of 10.13% and 5.21% over state-of-the-art satellite-based and cross-view methods on four datasets.
- **核心贡献**: 提出了卫星引导的BEV融合框架，解决了跨视角分割中的特征映射和分布不均问题。
- **创新点**: 创新性地将BEV与卫星引导重投影结合，优化了多视角特征融合。
- **结果**: 在多个城市数据集上mIOU显著提升，优于现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper aims at achieving fine-grained building attribute segmentation in a cross-view scenario, i.e., using satellite and street-view image pairs. The main challenge lies in overcoming the significant perspective differences between street views and satellite views. In this work, we introduce SG-BEV, a novel approach for satellite-guided BEV fusion for cross-view semantic segmentation. To overcome the limitations of existing cross-view projection methods in capturing the complete building facade features, we innovatively incorporate Bird's Eye View (BEV) method to establish a spatially explicit mapping of street-view features. Moreover, we fully leverage the advantages of multiple perspectives by introducing a novel satellite-guided reprojection module, optimizing the uneven feature distribution issues associated with traditional BEV methods. Our method demonstrates significant improvements on four cross-view datasets collected from multiple cities, including New York, San Francisco, and Boston. On average across these datasets, our method achieves an increase in mIOU by 10.13% and 5.21% compared with the state-of-the-art satellite-based and cross-view methods. The code and datasets of this work will be released at https://github.com/yejy53/SG-BEV.

</details>

### BerfScene: Bev-conditioned Equivariant Radiance Fields for Infinite 3D Scene Generation. **⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2312.02136](https://arxiv.org/abs/2312.02136) · 📚 被引 1
- **作者**: Qihang Zhang, Yinghao Xu, Yujun Shen, Bo Dai, Bolei Zhou, Ceyuan Yang
- **🏷️ 机构**: CUHK, Stanford, Ant Group
- **会议**: CVPR 2024
- **摘要（中）**: 针对大规模3D场景生成中复杂空间配置和多尺度物体的问题，提出BerfScene，结合BEV地图引导的等变辐射场。通过BEV地图控制物体操作，并利用位置编码和低通滤波器实现等变性，支持生成无限规模的3D场景。实验在多个3D场景数据集上验证了有效性。
- **摘要（英）**: BerfScene introduces a BEV-conditioned equivariant radiance field for large-scale 3D scene generation, enabling object manipulation via BEV maps and infinite scene synthesis through equivariance. Experiments on 3D scene datasets demonstrate effectiveness.
- **核心贡献**: 提出了BEV条件等变辐射场，支持大规模和无限3D场景生成。
- **创新点**: 创新性地利用BEV地图引导辐射场，实现场景的等变生成和拼接。
- **结果**: 在3D场景数据集上验证了生成效果和可控性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Generating large-scale 3D scenes cannot simply apply existing 3D object synthesis technique since 3D scenes usually hold complex spatial configurations and consist of a number of objects at varying scales. We thus propose a practical and efficient 3D representation that incorporates an equivariant radiance field with the guidance of a bird's-eye view (BEV) map. Concretely, objects of synthesized 3D scenes could be easily manipulated through steering the corresponding BEV maps. Moreover, by adequately incorporating positional encoding and low-pass filters into the generator, the representation becomes equivariant to the given BEV map. Such equivariance allows us to produce large-scale, even infinite-scale, 3D scenes via synthesizing local scenes and then stitching them with smooth consistency. Extensive experiments on 3D scene datasets demonstrate the effectiveness of our approach. Our project website is at https://zqh0253.github.io/BerfScene/.

</details>

## 跨领域论文（完整笔记在其他领域）

- CLIP-BEVFormer: Enhancing Multi-View Image-Based BEV Detector with Ground Truth Flow. → [3d-detection](../3d-detection/Guideline%202024.md)
- SeaBird: Segmentation in Bird's View with Dice Loss Improves Monocular 3D Detection of Large Objects. → [3d-detection](../3d-detection/Guideline%202024.md)
- GAFusion: Adaptive Fusing LiDAR and Camera with Multiple Guidance for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- BEVNeXt: Reviving Dense BEV Frameworks for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- UniMODE: Unified Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- RCBEVDet: Radar-Camera Fusion in Bird's Eye View for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- BEVSpread: Spread Voxel Pooling for Bird's-Eye-View Representation in Vision-Based Roadside 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- IS-Fusion: Instance-Scene Collaborative Fusion for Multimodal 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- Decoupled Pseudo-Labeling for Semi-Supervised Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- CRKD: Enhanced Camera-Radar Object Detection with Cross-Modality Knowledge Distillation. → [3d-detection](../3d-detection/Guideline%202024.md)
- Improving Bird's Eye View Semantic Segmentation by Task Decomposition. → [autonomous-driving](../autonomous-driving/Guideline%202024.md)
- PointBeV: A Sparse Approach to BeV Predictions. → [autonomous-driving](../autonomous-driving/Guideline%202024.md)
- UnO: Unsupervised Occupancy Fields for Perception and Forecasting. → [autonomous-driving](../autonomous-driving/Guideline%202024.md)
- SelfOcc: Self-Supervised Vision-Based 3D Occupancy Prediction. → [3d-detection](../3d-detection/Guideline%202024.md)
- SparseOcc: Rethinking Sparse Latent Representation for Vision-Based Semantic Occupancy Prediction. → [3d-detection](../3d-detection/Guideline%202024.md)
- DrivingGaussian: Composite Gaussian Splatting for Surrounding Dynamic Autonomous Driving Scenes. → [autonomous-driving](../autonomous-driving/Guideline%202024.md)
- Is Ego Status All You Need for Open-Loop End-to-End Autonomous Driving? → [autonomous-driving](../autonomous-driving/Guideline%202024.md)
- Multiagent Multitraversal Multimodal Self-Driving: Open MARS Dataset. → [autonomous-driving](../autonomous-driving/Guideline%202024.md)
