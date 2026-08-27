# Vision Transformer — 2022 Guideline

> 领域: 视觉 Transformer（ViT、混合架构、高效注意力）
> 论文数: 13 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Doubly-Fused ViT: Fuse Information from Vision Transformer Doubly with Local Representation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20050-2_43) · 📚 被引 14
- **作者**: Li Gao, Dong Nie, Bo Li, Xiaofeng Ren
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### UIA-ViT: Unsupervised Inconsistency-Aware Method Based on Vision Transformer for Face Forgery Detection.
- **链接**: [arXiv:2210.12752](https://arxiv.org/abs/2210.12752) · 📚 被引 130
- **作者**: Wanyi Zhuang, Qi Chu, Zhentao Tan, Qiankun Liu, Haojie Yuan, Changtao Miao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

- **摘要（英，原文）**:

  > Intra-frame inconsistency has been proved to be effective for the generalization of face forgery detection. However, learning to focus on these inconsistency requires extra pixel-level forged location annotations. Acquiring such annotations is non-trivial. Some existing methods generate large-scale synthesized data with location annotations, which is only composed of real images and cannot capture the properties of forgery regions. Others generate forgery location labels by subtracting paired real and fake images, yet such paired data is difficult to collected and the generated label is usually discontinuous. To overcome these limitations, we propose a novel Unsupervised Inconsistency-Aware method based on Vision Transformer, called UIA-ViT, which only makes use of video-level labels and can learn inconsistency-aware feature without pixel-level annotations. Due to the self-attention mechanism, the attention map among patch embeddings naturally represents the consistency relation, making the vision Transformer suitable for the consistency representation learning. Based on vision Transformer, we propose two key components: Unsupervised Patch Consistency Learning (UPCL) and Progressive Consistency Weighted Assemble (PCWA). UPCL is designed for learning the consistency-related representation with progressive optimized pseudo annotations. PCWA enhances the final classification embedding with previous patch embeddings optimized by UPCL to further improve the detection performance. Extensive experiments demonstrate the effectiveness of the proposed method.

### MaxViT: Multi-axis Vision Transformer.
- **链接**: [arXiv:2204.01697](https://arxiv.org/abs/2204.01697) · [代码](https://github.com/google-research/maxvit)
- **作者**: Zhengzhong Tu, Hossein Talebi, Han Zhang, Feng Yang, Peyman Milanfar, Alan C. Bovik et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

- **摘要（英，原文）**:

  > Transformers have recently gained significant attention in the computer vision community. However, the lack of scalability of self-attention mechanisms with respect to image size has limited their wide adoption in state-of-the-art vision backbones. In this paper we introduce an efficient and scalable attention model we call multi-axis attention, which consists of two aspects: blocked local and dilated global attention. These design choices allow global-local spatial interactions on arbitrary input resolutions with only linear complexity. We also present a new architectural element by effectively blending our proposed attention model with convolutions, and accordingly propose a simple hierarchical vision backbone, dubbed MaxViT, by simply repeating the basic building block over multiple stages. Notably, MaxViT is able to ''see'' globally throughout the entire network, even in earlier, high-resolution stages. We demonstrate the effectiveness of our model on a broad spectrum of vision tasks. On image classification, MaxViT achieves state-of-the-art performance under various settings: without extra data, MaxViT attains 86.5% ImageNet-1K top-1 accuracy; with ImageNet-21K pre-training, our model achieves 88.7% top-1 accuracy. For downstream tasks, MaxViT as a backbone delivers favorable performance on object detection as well as visual aesthetic assessment. We also show that our proposed model expresses strong generative modeling capability on ImageNet, demonstrating the superior potential of MaxViT blocks as a universal vision module. The source code and trained models will be available at https://github.com/google-research/maxvit.

### Convolutional Embedding Makes Hierarchical Vision Transformer Stronger.
- **链接**: [arXiv:2207.13317](https://arxiv.org/abs/2207.13317) · 📚 被引 25
- **作者**: Cong Wang, Hongmin Xu, Xiong Zhang, Li Wang, Zhitong Zheng, Haifeng Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

- **摘要（英，原文）**:

  > Vision Transformers (ViTs) have recently dominated a range of computer vision tasks, yet it suffers from low training data efficiency and inferior local semantic representation capability without appropriate inductive bias. Convolutional neural networks (CNNs) inherently capture regional-aware semantics, inspiring researchers to introduce CNNs back into the architecture of the ViTs to provide desirable inductive bias for ViTs. However, is the locality achieved by the micro-level CNNs embedded in ViTs good enough? In this paper, we investigate the problem by profoundly exploring how the macro architecture of the hybrid CNNs/ViTs enhances the performances of hierarchical ViTs. Particularly, we study the role of token embedding layers, alias convolutional embedding (CE), and systemically reveal how CE injects desirable inductive bias in ViTs. Besides, we apply the optimal CE configuration to 4 recently released state-of-the-art ViTs, effectively boosting the corresponding performances. Finally, a family of efficient hybrid CNNs/ViTs, dubbed CETNets, are released, which may serve as generic vision backbones. Specifically, CETNets achieve 84.9% Top-1 accuracy on ImageNet-1K (training from scratch), 48.6% box mAP on the COCO benchmark, and 51.6% mIoU on the ADE20K, substantially improving the performances of the corresponding state-of-the-art baselines.

### CAViT: Contextual Alignment Vision Transformer for Video Object Re-identification.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19781-9_32) · 📚 被引 27
- **作者**: Jinlin Wu, Lingxiao He, Wu Liu, Yang Yang, Zhen Lei, Tao Mei et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### ScalableViT: Rethinking the Context-Oriented Generalization of Vision Transformer.
- **链接**: [arXiv:2203.10790](https://arxiv.org/abs/2203.10790) · 📚 被引 50
- **作者**: Rui Yang, Hailong Ma, Jie Wu, Yansong Tang, Xuefeng Xiao, Min Zheng et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

- **摘要（英，原文）**:

  > The vanilla self-attention mechanism inherently relies on pre-defined and steadfast computational dimensions. Such inflexibility restricts it from possessing context-oriented generalization that can bring more contextual cues and global representations. To mitigate this issue, we propose a Scalable Self-Attention (SSA) mechanism that leverages two scaling factors to release dimensions of query, key, and value matrices while unbinding them with the input. This scalability fetches context-oriented generalization and enhances object sensitivity, which pushes the whole network into a more effective trade-off state between accuracy and cost. Furthermore, we propose an Interactive Window-based Self-Attention (IWSA), which establishes interaction between non-overlapping regions by re-merging independent value tokens and aggregating spatial information from adjacent windows. By stacking the SSA and IWSA alternately, the Scalable Vision Transformer (ScalableViT) achieves state-of-the-art performance in general-purpose vision tasks. For example, ScalableViT-S outperforms Twins-SVT-S by 1.4% and Swin-T by 1.8% on ImageNet-1K classification.

### Panoramic Vision Transformer for Saliency Detection in 360$\circ $ Videos.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19833-5_25) · 📚 被引 31
- **作者**: Heeseung Yun, Sehun Lee, Gunhee Kim
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Self-slimmed Vision Transformer.
- **链接**: [arXiv:2111.12624](https://arxiv.org/abs/2111.12624) · [代码](https://github.com/Sense-X/SiT)
- **作者**: Zhuofan Zong, Kunchang Li, Guanglu Song, Yali Wang, Yu Qiao, Biao Leng et al.
- **🏷️ 机构**: Shanghai AI Lab, SenseTime
- **会议**: ECCV 2022

- **摘要（英，原文）**:

  > Vision transformers (ViTs) have become the popular structures and outperformed convolutional neural networks (CNNs) on various vision tasks. However, such powerful transformers bring a huge computation burden, because of the exhausting token-to-token comparison. The previous works focus on dropping insignificant tokens to reduce the computational cost of ViTs. But when the dropping ratio increases, this hard manner will inevitably discard the vital tokens, which limits its efficiency. To solve the issue, we propose a generic self-slimmed learning approach for vanilla ViTs, namely SiT. Specifically, we first design a novel Token Slimming Module (TSM), which can boost the inference efficiency of ViTs by dynamic token aggregation. As a general method of token hard dropping, our TSM softly integrates redundant tokens into fewer informative ones. It can dynamically zoom visual attention without cutting off discriminative token relations in the images, even with a high slimming ratio. Furthermore, we introduce a concise Feature Recalibration Distillation (FRD) framework, wherein we design a reverse version of TSM (RTSM) to recalibrate the unstructured token in a flexible auto-encoder manner. Due to the similar structure between teacher and student, our FRD can effectively leverage structure knowledge for better convergence. Finally, we conduct extensive experiments to evaluate our SiT. It demonstrates that our method can speed up ViTs by 1.7x with negligible accuracy drop, and even speed up ViTs by 3.6x while maintaining 97% of their performance. Surprisingly, by simply arming LV-ViT with our SiT, we achieve new state-of-the-art performance on ImageNet. Code is available at https://github.com/Sense-X/SiT.

## 跨领域论文（完整笔记在其他领域）

- V2X-ViT: Vehicle-to-Everything Cooperative Perception with Vision Transformer. → [autonomous-driving](../autonomous-driving/Guideline%202022.md)
- A Simple Single-Scale Vision Transformer for Object Detection and Instance Segmentation. → [object-detection](../object-detection/Guideline%202022.md)
- Exploring Plain Vision Transformer Backbones for Object Detection. → [object-detection](../object-detection/Guideline%202022.md)
- ViTAS: Vision Transformer Architecture Search. → [neural-architecture-search](../neural-architecture-search/Guideline%202022.md)
- Online Continual Learning with Contrastive Vision Transformer. → [continual-learning](../continual-learning/Guideline%202022.md)
