# Video Understanding — 2022 Guideline

> 领域: 视频理解（动作识别、时序动作、视频大模型）
> 论文数: 5 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### MeMViT: Memory-Augmented Multiscale Vision Transformer for Efficient Long-Term Video Recognition.
- **链接**: [arXiv:2201.08383](https://arxiv.org/abs/2201.08383) · [代码](https://github.com/facebookresearch/memvit) · 📚 被引 165
- **作者**: Chao-Yuan Wu, Yanghao Li, Karttikeya Mangalam, Haoqi Fan, Bo Xiong, Jitendra Malik et al.
- **🏷️ 机构**: Facebook AI Research
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > While today's video recognition systems parse snapshots or short clips accurately, they cannot connect the dots and reason across a longer range of time yet. Most existing video architectures can only process <5 seconds of a video without hitting the computation or memory bottlenecks. In this paper, we propose a new strategy to overcome this challenge. Instead of trying to process more frames at once like most existing methods, we propose to process videos in an online fashion and cache "memory" at each iteration. Through the memory, the model can reference prior context for long-term modeling, with only a marginal cost. Based on this idea, we build MeMViT, a Memory-augmented Multiscale Vision Transformer, that has a temporal support 30x longer than existing models with only 4.5% more compute; traditional methods need >3,000% more compute to do the same. On a wide range of settings, the increased temporal support enabled by MeMViT brings large gains in recognition accuracy consistently. MeMViT obtains state-of-the-art results on the AVA, EPIC-Kitchens-100 action classification, and action anticipation datasets. Code and models are available at https://github.com/facebookresearch/memvit.

### Motion-aware Contrastive Video Representation Learning via Foreground-background Merging.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00949) · 📚 被引 55
- **作者**: Shuangrui Ding, Maomao Li, Tianyu Yang, Rui Qian, Haohang Xu, Qingyi Chen et al.
- **🏷️ 机构**: Shanghai Jiao Tong University, Tencent AI Lab, The Chinese University of Hong Kong
- **会议**: CVPR 2022

## 跨领域论文（完整笔记在其他领域）

- Cross-Architecture Self-supervised Video Representation Learning. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
- TransRank: Self-supervised Video Representation Learning via Ranking-based Transformation Recognition. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
- Learning from Untrimmed Videos: Self-Supervised Video Representation Learning with Hierarchical Consistency. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
