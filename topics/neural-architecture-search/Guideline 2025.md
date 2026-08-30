# Neural Architecture Search — 2025 Guideline

> 领域: 神经架构搜索（NAS、Zero-Cost、搜索空间）
> 论文数: 3 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份:

### L-SWAG: Layer-Sample Wise Activation with Gradients Information for Zero-Shot NAS on Vision Transformers. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2505.07300](https://arxiv.org/abs/2505.07300) · 📚 被引 2
- **作者**: Sofia Casarin, Sergio Escalera, Oswald Lanz
- **🏷️ 机构**: Free University of Bozen-Bolzano,Bolzano,Italy, Computer Vision Center,Barcelona,Spain
- **会议**: CVPR 2025
- **摘要（中）**: 针对现有零成本NAS代理主要适用于卷积搜索空间、难以泛化到Vision Transformer（ViT）的问题，本文提出了L-SWAG指标，利用层采样激活与梯度信息来统一评估卷积和Transformer架构，并构建了基于Autoformer搜索空间的新基准。此外，作者引入LIBRA-NAS方法，通过机器学习模型组合互补的代理信息并重新对齐偏差，以进一步提升搜索性能。实验在14个任务上验证了L-SWAG的泛化性，并展示了LIBRA-NAS在ViT搜索上的优势。
- **摘要（英）**: This paper addresses the limitation of zero-cost NAS proxies that are mostly designed for convolutional search spaces and fail to generalize to Vision Transformers. It proposes L-SWAG, a novel metric leveraging layer-wise activation and gradient information to characterize both CNN and ViT architectures, along with a new Autoformer-based benchmark. To further boost performance, LIBRA-NAS is introduced to strategically combine complementary proxies via an ML model with bias re-alignment, validated across 14 tasks.
- **核心贡献**: 提出了首个适用于ViT的零成本NAS代理L-SWAG及配套基准和组合方法LIBRA-NAS。
- **创新点**: 将零成本代理从CNN扩展到ViT，并通过梯度与激活信息实现跨架构泛化。
- **结果**: 在14个任务上验证了L-SWAG的泛化性，LIBRA-NAS进一步提升了搜索性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Training-free Neural Architecture Search (NAS) efficiently identifies high-performing neural networks using zero-cost (ZC) proxies. Unlike multi-shot and one-shot NAS approaches, ZC-NAS is both (i) time-efficient, eliminating the need for model training, and (ii) interpretable, with proxy designs often theoretically grounded. Despite rapid developments in the field, current SOTA ZC proxies are typically constrained to well-established convolutional search spaces. With the rise of Large Language Models shaping the future of deep learning, this work extends ZC proxy applicability to Vision Transformers (ViTs). We present a new benchmark using the Autoformer search space evaluated on 6 distinct tasks and propose Layer-Sample Wise Activation with Gradients information (L-SWAG), a novel, generalizable metric that characterizes both convolutional and transformer architectures across 14 tasks. Additionally, previous works highlighted how different proxies contain complementary information, motivating the need for a ML model to identify useful combinations. To further enhance ZC-NAS, we therefore introduce LIBRA-NAS (Low Information gain and Bias Re-Alignment), a method that strategically combines proxies to best represent a specific benchmark. Integrated into the NAS search, LIBRA-NAS outperforms evolution and gradient-based NAS techniques by identifying an architecture with a 17.0% test error on ImageNet1k in just 0.1 GPU days.

</details>

