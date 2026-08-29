# Tracking — 2025 Guideline

> 领域: 目标跟踪（MOT / 3D 跟踪 / 多目标多相机跟踪）
> 论文数: 10 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### TrackAny3D: Transferring Pretrained 3D Models for Category-Unified 3D Point Cloud Tracking.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02623) · 📚 被引 1
- **作者**: Mengmeng Wang, Haonan Wang, Yulong Li, Xiangjie Kong, Jiaxin Du, Guojiang Shen et al.
- **🏷️ 机构**: Zhejiang University of Technology, RMIT University
- **会议**: ICCV 2025

### GRAE-3DMOT: Geometry Relation-Aware Encoder for Online 3D Multi-Object Tracking.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Kim_GRAE-3DMOT_Geometry_Relation-Aware_Encoder_for_Online_3D_Multi-Object_Tracking_CVPR_2025_paper.html) · 📚 被引 0
- **作者**: Hyunseop Kim, Hyo-Jun Lee, Yonguk Lee, Jinu Lee, Hanul Kim, Yeong Jun Koh
- **🏷️ 机构**: Chungnam National University, Kangwon National University, 42Dot Inc.
- **会议**: CVPR 2025

### Omnidirectional Multi-Object Tracking.
- **链接**: [arXiv:2503.04565](https://arxiv.org/abs/2503.04565)
- **作者**: Kai Luo, Hao Shi, Sheng Wu, Fei Teng, Mengfei Duan, Chang Huang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### Language Decoupling with Fine-Grained Knowledge Guidance for Referring Multi-Object Tracking.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02193) · 📚 被引 0
- **作者**: Guangyao Li, Siping Zhuang, Yajun Jian, Yan Yan, Hanzi Wang
- **🏷️ 机构**: Xiamen University,Key Laboratory of Multimedia Trusted Perception and Efficient Computing, Ministry of Education of China,P.R. China,361005
- **会议**: ICCV 2025

> In this paper, we present a novel benchmark, GSOT3D, that aims at facilitating development of generic 3D single object tracking (SOT) in the wild. Specifically, GSOT3D offers 620 sequences with 123K frames, and covers a wide selection of 54 object categories. Each sequence is offered with multiple modalities, including the point cloud (PC), RGB image, and depth. This allows GSOT3D to support various 3D tracking tasks, such as single-modal 3D SOT on PC and multi-modal 3D SOT on RGB-PC or RGB-D, and thus greatly broadens research directions for 3D object tracking. To provide highquality per-frame 3D annotations, all sequences are labeled manually with multiple rounds of meticulous inspection and refinement. To our best knowledge, GSOT3D is the largest benchmark dedicated to various generic 3D object tracking tasks. To understand how existing 3D trackers perform and to provide comparisons for future research on GSOT3D, we assess eight representative point cloud-based tracking models. Our evaluation results exhibit that these models heavily degrade on GSOT3D, and more efforts are required for robust and generic 3D object tracking. Besides, to encourage future research, we present a simple yet effective generic 3D tracker, named PROT3D, that localizes the target object via a progressive spatial-temporal network and outperforms all current solutions by a large margin. By releasing GSOT3D, we expect to advance further 3D tracking in future research and applications. Our benchmark and model as well as the evaluation results will be publicly released at our webpage https://github.com/ailovejinx/GSOT3D.

</details>

### MUST: The First Dataset and Unified Framework for Multispectral UAV Single Object Tracking.
- **链接**: [arXiv:2503.17699](https://arxiv.org/abs/2503.17699) · 📚 被引 12
- **作者**: Haolin Qin, Tingfa Xu, Tianhao Li, Zhenxiang Chen, Tao Feng, Jianan Li
- **🏷️ 机构**: Beijing Institute of Technology
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce a data capture system and a new dataset, HO-Cap, for 3D reconstruction and pose tracking of hands and objects in videos. The system leverages multiple RGBD cameras and a HoloLens headset for data collection, avoiding the use of expensive 3D scanners or mocap systems. We propose a semi-automatic method for annotating the shape and pose of hands and objects in the collected videos, significantly reducing the annotation time compared to manual labeling. With this system, we captured a video dataset of humans interacting with objects to perform various tasks, including simple pick-and-place actions, handovers between hands, and using objects according to their affordance, which can serve as human demonstrations for research in embodied AI and robot manipulation. Our data capture setup and annotation framework will be available for the community to use in reconstructing 3D shapes of objects and human hands and tracking their poses in videos.

</details>

### Focusing on Tracks for Online Multi-Object Tracking.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Shim_Focusing_on_Tracks_for_Online_Multi-Object_Tracking_CVPR_2025_paper.html) · 📚 被引 20
- **作者**: Kyujin Shim, Kangwook Ko, Yujin Yang, Changick Kim
- **🏷️ 机构**: Korea Advanced Institute of Science and Technology (KAIST)
- **会议**: CVPR 2025

### SPMTrack: Spatio-Temporal Parameter-Efficient Fine-Tuning with Mixture of Experts for Scalable Visual Tracking.
- **链接**: [arXiv:2503.18338](https://arxiv.org/abs/2503.18338) · 📚 被引 13
- **作者**: Wenrui Cai, Qingjie Liu, Yunhong Wang
- **🏷️ 机构**: Beihang University,State Key Laboratory of Virtual Reality Technology and Systems,Beijing,China
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Most state-of-the-art trackers adopt one-stream paradigm, using a single Vision Transformer for joint feature extraction and relation modeling of template and search region images. However, relation modeling between different image patches exhibits significant variations. For instance, background regions dominated by target-irrelevant information require reduced attention allocation, while foreground, particularly boundary areas, need to be be emphasized. A single model may not effectively handle all kinds of relation modeling simultaneously. In this paper, we propose a novel tracker called SPMTrack based on mixture-of-experts tailored for visual tracking task (TMoE), combining the capability of multiple experts to handle diverse relation modeling more flexibly. Benefiting from TMoE, we extend relation modeling from image pairs to spatio-temporal context, further improving tracking accuracy with minimal increase in model parameters. Moreover, we employ TMoE as a parameter-efficient fine-tuning method, substantially reducing trainable parameters, which enables us to train SPMTrack of varying scales efficiently and preserve the generalization ability of pretrained models to achieve superior performance. We conduct experiments on seven datasets, and experimental results demonstrate that our method significantly outperforms current state-of-the-art trackers. The source code is available at https://github.com/WenRuiCai/SPMTrack.

</details>

### Autoregressive Sequential Pretraining for Visual Tracking.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Liang_Autoregressive_Sequential_Pretraining_for_Visual_Tracking_CVPR_2025_paper.html) · 📚 被引 8
- **作者**: Shiyi Liang, Yifan Bai, Yihong Gong, Xing Wei
- **🏷️ 机构**: Xi&#x2019;an Jiaotong University,School of Software Engineering
- **会议**: CVPR 2025

### Exploring Historical Information for RGBE Visual Tracking with Mamba.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Sun_Exploring_Historical_Information_for_RGBE_Visual_Tracking_with_Mamba_CVPR_2025_paper.html) · 📚 被引 7
- **作者**: Chuanyu Sun, Jiqing Zhang, Yang Wang, Huilin Ge, Qianchen Xia, Baocai Yin et al.
- **🏷️ 机构**: Dalian University of Technology,Key Laboratory of Social Computing and Cognitive Intelligence, Dalian Maritime University, Jiangsu University of Science and Technology
- **会议**: CVPR 2025

### GaPT-DAR: Category-level Garments Pose Tracking via Integrated 2D Deformation and 3D Reconstruction.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_GaPT-DAR_Category-level_Garments_Pose_Tracking_via_Integrated_2D_Deformation_and_CVPR_2025_paper.html) · 📚 被引 3
- **作者**: Li Zhang, Mingliang Xu, Jianan Wang, Qiaojun Yu, Lixin Yang, Yonglu Li et al.
- **🏷️ 机构**: University of Science and Technology of China,Hefei,China, Astribot,Shenzhen,China, Shanghai Jiao Tong University,Shanghai,China
- **会议**: CVPR 2025

### Delta: Dense Efficient Long-Range 3D tracking for any video.
- **链接**: [arXiv:2410.24211](https://arxiv.org/abs/2410.24211)
- **作者**: Tuan Duc Ngo, Peiye Zhuang, Evangelos Kalogerakis, Chuang Gan, Sergey Tulyakov, Hsin-Ying Lee et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Efficient Motion Prompt Learning for Robust Visual Tracking.
- **链接**: [arXiv:2505.16321](https://arxiv.org/abs/2505.16321) · [代码](https://github.com/zj5559/Motion-Prompt-Tracking)
- **作者**: Jie Zhao, Xin Chen, Yongsheng Yuan, Michael Felsberg, Dong Wang, Huchuan Lu
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Tracking dense 3D motion from monocular videos remains challenging, particularly when aiming for pixel-level precision over long sequences. We introduce DELTA, a novel method that efficiently tracks every pixel in 3D space, enabling accurate motion estimation across entire videos. Our approach leverages a joint global-local attention mechanism for reduced-resolution tracking, followed by a transformer-based upsampler to achieve high-resolution predictions. Unlike existing methods, which are limited by computational inefficiency or sparse tracking, DELTA delivers dense 3D tracking at scale, running over 8x faster than previous methods while achieving state-of-the-art accuracy. Furthermore, we explore the impact of depth representation on tracking performance and identify log-depth as the optimal choice. Extensive experiments demonstrate the superiority of DELTA on multiple benchmarks, achieving new state-of-the-art results in both 2D and 3D dense tracking tasks. Our method provides a robust solution for applications requiring fine-grained, long-term motion tracking in 3D space.

</details>

### 6D Object Pose Tracking in Internet Videos for Robotic Manipulation.
- **链接**: [arXiv:2503.10307](https://arxiv.org/abs/2503.10307)
- **作者**: Georgy Ponimatkin, Martin Cífka, Tomás Soucek, Médéric Fourmy, Yann Labbé, Vladimír Petrík et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We seek to extract a temporally consistent 6D pose trajectory of a manipulated object from an Internet instructional video. This is a challenging set-up for current 6D pose estimation methods due to uncontrolled capturing conditions, subtle but dynamic object motions, and the fact that the exact mesh of the manipulated object is not known. To address these challenges, we present the following contributions. First, we develop a new method that estimates the 6D pose of any object in the input image without prior knowledge of the object itself. The method proceeds by (i) retrieving a CAD model similar to the depicted object from a large-scale model database, (ii) 6D aligning the retrieved CAD model with the input image, and (iii) grounding the absolute scale of the object with respect to the scene. Second, we extract smooth 6D object trajectories from Internet videos by carefully tracking the detected objects across video frames. The extracted object trajectories are then retargeted via trajectory optimization into the configuration space of a robotic manipulator. Third, we thoroughly evaluate and ablate our 6D pose estimation method on YCB-V and HOPE-Video datasets as well as a new dataset of instructional videos manually annotated with approximate 6D object trajectories. We demonstrate significant improvements over existing state-of-the-art RGB 6D pose estimation methods. Finally, we show that the 6D object motion estimated from Internet videos can be transferred to a 7-axis robotic manipulator both in a virtual simulator as well as in a real world set-up. We also successfully apply our method to egocentric videos taken from the EPIC-KITCHENS dataset, demonstrating potential for Embodied AI applications.

</details>

## 跨领域论文（完整笔记在其他领域）

- All-Day Multi-Camera Multi-Target Tracking. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)

## 🆕 增量新增

### MMOT: The First Challenging Benchmark for Drone-based Multispectral Multi-Object Tracking. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2510.12565](https://arxiv.org/abs/2510.12565) · 📚 被引 1
- **作者**: Tianhao Li, Tingfa Xu, Ying Wang, Haolin Qin, Xu Lin, Jianan Li
- **🏷️ 机构**: Beijing Institute of Technology, Beijing Institute of Technology, Tsinghua University
- **会议**: NeurIPS 2025
- **摘要（中）**: 针对无人机多目标跟踪中RGB算法在航拍视角下因目标小、遮挡严重和背景杂乱而性能下降的问题，该论文提出了首个用于无人机多光谱多目标跟踪的基准数据集MMOT，包含125个视频序列和超过48.88万个标注，覆盖八类目标，并具有极端小目标、高密度、严重遮挡和复杂运动等挑战。此外，论文还提出了一个多光谱跟踪框架，利用定向标注和光谱特征提取来提升跟踪性能。相比现有RGB跟踪方法，该工作通过引入多光谱信息增强了目标判别能力，并提供了精确的定向标注以减少航拍视角下的定位模糊。实验表明，该数据集和框架为多光谱无人机跟踪提供了有效基准，推动了该领域的发展。
- **摘要（英）**: This paper addresses the performance degradation of RGB-based multi-object tracking in drone scenarios caused by small targets, severe occlusions, and cluttered backgrounds. It introduces MMOT, the first multispectral UAV tracking benchmark with 125 sequences and over 488.8K annotations, and a tracking framework leveraging spectral features and oriented annotations. The work improves object discriminability and localization accuracy under degraded spatial conditions, providing a comprehensive benchmark to advance multispectral drone tracking.
- **核心贡献**: 首个大规模多光谱无人机多目标跟踪基准数据集及配套跟踪框架。
- **创新点**: 引入多光谱信息和精确定向标注以应对航拍视角下的跟踪挑战。
- **结果**: 提供了包含48.88万标注的125个序列数据集，并验证了框架的有效性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Drone-based multi-object tracking is essential yet highly challenging due to small targets, severe occlusions, and cluttered backgrounds. Existing RGB-based tracking algorithms heavily depend on spatial appearance cues such as color and texture, which often degrade in aerial views, compromising reliability. Multispectral imagery, capturing pixel-level spectral reflectance, provides crucial cues that enhance object discriminability under degraded spatial conditions. However, the lack of dedicated multispectral UAV datasets has hindered progress in this domain. To bridge this gap, we introduce MMOT, the first challenging benchmark for drone-based multispectral multi-object tracking. It features three key characteristics: (i) Large Scale - 125 video sequences with over 488.8K annotations across eight categories; (ii) Comprehensive Challenges - covering diverse conditions such as extreme small targets, high-density scenarios, severe occlusions, and complex motion; and (iii) Precise Oriented Annotations - enabling accurate localization and reduced ambiguity under aerial perspectives. To better extract spectral features and leverage oriented annotations, we further present a multispectral and orientation-aware MOT scheme adapting existing methods, featuring: (i) a lightweight Spectral 3D-Stem integrating spectral features while preserving compatibility with RGB pretraining; (ii) an orientation-aware Kalman filter for precise state estimation; and (iii) an end-to-end orientation-adaptive transformer. Extensive experiments across representative trackers consistently show that multispectral input markedly improves tracking performance over RGB baselines, particularly for small and densely packed objects. We believe our work will advance drone-based multispectral multi-object tracking research. Our MMOT, code, and benchmarks are publicly available at https://github.com/Annzstbl/MMOT.

</details>

### Multiple Object Tracking as ID Prediction. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Gao_Multiple_Object_Tracking_as_ID_Prediction_CVPR_2025_paper.html) · 📚 被引 52
- **作者**: Ruopeng Gao, Ji Qi, Limin Wang
- **🏷️ 机构**: Nanjing University,State Key Laboratory for Novel Software Technology, China Mobile (Suzhou) Software Technology Co., Ltd.
- **会议**: CVPR 2025
- **摘要（中）**: 该论文针对多目标跟踪中数据关联的复杂性问题，提出将多目标跟踪视为ID预测任务，通过直接预测目标身份来简化跟踪流程。方法可能采用端到端的ID嵌入学习，避免传统两步法的误差累积。相比现有方法，该思路减少了手工设计的关联规则，提升了跟踪的简洁性和效率。实验效果未在摘要中给出，但该方向在MOT领域具有创新性。
- **摘要（英）**: This paper reformulates multi-object tracking as an ID prediction task, simplifying data association by directly predicting target identities. It likely employs end-to-end ID embedding learning to reduce error accumulation in traditional two-stage methods. This approach minimizes handcrafted association rules, enhancing tracking simplicity and efficiency, though specific results are not provided.
- **核心贡献**: 提出将MOT作为ID预测的新范式。
- **创新点**: 端到端ID预测替代传统关联步骤。
- **结果**: 未提供具体数据。

### GSOT3D: Towards Generic 3D Single Object Tracking in the Wild. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2412.02129](https://arxiv.org/abs/2412.02129)
- **作者**: Yifan Jiao, Yunhao Li, Junhua Ding, Qing Yang, Song Fu, Heng Fan et al.
- **🏷️ 机构**: Institute of Software Chinese Academy of Sciences, University of North Texas
- **会议**: ICCV 2025
- **摘要（中）**: ①针对野外环境下通用3D单目标跟踪（SOT）缺乏大规模基准的问题，现有数据集类别有限且模态单一。②提出了GSOT3D基准，包含620个序列、123K帧、54个类别，并提供点云、RGB图像和深度多模态数据，支持单模态和多模态3D跟踪任务，所有标注经过多轮人工精修。③相比已有基准，GSOT3D在规模、类别覆盖和模态多样性上显著提升，是最大的通用3D跟踪基准。④评估了8种代表性点云跟踪模型，结果显示现有模型性能大幅下降，表明需要更鲁棒的通用3D跟踪方法。
- **摘要（英）**: This paper addresses the lack of large-scale benchmarks for generic 3D single object tracking in the wild. It introduces GSOT3D, a benchmark with 620 sequences, 123K frames, 54 categories, and multi-modal data (point cloud, RGB, depth), supporting various tracking tasks. Compared to existing benchmarks, GSOT3D offers superior scale, category diversity, and modality richness. Evaluations of eight point cloud trackers show significant performance degradation, highlighting the need for more robust methods.
- **核心贡献**: 提出了最大规模的通用3D单目标跟踪基准GSOT3D，支持多模态和多任务评估。
- **创新点**: 首次提供覆盖54类、多模态的野外3D跟踪基准，并系统评估现有模型。
- **结果**: 现有8种点云跟踪模型在GSOT3D上性能显著下降，表明通用3D跟踪仍需改进。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we present a novel benchmark, GSOT3D, that aims at facilitating development of generic 3D single object tracking (SOT) in the wild. Specifically, GSOT3D offers 620 sequences with 123K frames, and covers a wide selection of 54 object categories. Each sequence is offered with multiple modalities, including the point cloud (PC), RGB image, and depth. This allows GSOT3D to support various 3D tracking tasks, such as single-modal 3D SOT on PC and multi-modal 3D SOT on RGB-PC or RGB-D, and thus greatly broadens research directions for 3D object tracking. To provide highquality per-frame 3D annotations, all sequences are labeled manually with multiple rounds of meticulous inspection and refinement. To our best knowledge, GSOT3D is the largest benchmark dedicated to various generic 3D object tracking tasks. To understand how existing 3D trackers perform and to provide comparisons for future research on GSOT3D, we assess eight representative point cloud-based tracking models. Our evaluation results exhibit that these models heavily degrade on GSOT3D, and more efforts are required for robust and generic 3D object tracking. Besides, to encourage future research, we present a simple yet effective generic 3D tracker, named PROT3D, that localizes the target object via a progressive spatial-temporal network and outperforms all current solutions by a large margin. By releasing GSOT3D, we expect to advance further 3D tracking in future research and applications. Our benchmark and model as well as the evaluation results will be publicly released at our webpage https://github.com/ailovejinx/GSOT3D.

</details>

### What You Have is What You Track: Adaptive and Robust Multimodal Tracking. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2507.05899](https://arxiv.org/abs/2507.05899) · 📚 被引 5
- **作者**: Yuedong Tan, Jiawei Shao, Eduard Zamfir, Ruanjun Li, Zhaochong An, Chao Ma et al.
- **🏷️ 机构**: China Telecom,TeleAI, University of Wurzburg,Computer Vision Lab, CAIDAS &#x0026; IFI, ShanghaiTech University
- **会议**: ICCV 2025
- **摘要（中）**: ①针对多模态跟踪中传感器同步问题导致模态数据时间不完整，现有跟踪器性能显著下降的问题。②提出了一个灵活框架，通过异构混合专家（MoE）融合机制和视频级掩码策略，动态激活计算单元以适应缺失模态，同时保持时间一致性和空间完整性。③相比已有方法，该框架能自适应不同缺失率和场景复杂度，提升鲁棒性。④实验表明，模型在多种缺失率下保持稳定性能，并优于现有跟踪器。
- **摘要（英）**: This paper addresses performance degradation in multimodal tracking due to temporally incomplete data from sensor synchronization issues. It proposes a flexible framework with a Heterogeneous Mixture-of-Experts fusion mechanism and video-level masking to dynamically adapt to missing modalities. Compared to existing methods, it maintains temporal consistency and spatial completeness, improving robustness. Experiments show stable performance across varying missing rates and superiority over existing trackers.
- **核心贡献**: 提出了自适应多模态跟踪框架，处理时间不完整数据。
- **创新点**: 引入异构MoE和视频级掩码策略，动态适应缺失模态。
- **结果**: 在多种缺失率下保持鲁棒性能，优于现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal data is known to be helpful for visual tracking by improving robustness to appearance variations. However, sensor synchronization challenges often compromise data availability, particularly in video settings where shortages can be temporal. Despite its importance, this area remains underexplored. In this paper, we present the first comprehensive study on tracker performance with temporally incomplete multimodal data. Unsurprisingly, under such a circumstance, existing trackers exhibit significant performance degradation, as their rigid architectures lack the adaptability needed to effectively handle missing modalities. To address these limitations, we propose a flexible framework for robust multimodal tracking. We venture that a tracker should dynamically activate computational units based on missing data rates. This is achieved through a novel Heterogeneous Mixture-of-Experts fusion mechanism with adaptive complexity, coupled with a video-level masking strategy that ensures both temporal consistency and spatial completeness which is critical for effective video tracking. Surprisingly, our model not only adapts to varying missing rates but also adjusts to scene complexity. Extensive experiments show that our model achieves SOTA performance across 9 benchmarks, excelling in both conventional complete and missing modality settings. The code and benchmark will be publicly available at https://github.com/supertyd/FlexTrack/tree/main.

</details>

### LA-MOTR: End-to-End Multi-Object Tracking by Learnable Association. **⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01156) · 📚 被引 7
- **作者**: Peng Wang, Yongcai Wang, Hualong Cao, Wang Chen, Deying Li
- **🏷️ 机构**: School of Information, Renmin University of China
- **会议**: ICCV 2025
- **摘要（中）**: 针对端到端多目标跟踪中关联模块设计不足的问题，提出LA-MOTR，通过可学习关联机制改进MOTR框架。方法引入可学习的关联模块，增强轨迹与检测的匹配能力，并优化查询传播。相比原有MOTR，提升了跟踪的鲁棒性和准确性。在MOT17等基准上取得显著性能提升。
- **摘要（英）**: Addressing the limitations of association in end-to-end multi-object tracking, this paper proposes LA-MOTR with a learnable association module to enhance query propagation and matching. It improves upon MOTR by enabling more robust tracking, achieving notable gains on benchmarks like MOT17.
- **核心贡献**: 提出可学习关联机制，改进端到端多目标跟踪性能。
- **创新点**: 将关联过程参数化并集成到Transformer跟踪框架中。
- **结果**: 在MOT基准上提升跟踪精度和鲁棒性。

### Samba: Synchronized Set-of-Sequences Modeling for Multiple Object Tracking. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2410.01806](https://arxiv.org/abs/2410.01806)
- **作者**: Mattia Segù, Luigi Piccinelli, Siyuan Li, Yung-Hsu Yang, Luc Van Gool, Bernt Schiele
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025
- **摘要（中）**: ①该论文针对多目标跟踪中复杂场景（如舞蹈、团队运动、动物群体）下轨迹长程依赖、轨迹间相互依赖以及时间遮挡难以建模的问题。②提出了Samba，一种线性时间的序列集合模型，通过同步多个选择性状态空间来联合处理多个轨迹，并自回归预测未来轨迹查询，同时维护跨轨迹的同步长程记忆表示；将其集成到基于传播的跟踪框架中，形成SambaMOTR，并引入MaskObs技术处理不确定观测。③相比现有方法，首次有效解决了长程依赖、轨迹间依赖和时间遮挡的联合建模问题，且具有线性时间复杂度。④实验表明，SambaMOTR在多个基准上显著提升跟踪性能，尤其在复杂场景下表现优异，但摘要未提供具体数值。
- **摘要（英）**: This paper addresses the challenge of modeling long-range dependencies, inter-tracklet dependencies, and temporal occlusions in multi-object tracking for complex scenarios. It proposes Samba, a linear-time set-of-sequences model that synchronizes multiple selective state-spaces to jointly process tracklets, integrated into a propagation-based tracker SambaMOTR with a MaskObs technique for uncertain observations. The method achieves significant performance improvements on multiple benchmarks, though specific numbers are not detailed in the abstract.
- **核心贡献**: 提出了SambaMOTR，首个联合建模长程依赖、轨迹间依赖和时间遮挡的线性时间多目标跟踪器。
- **创新点**: 通过同步多个选择性状态空间实现轨迹间记忆共享，创新性地处理复杂场景下的跟踪挑战。
- **结果**: 在多个基准上显著提升跟踪性能，尤其在复杂场景下表现优异。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multiple object tracking in complex scenarios - such as coordinated dance performances, team sports, or dynamic animal groups - presents unique challenges. In these settings, objects frequently move in coordinated patterns, occlude each other, and exhibit long-term dependencies in their trajectories. However, it remains a key open research question on how to model long-range dependencies within tracklets, interdependencies among tracklets, and the associated temporal occlusions. To this end, we introduce Samba, a novel linear-time set-of-sequences model designed to jointly process multiple tracklets by synchronizing the multiple selective state-spaces used to model each tracklet. Samba autoregressively predicts the future track query for each sequence while maintaining synchronized long-term memory representations across tracklets. By integrating Samba into a tracking-by-propagation framework, we propose SambaMOTR, the first tracker effectively addressing the aforementioned issues, including long-range dependencies, tracklet interdependencies, and temporal occlusions. Additionally, we introduce an effective technique for dealing with uncertain observations (MaskObs) and an efficient training recipe to scale SambaMOTR to longer sequences. By modeling long-range dependencies and interactions among tracked objects, SambaMOTR implicitly learns to track objects accurately through occlusions without any hand-crafted heuristics. Our approach significantly surpasses prior state-of-the-art on the DanceTrack, BFT, and SportsMOT datasets.

</details>

### CO-MOT: Boosting End-to-end Transformer-based Multi-Object Tracking via Coopetition Label Assignment and Shadow Sets.
- **链接**: [出版页](https://openreview.net/forum?id=0ov0dMQ3mN)
- **作者**: Feng Yan, Weixin Luo, Yujie Zhong, Yiyang Gan, Lin Ma
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### More Than Meets the Eye: Enhancing Multi-Object Tracking Even with Prolonged Occlusions.
- **链接**: [出版页](https://proceedings.mlr.press/v267/galoaa25a.html)
- **作者**: Bishoy Galoaa, Somaieh Amraee, Sarah Ostadabbas
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### S2-Track: A Simple yet Strong Approach for End-to-End 3D Multi-Object Tracking.
- **链接**: [出版页](https://proceedings.mlr.press/v267/tang25p.html)
- **作者**: Tao Tang, Lijun Zhou, Pengkun Hao, Zihang He, Kalok Ho, Shuo Gu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Visual Sync: Multi-Camera Synchronization via Cross-View Object Motion.
- **链接**: [arXiv:2512.02017](https://arxiv.org/abs/2512.02017)
- **作者**: Shaowei Liu, David Yifan Yao, Saurabh Gupta, Shenlong Wang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Today, people can easily record memorable moments, ranging from concerts, sports events, lectures, family gatherings, and birthday parties with multiple consumer cameras. However, synchronizing these cross-camera streams remains challenging. Existing methods assume controlled settings, specific targets, manual correction, or costly hardware. We present VisualSync, an optimization framework based on multi-view dynamics that aligns unposed, unsynchronized videos at millisecond accuracy. Our key insight is that any moving 3D point, when co-visible in two cameras, obeys epipolar constraints once properly synchronized. To exploit this, VisualSync leverages off-the-shelf 3D reconstruction, feature matching, and dense tracking to extract tracklets, relative poses, and cross-view correspondences. It then jointly minimizes the epipolar error to estimate each camera's time offset. Experiments on four diverse, challenging datasets show that VisualSync outperforms baseline methods, achieving an median synchronization error below 50 ms.

</details>

### SynCL: A Synergistic Training Strategy with Instance-Aware Contrastive Learning for End-to-End Multi-Camera 3D Tracking.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/056932270665ac01253e5ef7c5dc32aa-Abstract-Conference.html)
- **作者**: Shubo Lin, Yutong Kou, Zirui Wu, Shaoru Wang, Bing Li, Weiming Hu et al.
- **🏷️ 机构**: Institute of Automation, Chinese Academy of Sciences, Harbin Institute of Technology, Apple
- **会议**: NeurIPS 2025

### STAR: Spatial-Temporal Tracklet Matching for Multi-Object Tracking.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/62c599c5c2b365ba464a26ebad05b690-Abstract-Conference.html)
- **作者**: Xuewei Bai, Yongcai Wang, Deying Li, Haodi Ping, Chunxu Li
- **🏷️ 机构**: Renmin University of China, Beijing University of Technology
- **会议**: NeurIPS 2025

### Dual-Path Temporal Decoder for End-to-End Multi-Object Tracking.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/07054a34f24ac3ef64c5f2fdf571b8c0-Abstract-Conference.html)
- **作者**: Hyunseop Kim, Juheon Jeong, Hanul Kim, Yeong Jun Koh
- **🏷️ 机构**: Chungnam National University, Seoul National University of Science and Technology
- **会议**: NeurIPS 2025

### TrackingWorld: World-centric Monocular 3D Tracking of Almost All Pixels.
- **链接**: [arXiv:2512.08358](https://arxiv.org/abs/2512.08358)
- **作者**: Jiahao Lu, Weitao Xiong, Jiacheng Deng, Peng Li, Tianyu Huang, Zhiyang Dou et al.
- **🏷️ 机构**: The Hong Kong University of Science and Technology, Xiamen University (Malaysia Campus), University of Science and Technology of China
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular 3D tracking aims to capture the long-term motion of pixels in 3D space from a single monocular video and has witnessed rapid progress in recent years. However, we argue that the existing monocular 3D tracking methods still fall short in separating the camera motion from foreground dynamic motion and cannot densely track newly emerging dynamic subjects in the videos. To address these two limitations, we propose TrackingWorld, a novel pipeline for dense 3D tracking of almost all pixels within a world-centric 3D coordinate system. First, we introduce a tracking upsampler that efficiently lifts the arbitrary sparse 2D tracks into dense 2D tracks. Then, to generalize the current tracking methods to newly emerging objects, we apply the upsampler to all frames and reduce the redundancy of 2D tracks by eliminating the tracks in overlapped regions. Finally, we present an efficient optimization-based framework to back-project dense 2D tracks into world-centric 3D trajectories by estimating the camera poses and the 3D coordinates of these 2D tracks. Extensive evaluations on both synthetic and real-world datasets demonstrate that our system achieves accurate and dense 3D tracking in a world-centric coordinate frame.

</details>

### HO-Cap: A Capture System and Dataset for 3D Reconstruction and Pose Tracking of Hand-Object Interaction.
- **链接**: [arXiv:2406.06843](https://arxiv.org/abs/2406.06843)
- **作者**: Jikai Wang, Qifan Zhang, Yu-Wei Chao, Bowen Wen, Xiaohu Guo, Yu Xiang
- **🏷️ 机构**: University of Texas at Dallas, NVIDIA, University of Texas, Dallas
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce a data capture system and a new dataset, HO-Cap, for 3D reconstruction and pose tracking of hands and objects in videos. The system leverages multiple RGBD cameras and a HoloLens headset for data collection, avoiding the use of expensive 3D scanners or mocap systems. We propose a semi-automatic method for annotating the shape and pose of hands and objects in the collected videos, significantly reducing the annotation time compared to manual labeling. With this system, we captured a video dataset of humans interacting with objects to perform various tasks, including simple pick-and-place actions, handovers between hands, and using objects according to their affordance, which can serve as human demonstrations for research in embodied AI and robot manipulation. Our data capture setup and annotation framework will be available for the community to use in reconstructing 3D shapes of objects and human hands and tracking their poses in videos.

</details>

## 跨领域论文（完整笔记在其他领域）

- All-Day Multi-Camera Multi-Target Tracking. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
- Attention to Trajectory: Trajectory-Aware Open-Vocabulary Tracking. → [open-set-detection](../open-set-detection/Guideline%202025.md)
- VOVTrack: Exploring the Potentiality in Raw Videos for Open-Vocabulary Multi-Object Tracking. → [open-set-detection](../open-set-detection/Guideline%202025.md)
- Multi-View 3D Point Tracking. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
- Details Matter for Indoor Open-Vocabulary 3D Instance Segmentation. → [open-set-detection](../open-set-detection/Guideline%202025.md)
- AD-GS: Object-Aware B-Spline Gaussian Splatting for Self-Supervised Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202025.md)
- OVTR: End-to-End Open-Vocabulary Multiple Object Tracking with Transformer. → [open-set-detection](../open-set-detection/Guideline%202025.md)
<!-- COMPLETE v1 papers=28 -->
