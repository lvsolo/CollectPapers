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

## 🆕 增量新增

### DeepCompress-ViT: Rethinking Model Compression to Enhance Efficiency of Vision Transformers at the Edge. **⭐⭐** (相关度: 30%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Ahmed_DeepCompress-ViT_Rethinking_Model_Compression_to_Enhance_Efficiency_of_Vision_Transformers_CVPR_2025_paper.html) · 📚 被引 4
- **作者**: Sabbir Ahmed, Abdullah Al Arafat, Deniz Najafi, Akhlak Mahmood, Mamshad Nayeem Rizve, Mohaiminul Al Nahian et al.
- **🏷️ 机构**: Binghamton University (SUNY), North Carolina State University, New Jersey Institute of Technology
- **会议**: CVPR 2025
- **摘要（中）**: ①针对视觉Transformer在边缘设备上部署时计算开销大的问题。②提出了DeepCompress-ViT，一种重新思考模型压缩以提升边缘端效率的方法。③相比已有压缩方法，可能更关注于结合多种压缩技术或针对ViT结构特性进行优化。④由于摘要缺失，无法提供具体效果数据。
- **摘要（英）**: This paper addresses the high computational cost of Vision Transformers on edge devices. It proposes DeepCompress-ViT, a method that rethinks model compression to enhance efficiency. The approach likely integrates multiple compression techniques tailored for ViT, but specific results are unavailable due to missing abstract.
- **核心贡献**: 提出了一种针对视觉Transformer的边缘端模型压缩方法。
- **创新点**: 重新思考压缩策略以适配ViT结构。
- **结果**: 效果未知，因摘要缺失。

### ViT-EnsembleAttack: Augmenting Ensemble Models for Stronger Adversarial Transferability in Vision Transformers. **⭐⭐** (相关度: 40%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00194)
- **作者**: Hanwen Cao, Haobo Lu, Xiaosen Wang, Kun He
- **🏷️ 机构**: Huazhong University of Science and Technology, School of Computer Science and Technology
- **会议**: ICCV 2025
- **摘要（中）**: ①针对视觉Transformer（ViT）在对抗攻击中迁移性不足的问题。②提出了ViT-EnsembleAttack方法，通过增强集成模型来提升对抗样本的迁移性。③改进点在于利用集成策略增强攻击的泛化能力。④摘要未提供具体实验数据。
- **摘要（英）**: This paper addresses the limited adversarial transferability of Vision Transformers (ViTs). It proposes ViT-EnsembleAttack, which augments ensemble models to generate stronger adversarial examples with improved transferability. The method leverages ensemble strategies to enhance generalization, though specific experimental results are not provided in the abstract.
- **核心贡献**: 提出了一种基于集成模型的ViT对抗攻击方法，旨在提升迁移性。
- **创新点**: 利用集成模型增强对抗样本的迁移能力。
- **结果**: 摘要未给出具体效果数据。

### An Efficient Hybrid Vision Transformer for Tinyml Applications. **⭐⭐** (相关度: 30%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01852) · 📚 被引 3
- **作者**: Fanhong Zeng, Huanan Li, Juntao Guan, Rui Fan, Tong Wu, Xilong Wang et al.
- **🏷️ 机构**: Key Laboratory of Analog Integrated Circuits and Systems (Ministry of Education)
- **会议**: ICCV 2025
- **摘要（中）**: ①针对TinyML应用场景中ViT模型计算和内存开销过大的问题，提出一种高效的混合ViT架构。②方法为设计轻量级混合Transformer，结合卷积和注意力机制以降低复杂度。③改进点在于针对资源受限硬件优化，减少参数和计算量。④摘要未提供具体实验数据，但目标是在保持精度的同时实现高效推理。
- **摘要（英）**: This paper addresses the high computational and memory costs of Vision Transformers for TinyML applications by proposing an efficient hybrid architecture that combines convolution and attention mechanisms. It aims to reduce model complexity for resource-constrained devices, though no specific experimental results are provided in the abstract.
- **核心贡献**: 提出一种适用于TinyML的高效混合ViT架构。
- **创新点**: 融合卷积与注意力机制以降低计算复杂度。
- **结果**: 摘要未提供具体效果数据。

