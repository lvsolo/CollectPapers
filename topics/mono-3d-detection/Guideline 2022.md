# Mono 3D Detection — 2022 Guideline

> 领域: 单目 3D 检测（Monocular 3D Object Detection，含单目深度支撑的 3D 感知）
> 论文数: 32 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: [2026](Guideline%202026.md), [2025](Guideline%202025.md), [2024](Guideline%202024.md), [2023](Guideline%202023.md), [2021](Guideline%202021.md)

### Homography Loss for Monocular 3D Object Detection. **⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2204.00754](https://arxiv.org/abs/2204.00754) · 📚 被引 48
- **作者**: Jiaqi Gu, Bojian Wu, Lubin Fan, Jianqiang Huang, Shen Cao, Zhiyu Xiang et al.
- **🏷️ 机构**: Alibaba Cloud Computing Ltd., Zhejiang University
- **会议**: CVPR 2022
- **摘要（中）**: ①针对单目3D检测中，现有方法将每个物体独立训练，忽略物体间几何关系，缺乏空间约束的问题。②提出一种名为Homography Loss的可微损失函数，利用2D检测框作为全局约束，平衡不同物体间的位置关系，同时结合2D和3D信息优化预测的3D框。③相比已有方法，该损失函数设计简洁，可即插即用地集成到任何成熟的单目3D检测器中，无需修改网络结构。④实验表明，该方法显著提升了基线检测器的性能，具体数值未在摘要中给出。
- **摘要（英）**: This paper addresses the lack of spatial constraints in monocular 3D detection by proposing a Homography Loss that uses 2D boxes to globally constrain 3D box predictions. It is plug-and-play and boosts performance of existing detectors.
- **核心贡献**: 提出Homography Loss，利用2D-3D几何关系全局优化单目3D检测。
- **创新点**: 通过全局约束物体间位置关系，而非独立优化每个样本。
- **结果**: 在多个成熟检测器上显著提升性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular 3D object detection is an essential task in autonomous driving. However, most current methods consider each 3D object in the scene as an independent training sample, while ignoring their inherent geometric relations, thus inevitably resulting in a lack of leveraging spatial constraints. In this paper, we propose a novel method that takes all the objects into consideration and explores their mutual relationships to help better estimate the 3D boxes. Moreover, since 2D detection is more reliable currently, we also investigate how to use the detected 2D boxes as guidance to globally constrain the optimization of the corresponding predicted 3D boxes. To this end, a differentiable loss function, termed as Homography Loss, is proposed to achieve the goal, which exploits both 2D and 3D information, aiming at balancing the positional relationships between different objects by global constraints, so as to obtain more accurately predicted 3D boxes. Thanks to the concise design, our loss function is universal and can be plugged into any mature monocular 3D detector, while significantly boosting the performance over their baseline. Experiments demonstrate that our method yields the best performance (Nov. 2021) compared with the other state-of-the-arts by a large margin on KITTI 3D datasets.

</details>

### MonoDTR: Monocular 3D Object Detection with Depth-Aware Transformer. **⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2203.10981](https://arxiv.org/abs/2203.10981) · 📚 被引 225
- **作者**: Kuan-Chih Huang, Tsung-Han Wu, Hung-Ting Su, Winston H. Hsu
- **🏷️ 机构**: National Taiwan University
- **会议**: CVPR 2022
- **摘要（中）**: ①这篇论文针对单目3D目标检测中依赖外部深度估计器导致计算开销大且深度先验不准确的问题。②提出了MonoDTR，一个端到端的深度感知Transformer网络，包含深度感知特征增强（DFE）模块和深度感知Transformer（DTR）模块，并引入深度位置编码（DPE）。③改进点在于DFE通过辅助监督隐式学习深度特征，无需额外计算；DPE替代传统像素级位置编码，提供深度提示。④在KITTI数据集上，该方法优于先前最先进的单目方法，具体数据未在摘要中给出。
- **摘要（英）**: This paper addresses the issues of high computational cost and inaccurate depth priors in monocular 3D detection. It proposes MonoDTR, an end-to-end depth-aware transformer with a Depth-Aware Feature Enhancement module and a Depth-Aware Transformer module, plus novel depth positional encoding. The method outperforms prior state-of-the-art on KITTI, demonstrating effectiveness without extra computation.
- **核心贡献**: 提出深度感知Transformer网络，实现高效准确的单目3D检测。
- **创新点**: 引入深度位置编码和隐式深度特征学习，避免外部深度估计器。
- **结果**: 在KITTI上超越先前最先进方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular 3D object detection is an important yet challenging task in autonomous driving. Some existing methods leverage depth information from an off-the-shelf depth estimator to assist 3D detection, but suffer from the additional computational burden and achieve limited performance caused by inaccurate depth priors. To alleviate this, we propose MonoDTR, a novel end-to-end depth-aware transformer network for monocular 3D object detection. It mainly consists of two components: (1) the Depth-Aware Feature Enhancement (DFE) module that implicitly learns depth-aware features with auxiliary supervision without requiring extra computation, and (2) the Depth-Aware Transformer (DTR) module that globally integrates context- and depth-aware features. Moreover, different from conventional pixel-wise positional encodings, we introduce a novel depth positional encoding (DPE) to inject depth positional hints into transformers. Our proposed depth-aware modules can be easily plugged into existing image-only monocular 3D object detectors to improve the performance. Extensive experiments on the KITTI dataset demonstrate that our approach outperforms previous state-of-the-art monocular-based methods and achieves real-time detection. Code is available at https://github.com/kuanchihhuang/MonoDTR

</details>

