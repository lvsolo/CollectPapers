# Autonomous Driving — 2022 Guideline

> 领域: 自动驾驶感知与系统（端到端驾驶、规划、驾驶场景理解、数据集基准）
> 论文数: 12 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Coopernaut: End-to-End Driving with Cooperative Perception for Networked Vehicles.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01674) · 📚 被引 129
- **作者**: Jiaxun Cui, Hang Qiu, Dian Chen, Peter Stone, Yuke Zhu
- **🏷️ 机构**: The University of Texas at Austin, Stanford University
- **会议**: CVPR 2022

### Exploiting Temporal Relations on Radar Perception for Autonomous Driving.
- **链接**: [arXiv:2204.01184](https://arxiv.org/abs/2204.01184) · [出版页](https://doi.org/10.1109/CVPR52688.2022.01656) · 📚 被引 56
- **作者**: Peizhao Li, Pu Wang, Karl Berntorp, Hongfu Liu
- **🏷️ 机构**: Brandeis University, Mitsubishi Electric Research Laboratories
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > We consider the object recognition problem in autonomous driving using automotive radar sensors. Comparing to Lidar sensors, radar is cost-effective and robust in all-weather conditions for perception in autonomous driving. However, radar signals suffer from low angular resolution and precision in recognizing surrounding objects. To enhance the capacity of automotive radar, in this work, we exploit the temporal information from successive ego-centric bird-eye-view radar image frames for radar object recognition. We leverage the consistency of an object's existence and attributes (size, orientation, etc.), and propose a temporal relational layer to explicitly model the relations between objects within successive radar images. In both object detection and multiple object tracking, we show the superiority of our method compared to several baseline approaches.

### Generating Useful Accident-Prone Driving Scenarios via a Learned Traffic Prior.
- **链接**: [arXiv:2112.05077](https://arxiv.org/abs/2112.05077) · [出版页](https://doi.org/10.1109/CVPR52688.2022.01679) · 📚 被引 134
- **作者**: Davis Rempe, Jonah Philion, Leonidas J. Guibas, Sanja Fidler, Or Litany
- **🏷️ 机构**: NVIDIA / University of Toronto
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > Evaluating and improving planning for autonomous vehicles requires scalable generation of long-tail traffic scenarios. To be useful, these scenarios must be realistic and challenging, but not impossible to drive through safely. In this work, we introduce STRIVE, a method to automatically generate challenging scenarios that cause a given planner to produce undesirable behavior, like collisions. To maintain scenario plausibility, the key idea is to leverage a learned model of traffic motion in the form of a graph-based conditional VAE. Scenario generation is formulated as an optimization in the latent space of this traffic model, perturbing an initial real-world scene to produce trajectories that collide with a given planner. A subsequent optimization is used to find a "solution" to the scenario, ensuring it is useful to improve the given planner. Further analysis clusters generated scenarios based on collision type. We attack two planners and show that STRIVE successfully generates realistic, challenging scenarios in both cases. We additionally "close the loop" and use these scenarios to optimize hyperparameters of a rule-based planner.

### Towards Driving-Oriented Metric for Lane Detection Models.
- **链接**: [arXiv:2203.16851](https://arxiv.org/abs/2203.16851) · [出版页](https://doi.org/10.1109/CVPR52688.2022.01664) · 📚 被引 15
- **作者**: Takami Sato, Qi Alfred Chen
- **🏷️ 机构**: University of California,Irvine
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > After the 2017 TuSimple Lane Detection Challenge, its dataset and evaluation based on accuracy and F1 score have become the de facto standard to measure the performance of lane detection methods. While they have played a major role in improving the performance of lane detection methods, the validity of this evaluation method in downstream tasks has not been adequately researched. In this study, we design 2 new driving-oriented metrics for lane detection: End-to-End Lateral Deviation metric (E2E-LD) is directly formulated based on the requirements of autonomous driving, a core downstream task of lane detection; Per-frame Simulated Lateral Deviation metric (PSLD) is a lightweight surrogate metric of E2E-LD. To evaluate the validity of the metrics, we conduct a large-scale empirical study with 4 major types of lane detection approaches on the TuSimple dataset and our newly constructed dataset Comma2k19-LD. Our results show that the conventional metrics have strongly negative correlations ($\leq$-0.55) with E2E-LD, meaning that some recent improvements purely targeting the conventional metrics may not have led to meaningful improvements in autonomous driving, but rather may actually have made it worse by overfitting to the conventional metrics. As autonomous driving is a security/safety-critical system, the underestimation of robustness hinders the sound development of practical lane detection models. We hope that our study will help the community achieve more downstream task-aware evaluations for lane detection.

### Image-to-Lidar Self-Supervised Distillation for Autonomous Driving Data.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00966) · 📚 被引 112
- **作者**: Corentin Sautier, Gilles Puy, Spyros Gidaris, Alexandre Boulch, Andrei Bursuc, Renaud Marlet
- **🏷️ 机构**: valeo.ai,Paris,France
- **会议**: CVPR 2022

### LTP: Lane-based Trajectory Prediction for Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01662) · 📚 被引 83
- **作者**: Jingke Wang, Tengju Ye, Ziqing Gu, Junbo Chen
- **🏷️ 机构**: Alibaba Group
- **会议**: CVPR 2022

### Unifying Panoptic Segmentation for Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.02066) · 📚 被引 47
- **作者**: Oliver Zendel, Matthias Schörghuber, Bernhard Rainer, Markus Murschitz, Csaba Beleznai
- **🏷️ 机构**: AIT Austrian Institute of Technology
- **会议**: CVPR 2022

## 跨领域论文（完整笔记在其他领域）

- Pseudo-Stereo for Monocular 3D Object Detection in Autonomous Driving. → [3d-detection](../3d-detection/Guideline%202022.md)
- Investigating the Impact of Multi-LiDAR Placement on Object Detection for Autonomous Driving. → [3d-detection](../3d-detection/Guideline%202022.md)
- Time3D: End-to-End Joint Monocular 3D Object Detection and Tracking for Autonomous Driving. → [3d-detection](../3d-detection/Guideline%202022.md)
- Rope3D: The Roadside Perception Dataset for Autonomous Driving and Monocular 3D Object Detection Task. → [3d-detection](../3d-detection/Guideline%202022.md)
- DAIR-V2X: A Large-Scale Dataset for Vehicle-Infrastructure Cooperative 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
