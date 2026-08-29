# Neural Architecture Search — 2022 Guideline

> 领域: 神经架构搜索（NAS、Zero-Cost、搜索空间）
> 论文数: 13 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: [2024](Guideline%202024.md)

### EAutoDet: Efficient Architecture Search for Object Detection. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2203.10747](https://arxiv.org/abs/2203.10747) · 📚 被引 24
- **作者**: Xiaoxing Wang, Jiale Lin, Juanping Zhao, Xiaokang Yang, Junchi Yan
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对目标检测中CNN训练耗时、直接在检测数据集上搜索架构成本极高（通常需数十甚至数百GPU天）的问题。②提出了高效框架EAutoDet，构建覆盖backbone和FPN的超级网络，采用可微搜索方法，并提出内核复用技术（共享候选操作权重并合并为单一卷积）以降低GPU内存和计算成本，同时引入动态通道细化策略搜索通道数。③相比现有检测NAS方法，显著提升了搜索效率，将搜索成本降至1.4 GPU天。④在COCO test-dev上，发现的架构达到40.1 mAP（120 FPS）和49.2 mAP（41.3 FPS），超越SOTA检测NAS方法，并成功迁移至旋转检测任务（DOTA上77.05 mAP50）。
- **摘要（英）**: This paper addresses the high computational cost of neural architecture search for object detection by proposing EAutoDet, an efficient framework that searches backbone and FPN architectures in 1.4 GPU-days via a differentiable supernet with kernel reusing and dynamic channel refinement. The discovered architectures achieve 40.1 mAP at 120 FPS and 49.2 mAP at 41.3 FPS on COCO test-dev, surpassing prior detection NAS methods, and transfer well to rotation detection.
- **核心贡献**: 提出了一种高效的检测NAS框架，在极低搜索成本下发现高性能backbone和FPN架构。
- **创新点**: 内核复用技术和动态通道细化策略，实现了可微搜索中的高效计算。
- **结果**: 在COCO上以1.4 GPU天搜索成本达到SOTA检测性能，并成功迁移至旋转检测。

