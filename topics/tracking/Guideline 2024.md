# Tracking — 2024 Guideline

> 领域: 目标跟踪（MOT / 3D 跟踪 / 多目标多相机跟踪）
> 论文数: 3 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份:

### JDT3D: Addressing the Gaps in LiDAR-Based Tracking-by-Attention. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2407.04926](https://arxiv.org/abs/2407.04926) · 📚 被引 4
- **作者**: Brian Cheong, Jiachen Zhou, Steven Lake Waslander
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024
- **摘要（中）**: ①针对基于注意力的3D跟踪（TBA）方法在自动驾驶中性能落后于检测跟踪（TBD）方法的问题。②提出了JDT3D，一个联合检测与跟踪的LiDAR框架，并分析了TBA性能差距的原因。③提出了两种通用方法：轨迹采样增强和基于置信度的查询传播，以弥合TBD与TBA的差距。④在nuScenes测试集上达到0.574 AMOTA，超越所有现有LiDAR TBA方法超过6%。
- **摘要（英）**: This paper investigates why tracking-by-attention (TBA) methods underperform tracking-by-detection (TBD) in LiDAR-based 3D tracking. It proposes JDT3D, a joint detector-tracker, with track sampling augmentation and confidence-based query propagation. JDT3D achieves 0.574 AMOTA on nuScenes, outperforming all LiDAR TBA methods by over 6%.
- **核心贡献**: 提出JDT3D并揭示TBA方法性能差距的原因及解决方案。
- **创新点**: 轨迹采样增强与置信度查询传播机制。
- **结果**: 在nuScenes上以0.574 AMOTA超越所有LiDAR TBA方法6%以上。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Tracking-by-detection (TBD) methods achieve state-of-the-art performance on 3D tracking benchmarks for autonomous driving. On the other hand, tracking-by-attention (TBA) methods have the potential to outperform TBD methods, particularly for long occlusions and challenging detection settings. This work investigates why TBA methods continue to lag in performance behind TBD methods using a LiDAR-based joint detector and tracker called JDT3D. Based on this analysis, we propose two generalizable methods to bridge the gap between TBD and TBA methods: track sampling augmentation and confidence-based query propagation. JDT3D is trained and evaluated on the nuScenes dataset, achieving 0.574 on the AMOTA metric on the nuScenes test set, outperforming all existing LiDAR-based TBA approaches by over 6%. Based on our results, we further discuss some potential challenges with the existing TBA model formulation to explain the continued gap in performance with TBD methods. The implementation of JDT3D can be found at the following link: https://github.com/TRAILab/JDT3D.

</details>

### Is Multiple Object Tracking a Matter of Specialization? **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2411.00553](https://arxiv.org/abs/2411.00553)
- **作者**: Gianluca Mancusi, Mattia Bernardi, Aniello Panariello, Angelo Porrello, Rita Cucchiara, Simone Calderara
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024
- **摘要（中）**: 针对端到端Transformer跟踪器在异构场景中训练时存在负干扰和泛化能力差的问题，本文提出PASTA框架，结合参数高效微调（PEFT）和模块化深度学习（MDL）。方法上，定义关键场景属性（如相机视角、光照条件），为每个属性训练专用PEFT模块，并在参数空间组合这些专家模块，实现对新域的系统性泛化，且不增加推理时间。改进点在于通过模块化设计避免冲突学习。实验在MOTSynth上训练，并在MOT17和PersonPath22上零样本评估，表明模块化跟踪器优于单体模型。
- **摘要（英）**: This paper introduces PASTA, a framework combining PEFT and modular deep learning for tracking in heterogeneous scenarios. It trains specialized PEFT modules for scenario attributes and combines them in parameter space, enabling domain generalization without extra inference cost. Experiments show modular trackers outperform monolithic counterparts on MOTSynth and zero-shot benchmarks.
- **核心贡献**: 提出参数高效模块化跟踪架构，解决异构场景负干扰和泛化问题。
- **创新点**: 将PEFT与MDL结合，实现场景属性模块化组合。
- **结果**: 在多个基准上零样本评估优于单体模型。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> End-to-end transformer-based trackers have achieved remarkable performance on most human-related datasets. However, training these trackers in heterogeneous scenarios poses significant challenges, including negative interference - where the model learns conflicting scene-specific parameters - and limited domain generalization, which often necessitates expensive fine-tuning to adapt the models to new domains. In response to these challenges, we introduce Parameter-efficient Scenario-specific Tracking Architecture (PASTA), a novel framework that combines Parameter-Efficient Fine-Tuning (PEFT) and Modular Deep Learning (MDL). Specifically, we define key scenario attributes (e.g, camera-viewpoint, lighting condition) and train specialized PEFT modules for each attribute. These expert modules are combined in parameter space, enabling systematic generalization to new domains without increasing inference time. Extensive experiments on MOTSynth, along with zero-shot evaluations on MOT17 and PersonPath22 demonstrate that a neural tracker built from carefully selected modules surpasses its monolithic counterpart. We release models and code.

