# Autonomous Driving — 2020 Guideline

> 领域: 自动驾驶感知与系统（端到端驾驶、规划、驾驶场景理解、数据集基准）
> 论文数: 10 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份:

### MotionNet: Joint Perception and Motion Prediction for Autonomous Driving Based on Bird's Eye View Maps.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Wu_MotionNet_Joint_Perception_and_Motion_Prediction_for_Autonomous_Driving_Based_CVPR_2020_paper.html)
- **作者**: Pengxiang Wu, Siheng Chen, Dimitris N. Metaxas
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### nuScenes: A Multimodal Dataset for Autonomous Driving. **⭐⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:1903.11027](https://arxiv.org/abs/1903.11027) · 📚 被引 5835
- **作者**: Holger Caesar, Varun Bankiti, Alex H. Lang, Sourabh Vora, Venice Erin Liong, Qiang Xu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: 针对自动驾驶数据集缺乏完整传感器套件和丰富标注的问题，提出nuScenes多模态数据集。该数据集包含6个相机、5个雷达和1个激光雷达，全部360度视野，共1000个场景，每个20秒，标注23个类别的3D边界框和8个属性，标注量是KITTI的7倍，图像量是100倍。同时定义新的3D检测和跟踪指标，并提供激光雷达和图像检测跟踪基线。
- **摘要（英）**: To address the lack of full sensor suites and rich annotations in autonomous driving datasets, this paper introduces nuScenes, the first dataset with 6 cameras, 5 radars, and 1 lidar, all 360-degree, comprising 1000 scenes with 3D bounding boxes for 23 classes. It has 7x annotations and 100x images of KITTI, with novel metrics and baselines.
- **核心贡献**: 发布nuScenes多模态数据集，包含完整传感器套件和丰富3D标注，定义新指标。
- **创新点**: 创新性地提供多传感器融合基准，覆盖23类物体和8个属性，规模远超KITTI。
- **结果**: 数据集被广泛采用，成为自动驾驶感知研究的标准基准之一。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Robust detection and tracking of objects is crucial for the deployment of autonomous vehicle technology. Image based benchmark datasets have driven development in computer vision tasks such as object detection, tracking and segmentation of agents in the environment. Most autonomous vehicles, however, carry a combination of cameras and range sensors such as lidar and radar. As machine learning based methods for detection and tracking become more prevalent, there is a need to train and evaluate such methods on datasets containing range sensor data along with images. In this work we present nuTonomy scenes (nuScenes), the first dataset to carry the full autonomous vehicle sensor suite: 6 cameras, 5 radars and 1 lidar, all with full 360 degree field of view. nuScenes comprises 1000 scenes, each 20s long and fully annotated with 3D bounding boxes for 23 classes and 8 attributes. It has 7x as many annotations and 100x as many images as the pioneering KITTI dataset. We define novel 3D detection and tracking metrics. We also provide careful dataset analysis as well as baselines for lidar and image based detection and tracking. Data, development kit and more information are available online.

</details>

### PhysGAN: Generating Physical-World-Resilient Adversarial Examples for Autonomous Driving. **⭐⭐⭐** (相关度: 80%)
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Kong_PhysGAN_Generating_Physical-World-Resilient_Adversarial_Examples_for_Autonomous_Driving_CVPR_2020_paper.html) · 📚 被引 136
- **作者**: Zelun Kong, Junfeng Guo, Ang Li, Cong Liu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对自动驾驶中对抗样本在物理世界中的鲁棒性问题。②提出PhysGAN方法，生成物理世界可实现的对抗样本。③相比现有方法，考虑物理世界约束，提高攻击的实用性。④摘要缺失，但预期在物理攻击成功率上有提升。
- **摘要（英）**: This paper addresses the generation of physically realizable adversarial examples for autonomous driving. It proposes PhysGAN to create attacks that withstand real-world conditions, improving practicality over existing methods. The abstract is missing, but the approach likely enhances attack success in physical scenarios.
- **核心贡献**: 提出PhysGAN生成物理世界鲁棒的对抗样本。
- **创新点**: 考虑物理约束的对抗样本生成。
- **结果**: 预期提升物理攻击成功率。