### Time3D: End-to-End Joint Monocular 3D Object Detection and Tracking for Autonomous Driving. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2205.14882](https://arxiv.org/abs/2205.14882) · 📚 被引 58
- **作者**: Peixuan Li, Jieyu Jin
- **🏷️ 机构**: SAIC PP-CEM
- **会议**: CVPR 2022
- **摘要（中）**: ①这篇论文针对单目3D检测和2D跟踪分离导致误差无法传播的问题。②提出了Time3D，一种端到端联合训练单目3D检测和3D跟踪的框架，核心是空间-时间信息流模块，利用Transformer的自注意力聚合空间信息，交叉注意力关联时序帧中的对象。③改进点在于通过联合训练和时序一致性损失，使检测和跟踪相互优化。④摘要未提供具体数据，但方法在概念上具有创新性。
- **摘要（英）**: This paper addresses the disconnection between monocular 3D detection and tracking by proposing Time3D, an end-to-end framework for joint training. It uses a spatial-temporal information flow module with transformer attention to aggregate features and predict affinities. The approach enables error backpropagation between tasks, improving robustness.
- **核心贡献**: 提出端到端联合单目3D检测与跟踪框架。
- **创新点**: 利用Transformer注意力实现时空信息流和误差传播。
- **结果**: 摘要未提供具体性能数据。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While separately leveraging monocular 3D object detection and 2D multi-object tracking can be straightforwardly applied to sequence images in a frame-by-frame fashion, stand-alone tracker cuts off the transmission of the uncertainty from the 3D detector to tracking while cannot pass tracking error differentials back to the 3D detector. In this work, we propose jointly training 3D detection and 3D tracking from only monocular videos in an end-to-end manner. The key component is a novel spatial-temporal information flow module that aggregates geometric and appearance features to predict robust similarity scores across all objects in current and past frames. Specifically, we leverage the attention mechanism of the transformer, in which self-attention aggregates the spatial information in a specific frame, and cross-attention exploits relation and affinities of all objects in the temporal domain of sequence frames. The affinities are then supervised to estimate the trajectory and guide the flow of information between corresponding 3D objects. In addition, we propose a temporal -consistency loss that explicitly involves 3D target motion modeling into the learning, making the 3D trajectory smooth in the world coordinate system. Time3D achieves 21.4\% AMOTA, 13.6\% AMOTP on the nuScenes 3D tracking benchmark, surpassing all published competitors, and running at 38 FPS, while Time3D achieves 31.2\% mAP, 39.4\% NDS on the nuScenes 3D detection benchmark.

</details>

### Diversity Matters: Fully Exploiting Depth Clues for Reliable Monocular 3D Object Detection. **⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2205.09373](https://arxiv.org/abs/2205.09373) · 📚 被引 87
- **作者**: Zhuoling Li, Zhan Qu, Yang Zhou, Jianzhuang Liu, Haoqian Wang, Lihui Jiang
- **🏷️ 机构**: Tsinghua University, Huawei Noah&#x0027;s Ark Lab
- **会议**: CVPR 2022
- **摘要（中）**: ①这篇论文针对单目3D检测中深度线索利用不充分的问题。②提出了多样性增强方法，充分挖掘深度线索以提高检测可靠性。③改进点在于强调深度线索的多样性，可能通过多尺度或多种深度表示来增强特征。④摘要未提供具体数据，但题目暗示了性能提升。
- **摘要（英）**: This paper addresses the underutilization of depth clues in monocular 3D detection by proposing a diversity-based approach. It fully exploits various depth cues to improve detection reliability. The abstract lacks quantitative results but suggests performance gains.
- **核心贡献**: 提出利用多样性深度线索增强单目3D检测可靠性。
- **创新点**: 强调深度线索多样性以提升特征表达。
- **结果**: 摘要未提供具体数据。

### MonoJSG: Joint Semantic and Geometric Cost Volume for Monocular 3D Object Detection. **⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2203.08563](https://arxiv.org/abs/2203.08563) · 📚 被引 69
- **作者**: Qing Lian, Peiliang Li, Xiaozhi Chen
- **🏷️ 机构**: The Hong Kong University of Science and Technology, DJI
- **会议**: CVPR 2022
- **摘要（中）**: ①针对单目3D检测中缺乏深度信息导致定位不准的问题。②提出MonoJSG，构建联合语义和几何代价体，通过可微的代价体聚合和深度回归模块，同时估计语义类别和几何深度。③相比仅依赖语义或几何的方法，联合建模能互补信息，提升深度估计和3D框回归的鲁棒性。④在KITTI基准上，该方法在中等难度下达到领先的3D检测精度，AP值显著高于同类方法。
- **摘要（英）**: This paper tackles inaccurate localization in monocular 3D detection due to lack of depth. It proposes MonoJSG, which builds a joint semantic and geometric cost volume to simultaneously estimate semantics and depth via differentiable aggregation. Compared to semantic-only or geometric-only methods, joint modeling improves robustness, achieving leading 3D AP on KITTI under moderate difficulty.
- **核心贡献**: 提出语义与几何联合代价体，增强单目3D检测的深度估计。
- **创新点**: 将语义和几何信息统一到代价体框架中，实现端到端联合优化。
- **结果**: 在KITTI中等难度下达到领先的3D检测精度。

### Exploring Geometric Consistency for Monocular 3D Object Detection. **⭐⭐⭐** (相关度: 90%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00173) · 📚 被引 33
- **作者**: Qing Lian, Botao Ye, Ruijia Xu, Weilong Yao, Tong Zhang
- **🏷️ 机构**: The Hong Kong University of Science and Technology, Institute of Computing Technology, Chinese Academy of Sciences,China, Autowise.AI
- **会议**: CVPR 2022
- **摘要（中）**: ①针对单目3D检测中几何一致性约束不足的问题。②提出一种探索几何一致性的方法，通过利用多视图几何和投影约束，在训练中强化3D框与2D投影的一致性。③相比仅使用单帧监督的方法，该方法引入跨视角一致性损失，提升模型对深度和姿态的估计能力。④在KITTI和nuScenes上，该方法在多个难度级别上提升了3D检测AP，尤其在遮挡场景中效果明显。
- **摘要（英）**: This paper addresses insufficient geometric consistency in monocular 3D detection. It proposes a method that enforces consistency between 3D boxes and their 2D projections via multi-view geometry during training. Compared to single-frame supervision, it improves depth and pose estimation, yielding higher 3D AP on KITTI and nuScenes, especially under occlusion.
- **核心贡献**: 引入跨视角几何一致性损失，提升单目3D检测的鲁棒性。
- **创新点**: 利用多视图投影约束强化3D-2D一致性。
- **结果**: 在KITTI和nuScenes上提升3D检测精度。

