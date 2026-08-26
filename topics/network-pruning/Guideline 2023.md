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
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00205) · 📚 被引 63
- **作者**: Xuanyao Chen, Zhijian Liu, Haotian Tang, Li Yi, Hang Zhao, Song Han
- **🏷️ 机构**: Shanghai Qi Zhi Institute, MIT
- **会议**: CVPR 2023

### Joint Token Pruning and Squeezing Towards More Aggressive Compression of Vision Transformers.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00208) · 📚 被引 75
- **作者**: Siyuan Wei, Tianzhu Ye, Shen Zhang, Yao Tang, Jiajun Liang
- **🏷️ 机构**: MEGVII Technology, Tsinghua University
- **会议**: CVPR 2023

### Global Vision Transformer Pruning with Hessian-Aware Saliency.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01779) · 📚 被引 59
- **作者**: Huanrui Yang, Hongxu Yin, Maying Shen, Pavlo Molchanov, Hai Li, Jan Kautz
- **🏷️ 机构**: NVIDIA, Duke University
- **会议**: CVPR 2023

### Boost Vision Transformer with GPU-Friendly Sparsity and Quantization.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02170) · 📚 被引 35
- **作者**: Chong Yu, Tao Chen, Zhongxue Gan, Jiayuan Fan
- **🏷️ 机构**: Fudan University,Academy for Engineering and Technology, School for Information Science and Technology, Fudan University
- **会议**: CVPR 2023

### X-Pruner: eXplainable Pruning for Vision Transformers.
- **链接**: [arXiv:2303.04935](https://arxiv.org/abs/2303.04935) · 📚 被引 69
- **作者**: Lu Yu, Wei Xiang
- **🏷️ 机构**: James Cook University, La Trobe University
- **会议**: CVPR 2023

- **摘要（英，原文）**:

  > Recently vision transformer models have become prominent models for a range of tasks. These models, however, usually suffer from intensive computational costs and heavy memory requirements, making them impractical for deployment on edge platforms. Recent studies have proposed to prune transformers in an unexplainable manner, which overlook the relationship between internal units of the model and the target class, thereby leading to inferior performance. To alleviate this problem, we propose a novel explainable pruning framework dubbed X-Pruner, which is designed by considering the explainability of the pruning criterion. Specifically, to measure each prunable unit's contribution to predicting each target class, a novel explainability-aware mask is proposed and learned in an end-to-end manner. Then, to preserve the most informative units and learn the layer-wise pruning rate, we adaptively search the layer-wise threshold that differentiates between unpruned and pruned units based on their explainability-aware mask values. To verify and evaluate our method, we apply the X-Pruner on representative transformer models including the DeiT and Swin Transformer. Comprehensive simulation results demonstrate that the proposed X-Pruner outperforms the state-of-the-art black-box methods with significantly reduced computational costs and slight performance degradation.

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

- **摘要（英，原文）**:

  > Structural pruning enables model acceleration by removing structurally-grouped parameters from neural networks. However, the parameter-grouping patterns vary widely across different models, making architecture-specific pruners, which rely on manually-designed grouping schemes, non-generalizable to new architectures. In this work, we study a highly-challenging yet barely-explored task, any structural pruning, to tackle general structural pruning of arbitrary architecture like CNNs, RNNs, GNNs and Transformers. The most prominent obstacle towards this goal lies in the structural coupling, which not only forces different layers to be pruned simultaneously, but also expects all removed parameters to be consistently unimportant, thereby avoiding structural issues and significant performance degradation after pruning. To address this problem, we propose a general and {fully automatic} method, \emph{Dependency Graph} (DepGraph), to explicitly model the dependency between layers and comprehensively group coupled parameters for pruning. In this work, we extensively evaluate our method on several architectures and tasks, including ResNe(X)t, DenseNet, MobileNet and Vision transformer for images, GAT for graph, DGCNN for 3D point cloud, alongside LSTM for language, and demonstrate that, even with a simple norm-based criterion, the proposed method consistently yields gratifying performances.

### CP3: Channel Pruning Plug-in for Point-Based Networks.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00513)
- **作者**: Yaomin Huang, Ning Liu, Zhengping Che, Zhiyuan Xu, Chaomin Shen, Yaxin Peng et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

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
