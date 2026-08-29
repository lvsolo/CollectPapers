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

## 🆕 增量新增

### Transformer-Based Sensor Fusion for Autonomous Driving: A Survey. **⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2302.11481](https://arxiv.org/abs/2302.11481) · 📚 被引 34
- **作者**: Apoorv Singh
- **🏷️ 机构**: Motional Carnegie Mellon University
- **会议**: ICCV 2023
- **摘要（中）**: 针对自动驾驶中基于Transformer的传感器融合3D检测缺乏系统综述的问题，该论文提供了深入文献调研。内容涵盖Transformer检测头与CNN特征编码器结合的传感器融合框架，并简要介绍ViT基础和非Transformer方法。论文总结了传感器融合趋势并指出未来研究方向，附有持续更新的资源链接。该综述对自动驾驶感知研究者具有重要参考价值。
- **摘要（英）**: This survey provides an in-depth review of transformer-based sensor fusion for 3D object detection in autonomous driving, covering frameworks, ViT basics, and non-transformer methods. It summarizes trends and future directions, serving as a valuable reference for researchers.
- **核心贡献**: 提供了Transformer传感器融合3D检测的全面综述和趋势总结。
- **创新点**: 聚焦Transformer在传感器融合中的应用，并持续更新资源。
- **结果**: 为研究者提供了清晰的领域概览和未来方向。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Sensor fusion is an essential topic in many perception systems, such as autonomous driving and robotics. Transformers-based detection head and CNN-based feature encoder to extract features from raw sensor-data has emerged as one of the best performing sensor-fusion 3D-detection-framework, according to the dataset leaderboards. In this work we provide an in-depth literature survey of transformer based 3D-object detection task in the recent past, primarily focusing on the sensor fusion. We also briefly go through the Vision transformers (ViT) basics, so that readers can easily follow through the paper. Moreover, we also briefly go through few of the non-transformer based less-dominant methods for sensor fusion for autonomous driving. In conclusion we summarize with sensor-fusion trends to follow and provoke future research. More updated summary can be found at: https://github.com/ApoorvRoboticist/Transformers-Sensor-Fusion

</details>

### Benchmarking Robustness of 3D Object Detection to Common Corruptions in Autonomous Driving. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2303.11040](https://arxiv.org/abs/2303.11040) · 📚 被引 142
- **作者**: Yinpeng Dong, Caixin Kang, Jinlai Zhang, Zijian Zhu, Yikai Wang, Xiao Yang et al.
- **🏷️ 机构**: Institute for AI, Tsinghua-Bosch Joint ML Center, Tsinghua-China Mobile Communications Group Co., Ltd. Joint Institute, Tsinghua University,Dept. of Comp. Sci. and Tech., Institute of Artificial Intelligence, Beihang University, Guangxi University
- **会议**: CVPR 2023
- **摘要（中）**: ①针对3D检测器在真实世界恶劣天气、传感器噪声等干扰下鲁棒性不足的问题。②设计了27种针对LiDAR和相机输入的常见损坏类型，在KITTI、nuScenes和Waymo上建立鲁棒性基准KITTI-C、nuScenes-C和Waymo-C，并评估24种3D检测模型。③首次系统性地对3D检测的鲁棒性进行基准测试，涵盖多模态和单模态模型。④发现运动级损坏威胁最大，LiDAR-相机融合模型鲁棒性更好，相机-only模型对图像损坏极其脆弱。
- **摘要（英）**: This paper addresses the lack of robustness in 3D detectors under real-world corruptions by designing 27 types of corruptions for LiDAR and camera inputs, establishing benchmarks KITTI-C, nuScenes-C, and Waymo-C, and evaluating 24 models. Key findings include motion-level corruptions being most threatening, fusion models being more robust, and camera-only models being highly vulnerable to image corruptions.
- **核心贡献**: 建立3D检测鲁棒性基准并揭示关键脆弱性。
- **创新点**: 首次设计多模态损坏类型并大规模评估3D检测鲁棒性。
- **结果**: 发现运动级损坏影响最大，融合模型更鲁棒。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D object detection is an important task in autonomous driving to perceive the surroundings. Despite the excellent performance, the existing 3D detectors lack the robustness to real-world corruptions caused by adverse weathers, sensor noises, etc., provoking concerns about the safety and reliability of autonomous driving systems. To comprehensively and rigorously benchmark the corruption robustness of 3D detectors, in this paper we design 27 types of common corruptions for both LiDAR and camera inputs considering real-world driving scenarios. By synthesizing these corruptions on public datasets, we establish three corruption robustness benchmarks -- KITTI-C, nuScenes-C, and Waymo-C. Then, we conduct large-scale experiments on 24 diverse 3D object detection models to evaluate their corruption robustness. Based on the evaluation results, we draw several important findings, including: 1) motion-level corruptions are the most threatening ones that lead to significant performance drop of all models; 2) LiDAR-camera fusion models demonstrate better robustness; 3) camera-only models are extremely vulnerable to image corruptions, showing the indispensability of LiDAR point clouds. We release the benchmarks and codes at https://github.com/kkkcx/3D_Corruptions_AD. We hope that our benchmarks and findings can provide insights for future research on developing robust 3D object detection models.

