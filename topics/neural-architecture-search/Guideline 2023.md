# Neural Architecture Search — 2023 Guideline

> 领域: 神经架构搜索（NAS、Zero-Cost、搜索空间）
> 论文数: 4 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### EA-HAS-Bench: Energy-aware Hyperparameter and Architecture Search Benchmark.
- **链接**: [出版页](https://openreview.net/forum?id=n-bvaLSCC78)
- **作者**: Shuguang Dou, Xinyang Jiang, Cairong Zhao, Dongsheng Li
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Improving Differentiable Neural Architecture Search by Encouraging Transferability.
- **链接**: [出版页](https://openreview.net/forum?id=Tl8OmiibP99)
- **作者**: Parth Sheth, Pengtao Xie
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### AutoGT: Automated Graph Transformer Architecture Search.
- **链接**: [出版页](https://openreview.net/forum?id=GcM7qfl5zY)
- **作者**: Zizhao Zhang, Xin Wang, Chaoyu Guan, Ziwei Zhang, Haoyang Li, Wenwu Zhu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Meta-prediction Model for Distillation-Aware NAS on Unseen Datasets.
- **链接**: [arXiv:2305.16948](https://arxiv.org/abs/2305.16948) · [代码](https://github.com/CownowAn/DaSS)
- **作者**: Hayeon Lee, Sohyun An, Minseon Kim, Sung Ju Hwang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Distillation-aware Neural Architecture Search (DaNAS) aims to search for an optimal student architecture that obtains the best performance and/or efficiency when distilling the knowledge from a given teacher model. Previous DaNAS methods have mostly tackled the search for the neural architecture for fixed datasets and the teacher, which are not generalized well on a new task consisting of an unseen dataset and an unseen teacher, thus need to perform a costly search for any new combination of the datasets and the teachers. For standard NAS tasks without KD, meta-learning-based computationally efficient NAS methods have been proposed, which learn the generalized search process over multiple tasks (datasets) and transfer the knowledge obtained over those tasks to a new task. However, since they assume learning from scratch without KD from a teacher, they might not be ideal for DaNAS scenarios. To eliminate the excessive computational cost of DaNAS methods and the sub-optimality of rapid NAS methods, we propose a distillation-aware meta accuracy prediction model, DaSS (Distillation-aware Student Search), which can predict a given architecture's final performances on a dataset when performing KD with a given teacher, without having actually to train it on the target task. The experimental results demonstrate that our proposed meta-prediction model successfully generalizes to multiple unseen datasets for DaNAS tasks, largely outperforming existing meta-NAS methods and rapid NAS baselines. Code is available at https://github.com/CownowAn/DaSS

</details>
