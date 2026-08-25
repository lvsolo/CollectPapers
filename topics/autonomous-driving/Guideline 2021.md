# Autonomous Driving — 2021 Guideline

> 领域: 自动驾驶感知与系统（端到端驾驶、规划、驾驶场景理解、数据集基准）
> 论文数: 5 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Shared Cross-Modal Trajectory Prediction for Autonomous Driving.
- **链接**: [arXiv:2004.00202](https://arxiv.org/abs/2004.00202) · 📚 被引 56
- **作者**: Chiho Choi, Joon Hee Choi, Jiachen Li, Srikanth Malla
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

- **摘要（英，原文）**:

  > Predicting future trajectories of traffic agents in highly interactive environments is an essential and challenging problem for the safe operation of autonomous driving systems. On the basis of the fact that self-driving vehicles are equipped with various types of sensors (e.g., LiDAR scanner, RGB camera, radar, etc.), we propose a Cross-Modal Embedding framework that aims to benefit from the use of multiple input modalities. At training time, our model learns to embed a set of complementary features in a shared latent space by jointly optimizing the objective functions across different types of input data. At test time, a single input modality (e.g., LiDAR data) is required to generate predictions from the input perspective (i.e., in the LiDAR space), while taking advantages from the model trained with multiple sensor modalities. An extensive evaluation is conducted to show the efficacy of the proposed framework using two benchmark driving datasets.

### Self-Supervised Pillar Motion Learning for Autonomous Driving.
- **链接**: [arXiv:2104.08683](https://arxiv.org/abs/2104.08683) · 📚 被引 61
- **作者**: Chenxu Luo, Xiaodong Yang, Alan L. Yuille
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

- **摘要（英，原文）**:

  > Autonomous driving can benefit from motion behavior comprehension when interacting with diverse traffic participants in highly dynamic environments. Recently, there has been a growing interest in estimating class-agnostic motion directly from point clouds. Current motion estimation methods usually require vast amount of annotated training data from self-driving scenes. However, manually labeling point clouds is notoriously difficult, error-prone and time-consuming. In this paper, we seek to answer the research question of whether the abundant unlabeled data collections can be utilized for accurate and efficient motion learning. To this end, we propose a learning framework that leverages free supervisory signals from point clouds and paired camera images to estimate motion purely via self-supervision. Our model involves a point cloud based structural consistency augmented with probabilistic motion masking as well as a cross-sensor motion regularization to realize the desired self-supervision. Experiments reveal that our approach performs competitively to supervised methods, and achieves the state-of-the-art result when combining our self-supervised model with supervised fine-tuning.

### Multi-Modal Fusion Transformer for End-to-End Autonomous Driving.
- **链接**: [arXiv:2104.09224](https://arxiv.org/abs/2104.09224) · 📚 被引 546
- **作者**: Aditya Prakash, Kashyap Chitta, Andreas Geiger
- **🏷️ 机构**: Max Planck Institute for Intelligent Systems,T&#x00FC;bingen
- **会议**: CVPR 2021

- **摘要（英，原文）**:

  > How should representations from complementary sensors be integrated for autonomous driving? Geometry-based sensor fusion has shown great promise for perception tasks such as object detection and motion forecasting. However, for the actual driving task, the global context of the 3D scene is key, e.g. a change in traffic light state can affect the behavior of a vehicle geometrically distant from that traffic light. Geometry alone may therefore be insufficient for effectively fusing representations in end-to-end driving models. In this work, we demonstrate that imitation learning policies based on existing sensor fusion methods under-perform in the presence of a high density of dynamic agents and complex scenarios, which require global contextual reasoning, such as handling traffic oncoming from multiple directions at uncontrolled intersections. Therefore, we propose TransFuser, a novel Multi-Modal Fusion Transformer, to integrate image and LiDAR representations using attention. We experimentally validate the efficacy of our approach in urban settings involving complex scenarios using the CARLA urban driving simulator. Our approach achieves state-of-the-art driving performance while reducing collisions by 76% compared to geometry-based fusion.

### GeoSim: Realistic Video Simulation via Geometry-Aware Composition for Self-Driving.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Chen_GeoSim_Realistic_Video_Simulation_via_Geometry-Aware_Composition_for_Self-Driving_CVPR_2021_paper.html) · 📚 被引 89
- **作者**: Yun Chen, Frieda Rong, Shivam Duggal, Shenlong Wang, Xinchen Yan, Sivabalan Manivasagam et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### AdvSim: Generating Safety-Critical Scenarios for Self-Driving Vehicles.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Wang_AdvSim_Generating_Safety-Critical_Scenarios_for_Self-Driving_Vehicles_CVPR_2021_paper.html) · 📚 被引 176
- **作者**: Jingkang Wang, Ava Pun, James Tu, Sivabalan Manivasagam, Abbas Sadat, Sergio Casas et al.
- **🏷️ 机构**: Waabi / University of Toronto
- **会议**: CVPR 2021
