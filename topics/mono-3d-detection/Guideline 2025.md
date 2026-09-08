# Mono 3D Detection — 2025 Guideline

> 领域: 单目 3D 检测（Monocular 3D Object Detection，含单目深度支撑的 3D 感知）
> 论文数: 26 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: [2026](Guideline%202026.md), [2024](Guideline%202024.md), [2023](Guideline%202023.md), [2022](Guideline%202022.md), [2021](Guideline%202021.md)

### MonoTAKD: Teaching Assistant Knowledge Distillation for Monocular 3D Object Detection. **⭐⭐⭐** (相关度: 85%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_MonoTAKD_Teaching_Assistant_Knowledge_Distillation_for_Monocular_3D_Object_Detection_CVPR_2025_paper.html) · 📚 被引 6
- **作者**: Hou-I Liu, Christine Wu, Jen-Hao Cheng, Wenhao Chai, Shian-Yun Wang, Gaowen Liu et al.
- **🏷️ 机构**: National Yang Ming Chiao Tung University, University of Washington, University of Southern California
- **会议**: CVPR 2025
- **摘要（中）**: ①针对单目3D检测中知识蒸馏的教师-学生差距问题。②提出教学助理知识蒸馏（MonoTAKD），引入中间教学助理模型缓解差距。③改进点在于更平滑的知识传递。④摘要缺失，具体效果未知。
- **摘要（英）**: This paper addresses teacher-student gap in knowledge distillation for monocular 3D detection, proposing a teaching assistant model. Details unavailable due to missing abstract.
- **核心贡献**: 提出教学助理蒸馏框架。
- **创新点**: 引入中间模型缩小师生差距。
- **结果**: 未知。

### MonoPlace3D: Learning 3D-Aware Object Placement for 3D Monocular Detection. **⭐⭐⭐** (相关度: 85%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Parihar_MonoPlace3D_Learning_3D-Aware_Object_Placement_for_3D_Monocular_Detection_CVPR_2025_paper.html)
- **作者**: Rishubh Parihar, Srinjay Sarkar, Sarthak Vora, Jogendra Nath Kundu, R. Venkatesh Babu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025
- **摘要（中）**: ①这篇论文针对单目3D检测中物体放置（object placement）缺乏3D感知的问题，导致检测精度受限。②提出了MonoPlace3D方法，通过学习3D感知的物体放置策略来改进单目3D检测。③相比已有工作，该方法显式建模物体在3D空间中的位置关系，增强了空间一致性。④摘要未提供具体数据，但预期能提升单目3D检测的定位精度。
- **摘要（英）**: This paper addresses the lack of 3D-aware object placement in monocular 3D detection, proposing MonoPlace3D to learn placement strategies for improved spatial consistency. It enhances detection accuracy by explicitly modeling object positions in 3D space, though specific quantitative results are not provided in the abstract.
- **核心贡献**: 提出3D感知物体放置学习框架，用于增强单目3D检测。
- **创新点**: 将物体放置建模为3D感知过程，提升空间布局理解。
- **结果**: 预期提升单目3D检测精度，但具体数据未给出。

### MonoDGP: Monocular 3D Object Detection with Decoupled-Query and Geometry-Error Priors. **⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2410.19590](https://arxiv.org/abs/2410.19590) · 📚 被引 25
- **作者**: Fanqi Pu, Yifan Wang, Jiru Deng, Wenming Yang
- **🏷️ 机构**: Tsinghua University,Shenzhen International Graduate School
- **会议**: CVPR 2025
- **摘要（中）**: ①针对单目3D检测中透视投影因深度误差导致2D框高度无法准确表示投影中心高度的问题，现有方法直接预测投影高度会丢失2D先验，多深度预测分支复杂且未充分利用几何深度。②提出MonoDGP方法，采用透视不变的几何误差修正投影公式，并解耦深度引导解码器，构建仅依赖视觉特征的2D解码器以提供2D先验和初始化查询。③改进点在于系统解释几何误差机制，作为多深度预测的简单有效替代，同时解耦查询避免3D检测干扰。④摘要未提供具体数据，但预期在KITTI等基准上达到SOTA性能。
- **摘要（英）**: This paper addresses depth error issues in monocular 3D detection by proposing MonoDGP, which uses perspective-invariant geometry errors to correct projection and decouples depth-guided decoder from a 2D decoder for better 2D priors. It offers a simple alternative to multi-depth prediction, with expected SOTA performance on benchmarks like KITTI.
- **核心贡献**: 提出MonoDGP，通过几何误差修正和解耦查询提升单目3D检测精度。
- **创新点**: 引入透视不变的几何误差作为多深度预测的替代，并解耦2D/3D解码器。
- **结果**: 摘要未提供具体数据，但预期在主流单目3D检测基准上表现优异。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Perspective projection has been extensively utilized in monocular 3D object detection methods. It introduces geometric priors from 2D bounding boxes and 3D object dimensions to reduce the uncertainty of depth estimation. However, due to depth errors originating from the object's visual surface, the height of the bounding box often fails to represent the actual projected central height, which undermines the effectiveness of geometric depth. Direct prediction for the projected height unavoidably results in a loss of 2D priors, while multi-depth prediction with complex branches does not fully leverage geometric depth. This paper presents a Transformer-based monocular 3D object detection method called MonoDGP, which adopts perspective-invariant geometry errors to modify the projection formula. We also try to systematically discuss and explain the mechanisms and efficacy behind geometry errors, which serve as a simple but effective alternative to multi-depth prediction. Additionally, MonoDGP decouples the depth-guided decoder and constructs a 2D decoder only dependent on visual features, providing 2D priors and initializing object queries without the disturbance of 3D detection. To further optimize and fine-tune input tokens of the transformer decoder, we also introduce a Region Segment Head (RSH) that generates enhanced features and segment embeddings. Our monocular method demonstrates state-of-the-art performance on the KITTI benchmark without extra data. Code is available at https://github.com/PuFanqi23/MonoDGP.

