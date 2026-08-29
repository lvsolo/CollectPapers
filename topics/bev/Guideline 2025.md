# BEV — 2025 Guideline

> 领域: 鸟瞰图感知（BEV 特征、BEV 检测/分割/预测）
> 论文数: 5 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### ForestLPR: LiDAR Place Recognition in Forests Attentioning Multiple BEV Density Images.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Shen_ForestLPR_LiDAR_Place_Recognition_in_Forests_Attentioning_Multiple_BEV_Density_CVPR_2025_paper.html) · 📚 被引 6
- **作者**: Yanqing Shen, Turcan Tuna, Marco Hutter, César Cadena, Nanning Zheng
- **🏷️ 机构**: Xi&#x2019;an Jiaotong University,Institute of Artificial Intelligence and Robotics, ETH Zurich,Robotic Systems Lab
- **会议**: CVPR 2025

### SDGOCC: Semantic and Depth-Guided Bird's-Eye View Transformation for 3D Multimodal Occupancy Prediction.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Duan_SDGOCC_Semantic_and_Depth-Guided_Birds-Eye_View_Transformation_for_3D_Multimodal_CVPR_2025_paper.html)
- **作者**: Zaipeng Duan, Chenxu Dang, Xuzhong Hu, Pei An, Junfeng Ding, Jie Zhan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

## 跨领域论文（完整笔记在其他领域）

- RobuRCDet: Enhancing Robustness of Radar-Camera Fusion in Bird's Eye View for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202025.md)

## 🆕 增量新增

### Predictive Uncertainty Quantification for Bird's Eye View Segmentation: A Benchmark and Novel Loss Function. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [出版页](https://openreview.net/forum?id=k3y0oyK7sn)
- **作者**: Linlin Yu, Bowen Yang, Tianhao Wang, Kangshuo Li, Feng Chen
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025
- **摘要（中）**: ①针对BEV分割中预测不确定性量化缺乏基准和有效损失函数的问题。②构建了首个BEV分割不确定性量化基准，并提出一种新的损失函数来改进不确定性估计。③相比现有方法，该损失函数能更好地捕捉BEV空间中的空间相关性和类别不确定性。④在基准上验证了方法的有效性，提升了不确定性估计的准确性和校准度。
- **摘要（英）**: This paper addresses the lack of benchmarks and effective loss functions for predictive uncertainty quantification in BEV segmentation. It introduces the first benchmark for this task and proposes a novel loss function to improve uncertainty estimation. The method captures spatial correlations and class-wise uncertainty better than existing approaches, demonstrating improved accuracy and calibration on the benchmark.
- **核心贡献**: 构建了BEV分割不确定性量化基准并提出新损失函数。
- **创新点**: 首次系统性地研究BEV分割中的不确定性量化。
- **结果**: 在基准上提升了不确定性估计的准确性和校准度。

### BEVDiffuser: Plug-and-Play Diffusion Model for BEV Denoising with Ground-Truth Guidance. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Ye_BEVDiffuser_Plug-and-Play_Diffusion_Model_for_BEV_Denoising_with_Ground-Truth_Guidance_CVPR_2025_paper.html) · 📚 被引 6
- **作者**: Xin Ye, Burhaneddin Yaman, Sheng Cheng, Feng Tao, Abhirup Mallik, Liu Ren
- **🏷️ 机构**: Bosch Research North America &amp; Bosch Center for Artificial Intelligence (BCAI)
- **会议**: CVPR 2025
- **摘要（中）**: ①针对BEV感知中噪声和不确定性影响下游任务性能的问题。②提出BEVDiffuser，一种即插即用的扩散模型，用于BEV去噪，并利用真实标注作为引导。③相比现有去噪方法，该方法结合扩散模型的生成能力和真实标注引导，能更有效地恢复干净的BEV表示。④在多个BEV感知任务上验证了去噪效果，提升了感知精度。
- **摘要（英）**: This paper addresses noise and uncertainty in BEV perception that degrade downstream task performance. BEVDiffuser is proposed as a plug-and-play diffusion model for BEV denoising, guided by ground-truth annotations. It combines generative capabilities with GT guidance to recover clean BEV representations more effectively than existing methods, improving perception accuracy across tasks.
- **核心贡献**: 提出即插即用的BEV去噪扩散模型BEVDiffuser。
- **创新点**: 利用扩散模型和真实标注引导进行BEV去噪。
- **结果**: 在多个BEV感知任务上提升了感知精度。

