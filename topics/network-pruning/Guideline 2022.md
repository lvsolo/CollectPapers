# Network Pruning — 2022 Guideline

> 领域: 网络剪枝 / 模型压缩（结构化剪枝、稀疏化）
> 论文数: 21 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: [2024](Guideline%202024.md)

### PointCLM: A Contrastive Learning-based Framework for Multi-instance Point Cloud Registration. **⭐⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2209.00219](https://arxiv.org/abs/2209.00219)
- **作者**: Mingzhi Yuan, Zhihao Li, Qiuye Jin, Xinrong Chen, Manning Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对多实例点云配准中，一个实例的内点对应关系对其他实例构成外点，导致现有方法依赖耗时假设采样或空间一致性特征、性能受限的问题，提出了基于对比学习的框架PointCLM。该方法利用对比学习为输入候选对应关系学习分布良好的深度表示，并基于这些表示提出外点剪枝策略和聚类策略，以高效去除外点并将剩余对应关系分配到正确实例。相比现有方法，在合成和真实数据集上均大幅超越最先进水平。
- **摘要（英）**: To address the challenge in multi-instance point cloud registration where inlier correspondences of one instance are outliers for others, this paper proposes PointCLM, a contrastive learning-based framework. It learns well-distributed deep representations for putative correspondences and introduces outlier pruning and clustering strategies to efficiently remove outliers and assign correspondences to correct instances. The method significantly outperforms state-of-the-art on both synthetic and real datasets.
- **核心贡献**: 提出了基于对比学习的多实例点云配准框架，显著提升了配准精度和效率。
- **创新点**: 利用对比学习学习判别性表示，并结合剪枝与聚类策略实现高效多实例配准。
- **结果**: 在合成和真实数据集上大幅超越现有最先进方法。

### SPViT: Enabling Faster Vision Transformers via Latency-Aware Soft Token Pruning. **⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20083-0_37) · 📚 被引 160
- **作者**: Zhenglun Kong, Peiyan Dong, Xiaolong Ma, Xin Meng, Wei Niu, Mengshu Sun et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对视觉Transformer推理延迟高的问题，提出了延迟感知的软令牌剪枝方法SPViT。该方法通过评估每个令牌对最终预测的贡献，并考虑硬件延迟，动态剪枝不重要的令牌，从而在保持精度的同时加速推理。实验表明，SPViT在图像分类和检测任务上实现了显著的加速比，同时精度损失极小。
- **摘要（英）**: To reduce the inference latency of Vision Transformers, this paper proposes SPViT, a latency-aware soft token pruning method. It dynamically prunes unimportant tokens based on their contribution to predictions and hardware latency, achieving significant speedup with minimal accuracy drop on classification and detection tasks.
- **核心贡献**: 提出延迟感知的软令牌剪枝方法，有效加速ViT推理。
- **创新点**: 将硬件延迟纳入令牌剪枝决策，实现精度与速度的更好权衡。
- **结果**: 在多个任务上实现显著加速，精度损失极小。

