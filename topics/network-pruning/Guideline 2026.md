# Network Pruning — 2026 Guideline

> 领域: 网络剪枝 / 模型压缩（结构化剪枝、稀疏化）
> 论文数: 1 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份:

### Hilbert-Guided Sparse Local Attention **⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2511.05832](https://arxiv.org/abs/2511.05832)
- **作者**: Yunge Li, Lanyu Xu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2026
- **摘要（中）**: ①该论文针对全局自注意力在图像高分辨率下计算和内存成本呈二次增长的问题，以及传统局部注意力模式因窗口内token在1D序列中不连续而导致块稀疏内核加速效果不佳的问题。②提出了一种基于希尔伯特曲线构建窗口和邻域的方法，先将图像token沿希尔伯特曲线重新排序，再在重排序后的1D序列上形成窗口和邻域，从而与现有块稀疏内核结合以提升2D局部注意力的效率。③相比已有工作，该方法从块稀疏角度显著提高了块稀疏度，并可直接利用现有高效内核，无需设计新内核。④实验表明，所提出的希尔伯特窗口注意力和希尔伯特滑动注意力分别将窗口注意力和滑动注意力加速约4倍和18倍，并实例化为希尔伯特窗口Transformer和希尔伯特邻域Transformer，实现了端到端的性能提升。
- **摘要（英）**: This paper addresses the quadratic compute and memory costs of global self-attention in high-resolution images and the inefficiency of conventional local attention patterns due to non-contiguous tokens in 1D sequences. It proposes a Hilbert curve-based method to reorder image tokens and construct windows and neighborhoods on the reordered sequence, enhancing block sparsity for existing block-sparse kernels. Experiments show about 4x and 18x speedups for window and slide attention, respectively, with end-to-end improvements in the instantiated transformers.
- **核心贡献**: 提出基于希尔伯特曲线的窗口和邻域构建方法，以提高块稀疏局部注意力的计算效率。
- **创新点**: 利用希尔伯特曲线的空间填充特性重新排序token，增强块稀疏性以适配现有高效内核。
- **结果**: 窗口注意力和滑动注意力分别加速约4倍和18倍，并实现端到端性能提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The quadratic compute and memory costs of global self-attention severely limit its use in high-resolution images. Local attention reduces complexity by restricting attention to neighborhoods. Block-sparse kernels can further improve the efficiency of local attention, but conventional local attention patterns often fail to deliver significant speedups because tokens within a window are not contiguous in the 1D sequence. This work proposes a novel method for constructing windows and neighborhoods based on the Hilbert curve. Image tokens are first reordered along a Hilbert curve, and windows and neighborhoods are then formed on the reordered 1D sequence. From a block-sparse perspective, this strategy significantly increases block sparsity and can be combined with existing block-sparse kernels to improve the efficiency of 2D local attention. Experiments show that the proposed Hilbert Window Attention and Hilbert Slide Attention can accelerate window attention and slide attention by about $4\times$ and $18\times$, respectively. To assess practicality, the strategy is instantiated as the Hilbert Window Transformer and the Hilbert Neighborhood Transformer, both of which achieve end-to-end speedups with minimal accuracy loss. Overall, combining Hilbert-guided local attention with block-sparse kernels offers a general and practical approach to enhancing the efficiency of 2D local attention for images.

</details>

<!-- COMPLETE v1 papers=1 -->
