# Tracking — 2023 Guideline

> 领域: 目标跟踪（MOT / 3D 跟踪 / 多目标多相机跟踪）
> 论文数: 12 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份:

### CXTrack: Improving 3D Point Cloud Tracking with Contextual Information. **⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00111) · 📚 被引 39
- **作者**: Tian-Xing Xu, Yuan-Chen Guo, Yu-Kun Lai, Song-Hai Zhang
- **🏷️ 机构**: Tsinghua University,China, Cardiff University,United Kingdom
- **会议**: CVPR 2023
- **摘要（中）**: ①针对3D点云跟踪中目标外观相似或遮挡时，仅依赖几何特征导致跟踪鲁棒性不足的问题。②提出CXTrack，通过引入上下文信息（如周围点云场景和时序上下文）增强目标特征表达，并设计上下文感知的匹配模块。③相比现有基于几何或外观的方法，显式建模了上下文关系，提升了判别力。④在KITTI和nuScenes等基准上取得了领先的跟踪精度，尤其在遮挡场景下性能提升显著。
- **摘要（英）**: This paper addresses the robustness issue in 3D point cloud tracking caused by similar appearances or occlusions. It proposes CXTrack, which enhances target features by incorporating contextual information from the surrounding scene and temporal context, with a context-aware matching module. Compared to geometry- or appearance-based methods, it explicitly models contextual relations, achieving state-of-the-art tracking accuracy on benchmarks like KITTI and nuScenes, especially under occlusion.
- **核心贡献**: 提出一种利用上下文信息改进3D点云跟踪的新框架。
- **创新点**: 在特征提取和匹配中显式融合场景与时序上下文。
- **结果**: 在多个基准上取得领先性能，遮挡场景下提升显著。

### MOTRv2: Bootstrapping End-to-End Multi-Object Tracking by Pretrained Object Detectors. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02112) · 📚 被引 246
- **作者**: Yuang Zhang, Tiancai Wang, Xiangyu Zhang
- **🏷️ 机构**: Shanghai Jiao Tong University, MEGVII Technology
- **会议**: CVPR 2023
- **摘要（中）**: ①针对端到端多目标跟踪方法（如MOTR）在复杂场景下检测性能不足，导致跟踪精度受限的问题。②提出MOTRv2，利用预训练目标检测器（如DINO）的检测结果作为查询初始化，引导端到端跟踪器，实现检测与跟踪的协同优化。③相比纯端到端方法，通过引入强检测先验，提升了检测召回率和跟踪稳定性。④在多个MOT基准（如MOT17）上取得了SOTA性能，显著优于MOTR等基线。
- **摘要（英）**: This paper addresses the limited detection performance of end-to-end MOT methods like MOTR in complex scenes, which restricts tracking accuracy. It proposes MOTRv2, which uses a pretrained object detector (e.g., DINO) to initialize queries, guiding the end-to-end tracker for joint optimization. Compared to pure end-to-end approaches, it leverages strong detection priors, improving recall and tracking stability. It achieves SOTA performance on benchmarks like MOT17, significantly outperforming baselines.
- **核心贡献**: 提出一种利用预训练检测器引导端到端MOT的新范式。
- **创新点**: 将检测先验融入查询初始化，实现检测与跟踪的协同。
- **结果**: 在MOT17等基准上取得SOTA性能。

