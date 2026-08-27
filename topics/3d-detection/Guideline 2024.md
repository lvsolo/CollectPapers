# 3D Detection — 2024 Guideline

> 领域: 3D 目标检测（LiDAR / 相机 / 多模态融合）
> 论文数: 37 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: [2022](Guideline%202022.md)

### CLIP-BEVFormer: Enhancing Multi-View Image-Based BEV Detector with Ground Truth Flow. **⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2403.08919](https://arxiv.org/abs/2403.08919) · 📚 被引 24
- **作者**: Chenbin Pan, Burhaneddin Yaman, Senem Velipasalar, Liu Ren
- **🏷️ 机构**: Syracuse University, Bosch Research North America &#x0026; Bosch Center for Artificial Intelligence (BCAI)
- **会议**: CVPR 2024
- **摘要（中）**: 针对多视角图像BEV检测中缺乏清晰监督的问题，提出了CLIP-BEVFormer，利用对比学习增强BEV骨干网络，引入真值信息流。该方法通过CLIP对齐图像和BEV特征，提升3D检测性能。在nuScenes数据集上，NDS和mAP分别提升8.5%和9.2%，显著优于现有最先进模型。
- **摘要（英）**: This paper introduces CLIP-BEVFormer to address the lack of clear supervision in BEV detection by leveraging contrastive learning to enhance multi-view image-derived BEV backbones with ground truth flow. The method achieves significant improvements of 8.5% NDS and 9.2% mAP over state-of-the-art on nuScenes for 3D object detection.
- **核心贡献**: 提出了CLIP-BEVFormer，利用对比学习增强BEV特征并引入真值信息流。
- **创新点**: 将CLIP的对比学习机制引入BEV检测，解决监督不足问题。
- **结果**: 在nuScenes上NDS和mAP分别提升8.5%和9.2%，超越现有最先进方法。

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

### Learning Occupancy for Monocular 3D Object Detection. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2305.15694](https://arxiv.org/abs/2305.15694)
- **作者**: Liang Peng, Junkai Xu, Haoran Cheng, Zheng Yang, Xiaopei Wu, Wei Qian et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024
- **摘要（中）**: 针对单目3D检测中3D信息缺乏的问题，提出OccupancyM3D，通过直接学习视锥和3D空间中的占用状态，生成更判别性的3D特征。利用同步稀疏LiDAR点云定义空间状态并生成体素占用标签，将占用预测作为分类问题并设计损失函数，增强原始特征。在KITTI和Waymo数据集上，该方法显著超越现有方法，达到新SOTA。
- **摘要（英）**: OccupancyM3D tackles the lack of 3D information in monocular 3D detection by directly learning occupancy in frustum and 3D space, using sparse LiDAR to generate voxel labels and classification losses. It enhances 3D features and achieves new state-of-the-art results on KITTI and Waymo.
- **核心贡献**: 提出占用学习框架，通过分类任务增强单目3D检测的特征表示。
- **创新点**: 在视锥和3D空间直接学习占用，利用LiDAR生成标签。
- **结果**: 在KITTI和Waymo上显著超越现有方法。

### MonoDiff: Monocular 3D Object Detection and Pose Estimation with Diffusion Models. **⭐⭐⭐** (相关度: 80%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01014) · 📚 被引 26
- **作者**: Yasiru Ranasinghe, Deepti Hegde, Vishal M. Patel
- **🏷️ 机构**: Johns Hopkins University,Baltimore,USA
- **会议**: CVPR 2024
- **摘要（中）**: ①针对单目3D检测和姿态估计的挑战，利用扩散模型生成式建模。②提出MonoDiff，将扩散模型应用于3D检测和姿态估计，但摘要为空，无法获取具体方法细节。③相比现有方法，可能利用扩散模型的生成能力提升鲁棒性。④由于摘要缺失，无法评估效果。
- **摘要（英）**: This paper applies diffusion models to monocular 3D detection and pose estimation, but the abstract is empty, so details and results are unavailable. It likely leverages generative modeling for improved robustness.
- **核心贡献**: 探索扩散模型在单目3D检测中的应用。
- **创新点**: 将扩散模型用于3D检测和姿态估计。
- **结果**: 未知，因摘要缺失。

