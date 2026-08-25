# Autonomous Driving — 2023 Guideline

> 领域: 自动驾驶感知与系统（端到端驾驶、规划、驾驶场景理解、数据集基准）
> 论文数: 16 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Temporal Consistent 3D LiDAR Representation Learning for Semantic Perception in Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00505)
- **作者**: Lucas Nunes, Louis Wiesmann, Rodrigo Marcuzzi, Xieyuanli Chen, Jens Behley, Cyrill Stachniss
- **🏷️ 机构**: University of Bonn
- **会议**: CVPR 2023

### Unsupervised 3D Point Cloud Representation Learning by Triangle Constrained Contrast for Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00506)
- **作者**: Bo Pang, Hongchi Xia, Cewu Lu
- **🏷️ 机构**: Shanghai Jiao Tong University
- **会议**: CVPR 2023

### TBP-Former: Learning Temporal Bird's-Eye-View Pyramid for Joint Perception and Prediction in Vision-Centric Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00138)
- **作者**: Shaoheng Fang, Zi Wang, Yiqi Zhong, Junhao Ge, Siheng Chen
- **🏷️ 机构**: Shanghai Jiao Tong University,Cooperative Medianet Innovation Center, University of Southern California,Department of Computer Science
- **会议**: CVPR 2023

### Implicit Occupancy Flow Fields for Perception and Prediction in Self-Driving.
- **链接**: [arXiv:2308.01471](https://arxiv.org/abs/2308.01471) · 📚 被引 27
- **作者**: Ben Agro, Quinlan Sykora, Sergio Casas, Raquel Urtasun
- **🏷️ 机构**: Waabi, University of Toronto
- **会议**: CVPR 2023

- **摘要（英，原文）**:

  > A self-driving vehicle (SDV) must be able to perceive its surroundings and predict the future behavior of other traffic participants. Existing works either perform object detection followed by trajectory forecasting of the detected objects, or predict dense occupancy and flow grids for the whole scene. The former poses a safety concern as the number of detections needs to be kept low for efficiency reasons, sacrificing object recall. The latter is computationally expensive due to the high-dimensionality of the output grid, and suffers from the limited receptive field inherent to fully convolutional networks. Furthermore, both approaches employ many computational resources predicting areas or objects that might never be queried by the motion planner. This motivates our unified approach to perception and future prediction that implicitly represents occupancy and flow over time with a single neural network. Our method avoids unnecessary computation, as it can be directly queried by the motion planner at continuous spatio-temporal locations. Moreover, we design an architecture that overcomes the limited receptive field of previous explicit occupancy prediction methods by adding an efficient yet effective global attention mechanism. Through extensive experiments in both urban and highway settings, we demonstrate that our implicit model outperforms the current state-of-the-art. For more information, visit the project website: https://waabi.ai/research/implicito.

### Think Twice before Driving: Towards Scalable Decoders for End-to-End Autonomous Driving.
- **链接**: [arXiv:2305.06242](https://arxiv.org/abs/2305.06242) · 📚 被引 113
- **作者**: Xiaosong Jia, Penghao Wu, Li Chen, Jiangwei Xie, Conghui He, Junchi Yan et al.
- **🏷️ 机构**: Shanghai Jiao Tong University, Shanghai AI Laboratory
- **会议**: CVPR 2023

- **摘要（英，原文）**:

  > End-to-end autonomous driving has made impressive progress in recent years. Existing methods usually adopt the decoupled encoder-decoder paradigm, where the encoder extracts hidden features from raw sensor data, and the decoder outputs the ego-vehicle's future trajectories or actions. Under such a paradigm, the encoder does not have access to the intended behavior of the ego agent, leaving the burden of finding out safety-critical regions from the massive receptive field and inferring about future situations to the decoder. Even worse, the decoder is usually composed of several simple multi-layer perceptrons (MLP) or GRUs while the encoder is delicately designed (e.g., a combination of heavy ResNets or Transformer). Such an imbalanced resource-task division hampers the learning process. In this work, we aim to alleviate the aforementioned problem by two principles: (1) fully utilizing the capacity of the encoder; (2) increasing the capacity of the decoder. Concretely, we first predict a coarse-grained future position and action based on the encoder features. Then, conditioned on the position and action, the future scene is imagined to check the ramification if we drive accordingly. We also retrieve the encoder features around the predicted coordinate to obtain fine-grained information about the safety-critical region. Finally, based on the predicted future and the retrieved salient feature, we refine the coarse-grained position and action by predicting its offset from ground-truth. The above refinement module could be stacked in a cascaded fashion, which extends the capacity of the decoder with spatial-temporal prior knowledge about the conditioned future. We conduct experiments on the CARLA simulator and achieve state-of-the-art performance in closed-loop benchmarks. Extensive ablation studies demonstrate the effectiveness of each proposed module.

### RangeViT: Towards Vision Transformers for 3D Semantic Segmentation in Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00507)
- **作者**: Angelika Ando, Spyros Gidaris, Andrei Bursuc, Gilles Puy, Alexandre Boulch, Renaud Marlet
- **🏷️ 机构**: Valeo.ai,Paris,France
- **会议**: CVPR 2023

### Planning-oriented Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01712)
- **作者**: Yihan Hu, Jiazhi Yang, Li Chen, Keyu Li, Chonghao Sima, Xizhou Zhu et al.
- **🏷️ 机构**: Tsinghua / Shanghai AI Lab
- **会议**: CVPR 2023

### Localized Semantic Feature Mixers for Efficient Pedestrian Detection in Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00530)
- **作者**: Abdul Hannan Khan, Mohammed Shariq Nawaz, Andreas Dengel
- **🏷️ 机构**: RPTU Kaiserslautern-Landau,Department of Computer Science
- **会议**: CVPR 2023

### Weakly Supervised Class-agnostic Motion Prediction for Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01688)
- **作者**: Ruibo Li, Hanyu Shi, Ziang Fu, Zhe Wang, Guosheng Lin
- **🏷️ 机构**: Nanyang Technological University,S-Lab, School of Computer Science and Engineering, Nanyang Technological University, SenseTime Research
- **会议**: CVPR 2023

### MSeg3D: Multi-Modal 3D Semantic Segmentation for Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02078)
- **作者**: Jiale Li, Hang Dai, Hao Han, Yong Ding
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### Azimuth Super-Resolution for FMCW Radar in Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01679)
- **作者**: Yu-Jhe Li, Shawn Hunt, Jinhyung Park, Matthew O'Toole, Kris Kitani
- **🏷️ 机构**: Carnegie Mellon University, DENSO International America, Inc.
- **会议**: CVPR 2023

### Visual Exemplar Driven Task-Prompting for Unified Perception in Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00927)
- **作者**: Xiwen Liang, Minzhe Niu, Jianhua Han, Hang Xu, Chunjing Xu, Xiaodan Liang
- **🏷️ 机构**: Shenzhen Campus of Sun Yat-sen University, Huawei Noah&#x0027;s Ark Lab
- **会议**: CVPR 2023

### Neural Map Prior for Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01682)
- **作者**: Xuan Xiong, Yicheng Liu, Tianyuan Yuan, Yue Wang, Yilun Wang, Hang Zhao
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### ReasonNet: End-to-End Driving with Temporal and Global Reasoning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01319) · 📚 被引 100
- **作者**: Hao Shao, Letian Wang, Ruobing Chen, Steven L. Waslander, Hongsheng Li, Yu Liu
- **🏷️ 机构**: Sense Time Research, University of Toronto, CUHK MMLab
- **会议**: CVPR 2023

## 跨领域论文（完整笔记在其他领域）

- Benchmarking Robustness of 3D Object Detection to Common Corruptions in Autonomous Driving. → [3d-detection](../3d-detection/Guideline%202023.md)
- Understanding the Robustness of 3D Object Detection with Bird'View Representations in Autonomous Driving. → [3d-detection](../3d-detection/Guideline%202023.md)
