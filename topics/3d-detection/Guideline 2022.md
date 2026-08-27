# 3D Detection — 2022 Guideline

> 领域: 3D 目标检测（LiDAR / 相机 / 多模态融合）
> 论文数: 35 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: [2024](Guideline%202024.md)

### BEVFormer: Learning Bird's-Eye-View Representation from Multi-camera Images via Spatiotemporal Transformers. **⭐⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2203.17270](https://arxiv.org/abs/2203.17270) · 📚 被引 1286
- **作者**: Zhiqi Li, Wenhai Wang, Hongyang Li, Enze Xie, Chonghao Sima, Tong Lu et al.
- **🏷️ 机构**: Shanghai AI Lab, Tsinghua / Shanghai AI Lab
- **会议**: ECCV 2022
- **摘要（中）**: ①针对多相机图像下3D视觉感知任务（如3D检测和地图分割）中缺乏统一BEV表示的问题。②提出了BEVFormer框架，通过预定义的网格状BEV查询，利用空间交叉注意力聚合多相机视角的空间特征，并通过时间自注意力循环融合历史BEV信息。③相比已有方法，BEVFormer同时利用空间和时间信息，无需依赖LiDAR或深度估计，实现了端到端的统一表示学习。④在nuScenes测试集上NDS指标达到56.9%，比之前最优方法高9.0个百分点，与基于LiDAR的基线性能相当，并显著提升了速度估计准确率和低可见度条件下的目标召回率。
- **摘要（英）**: This paper addresses the lack of a unified BEV representation for multi-camera 3D perception tasks like detection and map segmentation. It proposes BEVFormer, which uses spatiotemporal transformers with grid-shaped BEV queries, spatial cross-attention for multi-view feature aggregation, and temporal self-attention for history fusion. It achieves state-of-the-art 56.9% NDS on nuScenes test, surpassing prior methods by 9.0 points and matching LiDAR-based baselines.
- **核心贡献**: 提出了基于时空Transformer的统一BEV表示学习框架，支持多种自动驾驶感知任务。
- **创新点**: 设计了空间交叉注意力和时间自注意力机制，有效融合多视角空间特征和历史时序信息。
- **结果**: 在nuScenes上NDS达56.9%，性能超越现有方法并媲美LiDAR基线。

### V2X-ViT: Vehicle-to-Everything Cooperative Perception with Vision Transformer. **⭐⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2203.10638](https://arxiv.org/abs/2203.10638) · 📚 被引 520
- **作者**: Runsheng Xu, Hao Xiang, Zhengzhong Tu, Xin Xia, Ming-Hsuan Yang, Jiaqi Ma
- **🏷️ 机构**: UC Merced
- **会议**: ECCV 2022
- **摘要（中）**: 针对自动驾驶中单车感知的局限，该论文提出V2X-ViT，利用车联网（V2X）通信和视觉Transformer实现多智能体协同感知。通过异构多智能体自注意力和多尺度窗口自注意力交替层，有效融合车辆和基础设施信息，并处理异步、位姿误差和异构性挑战。在CARLA和OpenCDA构建的大规模数据集上，V2X-ViT在3D目标检测上达到SOTA，且在噪声环境下表现鲁棒。
- **摘要（英）**: This paper proposes V2X-ViT, a vision Transformer-based cooperative perception framework for V2X communication, using alternating heterogeneous multi-agent self-attention and multi-scale window self-attention to fuse information across vehicles and infrastructure. It achieves SOTA 3D detection on a large-scale CARLA/OpenCDA dataset and remains robust under noisy conditions.
- **核心贡献**: 提出了基于视觉Transformer的V2X协同感知框架V2X-ViT。
- **创新点**: 设计异构多智能体自注意力与多尺度窗口自注意力的统一架构。
- **结果**: 在3D目标检测上达到SOTA，并在噪声环境下保持鲁棒性能。

### Deformable Feature Aggregation for Dynamic Multi-modal 3D Object Detection. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20074-8_36)
- **作者**: Zehui Chen, Zhenyu Li, Shiquan Zhang, Liangji Fang, Qinhong Jiang, Feng Zhao
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对动态多模态3D目标检测中，如何有效融合不同模态特征并适应动态场景的问题，论文提出了一种可变形特征聚合方法。该方法通过可变形注意力机制，动态调整多模态特征的采样位置和聚合权重，以增强跨模态信息交互。相比固定网格或均匀采样的融合方式，该方法能更灵活地捕捉动态目标的空间变化。实验表明，该方法在多个3D检测基准上显著提升了检测精度，尤其在动态场景下表现突出。
- **摘要（英）**: This paper addresses dynamic multi-modal 3D object detection by proposing a deformable feature aggregation method that adaptively adjusts sampling positions and weights for cross-modal fusion. It improves upon fixed-grid fusion by capturing spatial variations of dynamic objects, achieving notable accuracy gains on 3D detection benchmarks.
- **核心贡献**: 提出可变形特征聚合机制，提升动态多模态3D检测的鲁棒性。
- **创新点**: 将可变形注意力引入多模态特征融合，实现自适应采样。
- **结果**: 在多个基准上提升检测精度，尤其动态场景效果显著。

