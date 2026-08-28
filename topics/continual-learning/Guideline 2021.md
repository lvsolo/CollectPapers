# Continual Learning — 2021 Guideline

> 领域: 持续学习 / 增量学习（含 VLM/多模态场景）
> 论文数: 5 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### SSUL: Semantic Segmentation with Unknown Label for Exemplar-based Class-Incremental Learning.
- **链接**: [arXiv:2106.11562](https://arxiv.org/abs/2106.11562) · [代码](https://github.com/clovaai/SSUL)
- **作者**: Sungmin Cha, Beomyoung Kim, Youngjoon Yoo, Taesup Moon
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper introduces a solid state-of-the-art baseline for a class-incremental semantic segmentation (CISS) problem. While the recent CISS algorithms utilize variants of the knowledge distillation (KD) technique to tackle the problem, they failed to fully address the critical challenges in CISS causing the catastrophic forgetting; the semantic drift of the background class and the multi-label prediction issue. To better address these challenges, we propose a new method, dubbed SSUL-M (Semantic Segmentation with Unknown Label with Memory), by carefully combining techniques tailored for semantic segmentation. Specifically, we claim three main contributions. (1) defining unknown classes within the background class to help to learn future classes (help plasticity), (2) freezing backbone network and past classifiers with binary cross-entropy loss and pseudo-labeling to overcome catastrophic forgetting (help stability), and (3) utilizing tiny exemplar memory for the first time in CISS to improve both plasticity and stability. The extensively conducted experiments show the effectiveness of our method, achieving significantly better performance than the recent state-of-the-art baselines on the standard benchmark datasets. Furthermore, we justify our contributions with thorough ablation analyses and discuss different natures of the CISS problem compared to the traditional class-incremental learning targeting classification. The official code is available at https://github.com/clovaai/SSUL.

</details>

### RMM: Reinforced Memory Management for Class-Incremental Learning.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/1cbcaa5abbb6b70f378a3a03d0c26386-Abstract.html)
- **作者**: Yaoyao Liu, Bernt Schiele, Qianru Sun
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### Overcoming Catastrophic Forgetting in Incremental Few-Shot Learning by Finding Flat Minima.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/357cfba15668cc2e1e73111e09d54383-Abstract.html)
- **作者**: Guangyuan Shi, Jiaxin Chen, Wenlong Zhang, Li-Ming Zhan, Xiao-Ming Wu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### Class-Incremental Learning via Dual Augmentation.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/77ee3bc58ce560b86c2b59363281e914-Abstract.html)
- **作者**: Fei Zhu, Zhen Cheng, Xu-Yao Zhang, Cheng-Lin Liu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### Learning where to learn: Gradient sparsity in meta and continual learning.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/2a10665525774fa2501c2c8c4985ce61-Abstract.html)
- **作者**: Johannes von Oswald, Dominic Zhao, Seijin Kobayashi, Simon Schug, Massimo Caccia, Nicolas Zucchet et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021
