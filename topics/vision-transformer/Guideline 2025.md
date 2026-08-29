# Vision Transformer — 2025 Guideline

> 领域: 视觉 Transformer（ViT、混合架构、高效注意力）
> 论文数: 4 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### PADRe: A Unifying Polynomial Attention Drop-in Replacement for Efficient Vision Transformer.
- **链接**: [arXiv:2407.11306](https://arxiv.org/abs/2407.11306)
- **作者**: Pierre-David Letourneau, Manish Kumar Singh, Hsin-Pai Cheng, Shizhong Han, Yunxiao Shi, Dalton Jones et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present Polynomial Attention Drop-in Replacement (PADRe), a novel and unifying framework designed to replace the conventional self-attention mechanism in transformer models. Notably, several recent alternative attention mechanisms, including Hyena, Mamba, SimA, Conv2Former, and Castling-ViT, can be viewed as specific instances of our PADRe framework. PADRe leverages polynomial functions and draws upon established results from approximation theory, enhancing computational efficiency without compromising accuracy. PADRe's key components include multiplicative nonlinearities, which we implement using straightforward, hardware-friendly operations such as Hadamard products, incurring only linear computational and memory costs. PADRe further avoids the need for using complex functions such as Softmax, yet it maintains comparable or superior accuracy compared to traditional self-attention. We assess the effectiveness of PADRe as a drop-in replacement for self-attention across diverse computer vision tasks. These tasks include image classification, image-based 2D object detection, and 3D point cloud object detection. Empirical results demonstrate that PADRe runs significantly faster than the conventional self-attention (11x ~ 43x faster on server GPU and mobile NPU) while maintaining similar accuracy when substituting self-attention in the transformer models.

</details>

### CViT: Continuous Vision Transformer for Operator Learning.
- **链接**: [出版页](https://openreview.net/forum?id=cRnCcuLvyr)
- **作者**: Sifan Wang, Jacob H. Seidman, Shyam Sankaran, Hanwen Wang, George J. Pappas, Paris Perdikaris
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Spiking Vision Transformer with Saccadic Attention.
- **链接**: [arXiv:2502.12677](https://arxiv.org/abs/2502.12677)
- **作者**: Shuai Wang, Malu Zhang, Dehao Zhang, Ammar Belatreche, Yichen Xiao, Yu Liang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The combination of Spiking Neural Networks (SNNs) and Vision Transformers (ViTs) holds potential for achieving both energy efficiency and high performance, particularly suitable for edge vision applications. However, a significant performance gap still exists between SNN-based ViTs and their ANN counterparts. Here, we first analyze why SNN-based ViTs suffer from limited performance and identify a mismatch between the vanilla self-attention mechanism and spatio-temporal spike trains. This mismatch results in degraded spatial relevance and limited temporal interactions. To address these issues, we draw inspiration from biological saccadic attention mechanisms and introduce an innovative Saccadic Spike Self-Attention (SSSA) method. Specifically, in the spatial domain, SSSA employs a novel spike distribution-based method to effectively assess the relevance between Query and Key pairs in SNN-based ViTs. Temporally, SSSA employs a saccadic interaction module that dynamically focuses on selected visual areas at each timestep and significantly enhances whole scene understanding through temporal interactions. Building on the SSSA mechanism, we develop a SNN-based Vision Transformer (SNN-ViT). Extensive experiments across various visual tasks demonstrate that SNN-ViT achieves state-of-the-art performance with linear computational complexity. The effectiveness and efficiency of the SNN-ViT highlight its potential for power-critical edge vision applications.

</details>

### Asymmetric Factorized Bilinear Operation for Vision Transformer.
- **链接**: [出版页](https://openreview.net/forum?id=MJyqwBVgMs)
- **作者**: Junjie Wu, Qilong Wang, Jiangtao Xie, Pengfei Zhu, Qinghua Hu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025
