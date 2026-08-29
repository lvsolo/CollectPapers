# Autonomous Driving — 2021 Guideline

> 领域: 自动驾驶感知与系统（端到端驾驶、规划、驾驶场景理解、数据集基准）
> 论文数: 5 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### GeoSim: Realistic Video Simulation via Geometry-Aware Composition for Self-Driving.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Chen_GeoSim_Realistic_Video_Simulation_via_Geometry-Aware_Composition_for_Self-Driving_CVPR_2021_paper.html) · 📚 被引 89
- **作者**: Yun Chen, Frieda Rong, Shivam Duggal, Shenlong Wang, Xinchen Yan, Sivabalan Manivasagam et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Shared Cross-Modal Trajectory Prediction for Autonomous Driving.
- **链接**: [arXiv:2004.00202](https://arxiv.org/abs/2004.00202) · 📚 被引 56
- **作者**: Chiho Choi, Joon Hee Choi, Jiachen Li, Srikanth Malla
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Predicting future trajectories of traffic agents in highly interactive environments is an essential and challenging problem for the safe operation of autonomous driving systems. On the basis of the fact that self-driving vehicles are equipped with various types of sensors (e.g., LiDAR scanner, RGB camera, radar, etc.), we propose a Cross-Modal Embedding framework that aims to benefit from the use of multiple input modalities. At training time, our model learns to embed a set of complementary features in a shared latent space by jointly optimizing the objective functions across different types of input data. At test time, a single input modality (e.g., LiDAR data) is required to generate predictions from the input perspective (i.e., in the LiDAR space), while taking advantages from the model trained with multiple sensor modalities. An extensive evaluation is conducted to show the efficacy of the proposed framework using two benchmark driving datasets.

</details>

### Self-Supervised Pillar Motion Learning for Autonomous Driving.
- **链接**: [arXiv:2104.08683](https://arxiv.org/abs/2104.08683) · 📚 被引 62
- **作者**: Chenxu Luo, Xiaodong Yang, Alan L. Yuille
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D multi-object tracking in LiDAR point clouds is a key ingredient for self-driving vehicles. Existing methods are predominantly based on the tracking-by-detection pipeline and inevitably require a heuristic matching step for the detection association. In this paper, we present SimTrack to simplify the hand-crafted tracking paradigm by proposing an end-to-end trainable model for joint detection and tracking from raw point clouds. Our key design is to predict the first-appear location of each object in a given snippet to get the tracking identity and then update the location based on motion estimation. In the inference, the heuristic matching step can be completely waived by a simple read-off operation. SimTrack integrates the tracked object association, newborn object detection, and dead track killing in a single unified model. We conduct extensive evaluations on two large-scale datasets: nuScenes and Waymo Open Dataset. Experimental results reveal that our simple approach compares favorably with the state-of-the-art methods while ruling out the heuristic matching rules.

</details>

### MultiSiam: Self-supervised Multi-instance Siamese Representation Learning for Autonomous Driving.
- **链接**: [arXiv:2108.12178](https://arxiv.org/abs/2108.12178) · [代码](https://github.com/KaiChen1998/MultiSiam) · 📚 被引 35
- **作者**: Kai Chen, Lanqing Hong, Hang Xu, Zhenguo Li, Dit-Yan Yeung
- **🏷️ 机构**: Hong Kong University of Science and Technology, Huawei Noah&#x2019;s Ark Lab
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Autonomous driving has attracted much attention over the years but turns out to be harder than expected, probably due to the difficulty of labeled data collection for model training. Self-supervised learning (SSL), which leverages unlabeled data only for representation learning, might be a promising way to improve model performance. Existing SSL methods, however, usually rely on the single-centric-object guarantee, which may not be applicable for multi-instance datasets such as street scenes. To alleviate this limitation, we raise two issues to solve: (1) how to define positive samples for cross-view consistency and (2) how to measure similarity in multi-instance circumstances. We first adopt an IoU threshold during random cropping to transfer global-inconsistency to local-consistency. Then, we propose two feature alignment methods to enable 2D feature maps for multi-instance similarity measurement. Additionally, we adopt intra-image clustering with self-attention for further mining intra-image similarity and translation-invariance. Experiments show that, when pre-trained on Waymo dataset, our method called Multi-instance Siamese Network (MultiSiam) remarkably improves generalization ability and achieves state-of-the-art transfer performance on autonomous driving benchmarks, including Cityscapes and BDD100K, while existing SSL counterparts like MoCo, MoCo-v2, and BYOL show significant performance drop. By pre-training on SODA10M, a large-scale autonomous driving dataset, MultiSiam exceeds the ImageNet pre-trained MoCo-v2, demonstrating the potential of domain-specific pre-training. Code will be available at https://github.com/KaiChen1998/MultiSiam.

</details>

### NEAT: Neural Attention Fields for End-to-End Autonomous Driving.
- **链接**: [arXiv:2109.04456](https://arxiv.org/abs/2109.04456) · 📚 被引 212
- **作者**: Kashyap Chitta, Aditya Prakash, Andreas Geiger
- **🏷️ 机构**: Max Planck Institute for Intelligent Systems,T&#x00FC;bingen
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Efficient reasoning about the semantic, spatial, and temporal structure of a scene is a crucial prerequisite for autonomous driving. We present NEural ATtention fields (NEAT), a novel representation that enables such reasoning for end-to-end imitation learning models. NEAT is a continuous function which maps locations in Bird's Eye View (BEV) scene coordinates to waypoints and semantics, using intermediate attention maps to iteratively compress high-dimensional 2D image features into a compact representation. This allows our model to selectively attend to relevant regions in the input while ignoring information irrelevant to the driving task, effectively associating the images with the BEV representation. In a new evaluation setting involving adverse environmental conditions and challenging scenarios, NEAT outperforms several strong baselines and achieves driving scores on par with the privileged CARLA expert used to generate its training data. Furthermore, visualizing the attention maps for models with NEAT intermediate representations provides improved interpretability.

</details>

### GeoSim: Realistic Video Simulation via Geometry-Aware Composition for Self-Driving.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Chen_GeoSim_Realistic_Video_Simulation_via_Geometry-Aware_Composition_for_Self-Driving_CVPR_2021_paper.html) · 📚 被引 89
- **作者**: Yun Chen, Frieda Rong, Shivam Duggal, Shenlong Wang, Xinchen Yan, Sivabalan Manivasagam et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### AdvSim: Generating Safety-Critical Scenarios for Self-Driving Vehicles.
- **链接**: [arXiv:2101.06549](https://arxiv.org/abs/2101.06549) · 📚 被引 177
- **作者**: Jingkang Wang, Ava Pun, James Tu, Sivabalan Manivasagam, Abbas Sadat, Sergio Casas et al.
- **🏷️ 机构**: Waabi / University of Toronto
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> As self-driving systems become better, simulating scenarios where the autonomy stack may fail becomes more important. Traditionally, those scenarios are generated for a few scenes with respect to the planning module that takes ground-truth actor states as input. This does not scale and cannot identify all possible autonomy failures, such as perception failures due to occlusion. In this paper, we propose AdvSim, an adversarial framework to generate safety-critical scenarios for any LiDAR-based autonomy system. Given an initial traffic scenario, AdvSim modifies the actors' trajectories in a physically plausible manner and updates the LiDAR sensor data to match the perturbed world. Importantly, by simulating directly from sensor data, we obtain adversarial scenarios that are safety-critical for the full autonomy stack. Our experiments show that our approach is general and can identify thousands of semantically meaningful safety-critical scenarios for a wide range of modern self-driving systems. Furthermore, we show that the robustness and safety of these systems can be further improved by training them with scenarios generated by AdvSim.

</details>

## 🆕 增量新增

### Multi-Modal Fusion Transformer for End-to-End Autonomous Driving. **⭐⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2104.09224](https://arxiv.org/abs/2104.09224) · 📚 被引 548
- **作者**: Aditya Prakash, Kashyap Chitta, Andreas Geiger
- **🏷️ 机构**: Max Planck Institute for Intelligent Systems,T&#x00FC;bingen
- **会议**: CVPR 2021
- **摘要（中）**: ①针对端到端自动驾驶中多传感器融合的全局上下文推理不足问题。②提出了TransFuser，一种多模态融合Transformer，通过注意力机制整合图像和LiDAR表示。③相比基于几何的融合方法，该方法能捕捉全局上下文，如交通灯变化对远处车辆的影响，在复杂场景中表现更好。④在CARLA模拟器中达到最先进的驾驶性能，但摘要未提供具体数值。
- **摘要（英）**: This paper addresses insufficient global contextual reasoning in multi-sensor fusion for end-to-end autonomous driving. It proposes TransFuser, a multi-modal fusion transformer that integrates image and LiDAR representations via attention. Compared to geometry-based fusion, it captures global context better, achieving state-of-the-art driving performance in CARLA, though specific metrics are not given in the abstract.
- **核心贡献**: 提出了TransFuser，利用注意力机制实现图像和LiDAR的全局上下文融合。
- **创新点**: 将Transformer应用于多模态融合，解决几何融合的局限性。
- **结果**: 在CARLA模拟器中达到最先进的驾驶性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> How should representations from complementary sensors be integrated for autonomous driving? Geometry-based sensor fusion has shown great promise for perception tasks such as object detection and motion forecasting. However, for the actual driving task, the global context of the 3D scene is key, e.g. a change in traffic light state can affect the behavior of a vehicle geometrically distant from that traffic light. Geometry alone may therefore be insufficient for effectively fusing representations in end-to-end driving models. In this work, we demonstrate that imitation learning policies based on existing sensor fusion methods under-perform in the presence of a high density of dynamic agents and complex scenarios, which require global contextual reasoning, such as handling traffic oncoming from multiple directions at uncontrolled intersections. Therefore, we propose TransFuser, a novel Multi-Modal Fusion Transformer, to integrate image and LiDAR representations using attention. We experimentally validate the efficacy of our approach in urban settings involving complex scenarios using the CARLA urban driving simulator. Our approach achieves state-of-the-art driving performance while reducing collisions by 76% compared to geometry-based fusion.

</details>

### An Empirical Study of Adder Neural Networks for Object Detection. **⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2112.13608](https://arxiv.org/abs/2112.13608)
- **作者**: Xinghao Chen, Chang Xu, Minjing Dong, Chunjing Xu, Yunhe Wang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021
- **摘要（中）**: ①针对加法神经网络在目标检测中应用时性能下降和特征稀疏的问题。②提出了对AdderNets用于目标检测的实证研究，包括调整批归一化统计、增加捷径连接和设计新特征融合架构。③相比已有工作，该研究探索了加法检测器的设计选择，并提出了Adder FCOS。④在COCO val上达到37.8% AP，与卷积对应物性能相当，但能耗降低约1.4倍。
- **摘要（英）**: This paper addresses performance degradation and sparse features when applying AdderNets to object detection. It presents an empirical study, including unfreezing batch norm statistics, adding shortcuts, and designing a new fusion architecture, proposing Adder FCOS. Compared to prior work, it explores design choices, achieving 37.8% AP on COCO val, comparable to convolutional counterparts with about 1.4x energy reduction.
- **核心贡献**: 系统研究了AdderNets在目标检测中的应用，并提出了Adder FCOS。
- **创新点**: 针对加法层特性设计了检测器架构和训练策略。
- **结果**: 在COCO上达到37.8% AP，能耗降低约1.4倍。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Adder neural networks (AdderNets) have shown impressive performance on image classification with only addition operations, which are more energy efficient than traditional convolutional neural networks built with multiplications. Compared with classification, there is a strong demand on reducing the energy consumption of modern object detectors via AdderNets for real-world applications such as autonomous driving and face detection. In this paper, we present an empirical study of AdderNets for object detection. We first reveal that the batch normalization statistics in the pre-trained adder backbone should not be frozen, since the relatively large feature variance of AdderNets. Moreover, we insert more shortcut connections in the neck part and design a new feature fusion architecture for avoiding the sparse features of adder layers. We present extensive ablation studies to explore several design choices of adder detectors. Comparisons with state-of-the-arts are conducted on COCO and PASCAL VOC benchmarks. Specifically, the proposed Adder FCOS achieves a 37.8\% AP on the COCO val set, demonstrating comparable performance to that of the convolutional counterpart with an about $1.4\times$ energy reduction.

</details>

## 跨领域论文（完整笔记在其他领域）

- 3DIoUMatch: Leveraging IoU Prediction for Semi-Supervised 3D Object Detection. → [object-detection](../object-detection/Guideline%202021.md)
- To the Point: Efficient 3D Object Detection in the Range Image With Graph Convolution Kernels. → [3d-detection](../3d-detection/Guideline%202021.md)
- Offboard 3D Object Detection From Point Cloud Sequences. → [3d-detection](../3d-detection/Guideline%202021.md)
- Categorical Depth Distribution Network for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202021.md)
- Unsupervised Object Detection With LIDAR Clues. → [object-detection](../object-detection/Guideline%202021.md)
- 3D-MAN: 3D Multi-Frame Attention Network for Object Detection. → [multi-camera-perception](../multi-camera-perception/Guideline%202021.md)
- Monocular 3D Object Detection: An Extrinsic Parameter Free Approach. → [3d-detection](../3d-detection/Guideline%202021.md)
- LiDAR R-CNN: An Efficient and Universal 3D Object Detector. → [3d-detection](../3d-detection/Guideline%202021.md)
- Object DGCNN: 3D Object Detection using Dynamic Graphs. → [3d-detection](../3d-detection/Guideline%202021.md)
- Revisiting 3D Object Detection From an Egocentric Perspective. → [3d-detection](../3d-detection/Guideline%202021.md)
- Progressive Coordinate Transforms for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202021.md)
- 3D Siamese Voxel-to-BEV Tracker for Sparse Point Clouds. → [bev](../bev/Guideline%202021.md)
- Multimodal Virtual Point 3D Detection. → [3d-detection](../3d-detection/Guideline%202021.md)
<!-- COMPLETE v1 papers=9 -->
