# Occupancy — 2024 Guideline

> 领域: 占用栅格 / 占用网络（Occupancy Prediction / Occ3D）
> 论文数: 10 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: [2022](Guideline%202022.md)

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

## 跨领域论文（完整笔记在其他领域）

- Learning Occupancy for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- COTR: Compact Occupancy TRansformer for Vision-Based 3D Occupancy Prediction. → [autonomous-driving](../autonomous-driving/Guideline%202024.md)
- Collaborative Semantic Occupancy Prediction with Hybrid Feature Fusion in Connected Automated Vehicles. → [3d-detection](../3d-detection/Guideline%202024.md)
- UnO: Unsupervised Occupancy Fields for Perception and Forecasting. → [autonomous-driving](../autonomous-driving/Guideline%202024.md)
- SelfOcc: Self-Supervised Vision-Based 3D Occupancy Prediction. → [3d-detection](../3d-detection/Guideline%202024.md)
- SparseOcc: Rethinking Sparse Latent Representation for Vision-Based Semantic Occupancy Prediction. → [3d-detection](../3d-detection/Guideline%202024.md)
- DriveWorld: 4D Pre-Trained Scene Understanding via World Models for Autonomous Driving. → [3d-detection](../3d-detection/Guideline%202024.md)
- Volumetric Environment Representation for Vision-Language Navigation. → [3d-detection](../3d-detection/Guideline%202024.md)
