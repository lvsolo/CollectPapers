# Vision Transformer — 2022 Guideline

> 领域: 视觉 Transformer（ViT、混合架构、高效注意力）
> 论文数: 18 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### A-ViT: Adaptive Tokens for Efficient Vision Transformer.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01054) · 📚 被引 315
- **作者**: Hongxu Yin, Arash Vahdat, José M. Álvarez, Arun Mallya, Jan Kautz, Pavlo Molchanov
- **🏷️ 机构**: NVIDIA
- **会议**: CVPR 2022

### LAVT: Language-Aware Vision Transformer for Referring Image Segmentation.
- **链接**: [arXiv:2112.02244](https://arxiv.org/abs/2112.02244) · 📚 被引 380
- **作者**: Zhao Yang, Jiaqi Wang, Yansong Tang, Kai Chen, Hengshuang Zhao, Philip H. S. Torr
- **🏷️ 机构**: University of Oxford, Shanghai AI Laboratory, Tsinghua-Berkeley Shenzhen Institute, Tsinghua University
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > Referring image segmentation is a fundamental vision-language task that aims to segment out an object referred to by a natural language expression from an image. One of the key challenges behind this task is leveraging the referring expression for highlighting relevant positions in the image. A paradigm for tackling this problem is to leverage a powerful vision-language ("cross-modal") decoder to fuse features independently extracted from a vision encoder and a language encoder. Recent methods have made remarkable advancements in this paradigm by exploiting Transformers as cross-modal decoders, concurrent to the Transformer's overwhelming success in many other vision-language tasks. Adopting a different approach in this work, we show that significantly better cross-modal alignments can be achieved through the early fusion of linguistic and visual features in intermediate layers of a vision Transformer encoder network. By conducting cross-modal feature fusion in the visual feature encoding stage, we can leverage the well-proven correlation modeling power of a Transformer encoder for excavating helpful multi-modal context. This way, accurate segmentation results are readily harvested with a light-weight mask predictor. Without bells and whistles, our method surpasses the previous state-of-the-art methods on RefCOCO, RefCOCO+, and G-Ref by large margins.

### CSWin Transformer: A General Vision Transformer Backbone with Cross-Shaped Windows.
- **链接**: [arXiv:2107.00652](https://arxiv.org/abs/2107.00652) · [代码](https://github.com/microsoft/CSWin-Transformer) · 📚 被引 1160
- **作者**: Xiaoyi Dong, Jianmin Bao, Dongdong Chen, Weiming Zhang, Nenghai Yu, Lu Yuan et al.
- **🏷️ 机构**: University of Science and Technology of China, Microsoft Research Asia, Microsoft Cloud + AI
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > We present CSWin Transformer, an efficient and effective Transformer-based backbone for general-purpose vision tasks. A challenging issue in Transformer design is that global self-attention is very expensive to compute whereas local self-attention often limits the field of interactions of each token. To address this issue, we develop the Cross-Shaped Window self-attention mechanism for computing self-attention in the horizontal and vertical stripes in parallel that form a cross-shaped window, with each stripe obtained by splitting the input feature into stripes of equal width. We provide a mathematical analysis of the effect of the stripe width and vary the stripe width for different layers of the Transformer network which achieves strong modeling capability while limiting the computation cost. We also introduce Locally-enhanced Positional Encoding (LePE), which handles the local positional information better than existing encoding schemes. LePE naturally supports arbitrary input resolutions, and is thus especially effective and friendly for downstream tasks. Incorporated with these designs and a hierarchical structure, CSWin Transformer demonstrates competitive performance on common vision tasks. Specifically, it achieves 85.4\% Top-1 accuracy on ImageNet-1K without any extra training data or label, 53.9 box AP and 46.4 mask AP on the COCO detection task, and 52.2 mIOU on the ADE20K semantic segmentation task, surpassing previous state-of-the-art Swin Transformer backbone by +1.2, +2.0, +1.4, and +2.0 respectively under the similar FLOPs setting. By further pretraining on the larger dataset ImageNet-21K, we achieve 87.5% Top-1 accuracy on ImageNet-1K and high segmentation performance on ADE20K with 55.7 mIoU. The code and models are available at https://github.com/microsoft/CSWin-Transformer.

### NomMer: Nominate Synergistic Context in Vision Transformer for Visual Recognition.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01176) · 📚 被引 16
- **作者**: Hao Liu, Xinghua Jiang, Xin Li, Zhimin Bao, Deqiang Jiang, Bo Ren
- **🏷️ 机构**: Tencent YouTu Lab
- **会议**: CVPR 2022

### Vision Transformer Slimming: Multi-Dimension Searching in Continuous Optimization Space.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00488) · 📚 被引 68
- **作者**: Arnav Chavan, Zhiqiang Shen, Zhuang Liu, Zechun Liu, Kwang-Ting Cheng, Eric P. Xing
- **🏷️ 机构**: IIT Dhanbad, CMU, UC Berkeley
- **会议**: CVPR 2022

### Towards Practical Certifiable Patch Defense with Vision Transformer.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01472) · 📚 被引 57
- **作者**: Zhaoyu Chen, Bo Li, Jianghe Xu, Shuang Wu, Shouhong Ding, Wenqiang Zhang
- **🏷️ 机构**: Academy for Engineering and Technology, Fudan University, Tencent Youtu Lab
- **会议**: CVPR 2022

### Multi-Scale High-Resolution Vision Transformer for Semantic Segmentation.
- **链接**: [arXiv:2111.01236](https://arxiv.org/abs/2111.01236) · 📚 被引 238
- **作者**: Jiaqi Gu, Hyoukjun Kwon, Dilin Wang, Wei Ye, Meng Li, Yu-Hsin Chen et al.
- **🏷️ 机构**: University of Texas,Austin, Meta Platforms Inc.
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > Vision Transformers (ViTs) have emerged with superior performance on computer vision tasks compared to convolutional neural network (CNN)-based models. However, ViTs are mainly designed for image classification that generate single-scale low-resolution representations, which makes dense prediction tasks such as semantic segmentation challenging for ViTs. Therefore, we propose HRViT, which enhances ViTs to learn semantically-rich and spatially-precise multi-scale representations by integrating high-resolution multi-branch architectures with ViTs. We balance the model performance and efficiency of HRViT by various branch-block co-optimization techniques. Specifically, we explore heterogeneous branch designs, reduce the redundancy in linear layers, and augment the attention block with enhanced expressiveness. Those approaches enabled HRViT to push the Pareto frontier of performance and efficiency on semantic segmentation to a new level, as our evaluation results on ADE20K and Cityscapes show. HRViT achieves 50.20% mIoU on ADE20K and 83.16% mIoU on Cityscapes, surpassing state-of-the-art MiT and CSWin backbones with an average of +1.78 mIoU improvement, 28% parameter saving, and 21% FLOPs reduction, demonstrating the potential of HRViT as a strong vision backbone for semantic segmentation.

### Training Object Detectors from Scratch: An Empirical Study in the Era of Vision Transformer.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00462) · 📚 被引 13
- **作者**: Weixiang Hong, Jiangwei Lao, Wang Ren, Jian Wang, Jingdong Chen, Wei Chu
- **🏷️ 机构**: Ant Group
- **会议**: CVPR 2022

### MPViT: Multi-Path Vision Transformer for Dense Prediction.
- **链接**: [arXiv:2112.11010](https://arxiv.org/abs/2112.11010) · 📚 被引 331
- **作者**: Youngwan Lee, Jonghee Kim, Jeffrey Willette, Sung Ju Hwang
- **🏷️ 机构**: Electronics and Telecommunications Research Institute (ETRI),South Korea, Korea Advanced Institute of Science and Technology (KAIST),South Korea
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > Dense computer vision tasks such as object detection and segmentation require effective multi-scale feature representation for detecting or classifying objects or regions with varying sizes. While Convolutional Neural Networks (CNNs) have been the dominant architectures for such tasks, recently introduced Vision Transformers (ViTs) aim to replace them as a backbone. Similar to CNNs, ViTs build a simple multi-stage structure (i.e., fine-to-coarse) for multi-scale representation with single-scale patches. In this work, with a different perspective from existing Transformers, we explore multi-scale patch embedding and multi-path structure, constructing the Multi-Path Vision Transformer (MPViT). MPViT embeds features of the same size~(i.e., sequence length) with patches of different scales simultaneously by using overlapping convolutional patch embedding. Tokens of different scales are then independently fed into the Transformer encoders via multiple paths and the resulting features are aggregated, enabling both fine and coarse feature representations at the same feature level. Thanks to the diverse, multi-scale feature representations, our MPViTs scaling from tiny~(5M) to base~(73M) consistently achieve superior performance over state-of-the-art Vision Transformers on ImageNet classification, object detection, instance segmentation, and semantic segmentation. These extensive results demonstrate that MPViT can serve as a versatile backbone network for various vision tasks. Code will be made publicly available at \url{https://git.io/MPViT}.

### Towards Robust Vision Transformer.
- **链接**: [arXiv:2105.07926](https://arxiv.org/abs/2105.07926) · [代码](https://github.com/alibaba/easyrobust)
- **作者**: Xiaofeng Mao, Gege Qi, Yuefeng Chen, Xiaodan Li, Ranjie Duan, Shaokai Ye et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > Recent advances on Vision Transformer (ViT) and its improved variants have shown that self-attention-based networks surpass traditional Convolutional Neural Networks (CNNs) in most vision tasks. However, existing ViTs focus on the standard accuracy and computation cost, lacking the investigation of the intrinsic influence on model robustness and generalization. In this work, we conduct systematic evaluation on components of ViTs in terms of their impact on robustness to adversarial examples, common corruptions and distribution shifts. We find some components can be harmful to robustness. By using and combining robust components as building blocks of ViTs, we propose Robust Vision Transformer (RVT), which is a new vision transformer and has superior performance with strong robustness. We further propose two new plug-and-play techniques called position-aware attention scaling and patch-wise augmentation to augment our RVT, which we abbreviate as RVT*. The experimental results on ImageNet and six robustness benchmarks show the advanced robustness and generalization ability of RVT compared with previous ViTs and state-of-the-art CNNs. Furthermore, RVT-S* also achieves Top-1 rank on multiple robustness leaderboards including ImageNet-C and ImageNet-Sketch. The code will be available at \url{https://github.com/alibaba/easyrobust}.

### Affine Medical Image Registration with Coarse-to-Fine Vision Transformer.
- **链接**: [arXiv:2203.15216](https://arxiv.org/abs/2203.15216) · [代码](https://github.com/cwmok/C2FViT) · 📚 被引 90
- **作者**: Tony C. W. Mok, Albert C. S. Chung
- **🏷️ 机构**: The Hong Kong University of Science and Technology,Department of Computer Science and Engineering
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > Affine registration is indispensable in a comprehensive medical image registration pipeline. However, only a few studies focus on fast and robust affine registration algorithms. Most of these studies utilize convolutional neural networks (CNNs) to learn joint affine and non-parametric registration, while the standalone performance of the affine subnetwork is less explored. Moreover, existing CNN-based affine registration approaches focus either on the local misalignment or the global orientation and position of the input to predict the affine transformation matrix, which are sensitive to spatial initialization and exhibit limited generalizability apart from the training dataset. In this paper, we present a fast and robust learning-based algorithm, Coarse-to-Fine Vision Transformer (C2FViT), for 3D affine medical image registration. Our method naturally leverages the global connectivity and locality of the convolutional vision transformer and the multi-resolution strategy to learn the global affine registration. We evaluate our method on 3D brain atlas registration and template-matching normalization. Comprehensive results demonstrate that our method is superior to the existing CNNs-based affine registration methods in terms of registration accuracy, robustness and generalizability while preserving the runtime advantage of the learning-based methods. The source code is available at https://github.com/cwmok/C2FViT.

### Vision Transformer with Deformable Attention.
- **链接**: [arXiv:2201.00520](https://arxiv.org/abs/2201.00520) · [代码](https://github.com/LeapLabTHU/DAT) · 📚 被引 885
- **作者**: Zhuofan Xia, Xuran Pan, Shiji Song, Li Erran Li, Gao Huang
- **🏷️ 机构**: BNRist, Tsinghua University,Department of Automation, Amazon,AWS AI
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > Transformers have recently shown superior performances on various vision tasks. The large, sometimes even global, receptive field endows Transformer models with higher representation power over their CNN counterparts. Nevertheless, simply enlarging receptive field also gives rise to several concerns. On the one hand, using dense attention e.g., in ViT, leads to excessive memory and computational cost, and features can be influenced by irrelevant parts which are beyond the region of interests. On the other hand, the sparse attention adopted in PVT or Swin Transformer is data agnostic and may limit the ability to model long range relations. To mitigate these issues, we propose a novel deformable self-attention module, where the positions of key and value pairs in self-attention are selected in a data-dependent way. This flexible scheme enables the self-attention module to focus on relevant regions and capture more informative features. On this basis, we present Deformable Attention Transformer, a general backbone model with deformable attention for both image classification and dense prediction tasks. Extensive experiments show that our models achieve consistently improved results on comprehensive benchmarks. Code is available at https://github.com/LeapLabTHU/DAT.

### Lite Vision Transformer with Enhanced Self-Attention.
- **链接**: [arXiv:2112.10809](https://arxiv.org/abs/2112.10809) · 📚 被引 145
- **作者**: Chenglin Yang, Yilin Wang, Jianming Zhang, He Zhang, Zijun Wei, Zhe Lin et al.
- **🏷️ 机构**: Johns Hopkins University, Adobe Inc.
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > Despite the impressive representation capacity of vision transformer models, current light-weight vision transformer models still suffer from inconsistent and incorrect dense predictions at local regions. We suspect that the power of their self-attention mechanism is limited in shallower and thinner networks. We propose Lite Vision Transformer (LVT), a novel light-weight transformer network with two enhanced self-attention mechanisms to improve the model performances for mobile deployment. For the low-level features, we introduce Convolutional Self-Attention (CSA). Unlike previous approaches of merging convolution and self-attention, CSA introduces local self-attention into the convolution within a kernel of size 3x3 to enrich low-level features in the first stage of LVT. For the high-level features, we propose Recursive Atrous Self-Attention (RASA), which utilizes the multi-scale context when calculating the similarity map and a recursive mechanism to increase the representation capability with marginal extra parameter cost. The superiority of LVT is demonstrated on ImageNet recognition, ADE20K semantic segmentation, and COCO panoptic segmentation. The code is made publicly available.

### Temporally Efficient Vision Transformer for Video Instance Segmentation.
- **链接**: [arXiv:2204.08412](https://arxiv.org/abs/2204.08412) · [代码](https://github.com/hustvl/TeViT) · 📚 被引 76
- **作者**: Shusheng Yang, Xinggang Wang, Yu Li, Yuxin Fang, Jiemin Fang, Wenyu Liu et al.
- **🏷️ 机构**: School of EIC, Huazhong University of Science &#x0026; Technology, International Digital Economy Academy (IDEA), Applied Research Center (ARC), Tencent PCG
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > Recently vision transformer has achieved tremendous success on image-level visual recognition tasks. To effectively and efficiently model the crucial temporal information within a video clip, we propose a Temporally Efficient Vision Transformer (TeViT) for video instance segmentation (VIS). Different from previous transformer-based VIS methods, TeViT is nearly convolution-free, which contains a transformer backbone and a query-based video instance segmentation head. In the backbone stage, we propose a nearly parameter-free messenger shift mechanism for early temporal context fusion. In the head stages, we propose a parameter-shared spatiotemporal query interaction mechanism to build the one-to-one correspondence between video instances and queries. Thus, TeViT fully utilizes both framelevel and instance-level temporal context information and obtains strong temporal modeling capacity with negligible extra computational cost. On three widely adopted VIS benchmarks, i.e., YouTube-VIS-2019, YouTube-VIS-2021, and OVIS, TeViT obtains state-of-the-art results and maintains high inference speed, e.g., 46.6 AP with 68.9 FPS on YouTube-VIS-2019. Code is available at https://github.com/hustvl/TeViT.

## 跨领域论文（完整笔记在其他领域）

- Self-Supervised Pre-Training of Swin Transformers for 3D Medical Image Analysis. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
- Meta-attention for ViT-backed Continual Learning. → [continual-learning](../continual-learning/Guideline%202022.md)
- Continual Learning with Lifelong Vision Transformer. → [continual-learning](../continual-learning/Guideline%202022.md)
- MeMViT: Memory-Augmented Multiscale Vision Transformer for Efficient Long-Term Video Recognition. → [video-understanding](../video-understanding/Guideline%202022.md)