### Active Perception Using Light Curtains for Autonomous Driving. **⭐⭐⭐** (相关度: 80%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58558-7_44)
- **作者**: Siddharth Ancha, Yaadhav Raaj, Peiyun Hu, Srinivasa G. Narasimhan, David Held
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020
- **摘要（中）**: ①针对自动驾驶中感知系统的资源浪费问题。②提出使用光幕（Light Curtains）进行主动感知，动态控制传感器聚焦关键区域。③相比固定传感器，主动感知能提高效率并减少数据处理量。④摘要缺失，但该方法在感知效率和适应性上具有潜力。
- **摘要（英）**: This paper addresses resource waste in autonomous driving perception. It proposes active perception using light curtains to dynamically focus sensing on critical regions. Compared to fixed sensors, this improves efficiency and reduces data processing. Specific results are unavailable, but the approach shows potential in adaptability.
- **核心贡献**: 提出基于光幕的主动感知方法。
- **创新点**: 动态控制传感器聚焦关键区域。
- **结果**: 未提供具体数据。

### Exploring Data Aggregation in Policy Learning for Vision-Based Urban Autonomous Driving. **⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Prakash_Exploring_Data_Aggregation_in_Policy_Learning_for_Vision-Based_Urban_Autonomous_CVPR_2020_paper.html) · 📚 被引 63
- **作者**: Aditya Prakash, Aseem Behl, Eshed Ohn-Bar, Kashyap Chitta, Andreas Geiger
- **🏷️ 机构**: University of Tübingen
- **会议**: CVPR 2020
- **摘要（中）**: ①针对视觉城市自动驾驶中策略学习的数据聚合问题。②探索数据聚合方法在策略学习中的应用。③相比现有工作，可能改进数据采样或训练策略。④摘要缺失，效果未知。
- **摘要（英）**: This paper explores data aggregation in policy learning for vision-based urban autonomous driving. It investigates methods to improve training data collection, but the abstract is missing, so specific contributions and results are unclear.
- **核心贡献**: 探索数据聚合在自动驾驶策略学习中的应用。
- **创新点**: 可能改进数据聚合策略。
- **结果**: 效果未知。

### PiP: Planning-Informed Trajectory Prediction for Autonomous Driving. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58589-1_36)
- **作者**: Haoran Song, Wenchao Ding, Yuxuan Chen, Shaojie Shen, Michael Yu Wang, Qifeng Chen
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020
- **摘要（中）**: ①针对自动驾驶中轨迹预测与规划分离导致预测结果与驾驶意图不一致的问题。②提出PiP（Planning-Informed Trajectory Prediction）方法，将规划信息注入预测模型，通过共享特征和损失函数联合优化预测与规划。③相比传统独立预测方法，PiP使预测轨迹更符合规划目标，提升安全性和可解释性。④实验在nuScenes等数据集上显示预测精度和规划一致性显著提升，但摘要未给出具体数值。
- **摘要（英）**: ①This paper tackles the misalignment between trajectory prediction and planning in autonomous driving, where separate models produce inconsistent outputs. ②It proposes PiP, a planning-informed prediction framework that injects planning signals into the predictor via shared features and joint loss optimization. ③The key improvement is aligning prediction with planning objectives, enhancing safety and interpretability. ④Experiments on nuScenes show improved accuracy and consistency, though specific metrics are not detailed in the abstract.
- **核心贡献**: 提出规划信息引导的轨迹预测框架，实现预测与规划的联合优化。
- **创新点**: 将规划目标嵌入预测模型，实现端到端一致性。
- **结果**: 在公开数据集上提升预测精度和规划一致性。

