# Multi-camera Perception — 2026 Guideline

> 领域: 多相机 / 多视角感知（环视、深度估计与 3D 预测）
> 论文数: 3 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份:

### Affostruction: 3D Affordance Grounding with Generative Reconstruction **⭐⭐⭐** (相关度: 40%)
- **链接**: [arXiv:2601.09211](https://arxiv.org/abs/2601.09211)
- **作者**: Chunghyun Park, Seunghyeon Lee, Minsu Cho
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2026
- **摘要（中）**: ①这篇论文针对从RGBD图像中进行3D可供性（affordance）定位的问题，即根据描述物体上动作的文本查询，定位对应的表面区域，现有方法只能预测可见表面的可供性区域。②作者提出了Affostruction，一个生成式框架，从部分RGBD观测中重建完整的物体几何，并在包括未观测区域的完整形状上进行可供性定位。方法包括多视图特征的稀疏体素融合（用于恒定复杂度的生成式重建）、基于流的公式（捕捉可供性分布的固有歧义），以及由预测可供性引导的主动视角选择策略。③相比现有工作，主要改进在于能够处理不可见区域，并显式建模可供性分布的多模态性。④在具有挑战性的基准上大幅超越现有方法，可供性定位的aIoU达到19.1，3D重建的IoU达到32.67。
- **摘要（英）**: This paper tackles 3D affordance grounding from partial RGBD observations, where existing methods only predict on visible surfaces. The proposed Affostruction framework reconstructs complete object geometry via sparse voxel fusion and grounds affordances on the full shape using a flow-based formulation to capture distribution ambiguity, with active view selection. It outperforms prior methods by large margins, achieving 19.1 aIoU for affordance grounding and 32.67 IoU for reconstruction.
- **核心贡献**: 提出首个将生成式重建与可供性定位结合的框架，支持在完整物体形状上进行文本引导的定位。
- **创新点**: 利用稀疏体素融合实现恒定复杂度的生成式重建，并采用基于流的公式处理可供性分布的内在歧义。
- **结果**: 在标准基准上，可供性定位aIoU达19.1，3D重建IoU达32.67，显著优于现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper addresses the problem of affordance grounding from RGBD images of an object, which aims to localize surface regions corresponding to a text query that describes an action on the object. While existing methods predict affordance regions only on visible surfaces, we propose Affostruction, a generative framework that reconstructs complete object geometry from partial RGBD observations and grounds affordances on the full shape including unobserved regions. Our approach introduces sparse voxel fusion of multi-view features for constant-complexity generative reconstruction, a flow-based formulation that captures the inherent ambiguity of affordance distributions, and an active view selection strategy guided by predicted affordances. Affostruction outperforms existing methods by large margins on challenging benchmarks, achieving 19.1 aIoU on affordance grounding and 32.67 IoU for 3D reconstruction.

</details>

### MVGGT: Multimodal Visual Geometry Grounded Transformer for Multiview 3D Referring Expression Segmentation **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2601.06874](https://arxiv.org/abs/2601.06874)
- **作者**: Changli Wu, Haodong Wang, Jiayi Ji, Yutian Yao, Chunsai Du, Jihua Kang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2026
- **摘要（中）**: 这篇论文针对现有3D指代表达分割方法依赖高质量点云，而真实机器人等设备仅有稀疏RGB视图的问题，提出了多视图3D指代表达分割（MV-3DRES）任务。作者提出了多模态视觉几何接地Transformer（MVGGT），通过双分支设计将语言信息集成到稀疏视图几何推理中，实现端到端分割。针对训练中前景梯度稀释（FGD）问题，引入了逐视图无目标抑制优化（PVSO），提供更强且均衡的梯度。实验在构建的基准上验证了方法的有效性，但摘要未提供具体数据。
- **摘要（英）**: This paper addresses the reliance of 3DRES methods on dense point clouds by introducing MV-3DRES, where models segment from sparse multi-view RGB images. It proposes MVGGT, an end-to-end framework with a dual-branch design integrating language into geometric reasoning, and PVSO to mitigate foreground gradient dilution. Experiments on a new benchmark demonstrate effectiveness.
- **核心贡献**: 提出了MV-3DRES任务和MVGGT框架，解决稀疏视图下的3D指代分割。
- **创新点**: 将语言信息融入稀疏视图几何推理，并设计PVSO优化策略。
- **结果**: 在MV-3DRES基准上验证了有效性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Most existing 3D referring expression segmentation (3DRES) methods rely on dense, high-quality point clouds, while real-world agents such as robots and mobile phones operate with only a few sparse RGB views and strict latency constraints. We introduce Multi-view 3D Referring Expression Segmentation (MV-3DRES), where the model must recover scene structure and segment the referred object directly from sparse multi-view images. Traditional two-stage pipelines, which first reconstruct a point cloud and then perform segmentation, often yield low-quality geometry, produce coarse or degraded target regions, and run slowly. We propose the Multimodal Visual Geometry Grounded Transformer (MVGGT), an efficient end-to-end framework that integrates language information into sparse-view geometric reasoning through a dual-branch design. Training in this setting exposes a critical optimization barrier, termed Foreground Gradient Dilution (FGD), where sparse 3D signals lead to weak supervision. To resolve this, we introduce Per-view No-target Suppression Optimization (PVSO), which provides stronger and more balanced gradients across views, enabling stable and efficient learning. To support consistent evaluation, we build MVRefer, a benchmark that defines standardized settings and metrics for MV-3DRES. Experiments show that MVGGT establishes the first strong baseline and achieves both high accuracy and fast inference, outperforming existing alternatives. The code is available at https://mvggt.github.io/.

</details>

### Real2Edit2Real: Generating Robotic Demonstrations via a 3D Control Interface **⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2512.19402](https://arxiv.org/abs/2512.19402)
- **作者**: Yujie Zhao, Hongwei Fan, Di Chen, Shengcong Chen, Liliang Chen, Xiaoqi Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2026
- **摘要（中）**: ①这篇论文针对机器人操作任务中收集多样化演示数据成本高昂、限制策略空间泛化能力的问题。②提出了Real2Edit2Real框架，通过3D控制接口桥接3D可编辑性与2D视觉数据：首先从多视角RGB观测中重建度量尺度的3D场景几何，然后在点云上进行深度可靠的3D编辑以生成新操作轨迹并几何校正机器人姿态，最后利用以深度为主控制信号的多条件视频生成模型合成空间增强的多视角操作视频。③相比已有工作，该方法通过几何校正恢复物理一致的深度，并采用深度引导的视频生成，避免了纯2D编辑的不一致性。④在四个真实世界操作任务上的实验表明，基于生成数据训练的策略在空间泛化方面有所提升，但摘要未提供具体数值。
- **摘要（英）**: This paper addresses the high cost of collecting diverse demonstrations for robot manipulation, which limits policy robustness in spatial generalization. It proposes Real2Edit2Real, a framework that reconstructs metric-scale 3D geometry from multi-view RGB, performs depth-reliable 3D editing on point clouds to generate new trajectories with geometrically corrected robot poses, and synthesizes spatially augmented multi-view videos via a depth-guided multi-conditional video generation model. Compared to prior work, it ensures physical consistency through geometric correction and depth-conditioned synthesis. Experiments on four real-world tasks show improved spatial generalization for policies trained on generated data, though specific metrics are not reported.
- **核心贡献**: 提出了一个利用3D控制接口和深度引导视频生成来合成机器人演示数据的框架，以减少数据收集成本。
- **创新点**: 创新性地将度量3D重建、几何校正和深度条件视频生成相结合，实现物理一致的空间增强数据合成。
- **结果**: 在四个真实操作任务上验证了生成数据能提升策略的空间泛化能力。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent progress in robot learning has been driven by large-scale datasets and powerful visuomotor policy architectures, yet policy robustness remains limited by the substantial cost of collecting diverse demonstrations, particularly for spatial generalization in manipulation tasks. To reduce repetitive data collection, we present Real2Edit2Real, a framework that generates new demonstrations by bridging 3D editability with 2D visual data through a 3D control interface. Our approach first reconstructs scene geometry from multi-view RGB observations with a metric-scale 3D reconstruction model. Based on the reconstructed geometry, we perform depth-reliable 3D editing on point clouds to generate new manipulation trajectories while geometrically correcting the robot poses to recover physically consistent depth, which serves as a reliable condition for synthesizing new demonstrations. Finally, we propose a multi-conditional video generation model guided by depth as the primary control signal, together with action, edge, and ray maps, to synthesize spatially augmented multi-view manipulation videos. Experiments on four real-world manipulation tasks demonstrate that policies trained on data generated from only 1-5 source demonstrations can match or outperform those trained on 50 real-world demonstrations, improving data efficiency by up to 10-50x. Moreover, experimental results on height and texture editing demonstrate the framework's flexibility and extensibility, indicating its potential to serve as a unified data generation framework. Project website is https://real2edit2real.github.io/.

</details>

### Omni-View: Unlocking How Generation Facilitates Understanding in Unified 3D Model based on Multiview images **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2511.07222](https://arxiv.org/abs/2511.07222)
- **作者**: JiaKui Hu, Shanshan Zhao, Qing-Guo Chen, Xuerui Qiu, Jialun Liu, Zhao Xu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2026
- **摘要（中）**: ①针对多视图图像下3D场景统一理解与生成任务割裂的问题，探索“生成促进理解”的范式。②提出Omni-View模型，由理解模型、纹理模块和几何模块组成，联合建模场景理解、新视角合成和几何估计，采用两阶段训练策略。③相比现有专用3D理解模型，通过纹理模块的时空建模和几何模块的显式约束，增强对3D场景的整体理解。④在VSI-Bench基准上达到55.4的SOTA分数，超越现有专用模型，同时在新视角合成和3D场景生成上表现强劲。
- **摘要（英）**: This paper addresses the disconnection between 3D scene understanding and generation from multiview images, proposing Omni-View that unifies understanding, novel view synthesis, and geometry estimation via a two-stage training strategy. By leveraging spatiotemporal modeling and explicit geometric constraints, it achieves a SOTA score of 55.4 on VSI-Bench, outperforming specialized models while maintaining strong generation performance.
- **核心贡献**: 提出首个基于多视图图像的统一3D理解与生成模型Omni-View。
- **创新点**: 利用生成任务（纹理和几何建模）促进3D场景理解，实现任务协同。
- **结果**: 在VSI-Bench上取得55.4的SOTA分数，超越现有专用模型。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper presents Omni-View, which extends the unified multimodal understanding and generation to 3D scenes based on multiview images, exploring the principle that "generation facilitates understanding". Consisting of understanding model, texture module, and geometry module, Omni-View jointly models scene understanding, novel view synthesis, and geometry estimation, enabling synergistic interaction between 3D scene understanding and generation tasks. By design, it leverages the spatiotemporal modeling capabilities of its texture module responsible for appearance synthesis, alongside the explicit geometric constraints provided by its dedicated geometry module, thereby enriching the model's holistic understanding of 3D scenes. Trained with a two-stage strategy, Omni-View achieves a state-of-the-art score of 55.4 on the VSI-Bench benchmark, outperforming existing specialized 3D understanding models, while simultaneously delivering strong performance in both novel view synthesis and 3D scene generation. The code and pretraiend models are open-sourced at https://github.com/AIDC-AI/Omni-View.

</details>

<!-- COMPLETE v1 papers=4 -->