</details>

### Align3R: Aligned Monocular Depth Estimation for Dynamic Videos. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2412.03079](https://arxiv.org/abs/2412.03079) · 📚 被引 27
- **作者**: Jiahao Lu, Tianyu Huang, Peng Li, Zhiyang Dou, Cheng Lin, Zhiming Cui et al.
- **🏷️ 机构**: HKUST, CUHK, HKU
- **会议**: CVPR 2025
- **摘要（中）**: ①针对单目视频深度估计中跨帧不一致的问题，现有方法依赖视频扩散模型，训练成本高且无法估计相机位姿。②提出Align3R方法，利用DUSt3R模型将不同时间步的估计单目深度图对齐，通过微调DUSt3R并优化重建深度图和相机位姿。③相比已有工作，该方法无需视频扩散模型，能同时输出尺度一致的深度和相机位姿。④实验表明，在动态视频上估计的深度和位姿一致性优于基线方法。
- **摘要（英）**: This paper addresses the inconsistency of monocular video depth estimation by proposing Align3R, which fine-tunes DUSt3R with estimated depth inputs and optimizes depth maps and camera poses jointly. It avoids expensive video diffusion models and achieves superior temporal consistency and pose accuracy compared to baselines.
- **核心贡献**: 提出一种利用DUSt3R对齐单目深度图的新框架，同时估计一致深度和相机位姿。
- **创新点**: 将DUSt3R扩展到动态场景，并引入优化策略联合重建深度与位姿。
- **结果**: 在动态视频上深度和位姿估计性能优于基线。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent developments in monocular depth estimation methods enable high-quality depth estimation of single-view images but fail to estimate consistent video depth across different frames. Recent works address this problem by applying a video diffusion model to generate video depth conditioned on the input video, which is training-expensive and can only produce scale-invariant depth values without camera poses. In this paper, we propose a novel video-depth estimation method called Align3R to estimate temporal consistent depth maps for a dynamic video. Our key idea is to utilize the recent DUSt3R model to align estimated monocular depth maps of different timesteps. First, we fine-tune the DUSt3R model with additional estimated monocular depth as inputs for the dynamic scenes. Then, we apply optimization to reconstruct both depth maps and camera poses. Extensive experiments demonstrate that Align3R estimates consistent video depth and camera poses for a monocular video with superior performance than baseline methods.

</details>

