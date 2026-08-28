# Video Understanding — 2022 Guideline

> 领域: 视频理解（动作识别、时序动作、视频大模型）
> 论文数: 12 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: [2024](Guideline%202024.md)

### Point Primitive Transformer for Long-Term 4D Point Cloud Video Understanding. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2208.00281](https://arxiv.org/abs/2208.00281) · 📚 被引 30
- **作者**: Hao Wen, Yunze Liu, Jingwei Huang, Bo Duan, Li Yi
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对长期4D点云视频理解中，现有4D卷积或Transformer方法因相机运动、场景变化和采样模式导致效率与效果不佳的问题，提出以原始平面作为中间表征，构建层级骨干网络PPTr，包含原始内点Transformer和原始Transformer，以捕获长期时空上下文。相比已有无层级方法，该方法通过层级设计和平面表征提升了建模能力。实验表明PPTr在多个任务上优于先前最先进方法。
- **摘要（英）**: To address the inefficiency and ineffectiveness of existing 4D convolution or transformer methods for long-term point cloud video understanding due to camera motion and scene changes, this paper proposes a hierarchical backbone PPTr using primitive planes as mid-level representations, comprising intra-primitive and primitive transformers. It improves modeling capability over non-hierarchical methods and outperforms prior state-of-the-art across multiple tasks.
- **核心贡献**: 提出基于原始平面表征的层级4D点云视频理解骨干网络PPTr。
- **创新点**: 利用原始平面作为中间表征，结合层级Transformer捕获长期时空上下文。
- **结果**: 在多个4D点云视频任务上超越先前最先进方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper proposes a 4D backbone for long-term point cloud video understanding. A typical way to capture spatial-temporal context is using 4Dconv or transformer without hierarchy. However, those methods are neither effective nor efficient enough due to camera motion, scene changes, sampling patterns, and the complexity of 4D data. To address those issues, we leverage the primitive plane as a mid-level representation to capture the long-term spatial-temporal context in 4D point cloud videos and propose a novel hierarchical backbone named Point Primitive Transformer(PPTr), which is mainly composed of intra-primitive point transformers and primitive transformers. Extensive experiments show that PPTr outperforms the previous state of the arts on different tasks.

</details>

### Prompting Visual-Language Models for Efficient Video Understanding. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2112.04478](https://arxiv.org/abs/2112.04478)
- **作者**: Chen Ju, Tengda Han, Kunhao Zheng, Ya Zhang, Weidi Xie
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①该论文针对图像-语言预训练模型（如CLIP）难以直接高效应用于视频理解任务的问题，因为视频包含时序信息且计算资源消耗大。②提出了一种简单但强大的基线方法，通过优化少量随机向量（连续提示向量）将视频任务转换为与预训练目标相同的格式，并利用轻量级Transformer编码帧间时序信息。③相比现有方法，该方法只需优化极少量参数，显著降低训练成本，同时保持高性能。④在10个公开基准（动作识别、动作定位、文本-视频检索）的封闭集、少样本和零样本场景中，取得了与现有方法相当或最优的性能。
- **摘要（英）**: This paper tackles the challenge of efficiently adapting image-based visual-language pre-trained models to video understanding tasks, which are resource-intensive and require temporal modeling. It proposes a simple yet strong baseline that optimizes a few random continuous prompt vectors to reformulate video tasks into the pre-training format, with lightweight Transformers encoding temporal information. This approach minimizes trainable parameters, bridging the image-video gap, and achieves competitive or state-of-the-art performance on 10 benchmarks across closed-set, few-shot, and zero-shot settings.
- **核心贡献**: 提出了一种基于连续提示向量和轻量级Transformer的高效视频理解方法。
- **创新点**: 通过优化少量提示向量将视频任务统一到VLM预训练格式，并引入时序编码。
- **结果**: 在10个基准上取得竞争性或最优性能，且训练参数显著减少。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Image-based visual-language (I-VL) pre-training has shown great success for learning joint visual-textual representations from large-scale web data, revealing remarkable ability for zero-shot generalisation. This paper presents a simple but strong baseline to efficiently adapt the pre-trained I-VL model, and exploit its powerful ability for resource-hungry video understanding tasks, with minimal training. Specifically, we propose to optimise a few random vectors, termed as continuous prompt vectors, that convert video-related tasks into the same format as the pre-training objectives. In addition, to bridge the gap between static images and videos, temporal information is encoded with lightweight Transformers stacking on top of frame-wise visual features. Experimentally, we conduct extensive ablation studies to analyse the critical components. On 10 public benchmarks of action recognition, action localisation, and text-video retrieval, across closed-set, few-shot, and zero-shot scenarios, we achieve competitive or state-of-the-art performance to existing methods, despite optimising significantly fewer parameters.

</details>

### Source-Free Video Domain Adaptation by Learning Temporal Consistency for Action Recognition. **⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19830-4_9)
- **作者**: Yuecong Xu, Jianfei Yang, Haozhi Cao, Keyu Wu, Min Wu, Zhenghua Chen
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①该论文针对源域视频数据不可用时的无源域适应问题，即模型需从源域迁移到目标域但无法访问源数据。②提出通过学习时间一致性来适应动作识别模型，利用视频帧间的时序关系作为自监督信号，减少域间差异。③相比传统域适应方法，该方法无需源数据，更符合实际隐私和存储限制。④摘要未提供具体数据，但声称在动作识别任务上有效提升目标域性能。
- **摘要（英）**: This paper addresses source-free video domain adaptation for action recognition, where source data is unavailable during adaptation. It proposes learning temporal consistency as a self-supervised signal to align the model to the target domain, leveraging frame-level temporal relations. This approach overcomes the limitations of traditional domain adaptation that requires source data, improving target domain performance in action recognition.
- **核心贡献**: 提出了一种基于时间一致性的无源视频域适应方法。
- **创新点**: 利用时间一致性作为自监督信号进行无源域适应。
- **结果**: 在动作识别任务上有效提升目标域性能。

## 跨领域论文（完整笔记在其他领域）

- How Severe Is Benchmark-Sensitivity in Video Self-supervised Learning? → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
- Hierarchically Self-supervised Transformer for Human Skeleton Representation Learning. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
- GOCA: Guided Online Cluster Assignment for Self-supervised Video Representation Learning. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
- SOS! Self-supervised Learning over Sets of Handled Objects in Egocentric Action Recognition. → [object-detection](../object-detection/Guideline%202022.md)
- Motion Sensitive Contrastive Learning for Self-supervised Video Representation. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
- Domain Knowledge-Informed Self-supervised Representations for Workout Form Assessment. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
- Static and Dynamic Concepts for Self-supervised Video Representation Learning. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
- Federated Self-supervised Learning for Video Understanding. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
- Self-supervised Sparse Representation for Video Anomaly Detection. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
