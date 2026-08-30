# Neural Architecture Search — 2024 Guideline

> 领域: 神经架构搜索（NAS、Zero-Cost、搜索空间）
> 论文数: 3 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份:

### Auto-GAS: Automated Proxy Discovery for Training-Free Generative Architecture Search. **⭐⭐** (相关度: 25%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72652-1_3) · 📚 被引 14
- **作者**: Lujun Li, Haosen Sun, Shiwen Li, Peijie Dong, Wenhan Luo, Wei Xue et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024
- **摘要（中）**: ①针对生成式架构搜索中训练成本高的问题。②提出了Auto-GAS，自动发现训练无关的代理指标，用于生成式架构搜索。③相比手工设计代理指标，该方法通过自动化发现提高搜索效率。④摘要未提供具体数据，效果未知。
- **摘要（英）**: This paper addresses the high training cost in generative architecture search. It proposes Auto-GAS, which automatically discovers training-free proxies for generative architecture search. Compared to hand-crafted proxies, it improves search efficiency, though no specific results are provided.
- **核心贡献**: 提出自动发现训练无关代理指标的方法。
- **创新点**: 将代理发现自动化应用于生成式NAS。
- **结果**: 效果未明确报告。

### Auto-DAS: Automated Proxy Discovery for Training-Free Distillation-Aware Architecture Search. **⭐⭐** (相关度: 25%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72652-1_4) · 📚 被引 5
- **作者**: Haosen Sun, Lujun Li, Peijie Dong, Zimian Wei, Shitong Shao
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024
- **摘要（中）**: ①针对蒸馏感知架构搜索中代理指标设计困难的问题。②提出了Auto-DAS，自动发现训练无关的代理指标，用于蒸馏感知的架构搜索。③相比手工设计，该方法自动化代理发现，提升搜索效率。④摘要未提供具体数据，效果未知。
- **摘要（英）**: This paper addresses the difficulty of designing proxies in distillation-aware architecture search. It proposes Auto-DAS, which automatically discovers training-free proxies for distillation-aware NAS. Compared to manual design, it automates proxy discovery, though no specific results are provided.
- **核心贡献**: 提出自动发现蒸馏感知NAS代理指标的方法。
- **创新点**: 将代理发现自动化应用于蒸馏感知NAS。
- **结果**: 效果未明确报告。

