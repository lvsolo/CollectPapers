# Continual Learning — 2022 Guideline

> 领域: 持续学习 / 增量学习（含 VLM/多模态场景）
> 论文数: 16 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: [2024](Guideline%202024.md)

### Few-Shot Class-Incremental Learning for 3D Point Cloud Objects. **⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2205.15225](https://arxiv.org/abs/2205.15225)
- **作者**: Townim F. Chowdhury, Ali Cheraghian, Sameera Ramasinghe, Sahar Ahmadi, Morteza Saberi, Shafin Rahman
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对3D点云上的少样本类增量学习问题，该论文指出在真实场景中基类多为合成数据而新类仅有少量真实扫描样本，导致合成到真实的数据分布差异加剧灾难性遗忘和过拟合。方法提出Microshapes，即用预定义的正交基向量规则描述任意3D对象，以支持少样本增量训练并减小合成到真实的数据变化。实验表明该方法在后续增量步骤中能缓解性能下降，但摘要未提供具体数值。
- **摘要（英）**: This paper addresses few-shot class-incremental learning for 3D point clouds, focusing on the synthetic-to-real domain gap between base and novel classes. It proposes Microshapes, orthogonal basis vectors that describe 3D objects via predefined rules, to enable incremental training with few examples while mitigating distribution shift. The method reduces performance degradation in later incremental steps, though no quantitative results are reported in the abstract.
- **核心贡献**: 提出Microshapes方法解决3D点云少样本类增量学习中的合成到真实分布差异问题。
- **创新点**: 利用正交基向量规则描述3D对象，实现少样本增量训练并减小域差异。
- **结果**: 在后续增量步骤中缓解性能下降，但未提供具体数据。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Few-shot class-incremental learning (FSCIL) aims to incrementally fine-tune a model (trained on base classes) for a novel set of classes using a few examples without forgetting the previous training. Recent efforts address this problem primarily on 2D images. However, due to the advancement of camera technology, 3D point cloud data has become more available than ever, which warrants considering FSCIL on 3D data. This paper addresses FSCIL in the 3D domain. In addition to well-known issues of catastrophic forgetting of past knowledge and overfitting of few-shot data, 3D FSCIL can bring newer challenges. For example, base classes may contain many synthetic instances in a realistic scenario. In contrast, only a few real-scanned samples (from RGBD sensors) of novel classes are available in incremental steps. Due to the data variation from synthetic to real, FSCIL endures additional challenges, degrading performance in later incremental steps. We attempt to solve this problem using Microshapes (orthogonal basis vectors) by describing any 3D objects using a pre-defined set of rules. It supports incremental training with few-shot examples minimizing synthetic to real data variation. We propose new test protocols for 3D FSCIL using popular synthetic datasets (ModelNet and ShapeNet) and 3D real-scanned datasets (ScanObjectNN and CO3D). By comparing state-of-the-art methods, we establish the effectiveness of our approach in the 3D domain.

</details>