### BEVSpread: Spread Voxel Pooling for Bird's-Eye-View Representation in Vision-Based Roadside 3D Object Detection. **⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2406.08785](https://arxiv.org/abs/2406.08785) · 📚 被引 23
- **作者**: Wenjie Wang, Yehao Lu, Guangcong Zheng, Shuigen Zhan, Xiaoqing Ye, Zichang Tan et al.
- **🏷️ 机构**: College of Computer Science and Technology, Zhejiang University, Polytechnic Institute, Zhejiang University, Baidu
- **会议**: CVPR 2024
- **摘要（中）**: 针对视觉路侧3D检测中体素池化的位置近似误差问题，提出BEVSpread，将每个视锥点视为源，将图像特征传播到周围BEV网格并赋予自适应权重。设计了根据距离和深度动态控制衰减速度的权重函数，并通过CUDA并行加速保持推理速度。在两大路侧基准上，BEVSpread作为即插即用模块显著提升了现有基于视锥的BEV方法性能。
- **摘要（英）**: BEVSpread reduces position approximation error in voxel pooling for roadside 3D detection by spreading features from each frustum point to surrounding BEV grids with adaptive weights, controlled by distance and depth. It significantly improves existing frustum-based BEV methods on roadside benchmarks with comparable inference speed.
- **核心贡献**: 提出BEVSpread体素池化策略，减少位置误差并提升检测性能。
- **创新点**: 自适应权重传播和CUDA加速实现高效特征散布。
- **结果**: 在路侧基准上显著提升检测精度。

### Commonsense Prototype for Outdoor Unsupervised 3D Object Detection. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2404.16493](https://arxiv.org/abs/2404.16493) · 📚 被引 25
- **作者**: Hai Wu, Shijia Zhao, Xun Huang, Chenglu Wen, Xin Li, Cheng Wang
- **🏷️ 机构**: Xiamen University,Fujian Key Laboratory of Sensing and Computing for Smart Cities, Texas A&#x0026;M University,Section of Visual Computing and Interactive Media
- **会议**: CVPR 2024
- **摘要（中）**: 针对无监督3D检测中LiDAR稀疏性导致伪标签质量差的问题，提出基于常识原型的检测器CPD。首先构建高质量边界框和密集点云的常识原型，利用原型的大小先验优化低质量伪标签，并通过几何知识提升稀疏物体的检测精度。在Waymo、PandaSet和KITTI数据集上，CPD大幅超越现有无监督方法，且跨数据集测试接近全监督性能。
- **摘要（英）**: CPD addresses poor pseudo-labels in unsupervised 3D detection caused by LiDAR sparsity by constructing commonsense prototypes with high-quality boxes and dense points, refining labels and enhancing sparse object detection. It outperforms SOTA unsupervised detectors on Waymo, PandaSet, and KITTI, approaching fully supervised performance in cross-dataset settings.
- **核心贡献**: 提出基于常识原型的无监督3D检测器，显著改善伪标签质量。
- **创新点**: 利用常识先验构建原型，指导标签优化和几何增强。
- **结果**: 在多个数据集上大幅超越现有无监督方法，接近全监督性能。

### HINTED: Hard Instance Enhanced Detector with Mixed-Density Feature Fusion for Sparsely-Supervised 3D Object Detection. **⭐⭐⭐** (相关度: 75%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01451) · 📚 被引 28
- **作者**: Qiming Xia, Wei Ye, Hai Wu, Shijia Zhao, Leyuan Xing, Xun Huang et al.
- **🏷️ 机构**: Xiamen University,Fujian Key Laboratory of Sensing and Computing for Smart Cities,Xiamen,China, Texas A&#x0026;M University,Section of Visual Computing and Interactive Media,Texas,USA
- **会议**: CVPR 2024
- **摘要（中）**: ①针对稀疏监督3D检测中困难实例检测性能差的问题。②提出HINTED，包含困难实例增强和混合密度特征融合，但摘要为空，无法获取具体方法。③相比现有方法，可能通过特征融合提升稀疏监督下的检测精度。④由于摘要缺失，无法评估效果。
- **摘要（英）**: This paper addresses hard instance detection under sparse supervision in 3D detection, proposing HINTED with mixed-density feature fusion. The abstract is empty, so details and results are unavailable.
- **核心贡献**: 提出困难实例增强检测器用于稀疏监督3D检测。
- **创新点**: 混合密度特征融合策略。
- **结果**: 未知，因摘要缺失。

