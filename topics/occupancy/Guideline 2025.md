# Occupancy — 2025 Guideline

> 领域: 占用栅格 / 占用网络（Occupancy Prediction / Occ3D）
> 论文数: 9 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份:

### Rethinking Temporal Fusion with a Unified Gradient Descent View for 3D Semantic Occupancy Prediction. **⭐⭐⭐⭐** (相关度: 92%)
- **链接**: [arXiv:2504.12959](https://arxiv.org/abs/2504.12959) · 📚 被引 4
- **作者**: Dubing Chen, Huan Zheng, Jin Fang, Xingping Dong, Xianfei Li, Wenlong Liao et al.
- **🏷️ 机构**: SKL-IOTSC, CIS, University of Macau, Wuhan University, Cowarobot Co. Ltd.
- **会议**: CVPR 2025
- **摘要（中）**: 针对视觉3D占用预测中时间融合未充分探索的问题，提出GDFusion方法，系统分析VisionOcc流程，识别场景级一致性、运动校准和几何补全三个时间线索，并通过重解释RNN公式，利用特征上的梯度下降统一融合异构时间信息。在nuScenes和Occ3D上，相比基线提升1.4%-4.8% mIoU，并减少27%-72%内存消耗。
- **摘要（英）**: To explore temporal fusion in vision-based 3D occupancy prediction, GDFusion identifies scene-level consistency, motion calibration, and geometric complementation as key temporal cues, and unifies their fusion via gradient descent on features by reinterpreting RNNs. It achieves 1.4%-4.8% mIoU improvements on Occ3D with 27%-72% memory reduction.
- **核心贡献**: 提出GDFusion，基于梯度下降统一时间线索融合的3D占用预测方法。
- **创新点**: 将RNN公式重解释为特征上的梯度下降，统一融合异构时间信息。
- **结果**: 在Occ3D上提升1.4%-4.8% mIoU，内存减少27%-72%。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present GDFusion, a temporal fusion method for vision-based 3D semantic occupancy prediction (VisionOcc). GDFusion opens up the underexplored aspects of temporal fusion within the VisionOcc framework, focusing on both temporal cues and fusion strategies. It systematically examines the entire VisionOcc pipeline, identifying three fundamental yet previously overlooked temporal cues: scene-level consistency, motion calibration, and geometric complementation. These cues capture diverse facets of temporal evolution and make distinct contributions across various modules in the VisionOcc framework. To effectively fuse temporal signals across heterogeneous representations, we propose a novel fusion strategy by reinterpreting the formulation of vanilla RNNs. This reinterpretation leverages gradient descent on features to unify the integration of diverse temporal information, seamlessly embedding the proposed temporal cues into the network. Extensive experiments on nuScenes demonstrate that GDFusion significantly outperforms established baselines. Notably, on Occ3D benchmark, it achieves 1.4\%-4.8\% mIoU improvements and reduces memory consumption by 27\%-72\%.

</details>

### GaussRender: Learning 3D Occupancy with Gaussian Rendering.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02507) · 📚 被引 2
- **作者**: Loïck Chambon, Eloi Zablocki, Alexandre Boulch, Mickaël Chen, Matthieu Cord
- **🏷️ 机构**: ValeoAI,Paris,France, Sorbonne University,Paris,France, Hcompany.ai,Paris,France
- **会议**: ICCV 2025

> We introduce GaussianOcc, a systematic method that investigates the two usages of Gaussian splatting for fully self-supervised and efficient 3D occupancy estimation in surround views. First, traditional methods for self-supervised 3D occupancy estimation still require ground truth 6D poses from sensors during training. To address this limitation, we propose Gaussian Splatting for Projection (GSP) module to provide accurate scale information for fully self-supervised training from adjacent view projection. Additionally, existing methods rely on volume rendering for final 3D voxel representation learning using 2D signals (depth maps, semantic maps), which is both time-consuming and less effective. We propose Gaussian Splatting from Voxel space (GSV) to leverage the fast rendering properties of Gaussian splatting. As a result, the proposed GaussianOcc method enables fully self-supervised (no ground truth pose) 3D occupancy estimation in competitive performance with low computational cost (2.7 times faster in training and 5 times faster in rendering). The relevant code is available in https://github.com/GANWANSHUI/GaussianOcc.git.

### QuadricFormer: Scene as Superquadrics for 3D Semantic Occupancy Prediction. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2506.10977](https://arxiv.org/abs/2506.10977)
- **作者**: Sicheng Zuo, Wenzhao Zheng, Xiaoyong Han, Longchao Yang, Yong Pan, Jiwen Lu
- **🏷️ 机构**: Tsinghua University, University of California, Berkeley, Li Auto Inc.
- **会议**: NeurIPS 2025
- **摘要（中）**: ①这篇论文针对现有3D语义占用预测方法使用密集体素表示导致计算效率低，以及基于高斯椭球的物体中心表示难以建模复杂几何结构的问题。②提出了使用超二次曲面（superquadrics）作为场景基元，并开发了概率超二次曲面混合模型，将每个超二次曲面解释为占用概率分布，通过概率混合计算语义。③相比高斯椭球，超二次曲面具有更丰富的几何表达能力，能用更少的基元建模立方体、圆柱体等多样形状，提高表示效率。④QuadricFormer在3D语义占用预测任务上实现了高效且准确的预测，但摘要中未提供具体数值。
- **摘要（英）**: This paper tackles inefficiency in dense voxel-based 3D occupancy prediction and the limited shape expressiveness of Gaussian ellipsoids. It introduces superquadrics as scene primitives with a probabilistic mixture model, enabling efficient representation of diverse geometries. QuadricFormer achieves efficient and accurate semantic occupancy prediction, though specific metrics are not detailed in the abstract.
- **核心贡献**: 提出基于超二次曲面的概率混合模型，用于高效3D语义占用预测。
- **创新点**: 利用超二次曲面的几何多样性替代高斯椭球，减少基元数量。
- **结果**: 在3D语义占用预测中实现高效准确的性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D occupancy prediction is crucial for robust autonomous driving systems as it enables comprehensive perception of environmental structures and semantics. Most existing methods employ dense voxel-based scene representations, ignoring the sparsity of driving scenes and resulting in inefficiency. Recent works explore object-centric representations based on sparse Gaussians, but their ellipsoidal shape prior limits the modeling of diverse structures. In real-world driving scenes, objects exhibit rich geometries (e.g., cuboids, cylinders, and irregular shapes), necessitating excessive ellipsoidal Gaussians densely packed for accurate modeling, which leads to inefficient representations. To address this, we propose to use geometrically expressive superquadrics as scene primitives, enabling efficient representation of complex structures with fewer primitives through their inherent shape diversity. We develop a probabilistic superquadric mixture model, which interprets each superquadric as an occupancy probability distribution with a corresponding geometry prior, and calculates semantics through probabilistic mixture. Building on this, we present QuadricFormer, a superquadric-based model for efficient 3D occupancy prediction, and introduce a pruning-and-splitting module to further enhance modeling efficiency by concentrating superquadrics in occupied regions. Extensive experiments on the nuScenes dataset demonstrate that QuadricFormer achieves state-of-the-art performance while maintaining superior efficiency.

</details>

### EvOcc: Accurate Semantic Occupancy for Automated Driving Using Evidence Theory. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Kalble_EvOcc_Accurate_Semantic_Occupancy_for_Automated_Driving_Using_Evidence_Theory_CVPR_2025_paper.html) · 📚 被引 1
- **作者**: Jonas Kälble, Sascha Wirges, Maxim Tatarchenko, Eddy Ilg
- **🏷️ 机构**: Bosch Center for Artificial Intelligence, University of Technology Nuremberg
- **会议**: CVPR 2025
- **摘要（中）**: 针对自动驾驶中语义占用预测的不确定性问题，该论文提出EvOcc，利用证据理论（Dempster-Shafer）来建模每个体素的语义类别不确定性。方法通过证据神经网络输出多类别证据，并融合多视角特征，生成更可靠的语义占用结果。相比传统softmax分类，证据理论能显式处理未知和冲突信息，提升预测的鲁棒性。在公开数据集上，EvOcc在语义占用精度和不确定性校准方面均优于基线方法。
- **摘要（英）**: This paper tackles uncertainty in semantic occupancy prediction for autonomous driving by introducing EvOcc, which applies evidence theory to model per-voxel semantic uncertainty. It uses an evidential neural network to output multi-class evidence and fuses multi-view features for reliable occupancy results. Compared to softmax-based methods, evidence theory explicitly handles unknown and conflicting information, improving robustness. Experiments on public datasets show superior accuracy and uncertainty calibration over baselines.
- **核心贡献**: 提出基于证据理论的语义占用预测方法，显式建模不确定性。
- **创新点**: 利用Dempster-Shafer理论替代softmax，增强对未知类别的处理能力。
- **结果**: 在精度和不确定性校准上优于基线。

### OccMamba: Semantic Occupancy Prediction with State Space Models. **⭐⭐⭐⭐** (相关度: 88%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Li_OccMamba_Semantic_Occupancy_Prediction_with_State_Space_Models_CVPR_2025_paper.html) · 📚 被引 11
- **作者**: Heng Li, Yuenan Hou, Xiaohan Xing, Yuexin Ma, Xiao Sun, Yanyong Zhang
- **🏷️ 机构**: University of Science and Technology of China, Shanghai AI Laboratory, Stanford University
- **会议**: CVPR 2025
- **摘要（中）**: 针对3D语义占用预测中长距离依赖建模和计算效率的挑战，该论文提出OccMamba，将状态空间模型（如Mamba）应用于占用预测。方法利用Mamba的线性复杂度特性，高效处理3D体素序列，捕捉全局上下文信息。相比基于Transformer的方法，OccMamba在保持高精度的同时大幅降低计算量。在Occ3D-nuScenes等基准上，该方法取得了领先的性能，验证了状态空间模型在3D感知中的潜力。
- **摘要（英）**: This paper addresses long-range dependency modeling and computational efficiency in 3D semantic occupancy prediction by proposing OccMamba, which applies state space models like Mamba. It efficiently processes 3D voxel sequences with linear complexity, capturing global context. Compared to Transformer-based methods, OccMamba reduces computation while maintaining high accuracy. It achieves leading performance on benchmarks like Occ3D-nuScenes, demonstrating the potential of state space models in 3D perception.
- **核心贡献**: 首次将Mamba架构用于3D语义占用预测。
- **创新点**: 利用状态空间模型的线性复杂度实现高效全局建模。
- **结果**: 在多个基准上取得领先性能并降低计算成本。

### STCOcc: Sparse Spatial-Temporal Cascade Renovation for 3D Occupancy and Scene Flow Prediction. **⭐⭐⭐** (相关度: 80%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Liao_STCOcc_Sparse_Spatial-Temporal_Cascade_Renovation_for_3D_Occupancy_and_Scene_CVPR_2025_paper.html) · 📚 被引 5
- **作者**: Zhimin Liao, Ping Wei, Shuaijia Chen, Haoxuan Wang, Ziyang Ren
- **🏷️ 机构**: Xi&#x2019;an Jiaotong University,National Key Laboratory of Human-Machine Hybrid Augmented Intelligence Institute of Artificial Intelligence and Robotics
- **会议**: CVPR 2025
- **摘要（中）**: 针对3D占用预测和场景流估计的联合任务，该论文提出STCOcc，通过稀疏时空级联修复机制来提升预测精度。方法利用稀疏表示和时序信息，在空间和时间维度上逐步修复占用和场景流。相比独立处理两个任务的方法，STCOcc实现了联合优化，增强了动态场景的理解。在相关数据集上，该方法在占用和场景流指标上均表现出改进。
- **摘要（英）**: This paper addresses joint 3D occupancy prediction and scene flow estimation by proposing STCOcc, which uses sparse spatial-temporal cascade renovation. It leverages sparse representations and temporal information to iteratively refine occupancy and scene flow. Compared to separate task handling, STCOcc enables joint optimization, improving dynamic scene understanding. Experiments on relevant datasets show improvements in both occupancy and scene flow metrics.
- **核心贡献**: 提出稀疏时空级联修复框架，联合预测占用和场景流。
- **创新点**: 通过级联修复机制融合时空信息，实现任务协同。
- **结果**: 在占用和场景流指标上均有提升。

### 3D Occupancy Prediction with Low-Resolution Queries via Prototype-aware View Transformation. **⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2503.15185](https://arxiv.org/abs/2503.15185) · 📚 被引 1
- **作者**: Gyeongrok Oh, Sungjune Kim, Heeju Ko, Hyung-gun Chi, Jinkyu Kim, Dongwook Lee et al.
- **🏷️ 机构**: Korea University, Purdue University, Samsung Electronics,AI Center, DS Division
- **会议**: CVPR 2025
- **摘要（中）**: 针对相机3D占用预测中低分辨率体素查询导致信息丢失的问题，提出ProtoOcc方法。通过聚类图像段原型并在视图变换中映射到3D体素查询，编码高层视觉几何并补充空间信息。设计多视角解码策略解耦压缩视觉线索。在Occ3D和SemanticKITTI基准上验证了有效性，并取得竞争性结果。
- **摘要（英）**: To address information loss from low-resolution voxel queries in camera-based 3D occupancy prediction, ProtoOcc leverages prototypes of clustered image segments in view transformation to encode high-level geometry. A multi-perspective decoding strategy disentangles compressed cues. Experiments on Occ3D and SemanticKITTI show clear improvements over baselines.
- **核心贡献**: 提出原型感知视图变换增强低分辨率占用预测。
- **创新点**: 利用图像段原型映射到3D查询以补充空间信息。
- **结果**: 在多个基准上取得性能提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The resolution of voxel queries significantly influences the quality of view transformation in camera-based 3D occupancy prediction. However, computational constraints and the practical necessity for real-time deployment require smaller query resolutions, which inevitably leads to an information loss. Therefore, it is essential to encode and preserve rich visual details within limited query sizes while ensuring a comprehensive representation of 3D occupancy. To this end, we introduce ProtoOcc, a novel occupancy network that leverages prototypes of clustered image segments in view transformation to enhance low-resolution context. In particular, the mapping of 2D prototypes onto 3D voxel queries encodes high-level visual geometries and complements the loss of spatial information from reduced query resolutions. Additionally, we design a multi-perspective decoding strategy to efficiently disentangle the densely compressed visual cues into a high-dimensional 3D occupancy scene. Experimental results on both Occ3D and SemanticKITTI benchmarks demonstrate the effectiveness of the proposed method, showing clear improvements over the baselines. More importantly, ProtoOcc achieves competitive performance against the baselines even with 75\% reduced voxel resolution.

</details>

### GaussianWorld: Gaussian World Model for Streaming 3D Occupancy Prediction. **⭐⭐⭐⭐** (相关度: 93%)
- **链接**: [arXiv:2412.10373](https://arxiv.org/abs/2412.10373) · 📚 被引 13
- **作者**: Sicheng Zuo, Wenzhao Zheng, Yuanhui Huang, Jie Zhou, Jiwen Lu
- **🏷️ 机构**: Tsinghua University,Department of Automation,China
- **会议**: CVPR 2025
- **摘要（中）**: 针对现有3D占用预测忽略场景连续性和演化先验的问题，提出GaussianWorld框架，将占用预测重构为4D占用预测问题，分解场景演化为自车运动对齐、动态物体局部运动和新增场景补全三个因素，并在3D高斯空间中显式利用这些先验。在nuScenes上，相比单帧方法提升超过2% mIoU，且不引入额外计算。
- **摘要（英）**: To exploit scene continuity in 3D occupancy prediction, GaussianWorld reformulates it as 4D forecasting, decomposing evolution into ego-motion alignment, dynamic object movement, and scene completion, and infers evolution in 3D Gaussian space. It improves mIoU by over 2% over single-frame counterparts on nuScenes without extra computation.
- **核心贡献**: 提出GaussianWorld，基于世界模型的流式3D占用预测框架。
- **创新点**: 将占用预测重构为4D预测，分解场景演化因素并在高斯空间建模。
- **结果**: 在nuScenes上提升超过2% mIoU，且无额外计算开销。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D occupancy prediction is important for autonomous driving due to its comprehensive perception of the surroundings. To incorporate sequential inputs, most existing methods fuse representations from previous frames to infer the current 3D occupancy. However, they fail to consider the continuity of driving scenarios and ignore the strong prior provided by the evolution of 3D scenes (e.g., only dynamic objects move). In this paper, we propose a world-model-based framework to exploit the scene evolution for perception. We reformulate 3D occupancy prediction as a 4D occupancy forecasting problem conditioned on the current sensor input. We decompose the scene evolution into three factors: 1) ego motion alignment of static scenes; 2) local movements of dynamic objects; and 3) completion of newly-observed scenes. We then employ a Gaussian world model (GaussianWorld) to explicitly exploit these priors and infer the scene evolution in the 3D Gaussian space considering the current RGB observation. We evaluate the effectiveness of our framework on the widely used nuScenes dataset. Our GaussianWorld improves the performance of the single-frame counterpart by over 2% in mIoU without introducing additional computations. Code: https://github.com/zuosc19/GaussianWorld.