### Generative Negative Text Replay for Continual Vision-Language Pretraining. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2210.17322](https://arxiv.org/abs/2210.17322)
- **作者**: Shipeng Yan, Lanqing Hong, Hang Xu, Jianhua Han, Tinne Tuytelaars, Zhenguo Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对视觉-语言预训练（VLP）在流式数据下遭遇灾难性遗忘的问题。②提出生成式负文本回放（GNTR）方法，利用记忆中的图像生成硬负样本文本，增强对比学习的负样本多样性；同时提出多模态知识蒸馏，对齐新旧模型的实例级预测。③相比传统回放，生成式负样本更有效保留旧知识，且蒸馏损失提升跨模态一致性。④在Conceptual Caption数据集上的实例和类增量分割上评估，结果显示优于现有持续学习方法，但摘要未给出具体数值。
- **摘要（英）**: This paper addresses catastrophic forgetting in continual vision-language pretraining by proposing generative negative text replay (GNTR), which synthesizes hard negative texts from memory images, and multi-modal knowledge distillation to align predictions. This improves negative sample diversity and preserves learned knowledge. Experiments on Conceptual Caption splits show superior performance over existing methods, though specific numbers are not provided.
- **核心贡献**: 提出生成式负文本回放和知识蒸馏的持续视觉-语言预训练方法。
- **创新点**: 利用生成硬负样本增强回放效果。
- **结果**: 在持续学习基准上优于现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-language pre-training (VLP) has attracted increasing attention recently. With a large amount of image-text pairs, VLP models trained with contrastive loss have achieved impressive performance in various tasks, especially the zero-shot generalization on downstream datasets. In practical applications, however, massive data are usually collected in a streaming fashion, requiring VLP models to continuously integrate novel knowledge from incoming data and retain learned knowledge. In this work, we focus on learning a VLP model with sequential chunks of image-text pair data. To tackle the catastrophic forgetting issue in this multi-modal continual learning setting, we first introduce pseudo text replay that generates hard negative texts conditioned on the training images in memory, which not only better preserves learned knowledge but also improves the diversity of negative samples in the contrastive loss. Moreover, we propose multi-modal knowledge distillation between images and texts to align the instance-wise prediction between old and new models. We incrementally pre-train our model on both the instance and class incremental splits of the Conceptual Caption dataset, and evaluate the model on zero-shot image classification and image-text retrieval tasks. Our method consistently outperforms the existing baselines with a large margin, which demonstrates its superiority. Notably, we realize an average performance boost of $4.60\%$ on image-classification downstream datasets for the class incremental split.

</details>

### Online Continual Learning with Contrastive Vision Transformer. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2207.13516](https://arxiv.org/abs/2207.13516) · 📚 被引 30
- **作者**: Zhen Wang, Liu Liu, Yajing Kong, Jiaxian Guo, Dacheng Tao
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对在线持续学习（online CL）中灾难性遗忘与稳定性-可塑性平衡问题，提出基于对比视觉Transformer（CVT）的框架。方法包括：设计外部注意力机制隐式捕获先前任务信息，为每个类别引入可学习的焦点（focuses）以累积类别知识，并基于此设计焦点对比损失（focal contrastive loss）来重平衡新旧类别的对比学习，同时采用双分类器结构解耦当前类别学习与所有已见类别平衡。实验表明，该方法在在线CL基准上以更少参数达到最先进性能，有效缓解遗忘。
- **摘要（英）**: This paper addresses catastrophic forgetting and stability-plasticity trade-off in online continual learning by proposing a Contrastive Vision Transformer (CVT) framework. It introduces an external attention mechanism for implicit past-task information capture, learnable class-wise focuses for knowledge accumulation, a focal contrastive loss to rebalance new and past classes, and a dual-classifier structure for decoupling current and balanced learning. Extensive experiments show state-of-the-art performance with fewer parameters on online CL benchmarks.
- **核心贡献**: 提出CVT框架，通过焦点对比学习与外部注意力机制提升在线持续学习性能。
- **创新点**: 设计可学习类别焦点与焦点对比损失，实现新旧类别知识的动态平衡。
- **结果**: 在在线CL基准上以更少参数取得最先进性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Online continual learning (online CL) studies the problem of learning sequential tasks from an online data stream without task boundaries, aiming to adapt to new data while alleviating catastrophic forgetting on the past tasks. This paper proposes a framework Contrastive Vision Transformer (CVT), which designs a focal contrastive learning strategy based on a transformer architecture, to achieve a better stability-plasticity trade-off for online CL. Specifically, we design a new external attention mechanism for online CL that implicitly captures previous tasks' information. Besides, CVT contains learnable focuses for each class, which could accumulate the knowledge of previous classes to alleviate forgetting. Based on the learnable focuses, we design a focal contrastive loss to rebalance contrastive learning between new and past classes and consolidate previously learned representations. Moreover, CVT contains a dual-classifier structure for decoupling learning current classes and balancing all observed classes. The extensive experimental results show that our approach achieves state-of-the-art performance with even fewer parameters on online CL benchmarks and effectively alleviates the catastrophic forgetting.

</details>

