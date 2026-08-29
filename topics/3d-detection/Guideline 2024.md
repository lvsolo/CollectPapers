# 3D Detection — 2024 Guideline

> 领域: 3D 目标检测（LiDAR / 相机 / 多模态融合）
> 论文数: 27 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### V-DETR: DETR with Vertex Relative Position Encoding for 3D Object Detection.
- **链接**: [arXiv:2308.04409](https://arxiv.org/abs/2308.04409) · [代码](https://github.com/yichaoshen-MS/V-DETR)
- **作者**: Yichao Shen, Zigang Geng, Yuhui Yuan, Yutong Lin, Ze Liu, Chunyu Wang et al.
- **🏷️ 机构**: XJTU
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Autonomous driving stands as a pivotal domain in computer vision, shaping the future of transportation. Within this paradigm, the backbone of the system plays a crucial role in interpreting the complex environment. However, a notable challenge has been the loss of clear supervision when it comes to Bird's Eye View elements. To address this limitation, we introduce CLIP-BEVFormer, a novel approach that leverages the power of contrastive learning techniques to enhance the multi-view image-derived BEV backbones with ground truth information flow. We conduct extensive experiments on the challenging nuScenes dataset and showcase significant and consistent improvements over the SOTA. Specifically, CLIP-BEVFormer achieves an impressive 8.5\% and 9.2\% enhancement in terms of NDS and mAP, respectively, over the previous best BEV model on the 3D object detection task.

</details>

### Cam4DOcc: Benchmark for Camera-Only 4D Occupancy Forecasting in Autonomous Driving Applications. **⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2311.17663](https://arxiv.org/abs/2311.17663) · 📚 被引 35
- **作者**: Junyi Ma, Xieyuanli Chen, Jiawei Huang, Jingyi Xu, Zhen Luo, Jintao Xu et al.
- **🏷️ 机构**: Shanghai Jiao Tong University,IRMV Lab,Department of Automation, College of Intelligence Science and Technology, National University of Defense Technology, HAOMO.AI
- **会议**: CVPR 2024
- **摘要（中）**: 针对现有相机-only占用估计方法仅能表示当前3D空间、无法预测未来环境变化的问题，提出了Cam4DOcc基准，用于相机-only 4D占用预测。该基准基于nuScenes、nuScenes-Occupancy和Lyft-Level5等多个公开数据集构建，提供连续占用状态和3D后向向心流。引入了四种基线方法，包括静态世界占用模型、点云体素化等，以支持全面比较。该工作为自动驾驶中的时空占用预测提供了标准化评估平台。
- **摘要（英）**: To address the limitation of existing camera-only occupancy estimation methods that only represent the current 3D space without predicting future changes, this paper proposes Cam4DOcc, a benchmark for camera-only 4D occupancy forecasting. Built on multiple public datasets, it provides sequential occupancy states and 3D backward centripetal flow, along with four baseline implementations for comprehensive comparison. This work establishes a standardized evaluation platform for spatiotemporal occupancy prediction in autonomous driving.
- **核心贡献**: 提出了首个相机-only 4D占用预测基准及多种基线方法。
- **创新点**: 将占用估计从当前时刻扩展到未来时空预测，并引入3D流信息。
- **结果**: 提供了全面的基准和基线，支持未来研究比较。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Understanding how the surrounding environment changes is crucial for performing downstream tasks safely and reliably in autonomous driving applications. Recent occupancy estimation techniques using only camera images as input can provide dense occupancy representations of large-scale scenes based on the current observation. However, they are mostly limited to representing the current 3D space and do not consider the future state of surrounding objects along the time axis. To extend camera-only occupancy estimation into spatiotemporal prediction, we propose Cam4DOcc, a new benchmark for camera-only 4D occupancy forecasting, evaluating the surrounding scene changes in a near future. We build our benchmark based on multiple publicly available datasets, including nuScenes, nuScenes-Occupancy, and Lyft-Level5, which provides sequential occupancy states of general movable and static objects, as well as their 3D backward centripetal flow. To establish this benchmark for future research with comprehensive comparisons, we introduce four baseline types from diverse camera-based perception and prediction implementations, including a static-world occupancy model, voxelization of point cloud prediction, 2D-3D instance-based prediction, and our proposed novel end-to-end 4D occupancy forecasting network. Furthermore, the standardized evaluation protocol for preset multiple tasks is also provided to compare the performance of all the proposed baselines on present and future occupancy estimation with respect to objects of interest in autonomous driving scenarios. The dataset and our implementation of all four baselines in the proposed Cam4DOcc benchmark will be released here: https://github.com/haomo-ai/Cam4DOcc.

</details>

### Enhancing 3D Object Detection with 2D Detection-Guided Query Anchors. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2403.06093](https://arxiv.org/abs/2403.06093) · 📚 被引 13
- **作者**: Haoxuanye Ji, Pengpeng Liang, Erkang Cheng
- **🏷️ 机构**: Nullmax, School of Computer and Artificial Intelligence, Zhengzhou University
- **会议**: CVPR 2024
- **摘要（中）**: 针对多相机3D检测在远距离区域性能不佳的问题，提出了QAF2D方法，从2D检测结果生成3D查询锚点。该方法将2D框提升为3D锚点，并通过投影验证有效性，同时共享图像特征提取骨干。集成到多个查询-based 3D检测器中，显著提升性能。
- **摘要（英）**: This paper proposes QAF2D to improve query-based 3D object detection by generating 3D query anchors from 2D detection results. It lifts 2D boxes to 3D anchors, validates them via projection, and shares the backbone with prompt parameters. Integration into three popular detectors shows significant performance gains.
- **核心贡献**: 提出了QAF2D，从2D检测结果生成3D查询锚点以增强3D检测。
- **创新点**: 利用2D检测的可靠性，通过投影验证生成有效3D锚点。
- **结果**: 集成到多个3D检测器中，性能显著提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-camera-based 3D object detection has made notable progress in the past several years. However, we observe that there are cases (e.g. faraway regions) in which popular 2D object detectors are more reliable than state-of-the-art 3D detectors. In this paper, to improve the performance of query-based 3D object detectors, we present a novel query generating approach termed QAF2D, which infers 3D query anchors from 2D detection results. A 2D bounding box of an object in an image is lifted to a set of 3D anchors by associating each sampled point within the box with depth, yaw angle, and size candidates. Then, the validity of each 3D anchor is verified by comparing its projection in the image with its corresponding 2D box, and only valid anchors are kept and used to construct queries. The class information of the 2D bounding box associated with each query is also utilized to match the predicted boxes with ground truth for the set-based loss. The image feature extraction backbone is shared between the 3D detector and 2D detector by adding a small number of prompt parameters. We integrate QAF2D into three popular query-based 3D object detectors and carry out comprehensive evaluations on the nuScenes dataset. The largest improvement that QAF2D can bring about on the nuScenes validation subset is $2.3\%$ NDS and $2.7\%$ mAP. Code is available at https://github.com/nullmax-vision/QAF2D.

</details>

### SeaBird: Segmentation in Bird's View with Dice Loss Improves Monocular 3D Detection of Large Objects. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2403.20318](https://arxiv.org/abs/2403.20318) · 📚 被引 11
- **作者**: Abhinav Kumar, Yuliang Guo, Xinyu Huang, Liu Ren, Xiaoming Liu
- **🏷️ 机构**: Michigan State University, Bosch Research North America, Bosch Center for AI
- **会议**: CVPR 2024
- **摘要（中）**: 针对单目3D检测在大物体上性能下降的问题，指出深度回归损失对大物体噪声敏感是失败原因。通过数学证明，dice损失在大物体上比回归损失具有更好的噪声鲁棒性和收敛性。基于此提出SeaBird方法，将BEV分割与3D检测结合，并使用dice损失训练分割头。实验表明SeaBird在大物体检测上显著提升，同时保持小物体性能。
- **摘要（英）**: To address the performance drop of monocular 3D detection on large objects, this paper identifies the sensitivity of depth regression losses to noise as the cause. It mathematically proves that dice loss offers superior noise robustness and convergence for large objects. The proposed SeaBird integrates BEV segmentation with 3D detection, trained with dice loss, significantly improving large object detection while maintaining performance on smaller ones.
- **核心贡献**: 揭示了回归损失对大物体的敏感性，并提出基于dice损失的SeaBird方法。
- **创新点**: 数学证明dice损失在大物体上的优势，并用于BEV分割辅助检测。
- **结果**: 在大物体检测上显著提升，同时保持小物体性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular 3D detectors achieve remarkable performance on cars and smaller objects. However, their performance drops on larger objects, leading to fatal accidents. Some attribute the failures to training data scarcity or their receptive field requirements of large objects. In this paper, we highlight this understudied problem of generalization to large objects. We find that modern frontal detectors struggle to generalize to large objects even on nearly balanced datasets. We argue that the cause of failure is the sensitivity of depth regression losses to noise of larger objects. To bridge this gap, we comprehensively investigate regression and dice losses, examining their robustness under varying error levels and object sizes. We mathematically prove that the dice loss leads to superior noise-robustness and model convergence for large objects compared to regression losses for a simplified case. Leveraging our theoretical insights, we propose SeaBird (Segmentation in Bird's View) as the first step towards generalizing to large objects. SeaBird effectively integrates BEV segmentation on foreground objects for 3D detection, with the segmentation head trained with the dice loss. SeaBird achieves SoTA results on the KITTI-360 leaderboard and improves existing detectors on the nuScenes leaderboard, particularly for large objects. Code and models at https://github.com/abhi1kumar/SeaBird

</details>

### RadarDistill: Boosting Radar-Based Object Detection Performance via Knowledge Distillation from LiDAR Features. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2403.05061](https://arxiv.org/abs/2403.05061) · 📚 被引 49
- **作者**: Geonho Bang, Kwangjin Choi, Jisong Kim, Dongsuk Kum, Jun Won Choi
- **🏷️ 机构**: Hanyang University,Korea, KAIST,Korea, Seoul National University,Korea
- **会议**: CVPR 2024
- **摘要（中）**: ①该论文针对雷达数据在3D目标检测中噪声大、稀疏的问题，提出利用LiDAR数据提升雷达特征表示。②提出了RadarDistill知识蒸馏方法，包含跨模态对齐、基于激活的特征蒸馏和基于提议的特征蒸馏三个组件，有效将LiDAR特征迁移到雷达网络。③相比已有方法，通过膨胀操作增强雷达特征密度，并选择性蒸馏关键区域，解决了LiDAR到雷达知识迁移效率低的问题。④在nuScenes数据集上达到了雷达-only目标检测任务的最优性能。
- **摘要（英）**: This paper addresses the noisy and sparse nature of radar data in 3D object detection by leveraging LiDAR data. It proposes RadarDistill, a knowledge distillation method with cross-modality alignment, activation-based feature distillation, and proposal-based feature distillation to effectively transfer LiDAR features to radar networks. The method enhances radar feature density and selectively distills key regions, achieving state-of-the-art performance on nuScenes for radar-only detection.
- **核心贡献**: 提出RadarDistill知识蒸馏方法，显著提升雷达-only 3D目标检测性能。
- **创新点**: 通过跨模态对齐和选择性特征蒸馏，高效迁移LiDAR知识到雷达网络。
- **结果**: 在nuScenes数据集上达到雷达-only检测的最优性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The inherent noisy and sparse characteristics of radar data pose challenges in finding effective representations for 3D object detection. In this paper, we propose RadarDistill, a novel knowledge distillation (KD) method, which can improve the representation of radar data by leveraging LiDAR data. RadarDistill successfully transfers desirable characteristics of LiDAR features into radar features using three key components: Cross-Modality Alignment (CMA), Activation-based Feature Distillation (AFD), and Proposal-based Feature Distillation (PFD). CMA enhances the density of radar features by employing multiple layers of dilation operations, effectively addressing the challenge of inefficient knowledge transfer from LiDAR to radar. AFD selectively transfers knowledge based on regions of the LiDAR features, with a specific focus on areas where activation intensity exceeds a predefined threshold. PFD similarly guides the radar network to selectively mimic features from the LiDAR network within the object proposals. Our comparative analyses conducted on the nuScenes datasets demonstrate that RadarDistill achieves state-of-the-art (SOTA) performance for radar-only object detection task, recording 20.5% in mAP and 43.7% in NDS. Also, RadarDistill significantly improves the performance of the camera-radar fusion model.

</details>

### Towards Robust 3D Object Detection with LiDAR and 4D Radar Fusion in Various Weather Conditions. **⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01436) · 📚 被引 44
- **作者**: Yujeong Chae, Hyeonseong Kim, Kuk-Jin Yoon
- **🏷️ 机构**: KAIST
- **会议**: CVPR 2024
- **摘要（中）**: ①该论文针对不同天气条件下LiDAR和4D雷达融合的3D目标检测鲁棒性问题。②提出了融合LiDAR和4D雷达的鲁棒检测方法，可能涉及多模态特征融合和天气适应性设计。③相比单一传感器或传统融合方法，该方法利用4D雷达的额外信息，增强恶劣天气下的检测稳定性。④由于摘要被截断，具体效果未提及，但该方向对自动驾驶全天候感知至关重要。
- **摘要（英）**: This paper addresses the robustness of 3D object detection with LiDAR and 4D radar fusion under various weather conditions. It proposes a fusion method that leverages 4D radar's additional information to enhance detection stability in adverse weather. Compared to single-sensor or traditional fusion approaches, this method improves robustness. Specific results are unavailable due to truncated abstract.
- **核心贡献**: 提出LiDAR与4D雷达融合的鲁棒3D检测方法，提升全天候性能。
- **创新点**: 利用4D雷达的额外维度信息增强融合特征的天气适应性。
- **结果**: 具体效果未在摘要中提及。

### Weak-to-Strong 3D Object Detection with X-Ray Distillation. **⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2404.00679](https://arxiv.org/abs/2404.00679) · 📚 被引 1
- **作者**: Alexander Gambashidze, Aleksandr Dadukin, Maksim Golyadkin, Maria Razzhivina, Ilya Makarov
- **🏷️ 机构**: Artificial Intelligence Research Institute, HSE University
- **会议**: CVPR 2024
- **摘要（中）**: 针对LiDAR 3D目标检测中的稀疏性和遮挡问题，提出X-Ray Distillation框架，利用点云序列的时间信息生成Object-Complete帧，从多视角表示物体以解决遮挡和稀疏性。方法上，首次在3D计算机视觉中实现弱到强泛化，通过教师-学生框架进行知识蒸馏，鼓励强学生模型模仿处理简单输入的弱教师模型。相比依赖特定架构或辅助模块的方法，该技术可无缝集成到任何现有3D检测框架，适用于监督和半监督设置。
- **摘要（英）**: This paper introduces X-Ray Distillation with Object-Complete Frames, a versatile technique for LiDAR-based 3D object detection that leverages temporal information to create multi-view object representations, addressing sparsity and occlusion. It is the first to achieve weak-to-strong generalization in 3D vision, using knowledge distillation in a teacher-student framework, and integrates into any existing detection framework.
- **核心贡献**: 提出首个弱到强泛化的3D检测蒸馏框架，利用时间信息生成完整物体帧。
- **创新点**: 通过Object-Complete帧和知识蒸馏实现跨框架的稀疏性缓解。
- **结果**: 在监督和半监督设置下显著提升3D检测性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper addresses the critical challenges of sparsity and occlusion in LiDAR-based 3D object detection. Current methods often rely on supplementary modules or specific architectural designs, potentially limiting their applicability to new and evolving architectures. To our knowledge, we are the first to propose a versatile technique that seamlessly integrates into any existing framework for 3D Object Detection, marking the first instance of Weak-to-Strong generalization in 3D computer vision. We introduce a novel framework, X-Ray Distillation with Object-Complete Frames, suitable for both supervised and semi-supervised settings, that leverages the temporal aspect of point cloud sequences. This method extracts crucial information from both previous and subsequent LiDAR frames, creating Object-Complete frames that represent objects from multiple viewpoints, thus addressing occlusion and sparsity. Given the limitation of not being able to generate Object-Complete frames during online inference, we utilize Knowledge Distillation within a Teacher-Student framework. This technique encourages the strong Student model to emulate the behavior of the weaker Teacher, which processes simple and informative Object-Complete frames, effectively offering a comprehensive view of objects as if seen through X-ray vision. Our proposed methods surpass state-of-the-art in semi-supervised learning by 1-1.5 mAP and enhance the performance of five established supervised models by 1-2 mAP on standard autonomous driving datasets, even with default hyperparameters. Code for Object-Complete frames is available here: https://github.com/sakharok13/X-Ray-Teacher-Patching-Tools.

</details>

### PTT: Point-Trajectory Transformer for Efficient Temporal 3D Object Detection. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2312.08371](https://arxiv.org/abs/2312.08371) · 📚 被引 23
- **作者**: Kuan-Chih Huang, Weijie Lyu, Ming-Hsuan Yang, Yi-Hsuan Tsai
- **🏷️ 机构**: University of California,Merced, Google
- **会议**: CVPR 2024
- **摘要（中）**: 针对现有时间LiDAR 3D检测器依赖每帧物体或全点云导致内存占用高的问题，提出点轨迹Transformer（PTT），仅利用当前帧物体点云和历史轨迹作为输入，最小化内存需求。方法上，设计轨迹特征编码模块，关注长短期和未来感知信息，并有效聚合点云特征。相比基于拼接的简单融合，PTT增强点云与轨迹的交互，在Waymo数据集上达到先进性能。
- **摘要（英）**: This paper proposes a point-trajectory transformer with long short-term memory for efficient temporal 3D object detection, using only current-frame point clouds and historical trajectories to reduce memory usage. It introduces modules for trajectory encoding and effective aggregation with point cloud features, achieving state-of-the-art performance on Waymo.
- **核心贡献**: 提出高效的点轨迹Transformer，减少内存需求并提升时间3D检测性能。
- **创新点**: 设计长短期和未来感知的轨迹编码模块，增强点云与轨迹交互。
- **结果**: 在Waymo数据集上达到先进性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent temporal LiDAR-based 3D object detectors achieve promising performance based on the two-stage proposal-based approach. They generate 3D box candidates from the first-stage dense detector, followed by different temporal aggregation methods. However, these approaches require per-frame objects or whole point clouds, posing challenges related to memory bank utilization. Moreover, point clouds and trajectory features are combined solely based on concatenation, which may neglect effective interactions between them. In this paper, we propose a point-trajectory transformer with long short-term memory for efficient temporal 3D object detection. To this end, we only utilize point clouds of current-frame objects and their historical trajectories as input to minimize the memory bank storage requirement. Furthermore, we introduce modules to encode trajectory features, focusing on long short-term and future-aware perspectives, and then effectively aggregate them with point cloud features. We conduct extensive experiments on the large-scale Waymo dataset to demonstrate that our approach performs well against state-of-the-art methods. Code and models will be made publicly available at https://github.com/kuanchihhuang/PTT.

</details>

### GAFusion: Adaptive Fusing LiDAR and Camera with Multiple Guidance for 3D Object Detection. **⭐⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2411.00340](https://arxiv.org/abs/2411.00340) · 📚 被引 36
- **作者**: Xiaotian Li, Baojie Fan, Jiandong Tian, Huijie Fan
- **🏷️ 机构**: Nanjing University of Posts and Telecommunications, Shenyang Institute of Automation Chinese Academy of Science
- **会议**: CVPR 2024
- **摘要（中）**: 针对现有BEV多模态3D检测方法忽略LiDAR和相机间互补交互和引导的问题，提出了GAFusion方法，包含LiDAR引导的全局交互和自适应融合。引入稀疏深度引导和LiDAR占用引导生成具有深度信息的3D特征，并开发LiDAR引导的自适应融合transformer增强模态间交互。在nuScenes测试集上达到73.6% mAP和74.9% NDS，实现最先进性能。
- **摘要（英）**: To address the overlooked complementary interaction between LiDAR and camera in BEV-based multi-modal 3D detection, this paper proposes GAFusion with LiDAR-guided global interaction and adaptive fusion. It introduces sparse depth guidance and LiDAR occupancy guidance to generate depth-rich features, and a LiDAR-guided adaptive fusion transformer for enhanced cross-modal interaction. GAFusion achieves state-of-the-art results with 73.6% mAP and 74.9% NDS on nuScenes.
- **核心贡献**: 提出了GAFusion，通过LiDAR引导的全局交互和自适应融合提升多模态3D检测。
- **创新点**: 引入稀疏深度和占用引导，以及自适应融合transformer。
- **结果**: 在nuScenes上取得最先进性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent years have witnessed the remarkable progress of 3D multi-modality object detection methods based on the Bird's-Eye-View (BEV) perspective. However, most of them overlook the complementary interaction and guidance between LiDAR and camera. In this work, we propose a novel multi-modality 3D objection detection method, named GAFusion, with LiDAR-guided global interaction and adaptive fusion. Specifically, we introduce sparse depth guidance (SDG) and LiDAR occupancy guidance (LOG) to generate 3D features with sufficient depth information. In the following, LiDAR-guided adaptive fusion transformer (LGAFT) is developed to adaptively enhance the interaction of different modal BEV features from a global perspective. Meanwhile, additional downsampling with sparse height compression and multi-scale dual-path transformer (MSDPT) are designed to enlarge the receptive fields of different modal features. Finally, a temporal fusion module is introduced to aggregate features from previous frames. GAFusion achieves state-of-the-art 3D object detection results with 73.6$\%$ mAP and 74.9$\%$ NDS on the nuScenes test set.

</details>

### BEVNeXt: Reviving Dense BEV Frameworks for 3D Object Detection. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2312.01696](https://arxiv.org/abs/2312.01696) · 📚 被引 55
- **作者**: Zhenxin Li, Shiyi Lan, José M. Álvarez, Zuxuan Wu
- **🏷️ 机构**: School of CS, Fudan University,Shanghai Key Lab of Intell. Info. Processing, NVIDIA
- **会议**: CVPR 2024
- **摘要（中）**: 针对查询式transformer解码器在相机3D检测中超越传统密集BEV方法的现象，指出密集BEV框架在深度估计和物体定位上仍有优势。提出了BEVNeXt，通过CRF调制深度估计、长时时间聚合和两阶段解码器增强密集BEV框架。在nuScenes测试集上达到64.2 NDS，超越BEV和查询式方法，实现最先进性能。
- **摘要（英）**: To address the rise of query-based decoders surpassing dense BEV methods in camera-based 3D detection, this paper argues that dense BEV frameworks retain advantages in depth estimation and localization. It proposes BEVNeXt with CRF-modulated depth estimation, long-term temporal aggregation, and a two-stage decoder. BEVNeXt achieves 64.2 NDS on nuScenes, outperforming both BEV and query-based methods.
- **核心贡献**: 提出了BEVNeXt，通过多项增强组件提升密集BEV检测性能。
- **创新点**: 引入CRF调制深度估计和长时时间聚合。
- **结果**: 在nuScenes上取得最先进NDS。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, the rise of query-based Transformer decoders is reshaping camera-based 3D object detection. These query-based decoders are surpassing the traditional dense BEV (Bird's Eye View)-based methods. However, we argue that dense BEV frameworks remain important due to their outstanding abilities in depth estimation and object localization, depicting 3D scenes accurately and comprehensively. This paper aims to address the drawbacks of the existing dense BEV-based 3D object detectors by introducing our proposed enhanced components, including a CRF-modulated depth estimation module enforcing object-level consistencies, a long-term temporal aggregation module with extended receptive fields, and a two-stage object decoder combining perspective techniques with CRF-modulated depth embedding. These enhancements lead to a "modernized" dense BEV framework dubbed BEVNeXt. On the nuScenes benchmark, BEVNeXt outperforms both BEV-based and query-based frameworks under various settings, achieving a state-of-the-art result of 64.2 NDS on the nuScenes test set. Code will be available at \url{https://github.com/woxihuanjiangguo/BEVNeXt}.

</details>

### UniMODE: Unified Monocular 3D Object Detection. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2402.18573](https://arxiv.org/abs/2402.18573) · 📚 被引 24
- **作者**: Zhuoling Li, Xiaogang Xu, Ser-Nam Lim, Hengshuang Zhao
- **🏷️ 机构**: IHKU, CUHK, UCF
- **会议**: CVPR 2024
- **摘要（中）**: ①针对单目3D检测中室内外场景统一建模的难题，即几何特性差异大和域分布异构导致训练不稳定。②提出UniMODE，基于BEV检测范式，将架构分为两阶段，设计不均匀BEV网格处理几何差异，采用稀疏BEV特征投影降低计算量，并提出统一域对齐方法；数据层面引入深度信息增强训练鲁棒性。③相比现有方法，首次系统性地从算法和数据双角度解决室内外统一检测，通过显式特征投影缓解几何学习歧义。④在室内外数据集上验证了统一检测的有效性，但摘要未提供具体数值。
- **摘要（英）**: This paper addresses unified monocular 3D detection across indoor and outdoor scenes, tackling geometry and domain gaps. It proposes UniMODE with a two-stage BEV detector, uneven grid design, sparse projection, and unified domain alignment, plus depth-aware training. The method improves stability and efficiency, though specific metrics are not detailed in the abstract.
- **核心贡献**: 提出首个统一室内外单目3D检测框架UniMODE，解决几何与域差异。
- **创新点**: 采用不均匀BEV网格和稀疏投影策略，结合统一域对齐。
- **结果**: 在统一检测任务上实现有效训练，但具体性能未在摘要中给出。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Realizing unified 3D object detection, including both indoor and outdoor scenes, holds great importance in applications like robot navigation. However, involving various scenarios of data to train models poses challenges due to their significantly distinct characteristics, \eg, diverse geometry properties and heterogeneous domain distributions. In this work, we propose to address the challenges from two perspectives, the algorithm perspective and data perspective. In terms of the algorithm perspective, we first build a monocular 3D object detector based on the bird's-eye-view (BEV) detection paradigm, where the explicit feature projection is beneficial to addressing the geometry learning ambiguity. In this detector, we split the classical BEV detection architecture into two stages and propose an uneven BEV grid design to handle the convergence instability caused by geometry difference between scenarios. Besides, we develop a sparse BEV feature projection strategy to reduce the computational cost and a unified domain alignment method to handle heterogeneous domains. From the data perspective, we propose to incorporate depth information to improve training robustness. Specifically, we build the first unified multi-modal 3D object detection benchmark MM-Omni3D and extend the aforementioned monocular detector to its multi-modal version, which is the first unified multi-modal 3D object detector. We name the designed monocular and multi-modal detectors as UniMODE and MM-UniMODE, respectively. The experimental results reveal several insightful findings highlighting the benefits of multi-modal data and confirm the effectiveness of all the proposed strategies.

</details>

### RCBEVDet: Radar-Camera Fusion in Bird's Eye View for 3D Object Detection. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2403.16440](https://arxiv.org/abs/2403.16440) · 📚 被引 135
- **作者**: Zhiwei Lin, Zhe Liu, Zhongyu Xia, Xinhao Wang, Yongtao Wang, Shengxiang Qi et al.
- **🏷️ 机构**: Wangxuan Institute of Computer Technology, Peking University, School of Information and Communication Engineering, University of Electronic Science and Technology of China, Chongqing Changan Automobile Co., Ltd.
- **会议**: CVPR 2024
- **摘要（中）**: 针对纯相机3D检测精度和鲁棒性不足的问题，提出RCBEVDet，一种基于BEV的雷达-相机融合3D检测方法。设计了RadarBEVNet，包含双流雷达主干和RCS感知BEV编码器，通过点编码器和Transformer编码器提取特征，并利用RCS作为物体尺寸先验散射点特征。此外，提出跨注意力多层融合模块自动融合多模态特征。该方法在低成本传感器配置下提升了3D检测的准确性和可靠性。
- **摘要（英）**: To address the limitations of camera-only 3D detection, RCBEVDet introduces a radar-camera fusion method in BEV, featuring RadarBEVNet with dual-stream radar backbone and RCS-aware BEV encoder, plus a cross-attention multi-layer fusion module. It enhances detection accuracy and robustness using low-cost sensors.
- **核心贡献**: 提出RCS感知的BEV编码器和跨注意力融合模块，提升雷达-相机融合检测性能。
- **创新点**: 利用RCS作为先验改进BEV特征散射，并设计双流雷达编码器。
- **结果**: 在BEV融合检测中显著提升3D目标检测精度。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Three-dimensional object detection is one of the key tasks in autonomous driving. To reduce costs in practice, low-cost multi-view cameras for 3D object detection are proposed to replace the expansive LiDAR sensors. However, relying solely on cameras is difficult to achieve highly accurate and robust 3D object detection. An effective solution to this issue is combining multi-view cameras with the economical millimeter-wave radar sensor to achieve more reliable multi-modal 3D object detection. In this paper, we introduce RCBEVDet, a radar-camera fusion 3D object detection method in the bird's eye view (BEV). Specifically, we first design RadarBEVNet for radar BEV feature extraction. RadarBEVNet consists of a dual-stream radar backbone and a Radar Cross-Section (RCS) aware BEV encoder. In the dual-stream radar backbone, a point-based encoder and a transformer-based encoder are proposed to extract radar features, with an injection and extraction module to facilitate communication between the two encoders. The RCS-aware BEV encoder takes RCS as the object size prior to scattering the point feature in BEV. Besides, we present the Cross-Attention Multi-layer Fusion module to automatically align the multi-modal BEV feature from radar and camera with the deformable attention mechanism, and then fuse the feature with channel and spatial fusion layers. Experimental results show that RCBEVDet achieves new state-of-the-art radar-camera fusion results on nuScenes and view-of-delft (VoD) 3D object detection benchmarks. Furthermore, RCBEVDet achieves better 3D detection results than all real-time camera-only and radar-camera 3D object detectors with a faster inference speed at 21~28 FPS. The source code will be released at https://github.com/VDIGPKU/RCBEVDet.

</details>

### VSRD: Instance-Aware Volumetric Silhouette Rendering for Weakly Supervised 3D Object Detection. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2404.00149](https://arxiv.org/abs/2404.00149) · 📚 被引 5
- **作者**: Zihua Liu, Hiroki Sakuma, Masatoshi Okutomi
- **🏷️ 机构**: Tokyo Institute of Technology, T2 Inc.
- **会议**: CVPR 2024
- **摘要（中）**: ①针对弱监督3D检测中依赖昂贵LiDAR标注的问题，提出仅用2D监督训练3D检测器。②提出VSRD框架，包含多视图3D自动标注和后续单目检测器训练；自动标注阶段用SDF表示实例表面，通过实例感知体素轮廓渲染生成伪标签，并将SDF分解为立方体SDF和残差场以直接优化3D框。③相比现有弱监督方法，通过可微渲染直接优化3D框，减少标注成本。④摘要未提供具体数值，但展示了无需3D标签的可行性。
- **摘要（英）**: This paper tackles weakly supervised 3D detection without 3D labels, proposing VSRD with multi-view auto-labeling via instance-aware volumetric silhouette rendering. It decomposes SDF into cuboid and residual components for direct box optimization. The method reduces annotation cost, though quantitative results are not in the abstract.
- **核心贡献**: 提出VSRD，实现仅用2D监督的3D检测器训练。
- **创新点**: 实例感知体素轮廓渲染与SDF分解优化3D框。
- **结果**: 在无3D标签条件下实现有效检测，具体性能待见全文。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular 3D object detection poses a significant challenge in 3D scene understanding due to its inherently ill-posed nature in monocular depth estimation. Existing methods heavily rely on supervised learning using abundant 3D labels, typically obtained through expensive and labor-intensive annotation on LiDAR point clouds. To tackle this problem, we propose a novel weakly supervised 3D object detection framework named VSRD (Volumetric Silhouette Rendering for Detection) to train 3D object detectors without any 3D supervision but only weak 2D supervision. VSRD consists of multi-view 3D auto-labeling and subsequent training of monocular 3D object detectors using the pseudo labels generated in the auto-labeling stage. In the auto-labeling stage, we represent the surface of each instance as a signed distance field (SDF) and render its silhouette as an instance mask through our proposed instance-aware volumetric silhouette rendering. To directly optimize the 3D bounding boxes through rendering, we decompose the SDF of each instance into the SDF of a cuboid and the residual distance field (RDF) that represents the residual from the cuboid. This mechanism enables us to optimize the 3D bounding boxes in an end-to-end manner by comparing the rendered instance masks with the ground truth instance masks. The optimized 3D bounding boxes serve as effective training data for 3D object detection. We conduct extensive experiments on the KITTI-360 dataset, demonstrating that our method outperforms the existing weakly supervised 3D object detection methods. The code is available at https://github.com/skmhrk1209/VSRD.

</details>

### Multi-View Attentive Contextualization for Multi-View 3D Object Detection. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2405.12200](https://arxiv.org/abs/2405.12200) · 📚 被引 10
- **作者**: Xianpeng Liu, Ce Zheng, Ming Qian, Nan Xue, Chen Chen, Zhebin Zhang et al.
- **🏷️ 机构**: North Carolina State University, University of Central Florida, Ant Group
- **会议**: CVPR 2024
- **摘要（中）**: 针对查询式多视图3D检测中2D到3D特征提升的不足，提出MvACon方法，通过表示密集但计算稀疏的注意力特征上下文化方案，兼顾高分辨率2D特征利用和计算效率。该方法与具体特征提升方法无关，可应用于BEVFormer、DFA3D和PETR等框架。在nuScenes和Waymo-mini基准上，MvACon一致提升了检测性能，尤其在位置、方向和速度预测方面。
- **摘要（英）**: MvACon addresses the trade-off between dense feature exploitation and computational cost in query-based multi-view 3D detection via a representationally dense yet computationally sparse attentive contextualization scheme. It consistently improves detection performance on nuScenes and Waymo-mini across BEVFormer, DFA3D, and PETR, particularly in location, orientation, and velocity prediction.
- **核心贡献**: 提出MvACon，一种即插即用的注意力上下文化方案，提升多视图3D检测性能。
- **创新点**: 通过稀疏注意力实现密集特征上下文化，兼顾精度和效率。
- **结果**: 在多个基准上一致提升检测精度，尤其是运动状态预测。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present Multi-View Attentive Contextualization (MvACon), a simple yet effective method for improving 2D-to-3D feature lifting in query-based multi-view 3D (MV3D) object detection. Despite remarkable progress witnessed in the field of query-based MV3D object detection, prior art often suffers from either the lack of exploiting high-resolution 2D features in dense attention-based lifting, due to high computational costs, or from insufficiently dense grounding of 3D queries to multi-scale 2D features in sparse attention-based lifting. Our proposed MvACon hits the two birds with one stone using a representationally dense yet computationally sparse attentive feature contextualization scheme that is agnostic to specific 2D-to-3D feature lifting approaches. In experiments, the proposed MvACon is thoroughly tested on the nuScenes benchmark, using both the BEVFormer and its recent 3D deformable attention (DFA3D) variant, as well as the PETR, showing consistent detection performance improvement, especially in enhancing performance in location, orientation, and velocity prediction. It is also tested on the Waymo-mini benchmark using BEVFormer with similar improvement. We qualitatively and quantitatively show that global cluster-based contexts effectively encode dense scene-level contexts for MV3D object detection. The promising results of our proposed MvACon reinforces the adage in computer vision -- ``(contextualized) feature matters".

</details>

### Learning Occupancy for Monocular 3D Object Detection. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2305.15694](https://arxiv.org/abs/2305.15694)
- **作者**: Liang Peng, Junkai Xu, Haoran Cheng, Zheng Yang, Xiaopei Wu, Wei Qian et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Weakly supervised 3D object detection aims to learn a 3D detector with lower annotation cost, e.g., 2D labels. Unlike prior work which still relies on few accurate 3D annotations, we propose a framework to study how to leverage constraints between 2D and 3D domains without requiring any 3D labels. Specifically, we employ visual data from three perspectives to establish connections between 2D and 3D domains. First, we design a feature-level constraint to align LiDAR and image features based on object-aware regions. Second, the output-level constraint is developed to enforce the overlap between 2D and projected 3D box estimations. Finally, the training-level constraint is utilized by producing accurate and consistent 3D pseudo-labels that align with the visual data. We conduct extensive experiments on the KITTI dataset to validate the effectiveness of the proposed three constraints. Without using any 3D labels, our method achieves favorable performance against state-of-the-art approaches and is competitive with the method that uses 500-frame 3D annotations. Code will be made publicly available at https://github.com/kuanchihhuang/VG-W3D.

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

### LiDAR-Based All-Weather 3D Object Detection via Prompting and Distilling 4D Radar.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72992-8_21) · 📚 被引 8
- **作者**: Yujeong Chae, Hyeonseong Kim, Changgyoon Oh, Minseok Kim, Kuk-Jin Yoon
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-vocabulary 3D object detection (OV-3DDet) aims to localize and recognize both seen and previously unseen object categories within any new 3D scene. While language and vision foundation models have achieved success in handling various open-vocabulary tasks with abundant training data, OV-3DDet faces a significant challenge due to the limited availability of training data. Although some pioneering efforts have integrated vision-language models (VLM) knowledge into OV-3DDet learning, the full potential of these foundational models has yet to be fully exploited. In this paper, we unlock the textual and visual wisdom to tackle the open-vocabulary 3D detection task by leveraging the language and vision foundation models. We leverage a vision foundation model to provide image-wise guidance for discovering novel classes in 3D scenes. Specifically, we utilize a object detection vision foundation model to enable the zero-shot discovery of objects in images, which serves as the initial seeds and filtering guidance to identify novel 3D objects. Additionally, to align the 3D space with the powerful vision-language space, we introduce a hierarchical alignment approach, where the 3D feature space is aligned with the vision-language feature space using a pre-trained VLM at the instance, category, and scene levels. Through extensive experimentation, we demonstrate significant improvements in accuracy and generalization, highlighting the potential of foundation models in advancing open-vocabulary 3D object detection in real-world scenarios.

</details>

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Point-cloud-based 3D object detection suffers from performance degradation when encountering data with novel domain gaps. To tackle it, the single-domain generalization (SDG) aims to generalize the detection model trained in a limited single source domain to perform robustly on unexplored domains. In this paper, we propose an SDG method to improve the generalizability of 3D object detection to unseen target domains. Unlike prior SDG works for 3D object detection solely focusing on data augmentation, our work introduces a novel data augmentation method and contributes a new multi-task learning strategy in the methodology. Specifically, from the perspective of data augmentation, we design a universal physical-aware density-based data augmentation (PDDA) method to mitigate the performance loss stemming from diverse point densities. From the learning methodology viewpoint, we develop a multi-task learning for 3D object detection: during source training, besides the main standard detection task, we leverage an auxiliary self-supervised 3D scene restoration task to enhance the comprehension of the encoder on background and foreground details for better recognition and detection of objects. Furthermore, based on the auxiliary self-supervised task, we propose the first test-time adaptation method for domain generalization of 3D object detection, which efficiently adjusts the encoder's parameters to adapt to unseen target domains during testing time, to further bridge domain gaps. Extensive cross-dataset experiments covering "Car", "Pedestrian", and "Cyclist" detections, demonstrate our method outperforms state-of-the-art SDG methods and even overpass unsupervised domain adaptation methods under some circumstances.

</details>

### LiDAR-PTQ: Post-Training Quantization for Point Cloud 3D Object Detection.
- **链接**: [arXiv:2401.15865](https://arxiv.org/abs/2401.15865) · [代码](https://github.com/StiphyJay/LiDAR-PTQ)
- **作者**: Sifan Zhou, Liang Li, Xinyu Zhang, Bo Zhang, Shipeng Bai, Miao Sun et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### CMD: A Cross Mechanism Domain Adaptation Dataset for 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72998-0_13) · 📚 被引 8
- **作者**: Jinhao Deng, Wei Ye, Hai Wu, Xun Huang, Qiming Xia, Xin Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular 3D object detection is an important challenging task in autonomous driving. Existing methods mainly focus on performing 3D detection in ideal weather conditions, characterized by scenarios with clear and optimal visibility. However, the challenge of autonomous driving requires the ability to handle changes in weather conditions, such as foggy weather, not just clear weather. We introduce MonoWAD, a novel weather-robust monocular 3D object detector with a weather-adaptive diffusion model. It contains two components: (1) the weather codebook to memorize the knowledge of the clear weather and generate a weather-reference feature for any input, and (2) the weather-adaptive diffusion model to enhance the feature representation of the input feature by incorporating a weather-reference feature. This serves an attention role in indicating how much improvement is needed for the input feature according to the weather conditions. To achieve this goal, we introduce a weather-adaptive enhancement loss to enhance the feature representation under both clear and foggy weather conditions. Extensive experiments under various weather conditions demonstrate that MonoWAD achieves weather-robust monocular 3D object detection. The code and dataset are released at https://github.com/VisualAIKHU/MonoWAD.

</details>

> While 3D object bounding box (bbox) representation has been widely used in autonomous driving perception, it lacks the ability to capture the precise details of an object's intrinsic geometry. Recently, occupancy has emerged as a promising alternative for 3D scene perception. However, constructing a high-resolution occupancy map remains infeasible for large scenes due to computational constraints. Recognizing that foreground objects only occupy a small portion of the scene, we introduce object-centric occupancy as a supplement to object bboxes. This representation not only provides intricate details for detected objects but also enables higher voxel resolution in practical applications. We advance the development of object-centric occupancy perception from both data and algorithm perspectives. On the data side, we construct the first object-centric occupancy dataset from scratch using an automated pipeline. From the algorithmic standpoint, we introduce a novel object-centric occupancy completion network equipped with an implicit shape decoder that manages dynamic-size occupancy generation. This network accurately predicts the complete object-centric occupancy volume for inaccurate object proposals by leveraging temporal information from long sequences. Our method demonstrates robust performance in completing object shapes under noisy detection and tracking conditions. Additionally, we show that our occupancy features significantly enhance the detection results of state-of-the-art 3D object detectors, especially for incomplete or distant objects in the Waymo Open Dataset.

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The field of autonomous driving has attracted considerable interest in approaches that directly infer 3D objects in the Bird's Eye View (BEV) from multiple cameras. Some attempts have also explored utilizing 2D detectors from single images to enhance the performance of 3D detection. However, these approaches rely on a two-stage process with separate detectors, where the 2D detection results are utilized only once for token selection or query initialization. In this paper, we present a single model termed SimPB, which simultaneously detects 2D objects in the perspective view and 3D objects in the BEV space from multiple cameras. To achieve this, we introduce a hybrid decoder consisting of several multi-view 2D decoder layers and several 3D decoder layers, specifically designed for their respective detection tasks. A Dynamic Query Allocation module and an Adaptive Query Aggregation module are proposed to continuously update and refine the interaction between 2D and 3D results, in a cyclic 3D-2D-3D manner. Additionally, Query-group Attention is utilized to strengthen the interaction among 2D queries within each camera group. In the experiments, we evaluate our method on the nuScenes dataset and demonstrate promising results for both 2D and 3D detection tasks. Our code is available at: https://github.com/nullmax-vision/SimPB.

</details>

### OV-Uni3DETR: Towards Unified Open-Vocabulary 3D Object Detection via Cycle-Modality Propagation.
- **链接**: [arXiv:2403.19580](https://arxiv.org/abs/2403.19580) · 📚 被引 10
- **作者**: Zhenyu Wang, Yali Li, Taichi Liu, Hengshuang Zhao, Shengjin Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In the current state of 3D object detection research, the severe scarcity of annotated 3D data, substantial disparities across different data modalities, and the absence of a unified architecture, have impeded the progress towards the goal of universality. In this paper, we propose \textbf{OV-Uni3DETR}, a unified open-vocabulary 3D detector via cycle-modality propagation. Compared with existing 3D detectors, OV-Uni3DETR offers distinct advantages: 1) Open-vocabulary 3D detection: During training, it leverages various accessible data, especially extensive 2D detection images, to boost training diversity. During inference, it can detect both seen and unseen classes. 2) Modality unifying: It seamlessly accommodates input data from any given modality, effectively addressing scenarios involving disparate modalities or missing sensor information, thereby supporting test-time modality switching. 3) Scene unifying: It provides a unified multi-modal model architecture for diverse scenes collected by distinct sensors. Specifically, we propose the cycle-modality propagation, aimed at propagating knowledge bridging 2D and 3D modalities, to support the aforementioned functionalities. 2D semantic knowledge from large-vocabulary learning guides novel class discovery in the 3D domain, and 3D geometric knowledge provides localization supervision for 2D detection images. OV-Uni3DETR achieves the state-of-the-art performance on various scenarios, surpassing existing methods by more than 6\% on average. Its performance using only RGB images is on par with or even surpasses that of previous point cloud based methods. Code and pre-trained models will be released later.

</details>

### Towards Stable 3D Object Detection.
- **链接**: [arXiv:2407.04305](https://arxiv.org/abs/2407.04305)
- **作者**: Jiabao Wang, Qiang Meng, Guochao Liu, Liujiang Yan, Ke Wang, Ming-Ming Cheng et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In autonomous driving, the temporal stability of 3D object detection greatly impacts the driving safety. However, the detection stability cannot be accessed by existing metrics such as mAP and MOTA, and consequently is less explored by the community. To bridge this gap, this work proposes Stability Index (SI), a new metric that can comprehensively evaluate the stability of 3D detectors in terms of confidence, box localization, extent, and heading. By benchmarking state-of-the-art object detectors on the Waymo Open Dataset, SI reveals interesting properties of object stability that have not been previously discovered by other metrics. To help models improve their stability, we further introduce a general and effective training strategy, called Prediction Consistency Learning (PCL). PCL essentially encourages the prediction consistency of the same objects under different timestamps and augmentations, leading to enhanced detection stability. Furthermore, we examine the effectiveness of PCL with the widely-used CenterPoint, and achieve a remarkable SI of 86.00 for vehicle class, surpassing the baseline by 5.48. We hope our work could serve as a reliable baseline and draw the community's attention to this crucial issue in 3D object detection. Codes will be made publicly available.

</details>

### Reg-TTA3D: Better Regression Makes Better Test-Time Adaptive 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72775-7_12) · 📚 被引 2
- **作者**: Jiakang Yuan, Bo Zhang, Kaixiong Gong, Xiangyu Yue, Botian Shi, Yu Qiao et al.
- **🏷️ 机构**: Shanghai AI Lab
- **会议**: ECCV 2024

### General Geometry-Aware Weakly Supervised 3D Object Detection.
- **链接**: [arXiv:2407.13748](https://arxiv.org/abs/2407.13748) · [代码](https://github.com/gwenzhang/GGA)
- **作者**: Guowen Zhang, Junsong Fan, Liyi Chen, Zhaoxiang Zhang, Zhen Lei, Lei Zhang
- **🏷️ 机构**: PolyU / OPPO
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D object detection is an indispensable component for scene understanding. However, the annotation of large-scale 3D datasets requires significant human effort. To tackle this problem, many methods adopt weakly supervised 3D object detection that estimates 3D boxes by leveraging 2D boxes and scene/class-specific priors. However, these approaches generally depend on sophisticated manual priors, which is hard to generalize to novel categories and scenes. In this paper, we are motivated to propose a general approach, which can be easily adapted to new scenes and/or classes. A unified framework is developed for learning 3D object detectors from RGB images and associated 2D boxes. In specific, we propose three general components: prior injection module to obtain general object geometric priors from LLM model, 2D space projection constraint to minimize the discrepancy between the boundaries of projected 3D boxes and their corresponding 2D boxes on the image plane, and 3D space geometry constraint to build a Point-to-Box alignment loss to further refine the pose of estimated 3D boxes. Experiments on KITTI and SUN-RGBD datasets demonstrate that our method yields surprisingly high-quality 3D bounding boxes with only 2D annotation. The source code is available at https://github.com/gwenzhang/GGA.

</details>

### Interactive 3D Object Detection with Prompts.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72643-9_9)
- **作者**: Rui Zhang, Xiangru Lin, Wei Zhang, Jincheng Lu, Xuekuan Wang, Xiao Tan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### SparseLIF: High-Performance Sparse LiDAR-Camera Fusion for 3D Object Detection.
- **链接**: [arXiv:2403.07284](https://arxiv.org/abs/2403.07284) · 📚 被引 24
- **作者**: Hongcheng Zhang, Liu Liang, Pengxin Zeng, Xiao Song, Zhe Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Sparse 3D detectors have received significant attention since the query-based paradigm embraces low latency without explicit dense BEV feature construction. However, these detectors achieve worse performance than their dense counterparts. In this paper, we find the key to bridging the performance gap is to enhance the awareness of rich representations in two modalities. Here, we present a high-performance fully sparse detector for end-to-end multi-modality 3D object detection. The detector, termed SparseLIF, contains three key designs, which are (1) Perspective-Aware Query Generation (PAQG) to generate high-quality 3D queries with perspective priors, (2) RoI-Aware Sampling (RIAS) to further refine prior queries by sampling RoI features from each modality, (3) Uncertainty-Aware Fusion (UAF) to precisely quantify the uncertainty of each sensor modality and adaptively conduct final multi-modality fusion, thus achieving great robustness against sensor noises. By the time of paper submission, SparseLIF achieves state-of-the-art performance on the nuScenes dataset, ranking 1st on both validation set and test benchmark, outperforming all state-of-the-art 3D object detectors by a notable margin.

</details>

### CaKDP: Category-Aware Knowledge Distillation and Pruning Framework for Lightweight 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01452) · 📚 被引 17
- **作者**: Haonan Zhang, Longjun Liu, Yuqi Huang, Zhao Yang, Xinyu Lei, Bihan Wen
- **🏷️ 机构**: National Engineering Research Center for Visual Information and Applications, and Institute of Artificial Intelligence and Robotics, Xi&#x0027;an Jiaotong University,National Key Laboratory of Human-Machine Hybrid Augmented Intelligence, Nanyang Technological University
- **会议**: CVPR 2024

### FSD-BEV: Foreground Self-distillation for Multi-view 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73242-3_7)
- **作者**: Zheng Jiang, Jinqing Zhang, Yanan Zhang, Qingjie Liu, Zhenghui Hu, Baohui Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The unsupervised 3D object detection is to accurately detect objects in unstructured environments with no explicit supervisory signals. This task, given sparse LiDAR point clouds, often results in compromised performance for detecting distant or small objects due to the inherent sparsity and limited spatial resolution. In this paper, we are among the early attempts to integrate LiDAR data with 2D images for unsupervised 3D detection and introduce a new method, dubbed LiDAR-2D Self-paced Learning (LiSe). We argue that RGB images serve as a valuable complement to LiDAR data, offering precise 2D localization cues, particularly when scarce LiDAR points are available for certain objects. Considering the unique characteristics of both modalities, our framework devises a self-paced learning pipeline that incorporates adaptive sampling and weak model aggregation strategies. The adaptive sampling strategy dynamically tunes the distribution of pseudo labels during training, countering the tendency of models to overfit easily detected samples, such as nearby and large-sized objects. By doing so, it ensures a balanced learning trajectory across varying object scales and distances. The weak model aggregation component consolidates the strengths of models trained under different pseudo label distributions, culminating in a robust and powerful final model. Experimental evaluations validate the efficacy of our proposed LiSe method, manifesting significant improvements of +7.1% AP$_{BEV}$ and +3.4% AP$_{3D}$ on nuScenes, and +8.3% AP$_{BEV}$ and +7.4% AP$_{3D}$ on Lyft compared to existing techniques.

</details>

> Open-vocabulary 3D object detection (OV-3DDet) aims to localize and recognize both seen and previously unseen object categories within any new 3D scene. While language and vision foundation models have achieved success in handling various open-vocabulary tasks with abundant training data, OV-3DDet faces a significant challenge due to the limited availability of training data. Although some pioneering efforts have integrated vision-language models (VLM) knowledge into OV-3DDet learning, the full potential of these foundational models has yet to be fully exploited. In this paper, we unlock the textual and visual wisdom to tackle the open-vocabulary 3D detection task by leveraging the language and vision foundation models. We leverage a vision foundation model to provide image-wise guidance for discovering novel classes in 3D scenes. Specifically, we utilize a object detection vision foundation model to enable the zero-shot discovery of objects in images, which serves as the initial seeds and filtering guidance to identify novel 3D objects. Additionally, to align the 3D space with the powerful vision-language space, we introduce a hierarchical alignment approach, where the 3D feature space is aligned with the vision-language feature space using a pre-trained VLM at the instance, category, and scene levels. Through extensive experimentation, we demonstrate significant improvements in accuracy and generalization, highlighting the potential of foundation models in advancing open-vocabulary 3D object detection in real-world scenarios.

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In the field of 3D object detection for autonomous driving, LiDAR-Camera (LC) fusion is the top-performing sensor configuration. Still, LiDAR is relatively high cost, which hinders adoption of this technology for consumer automobiles. Alternatively, camera and radar are commonly deployed on vehicles already on the road today, but performance of Camera-Radar (CR) fusion falls behind LC fusion. In this work, we propose Camera-Radar Knowledge Distillation (CRKD) to bridge the performance gap between LC and CR detectors with a novel cross-modality KD framework. We use the Bird's-Eye-View (BEV) representation as the shared feature space to enable effective knowledge distillation. To accommodate the unique cross-modality KD path, we propose four distillation losses to help the student learn crucial features from the teacher model. We present extensive evaluations on the nuScenes dataset to demonstrate the effectiveness of the proposed CRKD framework. The project page for CRKD is https://song-jingyu.github.io/CRKD.

</details>

### Domain Generalization of 3D Object Detection by Density-Resampling.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73039-9_26)
- **作者**: Shuangzhi Li, Lei Ma, Xingyu Li
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### MonoTTA: Fully Test-Time Adaptation for Monocular 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72784-9_6) · 📚 被引 11
- **作者**: Hongbin Lin, Yifan Zhang, Shuaicheng Niu, Shuguang Cui, Zhen Li
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In contrast to extensive studies on general vision, pre-training for scalable visual autonomous driving remains seldom explored. Visual autonomous driving applications require features encompassing semantics, 3D geometry, and temporal information simultaneously for joint perception, prediction, and planning, posing dramatic challenges for pre-training. To resolve this, we bring up a new pre-training task termed as visual point cloud forecasting - predicting future point clouds from historical visual input. The key merit of this task captures the synergic learning of semantics, 3D structures, and temporal dynamics. Hence it shows superiority in various downstream tasks. To cope with this new problem, we present ViDAR, a general model to pre-train downstream visual encoders. It first extracts historical embeddings by the encoder. These representations are then transformed to 3D geometric space via a novel Latent Rendering operator for future point cloud prediction. Experiments show significant gain in downstream tasks, e.g., 3.1% NDS on 3D detection, ~10% error reduction on motion forecasting, and ~15% less collision rate on planning.

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Collaborative perception in automated vehicles leverages the exchange of information between agents, aiming to elevate perception results. Previous camera-based collaborative 3D perception methods typically employ 3D bounding boxes or bird's eye views as representations of the environment. However, these approaches fall short in offering a comprehensive 3D environmental prediction. To bridge this gap, we introduce the first method for collaborative 3D semantic occupancy prediction. Particularly, it improves local 3D semantic occupancy predictions by hybrid fusion of (i) semantic and occupancy task features, and (ii) compressed orthogonal attention features shared between vehicles. Additionally, due to the lack of a collaborative perception dataset designed for semantic occupancy prediction, we augment a current collaborative perception dataset to include 3D collaborative semantic occupancy labels for a more robust evaluation. The experimental findings highlight that: (i) our collaborative semantic occupancy predictions excel above the results from single vehicles by over 30%, and (ii) models anchored on semantic occupancy outpace state-of-the-art collaborative 3D detection techniques in subsequent perception applications, showcasing enhanced accuracy and enriched semantic-awareness in road environments.

</details>

### SAMFusion: Sensor-Adaptive Multimodal Fusion for 3D Object Detection in Adverse Weather.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73030-6_27)
- **作者**: Edoardo Palladin, Roland Dietze, Praveen Narayanan, Mario Bijelic, Felix Heide
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D occupancy prediction is an important task for the robustness of vision-centric autonomous driving, which aims to predict whether each point is occupied in the surrounding 3D space. Existing methods usually require 3D occupancy labels to produce meaningful results. However, it is very laborious to annotate the occupancy status of each voxel. In this paper, we propose SelfOcc to explore a self-supervised way to learn 3D occupancy using only video sequences. We first transform the images into the 3D space (e.g., bird's eye view) to obtain 3D representation of the scene. We directly impose constraints on the 3D representations by treating them as signed distance fields. We can then render 2D images of previous and future frames as self-supervision signals to learn the 3D representations. We propose an MVS-embedded strategy to directly optimize the SDF-induced weights with multiple depth proposals. Our SelfOcc outperforms the previous best method SceneRF by 58.7% using a single frame as input on SemanticKITTI and is the first self-supervised work that produces reasonable 3D occupancy for surround cameras on nuScenes. SelfOcc produces high-quality depth and achieves state-of-the-art results on novel depth synthesis, monocular depth estimation, and surround-view depth estimation on the SemanticKITTI, KITTI-2015, and nuScenes, respectively. Code: https://github.com/huang-yh/SelfOcc.

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-based perception for autonomous driving requires an explicit modeling of a 3D space, where 2D latent representations are mapped and subsequent 3D operators are applied. However, operating on dense latent spaces introduces a cubic time and space complexity, which limits scalability in terms of perception range or spatial resolution. Existing approaches compress the dense representation using projections like Bird's Eye View (BEV) or Tri-Perspective View (TPV). Although efficient, these projections result in information loss, especially for tasks like semantic occupancy prediction. To address this, we propose SparseOcc, an efficient occupancy network inspired by sparse point cloud processing. It utilizes a lossless sparse latent representation with three key innovations. Firstly, a 3D sparse diffuser performs latent completion using spatially decomposed 3D sparse convolutional kernels. Secondly, a feature pyramid and sparse interpolation enhance scales with information from others. Finally, the transformer head is redesigned as a sparse variant. SparseOcc achieves a remarkable 74.9% reduction on FLOPs over the dense baseline. Interestingly, it also improves accuracy, from 12.8% to 14.1% mIOU, which in part can be attributed to the sparse representation's ability to avoid hallucinations on empty voxels.

</details>

### OV-Uni3DETR: Towards Unified Open-Vocabulary 3D Object Detection via Cycle-Modality Propagation.
- **链接**: [arXiv:2403.19580](https://arxiv.org/abs/2403.19580) · 📚 被引 10
- **作者**: Zhenyu Wang, Yali Li, Taichi Liu, Hengshuang Zhao, Shengjin Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-centric autonomous driving has recently raised wide attention due to its lower cost. Pre-training is essential for extracting a universal representation. However, current vision-centric pre-training typically relies on either 2D or 3D pre-text tasks, overlooking the temporal characteristics of autonomous driving as a 4D scene understanding task. In this paper, we address this challenge by introducing a world model-based autonomous driving 4D representation learning framework, dubbed \emph{DriveWorld}, which is capable of pre-training from multi-camera driving videos in a spatio-temporal fashion. Specifically, we propose a Memory State-Space Model for spatio-temporal modelling, which consists of a Dynamic Memory Bank module for learning temporal-aware latent dynamics to predict future changes and a Static Scene Propagation module for learning spatial-aware latent statics to offer comprehensive scene contexts. We additionally introduce a Task Prompt to decouple task-aware features for various downstream tasks. The experiments demonstrate that DriveWorld delivers promising results on various autonomous driving tasks. When pre-trained with the OpenScene dataset, DriveWorld achieves a 7.5% increase in mAP for 3D object detection, a 3.0% increase in IoU for online mapping, a 5.0% increase in AMOTA for multi-object tracking, a 0.1m decrease in minADE for motion forecasting, a 3.0% increase in IoU for occupancy prediction, and a 0.34m reduction in average L2 error for planning.

</details>

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In the context of autonomous driving, the significance of effective feature learning is widely acknowledged. While conventional 3D self-supervised pre-training methods have shown widespread success, most methods follow the ideas originally designed for 2D images. In this paper, we present UniPAD, a novel self-supervised learning paradigm applying 3D volumetric differentiable rendering. UniPAD implicitly encodes 3D space, facilitating the reconstruction of continuous 3D shape structures and the intricate appearance characteristics of their 2D projections. The flexibility of our method enables seamless integration into both 2D and 3D frameworks, enabling a more holistic comprehension of the scenes. We manifest the feasibility and effectiveness of UniPAD by conducting extensive experiments on various downstream 3D tasks. Our method significantly improves lidar-, camera-, and lidar-camera-based baseline by 9.1, 7.7, and 6.9 NDS, respectively. Notably, our pre-training pipeline achieves 73.2 NDS for 3D object detection and 79.4 mIoU for 3D semantic segmentation on the nuScenes validation set, achieving state-of-the-art results in comparison with previous methods. The code will be available at https://github.com/Nightmare-n/UniPAD.

</details>

> In autonomous driving, the temporal stability of 3D object detection greatly impacts the driving safety. However, the detection stability cannot be accessed by existing metrics such as mAP and MOTA, and consequently is less explored by the community. To bridge this gap, this work proposes Stability Index (SI), a new metric that can comprehensively evaluate the stability of 3D detectors in terms of confidence, box localization, extent, and heading. By benchmarking state-of-the-art object detectors on the Waymo Open Dataset, SI reveals interesting properties of object stability that have not been previously discovered by other metrics. To help models improve their stability, we further introduce a general and effective training strategy, called Prediction Consistency Learning (PCL). PCL essentially encourages the prediction consistency of the same objects under different timestamps and augmentations, leading to enhanced detection stability. Furthermore, we examine the effectiveness of PCL with the widely-used CenterPoint, and achieve a remarkable SI of 86.00 for vehicle class, surpassing the baseline by 5.48. We hope our work could serve as a reliable baseline and draw the community's attention to this crucial issue in 3D object detection. Codes will be made publicly available.

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-language navigation (VLN) requires an agent to navigate through an 3D environment based on visual observations and natural language instructions. It is clear that the pivotal factor for successful navigation lies in the comprehensive scene understanding. Previous VLN agents employ monocular frameworks to extract 2D features of perspective views directly. Though straightforward, they struggle for capturing 3D geometry and semantics, leading to a partial and incomplete environment representation. To achieve a comprehensive 3D representation with fine-grained details, we introduce a Volumetric Environment Representation (VER), which voxelizes the physical world into structured 3D cells. For each cell, VER aggregates multi-view 2D features into such a unified 3D space via 2D-3D sampling. Through coarse-to-fine feature extraction and multi-task learning for VER, our agent predicts 3D occupancy, 3D room layout, and 3D bounding boxes jointly. Based on online collected VERs, our agent performs volume state estimation and builds episodic memory for predicting the next step. Experimental results show our environment representations from multi-task learning lead to evident performance gains on VLN. Our model achieves state-of-the-art performance across VLN benchmarks (R2R, REVERIE, and R4R).

</details>
