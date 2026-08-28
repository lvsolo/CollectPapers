# Tracking — 2022 Guideline

> 领域: 目标跟踪（MOT / 3D 跟踪 / 多目标多相机跟踪）
> 论文数: 13 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: [2024](Guideline%202024.md)

### Towards Generic 3D Tracking in RGBD Videos: Benchmark and Baseline. **⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20047-2_7) · 📚 被引 4
- **作者**: Jinyu Yang, Zhongqun Zhang, Zhe Li, Hyung Jin Chang, Ales Leonardis, Feng Zheng
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对RGBD视频中通用3D目标跟踪缺乏统一基准和基线方法的问题。②提出了一个大规模的RGBD 3D跟踪基准数据集，并设计了一个基于点云和RGB信息的基线跟踪器。③相比已有工作，该工作首次系统性地评估了RGBD信息在3D跟踪中的潜力，并提供了标准化的评估协议。④实验结果表明，该基线方法在基准上取得了合理的性能，为后续研究提供了参考。
- **摘要（英）**: This paper addresses the lack of a unified benchmark and baseline for generic 3D object tracking in RGBD videos. It introduces a large-scale RGBD 3D tracking benchmark and a baseline tracker that leverages both point cloud and RGB information. Compared to prior work, it provides a standardized evaluation protocol and systematically assesses the potential of RGBD data for 3D tracking. The baseline achieves reasonable performance, serving as a reference for future research.
- **核心贡献**: 提出了首个大规模RGBD 3D跟踪基准和基线方法。
- **创新点**: 系统性地将RGBD信息引入3D跟踪评估体系。
- **结果**: 建立了基准并验证了基线方法的有效性。

### ByteTrack: Multi-object Tracking by Associating Every Detection Box. **⭐⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20047-2_1) · 📚 被引 2132
- **作者**: Yifu Zhang, Peize Sun, Yi Jiang, Dongdong Yu, Fucheng Weng, Zehuan Yuan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对多目标跟踪中低分检测框常被丢弃导致轨迹碎片化的问题。②提出了ByteTrack方法，通过关联每个检测框（包括低分框）来提升跟踪性能，采用简单的关联策略，先关联高置信度框，再关联低置信度框。③相比已有工作，该方法无需复杂的外观特征或运动模型，仅利用检测框的几何信息即可实现SOTA性能。④在MOT17和MOT20上分别达到80.3和77.8的MOTA，在MOT17上IDF1达到77.3，显著优于现有方法。
- **摘要（英）**: This paper tackles the issue of fragmented trajectories caused by discarding low-confidence detection boxes in multi-object tracking. ByteTrack is proposed to associate every detection box, including low-score ones, using a simple two-stage association strategy. Unlike prior methods, it relies solely on geometric information without complex appearance or motion models. It achieves state-of-the-art performance with 80.3 MOTA on MOT17 and 77.8 on MOT20, and 77.3 IDF1 on MOT17.
- **核心贡献**: 提出利用低分检测框的简单关联策略，显著提升多目标跟踪性能。
- **创新点**: 首次系统性地利用低置信度检测框进行轨迹关联。
- **结果**: 在MOT17和MOT20上取得SOTA结果。

### CMT: Context-Matching-Guided Transformer for 3D Tracking in Point Clouds. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20047-2_6) · 📚 被引 17
- **作者**: Zhiyang Guo, Yunyao Mao, Wengang Zhou, Min Wang, Houqiang Li
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对点云中3D目标跟踪在相似物体和遮挡场景下性能不佳的问题。②提出了CMT（Context-Matching-Guided Transformer）方法，利用上下文匹配模块增强模板与搜索区域的特征交互，并通过Transformer架构捕捉全局依赖。③相比已有方法，CMT通过上下文信息引导匹配，有效缓解了外观相似和遮挡带来的歧义。④在KITTI和nuScenes数据集上取得了领先的跟踪精度，尤其在挑战性场景下提升显著。
- **摘要（英）**: This paper addresses the performance degradation of 3D object tracking in point clouds under similar-object and occlusion scenarios. CMT is proposed, which uses a context-matching module to enhance feature interaction between template and search region, and a Transformer to capture global dependencies. Compared to prior methods, CMT leverages contextual information to guide matching, effectively reducing ambiguity. It achieves leading tracking accuracy on KITTI and nuScenes, with significant gains in challenging scenes.
- **核心贡献**: 提出上下文匹配引导的Transformer框架用于点云3D跟踪。
- **创新点**: 利用上下文信息增强匹配鲁棒性。
- **结果**: 在KITTI和nuScenes上取得领先精度。