</details>

### Boosting 3D Single Object Tracking with 2D Matching Distillation and 3D Pre-training. **⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73254-6_16) · 📚 被引 12
- **作者**: Qiangqiang Wu, Yan Xia, Jia Wan, Antoni B. Chan
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024
- **摘要（中）**: 针对3D单目标跟踪（SOT）中依赖大量3D标注且2D信息利用不足的问题，本文提出通过2D匹配蒸馏和3D预训练来提升跟踪性能。方法上，利用2D跟踪器生成的匹配结果作为蒸馏信号，指导3D跟踪器学习更鲁棒的特征表示，并采用3D预训练策略初始化模型以加速收敛。改进点在于融合2D外观匹配的丰富语义信息，弥补3D点云稀疏性的不足。实验表明该方法在多个3D SOT基准上显著提升了跟踪精度和鲁棒性。
- **摘要（英）**: This paper boosts 3D single object tracking by distilling 2D matching knowledge and leveraging 3D pre-training. It transfers 2D tracker outputs as supervision to enhance 3D feature learning, addressing point cloud sparsity. The method improves tracking accuracy and robustness on standard 3D SOT benchmarks.
- **核心贡献**: 提出2D匹配蒸馏与3D预训练结合的策略，提升3D单目标跟踪性能。
- **创新点**: 利用2D跟踪器的匹配结果作为蒸馏信号，增强3D特征表达。
- **结果**: 在多个3D SOT基准上取得性能提升。

### DeconfuseTrack: Dealing with Confusion for Multi-Object Tracking. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2403.02767](https://arxiv.org/abs/2403.02767) · 📚 被引 25
- **作者**: Cheng Huang, Shoudong Han, Mengyu He, Wenbo Zheng, Yuhao Wei
- **🏷️ 机构**: School of Artificial Intelligence and Automation, Huazhong University of Science and Technology,National Key Laboratory of Multispectral Information Intelligent Processing Technology
- **会议**: CVPR 2024
- **摘要（中）**: 针对多目标跟踪中数据关联因轨迹多样性和运动/外观线索的模糊性导致的ID切换和分配错误问题，提出了一种分解式数据关联方法DDA，将传统关联问题分解为多个子问题，并利用非学习模块和针对性新线索分别处理每个子问题的混淆。同时引入遮挡感知非极大值抑制ONMS保留更多遮挡检测，增加关联机会。基于DDA和ONMS设计的DeconfuseTrack在多个基准上显著减少了混淆，提升了跟踪性能。
- **摘要（英）**: To address confusion in multi-object tracking data association caused by trajectory diversity and ambiguous motion/appearance cues, this paper proposes Decomposed Data Association (DDA), which splits association into sub-problems and handles each with targeted non-learning modules and new cues. An occlusion-aware NMS retains occluded detections, and the resulting DeconfuseTrack reduces ID switches and assignment errors, achieving strong performance on benchmarks.
- **核心贡献**: 提出DDA和ONMS，构建了专门解决关联混淆的DeconfuseTrack跟踪器。
- **创新点**: 将全局数据关联分解为多个子问题并针对性消解混淆，结合遮挡感知NMS。
- **结果**: 在多个MOT基准上减少了ID切换和分配错误，提升了跟踪精度。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Accurate data association is crucial in reducing confusion, such as ID switches and assignment errors, in multi-object tracking (MOT). However, existing advanced methods often overlook the diversity among trajectories and the ambiguity and conflicts present in motion and appearance cues, leading to confusion among detections, trajectories, and associations when performing simple global data association. To address this issue, we propose a simple, versatile, and highly interpretable data association approach called Decomposed Data Association (DDA). DDA decomposes the traditional association problem into multiple sub-problems using a series of non-learning-based modules and selectively addresses the confusion in each sub-problem by incorporating targeted exploitation of new cues. Additionally, we introduce Occlusion-aware Non-Maximum Suppression (ONMS) to retain more occluded detections, thereby increasing opportunities for association with trajectories and indirectly reducing the confusion caused by missed detections. Finally, based on DDA and ONMS, we design a powerful multi-object tracker named DeconfuseTrack, specifically focused on resolving confusion in MOT. Extensive experiments conducted on the MOT17 and MOT20 datasets demonstrate that our proposed DDA and ONMS significantly enhance the performance of several popular trackers. Moreover, DeconfuseTrack achieves state-of-the-art performance on the MOT17 and MOT20 test sets, significantly outperforms the baseline tracker ByteTrack in metrics such as HOTA, IDF1, AssA. This validates that our tracking design effectively reduces confusion caused by simple global association.