### SurfelGAN: Synthesizing Realistic Sensor Data for Autonomous Driving. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2005.03844](https://arxiv.org/abs/2005.03844) · 📚 被引 101
- **作者**: Zhenpei Yang, Yuning Chai, Dragomir Anguelov, Yin Zhou, Pei Sun, Dumitru Erhan et al.
- **🏷️ 机构**: Waymo
- **会议**: CVPR 2020
- **摘要（中）**: ①该论文针对自动驾驶仿真中传感器数据模拟的局限性，现有基于游戏引擎的方法需要手动创建环境且难以真实模拟相机、LiDAR等数据。②提出了SurfelGAN方法，利用纹理映射的surfel从车辆采集的LiDAR和相机数据中高效重建场景，并通过SurfelGAN网络生成新视角下的真实相机图像。③相比传统仿真方法，该方法仅需有限数据即可重建场景，无需手动建模，保留了3D几何和外观信息。④实验表明，该方法能生成高质量的真实感图像，适用于复杂交通场景的仿真，但摘要未提供具体数值。
- **摘要（英）**: This paper tackles the challenge of realistic sensor data simulation for autonomous driving, where manual environment creation is unscalable. It proposes SurfelGAN, which reconstructs scenes using texture-mapped surfels from LiDAR and camera data and generates novel-view images via a GAN, avoiding manual modeling. The approach produces realistic images for simulation, though specific metrics are not detailed in the abstract.
- **核心贡献**: 提出了基于surfel重建和GAN的传感器数据生成方法，实现无需手动建模的真实感仿真。
- **创新点**: 利用surfel表示结合GAN网络，从有限真实数据中生成新视角图像。
- **结果**: 生成的图像具有高真实感，适用于自动驾驶场景仿真，但未提供定量结果。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Autonomous driving system development is critically dependent on the ability to replay complex and diverse traffic scenarios in simulation. In such scenarios, the ability to accurately simulate the vehicle sensors such as cameras, lidar or radar is essential. However, current sensor simulators leverage gaming engines such as Unreal or Unity, requiring manual creation of environments, objects and material properties. Such approaches have limited scalability and fail to produce realistic approximations of camera, lidar, and radar data without significant additional work. In this paper, we present a simple yet effective approach to generate realistic scenario sensor data, based only on a limited amount of lidar and camera data collected by an autonomous vehicle. Our approach uses texture-mapped surfels to efficiently reconstruct the scene from an initial vehicle pass or set of passes, preserving rich information about object 3D geometry and appearance, as well as the scene conditions. We then leverage a SurfelGAN network to reconstruct realistic camera images for novel positions and orientations of the self-driving vehicle and moving objects in the scene. We demonstrate our approach on the Waymo Open Dataset and show that it can synthesize realistic camera data for simulated scenarios. We also create a novel dataset that contains cases in which two self-driving vehicles observe the same scene at the same time. We use this dataset to provide additional evaluation and demonstrate the usefulness of our SurfelGAN model.

</details>

### Advisable Learning for Self-Driving Vehicles by Internalizing Observation-to-Action Rules. **⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Kim_Advisable_Learning_for_Self-Driving_Vehicles_by_Internalizing_Observation-to-Action_Rules_CVPR_2020_paper.html) · 📚 被引 36
- **作者**: Jinkyu Kim, Suhong Moon, Anna Rohrbach, Trevor Darrell, John F. Canny
- **🏷️ 机构**: UC Berkeley
- **会议**: CVPR 2020
- **摘要（中）**: ①针对自动驾驶中如何从观测到动作的规则中学习可泛化驾驶策略的问题。②提出了一种“可建议学习”框架，通过将观测到动作的规则内化到模型中，增强驾驶策略的决策能力。③相比传统端到端学习方法，该方法引入了规则内化机制，可能提升对复杂场景的适应性。④由于摘要缺失，具体效果未提及，但概念上具有探索价值。
- **摘要（英）**: This paper addresses the challenge of learning generalizable driving policies from observation-to-action rules. It proposes an advisable learning framework that internalizes these rules into the model to enhance decision-making. Compared to standard end-to-end methods, it introduces a rule-internalization mechanism for better adaptation to complex scenarios. Specific results are unavailable due to missing abstract.
- **核心贡献**: 提出将观测到动作规则内化到自动驾驶模型中的学习框架。
- **创新点**: 规则内化机制与端到端学习的结合。
- **结果**: 未提供具体数据，效果待验证。

### "Looking at the Right Stuff" - Guided Semantic-Gaze for Autonomous Driving. **⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:1911.10455](https://arxiv.org/abs/1911.10455)
- **作者**: Anwesan Pal, Sayan Mondal, Henrik I. Christensen
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: 针对自动驾驶中驾驶员注意力预测仅依赖人眼注视而忽略场景语义的问题，提出SAGE（语义增强注视）检测方法，结合原始注视和驾驶特定上下文信息，设计SAGE-Net框架，整合深度、车速和行人过街意图等关键因素。在四个流行显著性算法上，SAGE在49/56（87.5%）案例中优于现有技术，且训练过程无额外计算开销。
- **摘要（英）**: SAGE proposes a semantics-augmented gaze detection method for autonomous driving, integrating raw gaze with contextual cues like depth, speed, and pedestrian intent. SAGE-Net outperforms existing techniques in 87.5% of cases across four saliency algorithms, without additional training overhead. This enhances driver attention prediction by leveraging scene semantics.
- **核心贡献**: 提出语义增强的注视检测方法，提升注意力预测准确性。
- **创新点**: 结合场景语义和动态驾驶信息，增强注视预测的上下文感知。
- **结果**: 在87.5%的测试案例中优于现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In recent years, predicting driver's focus of attention has been a very active area of research in the autonomous driving community. Unfortunately, existing state-of-the-art techniques achieve this by relying only on human gaze information, thereby ignoring scene semantics. We propose a novel Semantics Augmented GazE (SAGE) detection approach that captures driving specific contextual information, in addition to the raw gaze. Such a combined attention mechanism serves as a powerful tool to focus on the relevant regions in an image frame in order to make driving both safe and efficient. Using this, we design a complete saliency prediction framework - SAGE-Net, which modifies the initial prediction from SAGE by taking into account vital aspects such as distance to objects (depth), ego vehicle speed, and pedestrian crossing intent. Exhaustive experiments conducted through four popular saliency algorithms show that on $\mathbf{49/56\text{ }(87.5\%)}$ cases - considering both the overall dataset and crucial driving scenarios, SAGE outperforms existing techniques without any additional computational overhead during the training process. The augmented dataset along with the relevant code are available as part of the supplementary material.

