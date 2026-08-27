# Network Pruning — 2024 Guideline

> 领域: 网络剪枝 / 模型压缩（结构化剪枝、稀疏化）
> 论文数: 35 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: [2022](Guideline%202022.md)

### Scene Adaptive Sparse Transformer for Event-based Object Detection. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2404.01882](https://arxiv.org/abs/2404.01882) · 📚 被引 42
- **作者**: Yansong Peng, Hebei Li, Yueyi Zhang, Xiaoyan Sun, Feng Wu
- **🏷️ 机构**: University of Science and Technology of China
- **会议**: CVPR 2024
- **摘要（中）**: 针对基于事件相机的高计算成本问题，现有Transformer方法在事件目标检测中缺乏稀疏性和适应性，无法平衡token级稀疏化与窗口Transformer的效率，且缺乏场景特定优化导致信息丢失和召回率降低。本文提出场景自适应稀疏Transformer（SAST），通过窗口-令牌协同稀疏化增强容错性并降低计算开销，利用创新的评分和选择模块以及掩码稀疏窗口自注意力，实现场景感知的自适应稀疏度优化。相比已有工作，SAST能动态调整稀疏级别，仅关注重要目标，在保持性能的同时显著降低计算成本。实验表明，SAST在事件目标检测任务上实现了高效性和高召回率的平衡。
- **摘要（英）**: This paper addresses the high computational cost of Transformer-based event-based object detection by proposing a Scene Adaptive Sparse Transformer (SAST) that enables window-token co-sparsification and scene-aware sparsity optimization. SAST dynamically adjusts sparsity levels based on scene complexity, focusing on important objects while reducing overhead, achieving improved efficiency and recall compared to existing sparse Transformers.
- **核心贡献**: 提出SAST框架，通过窗口-令牌协同稀疏化实现高效的事件目标检测。
- **创新点**: 引入场景自适应稀疏度优化和掩码稀疏窗口自注意力机制。
- **结果**: 在降低计算开销的同时，保持了高召回率和检测性能。

### Transferable and Principled Efficiency for Open-Vocabulary Segmentation. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2404.07448](https://arxiv.org/abs/2404.07448) · 📚 被引 2
- **作者**: Jingxuan Xu, Wuyang Chen, Yao Zhao, Yunchao Wei
- **🏷️ 机构**: Beijing Jiaotong University, Simon Fraser University
- **会议**: CVPR 2024
- **摘要（中）**: 针对开放词汇分割依赖大型视觉语言基础模型导致计算开销大、微调成本高的问题，该论文提出一种可迁移且原则性的效率优化方法，旨在使用更小的模型和更低的训练成本达到与大型模型相当甚至更好的性能。核心策略是使效率优化具有原则性，从而无需定制即可无缝迁移到不同OVS框架。实验在多个OVS基准上验证了该方法在分割精度和计算成本之间的优越权衡，但摘要未给出具体数据。
- **摘要（英）**: This paper addresses the high computational and fine-tuning costs of open-vocabulary segmentation with large vision-language models by proposing a transferable and principled efficiency approach, enabling smaller models to achieve comparable or better performance. The strategy ensures seamless transferability across OVS frameworks without customization, demonstrating superior accuracy-efficiency trade-offs on diverse benchmarks, though specific metrics are not detailed.
- **核心贡献**: 提出了一种可迁移且原则性的效率优化方法，用于降低开放词汇分割的计算和训练成本。
- **创新点**: 通过原则性设计实现效率优化在不同OVS框架间的无缝迁移。
- **结果**: 在多个基准上实现了精度与计算成本的优越权衡。

### One Prompt Word is Enough to Boost Adversarial Robustness for Pre-Trained Vision-Language Models. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2403.01849](https://arxiv.org/abs/2403.01849) · 📚 被引 33
- **作者**: Lin Li, Haoyan Guan, Jianing Qiu, Michael W. Spratling
- **🏷️ 机构**: King&#x0027;s College,London, Imperial College,London
- **会议**: CVPR 2024
- **摘要（中）**: 针对预训练视觉语言模型（如CLIP）对对抗样本的脆弱性，本文从文本提示角度研究鲁棒性，而非模型权重。首先发现对抗攻击和防御的有效性对文本提示敏感，据此提出对抗提示调优（APT）方法，通过学习鲁棒文本提示提升模型抗攻击能力。APT在计算和数据效率上具有优势，在15个数据集和4种数据稀疏方案下进行了广泛实验，仅添加一个学习词即可显著提升准确率和鲁棒性，并展现出良好的分布偏移泛化能力。
- **摘要（英）**: This paper studies adversarial robustness of VLMs from the text prompt perspective, proposing Adversarial Prompt Tuning (APT) to learn robust prompts. APT is computationally and data efficient, significantly boosting accuracy and robustness with just one learned word across 15 datasets and various data sparsity settings.
- **核心贡献**: 提出对抗提示调优方法，通过学习鲁棒文本提示增强VLM的对抗鲁棒性。
- **创新点**: 首次从文本提示角度而非模型权重角度提升鲁棒性。
- **结果**: 在多个数据集上显著提升了准确率和鲁棒性，且仅需一个学习词。

