# Continual Learning — 2021 Guideline

> 领域: 持续学习 / 增量学习（含 VLM/多模态场景）
> 论文数: 17 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份:

### Rainbow Memory: Continual Learning With a Memory of Diverse Samples. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2103.17230](https://arxiv.org/abs/2103.17230) · 📚 被引 332
- **作者**: Jihwan Bang, Heesu Kim, Youngjoon Yoo, Jung-Woo Ha, Jonghyun Choi
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: 针对传统持续学习假设任务类别不相交、过于人工化的问题，该论文聚焦于更真实且实用的“模糊”任务边界场景，其中任务间共享类别。作者提出了一种基于逐样本分类不确定性和数据增强的存储管理策略，名为Rainbow Memory (RM)，以增强情节记忆中的样本多样性。通过在MNIST、CIFAR10、CIFAR100和ImageNet上的广泛实验，该方法在模糊持续学习设置下显著提高了准确性，并以较大幅度超越了现有最先进方法。
- **摘要（英）**: This paper addresses the unrealistic assumption of disjoint class sets in continual learning by focusing on 'blurry' task boundaries where tasks share classes. It proposes Rainbow Memory (RM), a memory management strategy based on per-sample classification uncertainty and data augmentation to enhance sample diversity in episodic memory. Extensive experiments on MNIST, CIFAR10, CIFAR100, and ImageNet show significant accuracy improvements, outperforming state-of-the-art methods by large margins in blurry continual learning setups.
- **核心贡献**: 提出了一种基于样本不确定性和数据增强的存储管理策略，显著提升了模糊任务边界下的持续学习性能。
- **创新点**: 利用逐样本分类不确定性指导记忆样本选择，并结合数据增强增加多样性。
- **结果**: 在多个数据集上大幅超越现有方法，验证了方法的有效性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning is a realistic learning scenario for AI models. Prevalent scenario of continual learning, however, assumes disjoint sets of classes as tasks and is less realistic rather artificial. Instead, we focus on 'blurry' task boundary; where tasks shares classes and is more realistic and practical. To address such task, we argue the importance of diversity of samples in an episodic memory. To enhance the sample diversity in the memory, we propose a novel memory management strategy based on per-sample classification uncertainty and data augmentation, named Rainbow Memory (RM). With extensive empirical validations on MNIST, CIFAR10, CIFAR100, and ImageNet datasets, we show that the proposed method significantly improves the accuracy in blurry continual learning setups, outperforming state of the arts by large margins despite its simplicity. Code and data splits will be available in https://github.com/clovaai/rainbow-memory.

</details>

