# Network Pruning — 2022 Guideline

> 领域: 网络剪枝 / 模型压缩（结构化剪枝、稀疏化）
> 论文数: 16 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Point Cloud Compression with Sibling Context and Surface Priors.
- **链接**: [arXiv:2205.00760](https://arxiv.org/abs/2205.00760) · 📚 被引 28
- **作者**: Zhili Chen, Zian Qian, Sukai Wang, Qifeng Chen
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a novel octree-based multi-level framework for large-scale point cloud compression, which can organize sparse and unstructured point clouds in a memory-efficient way. In this framework, we propose a new entropy model that explores the hierarchical dependency in an octree using the context of siblings' children, ancestors, and neighbors to encode the occupancy information of each non-leaf octree node into a bitstream. Moreover, we locally fit quadratic surfaces with a voxel-based geometry-aware module to provide geometric priors in entropy encoding. These strong priors empower our entropy framework to encode the octree into a more compact bitstream. In the decoding stage, we apply a two-step heuristic strategy to restore point clouds with better reconstruction quality. The quantitative evaluation shows that our method outperforms state-of-the-art baselines with a bitrate improvement of 11-16% and 12-14% on the KITTI Odometry and nuScenes datasets, respectively.

</details>

### SPViT: Enabling Faster Vision Transformers via Latency-Aware Soft Token Pruning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20083-0_37) · 📚 被引 160
- **作者**: Zhenglun Kong, Peiyan Dong, Xiaolong Ma, Xin Meng, Wei Niu, Mengshu Sun et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### SuperTickets: Drawing Task-Agnostic Lottery Tickets from Supernets via Jointly Architecture Searching and Parameter Pruning.
- **链接**: [arXiv:2207.03677](https://arxiv.org/abs/2207.03677) · [代码](https://github.com/RICE-EIC/SuperTickets) · 📚 被引 8
- **作者**: Haoran You, Baopu Li, Zhanyi Sun, Xu Ouyang, Yingyan Lin
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural architecture search (NAS) has demonstrated amazing success in searching for efficient deep neural networks (DNNs) from a given supernet. In parallel, the lottery ticket hypothesis has shown that DNNs contain small subnetworks that can be trained from scratch to achieve a comparable or higher accuracy than original DNNs. As such, it is currently a common practice to develop efficient DNNs via a pipeline of first search and then prune. Nevertheless, doing so often requires a search-train-prune-retrain process and thus prohibitive computational cost. In this paper, we discover for the first time that both efficient DNNs and their lottery subnetworks (i.e., lottery tickets) can be directly identified from a supernet, which we term as SuperTickets, via a two-in-one training scheme with jointly architecture searching and parameter pruning. Moreover, we develop a progressive and unified SuperTickets identification strategy that allows the connectivity of subnetworks to change during supernet training, achieving better accuracy and efficiency trade-offs than conventional sparse training. Finally, we evaluate whether such identified SuperTickets drawn from one task can transfer well to other tasks, validating their potential of handling multiple tasks simultaneously. Extensive experiments and ablation studies on three tasks and four benchmark datasets validate that our proposed SuperTickets achieve boosted accuracy and efficiency trade-offs than both typical NAS and pruning pipelines, regardless of having retraining or not. Codes and pretrained models are available at https://github.com/RICE-EIC/SuperTickets.

</details>

### Towards Ultra Low Latency Spiking Neural Networks for Vision and Sequential Tasks Using Temporal Pruning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20083-0_42) · 📚 被引 30
- **作者**: Sayeed Shafayet Chowdhury, Nitin Rathi, Kaushik Roy
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Bayesian Optimization with Clustering and Rollback for CNN Auto Pruning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20050-2_29) · 📚 被引 0
- **作者**: Hanwei Fan, Jiandong Mu, Wei Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Interpretations Steered Network Pruning via Amortized Inferred Saliency Maps.
- **链接**: [arXiv:2209.02869](https://arxiv.org/abs/2209.02869) · [代码](https://github.com/Alii-Ganjj/InterpretationsSteeredPruning) · 📚 被引 13
- **作者**: Alireza Ganjdanesh, Shangqian Gao, Heng Huang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Convolutional Neural Networks (CNNs) compression is crucial to deploying these models in edge devices with limited resources. Existing channel pruning algorithms for CNNs have achieved plenty of success on complex models. They approach the pruning problem from various perspectives and use different metrics to guide the pruning process. However, these metrics mainly focus on the model's `outputs' or `weights' and neglect its `interpretations' information. To fill in this gap, we propose to address the channel pruning problem from a novel perspective by leveraging the interpretations of a model to steer the pruning process, thereby utilizing information from both inputs and outputs of the model. However, existing interpretation methods cannot get deployed to achieve our goal as either they are inefficient for pruning or may predict non-coherent explanations. We tackle this challenge by introducing a selector model that predicts real-time smooth saliency masks for pruned models. We parameterize the distribution of explanatory masks by Radial Basis Function (RBF)-like functions to incorporate geometric prior of natural images in our selector model's inductive bias. Thus, we can obtain compact representations of explanations to reduce the computational costs of our pruning method. We leverage our selector model to steer the network pruning by maximizing the similarity of explanatory representations for the pruned and original models. Extensive experiments on CIFAR-10 and ImageNet benchmark datasets demonstrate the efficacy of our proposed method. Our implementations are available at \url{https://github.com/Alii-Ganjj/InterpretationsSteeredPruning}

</details>

### Disentangled Differentiable Network Pruning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20083-0_20) · 📚 被引 14
- **作者**: Shangqian Gao, Feihu Huang, Yanfu Zhang, Heng Huang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Filter Pruning via Feature Discrimination in Deep Neural Networks.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19803-8_15)
- **作者**: Zhiqiang He, Yaguan Qian, Yuqi Wang, Bin Wang, Xiaohui Guan, Zhaoquan Gu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Soft Masking for Cost-Constrained Channel Pruning.
- **链接**: [arXiv:2211.02206](https://arxiv.org/abs/2211.02206) · 📚 被引 15
- **作者**: Ryan Humble, Maying Shen, Jorge Albericio Latorre, Eric Darve, José M. Álvarez
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Structured channel pruning has been shown to significantly accelerate inference time for convolution neural networks (CNNs) on modern hardware, with a relatively minor loss of network accuracy. Recent works permanently zero these channels during training, which we observe to significantly hamper final accuracy, particularly as the fraction of the network being pruned increases. We propose Soft Masking for cost-constrained Channel Pruning (SMCP) to allow pruned channels to adaptively return to the network while simultaneously pruning towards a target cost constraint. By adding a soft mask re-parameterization of the weights and channel pruning from the perspective of removing input channels, we allow gradient updates to previously pruned channels and the opportunity for the channels to later return to the network. We then formulate input channel pruning as a global resource allocation problem. Our method outperforms prior works on both the ImageNet classification and PASCAL VOC detection datasets.

</details>

### CPrune: Compiler-Informed Model Pruning for Efficient Target-Aware DNN Execution.
- **链接**: [arXiv:2207.01260](https://arxiv.org/abs/2207.01260) · 📚 被引 5
- **作者**: Taeho Kim, Yongin Kwon, Jemin Lee, Taeho Kim, Sangtae Ha
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Mobile devices run deep learning models for various purposes, such as image classification and speech recognition. Due to the resource constraints of mobile devices, researchers have focused on either making a lightweight deep neural network (DNN) model using model pruning or generating an efficient code using compiler optimization. Surprisingly, we found that the straightforward integration between model compression and compiler auto-tuning often does not produce the most efficient model for a target device. We propose CPrune, a compiler-informed model pruning for efficient target-aware DNN execution to support an application with a required target accuracy. CPrune makes a lightweight DNN model through informed pruning based on the structural information of subgraphs built during the compiler tuning process. Our experimental results show that CPrune increases the DNN execution speed up to 2.73x compared to the state-of-the-art TVM auto-tune while satisfying the accuracy requirement.

</details>

### Ensemble Knowledge Guided Sub-network Search and Fine-Tuning for Filter Pruning.
- **链接**: [arXiv:2203.02651](https://arxiv.org/abs/2203.02651) · [代码](https://github.com/sseung0703/EKG) · 📚 被引 8
- **作者**: Seunghyun Lee, Byung Cheol Song
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Conventional NAS-based pruning algorithms aim to find the sub-network with the best validation performance. However, validation performance does not successfully represent test performance, i.e., potential performance. Also, although fine-tuning the pruned network to restore the performance drop is an inevitable process, few studies have handled this issue. This paper provides a novel Ensemble Knowledge Guidance (EKG) to solve both problems at once. First, we experimentally prove that the fluctuation of loss landscape can be an effective metric to evaluate the potential performance. In order to search a sub-network with the smoothest loss landscape at a low cost, we employ EKG as a search reward. EKG utilized for the following search iteration is composed of the ensemble knowledge of interim sub-networks, i.e., the by-products of the sub-network evaluation. Next, we reuse EKG to provide a gentle and informative guidance to the pruned network while fine-tuning the pruned network. Since EKG is implemented as a memory bank in both phases, it requires a negligible cost. For example, when pruning and training ResNet-50, just 315 GPU hours are required to remove around 45.04% of FLOPS without any performance degradation, which can operate even on a low-spec workstation. the implemented code is available at https://github.com/sseung0703/EKG.

</details>

### FairGRAPE: Fairness-Aware GRAdient Pruning mEthod for Face Attribute Classification.
- **链接**: [arXiv:2207.10888](https://arxiv.org/abs/2207.10888) · [代码](https://github.com/Bernardo1998/FairGRAPE) · 📚 被引 29
- **作者**: Xiaofeng Lin, Seungbae Kim, Jungseock Joo
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing pruning techniques preserve deep neural networks' overall ability to make correct predictions but may also amplify hidden biases during the compression process. We propose a novel pruning method, Fairness-aware GRAdient Pruning mEthod (FairGRAPE), that minimizes the disproportionate impacts of pruning on different sub-groups. Our method calculates the per-group importance of each model weight and selects a subset of weights that maintain the relative between-group total importance in pruning. The proposed method then prunes network edges with small importance values and repeats the procedure by updating importance values. We demonstrate the effectiveness of our method on four different datasets, FairFace, UTKFace, CelebA, and ImageNet, for the tasks of face attribute classification where our method reduces the disparity in performance degradation by up to 90% compared to the state-of-the-art pruning algorithms. Our method is substantially more effective in a setting with a high pruning rate (99%). The code and dataset used in the experiments are available at https://github.com/Bernardo1998/FairGRAPE

</details>

### Multi-granularity Pruning for Model Acceleration on Mobile Devices.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20083-0_29) · 📚 被引 5
- **作者**: Tianli Zhao, Xi Sheryl Zhang, Wentao Zhu, Jiaxing Wang, Sen Yang, Ji Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Learning Extremely Lightweight and Robust Model with Differentiable Constraints on Sparsity and Condition Number.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19772-7_40) · 📚 被引 1
- **作者**: Xian Wei, Yangyu Xu, Yanhui Huang, Hairong Lv, Hai Lan, Mingsong Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

## 跨领域论文（完整笔记在其他领域）

- Point Cloud Compression with Range Image-Based Entropy Model for Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202022.md)
- FOSTER: Feature Boosting and Compression for Class-Incremental Learning. → [continual-learning](../continual-learning/Guideline%202022.md)
