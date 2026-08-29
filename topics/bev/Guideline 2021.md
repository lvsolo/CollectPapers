# BEV — 2021 Guideline

> 领域: 鸟瞰图感知（BEV 特征、BEV 检测/分割/预测）
> 论文数: 2 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

## 跨领域论文（完整笔记在其他领域）

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Driving requires interacting with road agents and predicting their future behaviour in order to navigate safely. We present FIERY: a probabilistic future prediction model in bird's-eye view from monocular cameras. Our model predicts future instance segmentation and motion of dynamic agents that can be transformed into non-parametric future trajectories. Our approach combines the perception, sensor fusion and prediction components of a traditional autonomous driving stack by estimating bird's-eye-view prediction directly from surround RGB monocular camera inputs. FIERY learns to model the inherent stochastic nature of the future solely from camera driving data in an end-to-end manner, without relying on HD maps, and predicts multimodal future trajectories. We show that our model outperforms previous prediction baselines on the NuScenes and Lyft datasets. The code and trained models are available at https://github.com/wayveai/fiery.

</details>

### BEV-Net: Assessing Social Distancing Compliance by Joint People Localization and Geometric Reasoning.
- **链接**: [arXiv:2110.04931](https://arxiv.org/abs/2110.04931) · 📚 被引 9
- **作者**: Zhirui Dai, Yuepeng Jiang, Yi Li, Bo Liu, Antoni B. Chan, Nuno Vasconcelos
- **🏷️ 机构**: UC San Diego,Department of Electrical and Computer Engineering, Wormpex AI Research, City University of Hong Kong,Department of Computer Science
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Social distancing, an essential public health measure to limit the spread of contagious diseases, has gained significant attention since the outbreak of the COVID-19 pandemic. In this work, the problem of visual social distancing compliance assessment in busy public areas, with wide field-of-view cameras, is considered. A dataset of crowd scenes with people annotations under a bird's eye view (BEV) and ground truth for metric distances is introduced, and several measures for the evaluation of social distance detection systems are proposed. A multi-branch network, BEV-Net, is proposed to localize individuals in world coordinates and identify high-risk regions where social distancing is violated. BEV-Net combines detection of head and feet locations, camera pose estimation, a differentiable homography module to map image into BEV coordinates, and geometric reasoning to produce a BEV map of the people locations in the scene. Experiments on complex crowded scenes demonstrate the power of the approach and show superior performance over baselines derived from methods in the literature. Applications of interest for public health decision makers are finally discussed. Datasets, code and pretrained models are publicly available at GitHub.

</details>

## 🆕 增量新增

### SE-SSD: Self-Ensembling Single-Stage Object Detector From Point Cloud. **⭐⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2104.09804](https://arxiv.org/abs/2104.09804) · 📚 被引 388
- **作者**: Wu Zheng, Weiliang Tang, Li Jiang, Chi-Wing Fu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: 针对点云3D检测中单阶段模型精度不足的问题，提出自集成单阶段检测器SE-SSD。该方法利用教师-学生框架，通过IoU匹配策略过滤软目标并设计一致性损失对齐预测，同时提出形状感知增强和ODIoU损失优化硬目标。在KITTI基准上取得BEV和3D排行榜第一和第二，且推理速度极快。
- **摘要（英）**: This paper addresses the accuracy gap of single-stage 3D detectors by proposing SE-SSD, a self-ensembling framework with teacher-student SSDs. It uses IoU-based matching to filter soft targets, a consistency loss for alignment, shape-aware augmentation, and ODIoU loss for hard targets. It achieves top-1 and top-2 on KITTI BEV and 3D leaderboards with ultra-high inference speed.
- **核心贡献**: 提出自集成单阶段3D检测器，结合软硬目标优化。
- **创新点**: 设计形状感知增强和ODIoU损失，提升单阶段检测精度。
- **结果**: 在KITTI上取得BEV和3D排行榜第一第二。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present Self-Ensembling Single-Stage object Detector (SE-SSD) for accurate and efficient 3D object detection in outdoor point clouds. Our key focus is on exploiting both soft and hard targets with our formulated constraints to jointly optimize the model, without introducing extra computation in the inference. Specifically, SE-SSD contains a pair of teacher and student SSDs, in which we design an effective IoU-based matching strategy to filter soft targets from the teacher and formulate a consistency loss to align student predictions with them. Also, to maximize the distilled knowledge for ensembling the teacher, we design a new augmentation scheme to produce shape-aware augmented samples to train the student, aiming to encourage it to infer complete object shapes. Lastly, to better exploit hard targets, we design an ODIoU loss to supervise the student with constraints on the predicted box centers and orientations. Our SE-SSD attains top performance compared with all prior published works. Also, it attains top precisions for car detection in the KITTI benchmark (ranked 1st and 2nd on the BEV and 3D leaderboards, respectively) with an ultra-high inference speed. The code is available at https://github.com/Vegeta2020/SE-SSD.

</details>

### FIERY: Future Instance Prediction in Bird's-Eye View from Surround Monocular Cameras. **⭐⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01499)
- **作者**: Anthony Hu, Zak Murez, Nikhil Mohan, Sofía Dudas, Jeffrey Hawke, Vijay Badrinarayanan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021
- **摘要（中）**: ①针对多相机环视单目输入下的未来实例预测问题，即预测鸟瞰视角下动态目标的未来轨迹和运动状态。②提出了FIERY模型，利用可学习的鸟瞰投影将多相机特征转换到BEV空间，结合Transformer和概率性未来状态建模，实现端到端的未来实例分割与轨迹预测。③相比以往方法，首次在BEV空间统一处理多相机感知和时序预测，避免了逐相机独立预测的误差累积，并支持可变数量目标的联合推理。④在nuScenes数据集上，FIERY在未来的实例分割和运动预测任务上显著优于基线，展示了在复杂城市场景中的鲁棒性。
- **摘要（英）**: This paper addresses future instance prediction in bird's-eye view from surround monocular cameras, proposing FIERY, which projects multi-camera features into BEV space and uses a Transformer with probabilistic modeling for end-to-end future instance segmentation and trajectory prediction. It improves over prior work by unifying multi-camera perception and temporal forecasting in BEV, reducing error accumulation, and achieves superior performance on nuScenes.
- **核心贡献**: 首次提出端到端的多相机BEV未来实例预测框架，统一了感知与预测。
- **创新点**: 利用可学习BEV投影和Transformer实现多相机特征的时序融合与概率性未来建模。
- **结果**: 在nuScenes上显著超越基线，验证了方法的有效性和鲁棒性。

### 3D Siamese Voxel-to-BEV Tracker for Sparse Point Clouds. **⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2111.04426](https://arxiv.org/abs/2111.04426)
- **作者**: Le Hui, Lingpeng Wang, Mingmei Cheng, Jin Xie, Jian Yang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021
- **摘要（中）**: 针对稀疏点云中3D目标跟踪困难的问题，提出了一种Siamese体素到BEV的跟踪器，包含形状感知特征学习网络和体素到BEV目标定位网络。前者通过模板特征嵌入和密集3D形状生成来捕获物体形状信息，以区分稀疏点云中的目标；后者在BEV特征图上以无锚方式回归目标2D中心和z轴中心。该方法在稀疏点云场景下显著提升了跟踪性能。
- **摘要（英）**: This paper addresses 3D object tracking in sparse point clouds by proposing a Siamese voxel-to-BEV tracker with a shape-aware feature learning network and a voxel-to-BEV localization network. The former captures 3D shape information to identify targets, while the latter regresses 2D center and z-axis center in an anchor-free manner. It significantly improves tracking performance in sparse environments.
- **核心贡献**: 提出Siamese体素到BEV跟踪器，结合形状感知和BEV定位提升稀疏点云跟踪性能。
- **创新点**: 利用模板特征嵌入生成密集3D形状，并在BEV上无锚回归。
- **结果**: 在稀疏点云场景中显著提升跟踪性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D object tracking in point clouds is still a challenging problem due to the sparsity of LiDAR points in dynamic environments. In this work, we propose a Siamese voxel-to-BEV tracker, which can significantly improve the tracking performance in sparse 3D point clouds. Specifically, it consists of a Siamese shape-aware feature learning network and a voxel-to-BEV target localization network. The Siamese shape-aware feature learning network can capture 3D shape information of the object to learn the discriminative features of the object so that the potential target from the background in sparse point clouds can be identified. To this end, we first perform template feature embedding to embed the template's feature into the potential target and then generate a dense 3D shape to characterize the shape information of the potential target. For localizing the tracked target, the voxel-to-BEV target localization network regresses the target's 2D center and the $z$-axis center from the dense bird's eye view (BEV) feature map in an anchor-free manner. Concretely, we compress the voxelized point cloud along $z$-axis through max pooling to obtain a dense BEV feature map, where the regression of the 2D center and the $z$-axis center can be performed more effectively. Extensive evaluation on the KITTI and nuScenes datasets shows that our method significantly outperforms the current state-of-the-art methods by a large margin.

</details>
<!-- COMPLETE v1 papers=4 -->