</details>

### GaussianFormer-2: Probabilistic Gaussian Superposition for Efficient 3D Occupancy Prediction. **⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Huang_GaussianFormer-2_Probabilistic_Gaussian_Superposition_for_Efficient_3D_Occupancy_Prediction_CVPR_2025_paper.html) · 📚 被引 18
- **作者**: Yuanhui Huang, Amonnut Thammatadatrakoon, Wenzhao Zheng, Yunpeng Zhang, Dalong Du, Jiwen Lu
- **🏷️ 机构**: Tsinghua University,Department of Automation, Phigent Robotics
- **会议**: CVPR 2025
- **摘要（中）**: 针对现有3D占用预测方法在计算效率和精度上的不足，该论文提出GaussianFormer-2，利用概率高斯叠加来高效表示3D场景。方法通过预测一组概率高斯分布，并采用叠加策略生成占用场，避免了传统体素表示的密集计算。相比先前工作，它显著降低了计算开销，同时保持了高精度。在公开数据集上，该方法在效率和精度之间取得了更好的平衡，验证了其有效性。
- **摘要（英）**: This paper addresses the inefficiency and accuracy limitations of existing 3D occupancy prediction methods by proposing GaussianFormer-2, which employs probabilistic Gaussian superposition for efficient scene representation. It predicts a set of probabilistic Gaussians and aggregates them to form the occupancy field, avoiding dense voxel computations. Compared to prior work, it substantially reduces computational cost while maintaining high accuracy, achieving a better efficiency-accuracy trade-off on public benchmarks.
- **核心贡献**: 提出基于概率高斯叠加的高效3D占用预测框架。
- **创新点**: 利用高斯分布叠加替代传统体素表示，实现稀疏高效建模。
- **结果**: 在公开数据集上实现了更优的效率与精度平衡。