### MOTCOM: The Multi-Object Tracking Dataset Complexity Metric. **⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2207.10031](https://arxiv.org/abs/2207.10031) · 📚 被引 4
- **作者**: Malte Pedersen, Joakim Bruslund Haurum, Patrick Dendorfer, Thomas B. Moeslund
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对多目标跟踪数据集缺乏统一复杂度度量指标的问题。②提出了MOTCOM（MOT数据集复杂度度量），结合遮挡、 erratic运动、视觉相似性三个子指标来综合描述序列复杂度。③相比传统的密度和轨迹数量，MOTCOM能更全面地反映跟踪难度。④在MOT17、MOT20和MOTSynth上评估，证明其能有效区分序列复杂度，有助于深入讨论跟踪器性能。
- **摘要（英）**: This paper addresses the lack of a comprehensive complexity metric for multi-object tracking datasets. MOTCOM is proposed, combining three sub-metrics: occlusion, erratic motion, and visual similarity. Compared to conventional density and track count, MOTCOM provides a more holistic measure of tracking difficulty. Evaluated on MOT17, MOT20, and MOTSynth, it effectively differentiates sequence complexity and facilitates nuanced performance analysis.
- **核心贡献**: 提出首个综合性的MOT数据集复杂度度量。
- **创新点**: 结合多维度子指标量化跟踪难度。
- **结果**: 在多个基准上验证了度量的有效性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> There exists no comprehensive metric for describing the complexity of Multi-Object Tracking (MOT) sequences. This lack of metrics decreases explainability, complicates comparison of datasets, and reduces the conversation on tracker performance to a matter of leader board position. As a remedy, we present the novel MOT dataset complexity metric (MOTCOM), which is a combination of three sub-metrics inspired by key problems in MOT: occlusion, erratic motion, and visual similarity. The insights of MOTCOM can open nuanced discussions on tracker performance and may lead to a wider acknowledgement of novel contributions developed for either less known datasets or those aimed at solving sub-problems. We evaluate MOTCOM on the comprehensive MOT17, MOT20, and MOTSynth datasets and show that MOTCOM is far better at describing the complexity of MOT sequences compared to the conventional density and number of tracks. Project page at https://vap.aau.dk/motcom

</details>

### Robust Multi-object Tracking by Marginal Inference. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2208.03727](https://arxiv.org/abs/2208.03727)
- **作者**: Yifu Zhang, Chunyu Wang, Xinggang Wang, Wenjun Zeng, Wenyu Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对多目标跟踪中固定阈值丢弃特征距离较大的目标对导致关联不稳定的问题。②提出了基于边际推断的高效方法，实时计算每对目标的边际概率作为归一化距离，替代原始特征距离。③相比已有方法，边际概率在不同视频间更稳定，因此可以使用统一阈值，且方法通用，可应用于现有跟踪器。④在MOT17和MOT20上取得竞争性结果，IDF1指标提升约1点，且概率输出更具可解释性。
- **摘要（英）**: This paper addresses the instability of fixed thresholds for discarding object pairs in multi-object tracking. An efficient marginal inference approach is proposed to compute a marginal probability for each pair in real time, serving as a normalized distance. This probability is more stable across videos, enabling a single threshold for all. The method is general and improves IDF1 by about one point on existing trackers, achieving competitive results on MOT17 and MOT20.
- **核心贡献**: 提出基于边际推断的归一化距离用于数据关联。
- **创新点**: 利用边际概率替代原始特征距离，提高阈值稳定性。
- **结果**: 在MOT基准上提升IDF1约1点。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-object tracking in videos requires to solve a fundamental problem of one-to-one assignment between objects in adjacent frames. Most methods address the problem by first discarding impossible pairs whose feature distances are larger than a threshold, followed by linking objects using Hungarian algorithm to minimize the overall distance. However, we find that the distribution of the distances computed from Re-ID features may vary significantly for different videos. So there isn't a single optimal threshold which allows us to safely discard impossible pairs. To address the problem, we present an efficient approach to compute a marginal probability for each pair of objects in real time. The marginal probability can be regarded as a normalized distance which is significantly more stable than the original feature distance. As a result, we can use a single threshold for all videos. The approach is general and can be applied to the existing trackers to obtain about one point improvement in terms of IDF1 metric. It achieves competitive results on MOT17 and MOT20 benchmarks. In addition, the computed probability is more interpretable which facilitates subsequent post-processing operations.

</details>

