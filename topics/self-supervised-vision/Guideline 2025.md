# Self-supervised Vision — 2025 Guideline

> 领域: 视觉自监督学习（对比学习、MAE、DINO 系）
> 论文数: 54 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份:

### BOE-ViT: Boosting Orientation Estimation with Equivariance in Self-Supervised 3D Subtomogram Alignment. **⭐⭐⭐** (相关度: 40%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Jiang_BOE-ViT_Boosting_Orientation_Estimation_with_Equivariance_in_Self-Supervised_3D_Subtomogram_CVPR_2025_paper.html)
- **作者**: Runmin Jiang, Jackson Daggett, Shriya Pingulkar, Yizhou Zhao, Priyanshu Dhingra, Daniel Brown et al.
- **🏷️ 机构**: Carnegie Mellon University, K. J. Somaiya College of Engineering, Rajiv Gandhi Institute of Petroleum Technology
- **会议**: CVPR 2025
- **摘要（中）**: ①针对自监督3D亚断层图像对齐中方向估计精度不足的问题。②提出BOE-ViT，利用等变性（equivariance）增强方向估计，在自监督框架下进行3D亚断层图像对齐。③相比现有方法，通过引入等变性约束，提升了对旋转变化的鲁棒性和对齐精度。④摘要未提供具体数据，但方法在方向估计任务上具有理论优势。
- **摘要（英）**: This paper addresses the issue of inaccurate orientation estimation in self-supervised 3D subtomogram alignment. It proposes BOE-ViT, which leverages equivariance to enhance orientation estimation within a self-supervised framework. Compared to existing methods, it improves robustness to rotational variations and alignment accuracy. Specific quantitative results are not provided in the abstract.
- **核心贡献**: 提出基于等变性的自监督方向估计方法，提升3D亚断层图像对齐性能。
- **创新点**: 将等变性约束引入自监督3D对齐任务。
- **结果**: 在方向估计任务上实现更优的对齐精度（具体数据未给出）。

### Multi-Scale Neighborhood Occupancy Masked Autoencoder for Self-Supervised Learning in LiDAR Point Clouds. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2502.20316](https://arxiv.org/abs/2502.20316) · 📚 被引 5
- **作者**: Mohamed Abdelsamad, Michael Ulrich, Claudius Gläser, Abhinav Valada
- **🏷️ 机构**: Bosch Center for AI, University of Freiburg
- **会议**: CVPR 2025
- **摘要（中）**: 针对LiDAR点云掩码自编码器中大面积空区域导致的信息泄露和高计算复杂度问题，提出多尺度邻域占用掩码自编码器（NOMAE）。方法仅在非掩码体素邻域内进行占用重建，并通过分层掩码生成技术捕捉不同尺寸物体特征。在nuScenes和Waymo数据集上对语义分割和3D检测任务进行了评估，与判别式和生成式SSL方法对比。
- **摘要（英）**: To address information leakage and high computational complexity in masked autoencoders for LiDAR point clouds due to large empty areas, NOMAE performs occupancy reconstruction only in neighborhoods of non-masked voxels. It incorporates hierarchical mask generation for multi-scale feature capture. Evaluations on nuScenes and Waymo for segmentation and detection show effectiveness.
- **核心贡献**: 提出邻域占用重建的掩码自编码器，提升LiDAR点云自监督学习效率。
- **创新点**: 仅在非掩码体素邻域内重建占用，避免信息泄露并降低复杂度。
- **结果**: 在多个数据集和任务上优于现有SSL方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Masked autoencoders (MAE) have shown tremendous potential for self-supervised learning (SSL) in vision and beyond. However, point clouds from LiDARs used in automated driving are particularly challenging for MAEs since large areas of the 3D volume are empty. Consequently, existing work suffers from leaking occupancy information into the decoder and has significant computational complexity, thereby limiting the SSL pre-training to only 2D bird's eye view encoders in practice. In this work, we propose the novel neighborhood occupancy MAE (NOMAE) that overcomes the aforementioned challenges by employing masked occupancy reconstruction only in the neighborhood of non-masked voxels. We incorporate voxel masking and occupancy reconstruction at multiple scales with our proposed hierarchical mask generation technique to capture features of objects of different sizes in the point cloud. NOMAEs are extremely flexible and can be directly employed for SSL in existing 3D architectures. We perform extensive evaluations on the nuScenes and Waymo Open datasets for the downstream perception tasks of semantic segmentation and 3D object detection, comparing with both discriminative and generative SSL methods. The results demonstrate that NOMAE sets the new state-of-the-art on multiple benchmarks for multiple point cloud perception tasks.

</details>

### PSA-SSL: Pose and Size-aware Self-Supervised Learning on LiDAR Point Clouds. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2503.13914](https://arxiv.org/abs/2503.13914) · 📚 被引 4
- **作者**: Barza Nisar, Steven L. Waslander
- **🏷️ 机构**: University of Toronto Robotics Institute
- **会议**: CVPR 2025
- **摘要（中）**: 针对现有3D点云自监督学习预文本任务忽略物体姿态和尺度信息的问题，提出PSA-SSL方法。通过定义自监督边界框回归预文本任务保留姿态和尺寸信息，并引入LiDAR波束模式增强以学习传感器无关特征。在Waymo、nuScenes和SemanticKITTI数据集上，单预训练模型在有限标签的语义分割任务上取得显著提升。
- **摘要（英）**: To address the neglect of object pose and scale in 3D point cloud SSL pretext tasks, PSA-SSL defines a self-supervised bounding box regression task to retain geometric information. It also incorporates LiDAR beam pattern augmentation for sensor-agnostic features. Experiments on Waymo, nuScenes, and SemanticKITTI show significant improvements in segmentation with limited labels.
- **核心贡献**: 提出姿态和尺寸感知的自监督学习框架，提升3D点云特征质量。
- **创新点**: 引入边界框回归预文本任务和波束模式增强。
- **结果**: 在多个自动驾驶数据集上优于现有SSL方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning (SSL) on 3D point clouds has the potential to learn feature representations that can transfer to diverse sensors and multiple downstream perception tasks. However, recent SSL approaches fail to define pretext tasks that retain geometric information such as object pose and scale, which can be detrimental to the performance of downstream localization and geometry-sensitive 3D scene understanding tasks, such as 3D semantic segmentation and 3D object detection. We propose PSA-SSL, a novel extension to point cloud SSL that learns object pose and size-aware (PSA) features. Our approach defines a self-supervised bounding box regression pretext task, which retains object pose and size information. Furthermore, we incorporate LiDAR beam pattern augmentation on input point clouds, which encourages learning sensor-agnostic features. Our experiments demonstrate that with a single pretrained model, our light-weight yet effective extensions achieve significant improvements on 3D semantic segmentation with limited labels across popular autonomous driving datasets (Waymo, nuScenes, SemanticKITTI). Moreover, our approach outperforms other state-of-the-art SSL methods on 3D semantic segmentation (using up to 10 times less labels), as well as on 3D object detection. Our code will be released on https://github.com/TRAILab/PSA-SSL.

</details>

### A Unified Approach to Interpreting Self-supervised Pre-training Methods for 3D Point Clouds via Interactions. **⭐⭐⭐** (相关度: 50%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Li_A_Unified_Approach_to_Interpreting_Self-supervised_Pre-training_Methods_for_3D_CVPR_2025_paper.html) · 📚 被引 1
- **作者**: Qiang Li, Jian Ruan, Fanghao Wu, Yuchi Chen, Zhihua Wei, Wen Shen
- **🏷️ 机构**: Tongji University,Shanghai,China
- **会议**: CVPR 2025
- **摘要（中）**: ①针对3D点云自监督预训练方法缺乏统一解释框架的问题。②提出一种基于交互（interactions）的统一视角，用于解释多种自监督预训练方法。③相比零散的方法分析，提供了理论统一性，有助于理解不同方法的共性。④摘要未提供具体实验数据，主要贡献在理论层面。
- **摘要（英）**: This paper addresses the lack of a unified interpretation framework for self-supervised pre-training methods on 3D point clouds. It proposes a unified perspective based on interactions to explain various methods. Compared to fragmented analyses, it offers theoretical unification, aiding understanding of commonalities. No specific experimental data is provided in the abstract.
- **核心贡献**: 提出基于交互的统一解释框架，连接多种3D点云自监督方法。
- **创新点**: 从交互角度统一自监督预训练的理论基础。
- **结果**: 提供理论洞见，无具体实验数据。

### On-Device Self-Supervised Learning of Low-Latency Monocular Depth from Only Events. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2412.06359](https://arxiv.org/abs/2412.06359) · 📚 被引 1
- **作者**: Jesse J. Hagenaars, Yilun Wu, Federico Paredes-Vallés, Stein Stroobants, Guido C. H. E. de Croon
- **🏷️ 机构**: MAVLab, TU Delft, EUISPC, Sony Semiconductor Solutions Europe, Sony Europe B.V
- **会议**: CVPR 2025
- **摘要（中）**: ①针对事件相机在资源受限机器人（如小型无人机）上在线自监督单目深度估计的计算效率瓶颈。②提出改进对比最大化的时间和内存效率，实现设备端在线学习，并验证在线学习提升深度估计和避障性能。③相比仅预训练，在线学习在真实无人机上获得更准确深度和更优避障；相比现有自监督方法，达到最先进深度估计性能。④实验表明，所提管线高效且性能领先，但摘要未提供具体数值。
- **摘要（英）**: This paper addresses the computational bottleneck of online self-supervised monocular depth estimation from event cameras on resource-constrained robots. It improves the time and memory efficiency of contrast maximization, enabling on-device learning, and demonstrates that online learning yields more accurate depth and better obstacle avoidance than pre-training alone. The proposed pipeline achieves state-of-the-art depth estimation among self-supervised methods, though specific metrics are not detailed in the abstract.
- **核心贡献**: 首次实现事件相机单目深度估计的设备端在线自监督学习。
- **创新点**: 通过优化对比最大化管线的时间和内存效率，突破在线学习计算瓶颈。
- **结果**: 在线学习显著提升深度估计精度和避障成功率，并达到自监督方法最先进水平。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Event cameras provide low-latency perception for only milliwatts of power. This makes them highly suitable for resource-restricted, agile robots such as small flying drones. Self-supervised learning based on contrast maximization holds great potential for event-based robot vision, as it foregoes the need for high-frequency ground truth and allows for online learning in the robot's operational environment. However, online, on-board learning raises the major challenge of achieving sufficient computational efficiency for real-time learning, while maintaining competitive visual perception performance. In this work, we improve the time and memory efficiency of the contrast maximization pipeline, making on-device learning of low-latency monocular depth possible. We demonstrate that online learning on board a small drone yields more accurate depth estimates and more successful obstacle avoidance behavior compared to only pre-training. Benchmarking experiments show that the proposed pipeline is not only efficient, but also achieves state-of-the-art depth estimation performance among self-supervised approaches. Our work taps into the unused potential of online, on-device robot learning, promising smaller reality gaps and better performance.

</details>

### Improved Monocular Depth Prediction Using Distance Transform Over Pre-semantic Contours with Self-supervised Neural Networks. **⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2605.08320](https://arxiv.org/abs/2605.08320) · 📚 被引 2
- **作者**: Marwane Hariat, Antoine Manzanera, David Filliat
- **🏷️ 机构**: Institut Polytechnique de Paris,U2IS, ENSTA,Palaiseau,France
- **会议**: CVPR 2025
- **摘要（中）**: 针对自监督单目深度估计在低纹理区域深度预测模糊的问题，提出在预语义轮廓上应用距离变换以增强空间信息，联合估计轮廓、深度和自运动。理论证明距离变换是最优方差增强技术，在KITTI、Cityscapes、Waymo等数据集上超越现有自监督方法。
- **摘要（英）**: To address ambiguous depth in low-texture areas for self-supervised MDE, this work applies distance transform over pre-semantic contours to augment spatial information, jointly estimating contours, depth, and ego-motion. It theoretically proves optimality and outperforms self-supervised methods on KITTI, Cityscapes, Waymo, etc.
- **核心贡献**: 提出基于距离变换的预语义轮廓增强方法，提升自监督深度估计性能。
- **创新点**: 理论证明距离变换在低纹理区域方差增强中的最优性。
- **结果**: 在多个数据集上超越现有自监督深度估计方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular depth estimation (MDE) with self-supervised training approaches struggles in low-texture areas, where photometric losses may lead to ambiguous depth predictions. To address this, we propose a novel technique that enhances spatial information by applying a distance transform over pre-semantic contours, augmenting discriminative power in low texture regions. Our approach jointly estimates pre-semantic contours, depth and ego-motion. The pre-semantic contours are leveraged to produce new input images, with variance augmented by the distance transform in uniform areas. This approach results in more effective loss functions, enhancing the training process for depth and ego-motion. We demonstrate theoretically that the distance transform is the optimal variance-augmenting technique in this context. Through extensive experiments on KITTI, Cityscapes, Waymo, NYUv2 and ScanNet our model demonstrates robust performance, surpassing competing self-supervised methods in MDE.

</details>

