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

> High-resolution images enable neural networks to learn richer visual representations. However, this improved performance comes at the cost of growing computational complexity, hindering their usage in latency-sensitive applications. As not all pixels are equal, skipping computations for less-important regions offers a simple and effective measure to reduce the computation. This, however, is hard to be translated into actual speedup for CNNs since it breaks the regularity of the dense convolution workload. In this paper, we introduce SparseViT that revisits activation sparsity for recent window-based vision transformers (ViTs). As window attentions are naturally batched over blocks, actual speedup with window activation pruning becomes possible: i.e., ~50% latency reduction with 60% sparsity. Different layers should be assigned with different pruning ratios due to their diverse sensitivities and computational costs. We introduce sparsity-aware adaptation and apply the evolutionary search to efficiently find the optimal layerwise sparsity configuration within the vast search space. SparseViT achieves speedups of 1.5x, 1.4x, and 1.3x compared to its dense counterpart in monocular 3D object detection, 2D instance segmentation, and 2D semantic segmentation, respectively, with negligible to no loss of accuracy.

</details>

### Joint Token Pruning and Squeezing Towards More Aggressive Compression of Vision Transformers.
- **链接**: [arXiv:2304.10716](https://arxiv.org/abs/2304.10716) · [代码](https://github.com/megvii-research/TPS-CVPR2023) · 📚 被引 75
- **作者**: Siyuan Wei, Tianzhu Ye, Shen Zhang, Yao Tang, Jiajun Liang
- **🏷️ 机构**: MEGVII Technology, Tsinghua University
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Although vision transformers (ViTs) have shown promising results in various computer vision tasks recently, their high computational cost limits their practical applications. Previous approaches that prune redundant tokens have demonstrated a good trade-off between performance and computation costs. Nevertheless, errors caused by pruning strategies can lead to significant information loss. Our quantitative experiments reveal that the impact of pruned tokens on performance should be noticeable. To address this issue, we propose a novel joint Token Pruning & Squeezing module (TPS) for compressing vision transformers with higher efficiency. Firstly, TPS adopts pruning to get the reserved and pruned subsets. Secondly, TPS squeezes the information of pruned tokens into partial reserved tokens via the unidirectional nearest-neighbor matching and similarity-based fusing steps. Compared to state-of-the-art methods, our approach outperforms them under all token pruning intensities. Especially while shrinking DeiT-tiny&small computational budgets to 35%, it improves the accuracy by 1%-6% compared with baselines on ImageNet classification. The proposed method can accelerate the throughput of DeiT-small beyond DeiT-tiny, while its accuracy surpasses DeiT-tiny by 4.78%. Experiments on various transformers demonstrate the effectiveness of our method, while analysis experiments prove our higher robustness to the errors of the token pruning policy. Code is available at https://github.com/megvii-research/TPS-CVPR2023.

</details>

### Global Vision Transformer Pruning with Hessian-Aware Saliency.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01779) · 📚 被引 59
- **作者**: Huanrui Yang, Hongxu Yin, Maying Shen, Pavlo Molchanov, Hai Li, Jan Kautz
- **🏷️ 机构**: NVIDIA, Duke University
- **会议**: CVPR 2023

### Boost Vision Transformer with GPU-Friendly Sparsity and Quantization.
- **链接**: [arXiv:2305.10727](https://arxiv.org/abs/2305.10727) · 📚 被引 35
- **作者**: Chong Yu, Tao Chen, Zhongxue Gan, Jiayuan Fan
- **🏷️ 机构**: Fudan University,Academy for Engineering and Technology, School for Information Science and Technology, Fudan University
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The transformer extends its success from the language to the vision domain. Because of the stacked self-attention and cross-attention blocks, the acceleration deployment of vision transformer on GPU hardware is challenging and also rarely studied. This paper thoroughly designs a compression scheme to maximally utilize the GPU-friendly 2:4 fine-grained structured sparsity and quantization. Specially, an original large model with dense weight parameters is first pruned into a sparse one by 2:4 structured pruning, which considers the GPU's acceleration of 2:4 structured sparse pattern with FP16 data type, then the floating-point sparse model is further quantized into a fixed-point one by sparse-distillation-aware quantization aware training, which considers GPU can provide an extra speedup of 2:4 sparse calculation with integer tensors. A mixed-strategy knowledge distillation is used during the pruning and quantization process. The proposed compression scheme is flexible to support supervised and unsupervised learning styles. Experiment results show GPUSQ-ViT scheme achieves state-of-the-art compression by reducing vision transformer models 6.4-12.7 times on model size and 30.3-62 times on FLOPs with negligible accuracy degradation on ImageNet classification, COCO detection and ADE20K segmentation benchmarking tasks. Moreover, GPUSQ-ViT can boost actual deployment performance by 1.39-1.79 times and 3.22-3.43 times of latency and throughput on A100 GPU, and 1.57-1.69 times and 2.11-2.51 times improvement of latency and throughput on AGX Orin.

</details>

### X-Pruner: eXplainable Pruning for Vision Transformers.
- **链接**: [arXiv:2303.04935](https://arxiv.org/abs/2303.04935) · 📚 被引 69
- **作者**: Lu Yu, Wei Xiang
- **🏷️ 机构**: James Cook University, La Trobe University
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently vision transformer models have become prominent models for a range of tasks. These models, however, usually suffer from intensive computational costs and heavy memory requirements, making them impractical for deployment on edge platforms. Recent studies have proposed to prune transformers in an unexplainable manner, which overlook the relationship between internal units of the model and the target class, thereby leading to inferior performance. To alleviate this problem, we propose a novel explainable pruning framework dubbed X-Pruner, which is designed by considering the explainability of the pruning criterion. Specifically, to measure each prunable unit's contribution to predicting each target class, a novel explainability-aware mask is proposed and learned in an end-to-end manner. Then, to preserve the most informative units and learn the layer-wise pruning rate, we adaptively search the layer-wise threshold that differentiates between unpruned and pruned units based on their explainability-aware mask values. To verify and evaluate our method, we apply the X-Pruner on representative transformer models including the DeiT and Swin Transformer. Comprehensive simulation results demonstrate that the proposed X-Pruner outperforms the state-of-the-art black-box methods with significantly reduced computational costs and slight performance degradation.

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

> Channel pruning can effectively reduce both computational cost and memory footprint of the original network while keeping a comparable accuracy performance. Though great success has been achieved in channel pruning for 2D image-based convolutional networks (CNNs), existing works seldom extend the channel pruning methods to 3D point-based neural networks (PNNs). Directly implementing the 2D CNN channel pruning methods to PNNs undermine the performance of PNNs because of the different representations of 2D images and 3D point clouds as well as the network architecture disparity. In this paper, we proposed CP$^3$, which is a Channel Pruning Plug-in for Point-based network. CP$^3$ is elaborately designed to leverage the characteristics of point clouds and PNNs in order to enable 2D channel pruning methods for PNNs. Specifically, it presents a coordinate-enhanced channel importance metric to reflect the correlation between dimensional information and individual channel features, and it recycles the discarded points in PNN's sampling process and reconsiders their potentially-exclusive information to enhance the robustness of channel pruning. Experiments on various PNN architectures show that CP$^3$ constantly improves state-of-the-art 2D CNN pruning approaches on different point cloud tasks. For instance, our compressed PointNeXt-S on ScanObjectNN achieves an accuracy of 88.52% with a pruning rate of 57.8%, outperforming the baseline pruning methods with an accuracy gain of 1.94%.

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
