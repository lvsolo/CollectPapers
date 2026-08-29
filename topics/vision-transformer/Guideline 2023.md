# Vision Transformer — 2023 Guideline

> 领域: 视觉 Transformer（ViT、混合架构、高效注意力）
> 论文数: 3 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Understanding and Defending Patched-based Adversarial Attacks for Vision Transformer.
- **链接**: [出版页](https://proceedings.mlr.press/v202/liu23n.html)
- **作者**: Liang Liu, Yanan Guo, Youtao Zhang, Jun Yang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Hiera: A Hierarchical Vision Transformer without the Bells-and-Whistles.
- **链接**: [arXiv:2306.00989](https://arxiv.org/abs/2306.00989) · [代码](https://github.com/facebookresearch/hiera)
- **作者**: Chaitanya Ryali, Yuan-Ting Hu, Daniel Bolya, Chen Wei, Haoqi Fan, Po-Yao Huang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Modern hierarchical vision transformers have added several vision-specific components in the pursuit of supervised classification performance. While these components lead to effective accuracies and attractive FLOP counts, the added complexity actually makes these transformers slower than their vanilla ViT counterparts. In this paper, we argue that this additional bulk is unnecessary. By pretraining with a strong visual pretext task (MAE), we can strip out all the bells-and-whistles from a state-of-the-art multi-stage vision transformer without losing accuracy. In the process, we create Hiera, an extremely simple hierarchical vision transformer that is more accurate than previous models while being significantly faster both at inference and during training. We evaluate Hiera on a variety of tasks for image and video recognition. Our code and models are available at https://github.com/facebookresearch/hiera.

</details>

## 跨领域论文（完整笔记在其他领域）

- Architecture-Agnostic Masked Image Modeling - From ViT back to CNN. → [self-supervised-vision](../self-supervised-vision/Guideline%202023.md)
