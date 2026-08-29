# Neural Architecture Search — 2022 Guideline

> 领域: 神经架构搜索（NAS、Zero-Cost、搜索空间）
> 论文数: 11 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### BLOX: Macro Neural Architecture Search Benchmark and Algorithms.
- **链接**: [arXiv:2210.07271](https://arxiv.org/abs/2210.07271) · [代码](https://github.com/SamsungLabs/blox) · 📚 被引 1
- **作者**: Thomas Chau, Lukasz Dudziak, Hongkai Wen, Nicholas D. Lane, Mohamed S. Abdelfattah
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural architecture search (NAS) has been successfully used to design numerous high-performance neural networks. However, NAS is typically compute-intensive, so most existing approaches restrict the search to decide the operations and topological structure of a single block only, then the same block is stacked repeatedly to form an end-to-end model. Although such an approach reduces the size of search space, recent studies show that a macro search space, which allows blocks in a model to be different, can lead to better performance. To provide a systematic study of the performance of NAS algorithms on a macro search space, we release Blox - a benchmark that consists of 91k unique models trained on the CIFAR-100 dataset. The dataset also includes runtime measurements of all the models on a diverse set of hardware platforms. We perform extensive experiments to compare existing algorithms that are well studied on cell-based search spaces, with the emerging blockwise approaches that aim to make NAS scalable to much larger macro search spaces. The benchmark and code are available at https://github.com/SamsungLabs/blox.

</details>

### Saliency-Aware Neural Architecture Search.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/5e84e4413268b713f0d4a1b23a9dae57-Abstract-Conference.html) · 📚 被引 1
- **作者**: Ramtin Hosseini, Pengtao Xie
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### LiteTransformerSearch: Training-free Neural Architecture Search for Efficient Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/9949e6906be6448230cdba9a4cb2d564-Abstract-Conference.html) · 📚 被引 3
- **作者**: Mojan Javaheripi, Gustavo de Rosa, Subhabrata Mukherjee, Shital Shah, Tomasz Religa, Caio César Teodoro Mendes et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### NAS-Bench-Graph: Benchmarking Graph Neural Architecture Search.
- **链接**: [arXiv:2206.09166](https://arxiv.org/abs/2206.09166) · 📚 被引 5
- **作者**: Yijian Qin, Ziwei Zhang, Xin Wang, Zeyang Zhang, Wenwu Zhu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Graph neural architecture search (GraphNAS) has recently aroused considerable attention in both academia and industry. However, two key challenges seriously hinder the further research of GraphNAS. First, since there is no consensus for the experimental setting, the empirical results in different research papers are often not comparable and even not reproducible, leading to unfair comparisons. Secondly, GraphNAS often needs extensive computations, which makes it highly inefficient and inaccessible to researchers without access to large-scale computation. To solve these challenges, we propose NAS-Bench-Graph, a tailored benchmark that supports unified, reproducible, and efficient evaluations for GraphNAS. Specifically, we construct a unified, expressive yet compact search space, covering 26,206 unique graph neural network (GNN) architectures and propose a principled evaluation protocol. To avoid unnecessary repetitive training, we have trained and evaluated all of these architectures on nine representative graph datasets, recording detailed metrics including train, validation, and test performance in each epoch, the latency, the number of parameters, etc. Based on our proposed benchmark, the performance of GNN architectures can be directly obtained by a look-up table without any further computation, which enables fair, fully reproducible, and efficient comparisons. To demonstrate its usage, we make in-depth analyses of our proposed NAS-Bench-Graph, revealing several interesting findings for GraphNAS. We also showcase how the benchmark can be easily compatible with GraphNAS open libraries such as AutoGL and NNI. To the best of our knowledge, our work is the first benchmark for graph neural architecture search.

</details>

### Efficient Architecture Search for Diverse Tasks.
- **链接**: [arXiv:2204.07554](https://arxiv.org/abs/2204.07554) · 📚 被引 5
- **作者**: Junhong Shen, Mikhail Khodak, Ameet Talwalkar
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While neural architecture search (NAS) has enabled automated machine learning (AutoML) for well-researched areas, its application to tasks beyond computer vision is still under-explored. As less-studied domains are precisely those where we expect AutoML to have the greatest impact, in this work we study NAS for efficiently solving diverse problems. Seeking an approach that is fast, simple, and broadly applicable, we fix a standard convolutional network (CNN) topology and propose to search for the right kernel sizes and dilations its operations should take on. This dramatically expands the model's capacity to extract features at multiple resolutions for different types of data while only requiring search over the operation space. To overcome the efficiency challenges of naive weight-sharing in this search space, we introduce DASH, a differentiable NAS algorithm that computes the mixture-of-operations using the Fourier diagonalization of convolution, achieving both a better asymptotic complexity and an up-to-10x search time speedup in practice. We evaluate DASH on ten tasks spanning a variety of application domains such as PDE solving, protein folding, and heart disease detection. DASH outperforms state-of-the-art AutoML methods in aggregate, attaining the best-known automated performance on seven tasks. Meanwhile, on six of the ten tasks, the combined search and retraining time is less than 2x slower than simply training a CNN backbone that is far less accurate.

</details>

### Unifying and Boosting Gradient-Based Training-Free Neural Architecture Search.
- **链接**: [arXiv:2201.09785](https://arxiv.org/abs/2201.09785) · 📚 被引 1
- **作者**: Yao Shu, Zhongxiang Dai, Zhaoxuan Wu, Bryan Kian Hsiang Low
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural architecture search (NAS) has gained immense popularity owing to its ability to automate neural architecture design. A number of training-free metrics are recently proposed to realize NAS without training, hence making NAS more scalable. Despite their competitive empirical performances, a unified theoretical understanding of these training-free metrics is lacking. As a consequence, (a) the relationships among these metrics are unclear, (b) there is no theoretical interpretation for their empirical performances, and (c) there may exist untapped potential in existing training-free NAS, which probably can be unveiled through a unified theoretical understanding. To this end, this paper presents a unified theoretical analysis of gradient-based training-free NAS, which allows us to (a) theoretically study their relationships, (b) theoretically guarantee their generalization performances, and (c) exploit our unified theoretical understanding to develop a novel framework named hybrid NAS (HNAS) which consistently boosts training-free NAS in a principled way. Remarkably, HNAS can enjoy the advantages of both training-free (i.e., the superior search efficiency) and training-based (i.e., the remarkable search effectiveness) NAS, which we have demonstrated through extensive experiments.

</details>

### NAS-Bench-360: Benchmarking Neural Architecture Search on Diverse Tasks.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/506630e4a43bb9d64a49f98b9ba934e9-Abstract-Datasets_and_Benchmarks.html) · 📚 被引 4
- **作者**: Renbo Tu, Nicholas Roberts, Mikhail Khodak, Junhong Shen, Frederic Sala, Ameet Talwalkar
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### ZARTS: On Zero-order Optimization for Neural Architecture Search.
- **链接**: [arXiv:2110.04743](https://arxiv.org/abs/2110.04743) · 📚 被引 3
- **作者**: Xiaoxing Wang, Wenxuan Guo, Jianlin Su, Xiaokang Yang, Junchi Yan
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Differentiable architecture search (DARTS) has been a popular one-shot paradigm for NAS due to its high efficiency. It introduces trainable architecture parameters to represent the importance of candidate operations and proposes first/second-order approximation to estimate their gradients, making it possible to solve NAS by gradient descent algorithm. However, our in-depth empirical results show that the approximation will often distort the loss landscape, leading to the biased objective to optimize and in turn inaccurate gradient estimation for architecture parameters. This work turns to zero-order optimization and proposes a novel NAS scheme, called ZARTS, to search without enforcing the above approximation. Specifically, three representative zero-order optimization methods are introduced: RS, MGS, and GLD, among which MGS performs best by balancing the accuracy and speed. Moreover, we explore the connections between RS/MGS and gradient descent algorithm and show that our ZARTS can be seen as a robust gradient-free counterpart to DARTS. Extensive experiments on multiple datasets and search spaces show the remarkable performance of our method. In particular, results on 12 benchmarks verify the outstanding robustness of ZARTS, where the performance of DARTS collapses due to its known instability issue. Also, we search on the search space of DARTS to compare with peer methods, and our discovered architecture achieves 97.54% accuracy on CIFAR-10 and 75.7% top-1 accuracy on ImageNet, which are state-of-the-art performance.

</details>

### Few-shot Task-agnostic Neural Architecture Search for Distilling Large Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/b7c12689a89e98a61bcaa65285a41b7c-Abstract-Conference.html) · 📚 被引 1
- **作者**: Dongkuan Xu, Subhabrata Mukherjee, Xiaodong Liu, Debadeepta Dey, Wenhui Wang, Xiang Zhang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### TabNAS: Rejection Sampling for Neural Architecture Search on Tabular Datasets.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/4e392aa9bc70ed731d3c9c32810f92fb-Abstract-Conference.html) · 📚 被引 1
- **作者**: Chengrun Yang, Gabriel Bender, Hanxiao Liu, Pieter-Jan Kindermans, Madeleine Udell, Yifeng Lu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Interpreting Operation Selection in Differentiable Architecture Search: A Perspective from Influence-Directed Explanations.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/cf1129594f603fde9e1913d10b7dbf77-Abstract-Conference.html) · 📚 被引 1
- **作者**: Miao Zhang, Wei Huang, Bin Yang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022
