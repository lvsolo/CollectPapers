# Tracking — 2025 Guideline

> 领域: 目标跟踪（MOT / 3D 跟踪 / 多目标多相机跟踪）
> 论文数: 6 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### MMOT: The First Challenging Benchmark for Drone-based Multispectral Multi-Object Tracking.
- **链接**: [arXiv:2510.12565](https://arxiv.org/abs/2510.12565) · 📚 被引 1
- **作者**: Tianhao Li, Tingfa Xu, Ying Wang, Haolin Qin, Xu Lin, Jianan Li
- **🏷️ 机构**: Beijing Institute of Technology, Beijing Institute of Technology, Tsinghua University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Drone-based multi-object tracking is essential yet highly challenging due to small targets, severe occlusions, and cluttered backgrounds. Existing RGB-based tracking algorithms heavily depend on spatial appearance cues such as color and texture, which often degrade in aerial views, compromising reliability. Multispectral imagery, capturing pixel-level spectral reflectance, provides crucial cues that enhance object discriminability under degraded spatial conditions. However, the lack of dedicated multispectral UAV datasets has hindered progress in this domain. To bridge this gap, we introduce MMOT, the first challenging benchmark for drone-based multispectral multi-object tracking. It features three key characteristics: (i) Large Scale - 125 video sequences with over 488.8K annotations across eight categories; (ii) Comprehensive Challenges - covering diverse conditions such as extreme small targets, high-density scenarios, severe occlusions, and complex motion; and (iii) Precise Oriented Annotations - enabling accurate localization and reduced ambiguity under aerial perspectives. To better extract spectral features and leverage oriented annotations, we further present a multispectral and orientation-aware MOT scheme adapting existing methods, featuring: (i) a lightweight Spectral 3D-Stem integrating spectral features while preserving compatibility with RGB pretraining; (ii) an orientation-aware Kalman filter for precise state estimation; and (iii) an end-to-end orientation-adaptive transformer. Extensive experiments across representative trackers consistently show that multispectral input markedly improves tracking performance over RGB baselines, particularly for small and densely packed objects. We believe our work will advance drone-based multispectral multi-object tracking research. Our MMOT, code, and benchmarks are publicly available at https://github.com/Annzstbl/MMOT.

</details>

### STAR: Spatial-Temporal Tracklet Matching for Multi-Object Tracking.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/62c599c5c2b365ba464a26ebad05b690-Abstract-Conference.html) · 📚 被引 0
- **作者**: Xuewei Bai, Yongcai Wang, Deying Li, Haodi Ping, Chunxu Li
- **🏷️ 机构**: Renmin University of China, Beijing University of Technology
- **会议**: NeurIPS 2025

### Dual-Path Temporal Decoder for End-to-End Multi-Object Tracking.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/07054a34f24ac3ef64c5f2fdf571b8c0-Abstract-Conference.html) · 📚 被引 0
- **作者**: Hyunseop Kim, Juheon Jeong, Hanul Kim, Yeong Jun Koh
- **🏷️ 机构**: Chungnam National University, Seoul National University of Science and Technology
- **会议**: NeurIPS 2025

### HO-Cap: A Capture System and Dataset for 3D Reconstruction and Pose Tracking of Hand-Object Interaction.
- **链接**: [arXiv:2406.06843](https://arxiv.org/abs/2406.06843) · 📚 被引 0
- **作者**: Jikai Wang, Qifan Zhang, Yu-Wei Chao, Bowen Wen, Xiaohu Guo, Yu Xiang
- **🏷️ 机构**: University of Texas at Dallas, NVIDIA, University of Texas, Dallas
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce a data capture system and a new dataset, HO-Cap, for 3D reconstruction and pose tracking of hands and objects in videos. The system leverages multiple RGBD cameras and a HoloLens headset for data collection, avoiding the use of expensive 3D scanners or mocap systems. We propose a semi-automatic method for annotating the shape and pose of hands and objects in the collected videos, significantly reducing the annotation time compared to manual labeling. With this system, we captured a video dataset of humans interacting with objects to perform various tasks, including simple pick-and-place actions, handovers between hands, and using objects according to their affordance, which can serve as human demonstrations for research in embodied AI and robot manipulation. Our data capture setup and annotation framework will be available for the community to use in reconstructing 3D shapes of objects and human hands and tracking their poses in videos.

</details>

## 跨领域论文（完整笔记在其他领域）

- SynCL: A Synergistic Training Strategy with Instance-Aware Contrastive Learning for End-to-End Multi-Camera 3D Tracking. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
- TrackingWorld: World-centric Monocular 3D Tracking of Almost All Pixels. → [3d-detection](../3d-detection/Guideline%202025.md)