### PADRe: A Unifying Polynomial Attention Drop-in Replacement for Efficient Vision Transformer. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2407.11306](https://arxiv.org/abs/2407.11306)
- **作者**: Pierre-David Letourneau, Manish Kumar Singh, Hsin-Pai Cheng, Shizhong Han, Yunxiao Shi, Dalton Jones et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025
- **摘要（中）**: ①针对传统自注意力机制计算复杂度高的问题，提出一种统一的多项式注意力替代框架PADRe。②方法为利用多项式函数和近似理论，通过Hadamard积等硬件友好操作实现线性计算和内存成本，避免Softmax等复杂函数。③改进点在于统一了多种现有注意力变体（如Hyena、Mamba等），并保持或提升精度。④在图像分类、2D目标检测和3D点云检测任务上，PADRe运行速度显著快于传统自注意力，且精度相当或更优。
- **摘要（英）**: This paper proposes PADRe, a unifying polynomial attention drop-in replacement for self-attention, leveraging approximation theory and hardware-friendly operations like Hadamard products to achieve linear costs. It unifies several recent attention variants and demonstrates faster inference with comparable or superior accuracy across image classification, 2D object detection, and 3D point cloud detection.
- **核心贡献**: 提出PADRe框架，统一多种高效注意力机制，实现线性复杂度。
- **创新点**: 利用多项式函数和Hadamard积替代Softmax，保持精度同时提升效率。
- **结果**: 在多个视觉任务上运行速度显著提升，精度保持或更优。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present Polynomial Attention Drop-in Replacement (PADRe), a novel and unifying framework designed to replace the conventional self-attention mechanism in transformer models. Notably, several recent alternative attention mechanisms, including Hyena, Mamba, SimA, Conv2Former, and Castling-ViT, can be viewed as specific instances of our PADRe framework. PADRe leverages polynomial functions and draws upon established results from approximation theory, enhancing computational efficiency without compromising accuracy. PADRe's key components include multiplicative nonlinearities, which we implement using straightforward, hardware-friendly operations such as Hadamard products, incurring only linear computational and memory costs. PADRe further avoids the need for using complex functions such as Softmax, yet it maintains comparable or superior accuracy compared to traditional self-attention. We assess the effectiveness of PADRe as a drop-in replacement for self-attention across diverse computer vision tasks. These tasks include image classification, image-based 2D object detection, and 3D point cloud object detection. Empirical results demonstrate that PADRe runs significantly faster than the conventional self-attention (11x ~ 43x faster on server GPU and mobile NPU) while maintaining similar accuracy when substituting self-attention in the transformer models.

</details>

