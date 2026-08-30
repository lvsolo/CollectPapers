# Occupancy — 2024 Guideline

> 领域: 占用栅格 / 占用网络（Occupancy Prediction / Occ3D）
> 论文数: 3 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份:

### RadarOcc: Robust 3D Occupancy Prediction with 4D Imaging Radar. **⭐⭐⭐⭐** (相关度: 88%)
- **链接**: [arXiv:2405.14014](https://arxiv.org/abs/2405.14014) · 📚 被引 26
- **作者**: Fangqiang Ding, Xiangyu Wen, Yunzhou Zhu, Yiming Li, Chris Xiaoxuan Lu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024
- **摘要（中）**: ①针对恶劣天气下LiDAR和相机占用预测鲁棒性不足的问题。②提出RadarOcc，利用4D成像雷达张量直接处理，采用多普勒描述符、旁瓣感知稀疏化和距离自注意力。③相比稀疏点云方法，保留更多场景细节并减少坐标变换误差。④在基准上展示了鲁棒的占用预测性能。
- **摘要（英）**: This paper addresses the robustness issue of occupancy prediction in adverse weather. It proposes RadarOcc using 4D imaging radar tensors with Doppler descriptors and range-wise attention. This preserves details and reduces errors, achieving robust performance on benchmarks.
- **核心贡献**: 首次利用4D雷达张量进行占用预测。
- **创新点**: 设计多普勒描述符和球面特征聚合。
- **结果**: 在恶劣条件下保持高精度占用预测。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D occupancy-based perception pipeline has significantly advanced autonomous driving by capturing detailed scene descriptions and demonstrating strong generalizability across various object categories and shapes. Current methods predominantly rely on LiDAR or camera inputs for 3D occupancy prediction. These methods are susceptible to adverse weather conditions, limiting the all-weather deployment of self-driving cars. To improve perception robustness, we leverage the recent advances in automotive radars and introduce a novel approach that utilizes 4D imaging radar sensors for 3D occupancy prediction. Our method, RadarOcc, circumvents the limitations of sparse radar point clouds by directly processing the 4D radar tensor, thus preserving essential scene details. RadarOcc innovatively addresses the challenges associated with the voluminous and noisy 4D radar data by employing Doppler bins descriptors, sidelobe-aware spatial sparsification, and range-wise self-attention mechanisms. To minimize the interpolation errors associated with direct coordinate transformations, we also devise a spherical-based feature encoding followed by spherical-to-Cartesian feature aggregation. We benchmark various baseline methods based on distinct modalities on the public K-Radar dataset. The results demonstrate RadarOcc's state-of-the-art performance in radar-based 3D occupancy prediction and promising results even when compared with LiDAR- or camera-based methods. Additionally, we present qualitative evidence of the superior performance of 4D radar in adverse weather conditions and explore the impact of key pipeline components through ablation studies.

</details>

### OctreeOcc: Efficient and Multi-Granularity Occupancy Prediction Using Octree Queries. **⭐⭐⭐⭐⭐** (相关度: 92%)
- **链接**: [arXiv:2312.03774](https://arxiv.org/abs/2312.03774) · 📚 被引 21
- **作者**: Yuhang Lu, Xinge Zhu, Tai Wang, Yuexin Ma
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024
- **摘要（中）**: ①针对密集网格占用预测计算量大且小物体细节丢失的问题。②提出OctreeOcc，利用八叉树表示自适应捕捉3D信息，结合图像语义优化初始结构并迭代修正。③相比密集网格方法，提供可变粒度并降低计算开销。④在基准上超越SOTA，计算量减少15%-24%。
- **摘要（英）**: This paper addresses the high computation and detail loss in dense grid occupancy prediction. It proposes OctreeOcc using octree representation with semantic refinement. This offers variable granularity and reduces computation by 15%-24%, surpassing SOTA.
- **核心贡献**: 提出基于八叉树的占用预测框架。
- **创新点**: 利用图像语义迭代优化八叉树结构。
- **结果**: 超越SOTA并显著降低计算开销。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Occupancy prediction has increasingly garnered attention in recent years for its fine-grained understanding of 3D scenes. Traditional approaches typically rely on dense, regular grid representations, which often leads to excessive computational demands and a loss of spatial details for small objects. This paper introduces OctreeOcc, an innovative 3D occupancy prediction framework that leverages the octree representation to adaptively capture valuable information in 3D, offering variable granularity to accommodate object shapes and semantic regions of varying sizes and complexities. In particular, we incorporate image semantic information to improve the accuracy of initial octree structures and design an effective rectification mechanism to refine the octree structure iteratively. Our extensive evaluations show that OctreeOcc not only surpasses state-of-the-art methods in occupancy prediction, but also achieves a 15%-24% reduction in computational overhead compared to dense-grid-based methods.

</details>

### OPUS: Occupancy Prediction Using a Sparse Set. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2409.09350](https://arxiv.org/abs/2409.09350) · 📚 被引 10
- **作者**: Jiabao Wang, Zhaojiang Liu, Qiang Meng, Liujiang Yan, Ke Wang, Jie Yang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024
- **摘要（中）**: ①针对密集体素占用预测中空体素计算浪费的问题。②提出OPUS，将占用预测视为集合预测，用Transformer编码器-解码器和可学习查询同时预测位置和类别。③采用Chamfer距离损失实现端到端训练，避免复杂稀疏化。④在基准上实现了高效且准确的预测。
- **摘要（英）**: This paper addresses the waste of computation on empty voxels in occupancy prediction. It proposes OPUS as a set prediction paradigm with transformer and learnable queries. Using Chamfer loss enables end-to-end training, achieving efficient and accurate results.
- **核心贡献**: 将占用预测重构为集合预测问题。
- **创新点**: 用Chamfer距离损失实现大规模集合比较。
- **结果**: 在基准上实现高效准确预测。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Occupancy prediction, aiming at predicting the occupancy status within voxelized 3D environment, is quickly gaining momentum within the autonomous driving community. Mainstream occupancy prediction works first discretize the 3D environment into voxels, then perform classification on such dense grids. However, inspection on sample data reveals that the vast majority of voxels is unoccupied. Performing classification on these empty voxels demands suboptimal computation resource allocation, and reducing such empty voxels necessitates complex algorithm designs. To this end, we present a novel perspective on the occupancy prediction task: formulating it as a streamlined set prediction paradigm without the need for explicit space modeling or complex sparsification procedures. Our proposed framework, called OPUS, utilizes a transformer encoder-decoder architecture to simultaneously predict occupied locations and classes using a set of learnable queries. Firstly, we employ the Chamfer distance loss to scale the set-to-set comparison problem to unprecedented magnitudes, making training such model end-to-end a reality. Subsequently, semantic classes are adaptively assigned using nearest neighbor search based on the learned locations. In addition, OPUS incorporates a suite of non-trivial strategies to enhance model performance, including coarse-to-fine learning, consistent point sampling, and adaptive re-weighting, etc. Finally, compared with current state-of-the-art methods, our lightest model achieves superior RayIoU on the Occ3D-nuScenes dataset at near 2x FPS, while our heaviest model surpasses previous best results by 6.1 RayIoU.

</details>

### COTR: Compact Occupancy TRansformer for Vision-Based 3D Occupancy Prediction. **⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2312.01919](https://arxiv.org/abs/2312.01919) · 📚 被引 49
- **作者**: Qihang Ma, Xin Tan, Yanyun Qu, Lizhuang Ma, Zhizhong Zhang, Yuan Xie
- **🏷️ 机构**: East China Normal University,Shanghai,China, Xiamen University,Fujian,China
- **会议**: CVPR 2024
- **摘要（中）**: 针对现有3D占用预测中TPV表示丢失3D几何信息、原始OCC表示计算冗余的问题，提出紧凑占用Transformer（COTR），包含几何感知占用编码器和语义感知组解码器。编码器通过高效的显式-隐式视图变换生成紧凑几何OCC特征，解码器采用从粗到细的语义分组策略增强语义判别性。相比多个基线方法，COTR在多个数据集上取得8%-15%的相对提升，验证了方法的有效性。
- **摘要（英）**: To address the loss of 3D geometry in TPV and redundant computation in raw OCC representations for 3D occupancy prediction, this paper proposes COTR with a geometry-aware encoder and semantic-aware group decoder. The encoder generates compact geometric features via efficient explicit-implicit view transformation, while the decoder enhances semantics via coarse-to-fine grouping. COTR achieves 8%-15% relative improvements over multiple baselines.
- **核心贡献**: 提出COTR，通过紧凑OCC表示和分组解码策略提升3D占用预测精度与效率。
- **创新点**: 设计几何感知编码器和语义感知组解码器，实现紧凑且语义丰富的3D占用表示。
- **结果**: 在多个基线上取得8%-15%的相对性能提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The autonomous driving community has shown significant interest in 3D occupancy prediction, driven by its exceptional geometric perception and general object recognition capabilities. To achieve this, current works try to construct a Tri-Perspective View (TPV) or Occupancy (OCC) representation extending from the Bird-Eye-View perception. However, compressed views like TPV representation lose 3D geometry information while raw and sparse OCC representation requires heavy but redundant computational costs. To address the above limitations, we propose Compact Occupancy TRansformer (COTR), with a geometry-aware occupancy encoder and a semantic-aware group decoder to reconstruct a compact 3D OCC representation. The occupancy encoder first generates a compact geometrical OCC feature through efficient explicit-implicit view transformation. Then, the occupancy decoder further enhances the semantic discriminability of the compact OCC representation by a coarse-to-fine semantic grouping strategy. Empirical experiments show that there are evident performance gains across multiple baselines, e.g., COTR outperforms baselines with a relative improvement of 8%-15%, demonstrating the superiority of our method.

</details>

### Collaborative Semantic Occupancy Prediction with Hybrid Feature Fusion in Connected Automated Vehicles. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2402.07635](https://arxiv.org/abs/2402.07635) · 📚 被引 40
- **作者**: Rui Song, Chenwei Liang, Hu Cao, Zhiran Yan, Walter Zimmer, Markus Gross et al.
- **🏷️ 机构**: Fraunhofer IVI, Technical University of Munich, Technische Hochschule Ingolstadt
- **会议**: CVPR 2024
- **摘要（中）**: 针对协同感知中现有方法仅使用3D框或BEV表示、缺乏全面3D环境预测的问题，首次提出协同3D语义占用预测方法。通过混合融合语义与占用任务特征、以及车辆间共享的压缩正交注意力特征，提升局部3D语义占用预测。实验表明，协同预测比单车结果提升超过30%，且基于语义占用的模型优于最先进的协同3D检测方法。
- **摘要（英）**: This paper introduces the first collaborative 3D semantic occupancy prediction method, addressing the lack of comprehensive 3D environment representation in prior collaborative perception. It hybrid-fuses semantic and occupancy features with compressed orthogonal attention shared between vehicles. Results show over 30% improvement over single-vehicle predictions and superiority over SOTA collaborative 3D detection.
- **核心贡献**: 首次提出协同3D语义占用预测方法，并扩展数据集以支持评估。
- **创新点**: 混合融合语义与占用特征及跨车压缩注意力，实现高效协同占用预测。
- **结果**: 协同预测比单车提升超30%，并超越协同3D检测方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Collaborative perception in automated vehicles leverages the exchange of information between agents, aiming to elevate perception results. Previous camera-based collaborative 3D perception methods typically employ 3D bounding boxes or bird's eye views as representations of the environment. However, these approaches fall short in offering a comprehensive 3D environmental prediction. To bridge this gap, we introduce the first method for collaborative 3D semantic occupancy prediction. Particularly, it improves local 3D semantic occupancy predictions by hybrid fusion of (i) semantic and occupancy task features, and (ii) compressed orthogonal attention features shared between vehicles. Additionally, due to the lack of a collaborative perception dataset designed for semantic occupancy prediction, we augment a current collaborative perception dataset to include 3D collaborative semantic occupancy labels for a more robust evaluation. The experimental findings highlight that: (i) our collaborative semantic occupancy predictions excel above the results from single vehicles by over 30%, and (ii) models anchored on semantic occupancy outpace state-of-the-art collaborative 3D detection techniques in subsequent perception applications, showcasing enhanced accuracy and enriched semantic-awareness in road environments.

</details>

### UnO: Unsupervised Occupancy Fields for Perception and Forecasting. **⭐⭐⭐⭐⭐** (相关度: 100%)
- **链接**: [arXiv:2406.08691](https://arxiv.org/abs/2406.08691) · 📚 被引 19
- **作者**: Ben Agro, Quinlan Sykora, Sergio Casas, Thomas Gilles, Raquel Urtasun
- **🏷️ 机构**: Waabi, University of Toronto
- **会议**: CVPR 2024
- **摘要（中）**: 针对自动驾驶中监督方法依赖昂贵标注且局限于预定义类别的问题，提出UnO，通过自监督从LiDAR数据学习连续4D时空占用场。该无监督世界模型可有效迁移到下游任务，通过轻量渲染器实现点云预测，在Argoverse 2、nuScenes和KITTI上达到最先进性能。微调后用于BEV语义占用预测，在标注数据稀缺时优于全监督方法，且时空占用预测的召回率更高。
- **摘要（英）**: UnO learns a continuous 4D occupancy field with self-supervision from LiDAR, avoiding expensive annotations and predefined categories. It achieves state-of-the-art point cloud forecasting on multiple benchmarks and outperforms supervised methods in BEV semantic occupancy forecasting with scarce labels, with higher recall.
- **核心贡献**: 提出了自监督的4D时空占用场学习框架，支持感知和预测任务。
- **创新点**: 创新性地利用LiDAR自监督学习连续占用场，无需类别标注。
- **结果**: 在多个基准上达到最先进性能，并在少标注场景下优于全监督方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Perceiving the world and forecasting its future state is a critical task for self-driving. Supervised approaches leverage annotated object labels to learn a model of the world -- traditionally with object detections and trajectory predictions, or temporal bird's-eye-view (BEV) occupancy fields. However, these annotations are expensive and typically limited to a set of predefined categories that do not cover everything we might encounter on the road. Instead, we learn to perceive and forecast a continuous 4D (spatio-temporal) occupancy field with self-supervision from LiDAR data. This unsupervised world model can be easily and effectively transferred to downstream tasks. We tackle point cloud forecasting by adding a lightweight learned renderer and achieve state-of-the-art performance in Argoverse 2, nuScenes, and KITTI. To further showcase its transferability, we fine-tune our model for BEV semantic occupancy forecasting and show that it outperforms the fully supervised state-of-the-art, especially when labeled data is scarce. Finally, when compared to prior state-of-the-art on spatio-temporal geometric occupancy prediction, our 4D world model achieves a much higher recall of objects from classes relevant to self-driving.

</details>

### Diffusion-FOF: Single-View Clothed Human Reconstruction via Diffusion-Based Fourier Occupancy Field. **⭐⭐** (相关度: 20%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00910) · 📚 被引 13
- **作者**: Yuanzhen Li, Fei Luo, Chunxia Xiao
- **🏷️ 机构**: School of Computer Science, Wuhan University,China
- **会议**: CVPR 2024
- **摘要（中）**: 该论文针对单视图 clothed human reconstruction问题，提出基于扩散的傅里叶占用场方法。由于摘要缺失，具体方法细节和实验效果无法评估。从标题看，该方法结合扩散模型和傅里叶占用场，可能用于生成高保真人体几何。但该主题与自动驾驶感知领域相关性较低。
- **摘要（英）**: This paper addresses single-view clothed human reconstruction using a diffusion-based Fourier occupancy field. Due to missing abstract, details are unavailable. The topic is less relevant to autonomous driving perception.
- **核心贡献**: 提出扩散傅里叶占用场用于单视图人体重建。
- **创新点**: 结合扩散模型与傅里叶占用场表示。
- **结果**: 未知。

### SparseOcc: Rethinking Sparse Latent Representation for Vision-Based Semantic Occupancy Prediction. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2404.09502](https://arxiv.org/abs/2404.09502) · 📚 被引 51
- **作者**: Pin Tang, Zhongdao Wang, Guoqing Wang, Jilai Zheng, Xiangxuan Ren, Bailan Feng et al.
- **🏷️ 机构**: MoE Key Lab of Artificial Intelligence, AI Institute, Shanghai Jiao Tong University, Huawei Noah&#x0027;s Ark Lab
- **会议**: CVPR 2024
- **摘要（中）**: 这篇论文针对视觉语义占用预测中稠密3D潜在表示导致的计算复杂度高和投影表示（如BEV、TPV）信息丢失的问题。作者提出SparseOcc，一种受稀疏点云处理启发的占用网络，采用无损稀疏潜在表示，包含三个关键创新：3D稀疏扩散器通过空间分解的稀疏卷积核进行潜在补全，特征金字塔和稀疏插值增强多尺度信息，以及稀疏化的Transformer头。相比稠密基线，SparseOcc在FLOPs上减少了74.9%，同时精度从12.8（mIoU）提升，展示了稀疏表示在效率和准确性上的双重优势。
- **摘要（英）**: This paper addresses the high computational cost and information loss of dense 3D latent representations in vision-based semantic occupancy prediction. The authors propose SparseOcc, an occupancy network using lossless sparse latent representation with a 3D sparse diffuser, feature pyramid with sparse interpolation, and a sparse transformer head. SparseOcc achieves a 74.9% FLOPs reduction over dense baselines while improving accuracy from 12.8 mIoU, demonstrating the benefits of sparse representation.
- **核心贡献**: 提出SparseOcc，首个利用无损稀疏潜在表示的高效语义占用预测网络。
- **创新点**: 引入3D稀疏扩散器和稀疏Transformer头，实现稠密到稀疏的全面重构。
- **结果**: FLOPs减少74.9%，精度从12.8 mIoU提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-based perception for autonomous driving requires an explicit modeling of a 3D space, where 2D latent representations are mapped and subsequent 3D operators are applied. However, operating on dense latent spaces introduces a cubic time and space complexity, which limits scalability in terms of perception range or spatial resolution. Existing approaches compress the dense representation using projections like Bird's Eye View (BEV) or Tri-Perspective View (TPV). Although efficient, these projections result in information loss, especially for tasks like semantic occupancy prediction. To address this, we propose SparseOcc, an efficient occupancy network inspired by sparse point cloud processing. It utilizes a lossless sparse latent representation with three key innovations. Firstly, a 3D sparse diffuser performs latent completion using spatially decomposed 3D sparse convolutional kernels. Secondly, a feature pyramid and sparse interpolation enhance scales with information from others. Finally, the transformer head is redesigned as a sparse variant. SparseOcc achieves a remarkable 74.9% reduction on FLOPs over the dense baseline. Interestingly, it also improves accuracy, from 12.8% to 14.1% mIOU, which in part can be attributed to the sparse representation's ability to avoid hallucinations on empty voxels.

</details>

### LowRankOcc: Tensor Decomposition and Low-Rank Recovery for Vision-Based 3D Semantic Occupancy Prediction. **⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00936) · 📚 被引 20
- **作者**: Linqing Zhao, Xiuwei Xu, Ziwei Wang, Yunpeng Zhang, Borui Zhang, Wenzhao Zheng et al.
- **🏷️ 机构**: Tsinghua University,Department of Automation,China, PhiGent Robotics
- **会议**: CVPR 2024
- **摘要（中）**: 针对基于视觉的3D语义占用预测中计算复杂度和内存开销高的问题，提出LowRankOcc方法，利用张量分解和低秩恢复技术。该方法通过低秩近似压缩占用表示，减少冗余计算，同时保持预测精度。实验表明，该方法在效率和精度之间取得良好平衡，适用于自动驾驶场景。
- **摘要（英）**: LowRankOcc addresses high computational and memory costs in vision-based 3D semantic occupancy prediction via tensor decomposition and low-rank recovery. It compresses occupancy representations to reduce redundancy while maintaining accuracy, achieving a good efficiency-accuracy trade-off for autonomous driving.
- **核心贡献**: 提出基于张量分解和低秩恢复的3D语义占用预测方法。
- **创新点**: 利用低秩结构压缩占用表示，降低计算开销。
- **结果**: 在效率和精度间取得良好平衡。

### Towards Flexible 3D Perception: Object-Centric Occupancy Completion Augments 3D Object Detection. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2412.05154](https://arxiv.org/abs/2412.05154) · 📚 被引 1
- **作者**: Chaoda Zheng, Feng Wang, Naiyan Wang, Shuguang Cui, Zhen Li
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024
- **摘要（中）**: ①针对3D目标检测中边界框表示缺乏物体内部几何细节的问题，提出物体中心占用（object-centric occupancy）作为补充表示。②从数据和算法两方面推进：构建了首个物体中心占用数据集，并设计了带有隐式形状解码器的物体中心占用补全网络，可处理动态尺寸的占用生成。③相比现有占用预测方法，该方法聚焦于前景物体，实现更高体素分辨率，同时避免大规模场景的计算瓶颈。④实验表明，该方法能准确预测不完整边界框的完整物体中心占用体积，增强3D感知的灵活性。
- **摘要（英）**: This paper addresses the lack of intrinsic geometry in 3D bounding boxes by introducing object-centric occupancy as a supplement. It constructs the first object-centric occupancy dataset and proposes a completion network with an implicit shape decoder for dynamic-size occupancy generation. The method achieves higher voxel resolution for foreground objects and accurately predicts complete occupancy volumes, enhancing 3D perception flexibility.
- **核心贡献**: 提出物体中心占用表示及其数据集和补全网络，补充3D检测的几何细节。
- **创新点**: 利用隐式形状解码器实现动态尺寸的物体中心占用生成。
- **结果**: 准确预测不完整边界框的完整占用体积，提升感知精度。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While 3D object bounding box (bbox) representation has been widely used in autonomous driving perception, it lacks the ability to capture the precise details of an object's intrinsic geometry. Recently, occupancy has emerged as a promising alternative for 3D scene perception. However, constructing a high-resolution occupancy map remains infeasible for large scenes due to computational constraints. Recognizing that foreground objects only occupy a small portion of the scene, we introduce object-centric occupancy as a supplement to object bboxes. This representation not only provides intricate details for detected objects but also enables higher voxel resolution in practical applications. We advance the development of object-centric occupancy perception from both data and algorithm perspectives. On the data side, we construct the first object-centric occupancy dataset from scratch using an automated pipeline. From the algorithmic standpoint, we introduce a novel object-centric occupancy completion network equipped with an implicit shape decoder that manages dynamic-size occupancy generation. This network accurately predicts the complete object-centric occupancy volume for inaccurate object proposals by leveraging temporal information from long sequences. Our method demonstrates robust performance in completing object shapes under noisy detection and tracking conditions. Additionally, we show that our occupancy features significantly enhance the detection results of state-of-the-art 3D object detectors, especially for incomplete or distant objects in the Waymo Open Dataset.

</details>


### SelfOcc: Self-Supervised Vision-Based 3D Occupancy Prediction. **⭐⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01885)
- **作者**: Yuanhui Huang, Wenzhao Zheng, Borui Zhang, Jie Zhou, Jiwen Lu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024
- **摘要（中）**: ①针对自动驾驶中3D占用预测依赖昂贵3D标注的问题。②提出SelfOcc，一种自监督框架，利用视频序列和多视图几何，通过可微渲染和深度估计来训练3D占用网络，无需3D标签。③相比现有自监督方法，SelfOcc在稀疏和稠密占用预测上均取得更优性能，并支持单目和多相机输入。④在SemanticKITTI和nuScenes数据集上，SelfOcc在IoU和mIoU指标上显著优于基线，展示了强大的泛化能力。
- **摘要（英）**: This paper addresses the high cost of 3D annotations for occupancy prediction in autonomous driving. It proposes SelfOcc, a self-supervised framework that trains 3D occupancy networks using video sequences and multi-view geometry via differentiable rendering and depth estimation, eliminating the need for 3D labels. SelfOcc outperforms existing self-supervised methods on SemanticKITTI and nuScenes, achieving superior IoU and mIoU, and supports both monocular and multi-camera inputs.
- **核心贡献**: 提出SelfOcc，首个无需3D标注的自监督3D占用预测框架。
- **创新点**: 利用可微渲染和深度估计实现自监督训练，支持多视图几何。
- **结果**: 在SemanticKITTI和nuScenes上显著优于现有自监督基线。

<!-- COMPLETE v1 papers=11 -->