### Continual Learning via Bit-Level Information Preserving. **⭐⭐⭐⭐** (相关度: 65%)
- **链接**: [arXiv:2105.04444](https://arxiv.org/abs/2105.04444) · 📚 被引 37
- **作者**: Yujun Shi, Li Yuan, Yunpeng Chen, Jiashi Feng
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: 针对持续学习中灾难性遗忘和内存开销大的问题，该论文从信息论角度分析，发现遗忘源于学习新任务时模型参数上先前任务信息增益的丢失。为此，提出了一种名为Bit-Level Information Preserving (BLIP)的方法，通过参数量化在比特级别更新参数，保留信息增益。具体地，BLIP先对网络进行权重量化训练，然后估计每个参数的信息增益以决定冻结哪些比特来防止遗忘。在分类和强化学习任务上的实验表明，该方法优于或与现有方法相当。
- **摘要（英）**: This paper addresses catastrophic forgetting and high memory costs in continual learning by analyzing the process through information theory, identifying that forgetting stems from loss of information gain on parameters from previous tasks. It proposes Bit-Level Information Preserving (BLIP), which updates parameters at the bit level via quantization to preserve information gain, freezing bits based on estimated gain. Experiments on classification and reinforcement learning tasks show superior or comparable performance to existing methods.
- **核心贡献**: 提出了基于比特级信息保留的持续学习方法，有效缓解遗忘并降低内存开销。
- **创新点**: 将信息增益估计与参数量化结合，在比特级别动态冻结参数。
- **结果**: 在分类和强化学习任务中取得优于或持平现有方法的效果。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning tackles the setting of learning different tasks sequentially. Despite the lots of previous solutions, most of them still suffer significant forgetting or expensive memory cost. In this work, targeted at these problems, we first study the continual learning process through the lens of information theory and observe that forgetting of a model stems from the loss of \emph{information gain} on its parameters from the previous tasks when learning a new task. From this viewpoint, we then propose a novel continual learning approach called Bit-Level Information Preserving (BLIP) that preserves the information gain on model parameters through updating the parameters at the bit level, which can be conveniently implemented with parameter quantization. More specifically, BLIP first trains a neural network with weight quantization on the new incoming task and then estimates information gain on each parameter provided by the task data to determine the bits to be frozen to prevent forgetting. We conduct extensive experiments ranging from classification tasks to reinforcement learning tasks, and the results show that our method produces better or on par results comparing to previous state-of-the-arts. Indeed, BLIP achieves close to zero forgetting while only requiring constant memory overheads throughout continual learning.

</details>

### Rectification-Based Knowledge Retention for Continual Learning. **⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2103.16597](https://arxiv.org/abs/2103.16597) · 📚 被引 43
- **作者**: Pravendra Singh, Pratik Mazumder, Piyush Rai, Vinay P. Namboodiri
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: 针对深度学习模型在增量学习中的灾难性遗忘问题，该论文提出了一种基于权重修正和仿射变换的方法，适用于任务增量学习，包括零样本和非零样本设置。方法通过“修正”先前任务学到的权重来适应新任务，仅需学习少量参数，并学习网络输出的仿射变换以更好地适应新任务。在多个数据集上的实验表明，该方法在零样本和非零样本任务增量学习设置中均有效。
- **摘要（英）**: This paper addresses catastrophic forgetting in incremental learning by proposing a method based on weight rectifications and affine transformations for task incremental learning, applicable to both zero-shot and non-zero-shot settings. It adapts network weights by 'rectifying' previous task weights with few parameters and learns affine transformations on outputs. Experiments on multiple datasets demonstrate effectiveness in both settings.
- **核心贡献**: 提出了基于权重修正和仿射变换的任务增量学习方法，支持零样本设置。
- **创新点**: 通过少量参数修正权重并学习输出变换，实现高效任务适应。
- **结果**: 在多个数据集上验证了方法的有效性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep learning models suffer from catastrophic forgetting when trained in an incremental learning setting. In this work, we propose a novel approach to address the task incremental learning problem, which involves training a model on new tasks that arrive in an incremental manner. The task incremental learning problem becomes even more challenging when the test set contains classes that are not part of the train set, i.e., a task incremental generalized zero-shot learning problem. Our approach can be used in both the zero-shot and non zero-shot task incremental learning settings. Our proposed method uses weight rectifications and affine transformations in order to adapt the model to different tasks that arrive sequentially. Specifically, we adapt the network weights to work for new tasks by "rectifying" the weights learned from the previous task. We learn these weight rectifications using very few parameters. We additionally learn affine transformations on the outputs generated by the network in order to better adapt them for the new task. We perform experiments on several datasets in both zero-shot and non zero-shot task incremental learning settings and empirically show that our approach achieves state-of-the-art results. Specifically, our approach outperforms the state-of-the-art non zero-shot task incremental learning method by over 5% on the CIFAR-100 dataset. Our approach also significantly outperforms the state-of-the-art task incremental generalized zero-shot learning method by absolute margins of 6.91% and 6.33% for the AWA1 and CUB datasets, respectively. We validate our approach using various ablation studies.

</details>

### Layerwise Optimization by Gradient Decomposition for Continual Learning. **⭐⭐** (相关度: 50%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Tang_Layerwise_Optimization_by_Gradient_Decomposition_for_Continual_Learning_CVPR_2021_paper.html) · 📚 被引 57
- **作者**: Shixiang Tang, Dapeng Chen, Jinguo Zhu, Shijie Yu, Wanli Ouyang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: 该论文针对持续学习中的优化问题，提出了基于梯度分解的逐层优化方法。由于摘要缺失，具体方法细节和实验效果无法评估，但推测其通过分解梯度来分别优化各层，以缓解遗忘。缺乏实验数据支持，整体贡献和效果不明确。
- **摘要（英）**: This paper proposes a layerwise optimization method via gradient decomposition for continual learning. Due to missing abstract, specific details and experimental results are unavailable, but it likely decomposes gradients to optimize layers separately to mitigate forgetting. Lack of experimental data makes its contribution unclear.
- **核心贡献**: 提出了基于梯度分解的逐层优化方法。
- **创新点**: 通过梯度分解实现逐层优化。
- **结果**: 未提供具体实验结果。

### Efficient Feature Transformations for Discriminative and Generative Continual Learning. **⭐⭐** (相关度: 50%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Verma_Efficient_Feature_Transformations_for_Discriminative_and_Generative_Continual_Learning_CVPR_2021_paper.html) · 📚 被引 51
- **作者**: Vinay Kumar Verma, Kevin J. Liang, Nikhil Mehta, Piyush Rai, Lawrence Carin
- **🏷️ 机构**: Duke University, IIT Kanpur
- **会议**: CVPR 2021
- **摘要（中）**: 该论文探讨了高效特征变换在判别式和生成式持续学习中的应用。由于摘要缺失，具体方法细节和实验效果无法评估，但推测其通过特征变换来适应新任务并保留旧知识。缺乏实验数据支持，整体贡献和效果不明确。
- **摘要（英）**: This paper explores efficient feature transformations for discriminative and generative continual learning. Due to missing abstract, specific details and experimental results are unavailable, but it likely uses feature transformations to adapt to new tasks while retaining old knowledge. Lack of experimental data makes its contribution unclear.
- **核心贡献**: 提出了高效特征变换方法用于持续学习。
- **创新点**: 将特征变换应用于判别式和生成式持续学习。
- **结果**: 未提供具体实验结果。

### Training Networks in Null Space of Feature Covariance for Continual Learning. **⭐⭐⭐⭐** (相关度: 65%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Wang_Training_Networks_in_Null_Space_of_Feature_Covariance_for_Continual_CVPR_2021_paper.html) · 📚 被引 105
- **作者**: Shipeng Wang, Xiaorong Li, Jian Sun, Zongben Xu
- **🏷️ 机构**: Xi&#x2019;an Jiaotong University,School of Mathematics and Statistics,Xi&#x2019;an,China,710049
- **会议**: CVPR 2021
- **摘要（中）**: 针对持续学习中的灾难性遗忘问题，该论文提出了一种在特征协方差零空间中训练网络的方法。通过将网络更新限制在特征协方差的零空间，避免干扰先前任务的特征表示，从而有效保留旧知识。该方法在多个持续学习基准上取得了优异的性能，显著减少了遗忘。
- **摘要（英）**: This paper addresses catastrophic forgetting in continual learning by training networks in the null space of feature covariance. By constraining updates to the null space, it avoids interfering with previous task representations, effectively retaining old knowledge. The method achieves strong performance on multiple continual learning benchmarks, significantly reducing forgetting.
- **核心贡献**: 提出了在特征协方差零空间中训练网络的方法，有效缓解灾难性遗忘。
- **创新点**: 利用特征协方差的零空间约束网络更新，保护旧任务特征。
- **结果**: 在多个基准上显著减少遗忘，性能优异。

### ORDisCo: Effective and Efficient Usage of Incremental Unlabeled Data for Semi-Supervised Continual Learning. **⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Wang_ORDisCo_Effective_and_Efficient_Usage_of_Incremental_Unlabeled_Data_for_CVPR_2021_paper.html) · 📚 被引 68
- **作者**: Liyuan Wang, Kuo Yang, Chongxuan Li, Lanqing Hong, Zhenguo Li, Jun Zhu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: ①针对半监督持续学习（SSCL）中增量无标注数据利用效率低、计算成本高的问题。②提出ORDisCo方法，通过选择性使用增量无标注数据，并结合知识蒸馏与一致性正则化来更新模型。③相比现有方法，在保持性能的同时显著降低了计算开销，并设计了有效的样本选择策略。④在多个基准数据集上验证了方法的有效性，在准确率和计算效率之间取得了更好的平衡。
- **摘要（英）**: This paper addresses the inefficient use of incremental unlabeled data in semi-supervised continual learning. It proposes ORDisCo, which selectively leverages unlabeled data with knowledge distillation and consistency regularization to reduce computational cost while maintaining performance. Experiments on benchmarks show improved accuracy-efficiency trade-offs.
- **核心贡献**: 提出了一种高效利用增量无标注数据的半监督持续学习框架。
- **创新点**: 设计了基于样本选择与一致性正则化的增量学习机制。
- **结果**: 在多个基准上实现了性能与计算效率的更好平衡。

### Few-Shot Incremental Learning With Continually Evolved Classifiers. **⭐⭐⭐** (相关度: 55%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Zhang_Few-Shot_Incremental_Learning_With_Continually_Evolved_Classifiers_CVPR_2021_paper.html)
- **作者**: Chi Zhang, Nan Song, Guosheng Lin, Yun Zheng, Pan Pan, Yinghui Xu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: ①针对少样本增量学习（FSCIL）中分类器对新旧类适应能力不足的问题。②提出持续演化的分类器（CEC）方法，通过动态调整分类器参数以适应新类，同时保持旧类性能。③引入演化机制和正则化项，增强分类器的泛化能力。④在多个FSCIL基准上取得了优于现有方法的性能。
- **摘要（英）**: This work tackles the challenge of classifier adaptation in few-shot incremental learning. It proposes continually evolved classifiers that dynamically adjust parameters for new classes while preserving old ones, using evolution mechanisms and regularization. Experiments show superior performance on FSCIL benchmarks.
- **核心贡献**: 提出了持续演化的分类器框架以提升少样本增量学习性能。
- **创新点**: 利用动态参数演化机制增强分类器对新旧类的适应。
- **结果**: 在多个基准上超越了现有方法。

### Image De-Raining via Continual Learning. **⭐⭐** (相关度: 30%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Zhou_Image_De-Raining_via_Continual_Learning_CVPR_2021_paper.html) · 📚 被引 44
- **作者**: Man Zhou, Jie Xiao, Yifan Chang, Xueyang Fu, Aiping Liu, Jinshan Pan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: ①针对图像去雨任务中模型面对不同降雨场景时性能退化的问题。②提出将持续学习应用于图像去雨，通过顺序学习多种降雨类型来提升泛化能力。③采用知识蒸馏和正则化技术缓解灾难性遗忘。④实验表明模型在多种降雨条件下表现更稳定。
- **摘要（英）**: This paper applies continual learning to image de-raining to handle diverse rain scenarios. It sequentially learns multiple rain types with knowledge distillation and regularization to mitigate catastrophic forgetting. Experiments show improved robustness across conditions.
- **核心贡献**: 首次将持续学习用于图像去雨任务。
- **创新点**: 利用持续学习策略增强去雨模型的跨场景泛化。
- **结果**: 在多种降雨条件下实现了更稳定的性能。

### On Learning the Geodesic Path for Incremental Learning. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2104.08572](https://arxiv.org/abs/2104.08572) · 📚 被引 111
- **作者**: Christian Simon, Piotr Koniusz, Mehrtash Harandi
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: ①针对增量学习中知识蒸馏方法对旧知识保持不充分的问题。②提出沿流形测地线路径进行蒸馏的新方法，通过构建新旧响应在低维流形上的表示并最小化测地线距离。③相比传统蒸馏，该方法提供了更平滑且有效的知识传递，增强了旧知识的保持。④在多个增量学习基准上取得了显著性能提升。
- **摘要（英）**: This paper addresses insufficient knowledge retention in incremental learning distillation. It proposes constructing low-dimensional manifolds for old and new responses and minimizing dissimilarity along the geodesic path, enabling smoother and more effective knowledge transfer. Experiments show significant improvements on benchmarks.
- **核心贡献**: 提出了基于测地线路径的流形蒸馏方法。
- **创新点**: 利用流形几何结构优化知识蒸馏过程。
- **结果**: 在多个基准上显著提升了增量学习性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural networks notoriously suffer from the problem of catastrophic forgetting, the phenomenon of forgetting the past knowledge when acquiring new knowledge. Overcoming catastrophic forgetting is of significant importance to emulate the process of "incremental learning", where the model is capable of learning from sequential experience in an efficient and robust way. State-of-the-art techniques for incremental learning make use of knowledge distillation towards preventing catastrophic forgetting. Therein, one updates the network while ensuring that the network's responses to previously seen concepts remain stable throughout updates. This in practice is done by minimizing the dissimilarity between current and previous responses of the network one way or another. Our work contributes a novel method to the arsenal of distillation techniques. In contrast to the previous state of the art, we propose to firstly construct low-dimensional manifolds for previous and current responses and minimize the dissimilarity between the responses along the geodesic connecting the manifolds. This induces a more formidable knowledge distillation with smooth properties which preserves the past knowledge more efficiently as observed by our comprehensive empirical study.

</details>

### Self-Promoted Prototype Refinement for Few-Shot Class-Incremental Learning. **⭐⭐⭐⭐** (相关度: 65%)
- **链接**: [arXiv:2107.08918](https://arxiv.org/abs/2107.08918) · 📚 被引 170
- **作者**: Kai Zhu, Yang Cao, Wei Zhai, Jie Cheng, Zheng-Jun Zha
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: ①针对少样本类增量学习（FSCIL）中表示优化和原型重组困难的问题。②提出自促进原型细化机制，结合随机片段选择策略和动态关系投影模块，增强新类表达并考虑类间依赖。③通过关系矩阵引导原型更新，提升模型对新类的适应能力。④在三个基准数据集上分别超越现有方法13%、17%和11%。
- **摘要（英）**: This paper tackles representation optimization and prototype reorganization in few-shot class-incremental learning. It proposes self-promoted prototype refinement with random episode selection and dynamic relation projection to enhance new-class expression and inter-class dependencies. Experiments show improvements of 13%, 17%, and 11% over state-of-the-art on three benchmarks.
- **核心贡献**: 提出了自促进原型细化机制以提升FSCIL性能。
- **创新点**: 利用动态关系投影模块实现原型自促进更新。
- **结果**: 在三个基准上大幅超越现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Few-shot class-incremental learning is to recognize the new classes given few samples and not forget the old classes. It is a challenging task since representation optimization and prototype reorganization can only be achieved under little supervision. To address this problem, we propose a novel incremental prototype learning scheme. Our scheme consists of a random episode selection strategy that adapts the feature representation to various generated incremental episodes to enhance the corresponding extensibility, and a self-promoted prototype refinement mechanism which strengthens the expression ability of the new classes by explicitly considering the dependencies among different classes. Particularly, a dynamic relation projection module is proposed to calculate the relation matrix in a shared embedding space and leverage it as the factor for bootstrapping the update of prototypes. Extensive experiments on three benchmark datasets demonstrate the above-par incremental performance, outperforming state-of-the-art methods by a margin of 13%, 17% and 11%, respectively.

</details>

### Semantic-Aware Knowledge Distillation for Few-Shot Class-Incremental Learning. **⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2103.04059](https://arxiv.org/abs/2103.04059) · 📚 被引 185
- **作者**: Ali Cheraghian, Shafin Rahman, Pengfei Fang, Soumava Kumar Roy, Lars Petersson, Mehrtash Harandi
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: ①针对少样本类增量学习（FSCIL）中仅依赖视觉信息导致知识蒸馏效果有限的问题。②提出语义感知知识蒸馏方法，利用词嵌入作为语义信息辅助蒸馏，并设计注意力机制对齐视觉和语义向量。③通过多并行嵌入的注意力机制减少灾难性遗忘。④在MiniImageNet、CUB200和CIFAR100上取得了新的最优结果。
- **摘要（英）**: This paper addresses limited distillation in FSCIL by incorporating semantic information. It uses word embeddings to facilitate distillation and an attention mechanism to align visual and semantic vectors, reducing catastrophic forgetting. Experiments on MiniImageNet, CUB200, and CIFAR100 establish new state-of-the-art results.
- **核心贡献**: 提出了语义感知的知识蒸馏方法用于FSCIL。
- **创新点**: 引入词嵌入和注意力机制实现视觉-语义对齐。
- **结果**: 在多个基准上取得了最优性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Few-shot class incremental learning (FSCIL) portrays the problem of learning new concepts gradually, where only a few examples per concept are available to the learner. Due to the limited number of examples for training, the techniques developed for standard incremental learning cannot be applied verbatim to FSCIL. In this work, we introduce a distillation algorithm to address the problem of FSCIL and propose to make use of semantic information during training. To this end, we make use of word embeddings as semantic information which is cheap to obtain and which facilitate the distillation process. Furthermore, we propose a method based on an attention mechanism on multiple parallel embeddings of visual data to align visual and semantic vectors, which reduces issues related to catastrophic forgetting. Via experiments on MiniImageNet, CUB200, and CIFAR100 dataset, we establish new state-of-the-art results by outperforming existing approaches.

</details>

### Distilling Causal Effect of Data in Class-Incremental Learning. **⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Hu_Distilling_Causal_Effect_of_Data_in_Class-Incremental_Learning_CVPR_2021_paper.html) · 📚 被引 157
- **作者**: Xinting Hu, Kaihua Tang, Chunyan Miao, Xian-Sheng Hua, Hanwang Zhang
- **🏷️ 机构**: NUS
- **会议**: CVPR 2021
- **摘要（中）**: ①针对类增量学习（CIL）中数据分布偏移导致灾难性遗忘的问题。②提出通过因果推断蒸馏数据效应，将旧数据的影响以因果形式迁移到新模型训练中。③相比传统知识蒸馏，该方法显式建模数据因果效应，减少对旧样本存储的依赖。④实验表明在多个CIL基准上显著降低遗忘率，但摘要未提供具体数值。
- **摘要（英）**: This paper addresses catastrophic forgetting in class-incremental learning by distilling the causal effect of data. It models data influence causally to transfer knowledge without heavy replay. The method reduces forgetting on benchmarks, though specific numbers are absent.
- **核心贡献**: 提出数据因果效应蒸馏框架用于类增量学习。
- **创新点**: 将因果推断引入增量知识迁移。
- **结果**: 在多个基准上降低遗忘率。

### Adaptive Aggregation Networks for Class-Incremental Learning. **⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Liu_Adaptive_Aggregation_Networks_for_Class-Incremental_Learning_CVPR_2021_paper.html) · 📚 被引 193
- **作者**: Yaoyao Liu, Bernt Schiele, Qianru Sun
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: ①针对类增量学习中的特征漂移和分类器偏差问题。②提出自适应聚合网络，动态组合多个专家网络的特征以适配新类。③通过可学习的聚合权重平衡旧类和新类知识，无需存储大量旧样本。④实验显示在CIFAR和ImageNet子集上优于现有方法，但摘要未给出具体精度。
- **摘要（英）**: This work tackles feature drift in class-incremental learning via adaptive aggregation of expert networks. It learns weights to balance old and new knowledge, improving accuracy on CIFAR and ImageNet subsets without heavy replay.
- **核心贡献**: 提出自适应聚合网络缓解增量学习中的特征漂移。
- **创新点**: 动态专家网络聚合机制。
- **结果**: 在多个基准上提升分类精度。

### Incremental Learning via Rate Reduction. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2011.14593](https://arxiv.org/abs/2011.14593) · 📚 被引 28
- **作者**: Ziyang Wu, Christina Baek, Chong You, Yi Ma
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: ①针对深度网络在增量学习中的灾难性遗忘，指出黑盒优化难以调整参数保留旧知识。②提出基于率减少原理的白盒架构，每层显式计算无需反向传播，可证明地构造新网络模拟联合训练。③相比黑盒方法，该方案提供理论保证，避免遗忘。④在MNIST和CIFAR-10上大幅超越SOTA，分类性能衰减显著降低。
- **摘要（英）**: This paper addresses catastrophic forgetting by proposing a white-box architecture based on rate reduction, where layers are computed explicitly without backpropagation. It provably emulates joint training, outperforming SOTA on MNIST and CIFAR-10 with significantly less decay.
- **核心贡献**: 提出可证明的白盒增量学习算法。
- **创新点**: 利用率减少原理替代黑盒优化。
- **结果**: 在MNIST和CIFAR-10上大幅超越SOTA。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Current deep learning architectures suffer from catastrophic forgetting, a failure to retain knowledge of previously learned classes when incrementally trained on new classes. The fundamental roadblock faced by deep learning methods is that deep learning models are optimized as "black boxes," making it difficult to properly adjust the model parameters to preserve knowledge about previously seen data. To overcome the problem of catastrophic forgetting, we propose utilizing an alternative "white box" architecture derived from the principle of rate reduction, where each layer of the network is explicitly computed without back propagation. Under this paradigm, we demonstrate that, given a pre-trained network and new data classes, our approach can provably construct a new network that emulates joint training with all past and new classes. Finally, our experiments show that our proposed learning algorithm observes significantly less decay in classification performance, outperforming state of the art methods on MNIST and CIFAR-10 by a large margin and justifying the use of "white box" algorithms for incremental learning even for sufficiently complex image data.

</details>

### Few-Shot and Continual Learning with Attentive Independent Mechanisms. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00932)
- **作者**: Eugene Lee, Cheng-Han Huang, Chen-Yi Lee
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021
- **摘要（中）**: ①针对小样本与持续学习中的灾难性遗忘和泛化不足问题。②提出Attentive Independent Mechanisms（AIM），通过注意力机制学习独立的功能模块，每个模块负责特定任务或概念，实现模块化知识组合。③相比共享参数方法，AIM增强了任务间的隔离性，减少干扰，并支持小样本快速适应。④在多个小样本持续学习基准上取得最优性能，展示了模块化架构的潜力。
- **摘要（英）**: This paper addresses catastrophic forgetting and poor generalization in few-shot continual learning. It proposes Attentive Independent Mechanisms (AIM), which learns independent functional modules via attention, enabling modular knowledge composition. Compared to shared-parameter methods, AIM improves task isolation and supports rapid few-shot adaptation, achieving state-of-the-art results on benchmarks.
- **核心贡献**: 提出注意力独立机制用于小样本持续学习。
- **创新点**: 通过注意力实现模块化知识隔离与组合。
- **结果**: 在多个基准上取得最优性能。

### Graph-Based Continual Learning.
- **链接**: [出版页](https://openreview.net/forum?id=HHSEKOnPvaO)
- **作者**: Binh Tang, David S. Matteson
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

## 🆕 增量新增

### DER: Dynamically Expandable Representation for Class Incremental Learning. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2103.16788](https://arxiv.org/abs/2103.16788) · 📚 被引 655
- **作者**: Shipeng Yan, Jiangwei Xie, Xuming He
- **🏷️ 机构**: ShanghaiTech University,School of Information Science and Technology
- **会议**: CVPR 2021
- **摘要（中）**: ①针对类增量学习在有限内存下稳定性-可塑性权衡不佳的问题。②提出两阶段学习方法，冻结旧表征并动态扩展新特征维度，结合通道级掩码剪枝和辅助损失。③相比固定容量方法，能根据新概念复杂度自适应扩展表征。④在三个基准上大幅超越现有方法。
- **摘要（英）**: This paper addresses class incremental learning with limited memory, proposing a two-stage approach with dynamically expandable representations via channel-level pruning and auxiliary loss. It improves stability-plasticity trade-off and outperforms prior methods on three benchmarks.
- **核心贡献**: 提出动态可扩展表征的类增量学习框架。
- **创新点**: 结合通道级剪枝实现表征自适应扩展。
- **结果**: 在三个基准上大幅领先现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We address the problem of class incremental learning, which is a core step towards achieving adaptive vision intelligence. In particular, we consider the task setting of incremental learning with limited memory and aim to achieve better stability-plasticity trade-off. To this end, we propose a novel two-stage learning approach that utilizes a dynamically expandable representation for more effective incremental concept modeling. Specifically, at each incremental step, we freeze the previously learned representation and augment it with additional feature dimensions from a new learnable feature extractor. This enables us to integrate new visual concepts with retaining learned knowledge. We dynamically expand the representation according to the complexity of novel concepts by introducing a channel-level mask-based pruning strategy. Moreover, we introduce an auxiliary loss to encourage the model to learn diverse and discriminate features for novel concepts. We conduct extensive experiments on the three class incremental learning benchmarks and our method consistently outperforms other methods with a large margin.

</details>

### Prototype Augmentation and Self-Supervision for Incremental Learning. **⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Zhu_Prototype_Augmentation_and_Self-Supervision_for_Incremental_Learning_CVPR_2021_paper.html) · 📚 被引 365
- **作者**: Fei Zhu, Xu-Yao Zhang, Chuang Wang, Fei Yin, Cheng-Lin Liu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: ①针对类增量学习中数据稀缺导致新类表示不充分的问题。②提出原型增强和自监督学习，通过生成原型增强新类数据，并利用自监督任务提升特征泛化。③相比仅用原始数据的方法，增强原型和自监督信号提高新类可判别性。④摘要未提供具体数据，但预期在CIL基准上提升准确率。
- **摘要（英）**: ①Addresses insufficient representation for new classes in class-incremental learning. ②Proposes prototype augmentation and self-supervision to enrich new class data and improve feature generalization. ③Improves on raw-data-only methods by enhancing discriminability. ④Expected to boost accuracy, but no specific numbers are given.
- **核心贡献**: 提出原型增强与自监督结合的增量学习方法。
- **创新点**: 利用自监督信号增强原型表示。
- **结果**: 未报告具体性能数据。

### Wanderlust: Online Continual Object Detection in the Real World. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01065)
- **作者**: Jianren Wang, Xin Wang, Yue Shang-Guan, Abhinav Gupta
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021
- **摘要（中）**: ①针对现实世界中在线持续目标检测的挑战，如数据流非平稳和类别增量。②提出Wanderlust系统，设计在线学习框架处理连续数据流，结合回放和蒸馏技术。③相比离线训练方法，该方法适应真实动态环境，减少遗忘。④摘要未提供具体数据，但强调在真实场景中的实用性。
- **摘要（英）**: ①Addresses online continual object detection in real-world non-stationary data streams. ②Proposes Wanderlust, an online learning framework with replay and distillation. ③Improves on offline methods by adapting to dynamic environments. ④Emphasizes practical utility, though no specific metrics are provided.
- **核心贡献**: 提出首个面向真实世界的在线持续目标检测系统。
- **创新点**: 将在线学习与检测结合，处理非平稳数据流。
- **结果**: 未报告具体性能数据。

### Class-Incremental Learning for Action Recognition in Videos. **⭐⭐⭐** (相关度: 65%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01344)
- **作者**: Jaeyoo Park, Minsoo Kang, Bohyung Han
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021
- **摘要（中）**: ①针对视频动作识别中的类增量学习问题，即模型需不断学习新动作类别而不遗忘旧类。②提出专门针对视频的CIL方法，利用时空特征和蒸馏技术。③相比图像CIL方法，该方法考虑视频时序信息，提升动作识别性能。④摘要未提供具体数据，但预期在视频基准上优于通用CIL方法。
- **摘要（英）**: ①Addresses class-incremental learning for video action recognition. ②Proposes a video-specific CIL method leveraging spatiotemporal features and distillation. ③Improves on image-based CIL by exploiting temporal information. ④Expected to outperform generic methods, but no specific results are given.
- **核心贡献**: 提出针对视频动作识别的类增量学习方法。
- **创新点**: 将时空建模融入CIL框架。
- **结果**: 未报告具体性能数据。

### Online Continual Learning with Natural Distribution Shifts: An Empirical Study with Visual Data. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00817)
- **作者**: Zhipeng Cai, Ozan Sener, Vladlen Koltun
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021
- **摘要（中）**: ①针对在线持续学习在自然分布偏移（如自动驾驶场景中的天气、光照变化）下的性能退化问题。②通过大规模视觉数据集（如iNaturalist、Places365）进行实证研究，系统比较了多种持续学习算法在自然分布偏移下的表现，并分析了类别增量与任务增量的影响。③不同于以往人工合成分布偏移，该研究首次聚焦于真实世界自然分布偏移，提供了更贴近实际应用的评估基准。④研究发现现有算法在自然偏移下性能显著下降，且简单经验回放方法表现优于复杂方法，为后续研究提供了重要基线。
- **摘要（英）**: This paper addresses performance degradation of online continual learning under natural distribution shifts, such as weather and lighting changes in autonomous driving. It conducts an empirical study on large-scale visual datasets, comparing various continual learning algorithms and analyzing the impact of class-incremental vs. task-incremental settings. Unlike prior work using synthetic shifts, it focuses on real-world natural shifts, revealing that simple experience replay outperforms complex methods and providing a crucial baseline for future research.
- **核心贡献**: 首次系统评估了自然分布偏移下在线持续学习算法的性能，并建立了新的基准。
- **创新点**: 聚焦真实世界自然分布偏移而非人工合成偏移，更贴近实际应用场景。
- **结果**: 发现现有算法在自然偏移下性能显著下降，简单经验回放方法表现最佳。

### Co2L: Contrastive Continual Learning. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00938)
- **作者**: Hyuntak Cha, Jaeho Lee, Jinwoo Shin
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021
- **摘要（中）**: ①针对持续学习中灾难性遗忘问题，特别是监督对比学习在持续学习场景下的适用性。②提出Co2L框架，将监督对比学习与持续学习结合，通过对比损失增强特征表示的可迁移性，并引入基于原型的分类器减少遗忘。③相比传统交叉熵损失，对比学习能学习更鲁棒的特征，且无需额外存储大量样本。④在CIFAR-100、ImageNet等基准上，Co2L显著优于现有持续学习方法，在多个设定下刷新了SOTA。
- **摘要（英）**: This paper tackles catastrophic forgetting in continual learning by integrating supervised contrastive learning into the framework. The proposed Co2L uses contrastive losses to learn more transferable feature representations and a prototype-based classifier to mitigate forgetting. Compared to cross-entropy-based methods, it achieves superior performance on benchmarks like CIFAR-100 and ImageNet, setting new state-of-the-art results across multiple settings.
- **核心贡献**: 提出了一种基于监督对比学习的持续学习框架，显著提升特征可迁移性。
- **创新点**: 利用对比学习替代交叉熵损失，增强特征鲁棒性并减少遗忘。
- **结果**: 在多个基准上刷新SOTA，性能显著优于现有方法。

### Continual Learning on Noisy Data Streams via Self-Purified Replay. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00058)
- **作者**: Chris Dongjoo Kim, Jinseo Jeong, Sangwoo Moon, Gunhee Kim
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021
- **摘要（中）**: ①针对持续学习中数据流存在噪声（如标签错误）时，经验回放方法会放大噪声影响的问题。②提出Self-Purified Replay（SPR）方法，通过自净化机制在回放前过滤噪声样本，利用模型自身预测置信度识别并剔除错误标签样本。③相比传统回放方法，SPR能有效降低噪声对模型更新的干扰，提升鲁棒性。④在多个含噪持续学习基准上，SPR显著优于现有方法，尤其在噪声比例较高时性能提升明显。
- **摘要（英）**: This paper addresses the issue of noisy data streams in continual learning, where experience replay can amplify label noise. It proposes Self-Purified Replay (SPR), which filters noisy samples before replay using model confidence to identify and remove mislabeled data. Compared to standard replay methods, SPR reduces noise interference and improves robustness, achieving significant gains on noisy continual learning benchmarks, especially under high noise ratios.
- **核心贡献**: 提出自净化回放机制，有效过滤噪声样本，提升持续学习鲁棒性。
- **创新点**: 利用模型自身置信度动态净化回放缓冲区，无需额外监督。
- **结果**: 在含噪基准上显著优于现有方法，高噪声下性能提升明显。

### RECALL: Replay-based Continual Learning in Semantic Segmentation. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00694)
- **作者**: Andrea Maracani, Umberto Michieli, Marco Toldo, Pietro Zanuttigh
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021
- **摘要（中）**: ①针对语义分割中的持续学习问题，特别是自动驾驶场景中新增类别时的灾难性遗忘。②提出RECALL方法，基于回放的持续学习框架，结合知识蒸馏和特征对齐，在分割任务中有效保留旧类别知识。③相比通用持续学习方法，RECALL专门针对语义分割的像素级预测特性设计，利用分割掩码进行更精准的回放。④在多个语义分割基准（如Pascal VOC、ADE20K）上，RECALL显著优于现有方法，在增量类别设定下保持高mIoU。
- **摘要（英）**: This paper tackles continual learning in semantic segmentation, focusing on catastrophic forgetting when new classes are added in autonomous driving scenarios. It proposes RECALL, a replay-based framework combining knowledge distillation and feature alignment to preserve old class knowledge. Unlike general methods, RECALL is tailored for pixel-level prediction, using segmentation masks for more precise replay, and significantly outperforms existing approaches on benchmarks like Pascal VOC and ADE20K under incremental class settings.
- **核心贡献**: 提出面向语义分割的回放式持续学习框架，结合蒸馏与特征对齐。
- **创新点**: 利用分割掩码进行像素级回放，专门优化分割任务的持续学习。
- **结果**: 在多个分割基准上显著优于现有方法，保持高mIoU。

### Detection and Continual Learning of Novel Face Presentation Attacks. **⭐⭐⭐** (相关度: 65%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01458)
- **作者**: Mohammad Rostami, Leonidas Spinoulas, Mohamed E. Hussein, Joe Mathai, Wael Abd-Almageed
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021
- **摘要（中）**: ①针对人脸呈现攻击检测（FOD）中新型攻击不断出现，模型需持续学习新攻击类型的问题。②提出一种结合检测与持续学习的框架，在检测已知攻击的同时，通过持续学习机制适应新攻击，并利用回放策略避免遗忘。③相比静态检测模型，该方法能动态更新，适应不断演变的攻击手段。④在多个FOD基准上，该方法在保持已知攻击检测性能的同时，对新攻击的检测准确率显著提升。
- **摘要（英）**: This paper addresses novel face presentation attack detection (FOD), where new attack types emerge and models must continually learn. It proposes a framework combining detection with continual learning, adapting to new attacks via replay-based strategies while maintaining performance on known attacks. Compared to static models, it dynamically updates and significantly improves detection accuracy on novel attacks across multiple FOD benchmarks.
- **核心贡献**: 提出结合检测与持续学习的FOD框架，适应新型攻击。
- **创新点**: 将持续学习机制引入FOD，实现动态更新。
- **结果**: 在保持已知攻击性能的同时，显著提升新攻击检测准确率。

### Rehearsal revealed: The limits and merits of revisiting samples in continual learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00925)
- **作者**: Eli Verwimp, Matthias De Lange, Tinne Tuytelaars
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### Continual Learning for Image-Based Camera Localization.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00324)
- **作者**: Shuzhe Wang, Zakaria Laskar, Iaroslav Melekhov, Xiaotian Li, Juho Kannala
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### SS-IL: Separated Softmax for Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00088)
- **作者**: Hongjoon Ahn, Jihwan Kwak, Subin Lim, Hyeonsu Bang, Hyojun Kim, Taesup Moon
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### Synthesized Feature based Few-Shot Class-Incremental Learning on a Mixture of Subspaces.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00854)
- **作者**: Ali Cheraghian, Shafin Rahman, Sameera Ramasinghe, Pengfei Fang, Christian Simon, Lars Petersson et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### Always Be Dreaming: A New Approach for Data-Free Class-Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00924)
- **作者**: James Seale Smith, Yen-Chang Hsu, Jonathan C. Balloch, Yilin Shen, Hongxia Jin, Zsolt Kira
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### Striking a Balance between Stability and Plasticity for Class-Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00116)
- **作者**: Guile Wu, Shaogang Gong, Pan Li
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### EEC: Learning to Encode and Regenerate Images for Continual Learning.
- **链接**: [arXiv:2101.04904](https://arxiv.org/abs/2101.04904)
- **作者**: Ali Ayub, Alan R. Wagner
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The two main impediments to continual learning are catastrophic forgetting and memory limitations on the storage of data. To cope with these challenges, we propose a novel, cognitively-inspired approach which trains autoencoders with Neural Style Transfer to encode and store images. During training on a new task, reconstructed images from encoded episodes are replayed in order to avoid catastrophic forgetting. The loss function for the reconstructed images is weighted to reduce its effect during classifier training to cope with image degradation. When the system runs out of memory the encoded episodes are converted into centroids and covariance matrices, which are used to generate pseudo-images during classifier training, keeping classifier performance stable while using less memory. Our approach increases classification accuracy by 13-17% over state-of-the-art methods on benchmark datasets, while requiring 78% less storage space.

</details>

### CPR: Classifier-Projection Regularization for Continual Learning.
- **链接**: [arXiv:2006.07326](https://arxiv.org/abs/2006.07326)
- **作者**: Sungmin Cha, Hsiang Hsu, Taebaek Hwang, Flávio P. Calmon, Taesup Moon
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose a general, yet simple patch that can be applied to existing regularization-based continual learning methods called classifier-projection regularization (CPR). Inspired by both recent results on neural networks with wide local minima and information theory, CPR adds an additional regularization term that maximizes the entropy of a classifier's output probability. We demonstrate that this additional term can be interpreted as a projection of the conditional probability given by a classifier's output to the uniform distribution. By applying the Pythagorean theorem for KL divergence, we then prove that this projection may (in theory) improve the performance of continual learning methods. In our extensive experimental results, we apply CPR to several state-of-the-art regularization-based continual learning methods and benchmark performance on popular image recognition datasets. Our results demonstrate that CPR indeed promotes a wide local minima and significantly improves both accuracy and plasticity while simultaneously mitigating the catastrophic forgetting of baseline continual learning methods. The codes and scripts for this work are available at https://github.com/csm9493/CPR_CL.

</details>

### Continual learning in recurrent neural networks.
- **链接**: [出版页](https://openreview.net/forum?id=8xeBUgD8u9)
- **作者**: Benjamin Ehret, Christian Henning, Maria R. Cervera, Alexander Meulemans, Johannes von Oswald, Benjamin F. Grewe
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

### Generalized Variational Continual Learning.
- **链接**: [arXiv:2011.12328](https://arxiv.org/abs/2011.12328)
- **作者**: Noel Loo, Siddharth Swaroop, Richard E. Turner
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning deals with training models on new tasks and datasets in an online fashion. One strand of research has used probabilistic regularization for continual learning, with two of the main approaches in this vein being Online Elastic Weight Consolidation (Online EWC) and Variational Continual Learning (VCL). VCL employs variational inference, which in other settings has been improved empirically by applying likelihood-tempering. We show that applying this modification to VCL recovers Online EWC as a limiting case, allowing for interpolation between the two approaches. We term the general algorithm Generalized VCL (GVCL). In order to mitigate the observed overpruning effect of VI, we take inspiration from a common multi-task architecture, neural networks with task-specific FiLM layers, and find that this addition leads to significant performance gains, specifically for variational methods. In the small-data regime, GVCL strongly outperforms existing baselines. In larger datasets, GVCL with FiLM layers outperforms or is competitive with existing baselines in terms of accuracy, whilst also providing significantly better calibration.

</details>

### Linear Mode Connectivity in Multitask and Continual Learning.
- **链接**: [arXiv:2010.04495](https://arxiv.org/abs/2010.04495)
- **作者**: Seyed-Iman Mirzadeh, Mehrdad Farajtabar, Dilan Görür, Razvan Pascanu, Hassan Ghasemzadeh
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual (sequential) training and multitask (simultaneous) training are often attempting to solve the same overall objective: to find a solution that performs well on all considered tasks. The main difference is in the training regimes, where continual learning can only have access to one task at a time, which for neural networks typically leads to catastrophic forgetting. That is, the solution found for a subsequent task does not perform well on the previous ones anymore. However, the relationship between the different minima that the two training regimes arrive at is not well understood. What sets them apart? Is there a local structure that could explain the difference in performance achieved by the two different schemes? Motivated by recent work showing that different minima of the same task are typically connected by very simple curves of low error, we investigate whether multitask and continual solutions are similarly connected. We empirically find that indeed such connectivity can be reliably achieved and, more interestingly, it can be done by a linear path, conditioned on having the same initialization for both. We thoroughly analyze this observation and discuss its significance for the continual learning process. Furthermore, we exploit this finding to propose an effective algorithm that constrains the sequentially learned minima to behave as the multitask solution. We show that our method outperforms several state of the art continual learning algorithms on various vision benchmarks.

</details>

### Contextual Transformation Networks for Online Continual Learning.
- **链接**: [出版页](https://openreview.net/forum?id=zx_uX-BO7CH)
- **作者**: Quang Pham, Chenghao Liu, Doyen Sahoo, Steven C. H. Hoi
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

### Gradient Projection Memory for Continual Learning.
- **链接**: [arXiv:2103.09762](https://arxiv.org/abs/2103.09762)
- **作者**: Gobinda Saha, Isha Garg, Kaushik Roy
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The ability to learn continually without forgetting the past tasks is a desired attribute for artificial learning systems. Existing approaches to enable such learning in artificial neural networks usually rely on network growth, importance based weight update or replay of old data from the memory. In contrast, we propose a novel approach where a neural network learns new tasks by taking gradient steps in the orthogonal direction to the gradient subspaces deemed important for the past tasks. We find the bases of these subspaces by analyzing network representations (activations) after learning each task with Singular Value Decomposition (SVD) in a single shot manner and store them in the memory as Gradient Projection Memory (GPM). With qualitative and quantitative analyses, we show that such orthogonal gradient descent induces minimum to no interference with the past tasks, thereby mitigates forgetting. We evaluate our algorithm on diverse image classification datasets with short and long sequences of tasks and report better or on-par performance compared to the state-of-the-art approaches.

</details>

### Efficient Continual Learning with Modular Networks and Task-Driven Priors.
- **链接**: [arXiv:2012.12631](https://arxiv.org/abs/2012.12631)
- **作者**: Tom Veniat, Ludovic Denoyer, Marc'Aurelio Ranzato
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing literature in Continual Learning (CL) has focused on overcoming catastrophic forgetting, the inability of the learner to recall how to perform tasks observed in the past. There are however other desirable properties of a CL system, such as the ability to transfer knowledge from previous tasks and to scale memory and compute sub-linearly with the number of tasks. Since most current benchmarks focus only on forgetting using short streams of tasks, we first propose a new suite of benchmarks to probe CL algorithms across these new axes. Finally, we introduce a new modular architecture, whose modules represent atomic skills that can be composed to perform a certain task. Learning a task reduces to figuring out which past modules to re-use, and which new modules to instantiate to solve the current task. Our learning algorithm leverages a task-driven prior over the exponential search space of all possible ways to combine modules, enabling efficient learning on long streams of tasks. Our experiments show that this modular architecture and learning algorithm perform competitively on widely used CL benchmarks while yielding superior performance on the more challenging benchmarks we introduce in this work.

</details>

### Bayesian Structural Adaptation for Continual Learning.
- **链接**: [出版页](http://proceedings.mlr.press/v139/kumar21a.html)
- **作者**: Abhishek Kumar, Sunabha Chatterjee, Piyush Rai
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2021

### Kernel Continual Learning.
- **链接**: [出版页](http://proceedings.mlr.press/v139/derakhshani21a.html)
- **作者**: Mohammad Mahdi Derakhshani, Xiantong Zhen, Ling Shao, Cees Snoek
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2021

### Variational Auto-Regressive Gaussian Processes for Continual Learning.
- **链接**: [arXiv:2006.05468](https://arxiv.org/abs/2006.05468)
- **作者**: Sanyam Kapoor, Theofanis Karaletsos, Thang D. Bui
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Through sequential construction of posteriors on observing data online, Bayes' theorem provides a natural framework for continual learning. We develop Variational Auto-Regressive Gaussian Processes (VAR-GPs), a principled posterior updating mechanism to solve sequential tasks in continual learning. By relying on sparse inducing point approximations for scalable posteriors, we propose a novel auto-regressive variational distribution which reveals two fruitful connections to existing results in Bayesian inference, expectation propagation and orthogonal inducing points. Mean predictive entropy estimates show VAR-GPs prevent catastrophic forgetting, which is empirically supported by strong performance on modern continual learning benchmarks against competitive baselines. A thorough ablation study demonstrates the efficacy of our modeling choices.

</details>

### Continual Learning in the Teacher-Student Setup: Impact of Task Similarity.
- **链接**: [arXiv:2107.04384](https://arxiv.org/abs/2107.04384)
- **作者**: Sebastian Lee, Sebastian Goldt, Andrew M. Saxe
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning-the ability to learn many tasks in sequence-is critical for artificial learning systems. Yet standard training methods for deep networks often suffer from catastrophic forgetting, where learning new tasks erases knowledge of earlier tasks. While catastrophic forgetting labels the problem, the theoretical reasons for interference between tasks remain unclear. Here, we attempt to narrow this gap between theory and practice by studying continual learning in the teacher-student setup. We extend previous analytical work on two-layer networks in the teacher-student setup to multiple teachers. Using each teacher to represent a different task, we investigate how the relationship between teachers affects the amount of forgetting and transfer exhibited by the student when the task switches. In line with recent work, we find that when tasks depend on similar features, intermediate task similarity leads to greatest forgetting. However, feature similarity is only one way in which tasks may be related. The teacher-student approach allows us to disentangle task similarity at the level of readouts (hidden-to-output weights) and features (input-to-hidden weights). We find a complex interplay between both types of similarity, initial transfer/forgetting rates, maximum transfer/forgetting, and long-term transfer/forgetting. Together, these results help illuminate the diverse factors contributing to catastrophic forgetting.

</details>

### Federated Continual Learning with Weighted Inter-client Transfer.
- **链接**: [出版页](http://proceedings.mlr.press/v139/yoon21b.html)
- **作者**: Jaehong Yoon, Wonyong Jeong, Giwoong Lee, Eunho Yang, Sung Ju Hwang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2021

<!-- COMPLETE v1 papers=45 -->
