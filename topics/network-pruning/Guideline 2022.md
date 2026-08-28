# Network Pruning — 2022 Guideline

> 领域: 网络剪枝 / 模型压缩（结构化剪枝、稀疏化）
> 论文数: 13 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Sparse DETR: Efficient End-to-End Object Detection with Learnable Sparsity.
- **链接**: [arXiv:2111.14330](https://arxiv.org/abs/2111.14330) · [代码](https://github.com/kakaobrain/sparse-detr) · 📚 被引 0
- **作者**: Byungseok Roh, Jaewoong Shin, Wuhyun Shin, Saehoon Kim
- **🏷️ 机构**: Yanan University, Chongqing University of Science and Technology
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> DETR is the first end-to-end object detector using a transformer encoder-decoder architecture and demonstrates competitive performance but low computational efficiency on high resolution feature maps. The subsequent work, Deformable DETR, enhances the efficiency of DETR by replacing dense attention with deformable attention, which achieves 10x faster convergence and improved performance. Deformable DETR uses the multiscale feature to ameliorate performance, however, the number of encoder tokens increases by 20x compared to DETR, and the computation cost of the encoder attention remains a bottleneck. In our preliminary experiment, we observe that the detection performance hardly deteriorates even if only a part of the encoder token is updated. Inspired by this observation, we propose Sparse DETR that selectively updates only the tokens expected to be referenced by the decoder, thus help the model effectively detect objects. In addition, we show that applying an auxiliary detection loss on the selected tokens in the encoder improves the performance while minimizing computational overhead. We validate that Sparse DETR achieves better performance than Deformable DETR even with only 10% encoder tokens on the COCO dataset. Albeit only the encoder tokens are sparsified, the total computation cost decreases by 38% and the frames per second (FPS) increases by 42% compared to Deformable DETR. Code is available at https://github.com/kakaobrain/sparse-detr

</details>

### Prospect Pruning: Finding Trainable Weights at Initialization using Meta-Gradients.
- **链接**: [arXiv:2202.08132](https://arxiv.org/abs/2202.08132)
- **作者**: Milad Alizadeh, Shyam A. Tailor, Luisa M. Zintgraf, Joost van Amersfoort, Sebastian Farquhar, Nicholas Donald Lane et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pruning neural networks at initialization would enable us to find sparse models that retain the accuracy of the original network while consuming fewer computational resources for training and inference. However, current methods are insufficient to enable this optimization and lead to a large degradation in model performance. In this paper, we identify a fundamental limitation in the formulation of current methods, namely that their saliency criteria look at a single step at the start of training without taking into account the trainability of the network. While pruning iteratively and gradually has been shown to improve pruning performance, explicit consideration of the training stage that will immediately follow pruning has so far been absent from the computation of the saliency criterion. To overcome the short-sightedness of existing methods, we propose Prospect Pruning (ProsPr), which uses meta-gradients through the first few steps of optimization to determine which weights to prune. ProsPr combines an estimate of the higher-order effects of pruning on the loss and the optimization trajectory to identify the trainable sub-network. Our method achieves state-of-the-art pruning performance on a variety of vision classification tasks, with less data and in a single shot compared to existing pruning-at-initialization methods.

</details>

### The Unreasonable Effectiveness of Random Pruning: Return of the Most Naive Baseline for Sparse Training.
- **链接**: [arXiv:2202.02643](https://arxiv.org/abs/2202.02643) · [代码](https://github.com/VITA-Group/Random_Pruning)
- **作者**: Shiwei Liu, Tianlong Chen, Xiaohan Chen, Li Shen, Decebal Constantin Mocanu, Zhangyang Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Random pruning is arguably the most naive way to attain sparsity in neural networks, but has been deemed uncompetitive by either post-training pruning or sparse training. In this paper, we focus on sparse training and highlight a perhaps counter-intuitive finding, that random pruning at initialization can be quite powerful for the sparse training of modern neural networks. Without any delicate pruning criteria or carefully pursued sparsity structures, we empirically demonstrate that sparsely training a randomly pruned network from scratch can match the performance of its dense equivalent. There are two key factors that contribute to this revival: (i) the network sizes matter: as the original dense networks grow wider and deeper, the performance of training a randomly pruned sparse network will quickly grow to matching that of its dense equivalent, even at high sparsity ratios; (ii) appropriate layer-wise sparsity ratios can be pre-chosen for sparse training, which shows to be another important performance booster. Simple as it looks, a randomly pruned subnetwork of Wide ResNet-50 can be sparsely trained to outperforming a dense Wide ResNet-50, on ImageNet. We also observed such randomly pruned networks outperform dense counterparts in other favorable aspects, such as out-of-distribution detection, uncertainty estimation, and adversarial robustness. Overall, our results strongly suggest there is larger-than-expected room for sparse training at scale, and the benefits of sparsity might be more universal beyond carefully designed pruning. Our source code can be found at https://github.com/VITA-Group/Random_Pruning.

</details>

### Learning Pruning-Friendly Networks via Frank-Wolfe: One-Shot, Any-Sparsity, And No Retraining.
- **链接**: [出版页](https://openreview.net/forum?id=O1DEtITim__)
- **作者**: Lu Miao, Xiaolong Luo, Tianlong Chen, Wuyang Chen, Dong Liu, Zhangyang Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

### SOSP: Efficiently Capturing Global Correlations by Second-Order Structured Pruning.
- **链接**: [arXiv:2110.11395](https://arxiv.org/abs/2110.11395)
- **作者**: Manuel Nonnenmacher, Thomas Pfeil, Ingo Steinwart, David Reeb
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pruning neural networks reduces inference time and memory costs. On standard hardware, these benefits will be especially prominent if coarse-grained structures, like feature maps, are pruned. We devise two novel saliency-based methods for second-order structured pruning (SOSP) which include correlations among all structures and layers. Our main method SOSP-H employs an innovative second-order approximation, which enables saliency evaluations by fast Hessian-vector products. SOSP-H thereby scales like a first-order method despite taking into account the full Hessian. We validate SOSP-H by comparing it to our second method SOSP-I that uses a well-established Hessian approximation, and to numerous state-of-the-art methods. While SOSP-H performs on par or better in terms of accuracy, it has clear advantages in terms of scalability and efficiency. This allowed us to scale SOSP-H to large-scale vision tasks, even though it captures correlations across all layers of the network. To underscore the global nature of our pruning methods, we evaluate their performance not only by removing structures from a pretrained network, but also by detecting architectural bottlenecks. We show that our algorithms allow to systematically reveal architectural bottlenecks, which we then remove to further increase the accuracy of the networks.

</details>

### An Operator Theoretic View On Pruning Deep Neural Networks.
- **链接**: [出版页](https://openreview.net/forum?id=pWBNOgdeURp)
- **作者**: William T. Redman, Maria Fonoberova, Ryan Mohr, Yannis G. Kevrekidis, Igor Mezic
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

### Learning Efficient Image Super-Resolution Networks via Structure-Regularized Pruning.
- **链接**: [出版页](https://openreview.net/forum?id=AjGC97Aofee)
- **作者**: Yulun Zhang, Huan Wang, Can Qin, Yun Fu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

### Revisit Kernel Pruning with Lottery Regulated Grouped Convolutions.
- **链接**: [出版页](https://openreview.net/forum?id=LdEhiMG9WLO)
- **作者**: Shaochen (Henry) Zhong, Guanqun Zhang, Ningjia Huang, Shuai Xu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

### Sparsity Winning Twice: Better Robust Generalization from More Efficient Training.
- **链接**: [arXiv:2202.09844](https://arxiv.org/abs/2202.09844) · [代码](https://github.com/VITA-Group/Sparsity-Win-Robust-Generalization)
- **作者**: Tianlong Chen, Zhenyu Zhang, Pengjun Wang, Santosh Balachandra, Haoyu Ma, Zehao Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent studies demonstrate that deep networks, even robustified by the state-of-the-art adversarial training (AT), still suffer from large robust generalization gaps, in addition to the much more expensive training costs than standard training. In this paper, we investigate this intriguing problem from a new perspective, i.e., injecting appropriate forms of sparsity during adversarial training. We introduce two alternatives for sparse adversarial training: (i) static sparsity, by leveraging recent results from the lottery ticket hypothesis to identify critical sparse subnetworks arising from the early training; (ii) dynamic sparsity, by allowing the sparse subnetwork to adaptively adjust its connectivity pattern (while sticking to the same sparsity ratio) throughout training. We find both static and dynamic sparse methods to yield win-win: substantially shrinking the robust generalization gap and alleviating the robust overfitting, meanwhile significantly saving training and inference FLOPs. Extensive experiments validate our proposals with multiple network architectures on diverse datasets, including CIFAR-10/100 and Tiny-ImageNet. For example, our methods reduce robust generalization gap and overfitting by 34.44% and 4.02%, with comparable robust/standard accuracy boosts and 87.83%/87.82% training/inference FLOPs savings on CIFAR-100 with ResNet-18. Besides, our approaches can be organically combined with existing regularizers, establishing new state-of-the-art results in AT. Codes are available in https://github.com/VITA-Group/Sparsity-Win-Robust-Generalization.

</details>

### Deep Ensembling with No Overhead for either Training or Testing: The All-Round Blessings of Dynamic Sparsity.
- **链接**: [出版页](https://openreview.net/forum?id=RLtqs6pzj1-)
- **作者**: Shiwei Liu, Tianlong Chen, Zahra Atashgahi, Xiaohan Chen, Ghada Sokar, Elena Mocanu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

### Encoding Weights of Irregular Sparsity for Fixed-to-Fixed Model Compression.
- **链接**: [出版页](https://openreview.net/forum?id=Vs5NK44aP9P)
- **作者**: Baeseong Park, Se Jung Kwon, Daehwan Oh, Byeongwook Kim, Dongsoo Lee
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

### ZeroFL: Efficient On-Device Training for Federated Learning with Local Sparsity.
- **链接**: [arXiv:2208.02507](https://arxiv.org/abs/2208.02507)
- **作者**: Xinchi Qiu, Javier Fernández-Marqués, Pedro P. B. de Gusmao, Yan Gao, Titouan Parcollet, Nicholas Donald Lane
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> When the available hardware cannot meet the memory and compute requirements to efficiently train high performing machine learning models, a compromise in either the training quality or the model complexity is needed. In Federated Learning (FL), nodes are orders of magnitude more constrained than traditional server-grade hardware and are often battery powered, severely limiting the sophistication of models that can be trained under this paradigm. While most research has focused on designing better aggregation strategies to improve convergence rates and in alleviating the communication costs of FL, fewer efforts have been devoted to accelerating on-device training. Such stage, which repeats hundreds of times (i.e. every round) and can involve thousands of devices, accounts for the majority of the time required to train federated models and, the totality of the energy consumption at the client side. In this work, we present the first study on the unique aspects that arise when introducing sparsity at training time in FL workloads. We then propose ZeroFL, a framework that relies on highly sparse operations to accelerate on-device training. Models trained with ZeroFL and 95% sparsity achieve up to 2.3% higher accuracy compared to competitive baselines obtained from adapting a state-of-the-art sparse training framework to the FL setting.

</details>

## 跨领域论文（完整笔记在其他领域）

- Memory Replay with Data Compression for Continual Learning. → [continual-learning](../continual-learning/Guideline%202022.md)