### Large-Scale Graph Neural Architecture Search.
- **链接**: [出版页](https://proceedings.mlr.press/v162/guan22d.html)
- **作者**: Chaoyu Guan, Xin Wang, Hong Chen, Ziwei Zhang, Wenwu Zhu
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

> Training CNN for detection is time-consuming due to the large dataset and complex network modules, making it hard to search architectures on detection datasets directly, which usually requires vast search costs (usually tens and even hundreds of GPU-days). In contrast, this paper introduces an efficient framework, named EAutoDet, that can discover practical backbone and FPN architectures for object detection in 1.4 GPU-days. Specifically, we construct a supernet for both backbone and FPN modules and adopt the differentiable method. To reduce the GPU memory requirement and computational cost, we propose a kernel reusing technique by sharing the weights of candidate operations on one edge and consolidating them into one convolution. A dynamic channel refinement strategy is also introduced to search channel numbers. Extensive experiments show significant efficacy and efficiency of our method. In particular, the discovered architectures surpass state-of-the-art object detection NAS methods and achieve 40.1 mAP with 120 FPS and 49.2 mAP with 41.3 FPS on COCO test-dev set. We also transfer the discovered architectures to rotation detection task, which achieve 77.05 mAP$_{\text{50}}$ on DOTA-v1.0 test set with 21.1M parameters.

### AGNAS: Attention-Guided Micro and Macro-Architecture Search.
- **链接**: [出版页](https://proceedings.mlr.press/v162/sun22a.html)
- **作者**: Zihao Sun, Yu Hu, Shun Lu, Longxing Yang, Jilin Mei, Yinhe Han et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

### ViTAS: Vision Transformer Architecture Search. **⭐⭐** (相关度: 40%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19803-8_9)
- **作者**: Xiu Su, Shan You, Jiyang Xie, Mingkai Zheng, Fei Wang, Chen Qian et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①该论文针对视觉Transformer架构搜索问题。②提出ViTAS方法，用于自动搜索高效的Vision Transformer架构。③相比手工设计，通过搜索优化架构性能。④由于摘要缺失，无法提供具体结果。
- **摘要（英）**: This paper addresses architecture search for Vision Transformers. It proposes ViTAS to automatically search efficient ViT architectures. Compared to manual design, it optimizes performance via search. Specific results are unavailable due to missing abstract.
- **核心贡献**: 提出视觉Transformer的架构搜索方法。
- **创新点**: 将NAS应用于ViT设计。
- **结果**: 未提供具体数据。

### Spectrum-Aware and Transferable Architecture Search for Hyperspectral Image Restoration. **⭐⭐** (相关度: 30%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19800-7_2) · 📚 被引 14
- **作者**: Wei He, Quanming Yao, Naoto Yokoya, Tatsumi Uezato, Hongyan Zhang, Liangpei Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对高光谱图像恢复任务中架构搜索的效率和泛化性问题。②提出了频谱感知和可迁移的架构搜索方法，但摘要内容缺失，无法详细描述具体方法。③改进点可能在于利用频谱特性提升搜索效率和跨数据集迁移能力。④由于摘要不完整，无法提供具体效果数据。
- **摘要（英）**: This paper proposes a spectrum-aware and transferable architecture search method for hyperspectral image restoration, but the abstract is incomplete, limiting detailed assessment. It likely focuses on leveraging spectral characteristics to improve search efficiency and generalization, though no quantitative results are available.
- **核心贡献**: 针对高光谱图像恢复提出频谱感知的NAS方法。
- **创新点**: 频谱感知和可迁移性设计。
- **结果**: 未提供具体效果数据。

### UniNet: Unified Architecture Search with Convolution, Transformer, and MLP. **⭐⭐⭐⭐** (相关度: 65%)
- **链接**: [arXiv:2207.05420](https://arxiv.org/abs/2207.05420) · 📚 被引 21
- **作者**: Jihao Liu, Xin Huang, Guanglu Song, Hongsheng Li, Yu Liu
- **🏷️ 机构**: CUHK, SenseTime
- **会议**: ECCV 2022
- **摘要（中）**: ①该论文针对如何有效组合卷积、Transformer和MLP算子以形成高性能混合视觉架构的问题。②提出了统一架构搜索方法UniNet，包含两个关键设计：将不同搜索算子统一建模，用相同配置参数表征，减少搜索空间大小；提出上下文感知下采样模块（DSMs）以缓解不同算子间的差距。③相比现有方法，统一建模降低了搜索成本，DSMs增强了特征适应性，有助于识别高性能混合架构。④摘要未提供具体数据，但通过强化学习搜索，预期在视觉任务上达到先进性能。
- **摘要（英）**: This paper addresses the challenge of effectively combining convolution, Transformer, and MLP operators for high-performance hybrid architectures. It proposes UniNet, a unified architecture search approach with unified operator modeling to reduce search space and context-aware downsampling modules (DSMs) to bridge operator gaps. This enables affordable search and better feature adaptation, with expected SOTA performance via RL-based search. Specific results are not provided.
- **核心贡献**: 提出统一架构搜索方法UniNet，结合卷积、Transformer和MLP，降低搜索成本。
- **创新点**: 统一算子建模和上下文感知下采样模块设计。
- **结果**: 摘要未提供具体数据，预期在视觉任务上表现优异。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, transformer and multi-layer perceptron (MLP) architectures have achieved impressive results on various vision tasks. However, how to effectively combine those operators to form high-performance hybrid visual architectures still remains a challenge. In this work, we study the learnable combination of convolution, transformer, and MLP by proposing a novel unified architecture search approach. Our approach contains two key designs to achieve the search for high-performance networks. First, we model the very different searchable operators in a unified form, and thus enable the operators to be characterized with the same set of configuration parameters. In this way, the overall search space size is significantly reduced, and the total search cost becomes affordable. Second, we propose context-aware downsampling modules (DSMs) to mitigate the gap between the different types of operators. Our proposed DSMs are able to better adapt features from different types of operators, which is important for identifying high-performance hybrid architectures. Finally, we integrate configurable operators and DSMs into a unified search space and search with a Reinforcement Learning-based search algorithm to fully explore the optimal combination of the operators. To this end, we search a baseline network and scale it up to obtain a family of models, named UniNets, which achieve much better accuracy and efficiency than previous ConvNets and Transformers. In particular, our UniNet-B5 achieves 84.9% top-1 accuracy on ImageNet, outperforming EfficientNet-B7 and BoTNet-T7 with 44% and 55% fewer FLOPs respectively. By pretraining on the ImageNet-21K, our UniNet-B6 achieves 87.4%, outperforming Swin-L with 51% fewer FLOPs and 41% fewer parameters. Code is available at https://github.com/Sense-X/UniNet.

</details>

### Data-Free Neural Architecture Search via Recursive Label Calibration. **⭐⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2112.02086](https://arxiv.org/abs/2112.02086) · 📚 被引 5
- **作者**: Zechun Liu, Zhiqiang Shen, Yun Long, Eric P. Xing, Kwang-Ting Cheng, Chas Leichner
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对隐私保护和偏差避免等场景中，仅给定预训练模型而无原始训练数据时进行NAS的可行性问题。②提出通过递归标签校准合成可用数据，并采用区域更新策略生成多样且语义丰富的合成数据，同时使用输入和特征级正则化减少与自然图像的域差距，然后基于合成数据指导NAS。③相比现有数据-free NAS方法，增强了合成数据的语义、多样性和域一致性。④在DARTS、ProxylessNAS和SPOS三种NAS算法上验证，搜索到的架构性能与使用原始数据搜索的相当，证明了方法的有效性。
- **摘要（英）**: This paper explores data-free NAS by synthesizing data from a pre-trained model using recursive label calibration, regional update for diversity, and input/feature-level regularization to minimize domain gap. The approach is validated with DARTS, ProxylessNAS, and SPOS, achieving competitive architecture performance without original training data, addressing privacy and bias concerns.
- **核心贡献**: 提出了数据-free NAS框架，通过递归标签校准合成高质量数据以指导架构搜索。
- **创新点**: 递归标签校准和区域更新策略，提升合成数据的语义和多样性。
- **结果**: 在多种NAS算法上验证，性能与原始数据搜索相当。

### TabNAS: Rejection Sampling for Neural Architecture Search on Tabular Datasets.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/4e392aa9bc70ed731d3c9c32810f92fb-Abstract-Conference.html) · 📚 被引 1
- **作者**: Chengrun Yang, Gabriel Bender, Hanxiao Liu, Pieter-Jan Kindermans, Madeleine Udell, Yifeng Lu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

> This paper aims to explore the feasibility of neural architecture search (NAS) given only a pre-trained model without using any original training data. This is an important circumstance for privacy protection, bias avoidance, etc., in real-world scenarios. To achieve this, we start by synthesizing usable data through recovering the knowledge from a pre-trained deep neural network. Then we use the synthesized data and their predicted soft-labels to guide neural architecture search. We identify that the NAS task requires the synthesized data (we target at image domain here) with enough semantics, diversity, and a minimal domain gap from the natural images. For semantics, we propose recursive label calibration to produce more informative outputs. For diversity, we propose a regional update strategy to generate more diverse and semantically-enriched synthetic data. For minimal domain gap, we use input and feature-level regularization to mimic the original data distribution in latent space. We instantiate our proposed framework with three popular NAS algorithms: DARTS, ProxylessNAS and SPOS. Surprisingly, our results demonstrate that the architectures discovered by searching with our synthetic data achieve accuracy that is comparable to, or even higher than, architectures discovered by searching from the original ones, for the first time, deriving the conclusion that NAS can be done effectively with no need of access to the original or called natural data if the synthesis method is well designed.

</details>

### Robust Network Architecture Search via Feature Distortion Restraining. **⭐⭐** (相关度: 40%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20065-6_8) · 📚 被引 6
- **作者**: Yaguan Qian, Shenghui Huang, Bin Wang, Xiang Ling, Xiaohui Guan, Zhaoquan Gu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对NAS搜索过程中特征失真导致架构性能下降的问题。②提出了通过特征失真抑制的鲁棒NAS方法，但摘要内容缺失，无法详细描述具体技术。③改进点可能在于增强搜索过程的稳定性。④由于摘要不完整，无法提供具体效果数据。
- **摘要（英）**: This paper proposes a robust NAS method via feature distortion restraining, but the abstract is incomplete, preventing detailed evaluation. It likely aims to improve search stability by mitigating feature distortion, though no quantitative results are provided.
- **核心贡献**: 提出特征失真抑制的鲁棒NAS方法。
- **创新点**: 特征失真抑制机制。
- **结果**: 未提供具体效果数据。

### Compiler-Aware Neural Architecture Search for On-Mobile Real-time Super-Resolution. **⭐⭐⭐** (相关度: 50%)
- **链接**: [arXiv:2207.12577](https://arxiv.org/abs/2207.12577) · 📚 被引 25
- **作者**: Yushu Wu, Yifan Gong, Pu Zhao, Yanyu Li, Zheng Zhan, Wei Niu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对移动设备上超分辨率（SR）推理的实时性需求，现有方法计算量大、功耗高。②提出了编译器感知的SR NAS框架，进行深度和每层宽度搜索，并采用自适应SR块，将推理速度直接纳入优化目标，同时使用集成编译器优化的速度模型预测延迟以加速收敛。③相比传统方法，直接考虑编译器优化和移动平台约束，实现了实时推理。④在移动平台GPU/DSP上实现720p分辨率的实时SR推理，PSNR和SSIM性能具有竞争力。
- **摘要（英）**: This paper proposes a compiler-aware NAS framework for real-time super-resolution on mobile devices, conducting depth and width search with adaptive blocks and incorporating a compiler-optimized speed model for latency prediction. It achieves real-time 720p SR inference on mobile GPU/DSP with competitive PSNR and SSIM, addressing computational and power constraints.
- **核心贡献**: 提出了编译器感知的NAS框架，实现移动端实时SR推理。
- **创新点**: 将编译器优化集成到速度模型中，联合优化图像质量和延迟。
- **结果**: 在移动平台上实现实时720p SR，性能具有竞争力。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep learning-based super-resolution (SR) has gained tremendous popularity in recent years because of its high image quality performance and wide application scenarios. However, prior methods typically suffer from large amounts of computations and huge power consumption, causing difficulties for real-time inference, especially on resource-limited platforms such as mobile devices. To mitigate this, we propose a compiler-aware SR neural architecture search (NAS) framework that conducts depth search and per-layer width search with adaptive SR blocks. The inference speed is directly taken into the optimization along with the SR loss to derive SR models with high image quality while satisfying the real-time inference requirement. Instead of measuring the speed on mobile devices at each iteration during the search process, a speed model incorporated with compiler optimizations is leveraged to predict the inference latency of the SR block with various width configurations for faster convergence. With the proposed framework, we achieve real-time SR inference for implementing 720p resolution with competitive SR performance (in terms of PSNR and SSIM) on GPU/DSP of mobile platforms (Samsung Galaxy S21).

</details>

### A Max-Flow Based Approach for Neural Architecture Search. **⭐⭐** (相关度: 30%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20044-1_39)
- **作者**: Chao Xue, Xiaoxing Wang, Junchi Yan, Chun-Guang Li
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对NAS中架构搜索的优化问题。②提出了基于最大流（Max-Flow）的NAS方法，但摘要内容缺失，无法详细描述具体算法。③改进点可能在于利用图论方法提升搜索效率。④由于摘要不完整，无法提供具体效果数据。
- **摘要（英）**: This paper proposes a max-flow based approach for neural architecture search, but the abstract is incomplete, limiting detailed assessment. It likely leverages graph theory for efficient search, though no quantitative results are available.
- **核心贡献**: 提出基于最大流的NAS优化方法。
- **创新点**: 将最大流理论应用于架构搜索。
- **结果**: 未提供具体效果数据。

### EAGAN: Efficient Two-Stage Evolutionary Architecture Search for GANs. **⭐⭐⭐** (相关度: 30%)
- **链接**: [arXiv:2111.15097](https://arxiv.org/abs/2111.15097) · 📚 被引 22
- **作者**: Guohao Ying, Xin He, Bin Gao, Bo Han, Xiaowen Chu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①该论文针对GAN训练不稳定且手动设计架构需要专业知识的问题，提出自动搜索GAN架构的NAS方法。②提出了EAGAN，一种高效的两阶段进化算法NAS框架，将生成器（G）和判别器（D）的搜索解耦为两个阶段：阶段1用固定D搜索G并采用多对一训练策略，阶段2用最优G搜索D并采用一对一训练和权重重置策略。③相比早期仅搜索G的方法，EAGAN同时优化G和D，避免次优解；相比联合搜索方法，通过两阶段解耦和稳定性策略缓解了GAN训练不稳定性。④实验表明，EAGAN在多个数据集上取得了有竞争力的IS和FID分数，同时模型尺寸更小，但摘要未提供具体数值。
- **摘要（英）**: This paper addresses the instability of GAN training and the expertise required for manual architecture design by proposing EAGAN, an efficient two-stage evolutionary NAS framework that decouples generator and discriminator search. Stage-1 searches G with a fixed D using many-to-one training, while stage-2 searches D with the optimal G using one-to-one training and weight resetting, enhancing training stability. Compared to prior works, it jointly optimizes both G and D while mitigating instability, achieving competitive IS and FID scores with smaller model sizes, though specific numbers are not detailed in the abstract.
- **核心贡献**: 提出了一种两阶段进化NAS框架EAGAN，通过解耦G和D的搜索并引入稳定性策略，实现了高效且稳定的GAN架构自动搜索。
- **创新点**: 创新性地将GAN的G和D搜索解耦为两阶段，并采用多对一/一对一训练和权重重置策略来平衡搜索效率与训练稳定性。
- **结果**: 在图像生成任务上取得了有竞争力的IS和FID分数，同时降低了模型尺寸。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Generative adversarial networks (GANs) have proven successful in image generation tasks. However, GAN training is inherently unstable. Although many works try to stabilize it by manually modifying GAN architecture, it requires much expertise. Neural architecture search (NAS) has become an attractive solution to search GANs automatically. The early NAS-GANs search only generators to reduce search complexity but lead to a sub-optimal GAN. Some recent works try to search both generator (G) and discriminator (D), but they suffer from the instability of GAN training. To alleviate the instability, we propose an efficient two-stage evolutionary algorithm-based NAS framework to search GANs, namely EAGAN. We decouple the search of G and D into two stages, where stage-1 searches G with a fixed D and adopts the many-to-one training strategy, and stage-2 searches D with the optimal G found in stage-1 and adopts the one-to-one training and weight-resetting strategies to enhance the stability of GAN training. Both stages use the non-dominated sorting method to produce Pareto-front architectures under multiple objectives (e.g., model size, Inception Score (IS), and Fréchet Inception Distance (FID)). EAGAN is applied to the unconditional image generation task and can efficiently finish the search on the CIFAR-10 dataset in 1.2 GPU days. Our searched GANs achieve competitive results (IS=8.81$\pm$0.10, FID=9.91) on the CIFAR-10 dataset and surpass prior NAS-GANs on the STL-10 dataset (IS=10.44$\pm$0.087, FID=22.18). Source code: https://github.com/marsggbo/EAGAN.

</details>

### U-Boost NAS: Utilization-Boosted Differentiable Neural Architecture Search. **⭐⭐** (相关度: 20%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19775-8_11) · 📚 被引 3
- **作者**: Ahmet Caner Yüzügüler, Nikolaos Dimitriadis, Pascal Frossard
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①该论文针对可微分神经网络架构搜索（DARTS）中架构利用率低的问题，即搜索过程中许多候选操作未被充分训练，导致搜索到的架构性能不佳。②提出了U-Boost NAS，一种利用率增强的可微分NAS方法，通过改进训练策略来提升候选操作的利用效率，但摘要内容不完整，具体方法细节未提供。③相比标准DARTS，U-Boost NAS旨在提高架构搜索的稳定性和最终性能，但缺乏详细对比信息。④由于摘要截断，无法获取具体实验效果和数据。
- **摘要（英）**: This paper addresses the low utilization of candidate operations in differentiable neural architecture search (DARTS), which leads to suboptimal searched architectures. It proposes U-Boost NAS, a utilization-boosted differentiable NAS method that enhances training efficiency of candidates, though the abstract is incomplete and lacks method details. Compared to standard DARTS, it aims to improve search stability and final performance, but no specific experimental results are available due to truncation.
- **核心贡献**: 提出了U-Boost NAS，一种通过提升候选操作利用率来改进可微分NAS的方法。
- **创新点**: 创新点在于通过利用率增强策略优化DARTS的训练过程，但具体机制未在摘要中阐明。
- **结果**: 由于摘要不完整，无法评估具体效果。

## 跨领域论文（完整笔记在其他领域）

- Neural Architecture Search for Spiking Neural Networks. → [network-pruning](../network-pruning/Guideline%202022.md)
- SuperTickets: Drawing Task-Agnostic Lottery Tickets from Supernets via Jointly Architecture Searching and Parameter Pruning. → [network-pruning](../network-pruning/Guideline%202022.md)
- Ensemble Knowledge Guided Sub-network Search and Fine-Tuning for Filter Pruning. → [network-pruning](../network-pruning/Guideline%202022.md)
