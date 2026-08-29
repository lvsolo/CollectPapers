# Autonomous Driving — 2023 Guideline

> 领域: 自动驾驶感知与系统（端到端驾驶、规划、驾驶场景理解、数据集基准）
> 论文数: 16 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Temporal Consistent 3D LiDAR Representation Learning for Semantic Perception in Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00505) · 📚 被引 43
- **作者**: Lucas Nunes, Louis Wiesmann, Rodrigo Marcuzzi, Xieyuanli Chen, Jens Behley, Cyrill Stachniss
- **🏷️ 机构**: University of Bonn
- **会议**: CVPR 2023

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

> A self-driving vehicle (SDV) must be able to perceive its surroundings and predict the future behavior of other traffic participants. Existing works either perform object detection followed by trajectory forecasting of the detected objects, or predict dense occupancy and flow grids for the whole scene. The former poses a safety concern as the number of detections needs to be kept low for efficiency reasons, sacrificing object recall. The latter is computationally expensive due to the high-dimensionality of the output grid, and suffers from the limited receptive field inherent to fully convolutional networks. Furthermore, both approaches employ many computational resources predicting areas or objects that might never be queried by the motion planner. This motivates our unified approach to perception and future prediction that implicitly represents occupancy and flow over time with a single neural network. Our method avoids unnecessary computation, as it can be directly queried by the motion planner at continuous spatio-temporal locations. Moreover, we design an architecture that overcomes the limited receptive field of previous explicit occupancy prediction methods by adding an efficient yet effective global attention mechanism. Through extensive experiments in both urban and highway settings, we demonstrate that our implicit model outperforms the current state-of-the-art. For more information, visit the project website: https://waabi.ai/research/implicito.

</details>

### Think Twice before Driving: Towards Scalable Decoders for End-to-End Autonomous Driving.
- **链接**: [arXiv:2305.06242](https://arxiv.org/abs/2305.06242) · 📚 被引 113
- **作者**: Xiaosong Jia, Penghao Wu, Li Chen, Jiangwei Xie, Conghui He, Junchi Yan et al.
- **🏷️ 机构**: Shanghai Jiao Tong University, Shanghai AI Laboratory
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> End-to-end autonomous driving has made impressive progress in recent years. Existing methods usually adopt the decoupled encoder-decoder paradigm, where the encoder extracts hidden features from raw sensor data, and the decoder outputs the ego-vehicle's future trajectories or actions. Under such a paradigm, the encoder does not have access to the intended behavior of the ego agent, leaving the burden of finding out safety-critical regions from the massive receptive field and inferring about future situations to the decoder. Even worse, the decoder is usually composed of several simple multi-layer perceptrons (MLP) or GRUs while the encoder is delicately designed (e.g., a combination of heavy ResNets or Transformer). Such an imbalanced resource-task division hampers the learning process. In this work, we aim to alleviate the aforementioned problem by two principles: (1) fully utilizing the capacity of the encoder; (2) increasing the capacity of the decoder. Concretely, we first predict a coarse-grained future position and action based on the encoder features. Then, conditioned on the position and action, the future scene is imagined to check the ramification if we drive accordingly. We also retrieve the encoder features around the predicted coordinate to obtain fine-grained information about the safety-critical region. Finally, based on the predicted future and the retrieved salient feature, we refine the coarse-grained position and action by predicting its offset from ground-truth. The above refinement module could be stacked in a cascaded fashion, which extends the capacity of the decoder with spatial-temporal prior knowledge about the conditioned future. We conduct experiments on the CARLA simulator and achieve state-of-the-art performance in closed-loop benchmarks. Extensive ablation studies demonstrate the effectiveness of each proposed module.

</details>

### RangeViT: Towards Vision Transformers for 3D Semantic Segmentation in Autonomous Driving.
- **链接**: [arXiv:2301.10222](https://arxiv.org/abs/2301.10222) · [代码](https://github.com/valeoai/rangevit) · 📚 被引 141
- **作者**: Angelika Ando, Spyros Gidaris, Andrei Bursuc, Gilles Puy, Alexandre Boulch, Renaud Marlet
- **🏷️ 机构**: Valeo.ai,Paris,France
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Casting semantic segmentation of outdoor LiDAR point clouds as a 2D problem, e.g., via range projection, is an effective and popular approach. These projection-based methods usually benefit from fast computations and, when combined with techniques which use other point cloud representations, achieve state-of-the-art results. Today, projection-based methods leverage 2D CNNs but recent advances in computer vision show that vision transformers (ViTs) have achieved state-of-the-art results in many image-based benchmarks. In this work, we question if projection-based methods for 3D semantic segmentation can benefit from these latest improvements on ViTs. We answer positively but only after combining them with three key ingredients: (a) ViTs are notoriously hard to train and require a lot of training data to learn powerful representations. By preserving the same backbone architecture as for RGB images, we can exploit the knowledge from long training on large image collections that are much cheaper to acquire and annotate than point clouds. We reach our best results with pre-trained ViTs on large image datasets. (b) We compensate ViTs' lack of inductive bias by substituting a tailored convolutional stem for the classical linear embedding layer. (c) We refine pixel-wise predictions with a convolutional decoder and a skip connection from the convolutional stem to combine low-level but fine-grained features of the the convolutional stem with the high-level but coarse predictions of the ViT encoder. With these ingredients, we show that our method, called RangeViT, outperforms existing projection-based methods on nuScenes and SemanticKITTI. The code is available at https://github.com/valeoai/rangevit.

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

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

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