### Generative Map Priors for Collaborative BEV Semantic Segmentation. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Fu_Generative_Map_Priors_for_Collaborative_BEV_Semantic_Segmentation_CVPR_2025_paper.html) · 📚 被引 4
- **作者**: Jiahui Fu, Yue Gong, Luting Wang, Shifeng Zhang, Xu Zhou, Si Liu
- **🏷️ 机构**: Beihang University,Institute of Artificial Intelligence, Sangfor Technologies Inc.
- **会议**: CVPR 2025
- **摘要（中）**: ①针对协同BEV语义分割中地图先验信息利用不足的问题。②提出利用生成式地图先验来增强协同BEV语义分割，通过生成模型提供结构化先验。③相比现有协同感知方法，该方法将地图先验融入分割过程，提升了复杂场景下的分割一致性。④在协同感知数据集上验证了性能提升。
- **摘要（英）**: This paper addresses the underutilization of map priors in collaborative BEV semantic segmentation. It proposes generative map priors to enhance segmentation by providing structured priors from generative models. Compared to existing collaborative perception methods, it integrates map priors into the segmentation process, improving consistency in complex scenes and demonstrating performance gains on collaborative datasets.
- **核心贡献**: 提出生成式地图先验用于协同BEV语义分割。
- **创新点**: 将生成式地图先验融入协同分割框架。
- **结果**: 在协同感知数据集上验证了性能提升。

### Toward Real-world BEV Perception: Depth Uncertainty Estimation via Gaussian Splatting. **⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2504.01957](https://arxiv.org/abs/2504.01957) · 📚 被引 8
- **作者**: Shu-Wei Lu, Yi-Hsuan Tsai, Yi-Ting Chen
- **🏷️ 机构**: National Yang Ming Chiao Tung University, Atmanity Inc.
- **会议**: CVPR 2025
- **摘要（中）**: 针对BEV感知中缺乏不确定性建模和高计算成本的问题，提出GaussianLSS框架，重新审视LSS范式，通过学习软深度均值和方差来建模深度不确定性，并转换为3D高斯进行光栅化，构建不确定性感知的BEV特征。在nuScenes上取得最先进性能，同时降低计算需求。
- **摘要（英）**: To address the lack of uncertainty modeling and high computational cost in BEV perception, GaussianLSS revisits the LSS paradigm, learns soft depth mean and variance to model depth uncertainty, and rasterizes 3D Gaussians for uncertainty-aware BEV features. It achieves state-of-the-art performance on nuScenes with reduced computation.
- **核心贡献**: 提出基于高斯溅射的不确定性感知BEV感知框架。
- **创新点**: 利用深度分布方差隐式捕捉物体范围，构建不确定性BEV特征。
- **结果**: 在nuScenes上取得最先进性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Bird's-eye view (BEV) perception has gained significant attention because it provides a unified representation to fuse multiple view images and enables a wide range of down-stream autonomous driving tasks, such as forecasting and planning. Recent state-of-the-art models utilize projection-based methods which formulate BEV perception as query learning to bypass explicit depth estimation. While we observe promising advancements in this paradigm, they still fall short of real-world applications because of the lack of uncertainty modeling and expensive computational requirement. In this work, we introduce GaussianLSS, a novel uncertainty-aware BEV perception framework that revisits unprojection-based methods, specifically the Lift-Splat-Shoot (LSS) paradigm, and enhances them with depth un-certainty modeling. GaussianLSS represents spatial dispersion by learning a soft depth mean and computing the variance of the depth distribution, which implicitly captures object extents. We then transform the depth distribution into 3D Gaussians and rasterize them to construct uncertainty-aware BEV features. We evaluate GaussianLSS on the nuScenes dataset, achieving state-of-the-art performance compared to unprojection-based methods. In particular, it provides significant advantages in speed, running 2.5x faster, and in memory efficiency, using 0.3x less memory compared to projection-based methods, while achieving competitive performance with only a 0.4% IoU difference.

