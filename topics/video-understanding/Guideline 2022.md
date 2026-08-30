# Video Understanding — 2022 Guideline

> 领域: 视频理解（动作识别、时序动作、视频大模型）
> 论文数: 6 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份:

### MeMViT: Memory-Augmented Multiscale Vision Transformer for Efficient Long-Term Video Recognition.
- **链接**: [arXiv:2201.08383](https://arxiv.org/abs/2201.08383) · [代码](https://github.com/facebookresearch/memvit) · 📚 被引 165
- **作者**: Chao-Yuan Wu, Yanghao Li, Karttikeya Mangalam, Haoqi Fan, Bo Xiong, Jitendra Malik et al.
- **🏷️ 机构**: Facebook AI Research
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While today's video recognition systems parse snapshots or short clips accurately, they cannot connect the dots and reason across a longer range of time yet. Most existing video architectures can only process <5 seconds of a video without hitting the computation or memory bottlenecks. In this paper, we propose a new strategy to overcome this challenge. Instead of trying to process more frames at once like most existing methods, we propose to process videos in an online fashion and cache "memory" at each iteration. Through the memory, the model can reference prior context for long-term modeling, with only a marginal cost. Based on this idea, we build MeMViT, a Memory-augmented Multiscale Vision Transformer, that has a temporal support 30x longer than existing models with only 4.5% more compute; traditional methods need >3,000% more compute to do the same. On a wide range of settings, the increased temporal support enabled by MeMViT brings large gains in recognition accuracy consistently. MeMViT obtains state-of-the-art results on the AVA, EPIC-Kitchens-100 action classification, and action anticipation datasets. Code and models are available at https://github.com/facebookresearch/memvit.

</details>

### Motion-aware Contrastive Video Representation Learning via Foreground-background Merging.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00949) · 📚 被引 55
- **作者**: Shuangrui Ding, Maomao Li, Tianyu Yang, Rui Qian, Haohang Xu, Qingyi Chen et al.
- **🏷️ 机构**: Shanghai Jiao Tong University, Tencent AI Lab, The Chinese University of Hong Kong
- **会议**: CVPR 2022

### Revisiting the "Video" in Video-Language Understanding. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2206.01720](https://arxiv.org/abs/2206.01720)
- **作者**: Shyamal Buch, Cristóbal Eyzaguirre, Adrien Gaidon, Jiajun Wu, Li Fei-Fei, Juan Carlos Niebles
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2022
- **摘要（中）**: ①针对视频语言理解任务中，事件时间性理解是否必要的问题。②提出了ATP（atemporal probe）模型，通过图像级理解约束多模态模型的基线性能，用于分析视频语言基准。③发现即使在大规模视频语言模型和旨在测试深层理解的场景中，时间性理解往往不是实现强性能所必需的。④ATP可用于改进数据集和模型设计，帮助识别时间挑战性数据子集。
- **摘要（英）**: This paper revisits video-language understanding by proposing ATP, an atemporal probe that bounds baseline accuracy using image-level understanding. It reveals that temporal understanding is often unnecessary for strong performance, and ATP aids in improving dataset and model design.
- **核心贡献**: 提出ATP模型，量化视频语言任务中时间性理解的必要性。
- **创新点**: 通过图像级约束探针，揭示基准的局限性。
- **结果**: 证明时间性理解非必需，并改进基准设计。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> What makes a video task uniquely suited for videos, beyond what can be understood from a single image? Building on recent progress in self-supervised image-language models, we revisit this question in the context of video and language tasks. We propose the atemporal probe (ATP), a new model for video-language analysis which provides a stronger bound on the baseline accuracy of multimodal models constrained by image-level understanding. By applying this model to standard discriminative video and language tasks, such as video question answering and text-to-video retrieval, we characterize the limitations and potential of current video-language benchmarks. We find that understanding of event temporality is often not necessary to achieve strong or state-of-the-art performance, even compared with recent large-scale video-language models and in contexts intended to benchmark deeper video-level understanding. We also demonstrate how ATP can improve both video-language dataset and model design. We describe a technique for leveraging ATP to better disentangle dataset subsets with a higher concentration of temporally challenging data, improving benchmarking efficacy for causal and temporal understanding. Further, we show that effectively integrating ATP into full video-level temporal models can improve efficiency and state-of-the-art accuracy.

</details>

### Recurring the Transformer for Video Action Recognition. **⭐** (相关度: 10%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01367) · 📚 被引 124
- **作者**: Jiewen Yang, Xingbo Dong, Liujun Liu, Chao Zhang, Jiajun Shen, Dahai Yu
- **🏷️ 机构**: TCL Corporate Research (HK) Co., Ltd
- **会议**: CVPR 2022
- **摘要（中）**: ①这篇论文针对视频动作识别中Transformer架构的递归改进问题，但摘要内容缺失，无法获取具体方法细节。②由于摘要为空，无法判断其提出的方法或具体做法。③同样无法评估其相比已有工作的改进点。④由于缺乏摘要信息，无法提供效果数据。
- **摘要（英）**: This paper addresses the issue of recurring Transformer for video action recognition, but the abstract is missing, making it impossible to assess the proposed method, improvements, or results.
- **核心贡献**: 无法确定核心贡献。
- **创新点**: 无法确定创新点。
- **结果**: 无法确定效果。

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

### TAda! Temporally-Adaptive Convolutions for Video Understanding. **⭐⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2110.06178](https://arxiv.org/abs/2110.06178)
- **作者**: Ziyuan Huang, Shiwei Zhang, Liang Pan, Zhiwu Qing, Mingqian Tang, Ziwei Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022
- **摘要（中）**: ①该论文针对视频理解中空间卷积假设时空不变性、难以建模复杂时序动态的问题。②提出了时间自适应卷积（TAdaConv），通过根据局部和全局时序上下文校准每帧的卷积核权重，赋予空间卷积时序建模能力。③相比以往时序建模操作，TAdaConv在卷积核而非特征上操作，维度小一个数量级，更高效，且核校准增加了模型容量。④构建的TAda2D和TAdaConvNeXt网络在多个视频动作识别和定位基准上达到与最先进方法相当或更好的性能。
- **摘要（英）**: This paper addresses the limitation of spatial convolutions assuming spatio-temporal invariance in video understanding. It proposes Temporally-Adaptive Convolutions (TAdaConv) that calibrate convolution weights per frame based on local and global temporal context, enabling efficient temporal modeling. Operating on kernels rather than features reduces computational cost by an order of magnitude. TAda2D and TAdaConvNeXt achieve state-of-the-art or better performance on multiple video benchmarks.
- **核心贡献**: 提出时间自适应卷积，实现高效时序建模。
- **创新点**: 在卷积核层面进行时间自适应校准。
- **结果**: 在多个基准上达到最先进或更优性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Spatial convolutions are widely used in numerous deep video models. It fundamentally assumes spatio-temporal invariance, i.e., using shared weights for every location in different frames. This work presents Temporally-Adaptive Convolutions (TAdaConv) for video understanding, which shows that adaptive weight calibration along the temporal dimension is an efficient way to facilitate modelling complex temporal dynamics in videos. Specifically, TAdaConv empowers the spatial convolutions with temporal modelling abilities by calibrating the convolution weights for each frame according to its local and global temporal context. Compared to previous temporal modelling operations, TAdaConv is more efficient as it operates over the convolution kernels instead of the features, whose dimension is an order of magnitude smaller than the spatial resolutions. Further, the kernel calibration brings an increased model capacity. We construct TAda2D and TAdaConvNeXt networks by replacing the 2D convolutions in ResNet and ConvNeXt with TAdaConv, which leads to at least on par or better performance compared to state-of-the-art approaches on multiple video action recognition and localization benchmarks. We also demonstrate that as a readily plug-in operation with negligible computation overhead, TAdaConv can effectively improve many existing video models with a convincing margin.

</details>

## 跨领域论文（完整笔记在其他领域）

- How Severe Is Benchmark-Sensitivity in Video Self-supervised Learning? → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
- Implicit Motion Handling for Video Camouflaged Object Detection. → [object-detection](../object-detection/Guideline%202022.md)
- SPAct: Self-supervised Privacy Preservation for Action Recognition. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
- Hierarchically Self-supervised Transformer for Human Skeleton Representation Learning. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
- GOCA: Guided Online Cluster Assignment for Self-supervised Video Representation Learning. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
- SOS! Self-supervised Learning over Sets of Handled Objects in Egocentric Action Recognition. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
- Motion Sensitive Contrastive Learning for Self-supervised Video Representation. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
- Domain Knowledge-Informed Self-supervised Representations for Workout Form Assessment. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
- Static and Dynamic Concepts for Self-supervised Video Representation Learning. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
- Federated Self-supervised Learning for Video Understanding. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
- Self-supervised Sparse Representation for Video Anomaly Detection. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
- Learning a Condensed Frame for Memory-Efficient Video Class-Incremental Learning. → [continual-learning](../continual-learning/Guideline%202022.md)

<!-- COMPLETE v1 papers=8 -->