### MPPNet: Multi-frame Feature Intertwining with Proxy Points for 3D Temporal Object Detection. **⭐⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2205.05979](https://arxiv.org/abs/2205.05979) · 📚 被引 75
- **作者**: Xuesong Chen, Shaoshuai Shi, Benjin Zhu, Ka Chun Cheung, Hang Xu, Hongsheng Li
- **🏷️ 机构**: CUHK
- **会议**: ECCV 2022
- **摘要（中）**: 针对点云序列中3D时间目标检测的长时序特征建模问题，论文提出了MPPNet框架，采用三层次结构：逐帧编码、短片段融合和全序列聚合。通过代理点作为一致的对象表示和帧间特征交互的载体，并设计组内特征混合和组间特征注意力，以高效处理长序列。相比现有方法，MPPNet在短序列和长序列上均显著提升性能。在Waymo开放数据集上，该方法大幅超越最先进方法，尤其长序列检测精度提升明显。
- **摘要（英）**: This paper addresses long-term temporal 3D object detection in point cloud sequences by proposing MPPNet, a three-hierarchy framework with proxy points for per-frame encoding, short-clip fusion, and whole-sequence aggregation. It introduces intra-group mixing and inter-group attention for efficient long-sequence processing, significantly outperforming state-of-the-art on Waymo dataset for both short and long sequences.
- **核心贡献**: 提出MPPNet框架，利用代理点实现高效多帧特征交互。
- **创新点**: 三层次结构和代理点机制创新性地处理长时序点云。
- **结果**: 在Waymo数据集上大幅超越现有方法。

### SpatialDETR: Robust Scalable Transformer-Based 3D Object Detection From Multi-view Camera Images With Global Cross-Sensor Attention. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19842-7_14) · 📚 被引 24
- **作者**: Simon Doll, Richard Schulz, Lukas Schneider, Viviane Benzin, Markus Enzweiler, Hendrik P. A. Lensch
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对多视角相机3D目标检测中，现有方法难以有效利用全局跨传感器信息，导致检测精度和鲁棒性不足的问题。②提出了SpatialDETR，一种基于Transformer的架构，通过全局跨传感器注意力机制，将多视角图像特征与3D空间位置信息融合，实现端到端的3D目标检测。③相比现有方法，引入了可扩展的注意力设计，能够处理任意数量的相机视角，并增强了对不同传感器配置的适应性。④在nuScenes等基准上取得了显著的性能提升，展示了良好的鲁棒性和可扩展性。
- **摘要（英）**: This paper addresses the challenge of effectively leveraging global cross-sensor information in multi-view camera-based 3D object detection. It proposes SpatialDETR, a scalable Transformer-based architecture with global cross-sensor attention, enabling end-to-end detection. The method improves robustness and scalability over existing approaches, achieving significant performance gains on benchmarks like nuScenes.
- **核心贡献**: 提出了一种可扩展的基于Transformer的多视角3D检测框架，引入全局跨传感器注意力。
- **创新点**: 全局跨传感器注意力机制，支持任意数量相机视角的灵活融合。
- **结果**: 在nuScenes基准上显著提升了检测精度和鲁棒性。

### 3D Object Detection with a Self-supervised Lidar Scene Flow Backbone. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2205.00705](https://arxiv.org/abs/2205.00705) · 📚 被引 25
- **作者**: Emeç Erçelik, Ekim Yurtsever, Mingyu Liu, Zhijie Yang, Hanzhen Zhang, Pinar Topçam et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对激光雷达3D目标检测依赖大量标注数据、成本高昂且泛化受限的问题。②提出利用自监督场景流估计模型作为骨干网络，通过循环一致性训练学习点云运动表示，再将其与监督检测头结合，用于单帧3D检测。③改进点在于将自监督预训练与下游检测任务有效衔接，使检测模型能利用运动信息区分动态物体。④在KITTI和nuScenes基准上，自监督预训练显著提升了3D检测性能。
- **摘要（英）**: This paper tackles the high annotation cost and limited generalization of lidar-based 3D object detection by introducing a self-supervised scene flow backbone. A cycle-consistent flow model is pre-trained and its encoder is reused for a supervised detection head, enabling motion-aware detection. Experiments on KITTI and nuScenes show significant performance improvements.
- **核心贡献**: 提出将自监督场景流骨干与监督检测头结合，提升3D检测性能。
- **创新点**: 利用自监督运动表示增强单帧检测的动态物体区分能力。
- **结果**: 在KITTI和nuScenes上显著提高检测精度。

### Cross-Modality Knowledge Distillation Network for Monocular 3D Object Detection. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2211.07171](https://arxiv.org/abs/2211.07171)
- **作者**: Yu Hong, Hang Dai, Yong Ding
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对单目3D检测中LiDAR信息利用不充分和训练策略非端到端的问题。②提出了跨模态知识蒸馏（CMKD）网络，在特征和响应层面高效地将LiDAR模态知识迁移到图像模态，并扩展为半监督框架利用未标注数据。③相比Pseudo-LiDAR等方法，CMKD实现了端到端训练，更充分地挖掘LiDAR数据潜力。④在KITTI测试集和Waymo验证集上排名第一，显著优于现有单目3D检测方法。
- **摘要（英）**: This paper tackles insufficient LiDAR utilization and non-end-to-end training in monocular 3D detection. It proposes CMKD, a cross-modality knowledge distillation network that transfers LiDAR knowledge to image modality at feature and response levels, extended to semi-supervised learning with unlabeled data. It ranks first on KITTI test and Waymo val sets, significantly outperforming prior monocular detectors.
- **核心贡献**: 提出了跨模态知识蒸馏框架，实现LiDAR到图像的高效知识迁移。
- **创新点**: 在特征和响应层面同时蒸馏，并支持半监督训练。
- **结果**: 在KITTI和Waymo上达到最优性能。

