# Neural Architecture Search — 2022 Guideline

> 领域: 神经架构搜索（NAS、Zero-Cost、搜索空间）
> 论文数: 11 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### BLOX: Macro Neural Architecture Search Benchmark and Algorithms.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/c7589a96e8adfcf5a006c452b3758fd5-Abstract-Datasets_and_Benchmarks.html) · 📚 被引 1
- **作者**: Thomas Chau, Lukasz Dudziak, Hongkai Wen, Nicholas D. Lane, Mohamed S. Abdelfattah
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

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
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/004bed4e186fdd7ebb73aad6e97c2332-Abstract-Datasets_and_Benchmarks.html) · 📚 被引 5
- **作者**: Yijian Qin, Ziwei Zhang, Xin Wang, Zeyang Zhang, Wenwu Zhu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Efficient Architecture Search for Diverse Tasks.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/6724eae98f3917968d54c193ac0b45f1-Abstract-Conference.html) · 📚 被引 5
- **作者**: Junhong Shen, Mikhail Khodak, Ameet Talwalkar
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

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
