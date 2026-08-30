# Continual Learning — 2022 Guideline

> 领域: 持续学习 / 增量学习（含 VLM/多模态场景）
> 论文数: 29 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份:

### Meta-attention for ViT-backed Continual Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00025)
- **作者**: Mengqi Xue, Haofei Zhang, Jie Song, Mingli Song
- **🏷️ 机构**: ZJU
- **会议**: CVPR 2022

### vCLIMB: A Novel Video Class Incremental Learning Benchmark. **⭐⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2201.09381](https://arxiv.org/abs/2201.09381) · 📚 被引 35
- **作者**: Andrés Villa, Kumail Alhamoud, Victor Escorcia, Fabian Caba Heilbron, Juan León Alcázar, Bernard Ghanem
- **🏷️ 机构**: Pontificia Universidad Cat&#x00F3;lica de Chile, King Abdullah University of Science and Technology (KAUST), Samsung AI Center Cambridge
- **会议**: CVPR 2022
- **摘要（中）**: 针对视频持续学习领域缺乏标准化基准的问题，本文提出vCLIMB基准，专注于类增量学习，均匀分配类别分布，并发现视频数据中帧级记忆选择和未修剪数据影响采样策略的独特挑战。为解决这些问题，提出时间一致性正则化，可应用于基于记忆的持续学习方法，在未修剪持续学习任务上提升基线高达24%。
- **摘要（英）**: This paper introduces vCLIMB, a standardized video continual learning benchmark focusing on class incremental learning with uniform class distribution, and identifies unique challenges in frame-level memory selection and untrimmed data sampling. A temporal consistency regularization is proposed to address these, improving baseline performance by up to 24% on untrimmed tasks.
- **核心贡献**: 提出了视频持续学习基准vCLIMB和时间一致性正则化方法，解决了视频数据中的独特挑战。
- **创新点**: 首次系统分析视频持续学习中的帧级记忆和未修剪数据问题，并设计针对性正则化。
- **结果**: 在vCLIMB上显著提升持续学习性能，最高提升24%。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning (CL) is under-explored in the video domain. The few existing works contain splits with imbalanced class distributions over the tasks, or study the problem in unsuitable datasets. We introduce vCLIMB, a novel video continual learning benchmark. vCLIMB is a standardized test-bed to analyze catastrophic forgetting of deep models in video continual learning. In contrast to previous work, we focus on class incremental continual learning with models trained on a sequence of disjoint tasks, and distribute the number of classes uniformly across the tasks. We perform in-depth evaluations of existing CL methods in vCLIMB, and observe two unique challenges in video data. The selection of instances to store in episodic memory is performed at the frame level. Second, untrimmed training data influences the effectiveness of frame sampling strategies. We address these two challenges by proposing a temporal consistency regularization that can be applied on top of memory-based continual learning methods. Our approach significantly improves the baseline, by up to 24% on the untrimmed continual learning task.

</details>

### Overcoming Catastrophic Forgetting in Incremental Object Detection via Elastic Response Distillation. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2204.02136](https://arxiv.org/abs/2204.02136) · 📚 被引 117
- **作者**: Tao Feng, Mang Wang, Hangjie Yuan
- **🏷️ 机构**: Alibaba Group, Zhejiang University
- **会议**: CVPR 2022
- **摘要（中）**: 针对增量目标检测（IOD）中灾难性遗忘问题，本文提出弹性响应蒸馏（ERD）方法，专注于从分类头和回归头弹性学习响应，通过弹性响应选择（ERS）策略评估位置质量并提供有价值响应，并强调不同响应在蒸馏中应分配不同重要性。在MS COCO上的实验表明，ERD有效缓解遗忘，提升增量检测性能。
- **摘要（英）**: This paper addresses catastrophic forgetting in incremental object detection (IOD) by proposing Elastic Response Distillation (ERD), which focuses on elastically learning responses from classification and regression heads, with an Elastic Response Selection (ERS) strategy to evaluate location quality and assign importance. Experiments on MS COCO demonstrate ERD effectively mitigates forgetting and improves incremental detection performance.
- **核心贡献**: 提出了弹性响应蒸馏方法，通过选择性响应蒸馏提升增量目标检测性能。
- **创新点**: 引入弹性响应选择策略，动态评估响应质量并分配重要性，优于传统蒸馏方法。
- **结果**: 在MS COCO上验证了方法的有效性，显著缓解灾难性遗忘。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Traditional object detectors are ill-equipped for incremental learning. However, fine-tuning directly on a well-trained detection model with only new data will lead to catastrophic forgetting. Knowledge distillation is a flexible way to mitigate catastrophic forgetting. In Incremental Object Detection (IOD), previous work mainly focuses on distilling for the combination of features and responses. However, they under-explore the information that contains in responses. In this paper, we propose a response-based incremental distillation method, dubbed Elastic Response Distillation (ERD), which focuses on elastically learning responses from the classification head and the regression head. Firstly, our method transfers category knowledge while equipping student detector with the ability to retain localization information during incremental learning. In addition, we further evaluate the quality of all locations and provide valuable responses by the Elastic Response Selection (ERS) strategy. Finally, we elucidate that the knowledge from different responses should be assigned with different importance during incremental distillation. Extensive experiments conducted on MS COCO demonstrate our method achieves state-of-the-art result, which substantially narrows the performance gap towards full training.

</details>

### Continual Learning with Lifelong Vision Transformer. **⭐⭐⭐** (相关度: 65%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00027) · 📚 被引 63
- **作者**: Zhen Wang, Liu Liu, Yiqun Duan, Yajing Kong, Dacheng Tao
- **🏷️ 机构**: The University of Sydney,Australia, University of Technology Sydney,Australia, JD Explore Academy,China
- **会议**: CVPR 2022
- **摘要（中）**: 该论文摘要缺失，无法获取具体内容。根据标题推测，可能涉及使用终身视觉Transformer进行持续学习，但缺乏详细信息。
- **摘要（英）**: The abstract is missing, so specific details are unavailable. Based on the title, it likely explores lifelong vision transformers for continual learning, but no concrete information is provided.
- **核心贡献**: 未知，因摘要缺失。
- **创新点**: 未知，因摘要缺失。
- **结果**: 未知，因摘要缺失。

### Learning to Prompt for Continual Learning. **⭐⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2112.08654](https://arxiv.org/abs/2112.08654)
- **作者**: Zifeng Wang, Zizhao Zhang, Chen-Yu Lee, Han Zhang, Ruoxi Sun, Xiaoqi Ren et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2022
- **摘要（中）**: 针对传统持续学习依赖重放缓冲区或任务身份的问题，本文提出L2P方法，通过动态提示（prompts）预训练模型，在无需任务身份的情况下顺序学习任务。提示作为可学习参数存储在记忆空间中，优化以管理任务不变和任务特定知识，保持模型可塑性。在多个图像分类基准上，L2P一致优于现有方法，甚至在没有重放缓冲区的情况下达到与基于重放方法竞争的结果。
- **摘要（英）**: This paper proposes L2P, a new continual learning paradigm that dynamically prompts a pre-trained model to learn tasks sequentially without task identity at test time. Prompts are learnable parameters in a memory space, optimized to manage task-invariant and task-specific knowledge, achieving state-of-the-art results on image classification benchmarks and competitive performance with rehearsal-based methods even without a buffer.
- **核心贡献**: 提出了基于动态提示的持续学习框架，无需任务身份和重放缓冲区。
- **创新点**: 将提示学习引入持续学习，通过可学习提示管理知识，创新性强。
- **结果**: 在多个基准上超越现有方法，且无缓冲区时仍具竞争力。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The mainstream paradigm behind continual learning has been to adapt the model parameters to non-stationary data distributions, where catastrophic forgetting is the central challenge. Typical methods rely on a rehearsal buffer or known task identity at test time to retrieve learned knowledge and address forgetting, while this work presents a new paradigm for continual learning that aims to train a more succinct memory system without accessing task identity at test time. Our method learns to dynamically prompt (L2P) a pre-trained model to learn tasks sequentially under different task transitions. In our proposed framework, prompts are small learnable parameters, which are maintained in a memory space. The objective is to optimize prompts to instruct the model prediction and explicitly manage task-invariant and task-specific knowledge while maintaining model plasticity. We conduct comprehensive experiments under popular image classification benchmarks with different challenging continual learning settings, where L2P consistently outperforms prior state-of-the-art methods. Surprisingly, L2P achieves competitive results against rehearsal-based methods even without a rehearsal buffer and is directly applicable to challenging task-agnostic continual learning. Source code is available at https://github.com/google-research/l2p.

</details>

### Learning Bayesian Sparse Networks with Full Experience Replay for Continual Learning. **⭐⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2202.10203](https://arxiv.org/abs/2202.10203) · 📚 被引 35
- **作者**: Qingsen Yan, Dong Gong, Yuhang Liu, Anton van den Hengel, Javen Qinfeng Shi
- **🏷️ 机构**: The Australian Institute for Machine Learning, The University of Adelaide,Australia
- **会议**: CVPR 2022
- **摘要（中）**: ①针对持续学习中的灾难性遗忘问题，现有方法仍受任务间干扰影响。②提出了稀疏神经网络持续学习（SNCL），使用变分贝叶斯稀疏先验激活神经元，并采用全经验回放（FER）提供监督，同时开发了损失感知的储层采样策略。③相比已有方法，通过稀疏激活减少参数干扰，保留模型容量给未来任务，且与网络结构和任务边界无关。④实验表明SNCL在多个基准上有效缓解遗忘，性能优于现有方法。
- **摘要（英）**: This paper addresses catastrophic forgetting in continual learning, proposing SNCL, a sparse neural network with variational Bayesian sparsity priors and full experience replay. It minimizes parameter interference and achieves superior performance on benchmarks.
- **核心贡献**: 提出了SNCL，通过稀疏激活和全经验回放减少任务间干扰。
- **创新点**: 变分贝叶斯稀疏先验结合损失感知采样，实现动态稀疏网络。
- **结果**: 在多个持续学习基准上有效缓解遗忘，性能优于现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual Learning (CL) methods aim to enable machine learning models to learn new tasks without catastrophic forgetting of those that have been previously mastered. Existing CL approaches often keep a buffer of previously-seen samples, perform knowledge distillation, or use regularization techniques towards this goal. Despite their performance, they still suffer from interference across tasks which leads to catastrophic forgetting. To ameliorate this problem, we propose to only activate and select sparse neurons for learning current and past tasks at any stage. More parameters space and model capacity can thus be reserved for the future tasks. This minimizes the interference between parameters for different tasks. To do so, we propose a Sparse neural Network for Continual Learning (SNCL), which employs variational Bayesian sparsity priors on the activations of the neurons in all layers. Full Experience Replay (FER) provides effective supervision in learning the sparse activations of the neurons in different layers. A loss-aware reservoir-sampling strategy is developed to maintain the memory buffer. The proposed method is agnostic as to the network structures and the task boundaries. Experiments on different datasets show that our approach achieves state-of-the-art performance for mitigating forgetting.

</details>

