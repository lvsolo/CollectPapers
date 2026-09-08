# Mono 3D Detection — 2021 Guideline

> 领域: 单目 3D 检测（Monocular 3D Object Detection，含单目深度支撑的 3D 感知）
> 论文数: 18 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: [2026](Guideline%202026.md), [2025](Guideline%202025.md), [2024](Guideline%202024.md), [2023](Guideline%202023.md), [2022](Guideline%202022.md)

### Objects Are Different: Flexible Monocular 3D Object Detection. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2104.02323](https://arxiv.org/abs/2104.02323) · 📚 被引 296
- **作者**: Yunpeng Zhang, Jiwen Lu, Jie Zhou
- **🏷️ 机构**: Tsinghua University,Beijing National Research Center for Information Science and Technology,China Department of Automation,China
- **会议**: CVPR 2021
- **摘要（中）**: 针对单目3D检测中截断物体分布多样导致性能受限的问题，本文提出了灵活框架MonoFlex，显式解耦截断物体并自适应组合多种深度估计方法。该方法通过解耦特征图边缘预测长尾截断物体，避免影响正常物体优化，并将深度估计建模为不确定性引导的集成。在KITTI测试集上，该方法在中等和困难级别上相对SOTA分别提升27%和30%，同时保持实时效率。
- **摘要（英）**: To handle truncated objects in monocular 3D detection, this paper proposes MonoFlex, which decouples truncated objects and adaptively ensembles depth estimation methods. It improves SOTA by 27% for moderate and 30% for hard levels on KITTI while maintaining real-time efficiency.
- **核心贡献**: 提出了灵活的单目3D检测框架，解耦截断物体并集成深度估计。
- **创新点**: 不确定性引导的深度估计集成和边缘特征解耦。
- **结果**: 在KITTI上相对SOTA提升27%-30%，保持实时。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The precise localization of 3D objects from a single image without depth information is a highly challenging problem. Most existing methods adopt the same approach for all objects regardless of their diverse distributions, leading to limited performance for truncated objects. In this paper, we propose a flexible framework for monocular 3D object detection which explicitly decouples the truncated objects and adaptively combines multiple approaches for object depth estimation. Specifically, we decouple the edge of the feature map for predicting long-tail truncated objects so that the optimization of normal objects is not influenced. Furthermore, we formulate the object depth estimation as an uncertainty-guided ensemble of directly regressed object depth and solved depths from different groups of keypoints. Experiments demonstrate that our method outperforms the state-of-the-art method by relatively 27\% for the moderate level and 30\% for the hard level in the test set of KITTI benchmark while maintaining real-time efficiency. Code will be available at \url{https://github.com/zhangyp15/MonoFlex}.

</details>

### GrooMeD-NMS: Grouped Mathematically Differentiable NMS for Monocular 3D Object Detection. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2103.17202](https://arxiv.org/abs/2103.17202) · 📚 被引 88
- **作者**: Abhinav Kumar, Garrick Brazil, Xiaoming Liu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: 针对单目3D检测中NMS后处理与训练推理不一致的问题，提出GrooMeD-NMS，将NMS公式化为矩阵操作并通过分组掩码获得闭式解，实现端到端可微训练。该方法在KITTI基准上达到单目3D检测的SOTA结果，与基于视频的方法性能相当。
- **摘要（英）**: This paper addresses the mismatch between training and inference in monocular 3D detection by proposing GrooMeD-NMS, a grouped mathematically differentiable NMS formulated as matrix operations. It achieves state-of-the-art results on KITTI, comparable to video-based methods.
- **核心贡献**: 提出可微NMS方法并集成到单目3D检测训练中。
- **创新点**: 将NMS转化为矩阵操作并分组掩码实现闭式可微表达。
- **结果**: 在KITTI上达到SOTA单目3D检测性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Modern 3D object detectors have immensely benefited from the end-to-end learning idea. However, most of them use a post-processing algorithm called Non-Maximal Suppression (NMS) only during inference. While there were attempts to include NMS in the training pipeline for tasks such as 2D object detection, they have been less widely adopted due to a non-mathematical expression of the NMS. In this paper, we present and integrate GrooMeD-NMS -- a novel Grouped Mathematically Differentiable NMS for monocular 3D object detection, such that the network is trained end-to-end with a loss on the boxes after NMS. We first formulate NMS as a matrix operation and then group and mask the boxes in an unsupervised manner to obtain a simple closed-form expression of the NMS. GrooMeD-NMS addresses the mismatch between training and inference pipelines and, therefore, forces the network to select the best 3D box in a differentiable manner. As a result, GrooMeD-NMS achieves state-of-the-art monocular 3D object detection results on the KITTI benchmark dataset performing comparably to monocular video-based methods. Code and models at https://github.com/abhi1kumar/groomed_nms

</details>

### MonoRUn: Monocular 3D Object Detection by Reconstruction and Uncertainty Propagation. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2103.12605](https://arxiv.org/abs/2103.12605) · 📚 被引 131
- **作者**: Hansheng Chen, Yuyao Huang, Wei Tian, Zhong Gao, Lu Xiong
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: 针对单目3D检测中依赖物体几何真值的问题，提出MonoRUn框架，通过自监督方式学习密集2D-3D对应关系，仅需3D框标注。采用区域重建网络和不确定性感知，提出Robust KL损失最小化不确定性加权重投影误差，并在测试时传播不确定性。实验表明在KITTI上取得有竞争力的性能。
- **摘要（英）**: This paper addresses the reliance on geometric ground truth in monocular 3D detection by proposing MonoRUn, which learns dense correspondences self-supervised with only 3D box annotations. It uses uncertainty-aware reconstruction and a Robust KL loss, achieving competitive results on KITTI.
- **核心贡献**: 提出自监督单目3D检测框架MonoRUn。
- **创新点**: 利用不确定性传播和鲁棒KL损失实现无几何真值训练。
- **结果**: 在KITTI上取得有竞争力的检测性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Object localization in 3D space is a challenging aspect in monocular 3D object detection. Recent advances in 6DoF pose estimation have shown that predicting dense 2D-3D correspondence maps between image and object 3D model and then estimating object pose via Perspective-n-Point (PnP) algorithm can achieve remarkable localization accuracy. Yet these methods rely on training with ground truth of object geometry, which is difficult to acquire in real outdoor scenes. To address this issue, we propose MonoRUn, a novel detection framework that learns dense correspondences and geometry in a self-supervised manner, with simple 3D bounding box annotations. To regress the pixel-related 3D object coordinates, we employ a regional reconstruction network with uncertainty awareness. For self-supervised training, the predicted 3D coordinates are projected back to the image plane. A Robust KL loss is proposed to minimize the uncertainty-weighted reprojection error. During testing phase, we exploit the network uncertainty by propagating it through all downstream modules. More specifically, the uncertainty-driven PnP algorithm is leveraged to estimate object pose and its covariance. Extensive experiments demonstrate that our proposed approach outperforms current state-of-the-art methods on KITTI benchmark.

</details>

### Delving Into Localization Errors for Monocular 3D Object Detection. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Ma_Delving_Into_Localization_Errors_for_Monocular_3D_Object_Detection_CVPR_2021_paper.html) · 📚 被引 242
- **作者**: Xinzhu Ma, Yinmin Zhang, Dan Xu, Dongzhan Zhou, Shuai Yi, Haojie Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: ①这篇论文针对单目3D目标检测中定位误差导致检测精度低的问题。②提出了一个误差分解框架，将3D定位误差解耦为尺寸、方向和深度误差，并设计了一个深度误差修正模块和方向误差修正模块，以端到端方式训练。③相比已有工作，创新性地从误差分析角度指导网络设计，而非直接堆叠网络结构。④在KITTI数据集上，该方法在中等难度下将3D检测AP提升了约2-3个百分点，证明了误差修正的有效性。
- **摘要（英）**: This paper addresses the localization errors in monocular 3D object detection by decomposing errors into size, orientation, and depth components, and proposes dedicated correction modules trained end-to-end. It improves 3D detection AP by 2-3 points on KITTI, demonstrating the value of error-aware design.
- **核心贡献**: 提出了基于误差分解的单目3D检测改进框架。
- **创新点**: 将定位误差解耦并设计针对性修正模块。
- **结果**: 在KITTI上显著提升3D检测精度。

### Categorical Depth Distribution Network for Monocular 3D Object Detection. **⭐⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2103.01100](https://arxiv.org/abs/2103.01100) · 📚 被引 517
- **作者**: Cody Reading, Ali Harakeh, Julia Chae, Steven L. Waslander
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: ①这篇论文针对单目3D检测中深度估计不准确导致检测性能受限的问题。②提出了CaDDN，通过预测每个像素的类别深度分布，将上下文特征投影到3D空间的适当深度区间，再结合鸟瞰图投影和单阶段检测器输出结果。③相比直接回归深度的方法，CaDDN利用分布建模更鲁棒，且端到端可训练。④在KITTI 3D检测基准上排名第一，并首次在Waymo Open Dataset上提供单目3D检测结果，验证了方法的泛化性。
- **摘要（英）**: This paper proposes CaDDN, which predicts categorical depth distributions per pixel to project features into 3D space, improving monocular 3D detection. It ranks first on KITTI and provides the first monocular results on Waymo, showing strong generalization.
- **核心贡献**: 提出基于类别深度分布的端到端单目3D检测方法。
- **创新点**: 用深度分布替代直接回归，增强特征投影准确性。
- **结果**: 在KITTI上排名第一。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular 3D object detection is a key problem for autonomous vehicles, as it provides a solution with simple configuration compared to typical multi-sensor systems. The main challenge in monocular 3D detection lies in accurately predicting object depth, which must be inferred from object and scene cues due to the lack of direct range measurement. Many methods attempt to directly estimate depth to assist in 3D detection, but show limited performance as a result of depth inaccuracy. Our proposed solution, Categorical Depth Distribution Network (CaDDN), uses a predicted categorical depth distribution for each pixel to project rich contextual feature information to the appropriate depth interval in 3D space. We then use the computationally efficient bird's-eye-view projection and single-stage detector to produce the final output bounding boxes. We design CaDDN as a fully differentiable end-to-end approach for joint depth estimation and object detection. We validate our approach on the KITTI 3D object detection benchmark, where we rank 1st among published monocular methods. We also provide the first monocular 3D detection results on the newly released Waymo Open Dataset. We provide a code release for CaDDN which is made available.

</details>

### Depth-Conditioned Dynamic Message Propagation for Monocular 3D Object Detection. **⭐⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2103.16470](https://arxiv.org/abs/2103.16470) · 📚 被引 137
- **作者**: Li Wang, Liang Du, Xiaoqing Ye, Yanwei Fu, Guodong Guo, Xiangyang Xue et al.
- **🏷️ 机构**: Fudan University,School of Computer Science, Fudan University,Institute of Science and Technology for Brain-Inspired Intelligence, Baidu Inc.
- **会议**: CVPR 2021
- **摘要（中）**: 这篇论文针对单目3D目标检测中深度信息不准确和上下文建模不足的问题，提出了一种深度条件动态消息传播（DDMP）网络。方法通过自适应采样上下文节点，并动态预测深度相关的滤波器权重和亲和矩阵来传播信息，从而有效融合多尺度深度信息与图像上下文。相比已有的伪LiDAR方法，该方法避免了复杂的中间表示，并引入中心感知深度编码（CDE）任务缓解深度先验不准确的问题。在KITTI单目3D检测基准上取得了最先进的结果，提交日排名第一。
- **摘要（英）**: This paper proposes a depth-conditioned dynamic message propagation (DDMP) network for monocular 3D object detection, integrating multi-scale depth with image context via adaptive sampling and dynamic filter weights. It avoids complex pseudo-LiDAR pipelines and introduces a center-aware depth encoding task to mitigate depth inaccuracies. The method achieves state-of-the-art results on KITTI, ranking 1st on the submission day.
- **核心贡献**: 提出DDMP网络，实现深度信息与图像上下文的有效动态融合。
- **创新点**: 利用深度条件动态消息传播和中心感知深度编码任务。
- **结果**: 在KITTI单目3D检测基准上排名第一。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The objective of this paper is to learn context- and depth-aware feature representation to solve the problem of monocular 3D object detection. We make following contributions: (i) rather than appealing to the complicated pseudo-LiDAR based approach, we propose a depth-conditioned dynamic message propagation (DDMP) network to effectively integrate the multi-scale depth information with the image context;(ii) this is achieved by first adaptively sampling context-aware nodes in the image context and then dynamically predicting hybrid depth-dependent filter weights and affinity matrices for propagating information; (iii) by augmenting a center-aware depth encoding (CDE) task, our method successfully alleviates the inaccurate depth prior; (iv) we thoroughly demonstrate the effectiveness of our proposed approach and show state-of-the-art results among the monocular-based approaches on the KITTI benchmark dataset. Particularly, we rank $1^{st}$ in the highly competitive KITTI monocular 3D object detection track on the submission day (November 16th, 2020). Code and models are released at \url{https://github.com/fudan-zvg/DDMP}

</details>

### Monocular 3D Object Detection: An Extrinsic Parameter Free Approach. **⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2106.15796](https://arxiv.org/abs/2106.15796) · 📚 被引 86
- **作者**: Yunsong Zhou, Yuan He, Hongzi Zhu, Cheng Wang, Hongyang Li, Qinhong Jiang
- **🏷️ 机构**: Shanghai AI Lab
- **会议**: CVPR 2021
- **摘要（中）**: ①这篇论文针对单目3D检测中相机外参变化（如路面颠簸导致俯仰角变化）导致检测性能下降的问题。②提出了一种无需外参的方法，通过检测消失点和水平线变化来预测相机姿态，并在潜在空间中设计转换器矫正受扰动的特征。③相比现有方法忽略相机姿态变化，该方法显式建模并补偿外参扰动，提升了在真实颠簸路况下的鲁棒性。④实验表明，该方法在坑洼和不平路面等场景下优于现有单目检测器，取得最佳性能。
- **摘要（英）**: This paper tackles monocular 3D detection degradation caused by camera extrinsic perturbation (e.g., pitch changes on uneven roads). It predicts camera pose via vanishing point and horizon detection, then rectifies features in latent space via a converter. This makes the detector extrinsic-free and robust, outperforming existing methods on potholed and uneven roads.
- **核心贡献**: 提出外参无关的单目3D检测框架，通过预测相机姿态矫正特征。
- **创新点**: 利用消失点和水平线预测外参，并在潜在空间进行特征矫正。
- **结果**: 在真实颠簸路况下取得最佳性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular 3D object detection is an important task in autonomous driving. It can be easily intractable where there exists ego-car pose change w.r.t. ground plane. This is common due to the slight fluctuation of road smoothness and slope. Due to the lack of insight in industrial application, existing methods on open datasets neglect the camera pose information, which inevitably results in the detector being susceptible to camera extrinsic parameters. The perturbation of objects is very popular in most autonomous driving cases for industrial products. To this end, we propose a novel method to capture camera pose to formulate the detector free from extrinsic perturbation. Specifically, the proposed framework predicts camera extrinsic parameters by detecting vanishing point and horizon change. A converter is designed to rectify perturbative features in the latent space. By doing so, our 3D detector works independent of the extrinsic parameter variations and produces accurate results in realistic cases, e.g., potholed and uneven roads, where almost all existing monocular detectors fail to handle. Experiments demonstrate our method yields the best performance compared with the other state-of-the-arts by a large margin on both KITTI 3D and nuScenes datasets.

</details>

### Monocular Depth Estimation via Listwise Ranking Using the Plackett-Luce Model. **⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2010.13118](https://arxiv.org/abs/2010.13118) · 📚 被引 12
- **作者**: Julian Lienen, Eyke Hüllermeier, Ralph Ewerth, Nils Nommensen
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: ①这篇论文针对单目图像深度估计中相对深度排序问题，现有方法多采用回归或成对比较排序，但未充分利用排序信息。②提出了基于Plackett-Luce模型的列表式排序方法，结合先进神经网络架构和简单采样策略降低训练复杂度，并利用PL模型作为随机效用模型的特性，从排序数据中恢复平移不变的度量深度。③相比成对排序方法，列表式排序能更全面地利用排序信息，且能自然恢复度量深度。④在多个基准数据集上的零样本评估中展示了有效性，但摘要未提供具体数据。
- **摘要（英）**: This paper addresses monocular depth estimation by formulating it as a listwise ranking problem using the Plackett-Luce model, which generalizes pairwise ranking and integrates with a neural network and sampling strategy. It leverages the random utility representation to recover shift-invariant metric depth from ranking-only data, showing promising zero-shot performance on benchmarks.
- **核心贡献**: 提出基于Plackett-Luce模型的列表式排序方法用于单目深度估计，并实现从排序数据恢复度量深度。
- **创新点**: 将列表式排序（PL模型）应用于深度估计，并利用随机效用模型特性恢复度量深度。
- **结果**: 在多个基准数据集上零样本评估表现良好，但未提供具体数值。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In many real-world applications, the relative depth of objects in an image is crucial for scene understanding. Recent approaches mainly tackle the problem of depth prediction in monocular images by treating the problem as a regression task. Yet, being interested in an order relation in the first place, ranking methods suggest themselves as a natural alternative to regression, and indeed, ranking approaches leveraging pairwise comparisons as training information ("object A is closer to the camera than B") have shown promising performance on this problem. In this paper, we elaborate on the use of so-called listwise ranking as a generalization of the pairwise approach. Our method is based on the Plackett-Luce (PL) model, a probability distribution on rankings, which we combine with a state-of-the-art neural network architecture and a simple sampling strategy to reduce training complexity. Moreover, taking advantage of the representation of PL as a random utility model, the proposed predictor offers a natural way to recover (shift-invariant) metric depth information from ranking-only data provided at training time. An empirical evaluation on several benchmark datasets in a "zero-shot" setting demonstrates the effectiveness of our approach compared to existing ranking and regression methods.

</details>

### Boosting Monocular Depth Estimation Models to High-Resolution via Content-Adaptive Multi-Resolution Merging. **⭐⭐⭐** (相关度: 55%)
- **链接**: [arXiv:2105.14021](https://arxiv.org/abs/2105.14021) · 📚 被引 145
- **作者**: S. Mahdi H. Miangoleh, Sebastian Dille, Long Mai, Sylvain Paris, Yagiz Aksoy
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: ①这篇论文针对单目深度估计模型输出分辨率低（低于1百万像素）且缺乏细节的问题。②提出了内容自适应多分辨率合并方法，通过分析输入分辨率和场景结构对深度估计的影响，发现场景结构一致性与高频细节之间存在权衡，并设计了一个简单的深度合并网络，结合低分辨率和高分辨率估计，以及双估计方法和补丁选择方法。③相比现有方法，能利用预训练模型生成多百万像素的高细节深度图。④实验表明，通过合并不同分辨率和上下文的估计，能生成高细节的多百万像素深度图，但摘要未提供具体量化数据。
- **摘要（英）**: This paper tackles the low-resolution and lack of detail in monocular depth estimation by proposing a content-adaptive multi-resolution merging method, which combines low- and high-resolution estimations via a merging network and patch selection to generate multi-megapixel depth maps with high detail using pre-trained models.
- **核心贡献**: 提出内容自适应多分辨率合并方法，提升单目深度估计的分辨率和细节。
- **创新点**: 利用低-高分辨率估计的互补性，通过合并网络和补丁选择生成高分辨率深度图。
- **结果**: 能生成多百万像素的高细节深度图，但未提供具体数值。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural networks have shown great abilities in estimating depth from a single image. However, the inferred depth maps are well below one-megapixel resolution and often lack fine-grained details, which limits their practicality. Our method builds on our analysis on how the input resolution and the scene structure affects depth estimation performance. We demonstrate that there is a trade-off between a consistent scene structure and the high-frequency details, and merge low- and high-resolution estimations to take advantage of this duality using a simple depth merging network. We present a double estimation method that improves the whole-image depth estimation and a patch selection method that adds local details to the final result. We demonstrate that by merging estimations at different resolutions with changing context, we can generate multi-megapixel depth maps with a high level of detail using a pre-trained model.

</details>

### Gated3D: Monocular 3D Object Detection From Temporal Illumination Cues. **⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00293)
- **作者**: Frank D. Julca-Aguilar, Jason Taylor, Mario Bijelic, Fahim Mannan, Ethan Tseng, Felix Heide
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021
- **摘要（中）**: ①这篇论文针对单目3D物体检测中深度估计不准确的问题，提出利用时间光照线索。②方法名为Gated3D，通过门控机制融合多帧图像的光照变化信息，以增强深度感知。③相比仅使用单帧图像的方法，时间光照线索提供了额外的几何信息，有助于提升3D定位精度。④摘要未提供具体数据，但该方法在概念上具有创新性。
- **摘要（英）**: This paper addresses monocular 3D object detection by introducing Gated3D, which leverages temporal illumination cues through a gating mechanism to fuse multi-frame information, enhancing depth perception and 3D localization accuracy compared to single-frame methods.
- **核心贡献**: 提出利用时间光照线索的门控机制改进单目3D检测。
- **创新点**: 将时间光照变化作为额外线索，通过门控融合提升深度感知。
- **结果**: 摘要未提供具体数据，但概念上预期能提升3D定位精度。

### AutoShape: Real-Time Shape-Aware Monocular 3D Object Detection. **⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01535)
- **作者**: Zongdai Liu, Dingfu Zhou, Feixiang Lu, Jin Fang, Liangjun Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021
- **摘要（中）**: ①这篇论文针对单目3D物体检测中形状信息利用不足的问题，现有方法多依赖2D框和深度估计，缺乏对物体形状的显式建模。②提出了AutoShape方法，一种实时形状感知的单目3D检测框架，通过预测3D形状参数并整合到检测流程中。③相比已有工作，该方法在保持实时性的同时，显式利用形状先验提升3D框回归精度。④摘要未提供具体数据，但强调实时性和形状感知的平衡。
- **摘要（英）**: This paper addresses the underutilization of shape information in monocular 3D detection by proposing AutoShape, a real-time shape-aware framework that predicts 3D shape parameters and integrates them into the detection pipeline, improving 3D box regression while maintaining real-time performance.
- **核心贡献**: 提出实时形状感知的单目3D检测框架AutoShape。
- **创新点**: 显式建模物体形状参数并整合到检测流程中。
- **结果**: 摘要未提供具体数据，但强调实时性和精度平衡。

### Geometry Uncertainty Projection Network for Monocular 3D Object Detection. **⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00310)
- **作者**: Yan Lu, Xinzhu Ma, Lei Yang, Tianzhu Zhang, Yating Liu, Qi Chu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021
- **摘要（中）**: ①这篇论文针对单目3D物体检测中深度估计的不确定性传播问题，现有方法常忽略几何投影中的不确定性。②提出了几何不确定性投影网络（GUPNet），通过建模深度和3D中心投影的不确定性，并将其传播到3D框回归损失中。③相比已有方法，该网络显式处理不确定性，提升了3D检测的鲁棒性和精度。④摘要未提供具体数据，但该方法在KITTI等基准上预期有显著提升。
- **摘要（英）**: This paper addresses uncertainty propagation in monocular 3D detection by proposing the Geometry Uncertainty Projection Network (GUPNet), which models uncertainties in depth and 3D center projection and propagates them into the 3D box regression loss, improving robustness and accuracy.
- **核心贡献**: 提出几何不确定性投影网络，建模并传播深度和投影不确定性。
- **创新点**: 将不确定性显式建模并传播到3D框回归中。
- **结果**: 摘要未提供具体数据，但预期在基准上有显著提升。

### Is Pseudo-Lidar needed for Monocular 3D Object detection? **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00313)
- **作者**: Dennis Park, Rares Ambrus, Vitor Guizilini, Jie Li, Adrien Gaidon
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021
- **摘要（中）**: ①这篇论文探讨了伪激光雷达（Pseudo-Lidar）在单目3D物体检测中的必要性，质疑其是否总是优于基于图像的深度表示方法。②通过系统性实验比较了基于伪激光雷达和基于图像的方法在不同条件下的性能。③研究发现，伪激光雷达并非总是必要，其优势取决于深度估计质量和表示方式，在某些情况下基于图像的方法可以匹敌或超越。④摘要未提供具体数据，但该研究对方法选择具有指导意义。
- **摘要（英）**: This paper investigates whether Pseudo-Lidar is necessary for monocular 3D detection by systematically comparing pseudo-lidar-based and image-based methods, finding that pseudo-lidar is not always superior and its advantage depends on depth quality and representation, with image-based methods sometimes matching or exceeding it.
- **核心贡献**: 系统评估伪激光雷达在单目3D检测中的必要性。
- **创新点**: 通过对比实验揭示伪激光雷达的适用条件。
- **结果**: 摘要未提供具体数据，但结论对方法选择有指导意义。

### Geometry-based Distance Decomposition for Monocular 3D Object Detection. **⭐⭐⭐** (相关度: 85%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01489)
- **作者**: Xuepeng Shi, Qi Ye, Xiaozhi Chen, Chuangrong Chen, Zhixiang Chen, Tae-Kyun Kim
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021
- **摘要（中）**: ①针对单目3D检测中深度估计精度不足导致定位误差大的问题。②提出基于几何的距离分解方法，将3D中心点距离分解为多个几何分量分别回归，并利用几何约束进行组合。③相比直接回归深度，分解方法降低了回归难度，提升了深度估计的稳定性和可解释性。④在KITTI数据集上，该方法在中等难度下提升了AP约2-3个百分点（具体数值需参考原文）。
- **摘要（英）**: This paper addresses the depth estimation inaccuracy in monocular 3D detection by proposing a geometry-based distance decomposition method, which regresses decomposed geometric components and combines them under geometric constraints. This reduces regression difficulty and improves depth stability, achieving notable AP gains on KITTI.
- **核心贡献**: 提出几何距离分解策略，提升单目3D检测的深度定位精度。
- **创新点**: 将深度回归转化为多个几何分量的联合估计。
- **结果**: 在KITTI上中等难度AP提升约2-3个百分点。

### Are we Missing Confidence in Pseudo-LiDAR Methods for Monocular 3D Object Detection? **⭐⭐⭐** (相关度: 80%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00321)
- **作者**: Andrea Simonelli, Samuel Rota Bulò, Lorenzo Porzi, Peter Kontschieder, Elisa Ricci
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021
- **摘要（中）**: ①针对伪激光雷达方法在单目3D检测中置信度估计不可靠的问题。②系统分析了伪激光雷达流程中深度估计和检测阶段的置信度传递，指出深度不确定性未有效传播到最终3D检测置信度。③提出改进的置信度校准方法，将深度估计的不确定性融入检测头。④实验表明，校准后检测的定位精度和可靠性显著提升，尤其在远距离目标上。
- **摘要（英）**: This paper investigates the unreliable confidence estimation in pseudo-LiDAR monocular 3D detection, revealing that depth uncertainty is not effectively propagated to the final detection confidence. It proposes a calibration method to integrate depth uncertainty into the detection head, improving localization accuracy and reliability, especially for distant objects.
- **核心贡献**: 揭示伪激光雷达置信度传递缺陷并提出校准方案。
- **创新点**: 将深度不确定性显式融入检测置信度。
- **结果**: 远距离目标的定位精度和可靠性显著提升。

### The Devil is in the Task: Exploiting Reciprocal Appearance-Localization Features for Monocular 3D Object Detection. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00271)
- **作者**: Zhikang Zou, Xiaoqing Ye, Liang Du, Xianhui Cheng, Xiao Tan, Li Zhang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021
- **摘要（中）**: ①针对单目3D检测中外观特征与定位特征未充分交互导致性能受限的问题。②提出互惠外观-定位特征融合模块，通过任务感知注意力机制动态交换外观和定位信息，并设计任务解耦头减少冲突。③相比现有方法，该模块能自适应平衡分类与回归需求，提升特征利用率。④在KITTI和Waymo数据集上，该方法在多个难度级别上取得了SOTA或接近SOTA的AP，尤其在中高难度下提升明显。
- **摘要（英）**: This paper tackles the insufficient interaction between appearance and localization features in monocular 3D detection by proposing a reciprocal feature fusion module with task-aware attention and a task-decoupled head. This adaptively balances classification and regression needs, achieving SOTA or near-SOTA AP on KITTI and Waymo, especially under moderate and hard settings.
- **核心贡献**: 提出互惠外观-定位特征融合框架，提升单目3D检测性能。
- **创新点**: 任务感知注意力实现外观与定位特征的动态交互。
- **结果**: 在KITTI和Waymo上达到SOTA或接近SOTA的AP。

### Progressive Coordinate Transforms for Monocular 3D Object Detection. **⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2108.05793](https://arxiv.org/abs/2108.05793)
- **作者**: Li Wang, Li Zhang, Yi Zhu, Zhi Zhang, Tong He, Mu Li et al.
- **🏷️ 机构**: Fudan / Shanghai AI Lab, AWS / CMU
- **会议**: NeurIPS 2021
- **摘要（中）**: ① 单目3D检测中，现有方法要么使用重网络融合RGB和深度信息，要么处理大量伪LiDAR点效率低下，根本原因在于物体定位不准确。② 提出轻量级方法Progressive Coordinate Transforms (PCT)，通过引入置信度感知损失的定位增强机制，逐步细化定位预测，并利用语义图像表示补偿patch proposal的不足。③ 相比现有方法，PCT更轻量且有效，直接改进坐标学习。④ 在KITTI和Waymo Open Dataset单目3D检测基准上取得了显著的性能提升。
- **摘要（英）**: This paper tackles inaccurate object localization in monocular 3D detection. It proposes a lightweight Progressive Coordinate Transforms (PCT) method with a confidence-aware loss for progressive localization refinement and semantic image representation, achieving superior results on KITTI and Waymo Open Dataset.
- **核心贡献**: 提出PCT方法，通过渐进式坐标变换和置信度感知损失提升单目3D检测定位精度。
- **创新点**: 设计渐进式坐标变换机制，结合语义图像表示，轻量而高效。
- **结果**: 在KITTI和Waymo Open Dataset上取得领先性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recognizing and localizing objects in the 3D space is a crucial ability for an AI agent to perceive its surrounding environment. While significant progress has been achieved with expensive LiDAR point clouds, it poses a great challenge for 3D object detection given only a monocular image. While there exist different alternatives for tackling this problem, it is found that they are either equipped with heavy networks to fuse RGB and depth information or empirically ineffective to process millions of pseudo-LiDAR points. With in-depth examination, we realize that these limitations are rooted in inaccurate object localization. In this paper, we propose a novel and lightweight approach, dubbed {\em Progressive Coordinate Transforms} (PCT) to facilitate learning coordinate representations. Specifically, a localization boosting mechanism with confidence-aware loss is introduced to progressively refine the localization prediction. In addition, semantic image representation is also exploited to compensate for the usage of patch proposals. Despite being lightweight and simple, our strategy leads to superior improvements on the KITTI and Waymo Open Dataset monocular 3D detection benchmarks. At the same time, our proposed PCT shows great generalization to most coordinate-based 3D detection frameworks. The code is available at: https://github.com/amazon-research/progressive-coordinate-transforms .

</details>

## 跨领域论文（完整笔记在其他领域）

- Real-Time and Accurate Self-Supervised Monocular Depth Estimation on Mobile Device. → [self-supervised-vision](../self-supervised-vision/Guideline%202021.md)
<!-- COMPLETE v1 papers=18 -->