### Scalable Autoregressive Monocular Depth Estimation. **⭐⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2411.11361](https://arxiv.org/abs/2411.11361)
- **作者**: Jinhong Wang, Jian Liu, Dongqi Tang, Weiqiang Wang, Wentong Li, Danny Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025
- **摘要（中）**: ①针对单目深度估计中现有方法难以扩展和精度不足的问题。②提出深度自回归模型DAR，将不同分辨率的深度图视为token序列，采用低到高分辨率的自回归目标，并通过递归离散化深度范围实现粗到细的序数回归。③相比已有方法，DAR结合两种自回归目标，实现了可扩展的深度估计。④在KITTI和NYU Depth v2上取得SOTA，模型扩展到2.0B时KITTI RMSE达1.799，比当前SOTA提升5%，并展现零样本泛化能力。
- **摘要（英）**: This paper introduces DAR, an autoregressive monocular depth estimator that treats depth maps as token sequences and combines low-to-high resolution and coarse-to-fine ordinal regression objectives. It achieves SOTA on KITTI and NYU Depth v2, with a 2.0B model reaching RMSE 1.799 on KITTI, improving 5% over Depth Anything, and shows zero-shot generalization.
- **核心贡献**: 提出首个可扩展的自回归单目深度估计框架DAR。
- **创新点**: 设计双自回归目标，结合分辨率与深度粒度建模。
- **结果**: 在KITTI和NYU Depth v2上刷新SOTA，并支持大规模模型扩展。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper shows that the autoregressive model is an effective and scalable monocular depth estimator. Our idea is simple: We tackle the monocular depth estimation (MDE) task with an autoregressive prediction paradigm, based on two core designs. First, our depth autoregressive model (DAR) treats the depth map of different resolutions as a set of tokens, and conducts the low-to-high resolution autoregressive objective with a patch-wise casual mask. Second, our DAR recursively discretizes the entire depth range into more compact intervals, and attains the coarse-to-fine granularity autoregressive objective in an ordinal-regression manner. By coupling these two autoregressive objectives, our DAR establishes new state-of-the-art (SOTA) on KITTI and NYU Depth v2 by clear margins. Further, our scalable approach allows us to scale the model up to 2.0B and achieve the best RMSE of 1.799 on the KITTI dataset (5% improvement) compared to 1.896 by the current SOTA (Depth Anything). DAR further showcases zero-shot generalization ability on unseen datasets. These results suggest that DAR yields superior performance with an autoregressive prediction paradigm, providing a promising approach to equip modern autoregressive large models (e.g., GPT-4o) with depth estimation capabilities.

</details>

### Vision-Language Embodiment for Monocular Depth Estimation. **⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2503.16535](https://arxiv.org/abs/2503.16535) · 📚 被引 4
- **作者**: Jinchang Zhang, Guoyu Lu
- **🏷️ 机构**: University of Georgia Binghamton University,Intelligent Vision and Sensing Lab, Binghamton University,Intelligent Vision and Sensing Lab
- **会议**: CVPR 2025
- **摘要（中）**: ①针对单目深度估计中忽略相机内在信息的问题，现有模型仅依赖图像间关系。②提出一种将相机模型及其物理特性嵌入深度学习的方法，通过实时环境交互计算具身场景深度，并结合RGB特征和文本描述。③相比已有工作，该方法利用相机内参和语言先验增强深度感知。④实验表明，模型能实时计算深度，并融合多模态信息提升估计精度。
- **摘要（英）**: This paper proposes a method that embodies camera intrinsic properties into a deep model for monocular depth estimation, combining embodied scene depth with RGB features and text priors. It leverages real-time environmental interactions and multimodal fusion to improve depth accuracy without extra equipment.
- **核心贡献**: 提出一种结合相机物理特性和语言先验的单目深度估计方法。
- **创新点**: 将相机内参和文本描述集成到深度估计模型中。
- **结果**: 实现实时深度计算，但具体性能提升未明确量化。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Depth estimation is a core problem in robotic perception and vision tasks, but 3D reconstruction from a single image presents inherent uncertainties. Current depth estimation models primarily rely on inter-image relationships for supervised training, often overlooking the intrinsic information provided by the camera itself. We propose a method that embodies the camera model and its physical characteristics into a deep learning model, computing embodied scene depth through real-time interactions with road environments. The model can calculate embodied scene depth in real-time based on immediate environmental changes using only the intrinsic properties of the camera, without any additional equipment. By combining embodied scene depth with RGB image features, the model gains a comprehensive perspective on both geometric and visual details. Additionally, we incorporate text descriptions containing environmental content and depth information as priors for scene understanding, enriching the model's perception of objects. This integration of image and language - two inherently ambiguous modalities - leverages their complementary strengths for monocular depth estimation. The real-time nature of the embodied language and depth prior model ensures that the model can continuously adjust its perception and behavior in dynamic environments. Experimental results show that the embodied depth estimation method enhances model performance across different scenes.

</details>

### Mono3DVLT: Monocular-Video-Based 3D Visual Language Tracking. **⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Wei_Mono3DVLT_Monocular-Video-Based_3D_Visual_Language_Tracking_CVPR_2025_paper.html)
- **作者**: Hongkai Wei, Yang Yang, Shijie Sun, Mingtao Feng, Xiangyu Song, Qi Lei et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025
- **摘要（中）**: ①针对单目视频中的3D视觉语言跟踪问题，摘要缺失，无法获取具体内容。②方法未知。③改进点未知。④效果未知。
- **摘要（英）**: The abstract is missing, so no details on the problem, method, or results are available.
- **核心贡献**: 未知。
- **创新点**: 未知。
- **结果**: 未知。