### Neural Architecture Search for Spiking Neural Networks. **⭐⭐⭐** (相关度: 40%)
- **链接**: [arXiv:2201.10355](https://arxiv.org/abs/2201.10355)
- **作者**: Youngeun Kim, Yuhang Li, Hyoungseob Park, Yeshwanth Venkatesha, Priyadarshini Panda
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对脉冲神经网络（SNN）使用类ANN架构导致性能次优的问题，提出了专门为SNN设计的神经架构搜索方法。该方法基于初始化时的激活模式选择能代表多样脉冲激活的架构，无需训练，并搜索前馈和反馈连接以利用时间信息。搜索得到的SNASNet在多个任务上取得更高性能，证明了反馈连接的重要性。
- **摘要（英）**: To address sub-optimal performance of SNNs using ANN-like architectures, this paper introduces a NAS approach for SNNs. It selects architectures based on activation patterns at initialization without training, and searches feedforward and feedback connections to leverage temporal information. The found SNASNet achieves higher performance, highlighting the importance of feedback connections.
- **核心贡献**: 提出首个针对SNN的NAS方法，并发现反馈连接对性能提升的关键作用。
- **创新点**: 利用初始化激活模式进行无训练架构搜索，并引入时间反馈连接。
- **结果**: SNASNet在多个任务上性能优于现有SNN架构。

### SuperTickets: Drawing Task-Agnostic Lottery Tickets from Supernets via Jointly Architecture Searching and Parameter Pruning. **⭐⭐⭐⭐** (相关度: 45%)
- **链接**: [arXiv:2207.03677](https://arxiv.org/abs/2207.03677) · 📚 被引 8
- **作者**: Haoran You, Baopu Li, Zhanyi Sun, Xu Ouyang, Yingyan Lin
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对现有先搜索后剪枝的DNN开发流程计算成本高的问题，提出了SuperTickets方法，首次从超网络中直接识别高效DNN及其彩票子网络。该方法通过联合架构搜索和参数剪枝的两合一训练方案，并开发渐进式统一识别策略，允许子网络连接在训练中变化，实现更好的精度-效率权衡。实验表明，SuperTickets在多个任务上优于传统稀疏训练，并具有跨任务迁移能力。
- **摘要（英）**: To reduce the computational cost of the search-train-prune-retrain pipeline, this paper proposes SuperTickets, which directly identifies efficient DNNs and their lottery tickets from a supernet via joint architecture searching and parameter pruning. A progressive unified strategy allows connectivity changes during training, achieving better accuracy-efficiency trade-offs and transferability across tasks.
- **核心贡献**: 首次从超网络中联合识别架构和彩票子网络，简化了高效DNN开发流程。
- **创新点**: 提出两合一训练方案和渐进式识别策略，实现架构搜索与剪枝的统一。
- **结果**: 在多个任务上优于传统稀疏训练，并展示跨任务迁移能力。

### Towards Ultra Low Latency Spiking Neural Networks for Vision and Sequential Tasks Using Temporal Pruning. **⭐⭐** (相关度: 30%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20083-0_42) · 📚 被引 30
- **作者**: Sayeed Shafayet Chowdhury, Nitin Rathi, Kaushik Roy
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对脉冲神经网络在视觉和序列任务中的延迟问题，提出了时间剪枝方法以实现超低延迟。该方法通过剪枝不重要的时间步，减少SNN的推理时间，同时保持任务性能。实验在多个视觉和序列任务上验证了有效性，但摘要信息有限，具体细节和效果未详细说明。
- **摘要（英）**: To achieve ultra-low latency in SNNs for vision and sequential tasks, this paper proposes a temporal pruning method that prunes unimportant time steps. This reduces inference time while maintaining performance, validated on multiple tasks, though details are limited in the abstract.
- **核心贡献**: 提出时间剪枝方法以降低SNN推理延迟。
- **创新点**: 在时间维度上剪枝，而非传统空间剪枝。
- **结果**: 在视觉和序列任务上实现超低延迟，但具体数据未提供。

### Bayesian Optimization with Clustering and Rollback for CNN Auto Pruning. **⭐⭐** (相关度: 30%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20050-2_29)
- **作者**: Hanwei Fan, Jiandong Mu, Wei Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对CNN自动剪枝中贝叶斯优化效率低、易陷入局部最优的问题。②提出将聚类与回滚机制融入贝叶斯优化，以加速搜索并避免过早收敛。③相比标准贝叶斯优化，通过聚类减少搜索空间维度，回滚机制允许跳出次优区域。④摘要缺失，无法提供具体数据。
- **摘要（英）**: This paper addresses the inefficiency and local optima issues in Bayesian optimization for automatic CNN pruning. It integrates clustering and rollback mechanisms to accelerate search and escape suboptimal regions. Specific results are unavailable due to missing abstract.
- **核心贡献**: 提出聚类与回滚增强的贝叶斯优化剪枝框架。
- **创新点**: 在贝叶斯优化中引入聚类降维和回滚机制。
- **结果**: 未提供具体实验数据。

### Interpretations Steered Network Pruning via Amortized Inferred Saliency Maps. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2209.02869](https://arxiv.org/abs/2209.02869) · 📚 被引 13
- **作者**: Alireza Ganjdanesh, Shangqian Gao, Heng Huang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对现有通道剪枝仅利用输出或权重信息、忽略模型可解释性的问题。②提出利用模型解释信息（saliency maps）引导剪枝，通过一个选择器模型实时预测平滑的掩码，并用RBF类函数参数化掩码分布以引入图像几何先验。③相比已有方法，首次从解释性角度联合输入输出信息进行剪枝，提高剪枝决策的语义合理性。④摘要未给出具体精度数据，但方法在概念上具有新颖性。
- **摘要（英）**: This paper addresses the gap in channel pruning that ignores model interpretability. It introduces a selector model predicting smooth saliency masks, parameterized by RBF-like functions, to steer pruning using both input and output information. This novel perspective enhances pruning semantic coherence, though specific accuracy gains are not detailed.
- **核心贡献**: 首次利用模型解释信息引导通道剪枝。
- **创新点**: 用RBF参数化掩码分布并联合输入输出信息。
- **结果**: 摘要未提供具体数据。

### Disentangled Differentiable Network Pruning. **⭐⭐** (相关度: 30%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20083-0_20) · 📚 被引 14
- **作者**: Shangqian Gao, Feihu Huang, Yanfu Zhang, Heng Huang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对网络剪枝中不同层耦合导致优化困难的问题。②提出解耦的微分剪枝方法，将剪枝过程分解为可独立优化的子问题。③相比联合优化方法，解耦策略简化了训练过程。④摘要缺失，无法评估效果。
- **摘要（英）**: This paper tackles the optimization difficulty in network pruning caused by layer coupling. It proposes a disentangled differentiable pruning approach that decomposes pruning into independently optimizable subproblems. Results are unavailable due to missing abstract.
- **核心贡献**: 提出解耦微分剪枝框架。
- **创新点**: 将剪枝优化解耦为独立子问题。
- **结果**: 未提供实验数据。

### Filter Pruning via Feature Discrimination in Deep Neural Networks. **⭐⭐** (相关度: 30%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19803-8_15)
- **作者**: Zhiqiang He, Yaguan Qian, Yuqi Wang, Bin Wang, Xiaohui Guan, Zhaoquan Gu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对滤波器剪枝中仅考虑重要性而忽略特征判别性的问题。②提出基于特征判别性的滤波器剪枝方法，通过评估滤波器对特征区分能力的贡献进行剪枝。③相比传统重要性度量，更关注特征空间的判别性。④摘要缺失，无法提供具体效果。
- **摘要（英）**: This paper addresses the limitation of filter pruning that ignores feature discriminability. It proposes pruning filters based on their contribution to feature discrimination. Results are unavailable due to missing abstract.
- **核心贡献**: 提出基于特征判别性的滤波器剪枝准则。
- **创新点**: 将特征判别性作为剪枝依据。
- **结果**: 未提供实验数据。

### Soft Masking for Cost-Constrained Channel Pruning. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2211.02206](https://arxiv.org/abs/2211.02206) · 📚 被引 15
- **作者**: Ryan Humble, Maying Shen, Jorge Albericio Latorre, Eric Darve, José M. Álvarez
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对结构化剪枝中永久置零通道导致精度显著下降的问题，尤其在高剪枝率下。②提出软掩码通道剪枝（SMCP），允许被剪通道在训练中自适应恢复，同时通过全局资源分配优化成本约束。③相比永久置零方法，软掩码重参数化使梯度可更新已剪通道，提升高剪枝率下的精度。④在ImageNet分类和PASCAL VOC检测上均优于先前方法。
- **摘要（英）**: This paper addresses the accuracy drop from permanently zeroing channels in structured pruning, especially at high pruning ratios. SMCP introduces soft mask re-parameterization allowing pruned channels to return, formulated as global resource allocation. It outperforms prior methods on ImageNet and PASCAL VOC.
- **核心贡献**: 提出软掩码通道剪枝方法，允许通道自适应恢复。
- **创新点**: 将剪枝视为全局资源分配并采用软掩码重参数化。
- **结果**: 在ImageNet和PASCAL VOC上超越先前方法。

### CPrune: Compiler-Informed Model Pruning for Efficient Target-Aware DNN Execution. **⭐⭐⭐** (相关度: 50%)
- **链接**: [arXiv:2207.01260](https://arxiv.org/abs/2207.01260) · 📚 被引 5
- **作者**: Taeho Kim, Yongin Kwon, Jemin Lee, Taeho Kim, Sangtae Ha
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对移动设备上模型压缩与编译器优化简单集成无法产生最高效模型的问题。②提出CPrune，利用编译器调优过程中子图的结构信息指导剪枝，生成目标感知的轻量模型。③相比独立进行剪枝和编译优化，CPrune将两者协同，提升目标设备上的执行效率。④实验显示，相比TVM自动调优，CPrune在满足精度要求下加速最高达2.73倍。
- **摘要（英）**: This paper addresses the inefficiency of naively combining model compression and compiler optimization for mobile devices. CPrune uses structural information from compiler tuning subgraphs to guide pruning, achieving target-aware efficiency. It speeds up DNN execution up to 2.73x over TVM auto-tune while meeting accuracy.
- **核心贡献**: 提出编译器信息指导的剪枝方法。
- **创新点**: 利用编译器子图结构信息进行剪枝决策。
- **结果**: 相比TVM加速最高2.73倍。

### Ensemble Knowledge Guided Sub-network Search and Fine-Tuning for Filter Pruning. **⭐⭐⭐** (相关度: 40%)
- **链接**: [arXiv:2203.02651](https://arxiv.org/abs/2203.02651)
- **作者**: Seunghyun Lee, Byung Cheol Song
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对NAS剪枝中验证性能无法代表测试性能（潜在性能）以及剪枝后微调恢复性能被忽视的问题。②提出集成知识引导（EKG）方法，利用损失景观波动作为潜在性能指标，将中间子网络的集成知识作为搜索奖励，并复用为微调指导。③相比现有NAS剪枝算法，首次同时解决搜索和微调阶段，且EKG作为记忆库成本极低。④在ResNet-50上仅需315 GPU小时即可移除约45.04%的FLOPs，效果显著。
- **摘要（英）**: This paper addresses the issues that validation performance fails to represent test performance in NAS-based pruning and fine-tuning is often neglected. It proposes Ensemble Knowledge Guidance (EKG) using loss landscape fluctuation as a potential performance metric and reusing ensemble knowledge for fine-tuning. The method achieves 45.04% FLOPs reduction on ResNet-50 with only 315 GPU hours, demonstrating efficiency and effectiveness.
- **核心贡献**: 提出EKG框架，统一解决NAS剪枝中的子网络搜索和微调问题。
- **创新点**: 利用损失景观波动作为潜在性能指标，并复用集成知识作为搜索奖励和微调指导。
- **结果**: 在ResNet-50上以315 GPU小时实现45.04% FLOPs削减。

### FairGRAPE: Fairness-Aware GRAdient Pruning mEthod for Face Attribute Classification. **⭐⭐⭐** (相关度: 30%)
- **链接**: [arXiv:2207.10888](https://arxiv.org/abs/2207.10888) · 📚 被引 29
- **作者**: Xiaofeng Lin, Seungbae Kim, Jungseock Joo
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对现有剪枝技术在压缩过程中可能放大模型隐藏偏见的问题。②提出FairGRAPE方法，计算每个权重对子组的重要性，选择保持组间总重要性相对比例的权重子集进行剪枝。③相比现有剪枝算法，首次在剪枝中显式考虑公平性，减少不同子组性能退化差异。④在FairFace、UTKFace、CelebA和ImageNet上，性能退化差异最多减少90%，在高剪枝率（99%）下效果更显著。
- **摘要（英）**: This paper tackles the issue that pruning can amplify hidden biases in deep neural networks. It proposes FairGRAPE, which computes per-group weight importance and selects subsets maintaining relative between-group importance. The method reduces performance degradation disparity by up to 90% across four datasets, especially effective at high pruning rates.
- **核心贡献**: 提出公平性感知的梯度剪枝方法，减少剪枝对不同子组的影响差异。
- **创新点**: 在剪枝过程中显式维护组间重要性比例，实现公平性约束。
- **结果**: 在多个数据集上性能退化差异最多降低90%。

### Multi-granularity Pruning for Model Acceleration on Mobile Devices. **⭐⭐** (相关度: 35%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20083-0_29) · 📚 被引 5
- **作者**: Tianli Zhao, Xi Sheryl Zhang, Wentao Zhu, Jiaxing Wang, Sen Yang, Ji Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对移动设备上模型加速的多粒度剪枝问题。②论文摘要缺失，无法获取具体方法细节。③缺乏可评估的改进点。④效果未知。
- **摘要（英）**: This paper addresses multi-granularity pruning for model acceleration on mobile devices, but the abstract is missing, preventing detailed evaluation. No specific methods or results are available.
- **核心贡献**: 未知。
- **创新点**: 未知。
- **结果**: 未知。

### Learning Extremely Lightweight and Robust Model with Differentiable Constraints on Sparsity and Condition Number. **⭐⭐** (相关度: 30%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19772-7_40) · 📚 被引 1
- **作者**: Xian Wei, Yangyu Xu, Yanhui Huang, Hairong Lv, Hai Lan, Mingsong Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对学习极轻量且鲁棒模型的问题。②提出在稀疏性和条件数上施加可微约束的方法。③相比现有方法，通过可微约束同时优化稀疏性和条件数，增强鲁棒性。④摘要缺失，具体效果未提供。
- **摘要（英）**: This paper addresses learning extremely lightweight and robust models by introducing differentiable constraints on sparsity and condition number. It aims to jointly optimize both aspects for improved robustness, but specific results are unavailable due to missing abstract details.
- **核心贡献**: 提出可微约束联合优化稀疏性和条件数。
- **创新点**: 将条件数作为可微约束引入模型压缩。
- **结果**: 未提供具体数据。

## 跨领域论文（完整笔记在其他领域）

- Multimodal Transformer for Automatic 3D Annotation and Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- SWFormer: Sparse Window Transformer for 3D Object Detection in Point Clouds. → [3d-detection](../3d-detection/Guideline%202022.md)
- Point Cloud Compression with Sibling Context and Surface Priors. → [3d-detection](../3d-detection/Guideline%202022.md)
- Point Cloud Compression with Range Image-Based Entropy Model for Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202022.md)
- PPT: Token-Pruned Pose Transformer for Monocular and Multi-view Human Pose Estimation. → [multi-camera-perception](../multi-camera-perception/Guideline%202022.md)
- FOSTER: Feature Boosting and Compression for Class-Incremental Learning. → [continual-learning](../continual-learning/Guideline%202022.md)