</details>

### Bridging Past and Future: End-to-End Autonomous Driving with Historical Prediction and Planning. **⭐⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2503.14182](https://arxiv.org/abs/2503.14182) · 📚 被引 7
- **作者**: Bozhou Zhang, Nan Song, Xin Jin, Li Zhang
- **🏷️ 机构**: Fudan University,School of Data Science, Eastern Institute of Technology
- **会议**: CVPR 2025
- **摘要（中）**: ①针对端到端自动驾驶中历史信息利用不足和与多步规划不匹配的问题。②提出BridgeAD，将运动和规划查询重构为多步查询，区分每个未来时间步，并分别用于感知和运动规划，实现历史预测与规划的桥接。③相比现有方法，该方法更符合规划的多步特性，提升了感知和规划性能。④在端到端自动驾驶基准上验证了有效性，取得了显著改进。
- **摘要（英）**: This paper addresses insufficient historical information utilization and misalignment with multi-step planning in end-to-end autonomous driving. BridgeAD reformulates motion and planning queries as multi-step queries, applying historical queries to perception and future queries to planning, bridging past and future. It improves both perception and planning, demonstrating significant gains on end-to-end driving benchmarks.
- **核心贡献**: 提出BridgeAD，通过多步查询桥接历史预测与规划。
- **创新点**: 将查询重构为多步以匹配规划特性。
- **结果**: 在端到端自动驾驶基准上取得显著改进。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> End-to-end autonomous driving unifies tasks in a differentiable framework, enabling planning-oriented optimization and attracting growing attention. Current methods aggregate historical information either through dense historical bird's-eye-view (BEV) features or by querying a sparse memory bank, following paradigms inherited from detection. However, we argue that these paradigms either omit historical information in motion planning or fail to align with its multi-step nature, which requires predicting or planning multiple future time steps. In line with the philosophy of future is a continuation of past, we propose BridgeAD, which reformulates motion and planning queries as multi-step queries to differentiate the queries for each future time step. This design enables the effective use of historical prediction and planning by applying them to the appropriate parts of the end-to-end system based on the time steps, which improves both perception and motion planning. Specifically, historical queries for the current frame are combined with perception, while queries for future frames are integrated with motion planning. In this way, we bridge the gap between past and future by aggregating historical insights at every time step, enhancing the overall coherence and accuracy of the end-to-end autonomous driving pipeline. Extensive experiments on the nuScenes dataset in both open-loop and closed-loop settings demonstrate that BridgeAD achieves state-of-the-art performance.

</details>

### RobuRCDet: Enhancing Robustness of Radar-Camera Fusion in Bird's Eye View for 3D Object Detection. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2502.13071](https://arxiv.org/abs/2502.13071)
- **作者**: Jingtong Yue, Zhiwei Lin, Xin Lin, Xiaoyu Zhou, Xiangtai Li, Lu Qi et al.
- **🏷️ 机构**: UC Merced
- **会议**: ICLR 2025
- **摘要（中）**: 针对雷达-相机融合3D检测在恶劣环境和传感器噪声下的鲁棒性问题，首次系统分析五种噪声的影响，提出RobuRCDet模型。设计3D高斯扩展模块，利用RCS和速度先验生成可变形核图，缓解雷达点位置、RCS和速度的不确定性；引入天气自适应融合模块，根据相机信号置信度自适应融合雷达和相机特征。在nuScenes基准上，该方法在多种噪声条件下取得竞争性结果，显著提升鲁棒性。
- **摘要（英）**: This paper addresses robustness in radar-camera 3D detection by systematically analyzing five noise types and proposing RobuRCDet with a 3D Gaussian Expansion module and weather-adaptive fusion. It achieves competitive performance on nuScenes under various disturbances.
- **核心贡献**: 提出鲁棒的雷达-相机BEV融合检测框架，增强抗噪能力。
- **创新点**: 利用3D高斯扩展和天气自适应融合处理传感器噪声。
- **结果**: 在nuScenes上多种噪声下保持高检测性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While recent low-cost radar-camera approaches have shown promising results in multi-modal 3D object detection, both sensors face challenges from environmental and intrinsic disturbances. Poor lighting or adverse weather conditions degrade camera performance, while radar suffers from noise and positional ambiguity. Achieving robust radar-camera 3D object detection requires consistent performance across varying conditions, a topic that has not yet been fully explored. In this work, we first conduct a systematic analysis of robustness in radar-camera detection on five kinds of noises and propose RobuRCDet, a robust object detection model in BEV. Specifically, we design a 3D Gaussian Expansion (3DGE) module to mitigate inaccuracies in radar points, including position, Radar Cross-Section (RCS), and velocity. The 3DGE uses RCS and velocity priors to generate a deformable kernel map and variance for kernel size adjustment and value distribution. Additionally, we introduce a weather-adaptive fusion module, which adaptively fuses radar and camera features based on camera signal confidence. Extensive experiments on the popular benchmark, nuScenes, show that our model achieves competitive results in regular and noisy conditions.

