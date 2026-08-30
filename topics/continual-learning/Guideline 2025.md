# Continual Learning — 2025 Guideline

> 领域: 持续学习 / 增量学习（含 VLM/多模态场景）
> 论文数: 31 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份:

### AVQACL: A Novel Benchmark for Audio-Visual Question Answering Continual Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Wu_AVQACL_A_Novel_Benchmark_for_Audio-Visual_Question_Answering_Continual_Learning_CVPR_2025_paper.html)
- **作者**: Kaixuan Wu, Xinde Li, Xinling Li, Chuanfei Hu, Guoliang Wu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### Advancing Multiple Instance Learning with Continual Learning for Whole Slide Imaging. **⭐⭐⭐** (相关度: 20%)
- **链接**: [arXiv:2505.10649](https://arxiv.org/abs/2505.10649) · 📚 被引 1
- **作者**: Xianrui Li, Yufei Cui, Jun Li, Antoni B. Chan
- **🏷️ 机构**: City University of Hong Kong,Dept. of Computer Science, Noah&#x2019;s Ark Lab, Huawei Canada,Montreal,Canada, Guangzhou Bingli Technology Co., Ltd.,Guangzhou
- **会议**: CVPR 2025
- **摘要（中）**: 针对全切片图像分析中传统多实例学习模型无法适应数据分布变化、需要大量重训练的问题，本文分析了注意力多实例学习模型在持续学习中的遗忘机制，发现遗忘主要集中在注意力层。为此提出了注意力知识蒸馏和伪包记忆池两个组件，前者通过保留注意力层知识来缓解灾难性遗忘，后者通过选择性存储信息量最大的伪包来降低内存占用。实验表明该方法在多个全切片图像数据集上显著提升了准确率和内存效率。
- **摘要（英）**: This paper addresses the lack of adaptability in conventional multiple instance learning (MIL) models for whole slide image analysis under evolving datasets. By analyzing catastrophic forgetting in attention-based MIL, they identify attention layers as the main source of forgetting and propose Attention Knowledge Distillation (AKD) and Pseudo-Bag Memory Pool (PMP) to mitigate it. Experiments show significant improvements in accuracy and memory efficiency across diverse WSI datasets.
- **核心贡献**: 提出了针对注意力MIL模型的持续学习改进方法，包括注意力知识蒸馏和伪包记忆池。
- **创新点**: 首次分析并利用注意力层遗忘特性设计持续学习策略。
- **结果**: 在多个WSI数据集上显著提升准确率和内存效率。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Advances in medical imaging and deep learning have propelled progress in whole slide image (WSI) analysis, with multiple instance learning (MIL) showing promise for efficient and accurate diagnostics. However, conventional MIL models often lack adaptability to evolving datasets, as they rely on static training that cannot incorporate new information without extensive retraining. Applying continual learning (CL) to MIL models is a possible solution, but often sees limited improvements. In this paper, we analyze CL in the context of attention MIL models and find that the model forgetting is mainly concentrated in the attention layers of the MIL model. Using the results of this analysis we propose two components for improving CL on MIL: Attention Knowledge Distillation (AKD) and the Pseudo-Bag Memory Pool (PMP). AKD mitigates catastrophic forgetting by focusing on retaining attention layer knowledge between learning sessions, while PMP reduces the memory footprint by selectively storing only the most informative patches, or ``pseudo-bags'' from WSIs. Experimental evaluations demonstrate that our method significantly improves both accuracy and memory efficiency on diverse WSI datasets, outperforming current state-of-the-art CL methods. This work provides a foundation for CL in large-scale, weakly annotated clinical datasets, paving the way for more adaptable and resilient diagnostic models.

</details>

### Feature Decomposition-Recomposition in Large Vision-Language Model for Few-Shot Class-Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00302) · 📚 被引 0
- **作者**: Zongyao Xue, Meina Kan, Shiguang Shan, Xilin Chen
- **🏷️ 机构**: Institute of Computing Technology,Chinese Academy of Sciences,Beijing,China,100090
- **会议**: ICCV 2025

> Unified Multimodal Generative Models (UMGMs) unify visual understanding and image generation within a single autoregressive framework. However, their ability to continually learn new tasks is severely hindered by catastrophic forgetting, both within a modality (intra-modal) and across modalities (inter-modal). While intra-modal forgetting has been studied in prior continual learning (CL) work, inter-modal forgetting remains largely unexplored. In this paper, we identify and empirically validate this phenomenon in UMGMs and provide a theoretical explanation rooted in gradient conflict between modalities. To address both intra- and inter-modal forgetting, we propose Modality-Decoupled Experts (MoDE), a lightweight and scalable architecture that isolates modality-specific updates to mitigate the gradient conflict and leverages knowledge distillation to prevent catastrophic forgetting and preserve pre-trained capabilities. Unlike previous CL methods that remain modality-coupled and suffer from modality gradient conflict, MoDE explicitly decouples modalities to prevent interference. Experiments across diverse benchmarks demonstrate that MoDE significantly mitigates both inter- and intra-modal forgetting, outperforming prior CL baselines in unified multimodal generation settings. Codes will be publicly available: https://github.com/Christina200/MoDE-official.git

### PROL: Rehearsal Free Continual Learning in Streaming Data via Prompt Online Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00238) · 📚 被引 0
- **作者**: M. Anwar Ma'sum, Mahardhika Pratama, Savitha Ramasamy, Lin Liu, Habibullah Habibullah, Ryszard Kowalczyk
- **🏷️ 机构**: STEM University of South Australia,South Australia, Institute for Infocomm Research
- **会议**: ICCV 2025

### Self-Expansion of Pre-trained Models with Mixture of Adapters for Continual Learning. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2403.18886](https://arxiv.org/abs/2403.18886) · 📚 被引 15
- **作者**: Huiyi Wang, Haodong Lu, Lina Yao, Dong Gong
- **🏷️ 机构**: University of New South Wales, CSIRO&#x2019;s Data61
- **会议**: CVPR 2025
- **摘要（中）**: 针对基于预训练模型的持续学习方法因固定模块集导致学习能力受限、或周期性添加任务特定模块导致模型线性增长和知识复用不足的问题，本文提出SEMA方法，通过自动决定重用或添加适配器模块来控制稳定性-可塑性平衡。SEMA设计模块化适配器，包含功能适配器和表示描述符，根据表示级别的分布偏移检测来决定是否扩展。该方法在多个持续学习基准上取得了优于现有方法的性能。
- **摘要（英）**: This paper tackles the limited learning capacity and linear model growth in pre-trained model-based continual learning. SEMA automatically decides to reuse or add adapter modules based on distribution shift detection at different representation levels, using modular adapters with functional adapters and representation descriptors. It achieves superior performance on multiple continual learning benchmarks.
- **核心贡献**: 提出SEMA方法，通过模块化适配器的自动扩展实现高效的持续学习。
- **创新点**: 基于分布偏移检测的自适应模块扩展机制。
- **结果**: 在多个基准上优于现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning (CL) aims to continually accumulate knowledge from a non-stationary data stream without catastrophic forgetting of learned knowledge, requiring a balance between stability and adaptability. Relying on the generalizable representation in pre-trained models (PTMs), PTM-based CL methods perform effective continual adaptation on downstream tasks by adding learnable adapters or prompts upon the frozen PTMs. However, many existing PTM-based CL methods use restricted adaptation on a fixed set of these modules to avoid forgetting, suffering from limited CL ability. Periodically adding task-specific modules results in linear model growth rate and impaired knowledge reuse. We propose Self-Expansion of pre-trained models with Modularized Adaptation (SEMA), a novel approach to enhance the control of stability-plasticity balance in PTM-based CL. SEMA automatically decides to reuse or add adapter modules on demand in CL, depending on whether significant distribution shift that cannot be handled is detected at different representation levels. We design modular adapter consisting of a functional adapter and a representation descriptor. The representation descriptors are trained as a distribution shift indicator and used to trigger self-expansion signals. For better composing the adapters, an expandable weighting router is learned jointly for mixture of adapter outputs. SEMA enables better knowledge reuse and sub-linear expansion rate. Extensive experiments demonstrate the effectiveness of the proposed self-expansion method, achieving state-of-the-art performance compared to PTM-based CL methods without memory rehearsal. Code is available at https://github.com/huiyiwang01/SEMA-CL.

</details>

### CODE-CL: Conceptor-Based Gradient Projection for Deep Continual Learning.
- **链接**: [arXiv:2411.15235](https://arxiv.org/abs/2411.15235) · 📚 被引 1
- **作者**: Marco Paul E. Apolinario, Sakshi Choudhary, Kaushik Roy
- **🏷️ 机构**: Elmore Family School of Electrical and Computer Engineering Purdue University,West Lafayette,IN,USA,47906
- **会议**: ICCV 2025

> This paper studies the problem of class-incremental learning (CIL), a core setting within continual learning where a model learns a sequence of tasks, each containing a distinct set of classes. Traditional CIL methods, which do not leverage pre-trained models (PTMs), suffer from catastrophic forgetting (CF) due to the need to incrementally learn both feature representations and the classifier. The integration of PTMs into CIL has recently led to efficient approaches that treat the PTM as a fixed feature extractor combined with analytic classifiers, achieving state-of-the-art performance. However, they still face a major limitation: the inability to continually adapt feature representations to best suit the CIL tasks, leading to suboptimal performance. To address this, we propose AnaCP (Analytic Contrastive Projection), a novel method that preserves the efficiency of analytic classifiers while enabling incremental feature adaptation without gradient-based training, thereby eliminating the CF caused by gradient updates. Our experiments show that AnaCP not only outperforms existing baselines but also achieves the accuracy level of joint training, which is regarded as the upper bound of CIL.

### Mind the Gap: Preserving and Compensating for the Modality Gap in CLIP-Based Continual Learning.
- **链接**: [arXiv:2507.09118](https://arxiv.org/abs/2507.09118) · 📚 被引 3
- **作者**: Linlan Huang, Xusheng Cao, Haori Lu, Yifan Meng, Fei Yang, Xialei Liu
- **🏷️ 机构**: CS Nankai University,VCIP, NKIARI,Shenzhen,Futian
- **会议**: ICCV 2025

### Online Task-Free Continual Learning via Dynamic Expansionable Memory Distribution. **⭐⭐** (相关度: 50%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Ye_Online_Task-Free_Continual_Learning_via_Dynamic_Expansionable_Memory_Distribution_CVPR_2025_paper.html) · 📚 被引 1
- **作者**: Fei Ye, Adrian G. Bors
- **🏷️ 机构**: University of Electronic Science and Technology of China,School of Information and Software Engineering,Chengdu, University of York,Department of Computer Science,York,UK,YO10 5GH
- **会议**: CVPR 2025
- **摘要（中）**: 该论文摘要缺失，无法提供具体内容。根据标题推测，可能针对在线无任务持续学习问题，提出动态可扩展记忆分布的方法。由于缺乏细节，无法评估其方法质量和效果。
- **摘要（英）**: The abstract is missing, so the content cannot be summarized. Based on the title, it likely addresses online task-free continual learning with dynamic expandable memory distribution, but details are unavailable.
- **核心贡献**: 未知。
- **创新点**: 未知。
- **结果**: 未知。

### Joint Diffusion Models in Continual Learning.
- **链接**: [arXiv:2411.08224](https://arxiv.org/abs/2411.08224) · 📚 被引 0
- **作者**: Pawel Skiers, Kamil Deja
- **🏷️ 机构**: Warsaw University of Technology, Research Institute IDEAS, Warsaw University of Technology
- **会议**: ICCV 2025

### Any-SSR: How Recursive Least Squares Works in Continual Learning of Large Language Models.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00292) · 📚 被引 0
- **作者**: Kai Tong, Kang Pan, Xiao Zhang, Erli Meng, Run He, Yawen Cui et al.
- **🏷️ 机构**: South China University of Technology,China, Xiaomi Corporation,China, The Hong Kong Polytechnic University,Hong Kong
- **会议**: ICCV 2025

> Biological brains learn continually from a stream of unlabeled data, while integrating specialized information from sparsely labeled examples without compromising their ability to generalize. Meanwhile, machine learning methods are susceptible to catastrophic forgetting in this natural learning setting, as supervised specialist fine-tuning degrades performance on the original task. We introduce task-modulated contrastive learning (TMCL), which takes inspiration from the biophysical machinery in the neocortex, using predictive coding principles to integrate top-down information continually and without supervision. We follow the idea that these principles build a view-invariant representation space, and that this can be implemented using a contrastive loss. Then, whenever labeled samples of a new class occur, new affine modulations are learned that improve separation of the new class from all others, without affecting feedforward weights. By co-opting the view-invariance learning mechanism, we then train feedforward weights to match the unmodulated representation of a data sample to its modulated counterparts. This introduces modulation invariance into the representation space, and, by also using past modulations, stabilizes it. Our experiments show improvements in both class-incremental and transfer learning over state-of-the-art unsupervised approaches, as well as over comparable supervised approaches, using as few as 1% of available labels. Taken together, our work suggests that top-down modulations play a crucial role in balancing stability and plasticity.

### FedAGC: Federated Continual Learning with Asymmetric Gradient Correction.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00366) · 📚 被引 0
- **作者**: Chengchao Zhang, Fanhua Shang, Hongyin Liu, Liang Wan, Wei Feng
- **🏷️ 机构**: College of Intelligence and Computing, Tianjin University,China, Medical College, Tianjin University,China
- **会议**: ICCV 2025

### Bisecle: Binding and Separation in Continual Learning for Video Language Understanding.
- **链接**: [arXiv:2507.00469](https://arxiv.org/abs/2507.00469) · 📚 被引 0
- **作者**: Yue Tan, Xiaoqian Hu, Hao Xue, Celso de Melo, Flora D. Salim
- **🏷️ 机构**: University of New South Wales, The University of Queensland, The Hong Kong University of Science and Technology
- **会议**: NeurIPS 2025

### Revisiting Pool-Based Prompt Learning for Few-Shot Class-Incremental Learning.
- **链接**: [arXiv:2507.09183](https://arxiv.org/abs/2507.09183) · 📚 被引 0
- **作者**: Yongwei Jiang, Yixiong Zou, Yuhua Li, Ruixuan Li
- **🏷️ 机构**: School of Computer Science and Technology, Huazhong University of Science and Technology
- **会议**: ICCV 2025

> Frontier vision-language models (VLMs) have made remarkable improvements in video understanding tasks. However, real-world videos typically exist as continuously evolving data streams (e.g., dynamic scenes captured by wearable glasses), necessitating models to continually adapt to shifting data distributions and novel scenarios. Considering the prohibitive computational costs of fine-tuning models on new tasks, usually, a small subset of parameters is updated while the bulk of the model remains frozen. This poses new challenges to existing continual learning frameworks in the context of large multimodal foundation models, i.e., catastrophic forgetting and update conflict. While the foundation models struggle with parameter-efficient continual learning, the hippocampus in the human brain has evolved highly efficient mechanisms for memory formation and consolidation. Inspired by the rapid Binding and pattern separation mechanisms in the hippocampus, in this work, we propose Bisecle for video-language continual learning, where a multi-directional supervision module is used to capture more cross-modal relationships and a contrastive prompt learning scheme is designed to isolate task-specific knowledge to facilitate efficient memory storage. Binding and separation processes further strengthen the ability of VLMs to retain complex experiences, enabling robust and efficient continual learning in video understanding tasks. We perform a thorough evaluation of the proposed Bisecle, demonstrating its ability to mitigate forgetting and enhance cross-task generalization on several VideoQA benchmarks.

### Task-Aware Prompt Gradient Projection for Parameter-Efficient Tuning Federated Class-Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00253) · 📚 被引 1
- **作者**: Hualong Ke, Jiangming Shi, Yachao Zhang, Fangyong Wang, Yuan Xie, Yanyun Qu
- **🏷️ 机构**: School of Informatics, Xiamen University,Key Laboratory of Multimedia Trusted Perception and Efficient Computing, Ministry of Education of China, Hanjiang National Laboratory, Shanghai Innovation Institute
- **会议**: ICCV 2025

### KAC: Kolmogorov-Arnold Classifier for Continual Learning. **⭐⭐⭐** (相关度: 65%)
- **链接**: [arXiv:2503.21076](https://arxiv.org/abs/2503.21076) · 📚 被引 5
- **作者**: Yusong Hu, Zichen Liang, Fei Yang, Qibin Hou, Xialei Liu, Ming-Ming Cheng
- **🏷️ 机构**: Nankai University,VCIP, CS
- **会议**: CVPR 2025
- **摘要（中）**: 针对持续学习中线性分类器难以在连续任务中保持稳定分类空间的问题，本文提出基于Kolmogorov-Arnold网络的KAC分类器，并引入径向基函数以提升与持续学习的兼容性。将KAC替换多种现有方法中的线性分类器，在多个持续学习基准上均取得性能提升，验证了其有效性和鲁棒性。
- **摘要（英）**: This paper addresses the instability of linear classifiers in continual learning by proposing the Kolmogorov-Arnold Classifier (KAC) based on KAN structure, with Radial Basis Functions for improved compatibility. Replacing linear classifiers with KAC in several recent methods yields performance improvements across benchmarks, demonstrating effectiveness and robustness.
- **核心贡献**: 提出基于KAN的KAC分类器用于持续学习。
- **创新点**: 将KAN结构和RBF函数应用于持续学习分类器。
- **结果**: 在多个基准上提升性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning requires models to train continuously across consecutive tasks without forgetting. Most existing methods utilize linear classifiers, which struggle to maintain a stable classification space while learning new tasks. Inspired by the success of Kolmogorov-Arnold Networks (KAN) in preserving learning stability during simple continual regression tasks, we set out to explore their potential in more complex continual learning scenarios. In this paper, we introduce the Kolmogorov-Arnold Classifier (KAC), a novel classifier developed for continual learning based on the KAN structure. We delve into the impact of KAN's spline functions and introduce Radial Basis Functions (RBF) for improved compatibility with continual learning. We replace linear classifiers with KAC in several recent approaches and conduct experiments across various continual learning benchmarks, all of which demonstrate performance improvements, highlighting the effectiveness and robustness of KAC in continual learning. The code is available at https://github.com/Ethanhuhuhu/KAC.

</details>

### Do Your Best and Get Enough Rest for Continual Learning. **⭐⭐** (相关度: 30%)
- **链接**: [arXiv:2503.18371](https://arxiv.org/abs/2503.18371) · 📚 被引 1
- **作者**: Hankyul Kang, Gregor Seifer, Donghyun Lee, Jongbin Ryu
- **🏷️ 机构**: Ajou University, KAIST
- **会议**: CVPR 2025
- **摘要（中）**: ①针对持续学习中灾难性遗忘问题，受人类遗忘曲线理论启发，提出通过调整学习计划来优化重训练间隔。②提出了view-batch模型，包括一种保证最优回忆间隔的重放方法和一种自监督学习方法。③相比现有重放方法，创新性地将认知科学理论引入学习调度，强调回忆间隔的重要性。④摘要未提供具体实验数据，效果待验证。
- **摘要（英）**: This paper addresses catastrophic forgetting in continual learning by drawing inspiration from Ebbinghaus' forgetting curve theory. It proposes a view-batch model that adjusts learning schedules to optimize recall intervals, including a replay method and a self-supervised learning approach. The novelty lies in applying cognitive science principles to learning scheduling, though experimental results are not detailed in the abstract.
- **核心贡献**: 将遗忘曲线理论引入持续学习，提出基于回忆间隔优化的重放策略。
- **创新点**: 利用认知科学中的遗忘曲线来设计学习调度，而非仅依赖数据重放。
- **结果**: 摘要未提供具体效果数据。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> According to the forgetting curve theory, we can enhance memory retention by learning extensive data and taking adequate rest. This means that in order to effectively retain new knowledge, it is essential to learn it thoroughly and ensure sufficient rest so that our brain can memorize without forgetting. The main takeaway from this theory is that learning extensive data at once necessitates sufficient rest before learning the same data again. This aspect of human long-term memory retention can be effectively utilized to address the continual learning of neural networks. Retaining new knowledge for a long period of time without catastrophic forgetting is the critical problem of continual learning. Therefore, based on Ebbinghaus' theory, we introduce the view-batch model that adjusts the learning schedules to optimize the recall interval between retraining the same samples. The proposed view-batch model allows the network to get enough rest to learn extensive knowledge from the same samples with a recall interval of sufficient length. To this end, we specifically present two approaches: 1) a replay method that guarantees the optimal recall interval, and 2) a self-supervised learning that acquires extensive knowledge from a single training sample at a time. We empirically show that these approaches of our method are aligned with the forgetting curve theory, which can enhance long-term memory. In our experiments, we also demonstrate that our method significantly improves many state-of-the-art continual learning methods in various protocols and scenarios. We open-source this project at https://github.com/hankyul2/ViewBatchModel.

</details>

### Lark: Low-Rank Updates After Knowledge Localization for Few-Shot Class-Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00344) · 📚 被引 0
- **作者**: Jinxin Shi, Jiabao Zhao, Yifan Yang, Xingjiao Wu, Jiawen Li, Liang He
- **🏷️ 机构**: East China Normal University, Donghua University, Transwarp Technology (Shanghai) Co., Ltd
- **会议**: ICCV 2025

> Continual learning aims to learn multiple tasks sequentially while preserving prior knowledge, but faces the challenge of catastrophic forgetting when adapting to new tasks. Recently, approaches leveraging pre-trained models have gained increasing popularity in mitigating this issue, due to the strong generalization ability of foundation models. To adjust pre-trained models for new tasks, existing methods usually employ low-rank adaptation, which restricts parameter updates to a fixed low-rank subspace. However, constraining the optimization space inherently compromises the model's learning capacity, resulting in inferior performance. To address this limitation, we propose Continuous Subspace Optimization for Continual Learning (CoSO) to fine-tune the model in a series of subspaces rather than a single one. These sequential subspaces are dynamically determined through the singular value decomposition of the gradients. CoSO updates the model by projecting gradients onto these subspaces, ensuring memory-efficient optimization. To mitigate forgetting, the optimization subspace of each task is constrained to be orthogonal to the historical task subspace. During task learning, CoSO maintains a task-specific component that captures the critical update directions for the current task. Upon completing a task, this component is used to update the historical task subspace, laying the groundwork for subsequent learning. Extensive experiments on multiple datasets demonstrate that CoSO significantly outperforms state-of-the-art methods, especially in challenging scenarios with long task sequences.

### Learning Yourself: Class-Incremental Semantic Segmentation with Language-Inspired Bootstrapped Disentanglement.
- **链接**: [arXiv:2509.00527](https://arxiv.org/abs/2509.00527) · 📚 被引 1
- **作者**: Ruitao Wu, Yifan Zhao, Jia Li
- **🏷️ 机构**: Beihang University,State Key Laboratory of Virtual Reality Technology and Systems, SCSE &#x0026; QRI
- **会议**: ICCV 2025

### LoRA Subtraction for Drift-Resistant Space in Exemplar-Free Continual Learning. **⭐⭐⭐⭐** (相关度: 40%)
- **链接**: [arXiv:2503.18985](https://arxiv.org/abs/2503.18985) · 📚 被引 8
- **作者**: Xuan Liu, Xiaobin Chang
- **🏷️ 机构**: School of Artificial Intelligence, Sun Yat-sen University,China
- **会议**: CVPR 2025
- **摘要（中）**: ①针对无样本持续学习（EFCL）中特征漂移导致的灾难性遗忘问题。②提出了漂移抵抗空间（DRS）概念，并设计了LoRA减法（LoRA-）方法，通过从预训练权重中减去旧任务的LoRA权重来构建DRS。③相比依赖静态特征或过时统计的方法，LoRA-无需显式特征建模或存储旧任务，能动态适应特征空间演化。④实验表明该方法在稳定性、效率和实现简便性上均有提升，但摘要未给出具体数值。
- **摘要（英）**: This paper tackles feature drift in exemplar-free continual learning by introducing a Drift-Resistant Space (DRS) and a Low-Rank Adaptation Subtraction (LoRA-) method. LoRA- subtracts old-task LoRA weights from pre-trained weights to establish DRS, avoiding explicit feature modeling and old-task storage. It enhances stability and efficiency, though specific performance numbers are not provided in the abstract.
- **核心贡献**: 提出LoRA-方法构建漂移抵抗空间，解决无样本持续学习中的特征漂移问题。
- **创新点**: 利用LoRA权重减法动态构建DRS，无需存储旧任务样本。
- **结果**: 提升了稳定性、效率和实现简便性，具体数值未给出。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In continual learning (CL), catastrophic forgetting often arises due to feature drift. This challenge is particularly prominent in the exemplar-free continual learning (EFCL) setting, where samples from previous tasks cannot be retained, making it difficult to preserve prior knowledge. To address this issue, some EFCL methods aim to identify feature spaces that minimize the impact on previous tasks while accommodating new ones. However, they rely on static features or outdated statistics stored from old tasks, which prevents them from capturing the dynamic evolution of the feature space in CL, leading to performance degradation over time. In this paper, we introduce the Drift-Resistant Space (DRS), which effectively handles feature drifts without requiring explicit feature modeling or the storage of previous tasks. A novel parameter-efficient fine-tuning approach called Low-Rank Adaptation Subtraction (LoRA-) is proposed to develop the DRS. This method subtracts the LoRA weights of old tasks from the initial pre-trained weight before processing new task data to establish the DRS for model training. Therefore, LoRA- enhances stability, improves efficiency, and simplifies implementation. Furthermore, stabilizing feature drifts allows for better plasticity by learning with a triplet loss. Our method consistently achieves state-of-the-art results, especially for long task sequences, across multiple datasets.

</details>

### Flexi-FSCIL: Adaptive Knowledge Retention for Breaking the Stability-Plasticity Dilemma in Few-Shot Class-Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00236) · 📚 被引 2
- **作者**: Wufei Xie, Yalin Wang, Chenliang Liu, Zhaohui Jiang, Xue Yang
- **🏷️ 机构**: Central South University, Shanghai Jiao Tong University
- **会议**: ICCV 2025

> Federated Continual Learning (FCL) aims to enable sequentially privacy-preserving model training on streams of incoming data that vary in edge devices by preserving previous knowledge while adapting to new data. Current FCL literature focuses on restricted data privacy and access to previously seen data while imposing no constraints on the training overhead. This is unreasonable for FCL applications in real-world scenarios, where edge devices are primarily constrained by resources such as storage, computational budget, and label rate. We revisit this problem with a large-scale benchmark and analyze the performance of state-of-the-art FCL approaches under different resource-constrained settings. Various typical FCL techniques and six datasets in two incremental learning scenarios (Class-IL and Domain-IL) are involved in our experiments. Through extensive experiments amounting to a total of over 1,000+ GPU hours, we find that, under limited resource-constrained settings, existing FCL approaches, with no exception, fail to achieve the expected performance. Our conclusions are consistent in the sensitivity analysis. This suggests that most existing FCL methods are particularly too resource-dependent for real-world deployment. Moreover, we study the performance of typical FCL techniques with resource constraints and shed light on future research directions in FCL.

### iManip: Skill-Incremental Learning for Robotic Manipulation.
- **链接**: [arXiv:2503.07087](https://arxiv.org/abs/2503.07087) · 📚 被引 0
- **作者**: Zexin Zheng, Jia-Feng Cai, Xiao-Ming Wu, Yi-Lin Wei, Yu-Ming Tang, Ancong Wu et al.
- **🏷️ 机构**: School of Computer Science and Engineering, Sun Yat-sen University,china
- **会议**: ICCV 2025

### Enhancing Online Continual Learning with Plug-and-Play State Space Model and Class-Conditional Mixture of Discretization. **⭐⭐⭐⭐** (相关度: 35%)
- **链接**: [arXiv:2412.18177](https://arxiv.org/abs/2412.18177) · 📚 被引 1
- **作者**: Sihao Liu, Yibo Yang, Xiaojie Li, David A. Clifton, Bernard Ghanem
- **🏷️ 机构**: Harbin Institute of Technology, King Abdullah University of Science and Technology, Harbin Institute of Technology (Shenzhen)
- **会议**: CVPR 2025
- **摘要（中）**: ①针对在线持续学习（OCL）中模型适应性不足，难以从在线数据流中增量学习泛化特征的问题。②提出了即插即用模块S6MOD，在骨干网络后添加分支，通过混合离散化方法调整选择性状态空间模型的参数，并设计了类条件路由算法和对比离散化损失。③相比现有依赖重放和正则化的方法，S6MOD直接提升模型适应性，可集成到多数现有方法中。④大量实验表明S6MOD显著提升模型适应性，但摘要未给出具体数值。
- **摘要（英）**: This work addresses the limited adaptability of models in online continual learning by proposing a plug-and-play module S6MOD. It adds a branch after the backbone, using a mixture of discretization to adjust selective state space model parameters, with a class-conditional routing algorithm and contrastive loss. S6MOD can be integrated into existing methods, significantly improving adaptability, though specific results are not detailed.
- **核心贡献**: 提出即插即用的S6MOD模块，增强在线持续学习中的模型适应性。
- **创新点**: 将选择性状态空间模型与混合离散化结合，实现动态参数调整。
- **结果**: 显著提升模型适应性，具体数值未在摘要中给出。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Online continual learning (OCL) seeks to learn new tasks from data streams that appear only once, while retaining knowledge of previously learned tasks. Most existing methods rely on replay, focusing on enhancing memory retention through regularization or distillation. However, they often overlook the adaptability of the model, limiting the ability to learn generalizable and discriminative features incrementally from online training data. To address this, we introduce a plug-and-play module, S6MOD, which can be integrated into most existing methods and directly improve adaptability. Specifically, S6MOD introduces an extra branch after the backbone, where a mixture of discretization selectively adjusts parameters in a selective state space model, enriching selective scan patterns such that the model can adaptively select the most sensitive discretization method for current dynamics. We further design a class-conditional routing algorithm for dynamic, uncertainty-based adjustment and implement a contrastive discretization loss to optimize it. Extensive experiments combining our module with various models demonstrate that S6MOD significantly enhances model adaptability, leading to substantial performance gains and achieving the state-of-the-art results.

</details>

### Handling Spatial-Temporal Data Heterogeneity for Federated Continual Learning via Tail Anchor. **⭐** (相关度: 20%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Yu_Handling_Spatial-Temporal_Data_Heterogeneity_for_Federated_Continual_Learning_via_Tail_CVPR_2025_paper.html) · 📚 被引 5
- **作者**: Hao Yu, Xin Yang, Le Zhang, Hanlin Gu, Tianrui Li, Lixin Fan et al.
- **🏷️ 机构**: Southwestern University of Finance and Economics, University of Electronic Science and Technology of China, WeBank
- **会议**: CVPR 2025
- **摘要（中）**: ①摘要为空，无法评估具体问题和方法。②论文标题涉及联邦持续学习中的时空数据异质性，可能提出Tail Anchor方法。③无可用信息。④无效果数据。
- **摘要（英）**: The abstract is empty, so no details on the problem, method, or results can be assessed. The title suggests a focus on spatial-temporal data heterogeneity in federated continual learning, possibly with a Tail Anchor approach.
- **核心贡献**: 未知，因摘要为空。
- **创新点**: 未知。
- **结果**: 未知。

### Ferret: An Efficient Online Continual Learning Framework under Varying Memory Constraints. **⭐⭐⭐⭐** (相关度: 30%)
- **链接**: [arXiv:2503.12053](https://arxiv.org/abs/2503.12053)
- **作者**: Yuhao Zhou, Yuxin Tian, Jindi Lv, Mingjia Shi, Yuanxi Li, Qing Ye et al.
- **🏷️ 机构**: Sichuan University, National University of Singapore, University of Illinois Urbana-Champaign
- **会议**: CVPR 2025
- **摘要（中）**: ①针对在线持续学习（OCL）在高频数据流中实时学习且内存受限的问题。②提出了Ferret框架，采用细粒度流水线并行策略和迭代梯度补偿算法，并自动进行模型分区和流水线规划以适应内存预算。③相比现有方法，Ferret在内存效率和适应性上显著提升。④在20个基准和5个OCL算法上，达到相同在线精度时内存开销降低3.7倍，且在不同内存预算下均优于对比方法。
- **摘要（英）**: This paper presents Ferret, a framework for online continual learning under varying memory constraints, using fine-grained pipeline parallelism and iterative gradient compensation. It automates model partitioning to adapt to memory budgets, achieving up to 3.7x lower memory overhead for the same online accuracy across 20 benchmarks and 5 OCL algorithms. Ferret consistently outperforms competing methods under diverse memory budgets.
- **核心贡献**: 提出Ferret框架，实现内存约束下的高效在线持续学习。
- **创新点**: 结合流水线并行和梯度补偿，动态适应内存预算。
- **结果**: 内存开销降低3.7倍，性能优于对比方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In the realm of high-frequency data streams, achieving real-time learning within varying memory constraints is paramount. This paper presents Ferret, a comprehensive framework designed to enhance online accuracy of Online Continual Learning (OCL) algorithms while dynamically adapting to varying memory budgets. Ferret employs a fine-grained pipeline parallelism strategy combined with an iterative gradient compensation algorithm, ensuring seamless handling of high-frequency data with minimal latency, and effectively counteracting the challenge of stale gradients in parallel training. To adapt to varying memory budgets, its automated model partitioning and pipeline planning optimizes performance regardless of memory limitations. Extensive experiments across 20 benchmarks and 5 integrated OCL algorithms show Ferret's remarkable efficiency, achieving up to 3.7$\times$ lower memory overhead to reach the same online accuracy compared to competing methods. Furthermore, Ferret consistently outperforms these methods across diverse memory budgets, underscoring its superior adaptability. These findings position Ferret as a premier solution for efficient and adaptive OCL framework in real-time environments.

</details>

### Model Inversion with Layer-Specific Modeling and Alignment for Data-Free Continual Learning.
- **链接**: [arXiv:2510.26311](https://arxiv.org/abs/2510.26311) · 📚 被引 0
- **作者**: Ruilin Tong, Haodong Lu, Yuhang Liu, Dong Gong
- **🏷️ 机构**: University of New South Wales, The University of Adelaide, The University of New South Wales (UNSW)
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual Learning (CL) aims to enable models to continuously acquire new knowledge from a sequence of tasks with avoiding the forgetting of learned information. However, existing CL methods only rely on the parameters of the most recent task for inference, which makes them susceptible to catastrophic forgetting. Inspired by the recent success of model merging techniques, we propose \textbf{Perturb-and-Merge (P\&M)}, a novel continual learning framework that integrates model merging into the CL paradigm to mitigate forgetting. Specifically, after training on each task, P\&M constructs a new model by forming a convex combination of the previous model and the newly trained task-specific model. Through theoretical analysis, We minimize the total loss increase across all tasks and derive a closed-form solution for the merging coefficient under mild assumptions. To further improve the performance of the merged model, we observe that the degradation introduced during merging can be alleviated by a regularization term composed of the task vector and the Hessian matrix of the loss function. Interestingly, we show that this term can be efficiently approximated using second-order symmetric finite differences, and a stochastic perturbation strategy along the task vector direction is accordingly devised which incurs no additional forward or backward passes while providing an effective approximation of the regularization term. Finally, we combine P\&M with LoRA, a parameter-efficient fine-tuning method, to reduce memory overhead. Our proposed approach achieves state-of-the-art performance on several continual learning benchmark datasets. The code is available at https://github.com/qhmiao/P-M-for-Continual-Learning.

</details>

### BiLoRA: Almost-Orthogonal Parameter Spaces for Continual Learning. **⭐⭐⭐** (相关度: 25%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhu_BiLoRA_Almost-Orthogonal_Parameter_Spaces_for_Continual_Learning_CVPR_2025_paper.html) · 📚 被引 6
- **作者**: Hao Zhu, Yifei Zhang, Junhao Dong, Piotr Koniusz
- **🏷️ 机构**: Data61&#x2665;CSIRO, Nanyang Technological University
- **会议**: CVPR 2025
- **摘要（中）**: ①针对持续学习中参数空间干扰导致灾难性遗忘的问题。②提出了BiLoRA方法，构建几乎正交的参数空间以减少任务间干扰。③相比标准LoRA，BiLoRA通过正交化设计提升知识保留能力。④摘要未提供具体实验数据，效果待验证。
- **摘要（英）**: This paper addresses parameter interference in continual learning by proposing BiLoRA, which constructs almost-orthogonal parameter spaces to reduce cross-task interference. It improves knowledge retention compared to standard LoRA, though specific experimental results are not provided in the abstract.
- **核心贡献**: 提出BiLoRA方法，利用几乎正交参数空间缓解持续学习中的遗忘。
- **创新点**: 将正交性引入LoRA参数空间设计。
- **结果**: 摘要未提供具体效果数据。

### Learning Conditional Space-Time Prompt Distributions for Video Class-Incremental Learning. **⭐⭐⭐** (相关度: 40%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zou_Learning_Conditional_Space-Time_Prompt_Distributions_for_Video_Class-Incremental_Learning_CVPR_2025_paper.html) · 📚 被引 1
- **作者**: Xiaohan Zou, Wenchao Ma, Shu Zhao
- **🏷️ 机构**: The Pennsylvania State University
- **会议**: CVPR 2025
- **摘要（中）**: ①针对视频类增量学习（Video Class-Incremental Learning）中灾难性遗忘和时序信息利用不足的问题。②提出学习条件空间-时间提示分布（Conditional Space-Time Prompt Distributions），通过条件生成机制动态调整提示以适应视频帧的时空变化。③相比静态提示方法，该方法能更好地捕捉视频中的动态特征，提升增量学习中的知识保留。④在多个视频基准上取得了优于现有方法的性能，具体数据未在摘要中提供。
- **摘要（英）**: This paper addresses catastrophic forgetting and insufficient temporal exploitation in video class-incremental learning. It proposes learning conditional space-time prompt distributions that dynamically adjust prompts to accommodate spatial-temporal variations in video frames. Compared to static prompt methods, it better captures dynamic features, improving knowledge retention. It achieves superior performance on multiple video benchmarks, though specific numbers are not provided.
- **核心贡献**: 提出条件空间-时间提示分布用于视频类增量学习。
- **创新点**: 将提示学习扩展到时空条件分布，动态适应视频动态。
- **结果**: 在视频基准上性能优于现有方法。

### Dual Consolidation for Pre-Trained Model-Based Domain-Incremental Learning. **⭐⭐⭐** (相关度: 40%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhou_Dual_Consolidation_for_Pre-Trained_Model-Based_Domain-Incremental_Learning_CVPR_2025_paper.html) · 📚 被引 14
- **作者**: Da-Wei Zhou, Zi-Wen Cai, Han-Jia Ye, Lijun Zhang, De-Chuan Zhan
- **🏷️ 机构**: Nanjing University,School of Artificial Intelligence
- **会议**: CVPR 2025
- **摘要（中）**: ①针对基于预训练模型的域增量学习（Domain-Incremental Learning）中灾难性遗忘问题。②提出双重巩固（Dual Consolidation）机制，结合参数和特征层面的巩固策略，以保持模型在多个域上的稳定性。③相比单一巩固方法，双重巩固更全面地保留预训练知识，同时适应新域。④在多个域增量基准上展示了有效性，具体数据未在摘要中提供。
- **摘要（英）**: This paper tackles catastrophic forgetting in pre-trained model-based domain-incremental learning. It proposes a dual consolidation mechanism combining parameter and feature-level strategies to maintain stability across domains. Compared to single consolidation, it more comprehensively preserves pre-trained knowledge while adapting to new domains. It demonstrates effectiveness on multiple benchmarks, though specific numbers are not provided.
- **核心贡献**: 提出双重巩固机制用于域增量学习。
- **创新点**: 结合参数和特征巩固，增强知识保留。
- **结果**: 在多个基准上有效。

### Reducing Class-wise Confusion for Incremental Learning with Disentangled Manifolds. **⭐⭐⭐⭐** (相关度: 50%)
- **链接**: [arXiv:2503.17677](https://arxiv.org/abs/2503.17677) · 📚 被引 5
- **作者**: Huitong Chen, Yu Wang, Yan Fan, Guosong Jiang, Qinghua Hu
- **🏷️ 机构**: Tianjin University,Tianjin Key Lab of Machine Learning, College of Intelligence and Computing,China
- **会议**: CVPR 2025
- **摘要（中）**: ①针对类增量学习（CIL）中原型方法表示能力不足和特征重叠导致的类间混淆问题。②提出Confusion-REduced AuTo-Encoder分类器（CREATE），使用轻量级自编码器为每个类学习紧凑流形，并设计混淆感知的潜在空间分离损失，使样本在正确自编码器上重建良好且远离其他类分布。③相比传统原型方法，增强了表示稳定性和类分布能力，缓解类间混淆。④实验表明方法性能更强，具体数据未在摘要中提供。
- **摘要（英）**: This paper addresses inadequate representation and feature overlap in prototype-based class incremental learning, causing class-wise confusion. It proposes CREATE, a confusion-reduced auto-encoder classifier that learns compact manifolds per class and uses a confusion-aware separation loss to keep samples close to their class manifold and away from others. Compared to prototype methods, it enhances representation stability and reduces confusion. Experiments show stronger performance, though specific numbers are not provided.
- **核心贡献**: 提出CREATE方法缓解类增量学习中的类间混淆。
- **创新点**: 利用自编码器流形和分离损失增强类表示。
- **结果**: 性能优于现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Class incremental learning (CIL) aims to enable models to continuously learn new classes without catastrophically forgetting old ones. A promising direction is to learn and use prototypes of classes during incremental updates. Despite simplicity and intuition, we find that such methods suffer from inadequate representation capability and unsatisfied feature overlap. These two factors cause class-wise confusion and limited performance. In this paper, we develop a Confusion-REduced AuTo-Encoder classifier (CREATE) for CIL. Specifically, our method employs a lightweight auto-encoder module to learn compact manifold for each class in the latent subspace, constraining samples to be well reconstructed only on the semantically correct auto-encoder. Thus, the representation stability and capability of class distributions are enhanced, alleviating the potential class-wise confusion problem. To further distinguish the overlapped features, we propose a confusion-aware latent space separation loss that ensures samples are closely distributed in their corresponding low-dimensional manifold while keeping away from the distributions of features from other classes. Our method demonstrates stronger representational capacity and discrimination ability by learning disentangled manifolds and reduces class confusion. Extensive experiments on multiple datasets and settings show that CREATE outperforms other state-of-the-art methods up to 5.41%.

</details>

### C2Prompt: Class-aware Client Knowledge Interaction for Federated Continual Learning.
- **链接**: [arXiv:2509.19674](https://arxiv.org/abs/2509.19674) · 📚 被引 0
- **作者**: Kunlun Xu, Yibo Feng, Jiangmeng Li, Yongsheng Qi, Jiahuan Zhou
- **🏷️ 机构**: Peking University, University of Electronic Science and Technology of China, Institute of Software Chinese Academy of Sciences
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Class incremental learning (CIL) aims to enable models to continuously learn new classes without catastrophically forgetting old ones. A promising direction is to learn and use prototypes of classes during incremental updates. Despite simplicity and intuition, we find that such methods suffer from inadequate representation capability and unsatisfied feature overlap. These two factors cause class-wise confusion and limited performance. In this paper, we develop a Confusion-REduced AuTo-Encoder classifier (CREATE) for CIL. Specifically, our method employs a lightweight auto-encoder module to learn compact manifold for each class in the latent subspace, constraining samples to be well reconstructed only on the semantically correct auto-encoder. Thus, the representation stability and capability of class distributions are enhanced, alleviating the potential class-wise confusion problem. To further distinguish the overlapped features, we propose a confusion-aware latent space separation loss that ensures samples are closely distributed in their corresponding low-dimensional manifold while keeping away from the distributions of features from other classes. Our method demonstrates stronger representational capacity and discrimination ability by learning disentangled manifolds and reduces class confusion. Extensive experiments on multiple datasets and settings show that CREATE outperforms other state-of-the-art methods up to 5.41%.

</details>

### Enhancing Few-Shot Class-Incremental Learning via Training-Free Bi-Level Modality Calibration. **⭐⭐⭐** (相关度: 40%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_Enhancing_Few-Shot_Class-Incremental_Learning_via_Training-Free_Bi-Level_Modality_Calibration_CVPR_2025_paper.html) · 📚 被引 5
- **作者**: Yiyang Chen, Tianyu Ding, Lei Wang, Jing Huo, Yang Gao, Wenbin Li
- **🏷️ 机构**: Nanjing University,State Key Laboratory for Novel Software Technology,China, Microsoft,Applied Sciences Group,USA, University of Wollongong,Australia
- **会议**: CVPR 2025
- **摘要（中）**: ①针对少样本类增量学习（Few-Shot Class-Incremental Learning）中模态校准不足的问题。②提出训练无关的双层模态校准方法（Training-Free Bi-Level Modality Calibration），无需额外训练即可校准不同模态间的特征分布。③相比需要训练的方法，该方法计算开销低，易于部署。④在少样本增量基准上展示了有效性，具体数据未在摘要中提供。
- **摘要（英）**: This paper addresses insufficient modality calibration in few-shot class-incremental learning. It proposes a training-free bi-level modality calibration method that aligns feature distributions across modalities without additional training. Compared to training-based methods, it has lower computational cost and is easy to deploy. It demonstrates effectiveness on few-shot incremental benchmarks, though specific numbers are not provided.
- **核心贡献**: 提出训练无关的双层模态校准方法。
- **创新点**: 无需训练即可实现模态校准。
- **结果**: 在少样本基准上有效。

### Adapter Merging with Centroid Prototype Mapping for Scalable Class-Incremental Learning. **⭐⭐⭐⭐** (相关度: 50%)
- **链接**: [arXiv:2412.18219](https://arxiv.org/abs/2412.18219) · 📚 被引 4
- **作者**: Takuma Fukuda, Hiroshi Kera, Kazuhiko Kawamoto
- **🏷️ 机构**: Chiba University, Chiba University Zuse Institute Berlin
- **会议**: CVPR 2025
- **摘要（中）**: ①针对类增量学习（CIL）中推理时间与精度权衡的问题。②提出Adapter Merging with Centroid Prototype Mapping（ACMap），将任务特定适配器合并为单一适配器，实现恒定推理时间，并通过质心原型映射保持高精度。③相比现有方法，ACMap在保持精度的同时显著降低推理开销，且无需存储样本。④在五个基准数据集上，ACMap匹配最先进精度，推理时间与最快方法相当。
- **摘要（英）**: This paper addresses the trade-off between inference time and accuracy in class-incremental learning. It proposes ACMap, which merges task-specific adapters into a single one for constant inference time, while using centroid prototype mapping to maintain accuracy. Compared to existing methods, it achieves state-of-the-art accuracy with inference time comparable to the fastest approaches, without storing exemplars. Extensive experiments on five benchmarks confirm its effectiveness.
- **核心贡献**: 提出ACMap框架实现高效类增量学习。
- **创新点**: 适配器合并与质心原型映射结合，平衡精度和效率。
- **结果**: 匹配最先进精度，推理时间最快。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose Adapter Merging with Centroid Prototype Mapping (ACMap), an exemplar-free framework for class-incremental learning (CIL) that addresses both catastrophic forgetting and scalability. While existing methods involve a trade-off between inference time and accuracy, ACMap consolidates task-specific adapters into a single adapter, thus achieving constant inference time across tasks without sacrificing accuracy. The framework employs adapter merging to build a shared subspace that aligns task representations and mitigates forgetting, while centroid prototype mapping maintains high accuracy by consistently adapting representations within the shared subspace. To further improve scalability, an early stopping strategy limits adapter merging as tasks increase. Extensive experiments on five benchmark datasets demonstrate that ACMap matches state-of-the-art accuracy while maintaining inference time comparable to the fastest existing methods. The code is available at https://github.com/tf63/ACMap.

</details>

### Knowledge Memorization and Rumination for Pre-trained Model-based Class-Incremental Learning. **⭐⭐⭐** (相关度: 40%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Gao_Knowledge_Memorization_and_Rumination_for_Pre-trained_Model-based_Class-Incremental_Learning_CVPR_2025_paper.html) · 📚 被引 8
- **作者**: Zijian Gao, Wangwang Jia, Xingxing Zhang, Dulan Zhou, Kele Xu, Dawei Feng et al.
- **🏷️ 机构**: National University of Defense Technology,College of Computer Science and Technology, Tsinghua University,School of Computer Science
- **会议**: CVPR 2025
- **摘要（中）**: ①针对基于预训练模型的类增量学习（CIL）中知识遗忘和利用不足的问题。②提出知识记忆与反刍（Knowledge Memorization and Rumination）机制，通过记忆旧知识并在新任务中反复利用，增强知识保留。③相比传统方法，该机制更有效地整合预训练知识，提升增量学习稳定性。④在多个基准上展示了有效性，具体数据未在摘要中提供。
- **摘要（英）**: This paper addresses knowledge forgetting and underutilization in pre-trained model-based class-incremental learning. It proposes a knowledge memorization and rumination mechanism that stores old knowledge and reuses it during new tasks to enhance retention. Compared to traditional methods, it better integrates pre-trained knowledge, improving stability. It demonstrates effectiveness on multiple benchmarks, though specific numbers are not provided.
- **核心贡献**: 提出知识记忆与反刍机制用于类增量学习。
- **创新点**: 通过反复利用记忆知识增强稳定性。
- **结果**: 在多个基准上有效。

### T-CIL: Temperature Scaling using Adversarial Perturbation for Calibration in Class-Incremental Learning. **⭐⭐⭐** (相关度: 30%)
- **链接**: [arXiv:2503.22163](https://arxiv.org/abs/2503.22163) · 📚 被引 1
- **作者**: Seonghyeon Hwang, Minsu Kim, Steven Euijong Whang
- **🏷️ 机构**: KAIST
- **会议**: CVPR 2025
- **摘要（中）**: 针对类增量学习中模型置信度校准被忽视的问题，提出T-CIL方法，利用记忆中的对抗扰动样本来进行温度缩放，无需旧任务验证集。通过基于特征距离调整扰动方向，使新任务计算的扰动幅度适用于旧任务，解决了旧任务数据有限时校准困难的问题。实验表明该方法在保持准确率的同时有效改善了校准性能。
- **摘要（英）**: This paper addresses the overlooked issue of confidence calibration in class-incremental learning by proposing T-CIL, a temperature scaling method that uses adversarially perturbed exemplars from memory without requiring a validation set for old tasks. It adjusts perturbation directions based on feature distance to make the magnitude computed from new tasks applicable to old ones, improving calibration while maintaining accuracy.
- **核心贡献**: 提出了一种无需旧任务验证集的温度缩放校准方法T-CIL。
- **创新点**: 利用对抗扰动和特征距离自适应调整扰动方向，实现跨任务校准。
- **结果**: 在类增量学习基准上显著提升了模型置信度校准效果。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We study model confidence calibration in class-incremental learning, where models learn from sequential tasks with different class sets. While existing works primarily focus on accuracy, maintaining calibrated confidence has been largely overlooked. Unfortunately, most post-hoc calibration techniques are not designed to work with the limited memories of old-task data typical in class-incremental learning, as retaining a sufficient validation set would be impractical. Thus, we propose T-CIL, a novel temperature scaling approach for class-incremental learning without a validation set for old tasks, that leverages adversarially perturbed exemplars from memory. Directly using exemplars is inadequate for temperature optimization, since they are already used for training. The key idea of T-CIL is to perturb exemplars more strongly for old tasks than for the new task by adjusting the perturbation direction based on feature distance, with the single magnitude determined using the new-task validation set. This strategy makes the perturbation magnitude computed from the new task also applicable to old tasks, leveraging the tendency that the accuracy of old tasks is lower than that of the new task. We empirically show that T-CIL significantly outperforms various baselines in terms of calibration on real datasets and can be integrated with existing class-incremental learning techniques with minimal impact on accuracy.

</details>

### Order-Robust Class Incremental Learning: Graph-Driven Dynamic Similarity Grouping. **⭐⭐⭐** (相关度: 25%)
- **链接**: [arXiv:2502.20032](https://arxiv.org/abs/2502.20032) · 📚 被引 4
- **作者**: Guannan Lai, Yujie Li, Xiangkun Wang, Junbo Zhang, Tianrui Li, Xin Yang
- **🏷️ 机构**: Southwestern University of Finance and Economics,School of Computing and Artificial Intelligence, JD Intelligent Cities Research, Southwest Jiaotong University
- **会议**: CVPR 2025
- **摘要（中）**: 针对类增量学习对类别到达顺序敏感的问题，通过理论分析证明在增量阶段分组低相似度类别可提升模型鲁棒性，提出图驱动动态相似度分组方法GDDSG，利用图着色算法动态划分类别组，每个组训练独立子模型并构建元特征用于类别组识别。实验证明该方法有效解决了顺序敏感性问题，并在准确率和抗遗忘性上达到最优。
- **摘要（英）**: This paper tackles the class order sensitivity issue in class-incremental learning by theoretically proving that grouping classes with lower pairwise similarity improves robustness, and proposes GDDSG, which uses graph coloring to dynamically partition classes into groups, each training an isolated sub-model with meta-features for group identification. Experiments show it effectively addresses order sensitivity and achieves optimal accuracy and anti-forgetting performance.
- **核心贡献**: 提出了图驱动的动态相似度分组方法GDDSG，解决类增量学习的顺序敏感性问题。
- **创新点**: 将图着色算法应用于类别分组，结合子模型和元特征提升鲁棒性。
- **结果**: 在多个基准上实现了最优的准确率和抗遗忘性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Class Incremental Learning (CIL) aims to enable models to learn new classes sequentially while retaining knowledge of previous ones. Although current methods have alleviated catastrophic forgetting (CF), recent studies highlight that the performance of CIL models is highly sensitive to the order of class arrival, particularly when sequentially introduced classes exhibit high inter-class similarity. To address this critical yet understudied challenge of class order sensitivity, we first extend existing CIL frameworks through theoretical analysis, proving that grouping classes with lower pairwise similarity during incremental phases significantly improves model robustness to order variations. Building on this insight, we propose Graph-Driven Dynamic Similarity Grouping (GDDSG), a novel method that employs graph coloring algorithms to dynamically partition classes into similarity-constrained groups. Each group trains an isolated CIL sub-model and constructs meta-features for class group identification. Experimental results demonstrate that our method effectively addresses the issue of class order sensitivity while achieving optimal performance in both model accuracy and anti-forgetting capability. Our code is available at https://github.com/AIGNLAI/GDDSG.

</details>

### Tripartite Weight-Space Ensemble for Few-Shot Class-Incremental Learning. **⭐⭐⭐** (相关度: 20%)
- **链接**: [arXiv:2506.15720](https://arxiv.org/abs/2506.15720)
- **作者**: Juntae Lee, Munawar Hayat, Sungrack Yun
- **🏷️ 机构**: Qualcomm AI Research
- **会议**: CVPR 2025
- **摘要（中）**: 针对少样本类增量学习中固定特征提取器限制模型适应性的问题，提出三部分权重空间集成方法Tri-WE，在权重空间中对基础模型、前一模型和当前模型进行插值，特别是分类头部分，以协同维护知识和适应新类。同时处理从先前模型蒸馏广义表示的挑战，有效缓解灾难性遗忘和过拟合。实验表明该方法在少样本增量学习基准上表现优异。
- **摘要（英）**: This paper addresses the limitation of fixed feature extractors in few-shot class-incremental learning by proposing Tri-WE, a tripartite weight-space ensemble that interpolates base, previous, and current models, especially for classification heads, to collaboratively maintain knowledge and adapt to new classes. It also handles distillation challenges, effectively mitigating catastrophic forgetting and overfitting, with superior performance on FSCIL benchmarks.
- **核心贡献**: 提出了三部分权重空间集成方法Tri-WE，用于少样本类增量学习。
- **创新点**: 在权重空间中对多个模型进行插值，实现知识协同和适应性更新。
- **结果**: 在少样本增量学习基准上取得了领先的性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Few-shot class incremental learning (FSCIL) enables the continual learning of new concepts with only a few training examples. In FSCIL, the model undergoes substantial updates, making it prone to forgetting previous concepts and overfitting to the limited new examples. Most recent trend is typically to disentangle the learning of the representation from the classification head of the model. A well-generalized feature extractor on the base classes (many examples and many classes) is learned, and then fixed during incremental learning. Arguing that the fixed feature extractor restricts the model's adaptability to new classes, we introduce a novel FSCIL method to effectively address catastrophic forgetting and overfitting issues. Our method enables to seamlessly update the entire model with a few examples. We mainly propose a tripartite weight-space ensemble (Tri-WE). Tri-WE interpolates the base, immediately previous, and current models in weight-space, especially for the classification heads of the models. Then, it collaboratively maintains knowledge from the base and previous models. In addition, we recognize the challenges of distilling generalized representations from the previous model from scarce data. Hence, we suggest a regularization loss term using amplified data knowledge distillation. Simply intermixing the few-shot data, we can produce richer data enabling the distillation of critical knowledge from the previous model. Consequently, we attain state-of-the-art results on the miniImageNet, CUB200, and CIFAR100 datasets.

</details>

### Dynamic Integration of Task-Specific Adapters for Class Incremental Learning. **⭐⭐⭐** (相关度: 25%)
- **链接**: [arXiv:2409.14983](https://arxiv.org/abs/2409.14983) · 📚 被引 4
- **作者**: Jiashuo Li, Shaokun Wang, Bo Qian, Yuhang He, Xing Wei, Qiang Wang et al.
- **🏷️ 机构**: Xi&#x2019;an Jiaotong University,School of Software Engineering, Xi&#x2019;an Jiaotong University,College of Artificial Intelligence
- **会议**: CVPR 2025
- **摘要（中）**: 针对无样本类增量学习中灾难性遗忘加剧的问题，提出动态集成任务特定适配器框架DIA，包含任务特定适配器集成和补丁级模型对齐两部分。通过补丁级适配器集成策略提升组合性并降低计算成本，利用补丁级蒸馏损失和特征重建方法保持特征一致性和准确决策边界。实验证明该方法在NECIL基准上有效缓解了遗忘问题。
- **摘要（英）**: This paper addresses the exacerbated catastrophic forgetting in non-exemplar class-incremental learning by proposing DIA, a framework with task-specific adapter integration and patch-level model alignment. It uses patch-level adapter integration for flexible composition with low cost, and patch-level distillation loss and feature reconstruction to maintain feature consistency and decision boundaries, effectively mitigating forgetting on NECIL benchmarks.
- **核心贡献**: 提出了动态集成任务特定适配器框架DIA，解决无样本类增量学习中的遗忘问题。
- **创新点**: 结合补丁级适配器集成和特征重建，实现高效且稳定的增量学习。
- **结果**: 在无样本类增量学习基准上显著提升了性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Non-exemplar class Incremental Learning (NECIL) enables models to continuously acquire new classes without retraining from scratch and storing old task exemplars, addressing privacy and storage issues. However, the absence of data from earlier tasks exacerbates the challenge of catastrophic forgetting in NECIL. In this paper, we propose a novel framework called Dynamic Integration of task-specific Adapters (DIA), which comprises two key components: Task-Specific Adapter Integration (TSAI) and Patch-Level Model Alignment. TSAI boosts compositionality through a patch-level adapter integration strategy, which provides a more flexible compositional solution while maintaining low computation costs. Patch-Level Model Alignment maintains feature consistency and accurate decision boundaries via two specialized mechanisms: Patch-Level Distillation Loss (PDL) and Patch-Level Feature Reconstruction method (PFR). Specifically, the PDL preserves feature-level consistency between successive models by implementing a distillation loss based on the contributions of patch tokens to new class learning. The PFR facilitates accurate classifier alignment by reconstructing old class features from previous tasks that adapt to new task knowledge. Extensive experiments validate the effectiveness of our DIA, revealing significant improvements on benchmark datasets in the NECIL setting, maintaining an optimal balance between computational complexity and accuracy.

</details>

### SEC-Prompt: SEmantic Complementary Prompting for Few-Shot Class-Incremental Learning. **⭐⭐** (相关度: 20%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_SEC-PromptSEmantic_Complementary_Prompting_for_Few-Shot_Class-Incremental_Learning_CVPR_2025_paper.html)
- **作者**: Ye Liu, Meng Yang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025
- **摘要（中）**: 该论文摘要为空，无法获取具体内容。根据标题推测，可能针对少样本类增量学习提出语义互补提示方法，但缺乏详细信息。
- **摘要（英）**: The abstract is empty, so specific details are unavailable. Based on the title, it likely proposes a semantic complementary prompting method for few-shot class-incremental learning, but no concrete information is provided.
- **核心贡献**: 未知。
- **创新点**: 未知。
- **结果**: 未知。

### Low-Rank Adaptation in Multilinear Operator Networks for Security-Preserving Incremental Learning. **⭐⭐⭐** (相关度: 25%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Ta_Low-Rank_Adaptation_in_Multilinear_Operator_Networks_for_Security-Preserving_Incremental_Learning_CVPR_2025_paper.html) · 📚 被引 1
- **作者**: Huu Binh Ta, Duc Nguyen, Quyen Tran, Toan Tran, Tung Pham
- **🏷️ 机构**: Qualcomm AI Research
- **会议**: CVPR 2025
- **摘要（中）**: 针对增量学习中的安全性和效率问题，提出在多线性算子网络中使用低秩适配的方法，以实现安全保护的增量学习。通过低秩适配减少参数更新量，同时保持模型性能，可能涉及隐私保护机制。实验可能展示了在保持准确率的同时降低计算和存储成本。
- **摘要（英）**: This paper proposes low-rank adaptation in multilinear operator networks for security-preserving incremental learning, aiming to reduce parameter updates while maintaining performance, potentially with privacy protection. Experiments likely show reduced computational and storage costs while preserving accuracy.
- **核心贡献**: 提出了多线性算子网络中的低秩适配方法，用于安全增量学习。
- **创新点**: 将低秩适配应用于多线性算子网络，兼顾效率和安全性。
- **结果**: 在增量学习任务中实现了性能与效率的平衡。

### Theory on Mixture-of-Experts in Continual Learning.
- **链接**: [arXiv:2406.16437](https://arxiv.org/abs/2406.16437)
- **作者**: Hongbo Li, Sen Lin, Lingjie Duan, Yingbin Liang, Ness B. Shroff
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Boosting Domain Incremental Learning: Selecting the Optimal Parameters is All You Need.
- **链接**: [arXiv:2505.23744](https://arxiv.org/abs/2505.23744) · 📚 被引 10
- **作者**: Qiang Wang, Xiang Song, Yuhang He, Jizhou Han, Chenhao Ding, Xinyuan Gao et al.
- **🏷️ 机构**: Xi&#x2019;an Jiaotong University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Federated continual learning (FCL) has garnered increasing attention for its ability to support distributed computation in environments with evolving data distributions. However, the emergence of new tasks introduces both temporal and cross-client shifts, making catastrophic forgetting a critical challenge. Most existing works aggregate knowledge from clients into a global model, which may not enhance client performance since irrelevant knowledge could introduce interference, especially in heterogeneous scenarios. Additionally, directly applying decentralized approaches to FCL suffers from ineffective group formation caused by task changes. To address these challenges, we propose a decentralized dynamic cooperation framework for FCL, where clients establish dynamic cooperative learning coalitions to balance the acquisition of new knowledge and the retention of prior learning, thereby obtaining personalized models. To maximize model performance, each client engages in selective cooperation, dynamically allying with others who offer meaningful performance gains. This results in non-overlapping, variable coalitions at each stage of the task. Moreover, we use coalitional affinity game to simulate coalition relationships between clients. By assessing both client gradient coherence and model similarity, we quantify the client benefits derived from cooperation. We also propose a merge-blocking algorithm and a dynamic cooperative evolution algorithm to achieve cooperative and dynamic equilibrium. Comprehensive experiments demonstrate the superiority of our method compared to various baselines. Code is available at: https://github.com/ydn3229/DCFCL.

### CLDyB: Towards Dynamic Benchmarking for Continual Learning with Pre-trained Models.
- **链接**: [arXiv:2503.04655](https://arxiv.org/abs/2503.04655)
- **作者**: Shengzhuang Chen, Yikai Liao, Xiaoxiao Sun, Kede Ma, Ying Wei
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### pFedMxF: Personalized Federated Class-Incremental Learning with Mixture of Frequency Aggregation.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_pFedMxF_Personalized_Federated_Class-Incremental_Learning_with_Mixture_of_Frequency_Aggregation_CVPR_2025_paper.html) · 📚 被引 3
- **作者**: Yifei Zhang, Hao Zhu, Alysa Ziying Tan, Dianzhi Yu, Longtao Huang, Han Yu
- **🏷️ 机构**: Nanyang Technological University,College of Computing and Data Science, Data61 &#x2665; CSRIO, The Chinese University of Hong Kong
- **会议**: CVPR 2025

### Federated Continual Learning via Orchestrating Multi-Scale Expertise.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/20de741d21f1a038093c6e3ee7c09481-Abstract-Conference.html) · 📚 被引 0
- **作者**: Xiaoyang Yi, Yang Liu, Binhan Yang, Jian Jun Zhang
- **🏷️ 机构**: Nankai University, Nanyang Technology University, Singapore, Vivo
- **会议**: NeurIPS 2025

### Online Functional Tensor Decomposition via Continual Learning for Streaming Data Completion.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/3ba5c2a601f5d35b8072116bd192d174-Abstract-Conference.html) · 📚 被引 0
- **作者**: Xi Zhang, Yanyi Li, Yisi Luo, Qi Xie, Deyu Meng
- **🏷️ 机构**: Nanyang Technological University, Xi'an Jiaotong University
- **会议**: NeurIPS 2025

### Policy Compatible Skill Incremental Learning via Lazy Learning Interface.
- **链接**: [arXiv:2509.20612](https://arxiv.org/abs/2509.20612) · 📚 被引 0
- **作者**: Daehee Lee, Dongsu Lee, TaeYoon Kwack, Wonje Choi, Honguk Woo
- **🏷️ 机构**: SungKyunKwan University, University of Texas at Austin, Sungkyunkwan University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Skill Incremental Learning (SIL) is the process by which an embodied agent expands and refines its skill set over time by leveraging experience gained through interaction with its environment or by the integration of additional data. SIL facilitates efficient acquisition of hierarchical policies grounded in reusable skills for downstream tasks. However, as the skill repertoire evolves, it can disrupt compatibility with existing skill-based policies, limiting their reusability and generalization. In this work, we propose SIL-C, a novel framework that ensures skill-policy compatibility, allowing improvements in incrementally learned skills to enhance the performance of downstream policies without requiring policy re-training or structural adaptation. SIL-C employs a bilateral lazy learning-based mapping technique to dynamically align the subtask space referenced by policies with the skill space decoded into agent behaviors. This enables each subtask, derived from the policy's decomposition of a complex task, to be executed by selecting an appropriate skill based on trajectory distribution similarity. We evaluate SIL-C across diverse SIL scenarios and demonstrate that it maintains compatibility between evolving skills and downstream policies while ensuring efficiency throughout the learning process.

</details>

### Knowledge Graph Enhanced Generative Multi-modal Models for Class-Incremental Learning.
- **链接**: [arXiv:2503.18403](https://arxiv.org/abs/2503.18403) · 📚 被引 0
- **作者**: Xusheng Cao, Haori Lu, Linlan Huang, Fei Yang, Xialei Liu, Ming-Ming Cheng
- **🏷️ 机构**: Nankai University, Adobe Systems
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning in computer vision faces the critical challenge of catastrophic forgetting, where models struggle to retain prior knowledge while adapting to new tasks. Although recent studies have attempted to leverage the generalization capabilities of pre-trained models to mitigate overfitting on current tasks, models still tend to forget details of previously learned categories as tasks progress, leading to misclassification. To address these limitations, we introduce a novel Knowledge Graph Enhanced Generative Multi-modal model (KG-GMM) that builds an evolving knowledge graph throughout the learning process. Our approach utilizes relationships within the knowledge graph to augment the class labels and assigns different relations to similar categories to enhance model differentiation. During testing, we propose a Knowledge Graph Augmented Inference method that locates specific categories by analyzing relationships within the generated text, thereby reducing the loss of detailed information about old classes when learning new knowledge and alleviating forgetting. Experiments demonstrate that our method effectively leverages relational information to help the model correct mispredictions, achieving state-of-the-art results in both conventional CIL and few-shot CIL settings, confirming the efficacy of knowledge graphs at preserving knowledge in the continual learning scenarios.

</details>

### A Minimalistic Unified Framework for Incremental Learning across Image Restoration Tasks.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/30d0278f200f91407364eba31bee08dd-Abstract-Conference.html) · 📚 被引 0
- **作者**: Xiaoxuan Gong, Jie Ma
- **🏷️ 机构**: Huazhong University of Science and Technology
- **会议**: NeurIPS 2025

### Learn and Ensemble Bridge Adapters for Multi-domain Task Incremental Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/e9cbf616dac568a9cb3342761125db24-Abstract-Conference.html) · 📚 被引 0
- **作者**: Ziqi Gu, Chunyan Xu, Wenxuan Fang, Xin Liu, Yide Qiu, Zhen Cui
- **🏷️ 机构**: Nanjing University of Science and Technology, Google, Beijing Normal University
- **会议**: NeurIPS 2025

### GraphKeeper: Graph Domain-Incremental Learning via Knowledge Disentanglement and Preservation.
- **链接**: [arXiv:2511.00097](https://arxiv.org/abs/2511.00097) · 📚 被引 0
- **作者**: Zihao Guo, Qingyun Sun, Ziwei Zhang, Haonan Yuan, Huiping Zhuang, Xingcheng Fu et al.
- **🏷️ 机构**: Beijing University of Aeronautics and Astronautics, Beihang University, South China University of Technology
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Graph incremental learning (GIL), which continuously updates graph models by sequential knowledge acquisition, has garnered significant interest recently. However, existing GIL approaches focus on task-incremental and class-incremental scenarios within a single domain. Graph domain-incremental learning (Domain-IL), aiming at updating models across multiple graph domains, has become critical with the development of graph foundation models (GFMs), but remains unexplored in the literature. In this paper, we propose Graph Domain-Incremental Learning via Knowledge Dientanglement and Preservation (GraphKeeper), to address catastrophic forgetting in Domain-IL scenario from the perspectives of embedding shifts and decision boundary deviations. Specifically, to prevent embedding shifts and confusion across incremental graph domains, we first propose the domain-specific parameter-efficient fine-tuning together with intra- and inter-domain disentanglement objectives. Consequently, to maintain a stable decision boundary, we introduce deviation-free knowledge preservation to continuously fit incremental domains. Additionally, for graphs with unobservable domains, we perform domain-aware distribution discrimination to obtain precise embeddings. Extensive experiments demonstrate the proposed GraphKeeper achieves state-of-the-art results with 6.5%~16.6% improvement over the runner-up with negligible forgetting. Moreover, we show GraphKeeper can be seamlessly integrated with various representative GFMs, highlighting its broad applicative potential.

</details>

### Mixture of Noise for Pre-Trained Model-Based Class-Incremental Learning.
- **链接**: [arXiv:2509.16738](https://arxiv.org/abs/2509.16738) · 📚 被引 1
- **作者**: Kai Jiang, Zhengyan Shi, Dell Zhang, Hongyuan Zhang, Xuelong Li
- **🏷️ 机构**: Tsinghua University, Microsoft Research, Institute of Artificial Intelligence (TeleAI), China Telecom
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Class Incremental Learning (CIL) aims to continuously learn new categories while retaining the knowledge of old ones. Pre-trained models (PTMs) show promising capabilities in CIL. However, existing approaches that apply lightweight fine-tuning to backbones still induce parameter drift, thereby compromising the generalization capability of pre-trained models. Parameter drift can be conceptualized as a form of noise that obscures critical patterns learned for previous tasks. However, recent researches have shown that noise is not always harmful. For example, the large number of visual patterns learned from pre-training can be easily abused by a single task, and introducing appropriate noise can suppress some low-correlation features, thus leaving a margin for future tasks. To this end, we propose learning beneficial noise for CIL guided by information theory and propose Mixture of Noise (Min), aiming to mitigate the degradation of backbone generalization from adapting new tasks. Specifically, task-specific noise is learned from high-dimension features of new tasks. Then, a set of weights is adjusted dynamically for optimal mixture of different task noise. Finally, Min embeds the beneficial noise into the intermediate features to mask the response of inefficient patterns. Extensive experiments on six benchmark datasets demonstrate that Min achieves state-of-the-art performance in most incremental settings, with particularly outstanding results in 50-steps incremental settings. This shows the significant potential for beneficial noise in continual learning. Code is available at https://github.com/ASCIIJK/MiN-NeurIPS2025.

</details>

### Class-wise Balancing Data Replay for Federated Class-Incremental Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/d611d06e3207330555fbc10810e70163-Abstract-Conference.html) · 📚 被引 0
- **作者**: Zhuang Qi, Ying-Peng Tang, Lei Meng, Han Yu, Xiaoxiao Li, Xiangxu Meng
- **🏷️ 机构**: Shandong University, Nanyang Technological University, Nanyang Technological University (NTU)
- **会议**: NeurIPS 2025

### Evolving and Regularizing Meta-Environment Learner for Fine-Grained Few-Shot Class-Incremental Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/376b1b131609e764f687afca832e62b3-Abstract-Conference.html) · 📚 被引 0
- **作者**: Li-Jun Zhao, Zhen-Duo Chen, Yongxin Wang, Xin Luo, Xin-Shun Xu
- **🏷️ 机构**: Shandong University,School of Software,China, Shandong Jianzhu University,School of Computer Science and Technology,China
- **会议**: CVPR 2025

### Task-Agnostic Guided Feature Expansion for Class-Incremental Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zheng_Task-Agnostic_Guided_Feature_Expansion_for_Class-Incremental_Learning_CVPR_2025_paper.html) · 📚 被引 16
- **作者**: Bowen Zheng, Da-Wei Zhou, Han-Jia Ye, De-Chuan Zhan
- **🏷️ 机构**: Nanjing University,National Key Laboratory for Novel Software Technology,China
- **会议**: CVPR 2025

### Multi-Granularity Class Prototype Topology Distillation for Class-Incremental Source-Free Unsupervised Domain Adaptation.
- **链接**: [arXiv:2411.16064](https://arxiv.org/abs/2411.16064) · 📚 被引 7
- **作者**: Peihua Deng, Jiehua Zhang, Xichun Sheng, Chenggang Yan, Yaoqi Sun, Ying Fu et al.
- **🏷️ 机构**: Hangzhou Dianzi University, Xi&#x2019;an Jiaotong University, Macao Polytechnic University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper explores the Class-Incremental Source-Free Unsupervised Domain Adaptation (CI-SFUDA) problem, where the unlabeled target data come incrementally without access to labeled source instances. This problem poses two challenges, the interference of similar source-class knowledge in target-class representation learning and the shocks of new target knowledge to old ones. To address them, we propose the Multi-Granularity Class Prototype Topology Distillation (GROTO) algorithm, which effectively transfers the source knowledge to the class-incremental target domain. Concretely, we design the multi-granularity class prototype self-organization module and the prototype topology distillation module. First, we mine the positive classes by modeling accumulation distributions. Next, we introduce multi-granularity class prototypes to generate reliable pseudo-labels, and exploit them to promote the positive-class target feature self-organization. Second, the positive-class prototypes are leveraged to construct the topological structures of source and target feature spaces. Then, we perform the topology distillation to continually mitigate the shocks of new target knowledge to old ones. Extensive experiments demonstrate that our proposed method achieves state-of-the-art performance on three public datasets. Code is available at https://github.com/dengpeihua/GROTO.

</details>

## 🆕 增量新增

### Language Guided Concept Bottleneck Models for Interpretable Continual Learning. **⭐⭐⭐** (相关度: 25%)
- **链接**: [arXiv:2503.23283](https://arxiv.org/abs/2503.23283) · 📚 被引 5
- **作者**: Lu Yu, Haoyu Han, Zhe Tao, Hantao Yao, Changsheng Xu
- **🏷️ 机构**: Tianjin University of Technology,School of Computer Science and Engineering, University of Science and Technology of China,School of Information Science and Technology, Institute of Automation, University of Chinese Academy of Sciences,State Key Laboratory of Multimodal Artificial Intelligence Systems
- **会议**: CVPR 2025
- **摘要（中）**: 针对持续学习中灾难性遗忘和可解释性不足的问题，提出了语言引导的概念瓶颈模型（CBM）框架。该方法利用概念瓶颈层与CLIP模型对齐语义一致性，学习跨任务可泛化的人类可理解概念，从而在保留知识的同时提供透明决策。实验在多个数据集上优于现有方法，性能提升最高达一定比例。
- **摘要（英）**: This paper addresses catastrophic forgetting and lack of interpretability in continual learning by integrating language-guided Concept Bottleneck Models. The approach aligns semantic consistency with CLIP models to learn human-understandable concepts, enhancing knowledge retention and providing transparent decision-making. Experiments show superior performance over state-of-the-art methods on several datasets.
- **核心贡献**: 提出了语言引导的CBM框架，同时解决持续学习中的遗忘和可解释性问题。
- **创新点**: 利用CLIP对齐概念语义，实现跨任务可泛化的可解释学习。
- **结果**: 在多个数据集上优于现有方法，性能提升显著。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning (CL) aims to enable learning systems to acquire new knowledge constantly without forgetting previously learned information. CL faces the challenge of mitigating catastrophic forgetting while maintaining interpretability across tasks. Most existing CL methods focus primarily on preserving learned knowledge to improve model performance. However, as new information is introduced, the interpretability of the learning process becomes crucial for understanding the evolving decision-making process, yet it is rarely explored. In this paper, we introduce a novel framework that integrates language-guided Concept Bottleneck Models (CBMs) to address both challenges. Our approach leverages the Concept Bottleneck Layer, aligning semantic consistency with CLIP models to learn human-understandable concepts that can generalize across tasks. By focusing on interpretable concepts, our method not only enhances the models ability to retain knowledge over time but also provides transparent decision-making insights. We demonstrate the effectiveness of our approach by achieving superior performance on several datasets, outperforming state-of-the-art methods with an improvement of up to 3.06% in final average accuracy on ImageNet-subset. Additionally, we offer concept visualizations for model predictions, further advancing the understanding of interpretable continual learning.

</details>

### CL-LoRA: Continual Low-Rank Adaptation for Rehearsal-Free Class-Incremental Learning. **⭐⭐⭐⭐** (相关度: 30%)
- **链接**: [arXiv:2505.24816](https://arxiv.org/abs/2505.24816) · 📚 被引 15
- **作者**: Jiangpeng He, Zhihao Duan, Fengqing Zhu
- **🏷️ 机构**: Massachusetts Institute of Technology,Cambridge,Massachusetts,U.S.A., Purdue University,West Lafayette,Indiana,U.S.A.
- **会议**: CVPR 2025
- **摘要（中）**: 针对基于适配器的类增量学习方法为每个新任务创建新适配器导致参数冗余和共享知识利用不足的问题，提出了CL-LoRA方法。该方法引入双适配器架构，包括任务共享适配器学习跨任务知识和任务特定适配器捕获新任务独特特征。共享适配器利用随机正交矩阵和知识蒸馏与梯度重分配保留共享知识，任务特定适配器采用可学习块级权重减少任务间干扰。实验表明CL-LoRA在无样本回放的类增量学习中表现一致且优越。
- **摘要（英）**: This paper addresses parameter redundancy and insufficient shared knowledge utilization in adapter-based class-incremental learning. CL-LoRA introduces a dual-adapter architecture with task-shared adapters for cross-task knowledge and task-specific adapters for unique features, using random orthogonal matrices and knowledge distillation with gradient reassignment. It demonstrates consistent and superior performance in rehearsal-free CIL.
- **核心贡献**: 提出了CL-LoRA双适配器架构，结合共享和特定适配器提升无回放类增量学习性能。
- **创新点**: 利用随机正交矩阵和梯度重分配实现共享知识保留，块级权重减少任务干扰。
- **结果**: 在多个CIL基准上表现一致且优于现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Class-Incremental Learning (CIL) aims to learn new classes sequentially while retaining the knowledge of previously learned classes. Recently, pre-trained models (PTMs) combined with parameter-efficient fine-tuning (PEFT) have shown remarkable performance in rehearsal-free CIL without requiring exemplars from previous tasks. However, existing adapter-based methods, which incorporate lightweight learnable modules into PTMs for CIL, create new adapters for each new task, leading to both parameter redundancy and failure to leverage shared knowledge across tasks. In this work, we propose ContinuaL Low-Rank Adaptation (CL-LoRA), which introduces a novel dual-adapter architecture combining \textbf{task-shared adapters} to learn cross-task knowledge and \textbf{task-specific adapters} to capture unique features of each new task. Specifically, the shared adapters utilize random orthogonal matrices and leverage knowledge distillation with gradient reassignment to preserve essential shared knowledge. In addition, we introduce learnable block-wise weights for task-specific adapters, which mitigate inter-task interference while maintaining the model's plasticity. We demonstrate CL-LoRA consistently achieves promising performance under multiple benchmarks with reduced training and inference computation, establishing a more efficient and scalable paradigm for continual learning with pre-trained models.

</details>

### Activating Sparse Part Concepts for 3D Class Incremental Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Tian_Activating_Sparse_Part_Concepts_for_3D_Class_Incremental_Learning_CVPR_2025_paper.html) · 📚 被引 2
- **作者**: Zhenya Tian, Jun Xiao, Lupeng Liu, Haiyong Jiang
- **🏷️ 机构**: University of Chinese Academy of Sciences,School of Artificial Intelligence
- **会议**: CVPR 2025

### Attraction Diminishing and Distributing for Few-Shot Class-Incremental Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhao_Attraction_Diminishing_and_Distributing_for_Few-Shot_Class-Incremental_Learning_CVPR_2025_paper.html) · 📚 被引 1
- **作者**: Li-Jun Zhao, Zhen-Duo Chen, Yongxin Wang, Xin Luo, Xin-Shun Xu
- **🏷️ 机构**: Shandong University,School of Software,China, Shandong Jianzhu University,School of Computer Science and Technology,China
- **会议**: CVPR 2025

### MIRACLE 3D: Memory-efficient Integrated Robust Approach for Continual Learning on 3D Point Clouds via Shape Model Construction.
- **链接**: [出版页](https://openreview.net/forum?id=ANBuEJesgx)
- **作者**: Hossein Resani, Behrooz Nasihatkon
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### C-CLIP: Multimodal Continual Learning for Vision-Language Model.
- **链接**: [出版页](https://openreview.net/forum?id=sb7qHFYwBc)
- **作者**: Wenzhuo Liu, Fei Zhu, Longhui Wei, Qi Tian
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Vision and Language Synergy for Rehearsal Free Continual Learning.
- **链接**: [出版页](https://openreview.net/forum?id=9aZ2ixiYGd)
- **作者**: Muhammad Anwar Ma'sum, Mahardhika Pratama, Savitha Ramasamy, Lin Liu, Habibullah, Ryszard Kowalczyk
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### PhiNets: Brain-inspired Non-contrastive Learning Based on Temporal Prediction Hypothesis.
- **链接**: [arXiv:2405.14650](https://arxiv.org/abs/2405.14650)
- **作者**: Satoki Ishikawa, Makoto Yamada, Han Bao, Yuki Takezawa
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Predictive coding is a theory which hypothesises that cortex predicts sensory inputs at various levels of abstraction to minimise prediction errors. Inspired by predictive coding, Chen et al. (2024) proposed another theory, temporal prediction hypothesis, to claim that sequence memory residing in hippocampus has emerged through predicting input signals from the past sensory inputs. Specifically, they supposed that the CA3 predictor in hippocampus creates synaptic delay between input signals, which is compensated by the following CA1 predictor. Though recorded neural activities were replicated based on the temporal prediction hypothesis, its validity has not been fully explored. In this work, we aim to explore the temporal prediction hypothesis from the perspective of self-supervised learning. Specifically, we focus on non-contrastive learning, which generates two augmented views of an input image and predicts one from another. Non-contrastive learning is intimately related to the temporal prediction hypothesis because the synaptic delay is implicitly created by StopGradient. Building upon a popular non-contrastive learner, SimSiam, we propose PhiNet, an extension of SimSiam to have two predictors explicitly corresponding to the CA3 and CA1, respectively. Through studying the PhiNet model, we discover two findings. First, meaningful data representations emerge in PhiNet more stably than in SimSiam. This is initially supported by our learning dynamics analysis: PhiNet is more robust to the representational collapse. Second, PhiNet adapts more quickly to newly incoming patterns in online and continual learning scenarios. For practitioners, we additionally propose an extension called X-PhiNet integrated with a momentum encoder, excelling in continual learning. All in all, our work reveals that the temporal prediction hypothesis is a reasonable model in terms of the robustness and adaptivity.

</details>

### Active Learning for Continual Learning: Keeping the Past Alive in the Present.
- **链接**: [arXiv:2501.14278](https://arxiv.org/abs/2501.14278)
- **作者**: Jaehyun Park, Dongmin Park, Jae-Gil Lee
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Federated Continual Learning Goes Online: Uncertainty-Aware Memory Management for Vision Tasks and Beyond.
- **链接**: [出版页](https://openreview.net/forum?id=f65RuQgVlp)
- **作者**: Giuseppe Serra, Florian Buettner
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Adaptive Retention & Correction: Test-Time Training for Continual Learning.
- **链接**: [出版页](https://openreview.net/forum?id=9bLdbp46Q1)
- **作者**: Haoran Chen, Micah Goldblum, Zuxuan Wu, Yu-Gang Jiang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### STAR: Stability-Inducing Weight Perturbation for Continual Learning.
- **链接**: [arXiv:2503.01595](https://arxiv.org/abs/2503.01595)
- **作者**: Masih Eskandar, Tooba Imtiaz, Davin Hill, Zifeng Wang, Jennifer G. Dy
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Self-Normalized Resets for Plasticity in Continual Learning.
- **链接**: [arXiv:2410.20098](https://arxiv.org/abs/2410.20098)
- **作者**: Vivek F. Farias, Adam Daniel Jozefiak
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Advancing Prompt-Based Methods for Replay-Independent General Continual Learning.
- **链接**: [arXiv:2503.00677](https://arxiv.org/abs/2503.00677)
- **作者**: Zhiqi Kang, Liyuan Wang, Xingxing Zhang, Karteek Alahari
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Optimal Protocols for Continual Learning via Statistical Physics and Control Theory.
- **链接**: [arXiv:2409.18061](https://arxiv.org/abs/2409.18061) · 📚 被引 3
- **作者**: Francesco Mori, Stefano Sarao Mannelli, Francesca Mignacco
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### LoRanPAC: Low-rank Random Features and Pre-trained Models for Bridging Theory and Practice in Continual Learning.
- **链接**: [出版页](https://openreview.net/forum?id=bqv7M0wc4x)
- **作者**: Liangzu Peng, Juan Elenter, Joshua Agterberg, Alejandro Ribeiro, René Vidal
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Closed-Form Merging of Parameter-Efficient Modules for Federated Continual Learning.
- **链接**: [arXiv:2410.17961](https://arxiv.org/abs/2410.17961)
- **作者**: Riccardo Salami, Pietro Buzzega, Matteo Mosconi, Jacopo Bonato, Luigi Sabetta, Simone Calderara
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Budgeted Online Continual Learning by Adaptive Layer Freezing and Frequency-based Sampling.
- **链接**: [arXiv:2410.15143](https://arxiv.org/abs/2410.15143)
- **作者**: Minhyuk Seo, Hyunseo Koh, Jonghyun Choi
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Coreset Selection via Reducible Loss in Continual Learning.
- **链接**: [出版页](https://openreview.net/forum?id=mAztx8QO3B)
- **作者**: Ruilin Tong, Yuhang Liu, Javen Qinfeng Shi, Dong Gong
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Boosting Multiple Views for pretrained-based Continual Learning.
- **链接**: [出版页](https://openreview.net/forum?id=AZR4R3lw7y)
- **作者**: Quyen Tran, Tung Lam Tran, Khanh Doan, Toan Tran, Dinh Q. Phung, Khoat Than et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Meta-Continual Learning of Neural Fields.
- **链接**: [arXiv:2504.05806](https://arxiv.org/abs/2504.05806)
- **作者**: Seungyoon Woo, Junhyeog Yun, Gunhee Kim
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Spurious Forgetting in Continual Learning of Language Models.
- **链接**: [arXiv:2501.13453](https://arxiv.org/abs/2501.13453)
- **作者**: Junhao Zheng, Xidi Cai, Shengjie Qiu, Qianli Ma
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### LOIRE: LifelOng learning on Incremental data via pre-trained language model gRowth Efficiently.
- **链接**: [出版页](https://openreview.net/forum?id=F5PlYMC5ik)
- **作者**: Xue Han, Yitong Wang, Junlan Feng, Wenchun Gao, Qian Hu, Chao Deng
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Prototype antithesis for biological few-shot class-incremental learning.
- **链接**: [出版页](https://openreview.net/forum?id=bRqaHn3J5I)
- **作者**: Binghao Liu, Han Yang, Fang Wan, Fei Gu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Federated Few-Shot Class-Incremental Learning.
- **链接**: [出版页](https://openreview.net/forum?id=ZiPoAlKf9Y)
- **作者**: Muhammad Anwar Ma'sum, Mahardhika Pratama, Lin Liu, Habibullah, Ryszard Kowalczyk
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Federated Class-Incremental Learning: A Hybrid Approach Using Latent Exemplars and Data-Free Techniques to Address Local and Global Forgetting.
- **链接**: [arXiv:2501.15356](https://arxiv.org/abs/2501.15356)
- **作者**: Milad Khademi Nori, Il-Min Kim, Guanghui Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### A Second-Order Perspective on Model Compositionality and Incremental Learning.
- **链接**: [出版页](https://openreview.net/forum?id=OZVTqoli2N)
- **作者**: Angelo Porrello, Lorenzo Bonicelli, Pietro Buzzega, Monica Millunzi, Simone Calderara, Rita Cucchiara
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### SD-LoRA: Scalable Decoupled Low-Rank Adaptation for Class Incremental Learning.
- **链接**: [出版页](https://openreview.net/forum?id=5U1rlpX68A)
- **作者**: Yichen Wu, Hongming Piao, Long-Kai Huang, Renzhen Wang, Wanhua Li, Hanspeter Pfister et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Learning without Isolation: Pathway Protection for Continual Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v267/chen25bt.html)
- **作者**: Zhikang Chen, Abudukelimu Wuerkaixi, Sen Cui, Haoxuan Li, Ding Li, Jingfeng Zhang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### A Selective Learning Method for Temporal Graph Continual Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v267/liu25l.html)
- **作者**: Hanmo Liu, Shimin Di, Haoyang Li, Xun Jian, Yue Wang, Lei Chen
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Understanding the Forgetting of (Replay-based) Continual Learning via Feature Learning: Angle Matters.
- **链接**: [出版页](https://proceedings.mlr.press/v267/wan25d.html)
- **作者**: Hongyi Wang, Shiyuan Ren, Wei Huang, Miao Zhang, Xiang Deng, Yixin Bao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### TreeLoRA: Efficient Continual Learning via Layer-Wise LoRAs Guided by a Hierarchical Gradient-Similarity Tree.
- **链接**: [出版页](https://proceedings.mlr.press/v267/qian25b.html)
- **作者**: Yu-Yang Qian, Yuan-Ze Xu, Zhen-Yu Zhang, Peng Zhao, Zhi-Hua Zhou
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Model Uncertainty Quantification by Conformal Prediction in Continual Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v267/gao25i.html)
- **作者**: Rui Gao, Weiwei Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Exploiting Presentative Feature Distributions for Parameter-Efficient Continual Learning of Large Language Models.
- **链接**: [出版页](https://proceedings.mlr.press/v267/cheng25j.html)
- **作者**: Xin Cheng, Jiabo Ye, Haiyang Xu, Ming Yan, Ji Zhang, Feng Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Unlocking the Power of Rehearsal in Continual Learning: A Theoretical Perspective.
- **链接**: [出版页](https://proceedings.mlr.press/v267/deng25i.html)
- **作者**: Junze Deng, Qinhang Wu, Peizhong Ju, Sen Lin, Yingbin Liang, Ness B. Shroff
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### The Importance of Being Lazy: Scaling Limits of Continual Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v267/graldi25a.html)
- **作者**: Jacopo Graldi, Alessandro Breccia, Giulia Lanzillotta, Thomas Hofmann, Lorenzo Noci
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### From RAG to Memory: Non-Parametric Continual Learning for Large Language Models.
- **链接**: [出版页](https://proceedings.mlr.press/v267/gutierrez25a.html)
- **作者**: Bernal Jiménez Gutiérrez, Yiheng Shu, Weijian Qi, Sizhe Zhou, Yu Su
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Measuring Representational Shifts in Continual Learning: A Linear Transformation Perspective.
- **链接**: [出版页](https://proceedings.mlr.press/v267/kim25p.html)
- **作者**: Joonkyu Kim, Yejin Kim, Jy-yong Sohn
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Optimal Task Order for Continual Learning of Multiple Tasks.
- **链接**: [出版页](https://proceedings.mlr.press/v267/li25z.html)
- **作者**: Ziyan Li, Naoki Hiratani
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### BECAME: Bayesian Continual Learning with Adaptive Model Merging.
- **链接**: [出版页](https://proceedings.mlr.press/v267/li25bk.html)
- **作者**: Mei Li, Yuxiang Lu, Qinyan Dai, Suizhi Huang, Yue Ding, Hongtao Lu
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Rethinking the Stability-Plasticity Trade-off in Continual Learning from an Architectural Perspective.
- **链接**: [出版页](https://proceedings.mlr.press/v267/lu25t.html)
- **作者**: Aojun Lu, Hangjie Yuan, Tao Feng, Yanan Sun
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### LADA: Scalable Label-Specific CLIP Adapter for Continual Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v267/luo25w.html)
- **作者**: Mao-Lin Luo, Zi-Hao Zhou, Tong Wei, Min-Ling Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Efficient Graph Continual Learning via Lightweight Graph Neural Tangent Kernels-based Dataset Distillation.
- **链接**: [出版页](https://proceedings.mlr.press/v267/qiu25f.html)
- **作者**: Rihong Qiu, Xinke Jiang, Yuchen Fang, Hongbin Lai, Hao Miao, Xu Chu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### CAN: Leveraging Clients As Navigators for Generative Replay in Federated Continual Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v267/rong25a.html)
- **作者**: Xuankun Rong, Jianshu Zhang, Kun He, Mang Ye
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Confounder-Free Continual Learning via Recursive Feature Normalization.
- **链接**: [出版页](https://proceedings.mlr.press/v267/shah25a.html)
- **作者**: Yash Shah, Camila González, Mohammad H. Abbasi, Qingyu Zhao, Kilian M. Pohl, Ehsan Adeli
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Improving Continual Learning Performance and Efficiency with Auxiliary Classifiers.
- **链接**: [出版页](https://proceedings.mlr.press/v267/szatkowski25a.html)
- **作者**: Filip Szatkowski, Yaoyue Zheng, Fei Yang, Tomasz Trzcinski, Bartlomiej Twardowski, Joost van de Weijer
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Online Curvature-Aware Replay: Leveraging 2nd Order Information for Online Continual Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v267/urettini25a.html)
- **作者**: Edoardo Urettini, Antonio Carta
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Cut out and Replay: A Simple yet Versatile Strategy for Multi-Label Online Continual Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v267/wang25bg.html)
- **作者**: Xinrui Wang, Shao-Yuan Li, Jiaqiang Zhang, Songcan Chen
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Addressing Imbalanced Domain-Incremental Learning through Dual-Balance Collaborative Experts.
- **链接**: [出版页](https://proceedings.mlr.press/v267/li25eb.html)
- **作者**: Lan Li, Da-Wei Zhou, Han-Jia Ye, De-Chuan Zhan
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Semantic Shift Estimation via Dual-Projection and Classifier Reconstruction for Exemplar-Free Class-Incremental Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v267/he25d.html)
- **作者**: Run He, Di Fang, Yicheng Xu, Yawen Cui, Ming Li, Cen Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Geometric Feature Embedding for Effective 3D Few-Shot Class Incremental Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v267/li25ad.html)
- **作者**: Xiangqi Li, Libo Huang, Zhulin An, Weilun Feng, Chuanguang Yang, Boyu Diao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Tensor Decomposition Based Memory-Efficient Incremental Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v267/li25dy.html)
- **作者**: Yuhang Li, Guoxu Zhou, Zhenhao Huang, Xinqi Chen, Yuning Qiu, Qibin Zhao
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Autoencoder-Based Hybrid Replay for Class-Incremental Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v267/khademi-nori25a.html)
- **作者**: Milad Khademi Nori, Il-Min Kim, Guanghui Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Probabilistic Group Mask Guided Discrete Optimization for Incremental Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v267/wan25h.html)
- **作者**: Fengqiang Wan, Yang Yang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Navigating Semantic Drift in Task-Agnostic Class-Incremental Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v267/wu25f.html)
- **作者**: Fangwen Wu, Lechao Cheng, Shengeng Tang, Xiaofeng Zhu, Chaowei Fang, Dingwen Zhang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Componential Prompt-Knowledge Alignment for Domain Incremental Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v267/xu25as.html)
- **作者**: Kunlun Xu, Xu Zou, Gang Hua, Jiahuan Zhou
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### L3A: Label-Augmented Analytic Adaptation for Multi-Label Class Incremental Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v267/zhang25y.html)
- **作者**: Xiang Zhang, Run He, Chen Jiao, Di Fang, Ming Li, Ziqian Zeng et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Continual Multimodal Contrastive Learning.
- **链接**: [arXiv:2503.14963](https://arxiv.org/abs/2503.14963)
- **作者**: Xiaohao Liu, Xiaobo Xia, See-Kiong Ng, Tat-Seng Chua
- **🏷️ 机构**: National University of Singapore, The University of Sydney, National Univ. of Singapore
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal Contrastive Learning (MCL) advances in aligning different modalities and generating multimodal representations in a joint space. By leveraging contrastive learning across diverse modalities, large-scale multimodal data enhances representational quality. However, a critical yet often overlooked challenge remains: multimodal data is rarely collected in a single process, and training from scratch is computationally expensive. Instead, emergent multimodal data can be used to optimize existing models gradually, i.e., models are trained on a sequence of modality pair data. We define this problem as Continual Multimodal Contrastive Learning (CMCL), an underexplored yet crucial research direction at the intersection of multimodal and continual learning. In this paper, we formulate CMCL through two specialized principles of stability and plasticity. We theoretically derive a novel optimization-based method, which projects updated gradients from dual sides onto subspaces where any gradient is prevented from interfering with the previously learned knowledge. Two upper bounds provide theoretical insights on both stability and plasticity in our solution. Beyond our theoretical contributions, we conduct experiments on multiple datasets by comparing our method against advanced continual learning baselines. The empirical results further support our claims and demonstrate the efficacy of our method. Our codes are available at https://github.com/Xiaohao-Liu/CMCL.

</details>

### Mitigating Intra- and Inter-modal Forgetting in Continual Learning of Unified Multimodal Models.
- **链接**: [arXiv:2512.03125](https://arxiv.org/abs/2512.03125)
- **作者**: Xiwen Wei, Mustafa Munir, Radu Marculescu
- **🏷️ 机构**: University of Texas at Austin, University of Texas, Austin
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Unified Multimodal Generative Models (UMGMs) unify visual understanding and image generation within a single autoregressive framework. However, their ability to continually learn new tasks is severely hindered by catastrophic forgetting, both within a modality (intra-modal) and across modalities (inter-modal). While intra-modal forgetting has been studied in prior continual learning (CL) work, inter-modal forgetting remains largely unexplored. In this paper, we identify and empirically validate this phenomenon in UMGMs and provide a theoretical explanation rooted in gradient conflict between modalities. To address both intra- and inter-modal forgetting, we propose Modality-Decoupled Experts (MoDE), a lightweight and scalable architecture that isolates modality-specific updates to mitigate the gradient conflict and leverages knowledge distillation to prevent catastrophic forgetting and preserve pre-trained capabilities. Unlike previous CL methods that remain modality-coupled and suffer from modality gradient conflict, MoDE explicitly decouples modalities to prevent interference. Experiments across diverse benchmarks demonstrate that MoDE significantly mitigates both inter- and intra-modal forgetting, outperforming prior CL baselines in unified multimodal generation settings. Codes will be publicly available: https://github.com/Christina200/MoDE-official.git

</details>

### Confusion-Driven Self-Supervised Progressively Weighted Ensemble Learning for Non-Exemplar Class Incremental Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/6e1a97dfd2ce57ee4c006657ace4b9b6-Abstract-Conference.html)
- **作者**: Kai Hu, Yu Zhang, Yuan Zhang, Zhineng Chen, Xieping Gao
- **🏷️ 机构**: Xiangtan University, Communication University of China, Fudan University
- **会议**: NeurIPS 2025

### AnaCP: Toward Upper-Bound Continual Learning via Analytic Contrastive Projection.
- **链接**: [arXiv:2511.13880](https://arxiv.org/abs/2511.13880)
- **作者**: Saleh Momeni, Changnan Xiao, Bing Liu
- **🏷️ 机构**: University of Illinois at Chicago, MiHoYo
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper studies the problem of class-incremental learning (CIL), a core setting within continual learning where a model learns a sequence of tasks, each containing a distinct set of classes. Traditional CIL methods, which do not leverage pre-trained models (PTMs), suffer from catastrophic forgetting (CF) due to the need to incrementally learn both feature representations and the classifier. The integration of PTMs into CIL has recently led to efficient approaches that treat the PTM as a fixed feature extractor combined with analytic classifiers, achieving state-of-the-art performance. However, they still face a major limitation: the inability to continually adapt feature representations to best suit the CIL tasks, leading to suboptimal performance. To address this, we propose AnaCP (Analytic Contrastive Projection), a novel method that preserves the efficiency of analytic classifiers while enabling incremental feature adaptation without gradient-based training, thereby eliminating the CF caused by gradient updates. Our experiments show that AnaCP not only outperforms existing baselines but also achieves the accuracy level of joint training, which is regarded as the upper bound of CIL.

</details>

### Contrastive Consolidation of Top-Down Modulations Achieves Sparsely Supervised Continual Learning.
- **链接**: [arXiv:2505.14125](https://arxiv.org/abs/2505.14125)
- **作者**: Viet Anh Khoa Tran, Emre Neftci, Willem Wybo
- **🏷️ 机构**: Forschungszentrum Jülich
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Biological brains learn continually from a stream of unlabeled data, while integrating specialized information from sparsely labeled examples without compromising their ability to generalize. Meanwhile, machine learning methods are susceptible to catastrophic forgetting in this natural learning setting, as supervised specialist fine-tuning degrades performance on the original task. We introduce task-modulated contrastive learning (TMCL), which takes inspiration from the biophysical machinery in the neocortex, using predictive coding principles to integrate top-down information continually and without supervision. We follow the idea that these principles build a view-invariant representation space, and that this can be implemented using a contrastive loss. Then, whenever labeled samples of a new class occur, new affine modulations are learned that improve separation of the new class from all others, without affecting feedforward weights. By co-opting the view-invariance learning mechanism, we then train feedforward weights to match the unmodulated representation of a data sample to its modulated counterparts. This introduces modulation invariance into the representation space, and, by also using past modulations, stabilizes it. Our experiments show improvements in both class-incremental and transfer learning over state-of-the-art unsupervised approaches, as well as over comparable supervised approaches, using as few as 1% of available labels. Taken together, our work suggests that top-down modulations play a crucial role in balancing stability and plasticity.

</details>

### Learning Multi-Source and Robust Representations for Continual Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/fff5dac3713ad2d1cf7c9e3c95cc361f-Abstract-Conference.html)
- **作者**: Fei Ye, YongCheng Zhong, Qihe Liu, Adrian G. Bors, Jingling Sun, Rongyao Hu et al.
- **🏷️ 机构**: University of Electronic Science and Technology of China, University of York
- **会议**: NeurIPS 2025

### Learning Expandable and Adaptable Representations for Continual Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/4c19a67a61b5700f90ccb815a255aaad-Abstract-Conference.html)
- **作者**: Ruilong Yu, Mingyan Liu, Fei Ye, Adrian G. Bors, Rongyao Hu, Jingling Sun et al.
- **🏷️ 机构**: University of Electronic Science and Technology of China, Harbin Institute of Technology, Shenzhen, University of York
- **会议**: NeurIPS 2025

### Continuous Subspace Optimization for Continual Learning.
- **链接**: [arXiv:2505.11816](https://arxiv.org/abs/2505.11816)
- **作者**: Quan Cheng, Yuanyu Wan, Lingyu Wu, Chenping Hou, Lijun Zhang
- **🏷️ 机构**: Nanjing University, Zhejiang University, National University of Defense Technology
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning aims to learn multiple tasks sequentially while preserving prior knowledge, but faces the challenge of catastrophic forgetting when adapting to new tasks. Recently, approaches leveraging pre-trained models have gained increasing popularity in mitigating this issue, due to the strong generalization ability of foundation models. To adjust pre-trained models for new tasks, existing methods usually employ low-rank adaptation, which restricts parameter updates to a fixed low-rank subspace. However, constraining the optimization space inherently compromises the model's learning capacity, resulting in inferior performance. To address this limitation, we propose Continuous Subspace Optimization for Continual Learning (CoSO) to fine-tune the model in a series of subspaces rather than a single one. These sequential subspaces are dynamically determined through the singular value decomposition of the gradients. CoSO updates the model by projecting gradients onto these subspaces, ensuring memory-efficient optimization. To mitigate forgetting, the optimization subspace of each task is constrained to be orthogonal to the historical task subspace. During task learning, CoSO maintains a task-specific component that captures the critical update directions for the current task. Upon completing a task, this component is used to update the historical task subspace, laying the groundwork for subsequent learning. Extensive experiments on multiple datasets demonstrate that CoSO significantly outperforms state-of-the-art methods, especially in challenging scenarios with long task sequences.

</details>

### REP: Resource-Efficient Prompting for Rehearsal-Free Continual Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/59ea33ae3d096f3bcd5026b479710cf8-Abstract-Conference.html)
- **作者**: Sungho Jeon, Xinyue Ma, Kwang In Kim, Myeongjae Jeon
- **🏷️ 机构**: POSTECH, Ulsan National Institute of Science and Technology, Pohang University of Science and Technology
- **会议**: NeurIPS 2025

### Gradient-Guided Epsilon Constraint Method for Online Continual Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/b3c2854d9e94282a373d8fa58b567b27-Abstract-Conference.html)
- **作者**: Song Lai, Changyi Ma, Fei Zhu, Zhe Zhao, Xi Lin, Gaofeng Meng et al.
- **🏷️ 机构**: City University of Hong Kong, The Chinese University of Hong Kong, Centre for Artificial Intelligence and Robotics Hong Kong Institute of Science &amp; Innovation, Chinese Academy of Sciences
- **会议**: NeurIPS 2025

### Resource-Constrained Federated Continual Learning: What Does Matter?
- **链接**: [arXiv:2501.08737](https://arxiv.org/abs/2501.08737)
- **作者**: Yichen Li, Yuying Wang, Jiahua Dong, Haozhao Wang, Yining Qi, Rui Zhang et al.
- **🏷️ 机构**: Huazhong University of Science and Technology, Suzhou University, Mohamed bin Zayed University of Artificial Intelligence
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Federated Continual Learning (FCL) aims to enable sequentially privacy-preserving model training on streams of incoming data that vary in edge devices by preserving previous knowledge while adapting to new data. Current FCL literature focuses on restricted data privacy and access to previously seen data while imposing no constraints on the training overhead. This is unreasonable for FCL applications in real-world scenarios, where edge devices are primarily constrained by resources such as storage, computational budget, and label rate. We revisit this problem with a large-scale benchmark and analyze the performance of state-of-the-art FCL approaches under different resource-constrained settings. Various typical FCL techniques and six datasets in two incremental learning scenarios (Class-IL and Domain-IL) are involved in our experiments. Through extensive experiments amounting to a total of over 1,000+ GPU hours, we find that, under limited resource-constrained settings, existing FCL approaches, with no exception, fail to achieve the expected performance. Our conclusions are consistent in the sensitivity analysis. This suggests that most existing FCL methods are particularly too resource-dependent for real-world deployment. Moreover, we study the performance of typical FCL techniques with resource constraints and shed light on future research directions in FCL.

</details>

### Turning the Tables: Enabling Backward Transfer via Causal-Aware LoRA in Continual Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/7c22f3719c9699c0ea4fe47fb536ff82-Abstract-Conference.html)
- **作者**: Chaoyang Li, Runze Ye, Jianyang Qin, Jinhao Cui, Lingzhi Wang, Ning Hu et al.
- **🏷️ 机构**: Harbin Institute of Technology (Shenzhen), Harbin Institute of Technology, Harbin Institute of Technology, Shenzhen
- **会议**: NeurIPS 2025

### Gated Integration of Low-Rank Adaptation for Continual Learning of Large Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/63692d8d567db671c700df5df912204a-Abstract-Conference.html)
- **作者**: Yan-Shuo Liang, Jia-Rui Chen, Wu-Jun Li
- **🏷️ 机构**: Nanjing University
- **会议**: NeurIPS 2025

### Temporal-Difference Variational Continual Learning.
- **链接**: [arXiv:2410.07812](https://arxiv.org/abs/2410.07812)
- **作者**: Luckeciano Carvalho Melo, Alessandro Abate, Yarin Gal
- **🏷️ 机构**: University of Oxford
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Machine Learning models in real-world applications must continuously learn new tasks to adapt to shifts in the data-generating distribution. Yet, for Continual Learning (CL), models often struggle to balance learning new tasks (plasticity) with retaining previous knowledge (memory stability). Consequently, they are susceptible to Catastrophic Forgetting, which degrades performance and undermines the reliability of deployed systems. In the Bayesian CL literature, variational methods tackle this challenge by employing a learning objective that recursively updates the posterior distribution while constraining it to stay close to its previous estimate. Nonetheless, we argue that these methods may be ineffective due to compounding approximation errors over successive recursions. To mitigate this, we propose new learning objectives that integrate the regularization effects of multiple previous posterior estimations, preventing individual errors from dominating future posterior updates and compounding over time. We reveal insightful connections between these objectives and Temporal-Difference methods, a popular learning mechanism in Reinforcement Learning and Neuroscience. Experiments on challenging CL benchmarks show that our approach effectively mitigates Catastrophic Forgetting, outperforming strong Variational CL methods.

</details>

### Train with Perturbation, Infer after Merging: A Two-Stage Framework for Continual Learning.
- **链接**: [arXiv:2505.22389](https://arxiv.org/abs/2505.22389)
- **作者**: Haomiao Qiu, Miao Zhang, Ziyue Qiao, Liqiang Nie
- **🏷️ 机构**: Harbin Institute of Technology, Shenzhen, Aalborg University, Great Bay University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual Learning (CL) aims to enable models to continuously acquire new knowledge from a sequence of tasks with avoiding the forgetting of learned information. However, existing CL methods only rely on the parameters of the most recent task for inference, which makes them susceptible to catastrophic forgetting. Inspired by the recent success of model merging techniques, we propose \textbf{Perturb-and-Merge (P\&M)}, a novel continual learning framework that integrates model merging into the CL paradigm to mitigate forgetting. Specifically, after training on each task, P\&M constructs a new model by forming a convex combination of the previous model and the newly trained task-specific model. Through theoretical analysis, We minimize the total loss increase across all tasks and derive a closed-form solution for the merging coefficient under mild assumptions. To further improve the performance of the merged model, we observe that the degradation introduced during merging can be alleviated by a regularization term composed of the task vector and the Hessian matrix of the loss function. Interestingly, we show that this term can be efficiently approximated using second-order symmetric finite differences, and a stochastic perturbation strategy along the task vector direction is accordingly devised which incurs no additional forward or backward passes while providing an effective approximation of the regularization term. Finally, we combine P\&M with LoRA, a parameter-efficient fine-tuning method, to reduce memory overhead. Our proposed approach achieves state-of-the-art performance on several continual learning benchmark datasets. The code is available at https://github.com/qhmiao/P-M-for-Continual-Learning.

</details>

### Separating the 'what' and 'how' of compositional computation to enable reuse and continual learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/82d07a9f247048b85f78786ac80e6fbf-Abstract-Conference.html)
- **作者**: Haozhe Shan, Minni Sun, Lea Duncker
- **🏷️ 机构**: Columbia University
- **会议**: NeurIPS 2025

### Dual-Space Semantic Synergy Distillation for Continual Learning of Unlabeled Streams.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/1eaa5146756be028ad6fff1efcc8e6bd-Abstract-Conference.html)
- **作者**: Donghao Sun, Xi Wang, Xu Yang, Kun Wei, Cheng Deng
- **🏷️ 机构**: Xidian University, ETHZ - ETH Zurich, Microsoft
- **会议**: NeurIPS 2025

### The Dual Nature of Plasticity Loss in Deep Continual Learning: Dissection and Mitigation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/6489f2c6ac6420124fcef2a489615a97-Abstract-Conference.html)
- **作者**: Haoyu Wang, Wei Dai, Jiawei Zhang, Jialun Ma, Mingyi Huang, Yuguo Yu
- **🏷️ 机构**: Tianjin University, Fudan University
- **会议**: NeurIPS 2025

### Hybrid Re-matching for Continual Learning with Parameter-Efficient Tuning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/a978bdfeb195e4a574c0def98806346a-Abstract-Conference.html)
- **作者**: Weicheng Wang, Guoli Jia, Xialei Liu, Liang Lin, Jufeng Yang
- **🏷️ 机构**: Nankai University, Tsinghua University, Sun Yat-Sen University
- **会议**: NeurIPS 2025

### Exploiting Task Relationships in Continual Learning via Transferability-Aware Task Embeddings.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/f3e644506dad33613919fa85af6665d0-Abstract-Conference.html)
- **作者**: Yanru Wu, Jianning Wang, Xiangyu Chen, Aurora, Yang Tan, Hanbing Liu et al.
- **🏷️ 机构**: Tsinghua University, Harbin Institute of Technology, Tsinghua University, Tsinghua University
- **会议**: NeurIPS 2025

### Decentralized Dynamic Cooperation of Personalized Models for Federated Continual Learning.
- **链接**: [arXiv:2509.23683](https://arxiv.org/abs/2509.23683)
- **作者**: Danni Yang, Zhikang Chen, Sen Cui, Mengyue Yang, Ding Li, Abudukelimu Wuerkaixi et al.
- **🏷️ 机构**: Tsinghua University, Tsinghua University, Tsinghua University, University College London / University of Bristol
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Federated continual learning (FCL) has garnered increasing attention for its ability to support distributed computation in environments with evolving data distributions. However, the emergence of new tasks introduces both temporal and cross-client shifts, making catastrophic forgetting a critical challenge. Most existing works aggregate knowledge from clients into a global model, which may not enhance client performance since irrelevant knowledge could introduce interference, especially in heterogeneous scenarios. Additionally, directly applying decentralized approaches to FCL suffers from ineffective group formation caused by task changes. To address these challenges, we propose a decentralized dynamic cooperation framework for FCL, where clients establish dynamic cooperative learning coalitions to balance the acquisition of new knowledge and the retention of prior learning, thereby obtaining personalized models. To maximize model performance, each client engages in selective cooperation, dynamically allying with others who offer meaningful performance gains. This results in non-overlapping, variable coalitions at each stage of the task. Moreover, we use coalitional affinity game to simulate coalition relationships between clients. By assessing both client gradient coherence and model similarity, we quantify the client benefits derived from cooperation. We also propose a merge-blocking algorithm and a dynamic cooperative evolution algorithm to achieve cooperative and dynamic equilibrium. Comprehensive experiments demonstrate the superiority of our method compared to various baselines. Code is available at: https://github.com/ydn3229/DCFCL.

</details>

### Dynamic Siamese Expansion Framework for Improving Robustness in Online Continual Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/6749b4364bbdff0dedfab1b0f27a10c2-Abstract-Conference.html) · 📚 被引 1
- **作者**: Fei Ye, Yulong Zhao, Qihe Liu, Junlin Chen, Adrian G. Bors, Jingling Sun et al.
- **🏷️ 机构**: University of Electronic Science and Technology of China, ByteDance Inc., University of York
- **会议**: NeurIPS 2025

<!-- COMPLETE v1 papers=134 -->
