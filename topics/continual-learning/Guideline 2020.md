# Continual Learning — 2020 Guideline

> 领域: 持续学习 / 增量学习（含 VLM/多模态场景）
> 论文数: 3 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Online Continual Learning from Imbalanced Data.
- **链接**: [出版页](http://proceedings.mlr.press/v119/chrysakis20a.html)
- **作者**: Aristotelis Chrysakis, Marie-Francine Moens
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020

### Neural Topic Modeling with Continual Lifelong Learning.
- **链接**: [arXiv:2006.10909](https://arxiv.org/abs/2006.10909)
- **作者**: Pankaj Gupta, Yatin Chaudhary, Thomas A. Runkler, Hinrich Schütze
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Lifelong learning has recently attracted attention in building machine learning systems that continually accumulate and transfer knowledge to help future learning. Unsupervised topic modeling has been popularly used to discover topics from document collections. However, the application of topic modeling is challenging due to data sparsity, e.g., in a small collection of (short) documents and thus, generate incoherent topics and sub-optimal document representations. To address the problem, we propose a lifelong learning framework for neural topic modeling that can continuously process streams of document collections, accumulate topics and guide future topic modeling tasks by knowledge transfer from several sources to better deal with the sparse data. In the lifelong process, we particularly investigate jointly: (1) sharing generative homologies (latent topics) over lifetime to transfer prior knowledge, and (2) minimizing catastrophic forgetting to retain the past learning via novel selective data augmentation, co-training and topic regularization approaches. Given a stream of document collections, we apply the proposed Lifelong Neural Topic Modeling (LNTM) framework in modeling three sparse document collections as future tasks and demonstrate improved performance quantified by perplexity, topic coherence and information retrieval task.

</details>

### Optimal Continual Learning has Perfect Memory and is NP-hard.
- **链接**: [arXiv:2006.05188](https://arxiv.org/abs/2006.05188)
- **作者**: Jeremias Knoblauch, Hisham Husain, Tom Diethe
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual Learning (CL) algorithms incrementally learn a predictor or representation across multiple sequentially observed tasks. Designing CL algorithms that perform reliably and avoid so-called catastrophic forgetting has proven a persistent challenge. The current paper develops a theoretical approach that explains why. In particular, we derive the computational properties which CL algorithms would have to possess in order to avoid catastrophic forgetting. Our main finding is that such optimal CL algorithms generally solve an NP-hard problem and will require perfect memory to do so. The findings are of theoretical interest, but also explain the excellent performance of CL algorithms using experience replay, episodic memory and core sets relative to regularization-based approaches.

</details>
