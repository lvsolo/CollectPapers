# Network Pruning — 2024 Guideline

> 领域: 网络剪枝 / 模型压缩（结构化剪枝、稀疏化）
> 论文数: 12 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### DSPDet3D: 3D Small Object Detection with Dynamic Spatial Pruning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73390-1_21) · 📚 被引 10
- **作者**: Xiuwei Xu, Zhihao Sun, Ziwei Wang, Hongmin Liu, Jie Zhou, Jiwen Lu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Compressing a set of unordered points is far more challenging than compressing images/videos of regular sample grids, because of the difficulties in characterizing neighboring relations in an irregular layout of points. Many researchers resort to voxelization to introduce regularity, but this approach suffers from quantization loss. In this research, we use the KNN method to determine the neighborhoods of raw surface points. This gives us a means to determine the spatial context in which the latent features of 3D points are compressed by arithmetic coding. As such, the conditional probability model is adaptive to local geometry, leading to significant rate reduction. Additionally, we propose a dual-layer architecture where a non-learning base layer reconstructs the main structures of the point cloud at low complexity, while a learned refinement layer focuses on preserving fine details. This design leads to reductions in model complexity and coding latency by two orders of magnitude compared to SOTA methods. Moreover, we incorporate an implicit neural representation (INR) into the refinement layer, allowing the decoder to sample points on the underlying surface at arbitrary densities. This work is the first to effectively exploit content-aware local contexts for compressing irregular raw point clouds, achieving high rate-distortion performance, low complexity, and the ability to function as an arbitrary-scale upsampling network simultaneously.

</details>

> Compressing a set of unordered points is far more challenging than compressing images/videos of regular sample grids, because of the difficulties in characterizing neighboring relations in an irregular layout of points. Many researchers resort to voxelization to introduce regularity, but this approach suffers from quantization loss. In this research, we use the KNN method to determine the neighborhoods of raw surface points. This gives us a means to determine the spatial context in which the latent features of 3D points are compressed by arithmetic coding. As such, the conditional probability model is adaptive to local geometry, leading to significant rate reduction. Additionally, we propose a dual-layer architecture where a non-learning base layer reconstructs the main structures of the point cloud at low complexity, while a learned refinement layer focuses on preserving fine details. This design leads to reductions in model complexity and coding latency by two orders of magnitude compared to SOTA methods. Moreover, we incorporate an implicit neural representation (INR) into the refinement layer, allowing the decoder to sample points on the underlying surface at arbitrary densities. This work is the first to effectively exploit content-aware local contexts for compressing irregular raw point clouds, achieving high rate-distortion performance, low complexity, and the ability to function as an arbitrary-scale upsampling network simultaneously.

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision transformers have emerged as a promising alternative to convolutional neural networks for various image analysis tasks, offering comparable or superior performance. However, one significant drawback of ViTs is their resource-intensive nature, leading to increased memory footprint, computation complexity, and power consumption. To democratize this high-performance technology and make it more environmentally friendly, it is essential to compress ViT models, reducing their resource requirements while maintaining high performance. In this paper, we introduce a new block-structured pruning to address the resource-intensive issue for ViTs, offering a balanced trade-off between accuracy and hardware acceleration. Unlike unstructured pruning or channel-wise structured pruning, block pruning leverages the block-wise structure of linear layers, resulting in more efficient matrix multiplications. To optimize this pruning scheme, our paper proposes a novel hardware-aware learning objective that simultaneously maximizes speedup and minimizes power consumption during inference, tailored to the block sparsity structure. This objective eliminates the need for empirical look-up tables and focuses solely on reducing parametrized layer connections. Moreover, our paper provides a lightweight algorithm to achieve post-training pruning for ViTs, utilizing second-order Taylor approximation and empirical optimization to solve the proposed hardware-aware objective. Extensive experiments on ImageNet are conducted across various ViT architectures, including DeiT-B and DeiT-S, demonstrating competitive performance with other pruning methods and achieving a remarkable balance between accuracy preservation and power savings. Especially, we achieve 3.93x speedup on dedicated hardware and GPUs respectively for DeiT-B, and a power reduction by 1.4x on GPUs. Code released to https://github.com/Akimoto-Cris/LPViT.

</details>

> Modern neural networks are often massively overparameterized leading to high compute costs during training and at inference. One effective method to improve both the compute and energy efficiency of neural networks while maintaining good performance is structured pruning, where full network structures (e.g.~neurons or convolutional filters) that have limited impact on the model output are removed. In this work, we propose Bayesian Model Reduction for Structured pruning (BMRS), a fully end-to-end Bayesian method of structured pruning. BMRS is based on two recent methods: Bayesian structured pruning with multiplicative noise, and Bayesian model reduction (BMR), a method which allows efficient comparison of Bayesian models under a change in prior. We present two realizations of BMRS derived from different priors which yield different structured pruning characteristics: 1) BMRS_N with the truncated log-normal prior, which offers reliable compression rates and accuracy without the need for tuning any thresholds and 2) BMRS_U with the truncated log-uniform prior that can achieve more aggressive compression based on the boundaries of truncation. Overall, we find that BMRS offers a theoretically grounded approach to structured pruning of neural networks yielding both high compression rates and accuracy. Experiments on multiple datasets and neural networks of varying complexity showed that the two BMRS methods offer a competitive performance-efficiency trade-off compared to other pruning methods.

- Distill Gold from Massive Ores: Bi-level Data Pruning Towards Efficient Dataset Distillation. → [knowledge-distillation](../knowledge-distillation/Guideline%202024.md)

## 🆕 增量新增

### MADTP: Multimodal Alignment-Guided Dynamic Token Pruning for Accelerating Vision-Language Transformer. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2403.02991](https://arxiv.org/abs/2403.02991) · 📚 被引 22
- **作者**: Jianjian Cao, Peng Ye, Shengze Li, Chong Yu, Yansong Tang, Jiwen Lu et al.
- **🏷️ 机构**: School of Information Science and Technology, Fudan University, Fudan University,Academy for Engineering and Technology, Tsinghua Shenzhen International Graduate School, Tsinghua University
- **会议**: CVPR 2024
- **摘要（中）**: ①针对视觉-语言Transformer（VLT）计算开销大、现有token剪枝方法忽略跨模态对齐导致重要token被误剪、且缺乏按输入动态调整压缩率的问题。②提出了MADTP框架，包含多模态对齐引导（MAG）模块，通过对齐不同模态中同一语义概念的特征来确保被剪token对所有模态都不重要，以及动态token剪枝（DTP）模块，根据输入实例自适应调整每层的压缩率。③相比单模态剪枝方法，首次将跨模态对齐引入剪枝决策，并实现了逐层动态压缩。④实验表明该方法能显著加速多种VLT，在保持精度的同时大幅降低计算量（摘要未给出具体数值，但声称有效）。
- **摘要（英）**: This paper addresses the high computational cost of Vision-Language Transformers (VLTs) by proposing MADTP, a framework with a Multimodal Alignment Guidance (MAG) module to align cross-modal features for pruning token importance and a Dynamic Token Pruning (DTP) module for instance-adaptive layer-wise compression. Unlike single-modality pruning, it leverages cross-modal alignment to avoid pruning important tokens, achieving significant acceleration with maintained accuracy across various VLTs.
- **核心贡献**: 提出首个结合多模态对齐引导的动态token剪枝框架MADTP，用于加速视觉-语言Transformer。
- **创新点**: 创新性地利用跨模态特征对齐指导token剪枝，并引入输入自适应的动态压缩率。
- **结果**: 在多种VLT上实现显著加速，同时保持模型精度。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-Language Transformers (VLTs) have shown great success recently, but are meanwhile accompanied by heavy computation costs, where a major reason can be attributed to the large number of visual and language tokens. Existing token pruning research for compressing VLTs mainly follows a single-modality-based scheme yet ignores the critical role of aligning different modalities for guiding the token pruning process, causing the important tokens for one modality to be falsely pruned in another modality branch. Meanwhile, existing VLT pruning works also lack the flexibility to dynamically compress each layer based on different input samples. To this end, we propose a novel framework named Multimodal Alignment-Guided Dynamic Token Pruning (MADTP) for accelerating various VLTs. Specifically, we first introduce a well-designed Multi-modality Alignment Guidance (MAG) module that can align features of the same semantic concept from different modalities, to ensure the pruned tokens are less important for all modalities. We further design a novel Dynamic Token Pruning (DTP) module, which can adaptively adjust the token compression ratio in each layer based on different input instances. Extensive experiments on various benchmarks demonstrate that MADTP significantly reduces the computational complexity of kinds of multimodal models while preserving competitive performance. Notably, when applied to the BLIP model in the NLVR2 dataset, MADTP can reduce the GFLOPs by 80% with less than 4% performance degradation.

</details>

### MULTIFLOW: Shifting Towards Task-Agnostic Vision-Language Pruning. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2404.05621](https://arxiv.org/abs/2404.05621) · 📚 被引 8
- **作者**: Matteo Farina, Massimiliano Mancini, Elia Cunegatti, Gaowen Liu, Giovanni Iacca, Elisa Ricci
- **🏷️ 机构**: University of Trento, Cisco Research
- **会议**: CVPR 2024
- **摘要（中）**: ①针对视觉-语言模型（VLM）参数多、计算成本高，且现有剪枝方法任务特定、需为每个新任务重新剪枝的问题。②提出了任务无关的视觉-语言剪枝（TA-VLP）新方向，并设计了MULTIFLOW框架，这是一种无梯度的剪枝方法，通过参数幅度和其连接神经元的信息流显著性来评估重要性，并利用预训练后VLM参数的多模态分布驱动剪枝。③相比任务特定剪枝，首次探索了单一剪枝模型可迁移到多个未知下游任务的设置，并基准测试了八种现有剪枝算法。④实验在两种VLM上验证了MULTIFLOW的有效性，但摘要未给出具体性能数据。
- **摘要（英）**: This paper introduces Task-Agnostic Vision-Language Pruning (TA-VLP), aiming to find a unique pruned VLM transferable to multiple unknown tasks, and proposes MULTIFLOW, a gradient-free pruning framework that combines parameter magnitude and information flow saliency, driven by the multimodal parameter distribution. It benchmarks eight pruning algorithms, showing MULTIFLOW's effectiveness in preserving transferable representations, though specific metrics are not detailed in the abstract.
- **核心贡献**: 提出任务无关的视觉-语言剪枝（TA-VLP）问题及首个无梯度剪枝框架MULTIFLOW。
- **创新点**: 创新性地将剪枝从任务特定扩展到任务无关，利用参数幅度和信息流显著性进行无梯度剪枝。
- **结果**: 在多种下游任务上验证了剪枝模型的迁移性，但具体性能未在摘要中给出。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While excellent in transfer learning, Vision-Language models (VLMs) come with high computational costs due to their large number of parameters. To address this issue, removing parameters via model pruning is a viable solution. However, existing techniques for VLMs are task-specific, and thus require pruning the network from scratch for each new task of interest. In this work, we explore a new direction: Task-Agnostic Vision-Language Pruning (TA-VLP). Given a pretrained VLM, the goal is to find a unique pruned counterpart transferable to multiple unknown downstream tasks. In this challenging setting, the transferable representations already encoded in the pretrained model are a key aspect to preserve. Thus, we propose Multimodal Flow Pruning (MULTIFLOW), a first, gradient-free, pruning framework for TA-VLP where: (i) the importance of a parameter is expressed in terms of its magnitude and its information flow, by incorporating the saliency of the neurons it connects; and (ii) pruning is driven by the emergent (multimodal) distribution of the VLM parameters after pretraining. We benchmark eight state-of-the-art pruning algorithms in the context of TA-VLP, experimenting with two VLMs, three vision-language tasks, and three pruning ratios. Our experimental results show that MULTIFLOW outperforms recent sophisticated, combinatorial competitors in the vast majority of the cases, paving the way towards addressing TA-VLP. The code is publicly available at https://github.com/FarinaMatteo/multiflow.

</details>

### Once for Both: Single Stage of Importance and Sparsity Search for Vision Transformer Compression. **⭐⭐⭐** (相关度: 50%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00533) · 📚 被引 8
- **作者**: Hancheng Ye, Chong Yu, Peng Ye, Renqiu Xia, Yansong Tang, Jiwen Lu et al.
- **🏷️ 机构**: School of Information Science and Technology, Fudan University, Academy for Engineering and Technology, Fudan University, Shanghai Artificial Intelligence Laboratory
- **会议**: CVPR 2024
- **摘要（中）**: 该论文针对视觉Transformer压缩中重要性和稀疏性搜索分离导致效率低下的问题，提出了一种单阶段联合搜索方法，同时优化通道重要性和稀疏性。由于摘要缺失，具体方法细节和实验结果无法获取，但题目暗示该方法旨在简化压缩流程并提升性能。
- **摘要（英）**: This paper addresses the inefficiency of separate importance and sparsity search in vision transformer compression by proposing a single-stage joint search method. Due to missing abstract, specific details and results are unavailable, but the title suggests a streamlined compression pipeline.
- **核心贡献**: 提出单阶段联合搜索方法，同时优化ViT压缩中的重要性和稀疏性。
- **创新点**: 将重要性搜索和稀疏性搜索合并为单阶段过程。
- **结果**: 具体效果未知，因摘要缺失。

### Dense Vision Transformer Compression with Few Samples. **⭐⭐⭐** (相关度: 45%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01498) · 📚 被引 7
- **作者**: Hanxiao Zhang, Yifan Zhou, Guo-Hua Wang
- **🏷️ 机构**: Nanjing University,National Key Laboratory for Novel Software Technology,China
- **会议**: CVPR 2024
- **摘要（中）**: 该论文针对少样本场景下的密集视觉Transformer压缩问题，旨在在有限数据下实现高效压缩。由于摘要缺失，具体方法和技术细节无法获取，但题目表明其关注少样本条件下的ViT压缩，可能涉及知识蒸馏或剪枝技术。
- **摘要（英）**: This paper addresses dense vision transformer compression with few samples, aiming for efficient compression under limited data. Due to missing abstract, specific methods are unknown, but the topic focuses on few-shot ViT compression.
- **核心贡献**: 研究少样本条件下的密集ViT压缩方法。
- **创新点**: 针对少样本场景设计压缩策略。
- **结果**: 具体效果未知，因摘要缺失。