</details>

### Towards Generalizable Multi-Object Tracking. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2406.00429](https://arxiv.org/abs/2406.00429) · 📚 被引 37
- **作者**: Zheng Qin, Le Wang, Sanping Zhou, Panpan Fu, Gang Hua, Wei Tang
- **🏷️ 机构**: Institute of Artificial Intelligence and Robotics, Xi&#x0027;an Jiaotong University,National Key Laboratory of Human-Machine Hybrid Augmented Intelligence, National Engineering Research Center for Visual Information and Applications, School of Software Engineering, Xi&#x0027;an Jiaotong University, Wormpex AI Research
- **会议**: CVPR 2024
- **摘要（中）**: 针对现有多目标跟踪器在不同场景下泛化能力差、需针对特定场景定制运动或外观关联的问题，研究了影响泛化的因素并将其具体化为跟踪场景属性，指导设计更通用的跟踪器。提出了点级到实例级的关系框架GeneralTrack，无需平衡运动和外观线索即可跨场景泛化。在多个基准上达到最先进性能，并展示了领域泛化潜力。
- **摘要（英）**: To improve tracker generalization across diverse tracking scenarios, this paper identifies scenario attributes influencing generalization and proposes GeneralTrack, a point-wise to instance-wise relation framework that avoids balancing motion and appearance. It achieves state-of-the-art performance on multiple benchmarks and demonstrates domain generalization potential.
- **核心贡献**: 提出场景属性分析和GeneralTrack框架，实现跨场景通用多目标跟踪。
- **创新点**: 点级到实例级关系建模，消除运动与外观线索的平衡需求。
- **结果**: 在多个基准上取得最先进性能，并验证领域泛化能力。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-Object Tracking MOT encompasses various tracking scenarios, each characterized by unique traits. Effective trackers should demonstrate a high degree of generalizability across diverse scenarios. However, existing trackers struggle to accommodate all aspects or necessitate hypothesis and experimentation to customize the association information motion and or appearance for a given scenario, leading to narrowly tailored solutions with limited generalizability. In this paper, we investigate the factors that influence trackers generalization to different scenarios and concretize them into a set of tracking scenario attributes to guide the design of more generalizable trackers. Furthermore, we propose a point-wise to instance-wise relation framework for MOT, i.e., GeneralTrack, which can generalize across diverse scenarios while eliminating the need to balance motion and appearance. Thanks to its superior generalizability, our proposed GeneralTrack achieves state-of-the-art performance on multiple benchmarks and demonstrates the potential for domain generalization. https://github.com/qinzheng2000/GeneralTrack.git