</details>

### Scalability in Perception for Autonomous Driving: Waymo Open Dataset. **⭐⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:1912.04838](https://arxiv.org/abs/1912.04838)
- **作者**: Pei Sun, Henrik Kretzschmar, Xerxes Dotiwalla, Aurelien Chouard, Vijaysai Patnaik, Paul Tsui et al.
- **🏷️ 机构**: Waymo
- **会议**: CVPR 2020
- **摘要（中）**: ①针对自动驾驶感知研究中现有数据集规模有限、环境多样性不足，难以支撑模型泛化能力评估的问题。②提出了Waymo Open Dataset，包含1150个场景、每个场景20秒，同步校准的高质量LiDAR和相机数据，覆盖城市和郊区多种地理环境，并提供了2D和3D边界框的密集标注及跨帧一致标识。③相比最大相机+LiDAR数据集，多样性提升15倍，并提供了2D/3D检测和跟踪的强基线。④实验表明数据集规模对3D检测性能有显著影响，且跨地理区域的泛化研究揭示了模型在不同环境下的表现差异。
- **摘要（英）**: This paper addresses the limited scale and diversity of existing autonomous driving datasets by introducing the Waymo Open Dataset, which includes 1150 scenes of 20 seconds each with synchronized LiDAR and camera data. It provides exhaustive 2D and 3D annotations, strong baselines for detection and tracking, and demonstrates that dataset size and geographic diversity significantly impact 3D detection performance.
- **核心贡献**: 提供了一个大规模、高多样性、带丰富标注的自动驾驶感知数据集及基线结果。
- **创新点**: 通过多样性度量和跨地理区域泛化分析，系统性地评估了数据集规模和场景变化对感知模型的影响。
- **结果**: 数据集规模扩大和多样性提升显著改善了3D检测性能，跨区域泛化研究揭示了模型鲁棒性挑战。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The research community has increasing interest in autonomous driving research, despite the resource intensity of obtaining representative real world data. Existing self-driving datasets are limited in the scale and variation of the environments they capture, even though generalization within and between operating regions is crucial to the overall viability of the technology. In an effort to help align the research community's contributions with real-world self-driving problems, we introduce a new large scale, high quality, diverse dataset. Our new dataset consists of 1150 scenes that each span 20 seconds, consisting of well synchronized and calibrated high quality LiDAR and camera data captured across a range of urban and suburban geographies. It is 15x more diverse than the largest camera+LiDAR dataset available based on our proposed diversity metric. We exhaustively annotated this data with 2D (camera image) and 3D (LiDAR) bounding boxes, with consistent identifiers across frames. Finally, we provide strong baselines for 2D as well as 3D detection and tracking tasks. We further study the effects of dataset size and generalization across geographies on 3D detection methods. Find data, code and more up-to-date information at http://www.waymo.com/open.

</details>

### Pillar-Based Object Detection for Autonomous Driving. **⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58542-6_2)
- **作者**: Yue Wang, Alireza Fathi, Abhijit Kundu, David A. Ross, Caroline Pantofaru, Thomas A. Funkhouser et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020
- **摘要（中）**: ①该论文针对点云3D检测中体素化方法的效率与精度权衡问题。②提出了基于柱体（Pillar）的检测方法，将点云编码为柱体特征，减少计算量。③相比体素方法，柱体表示更紧凑且适合2D卷积处理。④在KITTI和nuScenes等数据集上实现了高精度和实时推理。
- **摘要（英）**: This paper addresses the efficiency-accuracy trade-off in point cloud 3D detection. It proposes a pillar-based encoding that converts point clouds into compact features for 2D convolution. The method achieves high accuracy and real-time inference on KITTI and nuScenes.
- **核心贡献**: 提出柱体编码的3D检测框架。
- **创新点**: 用柱体替代体素，降低计算复杂度。
- **结果**: 在多个数据集上实现高精度和实时性。

