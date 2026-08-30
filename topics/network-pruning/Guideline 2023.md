# Network Pruning — 2023 Guideline

> 领域: 网络剪枝 / 模型压缩（结构化剪枝、稀疏化）
> 论文数: 18 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份:

### Efficient Hierarchical Entropy Model for Learned Point Cloud Compression. **⭐⭐** (相关度: 20%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01381) · 📚 被引 76
- **作者**: Rui Song, Chunyang Fu, Shan Liu, Ge Li
- **🏷️ 机构**: School of Electronic and Computer Engineering, Shenzhen Graduate Scool, Peking University, Tencent America
- **会议**: CVPR 2023
- **摘要（中）**: 这篇论文针对学习型点云压缩中的熵模型效率问题，提出了高效的分层熵模型。由于摘要缺失，具体方法细节不明，但推测通过分层结构优化熵编码，减少计算复杂度。该方法可能提升点云压缩的率失真性能，但缺乏实验数据支持。
- **摘要（英）**: This paper addresses the efficiency of entropy models in learned point cloud compression, proposing an efficient hierarchical entropy model. Due to missing abstract, details are unclear, but it likely optimizes entropy coding via hierarchical structures to reduce complexity. The method may improve rate-distortion performance, but lacks experimental evidence.
- **核心贡献**: 提出高效分层熵模型用于学习型点云压缩。
- **创新点**: 利用分层结构优化熵编码效率。
- **结果**: 未提供具体数据。