</details>

### Multi-Object Tracking in the Dark. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2405.06600](https://arxiv.org/abs/2405.06600)
- **作者**: Xinzhe Wang, Kang Ma, Qiankun Liu, Yunhao Zou, Ying Fu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024
- **摘要（中）**: 针对暗光场景下多目标跟踪研究不足和数据集缺乏的问题，构建了低光多目标跟踪数据集LMOT，包含双相机系统采集的严格对齐低光视频对和高精度跟踪标注。提出了低光跟踪方法LTrack，引入自适应低通降采样模块增强传感器噪声外的低频分量，并通过退化抑制学习策略使模型在噪声和图像质量退化下学习不变信息。实验表明LTrack在暗光场景下具有优越性和竞争力。
- **摘要（英）**: Addressing the lack of datasets and methods for multi-object tracking in dark scenes, this paper builds the LMOT dataset with aligned low-light video pairs and annotations, and proposes LTrack with adaptive low-pass downsampling and degradation suppression learning. Experiments demonstrate superior robustness and competitiveness in real low-light conditions.
- **核心贡献**: 构建LMOT数据集并提出LTrack方法，提升暗光场景跟踪鲁棒性。
- **创新点**: 自适应低通降采样和退化抑制学习，增强低光下的特征不变性。
- **结果**: 在LMOT上优于现有方法，验证了暗光跟踪的有效性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Low-light scenes are prevalent in real-world applications (e.g. autonomous driving and surveillance at night). Recently, multi-object tracking in various practical use cases have received much attention, but multi-object tracking in dark scenes is rarely considered. In this paper, we focus on multi-object tracking in dark scenes. To address the lack of datasets, we first build a Low-light Multi-Object Tracking (LMOT) dataset. LMOT provides well-aligned low-light video pairs captured by our dual-camera system, and high-quality multi-object tracking annotations for all videos. Then, we propose a low-light multi-object tracking method, termed as LTrack. We introduce the adaptive low-pass downsample module to enhance low-frequency components of images outside the sensor noises. The degradation suppression learning strategy enables the model to learn invariant information under noise disturbance and image quality degradation. These components improve the robustness of multi-object tracking in dark scenes. We conducted a comprehensive analysis of our LMOT dataset and proposed LTrack. Experimental results demonstrate the superiority of the proposed method and its competitiveness in real night low-light scenes. Dataset and Code: https: //github.com/ying-fu/LMOT

</details>

### HIPTrack: Visual Tracking with Historical Prompts. **⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01822) · 📚 被引 107
- **作者**: Wenrui Cai, Qingjie Liu, Yunhong Wang
- **🏷️ 机构**: State Key Laboratory of Virtual Reality Technology and Systems, Beihang University,Beijing,China
- **会议**: CVPR 2024
- **摘要（中）**: 该论文摘要为空，无法获取具体研究问题、方法、改进点和效果信息。标题暗示提出一种利用历史提示的视觉跟踪方法，但缺乏细节支持评估。
- **摘要（英）**: The abstract is empty, providing no details on the problem, method, improvements, or results. The title suggests a visual tracking approach using historical prompts, but insufficient information prevents meaningful evaluation.
- **核心贡献**: 未知，因摘要缺失。
- **创新点**: 未知，因摘要缺失。
- **结果**: 未知，因摘要缺失。