### MergeOcc: Bridge the Domain Gap between Different Lidars for Robust Occupancy Prediction. **⭐⭐⭐** (相关度: 85%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02463)
- **作者**: Zikun Xu, Shaobing Xu
- **🏷️ 机构**: Tsinghua University,China
- **会议**: ICCV 2025
- **摘要（中）**: ①针对不同LiDAR传感器（如机械式与固态式）在点云分布、密度和范围上的差异，导致占用预测模型跨传感器泛化性能差的问题。②提出了MergeOcc方法，通过设计域自适应模块，在特征层面对齐不同LiDAR的点云表示，并利用跨传感器数据增强策略进行训练。③相比现有仅针对单一传感器或简单拼接的方法，MergeOcc显式建模了传感器间的域差异，并利用多传感器数据互补性提升鲁棒性。④在多个LiDAR数据集上的实验表明，该方法显著缩小了跨传感器性能差距，但摘要未提供具体数值。
- **摘要（英）**: This paper addresses the domain gap in occupancy prediction caused by different LiDAR sensors. It proposes MergeOcc, which aligns point cloud features across sensors via domain adaptation and cross-sensor augmentation. The method improves cross-sensor generalization, though specific quantitative results are not provided in the abstract.
- **核心贡献**: 提出了一种跨LiDAR传感器的域自适应占用预测框架。
- **创新点**: 在特征层面显式对齐不同LiDAR传感器的点云分布。
- **结果**: 在跨传感器场景下提升了占用预测的鲁棒性。

