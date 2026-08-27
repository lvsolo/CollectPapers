# Multi-camera Perception — 2022 Guideline

> 领域: 多相机 / 多视角感知（环视、深度估计与 3D 预测）
> 论文数: 35 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: [2024](Guideline%202024.md)

### PseCo: Pseudo Labeling and Consistency Training for Semi-Supervised Object Detection. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2203.16317](https://arxiv.org/abs/2203.16317)
- **作者**: Gang Li, Xiang Li, Yujie Wang, Yichao Wu, Ding Liang, Shanshan Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对半监督目标检测中伪标签定位精度不足和一致性训练仅关注标签级而忽略特征级一致性的问题。②提出了PseCo框架，包含Noisy Pseudo box Learning (NPL)和Multi-view Scale-invariant Learning (MSL)两个模块，NPL通过Prediction-guided Label Assignment和Positive-proposal Consistency Voting处理噪声伪框，MSL引入多视图尺度不变学习。③相比现有方法，同时优化了伪标签的定位质量和特征级一致性，更贴合目标检测的特性。④在COCO等标准基准上显著提升了半监督检测性能，尤其在低标注比例下表现突出。
- **摘要（英）**: This paper addresses the issues of imprecise pseudo boxes and insufficient feature-level consistency in semi-supervised object detection. It proposes PseCo with NPL and MSL modules to improve localization quality and scale invariance. The method achieves significant performance gains on COCO benchmarks, especially under low annotation ratios.
- **核心贡献**: 提出了PseCo框架，通过NPL和MSL分别解决伪标签定位噪声和特征级一致性问题。
- **创新点**: 创新性地将预测引导的标签分配和正提议一致性投票用于伪标签质量提升，并引入多视图尺度不变学习。
- **结果**: 在COCO基准上显著提升半监督检测精度，低标注比例下性能提升尤为明显。

### MVSalNet: Multi-view Augmentation for RGB-D Salient Object Detection. **⭐⭐** (相关度: 30%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19818-2_16) · 📚 被引 29
- **作者**: Jiayuan Zhou, Lijun Wang, Huchuan Lu, Kaining Huang, Xinchu Shi, Bocong Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对RGB-D显著目标检测中多视图信息利用不足的问题。②提出了MVSalNet，通过多视图增强策略提升深度和RGB特征的融合效果。③相比单视图方法，增强了跨视图的互补性。④摘要缺失，无法提供具体数据。
- **摘要（英）**: This paper proposes MVSalNet for RGB-D salient object detection with multi-view augmentation. It enhances feature fusion across views but lacks detailed experimental results in the abstract.
- **核心贡献**: 提出多视图增强的RGB-D显著目标检测网络。
- **创新点**: 多视图增强策略用于RGB-D特征融合。
- **结果**: 未提供具体性能数据。

### Sequential Multi-view Fusion Network for Fast LiDAR Point Motion Estimation. **⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20047-2_17) · 📚 被引 3
- **作者**: Gang Zhang, Xiaoyan Li, Zhenhua Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对LiDAR点云运动估计的实时性问题。②提出了序列多视图融合网络，通过多帧信息融合加速运动估计。③相比单帧方法，利用了时序信息提升准确性。④摘要缺失，无法提供具体数据。
- **摘要（英）**: This paper introduces a sequential multi-view fusion network for fast LiDAR point motion estimation. It leverages temporal information across frames but lacks detailed results in the abstract.
- **核心贡献**: 提出序列多视图融合网络用于LiDAR运动估计。
- **创新点**: 多帧时序融合策略提升运动估计速度。
- **结果**: 未提供具体性能数据。