### 3DiffTection: 3D Object Detection with Geometry-Aware Diffusion Features. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2311.04391](https://arxiv.org/abs/2311.04391) · 📚 被引 19
- **作者**: Chenfeng Xu, Huan Ling, Sanja Fidler, Or Litany
- **🏷️ 机构**: NVIDIA
- **会议**: CVPR 2024
- **摘要（中）**: ①针对单目3D检测中标注成本高和扩散模型特征域差距的问题。②提出3DiffTection，利用3D感知扩散模型特征，通过几何调优（新视角合成+极线变换）和语义调优（检测监督）两阶段，并用ControlNet保持特征完整性。③相比现有方法，首次将扩散模型特征适配到3D检测，解决域差距。④摘要未提供具体数值，但声称达到最先进性能。
- **摘要（英）**: This paper proposes 3DiffTection for monocular 3D detection using 3D-aware diffusion features, with geometric tuning via novel view synthesis and semantic tuning with detection supervision. It bridges domain gaps and achieves state-of-the-art results, though metrics are not in the abstract.
- **核心贡献**: 提出基于扩散模型特征的3D检测方法，解决域差距。
- **创新点**: 几何和语义双阶段调优策略。
- **结果**: 达到最先进性能，具体数值见全文。

### MonoCD: Monocular 3D Object Detection with Complementary Depths. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2404.03181](https://arxiv.org/abs/2404.03181) · 📚 被引 74
- **作者**: Longfei Yan, Pei Yan, Shengzhou Xiong, Xuanyu Xiang, Yihua Tan
- **🏷️ 机构**: School of Artificial Intelligence and Automation, Huazhong University of Science and Technology,Hubei Engineering Research Center of Machine Vision and Intelligent Systems,China
- **会议**: CVPR 2024
- **摘要（中）**: ①针对单目3D检测中多深度预测误差同号导致精度受限的问题。②提出MonoCD，增加互补深度分支利用全局深度线索，并利用几何关系增强深度互补性。③相比现有方法，通过降低深度预测相关性提升组合精度。④在KITTI等数据集上取得显著提升，具体数值见全文。
- **摘要（英）**: This paper addresses correlated depth errors in monocular 3D detection, proposing MonoCD with a complementary depth branch and geometric relation exploitation. It reduces error correlation and improves accuracy, with significant gains on KITTI.
- **核心贡献**: 提出互补深度机制提升单目3D检测精度。
- **创新点**: 全局深度分支和几何关系增强互补性。
- **结果**: 在KITTI上取得显著性能提升。

### Improving Distant 3D Object Detection Using 2D Box Supervision. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2403.09230](https://arxiv.org/abs/2403.09230) · 📚 被引 9
- **作者**: Zetong Yang, Zhiding Yu, Christopher B. Choy, Renhao Wang, Anima Anandkumar, José M. Álvarez
- **🏷️ 机构**: CUHK, NVIDIA, UC Berkeley
- **会议**: CVPR 2024
- **摘要（中）**: ①该论文针对相机-based 3D检测中远距离物体（>200m）因LiDAR点云稀疏导致3D标注困难、检测性能下降的问题。②提出了LR3D框架，通过隐式投影头学习近处物体3D标注与2D框之间的映射关系，从而仅利用2D框监督来估计远距离物体的深度，实现远距离3D检测。③相比现有方法，LR3D无需远距离3D标注，利用近处物体的3D监督迁移到远处，降低了标注成本并扩展了检测范围。④实验表明，在没有远距离3D标注的情况下，LR3D使相机-based方法在超过200米的距离上达到与完全3D监督相当的检测精度，且框架具有通用性，可广泛适用于多种3D检测方法。
- **摘要（英）**: This paper addresses the challenge of distant 3D object detection in camera-based systems, where LiDAR point sparsity limits 3D annotation quality. The proposed LR3D framework learns an implicit projection head to map 2D boxes to depth using nearby 3D supervision, enabling depth estimation for distant objects with only 2D box annotations. Experiments demonstrate that LR3D achieves comparable accuracy to full 3D supervision for objects beyond 200 meters, offering a general and cost-effective solution for long-range 3D detection.
- **核心贡献**: 提出LR3D框架，利用2D框监督和近处3D标注的映射学习，实现远距离物体的3D检测。
- **创新点**: 通过隐式投影头学习2D框到深度的映射，将近处监督迁移至远处，避免远距离3D标注需求。
- **结果**: 在无远距离3D标注下，LR3D使相机-based方法在200米以上距离达到与完全3D监督相当的精度。