### S3C: Self-Supervised Stochastic Classifiers for Few-Shot Class-Incremental Learning. **⭐⭐⭐⭐** (相关度: 65%)
- **链接**: [arXiv:2307.02246](https://arxiv.org/abs/2307.02246) · 📚 被引 45
- **作者**: Jayateja Kalla, Soma Biswas
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对小样本类增量学习（FSCIL）中因数据稀缺导致的新类过拟合和旧类灾难性遗忘问题，提出自监督随机分类器（S3C）框架。方法通过引入分类器权重（类原型）的随机性，缓解新类样本不足和旧类样本缺失的负面影响，并利用自监督组件学习基类中可泛化到未来未见类的特征，从而减少遗忘。在三个基准数据集上的多指标评估验证了有效性，并额外测试了两种现实场景。
- **摘要（英）**: This paper tackles over-fitting on new classes and catastrophic forgetting in few-shot class-incremental learning (FSCIL) by proposing a self-supervised stochastic classifier (S3C). The stochasticity of classifier weights mitigates data scarcity effects, while self-supervision learns generalizable features from base classes to reduce forgetting. Extensive evaluation on three benchmarks and two realistic scenarios demonstrates effectiveness.
- **核心贡献**: 提出S3C框架，利用随机分类器权重和自监督学习应对FSCIL中的双重挑战。
- **创新点**: 将分类器权重的随机性引入FSCIL，以缓解数据稀缺和样本缺失问题。
- **结果**: 在三个基准数据集上验证了有效性，并扩展至现实场景。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Few-shot class-incremental learning (FSCIL) aims to learn progressively about new classes with very few labeled samples, without forgetting the knowledge of already learnt classes. FSCIL suffers from two major challenges: (i) over-fitting on the new classes due to limited amount of data, (ii) catastrophically forgetting about the old classes due to unavailability of data from these classes in the incremental stages. In this work, we propose a self-supervised stochastic classifier (S3C) to counter both these challenges in FSCIL. The stochasticity of the classifier weights (or class prototypes) not only mitigates the adverse effect of absence of large number of samples of the new classes, but also the absence of samples from previously learnt classes during the incremental steps. This is complemented by the self-supervision component, which helps to learn features from the base classes which generalize well to unseen classes that are encountered in future, thus reducing catastrophic forgetting. Extensive evaluation on three benchmark datasets using multiple evaluation metrics show the effectiveness of the proposed framework. We also experiment on two additional realistic scenarios of FSCIL, namely where the number of annotated data available for each of the new classes can be different, and also where the number of base classes is much lesser, and show that the proposed S3C performs significantly better than the state-of-the-art for all these challenging scenarios.

</details>

### DualPrompt: Complementary Prompting for Rehearsal-Free Continual Learning. **⭐⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2204.04799](https://arxiv.org/abs/2204.04799) · 📚 被引 421
- **作者**: Zifeng Wang, Zizhao Zhang, Sayna Ebrahimi, Ruoxi Sun, Han Zhang, Chen-Yu Lee et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对无回放持续学习中因隐私和内存限制无法存储旧样本的问题，提出DualPrompt框架，通过学习一组极小的提示参数（prompts）来指导预训练模型顺序学习任务，无需缓冲过去样本。方法将互补提示附加到预训练骨干网络，并将目标形式化为学习任务不变和任务特定的“指令”。在类增量设置下持续取得最先进性能，尤其优于使用较大缓冲区的先进方法，并引入更具挑战性的Split ImageNet-R基准。
- **摘要（英）**: This paper addresses rehearsal-free continual learning by proposing DualPrompt, which learns tiny prompt parameters to instruct a pre-trained model on sequential tasks without buffering past examples. It attaches complementary prompts to the backbone and formulates the objective as learning task-invariant and task-specific instructions. Extensive validation shows state-of-the-art performance in class-incremental settings, outperforming methods with larger buffers, and introduces the Split ImageNet-R benchmark.
- **核心贡献**: 提出DualPrompt框架，通过互补提示实现无回放持续学习，并引入新基准。
- **创新点**: 利用任务不变和任务特定提示的互补设计，高效指导预训练模型。
- **结果**: 在类增量设置下超越带大缓冲区的方法，取得最先进性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning aims to enable a single model to learn a sequence of tasks without catastrophic forgetting. Top-performing methods usually require a rehearsal buffer to store past pristine examples for experience replay, which, however, limits their practical value due to privacy and memory constraints. In this work, we present a simple yet effective framework, DualPrompt, which learns a tiny set of parameters, called prompts, to properly instruct a pre-trained model to learn tasks arriving sequentially without buffering past examples. DualPrompt presents a novel approach to attach complementary prompts to the pre-trained backbone, and then formulates the objective as learning task-invariant and task-specific "instructions". With extensive experimental validation, DualPrompt consistently sets state-of-the-art performance under the challenging class-incremental setting. In particular, DualPrompt outperforms recent advanced continual learning methods with relatively large buffer sizes. We also introduce a more challenging benchmark, Split ImageNet-R, to help generalize rehearsal-free continual learning research. Source code is available at https://github.com/google-research/l2p.

</details>

### Theoretical Understanding of the Information Flow on Continual Learning Performance. **⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2204.12010](https://arxiv.org/abs/2204.12010) · 📚 被引 4
- **作者**: Joshua Andle, Salimeh Yasaei Sekeh
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对持续学习中缺乏对神经网络学习新任务时行为理论理解的问题，建立概率框架分析任务序列中网络层间信息流及其对学习性能的影响。目标是优化学习新任务时层间信息保留，以管理任务特定知识传递并保持旧任务性能。该工作从理论角度研究CL性能退化，弥补了经验研究之外的不足。
- **摘要（英）**: This paper addresses the lack of theoretical understanding in continual learning by establishing a probabilistic framework to analyze information flow through layers for task sequences. It aims to optimize information preservation between layers while learning new tasks to manage task-specific knowledge and maintain previous task performance. This work provides theoretical insights into CL performance degradation.
- **核心贡献**: 建立概率框架分析持续学习中的信息流，优化层间信息保留。
- **创新点**: 从理论角度建模信息流与CL性能的关系。
- **结果**: 提供了理论分析，但未报告具体实验数据。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning (CL) is a setting in which an agent has to learn from an incoming stream of data sequentially. CL performance evaluates the model's ability to continually learn and solve new problems with incremental available information over time while retaining previous knowledge. Despite the numerous previous solutions to bypass the catastrophic forgetting (CF) of previously seen tasks during the learning process, most of them still suffer significant forgetting, expensive memory cost, or lack of theoretical understanding of neural networks' conduct while learning new tasks. While the issue that CL performance degrades under different training regimes has been extensively studied empirically, insufficient attention has been paid from a theoretical angle. In this paper, we establish a probabilistic framework to analyze information flow through layers in networks for task sequences and its impact on learning performance. Our objective is to optimize the information preservation between layers while learning new tasks to manage task-specific knowledge passing throughout the layers while maintaining model performance on previous tasks. In particular, we study CL performance's relationship with information flow in the network to answer the question "How can knowledge of information flow between layers be used to alleviate CF?". Our analysis provides novel insights of information adaptation within the layers during the incremental task learning process. Through our experiments, we provide empirical evidence and practically highlight the performance improvement across multiple tasks.

</details>

### Helpful or Harmful: Inter-task Association in Continual Learning. **⭐⭐** (相关度: 50%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20083-0_31) · 📚 被引 18
- **作者**: Hyundong Jin, Eunwoo Kim
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 该论文摘要为空，无法获取具体内容。根据标题推测，可能研究持续学习中任务间关联（inter-task association）对学习的影响，但缺乏详细信息。
- **摘要（英）**: The abstract is empty, so no specific content is available. Based on the title, it likely investigates the impact of inter-task association in continual learning, but details are missing.
- **核心贡献**: 未知，因摘要缺失。
- **创新点**: 未知，因摘要缺失。
- **结果**: 未知，因摘要缺失。

### Balancing Stability and Plasticity Through Advanced Null Space in Continual Learning. **⭐⭐⭐** (相关度: 55%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19809-0_13) · 📚 被引 25
- **作者**: Yajing Kong, Liu Liu, Zhen Wang, Dacheng Tao
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对持续学习中稳定性与可塑性平衡问题，提出基于高级零空间（Advanced Null Space）的方法。该方法可能通过投影或约束机制，在保留旧任务知识的同时学习新任务，但摘要未提供具体细节。
- **摘要（英）**: This paper addresses the stability-plasticity dilemma in continual learning by proposing an advanced null space-based method. It likely uses projection or constraint mechanisms to preserve old task knowledge while learning new tasks, but details are not provided in the abstract.
- **核心贡献**: 提出基于高级零空间的持续学习方法，以平衡稳定性与可塑性。
- **创新点**: 利用零空间理论实现任务知识保留。
- **结果**: 未报告具体结果。

### Online Task-free Continual Learning with Dynamic Sparse Distributed Memory. **⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19806-9_42) · 📚 被引 12
- **作者**: Julien Pourcel, Ngoc-Son Vu, Robert M. French
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对在线无任务持续学习中的灾难性遗忘问题。②提出动态稀疏分布式记忆（DSDM）机制，结合稀疏编码和记忆重放来存储和检索旧知识。③相比传统重放方法，DSDM 更高效且无需任务边界信息。④实验表明在多个基准上有效缓解遗忘，但摘要未提供具体数据。
- **摘要（英）**: This paper addresses catastrophic forgetting in online task-free continual learning by proposing a Dynamic Sparse Distributed Memory (DSDM) that combines sparse coding and memory replay. It improves efficiency over traditional replay methods without requiring task boundaries. Experiments show reduced forgetting on benchmarks, though specific metrics are not detailed in the abstract.
- **核心贡献**: 提出动态稀疏分布式记忆机制用于在线无任务持续学习。
- **创新点**: 将稀疏分布式记忆与动态更新策略结合，实现无需任务边界的知识存储与回放。
- **结果**: 在多个基准上有效缓解遗忘，但未提供具体数值。

### DLCFT: Deep Linear Continual Fine-Tuning for General Incremental Learning. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2208.08112](https://arxiv.org/abs/2208.08112) · 📚 被引 15
- **作者**: Hyounguk Shon, Janghyeon Lee, Seung Hwan Kim, Junmo Kim
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对预训练模型在持续微调中的灾难性遗忘问题。②提出深度线性持续微调（DLCFT）方法，利用预训练网络的线性化技术设计线性模型，并采用二次参数正则化作为最优策略。③相比传统 EWC 等方法，DLCFT 能应用于类增量场景，并从理论上解释了 EWC 在交叉熵损失下失效的原因。④实验表明在图像分类任务上能有效防止遗忘并保持高性能。
- **摘要（英）**: This paper tackles catastrophic forgetting in continual fine-tuning of pre-trained models by proposing Deep Linear Continual Fine-Tuning (DLCFT), which linearizes the pre-trained network and applies quadratic parameter regularization as an optimal policy. It extends regularization methods to class-incremental learning and provides theoretical insights into EWC's underperformance. Experiments on image classification demonstrate reduced forgetting and high performance.
- **核心贡献**: 提出基于线性化预训练网络的持续微调框架，并理论解释现有正则化方法的局限。
- **创新点**: 利用网络线性化技术将参数正则化方法适配到类增量学习。
- **结果**: 在图像分类任务上有效防止遗忘并保持高性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pre-trained representation is one of the key elements in the success of modern deep learning. However, existing works on continual learning methods have mostly focused on learning models incrementally from scratch. In this paper, we explore an alternative framework to incremental learning where we continually fine-tune the model from a pre-trained representation. Our method takes advantage of linearization technique of a pre-trained neural network for simple and effective continual learning. We show that this allows us to design a linear model where quadratic parameter regularization method is placed as the optimal continual learning policy, and at the same time enjoying the high performance of neural networks. We also show that the proposed algorithm enables parameter regularization methods to be applied to class-incremental problems. Additionally, we provide a theoretical reason why the existing parameter-space regularization algorithms such as EWC underperform on neural networks trained with cross-entropy loss. We show that the proposed method can prevent forgetting while achieving high continual fine-tuning performance on image classification tasks. To show that our method can be applied to general continual learning settings, we evaluate our method in data-incremental, task-incremental, and class-incremental learning problems.

</details>

### R-DFCIL: Relation-Guided Representation Learning for Data-Free Class Incremental Learning. **⭐⭐⭐⭐** (相关度: 65%)
- **链接**: [arXiv:2203.13104](https://arxiv.org/abs/2203.13104)
- **作者**: Qiankun Gao, Chen Zhao, Bernard Ghanem, Jian Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对无数据类增量学习（DFCIL）中合成数据与真实数据域差距导致的遗忘问题。②提出关系引导表示学习（RRL），通过关系知识蒸馏传递新数据的结构关系，并采用局部分类损失避免表示与分类器学习的干扰。③相比现有 DFCIL 方法，RRL 能更好地兼容新旧类表示，减少遗忘并提升可塑性。④实验表明在多个基准上显著降低遗忘，但摘要未给出具体数值。
- **摘要（英）**: This paper addresses the domain gap between synthetic and real data in data-free class-incremental learning (DFCIL) by proposing relation-guided representation learning (RRL), which uses relational knowledge distillation to transfer structural relations and local classification loss to avoid interference. It improves compatibility between old and new class representations, reducing forgetting and enhancing plasticity. Experiments show significant forgetting reduction on benchmarks.
- **核心贡献**: 提出关系引导表示学习框架，缓解无数据类增量学习中的域差距问题。
- **创新点**: 引入关系知识蒸馏和局部分类损失，优化表示学习与分类器训练的平衡。
- **结果**: 在多个基准上显著降低遗忘并提升新类学习能力。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Class-Incremental Learning (CIL) struggles with catastrophic forgetting when learning new knowledge, and Data-Free CIL (DFCIL) is even more challenging without access to the training data of previously learned classes. Though recent DFCIL works introduce techniques such as model inversion to synthesize data for previous classes, they fail to overcome forgetting due to the severe domain gap between the synthetic and real data. To address this issue, this paper proposes relation-guided representation learning (RRL) for DFCIL, dubbed R-DFCIL. In RRL, we introduce relational knowledge distillation to flexibly transfer the structural relation of new data from the old model to the current model. Our RRL-boosted DFCIL can guide the current model to learn representations of new classes better compatible with representations of previous classes, which greatly reduces forgetting while improving plasticity. To avoid the mutual interference between representation and classifier learning, we employ local rather than global classification loss during RRL. After RRL, the classification head is refined with global class-balanced classification loss to address the data imbalance issue as well as learn the decision boundaries between new and previous classes. Extensive experiments on CIFAR100, Tiny-ImageNet200, and ImageNet100 demonstrate that our R-DFCIL significantly surpasses previous approaches and achieves a new state-of-the-art performance for DFCIL. Code is available at https://github.com/jianzhangcs/R-DFCIL

</details>

### Class-Incremental Learning with Cross-Space Clustering and Controlled Transfer. **⭐⭐⭐⭐** (相关度: 65%)
- **链接**: [arXiv:2208.03767](https://arxiv.org/abs/2208.03767) · 📚 被引 31
- **作者**: Arjun Ashok, K. J. Joseph, Vineeth N. Balasubramanian
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对类增量学习中保持旧类表示和适应新类之间的平衡问题。②提出跨空间聚类（CSC）和受控迁移（CT）两个蒸馏目标，利用特征空间结构指导优化方向，促进类内聚类和类间分离。③相比传统蒸馏方法，CSC 通过群体免疫效应增强旧类抗遗忘能力，CT 控制新类学习迁移。④实验表明在多个基准上提升准确率，但摘要未提供具体数据。
- **摘要（英）**: This paper addresses the balance between preserving old class representations and adapting to new classes in class-incremental learning by proposing cross-space clustering (CSC) and controlled transfer (CT) distillation objectives. CSC leverages feature space structure to guide optimization directions, promoting intra-class clustering and herd immunity, while CT controls transfer for new classes. Experiments show accuracy improvements on benchmarks.
- **核心贡献**: 提出跨空间聚类和受控迁移的蒸馏方法，增强类增量学习的稳定性与可塑性。
- **创新点**: 利用特征空间结构定义优化方向，实现群体免疫式抗遗忘。
- **结果**: 在多个基准上提升类增量学习准确率。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In class-incremental learning, the model is expected to learn new classes continually while maintaining knowledge on previous classes. The challenge here lies in preserving the model's ability to effectively represent prior classes in the feature space, while adapting it to represent incoming new classes. We propose two distillation-based objectives for class incremental learning that leverage the structure of the feature space to maintain accuracy on previous classes, as well as enable learning the new classes. In our first objective, termed cross-space clustering (CSC), we propose to use the feature space structure of the previous model to characterize directions of optimization that maximally preserve the class: directions that all instances of a specific class should collectively optimize towards, and those that they should collectively optimize away from. Apart from minimizing forgetting, this indirectly encourages the model to cluster all instances of a class in the current feature space, and gives rise to a sense of herd-immunity, allowing all samples of a class to jointly combat the model from forgetting the class. Our second objective termed controlled transfer (CT) tackles incremental learning from an understudied perspective of inter-class transfer. CT explicitly approximates and conditions the current model on the semantic similarities between incrementally arriving classes and prior classes. This allows the model to learn classes in such a way that it maximizes positive forward transfer from similar prior classes, thus increasing plasticity, and minimizes negative backward transfer on dissimilar prior classes, whereby strengthening stability. We perform extensive experiments on two benchmark datasets, adding our method (CSCCT) on top of three prominent class-incremental learning methods. We observe consistent performance improvement on a variety of experimental settings.

</details>

### Few-Shot Class-Incremental Learning via Entropy-Regularized Data-Free Replay. **⭐⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2207.11213](https://arxiv.org/abs/2207.11213)
- **作者**: Huan Liu, Li Gu, Zhixiang Chi, Yang Wang, Yuanhao Yu, Jun Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对少样本类增量学习（FSCIL）中数据重放的有效性和隐私问题。②提出熵正则化数据自由重放方法，通过生成器合成数据，并施加熵正则化鼓励生成不确定样本，同时采用 one-hot 标签重标记以简化损失函数。③相比传统知识蒸馏方法，该方法避免了多目标平衡问题，并解决了隐私顾虑。④实验表明数据重放在 FSCIL 中有效，且方法在多个基准上表现优异，但摘要未给出具体数值。
- **摘要（英）**: This paper addresses the effectiveness and privacy concerns of data replay in few-shot class-incremental learning (FSCIL) by proposing entropy-regularized data-free replay, which synthesizes data with a generator and encourages uncertain samples via entropy regularization, using one-hot-like labels to simplify training. It mitigates multi-objective balancing issues and privacy risks. Experiments show replay is effective and the method performs well on benchmarks.
- **核心贡献**: 提出熵正则化数据自由重放方法，验证重放在 FSCIL 中的有效性并解决隐私问题。
- **创新点**: 通过熵正则化生成不确定样本和 one-hot 重标记，简化训练目标。
- **结果**: 在多个基准上表现优异，但未提供具体数值。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Few-shot class-incremental learning (FSCIL) has been proposed aiming to enable a deep learning system to incrementally learn new classes with limited data. Recently, a pioneer claims that the commonly used replay-based method in class-incremental learning (CIL) is ineffective and thus not preferred for FSCIL. This has, if truth, a significant influence on the fields of FSCIL. In this paper, we show through empirical results that adopting the data replay is surprisingly favorable. However, storing and replaying old data can lead to a privacy concern. To address this issue, we alternatively propose using data-free replay that can synthesize data by a generator without accessing real data. In observing the the effectiveness of uncertain data for knowledge distillation, we impose entropy regularization in the generator training to encourage more uncertain examples. Moreover, we propose to relabel the generated data with one-hot-like labels. This modification allows the network to learn by solely minimizing the cross-entropy loss, which mitigates the problem of balancing different objectives in the conventional knowledge distillation approach. Finally, we show extensive experimental results and analysis on CIFAR-100, miniImageNet and CUB-200 to demonstrate the effectiveness of our proposed one.

</details>

### Long-Tailed Class Incremental Learning. **⭐⭐** (相关度: 50%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19827-4_29)
- **作者**: Xialei Liu, Yusong Hu, Xu-Sheng Cao, Andrew D. Bagdanov, Ke Li, Ming-Ming Cheng
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①该论文标题为长尾类增量学习，但摘要为空，无法获取具体问题、方法、改进和效果信息。②可能针对长尾分布下的类增量学习挑战，但缺乏细节。③无法评估与现有工作的差异。④无实验数据。
- **摘要（英）**: This paper is titled 'Long-Tailed Class Incremental Learning' but the abstract is empty, so no details on problem, method, improvements, or results are available. It likely addresses challenges of class-incremental learning under long-tailed distributions, but cannot be assessed.
- **核心贡献**: 未知，因摘要为空。
- **创新点**: 未知，因摘要为空。
- **结果**: 未知，因摘要为空。

### Few-Shot Class-Incremental Learning from an Open-Set Perspective. **⭐⭐⭐** (相关度: 75%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19806-9_22)
- **作者**: Can Peng, Kun Zhao, Tianren Wang, Meng Li, Brian C. Lovell
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对小样本类增量学习中，新类样本有限且存在未知类干扰的问题，从开放集视角重新审视。②方法可能通过引入开放集识别机制，区分已知类和新类，并处理增量学习中的漂移。③相比传统类增量方法，更关注未知类的影响，提升鲁棒性。④摘要未提供具体数据，但预期在标准基准上改善小样本增量性能。
- **摘要（英）**: This paper rethinks few-shot class-incremental learning from an open-set perspective, addressing limited new-class samples and unknown-class interference. It likely introduces open-set recognition to distinguish known and novel classes, mitigating drift. Specific results are not provided, but improvements on benchmarks are expected.
- **核心贡献**: 将开放集视角引入小样本类增量学习，增强未知类处理能力。
- **创新点**: 结合开放集识别与增量学习，提升小样本场景鲁棒性。
- **结果**: 预期改善小样本增量性能，但具体数据未给出。

### FOSTER: Feature Boosting and Compression for Class-Incremental Learning. **⭐⭐⭐⭐** (相关度: 50%)
- **链接**: [arXiv:2204.04662](https://arxiv.org/abs/2204.04662) · 📚 被引 294
- **作者**: Fu-Yun Wang, Da-Wei Zhou, Han-Jia Ye, De-Chuan Zhan
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对深度神经网络在学习新类别时遭受灾难性遗忘的问题，提出了FOSTER两阶段学习范式。该方法受梯度提升算法启发，首先动态扩展新模块以拟合目标与原始模型输出之间的残差，然后通过有效的蒸馏策略移除冗余参数和特征维度，以维持单骨干网络。在CIFAR-100和ImageNet-100/1000上的实验表明，该方法在不同设置下均达到最先进性能。
- **摘要（英）**: To address catastrophic forgetting in continual learning, this paper proposes FOSTER, a two-stage paradigm inspired by gradient boosting. It first expands new modules to fit residuals between target and original model output, then removes redundant parameters via distillation to maintain a single backbone. Experiments on CIFAR-100 and ImageNet show state-of-the-art performance.
- **核心贡献**: 提出基于梯度提升的两阶段类增量学习方法，显著缓解灾难性遗忘。
- **创新点**: 动态扩展与压缩结合，实现自适应学习新类别并保持模型紧凑。
- **结果**: 在多个基准数据集上达到最先进性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The ability to learn new concepts continually is necessary in this ever-changing world. However, deep neural networks suffer from catastrophic forgetting when learning new categories. Many works have been proposed to alleviate this phenomenon, whereas most of them either fall into the stability-plasticity dilemma or take too much computation or storage overhead. Inspired by the gradient boosting algorithm to gradually fit the residuals between the target model and the previous ensemble model, we propose a novel two-stage learning paradigm FOSTER, empowering the model to learn new categories adaptively. Specifically, we first dynamically expand new modules to fit the residuals between the target and the output of the original model. Next, we remove redundant parameters and feature dimensions through an effective distillation strategy to maintain the single backbone model. We validate our method FOSTER on CIFAR-100 and ImageNet-100/1000 under different settings. Experimental results show that our method achieves state-of-the-art performance. Code is available at: https://github.com/G-U-N/ECCV22-FOSTER.

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
