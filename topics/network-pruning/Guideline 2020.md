# Network Pruning — 2020 Guideline

> 领域: 网络剪枝 / 模型压缩（结构化剪枝、稀疏化）
> 论文数: 8 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Efficient Robustness Certificates for Discrete Data: Sparsity-Aware Randomized Smoothing for Graphs, Images and More.
- **链接**: [arXiv:2008.12952](https://arxiv.org/abs/2008.12952)
- **作者**: Aleksandar Bojchevski, Johannes Klicpera, Stephan Günnemann
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing techniques for certifying the robustness of models for discrete data either work only for a small class of models or are general at the expense of efficiency or tightness. Moreover, they do not account for sparsity in the input which, as our findings show, is often essential for obtaining non-trivial guarantees. We propose a model-agnostic certificate based on the randomized smoothing framework which subsumes earlier work and is tight, efficient, and sparsity-aware. Its computational complexity does not depend on the number of discrete categories or the dimension of the input (e.g. the graph size), making it highly scalable. We show the effectiveness of our approach on a wide variety of models, datasets, and tasks -- specifically highlighting its use for Graph Neural Networks. So far, obtaining provable guarantees for GNNs has been difficult due to the discrete and non-i.i.d. nature of graph data. Our method can certify any GNN and handles perturbations to both the graph structure and the node attributes.

</details>

### Schatten Norms in Matrix Streams: Hello Sparsity, Goodbye Dimension.
- **链接**: [arXiv:1907.05457](https://arxiv.org/abs/1907.05457)
- **作者**: Vladimir Braverman, Robert Krauthgamer, Aditya Krishnan, Roi Sinoff
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Spectral functions of large matrices contains important structural information about the underlying data, and is thus becoming increasingly important. Many times, large matrices representing real-world data are \emph{sparse} or \emph{doubly sparse} (i.e., sparse in both rows and columns), and are accessed as a \emph{stream} of updates, typically organized in \emph{row-order}. In this setting, where space (memory) is the limiting resource, all known algorithms require space that is polynomial in the dimension of the matrix, even for sparse matrices. We address this challenge by providing the first algorithms whose space requirement is \emph{independent of the matrix dimension}, assuming the matrix is doubly-sparse and presented in row-order. Our algorithms approximate the Schatten $p$-norms, which we use in turn to approximate other spectral functions, such as logarithm of the determinant, trace of matrix inverse, and Estrada index. We validate these theoretical performance bounds by numerical experiments on real-world matrices representing social networks. We further prove that multiple passes are unavoidable in this setting, and show extensions of our primary technique, including a trade-off between space requirements and number of passes.

</details>

### DessiLBI: Exploring Structural Sparsity of Deep Networks via Differential Inclusion Paths.
- **链接**: [arXiv:2007.02010](https://arxiv.org/abs/2007.02010)
- **作者**: Yanwei Fu, Chen Liu, Donghao Li, Xinwei Sun, Jinshan Zeng, Yuan Yao
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Over-parameterization is ubiquitous nowadays in training neural networks to benefit both optimization in seeking global optima and generalization in reducing prediction error. However, compressive networks are desired in many real world applications and direct training of small networks may be trapped in local optima. In this paper, instead of pruning or distilling over-parameterized models to compressive ones, we propose a new approach based on differential inclusions of inverse scale spaces. Specifically, it generates a family of models from simple to complex ones that couples a pair of parameters to simultaneously train over-parameterized deep models and structural sparsity on weights of fully connected and convolutional layers. Such a differential inclusion scheme has a simple discretization, proposed as Deep structurally splitting Linearized Bregman Iteration (DessiLBI), whose global convergence analysis in deep learning is established that from any initializations, algorithmic iterations converge to a critical point of empirical risks. Experimental evidence shows that DessiLBI achieve comparable and even better performance than the competitive optimizers in exploring the structural sparsity of several widely used backbones on the benchmark datasets. Remarkably, with early stopping, DessiLBI unveils "winning tickets" in early epochs: the effective sparse structure with comparable test accuracy to fully trained over-parameterized models.

</details>

### Inducing and Exploiting Activation Sparsity for Fast Inference on Deep Neural Networks.
- **链接**: [出版页](http://proceedings.mlr.press/v119/kurtz20a.html)
- **作者**: Mark Kurtz, Justin Kopinsky, Rati Gelashvili, Alexander Matveev, John Carr, Michael Goin et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020

### Soft Threshold Weight Reparameterization for Learnable Sparsity.
- **链接**: [arXiv:2002.03231](https://arxiv.org/abs/2002.03231) · [代码](https://github.com/RAIVNLab/STR)
- **作者**: Aditya Kusupati, Vivek Ramanujan, Raghav Somani, Mitchell Wortsman, Prateek Jain, Sham M. Kakade et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Sparsity in Deep Neural Networks (DNNs) is studied extensively with the focus of maximizing prediction accuracy given an overall parameter budget. Existing methods rely on uniform or heuristic non-uniform sparsity budgets which have sub-optimal layer-wise parameter allocation resulting in a) lower prediction accuracy or b) higher inference cost (FLOPs). This work proposes Soft Threshold Reparameterization (STR), a novel use of the soft-threshold operator on DNN weights. STR smoothly induces sparsity while learning pruning thresholds thereby obtaining a non-uniform sparsity budget. Our method achieves state-of-the-art accuracy for unstructured sparsity in CNNs (ResNet50 and MobileNetV1 on ImageNet-1K), and, additionally, learns non-uniform budgets that empirically reduce the FLOPs by up to 50%. Notably, STR boosts the accuracy over existing results by up to 10% in the ultra sparse (99%) regime and can also be used to induce low-rank (structured sparsity) in RNNs. In short, STR is a simple mechanism which learns effective sparsity budgets that contrast with popular heuristics. Code, pretrained models and sparsity budgets are at https://github.com/RAIVNLab/STR.

</details>

### Input-Sparsity Low Rank Approximation in Schatten Norm.
- **链接**: [arXiv:2004.12646](https://arxiv.org/abs/2004.12646)
- **作者**: Yi Li, David P. Woodruff
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We give the first input-sparsity time algorithms for the rank-$k$ low rank approximation problem in every Schatten norm. Specifically, for a given $n\times n$ matrix $A$, our algorithm computes $Y,Z\in \mathbb{R}^{n\times k}$, which, with high probability, satisfy $\|A-YZ^T\|_p \leq (1+ε)\|A-A_k\|_p$, where $\|M\|_p = \left (\sum_{i=1}^n σ_i(M)^p \right )^{1/p}$ is the Schatten $p$-norm of a matrix $M$ with singular values $σ_1(M), \ldots, σ_n(M)$, and where $A_k$ is the best rank-$k$ approximation to $A$. Our algorithm runs in time $\tilde{O}(\operatorname{nnz}(A) + mn^{α_p}\operatorname{poly}(k/ε))$, where $α_p = 0$ for $p\in [1,2)$ and $α_p = (ω-1)(1-2/p)$ for $p>2$ and $ω\approx 2.374$ is the exponent of matrix multiplication. For the important case of $p = 1$, which corresponds to the more "robust" nuclear norm, we obtain $\tilde{O}(\operatorname{nnz}(A) + m \cdot \operatorname{poly}(k/ε))$ time, which was previously only known for the Frobenius norm ($p = 2$). Moreover, since $α_p < ω- 1$ for every $p$, our algorithm has a better dependence on $n$ than that in the singular value decomposition for every $p$. Crucial to our analysis is the use of dimensionality reduction for Ky-Fan $p$-norms.

</details>

### Fiedler Regularization: Learning Neural Networks with Graph Sparsity.
- **链接**: [arXiv:2003.00992](https://arxiv.org/abs/2003.00992)
- **作者**: Edric Tam, David B. Dunson
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce a novel regularization approach for deep learning that incorporates and respects the underlying graphical structure of the neural network. Existing regularization methods often focus on dropping/penalizing weights in a global manner that ignores the connectivity structure of the neural network. We propose to use the Fiedler value of the neural network's underlying graph as a tool for regularization. We provide theoretical support for this approach via spectral graph theory. We list several useful properties of the Fiedler value that makes it suitable in regularization. We provide an approximate, variational approach for fast computation in practical training of neural networks. We provide bounds on such approximations. We provide an alternative but equivalent formulation of this framework in the form of a structurally weighted L1 penalty, thus linking our approach to sparsity induction. We performed experiments on datasets that compare Fiedler regularization with traditional regularization methods such as dropout and weight decay. Results demonstrate the efficacy of Fiedler regularization.

</details>

### Near Input Sparsity Time Kernel Embeddings via Adaptive Sampling.
- **链接**: [arXiv:2007.03927](https://arxiv.org/abs/2007.03927)
- **作者**: David P. Woodruff, Amir Zandieh
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> To accelerate kernel methods, we propose a near input sparsity time algorithm for sampling the high-dimensional feature space implicitly defined by a kernel transformation. Our main contribution is an importance sampling method for subsampling the feature space of a degree $q$ tensoring of data points in almost input sparsity time, improving the recent oblivious sketching method of (Ahle et al., 2020) by a factor of $q^{5/2}/ε^2$. This leads to a subspace embedding for the polynomial kernel, as well as the Gaussian kernel, with a target dimension that is only linearly dependent on the statistical dimension of the kernel and in time which is only linearly dependent on the sparsity of the input dataset. We show how our subspace embedding bounds imply new statistical guarantees for kernel ridge regression. Furthermore, we empirically show that in large-scale regression tasks, our algorithm outperforms state-of-the-art kernel approximation methods.

</details>