### CramNet: Camera-Radar Fusion with Ray-Constrained Cross-Attention for Robust 3D Object Detection. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2210.09267](https://arxiv.org/abs/2210.09267) · 📚 被引 57
- **作者**: Jyh-Jing Hwang, Henrik Kretzschmar, Joshua Manela, Sean Rafferty, Nicholas Armstrong-Crews, Tiffany L. Chen et al.
- **🏷️ 机构**: Waymo
- **会议**: ECCV 2022
- **摘要（中）**: ①针对相机和雷达融合中深度和仰角信息缺失导致的几何对应模糊问题。②提出了CramNet，通过射线约束交叉注意力机制在联合3D空间中融合相机和雷达数据，并支持传感器模态丢弃训练。③相比现有融合方法，CramNet有效解决了跨模态几何匹配的歧义性，增强了鲁棒性。④在RADIATE数据集上验证了有效性，相机-only变体也表现出竞争力。
- **摘要（英）**: This paper addresses geometric ambiguity in camera-radar fusion due to missing depth and elevation. It proposes CramNet with ray-constrained cross-attention for joint 3D space fusion and modality dropout training. It demonstrates robust detection on RADIATE, with competitive camera-only performance.
- **核心贡献**: 提出了射线约束交叉注意力机制，实现相机和雷达数据的高效融合。
- **创新点**: 通过射线约束解决跨模态几何对应歧义，并支持传感器故障鲁棒性。
- **结果**: 在RADIATE数据集上实现鲁棒3D检测。

