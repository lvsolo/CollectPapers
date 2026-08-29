# Vision Transformer — 2022 Guideline

> 领域: 视觉 Transformer（ViT、混合架构、高效注意力）
> 论文数: 17 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### A-ViT: Adaptive Tokens for Efficient Vision Transformer.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01054) · 📚 被引 316
- **作者**: Hongxu Yin, Arash Vahdat, José M. Álvarez, Arun Mallya, Jan Kautz, Pavlo Molchanov
- **🏷️ 机构**: NVIDIA
- **会议**: CVPR 2022

### LAVT: Language-Aware Vision Transformer for Referring Image Segmentation.
- **链接**: [arXiv:2112.02244](https://arxiv.org/abs/2112.02244) · 📚 被引 384
- **作者**: Zhao Yang, Jiaqi Wang, Yansong Tang, Kai Chen, Hengshuang Zhao, Philip H. S. Torr
- **🏷️ 机构**: University of Oxford, Shanghai AI Laboratory, Tsinghua-Berkeley Shenzhen Institute, Tsinghua University
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Referring image segmentation is a fundamental vision-language task that aims to segment out an object referred to by a natural language expression from an image. One of the key challenges behind this task is leveraging the referring expression for highlighting relevant positions in the image. A paradigm for tackling this problem is to leverage a powerful vision-language ("cross-modal") decoder to fuse features independently extracted from a vision encoder and a language encoder. Recent methods have made remarkable advancements in this paradigm by exploiting Transformers as cross-modal decoders, concurrent to the Transformer's overwhelming success in many other vision-language tasks. Adopting a different approach in this work, we show that significantly better cross-modal alignments can be achieved through the early fusion of linguistic and visual features in intermediate layers of a vision Transformer encoder network. By conducting cross-modal feature fusion in the visual feature encoding stage, we can leverage the well-proven correlation modeling power of a Transformer encoder for excavating helpful multi-modal context. This way, accurate segmentation results are readily harvested with a light-weight mask predictor. Without bells and whistles, our method surpasses the previous state-of-the-art methods on RefCOCO, RefCOCO+, and G-Ref by large margins.

</details>

### CSWin Transformer: A General Vision Transformer Backbone with Cross-Shaped Windows.
- **链接**: [arXiv:2107.00652](https://arxiv.org/abs/2107.00652) · [代码](https://github.com/microsoft/CSWin-Transformer) · 📚 被引 1161
- **作者**: Xiaoyi Dong, Jianmin Bao, Dongdong Chen, Weiming Zhang, Nenghai Yu, Lu Yuan et al.
- **🏷️ 机构**: University of Science and Technology of China, Microsoft Research Asia, Microsoft Cloud + AI
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present CSWin Transformer, an efficient and effective Transformer-based backbone for general-purpose vision tasks. A challenging issue in Transformer design is that global self-attention is very expensive to compute whereas local self-attention often limits the field of interactions of each token. To address this issue, we develop the Cross-Shaped Window self-attention mechanism for computing self-attention in the horizontal and vertical stripes in parallel that form a cross-shaped window, with each stripe obtained by splitting the input feature into stripes of equal width. We provide a mathematical analysis of the effect of the stripe width and vary the stripe width for different layers of the Transformer network which achieves strong modeling capability while limiting the computation cost. We also introduce Locally-enhanced Positional Encoding (LePE), which handles the local positional information better than existing encoding schemes. LePE naturally supports arbitrary input resolutions, and is thus especially effective and friendly for downstream tasks. Incorporated with these designs and a hierarchical structure, CSWin Transformer demonstrates competitive performance on common vision tasks. Specifically, it achieves 85.4\% Top-1 accuracy on ImageNet-1K without any extra training data or label, 53.9 box AP and 46.4 mask AP on the COCO detection task, and 52.2 mIOU on the ADE20K semantic segmentation task, surpassing previous state-of-the-art Swin Transformer backbone by +1.2, +2.0, +1.4, and +2.0 respectively under the similar FLOPs setting. By further pretraining on the larger dataset ImageNet-21K, we achieve 87.5% Top-1 accuracy on ImageNet-1K and high segmentation performance on ADE20K with 55.7 mIoU. The code and models are available at https://github.com/microsoft/CSWin-Transformer.

</details>

### NomMer: Nominate Synergistic Context in Vision Transformer for Visual Recognition.
- **链接**: [arXiv:2111.12994](https://arxiv.org/abs/2111.12994) · [代码](https://github.com/TencentYoutuResearch/VisualRecognition-NomMer) · 📚 被引 16
- **作者**: Hao Liu, Xinghua Jiang, Xin Li, Zhimin Bao, Deqiang Jiang, Bo Ren
- **🏷️ 机构**: Tencent YouTu Lab
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, Vision Transformers (ViT), with the self-attention (SA) as the de facto ingredients, have demonstrated great potential in the computer vision community. For the sake of trade-off between efficiency and performance, a group of works merely perform SA operation within local patches, whereas the global contextual information is abandoned, which would be indispensable for visual recognition tasks. To solve the issue, the subsequent global-local ViTs take a stab at marrying local SA with global one in parallel or alternative way in the model. Nevertheless, the exhaustively combined local and global context may exist redundancy for various visual data, and the receptive field within each layer is fixed. Alternatively, a more graceful way is that global and local context can adaptively contribute per se to accommodate different visual data. To achieve this goal, we in this paper propose a novel ViT architecture, termed NomMer, which can dynamically Nominate the synergistic global-local context in vision transforMer. By investigating the working pattern of our proposed NomMer, we further explore what context information is focused. Beneficial from this "dynamic nomination" mechanism, without bells and whistles, the NomMer can not only achieve 84.5% Top-1 classification accuracy on ImageNet with only 73M parameters, but also show promising performance on dense prediction tasks, i.e., object detection and semantic segmentation. The code and models will be made publicly available at https://github.com/TencentYoutuResearch/VisualRecognition-NomMer

</details>

### Vision Transformer Slimming: Multi-Dimension Searching in Continuous Optimization Space.
- **链接**: [arXiv:2201.00814](https://arxiv.org/abs/2201.00814) · [代码](https://github.com/Arnav0400/ViT-Slim) · 📚 被引 68
- **作者**: Arnav Chavan, Zhiqiang Shen, Zhuang Liu, Zechun Liu, Kwang-Ting Cheng, Eric P. Xing
- **🏷️ 机构**: IIT Dhanbad, CMU, UC Berkeley
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper explores the feasibility of finding an optimal sub-model from a vision transformer and introduces a pure vision transformer slimming (ViT-Slim) framework. It can search a sub-structure from the original model end-to-end across multiple dimensions, including the input tokens, MHSA and MLP modules with state-of-the-art performance. Our method is based on a learnable and unified $\ell_1$ sparsity constraint with pre-defined factors to reflect the global importance in the continuous searching space of different dimensions. The searching process is highly efficient through a single-shot training scheme. For instance, on DeiT-S, ViT-Slim only takes ~43 GPU hours for the searching process, and the searched structure is flexible with diverse dimensionalities in different modules. Then, a budget threshold is employed according to the requirements of accuracy-FLOPs trade-off on running devices, and a re-training process is performed to obtain the final model. The extensive experiments show that our ViT-Slim can compress up to 40% of parameters and 40% FLOPs on various vision transformers while increasing the accuracy by ~0.6% on ImageNet. We also demonstrate the advantage of our searched models on several downstream datasets. Our code is available at https://github.com/Arnav0400/ViT-Slim.

</details>

### Towards Practical Certifiable Patch Defense with Vision Transformer.
- **链接**: [arXiv:2203.08519](https://arxiv.org/abs/2203.08519) · 📚 被引 57
- **作者**: Zhaoyu Chen, Bo Li, Jianghe Xu, Shuang Wu, Shouhong Ding, Wenqiang Zhang
- **🏷️ 机构**: Academy for Engineering and Technology, Fudan University, Tencent Youtu Lab
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Patch attacks, one of the most threatening forms of physical attack in adversarial examples, can lead networks to induce misclassification by modifying pixels arbitrarily in a continuous region. Certifiable patch defense can guarantee robustness that the classifier is not affected by patch attacks. Existing certifiable patch defenses sacrifice the clean accuracy of classifiers and only obtain a low certified accuracy on toy datasets. Furthermore, the clean and certified accuracy of these methods is still significantly lower than the accuracy of normal classification networks, which limits their application in practice. To move towards a practical certifiable patch defense, we introduce Vision Transformer (ViT) into the framework of Derandomized Smoothing (DS). Specifically, we propose a progressive smoothed image modeling task to train Vision Transformer, which can capture the more discriminable local context of an image while preserving the global semantic information. For efficient inference and deployment in the real world, we innovatively reconstruct the global self-attention structure of the original ViT into isolated band unit self-attention. On ImageNet, under 2% area patch attacks our method achieves 41.70% certified accuracy, a nearly 1-fold increase over the previous best method (26.00%). Simultaneously, our method achieves 78.58% clean accuracy, which is quite close to the normal ResNet-101 accuracy. Extensive experiments show that our method obtains state-of-the-art clean and certified accuracy with inferring efficiently on CIFAR-10 and ImageNet.

</details>

### Multi-Scale High-Resolution Vision Transformer for Semantic Segmentation.
- **链接**: [arXiv:2111.01236](https://arxiv.org/abs/2111.01236) · 📚 被引 238
- **作者**: Jiaqi Gu, Hyoukjun Kwon, Dilin Wang, Wei Ye, Meng Li, Yu-Hsin Chen et al.
- **🏷️ 机构**: University of Texas,Austin, Meta Platforms Inc.
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision Transformers (ViTs) have emerged with superior performance on computer vision tasks compared to convolutional neural network (CNN)-based models. However, ViTs are mainly designed for image classification that generate single-scale low-resolution representations, which makes dense prediction tasks such as semantic segmentation challenging for ViTs. Therefore, we propose HRViT, which enhances ViTs to learn semantically-rich and spatially-precise multi-scale representations by integrating high-resolution multi-branch architectures with ViTs. We balance the model performance and efficiency of HRViT by various branch-block co-optimization techniques. Specifically, we explore heterogeneous branch designs, reduce the redundancy in linear layers, and augment the attention block with enhanced expressiveness. Those approaches enabled HRViT to push the Pareto frontier of performance and efficiency on semantic segmentation to a new level, as our evaluation results on ADE20K and Cityscapes show. HRViT achieves 50.20% mIoU on ADE20K and 83.16% mIoU on Cityscapes, surpassing state-of-the-art MiT and CSWin backbones with an average of +1.78 mIoU improvement, 28% parameter saving, and 21% FLOPs reduction, demonstrating the potential of HRViT as a strong vision backbone for semantic segmentation.

</details>

### Training Object Detectors from Scratch: An Empirical Study in the Era of Vision Transformer.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00462) · 📚 被引 13
- **作者**: Weixiang Hong, Jiangwei Lao, Wang Ren, Jian Wang, Jingdong Chen, Wei Chu
- **🏷️ 机构**: Ant Group
- **会议**: CVPR 2022

### MPViT: Multi-Path Vision Transformer for Dense Prediction.
- **链接**: [arXiv:2112.11010](https://arxiv.org/abs/2112.11010) · 📚 被引 333
- **作者**: Youngwan Lee, Jonghee Kim, Jeffrey Willette, Sung Ju Hwang
- **🏷️ 机构**: Electronics and Telecommunications Research Institute (ETRI),South Korea, Korea Advanced Institute of Science and Technology (KAIST),South Korea
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Dense computer vision tasks such as object detection and segmentation require effective multi-scale feature representation for detecting or classifying objects or regions with varying sizes. While Convolutional Neural Networks (CNNs) have been the dominant architectures for such tasks, recently introduced Vision Transformers (ViTs) aim to replace them as a backbone. Similar to CNNs, ViTs build a simple multi-stage structure (i.e., fine-to-coarse) for multi-scale representation with single-scale patches. In this work, with a different perspective from existing Transformers, we explore multi-scale patch embedding and multi-path structure, constructing the Multi-Path Vision Transformer (MPViT). MPViT embeds features of the same size~(i.e., sequence length) with patches of different scales simultaneously by using overlapping convolutional patch embedding. Tokens of different scales are then independently fed into the Transformer encoders via multiple paths and the resulting features are aggregated, enabling both fine and coarse feature representations at the same feature level. Thanks to the diverse, multi-scale feature representations, our MPViTs scaling from tiny~(5M) to base~(73M) consistently achieve superior performance over state-of-the-art Vision Transformers on ImageNet classification, object detection, instance segmentation, and semantic segmentation. These extensive results demonstrate that MPViT can serve as a versatile backbone network for various vision tasks. Code will be made publicly available at \url{https://git.io/MPViT}.

</details>

### Towards Robust Vision Transformer.
- **链接**: [arXiv:2105.07926](https://arxiv.org/abs/2105.07926) · [代码](https://github.com/alibaba/easyrobust)
- **作者**: Xiaofeng Mao, Gege Qi, Yuefeng Chen, Xiaodan Li, Ranjie Duan, Shaokai Ye et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advances on Vision Transformer (ViT) and its improved variants have shown that self-attention-based networks surpass traditional Convolutional Neural Networks (CNNs) in most vision tasks. However, existing ViTs focus on the standard accuracy and computation cost, lacking the investigation of the intrinsic influence on model robustness and generalization. In this work, we conduct systematic evaluation on components of ViTs in terms of their impact on robustness to adversarial examples, common corruptions and distribution shifts. We find some components can be harmful to robustness. By using and combining robust components as building blocks of ViTs, we propose Robust Vision Transformer (RVT), which is a new vision transformer and has superior performance with strong robustness. We further propose two new plug-and-play techniques called position-aware attention scaling and patch-wise augmentation to augment our RVT, which we abbreviate as RVT*. The experimental results on ImageNet and six robustness benchmarks show the advanced robustness and generalization ability of RVT compared with previous ViTs and state-of-the-art CNNs. Furthermore, RVT-S* also achieves Top-1 rank on multiple robustness leaderboards including ImageNet-C and ImageNet-Sketch. The code will be available at \url{https://github.com/alibaba/easyrobust}.

</details>

### Affine Medical Image Registration with Coarse-to-Fine Vision Transformer.
- **链接**: [arXiv:2203.15216](https://arxiv.org/abs/2203.15216) · [代码](https://github.com/cwmok/C2FViT) · 📚 被引 90
- **作者**: Tony C. W. Mok, Albert C. S. Chung
- **🏷️ 机构**: The Hong Kong University of Science and Technology,Department of Computer Science and Engineering
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Affine registration is indispensable in a comprehensive medical image registration pipeline. However, only a few studies focus on fast and robust affine registration algorithms. Most of these studies utilize convolutional neural networks (CNNs) to learn joint affine and non-parametric registration, while the standalone performance of the affine subnetwork is less explored. Moreover, existing CNN-based affine registration approaches focus either on the local misalignment or the global orientation and position of the input to predict the affine transformation matrix, which are sensitive to spatial initialization and exhibit limited generalizability apart from the training dataset. In this paper, we present a fast and robust learning-based algorithm, Coarse-to-Fine Vision Transformer (C2FViT), for 3D affine medical image registration. Our method naturally leverages the global connectivity and locality of the convolutional vision transformer and the multi-resolution strategy to learn the global affine registration. We evaluate our method on 3D brain atlas registration and template-matching normalization. Comprehensive results demonstrate that our method is superior to the existing CNNs-based affine registration methods in terms of registration accuracy, robustness and generalizability while preserving the runtime advantage of the learning-based methods. The source code is available at https://github.com/cwmok/C2FViT.

</details>

### Vision Transformer with Deformable Attention.
- **链接**: [arXiv:2201.00520](https://arxiv.org/abs/2201.00520) · [代码](https://github.com/LeapLabTHU/DAT) · 📚 被引 889
- **作者**: Zhuofan Xia, Xuran Pan, Shiji Song, Li Erran Li, Gao Huang
- **🏷️ 机构**: BNRist, Tsinghua University,Department of Automation, Amazon,AWS AI
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Transformers have recently shown superior performances on various vision tasks. The large, sometimes even global, receptive field endows Transformer models with higher representation power over their CNN counterparts. Nevertheless, simply enlarging receptive field also gives rise to several concerns. On the one hand, using dense attention e.g., in ViT, leads to excessive memory and computational cost, and features can be influenced by irrelevant parts which are beyond the region of interests. On the other hand, the sparse attention adopted in PVT or Swin Transformer is data agnostic and may limit the ability to model long range relations. To mitigate these issues, we propose a novel deformable self-attention module, where the positions of key and value pairs in self-attention are selected in a data-dependent way. This flexible scheme enables the self-attention module to focus on relevant regions and capture more informative features. On this basis, we present Deformable Attention Transformer, a general backbone model with deformable attention for both image classification and dense prediction tasks. Extensive experiments show that our models achieve consistently improved results on comprehensive benchmarks. Code is available at https://github.com/LeapLabTHU/DAT.

</details>

### Lite Vision Transformer with Enhanced Self-Attention.
- **链接**: [arXiv:2112.10809](https://arxiv.org/abs/2112.10809) · 📚 被引 146
- **作者**: Chenglin Yang, Yilin Wang, Jianming Zhang, He Zhang, Zijun Wei, Zhe Lin et al.
- **🏷️ 机构**: Johns Hopkins University, Adobe Inc.
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite the impressive representation capacity of vision transformer models, current light-weight vision transformer models still suffer from inconsistent and incorrect dense predictions at local regions. We suspect that the power of their self-attention mechanism is limited in shallower and thinner networks. We propose Lite Vision Transformer (LVT), a novel light-weight transformer network with two enhanced self-attention mechanisms to improve the model performances for mobile deployment. For the low-level features, we introduce Convolutional Self-Attention (CSA). Unlike previous approaches of merging convolution and self-attention, CSA introduces local self-attention into the convolution within a kernel of size 3x3 to enrich low-level features in the first stage of LVT. For the high-level features, we propose Recursive Atrous Self-Attention (RASA), which utilizes the multi-scale context when calculating the similarity map and a recursive mechanism to increase the representation capability with marginal extra parameter cost. The superiority of LVT is demonstrated on ImageNet recognition, ADE20K semantic segmentation, and COCO panoptic segmentation. The code is made publicly available.

</details>

### Temporally Efficient Vision Transformer for Video Instance Segmentation.
- **链接**: [arXiv:2204.08412](https://arxiv.org/abs/2204.08412) · [代码](https://github.com/hustvl/TeViT) · 📚 被引 76
- **作者**: Shusheng Yang, Xinggang Wang, Yu Li, Yuxin Fang, Jiemin Fang, Wenyu Liu et al.
- **🏷️ 机构**: School of EIC, Huazhong University of Science &#x0026; Technology, International Digital Economy Academy (IDEA), Applied Research Center (ARC), Tencent PCG
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently vision transformer has achieved tremendous success on image-level visual recognition tasks. To effectively and efficiently model the crucial temporal information within a video clip, we propose a Temporally Efficient Vision Transformer (TeViT) for video instance segmentation (VIS). Different from previous transformer-based VIS methods, TeViT is nearly convolution-free, which contains a transformer backbone and a query-based video instance segmentation head. In the backbone stage, we propose a nearly parameter-free messenger shift mechanism for early temporal context fusion. In the head stages, we propose a parameter-shared spatiotemporal query interaction mechanism to build the one-to-one correspondence between video instances and queries. Thus, TeViT fully utilizes both framelevel and instance-level temporal context information and obtains strong temporal modeling capacity with negligible extra computational cost. On three widely adopted VIS benchmarks, i.e., YouTube-VIS-2019, YouTube-VIS-2021, and OVIS, TeViT obtains state-of-the-art results and maintains high inference speed, e.g., 46.6 AP with 68.9 FPS on YouTube-VIS-2019. Code is available at https://github.com/hustvl/TeViT.

</details>

### Effectiveness of Vision Transformer for Fast and Accurate Single-Stage Pedestrian Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/afb8caec018d3c8f6ef8b81fa52386fe-Abstract-Conference.html) · 📚 被引 2
- **作者**: Jing Yuan, Panagiotis Barmpoutis, Tania Stathaki
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

## 跨领域论文（完整笔记在其他领域）

- Meta-attention for ViT-backed Continual Learning. → [continual-learning](../continual-learning/Guideline%202022.md)
- Continual Learning with Lifelong Vision Transformer. → [continual-learning](../continual-learning/Guideline%202022.md)
- MeMViT: Memory-Augmented Multiscale Vision Transformer for Efficient Long-Term Video Recognition. → [video-understanding](../video-understanding/Guideline%202022.md)

## 🆕 增量新增

### Meta-attention for ViT-backed Continual Learning. **⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2203.11684](https://arxiv.org/abs/2203.11684) · 📚 被引 44
- **作者**: Mengqi Xue, Haofei Zhang, Jie Song, Mingli Song
- **🏷️ 机构**: Zhejiang University
- **会议**: CVPR 2022
- **摘要（中）**: 针对视觉Transformer（ViT）在持续学习任务中性能退化的问题，本文提出了MEAT（MEta-ATtention）方法，通过元注意力机制对预训练ViT进行任务自适应。与Piggyback等全参数掩码方法不同，MEAT利用ViT的特性仅掩码部分参数，提高了效率和有效性。实验表明该方法在ViT-backed持续学习基准上优于现有方法。
- **摘要（英）**: This paper addresses the performance degradation of Vision Transformers (ViTs) in continual learning by proposing MEAT (MEta-ATtention), which adapts a pre-trained ViT to new tasks via meta-attention. Unlike full-parameter masking methods like Piggyback, MEAT masks only a subset of parameters, leveraging ViT characteristics for improved efficiency and effectiveness. Experiments show superior performance on ViT-backed continual learning benchmarks.
- **核心贡献**: 提出了一种针对ViT的元注意力掩码方法，实现高效持续学习。
- **创新点**: 利用ViT结构特性，仅掩码部分参数，提升效率。
- **结果**: 在ViT-backed持续学习任务中取得优于现有方法的性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning is a longstanding research topic due to its crucial role in tackling continually arriving tasks. Up to now, the study of continual learning in computer vision is mainly restricted to convolutional neural networks (CNNs). However, recently there is a tendency that the newly emerging vision transformers (ViTs) are gradually dominating the field of computer vision, which leaves CNN-based continual learning lagging behind as they can suffer from severe performance degradation if straightforwardly applied to ViTs. In this paper, we study ViT-backed continual learning to strive for higher performance riding on recent advances of ViTs. Inspired by mask-based continual learning methods in CNNs, where a mask is learned per task to adapt the pre-trained ViT to the new task, we propose MEta-ATtention (MEAT), i.e., attention to self-attention, to adapt a pre-trained ViT to new tasks without sacrificing performance on already learned tasks. Unlike prior mask-based methods like Piggyback, where all parameters are associated with corresponding masks, MEAT leverages the characteristics of ViTs and only masks a portion of its parameters. It renders MEAT more efficient and effective with less overhead and higher accuracy. Extensive experiments demonstrate that MEAT exhibits significant superiority to its state-of-the-art CNN counterparts, with 4.0~6.0% absolute boosts in accuracy. Our code has been released at https://github.com/zju-vipa/MEAT-TIL.

</details>

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

### ViT-NeT: Interpretable Vision Transformers with Neural Tree Decoder. **⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://proceedings.mlr.press/v162/kim22g.html)
- **作者**: Sangwon Kim, Jae-Yeal Nam, ByoungChul Ko
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022
- **摘要（中）**: ①该论文针对视觉Transformer（ViT）的可解释性问题，即模型决策过程难以理解。②提出了ViT-NeT，将神经树解码器与ViT结合，通过树结构进行层次化决策。③相比标准ViT的线性分类头，树解码器提供了更结构化的特征聚合和可解释的决策路径。④摘要未提供具体数据，但强调在保持性能的同时增强可解释性。
- **摘要（英）**: This paper addresses the interpretability issue of Vision Transformers by proposing ViT-NeT, which integrates a neural tree decoder for hierarchical decision-making. It improves upon standard linear heads by offering structured feature aggregation and interpretable paths. The abstract lacks quantitative results but emphasizes interpretability without sacrificing performance.
- **核心贡献**: 提出一种结合神经树解码器的ViT架构，增强模型可解释性。
- **创新点**: 将神经树结构引入ViT解码阶段，实现层次化决策。
- **结果**: 在保持性能的同时提供可解释的决策路径。

### Q-ViT: Accurate and Fully Quantized Low-bit Vision Transformer. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2210.06707](https://arxiv.org/abs/2210.06707) · 📚 被引 19
- **作者**: Yanjing Li, Sheng Xu, Baochang Zhang, Xianbin Cao, Peng Gao, Guodong Guo
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022
- **摘要（中）**: 针对低比特量化视觉Transformer（ViT）性能严重下降的问题，本文通过实证分析发现瓶颈在于低比特自注意力图的信息失真。提出了信息修正模块（IRM）和分布引导蒸馏（DGD）方案，用于全量化ViT（Q-ViT），有效消除失真。在DeiT和Swin骨干上评估，Q-ViT在ViT-S上理论加速6倍，性能优于先前方法。
- **摘要（英）**: This paper addresses the severe performance drop in low-bit quantized Vision Transformers (ViTs), identifying information distortion in quantized self-attention maps as the bottleneck. It proposes an Information Rectification Module (IRM) and a Distribution Guided Distillation (DGD) scheme for fully quantized ViTs (Q-ViT), achieving better performance than prior arts on DeiT and Swin backbones, with theoretical 6x acceleration on ViT-S.
- **核心贡献**: 提出IRM和DGD方案，实现全量化ViT的高精度压缩。
- **创新点**: 识别自注意力图信息失真为瓶颈，并设计针对性修正与蒸馏机制。
- **结果**: 在ViT-S上理论加速6倍，性能优于现有量化方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The large pre-trained vision transformers (ViTs) have demonstrated remarkable performance on various visual tasks, but suffer from expensive computational and memory cost problems when deployed on resource-constrained devices. Among the powerful compression approaches, quantization extremely reduces the computation and memory consumption by low-bit parameters and bit-wise operations. However, low-bit ViTs remain largely unexplored and usually suffer from a significant performance drop compared with the real-valued counterparts. In this work, through extensive empirical analysis, we first identify the bottleneck for severe performance drop comes from the information distortion of the low-bit quantized self-attention map. We then develop an information rectification module (IRM) and a distribution guided distillation (DGD) scheme for fully quantized vision transformers (Q-ViT) to effectively eliminate such distortion, leading to a fully quantized ViTs. We evaluate our methods on popular DeiT and Swin backbones. Extensive experimental results show that our method achieves a much better performance than the prior arts. For example, our Q-ViT can theoretically accelerates the ViT-S by 6.14x and achieves about 80.9% Top-1 accuracy, even surpassing the full-precision counterpart by 1.0% on ImageNet dataset. Our codes and models are attached on https://github.com/YanjingLi0202/Q-ViT

</details>

### Exploring Plain Vision Transformer Backbones for Object Detection. **⭐⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2203.16527](https://arxiv.org/abs/2203.16527) · 📚 被引 708
- **作者**: Yanghao Li, Hanzi Mao, Ross B. Girshick, Kaiming He
- **🏷️ 机构**: MIT
- **会议**: ECCV 2022
- **摘要（中）**: ①针对传统目标检测依赖层级骨干网络（如ResNet、Swin）的问题，探索了使用普通非层级ViT作为骨干的可行性。②提出了ViTDet检测器，通过最小化微调适配，利用MAE预训练的普通ViT骨干，并构建简单特征金字塔和窗口注意力机制。③相比已有层级骨干方法，该设计无需重新设计预训练架构，简化了检测流程，并证明了单尺度特征图和少量跨窗口传播块即可达到高性能。④在COCO数据集上，仅使用ImageNet-1K预训练，ViTDet达到了61.3 AP_box，与基于层级骨干的领先方法竞争。
- **摘要（英）**: This paper explores plain ViT backbones for object detection, proposing ViTDet with minimal adaptations like a simple feature pyramid and window attention. It achieves 61.3 AP_box on COCO with ImageNet-1K pre-training, competing with hierarchical backbone methods. The study highlights the potential of plain-backbone detectors.
- **核心贡献**: 提出了基于普通ViT骨干的ViTDet检测器，实现了与层级骨干方法相当的性能。
- **创新点**: 利用MAE预训练的普通ViT，通过简单特征金字塔和窗口注意力适配检测任务。
- **结果**: 在COCO上达到61.3 AP_box，仅需ImageNet-1K预训练。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We explore the plain, non-hierarchical Vision Transformer (ViT) as a backbone network for object detection. This design enables the original ViT architecture to be fine-tuned for object detection without needing to redesign a hierarchical backbone for pre-training. With minimal adaptations for fine-tuning, our plain-backbone detector can achieve competitive results. Surprisingly, we observe: (i) it is sufficient to build a simple feature pyramid from a single-scale feature map (without the common FPN design) and (ii) it is sufficient to use window attention (without shifting) aided with very few cross-window propagation blocks. With plain ViT backbones pre-trained as Masked Autoencoders (MAE), our detector, named ViTDet, can compete with the previous leading methods that were all based on hierarchical backbones, reaching up to 61.3 AP_box on the COCO dataset using only ImageNet-1K pre-training. We hope our study will draw attention to research on plain-backbone detectors. Code for ViTDet is available in Detectron2.

</details>

### ViTAS: Vision Transformer Architecture Search. **⭐⭐** (相关度: 40%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19803-8_9)
- **作者**: Xiu Su, Shan You, Jiyang Xie, Mingkai Zheng, Fei Wang, Chen Qian et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①该论文针对视觉Transformer架构搜索问题。②提出ViTAS方法，用于自动搜索高效的Vision Transformer架构。③相比手工设计，通过搜索优化架构性能。④由于摘要缺失，无法提供具体结果。
- **摘要（英）**: This paper addresses architecture search for Vision Transformers. It proposes ViTAS to automatically search efficient ViT architectures. Compared to manual design, it optimizes performance via search. Specific results are unavailable due to missing abstract.
- **核心贡献**: 提出视觉Transformer的架构搜索方法。
- **创新点**: 将NAS应用于ViT设计。
- **结果**: 未提供具体数据。

### MaxViT: Multi-axis Vision Transformer. **⭐⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2204.01697](https://arxiv.org/abs/2204.01697)
- **作者**: Zhengzhong Tu, Hossein Talebi, Han Zhang, Feng Yang, Peyman Milanfar, Alan C. Bovik et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①该论文针对自注意力机制在图像尺寸上可扩展性差的问题。②提出多轴注意力（multi-axis attention），包括分块局部和扩张全局注意力，实现线性复杂度，并设计MaxViT层级骨干网络，将注意力与卷积有效融合。③相比现有Transformer，能在任意分辨率下进行全局-局部交互，且早期高分辨率阶段也能全局感知。④在ImageNet-1K上达到86.5% top-1准确率，ImageNet-21K预训练后性能更优。
- **摘要（英）**: This paper addresses the scalability issue of self-attention with image size. It introduces multi-axis attention with blocked local and dilated global attention, achieving linear complexity, and proposes MaxViT, a hierarchical backbone blending attention with convolutions. Compared to existing Transformers, it enables global-local interactions at arbitrary resolutions and global perception even in early stages. It achieves 86.5% ImageNet-1K top-1 accuracy, with further gains from ImageNet-21K pretraining.
- **核心贡献**: 提出多轴注意力机制和MaxViT骨干网络。
- **创新点**: 线性复杂度的全局-局部注意力融合。
- **结果**: ImageNet-1K 86.5% top-1准确率。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Transformers have recently gained significant attention in the computer vision community. However, the lack of scalability of self-attention mechanisms with respect to image size has limited their wide adoption in state-of-the-art vision backbones. In this paper we introduce an efficient and scalable attention model we call multi-axis attention, which consists of two aspects: blocked local and dilated global attention. These design choices allow global-local spatial interactions on arbitrary input resolutions with only linear complexity. We also present a new architectural element by effectively blending our proposed attention model with convolutions, and accordingly propose a simple hierarchical vision backbone, dubbed MaxViT, by simply repeating the basic building block over multiple stages. Notably, MaxViT is able to ''see'' globally throughout the entire network, even in earlier, high-resolution stages. We demonstrate the effectiveness of our model on a broad spectrum of vision tasks. On image classification, MaxViT achieves state-of-the-art performance under various settings: without extra data, MaxViT attains 86.5% ImageNet-1K top-1 accuracy; with ImageNet-21K pre-training, our model achieves 88.7% top-1 accuracy. For downstream tasks, MaxViT as a backbone delivers favorable performance on object detection as well as visual aesthetic assessment. We also show that our proposed model expresses strong generative modeling capability on ImageNet, demonstrating the superior potential of MaxViT blocks as a universal vision module. The source code and trained models will be available at https://github.com/google-research/maxvit.

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

### CrossFormer: A Versatile Vision Transformer Hinging on Cross-scale Attention. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [出版页](https://openreview.net/forum?id=_PHymLIxuI) · 📚 被引 15
- **作者**: Wenxiao Wang, Lu Yao, Long Chen, Binbin Lin, Deng Cai, Xiaofei He et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022
- **摘要（中）**: ①该论文针对视觉Transformer中多尺度特征交互不足的问题，限制了模型对细粒度与全局信息的融合。②提出了CrossFormer，引入跨尺度注意力机制，通过动态生成多尺度token并交互。③相比标准ViT的固定patch划分，CrossFormer能自适应地捕捉不同尺度的特征，增强表示能力。④摘要未提供具体数据，但声称在多个视觉任务上达到SOTA。
- **摘要（英）**: This paper tackles the insufficient multi-scale feature interaction in Vision Transformers by proposing CrossFormer with cross-scale attention, which dynamically generates and interacts tokens across scales. It improves over fixed patch embeddings by enabling adaptive multi-scale representation. The abstract claims state-of-the-art performance across multiple vision tasks without specific numbers.
- **核心贡献**: 提出跨尺度注意力机制，增强ViT的多尺度特征融合能力。
- **创新点**: 动态生成多尺度token并实现跨尺度交互。
- **结果**: 在多个视觉任务上达到先进性能。

### RelViT: Concept-guided Vision Transformer for Visual Relational Reasoning. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2204.11167](https://arxiv.org/abs/2204.11167)
- **作者**: Xiaojian Ma, Weili Nie, Zhiding Yu, Huaizu Jiang, Chaowei Xiao, Yuke Zhu et al.
- **🏷️ 机构**: NVIDIA
- **会议**: ICLR 2022
- **摘要（中）**: ①该论文针对视觉关系推理中的系统泛化问题，即模型难以泛化到未见过的物体-关系组合。②提出了RelViT，引入概念特征字典和两个辅助任务（全局关系推理和局部物体中心对应学习），以增强ViT的推理能力。③相比标准ViT，RelViT显式利用概念（物体和关系）指导特征学习，提升泛化性。④在HICO和GQA基准上引入系统化划分，实验显示RelViT在系统泛化上显著优于基线。
- **摘要（英）**: This paper addresses systematic generalization in visual relational reasoning by proposing RelViT, which uses a concept-feature dictionary and two auxiliary tasks to guide ViT learning. It improves over standard ViTs by explicitly leveraging concepts for feature retrieval and reasoning. Experiments on systematic splits of HICO and GQA show significant gains over baselines.
- **核心贡献**: 提出概念引导的ViT方法，提升视觉关系推理的系统泛化能力。
- **创新点**: 引入概念特征字典和双辅助任务，实现概念驱动的特征学习。
- **结果**: 在HICO和GQA系统化划分上显著优于基线。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Reasoning about visual relationships is central to how humans interpret the visual world. This task remains challenging for current deep learning algorithms since it requires addressing three key technical problems jointly: 1) identifying object entities and their properties, 2) inferring semantic relations between pairs of entities, and 3) generalizing to novel object-relation combinations, i.e., systematic generalization. In this work, we use vision transformers (ViTs) as our base model for visual reasoning and make better use of concepts defined as object entities and their relations to improve the reasoning ability of ViTs. Specifically, we introduce a novel concept-feature dictionary to allow flexible image feature retrieval at training time with concept keys. This dictionary enables two new concept-guided auxiliary tasks: 1) a global task for promoting relational reasoning, and 2) a local task for facilitating semantic object-centric correspondence learning. To examine the systematic generalization of visual reasoning models, we introduce systematic splits for the standard HICO and GQA benchmarks. We show the resulting model, Concept-guided Vision Transformer (or RelViT for short) significantly outperforms prior approaches on HICO and GQA by 16% and 13% in the original split, and by 43% and 18% in the systematic split. Our ablation analyses also reveal our model's compatibility with multiple ViT variants and robustness to hyper-parameters.

</details>

### Discrete Representations Strengthen Vision Transformer Robustness. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2111.10493](https://arxiv.org/abs/2111.10493)
- **作者**: Chengzhi Mao, Lu Jiang, Mostafa Dehghani, Carl Vondrick, Rahul Sukthankar, Irfan Essa
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022
- **摘要（中）**: ①该论文针对ViT在ImageNet训练后过于依赖局部纹理、泛化到分布外数据能力不足的问题。②提出了在ViT输入层添加由向量量化编码器生成的离散token，替代标准连续像素token。③离散token对微小扰动不变且信息量更少，促使ViT学习全局不变特征。④实验表明，在四种ViT变体上，该方法在七个ImageNet鲁棒性基准上平均提升高达12%，同时保持ImageNet性能。
- **摘要（英）**: This paper addresses ViT's over-reliance on local textures and poor out-of-distribution generalization by adding discrete tokens from a vector-quantized encoder to the input layer. Discrete tokens are perturbation-invariant and less informative, encouraging global feature learning. Experiments show up to 12% average robustness improvement across seven benchmarks on four ViT variants while maintaining ImageNet accuracy.
- **核心贡献**: 提出离散表示增强ViT鲁棒性的简单有效方法。
- **创新点**: 利用向量量化编码器生成离散token，替代连续像素token。
- **结果**: 在七个鲁棒性基准上平均提升高达12%，且不损失ImageNet性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision Transformer (ViT) is emerging as the state-of-the-art architecture for image recognition. While recent studies suggest that ViTs are more robust than their convolutional counterparts, our experiments find that ViTs trained on ImageNet are overly reliant on local textures and fail to make adequate use of shape information. ViTs thus have difficulties generalizing to out-of-distribution, real-world data. To address this deficiency, we present a simple and effective architecture modification to ViT's input layer by adding discrete tokens produced by a vector-quantized encoder. Different from the standard continuous pixel tokens, discrete tokens are invariant under small perturbations and contain less information individually, which promote ViTs to learn global information that is invariant. Experimental results demonstrate that adding discrete representation on four architecture variants strengthens ViT robustness by up to 12% across seven ImageNet robustness benchmarks while maintaining the performance on ImageNet.

</details>

### MobileViT: Light-weight, General-purpose, and Mobile-friendly Vision Transformer.
- **链接**: [arXiv:2110.02178](https://arxiv.org/abs/2110.02178)
- **作者**: Sachin Mehta, Mohammad Rastegari
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Light-weight convolutional neural networks (CNNs) are the de-facto for mobile vision tasks. Their spatial inductive biases allow them to learn representations with fewer parameters across different vision tasks. However, these networks are spatially local. To learn global representations, self-attention-based vision trans-formers (ViTs) have been adopted. Unlike CNNs, ViTs are heavy-weight. In this paper, we ask the following question: is it possible to combine the strengths of CNNs and ViTs to build a light-weight and low latency network for mobile vision tasks? Towards this end, we introduce MobileViT, a light-weight and general-purpose vision transformer for mobile devices. MobileViT presents a different perspective for the global processing of information with transformers, i.e., transformers as convolutions. Our results show that MobileViT significantly outperforms CNN- and ViT-based networks across different tasks and datasets. On the ImageNet-1k dataset, MobileViT achieves top-1 accuracy of 78.4% with about 6 million parameters, which is 3.2% and 6.2% more accurate than MobileNetv3 (CNN-based) and DeIT (ViT-based) for a similar number of parameters. On the MS-COCO object detection task, MobileViT is 5.7% more accurate than MobileNetv3 for a similar number of parameters. Our source code is open-source and available at: https://github.com/apple/ml-cvnets

</details>

### Orthogonal Transformer: An Efficient Vision Transformer Backbone with Token Orthogonalization.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/5d8c01de2dc698c54201c1c7d0b86974-Abstract-Conference.html) · 📚 被引 2
- **作者**: Huaibo Huang, Xiaoqiang Zhou, Ran He
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Green Hierarchical Vision Transformer for Masked Image Modeling.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/7e487c72fce6e45879a78ee0872d991d-Abstract-Conference.html) · 📚 被引 9
- **作者**: Lang Huang, Shan You, Mingkai Zheng, Fei Wang, Chen Qian, Toshihiko Yamasaki
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### M³ViT: Mixture-of-Experts Vision Transformer for Efficient Multi-task Learning with Model-Accelerator Co-design.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/b653f34d576d1790481e3797cb740214-Abstract-Conference.html) · 📚 被引 10
- **作者**: Hanxue Liang, Zhiwen Fan, Rishov Sarkar, Ziyu Jiang, Tianlong Chen, Kai Zou et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Expediting Large-Scale Vision Transformer for Dense Prediction without Fine-tuning.
- **链接**: [arXiv:2210.01035](https://arxiv.org/abs/2210.01035)
- **作者**: Weicong Liang, Yuhui Yuan, Henghui Ding, Xiao Luo, Weihong Lin, Ding Jia et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision transformers have recently achieved competitive results across various vision tasks but still suffer from heavy computation costs when processing a large number of tokens. Many advanced approaches have been developed to reduce the total number of tokens in large-scale vision transformers, especially for image classification tasks. Typically, they select a small group of essential tokens according to their relevance with the class token, then fine-tune the weights of the vision transformer. Such fine-tuning is less practical for dense prediction due to the much heavier computation and GPU memory cost than image classification. In this paper, we focus on a more challenging problem, i.e., accelerating large-scale vision transformers for dense prediction without any additional re-training or fine-tuning. In response to the fact that high-resolution representations are necessary for dense prediction, we present two non-parametric operators, a token clustering layer to decrease the number of tokens and a token reconstruction layer to increase the number of tokens. The following steps are performed to achieve this: (i) we use the token clustering layer to cluster the neighboring tokens together, resulting in low-resolution representations that maintain the spatial structures; (ii) we apply the following transformer layers only to these low-resolution representations or clustered tokens; and (iii) we use the token reconstruction layer to re-create the high-resolution representations from the refined low-resolution representations. The results obtained by our method are promising on five dense prediction tasks, including object detection, semantic segmentation, panoptic segmentation, instance segmentation, and depth estimation.

</details>

### Peripheral Vision Transformer.
- **链接**: [arXiv:2206.06801](https://arxiv.org/abs/2206.06801)
- **作者**: Juhong Min, Yucheng Zhao, Chong Luo, Minsu Cho
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Human vision possesses a special type of visual processing systems called peripheral vision. Partitioning the entire visual field into multiple contour regions based on the distance to the center of our gaze, the peripheral vision provides us the ability to perceive various visual features at different regions. In this work, we take a biologically inspired approach and explore to model peripheral vision in deep neural networks for visual recognition. We propose to incorporate peripheral position encoding to the multi-head self-attention layers to let the network learn to partition the visual field into diverse peripheral regions given training data. We evaluate the proposed network, dubbed PerViT, on ImageNet-1K and systematically investigate the inner workings of the model for machine perception, showing that the network learns to perceive visual data similarly to the way that human vision does. The performance improvements in image classification over the baselines across different model sizes demonstrate the efficacy of the proposed method.

</details>

### ViTPose: Simple Vision Transformer Baselines for Human Pose Estimation.
- **链接**: [arXiv:2204.12484](https://arxiv.org/abs/2204.12484) · 📚 被引 142
- **作者**: Yufei Xu, Jing Zhang, Qiming Zhang, Dacheng Tao
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Although no specific domain knowledge is considered in the design, plain vision transformers have shown excellent performance in visual recognition tasks. However, little effort has been made to reveal the potential of such simple structures for pose estimation tasks. In this paper, we show the surprisingly good capabilities of plain vision transformers for pose estimation from various aspects, namely simplicity in model structure, scalability in model size, flexibility in training paradigm, and transferability of knowledge between models, through a simple baseline model called ViTPose. Specifically, ViTPose employs plain and non-hierarchical vision transformers as backbones to extract features for a given person instance and a lightweight decoder for pose estimation. It can be scaled up from 100M to 1B parameters by taking the advantages of the scalable model capacity and high parallelism of transformers, setting a new Pareto front between throughput and performance. Besides, ViTPose is very flexible regarding the attention type, input resolution, pre-training and finetuning strategy, as well as dealing with multiple pose tasks. We also empirically demonstrate that the knowledge of large ViTPose models can be easily transferred to small ones via a simple knowledge token. Experimental results show that our basic ViTPose model outperforms representative methods on the challenging MS COCO Keypoint Detection benchmark, while the largest model sets a new state-of-the-art. The code and models are available at https://github.com/ViTAE-Transformer/ViTPose.

</details>

### SAViT: Structure-Aware Vision Transformer Pruning via Collaborative Optimization.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/3b11c5cc84b6da2838db348b37dbd1a2-Abstract-Conference.html) · 📚 被引 6
- **作者**: Chuanyang Zheng, Zheyang Li, Kai Zhang, Zhi Yang, Wenming Tan, Jun Xiao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

## 跨领域论文（完整笔记在其他领域）

- V2X-ViT: Vehicle-to-Everything Cooperative Perception with Vision Transformer. → [autonomous-driving](../autonomous-driving/Guideline%202022.md)
- SimMIM: a Simple Framework for Masked Image Modeling. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
- Continual Learning with Lifelong Vision Transformer. → [continual-learning](../continual-learning/Guideline%202022.md)
- Training-free Transformer Architecture Search. → [neural-architecture-search](../neural-architecture-search/Guideline%202022.md)
- A Simple Single-Scale Vision Transformer for Object Detection and Instance Segmentation. → [object-detection](../object-detection/Guideline%202022.md)
- Open-Set Semi-Supervised Object Detection. → [open-set-detection](../open-set-detection/Guideline%202022.md)
- PPT: Token-Pruned Pose Transformer for Monocular and Multi-view Human Pose Estimation. → [network-pruning](../network-pruning/Guideline%202022.md)
- Online Continual Learning with Contrastive Vision Transformer. → [continual-learning](../continual-learning/Guideline%202022.md)
- UniNet: Unified Architecture Search with Convolution, Transformer, and MLP. → [neural-architecture-search](../neural-architecture-search/Guideline%202022.md)
- VTC-LFC: Vision Transformer Compression with Low-Frequency Components. → [network-pruning](../network-pruning/Guideline%202022.md)
<!-- COMPLETE v1 papers=39 -->
