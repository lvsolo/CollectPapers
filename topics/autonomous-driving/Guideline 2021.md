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