### AiATrack: Attention in Attention for Transformer Visual Tracking. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2207.09603](https://arxiv.org/abs/2207.09603) · 📚 被引 333
- **作者**: Shenyuan Gao, Chunluan Zhou, Chao Ma, Xinggang Wang, Junsong Yuan
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对Transformer跟踪器中注意力机制独立计算导致注意力权重噪声大、模糊的问题。②提出注意力中的注意力（AiA）模块，通过在所有相关向量中寻求共识来增强正确相关性、抑制错误相关性，并构建了AiATrack框架，引入高效特征复用和目标-背景嵌入以充分利用时间参考。③相比现有Transformer跟踪器，AiA模块可灵活应用于自注意力和交叉注意力块，且框架设计轻量高效。④在六个跟踪基准上达到最先进性能，同时保持实时运行速度。
- **摘要（英）**: This paper addresses noisy and ambiguous attention weights in Transformer trackers by proposing an attention-in-attention (AiA) module that seeks consensus among correlation vectors. The AiATrack framework integrates this module with efficient feature reuse and target-background embeddings, achieving state-of-the-art performance on six benchmarks at real-time speed.
- **核心贡献**: 提出AiA模块和AiATrack框架，显著提升Transformer跟踪器的准确性和鲁棒性。
- **创新点**: 通过注意力内注意力机制增强相关一致性，抑制噪声相关性。
- **结果**: 在六个跟踪基准上达到最先进性能，并保持实时速度。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Transformer trackers have achieved impressive advancements recently, where the attention mechanism plays an important role. However, the independent correlation computation in the attention mechanism could result in noisy and ambiguous attention weights, which inhibits further performance improvement. To address this issue, we propose an attention in attention (AiA) module, which enhances appropriate correlations and suppresses erroneous ones by seeking consensus among all correlation vectors. Our AiA module can be readily applied to both self-attention blocks and cross-attention blocks to facilitate feature aggregation and information propagation for visual tracking. Moreover, we propose a streamlined Transformer tracking framework, dubbed AiATrack, by introducing efficient feature reuse and target-background embeddings to make full use of temporal references. Experiments show that our tracker achieves state-of-the-art performance on six tracking benchmarks while running at a real-time speed.

</details>