### Observation-Centric SORT: Rethinking SORT for Robust Multi-Object Tracking. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00934) · 📚 被引 910
- **作者**: Jinkun Cao, Jiangmiao Pang, Xinshuo Weng, Rawal Khirodkar, Kris Kitani
- **🏷️ 机构**: Carnegie Mellon University, Shanghai AI Laboratory, Nvidia
- **会议**: CVPR 2023
- **摘要（中）**: ①针对经典SORT方法在遮挡和相机运动下关联不准确、鲁棒性差的问题。②提出Observation-Centric SORT（OC-SORT），重新设计SORT，以观测为中心，利用观测间的运动一致性（如恒定速度模型）和观测噪声建模，改进关联过程。③相比原SORT，增强了在非线性运动和遮挡场景下的稳定性。④在MOT17、MOT20等基准上取得了SOTA性能，尤其在拥挤场景下表现突出。
- **摘要（英）**: This paper addresses the inaccurate association and poor robustness of classic SORT under occlusion and camera motion. It proposes Observation-Centric SORT (OC-SORT), which redesigns SORT to be observation-centric, using motion consistency between observations and noise modeling to improve association. Compared to original SORT, it enhances stability in nonlinear motion and occlusion. It achieves SOTA performance on MOT17 and MOT20, especially in crowded scenes.
- **核心贡献**: 提出观测为中心的SORT变体，提升关联鲁棒性。
- **创新点**: 利用观测间运动一致性替代预测中心，减少误差累积。
- **结果**: 在MOT17和MOT20上取得SOTA性能。

### MotionTrack: Learning Robust Short-Term and Long-Term Motions for Multi-Object Tracking. **⭐⭐⭐** (相关度: 75%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01720) · 📚 被引 167
- **作者**: Zheng Qin, Sanping Zhou, Le Wang, Jinghai Duan, Gang Hua, Wei Tang
- **🏷️ 机构**: Institute of Artificial Intelligence and Robotics, Xi&#x0027;an Jiaotong University,National Key Laboratory of Human-Machine Hybrid Augmented Intelligence, National Engineering Research Center for Visual Information and Applications, School of Software Engineering, Xi&#x0027;an Jiaotong University, Wormpex AI Research
- **会议**: CVPR 2023
- **摘要（中）**: ①针对多目标跟踪中短期运动（如快速移动）和长期运动（如遮挡后重现）建模不足的问题。②提出MotionTrack，学习鲁棒的短期和长期运动模型，短期运动用于帧间关联，长期运动用于轨迹重连。③相比仅依赖短期运动的方法，显式建模长期运动，增强了遮挡恢复能力。④在MOT17和MOT20上取得了有竞争力的性能，尤其在长期遮挡场景下ID切换减少。
- **摘要（英）**: This paper addresses insufficient modeling of short-term motions (e.g., fast movement) and long-term motions (e.g., reappearance after occlusion) in MOT. It proposes MotionTrack, which learns robust short- and long-term motion models for inter-frame association and track reconnection. Compared to short-term-only methods, it explicitly models long-term motion, improving occlusion recovery. It achieves competitive performance on MOT17 and MOT20, with reduced ID switches in long-term occlusion scenarios.
- **核心贡献**: 提出联合学习短期和长期运动的多目标跟踪方法。
- **创新点**: 将长期运动建模用于轨迹重连。
- **结果**: 在MOT17和MOT20上取得有竞争力性能。

### Focus On Details: Online Multi-Object Tracking with Diverse Fine-Grained Representation. **⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01086) · 📚 被引 85
- **作者**: Hao Ren, Shoudong Han, Huilin Ding, Ziwen Zhang, Hongwei Wang, Faquan Wang
- **🏷️ 机构**: School of Artificial Intelligence and Automation, Huazhong University of Science and Technology,National Key Laboratory of Science and Technology on Multispectral Information Processing
- **会议**: CVPR 2023
- **摘要（中）**: ①针对在线多目标跟踪中，仅使用粗粒度特征（如全局外观）导致相似目标区分困难的问题。②提出Focus On Details方法，学习多样化的细粒度表示（如局部区域特征），并设计特征融合策略以增强判别力。③相比单一全局特征，细粒度表示能更好区分外观相似的目标。④在MOT17和MOT20上取得了有竞争力的性能，尤其在密集场景下关联精度提升。
- **摘要（英）**: This paper addresses the difficulty in distinguishing similar targets when using only coarse-grained features (e.g., global appearance) in online MOT. It proposes Focus On Details, which learns diverse fine-grained representations (e.g., local region features) with a fusion strategy to enhance discriminability. Compared to single global features, fine-grained representations better differentiate similar targets. It achieves competitive performance on MOT17 and MOT20, with improved association accuracy in dense scenes.
- **核心贡献**: 提出基于多样细粒度表示的在线多目标跟踪方法。
- **创新点**: 利用局部区域特征增强目标判别力。
- **结果**: 在MOT17和MOT20上取得有竞争力性能。

