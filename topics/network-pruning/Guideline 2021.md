# Network Pruning — 2021 Guideline

> 领域: 网络剪枝 / 模型压缩（结构化剪枝、稀疏化）
> 论文数: 8 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Accelerate CNNs from Three Dimensions: A Comprehensive Pruning Framework.
- **链接**: [出版页](http://proceedings.mlr.press/v139/wang21e.html)
- **作者**: Wenxiao Wang, Minghao Chen, Shuai Zhao, Long Chen, Jinming Hu, Haifeng Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2021

### Group Fisher Pruning for Practical Network Compression.
- **链接**: [出版页](http://proceedings.mlr.press/v139/liu21ab.html)
- **作者**: Liyang Liu, Shilong Zhang, Zhanghui Kuang, Aojun Zhou, Jing-Hao Xue, Xinjiang Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2021

### A Probabilistic Approach to Neural Network Pruning.
- **链接**: [arXiv:2105.10065](https://arxiv.org/abs/2105.10065)
- **作者**: Xin Qian, Diego Klabjan
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2021

### On the Predictability of Pruning Across Scales.
- **链接**: [arXiv:2006.10621](https://arxiv.org/abs/2006.10621)
- **作者**: Jonathan S. Rosenfeld, Jonathan Frankle, Michael Carbin, Nir Shavit
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We show that the error of iteratively magnitude-pruned networks empirically follows a scaling law with interpretable coefficients that depend on the architecture and task. We functionally approximate the error of the pruned networks, showing it is predictable in terms of an invariant tying width, depth, and pruning level, such that networks of vastly different pruned densities are interchangeable. We demonstrate the accuracy of this approximation over orders of magnitude in depth, width, dataset size, and density. We show that the functional form holds (generalizes) for large scale data (e.g., ImageNet) and architectures (e.g., ResNets). As neural networks become ever larger and costlier to train, our findings suggest a framework for reasoning conceptually and analytically about a standard method for unstructured pruning.

</details>

### Improving Molecular Graph Neural Network Explainability with Orthonormalization and Induced Sparsity.
- **链接**: [arXiv:2105.04854](https://arxiv.org/abs/2105.04854)
- **作者**: Ryan Henderson, Djork-Arné Clevert, Floriane Montanari
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Rationalizing which parts of a molecule drive the predictions of a molecular graph convolutional neural network (GCNN) can be difficult. To help, we propose two simple regularization techniques to apply during the training of GCNNs: Batch Representation Orthonormalization (BRO) and Gini regularization. BRO, inspired by molecular orbital theory, encourages graph convolution operations to generate orthonormal node embeddings. Gini regularization is applied to the weights of the output layer and constrains the number of dimensions the model can use to make predictions. We show that Gini and BRO regularization can improve the accuracy of state-of-the-art GCNN attribution methods on artificial benchmark datasets. In a real-world setting, we demonstrate that medicinal chemists significantly prefer explanations extracted from regularized models. While we only study these regularizers in the context of GCNNs, both can be applied to other types of neural networks

</details>

### In-Database Regression in Input Sparsity Time.
- **链接**: [arXiv:2107.05672](https://arxiv.org/abs/2107.05672)
- **作者**: Rajesh Jayaram, Alireza Samadian, David P. Woodruff, Peng Ye
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Sketching is a powerful dimensionality reduction technique for accelerating algorithms for data analysis. A crucial step in sketching methods is to compute a subspace embedding (SE) for a large matrix $\mathbf{A} \in \mathbb{R}^{N \times d}$. SE's are the primary tool for obtaining extremely efficient solutions for many linear-algebraic tasks, such as least squares regression and low rank approximation. Computing an SE often requires an explicit representation of $\mathbf{A}$ and running time proportional to the size of $\mathbf{A}$. However, if $\mathbf{A}= \mathbf{T}_1 \Join \mathbf{T}_2 \Join \dots \Join \mathbf{T}_m$ is the result of a database join query on several smaller tables $\mathbf{T}_i \in \mathbb{R}^{n_i \times d_i}$, then this running time can be prohibitive, as $\mathbf{A}$ itself can have as many as $O(n_1 n_2 \cdots n_m)$ rows. In this work, we design subspace embeddings for database joins which can be computed significantly faster than computing the join. For the case of a two table join $\mathbf{A} = \mathbf{T}_1 \Join \mathbf{T}_2$ we give input-sparsity algorithms for computing subspace embeddings, with running time bounded by the number of non-zero entries in $\mathbf{T}_1,\mathbf{T}_2$. This results in input-sparsity time algorithms for high accuracy regression, significantly improving upon the running time of prior FAQ-based methods for regression. We extend our results to arbitrary joins for the ridge regression problem, also considerably improving the running time of prior methods. Empirically, we apply our method to real datasets and show that it is significantly faster than existing algorithms.

</details>

### Sparsity-Agnostic Lasso Bandit.
- **链接**: [arXiv:2007.08477](https://arxiv.org/abs/2007.08477)
- **作者**: Min-hwan Oh, Garud Iyengar, Assaf Zeevi
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We consider a stochastic contextual bandit problem where the dimension $d$ of the feature vectors is potentially large, however, only a sparse subset of features of cardinality $s_0 \ll d$ affect the reward function. Essentially all existing algorithms for sparse bandits require a priori knowledge of the value of the sparsity index $s_0$. This knowledge is almost never available in practice, and misspecification of this parameter can lead to severe deterioration in the performance of existing methods. The main contribution of this paper is to propose an algorithm that does not require prior knowledge of the sparsity index $s_0$ and establish tight regret bounds on its performance under mild conditions. We also comprehensively evaluate our proposed algorithm numerically and show that it consistently outperforms existing methods, even when the correct sparsity index is revealed to them but is kept hidden from our algorithm.

</details>

### Homomorphic Sensing: Sparsity and Noise.
- **链接**: [出版页](http://proceedings.mlr.press/v139/peng21a.html)
- **作者**: Liangzu Peng, Boshi Wang, Manolis C. Tsakiris
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2021
