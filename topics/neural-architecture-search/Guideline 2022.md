# Neural Architecture Search — 2022 Guideline

> 领域: 神经架构搜索（NAS、Zero-Cost、搜索空间）
> 论文数: 4 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### NASViT: Neural Architecture Search for Efficient Vision Transformers with Gradient Conflict aware Supernet Training.
- **链接**: [出版页](https://openreview.net/forum?id=Qaw16njk6L)
- **作者**: Chengyue Gong, Dilin Wang, Meng Li, Xinlei Chen, Zhicheng Yan, Yuandong Tian et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

### SUMNAS: Supernet with Unbiased Meta-Features for Neural Architecture Search.
- **链接**: [出版页](https://openreview.net/forum?id=Z8FzvVU6_Kj)
- **作者**: Hyeonmin Ha, Ji-Hoon Kim, Semin Park, Byung-Gon Chun
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

### NASI: Label- and Data-agnostic Neural Architecture Search at Initialization.
- **链接**: [arXiv:2109.00817](https://arxiv.org/abs/2109.00817)
- **作者**: Yao Shu, Shaofeng Cai, Zhongxiang Dai, Beng Chin Ooi, Bryan Kian Hsiang Low
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent years have witnessed a surging interest in Neural Architecture Search (NAS). Various algorithms have been proposed to improve the search efficiency and effectiveness of NAS, i.e., to reduce the search cost and improve the generalization performance of the selected architectures, respectively. However, the search efficiency of these algorithms is severely limited by the need for model training during the search process. To overcome this limitation, we propose a novel NAS algorithm called NAS at Initialization (NASI) that exploits the capability of a Neural Tangent Kernel in being able to characterize the converged performance of candidate architectures at initialization, hence allowing model training to be completely avoided to boost the search efficiency. Besides the improved search efficiency, NASI also achieves competitive search effectiveness on various datasets like CIFAR-10/100 and ImageNet. Further, NASI is shown to be label- and data-agnostic under mild conditions, which guarantees the transferability of architectures selected by our NASI over different datasets.

</details>

### On Redundancy and Diversity in Cell-based Neural Architecture Search.
- **链接**: [arXiv:2203.08887](https://arxiv.org/abs/2203.08887) · [代码](https://github.com/xingchenwan/cell-based-NAS-analysis)
- **作者**: Xingchen Wan, Binxin Ru, Pedro M. Esperança, Zhenguo Li
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Searching for the architecture cells is a dominant paradigm in NAS. However, little attention has been devoted to the analysis of the cell-based search spaces even though it is highly important for the continual development of NAS. In this work, we conduct an empirical post-hoc analysis of architectures from the popular cell-based search spaces and find that the existing search spaces contain a high degree of redundancy: the architecture performance is minimally sensitive to changes at large parts of the cells, and universally adopted designs, like the explicit search for a reduction cell, significantly increase the complexities but have very limited impact on the performance. Across architectures found by a diverse set of search strategies, we consistently find that the parts of the cells that do matter for architecture performance often follow similar and simple patterns. By explicitly constraining cells to include these patterns, randomly sampled architectures can match or even outperform the state of the art. These findings cast doubts into our ability to discover truly novel architectures in the existing cell-based search spaces, and inspire our suggestions for improvement to guide future NAS research. Code is available at https://github.com/xingchenwan/cell-based-NAS-analysis.

</details>