### IS-Fusion: Instance-Scene Collaborative Fusion for Multimodal 3D Object Detection. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2403.15241](https://arxiv.org/abs/2403.15241) · 📚 被引 110
- **作者**: Junbo Yin, Jianbing Shen, Runnan Chen, Wei Li, Ruigang Yang, Pascal Frossard et al.
- **🏷️ 机构**: School of Computer Science and Technology, Beijing Institute of Technology, SKL-IOTSC, CIS, University of Macau, The University of Hong Kong
- **会议**: CVPR 2024
- **摘要（中）**: 针对BEV表示中物体尺寸小、点云稀疏导致3D感知可靠性差的问题，提出IS-Fusion多模态融合框架，联合捕获实例级和场景级上下文信息。通过层级场景融合模块（HSF）和实例引导融合模块（IGF），在不同粒度上融合多模态场景上下文，并利用实例候选增强场景特征。相比仅关注BEV场景级融合的现有方法，显式引入实例级多模态信息，提升实例中心任务性能。在挑战性数据集上验证了有效性。
- **摘要（英）**: To address the challenges of small object sizes and sparse point clouds in BEV representation for reliable 3D perception, this paper proposes IS-Fusion, a multimodal fusion framework that jointly captures instance- and scene-level contextual information. It introduces Hierarchical Scene Fusion (HSF) and Instance-Guided Fusion (IGF) modules to fuse multimodal context at different granularities and enhance scene features with instance guidance. Unlike existing BEV-only fusion methods, it explicitly incorporates instance-level information, improving instance-centric tasks like 3D detection. Experiments on challenging datasets demonstrate its effectiveness.
- **核心贡献**: 提出IS-Fusion框架，首次在BEV融合中显式结合实例级与场景级多模态上下文。
- **创新点**: 设计HSF和IGF模块，实现多粒度场景融合与实例引导的BEV特征增强。
- **结果**: 在挑战性数据集上验证了实例级融合对3D检测性能的提升。

### Pseudo Label Refinery for Unsupervised Domain Adaptation on Cross-Dataset 3D Object Detection. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2404.19384](https://arxiv.org/abs/2404.19384) · 📚 被引 12
- **作者**: Zhanwei Zhang, Minghao Chen, Shuai Xiao, Liang Peng, Hengjia Li, Binbin Lin et al.
- **🏷️ 机构**: Zhejiang University,State Key Lab of CAD&#x0026;CG, School of Computer Sciene and Technology, Hangzhou Dianzi University, Alibaba Group
- **会议**: CVPR 2024
- **摘要（中）**: 针对无监督域适应3D检测中伪标签选择引入不可靠3D框、污染训练过程的问题，提出伪标签精炼框架。通过互补增强策略，移除不可靠框内点或替换为高置信框，提高伪标签可靠性。同时，针对高束与低束数据集点数量差异，生成额外提议并对齐RoI特征。实验证明该方法在跨数据集3D检测域适应中有效。
- **摘要（英）**: To address the issue of unreliable pseudo labels in unsupervised domain adaptation for 3D object detection, this paper proposes a pseudo label refinery framework. It introduces a complementary augmentation strategy to remove or replace unreliable boxes, and generates additional proposals with RoI feature alignment to handle point density differences across domains. Experiments demonstrate improved performance in cross-dataset 3D detection adaptation.
- **核心贡献**: 提出伪标签精炼框架，通过互补增强和RoI对齐提升3D UDA性能。
- **创新点**: 设计互补增强策略和跨域RoI特征对齐，有效处理不可靠伪标签。
- **结果**: 实验验证了在跨数据集3D检测域适应中的性能提升。

