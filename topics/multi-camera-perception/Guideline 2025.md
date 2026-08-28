# Multi-camera Perception — 2025 Guideline

> 领域: 多相机 / 多视角感知（环视、深度估计与 3D 预测）
> 论文数: 11 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### SiM3D: Single-Instance Multiview Multimodal and Multisetup 3D Anomaly Detection Benchmark.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01947)
- **作者**: Alex Costanzino, Pierluigi Zama Ramirez, Luigi Lella, Matteo Ragaglia, Alessandro Oliva, Giuseppe Lisanti et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### ForeSight: Multi-View Streaming Joint Object Detection and Trajectory Forecasting.
- **链接**: [arXiv:2508.07089](https://arxiv.org/abs/2508.07089) · 📚 被引 2
- **作者**: Sandro Papais, Letian Wang, Brian Cheong, Steven L. Waslander
- **🏷️ 机构**: University of Toronto
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce ForeSight, a novel joint detection and forecasting framework for vision-based 3D perception in autonomous vehicles. Traditional approaches treat detection and forecasting as separate sequential tasks, limiting their ability to leverage temporal cues. ForeSight addresses this limitation with a multi-task streaming and bidirectional learning approach, allowing detection and forecasting to share query memory and propagate information seamlessly. The forecast-aware detection transformer enhances spatial reasoning by integrating trajectory predictions from a multiple hypothesis forecast memory queue, while the streaming forecast transformer improves temporal consistency using past forecasts and refined detections. Unlike tracking-based methods, ForeSight eliminates the need for explicit object association, reducing error propagation with a tracking-free model that efficiently scales across multi-frame sequences. Experiments on the nuScenes dataset show that ForeSight achieves state-of-the-art performance, achieving an EPA of 54.9%, surpassing previous methods by 9.3%, while also attaining the best mAP and minADE among multi-view detection and forecasting models.

</details>

### Point Cloud Self-Supervised Learning via 3D to Multi-View Masked Learner.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02564)
- **作者**: Zhimin Chen, Xuewei Chen, Xiao Guo, Yingwei Li, Longlong Jing, Liang Yang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### Multi-View 3D Point Tracking.
- **链接**: [arXiv:2508.21060](https://arxiv.org/abs/2508.21060)
- **作者**: Frano Rajic, Haofei Xu, Marko Mihajlovic, Siyuan Li, Irem Demir, Emircan Gündogdu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce the first data-driven multi-view 3D point tracker, designed to track arbitrary points in dynamic scenes using multiple camera views. Unlike existing monocular trackers, which struggle with depth ambiguities and occlusion, or prior multi-camera methods that require over 20 cameras and tedious per-sequence optimization, our feed-forward model directly predicts 3D correspondences using a practical number of cameras (e.g., four), enabling robust and accurate online tracking. Given known camera poses and either sensor-based or estimated multi-view depth, our tracker fuses multi-view features into a unified point cloud and applies k-nearest-neighbors correlation alongside a transformer-based update to reliably estimate long-range 3D correspondences, even under occlusion. We train on 5K synthetic multi-view Kubric sequences and evaluate on two real-world benchmarks: Panoptic Studio and DexYCB, achieving median trajectory errors of 3.1 cm and 2.0 cm, respectively. Our method generalizes well to diverse camera setups of 1-8 views with varying vantage points and video lengths of 24-150 frames. By releasing our tracker alongside training and evaluation datasets, we aim to set a new standard for multi-view 3D tracking research and provide a practical tool for real-world applications. Project page available at https://ethz-vlg.github.io/mvtracker.

</details>

### MVTrajecter: Multi-View Pedestrian Tracking With Trajectory Motion Cost and Trajectory Appearance Cost.
- **链接**: [arXiv:2509.01157](https://arxiv.org/abs/2509.01157) · 📚 被引 1
- **作者**: Taiga Yamane, Ryo Masumura, Satoshi Suzuki, Shota Orihashi
- **🏷️ 机构**: NTT Corporation,NTT Human Informatics Laboratries
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-View Pedestrian Tracking (MVPT) aims to track pedestrians in the form of a bird's eye view occupancy map from multi-view videos. End-to-end methods that detect and associate pedestrians within one model have shown great progress in MVPT. The motion and appearance information of pedestrians is important for the association, but previous end-to-end MVPT methods rely only on the current and its single adjacent past timestamp, discarding the past trajectories before that. This paper proposes a novel end-to-end MVPT method called Multi-View Trajectory Tracker (MVTrajecter) that utilizes information from multiple timestamps in past trajectories for robust association. MVTrajecter introduces trajectory motion cost and trajectory appearance cost to effectively incorporate motion and appearance information, respectively. These costs calculate which pedestrians at the current and each past timestamp are likely identical based on the information between those timestamps. Even if a current pedestrian could be associated with a false pedestrian at some past timestamp, these costs enable the model to associate that current pedestrian with the correct past trajectory based on other past timestamps. In addition, MVTrajecter effectively captures the relationships between multiple timestamps leveraging the attention mechanism. Extensive experiments demonstrate the effectiveness of each component in MVTrajecter and show that it outperforms the previous state-of-the-art methods.

</details>

### Hybrid-Grained Feature Aggregation with Coarse-to-Fine Language Guidance for Self-Supervised Monocular Depth Estimation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00629)
- **作者**: Wenyao Zhang, Hongsi Liu, Bohan Li, Jiawei He, Zekun Qi, Yunnan Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

## 跨领域论文（完整笔记在其他领域）

- OcRFDet: Object-Centric Radiance Fields for Multi-View 3D Object Detection in Autonomous Driving. → [3d-detection](../3d-detection/Guideline%202025.md)
- OpenM3D: Open Vocabulary Multi-View Indoor 3D Object Detection without Human Annotations. → [3d-detection](../3d-detection/Guideline%202025.md)
- MemDistill: Distilling LiDAR Knowledge into Memory for Camera-Only 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202025.md)
- FreqPDE: Rethinking Positional Depth Embedding for Multi-View 3D Object Detection Transformers. → [3d-detection](../3d-detection/Guideline%202025.md)
- Boosting Multi-View Indoor 3D Object Detection Via Adaptive 3D Volume Construction. → [3d-detection](../3d-detection/Guideline%202025.md)