### Rope3D: The Roadside Perception Dataset for Autonomous Driving and Monocular 3D Object Detection Task. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.02065) · 📚 被引 149
- **作者**: Xiaoqing Ye, Mao Shu, Hanyu Li, Yifeng Shi, Yingying Li, Guangjie Wang et al.
- **🏷️ 机构**: Baidu Inc., China University of Mining and Technology
- **会议**: CVPR 2022
- **摘要（中）**: ①这篇论文针对自动驾驶中路边感知（roadside perception）缺乏大规模、高多样性数据集的问题，特别是单目3D物体检测在复杂交通场景下的挑战。②作者构建了Rope3D数据集，包含5万帧图像和超过150万个3D标注框，覆盖晴天、雨天、雾天等多种天气和不同光照条件，并提供了详细的传感器标定和标注协议。③相比现有数据集（如KITTI、nuScenes），Rope3D专注于路边视角，具有更远的感知距离、更高的遮挡和截断比例，并引入了针对路边场景的评估指标（如基于距离的AP）。④实验表明，在该数据集上训练的模型在远距离和遮挡场景下的3D检测性能显著优于在现有数据集上的结果，为路边感知研究提供了基准。
- **摘要（英）**: This paper addresses the lack of large-scale, diverse roadside perception datasets for autonomous driving, particularly for monocular 3D object detection in complex traffic. The authors introduce Rope3D, containing 50k images with over 1.5M 3D annotations across various weather and lighting conditions, featuring longer perception ranges and higher occlusion/truncation ratios than existing datasets. Experiments show models trained on Rope3D achieve significantly better 3D detection performance in distant and occluded scenarios, establishing a new benchmark for roadside perception.
- **核心贡献**: 提供了首个大规模、多条件的路边单目3D检测数据集Rope3D及相应评估基准。
- **创新点**: 聚焦于路边视角，引入针对远距离和遮挡场景的评估指标，并覆盖多样化天气条件。
- **结果**: 在Rope3D上训练的模型在远距离和遮挡场景下的3D检测性能显著优于现有数据集训练的模型。

### Dimension Embeddings for Monocular 3D Object Detection. **⭐⭐⭐** (相关度: 90%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00164) · 📚 被引 20
- **作者**: Yunpeng Zhang, Wenzhao Zheng, Zheng Zhu, Guan Huang, Dalong Du, Jie Zhou et al.
- **🏷️ 机构**: Beijing National Research Center for Information Science and Technology,China, PhiGent Robotics
- **会议**: CVPR 2022
- **摘要（中）**: 这篇论文针对单目3D目标检测中缺乏深度信息的问题，提出使用维度嵌入（Dimension Embeddings）来增强检测性能。方法可能涉及将物体尺寸等维度信息编码为嵌入特征，以辅助3D定位。相比已有工作，该方法的改进点在于利用维度先验来缓解深度模糊性。由于摘要不完整，无法提供具体效果数据。
- **摘要（英）**: This paper addresses monocular 3D object detection by introducing dimension embeddings to improve localization. It likely encodes object size priors to mitigate depth ambiguity. Specific results are unavailable due to incomplete abstract.
- **核心贡献**: 提出维度嵌入用于单目3D检测。
- **创新点**: 利用维度信息作为辅助线索。
- **结果**: 未提供具体数据。

### Cross-Modality Knowledge Distillation Network for Monocular 3D Object Detection. **⭐⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2211.07171](https://arxiv.org/abs/2211.07171)
- **作者**: Yu Hong, Hang Dai, Yong Ding
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 这篇论文针对单目3D检测中已有跨模态方法训练策略非端到端且对LiDAR信息利用不充分的问题，提出了跨模态知识蒸馏网络CMKD。方法上，CMKD在特征和响应两个层面高效地将LiDAR模态知识直接迁移到图像模态，并进一步扩展为半监督训练框架，从大规模无标注数据中蒸馏知识。相比已有方法，CMKD实现了端到端训练并更充分地挖掘了LiDAR数据的潜力。在KITTI test集和Waymo val集上，CMKD在已发表方法中排名第一，显著优于之前的SOTA方法。
- **摘要（英）**: This paper proposes CMKD, a cross-modality knowledge distillation network for monocular 3D detection, which efficiently transfers LiDAR knowledge to the image modality at both feature and response levels. It is further extended to a semi-supervised framework by distilling from large-scale unlabeled data. CMKD achieves state-of-the-art performance, ranking first among published monocular detectors on KITTI test and Waymo val sets.
- **核心贡献**: 提出了一个高效的跨模态知识蒸馏框架，用于提升单目3D检测性能。
- **创新点**: 在特征和响应层面同时进行知识蒸馏，并扩展至半监督学习。
- **结果**: 在KITTI和Waymo基准上取得了最先进的性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Leveraging LiDAR-based detectors or real LiDAR point data to guide monocular 3D detection has brought significant improvement, e.g., Pseudo-LiDAR methods. However, the existing methods usually apply non-end-to-end training strategies and insufficiently leverage the LiDAR information, where the rich potential of the LiDAR data has not been well exploited. In this paper, we propose the Cross-Modality Knowledge Distillation (CMKD) network for monocular 3D detection to efficiently and directly transfer the knowledge from LiDAR modality to image modality on both features and responses. Moreover, we further extend CMKD as a semi-supervised training framework by distilling knowledge from large-scale unlabeled data and significantly boost the performance. Until submission, CMKD ranks $1^{st}$ among the monocular 3D detectors with publications on both KITTI $test$ set and Waymo $val$ set with significant performance gains compared to previous state-of-the-art methods.

</details>

