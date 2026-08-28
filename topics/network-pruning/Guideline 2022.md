# Network Pruning — 2022 Guideline

> 领域: 网络剪枝 / 模型压缩（结构化剪枝、稀疏化）
> 论文数: 12 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### The Combinatorial Brain Surgeon: Pruning Weights That Cancel One Another in Neural Networks.
- **链接**: [arXiv:2203.04466](https://arxiv.org/abs/2203.04466)
- **作者**: Xin Yu, Thiago Serra, Srikumar Ramalingam, Shandian Zhe
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

### Linearity Grafting: Relaxed Neuron Pruning Helps Certifiable Robustness.
- **链接**: [arXiv:2206.07839](https://arxiv.org/abs/2206.07839)
- **作者**: Tianlong Chen, Huan Zhang, Zhenyu Zhang, Shiyu Chang, Sijia Liu, Pin-Yu Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

### SPDY: Accurate Pruning with Speedup Guarantees.
- **链接**: [arXiv:2201.13096](https://arxiv.org/abs/2201.13096)
- **作者**: Elias Frantar, Dan Alistarh
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

### Sparse Double Descent: Where Network Pruning Aggravates Overfitting.
- **链接**: [arXiv:2206.08684](https://arxiv.org/abs/2206.08684)
- **作者**: Zheng He, Zeke Xie, Quanzhi Zhu, Zengchang Qin
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

### PAC-Net: A Model Pruning Approach to Inductive Transfer Learning.
- **链接**: [arXiv:2206.05703](https://arxiv.org/abs/2206.05703)
- **作者**: Sanghoon Myung, In Huh, Wonik Jang, Jae Myung Choe, Jisu Ryu, Daesin Kim et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

### Neural Network Pruning Denoises the Features and Makes Local Connectivity Emerge in Visual Tasks.
- **链接**: [出版页](https://proceedings.mlr.press/v162/pellegrini22a.html)
- **作者**: Franco Pellegrini, Giulio Biroli
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

### Winning the Lottery Ahead of Time: Efficient Early Network Pruning.
- **链接**: [arXiv:2206.10451](https://arxiv.org/abs/2206.10451)
- **作者**: John Rachwan, Daniel Zügner, Bertrand Charpentier, Simon Geisler, Morgane Ayle, Stephan Günnemann
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

### Topology-Aware Network Pruning using Multi-stage Graph Embedding and Reinforcement Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v162/yu22e.html)
- **作者**: Sixing Yu, Arya Mazaheri, Ali Jannesari
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

### PLATON: Pruning Large Transformer Models with Upper Confidence Bound of Weight Importance.
- **链接**: [arXiv:2206.12562](https://arxiv.org/abs/2206.12562)
- **作者**: Qingru Zhang, Simiao Zuo, Chen Liang, Alexander Bukharin, Pengcheng He, Weizhu Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

### SpeqNets: Sparsity-aware permutation-equivariant graph networks.
- **链接**: [arXiv:2203.13913](https://arxiv.org/abs/2203.13913)
- **作者**: Christopher Morris, Gaurav Rattan, Sandra Kiefer, Siamak Ravanbakhsh
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While (message-passing) graph neural networks have clear limitations in approximating permutation-equivariant functions over graphs or general relational data, more expressive, higher-order graph neural networks do not scale to large graphs. They either operate on $k$-order tensors or consider all $k$-node subgraphs, implying an exponential dependence on $k$ in memory requirements, and do not adapt to the sparsity of the graph. By introducing new heuristics for the graph isomorphism problem, we devise a class of universal, permutation-equivariant graph networks, which, unlike previous architectures, offer a fine-grained control between expressivity and scalability and adapt to the sparsity of the graph. These architectures lead to vastly reduced computation times compared to standard higher-order graph networks in the supervised node- and graph-level classification and regression regime while significantly improving over standard graph neural network and graph kernel architectures in terms of predictive performance.

</details>

### Sparsity in Partially Controllable Linear Systems.
- **链接**: [arXiv:2110.06150](https://arxiv.org/abs/2110.06150)
- **作者**: Yonathan Efroni, Sham M. Kakade, Akshay Krishnamurthy, Cyril Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> A fundamental concept in control theory is that of controllability, where any system state can be reached through an appropriate choice of control inputs. Indeed, a large body of classical and modern approaches are designed for controllable linear dynamical systems. However, in practice, we often encounter systems in which a large set of state variables evolve exogenously and independently of the control inputs; such systems are only partially controllable. The focus of this work is on a large class of partially controllable linear dynamical systems, specified by an underlying sparsity pattern. Our main results establish structural conditions and finite-sample guarantees for learning to control such systems. In particular, our structural results characterize those state variables which are irrelevant for optimal control, an analysis which departs from classical control techniques. Our algorithmic results adapt techniques from high-dimensional statistics -- specifically soft-thresholding and semiparametric least-squares -- to exploit the underlying sparsity pattern in order to obtain finite-sample guarantees that significantly improve over those based on certainty-equivalence. We also corroborate these theoretical improvements over certainty-equivalent control through a simulation study.

</details>

### Leverage Score Sampling for Tensor Product Matrices in Input Sparsity Time.
- **链接**: [arXiv:2202.04515](https://arxiv.org/abs/2202.04515)
- **作者**: David P. Woodruff, Amir Zandieh
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose an input sparsity time sampling algorithm that can spectrally approximate the Gram matrix corresponding to the $q$-fold column-wise tensor product of $q$ matrices using a nearly optimal number of samples, improving upon all previously known methods by poly$(q)$ factors. Furthermore, for the important special case of the $q$-fold self-tensoring of a dataset, which is the feature matrix of the degree-$q$ polynomial kernel, the leading term of our method's runtime is proportional to the size of the input dataset and has no dependence on $q$. Previous techniques either incur poly$(q)$ slowdowns in their runtime or remove the dependence on $q$ at the expense of having sub-optimal target dimension, and depend quadratically on the number of data-points in their runtime. Our sampling technique relies on a collection of $q$ partially correlated random projections which can be simultaneously applied to a dataset $X$ in total time that only depends on the size of $X$, and at the same time their $q$-fold Kronecker product acts as a near-isometry for any fixed vector in the column span of $X^{\otimes q}$. We also show that our sampling methods generalize to other classes of kernels beyond polynomial, such as Gaussian and Neural Tangent kernels.

</details>
