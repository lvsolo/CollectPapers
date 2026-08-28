# Vision Transformer — 2023 Guideline

> 领域: 视觉 Transformer（ViT、混合架构、高效注意力）
> 论文数: 23 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Video OWL-ViT: Temporally-consistent open-world localization in video.
- **链接**: [arXiv:2308.11093](https://arxiv.org/abs/2308.11093) · 📚 被引 11
- **作者**: Georg Heigold, Daniel Keysers, Matthias Minderer, Mario Lucic, Alexey A. Gritsenko, Fisher Yu et al.
- **🏷️ 机构**: Google DeepMind, ETH Zurich
- **会议**: ICCV 2023

### Castling-ViT: Compressing Self-Attention via Switching Towards Linear-Angular Attention at Vision Transformer Inference.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01387) · 📚 被引 57
- **作者**: Haoran You, Yunyang Xiong, Xiaoliang Dai, Bichen Wu, Peizhao Zhang, Haoqi Fan et al.
- **🏷️ 机构**: Georgia Institute of Technology, Meta Research
- **会议**: CVPR 2023

### ViPLO: Vision Transformer Based Pose-Conditioned Self-Loop Graph for Human-Object Interaction Detection.
- **链接**: [arXiv:2304.08114](https://arxiv.org/abs/2304.08114) · [代码](https://github.com/Jeeseung-Park/ViPLO) · 📚 被引 75
- **作者**: Jeeseung Park, Jin-Woo Park, Jong-Seok Lee
- **🏷️ 机构**: mAy-I Inc.,Seoul,Korea, Yonsei University,Korea
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Human-Object Interaction (HOI) detection, which localizes and infers relationships between human and objects, plays an important role in scene understanding. Although two-stage HOI detectors have advantages of high efficiency in training and inference, they suffer from lower performance than one-stage methods due to the old backbone networks and the lack of considerations for the HOI perception process of humans in the interaction classifiers. In this paper, we propose Vision Transformer based Pose-Conditioned Self-Loop Graph (ViPLO) to resolve these problems. First, we propose a novel feature extraction method suitable for the Vision Transformer backbone, called masking with overlapped area (MOA) module. The MOA module utilizes the overlapped area between each patch and the given region in the attention function, which addresses the quantization problem when using the Vision Transformer backbone. In addition, we design a graph with a pose-conditioned self-loop structure, which updates the human node encoding with local features of human joints. This allows the classifier to focus on specific human joints to effectively identify the type of interaction, which is motivated by the human perception process for HOI. As a result, ViPLO achieves the state-of-the-art results on two public benchmarks, especially obtaining a +2.07 mAP performance gain on the HICO-DET dataset. The source codes are available at https://github.com/Jeeseung-Park/ViPLO.

</details>

### Slide-Transformer: Hierarchical Vision Transformer with Local Self-Attention.
- **链接**: [arXiv:2304.04237](https://arxiv.org/abs/2304.04237) · [代码](https://github.com/LeapLabTHU/Slide-Transformer) · 📚 被引 103
- **作者**: Xuran Pan, Tianzhu Ye, Zhuofan Xia, Shiji Song, Gao Huang
- **🏷️ 机构**: BNRist, Tsinghua University,Department of Automation
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-attention mechanism has been a key factor in the recent progress of Vision Transformer (ViT), which enables adaptive feature extraction from global contexts. However, existing self-attention methods either adopt sparse global attention or window attention to reduce the computation complexity, which may compromise the local feature learning or subject to some handcrafted designs. In contrast, local attention, which restricts the receptive field of each query to its own neighboring pixels, enjoys the benefits of both convolution and self-attention, namely local inductive bias and dynamic feature selection. Nevertheless, current local attention modules either use inefficient Im2Col function or rely on specific CUDA kernels that are hard to generalize to devices without CUDA support. In this paper, we propose a novel local attention module, Slide Attention, which leverages common convolution operations to achieve high efficiency, flexibility and generalizability. Specifically, we first re-interpret the column-based Im2Col function from a new row-based perspective and use Depthwise Convolution as an efficient substitution. On this basis, we propose a deformed shifting module based on the re-parameterization technique, which further relaxes the fixed key/value positions to deformed features in the local region. In this way, our module realizes the local attention paradigm in both efficient and flexible manner. Extensive experiments show that our slide attention module is applicable to a variety of advanced Vision Transformer models and compatible with various hardware devices, and achieves consistently improved performances on comprehensive benchmarks. Code is available at https://github.com/LeapLabTHU/Slide-Transformer.

</details>

### SemiCVT: Semi-Supervised Convolutional Vision Transformer for Semantic Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01091) · 📚 被引 39
- **作者**: Huimin Huang, Shiao Xie, Lanfen Lin, Ruofeng Tong, Yen-Wei Chen, Yuexiang Li et al.
- **🏷️ 机构**: Zhejiang University, Ritsumeikan University, Tencent Jarvis Lab
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

### EfficientViT: Memory Efficient Vision Transformer with Cascaded Group Attention.
- **链接**: [arXiv:2305.07027](https://arxiv.org/abs/2305.07027) · [代码](https://github.com/microsoft/Cream) · 📚 被引 828
- **作者**: Xinyu Liu, Houwen Peng, Ningxin Zheng, Yuqing Yang, Han Hu, Yixuan Yuan
- **🏷️ 机构**: The Chinese University of Hong Kong, Microsoft Research
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision transformers have shown great success due to their high model capabilities. However, their remarkable performance is accompanied by heavy computation costs, which makes them unsuitable for real-time applications. In this paper, we propose a family of high-speed vision transformers named EfficientViT. We find that the speed of existing transformer models is commonly bounded by memory inefficient operations, especially the tensor reshaping and element-wise functions in MHSA. Therefore, we design a new building block with a sandwich layout, i.e., using a single memory-bound MHSA between efficient FFN layers, which improves memory efficiency while enhancing channel communication. Moreover, we discover that the attention maps share high similarities across heads, leading to computational redundancy. To address this, we present a cascaded group attention module feeding attention heads with different splits of the full feature, which not only saves computation cost but also improves attention diversity. Comprehensive experiments demonstrate EfficientViT outperforms existing efficient models, striking a good trade-off between speed and accuracy. For instance, our EfficientViT-M5 surpasses MobileNetV3-Large by 1.9% in accuracy, while getting 40.4% and 45.2% higher throughput on Nvidia V100 GPU and Intel Xeon CPU, respectively. Compared to the recent efficient model MobileViT-XXS, EfficientViT-M2 achieves 1.8% superior accuracy, while running 5.8x/3.7x faster on the GPU/CPU, and 7.4x faster when converted to ONNX format. Code and models are available at https://github.com/microsoft/Cream/tree/main/EfficientViT.

</details>

### BiFormer: Vision Transformer with Bi-Level Routing Attention.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00995) · 📚 被引 1070
- **作者**: Lei Zhu, Xinjiang Wang, Zhanghan Ke, Wayne Zhang, Rynson W. H. Lau
- **🏷️ 机构**: City University of Hong Kong, SenseTime Research
- **会议**: CVPR 2023

> The advent of high-capacity pre-trained models has revolutionized problem-solving in computer vision, shifting the focus from training task-specific models to adapting pre-trained models. Consequently, effectively adapting large pre-trained models to downstream tasks in an efficient manner has become a prominent research area. Existing solutions primarily concentrate on designing lightweight adapters and their interaction with pre-trained models, with the goal of minimizing the number of parameters requiring updates. In this study, we propose a novel Adapter Re-Composing (ARC) strategy that addresses efficient pre-trained model adaptation from a fresh perspective. Our approach considers the reusability of adaptation parameters and introduces a parameter-sharing scheme. Specifically, we leverage symmetric down-/up-projections to construct bottleneck operations, which are shared across layers. By learning low-dimensional re-scaling coefficients, we can effectively re-compose layer-adaptive adapters. This parameter-sharing strategy in adapter design allows us to significantly reduce the number of new parameters while maintaining satisfactory performance, thereby offering a promising approach to compress the adaptation cost. We conduct experiments on 24 downstream image classification tasks using various Vision Transformer variants to evaluate our method. The results demonstrate that our approach achieves compelling transfer learning performance with a reduced parameter count. Our code is available at \href{https://github.com/DavidYanAnDe/ARC}{https://github.com/DavidYanAnDe/ARC}.

- T-FFTRadNet: Object Detection with Swin Vision Transformers from Raw ADC Radar Signals. → [object-detection](../object-detection/Guideline%202023.md)
- MMST-ViT: Climate Change-aware Crop Yield Prediction via Multi-Modal Spatial-Temporal Vision Transformer. → [multimodal](../multimodal/Guideline%202023.md)
- Unleashing Vanilla Vision Transformer with Masked Image Modeling for Object Detection. → [object-detection](../object-detection/Guideline%202023.md)
- A Simple Vision Transformer for Weakly Semi-supervised 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Contrastive Feature Masking Open-Vocabulary Vision Transformer. → [open-set-detection](../open-set-detection/Guideline%202023.md)
- ElasticViT: Conflict-aware Supernet Training for Deploying Fast Vision Transformer on Diverse Mobile Devices. → [neural-architecture-search](../neural-architecture-search/Guideline%202023.md)
