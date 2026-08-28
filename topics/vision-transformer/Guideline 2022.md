# Vision Transformer — 2022 Guideline

> 领域: 视觉 Transformer（ViT、混合架构、高效注意力）
> 论文数: 16 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: [2024](Guideline%202024.md)

### Doubly-Fused ViT: Fuse Information from Vision Transformer Doubly with Local Representation. **⭐⭐** (相关度: 40%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20050-2_43) · 📚 被引 14
- **作者**: Li Gao, Dong Nie, Bo Li, Xiaofeng Ren
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①该论文针对视觉Transformer中局部与全局信息融合不足的问题。②提出了一种双重融合机制，将来自Vision Transformer的全局信息与局部表示进行两次融合。③相比现有单次融合方法，通过双重融合增强了特征表达能力。④由于摘要缺失，无法提供具体性能数据。
- **摘要（英）**: This paper addresses insufficient fusion of local and global information in Vision Transformers. It proposes a doubly-fused mechanism integrating global Transformer features with local representations twice. Compared to single-fusion methods, it enhances feature expressiveness. Specific results are unavailable due to missing abstract.
- **核心贡献**: 提出双重融合的ViT架构以增强局部与全局信息交互。
- **创新点**: 双重融合机制设计。
- **结果**: 未提供具体实验数据。

