# Neural Architecture Search — 2025 Guideline

> 领域: 神经架构搜索（NAS、Zero-Cost、搜索空间）
> 论文数: 5 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Per-Architecture Training-Free Metric Optimization for Neural Architecture Search.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/84f5e528dcab71efc71b79710f7d67eb-Abstract-Conference.html) · 📚 被引 2
- **作者**: Mingzhuo Lin, Jianping Luo
- **🏷️ 机构**: Shenzhen University, Department of Software Engineering, Shenzhen University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Evaluation is a critical but costly procedure in neural architecture search (NAS). Performance predictors have been widely adopted to reduce evaluation costs by directly estimating architecture performance. The effectiveness of predictors is heavily influenced by the choice of loss functions. While traditional predictors employ regression loss functions to evaluate the absolute accuracy of architectures, recent approaches have explored various ranking-based loss functions, such as pairwise and listwise ranking losses, to focus on the ranking of architecture performance. Despite their success in NAS, the effectiveness and characteristics of these loss functions have not been thoroughly investigated. In this paper, we conduct the first comprehensive study on loss functions in performance predictors, categorizing them into three main types: regression, ranking, and weighted loss functions. Specifically, we assess eight loss functions using a range of NAS-relevant metrics on 13 tasks across five search spaces. Our results reveal that specific categories of loss functions can be effectively combined to enhance predictor-based NAS. Furthermore, our findings could provide practical guidance for selecting appropriate loss functions for various tasks. We hope this work provides meaningful insights to guide the development of loss functions for predictor-based methods in the NAS community.

</details>

### TensorRL-QAS: Reinforcement learning with tensor networks for improved quantum architecture search.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/af008ae1c0301e218ee89a86833198e3-Abstract-Conference.html) · 📚 被引 0
- **作者**: Akash Kundu, Stefano Mangini
- **🏷️ 机构**: Delft University of Technology, University of Helsinki
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> N-shot neural architecture search (NAS) exploits a supernet containing all candidate subnets for a given search space. The subnets are typically trained with a static training strategy (e.g., using the same learning rate (LR) scheduler and optimizer for all subnets). This, however, does not consider that individual subnets have distinct characteristics, leading to two problems: (1) The supernet training is biased towards the low-complexity subnets (unfairness); (2) the momentum update in the supernet is noisy (noisy momentum). We present a dynamic supernet training technique to address these problems by adjusting the training strategy adaptive to the subnets. Specifically, we introduce a complexity-aware LR scheduler (CaLR) that controls the decay ratio of LR adaptive to the complexities of subnets, which alleviates the unfairness problem. We also present a momentum separation technique (MS). It groups the subnets with similar structural characteristics and uses a separate momentum for each group, avoiding the noisy momentum problem. Our approach can be applicable to various N-shot NAS methods with marginal cost, while improving the search performance drastically. We validate the effectiveness of our approach on various search spaces (e.g., NAS-Bench-201, Mobilenet spaces) and datasets (e.g., CIFAR-10/100, ImageNet).

</details>

### Training-free Neural Architecture Search through Variance of Knowledge of Deep Network Weights.
- **链接**: [arXiv:2502.04975](https://arxiv.org/abs/2502.04975) · 📚 被引 4
- **作者**: Ondrej Týbl, Lukás Neumann
- **🏷️ 机构**: Czech Technical University in Prague,CMP Visual Recognition Group, Faculty of Electrical Engineering
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep learning has revolutionized computer vision, but it achieved its tremendous success using deep network architectures which are mostly hand-crafted and therefore likely suboptimal. Neural Architecture Search (NAS) aims to bridge this gap by following a well-defined optimization paradigm which systematically looks for the best architecture, given objective criterion such as maximal classification accuracy. The main limitation of NAS is however its astronomical computational cost, as it typically requires training each candidate network architecture from scratch. In this paper, we aim to alleviate this limitation by proposing a novel training-free proxy for image classification accuracy based on Fisher Information. The proposed proxy has a strong theoretical background in statistics and it allows estimating expected image classification accuracy of a given deep network without training the network, thus significantly reducing computational cost of standard NAS algorithms. Our training-free proxy achieves state-of-the-art results on three public datasets and in two search spaces, both when evaluated using previously proposed metrics, as well as using a new metric that we propose which we demonstrate is more informative for practical NAS applications. The source code is publicly available at http://www.github.com/ondratybl/VKDNW

</details>
