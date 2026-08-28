# Vision Transformer — 2025 Guideline

> 领域: 视觉 Transformer（ViT、混合架构、高效注意力）
> 论文数: 4 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### APHQ-ViT: Post-Training Quantization with Average Perturbation Hessian Based Reconstruction for Vision Transformers.
- **链接**: [arXiv:2504.02508](https://arxiv.org/abs/2504.02508) · 📚 被引 5
- **作者**: Zhuguanyu Wu, Jiayi Zhang, Jiaxin Chen, Jinyang Guo, Di Huang, Yunhong Wang
- **🏷️ 机构**: Beihang University,State Key Laboratory of Virtual Reality Technology and Systems,China, Beihang University,School of Artificial Intelligence,Beijing,China, Beihang University,School of Computer Science and Engineering,Beijing,China
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision Transformers (ViTs) have become one of the most commonly used backbones for vision tasks. Despite their remarkable performance, they often suffer significant accuracy drops when quantized for practical deployment, particularly by post-training quantization (PTQ) under ultra-low bits. Recently, reconstruction-based PTQ methods have shown promising performance in quantizing Convolutional Neural Networks (CNNs). However, they fail when applied to ViTs, primarily due to the inaccurate estimation of output importance and the substantial accuracy degradation in quantizing post-GELU activations. To address these issues, we propose \textbf{APHQ-ViT}, a novel PTQ approach based on importance estimation with Average Perturbation Hessian (APH). Specifically, we first thoroughly analyze the current approximation approaches with Hessian loss, and propose an improved average perturbation Hessian loss. To deal with the quantization of the post-GELU activations, we design an MLP Reconstruction (MR) method by replacing the GELU function in MLP with ReLU and reconstructing it by the APH loss on a small unlabeled calibration set. Extensive experiments demonstrate that APHQ-ViT using linear quantizers outperforms existing PTQ methods by substantial margins in 3-bit and 4-bit across different vision tasks. The source code is available at https://github.com/GoatWu/APHQ-ViT.

</details>

### SHF: Symmetrical Hierarchical Forest with Pretrained Vision Transformer Encoder for High-Resolution Medical Segmentation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/cc44bf651235b9cd61c4143ae3bbb0de-Abstract-Conference.html) · 📚 被引 0
- **作者**: Enzhi Zhang, Peng Chen, Rui Zhong, Du Wu, Jun Igarashi, Isaac Lyngaas et al.
- **🏷️ 机构**: Hokkaido University, Institute of Physical and Chemical Research - RIKEN, Zhejiang University, Kuaishou- 快手科技
- **会议**: NeurIPS 2025

### BHViT: Binarized Hybrid Vision Transformer.
- **链接**: [arXiv:2503.02394](https://arxiv.org/abs/2503.02394) · 📚 被引 32
- **作者**: Tian Gao, Yu Zhang, Zhiyuan Zhang, Huajun Liu, Kaijie Yin, Chengzhong Xu et al.
- **🏷️ 机构**: Nanjing University of Science and Technology, Shanghai Jiaotong University, Singapore Management University
- **会议**: CVPR 2025

### Spiking Vision Transformer with Saccadic Attention.
- **链接**: [出版页](https://openreview.net/forum?id=qzZsz6MuEq)
- **作者**: Shuai Wang, Malu Zhang, Dehao Zhang, Ammar Belatreche, Yichen Xiao, Yu Liang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Why do gradient-based explanations struggle with Transformers, and how can we improve them? We identify gradient flow imbalances in Transformers that violate FullGrad-completeness, a critical property for attribution faithfulness that CNNs naturally possess. To address this issue, we introduce LibraGrad -- a theoretically grounded post-hoc approach that corrects gradient imbalances through pruning and scaling of backward paths, without changing the forward pass or adding computational overhead. We evaluate LibraGrad using three metric families: Faithfulness, which quantifies prediction changes under perturbations of the most and least relevant features; Completeness Error, which measures attribution conservation relative to model outputs; and Segmentation AP, which assesses alignment with human perception. Extensive experiments across 8 architectures, 4 model sizes, and 4 datasets show that LibraGrad universally enhances gradient-based methods, outperforming existing white-box methods -- including Transformer-specific approaches -- across all metrics. We demonstrate superior qualitative results through two complementary evaluations: precise text-prompted region highlighting on CLIP models and accurate class discrimination between co-occurring animals on ImageNet-finetuned models -- two settings on which existing methods often struggle. LibraGrad is effective even on the attention-free MLP-Mixer architecture, indicating potential for extension to other modern architectures. Our code is freely available at https://github.com/NightMachinery/LibraGrad.

</details>

## 跨领域论文（完整笔记在其他领域）

- When Pixel Difference Patterns Meet ViT: PiDiViT for Few-Shot Object Detection. → [object-detection](../object-detection/Guideline%202025.md)
- Boosting Generative Adversarial Transferability with Self-Supervised Vision Transformer Features. → [self-supervised-vision](../self-supervised-vision/Guideline%202025.md)
