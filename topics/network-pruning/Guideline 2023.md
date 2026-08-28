# Network Pruning — 2023 Guideline

> 领域: 网络剪枝 / 模型压缩（结构化剪枝、稀疏化）
> 论文数: 22 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Learning to Jointly Share and Prune Weights for Grounding Based Vision and Language Models.
- **链接**: [出版页](https://openreview.net/forum?id=UMERaIHMwB3)
- **作者**: Shangqian Gao, Burak Uzkent, Yilin Shen, Heng Huang, Hongxia Jin
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### MIMT: Masked Image Modeling Transformer for Video Compression.
- **链接**: [出版页](https://openreview.net/forum?id=j9m-mVnndbm)
- **作者**: Jinxi Xiang, Kuan Tian, Jun Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Dataset Pruning: Reducing Training Data by Examining Generalization Influence.
- **链接**: [arXiv:2205.09329](https://arxiv.org/abs/2205.09329) · 📚 被引 0
- **作者**: Shuo Yang, Zeke Xie, Hanyu Peng, Min Xu, Mingming Sun, Ping Li
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### A Unified Framework for Soft Threshold Pruning.
- **链接**: [arXiv:2302.13019](https://arxiv.org/abs/2302.13019)
- **作者**: Yanqi Chen, Zhengyu Ma, Wei Fang, Xiawu Zheng, Zhaofei Yu, Yonghong Tian
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Pruning Deep Neural Networks from a Sparsity Perspective.
- **链接**: [arXiv:2302.05601](https://arxiv.org/abs/2302.05601)
- **作者**: Enmao Diao, Ganghua Wang, Jiawei Zhang, Yuhong Yang, Jie Ding, Vahid Tarokh
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In recent years, deep network pruning has attracted significant attention in order to enable the rapid deployment of AI into small devices with computation and memory constraints. Pruning is often achieved by dropping redundant weights, neurons, or layers of a deep network while attempting to retain a comparable test performance. Many deep pruning algorithms have been proposed with impressive empirical success. However, existing approaches lack a quantifiable measure to estimate the compressibility of a sub-network during each pruning iteration and thus may under-prune or over-prune the model. In this work, we propose PQ Index (PQI) to measure the potential compressibility of deep neural networks and use this to develop a Sparsity-informed Adaptive Pruning (SAP) algorithm. Our extensive experiments corroborate the hypothesis that for a generic pruning procedure, PQI decreases first when a large model is being effectively regularized and then increases when its compressibility reaches a limit that appears to correspond to the beginning of underfitting. Subsequently, PQI decreases again when the model collapse and significant deterioration in the performance of the model start to occur. Additionally, our experiments demonstrate that the proposed adaptive pruning algorithm with proper choice of hyper-parameters is superior to the iterative pruning algorithms such as the lottery ticket-based pruning methods, in terms of both compression efficiency and robustness.

</details>

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
- **链接**: [arXiv:2304.02840](https://arxiv.org/abs/2304.02840)
- **作者**: Yite Wang, Dawei Li, Ruoyu Sun
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pruning neural networks before training has received increasing interest due to its potential to reduce training time and memory. One popular method is to prune the connections based on a certain metric, but it is not entirely clear what metric is the best choice. Recent advances in neural tangent kernel (NTK) theory suggest that the training dynamics of large enough neural networks is closely related to the spectrum of the NTK. Motivated by this finding, we propose to prune the connections that have the least influence on the spectrum of the NTK. This method can help maintain the NTK spectrum, which may help align the training dynamics to that of its dense counterpart. However, one possible issue is that the fixed-weight-NTK corresponding to a given initial point can be very different from the NTK corresponding to later iterates during the training phase. We further propose to sample multiple realizations of random weights to estimate the NTK spectrum. Note that our approach is weight-agnostic, which is different from most existing methods that are weight-dependent. In addition, we use random inputs to compute the fixed-weight-NTK, making our method data-agnostic as well. We name our foresight pruning algorithm Neural Tangent Kernel Spectrum-Aware Pruning (NTK-SAP). Empirically, our method achieves better performance than all baselines on multiple datasets.

</details>

### Symmetric Pruning in Quantum Neural Networks.
- **链接**: [arXiv:2208.14057](https://arxiv.org/abs/2208.14057)
- **作者**: Xinbiao Wang, Junyu Liu, Tongliang Liu, Yong Luo, Yuxuan Du, Dacheng Tao
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Many fundamental properties of a quantum system are captured by its Hamiltonian and ground state. Despite the significance of ground states preparation (GSP), this task is classically intractable for large-scale Hamiltonians. Quantum neural networks (QNNs), which exert the power of modern quantum machines, have emerged as a leading protocol to conquer this issue. As such, how to enhance the performance of QNNs becomes a crucial topic in GSP. Empirical evidence showed that QNNs with handcraft symmetric ansatzes generally experience better trainability than those with asymmetric ansatzes, while theoretical explanations have not been explored. To fill this knowledge gap, here we propose the effective quantum neural tangent kernel (EQNTK) and connect this concept with over-parameterization theory to quantify the convergence of QNNs towards the global optima. We uncover that the advance of symmetric ansatzes attributes to their large EQNTK value with low effective dimension, which requests few parameters and quantum circuit depth to reach the over-parameterization regime permitting a benign loss landscape and fast convergence. Guided by EQNTK, we further devise a symmetric pruning (SP) scheme to automatically tailor a symmetric ansatz from an over-parameterized and asymmetric one to greatly improve the performance of QNNs when the explicit symmetry information of Hamiltonian is unavailable. Extensive numerical simulations are conducted to validate the analytical results of EQNTK and the effectiveness of SP.

</details>

### Holistic Adversarially Robust Pruning.
- **链接**: [arXiv:2412.14714](https://arxiv.org/abs/2412.14714)
- **作者**: Qi Zhao, Christian Wressnegger
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural networks can be drastically shrunk in size by removing redundant parameters. While crucial for the deployment on resource-constraint hardware, oftentimes, compression comes with a severe drop in accuracy and lack of adversarial robustness. Despite recent advances, counteracting both aspects has only succeeded for moderate compression rates so far. We propose a novel method, HARP, that copes with aggressive pruning significantly better than prior work. For this, we consider the network holistically. We learn a global compression strategy that optimizes how many parameters (compression rate) and which parameters (scoring connections) to prune specific to each layer individually. Our method fine-tunes an existing model with dynamic regularization, that follows a step-wise incremental function balancing the different objectives. It starts by favoring robustness before shifting focus on reaching the target compression rate and only then handles the objectives equally. The learned compression strategies allow us to maintain the pre-trained model natural accuracy and its adversarial robustness for a reduction by 99% of the network original size. Moreover, we observe a crucial influence of non-uniform compression across layers.

</details>

### Coverage-centric Coreset Selection for High Pruning Rates.
- **链接**: [arXiv:2210.15809](https://arxiv.org/abs/2210.15809) · [代码](https://github.com/haizhongzheng/Coverage-centric-coreset-selection)
- **作者**: Haizhong Zheng, Rui Liu, Fan Lai, Atul Prakash
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> One-shot coreset selection aims to select a representative subset of the training data, given a pruning rate, that can later be used to train future models while retaining high accuracy. State-of-the-art coreset selection methods pick the highest importance examples based on an importance metric and are found to perform well at low pruning rates. However, at high pruning rates, they suffer from a catastrophic accuracy drop, performing worse than even random sampling. This paper explores the reasons behind this accuracy drop both theoretically and empirically. We first propose a novel metric to measure the coverage of a dataset on a specific distribution by extending the classical geometric set cover problem to a distribution cover problem. This metric helps explain why coresets selected by SOTA methods at high pruning rates perform poorly compared to random sampling because of worse data coverage. We then propose a novel one-shot coreset selection method, Coverage-centric Coreset Selection (CCS), that jointly considers overall data coverage upon a distribution as well as the importance of each example. We evaluate CCS on five datasets and show that, at high pruning rates (e.g., 90%), it achieves significantly better accuracy than previous SOTA methods (e.g., at least 19.56% higher on CIFAR10) as well as random selection (e.g., 7.04% higher on CIFAR10) and comparable accuracy at low pruning rates. We make our code publicly available at https://github.com/haizhongzheng/Coverage-centric-coreset-selection.

</details>

### Minimum Variance Unbiased N: M Sparsity for the Neural Gradients.
- **链接**: [出版页](https://openreview.net/forum?id=vuD2xEtxZcj)
- **作者**: Brian Chmiel, Itay Hubara, Ron Banner, Daniel Soudry
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Rethinking Graph Lottery Tickets: Graph Sparsity Matters.
- **链接**: [arXiv:2305.02190](https://arxiv.org/abs/2305.02190)
- **作者**: Bo Hui, Da Yan, Xiaolong Ma, Wei-Shinn Ku
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Lottery Ticket Hypothesis (LTH) claims the existence of a winning ticket (i.e., a properly pruned sub-network together with original weight initialization) that can achieve competitive performance to the original dense network. A recent work, called UGS, extended LTH to prune graph neural networks (GNNs) for effectively accelerating GNN inference. UGS simultaneously prunes the graph adjacency matrix and the model weights using the same masking mechanism, but since the roles of the graph adjacency matrix and the weight matrices are very different, we find that their sparsifications lead to different performance characteristics. Specifically, we find that the performance of a sparsified GNN degrades significantly when the graph sparsity goes beyond a certain extent. Therefore, we propose two techniques to improve GNN performance when the graph sparsity is high. First, UGS prunes the adjacency matrix using a loss formulation which, however, does not properly involve all elements of the adjacency matrix; in contrast, we add a new auxiliary loss head to better guide the edge pruning by involving the entire adjacency matrix. Second, by regarding unfavorable graph sparsification as adversarial data perturbations, we formulate the pruning process as a min-max optimization problem to gain the robustness of lottery tickets when the graph sparsity is high. We further investigate the question: Can the "retrainable" winning ticket of a GNN be also effective for graph transferring learning? We call it the transferable graph lottery ticket (GLT) hypothesis. Extensive experiments were conducted which demonstrate the superiority of our proposed sparsification method over UGS, and which empirically verified our transferable GLT hypothesis.

</details>

### Implicit Regularization for Group Sparsity.
- **链接**: [arXiv:2301.12540](https://arxiv.org/abs/2301.12540)
- **作者**: Jiangyuan Li, Thanh Van Nguyen, Chinmay Hegde, Raymond K. W. Wong
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We study the implicit regularization of gradient descent towards structured sparsity via a novel neural reparameterization, which we call a diagonally grouped linear neural network. We show the following intriguing property of our reparameterization: gradient descent over the squared regression loss, without any explicit regularization, biases towards solutions with a group sparsity structure. In contrast to many existing works in understanding implicit regularization, we prove that our training trajectory cannot be simulated by mirror descent. We analyze the gradient dynamics of the corresponding regression problem in the general noise setting and obtain minimax-optimal error rates. Compared to existing bounds for implicit sparse regularization using diagonal linear networks, our analysis with the new reparameterization shows improved sample complexity. In the degenerate case of size-one groups, our approach gives rise to a new algorithm for sparse linear regression. Finally, we demonstrate the efficacy of our approach with several numerical experiments.

</details>

### The Lazy Neuron Phenomenon: On Emergence of Activation Sparsity in Transformers.
- **链接**: [出版页](https://openreview.net/forum?id=TJ2nxciYCk-)
- **作者**: Zonglin Li, Chong You, Srinadh Bhojanapalli, Daliang Li, Ankit Singh Rawat, Sashank J. Reddi et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### More ConvNets in the 2020s: Scaling up Kernels Beyond 51x51 using Sparsity.
- **链接**: [arXiv:2207.03620](https://arxiv.org/abs/2207.03620)
- **作者**: Shiwei Liu, Tianlong Chen, Xiaohan Chen, Xuxi Chen, Qiao Xiao, Boqian Wu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Transformers have quickly shined in the computer vision world since the emergence of Vision Transformers (ViTs). The dominant role of convolutional neural networks (CNNs) seems to be challenged by increasingly effective transformer-based models. Very recently, a couple of advanced convolutional models strike back with large kernels motivated by the local-window attention mechanism, showing appealing performance and efficiency. While one of them, i.e. RepLKNet, impressively manages to scale the kernel size to 31x31 with improved performance, the performance starts to saturate as the kernel size continues growing, compared to the scaling trend of advanced ViTs such as Swin Transformer. In this paper, we explore the possibility of training extreme convolutions larger than 31x31 and test whether the performance gap can be eliminated by strategically enlarging convolutions. This study ends up with a recipe for applying extremely large kernels from the perspective of sparsity, which can smoothly scale up kernels to 61x61 with better performance. Built on this recipe, we propose Sparse Large Kernel Network (SLaK), a pure CNN architecture equipped with sparse factorized 51x51 kernels that can perform on par with or better than state-of-the-art hierarchical Transformers and modern ConvNet architectures like ConvNeXt and RepLKNet, on ImageNet classification as well as a wide range of downstream tasks including semantic segmentation on ADE20K, object detection on PASCAL VOC 2007, and object detection/segmentation on MS COCO.

</details>

### Sparsity May Cry: Let Us Fail (Current) Sparse Neural Networks Together!
- **链接**: [arXiv:2303.02141](https://arxiv.org/abs/2303.02141)
- **作者**: Shiwei Liu, Tianlong Chen, Zhenyu Zhang, Xuxi Chen, Tianjin Huang, Ajay Kumar Jaiswal et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Sparse Neural Networks (SNNs) have received voluminous attention predominantly due to growing computational and memory footprints of consistently exploding parameter count in large-scale models. Similar to their dense counterparts, recent SNNs generalize just as well and are equipped with numerous favorable benefits (e.g., low complexity, high scalability, and robustness), sometimes even better than the original dense networks. As research effort is focused on developing increasingly sophisticated sparse algorithms, it is startling that a comprehensive benchmark to evaluate the effectiveness of these algorithms has been highly overlooked. In absence of a carefully crafted evaluation benchmark, most if not all, sparse algorithms are evaluated against fairly simple and naive tasks (eg. CIFAR, ImageNet, GLUE, etc.), which can potentially camouflage many advantages as well unexpected predicaments of SNNs. In pursuit of a more general evaluation and unveiling the true potential of sparse algorithms, we introduce "Sparsity May Cry" Benchmark (SMC-Bench), a collection of carefully-curated 4 diverse tasks with 10 datasets, that accounts for capturing a wide range of domain-specific and sophisticated knowledge. Our systemic evaluation of the most representative sparse algorithms reveals an important obscured observation: the state-of-the-art magnitude- and/or gradient-based sparse algorithms seemingly fail to perform on SMC-Bench when applied out-of-the-box, sometimes at significantly trivial sparsity as low as 5%. By incorporating these well-thought and diverse tasks, SMC-Bench is designed to favor and encourage the development of more scalable and generalizable sparse algorithms.

</details>

### Sparsity-Constrained Optimal Transport.
- **链接**: [arXiv:2209.15466](https://arxiv.org/abs/2209.15466)
- **作者**: Tianlin Liu, Joan Puigcerver, Mathieu Blondel
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Regularized optimal transport (OT) is now increasingly used as a loss or as a matching layer in neural networks. Entropy-regularized OT can be computed using the Sinkhorn algorithm but it leads to fully-dense transportation plans, meaning that all sources are (fractionally) matched with all targets. To address this issue, several works have investigated quadratic regularization instead. This regularization preserves sparsity and leads to unconstrained and smooth (semi) dual objectives, that can be solved with off-the-shelf gradient methods. Unfortunately, quadratic regularization does not give direct control over the cardinality (number of nonzeros) of the transportation plan. We propose in this paper a new approach for OT with explicit cardinality constraints on the transportation plan. Our work is motivated by an application to sparse mixture of experts, where OT can be used to match input tokens such as image patches with expert models such as neural networks. Cardinality constraints ensure that at most $k$ tokens are matched with an expert, which is crucial for computational performance reasons. Despite the nonconvexity of cardinality constraints, we show that the corresponding (semi) dual problems are tractable and can be solved with first-order gradient methods. Our method can be thought as a middle ground between unregularized OT (recovered in the limit case $k=1$) and quadratically-regularized OT (recovered when $k$ is large enough). The smoothness of the objectives increases as $k$ increases, giving rise to a trade-off between convergence speed and sparsity of the optimal plan.

</details>

### Efficient recurrent architectures through activity sparsity and sparse back-propagation through time.
- **链接**: [出版页](https://openreview.net/forum?id=lJdOlWg8td)
- **作者**: Anand Subramoney, Khaleelulla Khan Nazeer, Mark Schöne, Christian Mayr, David Kappel
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023
