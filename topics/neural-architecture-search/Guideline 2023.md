# Neural Architecture Search — 2023 Guideline

> 领域: 神经架构搜索（NAS、Zero-Cost、搜索空间）
> 论文数: 5 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### QAS-Bench: Rethinking Quantum Architecture Search and A Benchmark.
- **链接**: [出版页](https://proceedings.mlr.press/v202/lu23f.html)
- **作者**: Xudong Lu, Kaisen Pan, Ge Yan, Jiaming Shan, Wenjie Wu, Junchi Yan
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Shortest Edit Path Crossover: A Theory-driven Solution to the Permutation Problem in Evolutionary Neural Architecture Search.
- **链接**: [arXiv:2210.14016](https://arxiv.org/abs/2210.14016)
- **作者**: Xin Qiu, Risto Miikkulainen
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Population-based search has recently emerged as a possible alternative to Reinforcement Learning (RL) for black-box neural architecture search (NAS). It performs well in practice even though it is not theoretically well understood. In particular, whereas traditional population-based search methods such as evolutionary algorithms (EAs) draw much power from crossover operations, it is difficult to take advantage of them in NAS. The main obstacle is believed to be the permutation problem: The mapping between genotype and phenotype in traditional graph representations is many-to-one, leading to a disruptive effect of standard crossover. This paper presents the first theoretical analysis of the behaviors of mutation, crossover and RL in black-box NAS, and proposes a new crossover operator based on the shortest edit path (SEP) in graph space. The SEP crossover is shown theoretically to overcome the permutation problem, and as a result, have a better expected improvement compared to mutation, standard crossover and RL. Further, it empirically outperform these other methods on state-of-the-art NAS benchmarks. The SEP crossover therefore allows taking full advantage of population-based search in NAS, and the underlying theory can serve as a foundation for deeper understanding of black-box NAS methods in general.

</details>

### PreNAS: Preferred One-Shot Learning Towards Efficient Neural Architecture Search.
- **链接**: [arXiv:2304.14636](https://arxiv.org/abs/2304.14636) · [代码](https://github.com/tinyvision/PreNAS)
- **作者**: Haibin Wang, Ce Ge, Hesen Chen, Xiuyu Sun
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The wide application of pre-trained models is driving the trend of once-for-all training in one-shot neural architecture search (NAS). However, training within a huge sample space damages the performance of individual subnets and requires much computation to search for an optimal model. In this paper, we present PreNAS, a search-free NAS approach that accentuates target models in one-shot training. Specifically, the sample space is dramatically reduced in advance by a zero-cost selector, and weight-sharing one-shot training is performed on the preferred architectures to alleviate update conflicts. Extensive experiments have demonstrated that PreNAS consistently outperforms state-of-the-art one-shot NAS competitors for both Vision Transformer and convolutional architectures, and importantly, enables instant specialization with zero search cost. Our code is available at https://github.com/tinyvision/PreNAS.

</details>

### QuantumDARTS: Differentiable Quantum Architecture Search for Variational Quantum Algorithms.
- **链接**: [出版页](https://proceedings.mlr.press/v202/wu23v.html)
- **作者**: Wenjie Wu, Ge Yan, Xudong Lu, Kaisen Pan, Junchi Yan
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Do Not Train It: A Linear Neural Architecture Search of Graph Neural Networks.
- **链接**: [arXiv:2305.14065](https://arxiv.org/abs/2305.14065)
- **作者**: Peng Xu, Lin Zhang, Xuanzhou Liu, Jiaqi Sun, Yue Zhao, Haiqin Yang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural architecture search (NAS) for Graph neural networks (GNNs), called NAS-GNNs, has achieved significant performance over manually designed GNN architectures. However, these methods inherit issues from the conventional NAS methods, such as high computational cost and optimization difficulty. More importantly, previous NAS methods have ignored the uniqueness of GNNs, where GNNs possess expressive power without training. With the randomly-initialized weights, we can then seek the optimal architecture parameters via the sparse coding objective and derive a novel NAS-GNNs method, namely neural architecture coding (NAC). Consequently, our NAC holds a no-update scheme on GNNs and can efficiently compute in linear time. Empirical evaluations on multiple GNN benchmark datasets demonstrate that our approach leads to state-of-the-art performance, which is up to $200\times$ faster and $18.8\%$ more accurate than the strong baselines.

</details>