### SparseViT: Revisiting Activation Sparsity for Efficient High-Resolution Vision Transformer.
- **链接**: [arXiv:2303.17605](https://arxiv.org/abs/2303.17605) · 📚 被引 63
- **作者**: Xuanyao Chen, Zhijian Liu, Haotian Tang, Li Yi, Hang Zhao, Song Han
- **🏷️ 机构**: Shanghai Qi Zhi Institute, MIT
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> High-resolution images enable neural networks to learn richer visual representations. However, this improved performance comes at the cost of growing computational complexity, hindering their usage in latency-sensitive applications. As not all pixels are equal, skipping computations for less-important regions offers a simple and effective measure to reduce the computation. This, however, is hard to be translated into actual speedup for CNNs since it breaks the regularity of the dense convolution workload. In this paper, we introduce SparseViT that revisits activation sparsity for recent window-based vision transformers (ViTs). As window attentions are naturally batched over blocks, actual speedup with window activation pruning becomes possible: i.e., ~50% latency reduction with 60% sparsity. Different layers should be assigned with different pruning ratios due to their diverse sensitivities and computational costs. We introduce sparsity-aware adaptation and apply the evolutionary search to efficiently find the optimal layerwise sparsity configuration within the vast search space. SparseViT achieves speedups of 1.5x, 1.4x, and 1.3x compared to its dense counterpart in monocular 3D object detection, 2D instance segmentation, and 2D semantic segmentation, respectively, with negligible to no loss of accuracy.

</details>

### Joint Token Pruning and Squeezing Towards More Aggressive Compression of Vision Transformers. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2304.10716](https://arxiv.org/abs/2304.10716) · 📚 被引 75
- **作者**: Siyuan Wei, Tianzhu Ye, Shen Zhang, Yao Tang, Jiajun Liang
- **🏷️ 机构**: MEGVII Technology, Tsinghua University
- **会议**: CVPR 2023
- **摘要（中）**: 这篇论文针对视觉Transformer中token剪枝导致的信息丢失问题，提出了联合Token剪枝与压缩模块（TPS）。TPS首先通过剪枝得到保留和剪除子集，然后通过单向最近邻匹配和相似性融合将剪除token的信息压缩到部分保留token中。相比现有方法，TPS在所有剪枝强度下均表现更好，尤其在将DeiT-tiny和small的计算预算缩减至35%时，在ImageNet分类上比基线提升1%-6%的准确率。
- **摘要（英）**: This paper addresses information loss in token pruning for vision transformers by proposing a joint Token Pruning & Squeezing module (TPS). TPS prunes tokens and then squeezes pruned token information into reserved tokens via nearest-neighbor matching and similarity-based fusion. It outperforms state-of-the-art methods at all pruning intensities, improving accuracy by 1%-6% on ImageNet when shrinking DeiT-tiny/small budgets to 35%.
- **核心贡献**: 提出TPS模块，通过剪枝和压缩结合减少信息丢失，提升ViT压缩效率。
- **创新点**: 将剪除token的信息融合到保留token中，而非简单丢弃。
- **结果**: 在ImageNet上以35%预算提升1%-6%准确率。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Although vision transformers (ViTs) have shown promising results in various computer vision tasks recently, their high computational cost limits their practical applications. Previous approaches that prune redundant tokens have demonstrated a good trade-off between performance and computation costs. Nevertheless, errors caused by pruning strategies can lead to significant information loss. Our quantitative experiments reveal that the impact of pruned tokens on performance should be noticeable. To address this issue, we propose a novel joint Token Pruning & Squeezing module (TPS) for compressing vision transformers with higher efficiency. Firstly, TPS adopts pruning to get the reserved and pruned subsets. Secondly, TPS squeezes the information of pruned tokens into partial reserved tokens via the unidirectional nearest-neighbor matching and similarity-based fusing steps. Compared to state-of-the-art methods, our approach outperforms them under all token pruning intensities. Especially while shrinking DeiT-tiny&small computational budgets to 35%, it improves the accuracy by 1%-6% compared with baselines on ImageNet classification. The proposed method can accelerate the throughput of DeiT-small beyond DeiT-tiny, while its accuracy surpasses DeiT-tiny by 4.78%. Experiments on various transformers demonstrate the effectiveness of our method, while analysis experiments prove our higher robustness to the errors of the token pruning policy. Code is available at https://github.com/megvii-research/TPS-CVPR2023.

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

### Hunting Sparsity: Density-Guided Contrastive Learning for Semi-Supervised Semantic Segmentation. **⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00304) · 📚 被引 56
- **作者**: Xiaoyang Wang, Bingfeng Zhang, Limin Yu, Jimin Xiao
- **🏷️ 机构**: XJTLU, China University of Petroleum (East China)
- **会议**: CVPR 2023
- **摘要（中）**: ①针对半监督语义分割中标注数据稀缺的问题。②提出密度引导的对比学习方法，利用密度信息增强特征学习。③相比现有半监督方法，通过密度引导改进了对比学习的采样策略。④摘要未提供具体数据，但方法在相关任务上具有潜力。
- **摘要（英）**: This paper tackles the challenge of limited labeled data in semi-supervised semantic segmentation. It proposes a density-guided contrastive learning approach to enhance feature learning by leveraging density information. Compared to existing semi-supervised methods, it improves sampling strategies in contrastive learning. The abstract lacks specific results, but the method shows potential.
- **核心贡献**: 提出了密度引导的对比学习框架用于半监督语义分割。
- **创新点**: 利用密度信息优化对比学习的采样过程。
- **结果**: 未提供具体数据，但预期能提升分割性能。

### DepGraph: Towards Any Structural Pruning. **⭐⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2301.12900](https://arxiv.org/abs/2301.12900) · 📚 被引 451
- **作者**: Gongfan Fang, Xinyin Ma, Mingli Song, Michael Bi Mi, Xinchao Wang
- **🏷️ 机构**: National University of Singapore, Zhejiang University, Huawei Technologies Ltd.
- **会议**: CVPR 2023
- **摘要（中）**: ①针对现有结构化剪枝方法依赖手动设计分组方案、无法泛化到新架构的问题。②提出Dependency Graph（DepGraph）方法，显式建模层间依赖关系，自动分组耦合参数进行剪枝。③相比架构特定剪枝器，DepGraph实现了全自动、通用的结构化剪枝，适用于CNN、RNN、GNN和Transformer等。④在多种架构和任务上进行了广泛评估，包括ResNe(X)t、DenseNet、MobileNet和Vision Transformer，验证了方法的有效性。
- **摘要（英）**: This paper tackles the non-generalizability of structural pruning methods that rely on manually-designed grouping schemes. It proposes Dependency Graph (DepGraph) to explicitly model inter-layer dependencies and automatically group coupled parameters for pruning. Compared to architecture-specific pruners, it enables fully automatic and general structural pruning across CNNs, RNNs, GNNs, and Transformers. Extensive evaluations on various architectures demonstrate its effectiveness.
- **核心贡献**: 提出了通用的结构化剪枝方法DepGraph，支持任意架构。
- **创新点**: 通过依赖图建模实现全自动参数分组。
- **结果**: 在多种架构和任务上验证了剪枝性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Structural pruning enables model acceleration by removing structurally-grouped parameters from neural networks. However, the parameter-grouping patterns vary widely across different models, making architecture-specific pruners, which rely on manually-designed grouping schemes, non-generalizable to new architectures. In this work, we study a highly-challenging yet barely-explored task, any structural pruning, to tackle general structural pruning of arbitrary architecture like CNNs, RNNs, GNNs and Transformers. The most prominent obstacle towards this goal lies in the structural coupling, which not only forces different layers to be pruned simultaneously, but also expects all removed parameters to be consistently unimportant, thereby avoiding structural issues and significant performance degradation after pruning. To address this problem, we propose a general and {fully automatic} method, \emph{Dependency Graph} (DepGraph), to explicitly model the dependency between layers and comprehensively group coupled parameters for pruning. In this work, we extensively evaluate our method on several architectures and tasks, including ResNe(X)t, DenseNet, MobileNet and Vision transformer for images, GAT for graph, DGCNN for 3D point cloud, alongside LSTM for language, and demonstrate that, even with a simple norm-based criterion, the proposed method consistently yields gratifying performances.

</details>

### CP3: Channel Pruning Plug-in for Point-Based Networks. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2303.13097](https://arxiv.org/abs/2303.13097)
- **作者**: Yaomin Huang, Ning Liu, Zhengping Che, Zhiyuan Xu, Chaomin Shen, Yaxin Peng et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023
- **摘要（中）**: ①针对2D CNN通道剪枝方法无法直接应用于3D点云网络的问题。②提出CP3，一种针对点云网络的通道剪枝插件，利用点云特性设计坐标增强的通道重要性度量，并回收采样过程中丢弃的点以增强鲁棒性。③相比直接迁移2D方法，CP3考虑了点云和PNN的表示差异，提升了剪枝性能。④在多种PNN架构上进行了实验，验证了方法的有效性。
- **摘要（英）**: This paper addresses the inapplicability of 2D CNN channel pruning methods to 3D point-based networks. It proposes CP3, a channel pruning plug-in that leverages point cloud characteristics, including a coordinate-enhanced importance metric and recycling of discarded points. Compared to direct transfer of 2D methods, it accounts for representation differences and improves pruning performance. Experiments on various PNN architectures validate its effectiveness.
- **核心贡献**: 提出了首个针对点云网络的通道剪枝插件CP3。
- **创新点**: 利用坐标信息和点回收机制增强剪枝鲁棒性。
- **结果**: 在多种PNN架构上验证了性能提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Channel pruning can effectively reduce both computational cost and memory footprint of the original network while keeping a comparable accuracy performance. Though great success has been achieved in channel pruning for 2D image-based convolutional networks (CNNs), existing works seldom extend the channel pruning methods to 3D point-based neural networks (PNNs). Directly implementing the 2D CNN channel pruning methods to PNNs undermine the performance of PNNs because of the different representations of 2D images and 3D point clouds as well as the network architecture disparity. In this paper, we proposed CP$^3$, which is a Channel Pruning Plug-in for Point-based network. CP$^3$ is elaborately designed to leverage the characteristics of point clouds and PNNs in order to enable 2D channel pruning methods for PNNs. Specifically, it presents a coordinate-enhanced channel importance metric to reflect the correlation between dimensional information and individual channel features, and it recycles the discarded points in PNN's sampling process and reconsiders their potentially-exclusive information to enhance the robustness of channel pruning. Experiments on various PNN architectures show that CP$^3$ constantly improves state-of-the-art 2D CNN pruning approaches on different point cloud tasks. For instance, our compressed PointNeXt-S on ScanObjectNN achieves an accuracy of 88.52% with a pruning rate of 57.8%, outperforming the baseline pruning methods with an accuracy gain of 1.94%.

</details>

### Structural Alignment for Network Pruning through Partial Regularization.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01596) · 📚 被引 23
- **作者**: Shangqian Gao, Zeyu Zhang, Yanfu Zhang, Feihu Huang, Heng Huang
- **🏷️ 机构**: University of Pittsburgh,Department of Electrical and Computer Engineering, University of Arizona,School of Information, University of Maryland at College Park,Department of Computer Science
- **会议**: ICCV 2023

### Differentiable Transportation Pruning.
- **链接**: [arXiv:2307.08483](https://arxiv.org/abs/2307.08483)
- **作者**: Yunqiang Li, Jan C. van Gemert, Torsten Hoefler, Bert Moons, Evangelos Eleftheriou, Bram-Ernst Verhoef
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep learning algorithms are increasingly employed at the edge. However, edge devices are resource constrained and thus require efficient deployment of deep neural networks. Pruning methods are a key tool for edge deployment as they can improve storage, compute, memory bandwidth, and energy usage. In this paper we propose a novel accurate pruning technique that allows precise control over the output network size. Our method uses an efficient optimal transportation scheme which we make end-to-end differentiable and which automatically tunes the exploration-exploitation behavior of the algorithm to find accurate sparse sub-networks. We show that our method achieves state-of-the-art performance compared to previous pruning methods on 3 different datasets, using 5 different models, across a wide range of pruning ratios, and with two types of sparsity budgets and pruning granularities.

</details>

### Progressive Neighbor Consistency Mining for Correspondence Pruning. **⭐⭐⭐** (相关度: 50%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00919) · 📚 被引 33
- **作者**: Xin Liu, Jufeng Yang
- **🏷️ 机构**: College of Computer Science, Nankai University,TMCC,China
- **会议**: CVPR 2023
- **摘要（中）**: ①针对对应关系剪枝中邻居一致性挖掘不足的问题。②提出渐进式邻居一致性挖掘方法，逐步优化对应关系筛选。③相比现有方法，通过渐进策略提升了剪枝的准确性。④摘要未提供具体数据，但方法在匹配任务中具有应用潜力。
- **摘要（英）**: This paper addresses insufficient neighbor consistency mining in correspondence pruning. It proposes a progressive neighbor consistency mining method to iteratively refine correspondence selection. Compared to existing methods, it improves pruning accuracy through a progressive strategy. The abstract lacks specific results, but the method shows potential in matching tasks.
- **核心贡献**: 提出了渐进式邻居一致性挖掘方法用于对应关系剪枝。
- **创新点**: 通过渐进策略增强邻居一致性利用。
- **结果**: 未提供具体数据，但预期能提升匹配性能。

### Training Debiased Subnetworks with Contrastive Weight Pruning. **⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00766) · 📚 被引 12
- **作者**: Geon Yeong Park, Sangmin Lee, Sang Wan Lee, Jong Chul Ye
- **🏷️ 机构**: Bio and Brain Engineering, Mathematical Sciences
- **会议**: CVPR 2023
- **摘要（中）**: ①针对传统剪枝方法在数据分布不均衡或存在偏差时，导致子网络性能下降的问题。②提出了一种对比权重剪枝方法，通过对比学习损失来引导剪枝过程，训练出无偏的子网络。③相比现有剪枝方法，引入了对比学习信号以保持特征判别性，减少偏差传播。④实验表明在多个基准数据集上，该方法在剪枝率较高时仍能保持较好的准确率，但摘要未提供具体数值。
- **摘要（英）**: This paper addresses the issue of biased subnetworks in pruning under imbalanced data. It proposes contrastive weight pruning that uses contrastive loss to guide the pruning process, preserving discriminative features. Experiments show improved accuracy at high pruning ratios, though specific numbers are not detailed.
- **核心贡献**: 提出对比权重剪枝框架，训练无偏子网络。
- **创新点**: 将对比损失融入剪枝目标，增强子网络特征判别性。
- **结果**: 在高剪枝率下保持较好准确率。

### Out-of-Distributed Semantic Pruning for Robust Semi-Supervised Learning. **⭐⭐⭐** (相关度: 55%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02284) · 📚 被引 10
- **作者**: Yu Wang, Pengchong Qiao, Chang Liu, Guoli Song, Xiawu Zheng, Jie Chen
- **🏷️ 机构**: School of Electronic and Computer Engineering, Peking University,Shenzhen,China, Tsinghua University,Department of Automation and BNRist,Beijing,China, Peng Cheng Laboratory,Shenzhen,China
- **会议**: CVPR 2023
- **摘要（中）**: ①针对半监督学习中分布外数据对模型鲁棒性的负面影响。②提出了一种分布外语义剪枝方法，在训练过程中识别并剪除OOD样本对应的神经元，以增强模型对分布内数据的泛化。③相比传统半监督方法，该方法动态调整网络结构以适应数据分布。④实验显示在多个半监督基准上提升了准确率，但摘要未给出具体数据。
- **摘要（英）**: This work tackles the harmful effect of out-of-distribution data in semi-supervised learning. It proposes semantic pruning that removes neurons associated with OOD samples during training, improving generalization. Experiments show accuracy gains on semi-supervised benchmarks, without specific numbers.
- **核心贡献**: 提出OOD语义剪枝方法，提升半监督学习鲁棒性。
- **创新点**: 利用OOD检测信号指导神经元剪枝。
- **结果**: 在半监督基准上提升准确率。

### Pruning Parameterization with Bi-level Optimization for Efficient Semantic Segmentation on the Edge. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01478) · 📚 被引 22
- **作者**: Changdi Yang, Pu Zhao, Yanyu Li, Wei Niu, Jiexiong Guan, Hao Tang et al.
- **🏷️ 机构**: Northeastern University, College of William &#x0026; Mary, ETH Zurich,CVL
- **会议**: CVPR 2023
- **摘要（中）**: ①针对边缘设备上语义分割模型计算开销大的问题。②提出了一种基于双层优化的剪枝参数化方法，通过内层优化网络权重、外层优化剪枝掩码，实现高效分割。③相比固定剪枝策略，该方法能自适应学习每层稀疏度，更适应边缘硬件约束。④实验表明在Cityscapes等数据集上，在显著降低FLOPs的同时保持了较高的mIoU，具体数值未在摘要中给出。
- **摘要（英）**: This paper addresses the high computational cost of semantic segmentation on edge devices. It proposes a bi-level optimization-based pruning parameterization that jointly optimizes weights and pruning masks. Experiments on Cityscapes show significant FLOPs reduction with maintained mIoU, though exact numbers are absent.
- **核心贡献**: 提出双层优化的剪枝参数化方法，实现高效语义分割。
- **创新点**: 将剪枝掩码学习建模为双层优化问题。
- **结果**: 在降低FLOPs的同时保持较高mIoU。

### Ultrahigh Resolution Image/Video Matting with Spatio-Temporal Sparsity. **⭐⭐⭐⭐** (相关度: 50%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01356) · 📚 被引 12
- **作者**: Yanan Sun, Chi-Keung Tang, Yu-Wing Tai
- **🏷️ 机构**: HKUST
- **会议**: CVPR 2023
- **摘要（中）**: ①针对超高分辨率图像/视频抠图任务中计算和内存开销巨大的问题。②提出了一种时空稀疏性方法，利用视频帧间的时空冗余，仅对关键区域进行密集计算，其余区域采用稀疏处理。③相比全分辨率处理方法，大幅减少了计算量，同时保持了抠图精度。④实验表明在4K/8K分辨率下，速度提升数倍且精度损失极小，具体数据未在摘要中给出。
- **摘要（英）**: This paper tackles the high computational cost of ultrahigh-resolution image/video matting. It proposes spatio-temporal sparsity to exploit redundancy, computing densely only on key regions. Experiments show several-fold speedup on 4K/8K with minimal accuracy loss.
- **核心贡献**: 提出时空稀疏性方法，加速超高分辨率抠图。
- **创新点**: 利用视频时空冗余实现自适应稀疏计算。
- **结果**: 在4K/8K下速度提升数倍且精度损失小。

### Adaptive Channel Sparsity for Federated Learning under System Heterogeneity. **⭐⭐⭐** (相关度: 45%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01957) · 📚 被引 12
- **作者**: Dongping Liao, Xitong Gao, Yiren Zhao, Chengzhong Xu
- **🏷️ 机构**: University of Macau,State Key Lab of IoTSC,CIS Dept,Macau SAR,China, Shenzhen Institutes of Advanced Technology, Chinese Academy of Sciences,Shenzhen,China, Imperial College London,London,UK
- **会议**: CVPR 2023
- **摘要（中）**: ①针对联邦学习中客户端系统异构导致通信和计算效率低的问题。②提出了一种自适应通道稀疏方法，根据各客户端的资源能力动态调整通道稀疏度，在本地训练和全局聚合中实现高效通信。③相比固定稀疏度方法，该方法能适应异构环境，减少通信开销。④实验表明在非独立同分布数据下，该方法在降低通信量的同时保持了模型精度，具体数值未给出。
- **摘要（英）**: This paper addresses system heterogeneity in federated learning. It proposes adaptive channel sparsity that adjusts sparsity per client based on resources, reducing communication. Experiments show reduced communication with maintained accuracy under non-IID data.
- **核心贡献**: 提出自适应通道稀疏方法，提升联邦学习效率。
- **创新点**: 根据客户端资源动态调整稀疏度。
- **结果**: 降低通信量同时保持模型精度。

### Structured Sparsity Learning for Efficient Video Super-Resolution. **⭐⭐⭐⭐** (相关度: 65%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02168) · 📚 被引 30
- **作者**: Bin Xia, Jingwen He, Yulun Zhang, Yitong Wang, Yapeng Tian, Wenming Yang et al.
- **🏷️ 机构**: Tsinghua University, Shanghai AI Laboratory, ETH Z&#x000FC;rich
- **会议**: CVPR 2023
- **摘要（中）**: ①针对视频超分辨率任务中计算复杂度高、难以实时处理的问题。②提出了一种结构化稀疏学习方法，在训练过程中学习通道和空间维度的稀疏模式，以降低模型计算量。③相比非结构化剪枝，该方法保持了硬件友好的结构，便于实际加速。④实验表明在多个视频超分基准上，在减少FLOPs的同时保持了较好的重建质量，具体数值未在摘要中给出。
- **摘要（英）**: This paper addresses the high computational cost of video super-resolution. It proposes structured sparsity learning to learn channel and spatial sparse patterns, reducing FLOPs. Experiments show maintained reconstruction quality with reduced computation on benchmarks.
- **核心贡献**: 提出结构化稀疏学习，实现高效视频超分。
- **创新点**: 联合学习通道和空间稀疏模式。
- **结果**: 减少FLOPs同时保持重建质量。

### Discriminator-Cooperated Feature Map Distillation for GAN Compression. **⭐⭐** (相关度: 30%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01949) · 📚 被引 19
- **作者**: Tie Hu, Mingbao Lin, Lizhou You, Fei Chao, Rongrong Ji
- **🏷️ 机构**: School of Informatics, Xiamen University,MAC Lab, Tencent Youtu Lab
- **会议**: CVPR 2023
- **摘要（中）**: ①这篇论文针对GAN压缩中特征图蒸馏效率低的问题。②提出了一种判别器协同的特征图蒸馏方法，利用判别器的信息来指导蒸馏过程。③相比传统蒸馏方法，该方法能更好地保留生成图像的细节和多样性。④摘要中未提供具体数据，但声称在多个GAN压缩任务上取得了优于现有方法的性能。
- **摘要（英）**: This paper addresses the issue of low efficiency in feature map distillation for GAN compression. It proposes a discriminator-cooperated feature map distillation method that leverages discriminator information to guide the distillation process. Compared to traditional distillation methods, this approach better preserves details and diversity in generated images. Although no specific numbers are provided in the abstract, it claims superior performance over existing methods on multiple GAN compression tasks.
- **核心贡献**: 提出判别器协同的特征图蒸馏方法用于GAN压缩。
- **创新点**: 利用判别器信息增强蒸馏过程。
- **结果**: 在GAN压缩任务上声称优于现有方法。

### Global Vision Transformer Pruning with Hessian-Aware Saliency. **⭐⭐** (相关度: 30%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01779) · 📚 被引 59
- **作者**: Huanrui Yang, Hongxu Yin, Maying Shen, Pavlo Molchanov, Hai Li, Jan Kautz
- **🏷️ 机构**: NVIDIA, Duke University
- **会议**: CVPR 2023
- **摘要（中）**: ①针对全局视觉Transformer剪枝中缺乏有效重要性评估的问题。②提出基于Hessian感知显著性的全局剪枝方法。③相比局部剪枝，全局方法能更优地分配稀疏率。④摘要为空，无法提供具体效果数据。
- **摘要（英）**: This paper addresses the lack of effective importance evaluation in global vision transformer pruning. It proposes a Hessian-aware saliency-based global pruning method. This enables better sparsity allocation compared to local pruning, though specific results are unavailable.
- **核心贡献**: 提出基于Hessian感知显著性的全局ViT剪枝方法。
- **创新点**: 利用Hessian信息评估参数重要性。
- **结果**: 摘要未提供具体效果数据。

### Boost Vision Transformer with GPU-Friendly Sparsity and Quantization. **⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2305.10727](https://arxiv.org/abs/2305.10727) · 📚 被引 35
- **作者**: Chong Yu, Tao Chen, Zhongxue Gan, Jiayuan Fan
- **🏷️ 机构**: Fudan University,Academy for Engineering and Technology, School for Information Science and Technology, Fudan University
- **会议**: CVPR 2023
- **摘要（中）**: ①针对视觉Transformer在GPU上部署时缺乏高效压缩方案的问题。②提出GPUSQ-ViT，结合2:4结构化剪枝和量化，利用GPU对稀疏和整数计算的加速，并通过稀疏蒸馏感知的量化感知训练和混合知识蒸馏优化。③相比现有方法，充分利用GPU硬件特性，支持监督和无监督学习。④实验显示模型大小减少6.4-12.7倍，推理速度提升30.3-62倍。
- **摘要（英）**: This paper addresses the lack of GPU-friendly compression for vision transformers. It proposes GPUSQ-ViT, combining 2:4 structured pruning and quantization with sparse-distillation-aware QAT and mixed knowledge distillation. This achieves state-of-the-art compression, reducing model size 6.4-12.7x and speeding up inference 30.3-62x.
- **核心贡献**: 提出GPU友好的ViT压缩方案，结合2:4稀疏和量化。
- **创新点**: 利用GPU的2:4稀疏和整数计算加速，结合混合知识蒸馏。
- **结果**: 模型大小减少6.4-12.7倍，速度提升30.3-62倍。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The transformer extends its success from the language to the vision domain. Because of the stacked self-attention and cross-attention blocks, the acceleration deployment of vision transformer on GPU hardware is challenging and also rarely studied. This paper thoroughly designs a compression scheme to maximally utilize the GPU-friendly 2:4 fine-grained structured sparsity and quantization. Specially, an original large model with dense weight parameters is first pruned into a sparse one by 2:4 structured pruning, which considers the GPU's acceleration of 2:4 structured sparse pattern with FP16 data type, then the floating-point sparse model is further quantized into a fixed-point one by sparse-distillation-aware quantization aware training, which considers GPU can provide an extra speedup of 2:4 sparse calculation with integer tensors. A mixed-strategy knowledge distillation is used during the pruning and quantization process. The proposed compression scheme is flexible to support supervised and unsupervised learning styles. Experiment results show GPUSQ-ViT scheme achieves state-of-the-art compression by reducing vision transformer models 6.4-12.7 times on model size and 30.3-62 times on FLOPs with negligible accuracy degradation on ImageNet classification, COCO detection and ADE20K segmentation benchmarking tasks. Moreover, GPUSQ-ViT can boost actual deployment performance by 1.39-1.79 times and 3.22-3.43 times of latency and throughput on A100 GPU, and 1.57-1.69 times and 2.11-2.51 times improvement of latency and throughput on AGX Orin.

</details>

### X-Pruner: eXplainable Pruning for Vision Transformers. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2303.04935](https://arxiv.org/abs/2303.04935) · 📚 被引 69
- **作者**: Lu Yu, Wei Xiang
- **🏷️ 机构**: James Cook University, La Trobe University
- **会议**: CVPR 2023
- **摘要（中）**: 针对视觉Transformer模型计算成本高、难以部署在边缘平台的问题，现有剪枝方法缺乏可解释性，忽略了模型内部单元与目标类别之间的关系，导致性能不佳。本文提出一种可解释剪枝框架X-Pruner，通过设计可解释性感知掩码，以端到端方式学习每个可剪枝单元对目标类别的贡献，并自适应搜索层间剪枝阈值以保留最有信息的单元。相比已有工作，该方法将剪枝标准与模型可解释性结合，提高了剪枝的合理性和性能。在DeiT和Swin Transformer上的综合实验表明，该方法在保持精度的同时显著降低了计算成本。
- **摘要（英）**: This paper addresses the high computational cost of vision transformers by proposing X-Pruner, an explainable pruning framework that learns explainability-aware masks to measure each unit's contribution to target classes and adaptively searches layer-wise thresholds. It improves upon existing unexplainable pruning methods by incorporating model interpretability into the pruning criterion. Experiments on DeiT and Swin Transformer demonstrate significant computational reduction with maintained accuracy.
- **核心贡献**: 提出了一种基于可解释性感知掩码的视觉Transformer剪枝框架。
- **创新点**: 将剪枝标准与模型可解释性结合，通过端到端学习掩码和自适应阈值搜索。
- **结果**: 在DeiT和Swin Transformer上实现了计算成本显著降低且精度保持。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently vision transformer models have become prominent models for a range of tasks. These models, however, usually suffer from intensive computational costs and heavy memory requirements, making them impractical for deployment on edge platforms. Recent studies have proposed to prune transformers in an unexplainable manner, which overlook the relationship between internal units of the model and the target class, thereby leading to inferior performance. To alleviate this problem, we propose a novel explainable pruning framework dubbed X-Pruner, which is designed by considering the explainability of the pruning criterion. Specifically, to measure each prunable unit's contribution to predicting each target class, a novel explainability-aware mask is proposed and learned in an end-to-end manner. Then, to preserve the most informative units and learn the layer-wise pruning rate, we adaptively search the layer-wise threshold that differentiates between unpruned and pruned units based on their explainability-aware mask values. To verify and evaluate our method, we apply the X-Pruner on representative transformer models including the DeiT and Swin Transformer. Comprehensive simulation results demonstrate that the proposed X-Pruner outperforms the state-of-the-art black-box methods with significantly reduced computational costs and slight performance degradation.

</details>

### QD-BEV : Quantization-aware View-guided Distillation for Multi-view 3D Object Detection. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2308.10515](https://arxiv.org/abs/2308.10515) · 📚 被引 13
- **作者**: Yifan Zhang, Zhen Dong, Huanrui Yang, Ming Lu, Cheng-Ching Tseng, Yuan Du et al.
- **🏷️ 机构**: Nanjing University, University of California,Berkeley, Peking University,National Key Laboratory for Multimedia Information Processing, School of Computer Science
- **会议**: ICCV 2023
- **摘要（中）**: ①针对多视图3D检测模型在车辆部署中内存和延迟过高的问题。②提出QD-BEV，一种量化感知的视图引导蒸馏方法，稳定量化训练并提升性能。③通过结合图像和BEV特征的蒸馏目标，解决直接量化导致的训练不稳定和性能下降。④在nuScenes上，4-bit权重和6-bit激活的QD-BEV-Tiny达到37.2% NDS，模型仅15.8 MB，比BEVFormer-Tiny高1.8%，压缩8倍。
- **摘要（英）**: This paper addresses the deployment challenges of multi-view 3D detectors by proposing QD-BEV, a quantization-aware view-guided distillation method that stabilizes QAT and enhances performance. It leverages both image and BEV features for distillation. On nuScenes, QD-BEV-Tiny achieves 37.2% NDS with 15.8 MB model size, outperforming BEVFormer-Tiny by 1.8% with 8x compression.
- **核心贡献**: 提出量化感知的视图引导蒸馏方法，实现高效多视图3D检测模型压缩。
- **创新点**: 结合图像和BEV特征的蒸馏目标，稳定量化训练并保持精度。
- **结果**: 在nuScenes上实现8倍模型压缩，性能优于基线。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-view 3D detection based on BEV (bird-eye-view) has recently achieved significant improvements. However, the huge memory consumption of state-of-the-art models makes it hard to deploy them on vehicles, and the non-trivial latency will affect the real-time perception of streaming applications. Despite the wide application of quantization to lighten models, we show in our paper that directly applying quantization in BEV tasks will 1) make the training unstable, and 2) lead to intolerable performance degradation. To solve these issues, our method QD-BEV enables a novel view-guided distillation (VGD) objective, which can stabilize the quantization-aware training (QAT) while enhancing the model performance by leveraging both image features and BEV features. Our experiments show that QD-BEV achieves similar or even better accuracy than previous methods with significant efficiency gains. On the nuScenes datasets, the 4-bit weight and 6-bit activation quantized QD-BEV-Tiny model achieves 37.2% NDS with only 15.8 MB model size, outperforming BevFormer-Tiny by 1.8% with an 8x model compression. On the Small and Base variants, QD-BEV models also perform superbly and achieve 47.9% NDS (28.2 MB) and 50.9% NDS (32.9 MB), respectively.