### Stealthy Backdoor Attack in Self-Supervised Learning Vision Encoders for Large Vision Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_Stealthy_Backdoor_Attack_in_Self-Supervised_Learning_Vision_Encoders_for_Large_CVPR_2025_paper.html)
- **作者**: Zhaoyi Liu, Huan Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### Anyattack: Towards Large-scale Self-supervised Adversarial Attacks on Vision-language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_Anyattack_Towards_Large-scale_Self-supervised_Adversarial_Attacks_on_Vision-language_Models_CVPR_2025_paper.html)
- **作者**: Jiaming Zhang, Junhong Ye, Xingjun Ma, Yige Li, Yunfan Yang, Yunhao Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### Masked Scene Modeling: Narrowing the Gap Between Supervised and Self-Supervised Learning in 3D Scene Understanding.
- **链接**: [arXiv:2504.06719](https://arxiv.org/abs/2504.06719) · [代码](https://github.com/phermosilla/msm) · 📚 被引 0
- **作者**: Pedro Hermosilla, Christian Stippel, Leon Sick
- **🏷️ 机构**: TU Wien, Ulm University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Estimating motion in videos is an essential computer vision problem with many downstream applications, including controllable video generation and robotics. Current solutions are primarily trained using synthetic data or require tuning of situation-specific heuristics, which inherently limits these models' capabilities in real-world contexts. Despite recent developments in large-scale self-supervised learning from videos, leveraging such representations for motion estimation remains relatively underexplored. In this work, we develop Opt-CWM, a self-supervised technique for flow and occlusion estimation from a pre-trained next-frame prediction model. Opt-CWM works by learning to optimize counterfactual probes that extract motion information from a base video model, avoiding the need for fixed heuristics while training on unrestricted video inputs. We achieve state-of-the-art performance for motion estimation on real-world videos while requiring no labeled data.

</details>

### 1000 Layer Networks for Self-Supervised RL: Scaling Depth Can Enable New Goal-Reaching Capabilities.
- **链接**: [arXiv:2503.14858](https://arxiv.org/abs/2503.14858) · 📚 被引 0
- **作者**: Kevin Wang, Ishaan Javali, Michal Bortkiewicz, Tomasz Trzcinski, Benjamin Eysenbach
- **🏷️ 机构**: Princeton University, Warsaw University of Technology, Warsaw University of Technology, Tooploox, IDEAS, Jagiellonian University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Scaling up self-supervised learning has driven breakthroughs in language and vision, yet comparable progress has remained elusive in reinforcement learning (RL). In this paper, we study building blocks for self-supervised RL that unlock substantial improvements in scalability, with network depth serving as a critical factor. Whereas most RL papers in recent years have relied on shallow architectures (around 2 - 5 layers), we demonstrate that increasing the depth up to 1024 layers can significantly boost performance. Our experiments are conducted in an unsupervised goal-conditioned setting, where no demonstrations or rewards are provided, so an agent must explore (from scratch) and learn how to maximize the likelihood of reaching commanded goals. Evaluated on simulated locomotion and manipulation tasks, our approach increases performance on the self-supervised contrastive RL algorithm by $2\times$ - $50\times$, outperforming other goal-conditioned baselines. Increasing the model depth not only increases success rates but also qualitatively changes the behaviors learned. The project webpage and code can be found here: https://wang-kevin3290.github.io/scaling-crl/.

</details>

### Not All Data are Good Labels: On the Self-supervised Labeling for Time Series Forecasting.
- **链接**: [arXiv:2502.14704](https://arxiv.org/abs/2502.14704) · [代码](https://github.com/SuDIS-ZJU/SCAM) · 📚 被引 0
- **作者**: Yuxuan Yang, Dalin Zhang, Yuxuan Liang, Hua Lu, Gang Chen, Huan Li
- **🏷️ 机构**: Zhejiang University, Hangzhou Dianzi University, The Hong Kong University of Science and Technology (Guangzhou)
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Time Series Forecasting (TSF) is a crucial task in various domains, yet existing TSF models rely heavily on high-quality data and insufficiently exploit all available data. This paper explores a novel self-supervised approach to re-label time series datasets by inherently constructing candidate datasets. During the optimization of a simple reconstruction network, intermediates are used as pseudo labels in a self-supervised paradigm, improving generalization for any predictor. We introduce the Self-Correction with Adaptive Mask (SCAM), which discards overfitted components and selectively replaces them with pseudo labels generated from reconstructions. Additionally, we incorporate Spectral Norm Regularization (SNR) to further suppress overfitting from a loss landscape perspective. Our experiments on eleven real-world datasets demonstrate that SCAM consistently improves the performance of various backbone models. This work offers a new perspective on constructing datasets and enhancing the generalization of TSF models through self-supervised learning. The code is available at https://github.com/SuDIS-ZJU/SCAM.

</details>

### Positive2Negative: Breaking the Information-Lossy Barrier in Self-Supervised Single Image Denoising.
- **链接**: [arXiv:2412.16460](https://arxiv.org/abs/2412.16460) · [代码](https://github.com/Li-Tong-621/P2N) · 📚 被引 5
- **作者**: Tong Li, Lizhi Wang, Zhiyuan Xu, Lin Zhu, Wanxuan Lu, Hua Huang
- **🏷️ 机构**: Beijing Institute of Technology,School of Computer Science and Technology, Beijing Normal University,School of Artificial Intelligence, Chinese Academy of Sciences,Aerospace Information Research Institute
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Image denoising enhances image quality, serving as a foundational technique across various computational photography applications. The obstacle to clean image acquisition in real scenarios necessitates the development of self-supervised image denoising methods only depending on noisy images, especially a single noisy image. Existing self-supervised image denoising paradigms (Noise2Noise and Noise2Void) rely heavily on information-lossy operations, such as downsampling and masking, culminating in low quality denoising performance. In this paper, we propose a novel self-supervised single image denoising paradigm, Positive2Negative, to break the information-lossy barrier. Our paradigm involves two key steps: Renoised Data Construction (RDC) and Denoised Consistency Supervision (DCS). RDC renoises the predicted denoised image by the predicted noise to construct multiple noisy images, preserving all the information of the original image. DCS ensures consistency across the multiple denoised images, supervising the network to learn robust denoising. Our Positive2Negative paradigm achieves state-of-the-art performance in self-supervised single image denoising with significant speed improvements. The code is released to the public at https://github.com/Li-Tong-621/P2N.

</details>

### Self-Supervised Cross-View Correspondence with Predictive Cycle Consistency.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Baade_Self-Supervised_Cross-View_Correspondence_with_Predictive_Cycle_Consistency_CVPR_2025_paper.html) · 📚 被引 1
- **作者**: Alan Baade, Changan Chen
- **🏷️ 机构**: The University of Texas at Austin, Stanford University
- **会议**: CVPR 2025

### Probing the Mid-level Vision Capabilities of Self-Supervised Learning.
- **链接**: [arXiv:2411.17474](https://arxiv.org/abs/2411.17474) · 📚 被引 3
- **作者**: Xuweiyi Chen, Markus Marks, Zezhou Cheng
- **🏷️ 机构**: University of Virginia, California Institute of Technology
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Mid-level vision capabilities - such as generic object localization and 3D geometric understanding - are not only fundamental to human vision but are also crucial for many real-world applications of computer vision. These abilities emerge with minimal supervision during the early stages of human visual development. Despite their significance, current self-supervised learning (SSL) approaches are primarily designed and evaluated for high-level recognition tasks, leaving their mid-level vision capabilities largely unexamined. In this study, we introduce a suite of benchmark protocols to systematically assess mid-level vision capabilities and present a comprehensive, controlled evaluation of 22 prominent SSL models across 8 mid-level vision tasks. Our experiments reveal a weak correlation between mid-level and high-level task performance. We also identify several SSL methods with highly imbalanced performance across mid-level and high-level capabilities, as well as some that excel in both. Additionally, we investigate key factors contributing to mid-level vision performance, such as pretraining objectives and network architectures. Our study provides a holistic and timely view of what SSL models have learned, complementing existing research that primarily focuses on high-level vision tasks. We hope our findings guide future SSL research to benchmark models not only on high-level vision tasks but on mid-level as well.

</details>

### ArticulatedGS: Self-supervised Digital Twin Modeling of Articulated Objects using 3D Gaussian Splatting.
- **链接**: [arXiv:2503.08135](https://arxiv.org/abs/2503.08135) · 📚 被引 13
- **作者**: Junfu Guo, Yu Xin, Gaoyi Liu, Kai Xu, Ligang Liu, Ruizhen Hu
- **🏷️ 机构**: University of Science and Technology of China, National University of Defense Technology, Shenzhen University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We tackle the challenge of concurrent reconstruction at the part level with the RGB appearance and estimation of motion parameters for building digital twins of articulated objects using the 3D Gaussian Splatting (3D-GS) method. With two distinct sets of multi-view imagery, each depicting an object in separate static articulation configurations, we reconstruct the articulated object in 3D Gaussian representations with both appearance and geometry information at the same time. Our approach decoupled multiple highly interdependent parameters through a multi-step optimization process, thereby achieving a stable optimization procedure and high-quality outcomes. We introduce ArticulatedGS, a self-supervised, comprehensive framework that autonomously learns to model shapes and appearances at the part level and synchronizes the optimization of motion parameters, all without reliance on 3D supervision, motion cues, or semantic labels. Our experimental results demonstrate that, among comparable methodologies, our approach has achieved optimal outcomes in terms of part segmentation accuracy, motion estimation accuracy, and visual quality.

</details>

### SF2T: Self-supervised Fragment Finetuning of Video-LLMs for Fine-Grained Understanding.
- **链接**: [arXiv:2504.07745](https://arxiv.org/abs/2504.07745) · 📚 被引 3
- **作者**: Yangliu Hu, Zikai Song, Na Feng, Yawei Luo, Junqing Yu, Yi-Ping Phoebe Chen et al.
- **🏷️ 机构**: Huazhong University of Science and Technology, Zhejiang University, La Trobe University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Inferring synaptic connectivity from neural population activity is a fundamental challenge in computational neuroscience, complicated by partial observability and mismatches between inference models and true circuit dynamics. In this study, we propose a graph-based neural inference model that simultaneously predicts neural activity and infers latent connectivity by modeling neurons as interacting nodes in a graph. The architecture features two distinct modules: one for learning structural connectivity and another for predicting future spiking activity via a graph neural network (GNN). Our model accommodates unobserved neurons through auxiliary nodes, allowing for inference in partially observed circuits. We evaluate this approach using synthetic data generated from ring attractor network models and real spike recordings from head direction cells in mice. Across a wide range of conditions, including varying recurrent connectivity, external inputs, and incomplete observations, our model reliably resolves spurious correlations and recovers accurate weight profiles. When applied to real data, the inferred connectivity aligns with theoretical predictions of continuous attractor models. These results highlight the potential of GNN-based models to infer latent neural circuitry through self-supervised structure learning, while leveraging the spike prediction task to flexibly link connectivity and dynamics across both simulated and biological neural systems.

</details>

### Contrastive Self-Supervised Learning As Neural Manifold Packing.
- **链接**: [arXiv:2506.13717](https://arxiv.org/abs/2506.13717) · 📚 被引 0
- **作者**: Guanming Zhang, David J. Heeger, Stefano Martiniani
- **🏷️ 机构**: New York University, NYU
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Contrastive self-supervised learning based on point-wise comparisons has been widely studied for vision tasks. In the visual cortex of the brain, neuronal responses to distinct stimulus classes are organized into geometric structures known as neural manifolds. Accurate classification of stimuli can be achieved by effectively separating these manifolds, akin to solving a packing problem. We introduce Contrastive Learning As Manifold Packing (CLAMP), a self-supervised framework that recasts representation learning as a manifold packing problem. CLAMP introduces a loss function inspired by the potential energy of short-range repulsive particle systems, such as those encountered in the physics of simple liquids and jammed packings. In this framework, each class consists of sub-manifolds embedding multiple augmented views of a single image. The sizes and positions of the sub-manifolds are dynamically optimized by following the gradient of a packing loss. This approach yields interpretable dynamics in the embedding space that parallel jamming physics, and introduces geometrically meaningful hyperparameters within the loss function. Under the standard linear evaluation protocol, which freezes the backbone and trains only a linear classifier, CLAMP achieves competitive performance with state-of-the-art self-supervised models. Furthermore, our analysis reveals that neural manifolds corresponding to different categories emerge naturally and are effectively separated in the learned representation space, highlighting the potential of CLAMP to bridge insights from physics, neural science, and machine learning.

</details>

### Concerto: Joint 2D-3D Self-Supervised Learning Emerges Spatial Representations.
- **链接**: [arXiv:2510.23607](https://arxiv.org/abs/2510.23607) · 📚 被引 0
- **作者**: Yujia Zhang, Xiaoyang Wu, Yixing Lao, Chengyao Wang, Zhuotao Tian, Naiyan Wang et al.
- **🏷️ 机构**: The University of Hong Kong, the University of Hong Kong, The Chinese University of Hong Kong
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Humans learn abstract concepts through multisensory synergy, and once formed, such representations can often be recalled from a single modality. Inspired by this principle, we introduce Concerto, a minimalist simulation of human concept learning for spatial cognition, combining 3D intra-modal self-distillation with 2D-3D cross-modal joint embedding. Despite its simplicity, Concerto learns more coherent and informative spatial features, as demonstrated by zero-shot visualizations. It outperforms both standalone SOTA 2D and 3D self-supervised models by 14.2% and 4.8%, respectively, as well as their feature concatenation, in linear probing for 3D scene perception. With full fine-tuning, Concerto sets new SOTA results across multiple scene understanding benchmarks (e.g., 80.7% mIoU on ScanNet). We further present a variant of Concerto tailored for video-lifted point cloud spatial understanding, and a translator that linearly projects Concerto representations into CLIP's language space, enabling open-world perception. These results highlight that Concerto emerges spatial representations with superior fine-grained geometric and semantic consistency.

</details>

### UniMRSeg: Unified Modality-Relax Segmentation via Hierarchical Self-Supervised Compensation.
- **链接**: [arXiv:2509.16170](https://arxiv.org/abs/2509.16170) · [代码](https://github.com/Xiaoqi-Zhao-DLUT/UniMRSeg) · 📚 被引 1
- **作者**: Xiaoqi Zhao, Youwei Pang, Chenyang Yu, Lihe Zhang, Huchuan Lu, Shijian Lu et al.
- **🏷️ 机构**: Yale University, Dalian University of Technology, Nanyang Technological University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-modal image segmentation faces real-world deployment challenges from incomplete/corrupted modalities degrading performance. While existing methods address training-inference modality gaps via specialized per-combination models, they introduce high deployment costs by requiring exhaustive model subsets and model-modality matching. In this work, we propose a unified modality-relax segmentation network (UniMRSeg) through hierarchical self-supervised compensation (HSSC). Our approach hierarchically bridges representation gaps between complete and incomplete modalities across input, feature and output levels. % First, we adopt modality reconstruction with the hybrid shuffled-masking augmentation, encouraging the model to learn the intrinsic modality characteristics and generate meaningful representations for missing modalities through cross-modal fusion. % Next, modality-invariant contrastive learning implicitly compensates the feature space distance among incomplete-complete modality pairs. Furthermore, the proposed lightweight reverse attention adapter explicitly compensates for the weak perceptual semantics in the frozen encoder. Last, UniMRSeg is fine-tuned under the hybrid consistency constraint to ensure stable prediction under all modality combinations without large performance fluctuations. Without bells and whistles, UniMRSeg significantly outperforms the state-of-the-art methods under diverse missing modality scenarios on MRI-based brain tumor segmentation, RGB-D semantic segmentation, RGB-D/T salient object segmentation. The code will be released at https://github.com/Xiaoqi-Zhao-DLUT/UniMRSeg.

</details>

### CellCLIP - Learning Perturbation Effects in Cell Painting via Text-Guided Contrastive Learning.
- **链接**: [arXiv:2506.06290](https://arxiv.org/abs/2506.06290) · 📚 被引 0
- **作者**: Mingyu Lu, Ethan Weinberger, Chanwoo Kim, Su-In Lee
- **🏷️ 机构**: University of Washington
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> High-content screening (HCS) assays based on high-throughput microscopy techniques such as Cell Painting have enabled the interrogation of cells' morphological responses to perturbations at an unprecedented scale. The collection of such data promises to facilitate a better understanding of the relationships between different perturbations and their effects on cellular state. Towards achieving this goal, recent advances in cross-modal contrastive learning could, in theory, be leveraged to learn a unified latent space that aligns perturbations with their corresponding morphological effects. However, the application of such methods to HCS data is not straightforward due to substantial differences in the semantics of Cell Painting images compared to natural images, and the difficulty of representing different classes of perturbations (e.g., small molecule vs CRISPR gene knockout) in a single latent space. In response to these challenges, here we introduce CellCLIP, a cross-modal contrastive learning framework for HCS data. CellCLIP leverages pre-trained image encoders coupled with a novel channel encoding scheme to better capture relationships between different microscopy channels in image embeddings, along with natural language encoders for representing perturbations. Our framework outperforms current open-source models, demonstrating the best performance in both cross-modal retrieval and biologically meaningful downstream tasks while also achieving significant reductions in computation time.

</details>

### Understanding Contrastive Learning via Gaussian Mixture Models.
- **链接**: [arXiv:2411.03517](https://arxiv.org/abs/2411.03517) · 📚 被引 0
- **作者**: Parikshit Bansal, Ali Kavis, Sujay Sanghavi
- **🏷️ 机构**: The University of Texas at Austin, UT Austin, UT-Austin
- **会议**: NeurIPS 2025

### Joint Self-Supervised Video Alignment and Action Segmentation.
- **链接**: [arXiv:2503.16832](https://arxiv.org/abs/2503.16832) · 📚 被引 3
- **作者**: Ali Shah Ali, Syed Ahmed Mahmood, Mubin Saeed, Andrey Konin, M. Zeeshan Zia, Quoc-Huy Tran
- **🏷️ 机构**: Retrocausal, Inc.,Redmond,WA
- **会议**: ICCV 2025

### AIM: Amending Inherent Interpretability via Self-Supervised Masking.
- **链接**: [arXiv:2508.11502](https://arxiv.org/abs/2508.11502) · 📚 被引 0
- **作者**: Eyad Alshami, Shashank Agnihotri, Bernt Schiele, Margret Keuper
- **🏷️ 机构**: Max-Planck-Institute for Informatics, Saarland Informatics Campus,Germany, Data and Web Science Group, University of Mannheim,Germany
- **会议**: ICCV 2025

### Progressor: A Perceptually Guided Reward Estimator with Self-Supervised Online Refinement.
- **链接**: [arXiv:2411.17764](https://arxiv.org/abs/2411.17764) · 📚 被引 0
- **作者**: Tewodros W. Ayalew, Xiao Zhang, Kevin Yuanbo Wu, Tianchong Jiang, Michael Maire, Matthew R. Walter
- **🏷️ 机构**: University of Chicago,USA, Toyota Technological Institute at Chicago,USA
- **会议**: ICCV 2025

> We introduce a novel approach for simultaneous self-supervised video alignment and action segmentation based on a unified optimal transport framework. In particular, we first tackle self-supervised video alignment by developing a fused Gromov-Wasserstein optimal transport formulation with a structural prior, which trains efficiently on GPUs and needs only a few iterations for solving the optimal transport problem. Our single-task method achieves the state-of-the-art performance on multiple video alignment benchmarks and outperforms VAVA, which relies on a traditional Kantorovich optimal transport formulation with an optimality prior. Furthermore, we extend our approach by proposing a unified optimal transport framework for joint self-supervised video alignment and action segmentation, which requires training and storing a single model and saves both time and memory consumption as compared to two different single-task models. Extensive evaluations on several video alignment and action segmentation datasets demonstrate that our multi-task method achieves comparable video alignment yet superior action segmentation results over previous methods in video alignment and action segmentation respectively. Finally, to the best of our knowledge, this is the first work to unify video alignment and action segmentation into a single model. Our code is available on our research website: https://retrocausal.ai/research/.

### Backdooring Self-Supervised Contrastive Learning by Noisy Alignment.
- **链接**: [arXiv:2508.14015](https://arxiv.org/abs/2508.14015) · 📚 被引 1
- **作者**: Tuo Chen, Jie Gui, Minjing Dong, Ju Jia, Lanting Fang, Jian Liu
- **🏷️ 机构**: Southeast University, City University of Hong Kong, Beijing Institute of Technology
- **会议**: ICCV 2025

### AIM: Amending Inherent Interpretability via Self-Supervised Masking.
- **链接**: [arXiv:2508.11502](https://arxiv.org/abs/2508.11502) · 📚 被引 0
- **作者**: Eyad Alshami, Shashank Agnihotri, Bernt Schiele, Margret Keuper
- **🏷️ 机构**: Max-Planck-Institute for Informatics, Saarland Informatics Campus,Germany, Data and Web Science Group, University of Mannheim,Germany
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> It has been observed that deep neural networks (DNNs) often use both genuine as well as spurious features. In this work, we propose "Amending Inherent Interpretability via Self-Supervised Masking" (AIM), a simple yet interestingly effective method that promotes the network's utilization of genuine features over spurious alternatives without requiring additional annotations. In particular, AIM uses features at multiple encoding stages to guide a self-supervised, sample-specific feature-masking process. As a result, AIM enables the training of well-performing and inherently interpretable models that faithfully summarize the decision process. We validate AIM across a diverse range of challenging datasets that test both out-of-distribution generalization and fine-grained visual understanding. These include general-purpose classification benchmarks such as ImageNet100, HardImageNet, and ImageWoof, as well as fine-grained classification datasets such as Waterbirds, TravelingBirds, and CUB-200. AIM demonstrates significant dual benefits: interpretability improvements, as measured by the Energy Pointing Game (EPG) score, and accuracy gains over strong baselines. These consistent gains across domains and architectures provide compelling evidence that AIM promotes the use of genuine and meaningful features that directly contribute to improved generalization and human-aligned interpretability.

</details>

### Progressor: A Perceptually Guided Reward Estimator with Self-Supervised Online Refinement.
- **链接**: [arXiv:2411.17764](https://arxiv.org/abs/2411.17764) · 📚 被引 0
- **作者**: Tewodros W. Ayalew, Xiao Zhang, Kevin Yuanbo Wu, Tianchong Jiang, Michael Maire, Matthew R. Walter
- **🏷️ 机构**: University of Chicago,USA, Toyota Technological Institute at Chicago,USA
- **会议**: ICCV 2025

### Adversarial Robustness of Discriminative Self-Supervised Learning in Vision.
- **链接**: [arXiv:2503.06361](https://arxiv.org/abs/2503.06361) · 📚 被引 0
- **作者**: Ömer Veysel Çagatan, Ömer Faruk Tal, M. Emre Gürsoy
- **🏷️ 机构**: Ko&#x00E7; University,Department of Computer Engineering
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning (SSL) has advanced significantly in visual representation learning, yet comprehensive evaluations of its adversarial robustness remain limited. In this study, we evaluate the adversarial robustness of seven discriminative self-supervised models and one supervised model across diverse tasks, including ImageNet classification, transfer learning, segmentation, and detection. Our findings suggest that discriminative SSL models generally exhibit better robustness to adversarial attacks compared to their supervised counterpart on ImageNet, with this advantage extending to transfer learning when using linear evaluation. However, when fine-tuning is applied, the robustness gap between SSL and supervised models narrows considerably. Similarly, this robustness advantage diminishes in segmentation and detection tasks. We also investigate how various factors might influence adversarial robustness, including architectural choices, training duration, data augmentations, and batch sizes. Our analysis contributes to the ongoing exploration of adversarial robustness in visual self-supervised representation systems.

</details>

### Backdooring Self-Supervised Contrastive Learning by Noisy Alignment.
- **链接**: [arXiv:2508.14015](https://arxiv.org/abs/2508.14015) · [代码](https://github.com/jsrdcht/Noisy-Alignment) · 📚 被引 1
- **作者**: Tuo Chen, Jie Gui, Minjing Dong, Ju Jia, Lanting Fang, Jian Liu
- **🏷️ 机构**: Southeast University, City University of Hong Kong, Beijing Institute of Technology
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised contrastive learning (CL) effectively learns transferable representations from unlabeled data containing images or image-text pairs but suffers vulnerability to data poisoning backdoor attacks (DPCLs). An adversary can inject poisoned images into pretraining datasets, causing compromised CL encoders to exhibit targeted misbehavior in downstream tasks. Existing DPCLs, however, achieve limited efficacy due to their dependence on fragile implicit co-occurrence between backdoor and target object and inadequate suppression of discriminative features in backdoored images. We propose Noisy Alignment (NA), a DPCL method that explicitly suppresses noise components in poisoned images. Inspired by powerful training-controllable CL attacks, we identify and extract the critical objective of noisy alignment, adapting it effectively into data-poisoning scenarios. Our method implements noisy alignment by strategically manipulating contrastive learning's random cropping mechanism, formulating this process as an image layout optimization problem with theoretically derived optimal parameters. The resulting method is simple yet effective, achieving state-of-the-art performance compared to existing DPCLs, while maintaining clean-data accuracy. Furthermore, Noisy Alignment demonstrates robustness against common backdoor defenses. Codes can be found at https://github.com/jsrdcht/Noisy-Alignment.

</details>

### DASH: 4D Hash Encoding with Self-Supervised Decomposition for Real-Time Dynamic Scene Rendering.
- **链接**: [arXiv:2507.19141](https://arxiv.org/abs/2507.19141) · [代码](https://github.com/chenj02/DASH) · 📚 被引 0
- **作者**: Jie Chen, Zhangchi Hu, Peixi Wu, Huyue Zhu, Hebei Li, Xiaoyan Sun
- **🏷️ 机构**: University of Science and Technology of China
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Dynamic scene reconstruction is a long-term challenge in 3D vision. Existing plane-based methods in dynamic Gaussian splatting suffer from an unsuitable low-rank assumption, causing feature overlap and poor rendering quality. Although 4D hash encoding provides an explicit representation without low-rank constraints, directly applying it to the entire dynamic scene leads to substantial hash collisions and redundancy. To address these challenges, we present DASH, a real-time dynamic scene rendering framework that employs 4D hash encoding coupled with self-supervised decomposition. Our approach begins with a self-supervised decomposition mechanism that separates dynamic and static components without manual annotations or precomputed masks. Next, we introduce a multiresolution 4D hash encoder for dynamic elements, providing an explicit representation that avoids the low-rank assumption. Finally, we present a spatio-temporal smoothness regularization strategy to mitigate unstable deformation artifacts. Experiments on real-world datasets demonstrate that DASH achieves state-of-the-art dynamic rendering performance, exhibiting enhanced visual quality at real-time speeds of 264 FPS on a single 4090 GPU. Code: https://github.com/chenj02/DASH.

</details>

### USP: Unified Self-Supervised Pretraining for Image Generation and Understanding.
- **链接**: [arXiv:2503.06132](https://arxiv.org/abs/2503.06132) · [代码](https://github.com/AMAP-ML/USP) · 📚 被引 3
- **作者**: Xiangxiang Chu, Renda Li, Yong Wang
- **🏷️ 机构**: AMAP, Alibaba Group
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent studies have highlighted the interplay between diffusion models and representation learning. Intermediate representations from diffusion models can be leveraged for downstream visual tasks, while self-supervised vision models can enhance the convergence and generation quality of diffusion models. However, transferring pretrained weights from vision models to diffusion models is challenging due to input mismatches and the use of latent spaces. To address these challenges, we propose Unified Self-supervised Pretraining (USP), a framework that initializes diffusion models via masked latent modeling in a Variational Autoencoder (VAE) latent space. USP achieves comparable performance in understanding tasks while significantly improving the convergence speed and generation quality of diffusion models. Our code will be publicly available at https://github.com/AMAP-ML/USP.

</details>

### Embodied Image Captioning: Self-Supervised Learning Agents for Spatially Coherent Image Descriptions.
- **链接**: [arXiv:2504.08531](https://arxiv.org/abs/2504.08531) · 📚 被引 0
- **作者**: Tommaso Galliena, Tommaso Apicella, Stefano Rosa, Pietro Morerio, Alessio Del Bue, Lorenzo Natale
- **🏷️ 机构**: Istituto Italiano di Tecnologia,Genoa,Italy
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a self-supervised method to improve an agent's abilities in describing arbitrary objects while actively exploring a generic environment. This is a challenging problem, as current models struggle to obtain coherent image captions due to different camera viewpoints and clutter. We propose a three-phase framework to fine-tune existing captioning models that enhances caption accuracy and consistency across views via a consensus mechanism. First, an agent explores the environment, collecting noisy image-caption pairs. Then, a consistent pseudo-caption for each object instance is distilled via consensus using a large language model. Finally, these pseudo-captions are used to fine-tune an off-the-shelf captioning model, with the addition of contrastive learning. We analyse the performance of the combination of captioning models, exploration policies, pseudo-labeling methods, and fine-tuning strategies, on our manually labeled test set. Results show that a policy can be trained to mine samples with higher disagreement compared to classical baselines. Our pseudo-captioning method, in combination with all policies, has a higher semantic similarity compared to other existing methods, and fine-tuning improves caption accuracy and consistency by a significant margin. Code and test set annotations available at https://hsp-iit.github.io/embodied-captioning/

</details>

### Self-Supervised Learning of Hybrid Part-Aware 3D Representations of 2D Gaussians and Superquadrics.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00900) · 📚 被引 4
- **作者**: Zhirui Gao, Renjiao Yi, Yuhang Huang, Wei Chen, Chenyang Zhu, Kai Xu
- **🏷️ 机构**: National University of Defense Technology
- **会议**: ICCV 2025

### No Pose at All: Self-Supervised Pose-Free 3D Gaussian Splatting from Sparse Views.
- **链接**: [arXiv:2508.01171](https://arxiv.org/abs/2508.01171) · 📚 被引 3
- **作者**: Ranran Huang, Krystian Mikolajczyk
- **🏷️ 机构**: Imperial College London
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce SPFSplat, an efficient framework for 3D Gaussian splatting from sparse multi-view images, requiring no ground-truth poses during training or inference. It employs a shared feature extraction backbone, enabling simultaneous prediction of 3D Gaussian primitives and camera poses in a canonical space from unposed inputs within a single feed-forward step. Alongside the rendering loss based on estimated novel-view poses, a reprojection loss is integrated to enforce the learning of pixel-aligned Gaussian primitives for enhanced geometric constraints. This pose-free training paradigm and efficient one-step feed-forward design make SPFSplat well-suited for practical applications. Remarkably, despite the absence of pose supervision, SPFSplat achieves state-of-the-art performance in novel view synthesis even under significant viewpoint changes and limited image overlap. It also surpasses recent methods trained with geometry priors in relative pose estimation. Code and trained models are available on our project page: https://ranrhuang.github.io/spfsplat/.

</details>

### Rayzer: a Self-Supervised Large View Synthesis Model.
- **链接**: [arXiv:2505.00702](https://arxiv.org/abs/2505.00702) · 📚 被引 4
- **作者**: Hanwen Jiang, Hao Tan, Peng Wang, Hai Jin, Yue Zhao, Sai Bi et al.
- **🏷️ 机构**: The University of Texas at Austin, Adobe Research, Cornell University
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present RayZer, a self-supervised multi-view 3D Vision model trained without any 3D supervision, i.e., camera poses and scene geometry, while exhibiting emerging 3D awareness. Concretely, RayZer takes unposed and uncalibrated images as input, recovers camera parameters, reconstructs a scene representation, and synthesizes novel views. During training, RayZer relies solely on its self-predicted camera poses to render target views, eliminating the need for any ground-truth camera annotations and allowing RayZer to be trained with 2D image supervision. The emerging 3D awareness of RayZer is attributed to two key factors. First, we design a self-supervised framework, which achieves 3D-aware auto-encoding of input images by disentangling camera and scene representations. Second, we design a transformer-based model in which the only 3D prior is the ray structure, connecting camera, pixel, and scene simultaneously. RayZer demonstrates comparable or even superior novel view synthesis performance than ``oracle'' methods that rely on pose annotations in both training and testing. Project: https://hwjiang1510.github.io/RayZer/

</details>

### Blind2Sound: Self-Supervised Image Denoising Without Residual Noise.
- **链接**: [arXiv:2303.05183](https://arxiv.org/abs/2303.05183) · 📚 被引 0
- **作者**: Jiazheng Liu, Zejin Wang, Bohao Chen, Hua Han
- **🏷️ 机构**: Institute of Automation, Chinese Academy of Sciences,State Key Laboratory of Brain Cognition and Brain-inspired Intelligence Technology,Beijing,China, School of Advanced Interdisciplinary Sciences, University of Chinese Academy of Sciences,Beijing,China
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised blind denoising for Poisson-Gaussian noise remains a challenging task. Pseudo-supervised pairs constructed from single noisy images re-corrupt the signal and degrade the performance. The visible blindspots solve the information loss in masked inputs. However, without explicitly noise sensing, mean square error as an objective function cannot adjust denoising intensities for dynamic noise levels, leading to noticeable residual noise. In this paper, we propose Blind2Sound, a simple yet effective approach to overcome residual noise in denoised images. The proposed adaptive re-visible loss senses noise levels and performs personalized denoising without noise residues while retaining the signal lossless. The theoretical analysis of intermediate medium gradients guarantees stable training, while the Cramer Gaussian loss acts as a regularization to facilitate the accurate perception of noise levels and improve the performance of the denoiser. Experiments on synthetic and real-world datasets show the superior performance of our method, especially for single-channel images.

</details>

### TESPEC: Temporally-Enhanced Self-Supervised Pretraining for Event Cameras.
- **链接**: [arXiv:2508.00913](https://arxiv.org/abs/2508.00913) · 📚 被引 1
- **作者**: Mohammad Mohammadi, Ziyi Wu, Igor Gilitschenski
- **🏷️ 机构**: University of Toronto
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Long-term temporal information is crucial for event-based perception tasks, as raw events only encode pixel brightness changes. Recent works show that when trained from scratch, recurrent models achieve better results than feedforward models in these tasks. However, when leveraging self-supervised pre-trained weights, feedforward models can outperform their recurrent counterparts. Current self-supervised learning (SSL) methods for event-based pre-training largely mimic RGB image-based approaches. They pre-train feedforward models on raw events within a short time interval, ignoring the temporal information of events. In this work, we introduce TESPEC, a self-supervised pre-training framework tailored for learning spatio-temporal information. TESPEC is well-suited for recurrent models, as it is the first framework to leverage long event sequences during pre-training. TESPEC employs the masked image modeling paradigm with a new reconstruction target. We design a novel method to accumulate events into pseudo grayscale videos containing high-level semantic information about the underlying scene, which is robust to sensor noise and reduces motion blur. Reconstructing this target thus requires the model to reason about long-term history of events. Extensive experiments demonstrate our state-of-the-art results in downstream tasks, including object detection, semantic segmentation, and monocular depth estimation. Project webpage: https://mhdmohammadi.github.io/TESPEC_webpage.

</details>

### Self-Supervised Sparse Sensor Fusion for Long Range Perception.
- **链接**: [arXiv:2508.13995](https://arxiv.org/abs/2508.13995) · 📚 被引 2
- **作者**: Edoardo Palladin, Samuel Brucker, Filippo Ghilotti, Praveen Narayanan, Mario Bijelic, Felix Heide
- **🏷️ 机构**: Torc Robotics
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Outside of urban hubs, autonomous cars and trucks have to master driving on intercity highways. Safe, long-distance highway travel at speeds exceeding 100 km/h demands perception distances of at least 250 m, which is about five times the 50-100m typically addressed in city driving, to allow sufficient planning and braking margins. Increasing the perception ranges also allows to extend autonomy from light two-ton passenger vehicles to large-scale forty-ton trucks, which need a longer planning horizon due to their high inertia. However, most existing perception approaches focus on shorter ranges and rely on Bird's Eye View (BEV) representations, which incur quadratic increases in memory and compute costs as distance grows. To overcome this limitation, we built on top of a sparse representation and introduced an efficient 3D encoding of multi-modal and temporal features, along with a novel self-supervised pre-training scheme that enables large-scale learning from unlabeled camera-LiDAR data. Our approach extends perception distances to 250 meters and achieves an 26.6% improvement in mAP in object detection and a decrease of 30.5% in Chamfer Distance in LiDAR forecasting compared to existing methods, reaching distances up to 250 meters. Project Page: https://light.princeton.edu/lrs4fusion/

</details>

### Mosic: Optimal-Transport Motion Trajectory for Dense Self-Supervised Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00617) · 📚 被引 0
- **作者**: Mohammadreza Salehi, Shashanka Venkataramanan, Ioana Simion, Efstratios Gavves, Cees G. M. Snoek, Yuki M. Asano
- **🏷️ 机构**: VIS Lab, UvA, Valeo.ai, Fundamental AI Lab, UTN
- **会议**: ICCV 2025

### SHeaP: Self-Supervised Head Geometry Predictor Learned via 2D Gaussians.
- **链接**: [arXiv:2504.12292](https://arxiv.org/abs/2504.12292) · 📚 被引 3
- **作者**: Liam Schoneveld, Zhe Chen, Davide Davoli, Jiapeng Tang, Saimon Terazawa, Ko Nishino et al.
- **🏷️ 机构**: Woven by Toyota, Toyota Motor Europe NV/SA associated partner by contracted service, Technical University of Munich
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Accurate, real-time 3D reconstruction of human heads from monocular images and videos underlies numerous visual applications. As 3D ground truth data is hard to come by at scale, previous methods have sought to learn from abundant 2D videos in a self-supervised manner. Typically, this involves the use of differentiable mesh rendering, which is effective but faces limitations. To improve on this, we propose SHeaP (Self-supervised Head Geometry Predictor Learned via 2D Gaussians). Given a source image, we predict a 3DMM mesh and a set of Gaussians that are rigged to this mesh. We then reanimate this rigged head avatar to match a target frame, and backpropagate photometric losses to both the 3DMM and Gaussian prediction networks. We find that using Gaussians for rendering substantially improves the effectiveness of this self-supervised approach. Training solely on 2D data, our method surpasses existing self-supervised approaches in geometric evaluations on the NoW benchmark for neutral faces and a new benchmark for non-neutral expressions. Our method also produces highly expressive meshes, outperforming state-of-the-art in emotion classification.

</details>

### Prototype-Based Contrastive Learning with Stage-Wise Progressive Augmentation for Self-Supervised Fine-Grained Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00393) · 📚 被引 2
- **作者**: Baofeng Tan, Xiu-Shen Wei, Lin Zhao
- **🏷️ 机构**: School of Computer Science and Engineering, Nanjing University of Science and Technology, School of Computer Science and Engineering, Southeast University,Key Laboratory of New Generation Artificial Intelligence Technology and Its Interdisciplinary Applications
- **会议**: ICCV 2025

### S3E: Self-Supervised State Estimation for Radar-Inertial System.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02477)
- **作者**: Shengpeng Wang, Yulong Xie, Qing Liao, Wei Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### TAGA: Self-supervised Learning for Template-free Animatable Gaussian Articulated Model.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhai_TAGA_Self-supervised_Learning_for_Template-free_Animatable_Gaussian_Articulated_Model_CVPR_2025_paper.html) · 📚 被引 4
- **作者**: Zhichao Zhai, Guikun Chen, Wenguan Wang, Dong Zheng, Jun Xiao
- **🏷️ 机构**: Zhejiang University
- **会议**: CVPR 2025

### Invisible Backdoor Attack against Self-supervised Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_Invisible_Backdoor_Attack_against_Self-supervised_Learning_CVPR_2025_paper.html) · 📚 被引 5
- **作者**: Hanrong Zhang, Zhenting Wang, Boheng Li, Fulin Lin, Tingxu Han, Mingyu Jin et al.
- **🏷️ 机构**: Zhejiang University, Rutgers University, Nanyang Technological University
- **会议**: CVPR 2025

### USP: Unified Self-Supervised Pretraining for Image Generation and Understanding.
- **链接**: [arXiv:2503.06132](https://arxiv.org/abs/2503.06132) · 📚 被引 3
- **作者**: Xiangxiang Chu, Renda Li, Yong Wang
- **🏷️ 机构**: AMAP, Alibaba Group
- **会议**: ICCV 2025

> Semi-supervised learning in medical image segmentation leverages unlabeled data to reduce annotation burdens through consistency learning. However, current methods struggle with class imbalance and high uncertainty from pathology variations, leading to inaccurate segmentation in 3D medical images. To address these challenges, we present DyCON, a Dynamic Uncertainty-aware Consistency and Contrastive Learning framework that enhances the generalization of consistency methods with two complementary losses: Uncertainty-aware Consistency Loss (UnCL) and Focal Entropy-aware Contrastive Loss (FeCL). UnCL enforces global consistency by dynamically weighting the contribution of each voxel to the consistency loss based on its uncertainty, preserving high-uncertainty regions instead of filtering them out. Initially, UnCL prioritizes learning from uncertain voxels with lower penalties, encouraging the model to explore challenging regions. As training progress, the penalty shift towards confident voxels to refine predictions and ensure global consistency. Meanwhile, FeCL enhances local feature discrimination in imbalanced regions by introducing dual focal mechanisms and adaptive confidence adjustments into the contrastive principle. These mechanisms jointly prioritizes hard positives and negatives while focusing on uncertain sample pairs, effectively capturing subtle lesion variations under class imbalance. Extensive evaluations on four diverse medical image segmentation datasets (ISLES'22, BraTS'19, LA, Pancreas) show DyCON's superior performance against SOTA methods.

### Rayzer: a Self-Supervised Large View Synthesis Model.
- **链接**: [arXiv:2505.00702](https://arxiv.org/abs/2505.00702) · 📚 被引 4
- **作者**: Hanwen Jiang, Hao Tan, Peng Wang, Hai Jin, Yue Zhao, Sai Bi et al.
- **🏷️ 机构**: The University of Texas at Austin, Adobe Research, Cornell University
- **会议**: ICCV 2025

> Semi-supervised learning in medical image segmentation leverages unlabeled data to reduce annotation burdens through consistency learning. However, current methods struggle with class imbalance and high uncertainty from pathology variations, leading to inaccurate segmentation in 3D medical images. To address these challenges, we present DyCON, a Dynamic Uncertainty-aware Consistency and Contrastive Learning framework that enhances the generalization of consistency methods with two complementary losses: Uncertainty-aware Consistency Loss (UnCL) and Focal Entropy-aware Contrastive Loss (FeCL). UnCL enforces global consistency by dynamically weighting the contribution of each voxel to the consistency loss based on its uncertainty, preserving high-uncertainty regions instead of filtering them out. Initially, UnCL prioritizes learning from uncertain voxels with lower penalties, encouraging the model to explore challenging regions. As training progress, the penalty shift towards confident voxels to refine predictions and ensure global consistency. Meanwhile, FeCL enhances local feature discrimination in imbalanced regions by introducing dual focal mechanisms and adaptive confidence adjustments into the contrastive principle. These mechanisms jointly prioritizes hard positives and negatives while focusing on uncertain sample pairs, effectively capturing subtle lesion variations under class imbalance. Extensive evaluations on four diverse medical image segmentation datasets (ISLES'22, BraTS'19, LA, Pancreas) show DyCON's superior performance against SOTA methods.

### Instruct-CLIP: Improving Instruction-Guided Image Editing with Automated Data Refinement Using Contrastive Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_Instruct-CLIP_Improving_Instruction-Guided_Image_Editing_with_Automated_Data_Refinement_Using_CVPR_2025_paper.html)
- **作者**: Sherry X. Chen, Misha Sra, Pradeep Sen
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### Instruct-CLIP: Improving Instruction-Guided Image Editing with Automated Data Refinement Using Contrastive Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_Instruct-CLIP_Improving_Instruction-Guided_Image_Editing_with_Automated_Data_Refinement_Using_CVPR_2025_paper.html)
- **作者**: Sherry X. Chen, Misha Sra, Pradeep Sen
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### A Tale of Two Classes: Adapting Supervised Contrastive Learning to Binary Imbalanced Datasets.
- **链接**: [arXiv:2503.17024](https://arxiv.org/abs/2503.17024) · 📚 被引 10
- **作者**: David Mildenberger, Paul Hager, Daniel Rueckert, Martin J. Menten
- **🏷️ 机构**: Technical University of Munich
- **会议**: CVPR 2025

### Salvaging the Overlooked: Leveraging Class-Aware Contrastive Learning for Multi-Class Anomaly Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01989) · 📚 被引 6
- **作者**: Lei Fan, Junjie Huang, Donglin Di, Anyang Su, Tianyou Song, Maurice Pagnucco et al.
- **🏷️ 机构**: UNSW,Sydney, DZ-Matrix, Columbia University
- **会议**: ICCV 2025

> Supervised contrastive learning (SupCon) has proven to be a powerful alternative to the standard cross-entropy loss for classification of multi-class balanced datasets. However, it struggles to learn well-conditioned representations of datasets with long-tailed class distributions. This problem is potentially exacerbated for binary imbalanced distributions, which are commonly encountered during many real-world problems such as medical diagnosis. In experiments on seven binary datasets of natural and medical images, we show that the performance of SupCon decreases with increasing class imbalance. To substantiate these findings, we introduce two novel metrics that evaluate the quality of the learned representation space. By measuring the class distribution in local neighborhoods, we are able to uncover structural deficiencies of the representation space that classical metrics cannot detect. Informed by these insights, we propose two new supervised contrastive learning strategies tailored to binary imbalanced datasets that improve the structure of the representation space and increase downstream classification accuracy over standard SupCon by up to 35%. We make our code available.

</details>

### CLOC: Contrastive Learning for Ordinal Classification with Multi-Margin N-pair Loss.
- **链接**: [arXiv:2504.17813](https://arxiv.org/abs/2504.17813) · 📚 被引 11
- **作者**: Dileepa Pitawela, Gustavo Carneiro, Hsiang-Ting Chen
- **🏷️ 机构**: University of Adelaide, Australia, University of Surrey,CVSSP,UK
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In ordinal classification, misclassifying neighboring ranks is common, yet the consequences of these errors are not the same. For example, misclassifying benign tumor categories is less consequential, compared to an error at the pre-cancerous to cancerous threshold, which could profoundly influence treatment choices. Despite this, existing ordinal classification methods do not account for the varying importance of these margins, treating all neighboring classes as equally significant. To address this limitation, we propose CLOC, a new margin-based contrastive learning method for ordinal classification that learns an ordered representation based on the optimization of multiple margins with a novel multi-margin n-pair loss (MMNP). CLOC enables flexible decision boundaries across key adjacent categories, facilitating smooth transitions between classes and reducing the risk of overfitting to biases present in the training data. We provide empirical discussion regarding the properties of MMNP and show experimental results on five real-world image datasets (Adience, Historical Colour Image Dating, Knee Osteoarthritis, Indian Diabetic Retinopathy Image, and Breast Carcinoma Subtyping) and one synthetic dataset simulating clinical decision bias. Our results demonstrate that CLOC outperforms existing ordinal classification methods and show the interpretability and controllability of CLOC in learning meaningful, ordered representations that align with clinical and practical needs.

</details>

### Adapting to Observation Length of Trajectory Prediction via Contrastive Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Qiu_Adapting_to_Observation_Length_of_Trajectory_Prediction_via_Contrastive_Learning_CVPR_2025_paper.html) · 📚 被引 5
- **作者**: Ruiqi Qiu, Jun Gong, Xinyu Zhang, Siqi Luo, Bowen Zhang, Yi Cen
- **🏷️ 机构**: Northeastern University,China
- **会议**: CVPR 2025

### Multi-modal Contrastive Learning with Negative Sampling Calibration for Phenotypic Drug Discovery.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Rao_Multi-modal_Contrastive_Learning_with_Negative_Sampling_Calibration_for_Phenotypic_Drug_CVPR_2025_paper.html)
- **作者**: Jiahua Rao, Hanjing Lin, Leyu Chen, Jiancong Xie, Shuangjia Zheng, Yuedong Yang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### UniNet: A Contrastive Learning-guided Unified Framework with Feature Selection for Anomaly Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Wei_UniNet_A_Contrastive_Learning-guided_Unified_Framework_with_Feature_Selection_for_CVPR_2025_paper.html) · 📚 被引 26
- **作者**: Shun Wei, Jielin Jiang, Xiaolong Xu
- **🏷️ 机构**: Nanjing University of Information Science and Technology,China
- **会议**: CVPR 2025

### Link-based Contrastive Learning for One-Shot Unsupervised Domain Adaptation.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_Link-based_Contrastive_Learning_for_One-Shot_Unsupervised_Domain_Adaptation_CVPR_2025_paper.html) · 📚 被引 5
- **作者**: Yue Zhang, Mingyue Bin, Yuyang Zhang, Zhongyuan Wang, Zhen Han, Chao Liang
- **🏷️ 机构**: Wuhan University National Engineering Research Center for Multimedia Software(NERCMS) Hubei Key Laboratory of Multimedia and Network Communication Engineering,School of Computer Science,Wuhan
- **会议**: CVPR 2025

### Perceptual Inductive Bias Is What You Need Before Contrastive Learning.
- **链接**: [arXiv:2506.01201](https://arxiv.org/abs/2506.01201) · 📚 被引 2
- **作者**: Junru Zhao, Tianqin Li, Dunhan Jiang, Shenghao Wu, Alan Ramirez, Tai Sing Lee
- **🏷️ 机构**: Carnegie Mellon University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> David Marr's seminal theory of human perception stipulates that visual processing is a multi-stage process, prioritizing the derivation of boundary and surface properties before forming semantic object representations. In contrast, contrastive representation learning frameworks typically bypass this explicit multi-stage approach, defining their objective as the direct learning of a semantic representation space for objects. While effective in general contexts, this approach sacrifices the inductive biases of vision, leading to slower convergence speed and learning shortcut resulting in texture bias. In this work, we demonstrate that leveraging Marr's multi-stage theory-by first constructing boundary and surface-level representations using perceptual constructs from early visual processing stages and subsequently training for object semantics-leads to 2x faster convergence on ResNet18, improved final representations on semantic segmentation, depth estimation, and object recognition, and enhanced robustness and out-of-distribution capability. Together, we propose a pretraining stage before the general contrastive representation pretraining to further enhance the final representation quality and reduce the overall convergence time via inductive bias from human vision systems.

</details>

### From Prototypes to General Distributions: An Efficient Curriculum for Masked Image Modeling.
- **链接**: [arXiv:2411.10685](https://arxiv.org/abs/2411.10685) · 📚 被引 3
- **作者**: Jinhong Lin, Cheng-En Wu, Huanran Li, Jifan Zhang, Yu Hen Hu, Pedro Morgado
- **🏷️ 机构**: University of Wisconsin&#x2013;Madison
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> AI-generated face detectors trained via supervised learning typically rely on synthesized images from specific generators, limiting their generalization to emerging generative techniques. To overcome this limitation, we introduce a self-supervised method based on bi-level optimization. In the inner loop, we pretrain a vision encoder only on photographic face images using a set of linearly weighted pretext tasks: classification of categorical exchangeable image file format (EXIF) tags, ranking of ordinal EXIF tags, and detection of artificial face manipulations. The outer loop then optimizes the relative weights of these pretext tasks to enhance the coarse-grained detection of manipulated faces, serving as a proxy task for identifying AI-generated faces. In doing so, it aligns self-supervised learning more closely with the ultimate goal of AI-generated face detection. Once pretrained, the encoder remains fixed, and AI-generated faces are detected either as anomalies under a Gaussian mixture model fitted to photographic face features or by a lightweight two-layer perceptron serving as a binary classifier. Extensive experiments demonstrate that our detectors significantly outperform existing approaches in both one-class and binary classification settings, exhibiting strong generalization to unseen generators.

</details>

### Salvaging the Overlooked: Leveraging Class-Aware Contrastive Learning for Multi-Class Anomaly Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01989) · 📚 被引 6
- **作者**: Lei Fan, Junjie Huang, Donglin Di, Anyang Su, Tianyou Song, Maurice Pagnucco et al.
- **🏷️ 机构**: UNSW,Sydney, DZ-Matrix, Columbia University
- **会议**: ICCV 2025

### Robust Dataset Condensation using Supervised Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00274) · 📚 被引 0
- **作者**: Nicole Hee-Yeon Kim, Hwanjun Song
- **🏷️ 机构**: Korea Advanced Institute of Science and Technology (KAIST),Daejeon,Republic of Korea
- **会议**: ICCV 2025

### Selective Contrastive Learning for Weakly Supervised Affordance Grounding.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00495) · 📚 被引 2
- **作者**: WonJun Moon, Hyun Seok Seong, Jae-Pil Heo
- **🏷️ 机构**: Sungkyunkwan University
- **会议**: ICCV 2025

### AMD: Adaptive Momentum and Decoupled Contrastive Learning Framework for Robust Long-Tail Trajectory Prediction.
- **链接**: [arXiv:2507.01801](https://arxiv.org/abs/2507.01801) · 📚 被引 1
- **作者**: Bin Rao, Haicheng Liao, Yanchen Guan, Chengyue Wang, Bonan Wang, Jiaxun Zhang et al.
- **🏷️ 机构**: University of Macau,State Key Laboratory of Internet of Things for Smart City
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Accurately predicting the future trajectories of traffic agents is essential in autonomous driving. However, due to the inherent imbalance in trajectory distributions, tail data in natural datasets often represents more complex and hazardous scenarios. Existing studies typically rely solely on a base model's prediction error, without considering the diversity and uncertainty of long-tail trajectory patterns. We propose an adaptive momentum and decoupled contrastive learning framework (AMD), which integrates unsupervised and supervised contrastive learning strategies. By leveraging an improved momentum contrast learning (MoCo-DT) and decoupled contrastive learning (DCL) module, our framework enhances the model's ability to recognize rare and complex trajectories. Additionally, we design four types of trajectory random augmentation methods and introduce an online iterative clustering strategy, allowing the model to dynamically update pseudo-labels and better adapt to the distributional shifts in long-tail data. We propose three different criteria to define long-tail trajectories and conduct extensive comparative experiments on the nuScenes and ETH$/$UCY datasets. The results show that AMD not only achieves optimal performance in long-tail trajectory prediction but also demonstrates outstanding overall prediction accuracy.

</details>

### DuoCLR: Dual-Surrogate Contrastive Learning for Skeleton-Based Human Action Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01278) · 📚 被引 1
- **作者**: Haitao Tian
- **🏷️ 机构**: University of Ottawa,Canada
- **会议**: ICCV 2025

### FIX-CLIP: Dual-Branch Hierarchical Contrastive Learning via Synthetic Captions for Better Understanding of Long Text.
- **链接**: [arXiv:2507.10095](https://arxiv.org/abs/2507.10095) · [代码](https://github.com/bcwang-sjtu/Fix-CLIP) · 📚 被引 4
- **作者**: Bingchao Wang, Zhiwei Ning, Jianyu Ding, Xuanang Gao, Yin Li, Dongsheng Jiang et al.
- **🏷️ 机构**: Shanghai Jiao Tong University, Huawei Inc.
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> CLIP has shown promising performance across many short-text tasks in a zero-shot manner. However, limited by the input length of the text encoder, CLIP struggles on under-stream tasks with long-text inputs ($>77$ tokens). To remedy this issue, we propose FIX-CLIP, which includes three novel modules: (1) A dual-branch training pipeline that aligns short and long texts with masked and raw images, respectively, which boosts the long-text representation while preserving the short-text ability. (2) Multiple learnable regional prompts with unidirectional masks in Transformer layers for regional information extraction. (3) A hierarchical feature alignment module in the intermediate encoder layers to promote the consistency of multi-scale features. Furthermore, we collect 30M images and utilize existing MLLMs to synthesize long-text captions for training. Extensive experiments show that FIX-CLIP achieves state-of-the-art performance on both long-text and short-text retrieval benchmarks. For downstream applications, we reveal that FIX-CLIP's text encoder delivers promising performance in a plug-and-play manner for diffusion models with long-text input. The code is available at https://github.com/bcwang-sjtu/Fix-CLIP.

</details>

### Keep Your Friends Close, and Your Enemies Farther: Distance-Aware Voxel-Wise Contrastive Learning for Semi-Supervised Multi-Organ Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02027) · 📚 被引 0
- **作者**: Haochen Zhao, Jianwei Niu, Xuefeng Liu, Xiaozheng Xie, Li Kuang, Haotian Yang et al.
- **🏷️ 机构**: SCSE, Beihang University,State Key Laboratory of Virtual Reality Technology and Systems, School of Computer and Communication Engineering, University of Science and Technology Beijing, Hangzhou International Innovation Institute of Beihang University
- **会议**: ICCV 2025

### Beyond [cls]: Exploring the True Potential of Masked Image Modeling Representations.
- **链接**: [arXiv:2412.03215](https://arxiv.org/abs/2412.03215) · 📚 被引 3
- **作者**: Marcin Przewiezlikowski, Randall Balestriero, Wojciech Jasinski, Marek Smieja, Bartosz Zielinski
- **🏷️ 机构**: Jagiellonian University,Faculty of Mathematics and Computer Science, Brown University
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Masked Image Modeling (MIM) has emerged as a promising approach for Self-Supervised Learning (SSL) of visual representations. However, the out-of-the-box performance of MIMs is typically inferior to competing approaches. Most users cannot afford fine-tuning due to the need for large amounts of data, high GPU consumption, and specialized user knowledge. Therefore, the practical use of MIM representations is limited. In this paper we ask what is the reason for the poor out-of-the-box performance of MIMs. Is it due to weaker features produced by MIM models, or is it due to suboptimal usage? Through detailed analysis, we show that attention in MIMs is spread almost uniformly over many patches, leading to ineffective aggregation by the [cls] token. Based on this insight, we propose Selective Aggregation to better capture the rich semantic information retained in patch tokens, which significantly improves the out-of-the-box performance of MIM.

</details>

### Unsupervised Part Discovery via Descriptor-Based Masked Image Restoration with Optimized Constraints.
- **链接**: [arXiv:2507.11985](https://arxiv.org/abs/2507.11985) · [代码](https://github.com/Jiahao-UTS/MPAE) · 📚 被引 0
- **作者**: Jiahao Xia, Yike Wu, Wenjian Huang, Jianguo Zhang, Jian Zhang
- **🏷️ 机构**: University of Technology Sydney,Faculty of Engineering and IT, Southern University of Science and Technology,Dept. of Comp. Sci. and Eng.
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Part-level features are crucial for image understanding, but few studies focus on them because of the lack of fine-grained labels. Although unsupervised part discovery can eliminate the reliance on labels, most of them cannot maintain robustness across various categories and scenarios, which restricts their application range. To overcome this limitation, we present a more effective paradigm for unsupervised part discovery, named Masked Part Autoencoder (MPAE). It first learns part descriptors as well as a feature map from the inputs and produces patch features from a masked version of the original images. Then, the masked regions are filled with the learned part descriptors based on the similarity between the local features and descriptors. By restoring these masked patches using the part descriptors, they become better aligned with their part shapes, guided by appearance features from unmasked patches. Finally, MPAE robustly discovers meaningful parts that closely match the actual object shapes, even in complex scenarios. Moreover, several looser yet more effective constraints are proposed to enable MPAE to identify the presence of parts across various scenarios and categories in an unsupervised manner. This provides the foundation for addressing challenges posed by occlusion and for exploring part similarity across multiple categories. Extensive experiments demonstrate that our method robustly discovers meaningful parts across various categories and scenarios. The code is available at the project https://github.com/Jiahao-UTS/MPAE.

### Robust Dataset Condensation using Supervised Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00274) · 📚 被引 0
- **作者**: Nicole Hee-Yeon Kim, Hwanjun Song
- **🏷️ 机构**: Korea Advanced Institute of Science and Technology (KAIST),Daejeon,Republic of Korea
- **会议**: ICCV 2025

### Selective Contrastive Learning for Weakly Supervised Affordance Grounding.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00495) · 📚 被引 2
- **作者**: WonJun Moon, Hyun Seok Seong, Jae-Pil Heo
- **🏷️ 机构**: Sungkyunkwan University
- **会议**: ICCV 2025

### AMD: Adaptive Momentum and Decoupled Contrastive Learning Framework for Robust Long-Tail Trajectory Prediction.
- **链接**: [arXiv:2507.01801](https://arxiv.org/abs/2507.01801) · 📚 被引 1
- **作者**: Bin Rao, Haicheng Liao, Yanchen Guan, Chengyue Wang, Bonan Wang, Jiaxun Zhang et al.
- **🏷️ 机构**: University of Macau,State Key Laboratory of Internet of Things for Smart City
- **会议**: ICCV 2025

### DuoCLR: Dual-Surrogate Contrastive Learning for Skeleton-Based Human Action Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01278) · 📚 被引 1
- **作者**: Haitao Tian
- **🏷️ 机构**: University of Ottawa,Canada
- **会议**: ICCV 2025

### FIX-CLIP: Dual-Branch Hierarchical Contrastive Learning via Synthetic Captions for Better Understanding of Long Text.
- **链接**: [arXiv:2507.10095](https://arxiv.org/abs/2507.10095) · 📚 被引 4
- **作者**: Bingchao Wang, Zhiwei Ning, Jianyu Ding, Xuanang Gao, Yin Li, Dongsheng Jiang et al.
- **🏷️ 机构**: Shanghai Jiao Tong University, Huawei Inc.
- **会议**: ICCV 2025

### Keep Your Friends Close, and Your Enemies Farther: Distance-Aware Voxel-Wise Contrastive Learning for Semi-Supervised Multi-Organ Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02027) · 📚 被引 0
- **作者**: Haochen Zhao, Jianwei Niu, Xuefeng Liu, Xiaozheng Xie, Li Kuang, Haotian Yang et al.
- **🏷️ 机构**: SCSE, Beihang University,State Key Laboratory of Virtual Reality Technology and Systems, School of Computer and Communication Engineering, University of Science and Technology Beijing, Hangzhou International Innovation Institute of Beihang University
- **会议**: ICCV 2025

### Beyond [cls]: Exploring the True Potential of Masked Image Modeling Representations.
- **链接**: [arXiv:2412.03215](https://arxiv.org/abs/2412.03215) · 📚 被引 3
- **作者**: Marcin Przewiezlikowski, Randall Balestriero, Wojciech Jasinski, Marek Smieja, Bartosz Zielinski
- **🏷️ 机构**: Jagiellonian University,Faculty of Mathematics and Computer Science, Brown University
- **会议**: ICCV 2025

### Unsupervised Part Discovery via Descriptor-Based Masked Image Restoration with Optimized Constraints.
- **链接**: [arXiv:2507.11985](https://arxiv.org/abs/2507.11985) · 📚 被引 0
- **作者**: Jiahao Xia, Yike Wu, Wenjian Huang, Jianguo Zhang, Jian Zhang
- **🏷️ 机构**: University of Technology Sydney,Faculty of Engineering and IT, Southern University of Science and Technology,Dept. of Comp. Sci. and Eng.
- **会议**: ICCV 2025

## 跨领域论文（完整笔记在其他领域）

- AVF-MAE++: Scaling Affective Video Facial Masked Autoencoders via Efficient Audio-Visual Self-Supervised Learning. → [multimodal](../multimodal/Guideline%202025.md)
- Large Self-Supervised Models Bridge the Gap in Domain Adaptive Object Detection. → [object-detection](../object-detection/Guideline%202025.md)
- Learning from Synchronization: Self-Supervised Uncalibrated Multi-View Person Association in Challenging Scenes. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
- Enhanced Contrastive Learning with Multi-view Longitudinal Data for Chest X-ray Report Generation. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
- GeoDepth: From Point-to-Depth to Plane-to-Depth Modeling for Self-Supervised Monocular Depth Estimation. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
- SplatFlow: Self-Supervised Dynamic Gaussian Splatting in Neural Motion Flow Field for Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202025.md)
- S4-Driver: Scalable Self-Supervised Driving Multimodal Large Language Model with Spatio-Temporal Visual Representation. → [multimodal](../multimodal/Guideline%202025.md)

## 🆕 增量新增

### AVF-MAE++: Scaling Affective Video Facial Masked Autoencoders via Efficient Audio-Visual Self-Supervised Learning. **⭐⭐⭐** (相关度: 35%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Wu_AVF-MAE_Scaling_Affective_Video_Facial_Masked_Autoencoders_via_Efficient_Audio-Visual_CVPR_2025_paper.html) · 📚 被引 10
- **作者**: Xuecheng Wu, Heli Sun, Yifan Wang, Jiayu Nie, Jie Zhang, Yabing Wang et al.
- **🏷️ 机构**: Xi&#x2019;an Jiaotong University,School of Computer Science and Technology, University of Science and Technology of China, A*STAR,CFAR and IHPC
- **会议**: CVPR 2025
- **摘要（中）**: 针对情感视频面部识别中自监督学习效率不足的问题，提出了AVF-MAE++，通过高效的音视频自监督学习扩展掩码自编码器。该方法利用音频和视觉模态的互补性，提升面部情感表征学习。相比现有MAE方法，其引入了跨模态对齐和高效训练策略。摘要为空，具体效果未提供，但推测在情感识别任务上有性能提升。
- **摘要（英）**: This paper presents AVF-MAE++, an extension of masked autoencoders for affective video facial recognition via efficient audio-visual self-supervised learning. It leverages cross-modal alignment to improve facial emotion representations, though specific results are unavailable due to empty abstract.
- **核心贡献**: 提出音视频自监督的MAE扩展用于情感面部识别。
- **创新点**: 高效跨模态自监督学习策略。
- **结果**: 未提供具体数据。

### DAP-MAE: Domain-Adaptive Point Cloud Masked Autoencoder for Effective Cross-Domain Learning. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00333) · 📚 被引 1
- **作者**: Ziqi Gao, Qiufu Li, Linlin Shen
- **🏷️ 机构**: School of Computer Science &#x0026; Software Engineering, Shenzhen University, School of Artificial Intelligence, Shenzhen University
- **会议**: ICCV 2025
- **摘要（中）**: ①针对跨域点云学习中域适应能力不足的问题。②提出DAP-MAE，一种域自适应点云掩码自编码器，通过域自适应机制提升跨域学习效果。③相比标准MAE，引入域自适应模块，增强模型在不同域间的泛化能力。④摘要未提供具体数据，但预期在跨域点云任务上表现更优。
- **摘要（英）**: This paper tackles the challenge of domain adaptation in point cloud learning. It introduces DAP-MAE, a domain-adaptive masked autoencoder that incorporates domain adaptation mechanisms to improve cross-domain performance. The key improvement over standard MAE is the explicit handling of domain shifts, enhancing generalization. Specific results are not detailed in the abstract.
- **核心贡献**: 提出域自适应点云掩码自编码器。
- **创新点**: 在MAE中集成域自适应机制。
- **结果**: 预期提升跨域点云学习性能。

### Large Self-Supervised Models Bridge the Gap in Domain Adaptive Object Detection. **⭐⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2503.23220](https://arxiv.org/abs/2503.23220) · 📚 被引 9
- **作者**: Marc-Antoine Lavoie, Anas Mahmoud, Steven L. Waslander
- **🏷️ 机构**: University of Toronto Robotics Institute
- **会议**: CVPR 2025
- **摘要（中）**: ①针对域自适应目标检测（DAOD）中Mean Teacher自标记方法的脆弱性和耦合问题。②提出DINO Teacher方法，利用大型冻结的DINOv2骨干网络在源数据上训练新标记器，生成更准确的目标域标签。③相比现有方法，解耦了学习与标签生成过程，利用预训练大模型提升标签质量。④摘要指出生成的标签更准确，但未提供具体数值，预期显著提升DAOD性能。
- **摘要（英）**: This paper addresses the brittleness of Mean Teacher self-labelling in domain adaptive object detection (DAOD). It proposes DINO Teacher, which trains a new labeller on source data using a large frozen DINOv2 backbone to generate more accurate target-domain labels. The key improvement is decoupling learning from label generation and leveraging pretrained models. The abstract indicates improved label accuracy, though specific metrics are not provided.
- **核心贡献**: 提出利用冻结DINOv2的DINO Teacher方法提升DAOD标签质量。
- **创新点**: 解耦DAOD中的学习与标签生成，利用大模型预训练知识。
- **结果**: 生成更准确的目标域标签，预期提升检测性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The current state-of-the-art methods in domain adaptive object detection (DAOD) use Mean Teacher self-labelling, where a teacher model, directly derived as an exponential moving average of the student model, is used to generate labels on the target domain which are then used to improve both models in a positive loop. This couples learning and generating labels on the target domain, and other recent works also leverage the generated labels to add additional domain alignment losses. We believe this coupling is brittle and excessively constrained: there is no guarantee that a student trained only on source data can generate accurate target domain labels and initiate the positive feedback loop, and much better target domain labels can likely be generated by using a large pretrained network that has been exposed to much more data. Vision foundational models are exactly such models, and they have shown impressive task generalization capabilities even when frozen. We want to leverage these models for DAOD and introduce DINO Teacher, which consists of two components. First, we train a new labeller on source data only using a large frozen DINOv2 backbone and show it generates more accurate labels than Mean Teacher. Next, we align the student's source and target image patch features with those from a DINO encoder, driving source and target representations closer to the generalizable DINO representation. We obtain state-of-the-art performance on multiple DAOD datasets. Code available at https://github.com/TRAILab/DINO_Teacher

</details>

### Learning from Synchronization: Self-Supervised Uncalibrated Multi-View Person Association in Challenging Scenes. **⭐⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2503.13739](https://arxiv.org/abs/2503.13739) · 📚 被引 2
- **作者**: Keqi Chen, Vinkle Srivastav, Didier Mutter, Nicolas Padoy
- **🏷️ 机构**: University of Strasbourg,CNRS, INSERM, ICube, UMR7357,Strasbourg,France, IHU Strasbourg,France
- **会议**: CVPR 2025
- **摘要（中）**: ①针对多视角人物关联在相似外观和未标定相机下的挑战。②提出Self-MVA，一种自监督无标定多视角人物关联方法，利用跨视角图像同步作为预文本任务。③相比现有方法，无需标注或相机标定，通过同步标签训练模型。④摘要未提供具体数据，但预期在挑战性场景中提升关联鲁棒性。
- **摘要（英）**: This paper addresses multi-view person association under similar appearances and uncalibrated cameras. It proposes Self-MVA, a self-supervised approach using cross-view image synchronization as a pretext task. The key improvement is eliminating the need for annotations and calibration. Specific results are not detailed in the abstract.
- **核心贡献**: 提出自监督无标定多视角人物关联方法。
- **创新点**: 利用同步任务实现自监督关联。
- **结果**: 预期提升挑战场景下的关联性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-view person association is a fundamental step towards multi-view analysis of human activities. Although the person re-identification features have been proven effective, they become unreliable in challenging scenes where persons share similar appearances. Therefore, cross-view geometric constraints are required for a more robust association. However, most existing approaches are either fully-supervised using ground-truth identity labels or require calibrated camera parameters that are hard to obtain. In this work, we investigate the potential of learning from synchronization, and propose a self-supervised uncalibrated multi-view person association approach, Self-MVA, without using any annotations. Specifically, we propose a self-supervised learning framework, consisting of an encoder-decoder model and a self-supervised pretext task, cross-view image synchronization, which aims to distinguish whether two images from different views are captured at the same time. The model encodes each person's unified geometric and appearance features, and we train it by utilizing synchronization labels for supervision after applying Hungarian matching to bridge the gap between instance-wise and image-wise distances. To further reduce the solution space, we propose two types of self-supervised linear constraints: multi-view re-projection and pairwise edge association. Extensive experiments on three challenging public benchmark datasets (WILDTRACK, MVOR, and SOLDIERS) show that our approach achieves state-of-the-art results, surpassing existing unsupervised and fully-supervised approaches. Code is available at https://github.com/CAMMA-public/Self-MVA.

</details>

### LamRA: Large Multimodal Model as Your Advanced Retrieval Assistant.
- **链接**: [arXiv:2412.01720](https://arxiv.org/abs/2412.01720) · 📚 被引 14
- **作者**: Yikun Liu, Yajie Zhang, Jiayin Cai, Xiaolong Jiang, Yao Hu, Jiangchao Yao et al.
- **🏷️ 机构**: Shanghai Jiao Tong University,School of Artificial Intelligence,China, Xiaohongshu Inc.,China, Shanghai Jiao Tong University,CMIC,China
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> With the rapid advancement of multimodal information retrieval, increasingly complex retrieval tasks have emerged. Existing methods predominately rely on task-specific fine-tuning of vision-language models, often those trained with image-text contrastive learning. In this paper, we explore the possibility of re-purposing generative Large Multimodal Models (LMMs) for retrieval. This approach enables unifying all retrieval tasks under the same formulation and, more importantly, allows for extrapolation towards unseen retrieval tasks without additional training. Our contributions can be summarised in the following aspects: (i) We introduce LamRA, a versatile framework designed to empower LMMs with sophisticated retrieval and reranking capabilities. (ii) For retrieval, we adopt a two-stage training strategy comprising language-only pre-training and multimodal instruction tuning to progressively enhance LMM's retrieval performance. (iii) For reranking, we employ joint training for both pointwise and listwise reranking, offering two distinct ways to further boost the retrieval performance. (iv) Extensive experimental results underscore the efficacy of our method in handling more than ten retrieval tasks, demonstrating robust performance in both supervised and zero-shot settings, including scenarios involving previously unseen retrieval tasks.

</details>

### Context-Aware Multimodal Pretraining.
- **链接**: [arXiv:2411.15099](https://arxiv.org/abs/2411.15099)
- **作者**: Karsten Roth, Zeynep Akata, Dima Damen, Ivana Balazevic, Olivier J. Hénaff
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large-scale multimodal representation learning successfully optimizes for zero-shot transfer at test time. Yet the standard pretraining paradigm (contrastive learning on large amounts of image-text data) does not explicitly encourage representations to support few-shot adaptation. In this work, we propose a simple, but carefully designed extension to multimodal pretraining which enables representations to accommodate additional context. Using this objective, we show that vision-language models can be trained to exhibit significantly increased few-shot adaptation: across 21 downstream tasks, we find up to four-fold improvements in test-time sample efficiency, and average few-shot adaptation gains of over 5%, while retaining zero-shot generalization performance across model scales and training durations. In particular, equipped with simple, training-free, metric-based adaptation mechanisms, our representations easily surpass more complex and expensive optimization-based schemes, vastly simplifying generalization to new domains.

</details>

### Self-Supervised Learning for Color Spike Camera Reconstruction.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Dong_Self-Supervised_Learning_for_Color_Spike_Camera_Reconstruction_CVPR_2025_paper.html) · 📚 被引 2
- **作者**: Yanchen Dong, Ruiqin Xiong, Xiaopeng Fan, Zhaofei Yu, Yonghong Tian, Tiejun Huang
- **🏷️ 机构**: Peking University,School of Computer Science, Harbin Institute of Technology,School of Computer Science and Technology, Peking University,Institute for Artificial Intelligence
- **会议**: CVPR 2025

### Sonata: Self-Supervised Learning of Reliable Point Representations.
- **链接**: [arXiv:2503.16429](https://arxiv.org/abs/2503.16429) · 📚 被引 19
- **作者**: Xiaoyang Wu, Daniel DeTone, Duncan P. Frost, Tianwei Shen, Chris Xie, Nan Yang et al.
- **🏷️ 机构**: The University of Hong Kong, Meta Reality Labs Research
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we question whether we have a reliable self-supervised point cloud model that can be used for diverse 3D tasks via simple linear probing, even with limited data and minimal computation. We find that existing 3D self-supervised learning approaches fall short when evaluated on representation quality through linear probing. We hypothesize that this is due to what we term the "geometric shortcut", which causes representations to collapse to low-level spatial features. This challenge is unique to 3D and arises from the sparse nature of point cloud data. We address it through two key strategies: obscuring spatial information and enhancing the reliance on input features, ultimately composing a Sonata of 140k point clouds through self-distillation. Sonata is simple and intuitive, yet its learned representations are strong and reliable: zero-shot visualizations demonstrate semantic grouping, alongside strong spatial reasoning through nearest-neighbor relationships. Sonata demonstrates exceptional parameter and data efficiency, tripling linear probing accuracy (from 21.8% to 72.5%) on ScanNet and nearly doubling performance with only 1% of the data compared to previous approaches. Full fine-tuning further advances SOTA across both 3D indoor and outdoor perception tasks.

</details>

### Linguistics-aware Masked Image Modeling for Self-supervised Scene Text Recognition.
- **链接**: [arXiv:2503.18746](https://arxiv.org/abs/2503.18746) · 📚 被引 8
- **作者**: Yifei Zhang, Chang Liu, Jin Wei, Xiaomeng Yang, Yu Zhou, Can Ma et al.
- **🏷️ 机构**: Chinese Academy of Sciences,Institute of Information Engineering, Tsinghua University,Department of Automation and BNRist, Lenovo Research
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Text images are unique in their dual nature, encompassing both visual and linguistic information. The visual component encompasses structural and appearance-based features, while the linguistic dimension incorporates contextual and semantic elements. In scenarios with degraded visual quality, linguistic patterns serve as crucial supplements for comprehension, highlighting the necessity of integrating both aspects for robust scene text recognition (STR). Contemporary STR approaches often use language models or semantic reasoning modules to capture linguistic features, typically requiring large-scale annotated datasets. Self-supervised learning, which lacks annotations, presents challenges in disentangling linguistic features related to the global context. Typically, sequence contrastive learning emphasizes the alignment of local features, while masked image modeling (MIM) tends to exploit local structures to reconstruct visual patterns, resulting in limited linguistic knowledge. In this paper, we propose a Linguistics-aware Masked Image Modeling (LMIM) approach, which channels the linguistic information into the decoding process of MIM through a separate branch. Specifically, we design a linguistics alignment module to extract vision-independent features as linguistic guidance using inputs with different visual appearances. As features extend beyond mere visual structures, LMIM must consider the global context to achieve reconstruction. Extensive experiments on various benchmarks quantitatively demonstrate our state-of-the-art performance, and attention visualizations qualitatively show the simultaneous capture of both visual and linguistic information.

</details>

### GaussTR: Foundation Model-Aligned Gaussian Transformer for Self-Supervised 3D Spatial Understanding.
- **链接**: [arXiv:2412.13193](https://arxiv.org/abs/2412.13193) · 📚 被引 9
- **作者**: Haoyi Jiang, Liu Liu, Tianheng Cheng, Xinjie Wang, Tianwei Lin, Zhizhong Su et al.
- **🏷️ 机构**: Huazhong University of Science &#x0026; Technology, Horizon Robotics
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D Semantic Occupancy Prediction is fundamental for spatial understanding, yet existing approaches face challenges in scalability and generalization due to their reliance on extensive labeled data and computationally intensive voxel-wise representations. In this paper, we introduce GaussTR, a novel Gaussian-based Transformer framework that unifies sparse 3D modeling with foundation model alignment through Gaussian representations to advance 3D spatial understanding. GaussTR predicts sparse sets of Gaussians in a feed-forward manner to represent 3D scenes. By splatting the Gaussians into 2D views and aligning the rendered features with foundation models, GaussTR facilitates self-supervised 3D representation learning and enables open-vocabulary semantic occupancy prediction without requiring explicit annotations. Empirical experiments on the Occ3D-nuScenes dataset demonstrate GaussTR's state-of-the-art zero-shot performance of 12.27 mIoU, along with a 40% reduction in training time. These results highlight the efficacy of GaussTR for scalable and holistic 3D spatial understanding, with promising implications in autonomous driving and embodied agents. The code is available at https://github.com/hustvl/GaussTR.

</details>

### Noise Modeling in One Hour: Minimizing Preparation Efforts for Self-supervised Low-Light RAW Image Denoising.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Li_Noise_Modeling_in_One_Hour_Minimizing_Preparation_Efforts_for_Self-supervised_CVPR_2025_paper.html) · 📚 被引 6
- **作者**: Feiran Li, Haiyang Jiang, Daisuke Iso
- **🏷️ 机构**: Tokyo University, Sony Research
- **会议**: CVPR 2025

### AutoSSVH: Exploring Automated Frame Sampling for Efficient Self-Supervised Video Hashing.
- **链接**: [arXiv:2504.03587](https://arxiv.org/abs/2504.03587) · 📚 被引 7
- **作者**: Niu Lian, Jun Li, Jinpeng Wang, Ruisheng Luo, Yaowei Wang, Shu-Tao Xia et al.
- **🏷️ 机构**: Harbin Institute of Technology,Shenzhen, Tsinghua University,Tsinghua Shenzhen International Graduate School, Peng Cheng Laboratory,Research Center of Artificial Intelligence
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-Supervised Video Hashing (SSVH) compresses videos into hash codes for efficient indexing and retrieval using unlabeled training videos. Existing approaches rely on random frame sampling to learn video features and treat all frames equally. This results in suboptimal hash codes, as it ignores frame-specific information density and reconstruction difficulty. To address this limitation, we propose a new framework, termed AutoSSVH, that employs adversarial frame sampling with hash-based contrastive learning. Our adversarial sampling strategy automatically identifies and selects challenging frames with richer information for reconstruction, enhancing encoding capability. Additionally, we introduce a hash component voting strategy and a point-to-set (P2Set) hash-based contrastive objective, which help capture complex inter-video semantic relationships in the Hamming space and improve the discriminability of learned hash codes. Extensive experiments demonstrate that AutoSSVH achieves superior retrieval efficacy and efficiency compared to state-of-the-art approaches. Code is available at https://github.com/EliSpectre/CVPR25-AutoSSVH.

</details>

### Rotation-Equivariant Self-Supervised Method in Image Denoising.
- **链接**: [arXiv:2505.19618](https://arxiv.org/abs/2505.19618) · 📚 被引 6
- **作者**: Hanze Liu, Jiahong Fu, Qi Xie, Deyu Meng
- **🏷️ 机构**: Xi&#x2019;an Jiaotong University,Xi&#x2019;an,China
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised image denoising methods have garnered significant research attention in recent years, for this kind of method reduces the requirement of large training datasets. Compared to supervised methods, self-supervised methods rely more on the prior embedded in deep networks themselves. As a result, most of the self-supervised methods are designed with Convolution Neural Networks (CNNs) architectures, which well capture one of the most important image prior, translation equivariant prior. Inspired by the great success achieved by the introduction of translational equivariance, in this paper, we explore the way to further incorporate another important image prior. Specifically, we first apply high-accuracy rotation equivariant convolution to self-supervised image denoising. Through rigorous theoretical analysis, we have proved that simply replacing all the convolution layers with rotation equivariant convolution layers would modify the network into its rotation equivariant version. To the best of our knowledge, this is the first time that rotation equivariant image prior is introduced to self-supervised image denoising at the network architecture level with a comprehensive theoretical analysis of equivariance errors, which offers a new perspective to the field of self-supervised image denoising. Moreover, to further improve the performance, we design a new mask mechanism to fusion the output of rotation equivariant network and vanilla CNN-based network, and construct an adaptive rotation equivariant framework. Through extensive experiments on three typical methods, we have demonstrated the effectiveness of the proposed method.

</details>

### When the Future Becomes the Past: Taming Temporal Correspondence for Self-supervised Video Representation Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_When_the_Future_Becomes_the_Past_Taming_Temporal_Correspondence_for_CVPR_2025_paper.html) · 📚 被引 7
- **作者**: Yang Liu, Qianqian Xu, Peisong Wen, Siran Dai, Qingming Huang
- **🏷️ 机构**: University of Chinese Academy of Sciences,School of Computer Science and Technology, Institute of Computing Technology,Chinese Academy of Sciences, Institute of Information Engineering,Chinese Academy of Sciences
- **会议**: CVPR 2025

### Shading Meets Motion: Self-supervised Indoor 3D Reconstruction Via Simultaneous Shape-from-Shading and Structure-from-Motion.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Lu_Shading_Meets_Motion_Self-supervised_Indoor_3D_Reconstruction_Via_Simultaneous_Shape-from-Shading_CVPR_2025_paper.html) · 📚 被引 2
- **作者**: Guoyu Lu
- **🏷️ 机构**: Intelligent Vision and Sensing Lab Binghamton University
- **会议**: CVPR 2025

### SpatialDreamer: Self-supervised Stereo Video Synthesis from Monocular Input.
- **链接**: [arXiv:2411.11934](https://arxiv.org/abs/2411.11934) · 📚 被引 2
- **作者**: Zhen Lv, Yangqi Long, Congzhentao Huang, Cao Li, Chengfei Lv, Hao Ren et al.
- **🏷️ 机构**: Alibaba Group, Sun Yat-sen University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Stereo video synthesis from a monocular input is a demanding task in the fields of spatial computing and virtual reality. The main challenges of this task lie on the insufficiency of high-quality paired stereo videos for training and the difficulty of maintaining the spatio-temporal consistency between frames. Existing methods primarily address these issues by directly applying novel view synthesis (NVS) techniques to video, while facing limitations such as the inability to effectively represent dynamic scenes and the requirement for large amounts of training data. In this paper, we introduce a novel self-supervised stereo video synthesis paradigm via a video diffusion model, termed SpatialDreamer, which meets the challenges head-on. Firstly, to address the stereo video data insufficiency, we propose a Depth based Video Generation module DVG, which employs a forward-backward rendering mechanism to generate paired videos with geometric and temporal priors. Leveraging data generated by DVG, we propose RefinerNet along with a self-supervised synthetic framework designed to facilitate efficient and dedicated training. More importantly, we devise a consistency control module, which consists of a metric of stereo deviation strength and a Temporal Interaction Learning module TIL for geometric and temporal consistency ensurance respectively. We evaluated the proposed method against various benchmark methods, with the results showcasing its superior performance.

</details>

### Generalized Recorrupted-to-Recorrupted: Self-Supervised Learning Beyond Gaussian Noise.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Monroy_Generalized_Recorrupted-to-Recorrupted_Self-Supervised_Learning_Beyond_Gaussian_Noise_CVPR_2025_paper.html) · 📚 被引 9
- **作者**: Brayan Monroy, Jorge Bacca, Julián Tachella
- **🏷️ 机构**: Universidad Industrial de Santander, CNRS &amp; ENS Lyon
- **会议**: CVPR 2025

### Self-supervised ControlNet with Spatio-Temporal Mamba for Real-world Video Super-resolution.
- **链接**: [arXiv:2506.01037](https://arxiv.org/abs/2506.01037) · 📚 被引 5
- **作者**: Shijun Shi, Jing Xu, Lijing Lu, Zhihang Li, Kai Hu
- **🏷️ 机构**: Jiangnan University, University of Science and Technology of China, Peking University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing diffusion-based video super-resolution (VSR) methods are susceptible to introducing complex degradations and noticeable artifacts into high-resolution videos due to their inherent randomness. In this paper, we propose a noise-robust real-world VSR framework by incorporating self-supervised learning and Mamba into pre-trained latent diffusion models. To ensure content consistency across adjacent frames, we enhance the diffusion model with a global spatio-temporal attention mechanism using the Video State-Space block with a 3D Selective Scan module, which reinforces coherence at an affordable computational cost. To further reduce artifacts in generated details, we introduce a self-supervised ControlNet that leverages HR features as guidance and employs contrastive learning to extract degradation-insensitive features from LR videos. Finally, a three-stage training strategy based on a mixture of HR-LR videos is proposed to stabilize VSR training. The proposed Self-supervised ControlNet with Spatio-Temporal Continuous Mamba based VSR algorithm achieves superior perceptual quality than state-of-the-arts on real-world VSR benchmark datasets, validating the effectiveness of the proposed model design and training strategies.

</details>

### Self-Supervised Spatial Correspondence Across Modalities.
- **链接**: [arXiv:2506.03148](https://arxiv.org/abs/2506.03148) · 📚 被引 1
- **作者**: Ayush Shrivastava, Andrew Owens
- **🏷️ 机构**: University of Michigan
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a method for finding cross-modal space-time correspondences. Given two images from different visual modalities, such as an RGB image and a depth map, our model identifies which pairs of pixels correspond to the same physical points in the scene. To solve this problem, we extend the contrastive random walk framework to simultaneously learn cycle-consistent feature representations for both cross-modal and intra-modal matching. The resulting model is simple and has no explicit photo-consistency assumptions. It can be trained entirely using unlabeled data, without the need for any spatially aligned multimodal image pairs. We evaluate our method on both geometric and semantic correspondence tasks. For geometric matching, we consider challenging tasks such as RGB-to-depth and RGB-to-thermal matching (and vice versa); for semantic matching, we evaluate on photo-sketch and cross-style image alignment. Our method achieves strong performance across all benchmarks.

</details>

### Common3D: Self-Supervised Learning of 3D Morphable Models for Common Objects in Neural Feature Space.
- **链接**: [arXiv:2504.21749](https://arxiv.org/abs/2504.21749) · 📚 被引 1
- **作者**: Leonhard Sommer, Olaf Dünkel, Christian Theobalt, Adam Kortylewski
- **🏷️ 机构**: University of Freiburg, Max Planck Institute for Informatics
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D morphable models (3DMMs) are a powerful tool to represent the possible shapes and appearances of an object category. Given a single test image, 3DMMs can be used to solve various tasks, such as predicting the 3D shape, pose, semantic correspondence, and instance segmentation of an object. Unfortunately, 3DMMs are only available for very few object categories that are of particular interest, like faces or human bodies, as they require a demanding 3D data acquisition and category-specific training process. In contrast, we introduce a new method, Common3D, that learns 3DMMs of common objects in a fully self-supervised manner from a collection of object-centric videos. For this purpose, our model represents objects as a learned 3D template mesh and a deformation field that is parameterized as an image-conditioned neural network. Different from prior works, Common3D represents the object appearance with neural features instead of RGB colors, which enables the learning of more generalizable representations through an abstraction from pixel intensities. Importantly, we train the appearance features using a contrastive objective by exploiting the correspondences defined through the deformable template mesh. This leads to higher quality correspondence features compared to related works and a significantly improved model performance at estimating 3D object pose and semantic correspondence. Common3D is the first completely self-supervised method that can solve various vision tasks in a zero-shot manner.

</details>

### ONDA-Pose: Occlusion-Aware Neural Domain Adaptation for Self-Supervised 6D Object Pose Estimation.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Tan_ONDA-Pose_Occlusion-Aware_Neural_Domain_Adaptation_for_Self-Supervised_6D_Object_Pose_CVPR_2025_paper.html) · 📚 被引 2
- **作者**: Tao Tan, Qiulei Dong
- **🏷️ 机构**: University of Chinese Academy of Sciences State Key Laboratory of Multimodal Artificial Intelligence Systems, CASIA,School of Artificial Intelligence
- **会议**: CVPR 2025

### FSFM: A Generalizable Face Security Foundation Model via Self-Supervised Facial Representation Learning.
- **链接**: [arXiv:2412.12032](https://arxiv.org/abs/2412.12032) · 📚 被引 9
- **作者**: Gaojian Wang, Feng Lin, Tong Wu, Zhenguang Liu, Zhongjie Ba, Kui Ren
- **🏷️ 机构**: Zhejiang University,State Key Laboratory of Blockchain and Data Security
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This work asks: with abundant, unlabeled real faces, how to learn a robust and transferable facial representation that boosts various face security tasks with respect to generalization performance? We make the first attempt and propose a self-supervised pretraining framework to learn fundamental representations of real face images, FSFM, that leverages the synergy between masked image modeling (MIM) and instance discrimination (ID). We explore various facial masking strategies for MIM and present a simple yet powerful CRFR-P masking, which explicitly forces the model to capture meaningful intra-region consistency and challenging inter-region coherency. Furthermore, we devise the ID network that naturally couples with MIM to establish underlying local-to-global correspondence via tailored self-distillation. These three learning objectives, namely 3C, empower encoding both local features and global semantics of real faces. After pretraining, a vanilla ViT serves as a universal vision foundation model for downstream face security tasks: cross-dataset deepfake detection, cross-domain face anti-spoofing, and unseen diffusion facial forgery detection. Extensive experiments on 10 public datasets demonstrate that our model transfers better than supervised pretraining, visual and facial self-supervised learning arts, and even outperforms task-specialized SOTA methods.

</details>

### Synthetic-to-Real Self-supervised Robust Depth Estimation via Learning with Motion and Structure Priors.
- **链接**: [arXiv:2503.20211](https://arxiv.org/abs/2503.20211) · 📚 被引 4
- **作者**: Weilong Yan, Ming Li, Haipeng Li, Shuwei Shao, Robby T. Tan
- **🏷️ 机构**: National University of Singapore, Guangdong Laboratory of Artificial Intelligence and Digital Economy (SZ), University of Electronic Science and Technology of China
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised depth estimation from monocular cameras in diverse outdoor conditions, such as daytime, rain, and nighttime, is challenging due to the difficulty of learning universal representations and the severe lack of labeled real-world adverse data. Previous methods either rely on synthetic inputs and pseudo-depth labels or directly apply daytime strategies to adverse conditions, resulting in suboptimal results. In this paper, we present the first synthetic-to-real robust depth estimation framework, incorporating motion and structure priors to capture real-world knowledge effectively. In the synthetic adaptation, we transfer motion-structure knowledge inside cost volumes for better robust representation, using a frozen daytime model to train a depth estimator in synthetic adverse conditions. In the innovative real adaptation, which targets to fix synthetic-real gaps, models trained earlier identify the weather-insensitive regions with a designed consistency-reweighting strategy to emphasize valid pseudo-labels. We introduce a new regularization by gathering explicit depth distributions to constrain the model when facing real-world data. Experiments show that our method outperforms the state-of-the-art across diverse conditions in multi-frame and single-frame evaluations. We achieve improvements of 7.5% and 4.3% in AbsRel and RMSE on average for nuScenes and Robotcar datasets (daytime, nighttime, rain). In zero-shot evaluation of DrivingStereo (rain, fog), our method generalizes better than the previous ones.

</details>

### ImagineFSL: Self-Supervised Pretraining Matters on Imagined Base Set for VLM-based Few-shot Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Yang_ImagineFSL_Self-Supervised_Pretraining_Matters_on_Imagined_Base_Set_for_VLM-based_CVPR_2025_paper.html) · 📚 被引 1
- **作者**: Haoyuan Yang, Xiaoou Li, Jiaming Lv, Xianjun Cheng, Qilong Wang, Peihua Li
- **🏷️ 机构**: Dalian University of Technology, Beijing University of Posts and Telecommunications, Tianjin University
- **会议**: CVPR 2025

### Temporal Overlapping Prediction: A Self-Supervised Pre-Training Method for LiDAR Moving Object Segmentation.
- **链接**: [arXiv:2503.07167](https://arxiv.org/abs/2503.07167) · 📚 被引 1
- **作者**: Ziliang Miao, Runjian Chen, Yixi Cai, Buwei He, Wenquan Zhao, Wenqi Shao et al.
- **🏷️ 机构**: The University of Hong Kong, KTH Royal Institute of Technology, Southern University of Science and Technology
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Moving object segmentation (MOS) on LiDAR point clouds is crucial for autonomous systems like self-driving vehicles. Previous supervised approaches rely heavily on costly manual annotations, while LiDAR sequences naturally capture temporal motion cues that can be leveraged for self-supervised learning. In this paper, we propose Temporal Overlapping Prediction (TOP), a self-supervised pre-training method that alleviate the labeling burden for MOS. TOP explores the temporal overlapping points that commonly observed by current and adjacent scans, and learns spatiotemporal representations by predicting the occupancy states of temporal overlapping points. Moreover, we utilize current occupancy reconstruction as an auxiliary pre-training objective, which enhances the current structural awareness of the model. We conduct extensive experiments and observe that the conventional metric Intersection-over-Union (IoU) shows strong bias to objects with more scanned points, which might neglect small or distant objects. To compensate for this bias, we introduce an additional metric called mIoU_obj to evaluate object-level performance. Experiments on nuScenes and SemanticKITTI show that TOPoutperforms both supervised training-from-scratch baseline and other self-supervised pre-training baselines by up to 28.77% relative improvement, demonstrating strong transferability across LiDAR setups and generalization to other tasks. Code and pre-trained models will be publicly available upon publication.

</details>

### Point Cloud Self-Supervised Learning via 3D to Multi-View Masked Learner.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02564)
- **作者**: Zhimin Chen, Xuewei Chen, Xiao Guo, Yingwei Li, Longlong Jing, Liang Yang et al.
- **🏷️ 机构**: Clemson University, Michigan State University, Johns Hopkins University
- **会议**: ICCV 2025

### Harnessing Text-to-Image Diffusion Models for Point Cloud Self-Supervised Learning.
- **链接**: [arXiv:2507.09102](https://arxiv.org/abs/2507.09102)
- **作者**: Yiyang Chen, Shanshan Zhao, Lunhao Duan, Changxing Ding, Dacheng Tao
- **🏷️ 机构**: South China University of Technology, Alibaba International Digital Commerce Group, Nanyang Technological University
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Diffusion-based models, widely used in text-to-image generation, have proven effective in 2D representation learning. Recently, this framework has been extended to 3D self-supervised learning by constructing a conditional point generator for enhancing 3D representations. However, its performance remains constrained by the 3D diffusion model, which is trained on the available 3D datasets with limited size. We hypothesize that the robust capabilities of text-to-image diffusion models, particularly Stable Diffusion (SD), which is trained on large-scale datasets, can help overcome these limitations. To investigate this hypothesis, we propose PointSD, a framework that leverages the SD model for 3D self-supervised learning. By replacing the SD model's text encoder with a 3D encoder, we train a point-to-image diffusion model that allows point clouds to guide the denoising of rendered noisy images. With the trained point-to-image diffusion model, we use noise-free images as the input and point clouds as the condition to extract SD features. Next, we train a 3D backbone by aligning its features with these SD features, thereby facilitating direct semantic learning. Comprehensive experiments on downstream point cloud tasks and ablation studies demonstrate that the SD model can enhance point cloud self-supervised learning. Code is publicly available at https://github.com/wdttt/PointSD.

</details>

### StruMamba3D: Exploring Structural Mamba for Self-Supervised Point Cloud Representation Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02651) · 📚 被引 2
- **作者**: Chuxin Wang, Yixin Zha, Wenfei Yang, Tianzhu Zhang
- **🏷️ 机构**: University of Science and Technology of China
- **会议**: ICCV 2025

### Towards More Diverse and Challenging Pre-Training for Point Cloud Learning: Self-Supervised Cross Reconstruction with Decoupled Views.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02665) · 📚 被引 3
- **作者**: Xiangdong Zhang, Shaofeng Zhang, Junchi Yan
- **🏷️ 机构**: School of AI, Shanghai Jiao Tong University
- **会议**: ICCV 2025

### Open-Set Cross Modal Generalization via Multimodal Unified Representation.
- **链接**: [arXiv:2507.14935](https://arxiv.org/abs/2507.14935)
- **作者**: Hai Huang, Yan Xia, Shulei Wang, Hanting Wang, Minghui Fang, Shengpeng Ji et al.
- **🏷️ 机构**: Zhejiang University
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper extends Cross Modal Generalization (CMG) to open-set environments by proposing the more challenging Open-set Cross Modal Generalization (OSCMG) task. This task evaluates multimodal unified representations in open-set conditions, addressing the limitations of prior closed-set cross-modal evaluations. OSCMG requires not only cross-modal knowledge transfer but also robust generalization to unseen classes within new modalities, a scenario frequently encountered in real-world applications. Existing multimodal unified representation work lacks consideration for open-set environments. To tackle this, we propose MICU, comprising two key components: Fine-Coarse Masked multimodal InfoNCE (FCMI) and Cross modal Unified Jigsaw Puzzles (CUJP). FCMI enhances multimodal alignment by applying contrastive learning at both holistic semantic and temporal levels, incorporating masking to enhance generalization. CUJP enhances feature diversity and model uncertainty by integrating modality-agnostic feature selection with self-supervised learning, thereby strengthening the model's ability to handle unknown categories in open-set tasks. Extensive experiments on CMG and the newly proposed OSCMG validate the effectiveness of our approach. The code is available at https://github.com/haihuangcode/CMG.

</details>

### Differential-Informed Sample Selection Accelerates Multimodal Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00281)
- **作者**: Zihua Zhao, Feng Hong, Mengxi Chen, Pengyi Chen, Benyuan Liu, Jiangchao Yao et al.
- **🏷️ 机构**: Cooperative Medianet Innovation Center, Shanghai Jiao Tong University, School of AI, Shanghai Jiao Tong University
- **会议**: ICCV 2025

### Are They the Same? Exploring Visual Correspondence Shortcomings of Multimodal LLMs.
- **链接**: [arXiv:2501.04670](https://arxiv.org/abs/2501.04670) · 📚 被引 1
- **作者**: Yikang Zhou, Tao Zhang, Shilin Xu, Shihao Chen, Qianyu Zhou, Yunhai Tong et al.
- **🏷️ 机构**: Wuhan University, Peking University, SJTU
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advancements in multimodal large language models (MLLM) have shown a strong ability in visual perception, reasoning abilities, and vision-language understanding. However, the visual matching ability of MLLMs is rarely studied, despite finding the visual correspondence of objects is essential in computer vision. Our research reveals that the matching capabilities in recent MLLMs still exhibit systematic shortcomings, even with current strong MLLMs models, GPT-4o. In particular, we construct a Multimodal Visual Matching (MMVM) benchmark to fairly benchmark over 30 different MLLMs. The MMVM benchmark is built from 15 open-source datasets and Internet videos with manual annotation. We categorize the data samples of MMVM benchmark into eight aspects based on the required cues and capabilities to more comprehensively evaluate and analyze current MLLMs. In addition, we have designed an automatic annotation pipeline to generate the MMVM SFT dataset, including 220K visual matching data with reasoning annotation. To our knowledge, this is the first visual corresponding dataset and benchmark for the MLLM community. Finally, we present CoLVA, a novel contrastive MLLM with two novel technical designs: fine-grained vision expert with object-level contrastive learning and instruction augmentation strategy. The former learns instance discriminative tokens, while the latter further improves instruction following ability. CoLVA-InternVL2-4B achieves an overall accuracy (OA) of 49.80\% on the MMVM benchmark, surpassing GPT-4o and the best open-source MLLM, Qwen2VL-72B, by 7.15\% and 11.72\% OA, respectively. These results demonstrate the effectiveness of our MMVM SFT dataset and our novel technical designs. Code, benchmark, dataset, and models will be released.

</details>

### Boosting Generative Adversarial Transferability with Self-Supervised Vision Transformer Features.
- **链接**: [arXiv:2506.21046](https://arxiv.org/abs/2506.21046)
- **作者**: Shangbo Wu, Yu-an Tan, Ruinan Ma, Wencong Ma, Dehua Zhu, Yuanzhang Li
- **🏷️ 机构**: School of Cyberspace Science and Technology, Beijing Institute of Technology, School of Computer Science and Technology, Beijing Institute of Technology
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The ability of deep neural networks (DNNs) come from extracting and interpreting features from the data provided. By exploiting intermediate features in DNNs instead of relying on hard labels, we craft adversarial perturbation that generalize more effectively, boosting black-box transferability. These features ubiquitously come from supervised learning in previous work. Inspired by the exceptional synergy between self-supervised learning and the Transformer architecture, this paper explores whether exploiting self-supervised Vision Transformer (ViT) representations can improve adversarial transferability. We present dSVA -- a generative dual self-supervised ViT features attack, that exploits both global structural features from contrastive learning (CL) and local textural features from masked image modeling (MIM), the self-supervised learning paradigm duo for ViTs. We design a novel generative training framework that incorporates a generator to create black-box adversarial examples, and strategies to train the generator by exploiting joint features and the attention mechanism of self-supervised ViTs. Our findings show that CL and MIM enable ViTs to attend to distinct feature tendencies, which, when exploited in tandem, boast great adversarial generalizability. By disrupting dual deep features distilled by self-supervised ViTs, we are rewarded with remarkable black-box transferability to models of various architectures that outperform state-of-the-arts. Code available at https://github.com/spencerwooo/dSVA.

</details>

### GaussianOcc: Fully Self-Supervised and Efficient 3D Occupancy Estimation with Gaussian Splatting.
- **链接**: [arXiv:2408.11447](https://arxiv.org/abs/2408.11447) · 📚 被引 3
- **作者**: Wanshui Gan, Fang Liu, Hongbin Xu, Ningkai Mo, Naoto Yokoya
- **🏷️ 机构**: The University of Tokyo, South China University of Technology, Shenzhen Institute of Advanced Technology, Chinese Academy of Sciences
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce GaussianOcc, a systematic method that investigates the two usages of Gaussian splatting for fully self-supervised and efficient 3D occupancy estimation in surround views. First, traditional methods for self-supervised 3D occupancy estimation still require ground truth 6D poses from sensors during training. To address this limitation, we propose Gaussian Splatting for Projection (GSP) module to provide accurate scale information for fully self-supervised training from adjacent view projection. Additionally, existing methods rely on volume rendering for final 3D voxel representation learning using 2D signals (depth maps, semantic maps), which is both time-consuming and less effective. We propose Gaussian Splatting from Voxel space (GSV) to leverage the fast rendering properties of Gaussian splatting. As a result, the proposed GaussianOcc method enables fully self-supervised (no ground truth pose) 3D occupancy estimation in competitive performance with low computational cost (2.7 times faster in training and 5 times faster in rendering). The relevant code is available in https://github.com/GANWANSHUI/GaussianOcc.git.

</details>

### SignRep: Enhancing Self-Supervised Sign Representations.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02117)
- **作者**: Ryan Wong, Necati Cihan Camgöz, Richard Bowden
- **🏷️ 机构**: University of Surrey, Meta Reality Labs
- **会议**: ICCV 2025

### Self-Supervised Monocular 4D Scene Reconstruction for Egocentric Videos.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00829) · 📚 被引 1
- **作者**: Chengbo Yuan, Geng Chen, Li Yi, Yang Gao
- **🏷️ 机构**: Institute for Interdisciplinary Information Sciences, Tsinghua University, Shanghai Qi Zhi Institute
- **会议**: ICCV 2025

### Hybrid-Grained Feature Aggregation with Coarse-to-Fine Language Guidance for Self-Supervised Monocular Depth Estimation.
- **链接**: [arXiv:2510.09320](https://arxiv.org/abs/2510.09320) · 📚 被引 1
- **作者**: Wenyao Zhang, Hongsi Liu, Bohan Li, Jiawei He, Zekun Qi, Yunnan Wang et al.
- **🏷️ 机构**: AI Institute, Shanghai Jiao Tong University,MoE Key Lab of Artificial Intelligence, Ningbo Institute of Digital Twin, Eastern Institute of Technology,Ningbo,China, CASIA
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Current self-supervised monocular depth estimation (MDE) approaches encounter performance limitations due to insufficient semantic-spatial knowledge extraction. To address this challenge, we propose Hybrid-depth, a novel framework that systematically integrates foundation models (e.g., CLIP and DINO) to extract visual priors and acquire sufficient contextual information for MDE. Our approach introduces a coarse-to-fine progressive learning framework: 1) Firstly, we aggregate multi-grained features from CLIP (global semantics) and DINO (local spatial details) under contrastive language guidance. A proxy task comparing close-distant image patches is designed to enforce depth-aware feature alignment using text prompts; 2) Next, building on the coarse features, we integrate camera pose information and pixel-wise language alignment to refine depth predictions. This module seamlessly integrates with existing self-supervised MDE pipelines (e.g., Monodepth2, ManyDepth) as a plug-and-play depth encoder, enhancing continuous depth estimation. By aggregating CLIP's semantic context and DINO's spatial details through language guidance, our method effectively addresses feature granularity mismatches. Extensive experiments on the KITTI benchmark demonstrate that our method significantly outperforms SOTA methods across all metrics, which also indeed benefits downstream tasks like BEV perception. Code is available at https://github.com/Zhangwenyao1/Hybrid-depth.

</details>

### CoraLSRT: Revisiting Coral Reef Semantic Segmentation by Feature Rectification via Self-Supervised Guidance.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01857) · 📚 被引 4
- **作者**: Ziqiang Zheng, Yuk-Kwan Wong, Binh-Son Hua, Jianbo Shi, Sai-Kit Yeung
- **🏷️ 机构**: The Hong Kong University of Science and Technology, Trinity College Dublin, University of Pennsylvania
- **会议**: ICCV 2025

### Bi-Level Optimization for Self-Supervised AI-Generated Face Detection.
- **链接**: [arXiv:2507.22824](https://arxiv.org/abs/2507.22824) · 📚 被引 1
- **作者**: Mian Zou, Nan Zhong, Baosheng Yu, Yibing Zhan, Kede Ma
- **🏷️ 机构**: Jiangxi University of Finance and Economics, City University of Hong Kong, Nanyang Technological University
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> AI-generated face detectors trained via supervised learning typically rely on synthesized images from specific generators, limiting their generalization to emerging generative techniques. To overcome this limitation, we introduce a self-supervised method based on bi-level optimization. In the inner loop, we pretrain a vision encoder only on photographic face images using a set of linearly weighted pretext tasks: classification of categorical exchangeable image file format (EXIF) tags, ranking of ordinal EXIF tags, and detection of artificial face manipulations. The outer loop then optimizes the relative weights of these pretext tasks to enhance the coarse-grained detection of manipulated faces, serving as a proxy task for identifying AI-generated faces. In doing so, it aligns self-supervised learning more closely with the ultimate goal of AI-generated face detection. Once pretrained, the encoder remains fixed, and AI-generated faces are detected either as anomalies under a Gaussian mixture model fitted to photographic face features or by a lightweight two-layer perceptron serving as a binary classifier. Extensive experiments demonstrate that our detectors significantly outperform existing approaches in both one-class and binary classification settings, exhibiting strong generalization to unseen generators.

</details>

### Semi-Supervised Vision-Centric 3D Occupancy World Model for Autonomous Driving.
- **链接**: [arXiv:2502.07309](https://arxiv.org/abs/2502.07309)
- **作者**: Xiang Li, Pengfei Li, Yupeng Zheng, Wei Sun, Yan Wang, Yilun Chen
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Understanding world dynamics is crucial for planning in autonomous driving. Recent methods attempt to achieve this by learning a 3D occupancy world model that forecasts future surrounding scenes based on current observation. However, 3D occupancy labels are still required to produce promising results. Considering the high annotation cost for 3D outdoor scenes, we propose a semi-supervised vision-centric 3D occupancy world model, PreWorld, to leverage the potential of 2D labels through a novel two-stage training paradigm: the self-supervised pre-training stage and the fully-supervised fine-tuning stage. Specifically, during the pre-training stage, we utilize an attribute projection head to generate different attribute fields of a scene (e.g., RGB, density, semantic), thus enabling temporal supervision from 2D labels via volume rendering techniques. Furthermore, we introduce a simple yet effective state-conditioned forecasting module to recursively forecast future occupancy and ego trajectory in a direct manner. Extensive experiments on the nuScenes dataset validate the effectiveness and scalability of our method, and demonstrate that PreWorld achieves competitive performance across 3D occupancy prediction, 4D occupancy forecasting and motion planning tasks.

</details>

### Gramian Multimodal Representation Learning and Alignment.
- **链接**: [arXiv:2412.11959](https://arxiv.org/abs/2412.11959)
- **作者**: Giordano Cicchetti, Eleonora Grassucci, Luigi Sigillo, Danilo Comminiello
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Human perception integrates multiple modalities, such as vision, hearing, and language, into a unified understanding of the surrounding reality. While recent multimodal models have achieved significant progress by aligning pairs of modalities via contrastive learning, their solutions are unsuitable when scaling to multiple modalities. These models typically align each modality to a designated anchor without ensuring the alignment of all modalities with each other, leading to suboptimal performance in tasks requiring a joint understanding of multiple modalities. In this paper, we structurally rethink the pairwise conventional approach to multimodal learning and we present the novel Gramian Representation Alignment Measure (GRAM), which overcomes the above-mentioned limitations. GRAM learns and then aligns $n$ modalities directly in the higher-dimensional space in which modality embeddings lie by minimizing the Gramian volume of the $k$-dimensional parallelotope spanned by the modality vectors, ensuring the geometric alignment of all modalities simultaneously. GRAM can replace cosine similarity in any downstream method, holding for 2 to $n$ modalities and providing more meaningful alignment with respect to previous similarity measures. The novel GRAM-based contrastive loss function enhances the alignment of multimodal models in the higher-dimensional embedding space, leading to new state-of-the-art performance in downstream tasks such as video-audio-text retrieval and audio-video classification. The project page, the code, and the pretrained models are available at https://ispamm.github.io/GRAM/.

</details>

### What to align in multimodal contrastive learning?
- **链接**: [出版页](https://openreview.net/forum?id=Pe3AxLq6Wf)
- **作者**: Benoit Dufumier, Javiera Castillo Navarro, Devis Tuia, Jean-Philippe Thiran
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Weighted Point Set Embedding for Multimodal Contrastive Learning Toward Optimal Similarity Metric.
- **链接**: [出版页](https://openreview.net/forum?id=uSz2K30RRd)
- **作者**: Toshimitsu Uesaka, Taiji Suzuki, Yuhta Takida, Chieh-Hsin Lai, Naoki Murata, Yuki Mitsufuji
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### An Information Criterion for Controlled Disentanglement of Multimodal Data.
- **链接**: [arXiv:2410.23996](https://arxiv.org/abs/2410.23996)
- **作者**: Chenyu Wang, Sharut Gupta, Xinyi Zhang, Sana Tonekaboni, Stefanie Jegelka, Tommi S. Jaakkola et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal representation learning seeks to relate and decompose information inherent in multiple modalities. By disentangling modality-specific information from information that is shared across modalities, we can improve interpretability and robustness and enable downstream tasks such as the generation of counterfactual outcomes. Separating the two types of information is challenging since they are often deeply entangled in many real-world applications. We propose Disentangled Self-Supervised Learning (DisentangledSSL), a novel self-supervised approach for learning disentangled representations. We present a comprehensive analysis of the optimality of each disentangled representation, particularly focusing on the scenario not covered in prior work where the so-called Minimum Necessary Information (MNI) point is not attainable. We demonstrate that DisentangledSSL successfully learns shared and modality-specific features on multiple synthetic and real-world datasets and consistently outperforms baselines on various downstream tasks, including prediction tasks for vision-language data, as well as molecule-phenotype retrieval tasks for biological data. The code is available at https://github.com/uhlerlab/DisentangledSSL.

</details>

## 跨领域论文（完整笔记在其他领域）

- MI-DETR: An Object Detection Model with Multi-time Inquiries Mechanism. → [object-detection](../object-detection/Guideline%202025.md)
- Dynamic-DINO: Fine-Grained Mixture of Experts Tuning for Real-Time Open-Vocabulary Object Detection. → [open-set-detection](../open-set-detection/Guideline%202025.md)
- Talking to DINO: Bridging Self-Supervised Vision Backbones with Language for Open-Vocabulary Segmentation. → [open-set-detection](../open-set-detection/Guideline%202025.md)
- CQ-DINO: Mitigating Gradient Dilution via Category Queries for Vast Vocabulary Object Detection. → [object-detection](../object-detection/Guideline%202025.md)
- CSPCL: Category Semantic Prior Contrastive Learning for Deformable DETR-Based Prohibited Item Detectors. → [object-detection](../object-detection/Guideline%202025.md)
- GeoDepth: From Point-to-Depth to Plane-to-Depth Modeling for Self-Supervised Monocular Depth Estimation. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
- Fine-Grained Image-Text Correspondence with Cost Aggregation for Open-Vocabulary Part Segmentation. → [open-set-detection](../open-set-detection/Guideline%202025.md)
- Mosaic3D: Foundation Dataset and Model for Open-Vocabulary 3D Segmentation. → [open-set-detection](../open-set-detection/Guideline%202025.md)
- DeCLIP: Decoupled Learning for Open-Vocabulary Dense Perception. → [vlm](../vlm/Guideline%202025.md)
- Forensic Self-Descriptions Are All You Need for Zero-Shot Detection, Open-Set Source Attribution, and Clustering of AI-generated Images. → [open-set-detection](../open-set-detection/Guideline%202025.md)
- VisionPAD: A Vision-Centric Pre-training Paradigm for Autonomous Driving. → [object-detection](../object-detection/Guideline%202025.md)
- SplatFlow: Self-Supervised Dynamic Gaussian Splatting in Neural Motion Flow Field for Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202025.md)
- S4-Driver: Scalable Self-Supervised Driving Multimodal Large Language Model with Spatio-Temporal Visual Representation. → [multimodal](../multimodal/Guideline%202025.md)
- Florence-VL: Enhancing Vision-Language Models with Generative Vision Encoder and Depth-Breadth Fusion. → [vlm](../vlm/Guideline%202025.md)
- Stealthy Backdoor Attack in Self-Supervised Learning Vision Encoders for Large Vision Language Models. → [vlm](../vlm/Guideline%202025.md)
- NLPrompt: Noise-Label Prompt Learning for Vision-Language Models. → [vlm](../vlm/Guideline%202025.md)
- SmartCLIP: Modular Vision-language Alignment with Identification Guarantees. → [vlm](../vlm/Guideline%202025.md)
- STiL: Semi-supervised Tabular-Image Learning for Comprehensive Task-Relevant Information Exploration in Multimodal Classification. → [multimodal](../multimodal/Guideline%202025.md)
- VidHalluc: Evaluating Temporal Hallucinations in Multimodal Large Language Models for Video Understanding. → [video-understanding](../video-understanding/Guideline%202025.md)
- VoteFlow: Enforcing Local Rigidity in Self-Supervised Scene Flow. → [autonomous-driving](../autonomous-driving/Guideline%202025.md)
- Do Your Best and Get Enough Rest for Continual Learning. → [continual-learning](../continual-learning/Guideline%202025.md)
- Plug-in Feedback Self-Adaptive Attention in CLIP for Training-Free Open-Vocabulary Segmentation. → [open-set-detection](../open-set-detection/Guideline%202025.md)
- Harnessing Vision Foundation Models for High-Performance, Training-Free Open Vocabulary Segmentation. → [open-set-detection](../open-set-detection/Guideline%202025.md)
- AD-GS: Object-Aware B-Spline Gaussian Splatting for Self-Supervised Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202025.md)
- AMD: Adaptive Momentum and Decoupled Contrastive Learning Framework for Robust Long-Tail Trajectory Prediction. → [autonomous-driving](../autonomous-driving/Guideline%202025.md)
- Enhancing End-to-End Autonomous Driving with Latent World Model. → [autonomous-driving](../autonomous-driving/Guideline%202025.md)

<!-- COMPLETE v1 papers=118 -->