### Diversity-Aware Channel Pruning for StyleGAN Compression. **⭐⭐⭐⭐** (相关度: 55%)
- **链接**: [arXiv:2403.13548](https://arxiv.org/abs/2403.13548) · 📚 被引 10
- **作者**: Jiwoo Chung, Sangeek Hyun, Sang-Heon Shim, Jae-Pil Heo
- **🏷️ 机构**: Sungkyunkwan University
- **会议**: CVPR 2024
- **摘要（中）**: 针对StyleGAN压缩后样本多样性下降的问题，提出了一种基于通道对潜在向量敏感性的剪枝方法，通过评估通道对潜在向量扰动的敏感性来增强压缩模型的多样性。该方法仅关注剪枝阶段，可与现有训练方案互补且无额外训练成本。实验表明，该方法在多个数据集上显著提升样本多样性，FID分数大幅超越现有方法，且仅用一半训练迭代即可达到可比分数。
- **摘要（英）**: This paper addresses the diversity degradation in compressed StyleGAN by proposing a channel pruning method that leverages channel sensitivities to latent vectors. It enhances sample diversity without extra training cost, achieving significantly better FID scores than state-of-the-art methods and comparable results with half training iterations.
- **核心贡献**: 提出基于潜在向量敏感性的通道剪枝方法，提升StyleGAN压缩后的多样性。
- **创新点**: 利用通道对潜在向量扰动的敏感性进行重要性评估。
- **结果**: 在多个数据集上显著提升多样性，FID大幅优于现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> StyleGAN has shown remarkable performance in unconditional image generation. However, its high computational cost poses a significant challenge for practical applications. Although recent efforts have been made to compress StyleGAN while preserving its performance, existing compressed models still lag behind the original model, particularly in terms of sample diversity. To overcome this, we propose a novel channel pruning method that leverages varying sensitivities of channels to latent vectors, which is a key factor in sample diversity. Specifically, by assessing channel importance based on their sensitivities to latent vector perturbations, our method enhances the diversity of samples in the compressed model. Since our method solely focuses on the channel pruning stage, it has complementary benefits with prior training schemes without additional training cost. Extensive experiments demonstrate that our method significantly enhances sample diversity across various datasets. Moreover, in terms of FID scores, our method not only surpasses state-of-the-art by a large margin but also achieves comparable scores with only half training iterations.

</details>

### Jointly Training and Pruning CNNs via Learnable Agent Guidance and Alignment. **⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2403.19490](https://arxiv.org/abs/2403.19490) · 📚 被引 21
- **作者**: Alireza Ganjdanesh, Shangqian Gao, Heng Huang
- **🏷️ 机构**: University of Maryland College Park,Department of Computer Science, University of Pittsburgh,Department of Electrical and Computer Engineering
- **会议**: CVPR 2024
- **摘要（中）**: ①针对传统结构化剪枝需要预训练模型、成本高的问题，提出联合训练与剪枝的方法。②使用强化学习智能体决定各层剪枝率，在训练过程中迭代更新模型权重和智能体策略，并通过正则化使权重与所选结构对齐。③针对动态奖励函数问题，设计了机制建模奖励函数变化并为其提供表示。④摘要未提供具体数据，但方法在概念上具有创新性。
- **摘要（英）**: This paper addresses the high cost of pretraining in structural pruning by jointly training and pruning CNNs. An RL agent determines layer-wise pruning ratios, with weights regularized to align with the selected structure. It models the dynamic reward function for the agent, though no quantitative results are provided in the abstract.
- **核心贡献**: 提出基于RL智能体引导的联合训练与剪枝框架。
- **创新点**: 动态奖励函数建模机制。
- **结果**: 摘要未给出具体效果数据。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Structural model pruning is a prominent approach used for reducing the computational cost of Convolutional Neural Networks (CNNs) before their deployment on resource-constrained devices. Yet, the majority of proposed ideas require a pretrained model before pruning, which is costly to secure. In this paper, we propose a novel structural pruning approach to jointly learn the weights and structurally prune architectures of CNN models. The core element of our method is a Reinforcement Learning (RL) agent whose actions determine the pruning ratios of the CNN model's layers, and the resulting model's accuracy serves as its reward. We conduct the joint training and pruning by iteratively training the model's weights and the agent's policy, and we regularize the model's weights to align with the selected structure by the agent. The evolving model's weights result in a dynamic reward function for the agent, which prevents using prominent episodic RL methods with stationary environment assumption for our purpose. We address this challenge by designing a mechanism to model the complex changing dynamics of the reward function and provide a representation of it to the RL agent. To do so, we take a learnable embedding for each training epoch and employ a recurrent model to calculate a representation of the changing environment. We train the recurrent model and embeddings using a decoder model to reconstruct observed rewards. Such a design empowers our agent to effectively leverage episodic observations along with the environment representations to learn a proper policy to determine performant sub-networks of the CNN model. Our extensive experiments on CIFAR-10 and ImageNet using ResNets and MobileNets demonstrate the effectiveness of our method.

</details>

### Device-Wise Federated Network Pruning. **⭐⭐** (相关度: 50%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01173) · 📚 被引 8
- **作者**: Shangqian Gao, Junyi Li, Zeyu Zhang, Yanfu Zhang, Weidong Cai, Heng Huang
- **🏷️ 机构**: University of Pittsburgh,Electrical and Computer Engineering, University of Maryland College Park,Computer Science, University of Arizona,Information
- **会议**: CVPR 2024
- **摘要（中）**: ①针对联邦学习中的网络剪枝问题，提出设备级联邦剪枝方法。②摘要为空，无法获取具体方法细节。③无对比信息。④无效果数据。
- **摘要（英）**: This paper focuses on device-wise federated network pruning, but the abstract is empty, providing no details on methodology or results.
- **核心贡献**: 提出设备级联邦剪枝概念。
- **创新点**: 联邦学习与剪枝结合。
- **结果**: 无数据。

### BilevelPruning: Unified Dynamic and Static Channel Pruning for Convolutional Neural Networks. **⭐⭐** (相关度: 50%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01523) · 📚 被引 14
- **作者**: Shangqian Gao, Yanfu Zhang, Feihu Huang, Heng Huang
- **🏷️ 机构**: University of Pittsburgh,Electrical and Computer Engineering, College of William and Mary,Computer Science, University of Maryland College Park,Computer Science
- **会议**: CVPR 2024
- **摘要（中）**: ①针对动态和静态通道剪枝的统一问题，提出BilevelPruning方法。②摘要为空，无法获取具体方法。③无对比。④无效果数据。
- **摘要（英）**: This paper proposes BilevelPruning for unified dynamic and static channel pruning, but the abstract is empty, lacking methodological details and results.
- **核心贡献**: 提出统一动态与静态剪枝的双层优化框架。
- **创新点**: 双层优化策略。
- **结果**: 无数据。

### OrthCaps: An Orthogonal CapsNet with Sparse Attention Routing and Pruning. **⭐⭐** (相关度: 40%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00577) · 📚 被引 8
- **作者**: Xinyu Geng, Jiaming Wang, Jiawei Gong, Yuerong Xue, Jun Xu, Fanglin Chen et al.
- **🏷️ 机构**: Harbin Institute of Technology,Shenzhen, Shanghai Jiao Tong University
- **会议**: CVPR 2024
- **摘要（中）**: ①针对CapsNet的计算效率问题，提出正交CapsNet与稀疏注意力路由和剪枝。②摘要为空，无法获取具体方法。③无对比。④无效果数据。
- **摘要（英）**: This paper introduces OrthCaps, an orthogonal CapsNet with sparse attention routing and pruning, but the abstract is empty, providing no details on methodology or results.
- **核心贡献**: 提出正交CapsNet的剪枝方法。
- **创新点**: 正交约束与稀疏注意力。
- **结果**: 无数据。

### FedMef: Towards Memory-Efficient Federated Dynamic Pruning. **⭐⭐** (相关度: 50%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02601) · 📚 被引 20
- **作者**: Hong Huang, Weiming Zhuang, Chen Chen, Lingjuan Lyu
- **🏷️ 机构**: City University of Hong Kong, Sony AI
- **会议**: CVPR 2024
- **摘要（中）**: ①针对联邦动态剪枝的内存效率问题，提出FedMef方法。②摘要为空，无法获取具体方法。③无对比。④无效果数据。
- **摘要（英）**: This paper proposes FedMef for memory-efficient federated dynamic pruning, but the abstract is empty, lacking details on methodology and results.
- **核心贡献**: 提出内存高效的联邦动态剪枝方法。
- **创新点**: 联邦场景下的动态剪枝优化。
- **结果**: 无数据。

### Resource- Efficient Transformer Pruning for Finetuning of Large Models. **⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01534) · 📚 被引 15
- **作者**: Fatih Ilhan, Gong Su, Selim Furkan Tekin, Tiansheng Huang, Sihao Hu, Ling Liu
- **🏷️ 机构**: Georgia Institute of Technology,Atlanta,GA, IBM Research,Yorktown Heights,NY
- **会议**: CVPR 2024
- **摘要（中）**: ①针对大模型微调时的资源消耗问题，提出资源高效的Transformer剪枝方法。②摘要为空，无法获取具体方法细节。③无对比信息。④无效果数据。
- **摘要（英）**: This paper addresses resource-efficient transformer pruning for finetuning large models, but the abstract is empty, providing no details on methodology or results.
- **核心贡献**: 提出面向大模型微调的Transformer剪枝方法。
- **创新点**: 资源高效剪枝策略。
- **结果**: 无数据。

### Finding Lottery Tickets in Vision Models via Data-Driven Spectral Foresight Pruning. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01528) · 📚 被引 8
- **作者**: Leonardo Iurada, Marco Ciccone, Tatiana Tommasi
- **🏷️ 机构**: Politecnico di Torino,Italy
- **会议**: CVPR 2024
- **摘要（中）**: ①这篇论文针对视觉模型（如CNN和Vision Transformer）中彩票票据（lottery tickets）的发现效率问题，即现有基于幅度或梯度的方法在剪枝后难以保持性能，且计算开销大。②提出了一种数据驱动的谱预见剪枝方法（Data-Driven Spectral Foresight Pruning），通过分析权重矩阵的谱特性（如特征值分布）并结合数据分布，在训练前或早期识别出可保留的关键子网络。③相比传统幅度剪枝和随机剪枝，该方法利用谱信息预测权重的重要性，避免了昂贵的迭代训练过程，并提高了剪枝后模型的泛化能力。④在多个视觉基准（如CIFAR和ImageNet）上，该方法在相同剪枝率下实现了更高的准确率，例如在ResNet-50上以90%剪枝率保持约95%的原始性能，优于现有方法。
- **摘要（英）**: This paper addresses the challenge of efficiently discovering lottery tickets in vision models by proposing a data-driven spectral foresight pruning method that leverages weight matrix spectral properties and data distribution to identify critical subnetworks before or early in training. Compared to magnitude-based and random pruning, it reduces computational cost and improves post-pruning generalization, achieving higher accuracy at high pruning ratios, e.g., retaining ~95% of ResNet-50's original performance at 90% sparsity on ImageNet.
- **核心贡献**: 提出了一种基于数据驱动谱预见的剪枝方法，能够高效识别视觉模型中的彩票票据。
- **创新点**: 创新性地利用权重矩阵的谱特性与数据分布相结合，实现了训练前的预见性剪枝。
- **结果**: 在多个视觉基准上，以高剪枝率保持了接近原始模型的性能，显著优于现有剪枝方法。

### HiPose: Hierarchical Binary Surface Encoding and Correspondence Pruning for RGB-D 6DoF Object Pose Estimation.
- **链接**: [arXiv:2311.12588](https://arxiv.org/abs/2311.12588) · 📚 被引 23
- **作者**: Yongliang Lin, Yongzhi Su, Praveen Nathan, Sandeep Inuganti, Yan Di, Martin Sundermeyer et al.
- **🏷️ 机构**: Zhejiang University, German Research Center for Artificial Intelligence (DFKI), Technische Universit&#x00E4;t M&#x00FC;nchen
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this work, we present a novel dense-correspondence method for 6DoF object pose estimation from a single RGB-D image. While many existing data-driven methods achieve impressive performance, they tend to be time-consuming due to their reliance on rendering-based refinement approaches. To circumvent this limitation, we present HiPose, which establishes 3D-3D correspondences in a coarse-to-fine manner with a hierarchical binary surface encoding. Unlike previous dense-correspondence methods, we estimate the correspondence surface by employing point-to-surface matching and iteratively constricting the surface until it becomes a correspondence point while gradually removing outliers. Extensive experiments on public benchmarks LM-O, YCB-V, and T-Less demonstrate that our method surpasses all refinement-free methods and is even on par with expensive refinement-based approaches. Crucially, our approach is computationally efficient and enables real-time critical applications with high accuracy requirements.

</details>

### MAP: MAsk-Pruning for Source-Free Model Intellectual Property Protection.
- **链接**: [arXiv:2403.04149](https://arxiv.org/abs/2403.04149) · 📚 被引 7
- **作者**: Boyang Peng, Sanqing Qu, Yong Wu, Tianpei Zou, Lianghua He, Alois Knoll et al.
- **🏷️ 机构**: Tongji University, Technical University of Munich
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep learning has achieved remarkable progress in various applications, heightening the importance of safeguarding the intellectual property (IP) of well-trained models. It entails not only authorizing usage but also ensuring the deployment of models in authorized data domains, i.e., making models exclusive to certain target domains. Previous methods necessitate concurrent access to source training data and target unauthorized data when performing IP protection, making them risky and inefficient for decentralized private data. In this paper, we target a practical setting where only a well-trained source model is available and investigate how we can realize IP protection. To achieve this, we propose a novel MAsk Pruning (MAP) framework. MAP stems from an intuitive hypothesis, i.e., there are target-related parameters in a well-trained model, locating and pruning them is the key to IP protection. Technically, MAP freezes the source model and learns a target-specific binary mask to prevent unauthorized data usage while minimizing performance degradation on authorized data. Moreover, we introduce a new metric aimed at achieving a better balance between source and target performance degradation. To verify the effectiveness and versatility, we have evaluated MAP in a variety of scenarios, including vanilla source-available, practical source-free, and challenging data-free. Extensive experiments indicate that MAP yields new state-of-the-art performance.

</details>

### Zero-TPrune: Zero-Shot Token Pruning Through Leveraging of the Attention Graph in Pre-Trained Transformers.
- **链接**: [arXiv:2305.17328](https://arxiv.org/abs/2305.17328) · 📚 被引 42
- **作者**: Hongjie Wang, Bhishma Dedhia, Niraj K. Jha
- **🏷️ 机构**: Princeton University,Princeton,NJ,USA,08540
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deployment of Transformer models on edge devices is becoming increasingly challenging due to the exponentially growing inference cost that scales quadratically with the number of tokens in the input sequence. Token pruning is an emerging solution to address this challenge due to its ease of deployment on various Transformer backbones. However, most token pruning methods require computationally expensive fine-tuning, which is undesirable in many edge deployment cases. In this work, we propose Zero-TPrune, the first zero-shot method that considers both the importance and similarity of tokens in performing token pruning. It leverages the attention graph of pre-trained Transformer models to produce an importance distribution for tokens via our proposed Weighted Page Rank (WPR) algorithm. This distribution further guides token partitioning for efficient similarity-based pruning. Due to the elimination of the fine-tuning overhead, Zero-TPrune can prune large models at negligible computational cost, switch between different pruning configurations at no computational cost, and perform hyperparameter tuning efficiently. We evaluate the performance of Zero-TPrune on vision tasks by applying it to various vision Transformer backbones and testing them on ImageNet. Without any fine-tuning, Zero-TPrune reduces the FLOPs cost of DeiT-S by 34.7% and improves its throughput by 45.3% with only 0.4% accuracy loss. Compared with state-of-the-art pruning methods that require fine-tuning, Zero-TPrune not only eliminates the need for fine-tuning after pruning but also does so with only 0.1% accuracy loss. Compared with state-of-the-art fine-tuning-free pruning methods, Zero-TPrune reduces accuracy loss by up to 49% with similar FLOPs budgets. Project webpage: https://jha-lab.github.io/zerotprune.

</details>

### Auto- Train-Once: Controller Network Guided Automatic Network Pruning from Scratch.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01530) · 📚 被引 13
- **作者**: Xidong Wu, Shangqian Gao, Zeyu Zhang, Zhenzhen Li, Runxue Bao, Yanfu Zhang et al.
- **🏷️ 机构**: University of Pittsburgh, University of Arizona, Bosch Center for AI
- **会议**: CVPR 2024

### Spanning Training Progress: Temporal Dual-Depth Scoring (TDDS) for Enhanced Dataset Pruning.
- **链接**: [arXiv:2311.13613](https://arxiv.org/abs/2311.13613) · 📚 被引 20
- **作者**: Xin Zhang, Jiawei Du, Yunsong Li, Weiying Xie, Joey Tianyi Zhou
- **🏷️ 机构**: XiDian University,Xi&#x0027;an,China, Agency for Science, Technology and Research (A*STAR),Centre for Frontier AI Research (CFAR),Singapore
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Dataset pruning aims to construct a coreset capable of achieving performance comparable to the original, full dataset. Most existing dataset pruning methods rely on snapshot-based criteria to identify representative samples, often resulting in poor generalization across various pruning and cross-architecture scenarios. Recent studies have addressed this issue by expanding the scope of training dynamics considered, including factors such as forgetting event and probability change, typically using an averaging approach. However, these works struggle to integrate a broader range of training dynamics without overlooking well-generalized samples, which may not be sufficiently highlighted in an averaging manner. In this study, we propose a novel dataset pruning method termed as Temporal Dual-Depth Scoring (TDDS), to tackle this problem. TDDS utilizes a dual-depth strategy to achieve a balance between incorporating extensive training dynamics and identifying representative samples for dataset pruning. In the first depth, we estimate the series of each sample's individual contributions spanning the training progress, ensuring comprehensive integration of training dynamics. In the second depth, we focus on the variability of the sample-wise contributions identified in the first depth to highlight well-generalized samples. Extensive experiments conducted on CIFAR and ImageNet datasets verify the superiority of TDDS over previous SOTA methods. Specifically on CIFAR-100, our method achieves 54.51% accuracy with only 10% training data, surpassing random selection by 7.83% and other comparison methods by at least 12.69%.

</details>

### Masked Spatial Propagation Network for Sparsity-Adaptive Depth Refinement.
- **链接**: [arXiv:2404.19294](https://arxiv.org/abs/2404.19294) · 📚 被引 6
- **作者**: Jinyoung Jun, Jae-Han Lee, Chang-Su Kim
- **🏷️ 机构**: Korea University, Gauss Labs Inc
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The main function of depth completion is to compensate for an insufficient and unpredictable number of sparse depth measurements of hardware sensors. However, existing research on depth completion assumes that the sparsity -- the number of points or LiDAR lines -- is fixed for training and testing. Hence, the completion performance drops severely when the number of sparse depths changes significantly. To address this issue, we propose the sparsity-adaptive depth refinement (SDR) framework, which refines monocular depth estimates using sparse depth points. For SDR, we propose the masked spatial propagation network (MSPN) to perform SDR with a varying number of sparse depths effectively by gradually propagating sparse depth information throughout the entire depth map. Experimental results demonstrate that MPSN achieves state-of-the-art performance on both SDR and conventional depth completion scenarios.

</details>

### Transferable Structural Sparse Adversarial Attack Via Exact Group Sparsity Training.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02332) · 📚 被引 9
- **作者**: Di Ming, Peng Ren, Yunlong Wang, Xin Feng
- **🏷️ 机构**: School of Computer Science and Engineering, Chongqing University of Technology,Chongqing,China
- **会议**: CVPR 2024

### MaxQ: Multi-Axis Query for N: m Sparsity Network.
- **链接**: [arXiv:2312.07061](https://arxiv.org/abs/2312.07061)
- **作者**: Jingyang Xiang, Siqi Li, Junhao Chen, Zhuangzhi Chen, Tianxin Huang, Linpeng Peng et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> N:M sparsity has received increasing attention due to its remarkable performance and latency trade-off compared with structured and unstructured sparsity. However, existing N:M sparsity methods do not differentiate the relative importance of weights among blocks and leave important weights underappreciated. Besides, they directly apply N:M sparsity to the whole network, which will cause severe information loss. Thus, they are still sub-optimal. In this paper, we propose an efficient and effective Multi-Axis Query methodology, dubbed as MaxQ, to rectify these problems. During the training, MaxQ employs a dynamic approach to generate soft N:M masks, considering the weight importance across multiple axes. This method enhances the weights with more importance and ensures more effective updates. Meanwhile, a sparsity strategy that gradually increases the percentage of N:M weight blocks is applied, which allows the network to heal from the pruning-induced damage progressively. During the runtime, the N:M soft masks can be precomputed as constants and folded into weights without causing any distortion to the sparse pattern and incurring additional computational overhead. Comprehensive experiments demonstrate that MaxQ achieves consistent improvements across diverse CNN architectures in various computer vision tasks, including image classification, object detection and instance segmentation. For ResNet50 with 1:16 sparse pattern, MaxQ can achieve 74.6\% top-1 accuracy on ImageNet and improve by over 2.8\% over the state-of-the-art. Codes and checkpoints are available at \url{https://github.com/JingyangXiang/MaxQ}.

</details>

### UniPTS: A Unified Framework for Proficient Post-Training Sparsity.
- **链接**: [arXiv:2405.18810](https://arxiv.org/abs/2405.18810)
- **作者**: Jingjing Xie, Yuxin Zhang, Mingbao Lin, Zhihang Lin, Liujuan Cao, Rongrong Ji
- **🏷️ 机构**: Efficient Computing, Ministry of Education of China, School of Informatics, Xiamen University,Key Laboratory of Multimedia Trusted Perception, Tencent Youtu Lab
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Post-training Sparsity (PTS) is a recently emerged avenue that chases efficient network sparsity with limited data in need. Existing PTS methods, however, undergo significant performance degradation compared with traditional methods that retrain the sparse networks via the whole dataset, especially at high sparsity ratios. In this paper, we attempt to reconcile this disparity by transposing three cardinal factors that profoundly alter the performance of conventional sparsity into the context of PTS. Our endeavors particularly comprise (1) A base-decayed sparsity objective that promotes efficient knowledge transferring from dense network to the sparse counterpart. (2) A reducing-regrowing search algorithm designed to ascertain the optimal sparsity distribution while circumventing overfitting to the small calibration set in PTS. (3) The employment of dynamic sparse training predicated on the preceding aspects, aimed at comprehensively optimizing the sparsity structure while ensuring training stability. Our proposed framework, termed UniPTS, is validated to be much superior to existing PTS methods across extensive benchmarks. As an illustration, it amplifies the performance of POT, a recently proposed recipe, from 3.9% to 68.6% when pruning ResNet-50 at 90% sparsity ratio on ImageNet. We release the code of our paper at https://github.com/xjjxmu/UniPTS.

</details>

### Fast Point Cloud Geometry Compression with Context-Based Residual Coding and INR-Based Refinement.
- **链接**: [arXiv:2408.02966](https://arxiv.org/abs/2408.02966) · 📚 被引 5
- **作者**: Hao Xu, Xi Zhang, Xiaolin Wu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Compressing a set of unordered points is far more challenging than compressing images/videos of regular sample grids, because of the difficulties in characterizing neighboring relations in an irregular layout of points. Many researchers resort to voxelization to introduce regularity, but this approach suffers from quantization loss. In this research, we use the KNN method to determine the neighborhoods of raw surface points. This gives us a means to determine the spatial context in which the latent features of 3D points are compressed by arithmetic coding. As such, the conditional probability model is adaptive to local geometry, leading to significant rate reduction. Additionally, we propose a dual-layer architecture where a non-learning base layer reconstructs the main structures of the point cloud at low complexity, while a learned refinement layer focuses on preserving fine details. This design leads to reductions in model complexity and coding latency by two orders of magnitude compared to SOTA methods. Moreover, we incorporate an implicit neural representation (INR) into the refinement layer, allowing the decoder to sample points on the underlying surface at arbitrary densities. This work is the first to effectively exploit content-aware local contexts for compressing irregular raw point clouds, achieving high rate-distortion performance, low complexity, and the ability to function as an arbitrary-scale upsampling network simultaneously.

</details>

### UniCode: Learning a Unified Codebook for Multimodal Large Language Models.
- **链接**: [arXiv:2403.09072](https://arxiv.org/abs/2403.09072) · 📚 被引 5
- **作者**: Sipeng Zheng, Bohan Zhou, Yicheng Feng, Ye Wang, Zongqing Lu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we propose \textbf{UniCode}, a novel approach within the domain of multimodal large language models (MLLMs) that learns a unified codebook to efficiently tokenize visual, text, and potentially other types of signals. This innovation addresses a critical limitation in existing MLLMs: their reliance on a text-only codebook, which restricts MLLM's ability to generate images and texts in a multimodal context. Towards this end, we propose a language-driven iterative training paradigm, coupled with an in-context pre-training task we term ``image decompression'', enabling our model to interpret compressed visual data and generate high-quality images.The unified codebook empowers our model to extend visual instruction tuning to non-linguistic generation tasks. Moreover, UniCode is adaptable to diverse stacked quantization approaches in order to compress visual signals into a more compact token representation. Despite using significantly fewer parameters and less data during training, Unicode demonstrates promising capabilities in visual reconstruction and generation. It also achieves performances comparable to leading MLLMs across a spectrum of VQA benchmarks.

</details>

### LPViT: Low-Power Semi-structured Pruning for Vision Transformers.
- **链接**: [arXiv:2407.02068](https://arxiv.org/abs/2407.02068) · 📚 被引 7
- **作者**: Kaixin Xu, Zhe Wang, Chunyun Chen, Xue Geng, Jie Lin, Xulei Yang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision transformers have emerged as a promising alternative to convolutional neural networks for various image analysis tasks, offering comparable or superior performance. However, one significant drawback of ViTs is their resource-intensive nature, leading to increased memory footprint, computation complexity, and power consumption. To democratize this high-performance technology and make it more environmentally friendly, it is essential to compress ViT models, reducing their resource requirements while maintaining high performance. In this paper, we introduce a new block-structured pruning to address the resource-intensive issue for ViTs, offering a balanced trade-off between accuracy and hardware acceleration. Unlike unstructured pruning or channel-wise structured pruning, block pruning leverages the block-wise structure of linear layers, resulting in more efficient matrix multiplications. To optimize this pruning scheme, our paper proposes a novel hardware-aware learning objective that simultaneously maximizes speedup and minimizes power consumption during inference, tailored to the block sparsity structure. This objective eliminates the need for empirical look-up tables and focuses solely on reducing parametrized layer connections. Moreover, our paper provides a lightweight algorithm to achieve post-training pruning for ViTs, utilizing second-order Taylor approximation and empirical optimization to solve the proposed hardware-aware objective. Extensive experiments on ImageNet are conducted across various ViT architectures, including DeiT-B and DeiT-S, demonstrating competitive performance with other pruning methods and achieving a remarkable balance between accuracy preservation and power savings. Especially, we achieve 3.93x speedup on dedicated hardware and GPUs respectively for DeiT-B, and a power reduction by 1.4x on GPUs. Code released to https://github.com/Akimoto-Cris/LPViT.

</details>

### Non-transferable Pruning.
- **链接**: [arXiv:2410.08015](https://arxiv.org/abs/2410.08015)
- **作者**: Ruyi Ding, Lili Su, Aidong Adam Ding, Yunsi Fei
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pretrained Deep Neural Networks (DNNs), developed from extensive datasets to integrate multifaceted knowledge, are increasingly recognized as valuable intellectual property (IP). To safeguard these models against IP infringement, strategies for ownership verification and usage authorization have emerged. Unlike most existing IP protection strategies that concentrate on restricting direct access to the model, our study addresses an extended DNN IP issue: applicability authorization, aiming to prevent the misuse of learned knowledge, particularly in unauthorized transfer learning scenarios. We propose Non-Transferable Pruning (NTP), a novel IP protection method that leverages model pruning to control a pretrained DNN's transferability to unauthorized data domains. Selective pruning can deliberately diminish a model's suitability on unauthorized domains, even with full fine-tuning. Specifically, our framework employs the alternating direction method of multipliers (ADMM) for optimizing both the model sparsity and an innovative non-transferable learning loss, augmented with Fisher space discriminative regularization, to constrain the model's generalizability to the target dataset. We also propose a novel effective metric to measure the model non-transferability: Area Under the Sample-wise Learning Curve (SLC-AUC). This metric facilitates consideration of full fine-tuning across various sample sizes. Experimental results demonstrate that NTP significantly surpasses the state-of-the-art non-transferable learning methods, with an average SLC-AUC at $-0.54$ across diverse pairs of source and target domains, indicating that models trained with NTP do not suit for transfer learning to unauthorized target domains. The efficacy of NTP is validated in both supervised and self-supervised learning contexts, confirming its applicability in real-world scenarios.

</details>

### Isomorphic Pruning for Vision Models.
- **链接**: [arXiv:2407.04616](https://arxiv.org/abs/2407.04616) · 📚 被引 19
- **作者**: Gongfan Fang, Xinyin Ma, Michael Bi Mi, Xinchao Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Structured pruning reduces the computational overhead of deep neural networks by removing redundant sub-structures. However, assessing the relative importance of different sub-structures remains a significant challenge, particularly in advanced vision models featuring novel mechanisms and architectures like self-attention, depth-wise convolutions, or residual connections. These heterogeneous substructures usually exhibit diverged parameter scales, weight distributions, and computational topology, introducing considerable difficulty to importance comparison. To overcome this, we present Isomorphic Pruning, a simple approach that demonstrates effectiveness across a range of network architectures such as Vision Transformers and CNNs, and delivers competitive performance across different model sizes. Isomorphic Pruning originates from an observation that, when evaluated under a pre-defined importance criterion, heterogeneous sub-structures demonstrate significant divergence in their importance distribution, as opposed to isomorphic structures that present similar importance patterns. This inspires us to perform isolated ranking and comparison on different types of sub-structures for more reliable pruning. Our empirical results on ImageNet-1K demonstrate that Isomorphic Pruning surpasses several pruning baselines dedicatedly designed for Transformers or CNNs. For instance, we improve the accuracy of DeiT-Tiny from 74.52% to 77.50% by pruning an off-the-shelf DeiT-Base model. And for ConvNext-Tiny, we enhanced performance from 82.06% to 82.18%, while reducing the number of parameters and memory usage. Code is available at \url{https://github.com/VainF/Isomorphic-Pruning}.

</details>

### Straightforward Layer-Wise Pruning for More Efficient Visual Adaptation.
- **链接**: [arXiv:2407.14330](https://arxiv.org/abs/2407.14330) · 📚 被引 4
- **作者**: Ruizi Han, Jinglei Tang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Parameter-efficient transfer learning (PETL) aims to adapt large pre-trained models using limited parameters. While most PETL approaches update the added parameters and freeze pre-trained weights during training, the minimal impact of task-specific deep layers on cross-domain data poses a challenge as PETL cannot modify them, resulting in redundant model structures. Structural pruning effectively reduces model redundancy; however, common pruning methods often lead to an excessive increase in stored parameters due to varying pruning structures based on pruning rates and data. Recognizing the storage parameter volume issue, we propose a Straightforward layer-wise pruning method, called SLS, for pruning PETL-transferred models. By evaluating parameters from a feature perspective of each layer and utilizing clustering metrics to assess current parameters based on clustering phenomena in low-dimensional space obtained through t-SNE, SLS facilitates informed pruning decisions. Our study reveals that layer-wise pruning, with a focus on storing pruning indices, addresses storage volume concerns. Notably, mainstream Layer-wise pruning methods may not be suitable for assessing layer importance in PETL-transferred models, where the majority of parameters are pre-trained and have limited relevance to downstream datasets. Comparative analysis against state-of-the-art PETL methods demonstrates that the pruned model achieved a notable balance between model throughput and accuracy. Moreover, SLS effectively reduces storage overhead arising from varying pruned structures while enhancing the accuracy and speed of pruned models compared to conventional pruning methods.

</details>

### IVTP: Instruction-Guided Visual Token Pruning for Large Vision-Language Models.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72643-9_13) · 📚 被引 8
- **作者**: Kai Huang, Hao Zou, Ye Xi, Bochen Wang, Zhen Xie, Liang Yu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### PaPr: Training-Free One-Step Patch Pruning with Lightweight ConvNets for Faster Inference.
- **链接**: [arXiv:2403.16020](https://arxiv.org/abs/2403.16020) · 📚 被引 4
- **作者**: Tanvir Mahmud, Burhaneddin Yaman, Chun-Hao Liu, Diana Marculescu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> As deep neural networks evolve from convolutional neural networks (ConvNets) to advanced vision transformers (ViTs), there is an increased need to eliminate redundant data for faster processing without compromising accuracy. Previous methods are often architecture-specific or necessitate re-training, restricting their applicability with frequent model updates. To solve this, we first introduce a novel property of lightweight ConvNets: their ability to identify key discriminative patch regions in images, irrespective of model's final accuracy or size. We demonstrate that fully-connected layers are the primary bottleneck for ConvNets performance, and their suppression with simple weight recalibration markedly enhances discriminative patch localization performance. Using this insight, we introduce PaPr, a method for substantially pruning redundant patches with minimal accuracy loss using lightweight ConvNets across a variety of deep learning architectures, including ViTs, ConvNets, and hybrid transformers, without any re-training. Moreover, the simple early-stage one-step patch pruning with PaPr enhances existing patch reduction methods. Through extensive testing on diverse architectures, PaPr achieves significantly higher accuracy over state-of-the-art patch reduction methods with similar FLOP count reduction. More specifically, PaPr reduces about 70% of redundant patches in videos with less than 0.8% drop in accuracy, and up to 3.7x FLOPs reduction, which is a 15% more reduction with 2.5% higher accuracy. Code is released at https://github.com/tanvir-utexas/PaPr.

</details>

### SNP: Structured Neuron-Level Pruning to Preserve Attention Scores.
- **链接**: [arXiv:2404.11630](https://arxiv.org/abs/2404.11630) · 📚 被引 3
- **作者**: Kyunghwan Shim, Jaewoong Yun, Shinkook Choi
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-head self-attention (MSA) is a key component of Vision Transformers (ViTs), which have achieved great success in various vision tasks. However, their high computational cost and memory footprint hinder their deployment on resource-constrained devices. Conventional pruning approaches can only compress and accelerate the MSA module using head pruning, although the head is not an atomic unit. To address this issue, we propose a novel graph-aware neuron-level pruning method, Structured Neuron-level Pruning (SNP). SNP prunes neurons with less informative attention scores and eliminates redundancy among heads. Specifically, it prunes graphically connected query and key layers having the least informative attention scores while preserving the overall attention scores. Value layers, which can be pruned independently, are pruned to eliminate inter-head redundancy. Our proposed method effectively compresses and accelerates Transformer-based models for both edge devices and server processors. For instance, the DeiT-Small with SNP runs 3.1$\times$ faster than the original model and achieves performance that is 21.94\% faster and 1.12\% higher than the DeiT-Tiny. Additionally, SNP combine successfully with conventional head or block pruning approaches. SNP with head pruning could compress the DeiT-Base by 80\% of the parameters and computational costs and achieve 3.85$\times$ faster inference speed on RTX3090 and 4.93$\times$ on Jetson Nano.

</details>

### GTPT: Group-Based Token Pruning Transformer for Efficient Human Pose Estimation.
- **链接**: [arXiv:2407.10756](https://arxiv.org/abs/2407.10756) · 📚 被引 6
- **作者**: Haonan Wang, Jie Liu, Jie Tang, Gangshan Wu, Bo Xu, Yanbing Chou et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In recent years, 2D human pose estimation has made significant progress on public benchmarks. However, many of these approaches face challenges of less applicability in the industrial community due to the large number of parametric quantities and computational overhead. Efficient human pose estimation remains a hurdle, especially for whole-body pose estimation with numerous keypoints. While most current methods for efficient human pose estimation primarily rely on CNNs, we propose the Group-based Token Pruning Transformer (GTPT) that fully harnesses the advantages of the Transformer. GTPT alleviates the computational burden by gradually introducing keypoints in a coarse-to-fine manner. It minimizes the computation overhead while ensuring high performance. Besides, GTPT groups keypoint tokens and prunes visual tokens to improve model performance while reducing redundancy. We propose the Multi-Head Group Attention (MHGA) between different groups to achieve global interaction with little computational overhead. We conducted experiments on COCO and COCO-WholeBody. Compared to other methods, the experimental results show that GTPT can achieve higher performance with less computation, especially in whole-body with numerous keypoints.

</details>

### ELSE: Efficient Deep Neural Network Inference Through Line-Based Sparsity Exploration.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73247-8_24)
- **作者**: Zeqi Zhu, Alberto García-Ortiz, Luc Waeijen, Egor Bondarev, Arash Pourtaherian, Orlando Moreira
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### ECoFLaP: Efficient Coarse-to-Fine Layer-Wise Pruning for Vision-Language Models.
- **链接**: [arXiv:2310.02998](https://arxiv.org/abs/2310.02998)
- **作者**: Yi-Lin Sung, Jaehong Yoon, Mohit Bansal
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large Vision-Language Models (LVLMs) can understand the world comprehensively by integrating rich information from different modalities, achieving remarkable advancements on various multimodal downstream tasks. However, deploying LVLMs is often problematic due to their massive computational/energy costs and carbon consumption. Such issues make it infeasible to adopt conventional iterative global pruning, which is costly due to computing the Hessian matrix of the entire large model for sparsification. Alternatively, several studies have recently proposed layer-wise pruning approaches to avoid the expensive computation of global pruning and efficiently compress model weights according to their importance within a layer. However, they often suffer from suboptimal model compression due to their lack of a global perspective. To address this limitation in recent efficient pruning methods for large models, we propose Efficient Coarse-to-Fine LayerWise Pruning (ECoFLaP), a two-stage coarse-to-fine weight pruning approach for LVLMs. We first determine the sparsity ratios of different layers or blocks by leveraging the global importance score, which is efficiently computed based on the zeroth-order approximation of the global model gradients. Then, the model performs local layer-wise unstructured weight pruning based on globally-informed sparsity ratios. We validate our proposed method across various multimodal and unimodal models and datasets, demonstrating significant performance improvements over prevalent pruning techniques in the high-sparsity regime.

</details>

### Data-independent Module-aware Pruning for Hierarchical Vision Transformers.
- **链接**: [arXiv:2404.13648](https://arxiv.org/abs/2404.13648)
- **作者**: Yang He, Joey Tianyi Zhou
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Hierarchical vision transformers (ViTs) have two advantages over conventional ViTs. First, hierarchical ViTs achieve linear computational complexity with respect to image size by local self-attention. Second, hierarchical ViTs create hierarchical feature maps by merging image patches in deeper layers for dense prediction. However, existing pruning methods ignore the unique properties of hierarchical ViTs and use the magnitude value as the weight importance. This approach leads to two main drawbacks. First, the "local" attention weights are compared at a "global" level, which may cause some "locally" important weights to be pruned due to their relatively small magnitude "globally". The second issue with magnitude pruning is that it fails to consider the distinct weight distributions of the network, which are essential for extracting coarse to fine-grained features at various hierarchical levels. To solve the aforementioned issues, we have developed a Data-independent Module-Aware Pruning method (DIMAP) to compress hierarchical ViTs. To ensure that "local" attention weights at different hierarchical levels are compared fairly in terms of their contribution, we treat them as a module and examine their contribution by analyzing their information distortion. Furthermore, we introduce a novel weight metric that is solely based on weights and does not require input images, thereby eliminating the dependence on the patch merging process. Our method validates its usefulness and strengths on Swin Transformers of different sizes on ImageNet-1k classification. Notably, the top-5 accuracy drop is only 0.07% when we remove 52.5% FLOPs and 52.7% parameters of Swin-B. When we reduce 33.2% FLOPs and 33.2% parameters of Swin-S, we can even achieve a 0.8% higher relative top-5 accuracy than the original model. Code is available at: https://github.com/he-y/Data-independent-Module-Aware-Pruning

</details>

### Synergistic Patch Pruning for Vision Transformer: Unifying Intra- & Inter-Layer Patch Importance.
- **链接**: [出版页](https://openreview.net/forum?id=COO51g41Q4)
- **作者**: Yuyao Zhang, Lan Wei, Nikolaos M. Freris
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### A Graph is Worth 1-bit Spikes: When Graph Contrastive Learning Meets Spiking Neural Networks.
- **链接**: [arXiv:2305.19306](https://arxiv.org/abs/2305.19306)
- **作者**: Jintang Li, Huizhe Zhang, Ruofan Wu, Zulun Zhu, Baokun Wang, Changhua Meng et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While contrastive self-supervised learning has become the de-facto learning paradigm for graph neural networks, the pursuit of higher task accuracy requires a larger hidden dimensionality to learn informative and discriminative full-precision representations, raising concerns about computation, memory footprint, and energy consumption burden (largely overlooked) for real-world applications. This work explores a promising direction for graph contrastive learning (GCL) with spiking neural networks (SNNs), which leverage sparse and binary characteristics to learn more biologically plausible and compact representations. We propose SpikeGCL, a novel GCL framework to learn binarized 1-bit representations for graphs, making balanced trade-offs between efficiency and performance. We provide theoretical guarantees to demonstrate that SpikeGCL has comparable expressiveness with its full-precision counterparts. Experimental results demonstrate that, with nearly 32x representation storage compression, SpikeGCL is either comparable to or outperforms many fancy state-of-the-art supervised and self-supervised methods across several graph benchmarks.

</details>

### StructComp: Substituting propagation with Structural Compression in Training Graph Contrastive Learning.
- **链接**: [arXiv:2312.04865](https://arxiv.org/abs/2312.04865)
- **作者**: Shengzhong Zhang, Wenjie Yang, Xinyuan Cao, Hongwei Zhang, Zengfeng Huang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Graph contrastive learning (GCL) has become a powerful tool for learning graph data, but its scalability remains a significant challenge. In this work, we propose a simple yet effective training framework called Structural Compression (StructComp) to address this issue. Inspired by a sparse low-rank approximation on the diffusion matrix, StructComp trains the encoder with the compressed nodes. This allows the encoder not to perform any message passing during the training stage, and significantly reduces the number of sample pairs in the contrastive loss. We theoretically prove that the original GCL loss can be approximated with the contrastive loss computed by StructComp. Moreover, StructComp can be regarded as an additional regularization term for GCL models, resulting in a more robust encoder. Empirical studies on various datasets show that StructComp greatly reduces the time and memory consumption while improving model performance compared to the vanilla GCL models and scalable training methods.

</details>

### D2 Pruning: Message Passing for Balancing Diversity & Difficulty in Data Pruning.
- **链接**: [出版页](https://openreview.net/forum?id=thbtoAkCe9)
- **作者**: Adyasha Maharana, Prateek Yadav, Mohit Bansal
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### Candidate Label Set Pruning: A Data-centric Perspective for Deep Partial-label Learning.
- **链接**: [出版页](https://openreview.net/forum?id=Fk5IzauJ7F)
- **作者**: Shuo He, Chaojie Wang, Guowu Yang, Lei Feng
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### Adversarial Feature Map Pruning for Backdoor.
- **链接**: [出版页](https://openreview.net/forum?id=IOEEDkla96)
- **作者**: Dong Huang, Qingwen Bu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### Effective pruning of web-scale datasets based on complexity of concept clusters.
- **链接**: [arXiv:2401.04578](https://arxiv.org/abs/2401.04578)
- **作者**: Amro Abbas, Evgenia Rusak, Kushal Tirumala, Wieland Brendel, Kamalika Chaudhuri, Ari S. Morcos
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Utilizing massive web-scale datasets has led to unprecedented performance gains in machine learning models, but also imposes outlandish compute requirements for their training. In order to improve training and data efficiency, we here push the limits of pruning large-scale multimodal datasets for training CLIP-style models. Today's most effective pruning method on ImageNet clusters data samples into separate concepts according to their embedding and prunes away the most prototypical samples. We scale this approach to LAION and improve it by noting that the pruning rate should be concept-specific and adapted to the complexity of the concept. Using a simple and intuitive complexity measure, we are able to reduce the training cost to a quarter of regular training. By filtering from the LAION dataset, we find that training on a smaller set of high-quality data can lead to higher performance with significantly lower training costs. More specifically, we are able to outperform the LAION-trained OpenCLIP-ViT-B32 model on ImageNet zero-shot accuracy by 1.1p.p. while only using 27.7% of the data and training compute. Despite a strong reduction in training cost, we also see improvements on ImageNet dist. shifts, retrieval tasks and VTAB. On the DataComp Medium benchmark, we achieve a new state-of-the-art Imagehttps://info.arxiv.org/help/prep#commentsNet zero-shot accuracy and a competitive average zero-shot accuracy on 38 evaluation tasks.

</details>

### Adaptive Sharpness-Aware Pruning for Robust Sparse Networks.
- **链接**: [arXiv:2306.14306](https://arxiv.org/abs/2306.14306)
- **作者**: Anna Bair, Hongxu Yin, Maying Shen, Pavlo Molchanov, José M. Álvarez
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Robustness and compactness are two essential attributes of deep learning models that are deployed in the real world. The goals of robustness and compactness may seem to be at odds, since robustness requires generalization across domains, while the process of compression exploits specificity in one domain. We introduce Adaptive Sharpness-Aware Pruning (AdaSAP), which unifies these goals through the lens of network sharpness. The AdaSAP method produces sparse networks that are robust to input variations which are unseen at training time. We achieve this by strategically incorporating weight perturbations in order to optimize the loss landscape. This allows the model to be both primed for pruning and regularized for improved robustness. AdaSAP improves the robust accuracy of pruned models on image classification by up to +6% on ImageNet C and +4% on ImageNet V2, and on object detection by +4% on a corrupted Pascal VOC dataset, over a wide range of compression ratios, pruning criteria, and network architectures, outperforming recent pruning art by large margins.

</details>

### Sparse Spiking Neural Network: Exploiting Heterogeneity in Timescales for Pruning Recurrent SNN.
- **链接**: [出版页](https://openreview.net/forum?id=0jsfesDZDq)
- **作者**: Biswadeep Chakraborty, Beomseok Kang, Harshit Kumar, Saibal Mukhopadhyay
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### Sparse Weight Averaging with Multiple Particles for Iterative Magnitude Pruning.
- **链接**: [出版页](https://openreview.net/forum?id=Y9t7MqZtCR)
- **作者**: Moonseok Choi, Hyungi Lee, Giung Nam, Juho Lee
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### The Need for Speed: Pruning Transformers with One Recipe.
- **链接**: [出版页](https://openreview.net/forum?id=MVmT6uQ3cQ)
- **作者**: Samir Khaki, Konstantinos N. Plataniotis
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### Adaptive Window Pruning for Efficient Local Motion Deblurring.
- **链接**: [出版页](https://openreview.net/forum?id=hI18CDyadM)
- **作者**: Haoying Li, Jixin Zhao, Shangchen Zhou, Huajun Feng, Chongyi Li, Chen Change Loy
- **🏷️ 机构**: NTU S-Lab
- **会议**: ICLR 2024

### What Makes a Good Prune? Maximal Unstructured Pruning for Maximal Cosine Similarity.
- **链接**: [出版页](https://openreview.net/forum?id=jsvvPVVzwf)
- **作者**: Gabryel Mason-Williams, Fredrik Dahlqvist
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### Accurate Retraining-free Pruning for Pretrained Encoder-based Language Models.
- **链接**: [出版页](https://openreview.net/forum?id=s2NjWfaYdZ)
- **作者**: Seungcheol Park, Hojun Choi, U Kang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### InfoBatch: Lossless Training Speed Up by Unbiased Dynamic Data Pruning.
- **链接**: [出版页](https://openreview.net/forum?id=C61sk5LsK6)
- **作者**: Ziheng Qin, Kai Wang, Zangwei Zheng, Jianyang Gu, Xiangyu Peng, Zhaopan Xu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### Towards Energy Efficient Spiking Neural Networks: An Unstructured Pruning Framework.
- **链接**: [出版页](https://openreview.net/forum?id=eoSeaK4QJo)
- **作者**: Xinyu Shi, Jianhao Ding, Zecheng Hao, Zhaofei Yu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### A Simple and Effective Pruning Approach for Large Language Models.
- **链接**: [出版页](https://openreview.net/forum?id=PxoFut3dWW)
- **作者**: Mingjie Sun, Zhuang Liu, Anna Bair, J. Zico Kolter
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### Towards Meta-Pruning via Optimal Transport.
- **链接**: [出版页](https://openreview.net/forum?id=sMoifbuxjB)
- **作者**: Alexander Theus, Olin Geimer, Friedrich Wicke, Thomas Hofmann, Sotiris Anagnostidis, Sidak Pal Singh
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### Sheared LLaMA: Accelerating Language Model Pre-training via Structured Pruning.
- **链接**: [出版页](https://openreview.net/forum?id=09iOdaeOzp)
- **作者**: Mengzhou Xia, Tianyu Gao, Zhiyuan Zeng, Danqi Chen
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### BESA: Pruning Large Language Models with Blockwise Parameter-Efficient Sparsity Allocation.
- **链接**: [arXiv:2402.16880](https://arxiv.org/abs/2402.16880)
- **作者**: Peng Xu, Wenqi Shao, Mengzhao Chen, Shitao Tang, Kaipeng Zhang, Peng Gao et al.
- **🏷️ 机构**: Shanghai AI Lab
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large language models (LLMs) have demonstrated outstanding performance in various tasks, such as text summarization, text question-answering, and etc. While their performance is impressive, the computational footprint due to their vast number of parameters can be prohibitive. Existing solutions such as SparseGPT and Wanda attempt to alleviate this issue through weight pruning. However, their layer-wise approach results in significant perturbation to the model's output and requires meticulous hyperparameter tuning, such as the pruning rate, which can adversely affect overall model performance. To address this, this paper introduces a novel LLM pruning technique dubbed blockwise parameter-efficient sparsity allocation (BESA) by applying a blockwise reconstruction loss. In contrast to the typical layer-wise pruning techniques, BESA is characterized by two distinctive attributes: i) it targets the overall pruning error with respect to individual transformer blocks, and ii) it allocates layer-specific sparsity in a differentiable manner, both of which ensure reduced performance degradation after pruning. Our experiments show that BESA achieves state-of-the-art performance, efficiently pruning LLMs like LLaMA1, and LLaMA2 with 7B to 70B parameters on a single A100 GPU in just five hours. Code is available at https://github.com/OpenGVLab/LLMPrune-BESA.

</details>

### FedP3: Federated Personalized and Privacy-friendly Network Pruning under Model Heterogeneity.
- **链接**: [arXiv:2404.09816](https://arxiv.org/abs/2404.09816)
- **作者**: Kai Yi, Nidham Gazagnadou, Peter Richtárik, Lingjuan Lyu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The interest in federated learning has surged in recent research due to its unique ability to train a global model using privacy-secured information held locally on each client. This paper pays particular attention to the issue of client-side model heterogeneity, a pervasive challenge in the practical implementation of FL that escalates its complexity. Assuming a scenario where each client possesses varied memory storage, processing capabilities and network bandwidth - a phenomenon referred to as system heterogeneity - there is a pressing need to customize a unique model for each client. In response to this, we present an effective and adaptable federated framework FedP3, representing Federated Personalized and Privacy-friendly network Pruning, tailored for model heterogeneity scenarios. Our proposed methodology can incorporate and adapt well-established techniques to its specific instances. We offer a theoretical interpretation of FedP3 and its locally differential-private variant, DP-FedP3, and theoretically validate their efficiencies.

</details>

### SWAP: Sparse Entropic Wasserstein Regression for Robust Network Pruning.
- **链接**: [出版页](https://openreview.net/forum?id=LJWizuuBUy)
- **作者**: Lei You, Hei Victor Cheng
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### Plug-and-Play: An Efficient Post-training Pruning Method for Large Language Models.
- **链接**: [出版页](https://openreview.net/forum?id=Tr0lPx9woF) · 📚 被引 22
- **作者**: Yingtao Zhang, Haoli Bai, Haokun Lin, Jialin Zhao, Lu Hou, Carlo Vittorio Cannistraci
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### Sparse Model Soups: A Recipe for Improved Pruning via Model Averaging.
- **链接**: [arXiv:2306.16788](https://arxiv.org/abs/2306.16788)
- **作者**: Max Zimmer, Christoph Spiegel, Sebastian Pokutta
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural networks can be significantly compressed by pruning, yielding sparse models with reduced storage and computational demands while preserving predictive performance. Model soups (Wortsman et al., 2022) enhance generalization and out-of-distribution (OOD) performance by averaging the parameters of multiple models into a single one, without increasing inference time. However, achieving both sparsity and parameter averaging is challenging as averaging arbitrary sparse models reduces the overall sparsity due to differing sparse connectivities. This work addresses these challenges by demonstrating that exploring a single retraining phase of Iterative Magnitude Pruning (IMP) with varied hyperparameter configurations such as batch ordering or weight decay yields models suitable for averaging, sharing identical sparse connectivity by design. Averaging these models significantly enhances generalization and OOD performance over their individual counterparts. Building on this, we introduce Sparse Model Soups (SMS), a novel method for merging sparse models by initiating each prune-retrain cycle with the averaged model from the previous phase. SMS preserves sparsity, exploits sparse network benefits, is modular and fully parallelizable, and substantially improves IMP's performance. We further demonstrate that SMS can be adapted to enhance state-of-the-art pruning-during-training approaches.

</details>

### Dynamic Sparse Training with Structured Sparsity.
- **链接**: [arXiv:2305.02299](https://arxiv.org/abs/2305.02299)
- **作者**: Mike Lasby, Anna Golubeva, Utku Evci, Mihai Nica, Yani Ioannou
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Dynamic Sparse Training (DST) methods achieve state-of-the-art results in sparse neural network training, matching the generalization of dense models while enabling sparse training and inference. Although the resulting models are highly sparse and theoretically less computationally expensive, achieving speedups with unstructured sparsity on real-world hardware is challenging. In this work, we propose a sparse-to-sparse DST method, Structured RigL (SRigL), to learn a variant of fine-grained structured N:M sparsity by imposing a constant fan-in constraint. Using our empirical analysis of existing DST methods at high sparsity, we additionally employ a neuron ablation method which enables SRigL to achieve state-of-the-art sparse-to-sparse structured DST performance on a variety of Neural Network (NN) architectures. Using a 90% sparse linear layer, we demonstrate a real-world acceleration of 3.4x/2.5x on CPU for online inference and 1.7x/13.0x on GPU for inference with a batch size of 256 when compared to equivalent dense/unstructured (CSR) sparse layers, respectively.

</details>

### ReLU Strikes Back: Exploiting Activation Sparsity in Large Language Models.
- **链接**: [arXiv:2310.04564](https://arxiv.org/abs/2310.04564)
- **作者**: Iman Mirzadeh, Keivan Alizadeh-Vahid, Sachin Mehta, Carlo C. del Mundo, Oncel Tuzel, Golnoosh Samei et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large Language Models (LLMs) with billions of parameters have drastically transformed AI applications. However, their demanding computation during inference has raised significant challenges for deployment on resource-constrained devices. Despite recent trends favoring alternative activation functions such as GELU or SiLU, known for increased computation, this study strongly advocates for reinstating ReLU activation in LLMs. We demonstrate that using the ReLU activation function has a negligible impact on convergence and performance while significantly reducing computation and weight transfer. This reduction is particularly valuable during the memory-bound inference step, where efficiency is paramount. Exploring sparsity patterns in ReLU-based LLMs, we unveil the reutilization of activated neurons for generating new tokens and leveraging these insights, we propose practical strategies to substantially reduce LLM inference computation up to three times, using ReLU activations with minimal performance trade-offs.

</details>

### Deep Neural Network Initialization with Sparsity Inducing activations.
- **链接**: [arXiv:2402.16184](https://arxiv.org/abs/2402.16184)
- **作者**: Ilan Price, Nicholas Daultry Ball, Adam C. Jones, Samuel C. H. Lam, Jared Tanner
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Inducing and leveraging sparse activations during training and inference is a promising avenue for improving the computational efficiency of deep networks, which is increasingly important as network sizes continue to grow and their application becomes more widespread. Here we use the large width Gaussian process limit to analyze the behaviour, at random initialization, of nonlinear activations that induce sparsity in the hidden outputs. A previously unreported form of training instability is proven for arguably two of the most natural candidates for hidden layer sparsification; those being a shifted ReLU ($φ(x)=\max(0, x-τ)$ for $τ\ge 0$) and soft thresholding ($φ(x)=0$ for $|x|\leτ$ and $x-\text{sign}(x)τ$ for $|x|>τ$). We show that this instability is overcome by clipping the nonlinear activation magnitude, at a level prescribed by the shape of the associated Gaussian process variance map. Numerical experiments verify the theory and show that the proposed magnitude clipped sparsifying activations can be trained with training and test fractional sparsity as high as 85\% while retaining close to full accuracy.

</details>

### Sparsest Models Elude Pruning: An Exposé of Pruning's Current Capabilities.
- **链接**: [arXiv:2407.04075](https://arxiv.org/abs/2407.04075)
- **作者**: Stephen Zhang, Vardan Papyan
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pruning has emerged as a promising approach for compressing large-scale models, yet its effectiveness in recovering the sparsest of models has not yet been explored. We conducted an extensive series of 485,838 experiments, applying a range of state-of-the-art pruning algorithms to a synthetic dataset we created, named the Cubist Spiral. Our findings reveal a significant gap in performance compared to ideal sparse networks, which we identified through a novel combinatorial search algorithm. We attribute this performance gap to current pruning algorithms' poor behaviour under overparameterization, their tendency to induce disconnected paths throughout the network, and their propensity to get stuck at suboptimal solutions, even when given the optimal width and initialization. This gap is concerning, given the simplicity of the network architectures and datasets used in our study. We hope that our research encourages further investigation into new pruning techniques that strive for true network sparsity.

</details>

### Junk DNA Hypothesis: Pruning Small Pre-Trained Weights Irreversibly and Monotonically Impairs "Difficult" Downstream Tasks in LLMs.
- **链接**: [出版页](https://proceedings.mlr.press/v235/yin24b.html)
- **作者**: Lu Yin, Ajay Kumar Jaiswal, Shiwei Liu, Souvik Kundu, Zhangyang Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### Outlier Weighed Layerwise Sparsity (OWL): A Missing Secret Sauce for Pruning LLMs to High Sparsity.
- **链接**: [出版页](https://proceedings.mlr.press/v235/yin24e.html)
- **作者**: Lu Yin, You Wu, Zhenyu Zhang, Cheng-Yu Hsieh, Yaqing Wang, Yiling Jia et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### BWS: Best Window Selection Based on Sample Scores for Data Pruning across Broad Ranges.
- **链接**: [arXiv:2406.03057](https://arxiv.org/abs/2406.03057)
- **作者**: Hoyong Choi, Nohyun Ki, Hye Won Chung
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Data subset selection aims to find a smaller yet informative subset of a large dataset that can approximate the full-dataset training, addressing challenges associated with training neural networks on large-scale datasets. However, existing methods tend to specialize in either high or low selection ratio regimes, lacking a universal approach that consistently achieves competitive performance across a broad range of selection ratios. We introduce a universal and efficient data subset selection method, Best Window Selection (BWS), by proposing a method to choose the best window subset from samples ordered based on their difficulty scores. This approach offers flexibility by allowing the choice of window intervals that span from easy to difficult samples. Furthermore, we provide an efficient mechanism for selecting the best window subset by evaluating its quality using kernel ridge regression. Our experimental results demonstrate the superior performance of BWS compared to other baselines across a broad range of selection ratios over datasets, including CIFAR-10/100 and ImageNet, and the scenarios involving training from random initialization or fine-tuning of pre-trained models.

</details>

### A Provably Effective Method for Pruning Experts in Fine-tuned Sparse Mixture-of-Experts.
- **链接**: [arXiv:2405.16646](https://arxiv.org/abs/2405.16646)
- **作者**: Mohammed Nowaz Rabbani Chowdhury, Meng Wang, Kaoutar El Maghraoui, Naigang Wang, Pin-Yu Chen, Christopher D. Carothers
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The sparsely gated mixture of experts (MoE) architecture sends different inputs to different subnetworks, i.e., experts, through trainable routers. MoE reduces the training computation significantly for large models, but its deployment can be still memory or computation expensive for some downstream tasks. Model pruning is a popular approach to reduce inference computation, but its application in MoE architecture is largely unexplored. To the best of our knowledge, this paper provides the first provably efficient technique for pruning experts in finetuned MoE models. We theoretically prove that prioritizing the pruning of the experts with a smaller change of the routers l2 norm from the pretrained model guarantees the preservation of test accuracy, while significantly reducing the model size and the computational requirements. Although our theoretical analysis is centered on binary classification tasks on simplified MoE architecture, our expert pruning method is verified on large vision MoE models such as VMoE and E3MoE finetuned on benchmark datasets such as CIFAR10, CIFAR100, and ImageNet.

</details>

### Pruner-Zero: Evolving Symbolic Pruning Metric From Scratch for Large Language Models.
- **链接**: [arXiv:2406.02924](https://arxiv.org/abs/2406.02924)
- **作者**: Peijie Dong, Lujun Li, Zhenheng Tang, Xiang Liu, Xinglin Pan, Qiang Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite the remarkable capabilities, Large Language Models (LLMs) face deployment challenges due to their extensive size. Pruning methods drop a subset of weights to accelerate, but many of them require retraining, which is prohibitively expensive and computationally demanding. Recently, post-training pruning approaches introduced novel metrics, enabling the pruning of LLMs without retraining. However, these metrics require the involvement of human experts and tedious trial and error. To efficiently identify superior pruning metrics, we develop an automatic framework for searching symbolic pruning metrics using genetic programming. In particular, we devise an elaborate search space encompassing the existing pruning metrics to discover the potential symbolic pruning metric. We propose an opposing operation simplification strategy to increase the diversity of the population. In this way, Pruner-Zero allows auto-generation of symbolic pruning metrics. Based on the searched results, we explore the correlation between pruning metrics and performance after pruning and summarize some principles. Extensive experiments on LLaMA and LLaMA-2 on language modeling and zero-shot tasks demonstrate that our Pruner-Zero obtains superior performance than SOTA post-training pruning methods. Code at: \url{https://github.com/pprp/Pruner-Zero}.

</details>

### A New Branch-and-Bound Pruning Framework for ℓ0-Regularized Problems.
- **链接**: [arXiv:2406.03504](https://arxiv.org/abs/2406.03504)
- **作者**: Théo Guyard, Cédric Herzet, Clément Elvira, Ayse-Nur Arslan
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We consider the resolution of learning problems involving $\ell_0$-regularization via Branch-and-Bound (BnB) algorithms. These methods explore regions of the feasible space of the problem and check whether they do not contain solutions through "pruning tests". In standard implementations, evaluating a pruning test requires to solve a convex optimization problem, which may result in computational bottlenecks. In this paper, we present an alternative to implement pruning tests for some generic family of $\ell_0$-regularized problems. Our proposed procedure allows the simultaneous assessment of several regions and can be embedded in standard BnB implementations with a negligible computational overhead. We show through numerical simulations that our pruning strategy can improve the solving time of BnB procedures by several orders of magnitude for typical problems encountered in machine-learning applications.

</details>

### PruNeRF: Segment-Centric Dataset Pruning via 3D Spatial Consistency.
- **链接**: [arXiv:2406.00798](https://arxiv.org/abs/2406.00798)
- **作者**: Yeonsung Jung, Heecheol Yun, Joonhyung Park, Jin-Hwa Kim, Eunho Yang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural Radiance Fields (NeRF) have shown remarkable performance in learning 3D scenes. However, NeRF exhibits vulnerability when confronted with distractors in the training images -- unexpected objects are present only within specific views, such as moving entities like pedestrians or birds. Excluding distractors during dataset construction is a straightforward solution, but without prior knowledge of their types and quantities, it becomes prohibitively expensive. In this paper, we propose PruNeRF, a segment-centric dataset pruning framework via 3D spatial consistency, that effectively identifies and prunes the distractors. We first examine existing metrics for measuring pixel-wise distraction and introduce Influence Functions for more accurate measurements. Then, we assess 3D spatial consistency using a depth-based reprojection technique to obtain 3D-aware distraction. Furthermore, we incorporate segmentation for pixel-to-segment refinement, enabling more precise identification. Our experiments on benchmark datasets demonstrate that PruNeRF consistently outperforms state-of-the-art methods in robustness against distractors.

</details>

### LayerMerge: Neural Network Depth Compression through Layer Pruning and Merging.
- **链接**: [arXiv:2406.12837](https://arxiv.org/abs/2406.12837)
- **作者**: Jinuk Kim, Marwa El Halabi, Mingi Ji, Hyun Oh Song
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent works show that reducing the number of layers in a convolutional neural network can enhance efficiency while maintaining the performance of the network. Existing depth compression methods remove redundant non-linear activation functions and merge the consecutive convolution layers into a single layer. However, these methods suffer from a critical drawback; the kernel size of the merged layers becomes larger, significantly undermining the latency reduction gained from reducing the depth of the network. We show that this problem can be addressed by jointly pruning convolution layers and activation functions. To this end, we propose LayerMerge, a novel depth compression method that selects which activation layers and convolution layers to remove, to achieve a desired inference speed-up while minimizing performance loss. Since the corresponding selection problem involves an exponential search space, we formulate a novel surrogate optimization problem and efficiently solve it via dynamic programming. Empirical results demonstrate that our method consistently outperforms existing depth compression and layer pruning methods on various network architectures, both on image classification and generation tasks. We release the code at https://github.com/snu-mllab/LayerMerge.

</details>

### No Free Prune: Information-Theoretic Barriers to Pruning at Initialization.
- **链接**: [arXiv:2402.01089](https://arxiv.org/abs/2402.01089)
- **作者**: Tanishq Kumar, Kevin Luo, Mark Sellke
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The existence of "lottery tickets" arXiv:1803.03635 at or near initialization raises the tantalizing question of whether large models are necessary in deep learning, or whether sparse networks can be quickly identified and trained without ever training the dense models that contain them. However, efforts to find these sparse subnetworks without training the dense model ("pruning at initialization") have been broadly unsuccessful arXiv:2009.08576. We put forward a theoretical explanation for this, based on the model's effective parameter count, $p_\text{eff}$, given by the sum of the number of non-zero weights in the final network and the mutual information between the sparsity mask and the data. We show the Law of Robustness of arXiv:2105.12806 extends to sparse networks with the usual parameter count replaced by $p_\text{eff}$, meaning a sparse neural network which robustly interpolates noisy data requires a heavily data-dependent mask. We posit that pruning during and after training outputs masks with higher mutual information than those produced by pruning at initialization. Thus two networks may have the same sparsities, but differ in effective parameter count based on how they were trained. This suggests that pruning near initialization may be infeasible and explains why lottery tickets exist, but cannot be found fast (i.e. without training the full network). Experiments on neural networks confirm that information gained during training may indeed affect model capacity.

</details>

### Towards efficient deep spiking neural networks construction with spiking activity based pruning.
- **链接**: [arXiv:2406.01072](https://arxiv.org/abs/2406.01072)
- **作者**: Yaxin Li, Qi Xu, Jiangrong Shen, Hongming Xu, Long Chen, Gang Pan
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The emergence of deep and large-scale spiking neural networks (SNNs) exhibiting high performance across diverse complex datasets has led to a need for compressing network models due to the presence of a significant number of redundant structural units, aiming to more effectively leverage their low-power consumption and biological interpretability advantages. Currently, most model compression techniques for SNNs are based on unstructured pruning of individual connections, which requires specific hardware support. Hence, we propose a structured pruning approach based on the activity levels of convolutional kernels named Spiking Channel Activity-based (SCA) network pruning framework. Inspired by synaptic plasticity mechanisms, our method dynamically adjusts the network's structure by pruning and regenerating convolutional kernels during training, enhancing the model's adaptation to the current target task. While maintaining model performance, this approach refines the network architecture, ultimately reducing computational load and accelerating the inference process. This indicates that structured dynamic sparse learning methods can better facilitate the application of deep SNNs in low-power and high-efficiency scenarios.

</details>

### COPAL: Continual Pruning in Large Language Generative Models.
- **链接**: [arXiv:2405.02347](https://arxiv.org/abs/2405.02347)
- **作者**: Srikanth Malla, Joon Hee Choi, Chiho Choi
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Adapting pre-trained large language models to different domains in natural language processing requires two key considerations: high computational demands and model's inability to continual adaptation. To simultaneously address both issues, this paper presents COPAL (COntinual Pruning in Adaptive Language settings), an algorithm developed for pruning large language generative models under a continual model adaptation setting. While avoiding resource-heavy finetuning or retraining, our pruning process is guided by the proposed sensitivity analysis. The sensitivity effectively measures model's ability to withstand perturbations introduced by the new dataset and finds model's weights that are relevant for all encountered datasets. As a result, COPAL allows seamless model adaptation to new domains while enhancing the resource efficiency. Our empirical evaluation on a various size of LLMs show that COPAL outperforms baseline models, demonstrating its efficacy in efficiency and adaptability.

</details>

### OSSCAR: One-Shot Structured Pruning in Vision and Language Models with Combinatorial Optimization.
- **链接**: [arXiv:2403.12983](https://arxiv.org/abs/2403.12983)
- **作者**: Xiang Meng, Shibal Ibrahim, Kayhan Behdin, Hussein Hazimeh, Natalia Ponomareva, Rahul Mazumder
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Structured pruning is a promising approach for reducing the inference costs of large vision and language models. By removing carefully chosen structures, e.g., neurons or attention heads, the improvements from this approach can be realized on standard deep learning hardware. In this work, we focus on structured pruning in the one-shot (post-training) setting, which does not require model retraining after pruning. We propose a novel combinatorial optimization framework for this problem, based on a layer-wise reconstruction objective and a careful reformulation that allows for scalable optimization. Moreover, we design a new local combinatorial optimization algorithm, which exploits low-rank updates for efficient local search. Our framework is time and memory-efficient and considerably improves upon state-of-the-art one-shot methods on vision models (e.g., ResNet50, MobileNet) and language models (e.g., OPT-1.3B -- OPT-30B). For language models, e.g., OPT-2.7B, OSSCAR can lead to $125\times$ lower test perplexity on WikiText with $2\times$ inference time speedup in comparison to the state-of-the-art ZipLM approach. Our framework is also $6\times$ -- $8\times$ faster. Notably, our work considers models with tens of billions of parameters, which is up to $100\times$ larger than what has been previously considered in the structured pruning literature.

</details>

### Ensemble Pruning for Out-of-distribution Generalization.
- **链接**: [出版页](https://proceedings.mlr.press/v235/qiao24a.html)
- **作者**: Fengchun Qiao, Xi Peng
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### Exploring Intrinsic Dimension for Vision-Language Model Pruning.
- **链接**: [出版页](https://proceedings.mlr.press/v235/wang24cp.html)
- **作者**: Hanzhang Wang, Jiawen Zhang, Qingyuan Ma
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### Assessing the Brittleness of Safety Alignment via Pruning and Low-Rank Modifications.
- **链接**: [arXiv:2402.05162](https://arxiv.org/abs/2402.05162)
- **作者**: Boyi Wei, Kaixuan Huang, Yangsibo Huang, Tinghao Xie, Xiangyu Qi, Mengzhou Xia et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large language models (LLMs) show inherent brittleness in their safety mechanisms, as evidenced by their susceptibility to jailbreaking and even non-malicious fine-tuning. This study explores this brittleness of safety alignment by leveraging pruning and low-rank modifications. We develop methods to identify critical regions that are vital for safety guardrails, and that are disentangled from utility-relevant regions at both the neuron and rank levels. Surprisingly, the isolated regions we find are sparse, comprising about $3\%$ at the parameter level and $2.5\%$ at the rank level. Removing these regions compromises safety without significantly impacting utility, corroborating the inherent brittleness of the model's safety mechanisms. Moreover, we show that LLMs remain vulnerable to low-cost fine-tuning attacks even when modifications to the safety-critical regions are restricted. These findings underscore the urgent need for more robust safety strategies in LLMs.

</details>

### Lightweight Image Super-Resolution via Flexible Meta Pruning.
- **链接**: [出版页](https://proceedings.mlr.press/v235/zhang24cc.html)
- **作者**: Yulun Zhang, Kai Zhang, Luc Van Gool, Martin Danelljan, Fisher Yu
- **🏷️ 机构**: ETH Zurich
- **会议**: ICML 2024

### APT: Adaptive Pruning and Tuning Pretrained Language Models for Efficient Training and Inference.
- **链接**: [arXiv:2401.12200](https://arxiv.org/abs/2401.12200)
- **作者**: Bowen Zhao, Hannaneh Hajishirzi, Qingqing Cao
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Fine-tuning and inference with large Language Models (LM) are generally known to be expensive. Parameter-efficient fine-tuning over pretrained LMs reduces training memory by updating a small number of LM parameters but does not improve inference efficiency. Structured pruning improves LM inference efficiency by removing consistent parameter blocks, yet often increases training memory and time. To improve both training and inference efficiency, we introduce APT that adaptively prunes and tunes parameters for the LMs. At the early stage of fine-tuning, APT dynamically adds salient tuning parameters for fast and accurate convergence while discarding unimportant parameters for efficiency. Compared to baselines, our experiments show that APT maintains up to 98% task performance when pruning RoBERTa and T5 models with 40% parameters left while keeping 86.4% LLaMA models' performance with 70% parameters remained. Furthermore, APT speeds up LMs fine-tuning by up to 8x and reduces large LMs memory training footprint by up to 70%.

</details>

### Defense against Backdoor Attack on Pre-trained Language Models via Head Pruning and Attention Normalization.
- **链接**: [出版页](https://proceedings.mlr.press/v235/zhao24r.html)
- **作者**: Xingyi Zhao, Depeng Xu, Shuhan Yuan
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### Accelerating Transformer Pre-training with 2: 4 Sparsity.
- **链接**: [arXiv:2404.01847](https://arxiv.org/abs/2404.01847)
- **作者**: Yuezhou Hu, Kang Zhao, Weiyu Huang, Jianfei Chen, Jun Zhu
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Training large transformers is slow, but recent innovations on GPU architecture give us an advantage. NVIDIA Ampere GPUs can execute a fine-grained 2:4 sparse matrix multiplication twice as fast as its dense equivalent. In the light of this property, we comprehensively investigate the feasibility of accelerating feed-forward networks (FFNs) of transformers in pre-training. First, we define a ``flip rate'' to monitor the stability of a 2:4 training process. Utilizing this metric, we propose three techniques to preserve accuracy: to modify the sparse-refined straight-through estimator by applying the masked decay term on gradients, to determine a feasible decay factor in warm-up stage, and to enhance the model's quality by a dense fine-tuning procedure near the end of pre-training. Besides, we devise two techniques to practically accelerate training: to calculate transposable 2:4 masks by convolution, and to accelerate gated activation functions by reducing GPU L2 cache miss. Experiments show that our 2:4 sparse training algorithm achieves similar convergence to dense training algorithms on several transformer pre-training tasks, while actual acceleration can be observed on different shapes of transformer block apparently. Our toolkit is available at https://github.com/huyz2023/2by4-pretrain.

</details>

### SPP: Sparsity-Preserved Parameter-Efficient Fine-Tuning for Large Language Models.
- **链接**: [arXiv:2405.16057](https://arxiv.org/abs/2405.16057)
- **作者**: Xudong Lu, Aojun Zhou, Yuhui Xu, Renrui Zhang, Peng Gao, Hongsheng Li
- **🏷️ 机构**: CUHK
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large Language Models (LLMs) have become pivotal in advancing the field of artificial intelligence, yet their immense sizes pose significant challenges for both fine-tuning and deployment. Current post-training pruning methods, while reducing the sizes of LLMs, often fail to maintain their original performance. To address these challenges, this paper introduces SPP, a Sparsity-Preserved Parameter-efficient fine-tuning method. Different from existing post-training pruning approaches that struggle with performance retention, SPP proposes to employ lightweight learnable column and row matrices to optimize sparse LLM weights, keeping the structure and sparsity of pruned pre-trained models intact. By element-wise multiplication and residual addition, SPP ensures the consistency of model sparsity pattern and ratio during both training and weight-merging processes. We demonstrate the effectiveness of SPP by applying it to the LLaMA and LLaMA-2 model families with recent post-training pruning methods. Our results show that SPP significantly enhances the performance of models with different sparsity patterns (i.e. unstructured and N:M sparsity), especially for those with high sparsity ratios (e.g. 75%), making it a promising solution for the efficient fine-tuning of sparse LLMs. Code will be made available at https://github.com/Lucky-Lance/SPP.

</details>

### SPADE: Sparsity-Guided Debugging for Deep Neural Networks.
- **链接**: [arXiv:2310.04519](https://arxiv.org/abs/2310.04519)
- **作者**: Arshia Soltani Moakhar, Eugenia Iofinova, Elias Frantar, Dan Alistarh
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> It is known that sparsity can improve interpretability for deep neural networks. However, existing methods in the area either require networks that are pre-trained with sparsity constraints, or impose sparsity after the fact, altering the network's general behavior. In this paper, we demonstrate, for the first time, that sparsity can instead be incorporated into the interpretation process itself, as a sample-specific preprocessing step. Unlike previous work, this approach, which we call SPADE, does not place constraints on the trained model and does not affect its behavior during inference on the sample. Given a trained model and a target sample, SPADE uses sample-targeted pruning to provide a "trace" of the network's execution on the sample, reducing the network to the most important connections prior to computing an interpretation. We demonstrate that preprocessing with SPADE significantly increases the accuracy of image saliency maps across several interpretability methods. Additionally, SPADE improves the usefulness of neuron visualizations, aiding humans in reasoning about network behavior. Our code is available at https://github.com/IST-DASLab/SPADE.

</details>

### QUEST: Query-Aware Sparsity for Efficient Long-Context LLM Inference.
- **链接**: [arXiv:2406.10774](https://arxiv.org/abs/2406.10774)
- **作者**: Jiaming Tang, Yilong Zhao, Kan Zhu, Guangxuan Xiao, Baris Kasikci, Song Han
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> As the demand for long-context large language models (LLMs) increases, models with context windows of up to 128K or 1M tokens are becoming increasingly prevalent. However, long-context LLM inference is challenging since the inference speed decreases significantly as the sequence length grows. This slowdown is primarily caused by loading a large KV cache during self-attention. Previous works have shown that a small portion of critical tokens will dominate the attention outcomes. However, we observe the criticality of a token highly depends on the query. To this end, we propose Quest, a query-aware KV cache selection algorithm. Quest keeps track of the minimal and maximal Key values in KV cache pages and estimates the criticality of a given page using Query vectors. By only loading the Top-K critical KV cache pages for attention, Quest significantly speeds up self-attention without sacrificing accuracy. We show that Quest can achieve up to 2.23x self-attention speedup, which reduces inference latency by 7.03x while performing well on tasks with long dependencies with negligible accuracy loss. Code is available at http://github.com/mit-han-lab/Quest .

</details>

### A Sparsity Principle for Partially Observable Causal Representation Learning.
- **链接**: [arXiv:2403.08335](https://arxiv.org/abs/2403.08335)
- **作者**: Danru Xu, Dingling Yao, Sébastien Lachapelle, Perouz Taslakian, Julius von Kügelgen, Francesco Locatello et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Causal representation learning aims at identifying high-level causal variables from perceptual data. Most methods assume that all latent causal variables are captured in the high-dimensional observations. We instead consider a partially observed setting, in which each measurement only provides information about a subset of the underlying causal state. Prior work has studied this setting with multiple domains or views, each depending on a fixed subset of latents. Here, we focus on learning from unpaired observations from a dataset with an instance-dependent partial observability pattern. Our main contribution is to establish two identifiability results for this setting: one for linear mixing functions without parametric assumptions on the underlying causal model, and one for piecewise linear mixing functions with Gaussian latent causal variables. Based on these insights, we propose two methods for estimating the underlying causal variables by enforcing sparsity in the inferred representation. Experiments on different simulated datasets and established benchmarks highlight the effectiveness of our approach in recovering the ground-truth latents.

</details>

### Smoothing Proximal Gradient Methods for Nonsmooth Sparsity Constrained Optimization: Optimality Conditions and Global Convergence.
- **链接**: [出版页](https://proceedings.mlr.press/v235/yuan24a.html)
- **作者**: Ganzhao Yuan
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### Exploring the Benefit of Activation Sparsity in Pre-training.
- **链接**: [arXiv:2410.03440](https://arxiv.org/abs/2410.03440)
- **作者**: Zhengyan Zhang, Chaojun Xiao, Qiujieli Qin, Yankai Lin, Zhiyuan Zeng, Xu Han et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pre-trained Transformers inherently possess the characteristic of sparse activation, where only a small fraction of the neurons are activated for each token. While sparse activation has been explored through post-training methods, its potential in pre-training remains untapped. In this work, we first study how activation properties change during pre-training. Our examination reveals that Transformers exhibit sparse activation throughout the majority of the pre-training process while the activation correlation keeps evolving as training progresses. Leveraging this observation, we propose Switchable Sparse-Dense Learning (SSD). SSD adaptively switches between the Mixtures-of-Experts (MoE) based sparse training and the conventional dense training during the pre-training process, leveraging the efficiency of sparse training and avoiding the static activation correlation of sparse training. Compared to dense training, SSD achieves comparable performance with identical model size and reduces pre-training costs. Moreover, the models trained with SSD can be directly used as MoE models for sparse inference and achieve the same performance as dense models with up to $2\times$ faster inference speed. Codes are available at https://github.com/thunlp/moefication.

</details>

### AlterMOMA: Fusion Redundancy Pruning for Camera-LiDAR Fusion Models with Alternative Modality Masking.
- **链接**: [arXiv:2409.17728](https://arxiv.org/abs/2409.17728)
- **作者**: Shiqi Sun, Yantao Lu, Ning Liu, Bo Jiang, Jinchao Chen, Ying Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Camera-LiDAR fusion models significantly enhance perception performance in autonomous driving. The fusion mechanism leverages the strengths of each modality while minimizing their weaknesses. Moreover, in practice, camera-LiDAR fusion models utilize pre-trained backbones for efficient training. However, we argue that directly loading single-modal pre-trained camera and LiDAR backbones into camera-LiDAR fusion models introduces similar feature redundancy across modalities due to the nature of the fusion mechanism. Unfortunately, existing pruning methods are developed explicitly for single-modal models, and thus, they struggle to effectively identify these specific redundant parameters in camera-LiDAR fusion models. In this paper, to address the issue above on camera-LiDAR fusion models, we propose a novelty pruning framework Alternative Modality Masking Pruning (AlterMOMA), which employs alternative masking on each modality and identifies the redundant parameters. Specifically, when one modality parameters are masked (deactivated), the absence of features from the masked backbone compels the model to reactivate previous redundant features of the other modality backbone. Therefore, these redundant features and relevant redundant parameters can be identified via the reactivation process. The redundant parameters can be pruned by our proposed importance score evaluation function, Alternative Evaluation (AlterEva), which is based on the observation of the loss changes when certain modality parameters are activated and deactivated. Extensive experiments on the nuScene and KITTI datasets encompassing diverse tasks, baseline models, and pruning algorithms showcase that AlterMOMA outperforms existing pruning methods, attaining state-of-the-art performance.

</details>

### A Unified Debiasing Approach for Vision-Language Models across Modalities and Tasks.
- **链接**: [arXiv:2410.07593](https://arxiv.org/abs/2410.07593) · 📚 被引 4
- **作者**: Hoin Jung, Taeuk Jang, Xiaoqian Wang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advancements in Vision-Language Models (VLMs) have enabled complex multimodal tasks by processing text and image data simultaneously, significantly enhancing the field of artificial intelligence. However, these models often exhibit biases that can skew outputs towards societal stereotypes, thus necessitating debiasing strategies. Existing debiasing methods focus narrowly on specific modalities or tasks, and require extensive retraining. To address these limitations, this paper introduces Selective Feature Imputation for Debiasing (SFID), a novel methodology that integrates feature pruning and low confidence imputation (LCI) to effectively reduce biases in VLMs. SFID is versatile, maintaining the semantic integrity of outputs and costly effective by eliminating the need for retraining. Our experimental results demonstrate SFID's effectiveness across various VLMs tasks including zero-shot classification, text-to-image retrieval, image captioning, and text-to-image generation, by significantly reducing gender biases without compromising performance. This approach not only enhances the fairness of VLMs applications but also preserves their efficiency and utility across diverse scenarios.

</details>

### BMRS: Bayesian Model Reduction for Structured Pruning.
- **链接**: [arXiv:2406.01345](https://arxiv.org/abs/2406.01345) · 📚 被引 2
- **作者**: Dustin Wright, Christian Igel, Raghavendra Selvan
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Modern neural networks are often massively overparameterized leading to high compute costs during training and at inference. One effective method to improve both the compute and energy efficiency of neural networks while maintaining good performance is structured pruning, where full network structures (e.g.~neurons or convolutional filters) that have limited impact on the model output are removed. In this work, we propose Bayesian Model Reduction for Structured pruning (BMRS), a fully end-to-end Bayesian method of structured pruning. BMRS is based on two recent methods: Bayesian structured pruning with multiplicative noise, and Bayesian model reduction (BMR), a method which allows efficient comparison of Bayesian models under a change in prior. We present two realizations of BMRS derived from different priors which yield different structured pruning characteristics: 1) BMRS_N with the truncated log-normal prior, which offers reliable compression rates and accuracy without the need for tuning any thresholds and 2) BMRS_U with the truncated log-uniform prior that can achieve more aggressive compression based on the boundaries of truncation. Overall, we find that BMRS offers a theoretically grounded approach to structured pruning of neural networks yielding both high compression rates and accuracy. Experiments on multiple datasets and neural networks of varying complexity showed that the two BMRS methods offer a competitive performance-efficiency trade-off compared to other pruning methods.

</details>

### Exploring Token Pruning in Vision State Space Models.
- **链接**: [arXiv:2409.18962](https://arxiv.org/abs/2409.18962) · 📚 被引 2
- **作者**: Zheng Zhan, Zhenglun Kong, Yifan Gong, Yushu Wu, Zichong Meng, Hangyu Zheng et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> State Space Models (SSMs) have the advantage of keeping linear computational complexity compared to attention modules in transformers, and have been applied to vision tasks as a new type of powerful vision foundation model. Inspired by the observations that the final prediction in vision transformers (ViTs) is only based on a subset of most informative tokens, we take the novel step of enhancing the efficiency of SSM-based vision models through token-based pruning. However, direct applications of existing token pruning techniques designed for ViTs fail to deliver good performance, even with extensive fine-tuning. To address this issue, we revisit the unique computational characteristics of SSMs and discover that naive application disrupts the sequential token positions. This insight motivates us to design a novel and general token pruning method specifically for SSM-based vision models. We first introduce a pruning-aware hidden state alignment method to stabilize the neighborhood of remaining tokens for performance enhancement. Besides, based on our detailed analysis, we propose a token importance evaluation method adapted for SSM models, to guide the token pruning. With efficient implementation and practical acceleration methods, our method brings actual speedup. Extensive experiments demonstrate that our approach can achieve significant computation reduction with minimal impact on performance across different tasks. Notably, we achieve 81.7\% accuracy on ImageNet with a 41.6\% reduction in the FLOPs for pruned PlainMamba-L3. Furthermore, our work provides deeper insights into understanding the behavior of SSM-based vision models for future research.

</details>

### SequentialAttention++ for Block Sparsification: Differentiable Pruning Meets Combinatorial Optimization.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/8735e0793cfd43327eceaacf39466a01-Abstract-Conference.html)
- **作者**: Taisuke Yasuda, Kyriakos Axiotis, Gang Fu, Mohammad Hossein Bateni, Vahab Mirrokni
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### S2HPruner: Soft-to-Hard Distillation Bridges the Discretization Gap in Pruning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/d368aba36f74776cc7a1079332a31973-Abstract-Conference.html) · 📚 被引 1
- **作者**: Weihao Lin, Shengji Tang, Chong Yu, Peng Ye, Tao Chen
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### SparseLLM: Towards Global Pruning of Pre-trained Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/522134ee1c52c7a2b929bc87cfe1781c-Abstract-Conference.html) · 📚 被引 13
- **作者**: Guangji Bai, Yijiang Li, Chen Ling, Kibaek Kim, Liang Zhao
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Finding Transformer Circuits With Edge Pruning.
- **链接**: [arXiv:2406.16778](https://arxiv.org/abs/2406.16778) · 📚 被引 6
- **作者**: Adithya Bhaskar, Alexander Wettig, Dan Friedman, Danqi Chen
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The path to interpreting a language model often proceeds via analysis of circuits -- sparse computational subgraphs of the model that capture specific aspects of its behavior. Recent work has automated the task of discovering circuits. Yet, these methods have practical limitations, as they rely either on inefficient search algorithms or inaccurate approximations. In this paper, we frame automated circuit discovery as an optimization problem and propose *Edge Pruning* as an effective and scalable solution. Edge Pruning leverages gradient-based pruning techniques, but instead of removing neurons or components, it prunes the \emph{edges} between components. Our method finds circuits in GPT-2 that use less than half the number of edges compared to circuits found by previous methods while being equally faithful to the full model predictions on standard circuit-finding tasks. Edge Pruning is efficient even with as many as 100K examples, outperforming previous methods in speed and producing substantially better circuits. It also perfectly recovers the ground-truth circuits in two models compiled with Tracr. Thanks to its efficiency, we scale Edge Pruning to CodeLlama-13B, a model over 100x the scale that prior methods operate on. We use this setting for a case study comparing the mechanisms behind instruction prompting and in-context learning. We find two circuits with more than 99.96% sparsity that match the performance of the full model and reveal that the mechanisms in the two settings overlap substantially. Our case study shows that Edge Pruning is a practical and scalable tool for interpretability and sheds light on behaviors that only emerge in large models.

</details>

### Beyond Efficiency: Molecular Data Pruning for Enhanced Generalization.
- **链接**: [arXiv:2409.01081](https://arxiv.org/abs/2409.01081) · 📚 被引 1
- **作者**: Dingshuo Chen, Zhixun Li, Yuyan Ni, Guibin Zhang, Ding Wang, Qiang Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> With the emergence of various molecular tasks and massive datasets, how to perform efficient training has become an urgent yet under-explored issue in the area. Data pruning (DP), as an oft-stated approach to saving training burdens, filters out less influential samples to form a coreset for training. However, the increasing reliance on pretrained models for molecular tasks renders traditional in-domain DP methods incompatible. Therefore, we propose a Molecular data Pruning framework for enhanced Generalization (MolPeg), which focuses on the source-free data pruning scenario, where data pruning is applied with pretrained models. By maintaining two models with different updating paces during training, we introduce a novel scoring function to measure the informativeness of samples based on the loss discrepancy. As a plug-and-play framework, MolPeg realizes the perception of both source and target domain and consistently outperforms existing DP methods across four downstream tasks. Remarkably, it can surpass the performance obtained from full-dataset training, even when pruning up to 60-70% of the data on HIV and PCBA dataset. Our work suggests that the discovery of effective data-pruning metrics could provide a viable path to both enhanced efficiency and superior generalization in transfer learning.

</details>

### DISP-LLM: Dimension-Independent Structural Pruning for Large Language Models.
- **链接**: [arXiv:2410.11988](https://arxiv.org/abs/2410.11988) · 📚 被引 14
- **作者**: Shangqian Gao, Chi-Heng Lin, Ting Hua, Zheng Tang, Yilin Shen, Hongxia Jin et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large Language Models (LLMs) have achieved remarkable success in various natural language processing tasks, including language modeling, understanding, and generation. However, the increased memory and computational costs associated with these models pose significant challenges for deployment on resource-limited devices. Structural pruning has emerged as a promising solution to reduce the costs of LLMs without requiring post-processing steps. Prior structural pruning methods either follow the dependence of structures at the cost of limiting flexibility, or introduce non-trivial additional parameters by incorporating different projection matrices. In this work, we propose a novel approach that relaxes the constraint imposed by regular structural pruning methods and eliminates the structural dependence along the embedding dimension. Our dimension-independent structural pruning method offers several benefits. Firstly, our method enables different blocks to utilize different subsets of the feature maps. Secondly, by removing structural dependence, we facilitate each block to possess varying widths along its input and output dimensions, thereby significantly enhancing the flexibility of structural pruning. We evaluate our method on various LLMs, including OPT, LLaMA, LLaMA-2, Phi-1.5, and Phi-2. Experimental results demonstrate that our approach outperforms other state-of-the-art methods, showing for the first time that structural pruning can achieve an accuracy similar to semi-structural pruning.

</details>

## 跨领域论文（完整笔记在其他领域）

- GAFusion: Adaptive Fusing LiDAR and Camera with Multiple Guidance for 3D Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- Scene Adaptive Sparse Transformer for Event-based Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- Commonsense Prototype for Outdoor Unsupervised 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- Improving Distant 3D Object Detection Using 2D Box Supervision. → [3d-detection](../3d-detection/Guideline%202024.md)
- CaKDP: Category-Aware Knowledge Distillation and Pruning Framework for Lightweight 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- Differentiable Information Bottleneck for Deterministic Multi-View Clustering. → [multi-camera-perception](../multi-camera-perception/Guideline%202024.md)
- Transferable and Principled Efficiency for Open-Vocabulary Segmentation. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- One Prompt Word is Enough to Boost Adversarial Robustness for Pre-Trained Vision-Language Models. → [vlm](../vlm/Guideline%202024.md)
- MoPE-CLIP: Structured Pruning for Efficient Vision-Language Models with Module-Wise Pruning Error Metric. → [vlm](../vlm/Guideline%202024.md)
- Sieve: Multimodal Dataset Pruning Using Image Captioning Models. → [multimodal](../multimodal/Guideline%202024.md)
- Multimodal Industrial Anomaly Detection by Crossmodal Feature Mapping. → [multimodal](../multimodal/Guideline%202024.md)
- Cloud-Device Collaborative Learning for Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202024.md)
- Towards Backward-Compatible Continual Learning of Image Compression. → [continual-learning](../continual-learning/Guideline%202024.md)
- FSD-BEV: Foreground Self-distillation for Multi-view 3D Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- Approaching Outside: Scaling Unsupervised 3D Object Detection from 2D Scene. → [bev](../bev/Guideline%202024.md)
- Image-to-Lidar Relational Distillation for Autonomous Driving Data. → [autonomous-driving](../autonomous-driving/Guideline%202024.md)
- Anytime Continual Learning for Open Vocabulary Classification. → [continual-learning](../continual-learning/Guideline%202024.md)
- Distill Gold from Massive Ores: Bi-level Data Pruning Towards Efficient Dataset Distillation. → [knowledge-distillation](../knowledge-distillation/Guideline%202024.md)
- LiDAR-PTQ: Post-Training Quantization for Point Cloud 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- Continual Learning on a Diet: Learning from Sparsely Labeled Streams Under Constrained Computation. → [continual-learning](../continual-learning/Guideline%202024.md)
- ZOPP: A Framework of Zero-shot Offboard Panoptic Perception for Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202024.md)
- Streaming Long Video Understanding with Large Language Models. → [video-understanding](../video-understanding/Guideline%202024.md)


## 🆕 增量新增

### Layer-Adaptive State Pruning for Deep State Space Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/14730e0dd6ac1c4a5765310909fd51b1-Abstract-Conference.html) · 📚 被引 2
- **作者**: Minseon Gwak, Seongrok Moon, Joohwan Ko, PooGyeon Park
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Pruning neural network models for gene regulatory dynamics using data and domain knowledge.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/d52d2281babd36913643392a09a56832-Abstract-Conference.html)
- **作者**: Intekhab Hossain, Jonas Fischer, Rebekka Burkholz, John Quackenbush
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### S-STE: Continuous Pruning Function for Efficient 2: 4 Sparse Pre-training.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/3b576711b12ab036b45130fc8eb78504-Abstract-Conference.html) · 📚 被引 2
- **作者**: Yuezhou Hu, Jun Zhu, Jianfei Chen
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Fast Iterative Hard Thresholding Methods with Pruning Gradient Computations.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/5eaa54503005d9125ad6aa3044e912d8-Abstract-Conference.html) · 📚 被引 2
- **作者**: Yasutoshi Ida, Sekitoshi Kanai, Atsutoshi Kumagai, Tomoharu Iwata, Yasuhiro Fujiwara
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Spectral Graph Pruning Against Over-Squashing and Over-Smoothing.
- **链接**: [arXiv:2404.04612](https://arxiv.org/abs/2404.04612) · 📚 被引 4
- **作者**: Adarsh Jamadandi, Celia Rubio-Madrigal, Rebekka Burkholz
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Message Passing Graph Neural Networks are known to suffer from two problems that are sometimes believed to be diametrically opposed: over-squashing and over-smoothing. The former results from topological bottlenecks that hamper the information flow from distant nodes and are mitigated by spectral gap maximization, primarily, by means of edge additions. However, such additions often promote over-smoothing that renders nodes of different classes less distinguishable. Inspired by the Braess phenomenon, we argue that deleting edges can address over-squashing and over-smoothing simultaneously. This insight explains how edge deletions can improve generalization, thus connecting spectral gap optimization to a seemingly disconnected objective of reducing computational resources by pruning graphs for lottery tickets. To this end, we propose a more effective spectral gap optimization framework to add or delete edges and demonstrate its effectiveness on large heterophilic datasets.

</details>

### DapperFL: Domain Adaptive Federated Learning with Model Fusion Pruning for Edge Devices.
- **链接**: [arXiv:2412.05823](https://arxiv.org/abs/2412.05823) · 📚 被引 5
- **作者**: Yongzhe Jia, Xuyun Zhang, Hongsheng Hu, Kim-Kwang Raymond Choo, Lianyong Qi, Xiaolong Xu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Federated learning (FL) has emerged as a prominent machine learning paradigm in edge computing environments, enabling edge devices to collaboratively optimize a global model without sharing their private data. However, existing FL frameworks suffer from efficacy deterioration due to the system heterogeneity inherent in edge computing, especially in the presence of domain shifts across local data. In this paper, we propose a heterogeneous FL framework DapperFL, to enhance model performance across multiple domains. In DapperFL, we introduce a dedicated Model Fusion Pruning (MFP) module to produce personalized compact local models for clients to address the system heterogeneity challenges. The MFP module prunes local models with fused knowledge obtained from both local and remaining domains, ensuring robustness to domain shifts. Additionally, we design a Domain Adaptive Regularization (DAR) module to further improve the overall performance of DapperFL. The DAR module employs regularization generated by the pruned model, aiming to learn robust representations across domains. Furthermore, we introduce a specific aggregation algorithm for aggregating heterogeneous local models with tailored architectures and weights. We implement DapperFL on a realworld FL platform with heterogeneous clients. Experimental results on benchmark datasets with multiple domains demonstrate that DapperFL outperforms several state-of-the-art FL frameworks by up to 2.28%, while significantly achieving model volume reductions ranging from 20% to 80%. Our code is available at: https://github.com/jyzgh/DapperFL.

</details>

### Discovering Sparsity Allocation for Layer-wise Pruning of Large Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/ff997469ac66cf893c4183efeb22212a-Abstract-Conference.html) · 📚 被引 7
- **作者**: Lujun Li, Peijie Dong, Zhenheng Tang, Xiang Liu, Qiang Wang, Wenhan Luo et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### SlimGPT: Layer-wise Structured Pruning for Large Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/c1c44e46358e0fb94dc94ec495a7fb1a-Abstract-Conference.html) · 📚 被引 12
- **作者**: Gui Ling, Ziyang Wang, Yuliang Yan, Qingwen Liu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### AlphaPruning: Using Heavy-Tailed Self Regularization Theory for Improved Layer-wise Pruning of Large Language Models.
- **链接**: [arXiv:2410.10912](https://arxiv.org/abs/2410.10912) · 📚 被引 8
- **作者**: Haiquan Lu, Yefan Zhou, Shiwei Liu, Zhangyang Wang, Michael W. Mahoney, Yaoqing Yang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent work on pruning large language models (LLMs) has shown that one can eliminate a large number of parameters without compromising performance, making pruning a promising strategy to reduce LLM model size. Existing LLM pruning strategies typically assign uniform pruning ratios across layers, limiting overall pruning ability; and recent work on layerwise pruning of LLMs is often based on heuristics that can easily lead to suboptimal performance. In this paper, we leverage Heavy-Tailed Self-Regularization (HT-SR) Theory, in particular the shape of empirical spectral densities (ESDs) of weight matrices, to design improved layerwise pruning ratios for LLMs. Our analysis reveals a wide variability in how well-trained, and thus relatedly how prunable, different layers of an LLM are. Based on this, we propose AlphaPruning, which uses shape metrics to allocate layerwise sparsity ratios in a more theoretically principled manner. AlphaPruning can be used in conjunction with multiple existing LLM pruning methods. Our empirical results show that AlphaPruning prunes LLaMA-7B to 80% sparsity while maintaining reasonable perplexity, marking a first in the literature on LLMs. We have open-sourced our code at https://github.com/haiquanlu/AlphaPruning.

</details>

## 跨领域论文（完整笔记在其他领域）

- CaKDP: Category-Aware Knowledge Distillation and Pruning Framework for Lightweight 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- MADTP: Multimodal Alignment-Guided Dynamic Token Pruning for Accelerating Vision-Language Transformer. → [multimodal](../multimodal/Guideline%202024.md)
- MoPE-CLIP: Structured Pruning for Efficient Vision-Language Models with Module-Wise Pruning Error Metric. → [vlm](../vlm/Guideline%202024.md)
- Sieve: Multimodal Dataset Pruning Using Image Captioning Models. → [multimodal](../multimodal/Guideline%202024.md)
- Towards Backward-Compatible Continual Learning of Image Compression. → [continual-learning](../continual-learning/Guideline%202024.md)
- FSD-BEV: Foreground Self-distillation for Multi-view 3D Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- Approaching Outside: Scaling Unsupervised 3D Object Detection from 2D Scene. → [bev](../bev/Guideline%202024.md)
- Image-to-Lidar Relational Distillation for Autonomous Driving Data. → [autonomous-driving](../autonomous-driving/Guideline%202024.md)
- UniCode: Learning a Unified Codebook for Multimodal Large Language Models. → [vlm](../vlm/Guideline%202024.md)
- Anytime Continual Learning for Open Vocabulary Classification. → [continual-learning](../continual-learning/Guideline%202024.md)
- Distill Gold from Massive Ores: Bi-level Data Pruning Towards Efficient Dataset Distillation. → [knowledge-distillation](../knowledge-distillation/Guideline%202024.md)
- LiDAR-PTQ: Post-Training Quantization for Point Cloud 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- Continual Learning on a Diet: Learning from Sparsely Labeled Streams Under Constrained Computation. → [continual-learning](../continual-learning/Guideline%202024.md)
- ZOPP: A Framework of Zero-shot Offboard Panoptic Perception for Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202024.md)
- Streaming Long Video Understanding with Large Language Models. → [video-understanding](../video-understanding/Guideline%202024.md)
<!-- COMPLETE v1 papers=107 -->