### Referring Multi-Object Tracking. **⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01406)
- **作者**: Dongming Wu, Wencheng Han, Tiancai Wang, Xingping Dong, Xiangyu Zhang, Jianbing Shen
- **🏷️ 机构**: MEGVII
- **会议**: CVPR 2023
- **摘要（中）**: ①该论文针对多目标跟踪中缺乏自然语言交互能力的问题，提出Referring Multi-Object Tracking任务。②方法上，可能结合了语言描述与视觉特征进行目标关联和跟踪。③相比传统MOT，其创新在于引入文本查询来指定跟踪目标。④由于摘要缺失，具体效果未知，但任务设定具有新颖性。
- **摘要（英）**: This paper addresses the lack of natural language interaction in multi-object tracking by proposing the Referring Multi-Object Tracking task. It likely integrates language descriptions with visual features for target association and tracking. The innovation lies in using textual queries to specify tracking targets, distinguishing it from traditional MOT. Specific results are unavailable due to missing abstract.
- **核心贡献**: 提出Referring Multi-Object Tracking任务，将语言描述引入多目标跟踪。
- **创新点**: 利用自然语言查询作为跟踪目标的指定方式。
- **结果**: 具体效果未知，因摘要缺失。

### UTM: A Unified Multiple Object Tracking Model with Identity-Aware Feature Enhancement. **⭐⭐⭐** (相关度: 75%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02095) · 📚 被引 87
- **作者**: Sisi You, Hantao Yao, Bing-Kun Bao, Changsheng Xu
- **🏷️ 机构**: Nanjing University of Posts and Telecommunications, Institute of Automation, Chinese Academy of Sciences (CASIA),State Key Laboratory of Multimodal Artificial Intelligence Systems
- **会议**: CVPR 2023
- **摘要（中）**: ①该论文针对多目标跟踪中身份特征不充分的问题，提出统一模型UTM。②方法上，通过身份感知特征增强模块提升目标区分度。③相比现有MOT方法，其改进在于统一处理检测和跟踪，并强化身份信息。④摘要缺失，具体性能数据未提供。
- **摘要（英）**: This paper addresses insufficient identity features in multi-object tracking by proposing a unified model UTM with identity-aware feature enhancement. It improves target discrimination through dedicated feature modules. The key improvement is unifying detection and tracking while strengthening identity cues. Specific performance metrics are unavailable due to missing abstract.
- **核心贡献**: 提出UTM统一多目标跟踪模型，增强身份感知特征。
- **创新点**: 身份感知特征增强模块用于提升跟踪鲁棒性。
- **结果**: 具体效果未知，因摘要缺失。

### 3D-POP - An Automated Annotation Approach to Facilitate Markerless 2D-3D Tracking of Freely Moving Birds with Marker-Based Motion Capture. **⭐⭐** (相关度: 30%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02038) · 📚 被引 27
- **作者**: Hemal Naik, Alex Hoi Hang Chan, Junran Yang, Mathilde Delacoux, Iain D. Couzin, Fumihiro Kano et al.
- **🏷️ 机构**: Max Planck Institute of Animal Behavior,Dept. of Collective Behavior and Dept. of Ecology of Animal Societies, University of Konstanz,Dept. of Biology
- **会议**: CVPR 2023
- **摘要（中）**: ①该论文针对自由活动鸟类的标记点追踪问题，提出自动化标注方法3D-POP。②方法上，结合标记点运动捕捉与无标记2D-3D追踪。③相比传统手动标注，其改进在于自动化流程。④摘要缺失，具体效果未提及。
- **摘要（英）**: This paper addresses markerless tracking of freely moving birds by proposing an automated annotation approach 3D-POP. It combines marker-based motion capture with 2D-3D tracking. The improvement is automating the annotation process. Specific results are unavailable due to missing abstract.
- **核心贡献**: 提出3D-POP自动化标注方法，用于鸟类运动追踪。
- **创新点**: 结合标记点捕捉与无标记追踪的自动化流程。
- **结果**: 具体效果未知，因摘要缺失。

