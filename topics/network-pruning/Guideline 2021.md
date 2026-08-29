# Network Pruning — 2021 Guideline

> 领域: 网络剪枝 / 模型压缩（结构化剪枝、稀疏化）
> 论文数: 10 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### NPAS: A Compiler-Aware Framework of Unified Network Pruning and Architecture Search for Beyond Real-Time Mobile Acceleration.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Li_NPAS_A_Compiler-Aware_Framework_of_Unified_Network_Pruning_and_Architecture_CVPR_2021_paper.html) · 📚 被引 25
- **作者**: Zhengang Li, Geng Yuan, Wei Niu, Pu Zhao, Yanyu Li, Yuxuan Cai et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Network Pruning via Performance Maximization.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Gao_Network_Pruning_via_Performance_Maximization_CVPR_2021_paper.html) · 📚 被引 110
- **作者**: Shangqian Gao, Feihu Huang, Weidong Cai, Heng Huang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Learnable Motion Coherence for Correspondence Pruning.
- **链接**: [arXiv:2011.14563](https://arxiv.org/abs/2011.14563) · 📚 被引 62
- **作者**: Yuan Liu, Lingjie Liu, Cheng Lin, Zhen Dong, Wenping Wang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Achieving on-Mobile Real-Time Super-Resolution with Neural Architecture and Pruning Search.
- **链接**: [arXiv:2108.08910](https://arxiv.org/abs/2108.08910) · 📚 被引 52
- **作者**: Zheng Zhan, Yifan Gong, Pu Zhao, Geng Yuan, Wei Niu, Yushu Wu et al.
- **🏷️ 机构**: Northeastern University, College of William &#x0026; Mary, Cleveland State University
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Motion coherence is an important clue for distinguishing true correspondences from false ones. Modeling motion coherence on sparse putative correspondences is challenging due to their sparsity and uneven distributions. Existing works on motion coherence are sensitive to parameter settings and have difficulty in dealing with complex motion patterns. In this paper, we introduce a network called Laplacian Motion Coherence Network (LMCNet) to learn motion coherence property for correspondence pruning. We propose a novel formulation of fitting coherent motions with a smooth function on a graph of correspondences and show that this formulation allows a closed-form solution by graph Laplacian. This closed-form solution enables us to design a differentiable layer in a learning framework to capture global motion coherence from putative correspondences. The global motion coherence is further combined with local coherence extracted by another local layer to robustly detect inlier correspondences. Experiments demonstrate that LMCNet has superior performances to the state of the art in relative camera pose estimation and correspondences pruning of dynamic scenes.

</details>

### Manifold Regularized Dynamic Network Pruning.
- **链接**: [arXiv:2103.05861](https://arxiv.org/abs/2103.05861) · 📚 被引 87
- **作者**: Yehui Tang, Yunhe Wang, Yixing Xu, Yiping Deng, Chao Xu, Dacheng Tao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural network pruning is an essential approach for reducing the computational complexity of deep models so that they can be well deployed on resource-limited devices. Compared with conventional methods, the recently developed dynamic pruning methods determine redundant filters variant to each input instance which achieves higher acceleration. Most of the existing methods discover effective sub-networks for each instance independently and do not utilize the relationship between different inputs. To maximally excavate redundancy in the given network architecture, this paper proposes a new paradigm that dynamically removes redundant filters by embedding the manifold information of all instances into the space of pruned networks (dubbed as ManiDP). We first investigate the recognition complexity and feature similarity between images in the training set. Then, the manifold relationship between instances and the pruned sub-networks will be aligned in the training procedure. The effectiveness of the proposed method is verified on several benchmarks, which shows better performance in terms of both accuracy and computational cost compared to the state-of-the-art methods. For example, our method can reduce 55.3% FLOPs of ResNet-34 with only 0.57% top-1 accuracy degradation on ImageNet.

</details>

### Convolutional Neural Network Pruning With Structural Redundancy Reduction.
- **链接**: [arXiv:2104.03438](https://arxiv.org/abs/2104.03438) · 📚 被引 175
- **作者**: Zi Wang, Chengcheng Li, Xiangyang Wang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Convolutional neural network (CNN) pruning has become one of the most successful network compression approaches in recent years. Existing works on network pruning usually focus on removing the least important filters in the network to achieve compact architectures. In this study, we claim that identifying structural redundancy plays a more essential role than finding unimportant filters, theoretically and empirically. We first statistically model the network pruning problem in a redundancy reduction perspective and find that pruning in the layer(s) with the most structural redundancy outperforms pruning the least important filters across all layers. Based on this finding, we then propose a network pruning approach that identifies structural redundancy of a CNN and prunes filters in the selected layer(s) with the most redundancy. Experiments on various benchmark network architectures and datasets show that our proposed approach significantly outperforms the previous state-of-the-art.

</details>

### Joint-DetNAS: Upgrade Your Detector With NAS, Pruning and Dynamic Distillation.
- **链接**: [arXiv:2105.12971](https://arxiv.org/abs/2105.12971) · 📚 被引 25
- **作者**: Lewei Yao, Renjie Pi, Hang Xu, Wei Zhang, Zhenguo Li, Tong Zhang
- **🏷️ 机构**: Hong Kong University of Science and Technology, Huawei Noah&#x2019;s Ark Lab
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose Joint-DetNAS, a unified NAS framework for object detection, which integrates 3 key components: Neural Architecture Search, pruning, and Knowledge Distillation. Instead of naively pipelining these techniques, our Joint-DetNAS optimizes them jointly. The algorithm consists of two core processes: student morphism optimizes the student's architecture and removes the redundant parameters, while dynamic distillation aims to find the optimal matching teacher. For student morphism, weight inheritance strategy is adopted, allowing the student to flexibly update its architecture while fully utilize the predecessor's weights, which considerably accelerates the search; To facilitate dynamic distillation, an elastic teacher pool is trained via integrated progressive shrinking strategy, from which teacher detectors can be sampled without additional cost in subsequent searches. Given a base detector as the input, our algorithm directly outputs the derived student detector with high performance without additional training. Experiments demonstrate that our Joint-DetNAS outperforms the naive pipelining approach by a great margin. Given a classic R101-FPN as the base detector, Joint-DetNAS is able to boost its mAP from 41.4 to 43.9 on MS COCO and reduce the latency by 47%, which is on par with the SOTA EfficientDet while requiring less search cost. We hope our proposed method can provide the community with a new way of jointly optimizing NAS, KD and pruning.

</details>

### Multi-Decoding Deraining Network and Quasi-Sparsity Based Training.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Wang_Multi-Decoding_Deraining_Network_and_Quasi-Sparsity_Based_Training_CVPR_2021_paper.html) · 📚 被引 33
- **作者**: Yinglong Wang, Chao Ma, Bing Zeng
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Exploring Sparsity in Image Super-Resolution for Efficient Inference.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Wang_Exploring_Sparsity_in_Image_Super-Resolution_for_Efficient_Inference_CVPR_2021_paper.html) · 📚 被引 291
- **作者**: Longguang Wang, Xiaoyu Dong, Yingqian Wang, Xinyi Ying, Zaiping Lin, Wei An et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Effective Sparsification of Neural Networks With Global Sparsity Constraint.
- **链接**: [arXiv:2105.01571](https://arxiv.org/abs/2105.01571) · 📚 被引 32
- **作者**: Xiao Zhou, Weizhong Zhang, Hang Xu, Tong Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Weight pruning is an effective technique to reduce the model size and inference time for deep neural networks in real-world deployments. However, since magnitudes and relative importance of weights are very different for different layers of a neural network, existing methods rely on either manual tuning or handcrafted heuristic rules to find appropriate pruning rates individually for each layer. This approach generally leads to suboptimal performance. In this paper, by directly working on the probability space, we propose an effective network sparsification method called {\it probabilistic masking} (ProbMask), which solves a natural sparsification formulation under global sparsity constraint. The key idea is to use probability as a global criterion for all layers to measure the weight importance. An appealing feature of ProbMask is that the amounts of weight redundancy can be learned automatically via our constraint and thus we avoid the problem of tuning pruning rates individually for different layers in a network. Extensive experimental results on CIFAR-10/100 and ImageNet demonstrate that our method is highly effective, and can outperform previous state-of-the-art methods by a significant margin, especially in the high pruning rate situation. Notably, the gap of Top-1 accuracy between our ProbMask and existing methods can be up to 10\%. As a by-product, we show ProbMask is also highly effective in identifying supermasks, which are subnetworks with high performance in a randomly weighted dense neural network.

</details>

## 跨领域论文（完整笔记在其他领域）

- VoxelContext-Net: An Octree Based Framework for Point Cloud Compression. → [3d-detection](../3d-detection/Guideline%202021.md)

## 🆕 增量新增

### ResRep: Lossless CNN Pruning via Decoupling Remembering and Forgetting. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00447)
- **作者**: Xiaohan Ding, Tianxiang Hao, Jianchao Tan, Ji Liu, Jungong Han, Yuchen Guo et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021
- **摘要（中）**: ①针对CNN剪枝中常见的精度损失问题，尤其是结构化剪枝后难以恢复性能。②提出ResRep方法，通过解耦“记忆”和“遗忘”过程：先训练带额外可剪枝结构的网络，再通过梯度重参数化实现无损剪枝。③相比已有剪枝方法，ResRep在保持精度的同时大幅减少计算量，且无需微调。④在ImageNet和CIFAR上，ResRep在ResNet-50上剪枝50% FLOPs时精度无损，甚至略有提升。
- **摘要（英）**: This paper addresses accuracy degradation in CNN pruning by decoupling the remembering and forgetting phases. ResRep introduces auxiliary trainable structures and uses gradient reparameterization to achieve lossless pruning without fine-tuning. On ImageNet, it prunes ResNet-50 by 50% FLOPs with no accuracy loss, demonstrating state-of-the-art performance.
- **核心贡献**: 提出无损CNN剪枝的ResRep方法。
- **创新点**: 解耦记忆与遗忘的剪枝训练范式。
- **结果**: 在ImageNet上实现50% FLOPs剪枝且精度无损。

### GDP: Stabilized Neural Network Pruning via Gates with Differentiable Polarization. **⭐⭐⭐⭐** (相关度: 65%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00519)
- **作者**: Yi Guo, Huan Yuan, Jianchao Tan, Zhangyang Wang, Sen Yang, Ji Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021
- **摘要（中）**: ①针对基于门控的剪枝方法在训练中不稳定、难以收敛到理想稀疏结构的问题。②提出GDP方法，通过可微极化（Differentiable Polarization）正则化门控值，使其趋向0或1，从而稳定剪枝过程。③相比已有门控剪枝，GDP增强了稀疏性诱导的稳定性，并减少了精度损失。④摘要未提供具体数据，但声称在多个网络和数据集上优于现有剪枝方法。
- **摘要（英）**: This paper addresses instability in gate-based pruning by introducing differentiable polarization to push gate values toward binary states. GDP stabilizes training and improves sparsity induction. It reports superior performance over existing pruning methods across multiple architectures and datasets, though specific numbers are not in the abstract.
- **核心贡献**: 提出可微极化正则化稳定门控剪枝。
- **创新点**: 利用极化损失强制门控二值化。
- **结果**: 在多个基准上优于现有剪枝方法。

### Auto Graph Encoder-Decoder for Neural Network Pruning. **⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00630)
- **作者**: Sixing Yu, Arya Mazaheri, Ali Jannesari
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021
- **摘要（中）**: ①针对传统剪枝方法依赖人工设计规则、难以自适应不同网络结构的问题。②提出Auto Graph Encoder-Decoder（AGED）框架，利用图神经网络学习剪枝策略，自动生成每层的剪枝比例。③相比手工规则，AGED能根据网络拓扑和层间依赖动态决策，提升剪枝效果。④摘要未提供具体数据，但声称在多个基准上优于现有自动剪枝方法。
- **摘要（英）**: This paper addresses the limitation of hand-crafted pruning rules by proposing Auto Graph Encoder-Decoder (AGED), which uses graph neural networks to learn layer-wise pruning ratios. AGED adapts to network topology and inter-layer dependencies. It claims improved performance over existing automatic pruning methods on several benchmarks, though specific metrics are not in the abstract.
- **核心贡献**: 提出基于图神经网络的自动剪枝策略生成框架。
- **创新点**: 用图编码器-解码器建模层间依赖。
- **结果**: 在多个基准上优于现有自动剪枝方法。

### Progressive Correspondence Pruning by Consensus Learning. **⭐⭐⭐** (相关度: 40%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00640)
- **作者**: Chen Zhao, Yixiao Ge, Feng Zhu, Rui Zhao, Hongsheng Li, Mathieu Salzmann
- **🏷️ 机构**: CUHK
- **会议**: ICCV 2021
- **摘要（中）**: ①该论文针对特征匹配中大量离群对应点导致位姿估计精度下降的问题。②提出了一种基于共识学习的渐进式对应点剪枝方法，通过迭代优化匹配一致性来剔除离群点。③相比传统RANSAC或单一几何约束方法，该方法利用学习到的共识分数进行渐进式筛选，提高了鲁棒性。④在多个标准匹配数据集上取得了更低的匹配误差和更高的位姿估计精度。
- **摘要（英）**: This paper addresses the problem of outlier correspondences in feature matching that degrade pose estimation accuracy. It proposes a progressive correspondence pruning method based on consensus learning, which iteratively refines matching consistency to remove outliers. Compared to RANSAC or single geometric constraints, it leverages learned consensus scores for progressive filtering, improving robustness. Experiments on standard matching benchmarks show lower matching errors and higher pose estimation accuracy.
- **核心贡献**: 提出基于共识学习的渐进式对应点剪枝框架。
- **创新点**: 将共识学习与渐进式剪枝结合，实现无需显式几何模型的离群点剔除。
- **结果**: 在标准数据集上显著降低匹配误差并提升位姿估计精度。

### Self-Supervised Cryo-Electron Tomography Volumetric Image Restoration from Single Noisy Volume with Sparsity Constraint. **⭐⭐** (相关度: 20%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00402)
- **作者**: Zhidong Yang, Fa Zhang, Renmin Han
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021
- **摘要（中）**: ①该论文针对冷冻电镜断层扫描（Cryo-ET）体积图像信噪比低、噪声严重的问题。②提出了一种自监督方法，仅利用单张含噪体积图像，结合稀疏约束进行图像恢复。③相比传统监督去噪方法，该方法无需干净标签，适用于生物成像中难以获取真值的场景。④实验表明在模拟和真实数据上均能有效提升信噪比并保留结构细节。
- **摘要（英）**: This paper tackles the low signal-to-noise ratio in Cryo-Electron Tomography volumetric images. It proposes a self-supervised restoration method using a single noisy volume with sparsity constraints, eliminating the need for clean labels. Compared to supervised denoising, it is applicable where ground truth is unavailable. Experiments on simulated and real data show improved SNR and preserved structural details.
- **核心贡献**: 提出单张含噪体积的自监督恢复方法。
- **创新点**: 利用稀疏约束实现无标签的体数据去噪。
- **结果**: 在Cryo-ET数据上有效提升信噪比。

### Online Multi-Granularity Distillation for GAN Compression. **⭐⭐⭐** (相关度: 35%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00672)
- **作者**: Yuxi Ren, Jie Wu, Xuefeng Xiao, Jianchao Yang
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021
- **摘要（中）**: ①该论文针对GAN模型压缩中蒸馏效率低、多粒度信息利用不足的问题。②提出了一种在线多粒度蒸馏方法，在训练过程中同时传递不同层级的特征知识给压缩模型。③相比离线蒸馏或单粒度蒸馏，该方法无需预训练教师，且能更全面地保留生成质量。④在多个GAN压缩任务上取得了更低的FID和更高的生成质量。
- **摘要（英）**: This paper addresses low efficiency and insufficient multi-granularity information in GAN compression. It proposes an online multi-granularity distillation method that transfers features at multiple levels during training. Compared to offline or single-granularity distillation, it requires no pre-trained teacher and better preserves generation quality. Experiments show lower FID and higher quality on several GAN compression tasks.
- **核心贡献**: 提出在线多粒度蒸馏用于GAN压缩。
- **创新点**: 在线蒸馏框架结合多粒度特征传递。
- **结果**: 在GAN压缩任务中取得更优FID。

### Multi-Prize Lottery Ticket Hypothesis: Finding Accurate Binary Neural Networks by Pruning A Randomly Weighted Network. **⭐⭐⭐⭐** (相关度: 55%)
- **链接**: [arXiv:2103.09377](https://arxiv.org/abs/2103.09377)
- **作者**: James Diffenderfer, Bhavya Kailkhura
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021
- **摘要（中）**: ①该论文针对传统彩票假设需要迭代训练和剪枝、成本高的问题。②提出了多奖彩票假设，证明随机初始化的过参数化网络包含多个子网络，无需训练即可达到与训练后稠密网络相当的精度，且对二值化量化鲁棒。③相比标准彩票假设，该方法无需训练即可获得高精度子网络，并支持极端量化。④在CIFAR-10和ImageNet上验证了该方法的有效性，尤其对深层宽网络效果显著。
- **摘要（英）**: This paper addresses the high cost of iterative training and pruning in the lottery ticket hypothesis. It proposes the Multi-Prize Lottery Ticket Hypothesis, proving that over-parameterized random networks contain subnetworks that achieve comparable accuracy to trained dense networks without further training and are robust to binarization. Compared to standard lottery tickets, it eliminates training and supports extreme quantization. Experiments on CIFAR-10 and ImageNet validate its effectiveness, especially for deep and wide networks.
- **核心贡献**: 提出多奖彩票假设，实现无需训练的高精度二值子网络。
- **创新点**: 证明随机网络中同时存在精度、免训练和量化鲁棒三种奖。
- **结果**: 在CIFAR-10和ImageNet上验证了无需训练即可获得高精度二值网络。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, Frankle & Carbin (2019) demonstrated that randomly-initialized dense networks contain subnetworks that once found can be trained to reach test accuracy comparable to the trained dense network. However, finding these high performing trainable subnetworks is expensive, requiring iterative process of training and pruning weights. In this paper, we propose (and prove) a stronger Multi-Prize Lottery Ticket Hypothesis: A sufficiently over-parameterized neural network with random weights contains several subnetworks (winning tickets) that (a) have comparable accuracy to a dense target network with learned weights (prize 1), (b) do not require any further training to achieve prize 1 (prize 2), and (c) is robust to extreme forms of quantization (i.e., binary weights and/or activation) (prize 3). This provides a new paradigm for learning compact yet highly accurate binary neural networks simply by pruning and quantizing randomly weighted full precision neural networks. We also propose an algorithm for finding multi-prize tickets (MPTs) and test it by performing a series of experiments on CIFAR-10 and ImageNet datasets. Empirical results indicate that as models grow deeper and wider, multi-prize tickets start to reach similar (and sometimes even higher) test accuracy compared to their significantly larger and full-precision counterparts that have been weight-trained. Without ever updating the weight values, our MPTs-1/32 not only set new binary weight network state-of-the-art (SOTA) Top-1 accuracy -- 94.8% on CIFAR-10 and 74.03% on ImageNet -- but also outperform their full-precision counterparts by 1.78% and 0.76%, respectively. Further, our MPT-1/1 achieves SOTA Top-1 accuracy (91.9%) for binary neural networks on CIFAR-10. Code and pre-trained models are available at: https://github.com/chrundle/biprop.

</details>

### Pruning Neural Networks at Initialization: Why Are We Missing the Mark? **⭐⭐⭐** (相关度: 50%)
- **链接**: [arXiv:2009.08576](https://arxiv.org/abs/2009.08576)
- **作者**: Jonathan Frankle, Gintare Karolina Dziugaite, Daniel M. Roy, Michael Carbin
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021
- **摘要（中）**: ①该论文针对初始化时剪枝方法（如SNIP、GraSP、SynFlow）效果不佳的问题。②通过实验分析发现，这些方法剪枝后的权重随机打乱或重新初始化后精度不变，说明其逐权重决策可被逐层剪枝比例替代。③相比现有方法，该研究揭示了初始化剪枝启发式的局限性，并指出当前方法缺乏逐层特异性。④在多个数据集上验证了该现象，表明初始化剪枝的精度仍低于训练后剪枝。
- **摘要（英）**: This paper investigates why pruning at initialization methods like SNIP, GraSP, and SynFlow underperform. It shows that randomly shuffling pruned weights or reinitializing them preserves accuracy, implying per-weight decisions can be replaced by per-layer pruning ratios. Compared to existing methods, it reveals limitations in current heuristics and lack of layer-specificity. Experiments across datasets confirm that initialization pruning remains below post-training magnitude pruning.
- **核心贡献**: 揭示初始化剪枝方法中逐权重决策的可替代性。
- **创新点**: 通过随机打乱实验证明剪枝决策的层内冗余性。
- **结果**: 表明现有初始化剪枝方法精度低于训练后剪枝。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent work has explored the possibility of pruning neural networks at initialization. We assess proposals for doing so: SNIP (Lee et al., 2019), GraSP (Wang et al., 2020), SynFlow (Tanaka et al., 2020), and magnitude pruning. Although these methods surpass the trivial baseline of random pruning, they remain below the accuracy of magnitude pruning after training, and we endeavor to understand why. We show that, unlike pruning after training, randomly shuffling the weights these methods prune within each layer or sampling new initial values preserves or improves accuracy. As such, the per-weight pruning decisions made by these methods can be replaced by a per-layer choice of the fraction of weights to prune. This property suggests broader challenges with the underlying pruning heuristics, the desire to prune at initialization, or both.

</details>

### Robust Pruning at Initialization. **⭐⭐** (相关度: 30%)
- **链接**: [出版页](https://openreview.net/forum?id=vXj_ucZQ4hA)
- **作者**: Soufiane Hayou, Jean-Francois Ton, Arnaud Doucet, Yee Whye Teh
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021
- **摘要（中）**: ①该论文针对网络剪枝领域中的初始化时剪枝（Pruning at Initialization）问题，旨在减少训练成本并保持模型性能。②由于提供的摘要为空，无法具体描述其提出的方法或实验内容。③同样，无法评估其相比已有工作的改进点。④由于缺乏摘要信息，无法提供具体效果数据。
- **摘要（英）**: This paper addresses the problem of pruning at initialization in neural networks to reduce training cost. However, due to the absence of an abstract, the proposed method, improvements, and results cannot be summarized.
- **核心贡献**: 无法确定，因摘要缺失。
- **创新点**: 无法确定，因摘要缺失。
- **结果**: 无法确定，因摘要缺失。

### Network Pruning That Matters: A Case Study on Retraining Variants. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2105.03193](https://arxiv.org/abs/2105.03193)
- **作者**: Duong H. Le, Binh-Son Hua
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021
- **摘要（中）**: ①该论文针对网络剪枝后重训练方法中性能差异的原因不明问题，特别是学习率回退（learning rate rewinding）为何优于传统微调。②通过大量实验验证并分析学习率回退的有效性，发现其成功关键在于使用较大的学习率，并观察到其他包含大学习率的学习率调度（如1-cycle）也有类似现象。③相比已有工作，该论文揭示了学习率调度在剪枝重训练中的关键作用，并展示了随机剪枝网络在正确调度下可超越方法性剪枝网络的意外现象。④实验表明，利用合适的学习率调度，随机剪枝网络甚至能比传统微调的方法性剪枝网络表现更好，强调了学习率调度的重要性。
- **摘要（英）**: This paper investigates why learning rate rewinding outperforms traditional fine-tuning in retraining pruned networks, discovering that the key factor is the use of a large learning rate. Through extensive experiments, it shows that other schedules with large learning rates, like 1-cycle, exhibit similar benefits, and that randomly pruned networks can surpass methodically pruned ones when retrained with appropriate schedules. The findings highlight the crucial role of learning rate scheduling in pruned network retraining.
- **核心贡献**: 揭示了学习率调度在剪枝网络重训练中的核心作用，并解释了学习率回退的成功原因。
- **创新点**: 通过实验发现大学习率是学习率回退成功的关键，并展示了随机剪枝在正确调度下的优越性。
- **结果**: 证明了合适的学习率调度可使随机剪枝网络性能超越传统方法性剪枝网络。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Network pruning is an effective method to reduce the computational expense of over-parameterized neural networks for deployment on low-resource systems. Recent state-of-the-art techniques for retraining pruned networks such as weight rewinding and learning rate rewinding have been shown to outperform the traditional fine-tuning technique in recovering the lost accuracy (Renda et al., 2020), but so far it is unclear what accounts for such performance. In this work, we conduct extensive experiments to verify and analyze the uncanny effectiveness of learning rate rewinding. We find that the reason behind the success of learning rate rewinding is the usage of a large learning rate. Similar phenomenon can be observed in other learning rate schedules that involve large learning rates, e.g., the 1-cycle learning rate schedule (Smith et al., 2019). By leveraging the right learning rate schedule in retraining, we demonstrate a counter-intuitive phenomenon in that randomly pruned networks could even achieve better performance than methodically pruned networks (fine-tuned with the conventional approach). Our results emphasize the cruciality of the learning rate schedule in pruned network retraining - a detail often overlooked by practitioners during the implementation of network pruning. One-sentence Summary: We study the effective of different retraining mechanisms while doing pruning

</details>

### Layer-adaptive Sparsity for the Magnitude-based Pruning. **⭐⭐** (相关度: 30%)
- **链接**: [出版页](https://openreview.net/forum?id=H6ATjJ0TKdf)
- **作者**: Jaeho Lee, Sejun Park, Sangwoo Mo, Sungsoo Ahn, Jinwoo Shin
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021
- **摘要（中）**: ①该论文针对基于幅度的剪枝方法中，各层剪枝率固定导致性能次优的问题，提出层自适应稀疏性策略。②由于提供的摘要为空，无法具体描述其方法细节或实验内容。③同样，无法评估其相比已有工作的改进点。④由于缺乏摘要信息，无法提供具体效果数据。
- **摘要（英）**: This paper addresses the issue of fixed layer-wise sparsity in magnitude-based pruning, proposing a layer-adaptive sparsity approach. However, due to the absence of an abstract, the method, improvements, and results cannot be summarized.
- **核心贡献**: 无法确定，因摘要缺失。
- **创新点**: 无法确定，因摘要缺失。
- **结果**: 无法确定，因摘要缺失。

### A Gradient Flow Framework For Analyzing Network Pruning.
- **链接**: [arXiv:2009.11839](https://arxiv.org/abs/2009.11839)
- **作者**: Ekdeep Singh Lubana, Robert P. Dick
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent network pruning methods focus on pruning models early-on in training. To estimate the impact of removing a parameter, these methods use importance measures that were originally designed to prune trained models. Despite lacking justification for their use early-on in training, such measures result in surprisingly low accuracy loss. To better explain this behavior, we develop a general framework that uses gradient flow to unify state-of-the-art importance measures through the norm of model parameters. We use this framework to determine the relationship between pruning measures and evolution of model parameters, establishing several results related to pruning models early-on in training: (i) magnitude-based pruning removes parameters that contribute least to reduction in loss, resulting in models that converge faster than magnitude-agnostic methods; (ii) loss-preservation based pruning preserves first-order model evolution dynamics and is therefore appropriate for pruning minimally trained models; and (iii) gradient-norm based pruning affects second-order model evolution dynamics, such that increasing gradient norm via pruning can produce poorly performing models. We validate our claims on several VGG-13, MobileNet-V1, and ResNet-56 models trained on CIFAR-10/CIFAR-100. Code available at https://github.com/EkdeepSLubana/flowandprune.

</details>

### ChipNet: Budget-Aware Pruning with Heaviside Continuous Approximations.
- **链接**: [arXiv:2102.07156](https://arxiv.org/abs/2102.07156)
- **作者**: Rishabh Tiwari, Udbhav Bamba, Arnav Chavan, Deepak K. Gupta
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Structured pruning methods are among the effective strategies for extracting small resource-efficient convolutional neural networks from their dense counterparts with minimal loss in accuracy. However, most existing methods still suffer from one or more limitations, that include 1) the need for training the dense model from scratch with pruning-related parameters embedded in the architecture, 2) requiring model-specific hyperparameter settings, 3) inability to include budget-related constraint in the training process, and 4) instability under scenarios of extreme pruning. In this paper, we present ChipNet, a deterministic pruning strategy that employs continuous Heaviside function and a novel crispness loss to identify a highly sparse network out of an existing dense network. Our choice of continuous Heaviside function is inspired by the field of design optimization, where the material distribution task is posed as a continuous optimization problem, but only discrete values (0 or 1) are practically feasible and expected as final outcomes. Our approach's flexible design facilitates its use with different choices of budget constraints while maintaining stability for very low target budgets. Experimental results show that ChipNet outperforms state-of-the-art structured pruning methods by remarkable margins of up to 16.1% in terms of accuracy. Further, we show that the masks obtained with ChipNet are transferable across datasets. For certain cases, it was observed that masks transferred from a model trained on feature-rich teacher dataset provide better performance on the student dataset than those obtained by directly pruning on the student data itself.

</details>

### Neural Pruning via Growing Regularization.
- **链接**: [arXiv:2012.09243](https://arxiv.org/abs/2012.09243)
- **作者**: Huan Wang, Can Qin, Yulun Zhang, Yun Fu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Regularization has long been utilized to learn sparsity in deep neural network pruning. However, its role is mainly explored in the small penalty strength regime. In this work, we extend its application to a new scenario where the regularization grows large gradually to tackle two central problems of pruning: pruning schedule and weight importance scoring. (1) The former topic is newly brought up in this work, which we find critical to the pruning performance while receives little research attention. Specifically, we propose an L2 regularization variant with rising penalty factors and show it can bring significant accuracy gains compared with its one-shot counterpart, even when the same weights are removed. (2) The growing penalty scheme also brings us an approach to exploit the Hessian information for more accurate pruning without knowing their specific values, thus not bothered by the common Hessian approximation problems. Empirically, the proposed algorithms are easy to implement and scalable to large datasets and networks in both structured and unstructured pruning. Their effectiveness is demonstrated with modern deep neural networks on the CIFAR and ImageNet datasets, achieving competitive results compared to many state-of-the-art algorithms. Our code and trained models are publicly available at https://github.com/mingsuntse/regularization-pruning.

</details>

### Learning a Latent Simplex in Input Sparsity Time.
- **链接**: [出版页](https://openreview.net/forum?id=04LZCAxMSco)
- **作者**: Ainesh Bakshi, Chiranjib Bhattacharyya, Ravi Kannan, David P. Woodruff, Samson Zhou
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

### A Discriminative Gaussian Mixture Model with Sparsity.
- **链接**: [出版页](https://openreview.net/forum?id=-_Zp7r2-cGK)
- **作者**: Hideaki Hayashi, Seiichi Uchida
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

### Understanding the effects of data parallelism and sparsity on neural network training.
- **链接**: [出版页](https://openreview.net/forum?id=rsogjAnYs4z)
- **作者**: Namhoon Lee, Thalaiyasingam Ajanthan, Philip H. S. Torr, Martin Jaggi
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

### BSQ: Exploring Bit-Level Sparsity for Mixed-Precision Neural Network Quantization.
- **链接**: [arXiv:2102.10462](https://arxiv.org/abs/2102.10462)
- **作者**: Huanrui Yang, Lin Duan, Yiran Chen, Hai Li
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Mixed-precision quantization can potentially achieve the optimal tradeoff between performance and compression rate of deep neural networks, and thus, have been widely investigated. However, it lacks a systematic method to determine the exact quantization scheme. Previous methods either examine only a small manually-designed search space or utilize a cumbersome neural architecture search to explore the vast search space. These approaches cannot lead to an optimal quantization scheme efficiently. This work proposes bit-level sparsity quantization (BSQ) to tackle the mixed-precision quantization from a new angle of inducing bit-level sparsity. We consider each bit of quantized weights as an independent trainable variable and introduce a differentiable bit-sparsity regularizer. BSQ can induce all-zero bits across a group of weight elements and realize the dynamic precision reduction, leading to a mixed-precision quantization scheme of the original model. Our method enables the exploration of the full mixed-precision space with a single gradient-based optimization process, with only one hyperparameter to tradeoff the performance and compression. BSQ achieves both higher accuracy and higher bit reduction on various model architectures on the CIFAR-10 and ImageNet datasets comparing to previous methods.

</details>

### Chasing Sparsity in Vision Transformers: An End-to-End Exploration.
- **链接**: [arXiv:2106.04533](https://arxiv.org/abs/2106.04533)
- **作者**: Tianlong Chen, Yu Cheng, Zhe Gan, Lu Yuan, Lei Zhang, Zhangyang Wang
- **🏷️ 机构**: PolyU / OPPO
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision transformers (ViTs) have recently received explosive popularity, but their enormous model sizes and training costs remain daunting. Conventional post-training pruning often incurs higher training budgets. In contrast, this paper aims to trim down both the training memory overhead and the inference complexity, without sacrificing the achievable accuracy. We carry out the first-of-its-kind comprehensive exploration, on taking a unified approach of integrating sparsity in ViTs "from end to end". Specifically, instead of training full ViTs, we dynamically extract and train sparse subnetworks, while sticking to a fixed small parameter budget. Our approach jointly optimizes model parameters and explores connectivity throughout training, ending up with one sparse network as the final output. The approach is seamlessly extended from unstructured to structured sparsity, the latter by considering to guide the prune-and-grow of self-attention heads inside ViTs. We further co-explore data and architecture sparsity for additional efficiency gains by plugging in a novel learnable token selector to adaptively determine the currently most vital patches. Extensive results on ImageNet with diverse ViT backbones validate the effectiveness of our proposals which obtain significantly reduced computational cost and almost unimpaired generalization. Perhaps most surprisingly, we find that the proposed sparse (co-)training can sometimes improve the ViT accuracy rather than compromising it, making sparsity a tantalizing "free lunch". For example, our sparsified DeiT-Small at (5%, 50%) sparsity for (data, architecture), improves 0.28% top-1 accuracy, and meanwhile enjoys 49.32% FLOPs and 4.40% running time savings. Our codes are available at https://github.com/VITA-Group/SViTE.

</details>

### PARP: Prune, Adjust and Re-Prune for Self-Supervised Speech Recognition.
- **链接**: [arXiv:2106.05933](https://arxiv.org/abs/2106.05933)
- **作者**: Cheng-I Jeff Lai, Yang Zhang, Alexander H. Liu, Shiyu Chang, Yi-Lun Liao, Yung-Sung Chuang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised speech representation learning (speech SSL) has demonstrated the benefit of scale in learning rich representations for Automatic Speech Recognition (ASR) with limited paired data, such as wav2vec 2.0. We investigate the existence of sparse subnetworks in pre-trained speech SSL models that achieve even better low-resource ASR results. However, directly applying widely adopted pruning methods such as the Lottery Ticket Hypothesis (LTH) is suboptimal in the computational cost needed. Moreover, we show that the discovered subnetworks yield minimal performance gain compared to the original dense network. We present Prune-Adjust-Re-Prune (PARP), which discovers and finetunes subnetworks for much better performance, while only requiring a single downstream ASR finetuning run. PARP is inspired by our surprising observation that subnetworks pruned for pre-training tasks need merely a slight adjustment to achieve a sizeable performance boost in downstream ASR tasks. Extensive experiments on low-resource ASR verify (1) sparse subnetworks exist in mono-lingual/multi-lingual pre-trained speech SSL, and (2) the computational advantage and performance gain of PARP over baseline pruning methods. In particular, on the 10min Librispeech split without LM decoding, PARP discovers subnetworks from wav2vec 2.0 with an absolute 10.9%/12.6% WER decrease compared to the full model. We further demonstrate the effectiveness of PARP via: cross-lingual pruning without any phone recognition degradation, the discovery of a multi-lingual subnetwork for 10 spoken languages in 1 finetuning run, and its applicability to pre-trained BERT/XLNet for natural language tasks.

</details>

## 跨领域论文（完整笔记在其他领域）

- General Instance Distillation for Object Detection. → [object-detection](../object-detection/Guideline%202021.md)
- VoxelContext-Net: An Octree Based Framework for Point Cloud Compression. → [3d-detection](../3d-detection/Guideline%202021.md)
- DER: Dynamically Expandable Representation for Class Incremental Learning. → [continual-learning](../continual-learning/Guideline%202021.md)
- Joint-DetNAS: Upgrade Your Detector With NAS, Pruning and Dynamic Distillation. → [neural-architecture-search](../neural-architecture-search/Guideline%202021.md)
- Neural Architecture Search on ImageNet in Four GPU Hours: A Theoretically Inspired Perspective. → [neural-architecture-search](../neural-architecture-search/Guideline%202021.md)
- 3D Siamese Voxel-to-BEV Tracker for Sparse Point Clouds. → [bev](../bev/Guideline%202021.md)
<!-- COMPLETE v1 papers=30 -->