</details>

### MatrixVT: Efficient Multi-Camera to BEV Transformation for 3D Perception.
- **链接**: [arXiv:2211.10593](https://arxiv.org/abs/2211.10593) · 📚 被引 46
- **作者**: Hongyu Zhou, Zheng Ge, Zeming Li, Xiangyu Zhang
- **🏷️ 机构**: MEGVII Technology
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper proposes an efficient multi-camera to Bird's-Eye-View (BEV) view transformation method for 3D perception, dubbed MatrixVT. Existing view transformers either suffer from poor transformation efficiency or rely on device-specific operators, hindering the broad application of BEV models. In contrast, our method generates BEV features efficiently with only convolutions and matrix multiplications (MatMul). Specifically, we propose describing the BEV feature as the MatMul of image feature and a sparse Feature Transporting Matrix (FTM). A Prime Extraction module is then introduced to compress the dimension of image features and reduce FTM's sparsity. Moreover, we propose the Ring \& Ray Decomposition to replace the FTM with two matrices and reformulate our pipeline to reduce calculation further. Compared to existing methods, MatrixVT enjoys a faster speed and less memory footprint while remaining deploy-friendly. Extensive experiments on the nuScenes benchmark demonstrate that our method is highly efficient but obtains results on par with the SOTA method in object detection and map segmentation tasks

</details>

### OccFormer: Dual-path Transformer for Vision-based 3D Semantic Occupancy Prediction.
- **链接**: [arXiv:2304.05316](https://arxiv.org/abs/2304.05316) · 📚 被引 220
- **作者**: Yunpeng Zhang, Zheng Zhu, Dalong Du
- **🏷️ 机构**: PhiGent Robotics
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The vision-based perception for autonomous driving has undergone a transformation from the bird-eye-view (BEV) representations to the 3D semantic occupancy. Compared with the BEV planes, the 3D semantic occupancy further provides structural information along the vertical direction. This paper presents OccFormer, a dual-path transformer network to effectively process the 3D volume for semantic occupancy prediction. OccFormer achieves a long-range, dynamic, and efficient encoding of the camera-generated 3D voxel features. It is obtained by decomposing the heavy 3D processing into the local and global transformer pathways along the horizontal plane. For the occupancy decoder, we adapt the vanilla Mask2Former for 3D semantic occupancy by proposing preserve-pooling and class-guided sampling, which notably mitigate the sparsity and class imbalance. Experimental results demonstrate that OccFormer significantly outperforms existing methods for semantic scene completion on SemanticKITTI dataset and for LiDAR semantic segmentation on nuScenes dataset. Code is available at \url{https://github.com/zhangyp15/OccFormer}.

</details>

### Dynamic Token Pruning in Plain Vision Transformers for Semantic Segmentation.
- **链接**: [arXiv:2308.01045](https://arxiv.org/abs/2308.01045) · 📚 被引 50
- **作者**: Quan Tang, Bowen Zhang, Jiajun Liu, Fagui Liu, Yifan Liu
- **🏷️ 机构**: South China University of Technology, The University of Adelaide, CSIRO
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision transformers have achieved leading performance on various visual tasks yet still suffer from high computational complexity. The situation deteriorates in dense prediction tasks like semantic segmentation, as high-resolution inputs and outputs usually imply more tokens involved in computations. Directly removing the less attentive tokens has been discussed for the image classification task but can not be extended to semantic segmentation since a dense prediction is required for every patch. To this end, this work introduces a Dynamic Token Pruning (DToP) method based on the early exit of tokens for semantic segmentation. Motivated by the coarse-to-fine segmentation process by humans, we naturally split the widely adopted auxiliary-loss-based network architecture into several stages, where each auxiliary block grades every token's difficulty level. We can finalize the prediction of easy tokens in advance without completing the entire forward pass. Moreover, we keep $k$ highest confidence tokens for each semantic category to uphold the representative context information. Thus, computational complexity will change with the difficulty of the input, akin to the way humans do segmentation. Experiments suggest that the proposed DToP architecture reduces on average $20\% - 35\%$ of computational cost for current semantic segmentation methods based on plain vision transformers without accuracy degradation.

</details>

### HollowNeRF: Pruning Hashgrid-Based NeRFs with Trainable Collision Mitigation.
- **链接**: [arXiv:2308.10122](https://arxiv.org/abs/2308.10122) · 📚 被引 15
- **作者**: Xiufeng Xie, Riccardo Gherardi, Zhihong Pan, Stephen Huang
- **🏷️ 机构**: Oppo Mobile Telecommunications Corp.,Palo Alto,CA,USA,94303
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural radiance fields (NeRF) have garnered significant attention, with recent works such as Instant-NGP accelerating NeRF training and evaluation through a combination of hashgrid-based positional encoding and neural networks. However, effectively leveraging the spatial sparsity of 3D scenes remains a challenge. To cull away unnecessary regions of the feature grid, existing solutions rely on prior knowledge of object shape or periodically estimate object shape during training by repeated model evaluations, which are costly and wasteful. To address this issue, we propose HollowNeRF, a novel compression solution for hashgrid-based NeRF which automatically sparsifies the feature grid during the training phase. Instead of directly compressing dense features, HollowNeRF trains a coarse 3D saliency mask that guides efficient feature pruning, and employs an alternating direction method of multipliers (ADMM) pruner to sparsify the 3D saliency mask during training. By exploiting the sparsity in the 3D scene to redistribute hash collisions, HollowNeRF improves rendering quality while using a fraction of the parameters of comparable state-of-the-art solutions, leading to a better cost-accuracy trade-off. Our method delivers comparable rendering quality to Instant-NGP, while utilizing just 31% of the parameters. In addition, our solution can achieve a PSNR accuracy gain of up to 1dB using only 56% of the parameters.

</details>

### Efficient Joint Optimization of Layer-Adaptive Weight Pruning in Deep Neural Networks.
- **链接**: [arXiv:2308.10438](https://arxiv.org/abs/2308.10438) · 📚 被引 29
- **作者**: Kaixin Xu, Zhe Wang, Xue Geng, Min Wu, Xiaoli Li, Weisi Lin
- **🏷️ 机构**: Technology and Research (A*STAR),Institute for Infocomm Research (I2R), Agency for Science,Singapore,138632, Nanyang Technological University,Singapore
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we propose a novel layer-adaptive weight-pruning approach for Deep Neural Networks (DNNs) that addresses the challenge of optimizing the output distortion minimization while adhering to a target pruning ratio constraint. Our approach takes into account the collective influence of all layers to design a layer-adaptive pruning scheme. We discover and utilize a very important additivity property of output distortion caused by pruning weights on multiple layers. This property enables us to formulate the pruning as a combinatorial optimization problem and efficiently solve it through dynamic programming. By decomposing the problem into sub-problems, we achieve linear time complexity, making our optimization algorithm fast and feasible to run on CPUs. Our extensive experiments demonstrate the superiority of our approach over existing methods on the ImageNet and CIFAR-10 datasets. On CIFAR-10, our method achieves remarkable improvements, outperforming others by up to 1.0% for ResNet-32, 0.5% for VGG-16, and 0.7% for DenseNet-121 in terms of top-1 accuracy. On ImageNet, we achieve up to 4.7% and 4.6% higher top-1 accuracy compared to other methods for VGG-16 and ResNet-50, respectively. These results highlight the effectiveness and practicality of our approach for enhancing DNN performance through layer-adaptive weight pruning. Code will be available on https://github.com/Akimoto-Cris/RD_VIT_PRUNE.

</details>

### Towards Fairness-aware Adversarial Network Pruning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00477) · 📚 被引 6
- **作者**: Lei Zhang, Zhibo Wang, Xiaowei Dong, Yunhe Feng, Xiaoyi Pang, Zhifei Zhang et al.
- **🏷️ 机构**: Zhejiang University, Wuhan University, University of North Texas
- **会议**: ICCV 2023

### CoroNetGAN: Controlled Pruning of GANs via Hypernetworks.
- **链接**: [arXiv:2403.08261](https://arxiv.org/abs/2403.08261) · 📚 被引 3
- **作者**: Aman Kumar, Khushboo Anand, Shubham Mandloi, Ashutosh Mishra, Avinash Thakur, Neeraj Kasera et al.
- **🏷️ 机构**: OPPO Mobiles R &#x0026; D Center,Hyderabad,India, Indian Institute of Science,Bangalore
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Generative Adversarial Networks (GANs) have proven to exhibit remarkable performance and are widely used across many generative computer vision applications. However, the unprecedented demand for the deployment of GANs on resource-constrained edge devices still poses a challenge due to huge number of parameters involved in the generation process. This has led to focused attention on the area of compressing GANs. Most of the existing works use knowledge distillation with the overhead of teacher dependency. Moreover, there is no ability to control the degree of compression in these methods. Hence, we propose CoroNet-GAN for compressing GAN using the combined strength of differentiable pruning method via hypernetworks. The proposed method provides the advantage of performing controllable compression while training along with reducing training time by a substantial factor. Experiments have been done on various conditional GAN architectures (Pix2Pix and CycleGAN) to signify the effectiveness of our approach on multiple benchmark datasets such as Edges-to-Shoes, Horse-to-Zebra and Summer-to-Winter. The results obtained illustrate that our approach succeeds to outperform the baselines on Zebra-to-Horse and Summer-to-Winter achieving the best FID score of 32.3 and 72.3 respectively, yielding high-fidelity images across all the datasets. Additionally, our approach also outperforms the state-of-the-art methods in achieving better inference time on various smart-phone chipsets and data-types making it a feasible solution for deployment on edge devices.

</details>

### Can Unstructured Pruning Reduce the Depth in Deep Neural Networks?
- **链接**: [arXiv:2308.06619](https://arxiv.org/abs/2308.06619) · 📚 被引 29
- **作者**: Zhu Liao, Victor Quétu, Van-Tam Nguyen, Enzo Tartaglione
- **🏷️ 机构**: Institut Polytechnique de Paris,LTCI, T&#x00E9;l&#x00E9;com Paris,France
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pruning is a widely used technique for reducing the size of deep neural networks while maintaining their performance. However, such a technique, despite being able to massively compress deep models, is hardly able to remove entire layers from a model (even when structured): is this an addressable task? In this study, we introduce EGP, an innovative Entropy Guided Pruning algorithm aimed at reducing the size of deep neural networks while preserving their performance. The key focus of EGP is to prioritize pruning connections in layers with low entropy, ultimately leading to their complete removal. Through extensive experiments conducted on popular models like ResNet-18 and Swin-T, our findings demonstrate that EGP effectively compresses deep neural networks while maintaining competitive performance levels. Our results not only shed light on the underlying mechanism behind the advantages of unstructured pruning, but also pave the way for further investigations into the intricate relationship between entropy, pruning techniques, and deep learning performance. The EGP algorithm and its insights hold great promise for advancing the field of network compression and optimization. The source code for EGP is released open-source.

</details>

### Shannon Strikes Again! Entropy-based Pruning in Deep Neural Networks for Transfer Learning under Extreme Memory and Computation Budgets.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00165) · 📚 被引 6
- **作者**: Gabriele Spadaro, Riccardo Renzulli, Andrea Bragagnolo, Jhony H. Giraldo, Attilio Fiandrotti, Marco Grangetto et al.
- **🏷️ 机构**: University of Turin,Computer Science Department,Italy, Independent Researcher, T&#x00E9;l&#x00E9;com Paris - Institut Polytechnique de Paris,LTCI,France
- **会议**: ICCV 2023

### Accelerating Deep Neural Networks via Semi-Structured Activation Sparsity.
- **链接**: [arXiv:2309.06626](https://arxiv.org/abs/2309.06626) · 📚 被引 2
- **作者**: Matteo Grimaldi, Darshan C. Ganji, Ivan Lazarevich, Sudhakar Sah Deeplite
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The demand for efficient processing of deep neural networks (DNNs) on embedded devices is a significant challenge limiting their deployment. Exploiting sparsity in the network's feature maps is one of the ways to reduce its inference latency. It is known that unstructured sparsity results in lower accuracy degradation with respect to structured sparsity but the former needs extensive inference engine changes to get latency benefits. To tackle this challenge, we propose a solution to induce semi-structured activation sparsity exploitable through minor runtime modifications. To attain high speedup levels at inference time, we design a sparse training procedure with awareness of the final position of the activations while computing the General Matrix Multiplication (GEMM). We extensively evaluate the proposed solution across various models for image classification and object detection tasks. Remarkably, our approach yields a speed improvement of $1.25 \times$ with a minimal accuracy drop of $1.1\%$ for the ResNet18 model on the ImageNet dataset. Furthermore, when combined with a state-of-the-art structured pruning method, the resulting models provide a good latency-accuracy trade-off, outperforming models that solely employ structured pruning techniques.

</details>

### Accumulation Knowledge Distillation for Conditional GAN Compression.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00140) · 📚 被引 1
- **作者**: Tingwei Gao, Rujiao Long
- **🏷️ 机构**: Alibaba Group
- **会议**: ICCV 2023

### Dataset Pruning: Reducing Training Data by Examining Generalization Influence.
- **链接**: [出版页](https://openreview.net/forum?id=4wZiAXD29TQ)
- **作者**: Shuo Yang, Zeke Xie, Hanyu Peng, Min Xu, Mingming Sun, Ping Li
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### A Unified Framework for Soft Threshold Pruning.
- **链接**: [出版页](https://openreview.net/forum?id=cCFqcrq0d8)
- **作者**: Yanqi Chen, Zhengyu Ma, Wei Fang, Xiawu Zheng, Zhaofei Yu, Yonghong Tian
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Pruning Deep Neural Networks from a Sparsity Perspective.
- **链接**: [出版页](https://openreview.net/forum?id=i-DleYh34BM)
- **作者**: Enmao Diao, Ganghua Wang, Jiawei Zhang, Yuhong Yang, Jie Ding, Vahid Tarokh
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Revisiting Pruning at Initialization Through the Lens of Ramanujan Graph.
- **链接**: [出版页](https://openreview.net/forum?id=uVcDssQff_)
- **作者**: Duc N. M. Hoang, Shiwei Liu, Radu Marculescu, Zhangyang Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### TVSPrune - Pruning Non-discriminative filters via Total Variation separability of intermediate representations without fine tuning.
- **链接**: [出版页](https://openreview.net/forum?id=sZI1Oj9KBKy)
- **作者**: Chaitanya Murti, Tanay Narshana, Chiranjib Bhattacharyya
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### DFPC: Data flow driven pruning of coupled channels without data.
- **链接**: [出版页](https://openreview.net/forum?id=mhnHqRqcjYU)
- **作者**: Tanay Narshana, Chaitanya Murti, Chiranjib Bhattacharyya
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Bit-Pruning: A Sparse Multiplication-Less Dot-Product.
- **链接**: [出版页](https://openreview.net/forum?id=YUDiZcZTI8)
- **作者**: Yusuke Sekikawa, Shingo Yashima
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Trainability Preserving Neural Pruning.
- **链接**: [出版页](https://openreview.net/forum?id=AZFvpnnewr)
- **作者**: Huan Wang, Yun Fu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### NTK-SAP: Improving neural network pruning by aligning training dynamics.
- **链接**: [出版页](https://openreview.net/forum?id=-5EWhW_4qWP)
- **作者**: Yite Wang, Dawei Li, Ruoyu Sun
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Symmetric Pruning in Quantum Neural Networks.
- **链接**: [出版页](https://openreview.net/forum?id=K96AogLDT2K)
- **作者**: Xinbiao Wang, Junyu Liu, Tongliang Liu, Yong Luo, Yuxuan Du, Dacheng Tao
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Holistic Adversarially Robust Pruning.
- **链接**: [出版页](https://openreview.net/forum?id=sAJDi9lD06L)
- **作者**: Qi Zhao, Christian Wressnegger
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Coverage-centric Coreset Selection for High Pruning Rates.
- **链接**: [出版页](https://openreview.net/forum?id=QwKvL6wC8Yi)
- **作者**: Haizhong Zheng, Rui Liu, Fan Lai, Atul Prakash
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Minimum Variance Unbiased N: M Sparsity for the Neural Gradients.
- **链接**: [出版页](https://openreview.net/forum?id=vuD2xEtxZcj)
- **作者**: Brian Chmiel, Itay Hubara, Ron Banner, Daniel Soudry
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Rethinking Graph Lottery Tickets: Graph Sparsity Matters.
- **链接**: [出版页](https://openreview.net/forum?id=fjh7UGQgOB)
- **作者**: Bo Hui, Da Yan, Xiaolong Ma, Wei-Shinn Ku
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Implicit Regularization for Group Sparsity.
- **链接**: [出版页](https://openreview.net/forum?id=d7Q0vVfJ0wO)
- **作者**: Jiangyuan Li, Thanh Van Nguyen, Chinmay Hegde, Raymond K. W. Wong
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### The Lazy Neuron Phenomenon: On Emergence of Activation Sparsity in Transformers.
- **链接**: [出版页](https://openreview.net/forum?id=TJ2nxciYCk-)
- **作者**: Zonglin Li, Chong You, Srinadh Bhojanapalli, Daliang Li, Ankit Singh Rawat, Sashank J. Reddi et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### More ConvNets in the 2020s: Scaling up Kernels Beyond 51x51 using Sparsity.
- **链接**: [出版页](https://openreview.net/forum?id=bXNl-myZkJl)
- **作者**: Shiwei Liu, Tianlong Chen, Xiaohan Chen, Xuxi Chen, Qiao Xiao, Boqian Wu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Sparsity May Cry: Let Us Fail (Current) Sparse Neural Networks Together!
- **链接**: [出版页](https://openreview.net/forum?id=J6F3lLg4Kdp)
- **作者**: Shiwei Liu, Tianlong Chen, Zhenyu Zhang, Xuxi Chen, Tianjin Huang, Ajay Kumar Jaiswal et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Sparsity-Constrained Optimal Transport.
- **链接**: [出版页](https://openreview.net/forum?id=yHY9NbQJ5BP)
- **作者**: Tianlin Liu, Joan Puigcerver, Mathieu Blondel
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Efficient recurrent architectures through activity sparsity and sparse back-propagation through time.
- **链接**: [出版页](https://openreview.net/forum?id=lJdOlWg8td)
- **作者**: Anand Subramoney, Khaleelulla Khan Nazeer, Mark Schöne, Christian Mayr, David Kappel
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### UPop: Unified and Progressive Pruning for Compressing Vision-Language Transformers.
- **链接**: [出版页](https://proceedings.mlr.press/v202/shi23e.html)
- **作者**: Dachuan Shi, Chaofan Tao, Ying Jin, Zhendong Yang, Chun Yuan, Jiaqi Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Fast as CHITA: Neural Network Pruning with Combinatorial Optimization.
- **链接**: [出版页](https://proceedings.mlr.press/v202/benbaki23a.html)
- **作者**: Riade Benbaki, Wenyu Chen, Xiang Meng, Hussein Hazimeh, Natalia Ponomareva, Zhe Zhao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Why Random Pruning Is All We Need to Start Sparse.
- **链接**: [出版页](https://proceedings.mlr.press/v202/gadhikar23a.html)
- **作者**: Advait Harshal Gadhikar, Sohom Mukherjee, Rebekka Burkholz
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Instant Soup: Cheap Pruning Ensembles in A Single Pass Can Draw Lottery Tickets from Large Models.
- **链接**: [出版页](https://proceedings.mlr.press/v202/jaiswal23b.html)
- **作者**: Ajay Kumar Jaiswal, Shiwei Liu, Tianlong Chen, Ying Ding, Zhangyang Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Reconstructive Neuron Pruning for Backdoor Defense.
- **链接**: [出版页](https://proceedings.mlr.press/v202/li23v.html)
- **作者**: Yige Li, Xixiang Lyu, Xingjun Ma, Nodens Koren, Lingjuan Lyu, Bo Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Pruning via Sparsity-indexed ODE: a Continuous Sparsity Viewpoint.
- **链接**: [出版页](https://proceedings.mlr.press/v202/mo23c.html)
- **作者**: Zhanfeng Mo, Haosen Shi, Sinno Jialin Pan
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Gradient-Free Structured Pruning with Unlabeled Data.
- **链接**: [出版页](https://proceedings.mlr.press/v202/nova23a.html)
- **作者**: Azade Nova, Hanjun Dai, Dale Schuurmans
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### UPSCALE: Unconstrained Channel Pruning.
- **链接**: [出版页](https://proceedings.mlr.press/v202/wan23a.html)
- **作者**: Alvin Wan, Hanxiang Hao, Kaushik Patnaik, Yueyang Xu, Omer Hadad, David Güera et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### A Three-regime Model of Network Pruning.
- **链接**: [出版页](https://proceedings.mlr.press/v202/zhou23p.html)
- **作者**: Yefan Zhou, Yaoqing Yang, Arin Chang, Michael W. Mahoney
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Does Sparsity Help in Learning Misspecified Linear Bandits?
- **链接**: [出版页](https://proceedings.mlr.press/v202/dong23g.html)
- **作者**: Jialin Dong, Lin Yang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Synergies between Disentanglement and Sparsity: Generalization and Identifiability in Multi-Task Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v202/lachapelle23a.html)
- **作者**: Sébastien Lachapelle, Tristan Deleu, Divyat Mahajan, Ioannis Mitliagkas, Yoshua Bengio, Simon Lacoste-Julien et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time.
- **链接**: [出版页](https://proceedings.mlr.press/v202/liu23am.html)
- **作者**: Zichang Liu, Jue Wang, Tri Dao, Tianyi Zhou, Binhang Yuan, Zhao Song et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### STEP: Learning N: M Structured Sparsity Masks from Scratch with Precondition.
- **链接**: [出版页](https://proceedings.mlr.press/v202/lu23c.html)
- **作者**: Yucheng Lu, Shivani Agrawal, Suvinay Subramanian, Oleg Rybakov, Christopher De Sa, Amir Yazdanbakhsh
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### SpENCNN: Orchestrating Encoding and Sparsity for Fast Homomorphically Encrypted Neural Network Inference.
- **链接**: [出版页](https://proceedings.mlr.press/v202/ran23b.html)
- **作者**: Ran Ran, Xinwei Luo, Wei Wang, Tao Liu, Gang Quan, Xiaolin Xu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Context Consistency Regularization for Label Sparsity in Time Series.
- **链接**: [出版页](https://proceedings.mlr.press/v202/shin23e.html)
- **作者**: Yooju Shin, Susik Yoon, Hwanjun Song, Dongmin Park, Byunghyun Kim, Jae-Gil Lee et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Extending Kernel PCA through Dualization: Sparsity, Robustness and Fast Algorithms.
- **链接**: [出版页](https://proceedings.mlr.press/v202/tonin23a.html)
- **作者**: Francesco Tonin, Alex Lambert, Panagiotis Patrinos, Johan A. K. Suykens
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### When Sparsity Meets Contrastive Models: Less Graph Data Can Bring Better Class-Balanced Representations.
- **链接**: [出版页](https://proceedings.mlr.press/v202/zhang23o.html)
- **作者**: Chunhui Zhang, Chao Huang, Yijun Tian, Qianlong Wen, Zhongyu Ouyang, Youhuan Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Less is More: Task-aware Layer-wise Distillation for Language Model Compression.
- **链接**: [出版页](https://proceedings.mlr.press/v202/liang23j.html)
- **作者**: Chen Liang, Simiao Zuo, Qingru Zhang, Pengcheng He, Weizhu Chen, Tuo Zhao
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### One Less Reason for Filter Pruning: Gaining Free Adversarial Robustness with Structured Grouped Kernel Pruning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/c3aba4234afd1c8116d879ba183f4835-Abstract-Conference.html)
- **作者**: Shaochen (Henry) Zhong, Zaichuan You, Jiamu Zhang, Sebastian Zhao, Zachary LeClaire, Zirui Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Dynamic Context Pruning for Efficient and Interpretable Autoregressive Transformers.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/cdaac2a02c4fdcae77ba083b110efcc3-Abstract-Conference.html)
- **作者**: Sotiris Anagnostidis, Dario Pavllo, Luca Biggio, Lorenzo Noci, Aurélien Lucchi, Thomas Hofmann
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Optimal Parameter and Neuron Pruning for Out-of-Distribution Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/a4316bb210a59fb7aafeca5dd21c2703-Abstract-Conference.html)
- **作者**: Chao Chen, Zhihang Fu, Kai Liu, Ze Chen, Mingyuan Tao, Jieping Ye
- **🏷️ 机构**:  Alibaba / Zhejiang Lab
- **会议**: NeurIPS 2023

### PDP: Parameter-free Differentiable Pruning is All You Need.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/8f9f4eb32b9081a90f2a0b2627eb2a24-Abstract-Conference.html)
- **作者**: Minsik Cho, Saurabh Adya, Devang Naik
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Structural Pruning for Diffusion Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/35c1d69d23bb5dd6b9abcd68be005d5c-Abstract-Conference.html)
- **作者**: Gongfan Fang, Xinyin Ma, Xinchao Wang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### You Only Condense Once: Two Rules for Pruning Condensed Datasets.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/7bdd36a198a8408f444834039b09f518-Abstract-Conference.html)
- **作者**: Yang He, Lingao Xiao, Joey Tianyi Zhou
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### ZipLM: Inference-Aware Structured Pruning of Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/ced46a50befedcb884ccf0cbe8c3ad23-Abstract-Conference.html)
- **作者**: Eldar Kurtic, Elias Frantar, Dan Alistarh
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Pruning vs Quantization: Which is Better?
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/c48bc80aa5d3cbbdd712d1cc107b8319-Abstract-Conference.html)
- **作者**: Andrey Kuzmin, Markus Nagel, Mart van Baalen, Arash Behboodi, Tijmen Blankevoort
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### CAP: Correlation-Aware Pruning for Highly-Accurate Sparse Vision Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/5bd9fbb3a5a985f80c16ddd0ec1dfc43-Abstract-Conference.html)
- **作者**: Denis Kuznedelev, Eldar Kurtic, Elias Frantar, Dan Alistarh
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### LLM-Pruner: On the Structural Pruning of Large Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/44956951349095f74492a5471128a7e0-Abstract-Conference.html)
- **作者**: Xinyin Ma, Gongfan Fang, Xinchao Wang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Robust Data Pruning under Label Noise via Maximizing Re-labeling Accuracy.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/ebb6bee50913ba7e1efeb91a1d47a002-Abstract-Conference.html)
- **作者**: Dongmin Park, Seola Choi, Doyoung Kim, Hwanjun Song, Jae-Gil Lee
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Neural Sculpting: Uncovering hierarchically modular task structure in neural networks through pruning and network analysis.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/3b1675de6b49cc00084374213f8c38ae-Abstract-Conference.html)
- **作者**: Shreyas Malakarjun Patil, Loizos Michael, Constantine Dovrolis
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Towards Data-Agnostic Pruning At Initialization: What Makes a Good Sparse Mask?
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/fd5013ea0c3f96931dec77174eaf9d80-Abstract-Conference.html)
- **作者**: Hoang Pham, The-Anh Ta, Shiwei Liu, Lichuan Xiang, Dung Le, Hongkai Wen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Greedy Pruning with Group Lasso Provably Generalizes for Matrix Sensing.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/bd2107343c9cc973635d90dbfc122223-Abstract-Conference.html)
- **作者**: Nived Rajaraman, Devvrit, Aryan Mokhtari, Kannan Ramchandran
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Data Pruning via Moving-one-Sample-out.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/3abe23bf7e295b44369c24465d68987a-Abstract-Conference.html)
- **作者**: Haoru Tan, Sitong Wu, Fei Du, Yukang Chen, Zhibin Wang, Fan Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Towards Higher Ranks via Adversarial Weight Pruning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/040ace837dd270a87055bb10dd7c0392-Abstract-Conference.html)
- **作者**: Yuchuan Tian, Hanting Chen, Tianyu Guo, Chao Xu, Yunhe Wang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### SUBP: Soft Uniform Block Pruning for 1×N Sparse CNNs Multithreading Acceleration.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/a36c3dbe676fa8445715a31a90c66ab3-Abstract-Conference.html)
- **作者**: Jingyang Xiang, Siqi Li, Jun Chen, Guang Dai, Shipeng Bai, Yukai Ma et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Selectivity Drives Productivity: Efficient Dataset Pruning for Enhanced Transfer Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/749252feedd44f7f10d47ec1d674a2f8-Abstract-Conference.html)
- **作者**: Yihua Zhang, Yimeng Zhang, Aochuan Chen, Jinghan Jia, Jiancheng Liu, Gaowen Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Dynamic Sparsity Is Channel-Level Sparsity Learner.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/d6d0e41e0b1ed38c76d13c9e417a8f1f-Abstract-Conference.html)
- **作者**: Lu Yin, Gen Li, Meng Fang, Li Shen, Tianjin Huang, Zhangyang Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Penalising the biases in norm regularisation enforces sparsity.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/b444ad72520a5f5c467343be88e352ed-Abstract-Conference.html)
- **作者**: Etienne Boursier, Nicolas Flammarion
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Path Regularization: A Convexity and Sparsity Inducing Regularization for Parallel ReLU Networks.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/bbf38332580c1bed99fa99bc9ee53229-Abstract-Conference.html)
- **作者**: Tolga Ergen, Mert Pilanci
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Sparsity-Preserving Differentially Private Training of Large Embedding Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/23ff02034404b65776080cbf7148addd-Abstract-Conference.html)
- **作者**: Badih Ghazi, Yangsibo Huang, Pritish Kamath, Ravi Kumar, Pasin Manurangsi, Amer Sinha et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### The Emergence of Essential Sparsity in Large Pre-trained Models: The Weights that Matter.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/7a69ab48efcbb0153e72d458fb091969-Abstract-Conference.html)
- **作者**: Ajay Jaiswal, Shiwei Liu, Tianlong Chen, Zhangyang Wang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Model Sparsity Can Simplify Machine Unlearning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/a204aa68ab4e970e1ceccfb5b5cdc5e4-Abstract-Conference.html)
- **作者**: Jinghan Jia, Jiancheng Liu, Parikshit Ram, Yuguang Yao, Gaowen Liu, Yang Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Robust Model Reasoning and Fitting via Dual Sparsity Pursuit.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/e1de63ec74f40d3234c4e053f3528e18-Abstract-Conference.html)
- **作者**: Xingyu Jiang, Jiayi Ma
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### High-dimensional Contextual Bandit Problem without Sparsity.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/9b35a0a20d617dc68ae98a7a57df2f51-Abstract-Conference.html)
- **作者**: Junpei Komiyama, Masaaki Imaizumi
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Emergence of Shape Bias in Convolutional Neural Networks through Activation Sparsity.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/e31c16c7b3e0ccee5159ae5443154fac-Abstract-Conference.html)
- **作者**: Tianqin Li, Ziqi Wen, Yangfan Li, Tai Sing Lee
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Stability-penalty-adaptive follow-the-regularized-leader: Sparsity, game-dependency, and best-of-both-worlds.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/9408564a4229f4a933ac9bd09a29ee96-Abstract-Conference.html)
- **作者**: Taira Tsuchiya, Shinji Ito, Junya Honda
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Generalizing Nonlinear ICA Beyond Structural Sparsity.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/2aebc17b683792a17dd4a24fcb038ba6-Abstract-Conference.html)
- **作者**: Yujia Zheng, Kun Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

## 跨领域论文（完整笔记在其他领域）

- RepQ-ViT: Scale Reparameterization for Post-Training Quantization of Vision Transformers. → [vision-transformer](../vision-transformer/Guideline%202023.md)
- Bi-LRFusion: Bi-Directional LiDAR-Radar Fusion for 3D Dynamic Object Detection. → [object-detection](../object-detection/Guideline%202023.md)
- itKD: Interchange Transfer-based Knowledge Distillation for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- SparseViT: Revisiting Activation Sparsity for Efficient High-Resolution Vision Transformer. → [vision-transformer](../vision-transformer/Guideline%202023.md)
- Class-Incremental Exemplar Compression for Class-Incremental Learning. → [continual-learning](../continual-learning/Guideline%202023.md)
- Representation Disparity-aware Distillation for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- MonoNeRD: NeRF-like Representations for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Ada3D : Exploiting the Spatial Redundancy with Adaptive Inference for Efficient 3D Object Detection. → [bev](../bev/Guideline%202023.md)
- Revisiting Vision Transformer from the View of Path Ensemble. → [vision-transformer](../vision-transformer/Guideline%202023.md)
- Growing a Brain with Sparsity-Inducing Generation for Continual Learning. → [continual-learning](../continual-learning/Guideline%202023.md)
- TinyCLIP: CLIP Distillation via Affinity Mimicking and Weight Inheritance. → [vlm](../vlm/Guideline%202023.md)

<!-- COMPLETE v1 papers=102 -->