</details>

### Temporal Consistent 3D LiDAR Representation Learning for Semantic Perception in Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00505) · 📚 被引 43
- **作者**: Lucas Nunes, Louis Wiesmann, Rodrigo Marcuzzi, Xieyuanli Chen, Jens Behley, Cyrill Stachniss
- **🏷️ 机构**: University of Bonn
- **会议**: CVPR 2023

### FEND: A Future Enhanced Distribution-Aware Contrastive Learning Framework for Long-Tail Trajectory Prediction.
- **链接**: [arXiv:2303.16574](https://arxiv.org/abs/2303.16574) · 📚 被引 44
- **作者**: Yuning Wang, Pu Zhang, Lei Bai, Jianru Xue
- **🏷️ 机构**: Institute of Artificial Intelligence and Robotics, Xi&#x0027;an Jiaotong University,China, DiDi Chuxing,China, Shanghai AI Laboratory,China
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Predicting the future trajectories of the traffic agents is a gordian technique in autonomous driving. However, trajectory prediction suffers from data imbalance in the prevalent datasets, and the tailed data is often more complicated and safety-critical. In this paper, we focus on dealing with the long-tail phenomenon in trajectory prediction. Previous methods dealing with long-tail data did not take into account the variety of motion patterns in the tailed data. In this paper, we put forward a future enhanced contrastive learning framework to recognize tail trajectory patterns and form a feature space with separate pattern clusters. Furthermore, a distribution aware hyper predictor is brought up to better utilize the shaped feature space. Our method is a model-agnostic framework and can be plugged into many well-known baselines. Experimental results show that our framework outperforms the state-of-the-art long-tail prediction method on tailed samples by 9.5% on ADE and 8.5% on FDE, while maintaining or slightly improving the averaged performance. Our method also surpasses many long-tail techniques on trajectory prediction task.

</details>

### Optimizing the Placement of Roadside LiDARs for Autonomous Driving.
- **链接**: [arXiv:2310.07247](https://arxiv.org/abs/2310.07247) · 📚 被引 19
- **作者**: Wentao Jiang, Hao Xiang, Xinyu Cai, Runsheng Xu, Jiaqi Ma, Yikang Li et al.
- **🏷️ 机构**: Beihang University, UCLA, Shanghai AI Laboratory
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-agent cooperative perception is an increasingly popular topic in the field of autonomous driving, where roadside LiDARs play an essential role. However, how to optimize the placement of roadside LiDARs is a crucial but often overlooked problem. This paper proposes an approach to optimize the placement of roadside LiDARs by selecting optimized positions within the scene for better perception performance. To efficiently obtain the best combination of locations, a greedy algorithm based on perceptual gain is proposed, which selects the location that can maximize the perceptual gain sequentially. We define perceptual gain as the increased perceptual capability when a new LiDAR is placed. To obtain the perception capability, we propose a perception predictor that learns to evaluate LiDAR placement using only a single point cloud frame. A dataset named Roadside-Opt is created using the CARLA simulator to facilitate research on the roadside LiDAR placement problem.

</details>

### MV-DeepSDF: Implicit Modeling with Multi-Sweep Point Clouds for 3D Vehicle Reconstruction in Autonomous Driving.
- **链接**: [arXiv:2309.16715](https://arxiv.org/abs/2309.16715) · 📚 被引 15
- **作者**: Yibo Liu, Kelly Zhu, Guile Wu, Yuan Ren, Bingbing Liu, Yang Liu et al.
- **🏷️ 机构**: Huawei Noah&#x2019;s Ark Lab, York University
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Reconstructing 3D vehicles from noisy and sparse partial point clouds is of great significance to autonomous driving. Most existing 3D reconstruction methods cannot be directly applied to this problem because they are elaborately designed to deal with dense inputs with trivial noise. In this work, we propose a novel framework, dubbed MV-DeepSDF, which estimates the optimal Signed Distance Function (SDF) shape representation from multi-sweep point clouds to reconstruct vehicles in the wild. Although there have been some SDF-based implicit modeling methods, they only focus on single-view-based reconstruction, resulting in low fidelity. In contrast, we first analyze multi-sweep consistency and complementarity in the latent feature space and propose to transform the implicit space shape estimation problem into an element-to-set feature extraction problem. Then, we devise a new architecture to extract individual element-level representations and aggregate them to generate a set-level predicted latent code. This set-level latent code is an expression of the optimal 3D shape in the implicit space, and can be subsequently decoded to a continuous SDF of the vehicle. In this way, our approach learns consistent and complementary information among multi-sweeps for 3D vehicle reconstruction. We conduct thorough experiments on two real-world autonomous driving datasets (Waymo and KITTI) to demonstrate the superiority of our approach over state-of-the-art alternative methods both qualitatively and quantitatively.

</details>

### Zenseact Open Dataset: A large-scale and diverse multimodal dataset for autonomous driving.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01846) · 📚 被引 70
- **作者**: Mina Alibeigi, William Ljungbergh, Adam Tonderski, Georg Hess, Adam Lilja, Carl Lindström et al.
- **🏷️ 机构**: Zenseact
- **会议**: ICCV 2023

### Video Task Decathlon: Unifying Image and Video Tasks in Autonomous Driving.
- **链接**: [arXiv:2309.04422](https://arxiv.org/abs/2309.04422) · 📚 被引 11
- **作者**: Thomas E. Huang, Yifan Liu, Luc Van Gool, Fisher Yu
- **🏷️ 机构**: ETH Z&#x00FC;rich
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Performing multiple heterogeneous visual tasks in dynamic scenes is a hallmark of human perception capability. Despite remarkable progress in image and video recognition via representation learning, current research still focuses on designing specialized networks for singular, homogeneous, or simple combination of tasks. We instead explore the construction of a unified model for major image and video recognition tasks in autonomous driving with diverse input and output structures. To enable such an investigation, we design a new challenge, Video Task Decathlon (VTD), which includes ten representative image and video tasks spanning classification, segmentation, localization, and association of objects and pixels. On VTD, we develop our unified network, VTDNet, that uses a single structure and a single set of weights for all ten tasks. VTDNet groups similar tasks and employs task interaction stages to exchange information within and between task groups. Given the impracticality of labeling all tasks on all frames, and the performance degradation associated with joint training of many tasks, we design a Curriculum training, Pseudo-labeling, and Fine-tuning (CPF) scheme to successfully train VTDNet on all tasks and mitigate performance loss. Armed with CPF, VTDNet significantly outperforms its single-task counterparts on most tasks with only 20% overall computations. VTD is a promising new direction for exploring the unification of perception tasks in autonomous driving.

</details>

### GameFormer: Game-theoretic Modeling and Learning of Transformer-based Interactive Prediction and Planning for Autonomous Driving.
- **链接**: [arXiv:2303.05760](https://arxiv.org/abs/2303.05760) · 📚 被引 145
- **作者**: Zhiyu Huang, Haochen Liu, Chen Lv
- **🏷️ 机构**: Nanyang Technological University,Singapore
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Autonomous vehicles operating in complex real-world environments require accurate predictions of interactive behaviors between traffic participants. This paper tackles the interaction prediction problem by formulating it with hierarchical game theory and proposing the GameFormer model for its implementation. The model incorporates a Transformer encoder, which effectively models the relationships between scene elements, alongside a novel hierarchical Transformer decoder structure. At each decoding level, the decoder utilizes the prediction outcomes from the previous level, in addition to the shared environmental context, to iteratively refine the interaction process. Moreover, we propose a learning process that regulates an agent's behavior at the current level to respond to other agents' behaviors from the preceding level. Through comprehensive experiments on large-scale real-world driving datasets, we demonstrate the state-of-the-art accuracy of our model on the Waymo interaction prediction task. Additionally, we validate the model's capacity to jointly reason about the motion plan of the ego agent and the behaviors of multiple agents in both open-loop and closed-loop planning tests, outperforming various baseline methods. Furthermore, we evaluate the efficacy of our model on the nuPlan planning benchmark, where it achieves leading performance.

</details>

### DriveAdapter: Breaking the Coupling Barrier of Perception and Planning in End-to-End Autonomous Driving.
- **链接**: [arXiv:2308.00398](https://arxiv.org/abs/2308.00398) · 📚 被引 76
- **作者**: Xiaosong Jia, Yulu Gao, Li Chen, Junchi Yan, Patrick Langechuan Liu, Hongyang Li
- **🏷️ 机构**: Shanghai Jiao Tong University,MoE Key Lab of Artificial Intelligence, Shanghai AI Lab,OpenDriveLab, Anker Innovations
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> End-to-end autonomous driving aims to build a fully differentiable system that takes raw sensor data as inputs and directly outputs the planned trajectory or control signals of the ego vehicle. State-of-the-art methods usually follow the `Teacher-Student' paradigm. The Teacher model uses privileged information (ground-truth states of surrounding agents and map elements) to learn the driving strategy. The student model only has access to raw sensor data and conducts behavior cloning on the data collected by the teacher model. By eliminating the noise of the perception part during planning learning, state-of-the-art works could achieve better performance with significantly less data compared to those coupled ones. However, under the current Teacher-Student paradigm, the student model still needs to learn a planning head from scratch, which could be challenging due to the redundant and noisy nature of raw sensor inputs and the casual confusion issue of behavior cloning. In this work, we aim to explore the possibility of directly adopting the strong teacher model to conduct planning while letting the student model focus more on the perception part. We find that even equipped with a SOTA perception model, directly letting the student model learn the required inputs of the teacher model leads to poor driving performance, which comes from the large distribution gap between predicted privileged inputs and the ground-truth. To this end, we propose DriveAdapter, which employs adapters with the feature alignment objective function between the student (perception) and teacher (planning) modules. Additionally, since the pure learning-based teacher model itself is imperfect and occasionally breaks safety rules, we propose a method of action-guided feature learning with a mask for those imperfect teacher features to further inject the priors of hand-crafted rules into the learning process.

</details>

### VAD: Vectorized Scene Representation for Efficient Autonomous Driving.
- **链接**: [arXiv:2303.12077](https://arxiv.org/abs/2303.12077) · 📚 被引 319
- **作者**: Bo Jiang, Shaoyu Chen, Qing Xu, Bencheng Liao, Jiajie Chen, Helong Zhou et al.
- **🏷️ 机构**: Huazhong University of Science &amp; Technology, Horizon Robotics
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Autonomous driving requires a comprehensive understanding of the surrounding environment for reliable trajectory planning. Previous works rely on dense rasterized scene representation (e.g., agent occupancy and semantic map) to perform planning, which is computationally intensive and misses the instance-level structure information. In this paper, we propose VAD, an end-to-end vectorized paradigm for autonomous driving, which models the driving scene as a fully vectorized representation. The proposed vectorized paradigm has two significant advantages. On one hand, VAD exploits the vectorized agent motion and map elements as explicit instance-level planning constraints which effectively improves planning safety. On the other hand, VAD runs much faster than previous end-to-end planning methods by getting rid of computation-intensive rasterized representation and hand-designed post-processing steps. VAD achieves state-of-the-art end-to-end planning performance on the nuScenes dataset, outperforming the previous best method by a large margin. Our base model, VAD-Base, greatly reduces the average collision rate by 29.0% and runs 2.5x faster. Besides, a lightweight variant, VAD-Tiny, greatly improves the inference speed (up to 9.3x) while achieving comparable planning performance. We believe the excellent performance and the high efficiency of VAD are critical for the real-world deployment of an autonomous driving system. Code and models are available at https://github.com/hustvl/VAD for facilitating future research.

</details>

### Unsupervised 3D Perception with 2D Vision-Language Distillation for Autonomous Driving.
- **链接**: [arXiv:2309.14491](https://arxiv.org/abs/2309.14491) · 📚 被引 27
- **作者**: Mahyar Najibi, Jingwei Ji, Yin Zhou, Charles R. Qi, Xinchen Yan, Scott Ettinger et al.
- **🏷️ 机构**: Waymo LLC
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Closed-set 3D perception models trained on only a pre-defined set of object categories can be inadequate for safety critical applications such as autonomous driving where new object types can be encountered after deployment. In this paper, we present a multi-modal auto labeling pipeline capable of generating amodal 3D bounding boxes and tracklets for training models on open-set categories without 3D human labels. Our pipeline exploits motion cues inherent in point cloud sequences in combination with the freely available 2D image-text pairs to identify and track all traffic participants. Compared to the recent studies in this domain, which can only provide class-agnostic auto labels limited to moving objects, our method can handle both static and moving objects in the unsupervised manner and is able to output open-vocabulary semantic labels thanks to the proposed vision-language knowledge distillation. Experiments on the Waymo Open Dataset show that our approach outperforms the prior work by significant margins on various unsupervised 3D perception tasks.

</details>

### Domain generalization of 3D semantic segmentation in autonomous driving.
- **链接**: [arXiv:2212.04245](https://arxiv.org/abs/2212.04245) · 📚 被引 34
- **作者**: Jules Sanchez, Jean-Emmanuel Deschaud, François Goulette
- **🏷️ 机构**: Mines Paris - PSL, PSL University,Centre for Robotics,Paris,France,75006
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Using deep learning, 3D autonomous driving semantic segmentation has become a well-studied subject, with methods that can reach very high performance. Nonetheless, because of the limited size of the training datasets, these models cannot see every type of object and scene found in real-world applications. The ability to be reliable in these various unknown environments is called \textup{domain generalization}. Despite its importance, domain generalization is relatively unexplored in the case of 3D autonomous driving semantic segmentation. To fill this gap, this paper presents the first benchmark for this application by testing state-of-the-art methods and discussing the difficulty of tackling Laser Imaging Detection and Ranging (LiDAR) domain shifts. We also propose the first method designed to address this domain generalization, which we call 3DLabelProp. This method relies on leveraging the geometry and sequentiality of the LiDAR data to enhance its generalization performances by working on partially accumulated point clouds. It reaches a mean Intersection over Union (mIoU) of 50.4% on SemanticPOSS and of 55.2% on PandaSet solid-state LiDAR while being trained only on SemanticKITTI, making it the state-of-the-art method for generalization (+5% and +33% better, respectively, than the second best method). The code for this method is available on GitHub: https://github.com/JulesSanchez/3DLabelProp.

</details>

### Does Physical Adversarial Example Really Matter to Autonomous Driving? Towards System-Level Effect of Adversarial Object Evasion Attack.
- **链接**: [arXiv:2308.11894](https://arxiv.org/abs/2308.11894) · 📚 被引 7
- **作者**: Ningfei Wang, Yunpeng Luo, Takami Sato, Kaidi Xu, Qi Alfred Chen
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In autonomous driving (AD), accurate perception is indispensable to achieving safe and secure driving. Due to its safety-criticality, the security of AD perception has been widely studied. Among different attacks on AD perception, the physical adversarial object evasion attacks are especially severe. However, we find that all existing literature only evaluates their attack effect at the targeted AI component level but not at the system level, i.e., with the entire system semantics and context such as the full AD pipeline. Thereby, this raises a critical research question: can these existing researches effectively achieve system-level attack effects (e.g., traffic rule violations) in the real-world AD context? In this work, we conduct the first measurement study on whether and how effectively the existing designs can lead to system-level effects, especially for the STOP sign-evasion attacks due to their popularity and severity. Our evaluation results show that all the representative prior works cannot achieve any system-level effects. We observe two design limitations in the prior works: 1) physical model-inconsistent object size distribution in pixel sampling and 2) lack of vehicle plant model and AD system model consideration. Then, we propose SysAdv, a novel system-driven attack design in the AD context and our evaluation results show that the system-level effects can be significantly improved, i.e., the violation rate increases by around 70%.

</details>

### Learning Human Dynamics in Autonomous Driving Scenarios.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01901) · 📚 被引 23
- **作者**: Jingbo Wang, Ye Yuan, Zhengyi Luo, Kevin Xie, Dahua Lin, Umar Iqbal et al.
- **🏷️ 机构**: NVIDIA, The Chinese University of Hong Kong
- **会议**: ICCV 2023

### SemARFlow: Injecting Semantics into Unsupervised Optical Flow Estimation for Autonomous Driving.
- **链接**: [arXiv:2303.06209](https://arxiv.org/abs/2303.06209) · 📚 被引 8
- **作者**: Shuai Yuan, Shuzhi Yu, Hannah Kim, Carlo Tomasi
- **🏷️ 机构**: Duke University
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Unsupervised optical flow estimation is especially hard near occlusions and motion boundaries and in low-texture regions. We show that additional information such as semantics and domain knowledge can help better constrain this problem. We introduce SemARFlow, an unsupervised optical flow network designed for autonomous driving data that takes estimated semantic segmentation masks as additional inputs. This additional information is injected into the encoder and into a learned upsampler that refines the flow output. In addition, a simple yet effective semantic augmentation module provides self-supervision when learning flow and its boundaries for vehicles, poles, and sky. Together, these injections of semantic information improve the KITTI-2015 optical flow test error rate from 11.80% to 8.38%. We also show visible improvements around object boundaries as well as a greater ability to generalize across datasets. Code is available at https://github.com/duke-vision/semantic-unsup-flow-release.

</details>

### Exploring the Road Graph in Trajectory Forecasting for Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00014) · 📚 被引 6
- **作者**: Rémy Sun, Diane Lingrand, Frédéric Precioso
- **🏷️ 机构**: Universit&#x00E9; C&#x00F4;te d&#x2019;Azur,Inria, CNRS, I3S,Maasai,Nice,France
- **会议**: ICCV 2023

### Sensitivity analysis of AI-based algorithms for autonomous driving on optical wavefront aberrations induced by the windshield.
- **链接**: [arXiv:2308.11711](https://arxiv.org/abs/2308.11711) · 📚 被引 1
- **作者**: Dominik Werner Wolf, Markus Ulrich, Nikhil Kapoor
- **🏷️ 机构**: Volkswagen Group, Karlsruhe Institute of Technology, CARIAD SE
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Autonomous driving perception techniques are typically based on supervised machine learning models that are trained on real-world street data. A typical training process involves capturing images with a single car model and windshield configuration. However, deploying these trained models on different car types can lead to a domain shift, which can potentially hurt the neural networks performance and violate working ADAS requirements. To address this issue, this paper investigates the domain shift problem further by evaluating the sensitivity of two perception models to different windshield configurations. This is done by evaluating the dependencies between neural network benchmark metrics and optical merit functions by applying a Fourier optics based threat model. Our results show that there is a performance gap introduced by windshields and existing optical metrics used for posing requirements might not be sufficient.

</details>

### Hidden Biases of End-to-End Driving Models.
- **链接**: [arXiv:2306.07957](https://arxiv.org/abs/2306.07957) · 📚 被引 72
- **作者**: Bernhard Jaeger, Kashyap Chitta, Andreas Geiger
- **🏷️ 机构**: University of T&#x00FC;bingen,T&#x00FC;bingen AI Center
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> End-to-end driving systems have recently made rapid progress, in particular on CARLA. Independent of their major contribution, they introduce changes to minor system components. Consequently, the source of improvements is unclear. We identify two biases that recur in nearly all state-of-the-art methods and are critical for the observed progress on CARLA: (1) lateral recovery via a strong inductive bias towards target point following, and (2) longitudinal averaging of multimodal waypoint predictions for slowing down. We investigate the drawbacks of these biases and identify principled alternatives. By incorporating our insights, we develop TF++, a simple end-to-end method that ranks first on the Longest6 and LAV benchmarks, gaining 11 driving score over the best prior work on Longest6.

</details>

### Unsupervised Self-Driving Attention Prediction via Uncertainty Mining and Knowledge Embedding.
- **链接**: [arXiv:2303.09706](https://arxiv.org/abs/2303.09706) · 📚 被引 14
- **作者**: Pengfei Zhu, Mengshi Qi, Xia Li, Weijian Li, Huadong Ma
- **🏷️ 机构**: Beijing University of Posts and Telecommunications,Beijing Key Laboratory of Intelligent Telecommunications Software and Multimedia,Beijing,100876, University of Rochester,Department of Computer Science
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Predicting attention regions of interest is an important yet challenging task for self-driving systems. Existing methodologies rely on large-scale labeled traffic datasets that are labor-intensive to obtain. Besides, the huge domain gap between natural scenes and traffic scenes in current datasets also limits the potential for model training. To address these challenges, we are the first to introduce an unsupervised way to predict self-driving attention by uncertainty modeling and driving knowledge integration. Our approach's Uncertainty Mining Branch (UMB) discovers commonalities and differences from multiple generated pseudo-labels achieved from models pre-trained on natural scenes by actively measuring the uncertainty. Meanwhile, our Knowledge Embedding Block (KEB) bridges the domain gap by incorporating driving knowledge to adaptively refine the generated pseudo-labels. Quantitative and qualitative results with equivalent or even more impressive performance compared to fully-supervised state-of-the-art approaches across all three public datasets demonstrate the effectiveness of the proposed method and the potential of this direction. The code will be made publicly available.

</details>

### Unsupervised Domain Adaptation for Self-Driving from Past Traversal Features.
- **链接**: [arXiv:2309.12140](https://arxiv.org/abs/2309.12140) · 📚 被引 2
- **作者**: Travis Zhang, Katie Luo, Cheng Perng Phoo, Yurong You, Wei-Lun Chao, Bharath Hariharan et al.
- **🏷️ 机构**: Cornell University, The Ohio State University
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The rapid development of 3D object detection systems for self-driving cars has significantly improved accuracy. However, these systems struggle to generalize across diverse driving environments, which can lead to safety-critical failures in detecting traffic participants. To address this, we propose a method that utilizes unlabeled repeated traversals of multiple locations to adapt object detectors to new driving environments. By incorporating statistics computed from repeated LiDAR scans, we guide the adaptation process effectively. Our approach enhances LiDAR-based detection models using spatial quantized historical features and introduces a lightweight regression head to leverage the statistics for feature regularization. Additionally, we leverage the statistics for a novel self-training process to stabilize the training. The framework is detector model-agnostic and experiments on real-world datasets demonstrate significant improvements, achieving up to a 20-point performance gain, especially in detecting pedestrians and distant objects. Code is available at https://github.com/zhangtravis/Hist-DA.

</details>

### Policy Pre-training for Autonomous Driving via Self-supervised Geometric Modeling.
- **链接**: [出版页](https://openreview.net/forum?id=X5SUR7g2vVw)
- **作者**: Penghao Wu, Li Chen, Hongyang Li, Xiaosong Jia, Junchi Yan, Yu Qiao
- **🏷️ 机构**: Shanghai AI Lab
- **会议**: ICLR 2023

### Transcendental Idealism of Planner: Evaluating Perception from Planning Perspective for Autonomous Driving.
- **链接**: [出版页](https://proceedings.mlr.press/v202/li23al.html)
- **作者**: Weixin Li, Xiaodong Yang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Waymax: An Accelerated, Data-Driven Simulator for Large-Scale Autonomous Driving Research.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/1838feeb71c4b4ea524d0df2f7074245-Abstract-Datasets_and_Benchmarks.html)
- **作者**: Cole Gulino, Justin Fu, Wenjie Luo, George Tucker, Eli Bronstein, Yiren Lu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### What Truly Matters in Trajectory Prediction for Autonomous Driving?
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/e197fe307eb3467035f892dc100d570a-Abstract-Conference.html)
- **作者**: Tran Phong, Haoran Wu, Cunjun Yu, Panpan Cai, Sifa Zheng, David Hsu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Online Map Vectorization for Autonomous Driving: A Rasterization Perspective.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/654f61ecd998c9095d30d42c03b832aa-Abstract-Conference.html)
- **作者**: Gongjie Zhang, Jiahao Lin, Shuang Wu, Yilin Song, Zhipeng Luo, Yang Xue et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Scenario Diffusion: Controllable Driving Scenario Generation With Diffusion.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/d95cb79a3421e6d9b6c9a9008c4d07c5-Abstract-Conference.html)
- **作者**: Ethan Pronovost, Meghana Reddy Ganesina, Noureldin Hendy, Zeyu Wang, Andres Morales, Kai Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

## 跨领域论文（完整笔记在其他领域）

- ConQueR: Query Contrast Voxel-DETR for 3D Object Detection. → [object-detection](../object-detection/Guideline%202023.md)
- BEVFormer v2: Adapting Modern Image Backbones to Bird's-Eye-View Recognition via Perspective Supervision. → [bev](../bev/Guideline%202023.md)
- Are We Ready for Vision-Centric Driving Streaming Perception? The ASAP Benchmark. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- Surround-View Vision-based 3D Detection for Autonomous Driving: A Survey. → [bev](../bev/Guideline%202023.md)
- Occ3D: A Large-Scale 3D Occupancy Prediction Benchmark for Autonomous Driving. → [occupancy](../occupancy/Guideline%202023.md)
- 3D Video Object Detection with Learnable Object-Centric Global Optimization. → [object-detection](../object-detection/Guideline%202023.md)
- Viewpoint Equivariance for Multi-View 3D Object Detection. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- Bi-LRFusion: Bi-Directional LiDAR-Radar Fusion for 3D Dynamic Object Detection. → [object-detection](../object-detection/Guideline%202023.md)
- Normalizing Flow based Feature Synthesis for Outlier-Aware Object Detection. → [object-detection](../object-detection/Guideline%202023.md)
- BEV-SAN: Accurate BEV 3D Object Detection via Slice Attention Networks. → [object-detection](../object-detection/Guideline%202023.md)
- itKD: Interchange Transfer-based Knowledge Distillation for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- AeDet: Azimuth-Invariant Multi-View 3D Object Detection. → [object-detection](../object-detection/Guideline%202023.md)
- MSF: Motion-guided Sequential Fusion for Efficient 3D Object Detection from Point Cloud Sequences. → [3d-detection](../3d-detection/Guideline%202023.md)
- MSMDFusion: Fusing LiDAR and Camera at Multiple Scales with Multi-Depth Seeds for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- PillarNeXt: Rethinking Network Designs for 3D Object Detection in LiDAR Point Clouds. → [3d-detection](../3d-detection/Guideline%202023.md)
- MoDAR: Using Motion Forecasting for 3D Object Detection in Point Cloud Sequences. → [3d-detection](../3d-detection/Guideline%202023.md)
- Towards Domain Generalization for Multi-view 3D Object Detection in Bird-Eye-View. → [object-detection](../object-detection/Guideline%202023.md)
- CAPE: Camera View Position Embedding for Multi-View 3D Object Detection. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- BEVHeight: A Robust Framework for Vision-based Roadside 3D Object Detection. → [object-detection](../object-detection/Guideline%202023.md)
- Uni3D: A Unified Baseline for Multi-Dataset 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Towards Unsupervised Object Detection from LiDAR Point Clouds. → [object-detection](../object-detection/Guideline%202023.md)
- UniDistill: A Universal Cross-Modality Knowledge Distillation Framework for 3D Object Detection in Bird's-Eye View. → [bev](../bev/Guideline%202023.md)
- Understanding the Robustness of 3D Object Detection with Bird'View Representations in Autonomous Driving. → [3d-detection](../3d-detection/Guideline%202023.md)
- DeepMapping2: Self-Supervised Large-Scale LiDAR Map Optimization. → [self-supervised-vision](../self-supervised-vision/Guideline%202023.md)
- Collaboration Helps Camera Overtake LiDAR in 3D Detection. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- GeoMAE: Masked Geometric Target Prediction for Self-supervised Point Cloud Pre-Training. → [self-supervised-vision](../self-supervised-vision/Guideline%202023.md)
- TBP-Former: Learning Temporal Bird's-Eye-View Pyramid for Joint Perception and Prediction in Vision-Centric Autonomous Driving. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- Learning to Fuse Monocular and Multi-view Cues for Multi-frame Depth Estimation in Dynamic Scenes. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- Standing Between Past and Future: Spatio-Temporal Modeling for Multi-Camera 3D Multi-Object Tracking. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- iDisc: Internal Discretization for Monocular Depth Estimation. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- OVTrack: Open-Vocabulary Multiple Object Tracking. → [open-set-detection](../open-set-detection/Guideline%202023.md)
- RangeViT: Towards Vision Transformers for 3D Semantic Segmentation in Autonomous Driving. → [vision-transformer](../vision-transformer/Guideline%202023.md)
- MSeg3D: Multi-Modal 3D Semantic Segmentation for Autonomous Driving. → [multimodal](../multimodal/Guideline%202023.md)
- Visual Exemplar Driven Task-Prompting for Unified Perception in Autonomous Driving. → [fod-detection](../fod-detection/Guideline%202023.md)
- Implicit Occupancy Flow Fields for Perception and Prediction in Self-Driving. → [object-detection](../object-detection/Guideline%202023.md)
- Self-Supervised Image-to-Point Distillation via Semantically Tolerant Contrastive Loss. → [self-supervised-vision](../self-supervised-vision/Guideline%202023.md)
- Objects do not disappear: Video object detection by single-frame object location anticipation. → [object-detection](../object-detection/Guideline%202023.md)
- Exploring Object-Centric Temporal Modeling for Efficient Multi-View 3D Object Detection. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- Efficient Transformer-based 3D Object Detection with Dynamic Token Halting. → [3d-detection](../3d-detection/Guideline%202023.md)
- DistillBEV: Boosting Multi-Camera 3D Object Detection with Cross-Modal Knowledge Distillation. → [multimodal](../multimodal/Guideline%202023.md)
- Revisiting Domain-Adaptive 3D Object Detection by Reliable, Diverse and Class-balanced Pseudo-Labeling. → [3d-detection](../3d-detection/Guideline%202023.md)
- FocalFormer3D : Focusing on Hard Instance for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- GPA-3D: Geometry-aware Prototype Alignment for Unsupervised Domain Adaptive 3D Object Detection from Point Clouds. → [bev](../bev/Guideline%202023.md)
- Representation Disparity-aware Distillation for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- SparseBEV: High-Performance Sparse 3D Object Detection from Multi-Camera Videos. → [bev](../bev/Guideline%202023.md)
- Kecor: Kernel Coding Rate Maximization for Active 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Towards Fair and Comprehensive Comparisons for Image-Based 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- DetZero: Rethinking Offboard 3D Object Detection with Long-term Sequential Point Clouds. → [3d-detection](../3d-detection/Guideline%202023.md)
- PARTNER: Level up the Polar Representation for LiDAR 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- GraphAlign: Enhancing Accurate Feature Alignment by Graph matching for Multi-Modal 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- SparseFusion: Fusing Multi-Modal Sparse Representations for Multi-Sensor 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- MonoNeRD: NeRF-like Representations for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- QD-BEV : Quantization-aware View-guided Distillation for Multi-view 3D Object Detection. → [network-pruning](../network-pruning/Guideline%202023.md)
- SA-BEV: Generating Semantic-Aware Bird's-Eye-View Feature for Multi-view 3D Object Detection. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- Ada3D : Exploiting the Spatial Redundancy with Adaptive Inference for Efficient 3D Object Detection. → [bev](../bev/Guideline%202023.md)
- On Offline Evaluation of 3D Object Detection for Autonomous Driving. → [3d-detection](../3d-detection/Guideline%202023.md)
- SVQNet: Sparse Voxel-Adjacent Query Network for 4D Spatio-Temporal LiDAR Semantic Segmentation. → [3d-detection](../3d-detection/Guideline%202023.md)
- UniSeg: A Unified Multi-Modal LiDAR Segmentation Network and the OpenPCSeg Codebase. → [multimodal](../multimodal/Guideline%202023.md)
- See More and Know More: Zero-shot Point Cloud Segmentation via Multi-modal Visual Data. → [multimodal](../multimodal/Guideline%202023.md)
- MBPTrack: Improving 3D Point Cloud Tracking with Memory networks and Box Priors. → [tracking](../tracking/Guideline%202023.md)
- MapPrior: Bird's-Eye View Map Layout Estimation with Generative Models. → [bev](../bev/Guideline%202023.md)
- MatrixVT: Efficient Multi-Camera to BEV Transformation for 3D Perception. → [network-pruning](../network-pruning/Guideline%202023.md)
- SurroundOcc: Multi-Camera 3D Occupancy Prediction for Autonomous Driving. → [occupancy](../occupancy/Guideline%202023.md)
- OccFormer: Dual-path Transformer for Vision-based 3D Semantic Occupancy Prediction. → [network-pruning](../network-pruning/Guideline%202023.md)
- Self-supervised Monocular Depth Estimation: Let's Talk About The Weather. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
<!-- COMPLETE v1 papers=42 -->