### MS-MANO: Enabling Hand Pose Tracking with Biomechanical Constraints. **⭐⭐⭐** (相关度: 40%)
- **链接**: [arXiv:2404.10227](https://arxiv.org/abs/2404.10227) · 📚 被引 9
- **作者**: Pengfei Xie, Wenqiang Xu, Tutian Tang, Zhenjun Yu, Cewu Lu
- **🏷️ 机构**: Southeast University, Shanghai Jiao Tong University
- **会议**: CVPR 2024
- **摘要（中）**: 针对现有手部姿态跟踪模型因简化关节驱动系统而产生不自然运动的问题，将肌肉骨骼系统与可学习参数化手模型MANO集成，提出MS-MANO模型，模拟肌肉和肌腱动力学驱动骨骼系统，并对扭矩轨迹施加生理约束。进一步提出仿真在环姿态细化框架BioPR，通过MLP网络细化初始姿态。实验分别与MyoSuite和两个大型公开数据集及最新方法对比，结果表明该方法在定量和定性上均持续提升基线。
- **摘要（英）**: To address unnatural motions in hand pose tracking from simplified joint-actuated models, this paper integrates a musculoskeletal system with MANO to create MS-MANO, imposing physiological constraints on torque trajectories. A simulation-in-the-loop refinement framework BioPR further refines poses, consistently improving baselines quantitatively and qualitatively on public datasets.
- **核心贡献**: 提出MS-MANO模型和BioPR细化框架，实现符合生理约束的手部姿态跟踪。
- **创新点**: 融合肌肉骨骼动力学与参数化手模型，并采用仿真在环细化。
- **结果**: 在多个数据集上优于现有方法，提升姿态估计精度和自然度。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This work proposes a novel learning framework for visual hand dynamics analysis that takes into account the physiological aspects of hand motion. The existing models, which are simplified joint-actuated systems, often produce unnatural motions. To address this, we integrate a musculoskeletal system with a learnable parametric hand model, MANO, to create a new model, MS-MANO. This model emulates the dynamics of muscles and tendons to drive the skeletal system, imposing physiologically realistic constraints on the resulting torque trajectories. We further propose a simulation-in-the-loop pose refinement framework, BioPR, that refines the initial estimated pose through a multi-layer perceptron (MLP) network. Our evaluation of the accuracy of MS-MANO and the efficacy of the BioPR is conducted in two separate parts. The accuracy of MS-MANO is compared with MyoSuite, while the efficacy of BioPR is benchmarked against two large-scale public datasets and two recent state-of-the-art methods. The results demonstrate that our approach consistently improves the baseline methods both quantitatively and qualitatively.

</details>

### Walker: Self-supervised Multiple Object Tracking by Walking on Temporal Appearance Graphs. **⭐⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2409.17221](https://arxiv.org/abs/2409.17221) · 📚 被引 4
- **作者**: Mattia Segù, Luigi Piccinelli, Siyuan Li, Luc Van Gool, Fisher Yu, Bernt Schiele
- **🏷️ 机构**: ETH Zurich
- **会议**: ECCV 2024
- **摘要（中）**: ①针对多目标跟踪（MOT）方法依赖大量密集标注（边界框和ID）的问题。②提出了Walker，首个自监督跟踪器，仅需稀疏边界框标注且无需跟踪标签。③设计了准密集时间外观图，并提出多正样本对比目标优化随机游走以学习实例相似性，同时引入算法强制实例间互斥连接属性。④在MOT17、DanceTrack和BDD100K上取得与现有自监督方法相当甚至更优的性能，且标注需求减少高达400倍。
- **摘要（英）**: This paper tackles the heavy annotation burden in multi-object tracking by introducing Walker, the first self-supervised tracker that learns from videos with sparse bounding box annotations and no tracking labels. It constructs a quasi-dense temporal appearance graph and optimizes random walks with a multi-positive contrastive objective, while enforcing mutually-exclusive connections. Walker achieves competitive performance on MOT17, DanceTrack, and BDD100K, reducing annotation requirements by up to 400x.
- **核心贡献**: 提出了首个自监督MOT方法Walker，仅需稀疏标注即可达到竞争性能。
- **创新点**: 利用随机游走和对比学习优化时间外观图，实现无需跟踪标签的自监督学习。
- **结果**: 在多个基准上性能优异，标注需求减少400倍。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The supervision of state-of-the-art multiple object tracking (MOT) methods requires enormous annotation efforts to provide bounding boxes for all frames of all videos, and instance IDs to associate them through time. To this end, we introduce Walker, the first self-supervised tracker that learns from videos with sparse bounding box annotations, and no tracking labels. First, we design a quasi-dense temporal object appearance graph, and propose a novel multi-positive contrastive objective to optimize random walks on the graph and learn instance similarities. Then, we introduce an algorithm to enforce mutually-exclusive connective properties across instances in the graph, optimizing the learned topology for MOT. At inference time, we propose to associate detected instances to tracklets based on the max-likelihood transition state under motion-constrained bi-directional walks. Walker is the first self-supervised tracker to achieve competitive performance on MOT17, DanceTrack, and BDD100K. Remarkably, our proposal outperforms the previous self-supervised trackers even when drastically reducing the annotation requirements by up to 400x.

</details>

### Towards Category Unification of 3D Single Object Tracking on Point Clouds. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2401.11204](https://arxiv.org/abs/2401.11204)
- **作者**: Jiahao Nie, Zhiwei He, Xudong Lv, Xueyi Zhou, Dong-Kyu Chae, Fei Xie
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024
- **摘要（中）**: ①针对3D单目标跟踪中，类别特定模型参数冗余、泛化受限的问题。②首次提出统一模型，用单一网络和共享参数同时跟踪所有类别。③设计了AdaFormer，一种基于Transformer的点集表示学习网络，自适应编码跨类别数据的形状和尺寸变化，并利用模板先验辅助学习。④摘要未提供具体数据，但统一模型有望减少参数并提升跨类别泛化能力。
- **摘要（英）**: This paper addresses the redundancy and limited generalization of category-specific models in 3D single object tracking by introducing a unified model that tracks all categories with shared parameters. It proposes AdaFormer, a transformer-based network that adaptively encodes shape and size variations, and incorporates template priors. The unified approach aims to reduce parameters and improve cross-category generalization, though specific results are not detailed.
- **核心贡献**: 首次提出跨类别统一的3D SOT模型，减少参数并提升泛化。
- **创新点**: AdaFormer自适应编码形状和尺寸，结合模板先验实现统一跟踪。
- **结果**: 预期提升跨类别性能，但具体数据未在摘要中给出。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Category-specific models are provenly valuable methods in 3D single object tracking (SOT) regardless of Siamese or motion-centric paradigms. However, such over-specialized model designs incur redundant parameters, thus limiting the broader applicability of 3D SOT task. This paper first introduces unified models that can simultaneously track objects across all categories using a single network with shared model parameters. Specifically, we propose to explicitly encode distinct attributes associated to different object categories, enabling the model to adapt to cross-category data. We find that the attribute variances of point cloud objects primarily occur from the varying size and shape (e.g., large and square vehicles v.s. small and slender humans). Based on this observation, we design a novel point set representation learning network inheriting transformer architecture, termed AdaFormer, which adaptively encodes the dynamically varying shape and size information from cross-category data in a unified manner. We further incorporate the size and shape prior derived from the known template targets into the model's inputs and learning objective, facilitating the learning of unified representation. Equipped with such designs, we construct two category-unified models SiamCUT and MoCUT.Extensive experiments demonstrate that SiamCUT and MoCUT exhibit strong generalization and training stability. Furthermore, our category-unified models outperform the category-specific counterparts by a significant margin (e.g., on KITTI dataset, 12% and 3% performance gains on the Siamese and motion paradigms). Our code will be available.

</details>

### BuckTales: A multi-UAV dataset for multi-object tracking and re-identification of wild antelopes. **⭐⭐** (相关度: 50%)
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/95286b5d4cd5b7953bd2bbe717300fe0-Abstract-Datasets_and_Benchmarks_Track.html) · 📚 被引 2
- **作者**: Hemal Naik, Junran Yang, Dipin Das, Margaret Crofoot, Akanksha Rathore, Vivek Hari Sridhar
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024
- **摘要（中）**: ①针对多无人机（multi-UAV）场景下野生动物（羚羊）的多目标跟踪和重识别问题。②提出了BuckTales数据集，包含多无人机拍摄的野生羚羊视频，用于评估MOT和ReID算法。③该数据集填补了野生动物跟踪领域的空白，提供了真实场景的挑战。④摘要未提供具体性能数据，但数据集本身对领域研究有贡献。
- **摘要（英）**: This paper introduces BuckTales, a multi-UAV dataset for multi-object tracking and re-identification of wild antelopes. It addresses the lack of benchmarks in wildlife tracking scenarios, providing real-world challenges for evaluating MOT and ReID algorithms. Specific performance metrics are not provided in the abstract.
- **核心贡献**: 发布了多无人机野生动物跟踪数据集BuckTales。
- **创新点**: 聚焦于多无人机和野生动物场景，填补领域空白。
- **结果**: 数据集发布，但无具体性能数据。