### CramNet: Camera-Radar Fusion with Ray-Constrained Cross-Attention for Robust 3D Object Detection. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2210.09267](https://arxiv.org/abs/2210.09267) · 📚 被引 57
- **作者**: Jyh-Jing Hwang, Henrik Kretzschmar, Joshua Manela, Sean Rafferty, Nicholas Armstrong-Crews, Tiffany L. Chen et al.
- **🏷️ 机构**: Waymo
- **会议**: ECCV 2022
- **摘要（中）**: 这篇论文针对相机和雷达融合中深度和仰角信息缺失导致几何对应模糊的问题，提出了CramNet。方法上，CramNet在联合3D空间中融合相机和雷达数据，并设计了射线约束交叉注意力机制，利用雷达测距信息改善相机深度预测，解决了几何对应歧义。此外，该方法支持传感器模态dropout训练，增强了在传感器故障时的鲁棒性。在RADIATE数据集上的实验验证了融合方法的有效性，其相机单模态变体也取得了有竞争力的性能。
- **摘要（英）**: This paper proposes CramNet, a camera-radar fusion network that addresses the geometric ambiguity in cross-modal matching by introducing a ray-constrained cross-attention mechanism. It fuses sensor data in a joint 3D space and supports modality dropout training for robustness. Experiments on the RADIATE dataset demonstrate the effectiveness of the fusion approach.
- **核心贡献**: 提出了一种基于射线约束交叉注意力的相机-雷达融合3D检测网络。
- **创新点**: 设计了射线约束交叉注意力机制，有效解决了跨模态几何对应歧义。
- **结果**: 在RADIATE数据集上验证了融合方法的有效性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Robust 3D object detection is critical for safe autonomous driving. Camera and radar sensors are synergistic as they capture complementary information and work well under different environmental conditions. Fusing camera and radar data is challenging, however, as each of the sensors lacks information along a perpendicular axis, that is, depth is unknown to camera and elevation is unknown to radar. We propose the camera-radar matching network CramNet, an efficient approach to fuse the sensor readings from camera and radar in a joint 3D space. To leverage radar range measurements for better camera depth predictions, we propose a novel ray-constrained cross-attention mechanism that resolves the ambiguity in the geometric correspondences between camera features and radar features. Our method supports training with sensor modality dropout, which leads to robust 3D object detection, even when a camera or radar sensor suddenly malfunctions on a vehicle. We demonstrate the effectiveness of our fusion approach through extensive experiments on the RADIATE dataset, one of the few large-scale datasets that provide radar radio frequency imagery. A camera-only variant of our method achieves competitive performance in monocular 3D object detection on the Waymo Open Dataset.

</details>

### DEVIANT: Depth EquiVarIAnt NeTwork for Monocular 3D Object Detection. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2207.10758](https://arxiv.org/abs/2207.10758) · 📚 被引 69
- **作者**: Abhinav Kumar, Garrick Brazil, Enrique Corona, Armin Parchami, Xiaoming Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 这篇论文针对单目3D检测中标准卷积块不具备投影流形上深度平移等变性、导致深度估计困难的问题，提出了DEVIANT网络。方法上，DEVIANT利用现有的尺度等变steerable块构建，使网络对投影流形中的深度平移具有等变性，而普通网络不具备此性质。相比已有方法，额外的深度等变性迫使DEVIANT学习一致的深度估计。在KITTI和Waymo数据集的图像单模态类别中，DEVIANT取得了最先进的单目3D检测结果，并在跨数据集评估中表现优于普通网络。
- **摘要（英）**: This paper proposes DEVIANT, a monocular 3D detection network built with scale-equivariant steerable blocks to achieve equivariance to depth translations in the projective manifold. This property forces consistent depth estimation, unlike vanilla networks. DEVIANT achieves state-of-the-art results on KITTI and Waymo in the image-only category and performs better in cross-dataset evaluation.
- **核心贡献**: 提出了一个深度等变网络DEVIANT，用于提升单目3D检测的深度估计一致性。
- **创新点**: 利用尺度等变steerable块实现投影流形上的深度平移等变性。
- **结果**: 在KITTI和Waymo上取得了最先进的单目3D检测性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Modern neural networks use building blocks such as convolutions that are equivariant to arbitrary 2D translations. However, these vanilla blocks are not equivariant to arbitrary 3D translations in the projective manifold. Even then, all monocular 3D detectors use vanilla blocks to obtain the 3D coordinates, a task for which the vanilla blocks are not designed for. This paper takes the first step towards convolutions equivariant to arbitrary 3D translations in the projective manifold. Since the depth is the hardest to estimate for monocular detection, this paper proposes Depth EquiVarIAnt NeTwork (DEVIANT) built with existing scale equivariant steerable blocks. As a result, DEVIANT is equivariant to the depth translations in the projective manifold whereas vanilla networks are not. The additional depth equivariance forces the DEVIANT to learn consistent depth estimates, and therefore, DEVIANT achieves state-of-the-art monocular 3D detection results on KITTI and Waymo datasets in the image-only category and performs competitively to methods using extra information. Moreover, DEVIANT works better than vanilla networks in cross-dataset evaluation. Code and models at https://github.com/abhi1kumar/DEVIANT

</details>

### Densely Constrained Depth Estimator for Monocular 3D Object Detection. **⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2207.10047](https://arxiv.org/abs/2207.10047)
- **作者**: Yingyan Li, Yuntao Chen, Jiawei He, Zhaoxiang Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 这篇论文针对单目3D检测中深度估计不准确的问题，指出现有方法仅利用垂直边缘作为投影约束，导致深度候选不足。作者提出使用任意方向边缘的密集投影约束，生成更多深度候选，并设计图匹配加权模块融合候选。在KITTI和WOD基准上达到最先进性能。
- **摘要（英）**: This paper tackles inaccurate depth estimation in monocular 3D detection by using dense projection constraints from edges of any direction, unlike prior vertical-edge-only methods. A graph matching weighting module merges depth candidates. It achieves state-of-the-art on KITTI and WOD benchmarks.
- **核心贡献**: 提出密集投影约束和加权融合模块。
- **创新点**: 利用任意方向边缘的密集约束。
- **结果**: 在KITTI和WOD上达到SOTA。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Estimating accurate 3D locations of objects from monocular images is a challenging problem because of lacking depth. Previous work shows that utilizing the object's keypoint projection constraints to estimate multiple depth candidates boosts the detection performance. However, the existing methods can only utilize vertical edges as projection constraints for depth estimation. So these methods only use a small number of projection constraints and produce insufficient depth candidates, leading to inaccurate depth estimation. In this paper, we propose a method that utilizes dense projection constraints from edges of any direction. In this way, we employ much more projection constraints and produce considerable depth candidates. Besides, we present a graph matching weighting module to merge the depth candidates. The proposed method DCD (Densely Constrained Detector) achieves state-of-the-art performance on the KITTI and WOD benchmarks. Code is released at https://github.com/BraveGroup/DCD.