### TF-MAS: Training-free Mamba2 Architecture Search. **⭐⭐** (相关度: 30%)
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/08561abd6843266509d95bf30b856283-Abstract-Conference.html)
- **作者**: Yi Fan, Yu-Bin Yang
- **🏷️ 机构**: Nanjing University, NanjingUniversity
- **会议**: NeurIPS 2025
- **摘要（中）**: ①针对Mamba2架构搜索中训练开销大的问题，提出无需训练的搜索方法。②通过分析Mamba2的线性注意力特性，设计代理指标直接评估候选架构性能，避免训练。③相比传统NAS方法，省去了训练成本，但缺乏对搜索空间多样性的深入探索。④摘要未提供具体数据，效果未知。
- **摘要（英）**: This paper addresses the high training cost in Mamba2 architecture search by proposing a training-free method. It uses proxy metrics based on Mamba2's linear attention properties to evaluate architectures without training. Compared to conventional NAS, it reduces computational overhead but lacks exploration of search space diversity. No specific results are reported in the abstract.
- **核心贡献**: 提出首个针对Mamba2的训练免费架构搜索框架。
- **创新点**: 利用Mamba2线性注意力特性设计无需训练的评估代理。
- **结果**: 摘要未给出量化结果，效果待验证。

### TensorRL-QAS: Reinforcement learning with tensor networks for improved quantum architecture search. **⭐⭐** (相关度: 20%)
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/af008ae1c0301e218ee89a86833198e3-Abstract-Conference.html)
- **作者**: Akash Kundu, Stefano Mangini
- **🏷️ 机构**: Delft University of Technology, University of Helsinki
- **会议**: NeurIPS 2025
- **摘要（中）**: ①针对量子架构搜索中计算复杂度和搜索效率问题，结合强化学习与张量网络。②利用张量网络压缩量子电路表示，强化学习驱动搜索过程。③相比传统量子NAS，提高了搜索效率并降低了模拟成本。④摘要未提供具体性能数据。
- **摘要（英）**: This paper addresses the computational complexity and search efficiency in quantum architecture search by combining reinforcement learning with tensor networks. Tensor networks compress quantum circuit representations, while RL drives the search. Compared to conventional quantum NAS, it improves search efficiency and reduces simulation cost. No specific results are reported.
- **核心贡献**: 提出张量网络增强的强化学习量子架构搜索方法。
- **创新点**: 将张量网络引入量子NAS以降低模拟复杂度。
- **结果**: 摘要未给出量化效果。