### SNED: Superposition Network Architecture Search for Efficient Video Diffusion Model. **⭐⭐** (相关度: 15%)
- **链接**: [arXiv:2406.00195](https://arxiv.org/abs/2406.00195)
- **作者**: Zhengang Li, Yan Kang, Yuchen Liu, Difan Liu, Tobias Hinz, Feng Liu et al.
- **🏷️ 机构**: Northeastern University, Adobe Research, Adobe
- **会议**: CVPR 2024
- **摘要（中）**: ①针对视频扩散模型架构复杂、计算需求高，难以应用于实际的问题。②提出SNED方法，采用超级网络训练范式，支持多种模型成本和分辨率选项，并引入训练采样预热优化。③相比现有视频扩散模型，通过权重共享实现高效架构搜索，适用于像素空间和潜空间模型。④实验表明SNED在不同分辨率和模型选项下均能生成一致的高质量视频，同时保持高效率。
- **摘要（英）**: This paper addresses the high computational cost of video diffusion models by proposing SNED, a superposition network architecture search method. It uses a supernet training paradigm with weight sharing and a sampling warm-up strategy to efficiently search across resolutions and model costs. Experiments demonstrate consistent video generation quality across 64x64 to 256x256 resolutions with high efficiency.
- **核心贡献**: 提出SNED方法，实现高效视频扩散模型的架构搜索。
- **创新点**: 采用超级网络和权重共享支持多分辨率视频生成。
- **结果**: 在多种分辨率下生成一致视频，显著提升效率。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While AI-generated content has garnered significant attention, achieving photo-realistic video synthesis remains a formidable challenge. Despite the promising advances in diffusion models for video generation quality, the complex model architecture and substantial computational demands for both training and inference create a significant gap between these models and real-world applications. This paper presents SNED, a superposition network architecture search method for efficient video diffusion model. Our method employs a supernet training paradigm that targets various model cost and resolution options using a weight-sharing method. Moreover, we propose the supernet training sampling warm-up for fast training optimization. To showcase the flexibility of our method, we conduct experiments involving both pixel-space and latent-space video diffusion models. The results demonstrate that our framework consistently produces comparable results across different model options with high efficiency. According to the experiment for the pixel-space video diffusion model, we can achieve consistent video generation results simultaneously across 64 x 64 to 256 x 256 resolutions with a large range of model sizes from 640M to 1.6B number of parameters for pixel-space video diffusion models.

</details>

## 🆕 增量新增

### Vision Transformer Neural Architecture Search for Out-of-Distribution Generalization: Benchmark and Insights. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2501.03782](https://arxiv.org/abs/2501.03782) · 📚 被引 2
- **作者**: Sy-Tuyen Ho, Tuan Van Vo, Somayeh Ebrahimkhani, Ngai-Man Cheung
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024
- **摘要（中）**: ①针对视觉Transformer（ViT）在真实场景中面对分布外（OoD）数据时泛化能力不足，且缺乏系统研究架构设计对OoD泛化影响的问题。②构建了首个面向OoD泛化的ViT神经架构搜索基准OoD-ViT-NAS，包含3000个不同计算预算的ViT架构，并在8个常见OoD数据集上评估。③通过基准分析发现ViT架构设计显著影响OoD泛化，且ID准确率不能可靠预测OoD准确率；首次研究了9种免训练NAS方法在ViT OoD鲁棒性上的表现。④结果显示现有免训练NAS方法在预测OoD准确率上效果不佳，而简单代理如Param或Flop反而优于复杂方法。
- **摘要（英）**: This paper addresses the critical gap in understanding how ViT architecture design affects out-of-distribution (OoD) generalization by introducing OoD-ViT-NAS, the first systematic benchmark with 3000 ViT architectures evaluated on 8 OoD datasets. Key findings reveal that architecture design significantly impacts OoD generalization, ID accuracy is a poor proxy for OoD accuracy, and existing training-free NAS methods fail to predict OoD performance, with simple proxies like Param or Flop surprisingly outperforming them.
- **核心贡献**: 构建了首个面向OoD泛化的ViT NAS基准，并系统分析了架构设计与OoD鲁棒性的关系。
- **创新点**: 首次将NAS研究扩展到ViT的OoD泛化场景，并揭示了免训练NAS方法在此任务上的局限性。
- **结果**: 发现简单计算代理优于复杂免训练NAS方法，为OoD鲁棒架构搜索提供了新方向。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While ViTs have achieved across machine learning tasks, deploying them in real-world scenarios faces a critical challenge: generalizing under OoD shifts. A crucial research gap exists in understanding how to design ViT architectures, both manually and automatically, for better OoD generalization. To this end, we introduce OoD-ViT-NAS, the first systematic benchmark for ViTs NAS focused on OoD generalization. This benchmark includes 3000 ViT architectures of varying computational budgets evaluated on 8 common OoD datasets. Using this benchmark, we analyze factors contributing to OoD generalization. Our findings reveal key insights. First, ViT architecture designs significantly affect OoD generalization. Second, ID accuracy is often a poor indicator of OoD accuracy, highlighting the risk of optimizing ViT architectures solely for ID performance. Third, we perform the first study of NAS for ViTs OoD robustness, analyzing 9 Training-free NAS methods. We find that existing Training-free NAS methods are largely ineffective in predicting OoD accuracy despite excelling at ID accuracy. Simple proxies like Param or Flop surprisingly outperform complex Training-free NAS methods in predicting OoD accuracy. Finally, we study how ViT architectural attributes impact OoD generalization and discover that increasing embedding dimensions generally enhances performance. Our benchmark shows that ViT architectures exhibit a wide range of OoD accuracy, with up to 11.85% improvement for some OoD shifts. This underscores the importance of studying ViT architecture design for OoD. We believe OoD-ViT-NAS can catalyze further research into how ViT designs influence OoD generalization.

</details>

### Boosting Order-Preserving and Transferability for Neural Architecture Search: A Joint Architecture Refined Search and Fine-Tuning Approach. **⭐⭐⭐** (相关度: 30%)
- **链接**: [arXiv:2403.11380](https://arxiv.org/abs/2403.11380) · 📚 被引 5
- **作者**: Beichen Zhang, Xiaoxing Wang, Xiaohan Qin, Junchi Yan
- **🏷️ 机构**: Shanghai Jiao Tong University,Department of Computer Science and Engineering &#x0026; MoE Key Lab of AI
- **会议**: CVPR 2024
- **摘要（中）**: ①针对两阶段NAS方法中超级网络对候选架构排序的局部保序性不足，导致搜索到的最优架构并非真正最优的问题。②提出Supernet Shifting概念，将架构搜索与超级网络微调相结合，在搜索过程中累积训练损失并每轮更新超级网络，使搜索偏向于高性能架构。③相比传统两阶段方法，通过动态调整超级网络权重，提升了对顶级架构的局部排序一致性。④实验表明该方法在多个数据集上提升了搜索架构的性能和排序质量。
- **摘要（英）**: This paper addresses the issue of insufficient local order-preserving ability in two-stage NAS methods, where supernet rankings of top architectures may not align with true performance. It proposes Supernet Shifting, a strategy that integrates architecture search with supernet fine-tuning by accumulating training loss and updating the supernet during search, thereby improving local ranking consistency. Experiments demonstrate enhanced performance and ranking quality on multiple benchmarks.
- **核心贡献**: 提出Supernet Shifting方法，通过联合搜索与微调提升超级网络的局部保序能力。
- **创新点**: 将架构搜索与超级网络微调动态结合，使搜索过程自适应聚焦于高性能架构。
- **结果**: 在多个数据集上提升了架构搜索的排序质量和最终性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Supernet is a core component in many recent Neural Architecture Search (NAS) methods. It not only helps embody the search space but also provides a (relative) estimation of the final performance of candidate architectures. Thus, it is critical that the top architectures ranked by a supernet should be consistent with those ranked by true performance, which is known as the order-preserving ability. In this work, we analyze the order-preserving ability on the whole search space (global) and a sub-space of top architectures (local), and empirically show that the local order-preserving for current two-stage NAS methods still need to be improved. To rectify this, we propose a novel concept of Supernet Shifting, a refined search strategy combining architecture searching with supernet fine-tuning. Specifically, apart from evaluating, the training loss is also accumulated in searching and the supernet is updated every iteration. Since superior architectures are sampled more frequently in evolutionary searching, the supernet is encouraged to focus on top architectures, thus improving local order-preserving. Besides, a pre-trained supernet is often un-reusable for one-shot methods. We show that Supernet Shifting can fulfill transferring supernet to a new dataset. Specifically, the last classifier layer will be unset and trained through evolutionary searching. Comprehensive experiments show that our method has better order-preserving ability and can find a dominating architecture. Moreover, the pre-trained supernet can be easily transferred into a new dataset with no loss of performance.

</details>

### Towards Accurate and Robust Architectures via Neural Architecture Search. **⭐⭐⭐** (相关度: 25%)
- **链接**: [arXiv:2405.05502](https://arxiv.org/abs/2405.05502) · 📚 被引 11
- **作者**: Yuwei Ou, Yuqi Feng, Yanan Sun
- **🏷️ 机构**: College of Computer Science, Sichuan University
- **会议**: CVPR 2024
- **摘要（中）**: ①针对对抗训练中模型架构限制了准确性和鲁棒性的问题，现有方法仅调整权重连接而忽略架构影响。②提出ARNAS方法，设计准确且鲁棒的搜索空间，并采用可微分的多目标搜索策略，同时优化自然损失和对抗损失。③相比传统对抗训练，通过架构搜索在敏感位置部署合适结构，同时提升准确性和鲁棒性。④在白盒攻击、黑盒攻击和迁移性实验中均取得优于基线方法的结果。
- **摘要（英）**: This work tackles the limitation that adversarial training performance is constrained by the network architecture, proposing ARNAS to search for accurate and robust architectures. It designs a specialized search space and uses a differentiable multi-objective strategy to optimize both natural and adversarial losses. Experiments show improved accuracy and robustness under white-box, black-box, and transfer attacks.
- **核心贡献**: 提出ARNAS方法，通过架构搜索同时优化模型的准确性和鲁棒性。
- **创新点**: 设计多目标可微分搜索策略，联合优化自然损失和对抗损失。
- **结果**: 在多种攻击场景下显著提升了模型的准确性和鲁棒性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> To defend deep neural networks from adversarial attacks, adversarial training has been drawing increasing attention for its effectiveness. However, the accuracy and robustness resulting from the adversarial training are limited by the architecture, because adversarial training improves accuracy and robustness by adjusting the weight connection affiliated to the architecture. In this work, we propose ARNAS to search for accurate and robust architectures for adversarial training. First we design an accurate and robust search space, in which the placement of the cells and the proportional relationship of the filter numbers are carefully determined. With the design, the architectures can obtain both accuracy and robustness by deploying accurate and robust structures to their sensitive positions, respectively. Then we propose a differentiable multi-objective search strategy, performing gradient descent towards directions that are beneficial for both natural loss and adversarial loss, thus the accuracy and robustness can be guaranteed at the same time. We conduct comprehensive experiments in terms of white-box attacks, black-box attacks, and transferability. Experimental results show that the searched architecture has the strongest robustness with the competitive accuracy, and breaks the traditional idea that NAS-based architectures cannot transfer well to complex tasks in robustness scenarios. By analyzing outstanding architectures searched, we also conclude that accurate and robust neural architectures tend to deploy different structures near the input and output, which has great practical significance on both hand-crafting and automatically designing of accurate and robust architectures.

</details>

### Insights from the Use of Previously Unseen Neural Architecture Search Datasets. **⭐⭐** (相关度: 20%)
- **链接**: [arXiv:2404.02189](https://arxiv.org/abs/2404.02189)
- **作者**: Rob Geada, David Towers, Matthew Forshaw, Amir Atapour-Abarghouei, A. Stephen McGough
- **🏷️ 机构**: Newcastle University,UK-, Durham University,UK-
- **会议**: CVPR 2024
- **摘要（中）**: ①针对NAS研究过度依赖少数标准数据集，缺乏对真实世界问题的代表性。②引入八个新数据集（如AddNIST、Language等）用于NAS挑战，并报告标准深度学习方法和挑战参与者的最佳结果。③相比现有工作，这些数据集覆盖多样任务，鼓励开发者在未知数据集上评估模型泛化能力。④实验表明这些数据集能有效暴露NAS方法的不足，推动更鲁棒的方法发展。
- **摘要（英）**: This paper addresses the lack of diverse benchmarks in NAS research by introducing eight new datasets for NAS challenges, covering various tasks. It presents baseline results from standard deep learning methods and challenge participants, highlighting the need for models that generalize to unseen datasets. The datasets aim to steer NAS development toward more robust and practical solutions.
- **核心贡献**: 引入八个新NAS数据集，促进模型泛化能力评估。
- **创新点**: 设计多样化的挑战数据集，模拟真实世界问题。
- **结果**: 通过挑战赛揭示了现有NAS方法的局限性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The boundless possibility of neural networks which can be used to solve a problem -- each with different performance -- leads to a situation where a Deep Learning expert is required to identify the best neural network. This goes against the hope of removing the need for experts. Neural Architecture Search (NAS) offers a solution to this by automatically identifying the best architecture. However, to date, NAS work has focused on a small set of datasets which we argue are not representative of real-world problems. We introduce eight new datasets created for a series of NAS Challenges: AddNIST, Language, MultNIST, CIFARTile, Gutenberg, Isabella, GeoClassing, and Chesseract. These datasets and challenges are developed to direct attention to issues in NAS development and to encourage authors to consider how their models will perform on datasets unknown to them at development time. We present experimentation using standard Deep Learning methods as well as the best results from challenge participants.

</details>

### AZ-NAS: Assembling Zero-Cost Proxies for Network Architecture Search. **⭐⭐⭐** (相关度: 25%)
- **链接**: [arXiv:2403.19232](https://arxiv.org/abs/2403.19232) · 📚 被引 33
- **作者**: Junghyup Lee, Bumsub Ham
- **🏷️ 机构**: Yonsei University
- **会议**: CVPR 2024
- **摘要（中）**: ①针对训练-free NAS方法中零成本代理与最终性能相关性弱的问题。②提出AZ-NAS方法，集成多个零成本代理（表达性、进展性、可训练性、复杂性），通过非线性排序聚合方法提升排序相关性。③相比单一代理，多代理互补分析架构特征，且可在单次前向反向传播中同时获取。④实验表明AZ-NAS在多个搜索空间上显著提升了排序相关性和搜索效率。
- **摘要（英）**: This paper addresses the weak correlation between zero-cost proxies and final performance in training-free NAS. It proposes AZ-NAS, which ensembles four novel complementary proxies and uses a non-linear ranking aggregation method to improve ranking accuracy. Experiments show significant improvements in correlation and efficiency across multiple search spaces.
- **核心贡献**: 提出AZ-NAS，通过集成零成本代理提升NAS排序相关性。
- **创新点**: 设计四个互补代理并采用非线性聚合方法。
- **结果**: 在多个搜索空间上显著提升了排序相关性和搜索效率。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Training-free network architecture search (NAS) aims to discover high-performing networks with zero-cost proxies, capturing network characteristics related to the final performance. However, network rankings estimated by previous training-free NAS methods have shown weak correlations with the performance. To address this issue, we propose AZ-NAS, a novel approach that leverages the ensemble of various zero-cost proxies to enhance the correlation between a predicted ranking of networks and the ground truth substantially in terms of the performance. To achieve this, we introduce four novel zero-cost proxies that are complementary to each other, analyzing distinct traits of architectures in the views of expressivity, progressivity, trainability, and complexity. The proxy scores can be obtained simultaneously within a single forward and backward pass, making an overall NAS process highly efficient. In order to integrate the rankings predicted by our proxies effectively, we introduce a non-linear ranking aggregation method that highlights the networks highly-ranked consistently across all the proxies. Experimental results conclusively demonstrate the efficacy and efficiency of AZ-NAS, outperforming state-of-the-art methods on standard benchmarks, all while maintaining a reasonable runtime cost.

</details>

### SuperFedNAS: Cost-Efficient Federated Neural Architecture Search for On-device Inference. **⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72986-7_10) · 📚 被引 3
- **作者**: Alind Khare, Animesh Agrawal, Aditya Annavajjala, Payman Behnam, Myungjin Lee, Hugo Latapie et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024
- **摘要（中）**: ①针对联邦学习场景下，在设备端进行神经架构搜索（NAS）时面临的计算和通信开销过高的问题。②提出了SuperFedNAS，一种成本高效的联邦NAS方法，旨在优化设备端推理的架构搜索过程。③通过设计高效的搜索策略和联邦聚合机制，减少了通信轮次和计算负担，同时保持模型性能。④实验表明该方法在降低开销的同时，搜索到的架构在设备端推理任务上取得了有竞争力的准确率。
- **摘要（英）**: This paper tackles the high computational and communication costs of neural architecture search (NAS) in federated learning for on-device inference. SuperFedNAS introduces a cost-efficient search strategy and federated aggregation mechanism to reduce overhead while maintaining competitive accuracy, demonstrating effectiveness in resource-constrained federated settings.
- **核心贡献**: 提出了一种成本高效的联邦NAS方法SuperFedNAS，显著降低设备端搜索开销。
- **创新点**: 结合联邦学习特性设计搜索与聚合策略，实现通信与计算效率的平衡。
- **结果**: 在降低开销的同时保持了有竞争力的模型性能。

### Dependency-Aware Differentiable Neural Architecture Search. **⭐⭐⭐** (相关度: 45%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73001-6_13)
- **作者**: Buang Zhang, Xinle Wu, Hao Miao, Chenjuan Guo, Bin Yang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024
- **摘要（中）**: ①针对可微分架构搜索（DARTS）中忽略架构单元间依赖关系，导致搜索不稳定和性能退化的问题。②提出了依赖感知的可微分架构搜索方法，在搜索过程中显式建模不同架构操作间的依赖。③通过引入依赖建模，提高了搜索的稳定性和最终架构的性能。④实验表明该方法在多个基准数据集上优于标准DARTS及其变体。
- **摘要（英）**: This paper addresses the instability and performance degradation in differentiable architecture search (DARTS) caused by ignoring dependencies between architecture operations. A dependency-aware approach explicitly models these dependencies during search, improving stability and final performance, with experiments showing superiority over standard DARTS variants.
- **核心贡献**: 提出了依赖感知的可微分架构搜索方法，建模操作间依赖。
- **创新点**: 在DARTS中引入依赖建模机制。
- **结果**: 在多个基准上优于标准DARTS。

### Masked Distillation Advances Self-Supervised Transformer Architecture Search. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://openreview.net/forum?id=LUpC8KTvdV)
- **作者**: Caixia Yan, Xiaojun Chang, Zhihui Li, Lina Yao, Minnan Luo, Qinghua Zheng
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024
- **摘要（中）**: ①针对自监督视觉Transformer架构搜索中，现有方法依赖监督信号或代理任务，导致搜索效率低且泛化性差的问题。②提出了掩码蒸馏方法，利用自监督预训练中的掩码机制来指导Transformer架构搜索，无需标签。③通过掩码蒸馏，将自监督知识有效传递到架构搜索过程，提升了搜索效率和架构质量。④实验表明该方法在多个视觉任务上搜索到的架构性能优于现有自监督NAS方法，且计算成本更低。
- **摘要（英）**: This paper addresses the inefficiency and poor generalization of self-supervised vision Transformer architecture search by proposing a masked distillation method that leverages masking mechanisms from self-supervised pretraining to guide search without labels. This approach effectively transfers self-supervised knowledge, improving search efficiency and architecture quality, with experiments showing superior performance over existing self-supervised NAS methods at lower cost.
- **核心贡献**: 提出了掩码蒸馏方法，推进自监督Transformer架构搜索。
- **创新点**: 利用掩码机制实现无监督知识蒸馏指导NAS。
- **结果**: 在多个视觉任务上优于现有自监督NAS方法，且成本更低。

### Robustifying and Boosting Training-Free Neural Architecture Search. **⭐⭐⭐** (相关度: 20%)
- **链接**: [arXiv:2403.07591](https://arxiv.org/abs/2403.07591)
- **作者**: Zhenfeng He, Yao Shu, Zhongxiang Dai, Bryan Kian Hsiang Low
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024
- **摘要（中）**: ①针对训练-free NAS中单一指标在不同任务上估计能力不稳定、且与真实性能存在差距的问题。②提出RoBoT算法，通过贝叶斯优化组合现有训练-free指标，形成鲁棒且更优的复合指标，并利用贪心搜索（利用）来弥合估计差距。③改进点在于将多指标融合与搜索策略结合，提升跨任务鲁棒性和搜索性能。④实验表明在多个NAS基准上，RoBoT相比单一指标和现有方法显著提升了搜索性能，但摘要未给出具体数值。
- **摘要（英）**: This paper addresses the instability of single training-free metrics across tasks and the estimation gap in training-free NAS. It proposes RoBoT, which combines existing metrics via Bayesian optimization and applies greedy search to boost performance. The method improves robustness and search efficacy on diverse NAS benchmarks, though specific numerical gains are not detailed in the abstract.
- **核心贡献**: 提出了一种通过贝叶斯优化组合训练-free指标并利用贪心搜索提升NAS性能的算法RoBoT。
- **创新点**: 创新性地将多指标融合与搜索利用策略结合，解决了训练-free NAS的鲁棒性和性能瓶颈。
- **结果**: 在多个NAS基准上取得了优于单一指标和现有方法的搜索性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural architecture search (NAS) has become a key component of AutoML and a standard tool to automate the design of deep neural networks. Recently, training-free NAS as an emerging paradigm has successfully reduced the search costs of standard training-based NAS by estimating the true architecture performance with only training-free metrics. Nevertheless, the estimation ability of these metrics typically varies across different tasks, making it challenging to achieve robust and consistently good search performance on diverse tasks with only a single training-free metric. Meanwhile, the estimation gap between training-free metrics and the true architecture performances limits training-free NAS to achieve superior performance. To address these challenges, we propose the robustifying and boosting training-free NAS (RoBoT) algorithm which (a) employs the optimized combination of existing training-free metrics explored from Bayesian optimization to develop a robust and consistently better-performing metric on diverse tasks, and (b) applies greedy search, i.e., the exploitation, on the newly developed metric to bridge the aforementioned gap and consequently to boost the search performance of standard training-free NAS further. Remarkably, the expected performance of our RoBoT can be theoretically guaranteed, which improves over the existing training-free NAS under mild conditions with additional interesting insights. Our extensive experiments on various NAS benchmark tasks yield substantial empirical evidence to support our theoretical results.

</details>

### Curriculum reinforcement learning for quantum architecture search under hardware errors. **⭐⭐** (相关度: 10%)
- **链接**: [arXiv:2402.03500](https://arxiv.org/abs/2402.03500)
- **作者**: Yash J. Patel, Akash Kundu, Mateusz Ostaszewski, Xavier Bonet-Monroig, Vedran Dunjko, Onur Danaci
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024
- **摘要（中）**: ①针对量子架构搜索在硬件噪声下性能受影响的问题。②提出基于课程学习的强化学习量子架构搜索算法（CRLQAS），引入3D架构编码和环境动态限制来探索电路架构空间。③改进点在于将课程学习引入强化学习，以应对噪声环境下的搜索挑战。④摘要未提供具体实验数据，但声称能有效处理真实VQA部署中的噪声问题。
- **摘要（英）**: This work tackles the challenge of quantum architecture search under hardware noise. It introduces CRLQAS, a curriculum-based reinforcement learning algorithm with 3D encoding and restricted environment dynamics. The method aims to improve search robustness in noisy settings, though no quantitative results are provided in the abstract.
- **核心贡献**: 提出了首个结合课程学习的强化学习量子架构搜索算法，以应对硬件噪声。
- **创新点**: 将课程学习策略引入量子架构搜索，创新性地处理噪声环境下的搜索问题。
- **结果**: 摘要未给出具体效果数据，但声称能提升噪声下的架构搜索性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The key challenge in the noisy intermediate-scale quantum era is finding useful circuits compatible with current device limitations. Variational quantum algorithms (VQAs) offer a potential solution by fixing the circuit architecture and optimizing individual gate parameters in an external loop. However, parameter optimization can become intractable, and the overall performance of the algorithm depends heavily on the initially chosen circuit architecture. Several quantum architecture search (QAS) algorithms have been developed to design useful circuit architectures automatically. In the case of parameter optimization alone, noise effects have been observed to dramatically influence the performance of the optimizer and final outcomes, which is a key line of study. However, the effects of noise on the architecture search, which could be just as critical, are poorly understood. This work addresses this gap by introducing a curriculum-based reinforcement learning QAS (CRLQAS) algorithm designed to tackle challenges in realistic VQA deployment. The algorithm incorporates (i) a 3D architecture encoding and restrictions on environment dynamics to explore the search space of possible circuits efficiently, (ii) an episode halting scheme to steer the agent to find shorter circuits, and (iii) a novel variant of simultaneous perturbation stochastic approximation as an optimizer for faster convergence. To facilitate studies, we developed an optimized simulator for our algorithm, significantly improving computational efficiency in simulating noisy quantum circuits by employing the Pauli-transfer matrix formalism in the Pauli-Liouville basis. Numerical experiments focusing on quantum chemistry tasks demonstrate that CRLQAS outperforms existing QAS algorithms across several metrics in both noiseless and noisy environments.

</details>

### Encodings for Prediction-based Neural Architecture Search. **⭐⭐⭐⭐** (相关度: 30%)
- **链接**: [arXiv:2403.02484](https://arxiv.org/abs/2403.02484)
- **作者**: Yash Akhauri, Mohamed S. Abdelfattah
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024
- **摘要（中）**: ①针对预测器-based NAS中架构编码方式对预测器性能影响显著的问题。②系统分类并研究了结构、学习和基于分数的三类编码，并引入统一编码以支持多搜索空间，提出FLAN预测器（Flow Attention for NAS）。③改进点在于统一编码和注意力机制的结合，实现了跨搜索空间的迁移学习。④在超过150万架构上实验，FLAN将训练成本降低了一个数量级以上，但具体精度数据未在摘要中给出。
- **摘要（英）**: This paper investigates neural architecture encodings for predictor-based NAS, categorizing them into structural, learned, and score-based types, and introduces unified encodings for multi-search-space support. It proposes FLAN, a flow attention predictor that integrates key insights, achieving over an order of magnitude cost reduction on 1.5 million architectures. The work provides a comprehensive empirical study across multiple NAS benchmarks.
- **核心贡献**: 系统分类了NAS编码方法，并提出了支持多搜索空间的统一编码和FLAN预测器。
- **创新点**: 创新性地引入统一编码和流注意力机制，实现了跨搜索空间的预测器迁移。
- **结果**: 在多个NAS基准上，FLAN将训练成本降低了一个数量级以上。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Predictor-based methods have substantially enhanced Neural Architecture Search (NAS) optimization. The efficacy of these predictors is largely influenced by the method of encoding neural network architectures. While traditional encodings used an adjacency matrix describing the graph structure of a neural network, novel encodings embrace a variety of approaches from unsupervised pretraining of latent representations to vectors of zero-cost proxies. In this paper, we categorize and investigate neural encodings from three main types: structural, learned, and score-based. Furthermore, we extend these encodings and introduce \textit{unified encodings}, that extend NAS predictors to multiple search spaces. Our analysis draws from experiments conducted on over 1.5 million neural network architectures on NAS spaces such as NASBench-101 (NB101), NB201, NB301, Network Design Spaces (NDS), and TransNASBench-101. Building on our study, we present our predictor \textbf{FLAN}: \textbf{Fl}ow \textbf{A}ttention for \textbf{N}AS. FLAN integrates critical insights on predictor design, transfer learning, and \textit{unified encodings} to enable more than an order of magnitude cost reduction for training NAS accuracy predictors. Our implementation and encodings for all neural networks are open-sourced at \href{https://github.com/abdelfattah-lab/flan_nas}{https://github.com/abdelfattah-lab/flan\_nas}.

</details>

### Towards Neural Architecture Search through Hierarchical Generative Modeling. **⭐⭐** (相关度: 15%)
- **链接**: [出版页](https://proceedings.mlr.press/v235/xiang24a.html)
- **作者**: Lichuan Xiang, Lukasz Dudziak, Mohamed S. Abdelfattah, Abhinav Mehrotra, Nicholas Donald Lane, Hongkai Wen
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024
- **摘要（中）**: ①针对神经架构搜索中搜索空间复杂性和计算成本高的问题。②提出通过层次生成建模来探索架构搜索空间，但摘要内容缺失，无法提供具体方法细节。③改进点可能在于利用生成模型捕捉架构的层次结构。④由于摘要缺失，无法评估具体效果。
- **摘要（英）**: This paper proposes a hierarchical generative modeling approach for neural architecture search, but the abstract is incomplete, lacking methodological details and experimental results. The potential contribution lies in leveraging generative models to capture hierarchical structures in architecture spaces.
- **核心贡献**: 提出了基于层次生成建模的NAS方法，但细节未公开。
- **创新点**: 可能创新点在于层次化生成模型的应用，但缺乏验证。
- **结果**: 未提供实验数据。

### Disentangled Continual Graph Neural Architecture Search with Invariant Modular Supernet. **⭐⭐** (相关度: 15%)
- **链接**: [出版页](https://proceedings.mlr.press/v235/zhang24bm.html)
- **作者**: Zeyang Zhang, Xin Wang, Yijian Qin, Hong Chen, Ziwei Zhang, Xu Chu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024
- **摘要（中）**: ①针对持续学习场景下神经架构搜索的挑战，如灾难性遗忘和架构适应性。②提出解耦的持续图神经架构搜索方法，结合不变模块化超网络，但摘要内容缺失。③改进点可能在于解耦设计和模块化超网络以支持持续学习。④由于摘要缺失，无法评估具体效果。
- **摘要（英）**: This paper addresses continual learning in neural architecture search, proposing a disentangled approach with invariant modular supernets. However, the abstract is incomplete, lacking details on methodology and results. The potential contribution is in handling catastrophic forgetting and architecture adaptation in dynamic environments.
- **核心贡献**: 提出了持续图NAS方法，但细节未公开。
- **创新点**: 可能创新点在于解耦和模块化超网络设计，但缺乏验证。
- **结果**: 未提供实验数据。

### MOTE-NAS: Multi-Objective Training-based Estimate for Efficient Neural Architecture Search. **⭐⭐⭐** (相关度: 20%)
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/b6e118c759c16f2424997bbb6a1ffd61-Abstract-Conference.html)
- **作者**: Yuming Zhang, Jun-Wei Hsieh, Xin Li, Ming-Ching Chang, Chun-Chieh Lee, Kuo-Chin Fan
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024
- **摘要（中）**: ①针对NAS中多目标优化（如精度与效率）的平衡问题。②提出MOTE-NAS，一种基于训练的多目标估计方法，用于高效NAS。③改进点在于将多目标估计融入训练过程，提升搜索效率。④摘要未提供具体数据，但声称能实现高效的多目标NAS。
- **摘要（英）**: This paper proposes MOTE-NAS, a multi-objective training-based estimation method for efficient neural architecture search. It integrates multi-objective considerations into the training process to balance accuracy and efficiency. The abstract lacks quantitative results but claims improved search efficiency.
- **核心贡献**: 提出了基于训练的多目标估计NAS方法MOTE-NAS。
- **创新点**: 创新性地将多目标估计融入训练过程，提升搜索效率。
- **结果**: 摘要未给出具体效果数据。

### CE-NAS: An End-to-End Carbon-Efficient Neural Architecture Search Framework. **⭐⭐⭐** (相关度: 40%)
- **链接**: [arXiv:2406.01414](https://arxiv.org/abs/2406.01414) · 📚 被引 2
- **作者**: Yiyang Zhao, Yunzhuo Liu, Bo Jiang, Tian Guo
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024
- **摘要（中）**: ①这篇论文针对神经网络架构搜索（NAS）过程中高碳排放的问题，旨在提高模型设计过程的碳效率。②提出了CE-NAS框架，利用强化学习代理根据时间序列Transformer预测的碳强度动态调整GPU资源，以平衡能量高效的采样和能量密集的评估任务，并采用多目标优化器减少搜索空间。③相比已有NAS方法，CE-NAS首次端到端地考虑碳排放因素，结合碳强度预测和资源调度，显著降低环境成本。④在HW-NasBench数据集上，碳排放减少高达7.22倍，同时保持与原始NAS相当的搜索效率；在开放域NAS任务中，CIFAR-10上达到97.35%的top-1准确率，仅1.68M参数，碳排放38.53磅CO2；在ImageNet上取得SOTA结果。
- **摘要（英）**: This paper addresses the high carbon cost of neural architecture search (NAS) by proposing CE-NAS, a framework that uses a reinforcement learning agent to dynamically adjust GPU resources based on carbon intensity predicted by a time-series transformer, and leverages a multi-objective optimizer to reduce the search space. Compared to existing NAS methods, CE-NAS achieves up to 7.22x carbon emission reduction on HW-NasBench while maintaining search efficiency, and attains SOTA results with 97.35% top-1 accuracy on CIFAR-10 and competitive performance on ImageNet.
- **核心贡献**: 提出了一个端到端的碳高效NAS框架，通过动态资源调度和搜索空间缩减显著降低碳排放。
- **创新点**: 将碳强度预测与强化学习资源管理结合，实现碳感知的NAS过程。
- **结果**: 在多个基准上实现碳排放减少高达7.22倍，同时保持或提升搜索性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This work presents a novel approach to neural architecture search (NAS) that aims to increase carbon efficiency for the model design process. The proposed framework CE-NAS addresses the key challenge of high carbon cost associated with NAS by exploring the carbon emission variations of energy and energy differences of different NAS algorithms. At the high level, CE-NAS leverages a reinforcement-learning agent to dynamically adjust GPU resources based on carbon intensity, predicted by a time-series transformer, to balance energy-efficient sampling and energy-intensive evaluation tasks. Furthermore, CE-NAS leverages a recently proposed multi-objective optimizer to effectively reduce the NAS search space. We demonstrate the efficacy of CE-NAS in lowering carbon emissions while achieving SOTA results for both NAS datasets and open-domain NAS tasks. For example, on the HW-NasBench dataset, CE-NAS reduces carbon emissions by up to 7.22X while maintaining a search efficiency comparable to vanilla NAS. For open-domain NAS tasks, CE-NAS achieves SOTA results with 97.35% top-1 accuracy on CIFAR-10 with only 1.68M parameters and a carbon consumption of 38.53 lbs of CO2. On ImageNet, our searched model achieves 80.6% top-1 accuracy with a 0.78 ms TensorRT latency using FP16 on NVIDIA V100, consuming only 909.86 lbs of CO2, making it comparable to other one-shot-based NAS baselines.

</details>

<!-- COMPLETE v1 papers=18 -->
