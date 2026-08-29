# Autonomous Driving — 2020 Guideline

> 领域: 自动驾驶感知与系统（端到端驾驶、规划、驾驶场景理解、数据集基准）
> 论文数: 10 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### MotionNet: Joint Perception and Motion Prediction for Autonomous Driving Based on Bird's Eye View Maps.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Wu_MotionNet_Joint_Perception_and_Motion_Prediction_for_Autonomous_Driving_Based_CVPR_2020_paper.html)
- **作者**: Pengxiang Wu, Siheng Chen, Dimitris N. Metaxas
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### nuScenes: A Multimodal Dataset for Autonomous Driving.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Caesar_nuScenes_A_Multimodal_Dataset_for_Autonomous_Driving_CVPR_2020_paper.html)
- **作者**: Holger Caesar, Varun Bankiti, Alex H. Lang, Sourabh Vora, Venice Erin Liong, Qiang Xu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### PhysGAN: Generating Physical-World-Resilient Adversarial Examples for Autonomous Driving.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Kong_PhysGAN_Generating_Physical-World-Resilient_Adversarial_Examples_for_Autonomous_Driving_CVPR_2020_paper.html) · 📚 被引 136
- **作者**: Zelun Kong, Junfeng Guo, Ang Li, Cong Liu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

</details>

### Active Perception Using Light Curtains for Autonomous Driving.
- **链接**: [arXiv:2008.02191](https://arxiv.org/abs/2008.02191) · 📚 被引 7
- **作者**: Siddharth Ancha, Yaadhav Raaj, Peiyun Hu, Srinivasa G. Narasimhan, David Held
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In recent years, predicting driver's focus of attention has been a very active area of research in the autonomous driving community. Unfortunately, existing state-of-the-art techniques achieve this by relying only on human gaze information, thereby ignoring scene semantics. We propose a novel Semantics Augmented GazE (SAGE) detection approach that captures driving specific contextual information, in addition to the raw gaze. Such a combined attention mechanism serves as a powerful tool to focus on the relevant regions in an image frame in order to make driving both safe and efficient. Using this, we design a complete saliency prediction framework - SAGE-Net, which modifies the initial prediction from SAGE by taking into account vital aspects such as distance to objects (depth), ego vehicle speed, and pedestrian crossing intent. Exhaustive experiments conducted through four popular saliency algorithms show that on $\mathbf{49/56\text{ }(87.5\%)}$ cases - considering both the overall dataset and crucial driving scenarios, SAGE outperforms existing techniques without any additional computational overhead during the training process. The augmented dataset along with the relevant code are available as part of the supplementary material.

</details>

### Exploring Data Aggregation in Policy Learning for Vision-Based Urban Autonomous Driving.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Prakash_Exploring_Data_Aggregation_in_Policy_Learning_for_Vision-Based_Urban_Autonomous_CVPR_2020_paper.html) · 📚 被引 63
- **作者**: Aditya Prakash, Aseem Behl, Eshed Ohn-Bar, Kashyap Chitta, Andreas Geiger
- **🏷️ 机构**: University of Tübingen
- **会议**: CVPR 2020

### PiP: Planning-Informed Trajectory Prediction for Autonomous Driving.
- **链接**: [arXiv:2003.11476](https://arxiv.org/abs/2003.11476)
- **作者**: Haoran Song, Wenchao Ding, Yuxuan Chen, Shaojie Shen, Michael Yu Wang, Qifeng Chen
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The research community has increasing interest in autonomous driving research, despite the resource intensity of obtaining representative real world data. Existing self-driving datasets are limited in the scale and variation of the environments they capture, even though generalization within and between operating regions is crucial to the overall viability of the technology. In an effort to help align the research community's contributions with real-world self-driving problems, we introduce a new large scale, high quality, diverse dataset. Our new dataset consists of 1150 scenes that each span 20 seconds, consisting of well synchronized and calibrated high quality LiDAR and camera data captured across a range of urban and suburban geographies. It is 15x more diverse than the largest camera+LiDAR dataset available based on our proposed diversity metric. We exhaustively annotated this data with 2D (camera image) and 3D (LiDAR) bounding boxes, with consistent identifiers across frames. Finally, we provide strong baselines for 2D as well as 3D detection and tracking tasks. We further study the effects of dataset size and generalization across geographies on 3D detection methods. Find data, code and more up-to-date information at http://www.waymo.com/open.

</details>

### SurfelGAN: Synthesizing Realistic Sensor Data for Autonomous Driving.
- **链接**: [arXiv:2005.03844](https://arxiv.org/abs/2005.03844) · 📚 被引 101
- **作者**: Zhenpei Yang, Yuning Chai, Dragomir Anguelov, Yin Zhou, Pei Sun, Dumitru Erhan et al.
- **🏷️ 机构**: Waymo
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Autonomous driving system development is critically dependent on the ability to replay complex and diverse traffic scenarios in simulation. In such scenarios, the ability to accurately simulate the vehicle sensors such as cameras, lidar or radar is essential. However, current sensor simulators leverage gaming engines such as Unreal or Unity, requiring manual creation of environments, objects and material properties. Such approaches have limited scalability and fail to produce realistic approximations of camera, lidar, and radar data without significant additional work. In this paper, we present a simple yet effective approach to generate realistic scenario sensor data, based only on a limited amount of lidar and camera data collected by an autonomous vehicle. Our approach uses texture-mapped surfels to efficiently reconstruct the scene from an initial vehicle pass or set of passes, preserving rich information about object 3D geometry and appearance, as well as the scene conditions. We then leverage a SurfelGAN network to reconstruct realistic camera images for novel positions and orientations of the self-driving vehicle and moving objects in the scene. We demonstrate our approach on the Waymo Open Dataset and show that it can synthesize realistic camera data for simulated scenarios. We also create a novel dataset that contains cases in which two self-driving vehicles observe the same scene at the same time. We use this dataset to provide additional evaluation and demonstrate the usefulness of our SurfelGAN model.

</details>

### Advisable Learning for Self-Driving Vehicles by Internalizing Observation-to-Action Rules.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Kim_Advisable_Learning_for_Self-Driving_Vehicles_by_Internalizing_Observation-to-Action_Rules_CVPR_2020_paper.html) · 📚 被引 36
- **作者**: Jinkyu Kim, Suhong Moon, Anna Rohrbach, Trevor Darrell, John F. Canny
- **🏷️ 机构**: UC Berkeley
- **会议**: CVPR 2020

## 跨领域论文（完整笔记在其他领域）

- IDA-3D: Instance-Depth-Aware 3D Object Detection From Stereo Vision for Autonomous Driving. → [3d-detection](../3d-detection/Guideline%202020.md)
- Joint 3D Instance Segmentation and Object Detection for Autonomous Driving. → [3d-detection](../3d-detection/Guideline%202020.md)