### AGO: Adaptive Grounding for Open World 3D Occupancy Prediction. **⭐⭐⭐** (相关度: 80%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00809) · 📚 被引 3
- **作者**: Peizheng Li, Shuxiao Ding, You Zhou, Qingwen Zhang, Onat Inak, Larissa Triess et al.
- **🏷️ 机构**: Mercedes-Benz AG, Sindelfingen, RPL, KTH Royal Institute of Technology
- **会议**: ICCV 2025
- **摘要（中）**: ①针对开放世界3D占用预测中，模型难以识别和预测未知类别物体的问题。②提出了AGO（Adaptive Grounding）方法，通过引入自适应接地机制，利用语言或视觉基础模型的知识来识别未知类别，并动态调整预测头。③相比传统封闭集占用预测，AGO能够处理训练中未出现的类别，提升了模型的开放世界感知能力。④摘要未提供具体实验数据，但声称在开放世界场景下具有优越性。
- **摘要（英）**: This work tackles open-world 3D occupancy prediction, where models fail on unseen object categories. It proposes AGO with adaptive grounding to leverage foundation model knowledge for unknown class identification. The method enhances open-world generalization, though no quantitative results are given in the abstract.
- **核心贡献**: 提出了开放世界3D占用预测的自适应接地方法。
- **创新点**: 利用基础模型知识实现未知类别的动态识别与预测。
- **结果**: 在开放世界场景下提升了未知类别的预测能力。