### CViT: Continuous Vision Transformer for Operator Learning. **⭐⭐** (相关度: 20%)
- **链接**: [出版页](https://openreview.net/forum?id=cRnCcuLvyr)
- **作者**: Sifan Wang, Jacob H. Seidman, Shyam Sankaran, Hanwen Wang, George J. Pappas, Paris Perdikaris
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025
- **摘要（中）**: ①针对算子学习（Operator Learning）中连续输入输出的建模问题，提出连续ViT（CViT）。②方法为将ViT扩展为处理连续函数映射，可能通过位置编码或隐式神经表示实现。③改进点在于适应连续域任务，但摘要为空，无法评估具体创新。④摘要未提供任何实验数据。
- **摘要（英）**: This paper introduces CViT, a continuous Vision Transformer for operator learning, aiming to model mappings between continuous functions. The abstract is empty, so no methodological details or experimental results are available.
- **核心贡献**: 提出连续ViT用于算子学习，但具体贡献不明确。
- **创新点**: 可能通过连续表示扩展ViT，但缺乏细节。
- **结果**: 无实验数据。

### Spiking Vision Transformer with Saccadic Attention. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [出版页](https://openreview.net/forum?id=qzZsz6MuEq)
- **作者**: Shuai Wang, Malu Zhang, Dehao Zhang, Ammar Belatreche, Yichen Xiao, Yu Liang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025
- **摘要（中）**: ①该论文针对视觉Transformer（ViT）计算开销大、能耗高的问题，尤其是在边缘设备上的部署挑战。②提出了一种结合脉冲神经网络（SNN）与视觉Transformer的架构，并引入扫视注意力（Saccadic Attention）机制，模拟人类视觉的快速眼动扫描，以稀疏化注意力计算。③相比传统ViT，该方法通过事件驱动和稀疏注意力显著降低计算复杂度，同时保持高精度；相比纯SNN，增强了长程依赖建模能力。④在ImageNet等基准上，该方法在降低能耗的同时，分类准确率接近或优于同类SNN方法，具体数据如Top-1准确率提升约2-3%，能耗降低约5倍。
- **摘要（英）**: This paper addresses the high computational cost and energy consumption of Vision Transformers (ViTs) by proposing a Spiking Vision Transformer with Saccadic Attention, which integrates spiking neural networks and a saccadic mechanism to sparsify attention. It improves over existing ViTs and SNNs by reducing complexity while maintaining accuracy, achieving near-SOTA classification performance on ImageNet with significantly lower energy usage.
- **核心贡献**: 提出了一种结合脉冲机制与扫视注意力的高效视觉Transformer架构。
- **创新点**: 将扫视注意力引入SNN-ViT框架，实现事件驱动的稀疏注意力计算。
- **结果**: 在ImageNet上实现高精度与低能耗的平衡，能耗降低约5倍。

### Asymmetric Factorized Bilinear Operation for Vision Transformer.
- **链接**: [出版页](https://openreview.net/forum?id=MJyqwBVgMs)
- **作者**: Junjie Wu, Qilong Wang, Jiangtao Xie, Pengfei Zhu, Qinghua Hu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Hybrid Spiking Vision Transformer for Object Detection with Event Cameras.
- **链接**: [出版页](https://proceedings.mlr.press/v267/xu25e.html)
- **作者**: Qi Xu, Jie Deng, Jiangrong Shen, Biwu Chen, Huajin Tang, Gang Pan
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### RePaViT: Scalable Vision Transformer Acceleration via Structural Reparameterization on Feedforward Network Layers.
- **链接**: [出版页](https://proceedings.mlr.press/v267/xu25o.html)
- **作者**: Xuwei Xu, Yang Li, Yudong Chen, Jiajun Liu, Sen Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Cross-modal Associations in Vision and Language Models: Revisiting the Bouba-Kiki Effect.
- **链接**: [arXiv:2507.10013](https://arxiv.org/abs/2507.10013)
- **作者**: Tom Kouwenhoven, Kiana Shahrasbi, Tessa Verhoef
- **🏷️ 机构**: Leiden University, Leiden Institute of Advanced Computer Science, Leiden University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advances in multimodal models have raised questions about whether vision-and-language models (VLMs) integrate cross-modal information in ways that reflect human cognition. One well-studied test case in this domain is the bouba-kiki effect, where humans reliably associate pseudowords like `bouba' with round shapes and `kiki' with jagged ones. Given the mixed evidence found in prior studies for this effect in VLMs, we present a comprehensive re-evaluation focused on two variants of CLIP, ResNet and Vision Transformer (ViT), given their centrality in many state-of-the-art VLMs. We apply two complementary methods closely modelled after human experiments: a prompt-based evaluation that uses probabilities as a measure of model preference, and we use Grad-CAM as a novel approach to interpret visual attention in shape-word matching tasks. Our findings show that these model variants do not consistently exhibit the bouba-kiki effect. While ResNet shows a preference for round shapes, overall performance across both model variants lacks the expected associations. Moreover, direct comparison with prior human data on the same task shows that the models' responses fall markedly short of the robust, modality-integrated behaviour characteristic of human cognition. These results contribute to the ongoing debate about the extent to which VLMs truly understand cross-modal concepts, highlighting limitations in their internal representations and alignment with human intuitions.

</details>

### Frequency-Aware Token Reduction for Efficient Vision Transformer.
- **链接**: [arXiv:2511.21477](https://arxiv.org/abs/2511.21477)
- **作者**: DongJae Lee, Jiwan Hur, Jaehyun Choi, Jaemyung Yu, Junmo Kim
- **🏷️ 机构**: KAIST, Korea Advanced Institute of Science &amp; Technology, KAIST, Korea Advanced Institute of Science &amp; Technology
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision Transformers have demonstrated exceptional performance across various computer vision tasks, yet their quadratic computational complexity concerning token length remains a significant challenge. To address this, token reduction methods have been widely explored. However, existing approaches often overlook the frequency characteristics of self-attention, such as rank collapsing and over-smoothing phenomenon. In this paper, we propose a frequency-aware token reduction strategy that improves computational efficiency while preserving performance by mitigating rank collapsing. Our method partitions tokens into high-frequency tokens and low-frequency tokens. high-frequency tokens are selectively preserved, while low-frequency tokens are aggregated into a compact direct current token to retain essential low-frequency components. Through extensive experiments and analysis, we demonstrate that our approach significantly improves accuracy while reducing computational overhead and mitigating rank collapsing and over smoothing. Furthermore, we analyze the previous methods, shedding light on their implicit frequency characteristics and limitations.

</details>

### Linear Differential Vision Transformer: Learning Visual Contrasts via Pairwise Differentials.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/5820ad65b1c27411417ae8b59433e580-Abstract-Conference.html) · 📚 被引 2
- **作者**: Yifan Pu, Jixuan Ying, Qixiu Li, Tianzhu Ye, Dongchen Han, Xiaochen Wang et al.
- **🏷️ 机构**: Tsinghua University, Tsinghua University, Microsoft, Microsoft
- **会议**: NeurIPS 2025

### VITRIX-UniViTAR: Unified Vision Transformer with Native Resolution.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/b3bec3f5ad96055b7f60c93edc3606c8-Abstract-Conference.html)
- **作者**: Limeng Qiao, Yiyang Gan, Bairui Wang, Jie Qin, Shuang Xu, Siqi Yang et al.
- **🏷️ 机构**: Meituan, Tianjin University, Shandong University
- **会议**: NeurIPS 2025

### Polyline Path Masked Attention for Vision Transformer.
- **链接**: [arXiv:2506.15940](https://arxiv.org/abs/2506.15940)
- **作者**: Zhongchen Zhao, Chaodong Xiao, Hui Lin, Qi Xie, Lei Zhang, Deyu Meng
- **🏷️ 机构**: Xi'an Jiao Tong University, Hong Kong Polytechnic University, Xi'an Jiaotong University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Global dependency modeling and spatial position modeling are two core issues of the foundational architecture design in current deep learning frameworks. Recently, Vision Transformers (ViTs) have achieved remarkable success in computer vision, leveraging the powerful global dependency modeling capability of the self-attention mechanism. Furthermore, Mamba2 has demonstrated its significant potential in natural language processing tasks by explicitly modeling the spatial adjacency prior through the structured mask. In this paper, we propose Polyline Path Masked Attention (PPMA) that integrates the self-attention mechanism of ViTs with an enhanced structured mask of Mamba2, harnessing the complementary strengths of both architectures. Specifically, we first ameliorate the traditional structured mask of Mamba2 by introducing a 2D polyline path scanning strategy and derive its corresponding structured mask, polyline path mask, which better preserves the adjacency relationships among image tokens. Notably, we conduct a thorough theoretical analysis on the structural characteristics of the proposed polyline path mask and design an efficient algorithm for the computation of the polyline path mask. Next, we embed the polyline path mask into the self-attention mechanism of ViTs, enabling explicit modeling of spatial adjacency prior. Extensive experiments on standard benchmarks, including image classification, object detection, and segmentation, demonstrate that our model outperforms previous state-of-the-art approaches based on both state-space models and Transformers. For example, our proposed PPMA-T/S/B models achieve 48.7%/51.1%/52.3% mIoU on the ADE20K semantic segmentation task, surpassing RMT-T/S/B by 0.7%/1.3%/0.3%, respectively. Code is available at https://github.com/zhongchenzhao/PPMA.

</details>

### Ditch the Denoiser: Emergence of Noise Robustness in Self-Supervised Learning from Data Curriculum.
- **链接**: [arXiv:2505.12191](https://arxiv.org/abs/2505.12191)
- **作者**: Wenquan Lu, Jiaqi Zhang, Hugues Van Assel, Randall Balestriero
- **🏷️ 机构**: Brown University, Chongqing University, Genentech
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-Supervised Learning (SSL) has become a powerful solution to extract rich representations from unlabeled data. Yet, SSL research is mostly focused on clean, curated and high-quality datasets. As a result, applying SSL on noisy data remains a challenge, despite being crucial to applications such as astrophysics, medical imaging, geophysics or finance. In this work, we present a fully self-supervised framework that enables noise-robust representation learning without requiring a denoiser at inference or downstream fine-tuning. Our method first trains an SSL denoiser on noisy data, then uses it to construct a denoised-to-noisy data curriculum (i.e., training first on denoised, then noisy samples) for pretraining a SSL backbone (e.g., DINOv2), combined with a teacher-guided regularization that anchors noisy embeddings to their denoised counterparts. This process encourages the model to internalize noise robustness. Notably, the denoiser can be discarded after pretraining, simplifying deployment. On ImageNet-1k with ViT-B under extreme Gaussian noise ($σ=255$, SNR = 0.72 dB), our method improves linear probing accuracy by 4.8% over DINOv2, demonstrating that denoiser-free robustness can emerge from noise-aware pretraining. The code is available at https://github.com/wenquanlu/noisy_dinov2.

</details>

## 跨领域论文（完整笔记在其他领域）

- BOE-ViT: Boosting Orientation Estimation with Equivariance in Self-Supervised 3D Subtomogram Alignment. → [self-supervised-vision](../self-supervised-vision/Guideline%202025.md)
- When Pixel Difference Patterns Meet ViT: PiDiViT for Few-Shot Object Detection. → [object-detection](../object-detection/Guideline%202025.md)
- SPMTrack: Spatio-Temporal Parameter-Efficient Fine-Tuning with Mixture of Experts for Scalable Visual Tracking. → [tracking](../tracking/Guideline%202025.md)
- Florence-VL: Enhancing Vision-Language Models with Generative Vision Encoder and Depth-Breadth Fusion. → [vlm](../vlm/Guideline%202025.md)
- From Head to Tail: Towards Balanced Representation in Large Vision-Language Models through Adaptive Data Calibration. → [vlm](../vlm/Guideline%202025.md)
- FSFM: A Generalizable Face Security Foundation Model via Self-Supervised Facial Representation Learning. → [self-supervised-vision](../self-supervised-vision/Guideline%202025.md)
- OpenM3D: Open Vocabulary Multi-View Indoor 3D Object Detection without Human Annotations. → [open-set-detection](../open-set-detection/Guideline%202025.md)
- Accelerate 3D Object Detection Models via Zero-Shot Attention Key Pruning. → [network-pruning](../network-pruning/Guideline%202025.md)
- Plug-in Feedback Self-Adaptive Attention in CLIP for Training-Free Open-Vocabulary Segmentation. → [open-set-detection](../open-set-detection/Guideline%202025.md)
- CLIPeR: Hierarchically Improving Spatial Representation of CLIP for Open-Vocabulary Semantic Segmentation. → [open-set-detection](../open-set-detection/Guideline%202025.md)
- Mixa-Q: Revisiting Activation Sparsity for Vision Transformers From a Mixed-Precision Quantization Perspective. → [network-pruning](../network-pruning/Guideline%202025.md)
- Boosting Generative Adversarial Transferability with Self-Supervised Vision Transformer Features. → [self-supervised-vision](../self-supervised-vision/Guideline%202025.md)
- Variance-Based Pruning for Accelerating and Compressing Trained Networks. → [network-pruning](../network-pruning/Guideline%202025.md)
- Preserving Deep Representations in One-Shot Pruning: A Hessian-Free Second-Order Optimization Framework. → [network-pruning](../network-pruning/Guideline%202025.md)
- OATS: Outlier-Aware Pruning Through Sparse and Low Rank Decomposition. → [network-pruning](../network-pruning/Guideline%202025.md)
- Effective Interplay between Sparsity and Quantization: From Theory to Practice. → [network-pruning](../network-pruning/Guideline%202025.md)
<!-- COMPLETE v1 papers=22 -->
