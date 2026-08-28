# Network Pruning — 2021 Guideline

> 领域: 网络剪枝 / 模型压缩（结构化剪枝、稀疏化）
> 论文数: 8 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Chasing Sparsity in Vision Transformers: An End-to-End Exploration.
- **链接**: [arXiv:2106.04533](https://arxiv.org/abs/2106.04533) · [代码](https://github.com/VITA-Group/SViTE)
- **作者**: Tianlong Chen, Yu Cheng, Zhe Gan, Lu Yuan, Lei Zhang, Zhangyang Wang
- **🏷️ 机构**: PolyU / OPPO
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision transformers (ViTs) have recently received explosive popularity, but their enormous model sizes and training costs remain daunting. Conventional post-training pruning often incurs higher training budgets. In contrast, this paper aims to trim down both the training memory overhead and the inference complexity, without sacrificing the achievable accuracy. We carry out the first-of-its-kind comprehensive exploration, on taking a unified approach of integrating sparsity in ViTs "from end to end". Specifically, instead of training full ViTs, we dynamically extract and train sparse subnetworks, while sticking to a fixed small parameter budget. Our approach jointly optimizes model parameters and explores connectivity throughout training, ending up with one sparse network as the final output. The approach is seamlessly extended from unstructured to structured sparsity, the latter by considering to guide the prune-and-grow of self-attention heads inside ViTs. We further co-explore data and architecture sparsity for additional efficiency gains by plugging in a novel learnable token selector to adaptively determine the currently most vital patches. Extensive results on ImageNet with diverse ViT backbones validate the effectiveness of our proposals which obtain significantly reduced computational cost and almost unimpaired generalization. Perhaps most surprisingly, we find that the proposed sparse (co-)training can sometimes improve the ViT accuracy rather than compromising it, making sparsity a tantalizing "free lunch". For example, our sparsified DeiT-Small at (5%, 50%) sparsity for (data, architecture), improves 0.28% top-1 accuracy, and meanwhile enjoys 49.32% FLOPs and 4.40% running time savings. Our codes are available at https://github.com/VITA-Group/SViTE.

</details>

### Exploiting Data Sparsity in Secure Cross-Platform Social Recommendation.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/56db57b4db0a6fcb7f9e0c0b504f6472-Abstract.html)
- **作者**: Jinming Cui, Chaochao Chen, Lingjuan Lyu, Carl Yang, Li Wang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### T-LoHo: A Bayesian Regularization Model for Structured Sparsity and Smoothness on Graphs.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/05a70454516ecd9194c293b0e415777f-Abstract.html)
- **作者**: Changwoo J. Lee, Zhao Tang Luo, Huiyan Sang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### Channel Permutations for N: M Sparsity.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/6e8404c3b93a9527c8db241a1846599a-Abstract.html)
- **作者**: Jeff Pool, Chong Yu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### Powerpropagation: A sparsity inducing weight reparameterisation.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/f1e709e6aef16ba2f0cd6c7e4f52b9b6-Abstract.html)
- **作者**: Jonathan Schwarz, Siddhant M. Jayakumar, Razvan Pascanu, Peter E. Latham, Yee Whye Teh
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### Post-Training Sparsity-Aware Quantization.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/9431c87f273e507e6040fcb07dcb4509-Abstract.html)
- **作者**: Gil Shomron, Freddy Gabbay, Samer Kurzum, Uri C. Weiser
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### Aligned Structured Sparsity Learning for Efficient Image Super-Resolution.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/15de21c670ae7c3f6f3f1f37029303c9-Abstract.html) · 📚 被引 39
- **作者**: Yulun Zhang, Huan Wang, Can Qin, Yun Fu
- **🏷️ 机构**: Department of ECE, Northeastern University, Boston, MA, USA, Computer Vision Lab, ETH Z&#x00FC;rich, Z&#x00FC;rich, Switzerland, Department of ECE and Khoury College of Computer Science, Northeastern University, Boston, MA, USA
- **会议**: NeurIPS 2021

## 跨领域论文（完整笔记在其他领域）

- Learning where to learn: Gradient sparsity in meta and continual learning. → [continual-learning](../continual-learning/Guideline%202021.md)