### Autoregressive Visual Tracking. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00935)
- **作者**: Xing Wei, Yifan Bai, Yongchao Zheng, Dahu Shi, Yihong Gong
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023
- **摘要（中）**: ①该论文针对视觉跟踪中的时序建模问题，提出自回归视觉跟踪方法。②方法上，利用自回归模型逐步预测目标状态，增强时序一致性。③相比传统跟踪器，其改进在于显式建模时间依赖。④摘要缺失，但自回归方法在生成任务中表现优异，预期可提升跟踪精度。
- **摘要（英）**: This paper addresses temporal modeling in visual tracking by proposing an autoregressive approach. It predicts target states sequentially, enhancing temporal consistency. The improvement is explicit modeling of time dependencies. Specific results are unavailable, but autoregressive methods show promise in generation tasks.
- **核心贡献**: 提出自回归视觉跟踪框架，改进时序建模。
- **创新点**: 将自回归生成机制应用于目标状态预测。
- **结果**: 具体效果未知，因摘要缺失。

### GarmentTracking: Category-Level Garment Pose Tracking. **⭐⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2303.13913](https://arxiv.org/abs/2303.13913) · 📚 被引 11
- **作者**: Han Xue, Wenqiang Xu, Jieyi Zhang, Tutian Tang, Yutong Li, Wenxin Du et al.
- **🏷️ 机构**: Shanghai Qi Zhi Institute, Shanghai Jiao Tong University, Cornell University
- **会议**: CVPR 2023
- **摘要（中）**: ①该论文针对服装类别级姿态跟踪问题，提出完整解决方案。②方法上，包括VR-Garment记录系统、VR-Folding数据集和GarmentTracking在线跟踪框架，预测点云序列中的完整服装姿态。③相比基线，其改进在于处理大非刚性变形，并同时提升速度和精度。④实验表明，GarmentTracking在复杂变形下表现优异，优于基线方法。
- **摘要（英）**: This paper addresses category-level garment pose tracking by proposing a complete package: VR-Garment recording system, VR-Folding dataset, and GarmentTracking framework. It predicts full garment pose from point cloud sequences. The improvement is handling large non-rigid deformations with better speed and accuracy. Experiments show superior performance over baselines.
- **核心贡献**: 提出VR-Folding数据集和GarmentTracking框架，解决服装姿态跟踪。
- **创新点**: 结合VR模拟与端到端跟踪，处理非刚性变形。
- **结果**: 在速度和精度上均优于基线方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Garments are important to humans. A visual system that can estimate and track the complete garment pose can be useful for many downstream tasks and real-world applications. In this work, we present a complete package to address the category-level garment pose tracking task: (1) A recording system VR-Garment, with which users can manipulate virtual garment models in simulation through a VR interface. (2) A large-scale dataset VR-Folding, with complex garment pose configurations in manipulation like flattening and folding. (3) An end-to-end online tracking framework GarmentTracking, which predicts complete garment pose both in canonical space and task space given a point cloud sequence. Extensive experiments demonstrate that the proposed GarmentTracking achieves great performance even when the garment has large non-rigid deformation. It outperforms the baseline approach on both speed and accuracy. We hope our proposed solution can serve as a platform for future research. Codes and datasets are available in https://garment-tracking.robotflow.ai.

</details>

