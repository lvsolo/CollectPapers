# Vision Transformer — 2025 Guideline

> 领域: 视觉 Transformer（ViT、混合架构、高效注意力）
> 论文数: 6 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### APHQ-ViT: Post-Training Quantization with Average Perturbation Hessian Based Reconstruction for Vision Transformers.
- **链接**: [arXiv:2504.02508](https://arxiv.org/abs/2504.02508) · 📚 被引 5
- **作者**: Zhuguanyu Wu, Jiayi Zhang, Jiaxin Chen, Jinyang Guo, Di Huang, Yunhong Wang
- **🏷️ 机构**: Beihang University,State Key Laboratory of Virtual Reality Technology and Systems,China, Beihang University,School of Artificial Intelligence,Beijing,China, Beihang University,School of Computer Science and Engineering,Beijing,China
- **会议**: CVPR 2025

### EA-Vit: Efficient Adaptation for Elastic Vision Transformer.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00104) · 📚 被引 1
- **作者**: Chen Zhu, Wangbo Zhao, Huiwen Zhang, Yuhao Zhou, Weidong Tang, Shuo Wang et al.
- **🏷️ 机构**: National University of Singapore, Xidian University, Houmo AI
- **会议**: ICCV 2025

### Efficient Adaptation of Pre-Trained Vision Transformer Underpinned by Approximately Orthogonal Fine-Tuning Strategy.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00464) · 📚 被引 0
- **作者**: Yiting Yang, Hao Luo, Yuan Sun, Qingsen Yan, Haokui Zhang, Wei Dong et al.
- **🏷️ 机构**: Xi&#x0027;an University of Architecture and Technology, University of Electronic Science and Technology of China, Northwestern Polytechnical University
- **会议**: ICCV 2025

</details>

### Similarity-Guided Layer-Adaptive Vision Transformer for UAV Tracking.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Xue_Similarity-Guided_Layer-Adaptive_Vision_Transformer_for_UAV_Tracking_CVPR_2025_paper.html) · 📚 被引 56
- **作者**: Chaocan Xue, Bineng Zhong, Qihua Liang, Yaozong Zheng, Ning Li, Yuanliang Xue et al.
- **🏷️ 机构**: Guangxi Normal University,Key Laboratory of Education Blockchain and Intelligent Technology, Ministry of Education,Guilin,China,541004, Xi&#x2019;an Research Institute of High Technology,Xi&#x2019;an,China,710025
- **会议**: CVPR 2025

### BHViT: Binarized Hybrid Vision Transformer.
- **链接**: [arXiv:2503.02394](https://arxiv.org/abs/2503.02394) · 📚 被引 32
- **作者**: Tian Gao, Yu Zhang, Zhiyuan Zhang, Huajun Liu, Kaijie Yin, Chengzhong Xu et al.
- **🏷️ 机构**: Nanjing University of Science and Technology, Shanghai Jiaotong University, Singapore Management University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Model binarization has made significant progress in enabling real-time and energy-efficient computation for convolutional neural networks (CNN), offering a potential solution to the deployment challenges faced by Vision Transformers (ViTs) on edge devices. However, due to the structural differences between CNN and Transformer architectures, simply applying binary CNN strategies to the ViT models will lead to a significant performance drop. To tackle this challenge, we propose BHViT, a binarization-friendly hybrid ViT architecture and its full binarization model with the guidance of three important observations. Initially, BHViT utilizes the local information interaction and hierarchical feature aggregation technique from coarse to fine levels to address redundant computations stemming from excessive tokens. Then, a novel module based on shift operations is proposed to enhance the performance of the binary Multilayer Perceptron (MLP) module without significantly increasing computational overhead. In addition, an innovative attention matrix binarization method based on quantization decomposition is proposed to evaluate the token's importance in the binarized attention matrix. Finally, we propose a regularization loss to address the inadequate optimization caused by the incompatibility between the weight oscillation in the binary layers and the Adam Optimizer. Extensive experimental results demonstrate that our proposed algorithm achieves SOTA performance among binary ViT methods.

</details>

### LibraGrad: Balancing Gradient Flow for Universally Better Vision Transformer Attributions.
- **链接**: [arXiv:2411.16760](https://arxiv.org/abs/2411.16760) · 📚 被引 1
- **作者**: Faridoun Mehri, Mahdieh Soleymani Baghshah, Mohammad Taher Pilehvar
- **🏷️ 机构**: Sharif University of Technology,Iran, Cardiff University,UK
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Why do gradient-based explanations struggle with Transformers, and how can we improve them? We identify gradient flow imbalances in Transformers that violate FullGrad-completeness, a critical property for attribution faithfulness that CNNs naturally possess. To address this issue, we introduce LibraGrad -- a theoretically grounded post-hoc approach that corrects gradient imbalances through pruning and scaling of backward paths, without changing the forward pass or adding computational overhead. We evaluate LibraGrad using three metric families: Faithfulness, which quantifies prediction changes under perturbations of the most and least relevant features; Completeness Error, which measures attribution conservation relative to model outputs; and Segmentation AP, which assesses alignment with human perception. Extensive experiments across 8 architectures, 4 model sizes, and 4 datasets show that LibraGrad universally enhances gradient-based methods, outperforming existing white-box methods -- including Transformer-specific approaches -- across all metrics. We demonstrate superior qualitative results through two complementary evaluations: precise text-prompted region highlighting on CLIP models and accurate class discrimination between co-occurring animals on ImageNet-finetuned models -- two settings on which existing methods often struggle. LibraGrad is effective even on the attention-free MLP-Mixer architecture, indicating potential for extension to other modern architectures. Our code is freely available at https://github.com/NightMachinery/LibraGrad.

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Why do gradient-based explanations struggle with Transformers, and how can we improve them? We identify gradient flow imbalances in Transformers that violate FullGrad-completeness, a critical property for attribution faithfulness that CNNs naturally possess. To address this issue, we introduce LibraGrad -- a theoretically grounded post-hoc approach that corrects gradient imbalances through pruning and scaling of backward paths, without changing the forward pass or adding computational overhead. We evaluate LibraGrad using three metric families: Faithfulness, which quantifies prediction changes under perturbations of the most and least relevant features; Completeness Error, which measures attribution conservation relative to model outputs; and Segmentation AP, which assesses alignment with human perception. Extensive experiments across 8 architectures, 4 model sizes, and 4 datasets show that LibraGrad universally enhances gradient-based methods, outperforming existing white-box methods -- including Transformer-specific approaches -- across all metrics. We demonstrate superior qualitative results through two complementary evaluations: precise text-prompted region highlighting on CLIP models and accurate class discrimination between co-occurring animals on ImageNet-finetuned models -- two settings on which existing methods often struggle. LibraGrad is effective even on the attention-free MLP-Mixer architecture, indicating potential for extension to other modern architectures. Our code is freely available at https://github.com/NightMachinery/LibraGrad.

</details>

### Multi-Kernel Correlation-Attention Vision Transformer for Enhanced Contextual Understanding and Multi-Scale Integration.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/65e876f6a98c6799d0b3145966dd73e2-Abstract-Conference.html) · 📚 被引 0
- **作者**: Hongkang Zhang, Shao-Lun Huang, Ercan E. Kuruoglu, Yanlong Wang
- **🏷️ 机构**: Tsinghua University, Tsinghua University, Tsinghua University, Tsinghua-Berkeley Shenzhen Institute
- **会议**: NeurIPS 2025

- DeepCompress-ViT: Rethinking Model Compression to Enhance Efficiency of Vision Transformers at the Edge. → [network-pruning](../network-pruning/Guideline%202025.md)
- BOE-ViT: Boosting Orientation Estimation with Equivariance in Self-Supervised 3D Subtomogram Alignment. → [self-supervised-vision](../self-supervised-vision/Guideline%202025.md)
