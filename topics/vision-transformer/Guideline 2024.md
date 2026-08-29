# Vision Transformer — 2024 Guideline

> 领域: 视觉 Transformer（ViT、混合架构、高效注意力）
> 论文数: 4 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### LUM-ViT: Learnable Under-sampling Mask Vision Transformer for Bandwidth Limited Optical Signal Acquisition.
- **链接**: [arXiv:2403.01412](https://arxiv.org/abs/2403.01412) · [代码](https://github.com/MaxLLF/LUM-ViT)
- **作者**: Lingfeng Liu, Dong Ni, Hangjie Yuan
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Bandwidth constraints during signal acquisition frequently impede real-time detection applications. Hyperspectral data is a notable example, whose vast volume compromises real-time hyperspectral detection. To tackle this hurdle, we introduce a novel approach leveraging pre-acquisition modulation to reduce the acquisition volume. This modulation process is governed by a deep learning model, utilizing prior information. Central to our approach is LUM-ViT, a Vision Transformer variant. Uniquely, LUM-ViT incorporates a learnable under-sampling mask tailored for pre-acquisition modulation. To further optimize for optical calculations, we propose a kernel-level weight binarization technique and a three-stage fine-tuning strategy. Our evaluations reveal that, by sampling a mere 10% of the original image pixels, LUM-ViT maintains the accuracy loss within 1.8% on the ImageNet classification task. The method sustains near-original accuracy when implemented on real-world optical hardware, demonstrating its practicality. Code will be available at https://github.com/MaxLLF/LUM-ViT.

</details>

### A Simple Romance Between Multi-Exit Vision Transformer and Token Reduction.
- **链接**: [出版页](https://openreview.net/forum?id=gJeYtRuguR)
- **作者**: Dongyang Liu, Meina Kan, Shiguang Shan, Xilin Chen
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

## 跨领域论文（完整笔记在其他领域）

- CLIPSelf: Vision Transformer Distills Itself for Open-Vocabulary Dense Prediction. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- Synergistic Patch Pruning for Vision Transformer: Unifying Intra- & Inter-Layer Patch Importance. → [network-pruning](../network-pruning/Guideline%202024.md)