### Exploring Lightweight Hierarchical Vision Transformers for Efficient Visual Tracking. **⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2308.06904](https://arxiv.org/abs/2308.06904) · 📚 被引 127
- **作者**: Ben Kang, Xin Chen, Dong Wang, Houwen Peng, Huchuan Lu
- **🏷️ 机构**: Dalian University of Technology,School of Information and Communication Engineering, Microsoft Research
- **会议**: ICCV 2023
- **摘要（中）**: 针对Transformer跟踪器速度慢、难以在计算受限设备上部署的问题，提出了HiT高效跟踪模型家族，通过Bridge Module将深层特征的高层信息融入浅层大分辨率特征，以生成更适合跟踪头的特征，并设计了双图像位置编码同时编码搜索区域和模板的位置信息。在Nvidia Jetson AGX边缘设备上达到61 fps，在LaSOT基准上取得64.6% AUC，超越所有先前高效跟踪器。
- **摘要（英）**: This paper tackles the low-speed limitation of Transformer-based trackers by introducing HiT, an efficient tracking family with a Bridge Module that integrates high-level deep features into shallow large-resolution features, plus a dual-image position encoding. It achieves 61 fps on edge devices and 64.6% AUC on LaSOT, outperforming prior efficient trackers.
- **核心贡献**: 提出轻量级层次化视觉Transformer跟踪器HiT，实现高速与高性能平衡。
- **创新点**: Bridge Module和双图像位置编码设计。
- **结果**: 在边缘设备上达到61 fps，LaSOT AUC 64.6%。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Transformer-based visual trackers have demonstrated significant progress owing to their superior modeling capabilities. However, existing trackers are hampered by low speed, limiting their applicability on devices with limited computational power. To alleviate this problem, we propose HiT, a new family of efficient tracking models that can run at high speed on different devices while retaining high performance. The central idea of HiT is the Bridge Module, which bridges the gap between modern lightweight transformers and the tracking framework. The Bridge Module incorporates the high-level information of deep features into the shallow large-resolution features. In this way, it produces better features for the tracking head. We also propose a novel dual-image position encoding technique that simultaneously encodes the position information of both the search region and template images. The HiT model achieves promising speed with competitive performance. For instance, it runs at 61 frames per second (fps) on the Nvidia Jetson AGX edge device. Furthermore, HiT attains 64.6% AUC on the LaSOT benchmark, surpassing all previous efficient trackers.

</details>

### Tracking without Label: Unsupervised Multiple Object Tracking via Contrastive Similarity Learning. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2309.00942](https://arxiv.org/abs/2309.00942) · 📚 被引 14
- **作者**: Sha Meng, Dian Shao, Jiacheng Guo, Shan Gao
- **🏷️ 机构**: Northwestern Polytechnical University,Xi&#x2019;an,China
- **会议**: ICCV 2023
- **摘要（中）**: 针对无监督多目标跟踪中缺乏标签且存在物体遮挡、相互干扰等问题，提出了基于对比相似性学习的UCSL方法，包含自对比、交叉对比和模糊对比三个模块，分别通过帧内直接和帧间间接对比学习判别性表示、对齐跨帧匹配结果以缓解遮挡影响、以及匹配模糊物体以增加关联确定性。在现有基准上，该方法仅需ReID头的有限帮助即可超越现有无监督方法，甚至比许多全监督方法精度更高。
- **摘要（英）**: This paper addresses unsupervised multiple object tracking challenges by proposing UCSL with three contrast modules: self-contrast for discriminative representations, cross-contrast to mitigate occlusion effects, and ambiguity contrast to enhance association certainty. It outperforms existing unsupervised methods and even surpasses many fully supervised approaches on benchmarks.
- **核心贡献**: 提出无监督对比相似性学习框架UCSL，显著提升无监督MOT精度。
- **创新点**: 三模块对比学习机制，特别是模糊对比处理。
- **结果**: 超越现有无监督方法，并接近或超过部分全监督方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Unsupervised learning is a challenging task due to the lack of labels. Multiple Object Tracking (MOT), which inevitably suffers from mutual object interference, occlusion, etc., is even more difficult without label supervision. In this paper, we explore the latent consistency of sample features across video frames and propose an Unsupervised Contrastive Similarity Learning method, named UCSL, including three contrast modules: self-contrast, cross-contrast, and ambiguity contrast. Specifically, i) self-contrast uses intra-frame direct and inter-frame indirect contrast to obtain discriminative representations by maximizing self-similarity. ii) Cross-contrast aligns cross- and continuous-frame matching results, mitigating the persistent negative effect caused by object occlusion. And iii) ambiguity contrast matches ambiguous objects with each other to further increase the certainty of subsequent object association through an implicit manner. On existing benchmarks, our method outperforms the existing unsupervised methods using only limited help from ReID head, and even provides higher accuracy than lots of fully supervised methods.