</details>

### DriveTransformer: Unified Transformer for Scalable End-to-End Autonomous Driving. **⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2503.07656](https://arxiv.org/abs/2503.07656)
- **作者**: Xiaosong Jia, Junqi You, Zhiyuan Zhang, Junchi Yan
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025
- **摘要（中）**: 针对端到端自动驾驶中顺序感知-预测-规划范式导致的累积误差和训练不稳定问题，提出DriveTransformer框架，采用任务并行、稀疏表示和流式处理三大特性。所有智能体、地图和规划查询在每个块中直接交互，任务查询直接与原始传感器特征交互，并存储历史信息。相比现有方法，该框架简化了系统设计，易于扩展，并利用任务间协同作用。实验表明在规划性能上优于基线，且计算效率更高。
- **摘要（英）**: DriveTransformer addresses cumulative errors in sequential E2E-AD by introducing task parallelism, sparse representation, and streaming processing, enabling direct interactions among queries and raw features. It improves planning performance and scalability over baselines.
- **核心贡献**: 提出统一Transformer框架，实现并行化、稀疏化的端到端自动驾驶。
- **创新点**: 采用任务查询并行交互和流式历史信息处理。
- **结果**: 在规划任务上取得更优性能和效率。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> End-to-end autonomous driving (E2E-AD) has emerged as a trend in the field of autonomous driving, promising a data-driven, scalable approach to system design. However, existing E2E-AD methods usually adopt the sequential paradigm of perception-prediction-planning, which leads to cumulative errors and training instability. The manual ordering of tasks also limits the system`s ability to leverage synergies between tasks (for example, planning-aware perception and game-theoretic interactive prediction and planning). Moreover, the dense BEV representation adopted by existing methods brings computational challenges for long-range perception and long-term temporal fusion. To address these challenges, we present DriveTransformer, a simplified E2E-AD framework for the ease of scaling up, characterized by three key features: Task Parallelism (All agent, map, and planning queries direct interact with each other at each block), Sparse Representation (Task queries direct interact with raw sensor features), and Streaming Processing (Task queries are stored and passed as history information). As a result, the new framework is composed of three unified operations: task self-attention, sensor cross-attention, temporal cross-attention, which significantly reduces the complexity of system and leads to better training stability. DriveTransformer achieves state-of-the-art performance in both simulated closed-loop benchmark Bench2Drive and real world open-loop benchmark nuScenes with high FPS.

</details>

### DrivingRecon: Large 4D Gaussian Reconstruction Model For Autonomous Driving. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2412.09043](https://arxiv.org/abs/2412.09043)
- **作者**: Hao Lu, Tianshuo Xu, Wenzhao Zheng, Yunpeng Zhang, Wei Zhan, Dalong Du et al.
- **🏷️ 机构**: Hong Kong University of Science and Technology, University of California, Berkeley, Tsinghua University
- **会议**: NeurIPS 2025
- **摘要（中）**: 针对自动驾驶街景4D重建依赖离线迭代、效率低的问题，提出DrivingRecon，一个可泛化的4D高斯重建模型，直接从环视视频预测4D高斯。设计剪枝和扩张块消除相邻视图重叠和冗余背景点，并采用动态静态解耦增强几何和运动学习。相比现有方法，DrivingRecon显著提升重建质量和新视角合成，并支持预训练、车辆适配和场景编辑等应用。
- **摘要（英）**: DrivingRecon proposes a generalizable 4D Gaussian reconstruction model for driving scenes, directly predicting from surround videos with prune-dilate blocks and dynamic-static decoupling. It improves reconstruction quality and enables downstream applications.
- **核心贡献**: 提出首个可泛化的大规模4D高斯重建模型。
- **创新点**: 利用剪枝扩张和动态静态解耦优化重建。
- **结果**: 在重建质量和应用效果上优于现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Photorealistic 4D reconstruction of street scenes is essential for developing real-world simulators in autonomous driving. However, most existing methods perform this task offline and rely on time-consuming iterative processes, limiting their practical applications. To this end, we introduce the Large 4D Gaussian Reconstruction Model (DrivingRecon), a generalizable driving scene reconstruction model, which directly predicts 4D Gaussian from surround view videos. To better integrate the surround-view images, the Prune and Dilate Block (PD-Block) is proposed to eliminate overlapping Gaussian points between adjacent views and remove redundant background points. To enhance cross-temporal information, dynamic and static decoupling is tailored to better learn geometry and motion features. Experimental results demonstrate that DrivingRecon significantly improves scene reconstruction quality and novel view synthesis compared to existing methods. Furthermore, we explore applications of DrivingRecon in model pre-training, vehicle adaptation, and scene editing. Our code is available at https://github.com/EnVision-Research/DriveRecon.

</details>

### GaussianFusion: Gaussian-Based Multi-Sensor Fusion for End-to-End Autonomous Driving. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2506.00034](https://arxiv.org/abs/2506.00034) · 📚 被引 1
- **作者**: Shuai Liu, Quanmin Liang, Zefeng Li, Boyang Li, Kai Huang
- **🏷️ 机构**: SUN YAT-SEN UNIVERSITY, Sun Yat-sen University, Nanyang Technological University
- **会议**: NeurIPS 2025
- **摘要（中）**: 针对端到端自动驾驶中多传感器融合可解释性差和计算开销大的问题，提出GaussianFusion框架，采用高斯表示作为中间载体聚合多模态信息。初始化均匀分布的2D高斯，参数化物理属性并配备显式和隐式特征，通过多模态特征逐步细化；显式特征捕获语义和空间信息，隐式特征辅助轨迹规划，并设计级联规划头迭代优化。相比注意力融合和BEV融合，该方法更直观且计算高效。实验在闭环仿真中取得优越性能。
- **摘要（英）**: GaussianFusion introduces a Gaussian-based multi-sensor fusion framework for E2E-AD, using compact 2D Gaussians as interpretable carriers to aggregate features and refine planning. It outperforms attention and BEV fusion methods in closed-loop simulations.
- **核心贡献**: 提出基于高斯的可解释多传感器融合框架。
- **创新点**: 利用物理属性参数化的高斯作为中间表示。
- **结果**: 在闭环仿真中取得优越规划性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-sensor fusion is crucial for improving the performance and robustness of end-to-end autonomous driving systems. Existing methods predominantly adopt either attention-based flatten fusion or bird's eye view fusion through geometric transformations. However, these approaches often suffer from limited interpretability or dense computational overhead. In this paper, we introduce GaussianFusion, a Gaussian-based multi-sensor fusion framework for end-to-end autonomous driving. Our method employs intuitive and compact Gaussian representations as intermediate carriers to aggregate information from diverse sensors. Specifically, we initialize a set of 2D Gaussians uniformly across the driving scene, where each Gaussian is parameterized by physical attributes and equipped with explicit and implicit features. These Gaussians are progressively refined by integrating multi-modal features. The explicit features capture rich semantic and spatial information about the traffic scene, while the implicit features provide complementary cues beneficial for trajectory planning. To fully exploit rich spatial and semantic information in Gaussians, we design a cascade planning head that iteratively refines trajectory predictions through interactions with Gaussians. Extensive experiments on the NAVSIM and Bench2Drive benchmarks demonstrate the effectiveness and robustness of the proposed GaussianFusion framework. The source code will be released at https://github.com/Say2L/GaussianFusion.

</details>

### AffordBot: 3D Fine-grained Embodied Reasoning via Multimodal Large Language Models.
- **链接**: [arXiv:2511.10017](https://arxiv.org/abs/2511.10017)
- **作者**: Xinyi Wang, Xun Yang, Yanlong Xu, Yuchen Wu, Zhen Li, Na Zhao
- **🏷️ 机构**: University of Science and Technology of China, University of Washington, Shanghai Artificial Intelligence Laboratory
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Effective human-agent collaboration in physical environments requires understanding not only what to act upon, but also where the actionable elements are and how to interact with them. Existing approaches often operate at the object level or disjointedly handle fine-grained affordance reasoning, lacking coherent, instruction-driven grounding and reasoning. In this work, we introduce a new task: Fine-grained 3D Embodied Reasoning, which requires an agent to predict, for each referenced affordance element in a 3D scene, a structured triplet comprising its spatial location, motion type, and motion axis, based on a task instruction. To solve this task, we propose AffordBot, a novel framework that integrates Multimodal Large Language Models (MLLMs) with a tailored chain-of-thought (CoT) reasoning paradigm. To bridge the gap between 3D input and 2D-compatible MLLMs, we render surround-view images of the scene and project 3D element candidates into these views, forming a rich visual representation aligned with the scene geometry. Our CoT pipeline begins with an active perception stage, prompting the MLLM to select the most informative viewpoint based on the instruction, before proceeding with step-by-step reasoning to localize affordance elements and infer plausible interaction motions. Evaluated on the SceneFun3D dataset, AffordBot achieves state-of-the-art performance, demonstrating strong generalization and physically grounded reasoning with only 3D point cloud input and MLLMs.

</details>

## 跨领域论文（完整笔记在其他领域）

- RaCFormer: Towards High-Quality 3D Object Detection via Query-based Radar-Camera Fusion. → [object-detection](../object-detection/Guideline%202025.md)
- SparseAlign: a Fully Sparse Framework for Cooperative Object Detection. → [object-detection](../object-detection/Guideline%202025.md)
- Multi-Scale Neighborhood Occupancy Masked Autoencoder for Self-Supervised Learning in LiDAR Point Clouds. → [self-supervised-vision](../self-supervised-vision/Guideline%202025.md)
- SDGOCC: Semantic and Depth-Guided Bird's-Eye View Transformation for 3D Multimodal Occupancy Prediction. → [multimodal](../multimodal/Guideline%202025.md)
- MITracker: Multi-View Integration for Visual Object Tracking. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
- Multi-modal Knowledge Distillation-based Human Trajectory Forecasting. → [knowledge-distillation](../knowledge-distillation/Guideline%202025.md)
- OcRFDet: Object-Centric Radiance Fields for Multi-View 3D Object Detection in Autonomous Driving. → [object-detection](../object-detection/Guideline%202025.md)
- RCTDistill: Cross-Modal Knowledge Distillation Framework for Radar-Camera 3D Object Detection with Temporal Fusion. → [object-detection](../object-detection/Guideline%202025.md)
- EVT: Efficient View Transformation for Multi-Modal 3D Object Detection. → [object-detection](../object-detection/Guideline%202025.md)
- MVTrajecter: Multi-View Pedestrian Tracking With Trajectory Motion Cost and Trajectory Appearance Cost. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
- Self-Supervised Sparse Sensor Fusion for Long Range Perception. → [self-supervised-vision](../self-supervised-vision/Guideline%202025.md)
- Hybrid-Grained Feature Aggregation with Coarse-to-Fine Language Guidance for Self-Supervised Monocular Depth Estimation. → [self-supervised-vision](../self-supervised-vision/Guideline%202025.md)
- See through the Dark: Learning Illumination-affined Representations for Nighttime Occupancy Prediction. → [occupancy](../occupancy/Guideline%202025.md)
- SQS: Enhancing Sparse Perception Models via Query-based Splatting in Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202025.md)
- Genesis: Multimodal Driving Scene Generation with Spatio-Temporal and Cross-Modal Consistency. → [video-understanding](../video-understanding/Guideline%202025.md)
<!-- COMPLETE v1 papers=12 -->