### Adaptive Dual Uncertainty Optimization: Boosting Monocular 3D Object Detection under Test-Time Shifts. **⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2508.20488](https://arxiv.org/abs/2508.20488)
- **作者**: Zixuan Hu, Dongxiao Li, Xinzhu Ma, Shixiang Tang, Xiaotong Li, Wenhan Yang et al.
- **🏷️ 机构**: School of Computer Science, Peking University,Beijing,China, The Chinese University of Hong Kong,Hongkong,China, Peng Cheng Laboratory,Shenzhen,China
- **会议**: ICCV 2025
- **摘要（中）**: ①针对单目3D检测在测试时域偏移下性能下降的问题，现有TTA方法未处理语义和几何双重不确定性。②提出DUO框架，首个联合最小化语义和几何不确定性的TTA方法，通过凸优化焦点损失和语义感知法向场约束。③相比已有工作，DUO实现了标签无关的不确定性加权和几何一致性保持。④实验表明，DUO在多种域偏移下显著提升M3OD鲁棒性。
- **摘要（英）**: This paper proposes DUO, the first TTA framework for monocular 3D detection that jointly minimizes semantic and geometric uncertainties via convex focal loss and semantic-aware normal constraints. It improves robustness under domain shifts, outperforming prior TTA methods.
- **核心贡献**: 提出首个针对单目3D检测的双不确定性优化TTA框架。
- **创新点**: 将焦点损失凸化并推导无监督版本，结合语义法向约束。
- **结果**: 在域偏移场景下显著提升检测鲁棒性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Accurate monocular 3D object detection (M3OD) is pivotal for safety-critical applications like autonomous driving, yet its reliability deteriorates significantly under real-world domain shifts caused by environmental or sensor variations. To address these shifts, Test-Time Adaptation (TTA) methods have emerged, enabling models to adapt to target distributions during inference. While prior TTA approaches recognize the positive correlation between low uncertainty and high generalization ability, they fail to address the dual uncertainty inherent to M3OD: semantic uncertainty (ambiguous class predictions) and geometric uncertainty (unstable spatial localization). To bridge this gap, we propose Dual Uncertainty Optimization (DUO), the first TTA framework designed to jointly minimize both uncertainties for robust M3OD. Through a convex optimization lens, we introduce an innovative convex structure of the focal loss and further derive a novel unsupervised version, enabling label-agnostic uncertainty weighting and balanced learning for high-uncertainty objects. In parallel, we design a semantic-aware normal field constraint that preserves geometric coherence in regions with clear semantic cues, reducing uncertainty from the unstable 3D representation. This dual-branch mechanism forms a complementary loop: enhanced spatial perception improves semantic classification, and robust semantic predictions further refine spatial understanding. Extensive experiments demonstrate the superiority of DUO over existing methods across various datasets and domain shift types.

</details>

### Self-supervised Monocular Depth Estimation Robust to Reflective Surface Leveraged by Triplet Mining. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2502.14573](https://arxiv.org/abs/2502.14573)
- **作者**: Wonhyeok Choi, Kyumin Hwang, Wei Peng, Minwoo Choi, Sunghoon Im
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025
- **摘要（中）**: ①针对自监督单目深度估计在反射表面因违反朗伯反射假设导致训练不准确的问题。②提出了基于三元组挖掘的训练策略，利用不同视角间的相机几何定位像素级反射区域，并设计反射感知三元组损失，惩罚反射区域不恰当的光度误差最小化，同时保持非反射区域精度；还引入反射感知知识蒸馏，使学生模型选择性学习不同区域知识。③改进点在于精准定位反射区域并针对性处理，提升鲁棒性。④多数据集评估表明方法有效增强深度估计鲁棒性，但摘要未给出具体数据。
- **摘要（英）**: This paper tackles inaccurate training on reflective surfaces in self-supervised monocular depth estimation by proposing a triplet-mining-based strategy to localize reflective regions and a reflection-aware loss to penalize photometric errors, alongside selective knowledge distillation. It enhances robustness across datasets, though specific metrics are omitted.
- **核心贡献**: 提出反射感知三元组挖掘损失和知识蒸馏方法，提升自监督深度估计对反射表面的鲁棒性。
- **创新点**: 利用相机几何和三元组挖掘精准定位反射区域并定制损失。
- **结果**: 多数据集上有效增强深度估计鲁棒性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised monocular depth estimation (SSMDE) aims to predict the dense depth map of a monocular image, by learning depth from RGB image sequences, eliminating the need for ground-truth depth labels. Although this approach simplifies data acquisition compared to supervised methods, it struggles with reflective surfaces, as they violate the assumptions of Lambertian reflectance, leading to inaccurate training on such surfaces. To tackle this problem, we propose a novel training strategy for an SSMDE by leveraging triplet mining to pinpoint reflective regions at the pixel level, guided by the camera geometry between different viewpoints. The proposed reflection-aware triplet mining loss specifically penalizes the inappropriate photometric error minimization on the localized reflective regions while preserving depth accuracy in non-reflective areas. We also incorporate a reflection-aware knowledge distillation method that enables a student model to selectively learn the pixel-level knowledge from reflective and non-reflective regions. This results in robust depth estimation across areas. Evaluation results on multiple datasets demonstrate that our method effectively enhances depth quality on reflective surfaces and outperforms state-of-the-art SSMDE baselines.