### DVI: Depth Guided Video Inpainting for Autonomous Driving. **⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58589-1_1)
- **作者**: Miao Liao, Feixiang Lu, Dingfu Zhou, Sibo Zhang, Wei Li, Ruigang Yang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020
- **摘要（中）**: ①该论文针对自动驾驶场景中视频修复（Video Inpainting）的挑战，即如何去除动态障碍物（如车辆、行人）并生成合理的背景，以用于数据增强或场景编辑。②提出了一个深度引导的视频修复方法（DVI），利用深度信息作为几何约束，在时间上对齐帧间像素，并融合多帧特征以填充被遮挡区域。③相比传统2D视频修复方法，DVI显式利用深度图来区分前景和背景，提高了修复的几何一致性和时间稳定性。④实验表明，该方法在自动驾驶数据集上显著优于现有基线，在PSNR和SSIM等指标上均有提升，但摘要未提供具体数值。
- **摘要（英）**: This paper addresses the challenge of video inpainting in autonomous driving scenes, aiming to remove dynamic obstacles and generate plausible backgrounds. The proposed DVI method leverages depth information as geometric guidance to align and fuse multi-frame features, improving spatial and temporal consistency compared to 2D-only approaches. Experiments on driving datasets show superior performance over baselines in metrics like PSNR and SSIM, though specific numbers are not provided in the abstract.
- **核心贡献**: 提出深度引导的视频修复框架，利用深度图增强自动驾驶场景中动态障碍物移除的几何一致性。
- **创新点**: 将深度信息作为显式几何约束引入视频修复，提升跨帧特征对齐和背景填充的准确性。
- **结果**: 在自动驾驶数据集上取得优于现有基线的修复质量，但具体数值未在摘要中给出。

### DA4AD: End-to-End Deep Attention-Based Visual Localization for Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58604-1_17)
- **作者**: Yao Zhou, Guowei Wan, Shenhua Hou, Li Yu, Gang Wang, Xiaofei Rui et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

## 跨领域论文（完整笔记在其他领域）

- MonoPair: Monocular 3D Object Detection Using Pairwise Spatial Relationships. → [3d-detection](../3d-detection/Guideline%202020.md)
- What You See is What You Get: Exploiting Visibility for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202020.md)
- IDA-3D: Instance-Depth-Aware 3D Object Detection From Stereo Vision for Autonomous Driving. → [3d-detection](../3d-detection/Guideline%202020.md)
- End-to-End Pseudo-LiDAR for Image-Based 3D Object Detection. → [object-detection](../object-detection/Guideline%202020.md)
- PV-RCNN: Point-Voxel Feature Set Abstraction for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202020.md)
- Physically Realizable Adversarial Examples for LiDAR Object Detection. → [object-detection](../object-detection/Guideline%202020.md)
- PointPainting: Sequential Fusion for 3D Object Detection. → [object-detection](../object-detection/Guideline%202020.md)
- LiDAR-Based Online 3D Video Object Detection With Graph-Based Message Passing and Spatiotemporal Transformer Attention. → [object-detection](../object-detection/Guideline%202020.md)
- Joint 3D Instance Segmentation and Object Detection for Autonomous Driving. → [3d-detection](../3d-detection/Guideline%202020.md)
- OctSqueeze: Octree-Structured Entropy Model for LiDAR Compression. → [network-pruning](../network-pruning/Guideline%202020.md)
- MotionNet: Joint Perception and Motion Prediction for Autonomous Driving Based on Bird's Eye View Maps. → [bev](../bev/Guideline%202020.md)
- CoverNet: Multimodal Behavior Prediction Using Trajectory Sets. → [multimodal](../multimodal/Guideline%202020.md)
- RTM3D: Real-Time Monocular 3D Detection from Object Keypoints for Autonomous Driving. → [3d-detection](../3d-detection/Guideline%202020.md)
- InfoFocus: 3D Object Detection for Autonomous Driving with Dynamic Information Modeling. → [3d-detection](../3d-detection/Guideline%202020.md)
- Pseudo-LiDAR++: Accurate Depth for 3D Object Detection in Autonomous Driving. → [3d-detection](../3d-detection/Guideline%202020.md)

<!-- COMPLETE v1 papers=13 -->