</details>

### MBPTrack: Improving 3D Point Cloud Tracking with Memory networks and Box Priors. **⭐⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2303.05071](https://arxiv.org/abs/2303.05071) · 📚 被引 25
- **作者**: Tian-Xing Xu, Yuan-Chen Guo, Yu-Kun Lai, Song-Hai Zhang
- **🏷️ 机构**: Tsinghua University,China, Cardiff University,United Kingdom
- **会议**: ICCV 2023
- **摘要（中）**: ①该论文针对3D单目标跟踪中外观变化和尺寸差异问题，提出MBPTrack，利用记忆网络和框先验进行粗到细定位。②方法上，采用外部记忆存储过去帧和目标掩码，通过transformer模块传播目标线索，并利用第一帧的框先验自适应采样参考点。③改进点在于结合记忆机制和框先验，提升不同尺寸目标的定位精度。④实验表明，MBPTrack在KITTI、nuScenes和Waymo数据集上达到最先进性能，显著优于现有方法。
- **摘要（英）**: This paper addresses appearance variation and size differences in 3D single object tracking by proposing MBPTrack, which uses memory networks and box priors for coarse-to-fine localization. It propagates target cues via transformer and adaptively samples reference points. Experiments show state-of-the-art performance on KITTI, nuScenes, and Waymo datasets.
- **核心贡献**: 提出MBPTrack，结合记忆网络和框先验提升3D跟踪性能。
- **创新点**: 记忆机制和自适应参考点采样。
- **结果**: 在多个数据集上达到最先进性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D single object tracking has been a crucial problem for decades with numerous applications such as autonomous driving. Despite its wide-ranging use, this task remains challenging due to the significant appearance variation caused by occlusion and size differences among tracked targets. To address these issues, we present MBPTrack, which adopts a Memory mechanism to utilize past information and formulates localization in a coarse-to-fine scheme using Box Priors given in the first frame. Specifically, past frames with targetness masks serve as an external memory, and a transformer-based module propagates tracked target cues from the memory to the current frame. To precisely localize objects of all sizes, MBPTrack first predicts the target center via Hough voting. By leveraging box priors given in the first frame, we adaptively sample reference points around the target center that roughly cover the target of different sizes. Then, we obtain dense feature maps by aggregating point features into the reference points, where localization can be performed more effectively. Extensive experiments demonstrate that MBPTrack achieves state-of-the-art performance on KITTI, nuScenes and Waymo Open Dataset, while running at 50 FPS on a single RTX3090 GPU.

</details>

### ZoomTrack: Target-aware Non-uniform Resizing for Efficient Visual Tracking. **⭐⭐** (相关度: 50%)
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/9fc291fef2f9607a46777d367f900a15-Abstract-Conference.html)
- **作者**: Yutong Kou, Jin Gao, Bing Li, Gang Wang, Weiming Hu, Yizheng Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023
- **摘要（中）**: 该论文摘要缺失，无法提供具体内容。根据标题推测，可能针对视觉跟踪中的目标感知非均匀缩放问题，提出ZoomTrack方法，但缺乏详细信息。
- **摘要（英）**: The abstract is missing, so specific details are unavailable. Based on the title, it likely addresses target-aware non-uniform resizing for efficient visual tracking, but no concrete information is provided.
- **核心贡献**: 未知，因摘要缺失。
- **创新点**: 未知，因摘要缺失。
- **结果**: 未知，因摘要缺失。

## 跨领域论文（完整笔记在其他领域）

- GeoMAE: Masked Geometric Target Prediction for Self-supervised Point Cloud Pre-Training. → [self-supervised-vision](../self-supervised-vision/Guideline%202023.md)
- Standing Between Past and Future: Spatio-Temporal Modeling for Multi-Camera 3D Multi-Object Tracking. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- OVTrack: Open-Vocabulary Multiple Object Tracking. → [open-set-detection](../open-set-detection/Guideline%202023.md)
- Unsupervised 3D Perception with 2D Vision-Language Distillation for Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202023.md)

<!-- COMPLETE v1 papers=14 -->