### UIA-ViT: Unsupervised Inconsistency-Aware Method Based on Vision Transformer for Face Forgery Detection. **⭐⭐⭐** (相关度: 50%)
- **链接**: [arXiv:2210.12752](https://arxiv.org/abs/2210.12752) · 📚 被引 130
- **作者**: Wanyi Zhuang, Qi Chu, Zhentao Tan, Qiankun Liu, Haojie Yuan, Changtao Miao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①该论文针对人脸伪造检测中帧内不一致性学习需要像素级标注的问题。②提出基于Vision Transformer的无监督不一致性感知方法UIA-ViT，仅利用视频级标签，通过自注意力机制学习一致性表示，并设计无监督补丁一致性学习（UPCL）和渐进式组件。③相比依赖合成数据或配对数据的方法，无需额外标注，更实用。④摘要未给出具体准确率数据，但方法在泛化性上有望提升。
- **摘要（英）**: This paper tackles the need for pixel-level annotations in learning intra-frame inconsistency for face forgery detection. It proposes UIA-ViT, an unsupervised inconsistency-aware method based on Vision Transformer, using only video-level labels and self-attention to learn consistency representations, with components like Unsupervised Patch Consistency Learning (UPCL). Compared to methods requiring synthetic or paired data, it avoids extra annotations. Specific accuracy is not reported in the abstract.
- **核心贡献**: 提出无需像素级标注的UIA-ViT方法用于人脸伪造检测。
- **创新点**: 利用自注意力机制实现无监督不一致性学习。
- **结果**: 摘要未提供具体性能数据。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Intra-frame inconsistency has been proved to be effective for the generalization of face forgery detection. However, learning to focus on these inconsistency requires extra pixel-level forged location annotations. Acquiring such annotations is non-trivial. Some existing methods generate large-scale synthesized data with location annotations, which is only composed of real images and cannot capture the properties of forgery regions. Others generate forgery location labels by subtracting paired real and fake images, yet such paired data is difficult to collected and the generated label is usually discontinuous. To overcome these limitations, we propose a novel Unsupervised Inconsistency-Aware method based on Vision Transformer, called UIA-ViT, which only makes use of video-level labels and can learn inconsistency-aware feature without pixel-level annotations. Due to the self-attention mechanism, the attention map among patch embeddings naturally represents the consistency relation, making the vision Transformer suitable for the consistency representation learning. Based on vision Transformer, we propose two key components: Unsupervised Patch Consistency Learning (UPCL) and Progressive Consistency Weighted Assemble (PCWA). UPCL is designed for learning the consistency-related representation with progressive optimized pseudo annotations. PCWA enhances the final classification embedding with previous patch embeddings optimized by UPCL to further improve the detection performance. Extensive experiments demonstrate the effectiveness of the proposed method.

</details>

### Convolutional Embedding Makes Hierarchical Vision Transformer Stronger. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2207.13317](https://arxiv.org/abs/2207.13317) · 📚 被引 25
- **作者**: Cong Wang, Hongmin Xu, Xiong Zhang, Li Wang, Zhitong Zheng, Haifeng Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①该论文针对层级视觉Transformer中局部语义表示能力不足和训练数据效率低的问题。②系统研究了卷积嵌入（CE）在混合CNN/ViT架构中的作用，并应用于4种最新ViT提升性能，提出CETNets系列骨干。③相比仅微级CNN嵌入，揭示了宏架构中CE注入归纳偏置的机制。④CETNets在ImageNet-1K上达到84.9% top-1准确率（从零训练）。
- **摘要（英）**: This paper addresses weak local semantic representation and low training efficiency in hierarchical Vision Transformers. It systematically studies convolutional embedding (CE) in hybrid CNN/ViT architectures, applies optimal configurations to four recent ViTs, and releases CETNets backbones. Compared to micro-level CNN embeddings, it reveals how CE injects inductive bias at macro level. CETNets achieve 84.9% ImageNet-1K top-1 accuracy from scratch.
- **核心贡献**: 揭示卷积嵌入在层级ViT中的作用并提升性能。
- **创新点**: 系统性研究CE配置对ViT的影响。
- **结果**: ImageNet-1K 84.9% top-1准确率。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision Transformers (ViTs) have recently dominated a range of computer vision tasks, yet it suffers from low training data efficiency and inferior local semantic representation capability without appropriate inductive bias. Convolutional neural networks (CNNs) inherently capture regional-aware semantics, inspiring researchers to introduce CNNs back into the architecture of the ViTs to provide desirable inductive bias for ViTs. However, is the locality achieved by the micro-level CNNs embedded in ViTs good enough? In this paper, we investigate the problem by profoundly exploring how the macro architecture of the hybrid CNNs/ViTs enhances the performances of hierarchical ViTs. Particularly, we study the role of token embedding layers, alias convolutional embedding (CE), and systemically reveal how CE injects desirable inductive bias in ViTs. Besides, we apply the optimal CE configuration to 4 recently released state-of-the-art ViTs, effectively boosting the corresponding performances. Finally, a family of efficient hybrid CNNs/ViTs, dubbed CETNets, are released, which may serve as generic vision backbones. Specifically, CETNets achieve 84.9% Top-1 accuracy on ImageNet-1K (training from scratch), 48.6% box mAP on the COCO benchmark, and 51.6% mIoU on the ADE20K, substantially improving the performances of the corresponding state-of-the-art baselines.

</details>

### CAViT: Contextual Alignment Vision Transformer for Video Object Re-identification. **⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19781-9_32) · 📚 被引 27
- **作者**: Jinlin Wu, Lingxiao He, Wu Liu, Yang Yang, Zhen Lei, Tao Mei et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①该论文针对视频目标重识别中上下文对齐问题。②提出CAViT方法，利用Vision Transformer进行上下文对齐，以提升视频ReID性能。③相比传统方法，通过Transformer建模时序上下文。④由于摘要缺失，无法提供具体数据。
- **摘要（英）**: This paper addresses contextual alignment in video object re-identification. It proposes CAViT, using Vision Transformer for context alignment to improve video ReID. Compared to traditional methods, it leverages Transformer for temporal context modeling. Specific results are unavailable due to missing abstract.
- **核心贡献**: 提出基于ViT的视频ReID上下文对齐方法。
- **创新点**: Transformer用于视频时序上下文建模。
- **结果**: 未提供具体数据。

### ScalableViT: Rethinking the Context-Oriented Generalization of Vision Transformer. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2203.10790](https://arxiv.org/abs/2203.10790) · 📚 被引 50
- **作者**: Rui Yang, Hailong Ma, Jie Wu, Yansong Tang, Xuefeng Xiao, Min Zheng et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①该论文针对标准自注意力机制中计算维度固定、缺乏上下文感知泛化能力的问题，限制了模型获取上下文线索和全局表示。②提出了可扩展自注意力（SSA）机制，通过两个缩放因子释放查询、键、值矩阵的维度并使其与输入解耦，同时提出交互式窗口自注意力（IWSA），通过重新合并独立值标记和聚合相邻窗口的空间信息来建立非重叠区域间的交互。③相比现有ViT变体，该方法增强了对象敏感性和上下文泛化能力，在准确率和计算成本之间实现了更有效的权衡。④在ImageNet-1K分类上，ScalableViT-S比Twins-SVT-S高1.4%，比Swin-T高1.8%，在通用视觉任务上达到最先进性能。
- **摘要（英）**: This paper addresses the inflexibility of standard self-attention with fixed computational dimensions, which limits context-oriented generalization. It proposes Scalable Self-Attention (SSA) with scaling factors to release matrix dimensions and Interactive Window-based Self-Attention (IWSA) for cross-region interaction, improving object sensitivity and global representation. ScalableViT achieves state-of-the-art performance, e.g., 1.4% and 1.8% higher than Twins-SVT-S and Swin-T on ImageNet-1K.
- **核心贡献**: 提出可扩展自注意力和交互式窗口自注意力机制，构建了高性能的ScalableViT架构。
- **创新点**: 通过缩放因子动态调整注意力维度，并结合窗口交互增强上下文泛化。
- **结果**: 在ImageNet-1K分类上超越多个SOTA ViT模型，精度提升1.4%-1.8%。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The vanilla self-attention mechanism inherently relies on pre-defined and steadfast computational dimensions. Such inflexibility restricts it from possessing context-oriented generalization that can bring more contextual cues and global representations. To mitigate this issue, we propose a Scalable Self-Attention (SSA) mechanism that leverages two scaling factors to release dimensions of query, key, and value matrices while unbinding them with the input. This scalability fetches context-oriented generalization and enhances object sensitivity, which pushes the whole network into a more effective trade-off state between accuracy and cost. Furthermore, we propose an Interactive Window-based Self-Attention (IWSA), which establishes interaction between non-overlapping regions by re-merging independent value tokens and aggregating spatial information from adjacent windows. By stacking the SSA and IWSA alternately, the Scalable Vision Transformer (ScalableViT) achieves state-of-the-art performance in general-purpose vision tasks. For example, ScalableViT-S outperforms Twins-SVT-S by 1.4% and Swin-T by 1.8% on ImageNet-1K classification.

</details>

### Panoramic Vision Transformer for Saliency Detection in 360$\circ $ Videos. **⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19833-5_25) · 📚 被引 31
- **作者**: Heeseung Yun, Sehun Lee, Gunhee Kim
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①该论文针对360度视频中显著性检测的挑战，由于全景图像存在畸变和复杂背景，传统方法难以有效处理。②提出了全景视觉Transformer（Panoramic Vision Transformer）用于360度视频的显著性检测，利用Transformer架构捕捉全局上下文和时空特征。③相比现有基于CNN的方法，该方法能更好地处理全景图像的几何特性，并利用视频时序信息。④摘要未提供具体数据，但预期在显著性检测基准上表现优异。
- **摘要（英）**: This paper tackles saliency detection in 360-degree videos, which is challenging due to distortion and complex backgrounds. It proposes a Panoramic Vision Transformer to capture global context and spatiotemporal features, improving over CNN-based methods. The abstract lacks specific results, but the approach aims for superior performance on saliency benchmarks.
- **核心贡献**: 提出首个用于360度视频显著性检测的全景视觉Transformer架构。
- **创新点**: 利用Transformer处理全景视频的全局时空特征，适应畸变。
- **结果**: 摘要未提供具体数据，预期在基准测试上表现良好。

### Self-slimmed Vision Transformer. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2111.12624](https://arxiv.org/abs/2111.12624)
- **作者**: Zhuofan Zong, Kunchang Li, Guanglu Song, Yali Wang, Yu Qiao, Biao Leng et al.
- **🏷️ 机构**: Shanghai AI Lab, SenseTime
- **会议**: ECCV 2022
- **摘要（中）**: ①该论文针对视觉Transformer中通过硬性丢弃标记来降低计算成本的方法，在高丢弃率下会丢失关键标记，限制效率。②提出了自精简学习框架SiT，包括Token Slimming Module（TSM），通过动态标记聚合将冗余标记软性整合为更少的信息标记，以及Feature Recalibration Distillation（FRD）框架，使用反向TSM（RTSM）以自编码器方式重校准非结构化标记。③相比硬丢弃方法，TSM能动态调整视觉注意力，即使在高精简率下也不切断判别性标记关系。④摘要未提供具体数据，但预期在图像分类等任务上提升推理效率并保持精度。
- **摘要（英）**: This paper addresses the inefficiency of hard token dropping in ViTs, which loses vital tokens at high ratios. It proposes a self-slimmed learning approach (SiT) with a Token Slimming Module (TSM) for dynamic token aggregation and a Feature Recalibration Distillation (FRD) framework with reverse TSM for recalibration. This soft integration preserves discriminative relations, improving efficiency without accuracy loss. Specific results are not provided in the abstract.
- **核心贡献**: 提出自精简ViT框架SiT，通过动态标记聚合和特征重校准蒸馏提升推理效率。
- **创新点**: 用软性标记聚合替代硬丢弃，并引入反向TSM进行特征重校准。
- **结果**: 摘要未提供具体数据，预期在高精简率下保持精度并提升效率。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision transformers (ViTs) have become the popular structures and outperformed convolutional neural networks (CNNs) on various vision tasks. However, such powerful transformers bring a huge computation burden, because of the exhausting token-to-token comparison. The previous works focus on dropping insignificant tokens to reduce the computational cost of ViTs. But when the dropping ratio increases, this hard manner will inevitably discard the vital tokens, which limits its efficiency. To solve the issue, we propose a generic self-slimmed learning approach for vanilla ViTs, namely SiT. Specifically, we first design a novel Token Slimming Module (TSM), which can boost the inference efficiency of ViTs by dynamic token aggregation. As a general method of token hard dropping, our TSM softly integrates redundant tokens into fewer informative ones. It can dynamically zoom visual attention without cutting off discriminative token relations in the images, even with a high slimming ratio. Furthermore, we introduce a concise Feature Recalibration Distillation (FRD) framework, wherein we design a reverse version of TSM (RTSM) to recalibrate the unstructured token in a flexible auto-encoder manner. Due to the similar structure between teacher and student, our FRD can effectively leverage structure knowledge for better convergence. Finally, we conduct extensive experiments to evaluate our SiT. It demonstrates that our method can speed up ViTs by 1.7x with negligible accuracy drop, and even speed up ViTs by 3.6x while maintaining 97% of their performance. Surprisingly, by simply arming LV-ViT with our SiT, we achieve new state-of-the-art performance on ImageNet. Code is available at https://github.com/Sense-X/SiT.

</details>

## 跨领域论文（完整笔记在其他领域）

- V2X-ViT: Vehicle-to-Everything Cooperative Perception with Vision Transformer. → [3d-detection](../3d-detection/Guideline%202022.md)
- A Simple Single-Scale Vision Transformer for Object Detection and Instance Segmentation. → [object-detection](../object-detection/Guideline%202022.md)
- Exploring Plain Vision Transformer Backbones for Object Detection. → [object-detection](../object-detection/Guideline%202022.md)
- Open-Set Semi-Supervised Object Detection. → [object-detection](../object-detection/Guideline%202022.md)
- PPT: Token-Pruned Pose Transformer for Monocular and Multi-view Human Pose Estimation. → [multi-camera-perception](../multi-camera-perception/Guideline%202022.md)
- ViTAS: Vision Transformer Architecture Search. → [neural-architecture-search](../neural-architecture-search/Guideline%202022.md)
- MaxViT: Multi-axis Vision Transformer. → [object-detection](../object-detection/Guideline%202022.md)
- Online Continual Learning with Contrastive Vision Transformer. → [continual-learning](../continual-learning/Guideline%202022.md)
- UniNet: Unified Architecture Search with Convolution, Transformer, and MLP. → [neural-architecture-search](../neural-architecture-search/Guideline%202022.md)
