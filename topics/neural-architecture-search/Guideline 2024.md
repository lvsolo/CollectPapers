# Neural Architecture Search — 2024 Guideline

> 领域: 神经架构搜索（NAS、Zero-Cost、搜索空间）
> 论文数: 3 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Encodings for Prediction-based Neural Architecture Search.
- **链接**: [arXiv:2403.02484](https://arxiv.org/abs/2403.02484) · [代码](https://github.com/abdelfattah-lab/flan_nas)
- **作者**: Yash Akhauri, Mohamed S. Abdelfattah
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Predictor-based methods have substantially enhanced Neural Architecture Search (NAS) optimization. The efficacy of these predictors is largely influenced by the method of encoding neural network architectures. While traditional encodings used an adjacency matrix describing the graph structure of a neural network, novel encodings embrace a variety of approaches from unsupervised pretraining of latent representations to vectors of zero-cost proxies. In this paper, we categorize and investigate neural encodings from three main types: structural, learned, and score-based. Furthermore, we extend these encodings and introduce \textit{unified encodings}, that extend NAS predictors to multiple search spaces. Our analysis draws from experiments conducted on over 1.5 million neural network architectures on NAS spaces such as NASBench-101 (NB101), NB201, NB301, Network Design Spaces (NDS), and TransNASBench-101. Building on our study, we present our predictor \textbf{FLAN}: \textbf{Fl}ow \textbf{A}ttention for \textbf{N}AS. FLAN integrates critical insights on predictor design, transfer learning, and \textit{unified encodings} to enable more than an order of magnitude cost reduction for training NAS accuracy predictors. Our implementation and encodings for all neural networks are open-sourced at \href{https://github.com/abdelfattah-lab/flan_nas}{https://github.com/abdelfattah-lab/flan\_nas}.

</details>

### Towards Neural Architecture Search through Hierarchical Generative Modeling.
- **链接**: [出版页](https://proceedings.mlr.press/v235/xiang24a.html)
- **作者**: Lichuan Xiang, Lukasz Dudziak, Mohamed S. Abdelfattah, Abhinav Mehrotra, Nicholas Donald Lane, Hongkai Wen
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### Disentangled Continual Graph Neural Architecture Search with Invariant Modular Supernet.
- **链接**: [出版页](https://proceedings.mlr.press/v235/zhang24bm.html)
- **作者**: Zeyang Zhang, Xin Wang, Yijian Qin, Hong Chen, Ziwei Zhang, Xu Chu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024