### MoPE-CLIP: Structured Pruning for Efficient Vision-Language Models with Module-Wise Pruning Error Metric. **⭐⭐⭐** (相关度: 65%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02584) · 📚 被引 21
- **作者**: Haokun Lin, Haoli Bai, Zhili Liu, Lu Hou, Muyi Sun, Linqi Song et al.
- **🏷️ 机构**: School of Artificial Intelligence, University of Chinese Academy of Sciences, Huawei Noah&#x0027;s Ark Lab, Institute of Automation, Chinese Academy of Sciences,CRIPAC &#x0026; MAIS
- **会议**: CVPR 2024
- **摘要（中）**: 针对视觉语言模型（VLM）的高计算成本，本文提出MoPE-CLIP结构化剪枝方法，引入模块级剪枝误差度量来指导剪枝过程。该方法通过评估每个模块的剪枝误差，实现更精确的剪枝决策，在保持模型性能的同时减少参数和计算量。相比现有剪枝方法，MoPE-CLIP考虑了模块间的差异，提高了剪枝的效率和效果。实验表明，该方法在VLM任务上实现了有效的模型压缩。
- **摘要（英）**: This paper proposes MoPE-CLIP, a structured pruning method for vision-language models using a module-wise pruning error metric. It guides pruning decisions by evaluating per-module errors, improving efficiency and maintaining performance, achieving effective model compression.
- **核心贡献**: 提出模块级剪枝误差度量，用于VLM的结构化剪枝。
- **创新点**: 引入模块级误差评估，提升剪枝精度。
- **结果**: 在保持性能的同时，有效减少了模型参数和计算量。

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

### Finding Lottery Tickets in Vision Models via Data-Driven Spectral Foresight Pruning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01528) · 📚 被引 8
- **作者**: Leonardo Iurada, Marco Ciccone, Tatiana Tommasi
- **🏷️ 机构**: Politecnico di Torino,Italy
- **会议**: CVPR 2024

