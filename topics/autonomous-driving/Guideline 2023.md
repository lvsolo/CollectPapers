# Autonomous Driving — 2023 Guideline

> 领域: 自动驾驶感知与系统（端到端驾驶、规划、驾驶场景理解、数据集基准）
> 论文数: 16 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### CO3: Cooperative Unsupervised 3D Representation Learning for Autonomous Driving.
- **链接**: [出版页](https://openreview.net/forum?id=QUaDoIdgo0)
- **作者**: Runjian Chen, Yao Mu, Runsen Xu, Wenqi Shao, Chenhan Jiang, Hang Xu et al.
- **🏷️ 机构**: Shanghai AI Lab
- **会议**: ICLR 2023

### Unsupervised 3D Point Cloud Representation Learning by Triangle Constrained Contrast for Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00506) · 📚 被引 17
- **作者**: Bo Pang, Hongchi Xia, Cewu Lu
- **🏷️ 机构**: Shanghai Jiao Tong University
- **会议**: CVPR 2023

### TBP-Former: Learning Temporal Bird's-Eye-View Pyramid for Joint Perception and Prediction in Vision-Centric Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00138) · 📚 被引 35
- **作者**: Shaoheng Fang, Zi Wang, Yiqi Zhong, Junhao Ge, Siheng Chen
- **🏷️ 机构**: Shanghai Jiao Tong University,Cooperative Medianet Innovation Center, University of Southern California,Department of Computer Science
- **会议**: CVPR 2023

### Implicit Occupancy Flow Fields for Perception and Prediction in Self-Driving.
- **链接**: [arXiv:2308.01471](https://arxiv.org/abs/2308.01471) · 📚 被引 27
- **作者**: Ben Agro, Quinlan Sykora, Sergio Casas, Raquel Urtasun
- **🏷️ 机构**: Waabi, University of Toronto
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Sensor fusion is an essential topic in many perception systems, such as autonomous driving and robotics. Transformers-based detection head and CNN-based feature encoder to extract features from raw sensor-data has emerged as one of the best performing sensor-fusion 3D-detection-framework, according to the dataset leaderboards. In this work we provide an in-depth literature survey of transformer based 3D-object detection task in the recent past, primarily focusing on the sensor fusion. We also briefly go through the Vision transformers (ViT) basics, so that readers can easily follow through the paper. Moreover, we also briefly go through few of the non-transformer based less-dominant methods for sensor fusion for autonomous driving. In conclusion we summarize with sensor-fusion trends to follow and provoke future research. More updated summary can be found at: https://github.com/ApoorvRoboticist/Transformers-Sensor-Fusion

</details>

### Think Twice before Driving: Towards Scalable Decoders for End-to-End Autonomous Driving.
- **链接**: [arXiv:2305.06242](https://arxiv.org/abs/2305.06242) · 📚 被引 113
- **作者**: Xiaosong Jia, Penghao Wu, Li Chen, Jiangwei Xie, Conghui He, Junchi Yan et al.
- **🏷️ 机构**: Shanghai Jiao Tong University, Shanghai AI Laboratory
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-agent cooperative perception is an increasingly popular topic in the field of autonomous driving, where roadside LiDARs play an essential role. However, how to optimize the placement of roadside LiDARs is a crucial but often overlooked problem. This paper proposes an approach to optimize the placement of roadside LiDARs by selecting optimized positions within the scene for better perception performance. To efficiently obtain the best combination of locations, a greedy algorithm based on perceptual gain is proposed, which selects the location that can maximize the perceptual gain sequentially. We define perceptual gain as the increased perceptual capability when a new LiDAR is placed. To obtain the perception capability, we propose a perception predictor that learns to evaluate LiDAR placement using only a single point cloud frame. A dataset named Roadside-Opt is created using the CARLA simulator to facilitate research on the roadside LiDAR placement problem.

</details>

### RangeViT: Towards Vision Transformers for 3D Semantic Segmentation in Autonomous Driving.
- **链接**: [arXiv:2301.10222](https://arxiv.org/abs/2301.10222) · [代码](https://github.com/valeoai/rangevit) · 📚 被引 141
- **作者**: Angelika Ando, Spyros Gidaris, Andrei Bursuc, Gilles Puy, Alexandre Boulch, Renaud Marlet
- **🏷️ 机构**: Valeo.ai,Paris,France
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Reconstructing 3D vehicles from noisy and sparse partial point clouds is of great significance to autonomous driving. Most existing 3D reconstruction methods cannot be directly applied to this problem because they are elaborately designed to deal with dense inputs with trivial noise. In this work, we propose a novel framework, dubbed MV-DeepSDF, which estimates the optimal Signed Distance Function (SDF) shape representation from multi-sweep point clouds to reconstruct vehicles in the wild. Although there have been some SDF-based implicit modeling methods, they only focus on single-view-based reconstruction, resulting in low fidelity. In contrast, we first analyze multi-sweep consistency and complementarity in the latent feature space and propose to transform the implicit space shape estimation problem into an element-to-set feature extraction problem. Then, we devise a new architecture to extract individual element-level representations and aggregate them to generate a set-level predicted latent code. This set-level latent code is an expression of the optimal 3D shape in the implicit space, and can be subsequently decoded to a continuous SDF of the vehicle. In this way, our approach learns consistent and complementary information among multi-sweeps for 3D vehicle reconstruction. We conduct thorough experiments on two real-world autonomous driving datasets (Waymo and KITTI) to demonstrate the superiority of our approach over state-of-the-art alternative methods both qualitatively and quantitatively.

</details>

### Planning-oriented Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01712)
- **作者**: Yihan Hu, Jiazhi Yang, Li Chen, Keyu Li, Chonghao Sima, Xizhou Zhu et al.
- **🏷️ 机构**: Tsinghua / Shanghai AI Lab
- **会议**: CVPR 2023

### Localized Semantic Feature Mixers for Efficient Pedestrian Detection in Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00530) · 📚 被引 42
- **作者**: Abdul Hannan Khan, Mohammed Shariq Nawaz, Andreas Dengel
- **🏷️ 机构**: RPTU Kaiserslautern-Landau,Department of Computer Science
- **会议**: CVPR 2023

### Weakly Supervised Class-agnostic Motion Prediction for Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01688) · 📚 被引 13
- **作者**: Ruibo Li, Hanyu Shi, Ziang Fu, Zhe Wang, Guosheng Lin
- **🏷️ 机构**: Nanyang Technological University,S-Lab, School of Computer Science and Engineering, Nanyang Technological University, SenseTime Research
- **会议**: CVPR 2023

### MSeg3D: Multi-Modal 3D Semantic Segmentation for Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02078)
- **作者**: Jiale Li, Hang Dai, Hao Han, Yong Ding
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### Azimuth Super-Resolution for FMCW Radar in Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01679) · 📚 被引 27
- **作者**: Yu-Jhe Li, Shawn Hunt, Jinhyung Park, Matthew O'Toole, Kris Kitani
- **🏷️ 机构**: Carnegie Mellon University, DENSO International America, Inc.
- **会议**: CVPR 2023

### Visual Exemplar Driven Task-Prompting for Unified Perception in Autonomous Driving.
- **链接**: [arXiv:2303.01788](https://arxiv.org/abs/2303.01788) · 📚 被引 22
- **作者**: Xiwen Liang, Minzhe Niu, Jianhua Han, Hang Xu, Chunjing Xu, Xiaodan Liang
- **🏷️ 机构**: Shenzhen Campus of Sun Yat-sen University, Huawei Noah&#x0027;s Ark Lab
- **会议**: CVPR 2023

### AD-PT: Autonomous Driving Pre-Training with Large-scale Point Cloud Dataset.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/95ab5c3e26fd82c7de3230bbad087d2d-Abstract-Conference.html) · 📚 被引 1
- **作者**: Jiakang Yuan, Bo Zhang, Xiangchao Yan, Botian Shi, Tao Chen, Yikang Li et al.
- **🏷️ 机构**: Shanghai AI Lab
- **会议**: NeurIPS 2023

> Multi-task learning has emerged as a powerful paradigm to solve a range of tasks simultaneously with good efficiency in both computation resources and inference time. However, these algorithms are designed for different tasks mostly not within the scope of autonomous driving, thus making it hard to compare multi-task methods in autonomous driving. Aiming to enable the comprehensive evaluation of present multi-task learning methods in autonomous driving, we extensively investigate the performance of popular multi-task methods on the large-scale driving dataset, which covers four common perception tasks, i.e., object detection, semantic segmentation, drivable area segmentation, and lane detection. We provide an in-depth analysis of current multi-task learning methods under different common settings and find out that the existing methods make progress but there is still a large performance gap compared with single-task baselines. To alleviate this dilemma in autonomous driving, we present an effective multi-task framework, VE-Prompt, which introduces visual exemplars via task-specific prompting to guide the model toward learning high-quality task-specific representations. Specifically, we generate visual exemplars based on bounding boxes and color-based markers, which provide accurate visual appearances of target categories and further mitigate the performance gap. Furthermore, we bridge transformer-based encoders and convolutional layers for efficient and accurate unified perception in autonomous driving. Comprehensive experimental results on the diverse self-driving dataset BDD100K show that the VE-Prompt improves the multi-task baseline and further surpasses single-task models.

</details>

### Neural Map Prior for Autonomous Driving.
- **链接**: [arXiv:2304.08481](https://arxiv.org/abs/2304.08481)
- **作者**: Xuan Xiong, Yicheng Liu, Tianyuan Yuan, Yue Wang, Yilun Wang, Hang Zhao
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> High-definition (HD) semantic maps are crucial in enabling autonomous vehicles to navigate urban environments. The traditional method of creating offline HD maps involves labor-intensive manual annotation processes, which are not only costly but also insufficient for timely updates. Recent studies have proposed an alternative approach that generates local maps using online sensor observations. However, this approach is limited by the sensor's perception range and its susceptibility to occlusions. In this study, we propose Neural Map Prior (NMP), a neural representation of global maps. This representation automatically updates itself and improves the performance of local map inference. Specifically, we utilize two approaches to achieve this. Firstly, to integrate a strong map prior into local map inference, we apply cross-attention, a mechanism that dynamically identifies correlations between current and prior features. Secondly, to update the global neural map prior, we utilize a learning-based fusion module that guides the network in fusing features from previous traversals. Our experimental results, based on the nuScenes dataset, demonstrate that our framework is highly compatible with various map segmentation and detection architectures. It significantly improves map prediction performance, even in challenging weather conditions and situations with a longer perception range. To the best of our knowledge, this is the first learning-based system for creating a global map prior.

</details>

### ReasonNet: End-to-End Driving with Temporal and Global Reasoning.
- **链接**: [arXiv:2305.10507](https://arxiv.org/abs/2305.10507) · 📚 被引 101
- **作者**: Hao Shao, Letian Wang, Ruobing Chen, Steven L. Waslander, Hongsheng Li, Yu Liu
- **🏷️ 机构**: Sense Time Research, University of Toronto, CUHK MMLab
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The large-scale deployment of autonomous vehicles is yet to come, and one of the major remaining challenges lies in urban dense traffic scenarios. In such cases, it remains challenging to predict the future evolution of the scene and future behaviors of objects, and to deal with rare adverse events such as the sudden appearance of occluded objects. In this paper, we present ReasonNet, a novel end-to-end driving framework that extensively exploits both temporal and global information of the driving scene. By reasoning on the temporal behavior of objects, our method can effectively process the interactions and relationships among features in different frames. Reasoning about the global information of the scene can also improve overall perception performance and benefit the detection of adverse events, especially the anticipation of potential danger from occluded objects. For comprehensive evaluation on occlusion events, we also release publicly a driving simulation benchmark DriveOcclusionSim consisting of diverse occlusion events. We conduct extensive experiments on multiple CARLA benchmarks, where our model outperforms all prior methods, ranking first on the sensor track of the public CARLA Leaderboard.

</details>

## 跨领域论文（完整笔记在其他领域）

- Benchmarking Robustness of 3D Object Detection to Common Corruptions in Autonomous Driving. → [3d-detection](../3d-detection/Guideline%202023.md)
- Understanding the Robustness of 3D Object Detection with Bird'View Representations in Autonomous Driving. → [3d-detection](../3d-detection/Guideline%202023.md)
