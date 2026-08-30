# Vision Transformer — 2021 Guideline

> 领域: 视觉 Transformer（ViT、混合架构、高效注意力）
> 论文数: 9 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份:

### Swin Transformer: Hierarchical Vision Transformer using Shifted Windows.
- **链接**: [arXiv:2103.14030](https://arxiv.org/abs/2103.14030) · [代码](https://github.com/microsoft/Swin-Transformer) · 📚 被引 30009
- **作者**: Ze Liu, Yutong Lin, Yue Cao, Han Hu, Yixuan Wei, Zheng Zhang et al.
- **🏷️ 机构**: Microsoft Research Asia
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper presents a new vision Transformer, called Swin Transformer, that capably serves as a general-purpose backbone for computer vision. Challenges in adapting Transformer from language to vision arise from differences between the two domains, such as large variations in the scale of visual entities and the high resolution of pixels in images compared to words in text. To address these differences, we propose a hierarchical Transformer whose representation is computed with \textbf{S}hifted \textbf{win}dows. The shifted windowing scheme brings greater efficiency by limiting self-attention computation to non-overlapping local windows while also allowing for cross-window connection. This hierarchical architecture has the flexibility to model at various scales and has linear computational complexity with respect to image size. These qualities of Swin Transformer make it compatible with a broad range of vision tasks, including image classification (87.3 top-1 accuracy on ImageNet-1K) and dense prediction tasks such as object detection (58.7 box AP and 51.1 mask AP on COCO test-dev) and semantic segmentation (53.5 mIoU on ADE20K val). Its performance surpasses the previous state-of-the-art by a large margin of +2.7 box AP and +2.6 mask AP on COCO, and +3.2 mIoU on ADE20K, demonstrating the potential of Transformer-based models as vision backbones. The hierarchical design and the shifted window approach also prove beneficial for all-MLP architectures. The code and models are publicly available at~\url{https://github.com/microsoft/Swin-Transformer}.

</details>

### Tokens-to-Token ViT: Training Vision Transformers from Scratch on ImageNet.
- **链接**: [arXiv:2101.11986](https://arxiv.org/abs/2101.11986) · [代码](https://github.com/yitu-opensource/T2T-ViT) · 📚 被引 1967
- **作者**: Li Yuan, Yunpeng Chen, Tao Wang, Weihao Yu, Yujun Shi, Zihang Jiang et al.
- **🏷️ 机构**: National University of Singapore, YITU Technology
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Transformers, which are popular for language modeling, have been explored for solving vision tasks recently, e.g., the Vision Transformer (ViT) for image classification. The ViT model splits each image into a sequence of tokens with fixed length and then applies multiple Transformer layers to model their global relation for classification. However, ViT achieves inferior performance to CNNs when trained from scratch on a midsize dataset like ImageNet. We find it is because: 1) the simple tokenization of input images fails to model the important local structure such as edges and lines among neighboring pixels, leading to low training sample efficiency; 2) the redundant attention backbone design of ViT leads to limited feature richness for fixed computation budgets and limited training samples. To overcome such limitations, we propose a new Tokens-To-Token Vision Transformer (T2T-ViT), which incorporates 1) a layer-wise Tokens-to-Token (T2T) transformation to progressively structurize the image to tokens by recursively aggregating neighboring Tokens into one Token (Tokens-to-Token), such that local structure represented by surrounding tokens can be modeled and tokens length can be reduced; 2) an efficient backbone with a deep-narrow structure for vision transformer motivated by CNN architecture design after empirical study. Notably, T2T-ViT reduces the parameter count and MACs of vanilla ViT by half, while achieving more than 3.0\% improvement when trained from scratch on ImageNet. It also outperforms ResNets and achieves comparable performance with MobileNets by directly training on ImageNet. For example, T2T-ViT with comparable size to ResNet50 (21.5M parameters) can achieve 83.3\% top1 accuracy in image resolution 384$\times$384 on ImageNet. (Code: https://github.com/yitu-opensource/T2T-ViT)

</details>

### Multi-Scale Vision Longformer: A New Vision Transformer for High-Resolution Image Encoding.
- **链接**: [arXiv:2103.15358](https://arxiv.org/abs/2103.15358) · [代码](https://github.com/microsoft/vision-longformer) · 📚 被引 245
- **作者**: Pengchuan Zhang, Xiyang Dai, Jianwei Yang, Bin Xiao, Lu Yuan, Lei Zhang et al.
- **🏷️ 机构**: Microsoft Corporation, International Digital Economy Academy (IDEA)
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper presents a new Vision Transformer (ViT) architecture Multi-Scale Vision Longformer, which significantly enhances the ViT of \cite{dosovitskiy2020image} for encoding high-resolution images using two techniques. The first is the multi-scale model structure, which provides image encodings at multiple scales with manageable computational cost. The second is the attention mechanism of vision Longformer, which is a variant of Longformer \cite{beltagy2020longformer}, originally developed for natural language processing, and achieves a linear complexity w.r.t. the number of input tokens. A comprehensive empirical study shows that the new ViT significantly outperforms several strong baselines, including the existing ViT models and their ResNet counterparts, and the Pyramid Vision Transformer from a concurrent work \cite{wang2021pyramid}, on a range of vision tasks, including image classification, object detection, and segmentation. The models and source code are released at \url{https://github.com/microsoft/vision-longformer}.

</details>

### ViViT: A Video Vision Transformer.
- **链接**: [arXiv:2103.15691](https://arxiv.org/abs/2103.15691) · [代码](https://github.com/google-research/scenic) · 📚 被引 2388
- **作者**: Anurag Arnab, Mostafa Dehghani, Georg Heigold, Chen Sun, Mario Lucic, Cordelia Schmid
- **🏷️ 机构**: Google Research
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present pure-transformer based models for video classification, drawing upon the recent success of such models in image classification. Our model extracts spatio-temporal tokens from the input video, which are then encoded by a series of transformer layers. In order to handle the long sequences of tokens encountered in video, we propose several, efficient variants of our model which factorise the spatial- and temporal-dimensions of the input. Although transformer-based models are known to only be effective when large training datasets are available, we show how we can effectively regularise the model during training and leverage pretrained image models to be able to train on comparatively small datasets. We conduct thorough ablation studies, and achieve state-of-the-art results on multiple video classification benchmarks including Kinetics 400 and 600, Epic Kitchens, Something-Something v2 and Moments in Time, outperforming prior methods based on deep 3D convolutional networks. To facilitate further research, we release code at https://github.com/google-research/scenic/tree/main/scenic/projects/vivit

</details>

### CrossViT: Cross-Attention Multi-Scale Vision Transformer for Image Classification.
- **链接**: [arXiv:2103.14899](https://arxiv.org/abs/2103.14899) · [代码](https://github.com/IBM/CrossViT) · 📚 被引 1849
- **作者**: Chun-Fu (Richard) Chen, Quanfu Fan, Rameswar Panda
- **🏷️ 机构**: MIT-IBM Watson AI Lab
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The recently developed vision transformer (ViT) has achieved promising results on image classification compared to convolutional neural networks. Inspired by this, in this paper, we study how to learn multi-scale feature representations in transformer models for image classification. To this end, we propose a dual-branch transformer to combine image patches (i.e., tokens in a transformer) of different sizes to produce stronger image features. Our approach processes small-patch and large-patch tokens with two separate branches of different computational complexity and these tokens are then fused purely by attention multiple times to complement each other. Furthermore, to reduce computation, we develop a simple yet effective token fusion module based on cross attention, which uses a single token for each branch as a query to exchange information with other branches. Our proposed cross-attention only requires linear time for both computational and memory complexity instead of quadratic time otherwise. Extensive experiments demonstrate that our approach performs better than or on par with several concurrent works on vision transformer, in addition to efficient CNN models. For example, on the ImageNet1K dataset, with some architectural changes, our approach outperforms the recent DeiT by a large margin of 2\% with a small to moderate increase in FLOPs and model parameters. Our source codes and models are available at \url{https://github.com/IBM/CrossViT}.

</details>

### LeViT: a Vision Transformer in ConvNet's Clothing for Faster Inference.
- **链接**: [arXiv:2104.01136](https://arxiv.org/abs/2104.01136) · [代码](https://github.com/facebookresearch/LeViT) · 📚 被引 812
- **作者**: Benjamin Graham, Alaaeldin El-Nouby, Hugo Touvron, Pierre Stock, Armand Joulin, Hervé Jégou et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision Transformer has shown great visual representation power in substantial vision tasks such as recognition and detection, and thus been attracting fast-growing efforts on manually designing more effective architectures. In this paper, we propose to use neural architecture search to automate this process, by searching not only the architecture but also the search space. The central idea is to gradually evolve different search dimensions guided by their E-T Error computed using a weight-sharing supernet. Moreover, we provide design guidelines of general vision transformers with extensive analysis according to the space searching process, which could promote the understanding of vision transformer. Remarkably, the searched models, named S3 (short for Searching the Search Space), from the searched space achieve superior performance to recently proposed models, such as Swin, DeiT and ViT, when evaluated on ImageNet. The effectiveness of S3 is also illustrated on object detection, semantic segmentation and visual question answering, demonstrating its generality to downstream vision and vision-language tasks. Code and models will be available at https://github.com/microsoft/Cream.

</details>

### Pyramid Vision Transformer: A Versatile Backbone for Dense Prediction without Convolutions.
- **链接**: [arXiv:2102.12122](https://arxiv.org/abs/2102.12122) · [代码](https://github.com/whai362/PVT) · 📚 被引 4524
- **作者**: Wenhai Wang, Enze Xie, Xiang Li, Deng-Ping Fan, Kaitao Song, Ding Liang et al.
- **🏷️ 机构**: Nanjing University, The University of Hong Kong, Nanjing University of Science and Technology
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The transformer architectures, based on self-attention mechanism and convolution-free design, recently found superior performance and booming applications in computer vision. However, the discontinuous patch-wise tokenization process implicitly introduces jagged artifacts into attention maps, arising the traditional problem of aliasing for vision transformers. Aliasing effect occurs when discrete patterns are used to produce high frequency or continuous information, resulting in the indistinguishable distortions. Recent researches have found that modern convolution networks still suffer from this phenomenon. In this work, we analyze the uncharted problem of aliasing in vision transformer and explore to incorporate anti-aliasing properties. Specifically, we propose a plug-and-play Aliasing-Reduction Module(ARM) to alleviate the aforementioned issue. We investigate the effectiveness and generalization of the proposed method across multiple tasks and various vision transformer families. This lightweight design consistently attains a clear boost over several famous structures. Furthermore, our module also improves data efficiency and robustness of vision transformers.

</details>

### Adder Attention for Vision Transformer. **⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/a57e8915461b83adefb011530b711704-Abstract.html)
- **作者**: Han Shu, Jiahao Wang, Hanting Chen, Lin Li, Yujiu Yang, Yunhe Wang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021
- **摘要（中）**: 该论文针对视觉Transformer中的注意力机制，提出使用加法注意力替代标准乘法注意力，但摘要内容为空，无法获取具体方法细节。通常此类工作旨在降低计算复杂度或提升效率，通过加法操作减少乘法运算。由于缺乏摘要信息，无法评估其具体改进和效果。
- **摘要（英）**: This paper proposes Adder Attention for Vision Transformers, but the abstract is empty, so no specific method or results are available. Typically, such work aims to reduce computational complexity by replacing multiplication with addition.
- **核心贡献**: 未明确，因摘要缺失。
- **创新点**: 未明确，因摘要缺失。
- **结果**: 未明确，因摘要缺失。

### ViTAE: Vision Transformer Advanced by Exploring Intrinsic Inductive Bias. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2106.03348](https://arxiv.org/abs/2106.03348)
- **作者**: Yufei Xu, Qiming Zhang, Jing Zhang, Dacheng Tao
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021
- **摘要（中）**: 针对视觉Transformer缺乏内在归纳偏置（如局部性和尺度不变性）而依赖大规模训练数据的问题，该论文提出ViTAE，通过卷积探索内在归纳偏置。ViTAE使用空间金字塔缩减模块，利用不同膨胀率的卷积将图像下采样为具有丰富多尺度上下文的token，从而获得尺度不变性；并在每个Transformer层中并行卷积块与多头自注意力，融合特征后输入前馈网络，获得局部性。实验表明，ViTAE在多个视觉任务上表现优异，尤其在数据效率方面有显著提升。
- **摘要（英）**: This paper proposes ViTAE to address the lack of intrinsic inductive bias in Vision Transformers by incorporating convolutions. It uses spatial pyramid reduction modules for multi-scale context and parallel convolution blocks with self-attention for locality, achieving scale invariance and improved data efficiency. ViTAE demonstrates strong performance across various vision tasks.
- **核心贡献**: 提出ViTAE架构，通过卷积探索内在归纳偏置，增强ViT的局部性和尺度不变性。
- **创新点**: 在Transformer中集成多尺度卷积和并行卷积块，无需大规模数据即可学习鲁棒特征。
- **结果**: ViTAE在多个任务上取得优异性能，并显著提升数据效率。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Transformers have shown great potential in various computer vision tasks owing to their strong capability in modeling long-range dependency using the self-attention mechanism. Nevertheless, vision transformers treat an image as 1D sequence of visual tokens, lacking an intrinsic inductive bias (IB) in modeling local visual structures and dealing with scale variance. Alternatively, they require large-scale training data and longer training schedules to learn the IB implicitly. In this paper, we propose a novel Vision Transformer Advanced by Exploring intrinsic IB from convolutions, ie, ViTAE. Technically, ViTAE has several spatial pyramid reduction modules to downsample and embed the input image into tokens with rich multi-scale context by using multiple convolutions with different dilation rates. In this way, it acquires an intrinsic scale invariance IB and is able to learn robust feature representation for objects at various scales. Moreover, in each transformer layer, ViTAE has a convolution block in parallel to the multi-head self-attention module, whose features are fused and fed into the feed-forward network. Consequently, it has the intrinsic locality IB and is able to learn local features and global dependencies collaboratively. Experiments on ImageNet as well as downstream tasks prove the superiority of ViTAE over the baseline transformer and concurrent works. Source code and pretrained models will be available at GitHub.

</details>

### Vision Transformer with Progressive Sampling.
- **链接**: [arXiv:2108.01684](https://arxiv.org/abs/2108.01684) · [代码](https://github.com/yuexy/PS-ViT) · 📚 被引 106
- **作者**: Xiaoyu Yue, Shuyang Sun, Zhanghui Kuang, Meng Wei, Philip H. S. Torr, Wayne Zhang et al.
- **🏷️ 机构**: Centre for Perceptual and Interactive Intelligence, University of Oxford, SenseTime Research
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Transformers with powerful global relation modeling abilities have been introduced to fundamental computer vision tasks recently. As a typical example, the Vision Transformer (ViT) directly applies a pure transformer architecture on image classification, by simply splitting images into tokens with a fixed length, and employing transformers to learn relations between these tokens. However, such naive tokenization could destruct object structures, assign grids to uninterested regions such as background, and introduce interference signals. To mitigate the above issues, in this paper, we propose an iterative and progressive sampling strategy to locate discriminative regions. At each iteration, embeddings of the current sampling step are fed into a transformer encoder layer, and a group of sampling offsets is predicted to update the sampling locations for the next step. The progressive sampling is differentiable. When combined with the Vision Transformer, the obtained PS-ViT network can adaptively learn where to look. The proposed PS-ViT is both effective and efficient. When trained from scratch on ImageNet, PS-ViT performs 3.8% higher than the vanilla ViT in terms of top-1 accuracy with about $4\times$ fewer parameters and $10\times$ fewer FLOPs. Code is available at https://github.com/yuexy/PS-ViT.

</details>

## 🆕 增量新增

### Searching the Search Space of Vision Transformer. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2111.14725](https://arxiv.org/abs/2111.14725)
- **作者**: Minghao Chen, Kan Wu, Bolin Ni, Houwen Peng, Bei Liu, Jianlong Fu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021
- **摘要（中）**: ①针对视觉Transformer架构设计依赖人工经验、搜索空间有限的问题，提出自动化搜索架构和搜索空间的方法。②通过权重共享超网络计算E-T Error，逐步演化不同的搜索维度，从而优化搜索空间。③提供了通用视觉Transformer的设计指南，并基于搜索空间得到S3模型。④在ImageNet上，S3模型性能优于Swin、DeiT和ViT，并在目标检测、语义分割和视觉问答等下游任务上验证了泛化性。
- **摘要（英）**: This paper automates the design of vision transformers by searching both the architecture and the search space, using E-T Error from a weight-sharing supernet to guide evolution. It provides design guidelines and produces the S3 model, which outperforms Swin, DeiT, and ViT on ImageNet and shows strong generalization on downstream tasks like detection and segmentation.
- **核心贡献**: 提出了一种同时搜索架构和搜索空间的NAS方法，并生成高性能的S3模型。
- **创新点**: 利用E-T Error动态演化搜索维度，突破了固定搜索空间的限制。
- **结果**: S3模型在ImageNet及多个下游任务上达到领先性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision Transformer has shown great visual representation power in substantial vision tasks such as recognition and detection, and thus been attracting fast-growing efforts on manually designing more effective architectures. In this paper, we propose to use neural architecture search to automate this process, by searching not only the architecture but also the search space. The central idea is to gradually evolve different search dimensions guided by their E-T Error computed using a weight-sharing supernet. Moreover, we provide design guidelines of general vision transformers with extensive analysis according to the space searching process, which could promote the understanding of vision transformer. Remarkably, the searched models, named S3 (short for Searching the Search Space), from the searched space achieve superior performance to recently proposed models, such as Swin, DeiT and ViT, when evaluated on ImageNet. The effectiveness of S3 is also illustrated on object detection, semantic segmentation and visual question answering, demonstrating its generality to downstream vision and vision-language tasks. Code and models will be available at https://github.com/microsoft/Cream.

</details>

### Post-Training Quantization for Vision Transformer. **⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/ec8956637a99787bd197eacd77acce5e-Abstract.html)
- **作者**: Zhenhua Liu, Yunhe Wang, Kai Han, Wei Zhang, Siwei Ma, Wen Gao
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021
- **摘要（中）**: ①针对视觉Transformer在部署时计算和存储开销大的问题，探索后训练量化方法。②摘要内容不完整，但推测提出了针对ViT的量化技术，以减少模型大小和推理延迟。③相比已有量化方法，可能针对ViT的自注意力机制进行了优化。④具体效果未在摘要中提供。
- **摘要（英）**: This paper addresses the deployment challenges of vision transformers by exploring post-training quantization techniques. The abstract is incomplete, but it likely proposes methods to reduce model size and inference latency, potentially tailored to the self-attention mechanism. Specific results are not available in the abstract.
- **核心贡献**: 探索了视觉Transformer的后训练量化方法。
- **创新点**: 可能针对ViT结构特性设计量化策略。
- **结果**: 效果未在摘要中明确。

### Blending Anti-Aliasing into Vision Transformer. **⭐⭐⭐⭐** (相关度: 65%)
- **链接**: [arXiv:2110.15156](https://arxiv.org/abs/2110.15156)
- **作者**: Shengju Qian, Hao Shao, Yi Zhu, Mu Li, Jiaya Jia
- **🏷️ 机构**: AWS / CMU, CUHK / SmartMore
- **会议**: NeurIPS 2021
- **摘要（中）**: ①针对视觉Transformer中patch-wise tokenization引入的锯齿伪影（混叠效应）问题，影响注意力图质量。②提出即插即用的Aliasing-Reduction Module（ARM）模块，融入反混叠特性。③该模块轻量级，可应用于多种ViT结构，并提升数据效率和鲁棒性。④在多个任务和ViT家族上验证，持续获得性能提升。
- **摘要（英）**: This paper identifies the aliasing problem in vision transformers caused by patch-wise tokenization and proposes a plug-and-play Aliasing-Reduction Module (ARM) to mitigate it. The lightweight module improves performance across multiple tasks and ViT variants, while also enhancing data efficiency and robustness.
- **核心贡献**: 提出了ARM模块，有效缓解ViT中的混叠效应。
- **创新点**: 将反混叠设计引入ViT，作为即插即用组件。
- **结果**: 在多个任务上获得性能提升，并增强鲁棒性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The transformer architectures, based on self-attention mechanism and convolution-free design, recently found superior performance and booming applications in computer vision. However, the discontinuous patch-wise tokenization process implicitly introduces jagged artifacts into attention maps, arising the traditional problem of aliasing for vision transformers. Aliasing effect occurs when discrete patterns are used to produce high frequency or continuous information, resulting in the indistinguishable distortions. Recent researches have found that modern convolution networks still suffer from this phenomenon. In this work, we analyze the uncharted problem of aliasing in vision transformer and explore to incorporate anti-aliasing properties. Specifically, we propose a plug-and-play Aliasing-Reduction Module(ARM) to alleviate the aforementioned issue. We investigate the effectiveness and generalization of the proposed method across multiple tasks and various vision transformer families. This lightweight design consistently attains a clear boost over several famous structures. Furthermore, our module also improves data efficiency and robustness of vision transformers.

</details>

### Glance-and-Gaze Vision Transformer. **⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2106.02277](https://arxiv.org/abs/2106.02277)
- **作者**: Qihang Yu, Yingda Xia, Yutong Bai, Yongyi Lu, Alan L. Yuille, Wei Shen
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021
- **摘要（中）**: ①针对视觉Transformer中自注意力机制对输入序列长度呈二次复杂度，导致高分辨率特征图上的密集预测任务计算和内存开销过大的问题。②提出了Glance-and-Gaze Transformer（GG-Transformer），通过两个并行分支模拟人类识别物体时的“扫视”和“凝视”行为：Glance分支在自适应膨胀划分的局部区域上执行自注意力以高效建模长距离依赖，Gaze分支则建模局部上下文。③相比现有Transformer，该方法在保持全局建模能力的同时显著降低计算复杂度，并兼顾局部细节。④实验表明，GG-Transformer在多个视觉任务上以更紧凑的模型尺寸取得了优于传统CNN和现有ViT的性能，但摘要未提供具体数值。
- **摘要（英）**: This paper addresses the quadratic complexity of self-attention in vision Transformers, which hinders dense prediction tasks on high-resolution feature maps. It proposes the Glance-and-Gaze Transformer (GG-Transformer) with two parallel branches: a Glance branch for efficient long-range dependency modeling via self-attention on adaptively dilated partitions, and a Gaze branch for local context. The method achieves superior performance with a more compact model size compared to CNNs and existing ViTs, though specific metrics are not detailed in the abstract.
- **核心贡献**: 提出GG-Transformer，通过Glance和Gaze双分支并行机制，在降低自注意力复杂度的同时兼顾全局和局部特征建模。
- **创新点**: 将人类视觉的扫视-凝视行为引入Transformer设计，采用自适应膨胀分区实现高效全局建模。
- **结果**: 在多个视觉任务上以更小模型尺寸取得优于传统CNN和现有ViT的性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, there emerges a series of vision Transformers, which show superior performance with a more compact model size than conventional convolutional neural networks, thanks to the strong ability of Transformers to model long-range dependencies. However, the advantages of vision Transformers also come with a price: Self-attention, the core part of Transformer, has a quadratic complexity to the input sequence length. This leads to a dramatic increase of computation and memory cost with the increase of sequence length, thus introducing difficulties when applying Transformers to the vision tasks that require dense predictions based on high-resolution feature maps. In this paper, we propose a new vision Transformer, named Glance-and-Gaze Transformer (GG-Transformer), to address the aforementioned issues. It is motivated by the Glance and Gaze behavior of human beings when recognizing objects in natural scenes, with the ability to efficiently model both long-range dependencies and local context. In GG-Transformer, the Glance and Gaze behavior is realized by two parallel branches: The Glance branch is achieved by performing self-attention on the adaptively-dilated partitions of the input, which leads to a linear complexity while still enjoying a global receptive field; The Gaze branch is implemented by a simple depth-wise convolutional layer, which compensates local image context to the features obtained by the Glance mechanism. We empirically demonstrate our method achieves consistently superior performance over previous state-of-the-art Transformers on various vision tasks and benchmarks. The codes and models will be made available at https://github.com/yucornetto/GG-Transformer.

</details>

### HRFormer: High-Resolution Vision Transformer for Dense Predict. **⭐⭐⭐** (相关度: 75%)
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/3bbfdde8842a5c44a0323518eec97cbe-Abstract.html)
- **作者**: Yuhui Yuan, Rao Fu, Lang Huang, Weihong Lin, Chao Zhang, Xilin Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021
- **摘要（中）**: ①针对高分辨率视觉Transformer在密集预测任务（如语义分割、目标检测）中计算成本高、难以保持高分辨率表示的问题。②提出了HRFormer，一种高分辨率视觉Transformer，通过并行多分支结构在不同分辨率下处理特征，并引入高效的自注意力机制以降低计算复杂度。③相比现有Transformer，HRFormer保留了高分辨率特征图，更适合密集预测，同时通过局部自注意力减少计算量。④实验表明，HRFormer在多个密集预测基准上取得了与Swin Transformer等先进方法相当或更优的性能，但摘要未提供具体数据。
- **摘要（英）**: This paper tackles the high computational cost and difficulty of maintaining high-resolution representations in vision Transformers for dense prediction tasks. It proposes HRFormer, a high-resolution vision Transformer with parallel multi-branch processing at different resolutions and efficient self-attention mechanisms. The method achieves competitive or better performance than advanced models like Swin Transformer on dense prediction benchmarks, though specific numbers are not given in the abstract.
- **核心贡献**: 提出HRFormer，一种保持高分辨率特征并高效建模的视觉Transformer，适用于密集预测任务。
- **创新点**: 通过并行多分支结构和局部自注意力，在高分辨率下实现高效全局建模。
- **结果**: 在多个密集预测基准上取得与先进方法相当或更优的性能。

### Learning Generative Vision Transformer with Energy-Based Latent Space for Saliency Prediction. **⭐⭐⭐** (相关度: 50%)
- **链接**: [arXiv:2112.13528](https://arxiv.org/abs/2112.13528)
- **作者**: Jing Zhang, Jianwen Xie, Nick Barnes, Ping Li
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021
- **摘要（中）**: ①针对现有生成式视觉Transformer在显著目标检测中，潜变量先验分布简单（如各向同性高斯），难以捕捉复杂数据分布的问题。②提出了一种生成式视觉Transformer，其潜变量遵循基于能量的信息先验，并通过马尔可夫链蒙特卡洛最大似然估计联合训练Transformer和先验模型，使用Langevin动力学采样。③相比现有生成模型，该方法采用更具表达力的能量先验，并能从图像中生成像素级不确定性图，指示模型预测置信度。④在RGB和RGB-D显著目标检测任务上，实验表明该方法不仅获得了准确的显著性预测，还提供了不确定性估计，但摘要未给出具体数值。
- **摘要（英）**: This paper addresses the limitation of simple isotropic Gaussian priors in generative vision Transformers for salient object detection. It proposes a generative vision Transformer with an energy-based informative prior for latent variables, trained via MCMC-based maximum likelihood estimation with Langevin dynamics. The method achieves accurate saliency prediction and pixel-wise uncertainty maps on RGB and RGB-D tasks, though specific metrics are not provided in the abstract.
- **核心贡献**: 提出基于能量先验的生成式视觉Transformer，用于显著目标检测和不确定性估计。
- **创新点**: 用能量先验替代高斯先验，并通过Langevin动力学联合训练。
- **结果**: 在RGB和RGB-D显著目标检测上取得准确预测和不确定性图。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision transformer networks have shown superiority in many computer vision tasks. In this paper, we take a step further by proposing a novel generative vision transformer with latent variables following an informative energy-based prior for salient object detection. Both the vision transformer network and the energy-based prior model are jointly trained via Markov chain Monte Carlo-based maximum likelihood estimation, in which the sampling from the intractable posterior and prior distributions of the latent variables are performed by Langevin dynamics. Further, with the generative vision transformer, we can easily obtain a pixel-wise uncertainty map from an image, which indicates the model confidence in predicting saliency from the image. Different from the existing generative models which define the prior distribution of the latent variables as a simple isotropic Gaussian distribution, our model uses an energy-based informative prior which can be more expressive to capture the latent space of the data. We apply the proposed framework to both RGB and RGB-D salient object detection tasks. Extensive experimental results show that our framework can achieve not only accurate saliency predictions but also meaningful uncertainty maps that are consistent with the human perception.

</details>

### MST: Masked Self-Supervised Transformer for Visual Representation. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2106.05656](https://arxiv.org/abs/2106.05656)
- **作者**: Zhaowen Li, Zhiyang Chen, Fan Yang, Wei Li, Yousong Zhu, Chaoyang Zhao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021
- **摘要（中）**: ①针对视觉自监督预训练中，现有方法仅关注全局高层特征，难以迁移到依赖局部特征的密集预测任务（如目标检测、语义分割）的问题。②提出了掩码自监督Transformer（MST），基于多头自注意力图动态掩码局部补丁的token，同时保留关键结构，并通过全局图像解码器恢复掩码token，以保留空间信息。③相比现有自监督方法，MST显式捕获局部上下文，同时保持全局语义，更适合下游密集预测任务。④在多个数据集上的实验表明，MST在多个下游任务上取得了有效性和泛化性，但摘要未提供具体数值。
- **摘要（英）**: This paper addresses the limitation of visual self-supervised pre-training methods that focus only on global features, which fail to transfer to dense prediction tasks requiring local context. It proposes Masked Self-supervised Transformer (MST), which dynamically masks tokens based on multi-head self-attention maps and recovers them with a global decoder to preserve spatial information. The method demonstrates effectiveness and generalization on multiple datasets, though specific metrics are not detailed in the abstract.
- **核心贡献**: 提出MST，一种基于注意力图动态掩码的自监督Transformer，兼顾局部和全局特征。
- **创新点**: 利用自注意力图指导掩码，并通过全局解码器恢复，增强空间信息保留。
- **结果**: 在多个数据集上验证了有效性和泛化性，适用于下游密集预测任务。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Transformer has been widely used for self-supervised pre-training in Natural Language Processing (NLP) and achieved great success. However, it has not been fully explored in visual self-supervised learning. Meanwhile, previous methods only consider the high-level feature and learning representation from a global perspective, which may fail to transfer to the downstream dense prediction tasks focusing on local features. In this paper, we present a novel Masked Self-supervised Transformer approach named MST, which can explicitly capture the local context of an image while preserving the global semantic information. Specifically, inspired by the Masked Language Modeling (MLM) in NLP, we propose a masked token strategy based on the multi-head self-attention map, which dynamically masks some tokens of local patches without damaging the crucial structure for self-supervised learning. More importantly, the masked tokens together with the remaining tokens are further recovered by a global image decoder, which preserves the spatial information of the image and is more friendly to the downstream dense prediction tasks. The experiments on multiple datasets demonstrate the effectiveness and generality of the proposed method. For instance, MST achieves Top-1 accuracy of 76.9% with DeiT-S only using 300-epoch pre-training by linear evaluation, which outperforms supervised methods with the same epoch by 0.4% and its comparable variant DINO by 1.0\%. For dense prediction tasks, MST also achieves 42.7% mAP on MS COCO object detection and 74.04% mIoU on Cityscapes segmentation only with 100-epoch pre-training.

</details>

## 跨领域论文（完整笔记在其他领域）

- History Aware Multimodal Transformer for Vision-and-Language Navigation. → [multimodal](../multimodal/Guideline%202021.md)
- VATT: Transformers for Multimodal Self-Supervised Learning from Raw Video, Audio and Text. → [self-supervised-vision](../self-supervised-vision/Guideline%202021.md)
- Chasing Sparsity in Vision Transformers: An End-to-End Exploration. → [network-pruning](../network-pruning/Guideline%202021.md)

<!-- COMPLETE v1 papers=17 -->