### Online Continual Learning on a Contaminated Data Stream with Blurry Task Boundaries. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2203.15355](https://arxiv.org/abs/2203.15355) · 📚 被引 23
- **作者**: Jihwan Bang, Hyunseo Koh, Seulki Park, Hwanjun Song, Jung-Woo Ha, Jonghyun Choi
- **🏷️ 机构**: NAVER CLOVA, NAVER AI Lab
- **会议**: CVPR 2022
- **摘要（中）**: 针对在线持续学习中数据流含噪声标签和模糊任务边界的问题，本文强调情景记忆中样本多样性和纯净性的重要性，提出统一方法结合标签噪声感知的多样采样和半监督学习进行鲁棒学习。在CIFAR10/100、mini-WebVision和Food-101N等数据集上，该方法显著优于现有持续学习方法。
- **摘要（英）**: This paper addresses online continual learning with noisy labels and blurry task boundaries, emphasizing the need for both diversity and purity in episodic memory. A unified approach combining label-noise-aware diverse sampling and semi-supervised learning is proposed, significantly outperforming prior methods on CIFAR10/100, mini-WebVision, and Food-101N.
- **核心贡献**: 提出了在噪声数据流中平衡记忆多样性和纯净性的持续学习策略。
- **创新点**: 结合标签噪声感知采样和半监督学习，统一处理多样性和纯净性。
- **结果**: 在多个真实和合成噪声数据集上显著优于现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Learning under a continuously changing data distribution with incorrect labels is a desirable real-world problem yet challenging. A large body of continual learning (CL) methods, however, assumes data streams with clean labels, and online learning scenarios under noisy data streams are yet underexplored. We consider a more practical CL task setup of an online learning from blurry data stream with corrupted labels, where existing CL methods struggle. To address the task, we first argue the importance of both diversity and purity of examples in the episodic memory of continual learning models. To balance diversity and purity in the episodic memory, we propose a novel strategy to manage and use the memory by a unified approach of label noise aware diverse sampling and robust learning with semi-supervised learning. Our empirical validations on four real-world or synthetic noise datasets (CIFAR10 and 100, mini-WebVision, and Food-101N) exhibit that our method significantly outperforms prior arts in this realistic and challenging continual learning scenario. Code and data splits are available in https://github.com/clovaai/puridiver.

</details>