### CSV-Occ: Fusing Multi-frame Alignment for Occupancy Prediction with Temporal Cross State Space Model and Central Voting Mechanism. **⭐⭐⭐** (相关度: 82%)
- **链接**: [出版页](https://proceedings.mlr.press/v267/zhu25ah.html)
- **作者**: Ziming Zhu, Yu Zhu, Jiahao Chen, Xiaofeng Ling, Huanlei Chen, Lihua Sun
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025
- **摘要（中）**: ①针对多帧信息融合在占用预测中时序建模不足和特征对齐不准确的问题。②提出了CSV-Occ，结合时间跨状态空间模型（Temporal Cross State Space Model）和中心投票机制（Central Voting Mechanism），用于多帧对齐和特征融合。③相比传统基于注意力的时序融合方法，CSV-Occ在长时序建模上更高效，并通过中心投票增强了几何一致性。④摘要未提供具体实验数据，但声称在占用预测任务上取得了改进。
- **摘要（英）**: This paper addresses insufficient temporal modeling and inaccurate feature alignment in multi-frame occupancy prediction. It proposes CSV-Occ with a temporal cross state space model and central voting mechanism for improved fusion. The method claims enhanced performance, though no quantitative results are provided in the abstract.
- **核心贡献**: 提出了结合状态空间模型和投票机制的多帧占用预测方法。
- **创新点**: 利用跨状态空间模型进行高效时序建模。
- **结果**: 在占用预测任务上声称有改进。

### ODG: Occupancy Prediction Using Dual Gaussians. **⭐⭐⭐** (相关度: 85%)
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/2e14be0332c04c76742710e417cedb2a-Abstract-Conference.html)
- **作者**: Yunxiao Shi, Yinhao Zhu, Herbert Cai, Shizhong Han, Jisoo Jeong, Amin Ansari et al.
- **🏷️ 机构**: Qualcomm AI Research, Qualcomm, Qualcomm Technologies, Inc.
- **会议**: NeurIPS 2025
- **摘要（中）**: ①针对现有占用预测方法在表示3D场景时精度和效率难以平衡的问题。②提出了ODG（Occupancy Prediction using Dual Gaussians），利用双高斯表示来建模场景中的静态和动态部分，分别优化几何和语义特征。③相比单高斯或体素表示，双高斯方法能够更灵活地捕捉不同物体的形状和运动特性。④摘要未提供具体实验数据，但声称在精度和效率上优于现有方法。
- **摘要（英）**: This paper addresses the trade-off between accuracy and efficiency in occupancy prediction. It proposes ODG using dual Gaussian representations to model static and dynamic scene parts separately. The method claims superior performance, though no quantitative results are given in the abstract.
- **核心贡献**: 提出了双高斯表示用于占用预测。
- **创新点**: 分别用双高斯建模静态和动态场景。
- **结果**: 声称在精度和效率上优于现有方法。

