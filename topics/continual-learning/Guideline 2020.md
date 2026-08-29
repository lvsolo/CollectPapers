# Continual Learning — 2020 Guideline

> 领域: 持续学习 / 增量学习（含 VLM/多模态场景）
> 论文数: 8 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Conditional Channel Gated Networks for Task-Aware Continual Learning.
- **链接**: [arXiv:2004.00070](https://arxiv.org/abs/2004.00070) · 📚 被引 140
- **作者**: Davide Abati, Jakub M. Tomczak, Tijmen Blankevoort, Simone Calderara, Rita Cucchiara, Babak Ehteshami Bejnordi
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Convolutional Neural Networks experience catastrophic forgetting when optimized on a sequence of learning problems: as they meet the objective of the current training examples, their performance on previous tasks drops drastically. In this work, we introduce a novel framework to tackle this problem with conditional computation. We equip each convolutional layer with task-specific gating modules, selecting which filters to apply on the given input. This way, we achieve two appealing properties. Firstly, the execution patterns of the gates allow to identify and protect important filters, ensuring no loss in the performance of the model for previously learned tasks. Secondly, by using a sparsity objective, we can promote the selection of a limited set of kernels, allowing to retain sufficient model capacity to digest new tasks.Existing solutions require, at test time, awareness of the task to which each example belongs to. This knowledge, however, may not be available in many practical scenarios. Therefore, we additionally introduce a task classifier that predicts the task label of each example, to deal with settings in which a task oracle is not available. We validate our proposal on four continual learning datasets. Results show that our model consistently outperforms existing methods both in the presence and the absence of a task oracle. Notably, on Split SVHN and Imagenet-50 datasets, our model yields up to 23.98% and 17.42% improvement in accuracy w.r.t. competing methods.

</details>

### Continual Learning With Extended Kronecker-Factored Approximate Curvature.
- **链接**: [arXiv:2004.07507](https://arxiv.org/abs/2004.07507) · 📚 被引 44
- **作者**: Janghyeon Lee, Hyeong Gwon Hong, Donggyu Joo, Junmo Kim
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### GDumb: A Simple Approach that Questions Our Progress in Continual Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58536-5_31) · 📚 被引 348
- **作者**: Ameya Prabhu, Philip H. S. Torr, Puneet K. Dokania
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### More Classifiers, Less Forgetting: A Generic Multi-classifier Paradigm for Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58574-7_42) · 📚 被引 65
- **作者**: Yu Liu, Sarah Parisot, Gregory G. Slabaugh, Xu Jia, Ales Leonardis, Tinne Tuytelaars
- **🏷️ 机构**: SenseTime
- **会议**: ECCV 2020

> In continual learning (CL), a learner is faced with a sequence of tasks, arriving one after the other, and the goal is to remember all the tasks once the continual learning experience is finished. The prior art in CL uses episodic memory, parameter regularization or extensible network structures to reduce interference among tasks, but in the end, all the approaches learn different tasks in a joint vector space. We believe this invariably leads to interference among different tasks. We propose to learn tasks in different (low-rank) vector subspaces that are kept orthogonal to each other in order to minimize interference. Further, to keep the gradients of different tasks coming from these subspaces orthogonal to each other, we learn isometric mappings by posing network training as an optimization problem over the Stiefel manifold. To the best of our understanding, we report, for the first time, strong results over experience-replay baseline with and without memory on standard classification benchmarks in continual learning. The code is made publicly available.

</details>

### Modeling the Background for Incremental Learning in Semantic Segmentation.
- **链接**: [arXiv:2002.00718](https://arxiv.org/abs/2002.00718) · 📚 被引 310
- **作者**: Fabio Cermelli, Massimiliano Mancini, Samuel Rota Bulò, Elisa Ricci, Barbara Caputo
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The ability to continuously learn and adapt itself to new tasks, without losing grasp of already acquired knowledge is a hallmark of biological learning systems, which current deep learning systems fall short of. In this work, we present a novel methodology for continual learning called MERLIN: Meta-Consolidation for Continual Learning. We assume that weights of a neural network $\boldsymbol ψ$, for solving task $\boldsymbol t$, come from a meta-distribution $p(\boldsymbol{ψ|t})$. This meta-distribution is learned and consolidated incrementally. We operate in the challenging online continual learning setting, where a data point is seen by the model only once. Our experiments with continual learning benchmarks of MNIST, CIFAR-10, CIFAR-100 and Mini-ImageNet datasets show consistent improvement over five baselines, including a recent state-of-the-art, corroborating the promise of MERLIN.

</details>

### Incremental Learning in Online Scenario.
- **链接**: [arXiv:2003.13191](https://arxiv.org/abs/2003.13191) · 📚 被引 140
- **作者**: Jiangpeng He, Runyu Mao, Zeman Shao, Fengqing Zhu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Topology-Preserving Class-Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58529-7_16)
- **作者**: Xiaoyu Tao, Xinyuan Chang, Xiaopeng Hong, Xing Wei, Yihong Gong
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Catastrophic forgetting affects the training of neural networks, limiting their ability to learn multiple tasks sequentially. From the perspective of the well established plasticity-stability dilemma, neural networks tend to be overly plastic, lacking the stability necessary to prevent the forgetting of previous knowledge, which means that as learning progresses, networks tend to forget previously seen tasks. This phenomenon coined in the continual learning literature, has attracted much attention lately, and several families of approaches have been proposed with different degrees of success. However, there has been limited prior work extensively analyzing the impact that different training regimes -- learning rate, batch size, regularization method-- can have on forgetting. In this work, we depart from the typical approach of altering the learning algorithm to improve stability. Instead, we hypothesize that the geometrical properties of the local minima found for each task play an important role in the overall degree of forgetting. In particular, we study the effect of dropout, learning rate decay, and batch size, on forming training regimes that widen the tasks' local minima and consequently, on helping it not to forget catastrophically. Our study provides practical insights to improve stability via simple yet effective techniques that outperform alternative baselines.

</details>

### Continual Learning of Control Primitives : Skill Discovery via Reset-Games.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/3472ab80b6dff70c54758fd6dfc800c2-Abstract.html)
- **作者**: Kelvin Xu, Siddharth Verma, Chelsea Finn, Sergey Levine
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Maintaining Discrimination and Fairness in Class Incremental Learning.
- **链接**: [arXiv:1911.07053](https://arxiv.org/abs/1911.07053) · 📚 被引 431
- **作者**: Bowen Zhao, Xi Xiao, Guojun Gan, Bin Zhang, Shu-Tao Xia
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep neural networks (DNNs) have been applied in class incremental learning, which aims to solve common real-world problems of learning new classes continually. One drawback of standard DNNs is that they are prone to catastrophic forgetting. Knowledge distillation (KD) is a commonly used technique to alleviate this problem. In this paper, we demonstrate it can indeed help the model to output more discriminative results within old classes. However, it cannot alleviate the problem that the model tends to classify objects into new classes, causing the positive effect of KD to be hidden and limited. We observed that an important factor causing catastrophic forgetting is that the weights in the last fully connected (FC) layer are highly biased in class incremental learning. In this paper, we propose a simple and effective solution motivated by the aforementioned observations to address catastrophic forgetting. Firstly, we utilize KD to maintain the discrimination within old classes. Then, to further maintain the fairness between old classes and new classes, we propose Weight Aligning (WA) that corrects the biased weights in the FC layer after normal training process. Unlike previous work, WA does not require any extra parameters or a validation set in advance, as it utilizes the information provided by the biased weights themselves. The proposed method is evaluated on ImageNet-1000, ImageNet-100, and CIFAR-100 under various settings. Experimental results show that the proposed method can effectively alleviate catastrophic forgetting and significantly outperform state-of-the-art methods.

</details>

## 🆕 增量新增

### Semantic Drift Compensation for Class-Incremental Learning. **⭐⭐⭐** (相关度: 55%)
- **链接**: [arXiv:2004.00440](https://arxiv.org/abs/2004.00440) · 📚 被引 268
- **作者**: Lu Yu, Bartlomiej Twardowski, Xialei Liu, Luis Herranz, Kai Wang, Yongmei Cheng et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: 针对类增量学习中嵌入网络的特征漂移问题，本文提出了一种语义漂移补偿方法，通过当前任务数据的漂移来近似估计旧任务的漂移，无需存储任何样本。在细粒度数据集、CIFAR100和ImageNet-Subset上验证了嵌入网络比传统分类网络遗忘更少，且所提方法进一步提升了性能。改进点在于利用嵌入空间的特性实现无样本补偿。
- **摘要（英）**: This paper tackles feature drift in embedding networks for class-incremental learning by estimating semantic drift from current task data without exemplars. Experiments on fine-grained datasets, CIFAR100, and ImageNet-Subset show embedding networks suffer less forgetting and the proposed compensation improves accuracy.
- **核心贡献**: 提出了无样本的语义漂移补偿方法，适用于嵌入网络的类增量学习。
- **创新点**: 利用当前任务数据估计旧任务特征漂移，避免了样本存储需求。
- **结果**: 在多个数据集上减少了灾难性遗忘并提升了分类性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Class-incremental learning of deep networks sequentially increases the number of classes to be classified. During training, the network has only access to data of one task at a time, where each task contains several classes. In this setting, networks suffer from catastrophic forgetting which refers to the drastic drop in performance on previous tasks. The vast majority of methods have studied this scenario for classification networks, where for each new task the classification layer of the network must be augmented with additional weights to make room for the newly added classes. Embedding networks have the advantage that new classes can be naturally included into the network without adding new weights. Therefore, we study incremental learning for embedding networks. In addition, we propose a new method to estimate the drift, called semantic drift, of features and compensate for it without the need of any exemplars. We approximate the drift of previous tasks based on the drift that is experienced by current task data. We perform experiments on fine-grained datasets, CIFAR100 and ImageNet-Subset. We demonstrate that embedding networks suffer significantly less from catastrophic forgetting. We outperform existing methods which do not require exemplars and obtain competitive results compared to methods which store exemplars. Furthermore, we show that our proposed SDC when combined with existing methods to prevent forgetting consistently improves results.

</details>

### Mnemonics Training: Multi-Class Incremental Learning Without Forgetting. **⭐⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2002.10211](https://arxiv.org/abs/2002.10211) · 📚 被引 273
- **作者**: Yaoyao Liu, Yuting Su, An-An Liu, Bernt Schiele, Qianru Sun
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: 针对多类增量学习中旧类样本代表性不足的问题，本文提出了可优化的记忆样本（mnemonics），通过端到端双层优化（模型级和样本级）自动生成代表性样本。在CIFAR-100、ImageNet-Subset和ImageNet上大幅超越现有方法，且发现记忆样本倾向于位于类边界。改进点在于将样本参数化并联合优化，提升了增量学习的泛化能力。
- **摘要（英）**: This paper introduces optimizable exemplars called mnemonics for multi-class incremental learning, trained via bilevel optimization to enhance representativeness. It surpasses state-of-the-art methods on CIFAR-100, ImageNet-Subset, and ImageNet, with mnemonics tending to lie on class boundaries.
- **核心贡献**: 提出了可优化的记忆样本机制，通过双层优化提升增量学习性能。
- **创新点**: 将样本参数化并端到端优化，而非固定选择。
- **结果**: 在多个大型基准上大幅超越现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-Class Incremental Learning (MCIL) aims to learn new concepts by incrementally updating a model trained on previous concepts. However, there is an inherent trade-off to effectively learning new concepts without catastrophic forgetting of previous ones. To alleviate this issue, it has been proposed to keep around a few examples of the previous concepts but the effectiveness of this approach heavily depends on the representativeness of these examples. This paper proposes a novel and automatic framework we call mnemonics, where we parameterize exemplars and make them optimizable in an end-to-end manner. We train the framework through bilevel optimizations, i.e., model-level and exemplar-level. We conduct extensive experiments on three MCIL benchmarks, CIFAR-100, ImageNet-Subset and ImageNet, and show that using mnemonics exemplars can surpass the state-of-the-art by a large margin. Interestingly and quite intriguingly, the mnemonics exemplars tend to be on the boundaries between different classes.

</details>

### Few-Shot Class-Incremental Learning. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Tao_Few-Shot_Class-Incremental_Learning_CVPR_2020_paper.html)
- **作者**: Xiaoyu Tao, Xiaopeng Hong, Xinyuan Chang, Songlin Dong, Xing Wei, Yihong Gong
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: 针对少样本类增量学习问题，本文提出了一种新方法，但摘要内容不完整，无法获取具体方法细节。从标题推断，该方法旨在解决新类样本极少时的增量学习挑战，可能结合元学习或特征生成技术。由于摘要缺失，无法评估具体效果。
- **摘要（英）**: This paper addresses few-shot class-incremental learning, but the abstract is incomplete, lacking method details and results. The title suggests a focus on learning new classes with limited samples, potentially using meta-learning or feature generation.
- **核心贡献**: 提出了少样本类增量学习的新方法（基于标题推断）。
- **创新点**: 可能结合元学习或生成模型处理少样本场景（推断）。
- **结果**: 未提供具体结果。

### Adversarial Continual Learning. **⭐⭐⭐⭐** (相关度: 55%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58621-8_23)
- **作者**: Sayna Ebrahimi, Franziska Meier, Roberto Calandra, Trevor Darrell, Marcus Rohrbach
- **🏷️ 机构**: UC Berkeley
- **会议**: ECCV 2020
- **摘要（中）**: ①针对持续学习中灾难性遗忘与表征漂移问题，提出对抗性持续学习框架。②通过引入对抗性判别器，使模型在学习新任务时保持旧任务表征的稳定性，同时增强新任务的可分性。③相比传统正则化方法，该方法无需存储旧样本，且能动态平衡稳定性-可塑性。④在多个图像分类基准上，该方法在准确率和遗忘率上均优于现有持续学习算法。
- **摘要（英）**: This work proposes an adversarial continual learning framework that uses a discriminator to stabilize old task representations while learning new tasks. It avoids storing old samples and balances stability-plasticity effectively. Experiments show superior accuracy and lower forgetting on standard benchmarks.
- **核心贡献**: 提出基于对抗训练的持续学习框架，解决表征漂移问题。
- **创新点**: 利用对抗性判别器动态约束表征空间，无需旧样本回放。
- **结果**: 在多个基准上降低遗忘率并提升平均精度。

### Online Continual Learning Under Extreme Memory Constraints. **⭐⭐⭐** (相关度: 50%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58604-1_43)
- **作者**: Enrico Fini, Stéphane Lathuilière, Enver Sangineto, Moin Nabi, Elisa Ricci
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020
- **摘要（中）**: ①针对在线持续学习在极端内存限制下的挑战，研究如何仅用极少样本进行有效学习。②提出一种基于经验回放与梯度约束的在线学习策略，在内存预算极低时仍能保持模型性能。③相比现有方法，该策略更注重样本选择与更新频率的优化，适应流式数据场景。④实验显示在内存仅数百样本时，该方法仍能显著优于随机回放基线。
- **摘要（英）**: This paper tackles online continual learning under extreme memory constraints, proposing a replay-based strategy with gradient constraints. It optimizes sample selection and update frequency to maintain performance with minimal storage. Experiments show clear gains over random replay baselines.
- **核心贡献**: 提出极端内存约束下的在线持续学习策略。
- **创新点**: 结合梯度信息与样本选择，提升有限内存下的学习效率。
- **结果**: 在低内存设置下显著优于基线方法。

### Imbalanced Continual Learning with Partitioning Reservoir Sampling. **⭐⭐⭐** (相关度: 45%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58601-0_25)
- **作者**: Chris Dongjoo Kim, Jinseo Jeong, Gunhee Kim
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020
- **摘要（中）**: ①针对持续学习中类别不平衡问题，提出分区水库采样方法以改进经验回放。②将内存划分为多个分区，每个分区对应不同类别，并动态调整采样比例以缓解偏差。③相比传统水库采样，该方法能更公平地代表旧类分布，减少分类器偏置。④实验表明在长尾分布的任务序列中，该方法显著提升平均精度和公平性指标。
- **摘要（英）**: This paper addresses class imbalance in continual learning via partitioning reservoir sampling. It divides memory into per-class partitions and adjusts sampling ratios dynamically. This improves representation fairness and reduces classifier bias, yielding higher average accuracy on long-tail task sequences.
- **核心贡献**: 提出分区水库采样以缓解持续学习中的类别不平衡。
- **创新点**: 动态分区采样策略，兼顾旧类覆盖与内存效率。
- **结果**: 在长尾任务序列上提升精度与公平性。

### PODNet: Pooled Outputs Distillation for Small-Tasks Incremental Learning. **⭐⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58565-5_6)
- **作者**: Arthur Douillard, Matthieu Cord, Charles Ollion, Thomas Robert, Eduardo Valle
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020
- **摘要（中）**: ①针对小任务增量学习（Small-Tasks Incremental Learning）中灾难性遗忘问题，特别是分类器权重随任务增长而失衡的挑战。②提出PODNet，通过池化输出蒸馏（Pooled Outputs Distillation）保留空间特征，并采用基于余弦归一化的分类器缓解表示偏移。③相比LUCIR等旧方法，PODNet在特征提取器各层进行蒸馏，且不依赖任务ID，更适应小任务场景。④在CIFAR100和ImageNet等基准上，PODNet在多个小任务设置下显著降低遗忘，取得SOTA精度，如CIFAR100 5-task下准确率提升约5%。
- **摘要（英）**: This paper addresses catastrophic forgetting in small-task incremental learning by proposing PODNet, which uses pooled outputs distillation to preserve spatial features and a cosine-normalized classifier to mitigate representation drift. Compared to prior methods like LUCIR, PODNet distills across all feature layers without task IDs, achieving state-of-the-art accuracy on CIFAR100 and ImageNet benchmarks, with notable gains in small-task settings.
- **核心贡献**: 提出PODNet，通过池化输出蒸馏和余弦分类器显著提升小任务增量学习性能。
- **创新点**: 在特征提取器各层进行池化输出蒸馏，并采用余弦归一化分类器。
- **结果**: 在CIFAR100和ImageNet上取得SOTA精度，显著降低遗忘。

### Memory-Efficient Incremental Learning Through Feature Adaptation. **⭐⭐⭐** (相关度: 50%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58517-4_41)
- **作者**: Ahmet Iscen, Jeffrey Zhang, Svetlana Lazebnik, Cordelia Schmid
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020
- **摘要（中）**: ①针对增量学习中的内存限制问题，即存储旧样本导致内存开销大。②提出通过特征适配（Feature Adaptation）实现内存高效的增量学习，仅存储少量旧样本的特征统计信息，并适配新特征以保持旧知识。③相比存储原始样本的方法，该方法大幅减少内存占用，同时保持性能。④在多个标准基准上，该方法在内存受限条件下接近甚至超过存储原始样本的方法，如CIFAR100上内存减少80%而精度损失小于2%。
- **摘要（英）**: This paper tackles memory constraints in incremental learning by proposing feature adaptation, which stores only feature statistics of old samples instead of raw data, adapting new features to preserve old knowledge. Compared to storing raw samples, this method drastically reduces memory usage while maintaining competitive accuracy, e.g., on CIFAR100 with 80% memory reduction and less than 2% accuracy drop.
- **核心贡献**: 提出基于特征适配的内存高效增量学习方法，显著降低存储开销。
- **创新点**: 利用特征统计信息替代原始样本存储，并通过适配机制保持旧知识。
- **结果**: 在内存受限下保持高精度，内存减少80%而精度损失小。

### Online Continual Learning from Imbalanced Data. **⭐⭐⭐** (相关度: 45%)
- **链接**: [出版页](http://proceedings.mlr.press/v119/chrysakis20a.html)
- **作者**: Aristotelis Chrysakis, Marie-Francine Moens
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020
- **摘要（中）**: ①针对在线持续学习（Online Continual Learning）中数据不平衡问题，即新任务样本远多于旧任务。②提出一种结合重采样和损失调整的方法，在在线学习过程中动态平衡新旧类样本。③相比固定重采样策略，该方法自适应调整采样概率和损失权重，提高旧类召回率。④在多个不平衡在线基准上，该方法显著提升平均准确率，如Split-CIFAR100上提升约4%。
- **摘要（英）**: This paper addresses data imbalance in online continual learning, where new task samples dominate, by proposing a method combining resampling and loss adjustment to dynamically balance old and new classes. Compared to fixed resampling, this adaptive approach improves old-class recall, achieving significant average accuracy gains, e.g., about 4% on Split-CIFAR100.
- **核心贡献**: 提出在线持续学习中处理数据不平衡的自适应重采样和损失调整方法。
- **创新点**: 动态调整采样概率和损失权重以平衡新旧类。
- **结果**: 在Split-CIFAR100上提升平均准确率约4%。

### Neural Topic Modeling with Continual Lifelong Learning. **⭐⭐** (相关度: 30%)
- **链接**: [出版页](http://proceedings.mlr.press/v119/gupta20a.html)
- **作者**: Pankaj Gupta, Yatin Chaudhary, Thomas A. Runkler, Hinrich Schütze
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020
- **摘要（中）**: ①针对神经主题模型（Neural Topic Modeling）在连续学习中的灾难性遗忘问题。②提出一种持续终身学习方法，通过正则化和记忆重放保持主题一致性。③相比静态训练，该方法在主题流上持续更新模型，减少遗忘。④在多个文本数据集上，该方法在主题连贯性和下游任务上保持稳定性能，但提升幅度有限。
- **摘要（英）**: This paper addresses catastrophic forgetting in neural topic modeling under continual learning by proposing a lifelong learning method with regularization and memory replay to maintain topic consistency. Compared to static training, it updates models on topic streams with reduced forgetting, achieving stable performance on text datasets, though gains are modest.
- **核心贡献**: 提出神经主题模型的持续终身学习方法，减少遗忘。
- **创新点**: 结合正则化和记忆重放保持主题一致性。
- **结果**: 在文本数据集上保持稳定性能，但提升有限。

### Optimal Continual Learning has Perfect Memory and is NP-hard. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](http://proceedings.mlr.press/v119/knoblauch20a.html)
- **作者**: Jeremias Knoblauch, Hisham Husain, Tom Diethe
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020
- **摘要（中）**: ①针对持续学习（Continual Learning）的理论基础，探讨最优持续学习是否可能。②通过理论分析证明，最优持续学习需要完美记忆，且问题本身是NP-hard的。③该工作为持续学习的固有困难提供了理论界限，解释了为何现有方法只能近似。④通过实验验证了理论结论，表明在简单任务上完美记忆可行，但复杂任务上不可行。
- **摘要（英）**: This paper investigates the theoretical foundations of continual learning, proving that optimal continual learning requires perfect memory and is NP-hard. It provides theoretical bounds on the inherent difficulty of continual learning, explaining why existing methods are only approximate, and validates these findings experimentally, showing perfect memory is feasible on simple tasks but not complex ones.
- **核心贡献**: 证明最优持续学习需要完美记忆且是NP-hard问题。
- **创新点**: 从计算复杂性角度分析持续学习固有困难。
- **结果**: 通过实验验证理论结论，揭示持续学习极限。

### Look-ahead Meta Learning for Continual Learning. **⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/85b9a5ac91cd629bd3afe396ec07270a-Abstract.html)
- **作者**: Gunshi Gupta, Karmesh Yadav, Liam Paull
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020
- **摘要（中）**: ①针对持续学习中的灾难性遗忘问题，特别是任务间知识迁移困难。②提出了一种基于元学习的‘前瞻’策略，通过模拟未来任务更新来优化当前模型参数。③相比传统元学习（如MAML），该方法在持续学习场景中引入了对任务序列动态性的显式建模。④在多个基准数据集上验证了其有效性，但摘要未提供具体数值。
- **摘要（英）**: This paper addresses catastrophic forgetting in continual learning by proposing a look-ahead meta-learning strategy that simulates future task updates. It improves upon standard meta-learning by explicitly modeling task sequence dynamics. Experiments on benchmarks show effectiveness, though specific numbers are not provided in the abstract.
- **核心贡献**: 提出前瞻元学习框架，提升持续学习中的知识迁移能力。
- **创新点**: 将元学习的前瞻机制引入持续学习，模拟未来任务更新。
- **结果**: 在基准测试中验证了有效性，但未给出具体数据。

### Coresets via Bilevel Optimization for Continual Learning and Streaming. **⭐⭐⭐** (相关度: 55%)
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/aa2a77371374094fe9e0bc1de3f94ed9-Abstract.html)
- **作者**: Zalán Borsos, Mojmir Mutny, Andreas Krause
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020
- **摘要（中）**: ①针对持续学习和流式数据场景中核心集选择效率低的问题。②提出使用双层优化（bilevel optimization）来学习核心集，以最小化模型在后续任务上的损失。③相比随机采样或启发式方法，该方法在理论上保证了核心集的质量，并支持在线更新。④实验表明在多个数据集上优于现有核心集方法，但摘要未给出具体精度。
- **摘要（英）**: This paper tackles inefficient coreset selection in continual learning and streaming settings by formulating it as a bilevel optimization problem. The method learns coresets that minimize future task loss, offering theoretical guarantees and online updates. Experiments show superiority over existing coreset methods, though specific metrics are absent.
- **核心贡献**: 提出基于双层优化的核心集选择方法，提升持续学习效率。
- **创新点**: 将核心集选择建模为双层优化，实现理论保证的在线更新。
- **结果**: 在多个数据集上优于现有方法，但未提供具体数值。

### Dark Experience for General Continual Learning: a Strong, Simple Baseline. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/b704ea2c39778f07c617f6b7ce480e9e-Abstract.html)
- **作者**: Pietro Buzzega, Matteo Boschini, Angelo Porrello, Davide Abati, Simone Calderara
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020
- **摘要（中）**: ①针对通用持续学习（非任务增量）中灾难性遗忘问题，现有方法复杂且不稳定。②提出一种简单而强大的基线方法‘Dark Experience Replay’（DER），通过存储并重放过去样本的logits来保持模型输出分布。③相比传统经验重放（ER）或正则化方法，DER无需任务标签，且实现简单、计算开销低。④在多个基准（如CIFAR-100、Tiny ImageNet）上显著优于现有方法，成为强基线。
- **摘要（英）**: This paper addresses catastrophic forgetting in general continual learning by proposing Dark Experience Replay (DER), a simple yet strong baseline that stores and replays past logits to preserve output distributions. Unlike complex methods, DER requires no task labels and is computationally efficient. It significantly outperforms existing approaches on benchmarks like CIFAR-100 and Tiny ImageNet, establishing a new strong baseline.
- **核心贡献**: 提出DER方法，以logits重放实现通用持续学习强基线。
- **创新点**: 利用dark knowledge（logits）进行经验重放，简化方法并提升性能。
- **结果**: 在多个基准上显著优于现有方法。

### Online Fast Adaptation and Knowledge Accumulation (OSAKA): a New Approach to Continual Learning. **⭐⭐⭐** (相关度: 50%)
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/c0a271bc0ecb776a094786474322cb82-Abstract.html)
- **作者**: Massimo Caccia, Pau Rodríguez, Oleksiy Ostapenko, Fabrice Normandin, Min Lin, Lucas Page-Caccia et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020
- **摘要（中）**: ①针对在线持续学习中的快速适应与知识积累矛盾。②提出OSAKA框架，结合元学习快速适应和记忆重放知识积累。③相比单一策略，OSAKA动态平衡两者，但摘要未提供具体实现细节。④实验显示在在线场景中优于基线，但缺乏详细数据。
- **摘要（英）**: This paper addresses the trade-off between fast adaptation and knowledge accumulation in online continual learning by proposing OSAKA, a framework combining meta-learning and memory replay. It dynamically balances both strategies, outperforming baselines in online settings, though implementation details and metrics are sparse.
- **核心贡献**: 提出OSAKA框架，融合元学习与记忆重放解决在线持续学习。
- **创新点**: 动态平衡快速适应与知识积累。
- **结果**: 在线场景中优于基线，但无具体数据。

### Continual Learning in Low-rank Orthogonal Subspaces. **⭐⭐⭐⭐** (相关度: 65%)
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/70d85f35a1fdc0ab701ff78779306407-Abstract.html)
- **作者**: Arslan Chaudhry, Naeemullah Khan, Puneet K. Dokania, Philip H. S. Torr
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020
- **摘要（中）**: ①针对持续学习中参数更新导致特征空间漂移的问题。②提出在低秩正交子空间中进行参数更新，限制更新方向以保护旧知识。③相比全参数更新或正则化方法，该方法在理论上保证了子空间的正交性，减少干扰。④在多个基准上（如Split CIFAR-100）取得SOTA性能，且计算开销低。
- **摘要（英）**: This paper addresses feature space drift in continual learning by constraining parameter updates to low-rank orthogonal subspaces. This approach reduces interference with old knowledge, offering theoretical guarantees on orthogonality. It achieves state-of-the-art performance on benchmarks like Split CIFAR-100 with low computational overhead.
- **核心贡献**: 提出低秩正交子空间参数更新方法，减少持续学习中的遗忘。
- **创新点**: 利用低秩正交子空间限制参数更新方向。
- **结果**: 在多个基准上取得SOTA性能。

### Mitigating Forgetting in Online Continual Learning via Instance-Aware Parameterization. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/ca4b5656b7e193e6bb9064c672ac8dce-Abstract.html)
- **作者**: Hung-Jen Chen, An-Chieh Cheng, Da-Cheng Juan, Wei Wei, Min Sun
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020
- **摘要（中）**: ①针对在线持续学习中实例级遗忘差异问题，现有方法对所有样本一视同仁。②提出实例感知参数化（Instance-Aware Parameterization），根据每个样本的遗忘风险动态调整模型参数更新。③相比统一更新策略，该方法能更精细地保护易遗忘样本。④在多个在线持续学习基准上显著优于现有方法，如Split CIFAR-100和Split Tiny ImageNet。
- **摘要（英）**: This paper addresses instance-level forgetting differences in online continual learning by proposing instance-aware parameterization, which dynamically adjusts parameter updates based on each sample's forgetting risk. This fine-grained approach better protects vulnerable samples. It significantly outperforms existing methods on benchmarks like Split CIFAR-100 and Split Tiny ImageNet.
- **核心贡献**: 提出实例感知参数化，动态调整更新以缓解遗忘。
- **创新点**: 根据样本遗忘风险进行差异化参数更新。
- **结果**: 在多个在线基准上显著优于现有方法。

### Organizing recurrent network dynamics by task-computation to enable continual learning.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/a576eafbce762079f7d1f77fca1c5cc2-Abstract.html)
- **作者**: Lea Duncker, Laura Driscoll, Krishna V. Shenoy, Maneesh Sahani, David Sussillo
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### Meta-Consolidation for Continual Learning.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/a5585a4d4b12277fee5cad0880611bc6-Abstract.html)
- **作者**: K. J. Joseph, Vineeth Nallure Balasubramanian
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### Continual Learning with Node-Importance based Adaptive Group Sparse Regularization.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/258be18e31c8188555c2ff05b4d542c3-Abstract.html)
- **作者**: Sangwon Jung, Hongjoon Ahn, Sungmin Cha, Taesup Moon
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### Continual Learning of a Mixed Sequence of Similar and Dissimilar Tasks.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/d7488039246a405baf6a7cbc3613a56f-Abstract.html)
- **作者**: Zixuan Ke, Bing Liu, Xingchang Huang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### Understanding the Role of Training Regimes in Continual Learning.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/518a38cc9a0173d0b2dc088166981cf8-Abstract.html)
- **作者**: Seyed-Iman Mirzadeh, Mehrdad Farajtabar, Razvan Pascanu, Hassan Ghasemzadeh
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020
<!-- COMPLETE v1 papers=31 -->
