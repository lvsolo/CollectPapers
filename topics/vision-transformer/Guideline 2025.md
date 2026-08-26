# Vision Transformer — 2025 Guideline

> 领域: 视觉 Transformer（ViT、混合架构、高效注意力）
> 论文数: 6 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### APHQ-ViT: Post-Training Quantization with Average Perturbation Hessian Based Reconstruction for Vision Transformers.
- **链接**: [arXiv:2504.02508](https://arxiv.org/abs/2504.02508) · 📚 被引 5
- **作者**: Zhuguanyu Wu, Jiayi Zhang, Jiaxin Chen, Jinyang Guo, Di Huang, Yunhong Wang
- **🏷️ 机构**: Beihang University,State Key Laboratory of Virtual Reality Technology and Systems,China, Beihang University,School of Artificial Intelligence,Beijing,China, Beihang University,School of Computer Science and Engineering,Beijing,China
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > Vision Transformers (ViTs) have become one of the most commonly used backbones for vision tasks. Despite their remarkable performance, they often suffer significant accuracy drops when quantized for practical deployment, particularly by post-training quantization (PTQ) under ultra-low bits. Recently, reconstruction-based PTQ methods have shown promising performance in quantizing Convolutional Neural Networks (CNNs). However, they fail when applied to ViTs, primarily due to the inaccurate estimation of output importance and the substantial accuracy degradation in quantizing post-GELU activations. To address these issues, we propose \textbf{APHQ-ViT}, a novel PTQ approach based on importance estimation with Average Perturbation Hessian (APH). Specifically, we first thoroughly analyze the current approximation approaches with Hessian loss, and propose an improved average perturbation Hessian loss. To deal with the quantization of the post-GELU activations, we design an MLP Reconstruction (MR) method by replacing the GELU function in MLP with ReLU and reconstructing it by the APH loss on a small unlabeled calibration set. Extensive experiments demonstrate that APHQ-ViT using linear quantizers outperforms existing PTQ methods by substantial margins in 3-bit and 4-bit across different vision tasks. The source code is available at https://github.com/GoatWu/APHQ-ViT.

### Similarity-Guided Layer-Adaptive Vision Transformer for UAV Tracking.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Xue_Similarity-Guided_Layer-Adaptive_Vision_Transformer_for_UAV_Tracking_CVPR_2025_paper.html) · 📚 被引 54
- **作者**: Chaocan Xue, Bineng Zhong, Qihua Liang, Yaozong Zheng, Ning Li, Yuanliang Xue et al.
- **🏷️ 机构**: Guangxi Normal University,Key Laboratory of Education Blockchain and Intelligent Technology, Ministry of Education,Guilin,China,541004, Xi&#x2019;an Research Institute of High Technology,Xi&#x2019;an,China,710025
- **会议**: CVPR 2025

### BHViT: Binarized Hybrid Vision Transformer.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Gao_BHViT_Binarized_Hybrid_Vision_Transformer_CVPR_2025_paper.html) · 📚 被引 31
- **作者**: Tian Gao, Yu Zhang, Zhiyuan Zhang, Huajun Liu, Kaijie Yin, Chengzhong Xu et al.
- **🏷️ 机构**: Nanjing University of Science and Technology, Shanghai Jiaotong University, Singapore Management University
- **会议**: CVPR 2025

### LibraGrad: Balancing Gradient Flow for Universally Better Vision Transformer Attributions.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Mehri_LibraGrad_Balancing_Gradient_Flow_for_Universally_Better_Vision_Transformer_Attributions_CVPR_2025_paper.html) · 📚 被引 1
- **作者**: Faridoun Mehri, Mahdieh Soleymani Baghshah, Mohammad Taher Pilehvar
- **🏷️ 机构**: Sharif University of Technology,Iran, Cardiff University,UK
- **会议**: CVPR 2025

## 跨领域论文（完整笔记在其他领域）

- DeepCompress-ViT: Rethinking Model Compression to Enhance Efficiency of Vision Transformers at the Edge. → [network-pruning](../network-pruning/Guideline%202025.md)
- BOE-ViT: Boosting Orientation Estimation with Equivariance in Self-Supervised 3D Subtomogram Alignment. → [self-supervised-vision](../self-supervised-vision/Guideline%202025.md)