### Probing Representation Forgetting in Supervised and Unsupervised Continual Learning. **⭐⭐⭐** (相关度: 50%)
- **链接**: [arXiv:2203.13381](https://arxiv.org/abs/2203.13381) · 📚 被引 46
- **作者**: MohammadReza Davari, Nader Asadi, Sudhir P. Mudur, Rahaf Aljundi, Eugene Belilovsky
- **🏷️ 机构**: Concordia University, Toyota Motor Europe
- **会议**: CVPR 2022
- **摘要（中）**: ①针对持续学习中灾难性遗忘的度量问题，传统方法仅关注任务性能下降，忽略了表示变化。②提出表示遗忘概念，通过比较新任务前后最优线性分类器的性能差异来度量。③重新审视标准持续学习基准，发现无显式遗忘控制的模型表示遗忘较小，尤其在长任务序列中。④该视角为持续学习提供新见解，可能改变对遗忘机制的理解。
- **摘要（英）**: This paper introduces representation forgetting, measured by the performance difference of an optimal linear classifier before and after new tasks. It revisits continual learning benchmarks and finds that models without explicit forgetting control often exhibit small representation forgetting, especially in longer sequences. This provides new insights into catastrophic forgetting.
- **核心贡献**: 提出表示遗忘度量并重新评估持续学习基准。
- **创新点**: 区分表示变化与知识丢失，提供更细粒度的遗忘分析。
- **结果**: 发现无显式控制模型在长序列中表示遗忘较小。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual Learning research typically focuses on tackling the phenomenon of catastrophic forgetting in neural networks. Catastrophic forgetting is associated with an abrupt loss of knowledge previously learned by a model when the task, or more broadly the data distribution, being trained on changes. In supervised learning problems this forgetting, resulting from a change in the model's representation, is typically measured or observed by evaluating the decrease in old task performance. However, a model's representation can change without losing knowledge about prior tasks. In this work we consider the concept of representation forgetting, observed by using the difference in performance of an optimal linear classifier before and after a new task is introduced. Using this tool we revisit a number of standard continual learning benchmarks and observe that, through this lens, model representations trained without any explicit control for forgetting often experience small representation forgetting and can sometimes be comparable to methods which explicitly control for forgetting, especially in longer task sequences. We also show that representation forgetting can lead to new insights on the effect of model capacity and loss function used in continual learning. Based on our results, we show that a simple yet competitive approach is to learn representations continually with standard supervised contrastive learning while constructing prototypes of class samples when queried on old samples.

</details>

### DyTox: Transformers for Continual Learning with DYnamic TOken eXpansion. **⭐⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2111.11326](https://arxiv.org/abs/2111.11326) · 📚 被引 318
- **作者**: Arthur Douillard, Alexandre Ramé, Guillaume Couairon, Matthieu Cord
- **🏷️ 机构**: Sorbonne Universite
- **会议**: CVPR 2022
- **摘要（中）**: ①针对持续学习中动态架构方法需要任务标识符、参数扩展难以平衡且任务间信息共享不足的问题。②提出基于Transformer的编码器-解码器框架，通过动态扩展特殊token来为每个任务定制解码器前向传播，编码器和解码器在所有任务间共享。③相比现有方法，无需任务标识符，无需超参数调优控制扩展，内存和时间开销极小。④在CIFAR100上取得优秀结果，在大型ImageNet数据集上达到最先进性能。
- **摘要（英）**: This paper addresses the limitations of dynamic architectures in continual learning, which require task identifiers and complex tuning. It proposes a Transformer encoder-decoder framework with dynamic token expansion to specialize decoder forward passes per task while sharing parameters. The method achieves excellent results on CIFAR100 and state-of-the-art performance on large-scale ImageNet, with negligible overhead.
- **核心贡献**: 提出了一种基于动态token扩展的Transformer架构，实现了无需任务标识符的高效持续学习。
- **创新点**: 通过动态扩展特殊token而非参数，实现了任务特化与参数共享的平衡。
- **结果**: 在CIFAR100和ImageNet上达到最先进性能，且内存和时间开销极小。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep network architectures struggle to continually learn new tasks without forgetting the previous tasks. A recent trend indicates that dynamic architectures based on an expansion of the parameters can reduce catastrophic forgetting efficiently in continual learning. However, existing approaches often require a task identifier at test-time, need complex tuning to balance the growing number of parameters, and barely share any information across tasks. As a result, they struggle to scale to a large number of tasks without significant overhead. In this paper, we propose a transformer architecture based on a dedicated encoder/decoder framework. Critically, the encoder and decoder are shared among all tasks. Through a dynamic expansion of special tokens, we specialize each forward of our decoder network on a task distribution. Our strategy scales to a large number of tasks while having negligible memory and time overheads due to strict control of the parameters expansion. Moreover, this efficient strategy doesn't need any hyperparameter tuning to control the network's expansion. Our model reaches excellent results on CIFAR100 and state-of-the-art performances on the large-scale ImageNet100 and ImageNet1000 while having less parameters than concurrent dynamic frameworks.

</details>

### Not Just Selection, but Exploration: Online Class-Incremental Continual Learning via Dual View Consistency. **⭐⭐⭐** (相关度: 50%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00729) · 📚 被引 73
- **作者**: Yanan Gu, Xu Yang, Kun Wei, Cheng Deng
- **🏷️ 机构**: School of Electronic Engineering, Xidian University,Xi&#x0027;an,China,710071
- **会议**: CVPR 2022
- **摘要（中）**: ①针对在线类增量持续学习中仅选择样本不足以有效利用数据的问题。②提出基于双视图一致性的方法，在样本选择之外强调探索，通过一致性约束增强模型对未选择样本的利用。③相比仅依赖回放选择的现有方法，增加了探索机制，提升了数据利用效率。④在多个基准上验证了方法的有效性，但摘要未提供具体数据。
- **摘要（英）**: This paper tackles the limitation of sample selection in online class-incremental continual learning by introducing a dual view consistency approach. It emphasizes exploration beyond selection to better utilize data, improving over replay-based methods. The method shows effectiveness on benchmarks, though specific results are not detailed in the abstract.
- **核心贡献**: 提出了双视图一致性机制，结合探索与选择提升在线类增量学习性能。
- **创新点**: 将探索机制引入样本选择，利用双视图一致性增强数据利用。
- **结果**: 在基准测试上验证了有效性，但具体数据未在摘要中给出。

### On Generalizing Beyond Domains in Cross-Domain Continual Learning. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2203.03970](https://arxiv.org/abs/2203.03970) · 📚 被引 30
- **作者**: Christian Simon, Masoud Faraki, Yi-Hsuan Tsai, Xiang Yu, Samuel Schulter, Yumin Suh et al.
- **🏷️ 机构**: The Australian National University, Phiar Technologies, Monash University
- **会议**: CVPR 2022
- **摘要（中）**: ①针对跨域持续学习中模型在未见领域上泛化能力不足的问题。②提出使用马氏距离计算类相似度作为分类器参数，并采用指数移动平均进行知识蒸馏，以学习语义特征。③相比现有持续学习算法，该方法在域偏移下能更好地处理遗忘问题，提升泛化能力。④在多个分布下学习新任务时准确率显著提升。
- **摘要（英）**: This paper addresses the generalization issue in cross-domain continual learning by equipping the classifier with Mahalanobis similarity metrics and using exponential moving average for distillation. It learns semantically meaningful features, improving over existing methods under domain shifts. The approach boosts accuracy when learning new tasks across multiple distributions.
- **核心贡献**: 提出了基于马氏距离的类相似度分类器和EMA蒸馏方法，提升跨域持续学习泛化能力。
- **创新点**: 将马氏距离引入分类器参数，并结合EMA蒸馏增强知识保留。
- **结果**: 在域偏移下准确率显著提升，优于现有持续学习算法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Humans have the ability to accumulate knowledge of new tasks in varying conditions, but deep neural networks often suffer from catastrophic forgetting of previously learned knowledge after learning a new task. Many recent methods focus on preventing catastrophic forgetting under the assumption of train and test data following similar distributions. In this work, we consider a more realistic scenario of continual learning under domain shifts where the model must generalize its inference to an unseen domain. To this end, we encourage learning semantically meaningful features by equipping the classifier with class similarity metrics as learning parameters which are obtained through Mahalanobis similarity computations. Learning of the backbone representation along with these extra parameters is done seamlessly in an end-to-end manner. In addition, we propose an approach based on the exponential moving average of the parameters for better knowledge distillation. We demonstrate that, to a great extent, existing continual learning algorithms fail to handle the forgetting issue under multiple distributions, while our proposed approach learns new tasks under domain shift with accuracy boosts up to 10% on challenging datasets such as DomainNet and OfficeHome.

</details>

### GCR: Gradient Coreset based Replay Buffer Selection for Continual Learning. **⭐⭐⭐⭐** (相关度: 65%)
- **链接**: [arXiv:2111.11210](https://arxiv.org/abs/2111.11210) · 📚 被引 105
- **作者**: Rishabh Tiwari, KrishnaTeja Killamsetty, Rishabh K. Iyer, Pradeep Shenoy
- **🏷️ 机构**: Indian Institute of Technology (ISM),Department of Physics,Dhanbad, University of Texas at Dallas,Department of Computer Science, Google Research,India
- **会议**: CVPR 2022
- **摘要（中）**: ①针对回放式持续学习中缓冲区样本选择策略不佳导致灾难性遗忘的问题。②提出梯度核心集回放（GCR）策略，通过优化准则选择和更新缓冲区，使核心集近似所有已见数据的梯度。③相比现有方法，GCR在离线持续学习设置中取得2%-4%的绝对提升，在线/流式设置中提升达5%。④结合监督对比学习进一步增强了效果。
- **摘要（英）**: This paper proposes Gradient Coreset Replay (GCR) for buffer selection in replay-based continual learning, optimizing a criterion to approximate the gradient of all seen data. It achieves 2%-4% absolute gains in offline settings and up to 5% in online settings over state-of-the-art. The method also benefits from supervised contrastive learning.
- **核心贡献**: 提出了基于梯度近似的核心集选择策略，显著提升回放式持续学习性能。
- **创新点**: 以梯度匹配为优化目标选择缓冲区样本，适用于离线与在线设置。
- **结果**: 在离线设置中提升2%-4%，在线设置中提升达5%。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning (CL) aims to develop techniques by which a single model adapts to an increasing number of tasks encountered sequentially, thereby potentially leveraging learnings across tasks in a resource-efficient manner. A major challenge for CL systems is catastrophic forgetting, where earlier tasks are forgotten while learning a new task. To address this, replay-based CL approaches maintain and repeatedly retrain on a small buffer of data selected across encountered tasks. We propose Gradient Coreset Replay (GCR), a novel strategy for replay buffer selection and update using a carefully designed optimization criterion. Specifically, we select and maintain a "coreset" that closely approximates the gradient of all the data seen so far with respect to current model parameters, and discuss key strategies needed for its effective application to the continual learning setting. We show significant gains (2%-4% absolute) over the state-of-the-art in the well-studied offline continual learning setting. Our findings also effectively transfer to online / streaming CL settings, showing upto 5% gains over existing approaches. Finally, we demonstrate the value of supervised contrastive loss for continual learning, which yields a cumulative gain of up to 5% accuracy when combined with our subset selection strategy.

</details>

### Continual Learning for Visual Search with Backward Consistent Feature Embedding. **⭐⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2205.13384](https://arxiv.org/abs/2205.13384) · 📚 被引 27
- **作者**: Timmy S. T. Wan, Jun-Cheng Chen, Tzer-Yi Wu, Chu-Song Chen
- **🏷️ 机构**: National Taiwan University, Academia Sinica, Ucfunnel Co. Ltd.
- **会议**: CVPR 2022
- **摘要（中）**: 针对视觉搜索中图库集增量增长且模型更新需重新提取特征的高计算成本问题，本文提出一种持续学习方法，通过保持后向一致的嵌入空间来处理增量图库。方法设计了会话间数据一致性、邻居会话模型一致性和会话内判别性损失，以训练持续学习器，并支持模糊边界场景下新类别的出现。实验在多个基准上验证了该方法在保持嵌入一致性的同时，有效处理了增量学习，降低了计算开销。
- **摘要（英）**: This paper addresses continual learning for visual search with incrementally growing galleries, proposing a method that enforces backward-consistent feature embeddings via inter-session coherence, neighbor-session model coherence, and intra-session discrimination losses. It handles both disjoint and blurry boundary scenarios, reducing re-computation costs. Experiments demonstrate effectiveness across benchmarks.
- **核心贡献**: 首次提出后向一致的持续学习框架，支持增量图库和模糊边界新类。
- **创新点**: 通过多损失约束实现嵌入空间的后向一致性。
- **结果**: 在多个基准上有效处理增量学习，降低计算成本。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In visual search, the gallery set could be incrementally growing and added to the database in practice. However, existing methods rely on the model trained on the entire dataset, ignoring the continual updating of the model. Besides, as the model updates, the new model must re-extract features for the entire gallery set to maintain compatible feature space, imposing a high computational cost for a large gallery set. To address the issues of long-term visual search, we introduce a continual learning (CL) approach that can handle the incrementally growing gallery set with backward embedding consistency. We enforce the losses of inter-session data coherence, neighbor-session model coherence, and intra-session discrimination to conduct a continual learner. In addition to the disjoint setup, our CL solution also tackles the situation of increasingly adding new classes for the blurry boundary without assuming all categories known in the beginning and during model update. To our knowledge, this is the first CL method both tackling the issue of backward-consistent feature embedding and allowing novel classes to occur in the new sessions. Extensive experiments on various benchmarks show the efficacy of our approach under a wide range of setups.

</details>

### MetaFSCIL: A Meta-Learning Approach for Few-Shot Class Incremental Learning. **⭐⭐⭐** (相关度: 45%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01377) · 📚 被引 155
- **作者**: Zhixiang Chi, Li Gu, Huan Liu, Yang Wang, Yuanhao Yu, Jin Tang
- **🏷️ 机构**: Noah&#x0027;s Ark Lab, Huawei Technologies
- **会议**: CVPR 2022
- **摘要（中）**: ①针对少样本类增量学习中新类样本稀少导致模型难以适应的问题。②提出元学习框架MetaFSCIL，通过元学习策略使模型快速适应新类。③相比传统类增量方法，该方法专门针对少样本场景，利用元学习提升泛化能力。④摘要未提供具体数据，但方法在少样本设置下具有潜力。
- **摘要（英）**: This paper addresses few-shot class incremental learning by proposing a meta-learning framework, MetaFSCIL, to enable rapid adaptation to new classes with limited samples. It leverages meta-learning to improve generalization over traditional methods. Specific results are not provided in the abstract.
- **核心贡献**: 提出了元学习框架用于少样本类增量学习，提升新类适应能力。
- **创新点**: 将元学习应用于类增量学习，解决少样本下的快速适应问题。
- **结果**: 具体效果未在摘要中给出。

### Learning to Imagine: Diversify Memory for Incremental Learning using Unlabeled Data. **⭐⭐⭐** (相关度: 45%)
- **链接**: [arXiv:2204.08932](https://arxiv.org/abs/2204.08932) · 📚 被引 37
- **作者**: Yu-Ming Tang, Yi-Xing Peng, Wei-Shi Zheng
- **🏷️ 机构**: Sun Yat-sen University,School of Computer Science and Engineering,China
- **会议**: CVPR 2022
- **摘要（中）**: ①针对增量学习中样本数量有限导致灾难性遗忘的问题。②提出利用未标注数据生成多样化的样本，通过可学习特征生成器结合语义和语义无关信息。③引入语义对比学习和语义解耦对比学习，保证生成样本的语义一致性和多样性。④方法不增加推理开销，有效缓解遗忘。
- **摘要（英）**: This paper addresses catastrophic forgetting in incremental learning with limited exemplars. It proposes a learnable feature generator that diversifies exemplars using unlabeled data, with semantic contrastive learning for consistency and decoupling for diversity. The method reduces forgetting without extra inference cost.
- **核心贡献**: 利用未标注数据生成多样化样本以缓解增量学习遗忘。
- **创新点**: 结合语义和语义无关信息进行特征生成。
- **结果**: 有效防止遗忘，但未提供具体数值。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep neural network (DNN) suffers from catastrophic forgetting when learning incrementally, which greatly limits its applications. Although maintaining a handful of samples (called `exemplars`) of each task could alleviate forgetting to some extent, existing methods are still limited by the small number of exemplars since these exemplars are too few to carry enough task-specific knowledge, and therefore the forgetting remains. To overcome this problem, we propose to `imagine` diverse counterparts of given exemplars referring to the abundant semantic-irrelevant information from unlabeled data. Specifically, we develop a learnable feature generator to diversify exemplars by adaptively generating diverse counterparts of exemplars based on semantic information from exemplars and semantically-irrelevant information from unlabeled data. We introduce semantic contrastive learning to enforce the generated samples to be semantic consistent with exemplars and perform semanticdecoupling contrastive learning to encourage diversity of generated samples. The diverse generated samples could effectively prevent DNN from forgetting when learning new tasks. Our method does not bring any extra inference cost and outperforms state-of-the-art methods on two benchmarks CIFAR-100 and ImageNet-Subset by a clear margin.

</details>

### Forward Compatible Few-Shot Class-Incremental Learning. **⭐⭐⭐⭐** (相关度: 65%)
- **链接**: [arXiv:2203.06953](https://arxiv.org/abs/2203.06953)
- **作者**: Da-Wei Zhou, Fu-Yun Wang, Han-Jia Ye, Liang Ma, Shiliang Pu, De-Chuan Zhan
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2022
- **摘要（中）**: 针对少样本类增量学习（FSCIL）中现有方法仅回顾式地适应旧模型的问题，本文提出前向兼容训练（FACT），通过预留嵌入空间给未来新类来前瞻性地准备模型更新。方法分配虚拟原型以压缩已知类嵌入并保留新类空间，同时预测可能的新类并准备更新过程，虚拟原型在推理时作为代理构建更强分类器。实验表明，FACT在多个FSCIL基准上显著优于现有方法，有效缓解了灾难性遗忘。
- **摘要（英）**: This paper proposes Forward Compatible Training (FACT) for few-shot class-incremental learning, which reserves embedding space for future classes via virtual prototypes and forecasts possible updates. This prospective approach contrasts with retrospective methods, improving adaptability. Experiments show significant gains over state-of-the-art on FSCIL benchmarks.
- **核心贡献**: 提出前向兼容训练框架，通过虚拟原型预留空间实现高效FSCIL。
- **创新点**: 从回顾式转向前瞻式学习，利用虚拟原型准备未来更新。
- **结果**: 在多个FSCIL基准上显著优于现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Novel classes frequently arise in our dynamically changing world, e.g., new users in the authentication system, and a machine learning model should recognize new classes without forgetting old ones. This scenario becomes more challenging when new class instances are insufficient, which is called few-shot class-incremental learning (FSCIL). Current methods handle incremental learning retrospectively by making the updated model similar to the old one. By contrast, we suggest learning prospectively to prepare for future updates, and propose ForwArd Compatible Training (FACT) for FSCIL. Forward compatibility requires future new classes to be easily incorporated into the current model based on the current stage data, and we seek to realize it by reserving embedding space for future new classes. In detail, we assign virtual prototypes to squeeze the embedding of known classes and reserve for new ones. Besides, we forecast possible new classes and prepare for the updating process. The virtual prototypes allow the model to accept possible updates in the future, which act as proxies scattered among embedding space to build a stronger classifier during inference. FACT efficiently incorporates new classes with forward compatibility and meanwhile resists forgetting of old ones. Extensive experiments validate FACT's state-of-the-art performance. Code is available at: https://github.com/zhoudw-zdw/CVPR22-Fact

</details>

### Self-Sustaining Representation Expansion for Non-Exemplar Class-Incremental Learning. **⭐⭐⭐⭐** (相关度: 55%)
- **链接**: [arXiv:2203.06359](https://arxiv.org/abs/2203.06359) · 📚 被引 153
- **作者**: Kai Zhu, Wei Zhai, Yang Cao, Jiebo Luo, Zhengjun Zha
- **🏷️ 机构**: University of Science and Technology of China, University of Rochester
- **会议**: CVPR 2022
- **摘要（中）**: ①针对无样本类增量学习中无法保存旧类样本导致特征保留困难的问题。②提出自维持表示扩展方案，包括结构重组策略融合主分支扩展和侧分支更新，以及主分支蒸馏传递不变知识，并设计原型选择机制增强新旧类判别。③相比现有方法，该方案无需旧样本即可有效保留旧特征。④在三个基准上分别超越最先进方法3%、3%和6%。
- **摘要（英）**: This paper proposes a self-sustaining representation expansion scheme for non-exemplar class-incremental learning, using structure reorganization and distillation to retain old features without storing samples. A prototype selection mechanism enhances discrimination between old and new classes. It outperforms state-of-the-art by 3%, 3%, and 6% on three benchmarks.
- **核心贡献**: 提出了自维持表示扩展方案，实现无样本类增量学习中的特征保留。
- **创新点**: 通过结构重组和原型选择机制，在无旧样本条件下维持旧特征。
- **结果**: 在三个基准上分别提升3%、3%和6%。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Non-exemplar class-incremental learning is to recognize both the old and new classes when old class samples cannot be saved. It is a challenging task since representation optimization and feature retention can only be achieved under supervision from new classes. To address this problem, we propose a novel self-sustaining representation expansion scheme. Our scheme consists of a structure reorganization strategy that fuses main-branch expansion and side-branch updating to maintain the old features, and a main-branch distillation scheme to transfer the invariant knowledge. Furthermore, a prototype selection mechanism is proposed to enhance the discrimination between the old and new classes by selectively incorporating new samples into the distillation process. Extensive experiments on three benchmarks demonstrate significant incremental performance, outperforming the state-of-the-art methods by a margin of 3%, 3% and 6%, respectively.

</details>

### Doodle It Yourself: Class Incremental Learning by Drawing a Few Sketches. **⭐⭐⭐** (相关度: 50%)
- **链接**: [arXiv:2203.14843](https://arxiv.org/abs/2203.14843) · 📚 被引 26
- **作者**: Ayan Kumar Bhunia, Viswanatha Reddy Gajjala, Subhadeep Koley, Rohit Kundu, Aneeshan Sain, Tao Xiang et al.
- **🏷️ 机构**: University of Surrey,SketchX, CVSSP,United Kingdom
- **会议**: CVPR 2022
- **摘要（中）**: 针对少样本类增量学习（FSCIL）中照片数据可能受隐私限制且模型仅从单一模态学习的问题，本文提出DIY框架，利用草图作为新类支持模态。方法结合梯度共识实现域不变学习、知识蒸馏保留旧类信息、图注意力网络传递新旧类消息，使用户可自由绘制草图来学习识别照片。实验表明，草图作为类支持比文本更有效，在多个基准上提升了FSCIL性能。
- **摘要（英）**: This paper proposes a DIY framework for FSCIL that uses sketches as a new modality for class support, addressing privacy constraints and multi-modal learning. It integrates gradient consensus, knowledge distillation, and graph attention networks. Experiments show sketches outperform text as support, improving FSCIL performance.
- **核心贡献**: 首次引入草图模态支持FSCIL，实现从草图到照片的跨域学习。
- **创新点**: 利用草图作为类支持，结合多种技术实现域不变学习。
- **结果**: 草图支持优于文本，在基准上提升性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The human visual system is remarkable in learning new visual concepts from just a few examples. This is precisely the goal behind few-shot class incremental learning (FSCIL), where the emphasis is additionally placed on ensuring the model does not suffer from "forgetting". In this paper, we push the boundary further for FSCIL by addressing two key questions that bottleneck its ubiquitous application (i) can the model learn from diverse modalities other than just photo (as humans do), and (ii) what if photos are not readily accessible (due to ethical and privacy constraints). Our key innovation lies in advocating the use of sketches as a new modality for class support. The product is a "Doodle It Yourself" (DIY) FSCIL framework where the users can freely sketch a few examples of a novel class for the model to learn to recognize photos of that class. For that, we present a framework that infuses (i) gradient consensus for domain invariant learning, (ii) knowledge distillation for preserving old class information, and (iii) graph attention networks for message passing between old and novel classes. We experimentally show that sketches are better class support than text in the context of FSCIL, echoing findings elsewhere in the sketching literature.

</details>

### Incremental Learning in Semantic Segmentation from Image Labels. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2112.01882](https://arxiv.org/abs/2112.01882) · 📚 被引 58
- **作者**: Fabio Cermelli, Dario Fontanel, Antonio Tavera, Marco Ciccone, Barbara Caputo
- **🏷️ 机构**: Politecnico di Torino
- **会议**: CVPR 2022
- **摘要（中）**: ①针对语义分割模型在增量学习新类别时依赖昂贵像素级标注、且现有方法需离线生成伪标签的问题。②提出弱监督增量学习框架WILSON，利用图像级标签训练的辅助分类器在线生成软伪标签，并受分割模型正则化，实现无离线伪标签的增量更新。③相比现有离线弱监督方法，通过软标签处理噪声，无需存储旧数据。④在Pascal VOC和COCO上超越离线弱监督方法，性能接近全监督增量学习。
- **摘要（英）**: This paper addresses incremental semantic segmentation with image-level labels, proposing WILSON, which uses an auxiliary classifier for online soft pseudo-label generation, outperforming offline weakly-supervised methods and matching fully-supervised incremental learning on Pascal VOC and COCO.
- **核心贡献**: 提出首个在线弱监督增量语义分割框架，减少对像素级标注的依赖。
- **创新点**: 利用辅助分类器在线生成软标签，避免离线伪标签生成。
- **结果**: 在Pascal VOC和COCO上性能优于离线弱监督方法，接近全监督结果。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Although existing semantic segmentation approaches achieve impressive results, they still struggle to update their models incrementally as new categories are uncovered. Furthermore, pixel-by-pixel annotations are expensive and time-consuming. This paper proposes a novel framework for Weakly Incremental Learning for Semantic Segmentation, that aims at learning to segment new classes from cheap and largely available image-level labels. As opposed to existing approaches, that need to generate pseudo-labels offline, we use an auxiliary classifier, trained with image-level labels and regularized by the segmentation model, to obtain pseudo-supervision online and update the model incrementally. We cope with the inherent noise in the process by using soft-labels generated by the auxiliary classifier. We demonstrate the effectiveness of our approach on the Pascal VOC and COCO datasets, outperforming offline weakly-supervised methods and obtaining results comparable with incremental learning methods with full supervision. Code can be found at https://github.com/fcdl94/WILSON.

</details>

### Few-Shot Incremental Learning for Label-to-Image Translation. **⭐⭐** (相关度: 50%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00368) · 📚 被引 9
- **作者**: Pei Chen, Yangkang Zhang, Zejian Li, Lingyun Sun
- **🏷️ 机构**: Alibaba-Zhejiang University Joint Institute of Frontier Technologies, Zhejiang University
- **会议**: CVPR 2022
- **摘要（中）**: ①针对标签到图像翻译任务中的少样本增量学习问题，摘要缺失，无法获取具体方法细节。②由于摘要为空，无法评估其方法或改进。③缺乏可验证的实验数据。④效果未知。
- **摘要（英）**: The abstract is missing, so the problem, method, and results cannot be assessed; likely focuses on few-shot incremental learning for label-to-image translation.
- **核心贡献**: 未知。
- **创新点**: 未知。
- **结果**: 未知。

### Federated Class-Incremental Learning. **⭐⭐** (相关度: 50%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00992)
- **作者**: Jiahua Dong, Lixu Wang, Zhen Fang, Gan Sun, Shichao Xu, Xiao Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2022
- **摘要（中）**: ①针对联邦学习中的类别增量学习问题，摘要缺失，无法获取具体方法。②由于摘要为空，无法评估方法或改进。③缺乏实验数据。④效果未知。
- **摘要（英）**: The abstract is missing, so the problem, method, and results cannot be assessed; likely addresses class-incremental learning in federated settings.
- **核心贡献**: 未知。
- **创新点**: 未知。
- **结果**: 未知。

### Constrained Few-shot Class-incremental Learning. **⭐⭐⭐** (相关度: 55%)
- **链接**: [arXiv:2203.16588](https://arxiv.org/abs/2203.16588)
- **作者**: Michael Hersche, Geethan Karunaratne, Giovanni Cherubini, Luca Benini, Abu Sebastian, Abbas Rahimi
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2022
- **摘要（中）**: 针对持续学习新类时需满足内存和计算约束的问题，本文提出C-FSCIL框架，由冻结的元学习特征提取器、可训练固定大小全连接层和可重写的动态增长记忆组成。方法利用超维度嵌入，在固定维度空间中表达更多类，并通过准正交对齐提高类向量质量，提供三种更新模式以权衡精度和计算成本。实验表明，C-FSCIL在满足约束的同时，在多个基准上取得了有竞争力的性能。
- **摘要（英）**: This paper proposes C-FSCIL for constrained few-shot class-incremental learning, using a frozen meta-learned extractor, a fixed-size FC layer, and a dynamic memory. Hyperdimensional embeddings enable many classes with minimal interference, and quasi-orthogonal alignment improves quality. Experiments show competitive performance under strict constraints.
- **核心贡献**: 提出满足内存和计算约束的C-FSCIL框架，利用超维度嵌入实现高效增量学习。
- **创新点**: 结合超维度计算和准正交对齐，支持动态类增长。
- **结果**: 在约束下取得有竞争力的性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continually learning new classes from fresh data without forgetting previous knowledge of old classes is a very challenging research problem. Moreover, it is imperative that such learning must respect certain memory and computational constraints such as (i) training samples are limited to only a few per class, (ii) the computational cost of learning a novel class remains constant, and (iii) the memory footprint of the model grows at most linearly with the number of classes observed. To meet the above constraints, we propose C-FSCIL, which is architecturally composed of a frozen meta-learned feature extractor, a trainable fixed-size fully connected layer, and a rewritable dynamically growing memory that stores as many vectors as the number of encountered classes. C-FSCIL provides three update modes that offer a trade-off between accuracy and compute-memory cost of learning novel classes. C-FSCIL exploits hyperdimensional embedding that allows to continually express many more classes than the fixed dimensions in the vector space, with minimal interference. The quality of class vector representations is further improved by aligning them quasi-orthogonally to each other by means of novel loss functions. Experiments on the CIFAR100, miniImageNet, and Omniglot datasets show that C-FSCIL outperforms the baselines with remarkable accuracy and compression. It also scales up to the largest problem size ever tried in this few-shot setting by learning 423 novel classes on top of 1200 base classes with less than 1.6% accuracy drop. Our code is available at https://github.com/IBM/constrained-FSCIL.

</details>

### Energy-based Latent Aligner for Incremental Learning. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2203.14952](https://arxiv.org/abs/2203.14952) · 📚 被引 36
- **作者**: K. J. Joseph, Salman Khan, Fahad Shahbaz Khan, Rao Muhammad Anwer, Vineeth N. Balasubramanian
- **🏷️ 机构**: Indian Institute of Technology,Hyderabad,India, Mohamed bin Zayed University of AI,UAE
- **会议**: CVPR 2022
- **摘要（中）**: ①针对增量学习中参数更新不匹配导致旧知识遗忘的问题。②提出基于能量的潜在对齐器ELI，学习能量流形使旧任务潜在表示低能量、新任务高能量，以抵消表示偏移，可作为即插即用模块。③相比现有方法，提供隐式正则化，无需额外存储。④在CIFAR-100、ImageNet子集、ImageNet 1k和Pascal VOC上，加入ELI后一致提升多种类增量学习方法，并在SOTA增量检测器上提升超5%。
- **摘要（英）**: This paper proposes ELI, an energy-based latent aligner that learns an energy manifold to counter representational shift in incremental learning, serving as a plug-and-play module; it consistently improves multiple methods on CIFAR-100, ImageNet, and Pascal VOC, with over 5% gain on SOTA incremental detectors.
- **核心贡献**: 提出能量基潜在对齐器，作为通用模块缓解增量学习中的表示偏移。
- **创新点**: 利用能量流形隐式正则化，无需旧样本。
- **结果**: 在多个数据集和多种方法上一致提升，检测任务提升超5%。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep learning models tend to forget their earlier knowledge while incrementally learning new tasks. This behavior emerges because the parameter updates optimized for the new tasks may not align well with the updates suitable for older tasks. The resulting latent representation mismatch causes forgetting. In this work, we propose ELI: Energy-based Latent Aligner for Incremental Learning, which first learns an energy manifold for the latent representations such that previous task latents will have low energy and the current task latents have high energy values. This learned manifold is used to counter the representational shift that happens during incremental learning. The implicit regularization that is offered by our proposed methodology can be used as a plug-and-play module in existing incremental learning methodologies. We validate this through extensive evaluation on CIFAR-100, ImageNet subset, ImageNet 1k and Pascal VOC datasets. We observe consistent improvement when ELI is added to three prominent methodologies in class-incremental learning, across multiple incremental settings. Further, when added to the state-of-the-art incremental object detector, ELI provides over 5% improvement in detection accuracy, corroborating its effectiveness and complementary advantage to existing art.

</details>

### Class-Incremental Learning by Knowledge Distillation with Adaptive Feature Consolidation. **⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2204.00895](https://arxiv.org/abs/2204.00895) · 📚 被引 197
- **作者**: Minsoo Kang, Jaeyoo Park, Bohyung Han
- **🏷️ 机构**: ECE, ASRI, &#x0026; IPAI, Seoul National University
- **会议**: CVPR 2022
- **摘要（中）**: 针对类增量学习中的灾难性遗忘问题，提出基于知识蒸馏的自适应特征巩固方法。通过估计特征变化与损失增加的关系，最小化损失上界，并利用特征图重要性限制关键特征更新。相比现有方法，在标准数据集上显著提升准确率。
- **摘要（英）**: This paper addresses catastrophic forgetting in class-incremental learning by proposing knowledge distillation with adaptive feature consolidation. It estimates the relationship between feature changes and loss increases, minimizing the loss upper bound and restricting updates of important features. Experiments show significant accuracy improvements over existing methods on standard datasets.
- **核心贡献**: 提出一种基于特征重要性的自适应知识蒸馏策略，缓解灾难性遗忘。
- **创新点**: 通过损失上界最小化与特征重要性估计，实现鲁棒性与灵活性的平衡。
- **结果**: 在标准数据集上显著提升类增量学习准确率。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a novel class incremental learning approach based on deep neural networks, which continually learns new tasks with limited memory for storing examples in the previous tasks. Our algorithm is based on knowledge distillation and provides a principled way to maintain the representations of old models while adjusting to new tasks effectively. The proposed method estimates the relationship between the representation changes and the resulting loss increases incurred by model updates. It minimizes the upper bound of the loss increases using the representations, which exploits the estimated importance of each feature map within a backbone model. Based on the importance, the model restricts updates of important features for robustness while allowing changes in less critical features for flexibility. This optimization strategy effectively alleviates the notorious catastrophic forgetting problem despite the limited accessibility of data in the previous tasks. The experimental results show significant accuracy improvement of the proposed algorithm over the existing methods on the standard datasets. Code is available.

</details>

### Towards Better Plasticity-Stability Trade-off in Incremental Learning: A Simple Linear Connector. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2110.07905](https://arxiv.org/abs/2110.07905) · 📚 被引 52
- **作者**: Guoliang Lin, Hanlu Chu, Hanjiang Lai
- **🏷️ 机构**: Sun Yat-sen University,Guangdong,China, South China Normal University,Guangdong,China
- **会议**: CVPR 2022
- **摘要（中）**: ①针对增量学习中可塑性-稳定性困境，且无法存储旧样本的场景。②提出使用损失景观中的模式连通性，连接旧任务的零空间投影和新任务的SGD优化点，以平衡新旧知识。③相比现有方法，无需旧样本，通过线性连接实现简单有效的权衡控制。④在多个基准数据集上显著提升，10-split-CIFAR-100上达到79.79%准确率。
- **摘要（英）**: This paper addresses the plasticity-stability dilemma without storing old samples by using mode connectivity to connect null-space projection and SGD optima, achieving notable improvements and 79.79% accuracy on 10-split-CIFAR-100.
- **核心贡献**: 提出基于模式连通性的无样本增量学习方法，改善可塑性-稳定性权衡。
- **创新点**: 利用损失景观连通性连接新旧任务最优解。
- **结果**: 在多个基准上显著提升，CIFAR-100准确率达79.79%。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Plasticity-stability dilemma is a main problem for incremental learning, where plasticity is referring to the ability to learn new knowledge, and stability retains the knowledge of previous tasks. Many methods tackle this problem by storing previous samples, while in some applications, training data from previous tasks cannot be legally stored. In this work, we propose to employ mode connectivity in loss landscapes to achieve better plasticity-stability trade-off without any previous samples. We give an analysis of why and how to connect two independently optimized optima of networks, null-space projection for previous tasks and simple SGD for the current task, can attain a meaningful balance between preserving already learned knowledge and granting sufficient flexibility for learning a new task. This analysis of mode connectivity also provides us a new perspective and technology to control the trade-off between plasticity and stability. We evaluate the proposed method on several benchmark datasets. The results indicate our simple method can achieve notable improvement, and perform well on both the past and current tasks. On 10-split-CIFAR-100 task, our method achieves 79.79% accuracy, which is 6.02% higher. Our method also achieves 6.33% higher accuracy on TinyImageNet. Code is available at https://github.com/lingl1024/Connector.

</details>

### Mimicking the Oracle: An Initial Phase Decorrelation Approach for Class Incremental Learning.
- **链接**: [arXiv:2112.04731](https://arxiv.org/abs/2112.04731) · 📚 被引 61
- **作者**: Yujun Shi, Kuangqi Zhou, Jian Liang, Zihang Jiang, Jiashi Feng, Philip H. S. Torr et al.
- **🏷️ 机构**: National University of Singapore, Institute of Automation, Chinese Academy of Sciences (CAS), ByteDance Inc
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Class Incremental Learning (CIL) aims at learning a multi-class classifier in a phase-by-phase manner, in which only data of a subset of the classes are provided at each phase. Previous works mainly focus on mitigating forgetting in phases after the initial one. However, we find that improving CIL at its initial phase is also a promising direction. Specifically, we experimentally show that directly encouraging CIL Learner at the initial phase to output similar representations as the model jointly trained on all classes can greatly boost the CIL performance. Motivated by this, we study the difference between a naïvely-trained initial-phase model and the oracle model. Specifically, since one major difference between these two models is the number of training classes, we investigate how such difference affects the model representations. We find that, with fewer training classes, the data representations of each class lie in a long and narrow region; with more training classes, the representations of each class scatter more uniformly. Inspired by this observation, we propose Class-wise Decorrelation (CwD) that effectively regularizes representations of each class to scatter more uniformly, thus mimicking the model jointly trained with all classes (i.e., the oracle model). Our CwD is simple to implement and easy to plug into existing methods. Extensive experiments on various benchmark datasets show that CwD consistently and significantly improves the performance of existing state-of-the-art methods by around 1\% to 3\%. Code will be released.

</details>

### Bring Evanescent Representations to Life in Lifelong Class Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01623) · 📚 被引 36
- **作者**: Marco Toldo, Mete Ozay
- **🏷️ 机构**: Samsung Research UK
- **会议**: CVPR 2022

### Class-Incremental Learning with Strong Pre-trained Models.
- **链接**: [arXiv:2204.03634](https://arxiv.org/abs/2204.03634) · [代码](https://github.com/amazon-research/sp-cil) · 📚 被引 65
- **作者**: Tz-Ying Wu, Gurumurthy Swaminathan, Zhizhong Li, Avinash Ravichandran, Nuno Vasconcelos, Rahul Bhotika et al.
- **🏷️ 机构**: AWS AI Labs, UC San Diego
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Class-incremental learning (CIL) has been widely studied under the setting of starting from a small number of classes (base classes). Instead, we explore an understudied real-world setting of CIL that starts with a strong model pre-trained on a large number of base classes. We hypothesize that a strong base model can provide a good representation for novel classes and incremental learning can be done with small adaptations. We propose a 2-stage training scheme, i) feature augmentation -- cloning part of the backbone and fine-tuning it on the novel data, and ii) fusion -- combining the base and novel classifiers into a unified classifier. Experiments show that the proposed method significantly outperforms state-of-the-art CIL methods on the large-scale ImageNet dataset (e.g. +10% overall accuracy than the best). We also propose and analyze understudied practical CIL scenarios, such as base-novel overlap with distribution shift. Our proposed method is robust and generalizes to all analyzed CIL settings. Code is available at https://github.com/amazon-research/sp-cil.

</details>

### General Incremental Learning with Domain-aware Categorical Representations.
- **链接**: [arXiv:2204.04078](https://arxiv.org/abs/2204.04078) · 📚 被引 34
- **作者**: Jiangwei Xie, Shipeng Yan, Xuming He
- **🏷️ 机构**: School of Information Science and Technology, ShanghaiTech University
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning is an important problem for achieving human-level intelligence in real-world applications as an agent must continuously accumulate knowledge in response to streaming data/tasks. In this work, we consider a general and yet under-explored incremental learning problem in which both the class distribution and class-specific domain distribution change over time. In addition to the typical challenges in class incremental learning, this setting also faces the intra-class stability-plasticity dilemma and intra-class domain imbalance problems. To address above issues, we develop a novel domain-aware continual learning method based on the EM framework. Specifically, we introduce a flexible class representation based on the von Mises-Fisher mixture model to capture the intra-class structure, using an expansion-and-reduction strategy to dynamically increase the number of components according to the class complexity. Moreover, we design a bi-level balanced memory to cope with data imbalances within and across classes, which combines with a distillation loss to achieve better inter- and intra-class stability-plasticity trade-off. We conduct exhaustive experiments on three benchmarks: iDigits, iDomainNet and iCIFAR-20. The results show that our approach consistently outperforms previous methods by a significant margin, demonstrating its superiority.

</details>

### Subspace Regularizers for Few-Shot Class Incremental Learning.
- **链接**: [arXiv:2110.07059](https://arxiv.org/abs/2110.07059)
- **作者**: Afra Feyza Akyürek, Ekin Akyürek, Derry Wijaya, Jacob Andreas
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Few-shot class incremental learning -- the problem of updating a trained classifier to discriminate among an expanded set of classes with limited labeled data -- is a key challenge for machine learning systems deployed in non-stationary environments. Existing approaches to the problem rely on complex model architectures and training procedures that are difficult to tune and re-use. In this paper, we present an extremely simple approach that enables the use of ordinary logistic regression classifiers for few-shot incremental learning. The key to this approach is a new family of subspace regularization schemes that encourage weight vectors for new classes to lie close to the subspace spanned by the weights of existing classes. When combined with pretrained convolutional feature extractors, logistic regression models trained with subspace regularization outperform specialized, state-of-the-art approaches to few-shot incremental image classification by up to 22% on the miniImageNet dataset. Because of its simplicity, subspace regularization can be straightforwardly extended to incorporate additional background information about the new classes (including class names and descriptions specified in natural language); these further improve accuracy by up to 2%. Our results show that simple geometric regularization of class representations offers an effective tool for continual learning.

</details>

### Looking Back on Learned Experiences For Class/task Incremental Learning.
- **链接**: [出版页](https://openreview.net/forum?id=RxplU3vmBx)
- **作者**: Mozhgan PourKeshavarz, Guoying Zhao, Mohammad Sabokrou
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

## 🆕 增量新增

### Few-Shot Class-Incremental Learning for 3D Point Cloud Objects.
- **链接**: [arXiv:2205.15225](https://arxiv.org/abs/2205.15225)
- **作者**: Townim F. Chowdhury, Ali Cheraghian, Sameera Ramasinghe, Sahar Ahmadi, Morteza Saberi, Shafin Rahman
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Few-shot class-incremental learning (FSCIL) aims to incrementally fine-tune a model (trained on base classes) for a novel set of classes using a few examples without forgetting the previous training. Recent efforts address this problem primarily on 2D images. However, due to the advancement of camera technology, 3D point cloud data has become more available than ever, which warrants considering FSCIL on 3D data. This paper addresses FSCIL in the 3D domain. In addition to well-known issues of catastrophic forgetting of past knowledge and overfitting of few-shot data, 3D FSCIL can bring newer challenges. For example, base classes may contain many synthetic instances in a realistic scenario. In contrast, only a few real-scanned samples (from RGBD sensors) of novel classes are available in incremental steps. Due to the data variation from synthetic to real, FSCIL endures additional challenges, degrading performance in later incremental steps. We attempt to solve this problem using Microshapes (orthogonal basis vectors) by describing any 3D objects using a pre-defined set of rules. It supports incremental training with few-shot examples minimizing synthetic to real data variation. We propose new test protocols for 3D FSCIL using popular synthetic datasets (ModelNet and ShapeNet) and 3D real-scanned datasets (ScanObjectNN and CO3D). By comparing state-of-the-art methods, we establish the effectiveness of our approach in the 3D domain.

</details>

### Online Continual Learning with Contrastive Vision Transformer.
- **链接**: [arXiv:2207.13516](https://arxiv.org/abs/2207.13516) · 📚 被引 30
- **作者**: Zhen Wang, Liu Liu, Yajing Kong, Jiaxian Guo, Dacheng Tao
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Online continual learning (online CL) studies the problem of learning sequential tasks from an online data stream without task boundaries, aiming to adapt to new data while alleviating catastrophic forgetting on the past tasks. This paper proposes a framework Contrastive Vision Transformer (CVT), which designs a focal contrastive learning strategy based on a transformer architecture, to achieve a better stability-plasticity trade-off for online CL. Specifically, we design a new external attention mechanism for online CL that implicitly captures previous tasks' information. Besides, CVT contains learnable focuses for each class, which could accumulate the knowledge of previous classes to alleviate forgetting. Based on the learnable focuses, we design a focal contrastive loss to rebalance contrastive learning between new and past classes and consolidate previously learned representations. Moreover, CVT contains a dual-classifier structure for decoupling learning current classes and balancing all observed classes. The extensive experimental results show that our approach achieves state-of-the-art performance with even fewer parameters on online CL benchmarks and effectively alleviates the catastrophic forgetting.

</details>

### S3C: Self-Supervised Stochastic Classifiers for Few-Shot Class-Incremental Learning.
- **链接**: [arXiv:2307.02246](https://arxiv.org/abs/2307.02246) · 📚 被引 45
- **作者**: Jayateja Kalla, Soma Biswas
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Few-shot class-incremental learning (FSCIL) aims to learn progressively about new classes with very few labeled samples, without forgetting the knowledge of already learnt classes. FSCIL suffers from two major challenges: (i) over-fitting on the new classes due to limited amount of data, (ii) catastrophically forgetting about the old classes due to unavailability of data from these classes in the incremental stages. In this work, we propose a self-supervised stochastic classifier (S3C) to counter both these challenges in FSCIL. The stochasticity of the classifier weights (or class prototypes) not only mitigates the adverse effect of absence of large number of samples of the new classes, but also the absence of samples from previously learnt classes during the incremental steps. This is complemented by the self-supervision component, which helps to learn features from the base classes which generalize well to unseen classes that are encountered in future, thus reducing catastrophic forgetting. Extensive evaluation on three benchmark datasets using multiple evaluation metrics show the effectiveness of the proposed framework. We also experiment on two additional realistic scenarios of FSCIL, namely where the number of annotated data available for each of the new classes can be different, and also where the number of base classes is much lesser, and show that the proposed S3C performs significantly better than the state-of-the-art for all these challenging scenarios.

</details>

### DualPrompt: Complementary Prompting for Rehearsal-Free Continual Learning.
- **链接**: [arXiv:2204.04799](https://arxiv.org/abs/2204.04799) · 📚 被引 421
- **作者**: Zifeng Wang, Zizhao Zhang, Sayna Ebrahimi, Ruoxi Sun, Han Zhang, Chen-Yu Lee et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning aims to enable a single model to learn a sequence of tasks without catastrophic forgetting. Top-performing methods usually require a rehearsal buffer to store past pristine examples for experience replay, which, however, limits their practical value due to privacy and memory constraints. In this work, we present a simple yet effective framework, DualPrompt, which learns a tiny set of parameters, called prompts, to properly instruct a pre-trained model to learn tasks arriving sequentially without buffering past examples. DualPrompt presents a novel approach to attach complementary prompts to the pre-trained backbone, and then formulates the objective as learning task-invariant and task-specific "instructions". With extensive experimental validation, DualPrompt consistently sets state-of-the-art performance under the challenging class-incremental setting. In particular, DualPrompt outperforms recent advanced continual learning methods with relatively large buffer sizes. We also introduce a more challenging benchmark, Split ImageNet-R, to help generalize rehearsal-free continual learning research. Source code is available at https://github.com/google-research/l2p.

</details>

### Theoretical Understanding of the Information Flow on Continual Learning Performance.
- **链接**: [arXiv:2204.12010](https://arxiv.org/abs/2204.12010) · 📚 被引 4
- **作者**: Joshua Andle, Salimeh Yasaei Sekeh
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning (CL) is a setting in which an agent has to learn from an incoming stream of data sequentially. CL performance evaluates the model's ability to continually learn and solve new problems with incremental available information over time while retaining previous knowledge. Despite the numerous previous solutions to bypass the catastrophic forgetting (CF) of previously seen tasks during the learning process, most of them still suffer significant forgetting, expensive memory cost, or lack of theoretical understanding of neural networks' conduct while learning new tasks. While the issue that CL performance degrades under different training regimes has been extensively studied empirically, insufficient attention has been paid from a theoretical angle. In this paper, we establish a probabilistic framework to analyze information flow through layers in networks for task sequences and its impact on learning performance. Our objective is to optimize the information preservation between layers while learning new tasks to manage task-specific knowledge passing throughout the layers while maintaining model performance on previous tasks. In particular, we study CL performance's relationship with information flow in the network to answer the question "How can knowledge of information flow between layers be used to alleviate CF?". Our analysis provides novel insights of information adaptation within the layers during the incremental task learning process. Through our experiments, we provide empirical evidence and practically highlight the performance improvement across multiple tasks.

</details>

### Helpful or Harmful: Inter-task Association in Continual Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20083-0_31) · 📚 被引 18
- **作者**: Hyundong Jin, Eunwoo Kim
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Balancing Stability and Plasticity Through Advanced Null Space in Continual Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19809-0_13) · 📚 被引 25
- **作者**: Yajing Kong, Liu Liu, Zhen Wang, Dacheng Tao
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Online Task-free Continual Learning with Dynamic Sparse Distributed Memory.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19806-9_42) · 📚 被引 12
- **作者**: Julien Pourcel, Ngoc-Son Vu, Robert M. French
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### DLCFT: Deep Linear Continual Fine-Tuning for General Incremental Learning.
- **链接**: [arXiv:2208.08112](https://arxiv.org/abs/2208.08112) · 📚 被引 15
- **作者**: Hyounguk Shon, Janghyeon Lee, Seung Hwan Kim, Junmo Kim
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pre-trained representation is one of the key elements in the success of modern deep learning. However, existing works on continual learning methods have mostly focused on learning models incrementally from scratch. In this paper, we explore an alternative framework to incremental learning where we continually fine-tune the model from a pre-trained representation. Our method takes advantage of linearization technique of a pre-trained neural network for simple and effective continual learning. We show that this allows us to design a linear model where quadratic parameter regularization method is placed as the optimal continual learning policy, and at the same time enjoying the high performance of neural networks. We also show that the proposed algorithm enables parameter regularization methods to be applied to class-incremental problems. Additionally, we provide a theoretical reason why the existing parameter-space regularization algorithms such as EWC underperform on neural networks trained with cross-entropy loss. We show that the proposed method can prevent forgetting while achieving high continual fine-tuning performance on image classification tasks. To show that our method can be applied to general continual learning settings, we evaluate our method in data-incremental, task-incremental, and class-incremental learning problems.

</details>

### R-DFCIL: Relation-Guided Representation Learning for Data-Free Class Incremental Learning.
- **链接**: [arXiv:2203.13104](https://arxiv.org/abs/2203.13104)
- **作者**: Qiankun Gao, Chen Zhao, Bernard Ghanem, Jian Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Class-Incremental Learning (CIL) struggles with catastrophic forgetting when learning new knowledge, and Data-Free CIL (DFCIL) is even more challenging without access to the training data of previously learned classes. Though recent DFCIL works introduce techniques such as model inversion to synthesize data for previous classes, they fail to overcome forgetting due to the severe domain gap between the synthetic and real data. To address this issue, this paper proposes relation-guided representation learning (RRL) for DFCIL, dubbed R-DFCIL. In RRL, we introduce relational knowledge distillation to flexibly transfer the structural relation of new data from the old model to the current model. Our RRL-boosted DFCIL can guide the current model to learn representations of new classes better compatible with representations of previous classes, which greatly reduces forgetting while improving plasticity. To avoid the mutual interference between representation and classifier learning, we employ local rather than global classification loss during RRL. After RRL, the classification head is refined with global class-balanced classification loss to address the data imbalance issue as well as learn the decision boundaries between new and previous classes. Extensive experiments on CIFAR100, Tiny-ImageNet200, and ImageNet100 demonstrate that our R-DFCIL significantly surpasses previous approaches and achieves a new state-of-the-art performance for DFCIL. Code is available at https://github.com/jianzhangcs/R-DFCIL

</details>

### Class-Incremental Learning with Cross-Space Clustering and Controlled Transfer.
- **链接**: [arXiv:2208.03767](https://arxiv.org/abs/2208.03767) · 📚 被引 31
- **作者**: Arjun Ashok, K. J. Joseph, Vineeth N. Balasubramanian
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In class-incremental learning, the model is expected to learn new classes continually while maintaining knowledge on previous classes. The challenge here lies in preserving the model's ability to effectively represent prior classes in the feature space, while adapting it to represent incoming new classes. We propose two distillation-based objectives for class incremental learning that leverage the structure of the feature space to maintain accuracy on previous classes, as well as enable learning the new classes. In our first objective, termed cross-space clustering (CSC), we propose to use the feature space structure of the previous model to characterize directions of optimization that maximally preserve the class: directions that all instances of a specific class should collectively optimize towards, and those that they should collectively optimize away from. Apart from minimizing forgetting, this indirectly encourages the model to cluster all instances of a class in the current feature space, and gives rise to a sense of herd-immunity, allowing all samples of a class to jointly combat the model from forgetting the class. Our second objective termed controlled transfer (CT) tackles incremental learning from an understudied perspective of inter-class transfer. CT explicitly approximates and conditions the current model on the semantic similarities between incrementally arriving classes and prior classes. This allows the model to learn classes in such a way that it maximizes positive forward transfer from similar prior classes, thus increasing plasticity, and minimizes negative backward transfer on dissimilar prior classes, whereby strengthening stability. We perform extensive experiments on two benchmark datasets, adding our method (CSCCT) on top of three prominent class-incremental learning methods. We observe consistent performance improvement on a variety of experimental settings.

</details>

### Few-Shot Class-Incremental Learning via Entropy-Regularized Data-Free Replay.
- **链接**: [arXiv:2207.11213](https://arxiv.org/abs/2207.11213)
- **作者**: Huan Liu, Li Gu, Zhixiang Chi, Yang Wang, Yuanhao Yu, Jun Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Few-shot class-incremental learning (FSCIL) has been proposed aiming to enable a deep learning system to incrementally learn new classes with limited data. Recently, a pioneer claims that the commonly used replay-based method in class-incremental learning (CIL) is ineffective and thus not preferred for FSCIL. This has, if truth, a significant influence on the fields of FSCIL. In this paper, we show through empirical results that adopting the data replay is surprisingly favorable. However, storing and replaying old data can lead to a privacy concern. To address this issue, we alternatively propose using data-free replay that can synthesize data by a generator without accessing real data. In observing the the effectiveness of uncertain data for knowledge distillation, we impose entropy regularization in the generator training to encourage more uncertain examples. Moreover, we propose to relabel the generated data with one-hot-like labels. This modification allows the network to learn by solely minimizing the cross-entropy loss, which mitigates the problem of balancing different objectives in the conventional knowledge distillation approach. Finally, we show extensive experimental results and analysis on CIFAR-100, miniImageNet and CUB-200 to demonstrate the effectiveness of our proposed one.

</details>

### Long-Tailed Class Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19827-4_29)
- **作者**: Xialei Liu, Yusong Hu, Xu-Sheng Cao, Andrew D. Bagdanov, Ke Li, Ming-Ming Cheng
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Few-Shot Class-Incremental Learning from an Open-Set Perspective.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19806-9_22)
- **作者**: Can Peng, Kun Zhao, Tianren Wang, Meng Li, Brian C. Lovell
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### FOSTER: Feature Boosting and Compression for Class-Incremental Learning.
- **链接**: [arXiv:2204.04662](https://arxiv.org/abs/2204.04662) · 📚 被引 294
- **作者**: Fu-Yun Wang, Da-Wei Zhou, Han-Jia Ye, De-Chuan Zhan
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The ability to learn new concepts continually is necessary in this ever-changing world. However, deep neural networks suffer from catastrophic forgetting when learning new categories. Many works have been proposed to alleviate this phenomenon, whereas most of them either fall into the stability-plasticity dilemma or take too much computation or storage overhead. Inspired by the gradient boosting algorithm to gradually fit the residuals between the target model and the previous ensemble model, we propose a novel two-stage learning paradigm FOSTER, empowering the model to learn new categories adaptively. Specifically, we first dynamically expand new modules to fit the residuals between the target and the output of the original model. Next, we remove redundant parameters and feature dimensions through an effective distillation strategy to maintain the single backbone model. We validate our method FOSTER on CIFAR-100 and ImageNet-100/1000 under different settings. Experimental results show that our method achieves state-of-the-art performance. Code is available at: https://github.com/G-U-N/ECCV22-FOSTER.

</details>

### Learning Fast, Learning Slow: A General Continual Learning Method based on Complementary Learning System.
- **链接**: [arXiv:2201.12604](https://arxiv.org/abs/2201.12604)
- **作者**: Elahe Arani, Fahad Sarfraz, Bahram Zonooz
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Humans excel at continually learning from an ever-changing environment whereas it remains a challenge for deep neural networks which exhibit catastrophic forgetting. The complementary learning system (CLS) theory suggests that the interplay between rapid instance-based learning and slow structured learning in the brain is crucial for accumulating and retaining knowledge. Here, we propose CLS-ER, a novel dual memory experience replay (ER) method which maintains short-term and long-term semantic memories that interact with the episodic memory. Our method employs an effective replay mechanism whereby new knowledge is acquired while aligning the decision boundaries with the semantic memories. CLS-ER does not utilize the task boundaries or make any assumption about the distribution of the data which makes it versatile and suited for "general continual learning". Our approach achieves state-of-the-art performance on standard benchmarks as well as more realistic general continual learning settings.

</details>

### Learning curves for continual learning in neural networks: Self-knowledge transfer and forgetting.
- **链接**: [出版页](https://openreview.net/forum?id=tFgdrQbbaa)
- **作者**: Ryo Karakida, Shotaro Akaho
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

### Continual Normalization: Rethinking Batch Normalization for Online Continual Learning.
- **链接**: [arXiv:2203.16102](https://arxiv.org/abs/2203.16102)
- **作者**: Quang Pham, Chenghao Liu, Steven C. H. Hoi
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing continual learning methods use Batch Normalization (BN) to facilitate training and improve generalization across tasks. However, the non-i.i.d and non-stationary nature of continual learning data, especially in the online setting, amplify the discrepancy between training and testing in BN and hinder the performance of older tasks. In this work, we study the cross-task normalization effect of BN in online continual learning where BN normalizes the testing data using moments biased towards the current task, resulting in higher catastrophic forgetting. This limitation motivates us to propose a simple yet effective method that we call Continual Normalization (CN) to facilitate training similar to BN while mitigating its negative effect. Extensive experiments on different continual learning algorithms and online scenarios show that CN is a direct replacement for BN and can provide substantial performance improvements. Our implementation is available at \url{https://github.com/phquang/Continual-Normalization}.

</details>

### New Insights on Reducing Abrupt Representation Change in Online Continual Learning.
- **链接**: [出版页](https://openreview.net/forum?id=N8MaByOzUfb)
- **作者**: Lucas Caccia, Rahaf Aljundi, Nader Asadi, Tinne Tuytelaars, Joelle Pineau, Eugene Belilovsky
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

### Online Continual Learning on Class Incremental Blurry Task Configuration with Anytime Inference.
- **链接**: [arXiv:2110.10031](https://arxiv.org/abs/2110.10031)
- **作者**: Hyunseo Koh, Dahyun Kim, Jung-Woo Ha, Jonghyun Choi
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite rapid advances in continual learning, a large body of research is devoted to improving performance in the existing setups. While a handful of work do propose new continual learning setups, they still lack practicality in certain aspects. For better practicality, we first propose a novel continual learning setup that is online, task-free, class-incremental, of blurry task boundaries and subject to inference queries at any moment. We additionally propose a new metric to better measure the performance of the continual learning methods subject to inference queries at any moment. To address the challenging setup and evaluation protocol, we propose an effective method that employs a new memory management scheme and novel learning techniques. Our empirical validation demonstrates that the proposed method outperforms prior arts by large margins. Code and data splits are available at https://github.com/naver-ai/i-Blurry.

</details>

### TRGP: Trust Region Gradient Projection for Continual Learning.
- **链接**: [arXiv:2202.02931](https://arxiv.org/abs/2202.02931)
- **作者**: Sen Lin, Li Yang, Deliang Fan, Junshan Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Catastrophic forgetting is one of the major challenges in continual learning. To address this issue, some existing methods put restrictive constraints on the optimization space of the new task for minimizing the interference to old tasks. However, this may lead to unsatisfactory performance for the new task, especially when the new task is strongly correlated with old tasks. To tackle this challenge, we propose Trust Region Gradient Projection (TRGP) for continual learning to facilitate the forward knowledge transfer based on an efficient characterization of task correlation. Particularly, we introduce a notion of `trust region' to select the most related old tasks for the new task in a layer-wise and single-shot manner, using the norm of gradient projection onto the subspace spanned by task inputs. Then, a scaled weight projection is proposed to cleverly reuse the frozen weights of the selected old tasks in the trust region through a layer-wise scaling matrix. By jointly optimizing the scaling matrices and the model, where the model is updated along the directions orthogonal to the subspaces of old tasks, TRGP can effectively prompt knowledge transfer without forgetting. Extensive experiments show that our approach achieves significant improvement over related state-of-the-art methods.

</details>

### Continual Learning with Recursive Gradient Optimization.
- **链接**: [arXiv:2201.12522](https://arxiv.org/abs/2201.12522)
- **作者**: Hao Liu, Huaping Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Learning multiple tasks sequentially without forgetting previous knowledge, called Continual Learning(CL), remains a long-standing challenge for neural networks. Most existing methods rely on additional network capacity or data replay. In contrast, we introduce a novel approach which we refer to as Recursive Gradient Optimization(RGO). RGO is composed of an iteratively updated optimizer that modifies the gradient to minimize forgetting without data replay and a virtual Feature Encoding Layer(FEL) that represents different long-term structures with only task descriptors. Experiments demonstrate that RGO has significantly better performance on popular continual classification benchmarks when compared to the baselines and achieves new state-of-the-art performance on 20-split-CIFAR100(82.22%) and 20-split-miniImageNet(72.63%). With higher average accuracy than Single-Task Learning(STL), this method is flexible and reliable to provide continual learning capabilities for learning models that rely on gradient descent.

</details>

### Representational Continuity for Unsupervised Continual Learning.
- **链接**: [出版页](https://openreview.net/forum?id=9Hrka5PA7LW)
- **作者**: Divyam Madaan, Jaehong Yoon, Yuanchun Li, Yunxin Liu, Sung Ju Hwang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

### Continual Learning with Filter Atom Swapping.
- **链接**: [出版页](https://openreview.net/forum?id=metRpM4Zrcb)
- **作者**: Zichen Miao, Ze Wang, Wei Chen, Qiang Qiu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

### CLEVA-Compass: A Continual Learning Evaluation Assessment Compass to Promote Research Transparency and Comparability.
- **链接**: [arXiv:2110.03331](https://arxiv.org/abs/2110.03331)
- **作者**: Martin Mundt, Steven Lang, Quentin Delfosse, Kristian Kersting
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> What is the state of the art in continual machine learning? Although a natural question for predominant static benchmarks, the notion to train systems in a lifelong manner entails a plethora of additional challenges with respect to set-up and evaluation. The latter have recently sparked a growing amount of critiques on prominent algorithm-centric perspectives and evaluation protocols being too narrow, resulting in several attempts at constructing guidelines in favor of specific desiderata or arguing against the validity of prevalent assumptions. In this work, we depart from this mindset and argue that the goal of a precise formulation of desiderata is an ill-posed one, as diverse applications may always warrant distinct scenarios. Instead, we introduce the Continual Learning EValuation Assessment Compass: the CLEVA-Compass. The compass provides the visual means to both identify how approaches are practically reported and how works can simultaneously be contextualized in the broader literature landscape. In addition to promoting compact specification in the spirit of recent replication trends, it thus provides an intuitive chart to understand the priorities of individual systems, where they resemble each other, and what elements are missing towards a fair comparison.

</details>

### Information-theoretic Online Memory Selection for Continual Learning.
- **链接**: [arXiv:2204.04763](https://arxiv.org/abs/2204.04763)
- **作者**: Shengyang Sun, Daniele Calandriello, Huiyi Hu, Ang Li, Michalis K. Titsias
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> A challenging problem in task-free continual learning is the online selection of a representative replay memory from data streams. In this work, we investigate the online memory selection problem from an information-theoretic perspective. To gather the most information, we propose the \textit{surprise} and the \textit{learnability} criteria to pick informative points and to avoid outliers. We present a Bayesian model to compute the criteria efficiently by exploiting rank-one matrix structures. We demonstrate that these criteria encourage selecting informative points in a greedy algorithm for online memory selection. Furthermore, by identifying the importance of \textit{the timing to update the memory}, we introduce a stochastic information-theoretic reservoir sampler (InfoRS), which conducts sampling among selective points with high information. Compared to reservoir sampling, InfoRS demonstrates improved robustness against data imbalance. Finally, empirical performances over continual learning benchmarks manifest its efficiency and efficacy.

</details>

### Memory Replay with Data Compression for Continual Learning.
- **链接**: [arXiv:2202.06592](https://arxiv.org/abs/2202.06592)
- **作者**: Liyuan Wang, Xingxing Zhang, Kuo Yang, Longhui Yu, Chongxuan Li, Lanqing Hong et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning needs to overcome catastrophic forgetting of the past. Memory replay of representative old training samples has been shown as an effective solution, and achieves the state-of-the-art (SOTA) performance. However, existing work is mainly built on a small memory buffer containing a few original data, which cannot fully characterize the old data distribution. In this work, we propose memory replay with data compression (MRDC) to reduce the storage cost of old training samples and thus increase their amount that can be stored in the memory buffer. Observing that the trade-off between the quality and quantity of compressed data is highly nontrivial for the efficacy of memory replay, we propose a novel method based on determinantal point processes (DPPs) to efficiently determine an appropriate compression quality for currently-arrived training samples. In this way, using a naive data compression algorithm with a properly selected quality can largely boost recent strong baselines by saving more compressed data in a limited storage space. We extensively validate this across several benchmarks of class-incremental learning and in a realistic scenario of object detection for autonomous driving.

</details>

### Pretrained Language Model in Continual Learning: A Comparative Study.
- **链接**: [出版页](https://openreview.net/forum?id=figzpGMrdD)
- **作者**: Tongtong Wu, Massimo Caccia, Zhuang Li, Yuan-Fang Li, Guilin Qi, Gholamreza Haffari
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

### Online Coreset Selection for Rehearsal-based Continual Learning.
- **链接**: [arXiv:2106.01085](https://arxiv.org/abs/2106.01085)
- **作者**: Jaehong Yoon, Divyam Madaan, Eunho Yang, Sung Ju Hwang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> A dataset is a shred of crucial evidence to describe a task. However, each data point in the dataset does not have the same potential, as some of the data points can be more representative or informative than others. This unequal importance among the data points may have a large impact in rehearsal-based continual learning, where we store a subset of the training examples (coreset) to be replayed later to alleviate catastrophic forgetting. In continual learning, the quality of the samples stored in the coreset directly affects the model's effectiveness and efficiency. The coreset selection problem becomes even more important under realistic settings, such as imbalanced continual learning or noisy data scenarios. To tackle this problem, we propose Online Coreset Selection (OCS), a simple yet effective method that selects the most representative and informative coreset at each iteration and trains them in an online manner. Our proposed method maximizes the model's adaptation to a current dataset while selecting high-affinity samples to past tasks, which directly inhibits catastrophic forgetting. We validate the effectiveness of our coreset selection mechanism over various standard, imbalanced, and noisy datasets against strong continual learning baselines, demonstrating that it improves task adaptation and prevents catastrophic forgetting in a sample-efficient manner.

</details>

### Learning a Condensed Frame for Memory-Efficient Video Class-Incremental Learning.
- **链接**: [arXiv:2211.00833](https://arxiv.org/abs/2211.00833) · 📚 被引 1
- **作者**: Yixuan Pei, Zhiwu Qing, Jun Cen, Xiang Wang, Shiwei Zhang, Yaxiong Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent incremental learning for action recognition usually stores representative videos to mitigate catastrophic forgetting. However, only a few bulky videos can be stored due to the limited memory. To address this problem, we propose FrameMaker, a memory-efficient video class-incremental learning approach that learns to produce a condensed frame for each selected video. Specifically, FrameMaker is mainly composed of two crucial components: Frame Condensing and Instance-Specific Prompt. The former is to reduce the memory cost by preserving only one condensed frame instead of the whole video, while the latter aims to compensate the lost spatio-temporal details in the Frame Condensing stage. By this means, FrameMaker enables a remarkable reduction in memory but keep enough information that can be applied to following incremental tasks. Experimental results on multiple challenging benchmarks, i.e., HMDB51, UCF101 and Something-Something V2, demonstrate that FrameMaker can achieve better performance to recent advanced methods while consuming only 20% memory. Additionally, under the same memory consumption conditions, FrameMaker significantly outperforms existing state-of-the-arts by a convincing margin.

</details>

### S-Prompts Learning with Pre-trained Transformers: An Occam's Razor for Domain Incremental Learning.
- **链接**: [arXiv:2207.12819](https://arxiv.org/abs/2207.12819) · 📚 被引 34
- **作者**: Yabin Wang, Zhiwu Huang, Xiaopeng Hong
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> State-of-the-art deep neural networks are still struggling to address the catastrophic forgetting problem in continual learning. In this paper, we propose one simple paradigm (named as S-Prompting) and two concrete approaches to highly reduce the forgetting degree in one of the most typical continual learning scenarios, i.e., domain increment learning (DIL). The key idea of the paradigm is to learn prompts independently across domains with pre-trained transformers, avoiding the use of exemplars that commonly appear in conventional methods. This results in a win-win game where the prompting can achieve the best for each domain. The independent prompting across domains only requests one single cross-entropy loss for training and one simple K-NN operation as a domain identifier for inference. The learning paradigm derives an image prompt learning approach and a novel language-image prompt learning approach. Owning an excellent scalability (0.03% parameter increase per domain), the best of our approaches achieves a remarkable relative improvement (an average of about 30%) over the best of the state-of-the-art exemplar-free methods for three standard DIL tasks, and even surpasses the best of them relatively by about 6% in average when they use exemplars. Source code is available at \url{https://github.com/iamwangyabin/S-Prompts}.

</details>

### ACIL: Analytic Class-Incremental Learning with Absolute Memorization and Privacy Protection.
- **链接**: [arXiv:2205.14922](https://arxiv.org/abs/2205.14922) · 📚 被引 12
- **作者**: Huiping Zhuang, Zhenyu Weng, Hongxin Wei, Renchunzi Xie, Kar-Ann Toh, Zhiping Lin
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Class-incremental learning (CIL) learns a classification model with training data of different classes arising progressively. Existing CIL either suffers from serious accuracy loss due to catastrophic forgetting, or invades data privacy by revisiting used exemplars. Inspired by linear learning formulations, we propose an analytic class-incremental learning (ACIL) with absolute memorization of past knowledge while avoiding breaching of data privacy (i.e., without storing historical data). The absolute memorization is demonstrated in the sense that class-incremental learning using ACIL given present data would give identical results to that from its joint-learning counterpart which consumes both present and historical samples. This equality is theoretically validated. Data privacy is ensured since no historical data are involved during the learning process. Empirical validations demonstrate ACIL's competitive accuracy performance with near-identical results for various incremental task settings (e.g., 5-50 phases). This also allows ACIL to outperform the state-of-the-art methods for large-phase scenarios (e.g., 25 and 50 phases).

</details>

### Margin-Based Few-Shot Class-Incremental Learning with Class-Level Overfitting Mitigation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/ae817e85f71ef86d5c9566598e185b89-Abstract-Conference.html) · 📚 被引 4
- **作者**: Yixiong Zou, Shanghang Zhang, Yuhua Li, Ruixuan Li
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Decomposed Knowledge Distillation for Class-Incremental Semantic Segmentation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/439bf902de1807088d8b731ca20b0777-Abstract-Conference.html) · 📚 被引 10
- **作者**: Donghyeon Baek, Youngmin Oh, Sanghoon Lee, Junghyup Lee, Bumsub Ham
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

## 跨领域论文（完整笔记在其他领域）

- Meta-attention for ViT-backed Continual Learning. → [vision-transformer](../vision-transformer/Guideline%202022.md)
- Generative Negative Text Replay for Continual Vision-Language Pretraining. → [vlm](../vlm/Guideline%202022.md)

<!-- COMPLETE v1 papers=65 -->
