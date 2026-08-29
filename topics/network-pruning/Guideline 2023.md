# Network Pruning — 2023 Guideline

> 领域: 网络剪枝 / 模型压缩（结构化剪枝、稀疏化）
> 论文数: 18 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Efficient Hierarchical Entropy Model for Learned Point Cloud Compression.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01381) · 📚 被引 76
- **作者**: Rui Song, Chunyang Fu, Shan Liu, Ge Li
- **🏷️ 机构**: School of Electronic and Computer Engineering, Shenzhen Graduate Scool, Peking University, Tencent America
- **会议**: CVPR 2023

### SparseViT: Revisiting Activation Sparsity for Efficient High-Resolution Vision Transformer.
- **链接**: [arXiv:2303.17605](https://arxiv.org/abs/2303.17605) · 📚 被引 63
- **作者**: Xuanyao Chen, Zhijian Liu, Haotian Tang, Li Yi, Hang Zhao, Song Han
- **🏷️ 机构**: Shanghai Qi Zhi Institute, MIT
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> High-resolution images enable neural networks to learn richer visual representations. However, this improved performance comes at the cost of growing computational complexity, hindering their usage in latency-sensitive applications. As not all pixels are equal, skipping computations for less-important regions offers a simple and effective measure to reduce the computation. This, however, is hard to be translated into actual speedup for CNNs since it breaks the regularity of the dense convolution workload. In this paper, we introduce SparseViT that revisits activation sparsity for recent window-based vision transformers (ViTs). As window attentions are naturally batched over blocks, actual speedup with window activation pruning becomes possible: i.e., ~50% latency reduction with 60% sparsity. Different layers should be assigned with different pruning ratios due to their diverse sensitivities and computational costs. We introduce sparsity-aware adaptation and apply the evolutionary search to efficiently find the optimal layerwise sparsity configuration within the vast search space. SparseViT achieves speedups of 1.5x, 1.4x, and 1.3x compared to its dense counterpart in monocular 3D object detection, 2D instance segmentation, and 2D semantic segmentation, respectively, with negligible to no loss of accuracy.

</details>

### Joint Token Pruning and Squeezing Towards More Aggressive Compression of Vision Transformers.
- **链接**: [arXiv:2304.10716](https://arxiv.org/abs/2304.10716) · [代码](https://github.com/megvii-research/TPS-CVPR2023) · 📚 被引 75
- **作者**: Siyuan Wei, Tianzhu Ye, Shen Zhang, Yao Tang, Jiajun Liang
- **🏷️ 机构**: MEGVII Technology, Tsinghua University
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision transformers have achieved leading performance on various visual tasks yet still suffer from high computational complexity. The situation deteriorates in dense prediction tasks like semantic segmentation, as high-resolution inputs and outputs usually imply more tokens involved in computations. Directly removing the less attentive tokens has been discussed for the image classification task but can not be extended to semantic segmentation since a dense prediction is required for every patch. To this end, this work introduces a Dynamic Token Pruning (DToP) method based on the early exit of tokens for semantic segmentation. Motivated by the coarse-to-fine segmentation process by humans, we naturally split the widely adopted auxiliary-loss-based network architecture into several stages, where each auxiliary block grades every token's difficulty level. We can finalize the prediction of easy tokens in advance without completing the entire forward pass. Moreover, we keep $k$ highest confidence tokens for each semantic category to uphold the representative context information. Thus, computational complexity will change with the difficulty of the input, akin to the way humans do segmentation. Experiments suggest that the proposed DToP architecture reduces on average $20\% - 35\%$ of computational cost for current semantic segmentation methods based on plain vision transformers without accuracy degradation.

</details>

### DiffRate : Differentiable Compression Rate for Efficient Vision Transformers.
- **链接**: [arXiv:2305.17997](https://arxiv.org/abs/2305.17997) · [代码](https://github.com/OpenGVLab/DiffRate) · 📚 被引 38
- **作者**: Mengzhao Chen, Wenqi Shao, Peng Xu, Mingbao Lin, Kaipeng Zhang, Fei Chao et al.
- **🏷️ 机构**: Xiamen University,Key Laboratory of Multimedia Trusted Perception and Efficient Computing, Ministry of Education of China, School of Informatics, Shanghai AI Laboratory,OpenGVLab, Tencent Holdings Ltd
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Token compression aims to speed up large-scale vision transformers (e.g. ViTs) by pruning (dropping) or merging tokens. It is an important but challenging task. Although recent advanced approaches achieved great success, they need to carefully handcraft a compression rate (i.e. number of tokens to remove), which is tedious and leads to sub-optimal performance. To tackle this problem, we propose Differentiable Compression Rate (DiffRate), a novel token compression method that has several appealing properties prior arts do not have. First, DiffRate enables propagating the loss function's gradient onto the compression ratio, which is considered as a non-differentiable hyperparameter in previous work. In this case, different layers can automatically learn different compression rates layer-wisely without extra overhead. Second, token pruning and merging can be naturally performed simultaneously in DiffRate, while they were isolated in previous works. Third, extensive experiments demonstrate that DiffRate achieves state-of-the-art performance. For example, by applying the learned layer-wise compression rates to an off-the-shelf ViT-H (MAE) model, we achieve a 40% FLOPs reduction and a 1.5x throughput improvement, with a minor accuracy drop of 0.16% on ImageNet without fine-tuning, even outperforming previous methods with fine-tuning. Codes and models are available at https://github.com/OpenGVLab/DiffRate.

</details>

### Single-Shot Pruning for Pre-trained Models: Rethinking the Importance of Magnitude Pruning.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00155) · 📚 被引 13
- **作者**: Hirokazu Kohama, Hiroaki Minoura, Tsubasa Hirakawa, Takayoshi Yamashita, Hironobu Fujiyoshi
- **🏷️ 机构**: Chubu University
- **会议**: ICCV 2023

### Automatic Network Pruning via Hilbert-Schmidt Independence Criterion Lasso under Information Bottleneck Principle.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01601) · 📚 被引 22
- **作者**: Song Guo, Lei Zhang, Xiawu Zheng, Yan Wang, Yuchao Li, Fei Chao et al.
- **🏷️ 机构**: Xiamen University,Key Laboratory of Multimedia Trusted Perception and Efficient Computing, Ministry of Education of China,Department of Artificial Intelligence, School of Informatics, Samsara Inc, Alibaba Group
- **会议**: ICCV 2023

### Unified Data-Free Compression: Pruning and Quantization without Fine-Tuning.
- **链接**: [arXiv:2308.07209](https://arxiv.org/abs/2308.07209) · 📚 被引 22
- **作者**: Shipeng Bai, Jun Chen, Xintian Shen, Yixuan Qian, Yong Liu
- **🏷️ 机构**: Zhejiang University,College of Control Science and Engineering
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Structured pruning and quantization are promising approaches for reducing the inference time and memory footprint of neural networks. However, most existing methods require the original training dataset to fine-tune the model. This not only brings heavy resource consumption but also is not possible for applications with sensitive or proprietary data due to privacy and security concerns. Therefore, a few data-free methods are proposed to address this problem, but they perform data-free pruning and quantization separately, which does not explore the complementarity of pruning and quantization. In this paper, we propose a novel framework named Unified Data-Free Compression(UDFC), which performs pruning and quantization simultaneously without any data and fine-tuning process. Specifically, UDFC starts with the assumption that the partial information of a damaged(e.g., pruned or quantized) channel can be preserved by a linear combination of other channels, and then derives the reconstruction form from the assumption to restore the information loss due to compression. Finally, we formulate the reconstruction error between the original network and its compressed network, and theoretically deduce the closed-form solution. We evaluate the UDFC on the large-scale image classification task and obtain significant improvements over various network architectures and compression methods. For example, we achieve a 20.54% accuracy improvement on ImageNet dataset compared to SOTA method with 30% pruning ratio and 6-bit quantization on ResNet-34.

</details>

### Hunting Sparsity: Density-Guided Contrastive Learning for Semi-Supervised Semantic Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00304) · 📚 被引 56
- **作者**: Xiaoyang Wang, Bingfeng Zhang, Limin Yu, Jimin Xiao
- **🏷️ 机构**: XJTLU, China University of Petroleum (East China)
- **会议**: CVPR 2023

### DepGraph: Towards Any Structural Pruning.
- **链接**: [arXiv:2301.12900](https://arxiv.org/abs/2301.12900) · 📚 被引 451
- **作者**: Gongfan Fang, Xinyin Ma, Mingli Song, Michael Bi Mi, Xinchao Wang
- **🏷️ 机构**: National University of Singapore, Zhejiang University, Huawei Technologies Ltd.
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Structural pruning enables model acceleration by removing structurally-grouped parameters from neural networks. However, the parameter-grouping patterns vary widely across different models, making architecture-specific pruners, which rely on manually-designed grouping schemes, non-generalizable to new architectures. In this work, we study a highly-challenging yet barely-explored task, any structural pruning, to tackle general structural pruning of arbitrary architecture like CNNs, RNNs, GNNs and Transformers. The most prominent obstacle towards this goal lies in the structural coupling, which not only forces different layers to be pruned simultaneously, but also expects all removed parameters to be consistently unimportant, thereby avoiding structural issues and significant performance degradation after pruning. To address this problem, we propose a general and {fully automatic} method, \emph{Dependency Graph} (DepGraph), to explicitly model the dependency between layers and comprehensively group coupled parameters for pruning. In this work, we extensively evaluate our method on several architectures and tasks, including ResNe(X)t, DenseNet, MobileNet and Vision transformer for images, GAT for graph, DGCNN for 3D point cloud, alongside LSTM for language, and demonstrate that, even with a simple norm-based criterion, the proposed method consistently yields gratifying performances.

</details>

### CP3: Channel Pruning Plug-in for Point-Based Networks.
- **链接**: [arXiv:2303.13097](https://arxiv.org/abs/2303.13097)
- **作者**: Yaomin Huang, Ning Liu, Zhengping Che, Zhiyuan Xu, Chaomin Shen, Yaxin Peng et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep learning algorithms are increasingly employed at the edge. However, edge devices are resource constrained and thus require efficient deployment of deep neural networks. Pruning methods are a key tool for edge deployment as they can improve storage, compute, memory bandwidth, and energy usage. In this paper we propose a novel accurate pruning technique that allows precise control over the output network size. Our method uses an efficient optimal transportation scheme which we make end-to-end differentiable and which automatically tunes the exploration-exploitation behavior of the algorithm to find accurate sparse sub-networks. We show that our method achieves state-of-the-art performance compared to previous pruning methods on 3 different datasets, using 5 different models, across a wide range of pruning ratios, and with two types of sparsity budgets and pruning granularities.

</details>

### Progressive Neighbor Consistency Mining for Correspondence Pruning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00919) · 📚 被引 33
- **作者**: Xin Liu, Jufeng Yang
- **🏷️ 机构**: College of Computer Science, Nankai University,TMCC,China
- **会议**: CVPR 2023

### Training Debiased Subnetworks with Contrastive Weight Pruning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00766) · 📚 被引 12
- **作者**: Geon Yeong Park, Sangmin Lee, Sang Wan Lee, Jong Chul Ye
- **🏷️ 机构**: Bio and Brain Engineering, Mathematical Sciences
- **会议**: CVPR 2023

### Out-of-Distributed Semantic Pruning for Robust Semi-Supervised Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02284) · 📚 被引 10
- **作者**: Yu Wang, Pengchong Qiao, Chang Liu, Guoli Song, Xiawu Zheng, Jie Chen
- **🏷️ 机构**: School of Electronic and Computer Engineering, Peking University,Shenzhen,China, Tsinghua University,Department of Automation and BNRist,Beijing,China, Peng Cheng Laboratory,Shenzhen,China
- **会议**: CVPR 2023

### Pruning Parameterization with Bi-level Optimization for Efficient Semantic Segmentation on the Edge.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01478) · 📚 被引 22
- **作者**: Changdi Yang, Pu Zhao, Yanyu Li, Wei Niu, Jiexiong Guan, Hao Tang et al.
- **🏷️ 机构**: Northeastern University, College of William &#x0026; Mary, ETH Zurich,CVL
- **会议**: CVPR 2023

### Ultrahigh Resolution Image/Video Matting with Spatio-Temporal Sparsity.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01356)
- **作者**: Yanan Sun, Chi-Keung Tang, Yu-Wing Tai
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### Adaptive Channel Sparsity for Federated Learning under System Heterogeneity.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01957) · 📚 被引 12
- **作者**: Dongping Liao, Xitong Gao, Yiren Zhao, Chengzhong Xu
- **🏷️ 机构**: University of Macau,State Key Lab of IoTSC,CIS Dept,Macau SAR,China, Shenzhen Institutes of Advanced Technology, Chinese Academy of Sciences,Shenzhen,China, Imperial College London,London,UK
- **会议**: CVPR 2023

### Structured Sparsity Learning for Efficient Video Super-Resolution.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02168) · 📚 被引 30
- **作者**: Bin Xia, Jingwen He, Yulun Zhang, Yitong Wang, Yapeng Tian, Wenming Yang et al.
- **🏷️ 机构**: Tsinghua University, Shanghai AI Laboratory, ETH Z&#x000FC;rich
- **会议**: CVPR 2023

### Discriminator-Cooperated Feature Map Distillation for GAN Compression.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01949) · 📚 被引 19
- **作者**: Tie Hu, Mingbao Lin, Lizhou You, Fei Chao, Rongrong Ji
- **🏷️ 机构**: School of Informatics, Xiamen University,MAC Lab, Tencent Youtu Lab
- **会议**: CVPR 2023

## 跨领域论文（完整笔记在其他领域）

- Class-Incremental Exemplar Compression for Class-Incremental Learning. → [continual-learning](../continual-learning/Guideline%202023.md)
