# BEV — 2022 Guideline

> 领域: 鸟瞰图感知（BEV 特征、BEV 检测/分割/预测）
> 论文数: 1 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### BEVFormer: Learning Bird's-Eye-View Representation from Multi-camera Images via Spatiotemporal Transformers.
- **链接**: [arXiv:2203.17270](https://arxiv.org/abs/2203.17270) · [代码](https://github.com/zhiqi-li/BEVFormer) · 📚 被引 1286
- **作者**: Zhiqi Li, Wenhai Wang, Hongyang Li, Enze Xie, Chonghao Sima, Tong Lu et al.
- **🏷️ 机构**: Shanghai AI Lab, Tsinghua / Shanghai AI Lab
- **会议**: ECCV 2022

- **摘要（英，原文）**:

  > 3D visual perception tasks, including 3D detection and map segmentation based on multi-camera images, are essential for autonomous driving systems. In this work, we present a new framework termed BEVFormer, which learns unified BEV representations with spatiotemporal transformers to support multiple autonomous driving perception tasks. In a nutshell, BEVFormer exploits both spatial and temporal information by interacting with spatial and temporal space through predefined grid-shaped BEV queries. To aggregate spatial information, we design spatial cross-attention that each BEV query extracts the spatial features from the regions of interest across camera views. For temporal information, we propose temporal self-attention to recurrently fuse the history BEV information. Our approach achieves the new state-of-the-art 56.9\% in terms of NDS metric on the nuScenes \texttt{test} set, which is 9.0 points higher than previous best arts and on par with the performance of LiDAR-based baselines. We further show that BEVFormer remarkably improves the accuracy of velocity estimation and recall of objects under low visibility conditions. The code is available at \url{https://github.com/zhiqi-li/BEVFormer}.
