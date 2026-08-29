# Vision Transformer — 2025 Guideline

> 领域: 视觉 Transformer（ViT、混合架构、高效注意力）
> 论文数: 6 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Frequency-Aware Token Reduction for Efficient Vision Transformer.
- **链接**: [arXiv:2511.21477](https://arxiv.org/abs/2511.21477) · 📚 被引 0
- **作者**: DongJae Lee, Jiwan Hur, Jaehyun Choi, Jaemyung Yu, Junmo Kim
- **🏷️ 机构**: KAIST, Korea Advanced Institute of Science &amp; Technology, KAIST, Korea Advanced Institute of Science &amp; Technology
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision Transformers have demonstrated exceptional performance across various computer vision tasks, yet their quadratic computational complexity concerning token length remains a significant challenge. To address this, token reduction methods have been widely explored. However, existing approaches often overlook the frequency characteristics of self-attention, such as rank collapsing and over-smoothing phenomenon. In this paper, we propose a frequency-aware token reduction strategy that improves computational efficiency while preserving performance by mitigating rank collapsing. Our method partitions tokens into high-frequency tokens and low-frequency tokens. high-frequency tokens are selectively preserved, while low-frequency tokens are aggregated into a compact direct current token to retain essential low-frequency components. Through extensive experiments and analysis, we demonstrate that our approach significantly improves accuracy while reducing computational overhead and mitigating rank collapsing and over smoothing. Furthermore, we analyze the previous methods, shedding light on their implicit frequency characteristics and limitations.

</details>

### Linear Differential Vision Transformer: Learning Visual Contrasts via Pairwise Differentials.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/5820ad65b1c27411417ae8b59433e580-Abstract-Conference.html) · 📚 被引 3
- **作者**: Yifan Pu, Jixuan Ying, Qixiu Li, Tianzhu Ye, Dongchen Han, Xiaochen Wang et al.
- **🏷️ 机构**: Tsinghua University, Tsinghua University, Microsoft, Microsoft
- **会议**: NeurIPS 2025

### VITRIX-UniViTAR: Unified Vision Transformer with Native Resolution.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/b3bec3f5ad96055b7f60c93edc3606c8-Abstract-Conference.html) · 📚 被引 0
- **作者**: Limeng Qiao, Yiyang Gan, Bairui Wang, Jie Qin, Shuang Xu, Siqi Yang et al.
- **🏷️ 机构**: Meituan, Tianjin University, Shandong University
- **会议**: NeurIPS 2025

### SHF: Symmetrical Hierarchical Forest with Pretrained Vision Transformer Encoder for High-Resolution Medical Segmentation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/cc44bf651235b9cd61c4143ae3bbb0de-Abstract-Conference.html) · 📚 被引 0
- **作者**: Enzhi Zhang, Peng Chen, Rui Zhong, Du Wu, Jun Igarashi, Isaac Lyngaas et al.
- **🏷️ 机构**: Hokkaido University, Institute of Physical and Chemical Research - RIKEN, Zhejiang University, Kuaishou- 快手科技
- **会议**: NeurIPS 2025

### Multi-Kernel Correlation-Attention Vision Transformer for Enhanced Contextual Understanding and Multi-Scale Integration.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/65e876f6a98c6799d0b3145966dd73e2-Abstract-Conference.html) · 📚 被引 0
- **作者**: Hongkang Zhang, Shao-Lun Huang, Ercan E. Kuruoglu, Yanlong Wang
- **🏷️ 机构**: Tsinghua University, Tsinghua University, Tsinghua University, Tsinghua-Berkeley Shenzhen Institute
- **会议**: NeurIPS 2025

### Polyline Path Masked Attention for Vision Transformer.
- **链接**: [arXiv:2506.15940](https://arxiv.org/abs/2506.15940) · 📚 被引 0
- **作者**: Zhongchen Zhao, Chaodong Xiao, Hui Lin, Qi Xie, Lei Zhang, Deyu Meng
- **🏷️ 机构**: Xi'an Jiao Tong University, Hong Kong Polytechnic University, Xi'an Jiaotong University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Global dependency modeling and spatial position modeling are two core issues of the foundational architecture design in current deep learning frameworks. Recently, Vision Transformers (ViTs) have achieved remarkable success in computer vision, leveraging the powerful global dependency modeling capability of the self-attention mechanism. Furthermore, Mamba2 has demonstrated its significant potential in natural language processing tasks by explicitly modeling the spatial adjacency prior through the structured mask. In this paper, we propose Polyline Path Masked Attention (PPMA) that integrates the self-attention mechanism of ViTs with an enhanced structured mask of Mamba2, harnessing the complementary strengths of both architectures. Specifically, we first ameliorate the traditional structured mask of Mamba2 by introducing a 2D polyline path scanning strategy and derive its corresponding structured mask, polyline path mask, which better preserves the adjacency relationships among image tokens. Notably, we conduct a thorough theoretical analysis on the structural characteristics of the proposed polyline path mask and design an efficient algorithm for the computation of the polyline path mask. Next, we embed the polyline path mask into the self-attention mechanism of ViTs, enabling explicit modeling of spatial adjacency prior. Extensive experiments on standard benchmarks, including image classification, object detection, and segmentation, demonstrate that our model outperforms previous state-of-the-art approaches based on both state-space models and Transformers. For example, our proposed PPMA-T/S/B models achieve 48.7%/51.1%/52.3% mIoU on the ADE20K semantic segmentation task, surpassing RMT-T/S/B by 0.7%/1.3%/0.3%, respectively. Code is available at https://github.com/zhongchenzhao/PPMA.

</details>