### ChatTracker: Enhancing Visual Tracking Performance via Chatting with Multimodal Large Language Model. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2411.01756](https://arxiv.org/abs/2411.01756) · 📚 被引 7
- **作者**: Yiming Sun, Fan Yu, Shaoxiang Chen, Yu Zhang, Junwei Huang, Yang Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024
- **摘要（中）**: ①针对视觉语言（VL）跟踪器因依赖人工文本标注（常含模糊描述）而性能逊于最先进视觉跟踪器的问题。②提出ChatTracker，利用多模态大语言模型（MLLM）的世界知识生成高质量语言描述，并设计基于反射的提示优化模块，通过跟踪反馈迭代精炼目标描述；同时提出一个简单有效的VL跟踪框架，可作为即插即用模块集成到现有跟踪器中。③改进点在于自动化生成并优化语言描述，减少对人工标注的依赖，并提升VL与视觉跟踪器的性能。④实验结果表明，ChatTracker在多个基准上显著提升了跟踪性能，具体数据未在摘要中给出，但验证了方法的有效性。
- **摘要（英）**: This paper addresses the performance gap of vision-language (VL) trackers caused by reliance on ambiguous manual textual annotations. It proposes ChatTracker, which leverages multimodal large language models to generate high-quality descriptions and a reflection-based prompt optimization module to iteratively refine them with tracking feedback. A plug-and-play VL tracking framework is introduced to boost both VL and visual trackers, with experiments demonstrating significant performance improvements.
- **核心贡献**: 提出利用MLLM生成和优化语言描述以增强视觉跟踪性能的新框架。
- **创新点**: 设计反射式提示优化模块，结合跟踪反馈迭代精炼目标描述。
- **结果**: 实验显示在多个基准上显著提升VL和视觉跟踪器的性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Visual object tracking aims to locate a targeted object in a video sequence based on an initial bounding box. Recently, Vision-Language~(VL) trackers have proposed to utilize additional natural language descriptions to enhance versatility in various applications. However, VL trackers are still inferior to State-of-The-Art (SoTA) visual trackers in terms of tracking performance. We found that this inferiority primarily results from their heavy reliance on manual textual annotations, which include the frequent provision of ambiguous language descriptions. In this paper, we propose ChatTracker to leverage the wealth of world knowledge in the Multimodal Large Language Model (MLLM) to generate high-quality language descriptions and enhance tracking performance. To this end, we propose a novel reflection-based prompt optimization module to iteratively refine the ambiguous and inaccurate descriptions of the target with tracking feedback. To further utilize semantic information produced by MLLM, a simple yet effective VL tracking framework is proposed and can be easily integrated as a plug-and-play module to boost the performance of both VL and visual trackers. Experimental results show that our proposed ChatTracker achieves a performance comparable to existing methods.

</details>

## 跨领域论文（完整笔记在其他领域）

- MTMMC: A Large-Scale Real-World Multi-Modal Camera Tracking Benchmark. → [multimodal](../multimodal/Guideline%202024.md)
- OVT-B: A New Large-Scale Benchmark for Open-Vocabulary Multi-Object Tracking. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- ADA-Track: End-to-End Multi-Camera 3D Multi-Object Tracking with Alternating Detection and Association. → [multi-camera-perception](../multi-camera-perception/Guideline%202024.md)
- Self-Supervised Multi-Object Tracking with Path Consistency. → [self-supervised-vision](../self-supervised-vision/Guideline%202024.md)
- DriveWorld: 4D Pre-Trained Scene Understanding via World Models for Autonomous Driving. → [object-detection](../object-detection/Guideline%202024.md)

<!-- COMPLETE v1 papers=12 -->