</details>

### Unsupervised Domain Adaptation for Monocular 3D Object Detection via Self-training. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2204.11590](https://arxiv.org/abs/2204.11590)
- **作者**: Zhenyu Li, Zehui Chen, Ang Li, Liangji Fang, Qinhong Jiang, Xianming Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 这篇论文针对单目3D检测在跨域部署时性能急剧下降的问题，提出了STMono3D无监督域适应框架。方法上，首先发现域差距的关键因素是几何错位导致的深度偏移问题，然后引入几何对齐的多尺度训练策略来解耦相机参数并保证域间几何一致性，并开发了教师-学生范式生成自适应伪标签。相比已有方法，该框架是端到端的，并通过质量感知监督策略利用实例级伪置信度提升训练效果。实验表明，该方法能有效缓解深度偏移并提升目标域检测性能。
- **摘要（英）**: This paper proposes STMono3D, a self-teaching framework for unsupervised domain adaptation in monocular 3D detection, addressing the depth-shift issue caused by geometric misalignment. It introduces a geometry-aligned multi-scale training strategy and a teacher-student paradigm with quality-aware supervision. The method effectively mitigates domain gaps and improves target-domain performance.
- **核心贡献**: 提出了一个针对单目3D检测的无监督域适应自训练框架。
- **创新点**: 通过几何对齐多尺度训练和实例级质量感知监督解决深度偏移问题。
- **结果**: 有效提升了跨域单目3D检测性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular 3D object detection (Mono3D) has achieved unprecedented success with the advent of deep learning techniques and emerging large-scale autonomous driving datasets. However, drastic performance degradation remains an unwell-studied challenge for practical cross-domain deployment as the lack of labels on the target domain. In this paper, we first comprehensively investigate the significant underlying factor of the domain gap in Mono3D, where the critical observation is a depth-shift issue caused by the geometric misalignment of domains. Then, we propose STMono3D, a new self-teaching framework for unsupervised domain adaptation on Mono3D. To mitigate the depth-shift, we introduce the geometry-aligned multi-scale training strategy to disentangle the camera parameters and guarantee the geometry consistency of domains. Based on this, we develop a teacher-student paradigm to generate adaptive pseudo labels on the target domain. Benefiting from the end-to-end framework that provides richer information of the pseudo labels, we propose the quality-aware supervision strategy to take instance-level pseudo confidences into account and improve the effectiveness of the target-domain training process. Moreover, the positive focusing training strategy and dynamic threshold are proposed to handle tremendous FN and FP pseudo samples. STMono3D achieves remarkable performance on all evaluated datasets and even surpasses fully supervised results on the KITTI 3D object detection dataset. To the best of our knowledge, this is the first study to explore effective UDA methods for Mono3D.

</details>

### DID-M3D: Decoupling Instance Depth for Monocular 3D Object Detection. **⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2207.08531](https://arxiv.org/abs/2207.08531) · 📚 被引 78
- **作者**: Liang Peng, Xiaopei Wu, Zheng Yang, Haifeng Liu, Deng Cai
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 这篇论文针对单目3D检测中实例深度估计困难的问题，指出现有直接回归方法不直观，因为深度耦合了视觉深度和属性深度。作者提出将实例深度解耦为视觉表面深度和属性深度，并分别估计不确定性。通过组合不同深度和不确定性获得最终深度，并改进数据增强。该方法在KITTI等基准上表现优异。
- **摘要（英）**: This paper addresses instance depth estimation in monocular 3D detection by decoupling it into visual surface depth and attribute depth, each with associated uncertainties. This reformulation improves learning and data augmentation. The method achieves strong performance on benchmarks like KITTI.
- **核心贡献**: 提出实例深度解耦方法。
- **创新点**: 区分视觉与属性深度。
- **结果**: 在KITTI等上表现优异。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular 3D detection has drawn much attention from the community due to its low cost and setup simplicity. It takes an RGB image as input and predicts 3D boxes in the 3D space. The most challenging sub-task lies in the instance depth estimation. Previous works usually use a direct estimation method. However, in this paper we point out that the instance depth on the RGB image is non-intuitive. It is coupled by visual depth clues and instance attribute clues, making it hard to be directly learned in the network. Therefore, we propose to reformulate the instance depth to the combination of the instance visual surface depth (visual depth) and the instance attribute depth (attribute depth). The visual depth is related to objects' appearances and positions on the image. By contrast, the attribute depth relies on objects' inherent attributes, which are invariant to the object affine transformation on the image. Correspondingly, we decouple the 3D location uncertainty into visual depth uncertainty and attribute depth uncertainty. By combining different types of depths and associated uncertainties, we can obtain the final instance depth. Furthermore, data augmentation in monocular 3D detection is usually limited due to the physical nature, hindering the boost of performance. Based on the proposed instance depth disentanglement strategy, we can alleviate this problem. Evaluated on KITTI, our method achieves new state-of-the-art results, and extensive ablation studies validate the effectiveness of each component in our method. The codes are released at https://github.com/SPengLiang/DID-M3D.

</details>