### Subnet-Aware Dynamic Supernet Training for Neural Architecture Search. **⭐⭐⭐⭐** (相关度: 65%)
- **链接**: [arXiv:2503.10740](https://arxiv.org/abs/2503.10740) · 📚 被引 6
- **作者**: Jeimin Jeon, Youngmin Oh, Junghyup Lee, Donghyeon Baek, Dohyung Kim, Chanho Eom et al.
- **🏷️ 机构**: Yonsei University, Samsung Research, Samsung Advanced Institute of Technology
- **会议**: CVPR 2025
- **摘要（中）**: 针对N-shot NAS中超级网络训练采用静态策略（如统一学习率调度）导致子网训练不公平和动量更新噪声大的问题，本文提出了动态超级网络训练技术。具体包括复杂度感知的学习率调度器（CaLR），根据子网复杂度自适应调整学习率衰减，缓解不公平性；以及动量分离技术（MS），将结构相似的子网分组并使用独立动量，避免噪声动量问题。该方法可低成本集成到多种N-shot NAS方法中，显著提升搜索性能。
- **摘要（英）**: This paper tackles the issues of unfair supernet training and noisy momentum updates in N-shot NAS caused by static training strategies. It introduces a complexity-aware learning rate scheduler (CaLR) that adapts LR decay to subnet complexity, and a momentum separation technique (MS) that groups similar subnets with separate momenta. The approach is plug-and-play with marginal cost and drastically improves search performance.
- **核心贡献**: 提出了动态超级网络训练方法，通过CaLR和MS分别解决不公平性和噪声动量问题。
- **创新点**: 首次将子网复杂度感知的学习率调度和动量分离引入N-shot NAS训练。
- **结果**: 在多种N-shot NAS方法上验证了显著性能提升，且额外开销极小。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> N-shot neural architecture search (NAS) exploits a supernet containing all candidate subnets for a given search space. The subnets are typically trained with a static training strategy (e.g., using the same learning rate (LR) scheduler and optimizer for all subnets). This, however, does not consider that individual subnets have distinct characteristics, leading to two problems: (1) The supernet training is biased towards the low-complexity subnets (unfairness); (2) the momentum update in the supernet is noisy (noisy momentum). We present a dynamic supernet training technique to address these problems by adjusting the training strategy adaptive to the subnets. Specifically, we introduce a complexity-aware LR scheduler (CaLR) that controls the decay ratio of LR adaptive to the complexities of subnets, which alleviates the unfairness problem. We also present a momentum separation technique (MS). It groups the subnets with similar structural characteristics and uses a separate momentum for each group, avoiding the noisy momentum problem. Our approach can be applicable to various N-shot NAS methods with marginal cost, while improving the search performance drastically. We validate the effectiveness of our approach on various search spaces (e.g., NAS-Bench-201, Mobilenet spaces) and datasets (e.g., CIFAR-10/100, ImageNet).

</details>

### Training-free Neural Architecture Search through Variance of Knowledge of Deep Network Weights. **⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2502.04975](https://arxiv.org/abs/2502.04975) · 📚 被引 4
- **作者**: Ondrej Týbl, Lukás Neumann
- **🏷️ 机构**: Czech Technical University in Prague,CMP Visual Recognition Group, Faculty of Electrical Engineering
- **会议**: CVPR 2025
- **摘要（中）**: 针对NAS中候选网络需从头训练导致计算成本高昂的问题，本文提出了一种基于Fisher信息的训练免费代理，用于估计网络在图像分类任务上的预期精度。该代理具有统计学理论基础，无需训练即可评估架构性能，显著降低NAS计算开销。在三个公开数据集和两个搜索空间上，该代理达到了最先进的性能，并提出了新的评估指标。
- **摘要（英）**: This paper proposes a training-free proxy based on Fisher Information to estimate image classification accuracy without training candidate networks, addressing the high computational cost of NAS. The proxy has strong statistical grounding and achieves state-of-the-art results on three datasets and two search spaces, with a new evaluation metric introduced.
- **核心贡献**: 提出了基于Fisher信息的训练免费NAS代理，并验证了其有效性。
- **创新点**: 将Fisher信息理论应用于零成本代理设计，提供理论支撑。
- **结果**: 在多个数据集和搜索空间上达到SOTA性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep learning has revolutionized computer vision, but it achieved its tremendous success using deep network architectures which are mostly hand-crafted and therefore likely suboptimal. Neural Architecture Search (NAS) aims to bridge this gap by following a well-defined optimization paradigm which systematically looks for the best architecture, given objective criterion such as maximal classification accuracy. The main limitation of NAS is however its astronomical computational cost, as it typically requires training each candidate network architecture from scratch. In this paper, we aim to alleviate this limitation by proposing a novel training-free proxy for image classification accuracy based on Fisher Information. The proposed proxy has a strong theoretical background in statistics and it allows estimating expected image classification accuracy of a given deep network without training the network, thus significantly reducing computational cost of standard NAS algorithms. Our training-free proxy achieves state-of-the-art results on three public datasets and in two search spaces, both when evaluated using previously proposed metrics, as well as using a new metric that we propose which we demonstrate is more informative for practical NAS applications. The source code is publicly available at http://www.github.com/ondratybl/VKDNW

</details>

### Loss Functions for Predictor-Based Neural Architecture Search. **⭐⭐⭐** (相关度: 45%)
- **链接**: [arXiv:2506.05869](https://arxiv.org/abs/2506.05869)
- **作者**: Han Ji, Yuqi Feng, Jiahao Fan, Yanan Sun
- **🏷️ 机构**: College of Computer Science, Sichuan University
- **会议**: ICCV 2025
- **摘要（中）**: ①针对NAS性能预测器中损失函数选择缺乏系统研究的问题。②首次全面研究了预测器中的损失函数，将其分为回归、排序和加权三类，并在5个搜索空间的13个任务上评估了8种损失函数。③相比以往仅关注单一损失类型，该研究揭示了不同类别损失函数可有效组合以增强预测器性能。④实验结果提供了实用的指导原则，有助于设计更有效的NAS预测器。
- **摘要（英）**: This paper presents the first comprehensive study on loss functions for NAS performance predictors, categorizing them into regression, ranking, and weighted types, and evaluating eight losses across 13 tasks and five search spaces. The findings show that combining different loss categories can enhance predictor-based NAS, offering practical guidance for predictor design.
- **核心贡献**: 首次系统评估NAS预测器中的损失函数，并给出组合建议。
- **创新点**: 对损失函数进行三分类并跨多任务全面比较。
- **结果**: 发现特定损失函数组合可提升预测器性能，提供实用指南。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Evaluation is a critical but costly procedure in neural architecture search (NAS). Performance predictors have been widely adopted to reduce evaluation costs by directly estimating architecture performance. The effectiveness of predictors is heavily influenced by the choice of loss functions. While traditional predictors employ regression loss functions to evaluate the absolute accuracy of architectures, recent approaches have explored various ranking-based loss functions, such as pairwise and listwise ranking losses, to focus on the ranking of architecture performance. Despite their success in NAS, the effectiveness and characteristics of these loss functions have not been thoroughly investigated. In this paper, we conduct the first comprehensive study on loss functions in performance predictors, categorizing them into three main types: regression, ranking, and weighted loss functions. Specifically, we assess eight loss functions using a range of NAS-relevant metrics on 13 tasks across five search spaces. Our results reveal that specific categories of loss functions can be effectively combined to enhance predictor-based NAS. Furthermore, our findings could provide practical guidance for selecting appropriate loss functions for various tasks. We hope this work provides meaningful insights to guide the development of loss functions for predictor-based methods in the NAS community.

</details>

### Neural Architecture Search Driven by Locally Guided Diffusion for Personalized Federated Learning. **⭐⭐** (相关度: 40%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00402)
- **作者**: Peng Liao, Xilu Wang, Yaochu Jin, Wenli Du, Han Hu
- **🏷️ 机构**: ECUST,Key Laboratory of Smart Manufacturing in Energy Chemical Process, Ministry of Education,Shanghai,China, Computer Science Research Centre, University of Surrey,Surrey,UK
- **会议**: ICCV 2025
- **摘要（中）**: ①针对个性化联邦学习中架构搜索的挑战，摘要缺失，无法获取具体问题和方法细节。②论文标题表明其利用局部引导扩散驱动NAS，但具体技术细节未知。③由于摘要为空，无法评估其改进点和效果。④建议查阅全文以获取完整信息。
- **摘要（英）**: This paper addresses NAS in personalized federated learning, but the abstract is missing, so specific problem formulation, methods, and results cannot be assessed. The title suggests a locally guided diffusion approach, but full details require reading the paper.
- **核心贡献**: 未知，因摘要缺失。
- **创新点**: 未知，因摘要缺失。
- **结果**: 未知，因摘要缺失。

### TRNAS: A Training-Free Robust Neural Architecture Search. **⭐⭐⭐** (相关度: 50%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00225) · 📚 被引 1
- **作者**: Yeming Yang, Qingling Zhu, Jianping Luo, Ka-Chun Wong, Qiuzhen Lin, Jianqiang Li
- **🏷️ 机构**: Shenzhen University, City University of Hong Kong
- **会议**: ICCV 2025
- **摘要（中）**: ①针对现有NAS方法在鲁棒性方面考虑不足的问题，提出训练免费的鲁棒NAS方法。②论文标题为TRNAS，但摘要缺失，具体方法细节未知。③由于摘要为空，无法评估其改进点和效果。④建议查阅全文以获取完整信息。
- **摘要（英）**: This paper proposes a training-free robust NAS method, but the abstract is missing, so specific techniques and results cannot be assessed. The title indicates a focus on robustness, but full details require reading the paper.
- **核心贡献**: 未知，因摘要缺失。
- **创新点**: 未知，因摘要缺失。
- **结果**: 未知，因摘要缺失。

### Multi-objective Differentiable Neural Architecture Search. **⭐⭐⭐⭐** (相关度: 30%)
- **链接**: [arXiv:2402.18213](https://arxiv.org/abs/2402.18213) · 📚 被引 1
- **作者**: Rhea Sanjay Sukthanker, Arber Zela, Benedikt Staffler, Samuel Dooley, Josif Grabocka, Frank Hutter
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025
- **摘要（中）**: ①针对多目标NAS中Pareto前沿求解计算成本高的问题，即需为每个硬件约束单独搜索。②提出一种编码用户偏好以权衡性能和硬件指标的NAS算法，通过超网络参数化跨设备和多目标的联合架构分布，可条件于硬件特征和偏好向量。③相比先前方法，无需为每个约束重复搜索，单次搜索即可生成代表性且多样的架构，并支持零样本迁移到新设备。④在多达19个硬件设备和3个不同目标上的实验证明了方法的有效性和可扩展性。
- **摘要（英）**: This paper addresses the high computational cost of Pareto front profiling in multi-objective NAS by proposing a novel algorithm that encodes user preferences to trade off performance and hardware metrics. It parameterizes a joint architecture distribution across devices and objectives via a hypernetwork conditioned on hardware features and preference vectors, enabling single-run search and zero-shot transfer. Experiments on up to 19 devices and 3 objectives demonstrate effectiveness and scalability.
- **核心贡献**: 提出一种单次搜索即可生成多设备Pareto最优架构的NAS方法。
- **创新点**: 利用超网络条件化硬件特征和偏好向量，实现零样本迁移。
- **结果**: 在19个硬件设备上验证了方法的有效性和可扩展性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pareto front profiling in multi-objective optimization (MOO), i.e., finding a diverse set of Pareto optimal solutions, is challenging, especially with expensive objectives that require training a neural network. Typically, in MOO for neural architecture search (NAS), we aim to balance performance and hardware metrics across devices. Prior NAS approaches simplify this task by incorporating hardware constraints into the objective function, but profiling the Pareto front necessitates a computationally expensive search for each constraint. In this work, we propose a novel NAS algorithm that encodes user preferences to trade-off performance and hardware metrics, yielding representative and diverse architectures across multiple devices in just a single search run. To this end, we parameterize the joint architectural distribution across devices and multiple objectives via a hypernetwork that can be conditioned on hardware features and preference vectors, enabling zero-shot transferability to new devices. Extensive experiments involving up to 19 hardware devices and 3 different objectives demonstrate the effectiveness and scalability of our method. Finally, we show that, without any additional costs, our method outperforms existing MOO NAS methods across a broad range of qualitatively different search spaces and datasets, including MobileNetV3 on ImageNet-1k, an encoder-decoder transformer space for machine translation and a decoder-only space for language modelling.

</details>

### RZ-NAS: Enhancing LLM-guided Neural Architecture Search via Reflective Zero-Cost Strategy. **⭐⭐⭐** (相关度: 25%)
- **链接**: [出版页](https://proceedings.mlr.press/v267/ji25a.html)
- **作者**: Zipeng Ji, Guanghui Zhu, Chunfeng Yuan, Yihua Huang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025
- **摘要（中）**: ①针对LLM引导的NAS中零成本策略评估不准确的问题。②提出反射式零成本策略（RZ-NAS），通过反思机制改进LLM的架构搜索指导。③相比现有LLM引导NAS方法，增强了搜索的鲁棒性和效率。④摘要缺失，具体效果未提供。
- **摘要（英）**: This paper tackles the inaccuracy of zero-cost strategies in LLM-guided NAS by introducing a reflective zero-cost strategy (RZ-NAS) that improves LLM-based architecture search guidance. It enhances robustness and efficiency compared to existing methods, though specific results are unavailable due to missing abstract.
- **核心贡献**: 提出反射式零成本策略以增强LLM引导的NAS。
- **创新点**: 将反思机制融入零成本评估，提升搜索指导质量。
- **结果**: 具体效果未在摘要中提供。

### An Architecture Search Framework for Inference-Time Techniques. **⭐⭐⭐** (相关度: 20%)
- **链接**: [出版页](https://proceedings.mlr.press/v267/saad-falcon25a.html)
- **作者**: Jon Saad-Falcon, Adrian Gamarra Lafuente, Shlok Natarajan, Nahum Maru, Hristo Todorov, Etash Kumar Guha et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025
- **摘要（中）**: ①针对推理时技术（如测试时增强、模型集成）的架构搜索框架缺失问题。②提出一个统一的架构搜索框架，用于自动发现最优的推理时技术组合。③相比手工设计推理策略，实现了自动化搜索。④摘要缺失，具体效果未提供。
- **摘要（英）**: This paper addresses the lack of a framework for searching inference-time techniques by proposing a unified architecture search framework to automatically discover optimal combinations. It automates the design of inference strategies, though specific results are unavailable due to missing abstract.
- **核心贡献**: 提出首个针对推理时技术的架构搜索框架。
- **创新点**: 将NAS应用于推理时策略的自动化设计。
- **结果**: 具体效果未在摘要中提供。

### Multi-agent Architecture Search via Agentic Supernet. **⭐⭐⭐** (相关度: 25%)
- **链接**: [出版页](https://proceedings.mlr.press/v267/zhang25bi.html)
- **作者**: Guibin Zhang, Luyang Niu, Junfeng Fang, Kun Wang, Lei Bai, Xiang Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025
- **摘要（中）**: ①针对多智能体系统中架构搜索的复杂性，传统NAS未考虑智能体间的交互。②提出基于智能体超网络的架构搜索方法（Agentic Supernet），联合搜索多个智能体的架构。③相比单智能体NAS，考虑了多智能体协作的架构设计。④摘要缺失，具体效果未提供。
- **摘要（英）**: This paper addresses the complexity of architecture search in multi-agent systems by proposing an agentic supernet-based method that jointly searches architectures for multiple agents. It considers inter-agent interactions, unlike single-agent NAS, though specific results are unavailable due to missing abstract.
- **核心贡献**: 提出多智能体架构搜索的Agentic Supernet方法。
- **创新点**: 通过超网络联合优化多智能体架构。
- **结果**: 具体效果未在摘要中提供。

### Puzzle: Distillation-Based NAS for Inference-Optimized LLMs. **⭐⭐⭐** (相关度: 20%)
- **链接**: [出版页](https://proceedings.mlr.press/v267/bercovich25a.html)
- **作者**: Akhiad Bercovich, Tomer Ronen, Talor Abramovich, Nir Ailon, Nave Assaf, Mohammad Dabbah et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025
- **摘要（中）**: ①针对LLM推理优化中架构搜索与知识蒸馏结合不足的问题。②提出基于蒸馏的NAS方法（Puzzle），用于推理优化的LLM架构搜索。③相比传统NAS，结合蒸馏信号指导搜索，提升推理效率。④摘要缺失，具体效果未提供。
- **摘要（英）**: This paper addresses the gap between NAS and knowledge distillation for LLM inference optimization by proposing a distillation-based NAS method (Puzzle). It integrates distillation signals to guide architecture search, improving inference efficiency, though specific results are unavailable due to missing abstract.
- **核心贡献**: 提出蒸馏引导的LLM推理优化NAS方法。
- **创新点**: 将知识蒸馏信号融入架构搜索过程。
- **结果**: 具体效果未在摘要中提供。

### Per-Architecture Training-Free Metric Optimization for Neural Architecture Search. **⭐⭐⭐⭐** (相关度: 30%)
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/84f5e528dcab71efc71b79710f7d67eb-Abstract-Conference.html) · 📚 被引 2
- **作者**: Mingzhuo Lin, Jianping Luo
- **🏷️ 机构**: Shenzhen University, Department of Software Engineering, Shenzhen University
- **会议**: NeurIPS 2025
- **摘要（中）**: ①针对NAS中训练免费指标（如零成本代理）在不同架构上评估不一致的问题。②提出逐架构的训练免费指标优化方法，为每个架构定制指标计算。③相比统一指标，提高了搜索的准确性和鲁棒性。④摘要未提供具体数据，但方法具有通用性。
- **摘要（英）**: This paper addresses the inconsistency of training-free metrics across architectures in NAS by proposing per-architecture metric optimization. It customizes metric computation for each architecture, improving search accuracy and robustness, though specific results are unavailable due to missing abstract.
- **核心贡献**: 提出逐架构的训练免费指标优化方法。
- **创新点**: 为每个架构定制指标计算，提升NAS搜索质量。
- **结果**: 具体效果未在摘要中提供。

### Jet-Nemotron: Efficient Language Model with Post Neural Architecture Search. **⭐⭐** (相关度: 15%)
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/4364fbe773a77fb373df5c7f1d4cbb53-Abstract-Conference.html)
- **作者**: Yuxian Gu, Qinghao Hu, Haocheng Xi, Junyu Chen, Shang Yang, Song Han et al.
- **🏷️ 机构**: Tsinghua University, Tsinghua University, Massachusetts Institute of Technology, University of California, Berkeley
- **会议**: NeurIPS 2025
- **摘要（中）**: ①针对语言模型推理效率低的问题。②提出Jet-Nemotron，结合后训练NAS优化模型架构，在保持性能的同时减少计算量。③相比传统NAS，聚焦于后训练阶段，利用已有模型权重进行高效搜索。④摘要未提供具体数据，但强调效率提升。
- **摘要（英）**: ①Addresses low inference efficiency in language models. ②Proposes Jet-Nemotron, integrating post-training NAS to optimize architecture for reduced computation. ③Focuses on post-training search using existing weights, unlike conventional NAS. ④Emphasizes efficiency gains without specific metrics in the abstract.
- **核心贡献**: 提出后训练NAS方法优化语言模型效率。
- **创新点**: 在训练后阶段进行架构搜索以利用已有权重。
- **结果**: 在保持性能的同时提升推理效率。

### High-Performance Arithmetic Circuit Optimization via Differentiable Architecture Search. **⭐⭐** (相关度: 15%)
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/2026b8cac62265e48c630c4449522550-Abstract-Conference.html)
- **作者**: Xilin Xia, Jie Wang, Wanbo Zhang, Zhihai Wang, Mingxuan Yuan, Jianye Hao et al.
- **🏷️ 机构**: University of Science and Technology of China, Southeast University, Huawei Noah's Ark Lab
- **会议**: NeurIPS 2025
- **摘要（中）**: ①针对算术电路优化中人工设计效率低的问题。②提出基于可微架构搜索的方法自动优化高性能算术电路。③相比传统电路设计，利用NAS的梯度优化能力探索电路结构。④摘要未提供具体数据，但声称在电路面积和延迟上取得改进。
- **摘要（英）**: ①Addresses low efficiency in manual arithmetic circuit design. ②Proposes a differentiable architecture search method for automatic circuit optimization. ③Leverages gradient-based NAS for circuit structure exploration. ④Claims improvements in area and delay without specific metrics in the abstract.
- **核心贡献**: 将可微NAS应用于算术电路自动优化。
- **创新点**: 首次将DARTS类方法用于电路级设计。
- **结果**: 在电路面积和延迟上取得改进。

<!-- COMPLETE v1 papers=16 -->