### AvatarPoser: Articulated Full-Body Pose Tracking from Sparse Motion Sensing. **⭐⭐** (相关度: 30%)
- **链接**: [arXiv:2207.13784](https://arxiv.org/abs/2207.13784) · 📚 被引 117
- **作者**: Jiaxi Jiang, Paul Streli, Huajian Qiu, Andreas Fender, Larissa Laich, Patrick Snape et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对混合现实头显仅跟踪头部和手部姿态，无法估计全身姿态的问题。②提出AvatarPoser，首个仅利用头部和手部运动输入预测全身姿态的学习方法，基于Transformer编码器提取特征，并解耦全局运动与局部关节方向。③相比依赖额外传感器的方法，减少了设备复杂度，适用于移动场景。④实验表明能生成类似动作捕捉的准确全身运动，但摘要未提供具体数据。
- **摘要（英）**: This paper tackles full-body pose estimation from sparse head and hand inputs in mixed reality. AvatarPoser uses a Transformer encoder and decouples global motion from local joint orientations, eliminating the need for extra sensors and achieving accurate full-body poses.
- **核心贡献**: 提出首个仅用头部和手部输入预测全身姿态的方法。
- **创新点**: 解耦全局运动与局部关节方向，结合Transformer和逆运动学优化。
- **结果**: 生成准确的全身体姿态，但缺乏具体量化数据。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Today's Mixed Reality head-mounted displays track the user's head pose in world space as well as the user's hands for interaction in both Augmented Reality and Virtual Reality scenarios. While this is adequate to support user input, it unfortunately limits users' virtual representations to just their upper bodies. Current systems thus resort to floating avatars, whose limitation is particularly evident in collaborative settings. To estimate full-body poses from the sparse input sources, prior work has incorporated additional trackers and sensors at the pelvis or lower body, which increases setup complexity and limits practical application in mobile settings. In this paper, we present AvatarPoser, the first learning-based method that predicts full-body poses in world coordinates using only motion input from the user's head and hands. Our method builds on a Transformer encoder to extract deep features from the input signals and decouples global motion from the learned local joint orientations to guide pose estimation. To obtain accurate full-body motions that resemble motion capture animations, we refine the arm joints' positions using an optimization routine with inverse kinematics to match the original tracking input. In our evaluation, AvatarPoser achieved new state-of-the-art results in evaluations on large motion capture datasets (AMASS). At the same time, our method's inference speed supports real-time operation, providing a practical interface to support holistic avatar control and representation for Metaverse applications.

</details>

### Towards Sequence-Level Training for Visual Tracking. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2208.05810](https://arxiv.org/abs/2208.05810)
- **作者**: Minji Kim, Seungkwan Lee, Jungseul Ok, Bohyung Han, Minsu Cho
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对视觉跟踪中帧级训练与序列级测试不一致的问题。②提出基于强化学习的序列级训练策略，包括序列级数据采样、学习目标和数据增强设计。③相比传统帧级训练，该方法统一了训练和测试的数据分布与任务目标，且无需修改模型架构。④在LaSOT、TrackingNet和GOT-10k基准上，四种代表性跟踪器（SiamRPN++、SiamAttn、TransT、TrDiMP）均获得一致提升。
- **摘要（英）**: This paper addresses the train-test inconsistency in visual tracking by introducing a sequence-level training strategy based on reinforcement learning. It redesigns data sampling, objectives, and augmentation at the sequence level, consistently improving four representative trackers on standard benchmarks without architectural changes.
- **核心贡献**: 提出序列级训练策略，弥合跟踪任务中训练与测试的差距。
- **创新点**: 将强化学习应用于序列级训练，统一数据分布和任务目标。
- **结果**: 四种代表性跟踪器在多个基准上均获得一致性能提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite the extensive adoption of machine learning on the task of visual object tracking, recent learning-based approaches have largely overlooked the fact that visual tracking is a sequence-level task in its nature; they rely heavily on frame-level training, which inevitably induces inconsistency between training and testing in terms of both data distributions and task objectives. This work introduces a sequence-level training strategy for visual tracking based on reinforcement learning and discusses how a sequence-level design of data sampling, learning objectives, and data augmentation can improve the accuracy and robustness of tracking algorithms. Our experiments on standard benchmarks including LaSOT, TrackingNet, and GOT-10k demonstrate that four representative tracking models, SiamRPN++, SiamAttn, TransT, and TrDiMP, consistently improve by incorporating the proposed methods in training without modifying architectures.

</details>

### Robust Visual Tracking by Segmentation. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2203.11191](https://arxiv.org/abs/2203.11191)
- **作者**: Matthieu Paul, Martin Danelljan, Christoph Mayer, Luc Van Gool
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对视觉跟踪中边界框无法准确描述复杂形状目标的问题。②提出以分割为中心的跟踪流程，内部使用分割掩码而非边界框，并设计独立的实例定位组件来条件化分割解码器。③相比传统框中心跟踪器，能更好区分目标与背景，提升目标表示能力。④在LaSOT基准上达到最先进性能，成功AUC分数为69.7%。
- **摘要（英）**: This paper addresses the limitation of bounding boxes in tracking complex-shaped targets by proposing a segmentation-centric pipeline that internally uses masks. It introduces an instance localization component to condition the segmentation decoder, achieving state-of-the-art performance on LaSOT with a 69.7% AUC score.
- **核心贡献**: 提出分割中心的跟踪框架，提升复杂形状目标的跟踪精度。
- **创新点**: 内部使用分割掩码替代边界框，并引入实例定位组件。
- **结果**: 在LaSOT上达到最先进性能，AUC为69.7%。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Estimating the target extent poses a fundamental challenge in visual object tracking. Typically, trackers are box-centric and fully rely on a bounding box to define the target in the scene. In practice, objects often have complex shapes and are not aligned with the image axis. In these cases, bounding boxes do not provide an accurate description of the target and often contain a majority of background pixels. We propose a segmentation-centric tracking pipeline that not only produces a highly accurate segmentation mask, but also internally works with segmentation masks instead of bounding boxes. Thus, our tracker is able to better learn a target representation that clearly differentiates the target in the scene from background content. In order to achieve the necessary robustness for the challenging tracking scenario, we propose a separate instance localization component that is used to condition the segmentation decoder when producing the output mask. We infer a bounding box from the segmentation mask, validate our tracker on challenging tracking datasets and achieve the new state of the art on LaSOT with a success AUC score of 69.7%. Since most tracking datasets do not contain mask annotations, we cannot use them to evaluate predicted segmentation masks. Instead, we validate our segmentation quality on two popular video object segmentation datasets.

</details>

### Hierarchical Feature Embedding for Visual Tracking. **⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20047-2_25)
- **作者**: Zhixiong Pi, Weitao Wan, Chong Sun, Changxin Gao, Nong Sang, Chen Li
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①该论文标题为“Hierarchical Feature Embedding for Visual Tracking”，但摘要内容为空，无法获取具体问题、方法、改进和效果信息。②由于缺乏摘要，无法评估其技术贡献和实验验证。③建议查阅完整论文以了解其层次化特征嵌入方法。④当前信息不足以进行有效评估。
- **摘要（英）**: The abstract for this paper is empty, providing no information on the problem, method, or results. The hierarchical feature embedding approach cannot be assessed without further details.
- **核心贡献**: 未知，因摘要缺失。
- **创新点**: 未知，因摘要缺失。
- **结果**: 未知，因摘要缺失。

## 跨领域论文（完整笔记在其他领域）

- 3D Siamese Transformer Network for Single Object Tracking on Point Clouds. → [autonomous-driving](../autonomous-driving/Guideline%202022.md)
- PolarMOT: How Far Can Geometric Relations Take us in 3D Multi-object Tracking? → [3d-detection](../3d-detection/Guideline%202022.md)
- Sound Localization by Self-supervised Time Delay Estimation. → [multimodal](../multimodal/Guideline%202022.md)