### Monocular 3D Object Detection with Depth from Motion. **⭐⭐⭐⭐** (相关度: 93%)
- **链接**: [arXiv:2207.12988](https://arxiv.org/abs/2207.12988)
- **作者**: Tai Wang, Jiangmiao Pang, Dahua Lin
- **🏷️ 机构**: CUHK
- **会议**: ECCV 2022
- **摘要（中）**: 这篇论文针对单目3D检测中绝对深度预测困难的问题，利用相机自运动提供的几何结构进行深度估计。作者分析了双视图情况下的挑战，包括累积误差和静态相机问题，并提出用几何感知成本体积建立立体对应，结合单目理解补偿。框架DfM将2D特征提升到3D空间检测，并支持无位姿版本。在多个基准上大幅超越现有方法。
- **摘要（英）**: This paper leverages camera ego-motion for depth estimation in monocular 3D detection, addressing challenges like cumulative errors and static cameras. It uses a geometry-aware cost volume for stereo correspondence, compensated by monocular understanding. The DfM framework lifts features to 3D and outperforms SOTA by a large margin.
- **核心贡献**: 提出基于运动深度的单目3D检测框架。
- **创新点**: 结合成本体积与单目补偿。
- **结果**: 大幅超越SOTA。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Perceiving 3D objects from monocular inputs is crucial for robotic systems, given its economy compared to multi-sensor settings. It is notably difficult as a single image can not provide any clues for predicting absolute depth values. Motivated by binocular methods for 3D object detection, we take advantage of the strong geometry structure provided by camera ego-motion for accurate object depth estimation and detection. We first make a theoretical analysis on this general two-view case and notice two challenges: 1) Cumulative errors from multiple estimations that make the direct prediction intractable; 2) Inherent dilemmas caused by static cameras and matching ambiguity. Accordingly, we establish the stereo correspondence with a geometry-aware cost volume as the alternative for depth estimation and further compensate it with monocular understanding to address the second problem. Our framework, named Depth from Motion (DfM), then uses the established geometry to lift 2D image features to the 3D space and detects 3D objects thereon. We also present a pose-free DfM to make it usable when the camera pose is unavailable. Our framework outperforms state-of-the-art methods by a large margin on the KITTI benchmark. Detailed quantitative and qualitative analyses also validate our theoretical conclusions. The code will be released at https://github.com/Tai-Wang/Depth-from-Motion.

</details>

### Depth Map Decomposition for Monocular Depth Estimation. **⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2208.10762](https://arxiv.org/abs/2208.10762)
- **作者**: Jinyoung Jun, Jaehan Lee, Chul Lee, Chang-Su Kim
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对单目深度估计中，当训练数据缺少度量深度标签时性能受限的问题。②提出将度量深度图分解为归一化深度图和尺度特征，网络由共享编码器和三个解码器（G-Net、N-Net、M-Net）组成，分别估计梯度图、归一化深度图和度量深度图。③相比现有方法，可以利用无度量深度标签的数据集提升度量深度估计性能。④在多个数据集上的实验表明，该方法不仅与最先进算法性能相当，而且在仅有少量度量深度数据时也能获得可接受的结果。
- **摘要（英）**: This paper addresses monocular depth estimation when metric depth labels are scarce. It decomposes a metric depth map into a normalized depth map and scale features, using a shared encoder and three decoders (G-Net, N-Net, M-Net). This allows leveraging datasets without metric labels, achieving competitive performance and robustness with limited metric data.
- **核心贡献**: 提出深度图分解方法，将度量深度估计分解为归一化深度和尺度特征，支持利用无度量标签数据。
- **创新点**: 通过G-Net和N-Net提取相对深度特征辅助M-Net，实现更准确的度量深度估计。
- **结果**: 在多个数据集上达到与最先进方法相当的性能，并在少量度量数据下表现良好。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose a novel algorithm for monocular depth estimation that decomposes a metric depth map into a normalized depth map and scale features. The proposed network is composed of a shared encoder and three decoders, called G-Net, N-Net, and M-Net, which estimate gradient maps, a normalized depth map, and a metric depth map, respectively. M-Net learns to estimate metric depths more accurately using relative depth features extracted by G-Net and N-Net. The proposed algorithm has the advantage that it can use datasets without metric depth labels to improve the performance of metric depth estimation. Experimental results on various datasets demonstrate that the proposed algorithm not only provides competitive performance to state-of-the-art algorithms but also yields acceptable results even when only a small amount of metric depth data is available for its training.

</details>

### Physical Attack on Monocular Depth Estimation with Optimal Adversarial Patches. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2207.04718](https://arxiv.org/abs/2207.04718) · 📚 被引 11
- **作者**: Zhiyuan Cheng, James Liang, Hongjun Choi, Guanhong Tao, Zhiwen Cao, Dongfang Liu et al.
- **🏷️ 机构**: School of Automation, Northwestern Polytechnical University, Xi&#x2019;an, Shaanxi, China
- **会议**: ECCV 2022
- **摘要（中）**: ①针对基于学习的单目深度估计在自动驾驶中的安全性，提出物理对抗攻击方法。②使用优化方法生成隐蔽的、面向物理对象的对抗补丁，攻击深度估计，结合对象导向设计、敏感区域定位和自然风格伪装。③相比现有攻击，平衡了隐蔽性和有效性，并评估了对下游3D检测任务的影响。④在真实驾驶场景中，对多个MDE模型和3D检测任务，实现了超过6米的平均深度估计误差和93%的攻击成功率，实车测试也验证了有效性。
- **摘要（英）**: This paper develops a physical attack against learning-based monocular depth estimation in autonomous driving. It generates stealthy object-oriented adversarial patches via optimization, balancing stealth and effectiveness. Real-world experiments show over 6 meters mean depth error and 93% attack success rate on 3D detection, highlighting security vulnerabilities.
- **核心贡献**: 提出针对单目深度估计的物理对抗补丁攻击方法，并验证了对下游任务的实际影响。
- **创新点**: 结合对象导向设计和自然风格伪装，生成隐蔽且有效的物理对抗补丁。
- **结果**: 在真实场景中实现超过6米深度误差和93%攻击成功率，证明了攻击的严重性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep learning has substantially boosted the performance of Monocular Depth Estimation (MDE), a critical component in fully vision-based autonomous driving (AD) systems (e.g., Tesla and Toyota). In this work, we develop an attack against learning-based MDE. In particular, we use an optimization-based method to systematically generate stealthy physical-object-oriented adversarial patches to attack depth estimation. We balance the stealth and effectiveness of our attack with object-oriented adversarial design, sensitive region localization, and natural style camouflage. Using real-world driving scenarios, we evaluate our attack on concurrent MDE models and a representative downstream task for AD (i.e., 3D object detection). Experimental results show that our method can generate stealthy, effective, and robust adversarial patches for different target objects and models and achieves more than 6 meters mean depth estimation error and 93% attack success rate (ASR) in object detection with a patch of 1/9 of the vehicle's rear area. Field tests on three different driving routes with a real vehicle indicate that we cause over 6 meters mean depth estimation error and reduce the object detection rate from 90.70% to 5.16% in continuous video frames.

