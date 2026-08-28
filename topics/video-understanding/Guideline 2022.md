# Video Understanding — 2022 Guideline

> 领域: 视频理解（动作识别、时序动作、视频大模型）
> 论文数: 8 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Point Primitive Transformer for Long-Term 4D Point Cloud Video Understanding.
- **链接**: [arXiv:2208.00281](https://arxiv.org/abs/2208.00281) · 📚 被引 30
- **作者**: Hao Wen, Yunze Liu, Jingwei Huang, Bo Duan, Li Yi
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper proposes a 4D backbone for long-term point cloud video understanding. A typical way to capture spatial-temporal context is using 4Dconv or transformer without hierarchy. However, those methods are neither effective nor efficient enough due to camera motion, scene changes, sampling patterns, and the complexity of 4D data. To address those issues, we leverage the primitive plane as a mid-level representation to capture the long-term spatial-temporal context in 4D point cloud videos and propose a novel hierarchical backbone named Point Primitive Transformer(PPTr), which is mainly composed of intra-primitive point transformers and primitive transformers. Extensive experiments show that PPTr outperforms the previous state of the arts on different tasks.

</details>

### Prompting Visual-Language Models for Efficient Video Understanding.
- **链接**: [arXiv:2112.04478](https://arxiv.org/abs/2112.04478)
- **作者**: Chen Ju, Tengda Han, Kunhao Zheng, Ya Zhang, Weidi Xie
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Image-based visual-language (I-VL) pre-training has shown great success for learning joint visual-textual representations from large-scale web data, revealing remarkable ability for zero-shot generalisation. This paper presents a simple but strong baseline to efficiently adapt the pre-trained I-VL model, and exploit its powerful ability for resource-hungry video understanding tasks, with minimal training. Specifically, we propose to optimise a few random vectors, termed as continuous prompt vectors, that convert video-related tasks into the same format as the pre-training objectives. In addition, to bridge the gap between static images and videos, temporal information is encoded with lightweight Transformers stacking on top of frame-wise visual features. Experimentally, we conduct extensive ablation studies to analyse the critical components. On 10 public benchmarks of action recognition, action localisation, and text-video retrieval, across closed-set, few-shot, and zero-shot scenarios, we achieve competitive or state-of-the-art performance to existing methods, despite optimising significantly fewer parameters.

</details>

### Source-Free Video Domain Adaptation by Learning Temporal Consistency for Action Recognition.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19830-4_9)
- **作者**: Yuecong Xu, Jianfei Yang, Haozhi Cao, Keyu Wu, Min Wu, Zhenghua Chen
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

## 跨领域论文（完整笔记在其他领域）

- GOCA: Guided Online Cluster Assignment for Self-supervised Video Representation Learning. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
- Motion Sensitive Contrastive Learning for Self-supervised Video Representation. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
- Static and Dynamic Concepts for Self-supervised Video Representation Learning. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
- Federated Self-supervised Learning for Video Understanding. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
- Self-supervised Sparse Representation for Video Anomaly Detection. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
