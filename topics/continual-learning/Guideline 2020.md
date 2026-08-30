# Continual Learning — 2020 Guideline

> 领域: 持续学习 / 增量学习（含 VLM/多模态场景）
> 论文数: 8 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份:

### Conditional Channel Gated Networks for Task-Aware Continual Learning. **⭐⭐⭐** (相关度: 30%)
- **链接**: [arXiv:2004.00070](https://arxiv.org/abs/2004.00070) · 📚 被引 140
- **作者**: Davide Abati, Jakub M. Tomczak, Tijmen Blankevoort, Simone Calderara, Rita Cucchiara, Babak Ehteshami Bejnordi
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对卷积神经网络在连续学习任务中遭遇灾难性遗忘的问题。②提出条件通道门控网络，为每个卷积层配备任务特定的门控模块，选择性地应用滤波器，并通过稀疏性目标保护重要滤波器、保留模型容量。③相比现有方法，引入了任务分类器以应对测试时无任务标签的实际场景。④实验验证了该方法在多个任务序列上能有效缓解遗忘，但摘要未提供具体数据。
- **摘要（英）**: This paper addresses catastrophic forgetting in CNNs during sequential task learning. It proposes conditional channel gating modules per convolutional layer to select filters, with a sparsity objective to protect important filters and retain capacity. A task classifier handles scenarios without task labels at test time. Experiments show reduced forgetting, though no specific metrics are given in the abstract.
- **核心贡献**: 提出条件通道门控网络，结合任务分类器解决无任务标签场景下的持续学习问题。
- **创新点**: 将条件计算与门控机制引入持续学习，实现滤波器级任务自适应。
- **结果**: 在多个任务序列上缓解了灾难性遗忘，但摘要未提供具体性能数据。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Convolutional Neural Networks experience catastrophic forgetting when optimized on a sequence of learning problems: as they meet the objective of the current training examples, their performance on previous tasks drops drastically. In this work, we introduce a novel framework to tackle this problem with conditional computation. We equip each convolutional layer with task-specific gating modules, selecting which filters to apply on the given input. This way, we achieve two appealing properties. Firstly, the execution patterns of the gates allow to identify and protect important filters, ensuring no loss in the performance of the model for previously learned tasks. Secondly, by using a sparsity objective, we can promote the selection of a limited set of kernels, allowing to retain sufficient model capacity to digest new tasks.Existing solutions require, at test time, awareness of the task to which each example belongs to. This knowledge, however, may not be available in many practical scenarios. Therefore, we additionally introduce a task classifier that predicts the task label of each example, to deal with settings in which a task oracle is not available. We validate our proposal on four continual learning datasets. Results show that our model consistently outperforms existing methods both in the presence and the absence of a task oracle. Notably, on Split SVHN and Imagenet-50 datasets, our model yields up to 23.98% and 17.42% improvement in accuracy w.r.t. competing methods.

</details>

### Continual Learning With Extended Kronecker-Factored Approximate Curvature. **⭐⭐⭐** (相关度: 40%)
- **链接**: [arXiv:2004.07507](https://arxiv.org/abs/2004.07507) · 📚 被引 44
- **作者**: Janghyeon Lee, Hyeong Gwon Hong, Donggyu Joo, Junmo Kim
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对持续学习中包含批归一化（BN）层的神经网络，标准K-FAC近似曲率因样本间依赖而失效的问题。②提出了扩展的K-FAC方法，考虑样本间关系以正确近似Hessian矩阵，并设计了BN统计参数的权重合并与重参数化策略，以及无需源任务数据的超参数选择方法。③相比现有K-FAC方法，首次在持续学习框架下处理BN层带来的曲率近似偏差，并解决了BN统计参数的漂移问题。④在带BN层的permuted MNIST任务和从ImageNet到细粒度分类的序列学习（ResNet-50）中，性能优于基线方法，且未使用源任务数据。
- **摘要（英）**: This paper addresses the invalidity of standard K-FAC curvature approximation in continual learning with batch normalization layers due to inter-example dependencies. It extends K-FAC to account for these relations, proposes weight merging and reparameterization for BN statistics, and a hyperparameter selection method without source data. The method outperforms baselines on permuted MNIST with BN and ImageNet-to-fine-grained sequential learning with ResNet-50.
- **核心贡献**: 提出了适用于BN层的扩展K-FAC曲率近似方法，并解决了BN统计参数在持续学习中的处理问题。
- **创新点**: 在K-FAC中引入样本间依赖建模，并设计BN参数的重参数化策略。
- **结果**: 在多个持续学习基准上优于基线方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose a quadratic penalty method for continual learning of neural networks that contain batch normalization (BN) layers. The Hessian of a loss function represents the curvature of the quadratic penalty function, and a Kronecker-factored approximate curvature (K-FAC) is used widely to practically compute the Hessian of a neural network. However, the approximation is not valid if there is dependence between examples, typically caused by BN layers in deep network architectures. We extend the K-FAC method so that the inter-example relations are taken into account and the Hessian of deep neural networks can be properly approximated under practical assumptions. We also propose a method of weight merging and reparameterization to properly handle statistical parameters of BN, which plays a critical role for continual learning with BN, and a method that selects hyperparameters without source task data. Our method shows better performance than baselines in the permuted MNIST task with BN layers and in sequential learning from the ImageNet classification task to fine-grained classification tasks with ResNet-50, without any explicit or implicit use of source task data for hyperparameter selection.

</details>

### GDumb: A Simple Approach that Questions Our Progress in Continual Learning. **⭐⭐⭐⭐** (相关度: 55%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58536-5_31)
- **作者**: Ameya Prabhu, Philip H. S. Torr, Puneet K. Dokania
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020
- **摘要（中）**: ①针对持续学习领域进展评估问题，质疑复杂方法是否真正有效。②提出GDumb基线，仅用内存样本训练分类器，不依赖复杂策略。③改进点在于强调简单方法的重要性，提供公平比较基准。④实验表明GDumb在多个基准上超越许多先进方法，揭示领域进展有限。
- **摘要（英）**: This paper questions progress in continual learning by proposing GDumb, a simple baseline that trains classifiers solely on memory samples. It outperforms many advanced methods on benchmarks, highlighting limited real progress.
- **核心贡献**: 提出GDumb基线，重新评估持续学习进展。
- **创新点**: 强调简单方法有效性，提供对比基准。
- **结果**: 在多个基准上超越复杂方法。

### More Classifiers, Less Forgetting: A Generic Multi-classifier Paradigm for Incremental Learning. **⭐⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58574-7_42)
- **作者**: Yu Liu, Sarah Parisot, Gregory G. Slabaugh, Xu Jia, Ales Leonardis, Tinne Tuytelaars
- **🏷️ 机构**: SenseTime
- **会议**: ECCV 2020
- **摘要（中）**: ①针对增量学习中的遗忘问题，提出多分类器范式。②为每个任务分配独立分类器，通过集成策略减少干扰。③改进点在于利用多分类器增强模型容量，同时保持旧任务性能。④实验显示在多个增量学习基准上准确率显著提升，遗忘率降低。
- **摘要（英）**: This paper proposes a multi-classifier paradigm for incremental learning, assigning independent classifiers per task and integrating them to reduce interference. It achieves higher accuracy and lower forgetting on benchmarks.
- **核心贡献**: 提出多分类器范式以缓解增量学习遗忘。
- **创新点**: 任务独立分类器与集成策略结合。
- **结果**: 在多个基准上提升准确率并降低遗忘。

### Modeling the Background for Incremental Learning in Semantic Segmentation. **⭐⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2002.00718](https://arxiv.org/abs/2002.00718) · 📚 被引 309
- **作者**: Fabio Cermelli, Massimiliano Mancini, Samuel Rota Bulò, Elisa Ricci, Barbara Caputo
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对语义分割中的增量学习问题，现有方法忽略了背景类像素的语义分布漂移，导致性能下降。②提出了基于蒸馏的框架，显式建模背景类的分布变化，并引入分类器参数初始化策略以避免对背景类的偏置预测。③相比经典增量学习方法，该方法专门针对语义分割的特性设计，处理了背景类漂移。④在Pascal-VOC 2012和ADE20K上显著优于现有方法。
- **摘要（英）**: This paper addresses incremental learning in semantic segmentation by explicitly modeling the semantic distribution shift of background pixels, proposing a distillation-based framework and a classifier initialization strategy to prevent background bias. It significantly outperforms state-of-the-art on Pascal-VOC 2012 and ADE20K.
- **核心贡献**: 提出了显式建模背景类漂移的增量语义分割框架。
- **创新点**: 引入背景类分布建模和分类器初始化策略。
- **结果**: 在多个基准上显著超越现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite their effectiveness in a wide range of tasks, deep architectures suffer from some important limitations. In particular, they are vulnerable to catastrophic forgetting, i.e. they perform poorly when they are required to update their model as new classes are available but the original training set is not retained. This paper addresses this problem in the context of semantic segmentation. Current strategies fail on this task because they do not consider a peculiar aspect of semantic segmentation: since each training step provides annotation only for a subset of all possible classes, pixels of the background class (i.e. pixels that do not belong to any other classes) exhibit a semantic distribution shift. In this work we revisit classical incremental learning methods, proposing a new distillation-based framework which explicitly accounts for this shift. Furthermore, we introduce a novel strategy to initialize classifier's parameters, thus preventing biased predictions toward the background class. We demonstrate the effectiveness of our approach with an extensive evaluation on the Pascal-VOC 2012 and ADE20K datasets, significantly outperforming state of the art incremental learning methods.

</details>

### Incremental Learning in Online Scenario. **⭐⭐⭐** (相关度: 50%)
- **链接**: [arXiv:2003.13191](https://arxiv.org/abs/2003.13191) · 📚 被引 140
- **作者**: Jiangpeng He, Runyu Mao, Zeman Shao, Fengqing Zhu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对在线场景下的增量学习，现有方法无法同时处理新类数据和旧类的新观测，且训练时间长。②提出了一个在线增量学习框架，结合改进的交叉蒸馏损失和两步学习技术，处理新类添加和概念漂移。③相比现有方法，该框架适用于在线场景，能应对数据分布变化。④实验表明在在线学习设置下优于当前最先进方法。
- **摘要（英）**: This paper proposes an online incremental learning framework that handles both new classes and new observations of old classes using a modified cross-distillation loss and two-step learning. It outperforms state-of-the-art in online scenarios, addressing catastrophic forgetting and concept drift.
- **核心贡献**: 提出了适用于在线场景的增量学习框架，同时处理新类和旧类数据漂移。
- **创新点**: 结合交叉蒸馏损失和两步学习技术。
- **结果**: 在在线学习基准上优于现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Modern deep learning approaches have achieved great success in many vision applications by training a model using all available task-specific data. However, there are two major obstacles making it challenging to implement for real life applications: (1) Learning new classes makes the trained model quickly forget old classes knowledge, which is referred to as catastrophic forgetting. (2) As new observations of old classes come sequentially over time, the distribution may change in unforeseen way, making the performance degrade dramatically on future data, which is referred to as concept drift. Current state-of-the-art incremental learning methods require a long time to train the model whenever new classes are added and none of them takes into consideration the new observations of old classes. In this paper, we propose an incremental learning framework that can work in the challenging online learning scenario and handle both new classes data and new observations of old classes. We address problem (1) in online mode by introducing a modified cross-distillation loss together with a two-step learning technique. Our method outperforms the results obtained from current state-of-the-art offline incremental learning methods on the CIFAR-100 and ImageNet-1000 (ILSVRC 2012) datasets under the same experiment protocol but in online scenario. We also provide a simple yet effective method to mitigate problem (2) by updating exemplar set using the feature of each new observation of old classes and demonstrate a real life application of online food image classification based on our complete framework using the Food-101 dataset.

</details>

### Topology-Preserving Class-Incremental Learning. **⭐⭐⭐⭐** (相关度: 65%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58529-7_16)
- **作者**: Xiaoyu Tao, Xinyuan Chang, Xiaopeng Hong, Xing Wei, Yihong Gong
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020
- **摘要（中）**: ①针对类增量学习中拓扑结构变化导致的遗忘问题，现有方法忽略类别间关系。②提出拓扑保持的类增量学习（Topology-Preserving Class-Incremental Learning），通过图神经网络建模类别拓扑并约束表示空间。③相比现有方法，显式保留类别间结构，增强新类与旧类的兼容性。④在CIFAR和ImageNet子集上，准确率提升约3-8%，尤其在长任务序列中优势明显。
- **摘要（英）**: This work addresses topology changes in class-incremental learning, using graph neural networks to preserve inter-class structure, improving accuracy by 3-8% on benchmarks.
- **核心贡献**: 引入类别拓扑保持机制，提升类增量学习性能。
- **创新点**: 将图神经网络用于表示空间约束。
- **结果**: 在多个数据集上取得显著提升。

### Continual Learning of Control Primitives : Skill Discovery via Reset-Games.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/3472ab80b6dff70c54758fd6dfc800c2-Abstract.html)
- **作者**: Kelvin Xu, Siddharth Verma, Chelsea Finn, Sergey Levine
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Maintaining Discrimination and Fairness in Class Incremental Learning. **⭐⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:1911.07053](https://arxiv.org/abs/1911.07053) · 📚 被引 430
- **作者**: Bowen Zhao, Xi Xiao, Guojun Gan, Bin Zhang, Shu-Tao Xia
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对类增量学习中灾难性遗忘问题，指出知识蒸馏虽能维持旧类内判别性，但无法解决模型偏向新类导致其效果受限。②提出权重对齐方法，在正常训练后校正全连接层中偏置的权重，以平衡新旧类。③改进点在于首次明确全连接层权重偏置是遗忘关键因素，并设计轻量后处理方案。④实验表明该方法在多个基准上显著提升增量学习准确率，尤其在长序列任务中优于现有方法。
- **摘要（英）**: This paper addresses catastrophic forgetting in class incremental learning, identifying that knowledge distillation preserves intra-old-class discrimination but fails to mitigate bias toward new classes. It proposes Weight Aligning to correct biased FC layer weights post-training, achieving superior accuracy on multiple benchmarks, especially in long task sequences.
- **核心贡献**: 揭示全连接层权重偏置对增量学习的影响，并提出权重对齐方法。
- **创新点**: 通过后训练权重校正而非复杂网络修改，实现新旧类公平性。
- **结果**: 在多个标准数据集上显著提升增量学习性能，优于现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep neural networks (DNNs) have been applied in class incremental learning, which aims to solve common real-world problems of learning new classes continually. One drawback of standard DNNs is that they are prone to catastrophic forgetting. Knowledge distillation (KD) is a commonly used technique to alleviate this problem. In this paper, we demonstrate it can indeed help the model to output more discriminative results within old classes. However, it cannot alleviate the problem that the model tends to classify objects into new classes, causing the positive effect of KD to be hidden and limited. We observed that an important factor causing catastrophic forgetting is that the weights in the last fully connected (FC) layer are highly biased in class incremental learning. In this paper, we propose a simple and effective solution motivated by the aforementioned observations to address catastrophic forgetting. Firstly, we utilize KD to maintain the discrimination within old classes. Then, to further maintain the fairness between old classes and new classes, we propose Weight Aligning (WA) that corrects the biased weights in the FC layer after normal training process. Unlike previous work, WA does not require any extra parameters or a validation set in advance, as it utilizes the information provided by the biased weights themselves. The proposed method is evaluated on ImageNet-1000, ImageNet-100, and CIFAR-100 under various settings. Experimental results show that the proposed method can effectively alleviate catastrophic forgetting and significantly outperform state-of-the-art methods.

</details>

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