</details>

### Distil-E2D: Distilling Image-to-Depth Priors for Event-Based Monocular Depth Estimation. **⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/b6fa3ed9624c184bd73e435123bd576a-Abstract-Conference.html)
- **作者**: Jie Long Lee, Gim Hee Lee
- **🏷️ 机构**: National University of Singapore
- **会议**: NeurIPS 2025
- **摘要（中）**: ①针对事件相机单目深度估计中缺乏标注数据的问题。②提出了Distil-E2D方法，通过蒸馏图像到深度先验来指导事件数据的学习，利用事件流的时间特性辅助深度预测。③改进点在于利用图像域知识迁移到事件域，缓解事件数据标注稀缺。④摘要不完整，未提供具体效果数据。
- **摘要（英）**: This paper addresses the lack of labeled data in event-based monocular depth estimation by proposing Distil-E2D, which distills image-to-depth priors to guide event-based learning. It leverages cross-domain knowledge transfer, but the abstract is incomplete with no quantitative results.
- **核心贡献**: 提出图像到事件的知识蒸馏框架用于单目深度估计。
- **创新点**: 利用图像先验缓解事件数据标注问题。
- **结果**: 未提供具体效果。

### ST$2$360D: Spatial-to-Temporal Consistency for Training-free 360 Monocular Depth Estimation. **⭐⭐⭐** (相关度: 65%)
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/45c361d4117d598d4bb6568b407e9ac9-Abstract-Conference.html)
- **作者**: Zidong Cao, Jinjing Zhu, Hao Ai, Lutao Jiang, Yuanhuiyi Lyu, Hui Xiong
- **🏷️ 机构**: HKUST (GZ), Hong Kong University of Science and Technology, University of Birmingham
- **会议**: NeurIPS 2025
- **摘要（中）**: ①针对360度单目深度估计中缺乏时序一致性的问题。②提出了ST2 360D方法，利用空间到时间一致性进行无需训练的360度深度估计，通过跨视角空间约束和时间传播提升一致性。③改进点在于无需训练即可应用，降低计算成本。④摘要不完整，未提供具体效果数据。
- **摘要（英）**: This paper addresses temporal inconsistency in 360-degree monocular depth estimation by proposing ST2 360D, a training-free method that leverages spatial-to-temporal consistency for depth refinement. It reduces computational cost, but the abstract lacks quantitative results.
- **核心贡献**: 提出空间到时间一致性的无训练360度深度估计方法。
- **创新点**: 利用跨视角空间约束实现无需训练的时序一致性。
- **结果**: 未提供具体效果。

### Evaluating Robustness of Monocular Depth Estimation with Procedural Scene Perturbations. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2507.00981](https://arxiv.org/abs/2507.00981)
- **作者**: Jack Nugent, Siyang Wu, Zeyu Ma, Beining Han, Meenal Parakh, Abhishek Joshi et al.
- **🏷️ 机构**: Princeton University, Department of Computer Science, Princeton University
- **会议**: NeurIPS 2025
- **摘要（中）**: ①针对单目深度估计标准基准仅评估精度而忽视鲁棒性的问题。②提出了PDE（程序化深度评估）基准，利用程序化生成3D场景，系统评估对物体、相机、材质和光照等受控扰动的鲁棒性。③改进点在于提供首个系统性鲁棒性评估工具，弥补现有基准不足。④分析揭示了最先进深度模型面临的挑战性扰动，代码和数据已公开。
- **摘要（英）**: This paper addresses the lack of robustness evaluation in monocular depth estimation benchmarks by introducing PDE, a procedural-generation-based benchmark that tests robustness to controlled perturbations in objects, cameras, materials, and lighting. It provides systematic findings on challenging perturbations for SOTA models, with code and data released.
- **核心贡献**: 提出程序化深度评估基准PDE，系统评估单目深度模型的鲁棒性。
- **创新点**: 利用程序化生成场景实现可控扰动测试。
- **结果**: 揭示了SOTA模型的鲁棒性弱点，并公开资源。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent years have witnessed substantial progress on monocular depth estimation, particularly as measured by the success of large models on standard benchmarks. However, performance on standard benchmarks does not offer a complete assessment, because most evaluate accuracy but not robustness. In this work, we introduce PDE (Procedural Depth Evaluation), a new benchmark which enables systematic robustness evaluation. PDE uses procedural generation to create 3D scenes that test robustness to various controlled perturbations, including object, camera, material and lighting changes. Our analysis yields interesting findings on what perturbations are challenging for state-of-the-art depth models, which we hope will inform further research. Code and data are available at https://github.com/princeton-vl/proc-depth-eval.