</details>

### BRNet: Exploring Comprehensive Features for Monocular Depth Estimation. **⭐⭐** (相关度: 50%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19839-7_34) · 📚 被引 40
- **作者**: Wencheng Han, Junbo Yin, Xiaogang Jin, Xiangdong Dai, Jianbing Shen
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①该论文摘要为空，无法获取具体研究问题和方法。②根据标题推测，可能探索单目深度估计的综合特征。③由于缺乏摘要，无法评估其改进点和效果。④建议查阅全文以获取详细信息。
- **摘要（英）**: The abstract is empty, so the specific problem, method, and results cannot be assessed. Based on the title, it likely explores comprehensive features for monocular depth estimation, but further details require the full paper.
- **核心贡献**: 未知，因摘要缺失。
- **创新点**: 未知，因摘要缺失。
- **结果**: 未知，因摘要缺失。

### Gradient-Based Uncertainty for Monocular Depth Estimation. **⭐⭐⭐⭐** (相关度: 65%)
- **链接**: [arXiv:2208.02005](https://arxiv.org/abs/2208.02005)
- **作者**: Julia Hornauer, Vasileios Belagiannis
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对单目深度估计中由于图像上下文干扰（如移动物体、反射材料）导致的错误预测，提出像素级不确定性估计的需求。②提出一种事后不确定性估计方法，针对已训练好的固定深度估计模型，利用辅助损失函数提取梯度来估计不确定性，辅助损失基于图像与其水平翻转的深度预测一致性。③相比现有方法，无需重新训练网络，且不依赖地面真值。④在KITTI和NYU Depth V2基准上达到最先进的不确定性估计结果，代码和模型已公开。
- **摘要（英）**: This paper proposes a post hoc uncertainty estimation method for monocular depth estimation, using gradients from an auxiliary loss based on depth prediction consistency between an image and its horizontally flipped version. It requires no retraining or ground truth, achieving state-of-the-art uncertainty results on KITTI and NYU Depth V2.
- **核心贡献**: 提出基于梯度的事后不确定性估计方法，无需重训网络即可获得高质量不确定性。
- **创新点**: 利用水平翻转一致性定义辅助损失，避免依赖地面真值。
- **结果**: 在KITTI和NYU Depth V2上达到最先进性能，并公开代码。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In monocular depth estimation, disturbances in the image context, like moving objects or reflecting materials, can easily lead to erroneous predictions. For that reason, uncertainty estimates for each pixel are necessary, in particular for safety-critical applications such as automated driving. We propose a post hoc uncertainty estimation approach for an already trained and thus fixed depth estimation model, represented by a deep neural network. The uncertainty is estimated with the gradients which are extracted with an auxiliary loss function. To avoid relying on ground-truth information for the loss definition, we present an auxiliary loss function based on the correspondence of the depth prediction for an image and its horizontally flipped counterpart. Our approach achieves state-of-the-art uncertainty estimation results on the KITTI and NYU Depth V2 benchmarks without the need to retrain the neural network. Models and code are publicly available at https://github.com/jhornauer/GrUMoDepth.

</details>

### Adaptive Co-teaching for Unsupervised Monocular Depth Estimation. **⭐⭐⭐** (相关度: 75%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19769-7_6)
- **作者**: Weisong Ren, Lijun Wang, Yongri Piao, Miao Zhang, Huchuan Lu, Ting Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①该论文针对无监督单目深度估计中伪标签噪声和训练不稳定的问题。②提出了一种自适应协同教学（Adaptive Co-teaching）框架，利用两个网络相互教学，并动态调整学习策略以过滤噪声样本。③相比已有协同教学方法，该方法引入了自适应机制，能根据训练进度和样本难度动态调整权重，提高了鲁棒性。④在KITTI等基准上取得了较好的深度估计性能，但摘要中未提供具体数值。
- **摘要（英）**: This paper tackles the issues of noisy pseudo-labels and training instability in unsupervised monocular depth estimation. It proposes an adaptive co-teaching framework where two networks teach each other with dynamically adjusted learning strategies to filter noisy samples. Compared to existing co-teaching methods, the adaptive mechanism adjusts weights based on training progress and sample difficulty, enhancing robustness. Improved depth estimation performance is achieved on benchmarks like KITTI, though specific numbers are not given in the abstract.
- **核心贡献**: 提出自适应协同教学框架，提升无监督单目深度估计对噪声伪标签的鲁棒性。
- **创新点**: 引入基于训练进度和样本难度的动态权重调整机制。
- **结果**: 在KITTI等基准上获得改进的深度估计性能。

### Spike Transformer: Monocular Depth Estimation for Spiking Camera.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20071-7_3) · 📚 被引 28
- **作者**: Jiyuan Zhang, Lulu Tang, Zhaofei Yu, Jiwen Lu, Tie-Jun Huang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Towards Scale-Aware, Robust, and Generalizable Unsupervised Monocular Depth Estimation by Integrating IMU Motion Dynamics.
- **链接**: [arXiv:2207.04680](https://arxiv.org/abs/2207.04680) · 📚 被引 38
- **作者**: Sen Zhang, Jing Zhang, Dacheng Tao
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Unsupervised monocular depth and ego-motion estimation has drawn extensive research attention in recent years. Although current methods have reached a high up-to-scale accuracy, they usually fail to learn the true scale metric due to the inherent scale ambiguity from training with monocular sequences. In this work, we tackle this problem and propose DynaDepth, a novel scale-aware framework that integrates information from vision and IMU motion dynamics. Specifically, we first propose an IMU photometric loss and a cross-sensor photometric consistency loss to provide dense supervision and absolute scales. To fully exploit the complementary information from both sensors, we further drive a differentiable camera-centric extended Kalman filter (EKF) to update the IMU preintegrated motions when observing visual measurements. In addition, the EKF formulation enables learning an ego-motion uncertainty measure, which is non-trivial for unsupervised methods. By leveraging IMU during training, DynaDepth not only learns an absolute scale, but also provides a better generalization ability and robustness against vision degradation such as illumination change and moving objects. We validate the effectiveness of DynaDepth by conducting extensive experiments and simulations on the KITTI and Make3D datasets.

</details>

### MonoDistill: Learning Spatial Features for Monocular 3D Object Detection.
- **链接**: [arXiv:2201.10830](https://arxiv.org/abs/2201.10830)
- **作者**: Zhiyu Chong, Xinzhu Ma, Hong Zhang, Yuxin Yue, Haojie Li, Zhihui Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D object detection is a fundamental and challenging task for 3D scene understanding, and the monocular-based methods can serve as an economical alternative to the stereo-based or LiDAR-based methods. However, accurately detecting objects in the 3D space from a single image is extremely difficult due to the lack of spatial cues. To mitigate this issue, we propose a simple and effective scheme to introduce the spatial information from LiDAR signals to the monocular 3D detectors, without introducing any extra cost in the inference phase. In particular, we first project the LiDAR signals into the image plane and align them with the RGB images. After that, we use the resulting data to train a 3D detector (LiDAR Net) with the same architecture as the baseline model. Finally, this LiDAR Net can serve as the teacher to transfer the learned knowledge to the baseline model. Experimental results show that the proposed method can significantly boost the performance of the baseline model and ranks the $1^{st}$ place among all monocular-based methods on the KITTI benchmark. Besides, extensive ablation studies are conducted, which further prove the effectiveness of each part of our designs and illustrate what the baseline model has learned from the LiDAR Net. Our code will be released at \url{https://github.com/monster-ghost/MonoDistill}.

</details>

### WeakM3D: Towards Weakly Supervised Monocular 3D Object Detection.
- **链接**: [arXiv:2203.08332](https://arxiv.org/abs/2203.08332)
- **作者**: Liang Peng, Senbo Yan, Boxi Wu, Zheng Yang, Xiaofei He, Deng Cai
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular 3D object detection is one of the most challenging tasks in 3D scene understanding. Due to the ill-posed nature of monocular imagery, existing monocular 3D detection methods highly rely on training with the manually annotated 3D box labels on the LiDAR point clouds. This annotation process is very laborious and expensive. To dispense with the reliance on 3D box labels, in this paper we explore the weakly supervised monocular 3D detection. Specifically, we first detect 2D boxes on the image. Then, we adopt the generated 2D boxes to select corresponding RoI LiDAR points as the weak supervision. Eventually, we adopt a network to predict 3D boxes which can tightly align with associated RoI LiDAR points. This network is learned by minimizing our newly-proposed 3D alignment loss between the 3D box estimates and the corresponding RoI LiDAR points. We will illustrate the potential challenges of the above learning problem and resolve these challenges by introducing several effective designs into our method. Codes will be available at https://github.com/SPengLiang/WeakM3D.

</details>

### MoGDE: Boosting Mobile Monocular 3D Object Detection with Ground Depth Estimation.
- **链接**: [arXiv:2303.13561](https://arxiv.org/abs/2303.13561) · 📚 被引 3
- **作者**: Yunsong Zhou, Quan Liu, Hongzi Zhu, Yunzhe Li, Shan Chang, Minyi Guo
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular 3D object detection (Mono3D) in mobile settings (e.g., on a vehicle, a drone, or a robot) is an important yet challenging task. Due to the near-far disparity phenomenon of monocular vision and the ever-changing camera pose, it is hard to acquire high detection accuracy, especially for far objects. Inspired by the insight that the depth of an object can be well determined according to the depth of the ground where it stands, in this paper, we propose a novel Mono3D framework, called MoGDE, which constantly estimates the corresponding ground depth of an image and then utilizes the estimated ground depth information to guide Mono3D. To this end, we utilize a pose detection network to estimate the pose of the camera and then construct a feature map portraying pixel-level ground depth according to the 3D-to-2D perspective geometry. Moreover, to improve Mono3D with the estimated ground depth, we design an RGB-D feature fusion network based on the transformer structure, where the long-range self-attention mechanism is utilized to effectively identify ground-contacting points and pin the corresponding ground depth to the image feature map. We conduct extensive experiments on the real-world KITTI dataset. The results demonstrate that MoGDE can effectively improve the Mono3D accuracy and robustness for both near and far objects. MoGDE yields the best performance compared with the state-of-the-art methods by a large margin and is ranked number one on the KITTI 3D benchmark.

</details>

## 跨领域论文（完整笔记在其他领域）

- Semi-supervised Monocular 3D Object Detection by Multi-view Consistency. → [3d-detection](../3d-detection/Guideline%202022.md)
- Lidar Point Cloud Guided Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- LiDAR Distillation: Bridging the Beam-Induced Domain Gap for 3D Object Detection. → [knowledge-distillation](../knowledge-distillation/Guideline%202022.md)
- RA-Depth: Resolution Adaptive Self-supervised Monocular Depth Estimation. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
- Towards Comprehensive Representation Enhancement in Semantics-Guided Self-supervised Monocular Depth Estimation. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
- Self-distilled Feature Aggregation for Self-supervised Monocular Depth Estimation. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
- DevNet: Self-supervised Monocular Depth Learning via Density Volume Construction. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
<!-- COMPLETE v1 papers=32 -->
