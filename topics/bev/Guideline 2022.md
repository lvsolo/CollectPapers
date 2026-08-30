# BEV — 2022 Guideline

> 领域: 鸟瞰图感知（BEV 特征、BEV 检测/分割/预测）
> 论文数: 1 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份:

### BEVFormer: Learning Bird's-Eye-View Representation from Multi-camera Images via Spatiotemporal Transformers. **⭐⭐⭐⭐⭐** (相关度: 100%)
- **链接**: [arXiv:2203.17270](https://arxiv.org/abs/2203.17270) · 📚 被引 1287
- **作者**: Zhiqi Li, Wenhai Wang, Hongyang Li, Enze Xie, Chonghao Sima, Tong Lu et al.
- **🏷️ 机构**: Shanghai AI Lab, Tsinghua / Shanghai AI Lab
- **会议**: ECCV 2022
- **摘要（中）**: ①针对多相机图像下3D感知任务（如3D检测和地图分割）中缺乏统一BEV表示和时序信息利用不足的问题。②提出了BEVFormer框架，通过预定义的网格状BEV查询，利用空间交叉注意力聚合多相机视角的空间特征，并通过时序自注意力循环融合历史BEV信息。③相比已有方法，首次在BEV空间中同时建模空间和时间信息，支持多任务，且无需昂贵的深度估计。④在nuScenes测试集上NDS达到56.9%，比之前最优方法高9.0点，与基于LiDAR的方法性能相当，并显著提升了速度估计精度和低可见度下的召回率。
- **摘要（英）**: This paper addresses the lack of unified BEV representation and temporal modeling in multi-camera 3D perception. It proposes BEVFormer, which uses spatiotemporal transformers with grid-shaped BEV queries and spatial cross-attention plus temporal self-attention to aggregate multi-view and historical features. It achieves 56.9% NDS on nuScenes test, surpassing prior art by 9.0 points and matching LiDAR-based methods.
- **核心贡献**: 提出基于时空Transformer的统一BEV表示框架，支持多任务3D感知。
- **创新点**: 通过网格化BEV查询结合空间交叉注意力和时序自注意力，实现多视角与时序信息的联合建模。
- **结果**: 在nuScenes上NDS达56.9%，超越现有方法并媲美LiDAR基线。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D visual perception tasks, including 3D detection and map segmentation based on multi-camera images, are essential for autonomous driving systems. In this work, we present a new framework termed BEVFormer, which learns unified BEV representations with spatiotemporal transformers to support multiple autonomous driving perception tasks. In a nutshell, BEVFormer exploits both spatial and temporal information by interacting with spatial and temporal space through predefined grid-shaped BEV queries. To aggregate spatial information, we design spatial cross-attention that each BEV query extracts the spatial features from the regions of interest across camera views. For temporal information, we propose temporal self-attention to recurrently fuse the history BEV information. Our approach achieves the new state-of-the-art 56.9\% in terms of NDS metric on the nuScenes \texttt{test} set, which is 9.0 points higher than previous best arts and on par with the performance of LiDAR-based baselines. We further show that BEVFormer remarkably improves the accuracy of velocity estimation and recall of objects under low visibility conditions. The code is available at \url{https://github.com/zhiqi-li/BEVFormer}.

</details>

### Lidar Point Cloud Guided Monocular 3D Object Detection. **⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2104.09035](https://arxiv.org/abs/2104.09035)
- **作者**: Liang Peng, Fei Liu, Zhengxu Yu, Senbo Yan, Dan Deng, Zheng Yang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对单目3D检测中昂贵的人工标注问题，该论文发现精确标注并非必要，使用随机扰动的粗糙标签也能达到相近精度，并指出3D位置部分更重要。基于此，提出LPCG框架，利用未标注的LiDAR点云生成伪标签，降低标注成本或提升精度。实验表明该方法有效，但摘要未提供具体数值。
- **摘要（英）**: This paper finds that precise 3D labels are unnecessary in monocular detection, with rough labels achieving similar accuracy, and proposes LPCG to generate pseudo-labels from unlabeled LiDAR point clouds. This reduces annotation costs or boosts accuracy, though specific results are not detailed.
- **核心贡献**: 提出利用LiDAR点云生成伪标签的单目3D检测框架。
- **创新点**: 揭示标签精度非关键，利用LiDAR测量替代人工标注。
- **结果**: 降低标注成本或提升检测精度。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular 3D object detection is a challenging task in the self-driving and computer vision community. As a common practice, most previous works use manually annotated 3D box labels, where the annotating process is expensive. In this paper, we find that the precisely and carefully annotated labels may be unnecessary in monocular 3D detection, which is an interesting and counterintuitive finding. Using rough labels that are randomly disturbed, the detector can achieve very close accuracy compared to the one using the ground-truth labels. We delve into this underlying mechanism and then empirically find that: concerning the label accuracy, the 3D location part in the label is preferred compared to other parts of labels. Motivated by the conclusions above and considering the precise LiDAR 3D measurement, we propose a simple and effective framework, dubbed LiDAR point cloud guided monocular 3D object detection (LPCG). This framework is capable of either reducing the annotation costs or considerably boosting the detection accuracy without introducing extra annotation costs. Specifically, It generates pseudo labels from unlabeled LiDAR point clouds. Thanks to accurate LiDAR 3D measurements in 3D space, such pseudo labels can replace manually annotated labels in the training of monocular 3D detectors, since their 3D location information is precise. LPCG can be applied into any monocular 3D detector to fully use massive unlabeled data in a self-driving system. As a result, in KITTI benchmark, we take the first place on both monocular 3D and BEV (bird's-eye-view) detection with a significant margin. In Waymo benchmark, our method using 10% labeled data achieves comparable accuracy to the baseline detector using 100% labeled data. The codes are released at https://github.com/SPengLiang/LPCG.

</details>

### Graph R-CNN: Towards Accurate 3D Object Detection with Semantic-Decorated Local Graph. **⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2208.03624](https://arxiv.org/abs/2208.03624) · 📚 被引 83
- **作者**: Honghui Yang, Zili Liu, Xiaopei Wu, Wenxiao Wang, Wei Qian, Xiaofei He et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对两阶段3D检测器中RoI特征提取对不均匀稀疏点云处理效率低的问题。②提出了Graph R-CNN，包含动态点聚合（patch search和动态最远体素采样）、RoI图池化（通过迭代消息传递建模上下文）和视觉特征增强。③相比现有方法，通过动态采样和图结构建模更好地适应点云分布，提升检测精度。④实验表明Graph R-CNN可应用于现有单阶段检测器，持续提升性能。
- **摘要（英）**: This paper improves two-stage 3D detection by proposing Graph R-CNN with dynamic point aggregation, RoI-graph pooling, and visual feature augmentation. It efficiently handles sparse and uneven points, enhancing contextual modeling, and consistently improves existing one-stage detectors.
- **核心贡献**: 提出了Graph R-CNN，通过动态聚合和图池化提升3D检测精度。
- **创新点**: 引入动态最远体素采样和RoI图池化，有效处理点云不均匀性。
- **结果**: 在多个数据集上持续提升单阶段检测器的性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Two-stage detectors have gained much popularity in 3D object detection. Most two-stage 3D detectors utilize grid points, voxel grids, or sampled keypoints for RoI feature extraction in the second stage. Such methods, however, are inefficient in handling unevenly distributed and sparse outdoor points. This paper solves this problem in three aspects. 1) Dynamic Point Aggregation. We propose the patch search to quickly search points in a local region for each 3D proposal. The dynamic farthest voxel sampling is then applied to evenly sample the points. Especially, the voxel size varies along the distance to accommodate the uneven distribution of points. 2) RoI-graph Pooling. We build local graphs on the sampled points to better model contextual information and mine point relations through iterative message passing. 3) Visual Features Augmentation. We introduce a simple yet effective fusion strategy to compensate for sparse LiDAR points with limited semantic cues. Based on these modules, we construct our Graph R-CNN as the second stage, which can be applied to existing one-stage detectors to consistently improve the detection performance. Extensive experiments show that Graph R-CNN outperforms the state-of-the-art 3D detection models by a large margin on both the KITTI and Waymo Open Dataset. And we rank first place on the KITTI BEV car detection leaderboard. Code will be available at \url{https://github.com/Nightmare-n/GraphRCNN}.

</details>

### ST-P3: End-to-End Vision-Based Autonomous Driving via Spatial-Temporal Feature Learning. **⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2207.07601](https://arxiv.org/abs/2207.07601) · 📚 被引 258
- **作者**: Shengchao Hu, Li Chen, Penghao Wu, Hongyang Li, Junchi Yan, Dacheng Tao
- **🏷️ 机构**: Shanghai AI Lab
- **会议**: ECCV 2022
- **摘要（中）**: ①这篇论文针对现有自动驾驶系统多阶段离散流水线（感知、预测、规划分离）导致误差累积、缺乏可解释性的问题，提出在可解释的视觉设置下进行端到端学习。②提出了ST-P3框架，通过空间-时间特征学习方案，联合优化感知、预测和规划任务，具体包括：用于BEV变换前保留3D几何信息的自我中心对齐累积技术、用于预测的考虑过去运动变化的双路径建模、以及用于规划补偿视觉元素识别的基于时间的细化单元。③相比已有工作，首次系统地研究了可解释的端到端视觉自动驾驶系统的每个部分，并显式设计空间-时间特征学习。④在nuScenes数据集上，ST-P3在3D目标检测、运动预测和规划等任务上均优于先前方法，并展示了更好的可解释性。
- **摘要（英）**: This paper addresses the issue of error accumulation and lack of interpretability in multi-stage discrete autonomous driving pipelines by proposing an interpretable vision-based end-to-end framework. It introduces ST-P3, which jointly learns perception, prediction, and planning through spatial-temporal feature learning, including egocentric-aligned accumulation for BEV transformation, dual-pathway modeling for motion prediction, and temporal-based refinement for planning. The method systematically improves all three tasks on nuScenes, outperforming prior approaches and enhancing interpretability.
- **核心贡献**: 提出了首个系统研究可解释端到端视觉自动驾驶各部分的ST-P3框架，通过空间-时间特征学习联合优化感知、预测和规划。
- **创新点**: 创新性地设计了自我中心对齐累积、双路径建模和时间细化单元，分别解决BEV变换中的几何信息保留、运动预测中的时序建模和规划中的视觉补偿问题。
- **结果**: 在nuScenes基准上，ST-P3在3D检测、运动预测和规划任务上均取得优于先前方法的性能，并提升了系统的可解释性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Many existing autonomous driving paradigms involve a multi-stage discrete pipeline of tasks. To better predict the control signals and enhance user safety, an end-to-end approach that benefits from joint spatial-temporal feature learning is desirable. While there are some pioneering works on LiDAR-based input or implicit design, in this paper we formulate the problem in an interpretable vision-based setting. In particular, we propose a spatial-temporal feature learning scheme towards a set of more representative features for perception, prediction and planning tasks simultaneously, which is called ST-P3. Specifically, an egocentric-aligned accumulation technique is proposed to preserve geometry information in 3D space before the bird's eye view transformation for perception; a dual pathway modeling is devised to take past motion variations into account for future prediction; a temporal-based refinement unit is introduced to compensate for recognizing vision-based elements for planning. To the best of our knowledge, we are the first to systematically investigate each part of an interpretable end-to-end vision-based autonomous driving system. We benchmark our approach against previous state-of-the-arts on both open-loop nuScenes dataset as well as closed-loop CARLA simulation. The results show the effectiveness of our method. Source code, model and protocol details are made publicly available at https://github.com/OpenPerceptionX/ST-P3.

</details>

### Fully Convolutional One-Stage 3D Object Detection on LiDAR Range Images. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2205.13764](https://arxiv.org/abs/2205.13764) · 📚 被引 16
- **作者**: Zhi Tian, Xiangxiang Chu, Xiaoming Wang, Xiaolin Wei, Chunhua Shen
- **🏷️ 机构**: ZJU
- **会议**: NeurIPS 2022
- **摘要（中）**: ①针对现有基于BEV的3D目标检测方法依赖复杂的体素化和稀疏卷积、计算开销大，而基于Range View的方法难以融合多帧点云的问题。②提出了FCOS-LiDAR，一种仅使用标准2D卷积的全卷积单阶段检测器，直接在LiDAR距离图像上进行检测，并设计了一种新颖的距离视图投影机制以融合多帧点云。③相比已有RV方法，首次实现了多帧融合，且无需稀疏卷积或体素化，显著简化了检测流程。④实验表明，该方法在保持与最先进BEV检测器相当性能的同时，速度更快、结构更简单，验证了RV方法的潜力。
- **摘要（英）**: This paper addresses the inefficiency of BEV-based 3D detectors and the multi-frame fusion challenge in range-view methods. It proposes FCOS-LiDAR, a fully convolutional one-stage detector using standard 2D convolutions on LiDAR range images, with a novel projection mechanism for multi-frame fusion. The method achieves comparable accuracy to state-of-the-art BEV detectors while being faster and simpler, marking the first successful multi-frame RV-based detection.
- **核心贡献**: 提出了首个支持多帧融合的基于距离图像的3D检测器，简化了检测流程。
- **创新点**: 设计了一种新颖的距离视图投影机制，实现多帧点云在RV空间的有效融合。
- **结果**: 在保持与BEV方法相当精度的同时，显著提升了检测速度和简化了模型结构。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a simple yet effective fully convolutional one-stage 3D object detector for LiDAR point clouds of autonomous driving scenes, termed FCOS-LiDAR. Unlike the dominant methods that use the bird-eye view (BEV), our proposed detector detects objects from the range view (RV, a.k.a. range image) of the LiDAR points. Due to the range view's compactness and compatibility with the LiDAR sensors' sampling process on self-driving cars, the range view-based object detector can be realized by solely exploiting the vanilla 2D convolutions, departing from the BEV-based methods which often involve complicated voxelization operations and sparse convolutions. For the first time, we show that an RV-based 3D detector with standard 2D convolutions alone can achieve comparable performance to state-of-the-art BEV-based detectors while being significantly faster and simpler. More importantly, almost all previous range view-based detectors only focus on single-frame point clouds, since it is challenging to fuse multi-frame point clouds into a single range view. In this work, we tackle this challenging issue with a novel range view projection mechanism, and for the first time demonstrate the benefits of fusing multi-frame point clouds for a range-view based detector. Extensive experiments on nuScenes show the superiority of our proposed method and we believe that our work can be strong evidence that an RV-based 3D detector can compare favourably with the current mainstream BEV-based detectors.

</details>

## 跨领域论文（完整笔记在其他领域）

- VISTA: Boosting 3D Object Detection via Dual Cross-VIew SpaTial Attention. → [object-detection](../object-detection/Guideline%202022.md)
- A Versatile Multi-View Framework for LiDAR-based 3D Object Detection with Guidance from Panoptic Segmentation. → [object-detection](../object-detection/Guideline%202022.md)
- Quo Vadis: Is Trajectory Forecasting the Key Towards Long-Term Multi-Object Tracking? → [tracking](../tracking/Guideline%202022.md)

<!-- COMPLETE v1 papers=5 -->