### Dynamic Focused Masking for Autoregressive Embodied Occupancy Prediction. **⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/ec3d49763c653ad7c8d587f52220c129-Abstract-Conference.html)
- **作者**: Yuan Sun, Julio Contreras, Jorge Ortiz
- **🏷️ 机构**: Sichuan University, Rutgers University
- **会议**: NeurIPS 2025
- **摘要（中）**: ①该论文针对自回归式具身占用预测中，传统随机掩码策略未能有效利用场景结构信息，导致预测效率与准确性不足的问题。②提出了一种动态聚焦掩码（Dynamic Focused Masking）方法，通过自适应地选择高信息量的区域进行掩码，引导模型关注关键空间结构。③相比现有固定或随机掩码策略，该方法能根据预测进度动态调整掩码位置，更好地平衡学习难度与信息利用。④实验表明，该方法在占用预测任务上显著提升了预测精度，并加快了收敛速度（具体数据未在摘要中提供）。
- **摘要（英）**: This paper addresses the inefficiency of random masking in autoregressive embodied occupancy prediction by proposing Dynamic Focused Masking, which adaptively selects informative regions for masking. It improves over static masking by dynamically adjusting focus during generation, enhancing prediction accuracy and convergence speed.
- **核心贡献**: 提出动态聚焦掩码机制，提升自回归占用预测的准确性与效率。
- **创新点**: 将掩码策略从静态随机转为动态聚焦，实现自适应信息选择。
- **结果**: 在占用预测任务上提升精度并加速收敛。