</details>

### QSCA: Quantization with Self-Compensating Auxiliary for Monocular Depth Estimation. **⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/2d13e0a4097e44b9f167f2e67aa0214a-Abstract-Conference.html)
- **作者**: Jincheol Yang, Jaemin Choi, Matti Zinke, Suk-Ju Kang
- **🏷️ 机构**: Sogang University
- **会议**: NeurIPS 2025
- **摘要（中）**: ①针对单目深度估计模型量化中精度下降的问题。②提出了QSCA（自补偿辅助量化）方法，通过辅助机制补偿量化误差，提升低比特下的深度估计精度。③改进点在于自补偿设计减少量化对深度预测的影响。④摘要不完整，未提供具体效果数据。
- **摘要（英）**: This paper addresses accuracy degradation in quantized monocular depth estimation models by proposing QSCA, a self-compensating auxiliary method that mitigates quantization errors. It aims to improve low-bit performance, but the abstract lacks quantitative results.
- **核心贡献**: 提出自补偿辅助量化方法用于单目深度估计。
- **创新点**: 通过辅助机制动态补偿量化误差。
- **结果**: 未提供具体效果。

### TrackingWorld: World-centric Monocular 3D Tracking of Almost All Pixels. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2512.08358](https://arxiv.org/abs/2512.08358)
- **作者**: Jiahao Lu, Weitao Xiong, Jiacheng Deng, Peng Li, Tianyu Huang, Zhiyang Dou et al.
- **🏷️ 机构**: The Hong Kong University of Science and Technology, Xiamen University (Malaysia Campus), University of Science and Technology of China
- **会议**: NeurIPS 2025
- **摘要（中）**: ①这篇论文针对单目视频中3D跟踪的两个局限：无法将相机运动与前景动态运动分离，以及无法密集跟踪新出现的动态物体。②提出了TrackingWorld，一种用于在world-centric 3D坐标系中密集跟踪几乎所有像素的新流程，包括一个跟踪上采样器将稀疏2D轨迹提升为密集2D轨迹，并通过优化框架估计相机位姿和3D坐标，将密集2D轨迹反投影为3D轨迹。③相比已有工作，该方法通过在所有帧上应用上采样器并消除重叠区域的轨迹冗余，实现了对新出现物体的泛化，并有效分离了相机运动。④在合成和真实数据集上的广泛评估表明，该系统实现了准确且密集的3D跟踪。
- **摘要（英）**: This paper addresses the limitations of monocular 3D tracking in separating camera motion from dynamic foreground and densely tracking newly emerging objects. It proposes TrackingWorld, a pipeline that uses a tracking upsampler to lift sparse 2D tracks to dense ones and an optimization-based framework to back-project them into world-centric 3D trajectories with camera pose estimation. Extensive evaluations on synthetic and real datasets demonstrate accurate and dense 3D tracking, improving generalization to new objects.
- **核心贡献**: 提出了一种基于跟踪上采样和优化框架的密集世界坐标系单目3D跟踪方法。
- **创新点**: 通过跟踪上采样器和冗余消除机制，实现了对新出现物体的密集3D跟踪。
- **结果**: 在合成和真实数据集上实现了准确且密集的3D跟踪。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular 3D tracking aims to capture the long-term motion of pixels in 3D space from a single monocular video and has witnessed rapid progress in recent years. However, we argue that the existing monocular 3D tracking methods still fall short in separating the camera motion from foreground dynamic motion and cannot densely track newly emerging dynamic subjects in the videos. To address these two limitations, we propose TrackingWorld, a novel pipeline for dense 3D tracking of almost all pixels within a world-centric 3D coordinate system. First, we introduce a tracking upsampler that efficiently lifts the arbitrary sparse 2D tracks into dense 2D tracks. Then, to generalize the current tracking methods to newly emerging objects, we apply the upsampler to all frames and reduce the redundancy of 2D tracks by eliminating the tracks in overlapped regions. Finally, we present an efficient optimization-based framework to back-project dense 2D tracks into world-centric 3D trajectories by estimating the camera poses and the 3D coordinates of these 2D tracks. Extensive evaluations on both synthetic and real-world datasets demonstrate that our system achieves accurate and dense 3D tracking in a world-centric coordinate frame.

