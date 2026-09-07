# Multi-camera Perception — 2026 Guideline

> 领域: 多相机 / 多视角感知（环视、深度估计与 3D 预测）
> 论文数: 3 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Affostruction: 3D Affordance Grounding with Generative Reconstruction
- **链接**: [arXiv:2601.09211](https://arxiv.org/abs/2601.09211)
- **作者**: Chunghyun Park, Seunghyeon Lee, Minsu Cho
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2026

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper addresses the problem of affordance grounding from RGBD images of an object, which aims to localize surface regions corresponding to a text query that describes an action on the object. While existing methods predict affordance regions only on visible surfaces, we propose Affostruction, a generative framework that reconstructs complete object geometry from partial RGBD observations and grounds affordances on the full shape including unobserved regions. Our approach introduces sparse voxel fusion of multi-view features for constant-complexity generative reconstruction, a flow-based formulation that captures the inherent ambiguity of affordance distributions, and an active view selection strategy guided by predicted affordances. Affostruction outperforms existing methods by large margins on challenging benchmarks, achieving 19.1 aIoU on affordance grounding and 32.67 IoU for 3D reconstruction.

</details>

### MVGGT: Multimodal Visual Geometry Grounded Transformer for Multiview 3D Referring Expression Segmentation
- **链接**: [arXiv:2601.06874](https://arxiv.org/abs/2601.06874)
- **作者**: Changli Wu, Haodong Wang, Jiayi Ji, Yutian Yao, Chunsai Du, Jihua Kang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2026

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Most existing 3D referring expression segmentation (3DRES) methods rely on dense, high-quality point clouds, while real-world agents such as robots and mobile phones operate with only a few sparse RGB views and strict latency constraints. We introduce Multi-view 3D Referring Expression Segmentation (MV-3DRES), where the model must recover scene structure and segment the referred object directly from sparse multi-view images. Traditional two-stage pipelines, which first reconstruct a point cloud and then perform segmentation, often yield low-quality geometry, produce coarse or degraded target regions, and run slowly. We propose the Multimodal Visual Geometry Grounded Transformer (MVGGT), an efficient end-to-end framework that integrates language information into sparse-view geometric reasoning through a dual-branch design. Training in this setting exposes a critical optimization barrier, termed Foreground Gradient Dilution (FGD), where sparse 3D signals lead to weak supervision. To resolve this, we introduce Per-view No-target Suppression Optimization (PVSO), which provides stronger and more balanced gradients across views, enabling stable and efficient learning. To support consistent evaluation, we build MVRefer, a benchmark that defines standardized settings and metrics for MV-3DRES. Experiments show that MVGGT establishes the first strong baseline and achieves both high accuracy and fast inference, outperforming existing alternatives. The code is available at https://mvggt.github.io/.

</details>

### Real2Edit2Real: Generating Robotic Demonstrations via a 3D Control Interface
- **链接**: [arXiv:2512.19402](https://arxiv.org/abs/2512.19402)
- **作者**: Yujie Zhao, Hongwei Fan, Di Chen, Shengcong Chen, Liliang Chen, Xiaoqi Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2026

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent progress in robot learning has been driven by large-scale datasets and powerful visuomotor policy architectures, yet policy robustness remains limited by the substantial cost of collecting diverse demonstrations, particularly for spatial generalization in manipulation tasks. To reduce repetitive data collection, we present Real2Edit2Real, a framework that generates new demonstrations by bridging 3D editability with 2D visual data through a 3D control interface. Our approach first reconstructs scene geometry from multi-view RGB observations with a metric-scale 3D reconstruction model. Based on the reconstructed geometry, we perform depth-reliable 3D editing on point clouds to generate new manipulation trajectories while geometrically correcting the robot poses to recover physically consistent depth, which serves as a reliable condition for synthesizing new demonstrations. Finally, we propose a multi-conditional video generation model guided by depth as the primary control signal, together with action, edge, and ray maps, to synthesize spatially augmented multi-view manipulation videos. Experiments on four real-world manipulation tasks demonstrate that policies trained on data generated from only 1-5 source demonstrations can match or outperform those trained on 50 real-world demonstrations, improving data efficiency by up to 10-50x. Moreover, experimental results on height and texture editing demonstrate the framework's flexibility and extensibility, indicating its potential to serve as a unified data generation framework. Project website is https://real2edit2real.github.io/.

</details>
<!-- COMPLETE v1 papers=3 -->