### RC-MVSNet: Unsupervised Multi-View Stereo with Neural Rendering. **⭐⭐⭐⭐** (相关度: 50%)
- **链接**: [arXiv:2203.03949](https://arxiv.org/abs/2203.03949) · 📚 被引 54
- **作者**: Di Chang, Aljaz Bozic, Tong Zhang, Qingsong Yan, Yingcong Chen, Sabine Süsstrunk et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对无监督多视图立体匹配中非朗伯表面和遮挡导致的对应关系歧义问题。②提出了RC-MVSNet，引入神经渲染的深度渲染一致性损失和参考视图合成损失。③相比现有无监督方法，通过几何约束和合成监督缓解了光照和遮挡影响。④在DTU和Tanks&Temples基准上达到无监督SOTA，性能接近有监督方法。
- **摘要（英）**: This paper addresses correspondence ambiguity in unsupervised MVS caused by non-Lambertian surfaces and occlusions. RC-MVSNet introduces depth rendering consistency and reference view synthesis losses. It achieves state-of-the-art unsupervised performance on DTU and Tanks&Temples, competitive with supervised methods.
- **核心贡献**: 提出基于神经渲染的无监督MVS方法，解决遮挡和非朗伯表面问题。
- **创新点**: 深度渲染一致性损失和参考视图合成损失联合优化。
- **结果**: 在DTU和Tanks&Temples上达到无监督SOTA，接近有监督性能。

### KD-MVS: Knowledge Distillation Based Self-supervised Learning for Multi-view Stereo. **⭐⭐⭐** (相关度: 45%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19821-2_36) · 📚 被引 31
- **作者**: Yikang Ding, Qingtian Zhu, Xiangyue Liu, Wentao Yuan, Haotian Zhang, Chi Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对多视图立体匹配自监督学习中的标签噪声问题。②提出了基于知识蒸馏的自监督学习方法KD-MVS。③相比传统自监督方法，通过蒸馏教师模型知识提升学生模型鲁棒性。④摘要缺失，无法提供具体数据。
- **摘要（英）**: This paper proposes KD-MVS, a knowledge distillation-based self-supervised learning method for multi-view stereo. It aims to reduce label noise but lacks detailed results in the abstract.
- **核心贡献**: 提出知识蒸馏驱动的自监督MVS方法。
- **创新点**: 利用教师模型知识增强学生模型的自监督学习。
- **结果**: 未提供具体性能数据。

### FLEX: Extrinsic Parameters-free Multi-view 3D Human Motion Reconstruction. **⭐⭐⭐** (相关度: 55%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19827-4_11) · 📚 被引 31
- **作者**: Brian Gordon, Sigal Raab, Guy Azov, Raja Giryes, Daniel Cohen-Or
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对多视角3D人体运动重建中依赖相机外参的问题。②提出了FLEX方法，无需外参即可重建3D人体运动。③相比传统方法，消除了标定需求，提升了实用性。④摘要缺失，无法提供具体数据。
- **摘要（英）**: This paper introduces FLEX for multi-view 3D human motion reconstruction without extrinsic parameters. It removes calibration requirements, enhancing practicality, but lacks detailed results in the abstract.
- **核心贡献**: 提出无需外参的多视角3D人体运动重建方法。
- **创新点**: 去除外参依赖，简化多相机系统部署。
- **结果**: 未提供具体性能数据。

### Depth Field Networks For Generalizable Multi-view Scene Representation. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2207.14287](https://arxiv.org/abs/2207.14287) · 📚 被引 13
- **作者**: Vitor Guizilini, Igor Vasiljevic, Jiading Fang, Rare Ambru, Greg Shakhnarovich, Matthew R. Walter et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对多视角场景表示中传统几何约束（如代价体、极线约束）导致领域泛化差的问题，提出深度场网络（DeFiNe），学习隐式多视角一致场景表示，并引入3D数据增强作为几何先验以增加视角多样性，同时将视图合成作为辅助任务提升深度估计。相比依赖显式几何约束的专用架构，该方法无需几何约束即可在立体和视频深度估计上达到最先进水平，并在零样本领域泛化上大幅提升。
- **摘要（英）**: To address poor domain generalization in multi-view scene representation caused by explicit geometric constraints, this paper proposes Depth Field Networks (DeFiNe), which learn an implicit multi-view consistent representation with 3D data augmentation as geometric prior and view synthesis as auxiliary task. Without explicit geometric constraints, DeFiNe achieves state-of-the-art results in stereo and video depth estimation and significantly improves zero-shot domain generalization.
- **核心贡献**: 提出无需显式几何约束的隐式多视角场景表示方法，提升深度估计的泛化能力。
- **创新点**: 将几何先验编码为输入而非约束，并引入3D数据增强和视图合成辅助任务。
- **结果**: 在立体和视频深度估计上达到最先进水平，零样本泛化大幅提升。

### Emotion-aware Multi-view Contrastive Learning for Facial Emotion Recognition. **⭐⭐** (相关度: 30%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19778-9_11) · 📚 被引 16
- **作者**: Dae Ha Kim, Byung Cheol Song
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 该论文针对面部表情识别中多视角信息利用不足的问题，提出情感感知的多视角对比学习方法，通过融合情感标签和跨视角特征增强表示。但摘要缺失，无法评估具体方法细节和实验效果。
- **摘要（英）**: This paper addresses insufficient multi-view information utilization in facial emotion recognition by proposing an emotion-aware multi-view contrastive learning method that integrates emotion labels and cross-view features. However, the abstract is missing, making it impossible to assess specific methods and results.
- **核心贡献**: 提出情感感知的多视角对比学习框架用于面部表情识别。
- **创新点**: 将情感标签融入多视角对比学习。
- **结果**: 未提供具体实验结果。

### MODE: Multi-view Omnidirectional Depth Estimation with 360$\circ $ Cameras. **⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19827-4_12)
- **作者**: Ming Li, Xueqian Jin, Xuejiao Hu, Jingzhao Dai, Sidan Du, Yang Li
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 该论文针对360度相机全景深度估计问题，提出多视角全向深度估计方法（MODE），利用多视角几何和全景图像特性提升深度精度。但摘要缺失，无法评估具体技术细节和性能数据。
- **摘要（英）**: This paper addresses omnidirectional depth estimation with 360-degree cameras by proposing a multi-view method that leverages panoramic geometry. However, the abstract is missing, so specific techniques and results cannot be assessed.
- **核心贡献**: 提出多视角全向深度估计方法。
- **创新点**: 结合全景相机多视角几何进行深度估计。
- **结果**: 未提供具体实验结果。

### PPT: Token-Pruned Pose Transformer for Monocular and Multi-view Human Pose Estimation. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2209.08194](https://arxiv.org/abs/2209.08194) · 📚 被引 76
- **作者**: Haoyu Ma, Zhe Wang, Yifei Chen, Deying Kong, Liangjian Chen, Xingwei Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对视觉Transformer在人体姿态估计中全局注意力计算开销大的问题，提出Token剪枝姿态Transformer（PPT），通过定位粗略人体掩膜并仅对选定token进行自注意力，降低计算量。进一步扩展到多视角姿态估计，提出人体区域融合策略，将所有人前景像素作为对应候选。在COCO和MPII上，PPT在保持精度的同时减少计算，在多视角数据集上实现高效融合并达到新最先进水平。
- **摘要（英）**: To reduce computational cost of global attention in vision transformers for pose estimation, this paper proposes token-Pruned Pose Transformer (PPT), which locates a rough human mask and performs self-attention only on selected tokens. Extended to multi-view with human area fusion, PPT matches accuracy of previous methods while reducing computation on COCO and MPII, and achieves state-of-the-art on multi-view datasets.
- **核心贡献**: 提出token剪枝机制和跨视角融合策略，提升姿态估计效率。
- **创新点**: 基于人体掩膜的token剪枝和人体区域融合。
- **结果**: 在COCO和MPII上精度匹配且计算减少，多视角数据集上达到新最先进水平。

### Neural Strands: Learning Hair Geometry and Appearance from Multi-view Images. **⭐⭐⭐** (相关度: 50%)
- **链接**: [arXiv:2207.14067](https://arxiv.org/abs/2207.14067) · 📚 被引 42
- **作者**: Radu Alexandru Rosu, Shunsuke Saito, Ziyan Wang, Chenglei Wu, Sven Behnke, Giljoo Nam
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对多视角图像中头发几何和外观建模的挑战，提出Neural Strands框架，基于神经头皮纹理编码每根发丝的几何和外观，并通过光栅化实现实时渲染。引入多视角几何先验，首次实现外观和显式头发几何的联合学习。实验证明该方法在保真度和效率上优于体积方法，支持实时高保真渲染。
- **摘要（英）**: For modeling hair geometry and appearance from multi-view images, this paper proposes Neural Strands, using a neural scalp texture to encode per-strand geometry and appearance, with rasterization-based neural rendering for real-time view-dependent effects. Jointly learning appearance and explicit geometry with multi-view priors, it achieves high fidelity and efficiency for various hairstyles.
- **核心贡献**: 提出基于神经纹理的头发几何和外观联合建模方法。
- **创新点**: 神经头皮纹理和光栅化神经渲染。
- **结果**: 实现实时高保真渲染，优于体积方法。

### A Real World Dataset for Multi-view 3D Reconstruction. **⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2203.11397](https://arxiv.org/abs/2203.11397) · 📚 被引 10
- **作者**: Rakesh Shrestha, Siqi Hu, Minghao Gou, Ziyuan Liu, Ping Tan
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对多视角3D重建缺乏真实世界基准数据集的问题。②构建了包含998个日常桌面物体3D模型和84.7万张真实RGB-D图像的数据集，并半自动标注相机位姿和物体位姿。③相比合成数据集，提供了真实世界的多视角图像和精确标注，填补了该任务基准的空白。④数据集和标注工具、评估基线已公开，可支持形状重建、姿态估计等任务。
- **摘要（英）**: This paper addresses the lack of real-world benchmarks for multi-view 3D reconstruction by presenting a dataset of 998 3D models with 847,000 real RGB-D images and semi-automated pose annotations. It fills the gap by providing accurate real-world data, and the dataset, tools, and baselines are publicly available.
- **核心贡献**: 提供了大规模真实世界多视角3D重建数据集及标注工具。
- **创新点**: 半自动化的相机和物体位姿标注流程。
- **结果**: 公开了998个物体和84.7万张图像的数据集，支持多种3D任务。

### MVSTER: Epipolar Transformer for Efficient Multi-view Stereo. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2204.07346](https://arxiv.org/abs/2204.07346) · 📚 被引 115
- **作者**: Xiaofeng Wang, Zheng Zhu, Guan Huang, Fangbo Qin, Yun Ye, Yijia He et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对学习型多视角立体（MVS）方法在代价体融合时未充分利用3D空间关联且计算开销大的问题。②提出了MVSTER，利用极线Transformer高效学习2D语义和3D空间关联，采用可分离的单目深度估计器增强2D语义，并通过交叉注意力沿极线构建数据相关的3D关联。③相比MVSNet和CasMVSNet，在DTU基准上分别获得34%和14%的相对提升，同时效率显著提高。④实验表明达到了最先进的重建性能。
- **摘要（英）**: This paper tackles inefficient cost volume fusion in MVS by proposing MVSTER, which uses an epipolar Transformer to jointly learn 2D semantics and 3D spatial associations, with a detachable monocular depth estimator. It achieves 34% and 14% relative improvements over MVSNet and CasMVSNet on DTU, with higher efficiency.
- **核心贡献**: 提出极线Transformer架构，高效融合2D和3D信息用于MVS。
- **创新点**: 利用交叉注意力沿极线构建数据相关的3D关联。
- **结果**: 在DTU基准上实现最先进性能，相对MVSNet提升34%。

### Incomplete Multi-view Domain Adaptation via Channel Enhancement and Knowledge Transfer. **⭐⭐** (相关度: 40%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19830-4_12) · 📚 被引 5
- **作者**: Haifeng Xia, Pu Wang, Zhengming Ding
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对不完整多视角域适应问题，即不同视角数据缺失且分布不一致。②提出了通道增强和知识迁移的方法，但摘要内容不完整，缺乏具体技术细节。③改进点不明确，可能涉及特征通道增强和跨域知识迁移。④效果未在摘要中给出。
- **摘要（英）**: This paper addresses incomplete multi-view domain adaptation with channel enhancement and knowledge transfer, but the abstract lacks technical details and results, limiting its assessment.
- **核心贡献**: 提出通道增强和知识迁移策略用于不完整多视角域适应。
- **创新点**: 结合通道增强与知识迁移处理数据缺失和分布偏移。
- **结果**: 未报告具体效果。

### PS-NeRF: Neural Inverse Rendering for Multi-view Photometric Stereo. **⭐⭐⭐⭐** (相关度: 65%)
- **链接**: [arXiv:2207.11406](https://arxiv.org/abs/2207.11406) · 📚 被引 69
- **作者**: Wenqi Yang, Guanying Chen, Chaofeng Chen, Zhenfang Chen, Kwan-Yee K. Wong
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对传统多视角光度立体（MVPS）方法多阶段分离导致误差累积的问题。②提出了PS-NeRF，一种基于隐式表示的神经逆渲染方法，联合估计几何、材质和光照。③利用多光图像估计每视角法线图以正则化神经辐射场，并通过阴影感知的可微渲染层联合优化法线、BRDF和光照。④在合成和真实数据集上，形状重建精度远超现有MVPS和神经渲染方法。
- **摘要（英）**: This paper addresses error accumulation in traditional MVPS by proposing PS-NeRF, a neural inverse rendering method that jointly estimates geometry, materials, and lights using implicit representation. It regularizes normals from multi-light images and optimizes via shadow-aware differentiable rendering, achieving far more accurate reconstruction than existing methods.
- **核心贡献**: 提出联合估计几何、材质和光照的神经逆渲染框架。
- **创新点**: 利用多光法线正则化和阴影感知渲染优化隐式表示。
- **结果**: 在合成和真实数据集上重建精度显著优于现有方法。

### MVDG: A Unified Multi-view Framework for Domain Generalization. **⭐⭐** (相关度: 50%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19812-0_10)
- **作者**: Jian Zhang, Lei Qi, Yinghuan Shi, Yang Gao
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对多视角域泛化问题，即模型在不同视角分布下泛化能力不足。②提出了统一的多视角框架MVDG，但摘要内容不完整，缺乏具体方法描述。③改进点可能涉及多视角特征融合和泛化策略。④效果未在摘要中给出。
- **摘要（英）**: This paper proposes a unified multi-view framework for domain generalization, but the abstract lacks details on methodology and results, making it difficult to evaluate.
- **核心贡献**: 提出统一多视角框架以提升域泛化能力。
- **创新点**: 多视角特征融合与泛化策略。
- **结果**: 未报告具体效果。

### Calibration-Free Multi-view Crowd Counting. **⭐⭐⭐** (相关度: 55%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20077-9_14) · 📚 被引 13
- **作者**: Qi Zhang, Antoni B. Chan
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对多视角人群计数中相机标定依赖和视角变化的问题。②提出了免标定的多视角人群计数方法，但摘要内容不完整，缺乏具体技术细节。③改进点可能涉及无需相机参数的自适应特征对齐。④效果未在摘要中给出。
- **摘要（英）**: This paper addresses calibration-free multi-view crowd counting, but the abstract lacks technical details and results, limiting its assessment.
- **核心贡献**: 提出免标定的多视角人群计数方法。
- **创新点**: 去除相机标定依赖，增强跨视角适应性。
- **结果**: 未报告具体效果。

### 3D Random Occlusion and Multi-layer Projection for Deep Multi-camera Pedestrian Localization. **⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2207.10895](https://arxiv.org/abs/2207.10895) · 📚 被引 35
- **作者**: Rui Qiu, Ming Xu, Yuyao Yan, Jeremy S. Smith, Xi Yang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对多视角相机行人定位中因遮挡导致性能下降以及标注数据稀缺易过拟合的问题，提出了一种3D随机遮挡（3D Random Occlusion）数据增强方法，在地面平面随机生成平均行人尺寸的3D圆柱体遮挡物并投影到多个视角，以缓解训练过拟合。同时，利用单应性将每个视角的特征图投影到不同高度的多个平行平面，使CNN能充分利用行人高度方向的特征来推断地面位置。在公开多视角数据集上，该方法相比最先进的基于深度学习的多视角行人检测方法取得了显著性能提升。
- **摘要（英）**: This paper addresses the issues of performance degradation under heavy occlusion and overfitting due to scarce annotated samples in multi-camera pedestrian localization. It proposes a 3D random occlusion augmentation that generates cylinder occlusions on the ground plane and projects them to multiple views, along with a multi-layer projection of feature maps at different heights via homographies to exploit height-wise features. The method achieves significantly improved performance over state-of-the-art deep learning baselines on multi-view pedestrian detection benchmarks.
- **核心贡献**: 提出了3D随机遮挡数据增强和多层投影特征融合方法，有效提升了多视角行人定位在遮挡场景下的鲁棒性。
- **创新点**: 创新性地将3D遮挡生成与多高度平面特征投影结合，增强了模型对遮挡和高度信息的利用。
- **结果**: 在多个多视角数据集上显著优于现有深度学习方法，验证了方法的有效性。

### Affine Correspondences Between Multi-camera Systems for 6DOF Relative Pose Estimation. **⭐⭐** (相关度: 50%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19824-3_37)
- **作者**: Banglei Guan, Ji Zhao
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 该论文针对多相机系统间6自由度相对位姿估计问题，利用仿射对应关系进行求解。由于摘要内容缺失，无法详细评估其具体方法、改进点和实验结果。从标题推测，该方法可能通过仿射变换约束来提升位姿估计的精度和鲁棒性，但缺乏摘要和实验数据支持，难以判断其实际贡献。
- **摘要（英）**: This paper tackles the problem of 6DOF relative pose estimation between multi-camera systems using affine correspondences. Due to the missing abstract, the specific methodology, improvements, and experimental results cannot be assessed. The title suggests a focus on leveraging affine constraints for pose estimation, but the lack of details limits evaluation of its contribution.
- **核心贡献**: 提出利用仿射对应关系进行多相机系统间6自由度相对位姿估计的方法。
- **创新点**: 将仿射对应关系引入多相机位姿估计，可能提高几何约束的利用效率。
- **结果**: 因摘要缺失，无法提供具体效果数据。

### RA-Depth: Resolution Adaptive Self-supervised Monocular Depth Estimation. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2207.11984](https://arxiv.org/abs/2207.11984)
- **作者**: Mu He, Le Hui, Yikai Bian, Jian Ren, Jin Xie, Jian Yang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对自监督单目深度估计模型在固定分辨率训练后迁移到其他分辨率时性能严重下降的问题，提出了分辨率自适应方法RA-Depth，通过学习场景深度的尺度不变性来提升跨分辨率泛化能力。具体包括：一种简单高效的数据增强方法生成同一场景任意尺度的图像；设计双高分辨率网络，利用多路径编码器和解码器及密集交互聚合多尺度特征；并构建跨尺度深度一致性损失，显式学习深度预测的尺度不变性。在KITTI、Make3D和NYU-V2数据集上的大量实验表明，RA-Depth不仅达到了最先进的性能，还展现出良好的分辨率适应能力。
- **摘要（英）**: This paper addresses the severe performance degradation of self-supervised monocular depth estimation models when evaluated at resolutions different from training. It proposes RA-Depth, which learns scale invariance of scene depth via a data augmentation method generating arbitrary-scale images, a dual high-resolution network with multi-path encoders/decoders and dense interactions for multi-scale feature aggregation, and a cross-scale depth consistency loss. Extensive experiments on KITTI, Make3D, and NYU-V2 demonstrate state-of-the-art performance and strong resolution adaptation ability.
- **核心贡献**: 提出了分辨率自适应自监督单目深度估计方法，通过学习尺度不变性显著提升跨分辨率泛化能力。
- **创新点**: 创新性地引入跨尺度深度一致性损失和双高分辨率网络，结合任意尺度数据增强，实现了对深度尺度不变性的显式建模。
- **结果**: 在KITTI、Make3D和NYU-V2上取得最先进性能，并展现出优异的分辨率适应能力。

### Depth Map Decomposition for Monocular Depth Estimation.
- **链接**: [arXiv:2208.10762](https://arxiv.org/abs/2208.10762)
- **作者**: Jinyoung Jun, Jaehan Lee, Chul Lee, Chang-Su Kim
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

- **摘要（英，原文）**:

  > We propose a novel algorithm for monocular depth estimation that decomposes a metric depth map into a normalized depth map and scale features. The proposed network is composed of a shared encoder and three decoders, called G-Net, N-Net, and M-Net, which estimate gradient maps, a normalized depth map, and a metric depth map, respectively. M-Net learns to estimate metric depths more accurately using relative depth features extracted by G-Net and N-Net. The proposed algorithm has the advantage that it can use datasets without metric depth labels to improve the performance of metric depth estimation. Experimental results on various datasets demonstrate that the proposed algorithm not only provides competitive performance to state-of-the-art algorithms but also yields acceptable results even when only a small amount of metric depth data is available for its training.

### BRNet: Exploring Comprehensive Features for Monocular Depth Estimation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19839-7_34) · 📚 被引 40
- **作者**: Wencheng Han, Junbo Yin, Xiaogang Jin, Xiangdong Dai, Jianbing Shen
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Gradient-Based Uncertainty for Monocular Depth Estimation.
- **链接**: [arXiv:2208.02005](https://arxiv.org/abs/2208.02005)
- **作者**: Julia Hornauer, Vasileios Belagiannis
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

- **摘要（英，原文）**:

  > In monocular depth estimation, disturbances in the image context, like moving objects or reflecting materials, can easily lead to erroneous predictions. For that reason, uncertainty estimates for each pixel are necessary, in particular for safety-critical applications such as automated driving. We propose a post hoc uncertainty estimation approach for an already trained and thus fixed depth estimation model, represented by a deep neural network. The uncertainty is estimated with the gradients which are extracted with an auxiliary loss function. To avoid relying on ground-truth information for the loss definition, we present an auxiliary loss function based on the correspondence of the depth prediction for an image and its horizontally flipped counterpart. Our approach achieves state-of-the-art uncertainty estimation results on the KITTI and NYU Depth V2 benchmarks without the need to retrain the neural network. Models and code are publicly available at https://github.com/jhornauer/GrUMoDepth.

### Towards Comprehensive Representation Enhancement in Semantics-Guided Self-supervised Monocular Depth Estimation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19769-7_18) · 📚 被引 21
- **作者**: Jingyuan Ma, Xiangyu Lei, Nan Liu, Xian Zhao, Shiliang Pu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Adaptive Co-teaching for Unsupervised Monocular Depth Estimation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19769-7_6)
- **作者**: Weisong Ren, Lijun Wang, Yongri Piao, Miao Zhang, Huchuan Lu, Ting Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

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

- **摘要（英，原文）**:

  > Unsupervised monocular depth and ego-motion estimation has drawn extensive research attention in recent years. Although current methods have reached a high up-to-scale accuracy, they usually fail to learn the true scale metric due to the inherent scale ambiguity from training with monocular sequences. In this work, we tackle this problem and propose DynaDepth, a novel scale-aware framework that integrates information from vision and IMU motion dynamics. Specifically, we first propose an IMU photometric loss and a cross-sensor photometric consistency loss to provide dense supervision and absolute scales. To fully exploit the complementary information from both sensors, we further drive a differentiable camera-centric extended Kalman filter (EKF) to update the IMU preintegrated motions when observing visual measurements. In addition, the EKF formulation enables learning an ego-motion uncertainty measure, which is non-trivial for unsupervised methods. By leveraging IMU during training, DynaDepth not only learns an absolute scale, but also provides a better generalization ability and robustness against vision degradation such as illumination change and moving objects. We validate the effectiveness of DynaDepth by conducting extensive experiments and simulations on the KITTI and Make3D datasets.

### Self-distilled Feature Aggregation for Self-supervised Monocular Depth Estimation.
- **链接**: [arXiv:2209.07088](https://arxiv.org/abs/2209.07088)
- **作者**: Zhengming Zhou, Qiulei Dong
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

- **摘要（英，原文）**:

  > Self-supervised monocular depth estimation has received much attention recently in computer vision. Most of the existing works in literature aggregate multi-scale features for depth prediction via either straightforward concatenation or element-wise addition, however, such feature aggregation operations generally neglect the contextual consistency between multi-scale features. Addressing this problem, we propose the Self-Distilled Feature Aggregation (SDFA) module for simultaneously aggregating a pair of low-scale and high-scale features and maintaining their contextual consistency. The SDFA employs three branches to learn three feature offset maps respectively: one offset map for refining the input low-scale feature and the other two for refining the input high-scale feature under a designed self-distillation manner. Then, we propose an SDFA-based network for self-supervised monocular depth estimation, and design a self-distilled training strategy to train the proposed network with the SDFA module. Experimental results on the KITTI dataset demonstrate that the proposed method outperforms the comparative state-of-the-art methods in most cases. The code is available at https://github.com/ZM-Zhou/SDFA-Net_pytorch.

### DevNet: Self-supervised Monocular Depth Learning via Density Volume Construction.
- **链接**: [arXiv:2209.06351](https://arxiv.org/abs/2209.06351) · 📚 被引 26
- **作者**: Kaichen Zhou, Lanqing Hong, Changhao Chen, Hang Xu, Chaoqiang Ye, Qingyong Hu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

- **摘要（英，原文）**:

  > Self-supervised depth learning from monocular images normally relies on the 2D pixel-wise photometric relation between temporally adjacent image frames. However, they neither fully exploit the 3D point-wise geometric correspondences, nor effectively tackle the ambiguities in the photometric warping caused by occlusions or illumination inconsistency. To address these problems, this work proposes Density Volume Construction Network (DevNet), a novel self-supervised monocular depth learning framework, that can consider 3D spatial information, and exploit stronger geometric constraints among adjacent camera frustums. Instead of directly regressing the pixel value from a single image, our DevNet divides the camera frustum into multiple parallel planes and predicts the pointwise occlusion probability density on each plane. The final depth map is generated by integrating the density along corresponding rays. During the training process, novel regularization strategies and loss functions are introduced to mitigate photometric ambiguities and overfitting. Without obviously enlarging model parameters size or running time, DevNet outperforms several representative baselines on both the KITTI-2015 outdoor dataset and NYU-V2 indoor dataset. In particular, the root-mean-square-deviation is reduced by around 4% with DevNet on both KITTI-2015 and NYU-V2 in the task of depth estimation. Code is available at https://github.com/gitkaichenzhou/DevNet.

## 跨领域论文（完整笔记在其他领域）

- BEVFormer: Learning Bird's-Eye-View Representation from Multi-camera Images via Spatiotemporal Transformers. → [3d-detection](../3d-detection/Guideline%202022.md)
- SpatialDETR: Robust Scalable Transformer-Based 3D Object Detection From Multi-view Camera Images With Global Cross-Sensor Attention. → [3d-detection](../3d-detection/Guideline%202022.md)
- Semi-supervised Monocular 3D Object Detection by Multi-view Consistency. → [3d-detection](../3d-detection/Guideline%202022.md)
- PETR: Position Embedding Transformation for Multi-view 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- MvDeCor: Multi-view Dense Correspondence Learning for Fine-Grained 3D Segmentation. → [3d-detection](../3d-detection/Guideline%202022.md)
- Physical Attack on Monocular Depth Estimation with Optimal Adversarial Patches. → [3d-detection](../3d-detection/Guideline%202022.md)