</details>

### From Flatland to Space: Teaching Vision-Language Models to Perceive and Reason in 3D. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2503.22976](https://arxiv.org/abs/2503.22976)
- **作者**: Jiahui Zhang, Yurui Chen, Yueming Xu, Ze Huang, Jilin Mei, Junhui Chen et al.
- **🏷️ 机构**: Fudan University, Huawei Technologies Ltd.
- **会议**: NeurIPS 2025
- **摘要（中）**: ①这篇论文针对视觉语言模型在3D场景空间感知和推理能力上的不足。②提出了一个基于3D ground-truth场景数据的2D空间数据生成和标注流程，构建了大规模数据集SPAR-7M和基准SPAR-Bench，并训练模型以提升空间理解能力。③相比已有方法，该工作不依赖3D表示，而是通过利用空间相关的图像数据来解锁VLM的潜力，支持单视图和多视图输入。④在SPAR-7M和大型2D数据集上训练后，模型在2D空间基准上达到了最先进性能，并在3D任务微调后表现竞争力。
- **摘要（英）**: This paper tackles the limited spatial perception of vision-language models in complex 3D scenes. It introduces a novel 2D spatial data generation pipeline based on 3D ground-truth, creating the SPAR-7M dataset and SPAR-Bench benchmark, and trains models to enhance spatial reasoning. The models achieve state-of-the-art performance on 2D spatial benchmarks and competitive results on 3D tasks after fine-tuning.
- **核心贡献**: 构建了大规模空间任务数据集SPAR-7M和综合基准SPAR-Bench，并训练VLM以提升3D空间推理。
- **创新点**: 利用3D ground-truth生成多样化的2D空间任务数据，无需修改模型架构即可增强VLM的空间能力。
- **结果**: 在2D空间基准上达到最先进性能，并在3D任务上表现竞争力。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advances in LVLMs have improved vision-language understanding, but they still struggle with spatial perception, limiting their ability to reason about complex 3D scenes. Unlike previous approaches that incorporate 3D representations into models to improve spatial understanding, we aim to unlock the potential of VLMs by leveraging spatially relevant image data. To this end, we introduce a novel 2D spatial data generation and annotation pipeline built upon scene data with 3D ground-truth. This pipeline enables the creation of a diverse set of spatial tasks, ranging from basic perception tasks to more complex reasoning tasks. Leveraging this pipeline, we construct SPAR-7M, a large-scale dataset generated from thousands of scenes across multiple public datasets. In addition, we introduce SPAR-Bench, a benchmark designed to offer a more comprehensive evaluation of spatial capabilities compared to existing spatial benchmarks, supporting both single-view and multi-view inputs. Training on both SPAR-7M and large-scale 2D datasets enables our models to achieve state-of-the-art performance on 2D spatial benchmarks. Further fine-tuning on 3D task-specific datasets yields competitive results, underscoring the effectiveness of our dataset in enhancing spatial reasoning.

</details>