### DEVIANT: Depth EquiVarIAnt NeTwork for Monocular 3D Object Detection. **⭐⭐⭐⭐** (相关度: 82%)
- **链接**: [arXiv:2207.10758](https://arxiv.org/abs/2207.10758) · 📚 被引 69
- **作者**: Abhinav Kumar, Garrick Brazil, Enrique Corona, Armin Parchami, Xiaoming Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对单目3D检测中深度估计困难且标准卷积块不具备射影流形下3D平移等变性的问题。②提出了DEVIANT网络，使用尺度等变steerable块构建深度等变卷积，使网络对射影流形中的深度平移具有等变性。③相比普通网络，DEVIANT强制学习一致的深度估计，提高了跨数据集泛化能力。④在KITTI和Waymo图像-only类别中达到最优性能，与使用额外信息的方法竞争力相当。
- **摘要（英）**: This paper addresses depth estimation challenges in monocular 3D detection by introducing depth-equivariant convolutions. It proposes DEVIANT with scale-equivariant steerable blocks, achieving equivariance to depth translations. It achieves state-of-the-art results on KITTI and Waymo, with better cross-dataset generalization.
- **核心贡献**: 提出了深度等变网络，提升单目3D检测的深度估计一致性。
- **创新点**: 利用尺度等变块实现射影流形下的深度平移等变性。
- **结果**: 在KITTI和Waymo上达到最优性能。

### Densely Constrained Depth Estimator for Monocular 3D Object Detection. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2207.10047](https://arxiv.org/abs/2207.10047)
- **作者**: Yingyan Li, Yuntao Chen, Jiawei He, Zhaoxiang Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对单目3D目标检测中深度估计不准确的问题，现有方法仅利用垂直边缘作为投影约束，导致深度候选不足。本文提出DCD方法，利用任意方向的密集投影约束生成大量深度候选，并设计图匹配加权模块融合候选深度。在KITTI和WOD基准上达到最先进性能，代码已开源。
- **摘要（英）**: This paper addresses inaccurate depth estimation in monocular 3D detection by proposing DCD, which uses dense projection constraints from edges of any direction to generate abundant depth candidates and a graph matching weighting module to merge them. It achieves state-of-the-art performance on KITTI and WOD benchmarks, with code released.
- **核心贡献**: 提出利用任意方向边缘的密集投影约束进行深度估计的方法。
- **创新点**: 将投影约束从垂直边缘扩展到任意方向，并引入图匹配加权融合。
- **结果**: 在KITTI和WOD上达到最先进性能。

### Unsupervised Domain Adaptation for Monocular 3D Object Detection via Self-training. **⭐⭐⭐⭐** (相关度: 84%)
- **链接**: [arXiv:2204.11590](https://arxiv.org/abs/2204.11590)
- **作者**: Zhenyu Li, Zehui Chen, Ang Li, Liangji Fang, Qinhong Jiang, Xianming Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对单目3D检测在跨域部署时性能急剧下降的问题。②提出了STMono3D，一种基于自训练的无监督域适应框架，通过几何对齐多尺度训练策略解耦相机参数，并采用教师-学生范式生成自适应伪标签。③相比现有方法，STMono3D有效缓解了深度偏移问题，并利用质量感知监督策略提升伪标签有效性。④在多个数据集上显著提升了目标域检测性能。
- **摘要（英）**: This paper addresses performance degradation in monocular 3D detection across domains. It proposes STMono3D, a self-training framework with geometry-aligned multi-scale training and teacher-student pseudo-labeling. It mitigates depth-shift and improves target-domain performance significantly.
- **核心贡献**: 提出了无监督域适应框架，解决单目3D检测的深度偏移问题。
- **创新点**: 结合几何对齐训练和质量感知伪标签策略。
- **结果**: 在跨域场景中显著提升检测性能。

### Homogeneous Multi-modal Feature Fusion and Interaction for 3D Object Detection. **⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2210.09615](https://arxiv.org/abs/2210.09615)
- **作者**: Xin Li, Botian Shi, Yuenan Hou, Xingjiao Wu, Tianlong Ma, Yikang Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对多模态3D检测中稀疏点云与密集图像融合导致信息丢失的问题，该论文提出HMFI方法，通过图像体素提升模块将2D特征转换到3D空间，生成同构的图像体素特征，并利用自注意力查询融合机制和体素特征交互模块实现跨模态融合。相比投影到2D平面或简单拼接的方法，HMFI避免了投影信息损失。实验在KITTI等数据集上验证了性能提升，但摘要未提供具体数值。
- **摘要（英）**: This paper tackles information loss in multi-modal 3D detection by proposing HMFI, which lifts 2D image features into 3D voxel space via an image voxel lifter, then fuses with point cloud features using self-attention query fusion and voxel interaction. It avoids projective loss compared to prior fusion methods, with improvements on KITTI, though specific numbers are omitted.
- **核心贡献**: 提出同构多模态融合框架HMFI，减少投影信息损失。
- **创新点**: 将图像特征提升为3D体素，实现同构融合。
- **结果**: 在KITTI等数据集上取得性能提升。

### Enhancing Multi-modal Features Using Local Self-attention for 3D Object Detection. **⭐⭐⭐** (相关度: 75%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20080-9_31) · 📚 被引 8
- **作者**: Hao Li, Zehan Zhang, Xian Zhao, Yulong Wang, Yuxi Shen, Shiliang Pu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对多模态3D目标检测中特征融合不充分的问题，本文提出利用局部自注意力增强多模态特征。方法通过局部自注意力机制在LiDAR和图像特征间进行交互，提升特征表示能力。实验验证了该方法在3D检测任务上的有效性。
- **摘要（英）**: This paper enhances multi-modal features for 3D object detection using local self-attention, which improves feature interaction between LiDAR and image modalities. Experiments demonstrate its effectiveness in boosting detection performance.
- **核心贡献**: 提出基于局部自注意力的多模态特征增强方法。
- **创新点**: 将局部自注意力应用于多模态3D检测的特征融合。
- **结果**: 实验验证了检测性能的提升。

### Semi-supervised Monocular 3D Object Detection by Multi-view Consistency. **⭐⭐⭐** (相关度: 80%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20074-8_41)
- **作者**: Qing Lian, Yanbo Xu, Weilong Yao, Yingcong Chen, Tong Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对单目3D目标检测中标注数据稀缺的问题，本文提出基于多视图一致性的半监督方法。方法利用多视图几何一致性生成伪标签，并设计一致性损失进行训练。实验表明该方法能有效利用未标注数据提升检测性能。
- **摘要（英）**: This paper proposes a semi-supervised monocular 3D detection method using multi-view consistency, which generates pseudo-labels via geometric consistency and trains with consistency losses. Experiments show improved performance by leveraging unlabeled data.
- **核心贡献**: 提出多视图一致性驱动的半监督单目3D检测框架。
- **创新点**: 利用多视图几何一致性生成高质量伪标签。
- **结果**: 有效利用未标注数据提升检测性能。

### Multimodal Transformer for Automatic 3D Annotation and Object Detection. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2207.09805](https://arxiv.org/abs/2207.09805)
- **作者**: Chang Liu, Xiaoyan Qian, Binxiao Huang, Xiaojuan Qi, Edmund Y. Lam, Siew-Chong Tan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对LiDAR扫描中3D框标注成本高的问题，本文提出端到端多模态Transformer自动标注器MTrans，利用LiDAR和图像从弱2D框生成精确3D框。方法通过图像信息生成新3D点来缓解点云稀疏性，并多任务同时进行前景分割、点云稠密化和3D框回归。在KITTI上，相比最先进自动标注器，moderate和hard样本的3D AP分别提升4.48%和4.03%，并扩展到3D检测达到89.45% AP。
- **摘要（英）**: This paper proposes MTrans, an end-to-end multimodal transformer autolabeler that generates precise 3D boxes from weak 2D boxes using LiDAR and images, densifying sparse point clouds with image-derived points. It improves 3D AP by 4.48% and 4.03% on KITTI moderate and hard samples versus SOTA autolabeler, and extends to detection with 89.45% AP.
- **核心贡献**: 提出多模态Transformer自动标注器，从弱2D框生成精确3D框。
- **创新点**: 通过图像生成3D点稠密化点云，缓解稀疏性问题。
- **结果**: 在KITTI上显著提升标注质量和检测精度。

### PETR: Position Embedding Transformation for Multi-view 3D Object Detection. **⭐⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2203.05625](https://arxiv.org/abs/2203.05625)
- **作者**: Yingfei Liu, Tiancai Wang, Xiangyu Zhang, Jian Sun
- **🏷️ 机构**: MEGVII
- **会议**: ECCV 2022
- **摘要（中）**: 针对多视图3D检测中如何有效利用3D位置信息的问题，该论文提出PETR，通过位置嵌入变换将3D坐标编码到图像特征中，生成3D位置感知特征，并利用对象查询进行端到端检测。相比基于投影或体素的方法，PETR简化了流程并提升了性能。在nuScenes上达到50.4% NDS和44.1% mAP，排名第一，成为强基线。
- **摘要（英）**: This paper introduces PETR for multi-view 3D detection by encoding 3D coordinates into image features via position embedding transformation, enabling end-to-end detection with object queries. It achieves state-of-the-art 50.4% NDS and 44.1% mAP on nuScenes, ranking first and serving as a strong baseline.
- **核心贡献**: 提出位置嵌入变换机制，统一多视图特征与查询交互。
- **创新点**: 将3D位置信息直接嵌入图像特征，避免复杂投影。
- **结果**: 在nuScenes上取得SOTA性能并排名第一。

### DetMatch: Two Teachers are Better than One for Joint 2D and 3D Semi-Supervised Object Detection. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2203.09510](https://arxiv.org/abs/2203.09510) · 📚 被引 24
- **作者**: Jinhyung Park, Chenfeng Xu, Yiyang Zhou, Masayoshi Tomizuka, Wei Zhan
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对2D和3D半监督检测中独立管道未利用多模态互补性的问题，该论文提出DetMatch框架，通过识别双传感器共同检测的物体生成更干净、鲁棒的伪标签，并利用RGB语义修正3D类别预测和定位。相比单模态方法，DetMatch减少了错误传播并提升伪标签质量。在KITTI和Waymo上优于强半监督方法。
- **摘要（英）**: This paper proposes DetMatch for joint 2D and 3D semi-supervised detection, using objects detected by both sensors to generate cleaner pseudo-labels and RGB semantics to rectify 3D predictions. It outperforms strong semi-supervised methods on KITTI and Waymo, reducing error propagation.
- **核心贡献**: 提出联合2D-3D半监督检测框架DetMatch。
- **创新点**: 利用双教师一致性生成高质量伪标签。
- **结果**: 在KITTI和Waymo上优于现有方法。

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

### DID-M3D: Decoupling Instance Depth for Monocular 3D Object Detection. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2207.08531](https://arxiv.org/abs/2207.08531) · 📚 被引 78
- **作者**: Liang Peng, Xiaopei Wu, Zheng Yang, Haifeng Liu, Deng Cai
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对单目3D检测中实例深度估计不直观的问题，本文指出深度由视觉深度线索和属性深度线索耦合而成，难以直接学习。提出将实例深度解耦为视觉表面深度和属性深度，并分别估计不确定性，最终融合得到实例深度。该方法在KITTI等基准上验证了有效性。
- **摘要（英）**: This paper decouples instance depth in monocular 3D detection into visual surface depth and attribute depth, addressing the non-intuitive coupling of depth clues. It estimates associated uncertainties and combines them for final depth, improving detection accuracy on benchmarks like KITTI.
- **核心贡献**: 提出实例深度解耦为视觉深度和属性深度的方法。
- **创新点**: 将深度估计分解为视觉和属性两部分并处理不确定性。
- **结果**: 在KITTI等基准上提升检测性能。

### FCAF3D: Fully Convolutional Anchor-Free 3D Object Detection. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20080-9_28) · 📚 被引 125
- **作者**: Danila Rukhovich, Anna Vorontsova, Anton Konushin
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对3D目标检测中锚框设计的复杂性，本文提出全卷积无锚框3D检测器FCAF3D。方法采用全卷积架构，直接在体素特征上预测3D框，避免锚框设计。实验在多个基准上验证了其高效性和准确性。
- **摘要（英）**: This paper proposes FCAF3D, a fully convolutional anchor-free 3D detector that directly predicts 3D boxes from voxel features, eliminating anchor design. Experiments show its efficiency and accuracy on multiple benchmarks.
- **核心贡献**: 提出全卷积无锚框3D检测架构。
- **创新点**: 去除锚框设计，实现端到端全卷积检测。
- **结果**: 在多个基准上验证了高效性和准确性。

### Rethinking IoU-based Optimization for Single-stage 3D Object Detection. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2207.09332](https://arxiv.org/abs/2207.09332)
- **作者**: Hualian Sheng, Sijia Cai, Na Zhao, Bing Deng, Jianqiang Huang, Xian-Sheng Hua et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对3D IoU优化计算成本高且对旋转敏感导致训练不稳定的问题，该论文提出旋转解耦IoU（RDIoU）方法，将旋转变量独立解耦，简化回归参数交互，同时保持3D IoU几何特性。将RDIoU用于回归和分类分支，鼓励网络学习更精确的边界框。相比直接3D IoU，RDIoU更高效且稳定，实验验证了性能提升。
- **摘要（英）**: This paper proposes Rotation-Decoupled IoU (RDIoU) to address the high cost and rotation sensitivity of 3D IoU optimization, decoupling rotation as an independent term while preserving geometry. It improves training stability and detection performance in single-stage 3D detectors.
- **核心贡献**: 提出RDIoU损失，解耦旋转变量提升优化效率。
- **创新点**: 将旋转独立处理，简化IoU计算并增强稳定性。
- **结果**: 提升单阶段3D检测的精度和训练稳定性。

### PillarNet: Real-Time and High-Performance Pillar-Based 3D Object Detection. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2205.07403](https://arxiv.org/abs/2205.07403) · 📚 被引 211
- **作者**: Guangsheng Shi, Ruifeng Li, Chao Ma
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对基于柱体（pillar）的3D检测器在精度上落后于基于体素（voxel）检测器的问题，旨在实现实时且高性能的3D目标检测。②提出了PillarNet，包含强大的编码器网络用于有效的柱体特征学习、用于空间-语义特征融合的颈部网络以及常用检测头，仅使用2D卷积，并设计了方向解耦的IoU回归损失和IoU感知预测分支。③相比现有柱体方法，PillarNet通过改进特征学习和损失设计缩小了与体素方法的性能差距，且支持灵活的柱体尺寸和经典2D骨干网络。④在nuScenes和Waymo数据集上的大量实验表明，PillarNet在实时性下取得了与顶尖体素方法相当或更优的检测精度。
- **摘要（英）**: This paper addresses the accuracy gap of pillar-based 3D detectors compared to voxel-based counterparts, aiming for real-time high-performance detection. It proposes PillarNet with a powerful encoder, a fusion neck, and an orientation-decoupled IoU loss with IoU-aware prediction, using only 2D convolutions. Experiments on nuScenes and Waymo show competitive accuracy with real-time efficiency.
- **核心贡献**: 提出了PillarNet，一种仅用2D卷积的实时高性能柱体3D检测器。
- **创新点**: 设计了方向解耦IoU回归损失和IoU感知分支，有效提升了柱体方法的精度。
- **结果**: 在nuScenes和Waymo上达到与体素方法相当的精度，同时保持实时速度。

### SWFormer: Sparse Window Transformer for 3D Object Detection in Point Clouds. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2210.07372](https://arxiv.org/abs/2210.07372) · 📚 被引 129
- **作者**: Pei Sun, Mingxing Tan, Weiyue Wang, Chenxi Liu, Fei Xia, Zhaoqi Leng et al.
- **🏷️ 机构**: Waymo
- **会议**: ECCV 2022
- **摘要（中）**: ①针对点云中3D目标检测的稀疏性问题，现有方法难以高效利用点云稀疏性。②提出了SWFormer，一种基于稀疏窗口Transformer的3D检测器，将点云转换为稀疏体素和窗口，通过分桶方案高效处理变长稀疏窗口，并引入多尺度特征融合、窗口移位和体素扩散技术。③相比现有Transformer检测器，SWFormer充分利用点云稀疏性，通过跨窗口相关性和体素扩散提升检测精度。④在Waymo数据集上达到73.36 L2 mAPH的SOTA性能，超越所有先前单阶段和两阶段模型，同时效率更高。
- **摘要（英）**: This paper tackles the sparsity challenge in 3D point cloud detection by proposing SWFormer, a sparse window Transformer that processes variable-length windows via bucketing and incorporates multi-scale fusion, window shifting, and voxel diffusion. It achieves state-of-the-art 73.36 L2 mAPH on Waymo, outperforming prior models with better efficiency.
- **核心贡献**: 提出了SWFormer，首个高效利用点云稀疏性的窗口Transformer 3D检测器。
- **创新点**: 引入分桶方案和体素扩散技术，有效处理稀疏窗口并提升检测精度。
- **结果**: 在Waymo上达到73.36 L2 mAPH的SOTA性能，效率优于先前模型。

### Monocular 3D Object Detection with Depth from Motion. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2207.12988](https://arxiv.org/abs/2207.12988)
- **作者**: Tai Wang, Jiangmiao Pang, Dahua Lin
- **🏷️ 机构**: CUHK
- **会议**: ECCV 2022
- **摘要（中）**: 这篇论文针对单目3D物体检测中绝对深度估计困难的问题，提出利用相机自运动（ego-motion）提供的几何结构来估计深度。作者首先理论分析了两视图情况下的挑战，包括多步估计的累积误差和静态相机或匹配歧义导致的固有困境，然后通过构建几何感知的成本体积（cost volume）建立立体对应关系，并结合单目理解进行补偿，提出了Depth from Motion (DfM)框架。该框架利用几何信息将2D图像特征提升到3D空间进行检测，并提供了无需相机位姿的变体（pose-free DfM）。实验结果表明，该方法在多个基准上大幅超越了现有最先进方法，验证了其有效性和实用性。
- **摘要（英）**: This paper addresses the challenge of absolute depth estimation in monocular 3D object detection by leveraging geometric structure from camera ego-motion. The authors theoretically analyze two-view cases, identifying issues like cumulative errors and dilemmas from static cameras or matching ambiguity, and propose a geometry-aware cost volume for stereo correspondence, compensated by monocular understanding, within the Depth from Motion (DfM) framework. The method lifts 2D features to 3D space for detection and includes a pose-free variant, achieving significant improvements over state-of-the-art methods on benchmarks.
- **核心贡献**: 提出了一种利用相机自运动几何信息进行单目3D物体检测的新框架DfM，显著提升了深度估计和检测精度。
- **创新点**: 创新性地将两视图几何分析与成本体积结合，并引入单目补偿机制，同时提供无需位姿的变体，增强了方法的鲁棒性和适用性。
- **结果**: 在多个基准数据集上大幅超越现有最先进方法，展示了显著的性能提升。

### LiDAR Distillation: Bridging the Beam-Induced Domain Gap for 3D Object Detection. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2203.14956](https://arxiv.org/abs/2203.14956)
- **作者**: Yi Wei, Zibu Wei, Yongming Rao, Jiaxin Li, Jie Zhou, Jiwen Lu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对不同LiDAR光束数导致的3D检测域差距问题，实际应用中低光束LiDAR难以利用高光束数据。②提出了LiDAR蒸馏框架，通过下采样生成低光束伪LiDAR，并采用教师-学生框架蒸馏高光束数据中的丰富信息。③相比现有域自适应方法，该框架通过对齐源域和目标域的点云密度，有效缓解光束引起的域偏移。④在Waymo、nuScenes和KITTI数据集上的大量实验验证了其有效性，适用于多种检测器。
- **摘要（英）**: This paper addresses the beam-induced domain gap in 3D detection by proposing LiDAR distillation, which generates low-beam pseudo LiDAR via downsampling and uses a teacher-student framework to distill rich information. It aligns point density across domains, effectively mitigating domain shift, as validated on Waymo, nuScenes, and KITTI.
- **核心贡献**: 提出了LiDAR蒸馏框架，用于桥接不同光束LiDAR之间的域差距。
- **创新点**: 通过密度对齐和教师-学生蒸馏，有效处理光束诱导的域偏移。
- **结果**: 在多个数据集上验证了有效性，适用于多种3D检测器。

### Graph R-CNN: Towards Accurate 3D Object Detection with Semantic-Decorated Local Graph.
- **链接**: [arXiv:2208.03624](https://arxiv.org/abs/2208.03624) · 📚 被引 83
- **作者**: Honghui Yang, Zili Liu, Xiaopei Wu, Wenxiao Wang, Wei Qian, Xiaofei He et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

- **摘要（英，原文）**:

  > Two-stage detectors have gained much popularity in 3D object detection. Most two-stage 3D detectors utilize grid points, voxel grids, or sampled keypoints for RoI feature extraction in the second stage. Such methods, however, are inefficient in handling unevenly distributed and sparse outdoor points. This paper solves this problem in three aspects. 1) Dynamic Point Aggregation. We propose the patch search to quickly search points in a local region for each 3D proposal. The dynamic farthest voxel sampling is then applied to evenly sample the points. Especially, the voxel size varies along the distance to accommodate the uneven distribution of points. 2) RoI-graph Pooling. We build local graphs on the sampled points to better model contextual information and mine point relations through iterative message passing. 3) Visual Features Augmentation. We introduce a simple yet effective fusion strategy to compensate for sparse LiDAR points with limited semantic cues. Based on these modules, we construct our Graph R-CNN as the second stage, which can be applied to existing one-stage detectors to consistently improve the detection performance. Extensive experiments show that Graph R-CNN outperforms the state-of-the-art 3D detection models by a large margin on both the KITTI and Waymo Open Dataset. And we rank first place on the KITTI BEV car detection leaderboard. Code will be available at \url{https://github.com/Nightmare-n/GraphRCNN}.

### Semi-supervised 3D Object Detection with Proficient Teachers.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19839-7_42) · 📚 被引 73
- **作者**: Junbo Yin, Jin Fang, Dingfu Zhou, Liangjun Zhang, Cheng-Zhong Xu, Jianbing Shen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### ProposalContrast: Unsupervised Pre-training for LiDAR-Based 3D Object Detection.
- **链接**: [arXiv:2207.12654](https://arxiv.org/abs/2207.12654) · 📚 被引 85
- **作者**: Junbo Yin, Dingfu Zhou, Liangjun Zhang, Jin Fang, Cheng-Zhong Xu, Jianbing Shen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

- **摘要（英，原文）**:

  > Existing approaches for unsupervised point cloud pre-training are constrained to either scene-level or point/voxel-level instance discrimination. Scene-level methods tend to lose local details that are crucial for recognizing the road objects, while point/voxel-level methods inherently suffer from limited receptive field that is incapable of perceiving large objects or context environments. Considering region-level representations are more suitable for 3D object detection, we devise a new unsupervised point cloud pre-training framework, called ProposalContrast, that learns robust 3D representations by contrasting region proposals. Specifically, with an exhaustive set of region proposals sampled from each point cloud, geometric point relations within each proposal are modeled for creating expressive proposal representations. To better accommodate 3D detection properties, ProposalContrast optimizes with both inter-cluster and inter-proposal separation, i.e., sharpening the discriminativeness of proposal representations across semantic classes and object instances. The generalizability and transferability of ProposalContrast are verified on various 3D detectors (i.e., PV-RCNN, CenterPoint, PointPillars and PointRCNN) and datasets (i.e., KITTI, Waymo and ONCE).

### CenterFormer: Center-Based Transformer for 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19839-7_29) · 📚 被引 162
- **作者**: Zixiang Zhou, Xiangchen Zhao, Yu Wang, Panqu Wang, Hassan Foroosh
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Point Cloud Compression with Sibling Context and Surface Priors.
- **链接**: [arXiv:2205.00760](https://arxiv.org/abs/2205.00760)
- **作者**: Zhili Chen, Zian Qian, Sukai Wang, Qifeng Chen
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

- **摘要（英，原文）**:

  > We present a novel octree-based multi-level framework for large-scale point cloud compression, which can organize sparse and unstructured point clouds in a memory-efficient way. In this framework, we propose a new entropy model that explores the hierarchical dependency in an octree using the context of siblings' children, ancestors, and neighbors to encode the occupancy information of each non-leaf octree node into a bitstream. Moreover, we locally fit quadratic surfaces with a voxel-based geometry-aware module to provide geometric priors in entropy encoding. These strong priors empower our entropy framework to encode the octree into a more compact bitstream. In the decoding stage, we apply a two-step heuristic strategy to restore point clouds with better reconstruction quality. The quantitative evaluation shows that our method outperforms state-of-the-art baselines with a bitrate improvement of 11-16% and 12-14% on the KITTI Odometry and nuScenes datasets, respectively.

### MvDeCor: Multi-view Dense Correspondence Learning for Fine-Grained 3D Segmentation.
- **链接**: [arXiv:2208.08580](https://arxiv.org/abs/2208.08580) · 📚 被引 10
- **作者**: Gopal Sharma, Kangxue Yin, Subhransu Maji, Evangelos Kalogerakis, Or Litany, Sanja Fidler
- **🏷️ 机构**: NVIDIA / University of Toronto
- **会议**: ECCV 2022

- **摘要（英，原文）**:

  > We propose to utilize self-supervised techniques in the 2D domain for fine-grained 3D shape segmentation tasks. This is inspired by the observation that view-based surface representations are more effective at modeling high-resolution surface details and texture than their 3D counterparts based on point clouds or voxel occupancy. Specifically, given a 3D shape, we render it from multiple views, and set up a dense correspondence learning task within the contrastive learning framework. As a result, the learned 2D representations are view-invariant and geometrically consistent, leading to better generalization when trained on a limited number of labeled shapes compared to alternatives that utilize self-supervision in 2D or 3D alone. Experiments on textured (RenderPeople) and untextured (PartNet) 3D datasets show that our method outperforms state-of-the-art alternatives in fine-grained part segmentation. The improvements over baselines are greater when only a sparse set of views is available for training or when shapes are textured, indicating that MvDeCor benefits from both 2D processing and 3D geometric reasoning.

### Physical Attack on Monocular Depth Estimation with Optimal Adversarial Patches.
- **链接**: [arXiv:2207.04718](https://arxiv.org/abs/2207.04718) · 📚 被引 11
- **作者**: Zhiyuan Cheng, James Liang, Hongjun Choi, Guanhong Tao, Zhiwen Cao, Dongfang Liu et al.
- **🏷️ 机构**: School of Automation, Northwestern Polytechnical University, Xi&#x2019;an, Shaanxi, China
- **会议**: ECCV 2022

- **摘要（英，原文）**:

  > Deep learning has substantially boosted the performance of Monocular Depth Estimation (MDE), a critical component in fully vision-based autonomous driving (AD) systems (e.g., Tesla and Toyota). In this work, we develop an attack against learning-based MDE. In particular, we use an optimization-based method to systematically generate stealthy physical-object-oriented adversarial patches to attack depth estimation. We balance the stealth and effectiveness of our attack with object-oriented adversarial design, sensitive region localization, and natural style camouflage. Using real-world driving scenarios, we evaluate our attack on concurrent MDE models and a representative downstream task for AD (i.e., 3D object detection). Experimental results show that our method can generate stealthy, effective, and robust adversarial patches for different target objects and models and achieves more than 6 meters mean depth estimation error and 93% attack success rate (ASR) in object detection with a patch of 1/9 of the vehicle's rear area. Field tests on three different driving routes with a real vehicle indicate that we cause over 6 meters mean depth estimation error and reduce the object detection rate from 90.70% to 5.16% in continuous video frames.

### PolarMOT: How Far Can Geometric Relations Take us in 3D Multi-object Tracking?
- **链接**: [arXiv:2208.01957](https://arxiv.org/abs/2208.01957) · 📚 被引 46
- **作者**: Aleksandr Kim, Guillem Brasó, Aljosa Osep, Laura Leal-Taixé
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

- **摘要（英，原文）**:

  > Most (3D) multi-object tracking methods rely on appearance-based cues for data association. By contrast, we investigate how far we can get by only encoding geometric relationships between objects in 3D space as cues for data-driven data association. We encode 3D detections as nodes in a graph, where spatial and temporal pairwise relations among objects are encoded via localized polar coordinates on graph edges. This representation makes our geometric relations invariant to global transformations and smooth trajectory changes, especially under non-holonomic motion. This allows our graph neural network to learn to effectively encode temporal and spatial interactions and fully leverage contextual and motion cues to obtain final scene interpretation by posing data association as edge classification. We establish a new state-of-the-art on nuScenes dataset and, more importantly, show that our method, PolarMOT, generalizes remarkably well across different locations (Boston, Singapore, Karlsruhe) and datasets (nuScenes and KITTI).

### Motion Inspired Unsupervised Perception and Prediction in Autonomous Driving.
- **链接**: [arXiv:2210.08061](https://arxiv.org/abs/2210.08061)
- **作者**: Mahyar Najibi, Jingwei Ji, Yin Zhou, Charles R. Qi, Xinchen Yan, Scott Ettinger et al.
- **🏷️ 机构**: Waymo
- **会议**: ECCV 2022

- **摘要（英，原文）**:

  > Learning-based perception and prediction modules in modern autonomous driving systems typically rely on expensive human annotation and are designed to perceive only a handful of predefined object categories. This closed-set paradigm is insufficient for the safety-critical autonomous driving task, where the autonomous vehicle needs to process arbitrarily many types of traffic participants and their motion behaviors in a highly dynamic world. To address this difficulty, this paper pioneers a novel and challenging direction, i.e., training perception and prediction models to understand open-set moving objects, with no human supervision. Our proposed framework uses self-learned flow to trigger an automated meta labeling pipeline to achieve automatic supervision. 3D detection experiments on the Waymo Open Dataset show that our method significantly outperforms classical unsupervised approaches and is even competitive to the counterpart with supervised scene flow. We further show that our approach generates highly promising results in open-set 3D detection and trajectory prediction, confirming its potential in closing the safety gap of fully supervised systems.

### A Closer Look at Invariances in Self-supervised Pre-training for 3D Vision.
- **链接**: [arXiv:2207.04997](https://arxiv.org/abs/2207.04997) · 📚 被引 21
- **作者**: Lanxiao Li, Michael Heizmann
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

- **摘要（英，原文）**:

  > Self-supervised pre-training for 3D vision has drawn increasing research interest in recent years. In order to learn informative representations, a lot of previous works exploit invariances of 3D features, e.g., perspective-invariance between views of the same scene, modality-invariance between depth and RGB images, format-invariance between point clouds and voxels. Although they have achieved promising results, previous researches lack a systematic and fair comparison of these invariances. To address this issue, our work, for the first time, introduces a unified framework, under which various pre-training methods can be investigated. We conduct extensive experiments and provide a closer look at the contributions of different invariances in 3D pre-training. Also, we propose a simple but effective method that jointly pre-trains a 3D encoder and a depth map encoder using contrastive learning. Models pre-trained with our method gain significant performance boost in downstream tasks. For instance, a pre-trained VoteNet outperforms previous methods on SUN RGB-D and ScanNet object detection benchmarks with a clear margin.