### See through the Dark: Learning Illumination-affined Representations for Nighttime Occupancy Prediction. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2505.20641](https://arxiv.org/abs/2505.20641) · 📚 被引 1
- **作者**: Yuan Wu, Zhiqiang Yan, Yigong Zhang, Xiang Li, Jian Yang
- **🏷️ 机构**: Nanjing University of Science and Technology, National University of Singapore, Nankai University
- **会议**: NeurIPS 2025
- **摘要（中）**: 针对夜间占用预测中可见度低和光照不均的问题，提出LIAR框架，学习光照仿射表示。首先引入选择性低光增强模块，利用白天光照先验判断夜间图像是否真正黑暗，实现针对性增强；然后基于光照图设计2D光照引导采样和3D光照驱动投影，分别处理局部欠曝和过曝。相比现有方法，LIAR有效提升夜间场景的占用预测精度。实验在夜间基准上显著优于基线。
- **摘要（英）**: LIAR tackles nighttime occupancy prediction by learning illumination-affined representations with selective low-light enhancement and illumination-guided sampling/projection. It significantly improves accuracy on nighttime benchmarks.
- **核心贡献**: 提出光照仿射表示学习框架，增强夜间占用预测。
- **创新点**: 利用光照先验和引导采样处理局部光照不均。
- **结果**: 在夜间占用预测基准上取得显著提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Occupancy prediction aims to estimate the 3D spatial distribution of occupied regions along with their corresponding semantic labels. Existing vision-based methods perform well on daytime benchmarks but struggle in nighttime scenarios due to limited visibility and challenging lighting conditions. To address these challenges, we propose LIAR, a novel framework that learns illumination-affined representations. LIAR first introduces Selective Low-light Image Enhancement (SLLIE), which leverages the illumination priors from daytime scenes to adaptively determine whether a nighttime image is genuinely dark or sufficiently well-lit, enabling more targeted global enhancement. Building on the illumination maps generated by SLLIE, LIAR further incorporates two illumination-aware components: 2D Illumination-guided Sampling (2D-IGS) and 3D Illumination-driven Projection (3D-IDP), to respectively tackle local underexposure and overexposure. Specifically, 2D-IGS modulates feature sampling positions according to illumination maps, assigning larger offsets to darker regions and smaller ones to brighter regions, thereby alleviating feature degradation in underexposed areas. Subsequently,3D-IDP enhances semantic understanding in overexposed regions by constructing illumination intensity fields and supplying refined residual queries to the BEV context refinement process. Extensive experiments on both real and synthetic datasets demonstrate the superior performance of LIAR under challenging nighttime scenarios. The source code and pretrained models are available [here](https://github.com/yanzq95/LIAR).

</details>

### RLGF: Reinforcement Learning with Geometric Feedback for Autonomous Driving Video Generation. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2509.16500](https://arxiv.org/abs/2509.16500)
- **作者**: Tianyi Yan, Wencheng Han, Xia Zhou, Xueyang Zhang, Kun Zhan, Cheng-Zhong Xu et al.
- **🏷️ 机构**: University of Macau, Li Auto Inc., LiAuto
- **会议**: NeurIPS 2025
- **摘要（中）**: ①该论文针对自动驾驶视频生成模型中存在的几何失真问题，这些失真虽不影响视觉真实性，但严重降低了下游3D检测性能。②提出强化学习与几何反馈（RLGF）方法，利用潜在空间中的AD感知模型提供奖励，通过潜在空间窗口优化和分层几何奖励（点-线-面对齐、场景占用一致性）来微调视频扩散模型。③相比仅优化视觉质量的现有方法，RLGF首次将几何感知反馈融入扩散模型训练，并引入GeoScores量化失真。④在nuScenes上，RLGF将DiVE模型的VP误差降低21%、深度误差降低57%，3D检测mAP提升12.7%，显著缩小了与真实数据的性能差距。
- **摘要（英）**: This paper addresses geometric distortions in autonomous driving video generation that degrade downstream 3D detection performance. It proposes RLGF, which refines video diffusion models using rewards from latent-space AD perception models, incorporating windowing optimization and hierarchical geometric rewards. On nuScenes, RLGF reduces VP error by 21% and depth error by 57%, and improves 3D detection mAP by 12.7%, narrowing the gap to real data.
- **核心贡献**: 提出RLGF框架，通过几何反馈强化学习优化视频生成模型，提升下游3D检测性能。
- **创新点**: 将AD感知模型的几何奖励融入扩散模型训练，并设计分层几何奖励机制。
- **结果**: 在nuScenes上大幅降低几何误差并提升3D检测mAP。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Synthetic data is crucial for advancing autonomous driving (AD) systems, yet current state-of-the-art video generation models, despite their visual realism, suffer from subtle geometric distortions that limit their utility for downstream perception tasks. We identify and quantify this critical issue, demonstrating a significant performance gap in 3D object detection when using synthetic versus real data. To address this, we introduce Reinforcement Learning with Geometric Feedback (RLGF), RLGF uniquely refines video diffusion models by incorporating rewards from specialized latent-space AD perception models. Its core components include an efficient Latent-Space Windowing Optimization technique for targeted feedback during diffusion, and a Hierarchical Geometric Reward (HGR) system providing multi-level rewards for point-line-plane alignment, and scene occupancy coherence. To quantify these distortions, we propose GeoScores. Applied to models like DiVE on nuScenes, RLGF substantially reduces geometric errors (e.g., VP error by 21\%, Depth error by 57\%) and dramatically improves 3D object detection mAP by 12.7\%, narrowing the gap to real-data performance. RLGF offers a plug-and-play solution for generating geometrically sound and reliable synthetic videos for AD development.

</details>

## 跨领域论文（完整笔记在其他领域）

- TopNet: Transformer-Efficient Occupancy Prediction Network for Octree-Structured Point Cloud Geometry Compression. → [network-pruning](../network-pruning/Guideline%202025.md)
- SDGOCC: Semantic and Depth-Guided Bird's-Eye View Transformation for 3D Multimodal Occupancy Prediction. → [multimodal](../multimodal/Guideline%202025.md)
- VisionPAD: A Vision-Centric Pre-training Paradigm for Autonomous Driving. → [object-detection](../object-detection/Guideline%202025.md)
- GaussTR: Foundation Model-Aligned Gaussian Transformer for Self-Supervised 3D Spatial Understanding. → [self-supervised-vision](../self-supervised-vision/Guideline%202025.md)
- SINR: Sparsity Driven Compressed Implicit Neural Representations. → [network-pruning](../network-pruning/Guideline%202025.md)
- GaussianOcc: Fully Self-Supervised and Efficient 3D Occupancy Estimation with Gaussian Splatting. → [self-supervised-vision](../self-supervised-vision/Guideline%202025.md)
- Semi-Supervised Vision-Centric 3D Occupancy World Model for Autonomous Driving. → [self-supervised-vision](../self-supervised-vision/Guideline%202025.md)
- SQS: Enhancing Sparse Perception Models via Query-based Splatting in Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202025.md)

<!-- COMPLETE v1 papers=16 -->