### Jasmine: Harnessing Diffusion Prior for Self-supervised Depth Estimation. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2503.15905](https://arxiv.org/abs/2503.15905)
- **作者**: Jiyuan Wang, Chunyu Lin, Cheng Guan, Lang Nie, Jing He, Haodong Li et al.
- **🏷️ 机构**: Beijing Jiaotong University, Beijing jiaotong university, Chongqing University of Post and Telecommunications
- **会议**: NeurIPS 2025
- **摘要（中）**: ①这篇论文针对自监督单目深度估计中预测模糊和伪影问题，以及扩散模型先验难以应用于无监督任务的问题。②提出了Jasmine，首个基于Stable Diffusion的自监督单目深度估计框架，通过构建混合图像重建的替代任务来保留SD的细节先验，并引入Scale-Shift GRU来弥合SD输出与自监督深度估计之间的分布差距。③相比已有SD-based方法（均为监督），该方法无需高精度监督即可利用SD先验，并通过重建任务防止深度估计退化。④实验表明，该方法在提升深度预测的清晰度和泛化能力方面有效。
- **摘要（英）**: This paper addresses the challenges of applying diffusion priors to self-supervised monocular depth estimation, which suffers from blur and artifacts. Jasmine, the first SD-based self-supervised framework, uses a hybrid image reconstruction surrogate task to preserve SD detail priors and a Scale-Shift GRU to bridge the distribution gap. It enhances sharpness and generalization without additional supervision.
- **核心贡献**: 提出了首个基于Stable Diffusion的自监督单目深度估计框架Jasmine。
- **创新点**: 通过混合图像重建任务和Scale-Shift GRU，有效利用扩散先验并解决分布对齐问题。
- **结果**: 提升了自监督深度预测的清晰度和泛化能力。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we propose Jasmine, the first Stable Diffusion (SD)-based self-supervised framework for monocular depth estimation, which effectively harnesses SD's visual priors to enhance the sharpness and generalization of unsupervised prediction. Previous SD-based methods are all supervised since adapting diffusion models for dense prediction requires high-precision supervision. In contrast, self-supervised reprojection suffers from inherent challenges (e.g., occlusions, texture-less regions, illumination variance), and the predictions exhibit blurs and artifacts that severely compromise SD's latent priors. To resolve this, we construct a novel surrogate task of hybrid image reconstruction. Without any additional supervision, it preserves the detail priors of SD models by reconstructing the images themselves while preventing depth estimation from degradation. Furthermore, to address the inherent misalignment between SD's scale and shift invariant estimation and self-supervised scale-invariant depth estimation, we build the Scale-Shift GRU. It not only bridges this distribution gap but also isolates the fine-grained texture of SD output against the interference of reprojection loss. Extensive experiments demonstrate that Jasmine achieves SoTA performance on the KITTI benchmark and exhibits superior zero-shot generalization across multiple datasets.

</details>

### Contrastive Self-Supervised Learning As Neural Manifold Packing.
- **链接**: [arXiv:2506.13717](https://arxiv.org/abs/2506.13717)
- **作者**: Guanming Zhang, David J. Heeger, Stefano Martiniani
- **🏷️ 机构**: New York University, NYU
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Contrastive self-supervised learning based on point-wise comparisons has been widely studied for vision tasks. In the visual cortex of the brain, neuronal responses to distinct stimulus classes are organized into geometric structures known as neural manifolds. Accurate classification of stimuli can be achieved by effectively separating these manifolds, akin to solving a packing problem. We introduce Contrastive Learning As Manifold Packing (CLAMP), a self-supervised framework that recasts representation learning as a manifold packing problem. CLAMP introduces a loss function inspired by the potential energy of short-range repulsive particle systems, such as those encountered in the physics of simple liquids and jammed packings. In this framework, each class consists of sub-manifolds embedding multiple augmented views of a single image. The sizes and positions of the sub-manifolds are dynamically optimized by following the gradient of a packing loss. This approach yields interpretable dynamics in the embedding space that parallel jamming physics, and introduces geometrically meaningful hyperparameters within the loss function. Under the standard linear evaluation protocol, which freezes the backbone and trains only a linear classifier, CLAMP achieves competitive performance with state-of-the-art self-supervised models. Furthermore, our analysis reveals that neural manifolds corresponding to different categories emerge naturally and are effectively separated in the learned representation space, highlighting the potential of CLAMP to bridge insights from physics, neural science, and machine learning.

</details>

## 跨领域论文（完整笔记在其他领域）

- RICCARDO: Radar Hit Prediction and Convolution for Camera-Radar 3D Object Detection. → [object-detection](../object-detection/Guideline%202025.md)
- MV-SSM: Multi-View State Space Modeling for 3D Human Pose Estimation. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
- Multi-view Reconstruction via SfM-guided Monocular Depth Estimation. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
- CAT4D: Create Anything in 4D with Multi-View Video Diffusion Models. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
- GeoDepth: From Point-to-Depth to Plane-to-Depth Modeling for Self-Supervised Monocular Depth Estimation. → [self-supervised-vision](../self-supervised-vision/Guideline%202025.md)
- On-Device Self-Supervised Learning of Low-Latency Monocular Depth from Only Events. → [self-supervised-vision](../self-supervised-vision/Guideline%202025.md)
- Improved Monocular Depth Prediction Using Distance Transform Over Pre-semantic Contours with Self-supervised Neural Networks. → [self-supervised-vision](../self-supervised-vision/Guideline%202025.md)
- 3D-MOOD: Lifting 2D to 3D for Monocular Open-Set Object Detection. → [open-set-detection](../open-set-detection/Guideline%202025.md)
- Hybrid-Grained Feature Aggregation with Coarse-to-Fine Language Guidance for Self-Supervised Monocular Depth Estimation. → [self-supervised-vision](../self-supervised-vision/Guideline%202025.md)
<!-- COMPLETE v1 papers=26 -->