### HiPose: Hierarchical Binary Surface Encoding and Correspondence Pruning for RGB-D 6DoF Object Pose Estimation.
- **链接**: [arXiv:2311.12588](https://arxiv.org/abs/2311.12588) · 📚 被引 23
- **作者**: Yongliang Lin, Yongzhi Su, Praveen Nathan, Sandeep Inuganti, Yan Di, Martin Sundermeyer et al.
- **🏷️ 机构**: Zhejiang University, German Research Center for Artificial Intelligence (DFKI), Technische Universit&#x00E4;t M&#x00FC;nchen
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > In this work, we present a novel dense-correspondence method for 6DoF object pose estimation from a single RGB-D image. While many existing data-driven methods achieve impressive performance, they tend to be time-consuming due to their reliance on rendering-based refinement approaches. To circumvent this limitation, we present HiPose, which establishes 3D-3D correspondences in a coarse-to-fine manner with a hierarchical binary surface encoding. Unlike previous dense-correspondence methods, we estimate the correspondence surface by employing point-to-surface matching and iteratively constricting the surface until it becomes a correspondence point while gradually removing outliers. Extensive experiments on public benchmarks LM-O, YCB-V, and T-Less demonstrate that our method surpasses all refinement-free methods and is even on par with expensive refinement-based approaches. Crucially, our approach is computationally efficient and enables real-time critical applications with high accuracy requirements.

### MAP: MAsk-Pruning for Source-Free Model Intellectual Property Protection.
- **链接**: [arXiv:2403.04149](https://arxiv.org/abs/2403.04149) · 📚 被引 7
- **作者**: Boyang Peng, Sanqing Qu, Yong Wu, Tianpei Zou, Lianghua He, Alois Knoll et al.
- **🏷️ 机构**: Tongji University, Technical University of Munich
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Deep learning has achieved remarkable progress in various applications, heightening the importance of safeguarding the intellectual property (IP) of well-trained models. It entails not only authorizing usage but also ensuring the deployment of models in authorized data domains, i.e., making models exclusive to certain target domains. Previous methods necessitate concurrent access to source training data and target unauthorized data when performing IP protection, making them risky and inefficient for decentralized private data. In this paper, we target a practical setting where only a well-trained source model is available and investigate how we can realize IP protection. To achieve this, we propose a novel MAsk Pruning (MAP) framework. MAP stems from an intuitive hypothesis, i.e., there are target-related parameters in a well-trained model, locating and pruning them is the key to IP protection. Technically, MAP freezes the source model and learns a target-specific binary mask to prevent unauthorized data usage while minimizing performance degradation on authorized data. Moreover, we introduce a new metric aimed at achieving a better balance between source and target performance degradation. To verify the effectiveness and versatility, we have evaluated MAP in a variety of scenarios, including vanilla source-available, practical source-free, and challenging data-free. Extensive experiments indicate that MAP yields new state-of-the-art performance.

### Zero-TPrune: Zero-Shot Token Pruning Through Leveraging of the Attention Graph in Pre-Trained Transformers.
- **链接**: [arXiv:2305.17328](https://arxiv.org/abs/2305.17328) · 📚 被引 42
- **作者**: Hongjie Wang, Bhishma Dedhia, Niraj K. Jha
- **🏷️ 机构**: Princeton University,Princeton,NJ,USA,08540
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Deployment of Transformer models on edge devices is becoming increasingly challenging due to the exponentially growing inference cost that scales quadratically with the number of tokens in the input sequence. Token pruning is an emerging solution to address this challenge due to its ease of deployment on various Transformer backbones. However, most token pruning methods require computationally expensive fine-tuning, which is undesirable in many edge deployment cases. In this work, we propose Zero-TPrune, the first zero-shot method that considers both the importance and similarity of tokens in performing token pruning. It leverages the attention graph of pre-trained Transformer models to produce an importance distribution for tokens via our proposed Weighted Page Rank (WPR) algorithm. This distribution further guides token partitioning for efficient similarity-based pruning. Due to the elimination of the fine-tuning overhead, Zero-TPrune can prune large models at negligible computational cost, switch between different pruning configurations at no computational cost, and perform hyperparameter tuning efficiently. We evaluate the performance of Zero-TPrune on vision tasks by applying it to various vision Transformer backbones and testing them on ImageNet. Without any fine-tuning, Zero-TPrune reduces the FLOPs cost of DeiT-S by 34.7% and improves its throughput by 45.3% with only 0.4% accuracy loss. Compared with state-of-the-art pruning methods that require fine-tuning, Zero-TPrune not only eliminates the need for fine-tuning after pruning but also does so with only 0.1% accuracy loss. Compared with state-of-the-art fine-tuning-free pruning methods, Zero-TPrune reduces accuracy loss by up to 49% with similar FLOPs budgets. Project webpage: https://jha-lab.github.io/zerotprune.

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

- **摘要（英，原文）**:

  > Dataset pruning aims to construct a coreset capable of achieving performance comparable to the original, full dataset. Most existing dataset pruning methods rely on snapshot-based criteria to identify representative samples, often resulting in poor generalization across various pruning and cross-architecture scenarios. Recent studies have addressed this issue by expanding the scope of training dynamics considered, including factors such as forgetting event and probability change, typically using an averaging approach. However, these works struggle to integrate a broader range of training dynamics without overlooking well-generalized samples, which may not be sufficiently highlighted in an averaging manner. In this study, we propose a novel dataset pruning method termed as Temporal Dual-Depth Scoring (TDDS), to tackle this problem. TDDS utilizes a dual-depth strategy to achieve a balance between incorporating extensive training dynamics and identifying representative samples for dataset pruning. In the first depth, we estimate the series of each sample's individual contributions spanning the training progress, ensuring comprehensive integration of training dynamics. In the second depth, we focus on the variability of the sample-wise contributions identified in the first depth to highlight well-generalized samples. Extensive experiments conducted on CIFAR and ImageNet datasets verify the superiority of TDDS over previous SOTA methods. Specifically on CIFAR-100, our method achieves 54.51% accuracy with only 10% training data, surpassing random selection by 7.83% and other comparison methods by at least 12.69%.

### Masked Spatial Propagation Network for Sparsity-Adaptive Depth Refinement.
- **链接**: [arXiv:2404.19294](https://arxiv.org/abs/2404.19294) · 📚 被引 6
- **作者**: Jinyoung Jun, Jae-Han Lee, Chang-Su Kim
- **🏷️ 机构**: Korea University, Gauss Labs Inc
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > The main function of depth completion is to compensate for an insufficient and unpredictable number of sparse depth measurements of hardware sensors. However, existing research on depth completion assumes that the sparsity -- the number of points or LiDAR lines -- is fixed for training and testing. Hence, the completion performance drops severely when the number of sparse depths changes significantly. To address this issue, we propose the sparsity-adaptive depth refinement (SDR) framework, which refines monocular depth estimates using sparse depth points. For SDR, we propose the masked spatial propagation network (MSPN) to perform SDR with a varying number of sparse depths effectively by gradually propagating sparse depth information throughout the entire depth map. Experimental results demonstrate that MPSN achieves state-of-the-art performance on both SDR and conventional depth completion scenarios.

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

- **摘要（英，原文）**:

  > N:M sparsity has received increasing attention due to its remarkable performance and latency trade-off compared with structured and unstructured sparsity. However, existing N:M sparsity methods do not differentiate the relative importance of weights among blocks and leave important weights underappreciated. Besides, they directly apply N:M sparsity to the whole network, which will cause severe information loss. Thus, they are still sub-optimal. In this paper, we propose an efficient and effective Multi-Axis Query methodology, dubbed as MaxQ, to rectify these problems. During the training, MaxQ employs a dynamic approach to generate soft N:M masks, considering the weight importance across multiple axes. This method enhances the weights with more importance and ensures more effective updates. Meanwhile, a sparsity strategy that gradually increases the percentage of N:M weight blocks is applied, which allows the network to heal from the pruning-induced damage progressively. During the runtime, the N:M soft masks can be precomputed as constants and folded into weights without causing any distortion to the sparse pattern and incurring additional computational overhead. Comprehensive experiments demonstrate that MaxQ achieves consistent improvements across diverse CNN architectures in various computer vision tasks, including image classification, object detection and instance segmentation. For ResNet50 with 1:16 sparse pattern, MaxQ can achieve 74.6\% top-1 accuracy on ImageNet and improve by over 2.8\% over the state-of-the-art. Codes and checkpoints are available at \url{https://github.com/JingyangXiang/MaxQ}.

### UniPTS: A Unified Framework for Proficient Post-Training Sparsity.
- **链接**: [arXiv:2405.18810](https://arxiv.org/abs/2405.18810)
- **作者**: Jingjing Xie, Yuxin Zhang, Mingbao Lin, Zhihang Lin, Liujuan Cao, Rongrong Ji
- **🏷️ 机构**: Efficient Computing, Ministry of Education of China, School of Informatics, Xiamen University,Key Laboratory of Multimedia Trusted Perception, Tencent Youtu Lab
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Post-training Sparsity (PTS) is a recently emerged avenue that chases efficient network sparsity with limited data in need. Existing PTS methods, however, undergo significant performance degradation compared with traditional methods that retrain the sparse networks via the whole dataset, especially at high sparsity ratios. In this paper, we attempt to reconcile this disparity by transposing three cardinal factors that profoundly alter the performance of conventional sparsity into the context of PTS. Our endeavors particularly comprise (1) A base-decayed sparsity objective that promotes efficient knowledge transferring from dense network to the sparse counterpart. (2) A reducing-regrowing search algorithm designed to ascertain the optimal sparsity distribution while circumventing overfitting to the small calibration set in PTS. (3) The employment of dynamic sparse training predicated on the preceding aspects, aimed at comprehensively optimizing the sparsity structure while ensuring training stability. Our proposed framework, termed UniPTS, is validated to be much superior to existing PTS methods across extensive benchmarks. As an illustration, it amplifies the performance of POT, a recently proposed recipe, from 3.9% to 68.6% when pruning ResNet-50 at 90% sparsity ratio on ImageNet. We release the code of our paper at https://github.com/xjjxmu/UniPTS.

## 跨领域论文（完整笔记在其他领域）

- Weak-to-Strong 3D Object Detection with X-Ray Distillation. → [3d-detection](../3d-detection/Guideline%202024.md)
- GAFusion: Adaptive Fusing LiDAR and Camera with Multiple Guidance for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- Commonsense Prototype for Outdoor Unsupervised 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- Improving Distant 3D Object Detection Using 2D Box Supervision. → [3d-detection](../3d-detection/Guideline%202024.md)
- CaKDP: Category-Aware Knowledge Distillation and Pruning Framework for Lightweight 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- Differentiable Information Bottleneck for Deterministic Multi-View Clustering. → [multi-camera-perception](../multi-camera-perception/Guideline%202024.md)
- MADTP: Multimodal Alignment-Guided Dynamic Token Pruning for Accelerating Vision-Language Transformer. → [multimodal](../multimodal/Guideline%202024.md)
- MULTIFLOW: Shifting Towards Task-Agnostic Vision-Language Pruning. → [multimodal](../multimodal/Guideline%202024.md)
- Sieve: Multimodal Dataset Pruning Using Image Captioning Models. → [multimodal](../multimodal/Guideline%202024.md)
- Multimodal Industrial Anomaly Detection by Crossmodal Feature Mapping. → [multimodal](../multimodal/Guideline%202024.md)
- Cloud-Device Collaborative Learning for Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202024.md)
- Towards Backward-Compatible Continual Learning of Image Compression. → [continual-learning](../continual-learning/Guideline%202024.md)