### SAFDNet: A Simple and Effective Network for Fully Sparse 3D Object Detection. **⭐⭐⭐⭐** (相关度: 88%)
- **链接**: [arXiv:2403.05817](https://arxiv.org/abs/2403.05817) · 📚 被引 78
- **作者**: Gang Zhang, Junnan Chen, Guohuan Gao, Jianmin Li, Si Liu, Xiaolin Hu
- **🏷️ 机构**: Institute for AI, BNRist, Tsinghua University,Department of Computer Science and Technology, Huazhong University of Science and Technology, Beijing Institute of Technology
- **会议**: CVPR 2024
- **摘要（中）**: 针对现有3D检测器依赖密集特征图导致计算成本随感知范围平方增长、难以扩展至长距离检测的问题，提出SAFDNet全稀疏3D检测架构。设计自适应特征扩散策略解决中心特征缺失问题。在Waymo Open、nuScenes和Argoverse2数据集上实验，在长距离检测场景（Argoverse2）上显著优于现有SOTA，验证了其有效性。
- **摘要（英）**: To address the quadratic computational cost of dense feature maps in 3D detectors and enable long-range detection, this paper proposes SAFDNet, a fully sparse 3D detection architecture. It introduces an adaptive feature diffusion strategy to handle missing center features. Experiments on Waymo Open, nuScenes, and Argoverse2 show superior performance, especially on long-range scenarios, demonstrating its efficacy.
- **核心贡献**: 提出SAFDNet，实现全稀疏3D检测，显著提升长距离场景性能。
- **创新点**: 设计自适应特征扩散策略，解决稀疏检测中的中心特征缺失问题。
- **结果**: 在Argoverse2上大幅超越SOTA，验证长距离检测优势。

### CaKDP: Category-Aware Knowledge Distillation and Pruning Framework for Lightweight 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01452) · 📚 被引 17
- **作者**: Haonan Zhang, Longjun Liu, Yuqi Huang, Zhao Yang, Xinyu Lei, Bihan Wen
- **🏷️ 机构**: National Engineering Research Center for Visual Information and Applications, and Institute of Artificial Intelligence and Robotics, Xi&#x0027;an Jiaotong University,National Key Laboratory of Human-Machine Hybrid Augmented Intelligence, Nanyang Technological University
- **会议**: CVPR 2024

### Decoupled Pseudo-Labeling for Semi-Supervised Monocular 3D Object Detection.
- **链接**: [arXiv:2403.17387](https://arxiv.org/abs/2403.17387) · 📚 被引 21
- **作者**: Jiacheng Zhang, Jiaming Li, Xiangru Lin, Wei Zhang, Xiao Tan, Junyu Han et al.
- **🏷️ 机构**: School of Computer Science and Engineering, Sun Yat-sen University,Guangzhou,China, Baidu Inc.,Department of Computer Vision Technology (VIS),China
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > We delve into pseudo-labeling for semi-supervised monocular 3D object detection (SSM3OD) and discover two primary issues: a misalignment between the prediction quality of 3D and 2D attributes and the tendency of depth supervision derived from pseudo-labels to be noisy, leading to significant optimization conflicts with other reliable forms of supervision. We introduce a novel decoupled pseudo-labeling (DPL) approach for SSM3OD. Our approach features a Decoupled Pseudo-label Generation (DPG) module, designed to efficiently generate pseudo-labels by separately processing 2D and 3D attributes. This module incorporates a unique homography-based method for identifying dependable pseudo-labels in BEV space, specifically for 3D attributes. Additionally, we present a DepthGradient Projection (DGP) module to mitigate optimization conflicts caused by noisy depth supervision of pseudo-labels, effectively decoupling the depth gradient and removing conflicting gradients. This dual decoupling strategy-at both the pseudo-label generation and gradient levels-significantly improves the utilization of pseudo-labels in SSM3OD. Our comprehensive experiments on the KITTI benchmark demonstrate the superiority of our method over existing approaches.

### Prompt3D: Random Prompt Assisted Weakly-Supervised 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02649) · 📚 被引 5
- **作者**: Xiaohong Zhang, Huisheng Ye, Jingwen Li, Qinyu Tang, Yuanqi Li, Yanwen Guo et al.
- **🏷️ 机构**: Nanjing University
- **会议**: CVPR 2024

### CRKD: Enhanced Camera-Radar Object Detection with Cross-Modality Knowledge Distillation.
- **链接**: [arXiv:2403.19104](https://arxiv.org/abs/2403.19104) · 📚 被引 35
- **作者**: Lingjun Zhao, Jingyu Song, Katherine A. Skinner
- **🏷️ 机构**: University of Michigan,Ann Arbor,MI,USA
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > In the field of 3D object detection for autonomous driving, LiDAR-Camera (LC) fusion is the top-performing sensor configuration. Still, LiDAR is relatively high cost, which hinders adoption of this technology for consumer automobiles. Alternatively, camera and radar are commonly deployed on vehicles already on the road today, but performance of Camera-Radar (CR) fusion falls behind LC fusion. In this work, we propose Camera-Radar Knowledge Distillation (CRKD) to bridge the performance gap between LC and CR detectors with a novel cross-modality KD framework. We use the Bird's-Eye-View (BEV) representation as the shared feature space to enable effective knowledge distillation. To accommodate the unique cross-modality KD path, we propose four distillation losses to help the student learn crucial features from the teacher model. We present extensive evaluations on the nuScenes dataset to demonstrate the effectiveness of the proposed CRKD framework. The project page for CRKD is https://song-jingyu.github.io/CRKD.

### Three Pillars Improving Vision Foundation Model Distillation for Lidar.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02033) · 📚 被引 28
- **作者**: Gilles Puy, Spyros Gidaris, Alexandre Boulch, Oriane Siméoni, Corentin Sautier, Patrick Pérez et al.
- **🏷️ 机构**: valeo.ai,Paris,France, Kyutai,Paris,France
- **会议**: CVPR 2024

### Visual Point Cloud Forecasting Enables Scalable Autonomous Driving.
- **链接**: [arXiv:2312.17655](https://arxiv.org/abs/2312.17655) · 📚 被引 58
- **作者**: Zetong Yang, Li Chen, Yanan Sun, Hongyang Li
- **🏷️ 机构**: OpenDriveLab and Shanghai AI Lab
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > In contrast to extensive studies on general vision, pre-training for scalable visual autonomous driving remains seldom explored. Visual autonomous driving applications require features encompassing semantics, 3D geometry, and temporal information simultaneously for joint perception, prediction, and planning, posing dramatic challenges for pre-training. To resolve this, we bring up a new pre-training task termed as visual point cloud forecasting - predicting future point clouds from historical visual input. The key merit of this task captures the synergic learning of semantics, 3D structures, and temporal dynamics. Hence it shows superiority in various downstream tasks. To cope with this new problem, we present ViDAR, a general model to pre-train downstream visual encoders. It first extracts historical embeddings by the encoder. These representations are then transformed to 3D geometric space via a novel Latent Rendering operator for future point cloud prediction. Experiments show significant gain in downstream tasks, e.g., 3.1% NDS on 3D detection, ~10% error reduction on motion forecasting, and ~15% less collision rate on planning.

### Collaborative Semantic Occupancy Prediction with Hybrid Feature Fusion in Connected Automated Vehicles.
- **链接**: [arXiv:2402.07635](https://arxiv.org/abs/2402.07635) · 📚 被引 40
- **作者**: Rui Song, Chenwei Liang, Hu Cao, Zhiran Yan, Walter Zimmer, Markus Gross et al.
- **🏷️ 机构**: Fraunhofer IVI, Technical University of Munich, Technische Hochschule Ingolstadt
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Collaborative perception in automated vehicles leverages the exchange of information between agents, aiming to elevate perception results. Previous camera-based collaborative 3D perception methods typically employ 3D bounding boxes or bird's eye views as representations of the environment. However, these approaches fall short in offering a comprehensive 3D environmental prediction. To bridge this gap, we introduce the first method for collaborative 3D semantic occupancy prediction. Particularly, it improves local 3D semantic occupancy predictions by hybrid fusion of (i) semantic and occupancy task features, and (ii) compressed orthogonal attention features shared between vehicles. Additionally, due to the lack of a collaborative perception dataset designed for semantic occupancy prediction, we augment a current collaborative perception dataset to include 3D collaborative semantic occupancy labels for a more robust evaluation. The experimental findings highlight that: (i) our collaborative semantic occupancy predictions excel above the results from single vehicles by over 30%, and (ii) models anchored on semantic occupancy outpace state-of-the-art collaborative 3D detection techniques in subsequent perception applications, showcasing enhanced accuracy and enriched semantic-awareness in road environments.

### SelfOcc: Self-Supervised Vision-Based 3D Occupancy Prediction.
- **链接**: [arXiv:2311.12754](https://arxiv.org/abs/2311.12754) · 📚 被引 79
- **作者**: Yuanhui Huang, Wenzhao Zheng, Borui Zhang, Jie Zhou, Jiwen Lu
- **🏷️ 机构**: Beijing National Research Center for Information Science and Technology,China, Tsinghua University,Department of Automation,China
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > 3D occupancy prediction is an important task for the robustness of vision-centric autonomous driving, which aims to predict whether each point is occupied in the surrounding 3D space. Existing methods usually require 3D occupancy labels to produce meaningful results. However, it is very laborious to annotate the occupancy status of each voxel. In this paper, we propose SelfOcc to explore a self-supervised way to learn 3D occupancy using only video sequences. We first transform the images into the 3D space (e.g., bird's eye view) to obtain 3D representation of the scene. We directly impose constraints on the 3D representations by treating them as signed distance fields. We can then render 2D images of previous and future frames as self-supervision signals to learn the 3D representations. We propose an MVS-embedded strategy to directly optimize the SDF-induced weights with multiple depth proposals. Our SelfOcc outperforms the previous best method SceneRF by 58.7% using a single frame as input on SemanticKITTI and is the first self-supervised work that produces reasonable 3D occupancy for surround cameras on nuScenes. SelfOcc produces high-quality depth and achieves state-of-the-art results on novel depth synthesis, monocular depth estimation, and surround-view depth estimation on the SemanticKITTI, KITTI-2015, and nuScenes, respectively. Code: https://github.com/huang-yh/SelfOcc.

### SparseOcc: Rethinking Sparse Latent Representation for Vision-Based Semantic Occupancy Prediction.
- **链接**: [arXiv:2404.09502](https://arxiv.org/abs/2404.09502) · 📚 被引 51
- **作者**: Pin Tang, Zhongdao Wang, Guoqing Wang, Jilai Zheng, Xiangxuan Ren, Bailan Feng et al.
- **🏷️ 机构**: MoE Key Lab of Artificial Intelligence, AI Institute, Shanghai Jiao Tong University, Huawei Noah&#x0027;s Ark Lab
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Vision-based perception for autonomous driving requires an explicit modeling of a 3D space, where 2D latent representations are mapped and subsequent 3D operators are applied. However, operating on dense latent spaces introduces a cubic time and space complexity, which limits scalability in terms of perception range or spatial resolution. Existing approaches compress the dense representation using projections like Bird's Eye View (BEV) or Tri-Perspective View (TPV). Although efficient, these projections result in information loss, especially for tasks like semantic occupancy prediction. To address this, we propose SparseOcc, an efficient occupancy network inspired by sparse point cloud processing. It utilizes a lossless sparse latent representation with three key innovations. Firstly, a 3D sparse diffuser performs latent completion using spatially decomposed 3D sparse convolutional kernels. Secondly, a feature pyramid and sparse interpolation enhance scales with information from others. Finally, the transformer head is redesigned as a sparse variant. SparseOcc achieves a remarkable 74.9% reduction on FLOPs over the dense baseline. Interestingly, it also improves accuracy, from 12.8% to 14.1% mIOU, which in part can be attributed to the sparse representation's ability to avoid hallucinations on empty voxels.

### DriveWorld: 4D Pre-Trained Scene Understanding via World Models for Autonomous Driving.
- **链接**: [arXiv:2405.04390](https://arxiv.org/abs/2405.04390) · 📚 被引 33
- **作者**: Chen Min, Dawei Zhao, Liang Xiao, Jian Zhao, Xinli Xu, Zheng Zhu et al.
- **🏷️ 机构**: School of Computer Science, Peking University, Unmanned Systems Technology Research Center, Defense Innovation Institute, China Telecom Institute of AI &#x0026; NPU
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Vision-centric autonomous driving has recently raised wide attention due to its lower cost. Pre-training is essential for extracting a universal representation. However, current vision-centric pre-training typically relies on either 2D or 3D pre-text tasks, overlooking the temporal characteristics of autonomous driving as a 4D scene understanding task. In this paper, we address this challenge by introducing a world model-based autonomous driving 4D representation learning framework, dubbed \emph{DriveWorld}, which is capable of pre-training from multi-camera driving videos in a spatio-temporal fashion. Specifically, we propose a Memory State-Space Model for spatio-temporal modelling, which consists of a Dynamic Memory Bank module for learning temporal-aware latent dynamics to predict future changes and a Static Scene Propagation module for learning spatial-aware latent statics to offer comprehensive scene contexts. We additionally introduce a Task Prompt to decouple task-aware features for various downstream tasks. The experiments demonstrate that DriveWorld delivers promising results on various autonomous driving tasks. When pre-trained with the OpenScene dataset, DriveWorld achieves a 7.5% increase in mAP for 3D object detection, a 3.0% increase in IoU for online mapping, a 5.0% increase in AMOTA for multi-object tracking, a 0.1m decrease in minADE for motion forecasting, a 3.0% increase in IoU for occupancy prediction, and a 0.34m reduction in average L2 error for planning.

### UniPAD: A Universal Pre-Training Paradigm for Autonomous Driving.
- **链接**: [arXiv:2310.08370](https://arxiv.org/abs/2310.08370) · 📚 被引 42
- **作者**: Honghui Yang, Sha Zhang, Di Huang, Xiaoyang Wu, Haoyi Zhu, Tong He et al.
- **🏷️ 机构**: Zhejiang University,State Key Lab of CAD&#x0026;CG, Shanghai Artificial Intelligence Laboratory, HongKong University
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > In the context of autonomous driving, the significance of effective feature learning is widely acknowledged. While conventional 3D self-supervised pre-training methods have shown widespread success, most methods follow the ideas originally designed for 2D images. In this paper, we present UniPAD, a novel self-supervised learning paradigm applying 3D volumetric differentiable rendering. UniPAD implicitly encodes 3D space, facilitating the reconstruction of continuous 3D shape structures and the intricate appearance characteristics of their 2D projections. The flexibility of our method enables seamless integration into both 2D and 3D frameworks, enabling a more holistic comprehension of the scenes. We manifest the feasibility and effectiveness of UniPAD by conducting extensive experiments on various downstream 3D tasks. Our method significantly improves lidar-, camera-, and lidar-camera-based baseline by 9.1, 7.7, and 6.9 NDS, respectively. Notably, our pre-training pipeline achieves 73.2 NDS for 3D object detection and 79.4 mIoU for 3D semantic segmentation on the nuScenes validation set, achieving state-of-the-art results in comparison with previous methods. The code will be available at https://github.com/Nightmare-n/UniPAD.

### Volumetric Environment Representation for Vision-Language Navigation.
- **链接**: [arXiv:2403.14158](https://arxiv.org/abs/2403.14158) · 📚 被引 43
- **作者**: Rui Liu, Wenguan Wang, Yi Yang
- **🏷️ 机构**: Zhejiang University,ReLER, CCAI
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Vision-language navigation (VLN) requires an agent to navigate through an 3D environment based on visual observations and natural language instructions. It is clear that the pivotal factor for successful navigation lies in the comprehensive scene understanding. Previous VLN agents employ monocular frameworks to extract 2D features of perspective views directly. Though straightforward, they struggle for capturing 3D geometry and semantics, leading to a partial and incomplete environment representation. To achieve a comprehensive 3D representation with fine-grained details, we introduce a Volumetric Environment Representation (VER), which voxelizes the physical world into structured 3D cells. For each cell, VER aggregates multi-view 2D features into such a unified 3D space via 2D-3D sampling. Through coarse-to-fine feature extraction and multi-task learning for VER, our agent predicts 3D occupancy, 3D room layout, and 3D bounding boxes jointly. Based on online collected VERs, our agent performs volume state estimation and builds episodic memory for predicting the next step. Experimental results show our environment representations from multi-task learning lead to evident performance gains on VLN. Our model achieves state-of-the-art performance across VLN benchmarks (R2R, REVERIE, and R4R).
