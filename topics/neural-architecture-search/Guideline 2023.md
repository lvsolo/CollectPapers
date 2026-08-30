# Neural Architecture Search — 2023 Guideline

> 领域: 神经架构搜索（NAS、Zero-Cost、搜索空间）
> 论文数: 5 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份:

### MDL-NAS: A Joint Multi-domain Learning Framework for Vision Transformer. **⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01924) · 📚 被引 16
- **作者**: Shiguang Wang, Tao Xie, Jian Cheng, Xingcheng Zhang, Haijun Liu
- **🏷️ 机构**: University of Electronic Science and Technology of China, Harbin Institute of Technology, SenseTime Research
- **会议**: CVPR 2023
- **摘要（中）**: ①针对Vision Transformer在多领域联合学习中的架构设计问题。②提出了MDL-NAS，一个联合多领域学习的NAS框架。③相比单领域NAS，支持跨领域共享与特定架构搜索。④摘要未给出具体数据，但框架旨在提升多任务泛化能力。
- **摘要（英）**: This paper addresses architecture design for Vision Transformers in joint multi-domain learning. It proposes MDL-NAS, a NAS framework for multi-domain learning. Compared to single-domain NAS, it supports cross-domain sharing and specific architecture search. The abstract lacks specific data, but the framework aims to improve multi-task generalization.
- **核心贡献**: 提出了面向Vision Transformer的联合多领域NAS框架。
- **创新点**: 在多领域学习中联合搜索共享与特定架构。
- **结果**: 旨在提升多任务泛化，具体效果未在摘要中量化。

### DisWOT: Student Architecture Search for Distillation WithOut Training. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01145) · 📚 被引 60
- **作者**: Peijie Dong, Lujun Li, Zimian Wei
- **🏷️ 机构**: National University of Defense Technology, Chinese Academy of Sciences
- **会议**: CVPR 2023
- **摘要（中）**: ①针对知识蒸馏中学生架构搜索需要训练成本高的问题。②提出了DisWOT，一种无需训练的学生架构搜索方法。③相比现有方法，通过蒸馏损失代理指标实现零训练搜索。④摘要未给出具体数据，但方法显著降低搜索成本。
- **摘要（英）**: This paper addresses the high training cost of student architecture search in knowledge distillation. It proposes DisWOT, a training-free student architecture search method. Compared to existing methods, it uses distillation loss proxies for zero-training search. The abstract lacks specific data, but the method significantly reduces search cost.
- **核心贡献**: 提出了无需训练的知识蒸馏学生架构搜索方法。
- **创新点**: 利用蒸馏代理指标实现零训练架构搜索。
- **结果**: 显著降低搜索成本，具体性能未在摘要中量化。

### Adversarially Robust Neural Architecture Search for Graph Neural Networks. **⭐⭐⭐⭐** (相关度: 65%)
- **链接**: [arXiv:2304.04168](https://arxiv.org/abs/2304.04168) · 📚 被引 21
- **作者**: Beini Xie, Heng Chang, Ziwei Zhang, Xin Wang, Daixin Wang, Zhiqiang Zhang et al.
- **🏷️ 机构**: Tsinghua University, Ant Group, Yale University
- **会议**: CVPR 2023
- **摘要（中）**: ①针对图神经网络易受对抗攻击且现有防御方法缺乏架构级鲁棒性的问题。②提出了G-RNA，一个面向GNN的鲁棒NAS框架，设计包含图结构掩码操作的搜索空间，并定义鲁棒性度量引导搜索。③相比现有图NAS，首次从架构角度增强鲁棒性。④摘要未给出具体数据，但框架能有效搜索最优防御架构。
- **摘要（英）**: This paper addresses GNN vulnerability to adversarial attacks and the lack of architectural robustness in existing defenses. It proposes G-RNA, a robust NAS framework for GNNs, designing a search space with graph structure mask operations and a robustness metric. Compared to existing graph NAS, it enhances robustness from an architectural perspective. The abstract lacks specific data, but the framework effectively searches optimal defensive architectures.
- **核心贡献**: 提出了面向GNN的鲁棒NAS框架G-RNA。
- **创新点**: 将图结构掩码操作和鲁棒性度量融入NAS搜索空间。
- **结果**: 有效搜索防御架构，具体性能未在摘要中量化。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Graph Neural Networks (GNNs) obtain tremendous success in modeling relational data. Still, they are prone to adversarial attacks, which are massive threats to applying GNNs to risk-sensitive domains. Existing defensive methods neither guarantee performance facing new data/tasks or adversarial attacks nor provide insights to understand GNN robustness from an architectural perspective. Neural Architecture Search (NAS) has the potential to solve this problem by automating GNN architecture designs. Nevertheless, current graph NAS approaches lack robust design and are vulnerable to adversarial attacks. To tackle these challenges, we propose a novel Robust Neural Architecture search framework for GNNs (G-RNA). Specifically, we design a robust search space for the message-passing mechanism by adding graph structure mask operations into the search space, which comprises various defensive operation candidates and allows us to search for defensive GNNs. Furthermore, we define a robustness metric to guide the search procedure, which helps to filter robust architectures. In this way, G-RNA helps understand GNN robustness from an architectural perspective and effectively searches for optimal adversarial robust GNNs. Extensive experimental results on benchmark datasets show that G-RNA significantly outperforms manually designed robust GNNs and vanilla graph NAS baselines by 12.1% to 23.4% under adversarial attacks.

</details>

### Evolutionary Neural Architecture Search for Transformer in Knowledge Tracing. **⭐⭐** (相关度: 10%)
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/3e53d82a1113e3d240059a9195668edc-Abstract-Conference.html)
- **作者**: Shangshang Yang, Xiaoshan Yu, Ye Tian, Xueming Yan, Haiping Ma, Xingyi Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023
- **摘要（中）**: ①该论文针对知识追踪（Knowledge Tracing）任务中Transformer架构的人工设计依赖问题，提出使用进化神经架构搜索（NAS）自动搜索最优Transformer结构。②方法上，采用进化算法在搜索空间中迭代优化Transformer的层数、头数、维度等超参数，并利用代理模型加速评估。③相比手工设计的Transformer，该方法能自动适应知识追踪数据的特性，减少人工调参成本。④摘要未提供具体性能数据，但声称搜索到的架构在基准数据集上优于基线模型。
- **摘要（英）**: This paper addresses the manual design dependency of Transformer architectures in Knowledge Tracing by proposing an evolutionary neural architecture search (NAS) method to automatically discover optimal structures. It employs evolutionary algorithms to iteratively optimize hyperparameters like layer count, heads, and dimensions, with surrogate models for efficient evaluation. Compared to hand-crafted Transformers, it reduces tuning effort and adapts to data characteristics, though no specific numeric results are provided in the abstract.
- **核心贡献**: 提出将进化NAS应用于知识追踪的Transformer架构搜索。
- **创新点**: 将进化算法与Transformer架构搜索结合，实现自动化设计。
- **结果**: 声称在基准数据集上优于基线，但缺乏具体数据支撑。

### HOTNAS: Hierarchical Optimal Transport for Neural Architecture Search. **⭐⭐⭐** (相关度: 50%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01154) · 📚 被引 15
- **作者**: Jiechao Yang, Yong Liu, Hongteng Xu
- **🏷️ 机构**: Gaoling School of Artificial Intelligence, Renmin University of China,Beijing,China
- **会议**: CVPR 2023
- **摘要（中）**: ①针对NAS中架构距离度量不准确的问题。②提出了HOTNAS，基于层次最优传输的NAS方法。③相比现有方法，利用最优传输理论改进架构相似性度量。④摘要未给出具体数据，但旨在提升搜索效率与准确性。
- **摘要（英）**: This paper addresses inaccurate architecture distance metrics in NAS. It proposes HOTNAS, a hierarchical optimal transport-based NAS method. Compared to existing methods, it improves architecture similarity measurement using optimal transport theory. The abstract lacks specific data, but it aims to enhance search efficiency and accuracy.
- **核心贡献**: 提出了基于层次最优传输的NAS方法。
- **创新点**: 将最优传输理论应用于架构距离度量。
- **结果**: 旨在提升搜索效率与准确性，具体效果未在摘要中量化。

### Differentiable Architecture Search with Random Features. **⭐⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2208.08835](https://arxiv.org/abs/2208.08835) · 📚 被引 18
- **作者**: Xuanyang Zhang, Yonggang Li, Xiangyu Zhang, Yongtao Wang, Jian Sun
- **🏷️ 机构**: MEGVII Technology, Peking University
- **会议**: CVPR 2023
- **摘要（中）**: ①针对DARTS在架构搜索中出现的性能崩溃问题。②提出仅训练BatchNorm的DARTS新范式，并引入随机特征（Random Features）来稀释跳跃连接在超网络优化中的辅助作用，使搜索算法更公平地选择操作。③相比原DARTS，通过理论分析和实验验证了随机特征的有效性，并实例化为RF-DARTS和RF-PCDARTS。④在CIFAR-10上达到94.36%测试准确率（NAS-Bench-201中最优结果），迁移到ImageNet上取得24.0%的top-1错误率，且在多个数据集上表现稳健。
- **摘要（英）**: This paper addresses the performance collapse issue in DARTS by proposing a new paradigm that trains only BatchNorm and introducing random features to dilute the auxiliary role of skip-connections, enabling fairer operation selection. The improved RF-DARTS achieves 94.36% accuracy on CIFAR-10 and 24.0% top-1 error on ImageNet, demonstrating robustness across datasets.
- **核心贡献**: 提出随机特征机制和仅训练BatchNorm的DARTS变体，有效缓解性能崩溃。
- **创新点**: 利用随机特征稀释跳跃连接影响，实现更公平的架构搜索。
- **结果**: 在CIFAR-10和ImageNet上取得最优或接近最优的性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Differentiable architecture search (DARTS) has significantly promoted the development of NAS techniques because of its high search efficiency and effectiveness but suffers from performance collapse. In this paper, we make efforts to alleviate the performance collapse problem for DARTS from two aspects. First, we investigate the expressive power of the supernet in DARTS and then derive a new setup of DARTS paradigm with only training BatchNorm. Second, we theoretically find that random features dilute the auxiliary connection role of skip-connection in supernet optimization and enable search algorithm focus on fairer operation selection, thereby solving the performance collapse problem. We instantiate DARTS and PC-DARTS with random features to build an improved version for each named RF-DARTS and RF-PCDARTS respectively. Experimental results show that RF-DARTS obtains \textbf{94.36\%} test accuracy on CIFAR-10 (which is the nearest optimal result in NAS-Bench-201), and achieves the newest state-of-the-art top-1 test error of \textbf{24.0\%} on ImageNet when transferring from CIFAR-10. Moreover, RF-DARTS performs robustly across three datasets (CIFAR-10, CIFAR-100, and SVHN) and four search spaces (S1-S4). Besides, RF-PCDARTS achieves even better results on ImageNet, that is, \textbf{23.9\%} top-1 and \textbf{7.1\%} top-5 test error, surpassing representative methods like single-path, training-free, and partial-channel paradigms directly searched on ImageNet.

</details>

### Extensible and Efficient Proxy for Neural Architecture Search. **⭐⭐** (相关度: 45%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00570) · 📚 被引 11
- **作者**: Yuhong Li, Jiajie Li, Cong Hao, Pan Li, Jinjun Xiong, Deming Chen
- **🏷️ 机构**: University of Illinois at Urbana-Champaign, University at Buffalo, Georgia Institute of Technology
- **会议**: ICCV 2023
- **摘要（中）**: ①该论文摘要为空，无法获取具体研究问题。②从标题推测，研究可扩展且高效的NAS代理方法。③可能旨在提高NAS搜索效率。④由于缺乏摘要和实验数据，无法评估具体效果。
- **摘要（英）**: The abstract is empty, so the specific problem is unclear. Based on the title, it likely focuses on developing extensible and efficient proxies for NAS, but no details or results are available.
- **核心贡献**: 未知，因摘要缺失。
- **创新点**: 未知，因摘要缺失。
- **结果**: 未知，因摘要缺失。

### An Experimental Protocol for Neural Architecture Search in Super-Resolution. **⭐⭐⭐** (相关度: 40%)
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00447) · 📚 被引 2
- **作者**: Jesús Leopoldo Llano García, Raúl Monroy, Víctor Adrián Sosa-Hernández
- **🏷️ 机构**: School of Engineering and Sciences,Tecnologico de Monterrey,Mexico,52926
- **会议**: ICCV 2023
- **摘要（中）**: ①针对超分辨率任务中NAS实验协议不统一、结果难以比较的问题。②提出一个标准化的实验协议，用于超分辨率NAS的评估和比较。③可能包括数据集、训练设置、评估指标等规范化。④由于摘要为空，具体效果未知，但旨在提升研究可复现性。
- **摘要（英）**: This paper proposes a standardized experimental protocol for NAS in super-resolution to address inconsistent evaluation practices. It likely specifies datasets, training settings, and metrics, but details are unavailable due to the empty abstract.
- **核心贡献**: 提出超分辨率NAS的实验协议。
- **创新点**: 标准化评估流程。
- **结果**: 未知，因摘要缺失。

### DONNAv2 - Lightweight Neural Architecture Search for Vision tasks. **⭐⭐⭐** (相关度: 40%)
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00149) · 📚 被引 3
- **作者**: Sweta Priyadarshi, Tianyu Jiang, Hsin-Pai Cheng, Sendil Krishna, Viswanath Ganapathy, Chirag Patel
- **🏷️ 机构**: Qualcomm AI Research,San Diego,CA,USA,92121
- **会议**: ICCV 2023
- **摘要（中）**: ①针对视觉任务中神经架构搜索（NAS）计算开销大的问题。②提出了DONNAv2，一种轻量级NAS方法，旨在高效搜索视觉任务的架构。③相比已有工作，可能通过改进搜索策略或代理模型来降低计算成本。④摘要缺失，无法提供具体效果数据。
- **摘要（英）**: ①Addresses the high computational cost of NAS for vision tasks. ②Proposes DONNAv2, a lightweight NAS method for efficient architecture search. ③Improves upon prior work by potentially reducing search overhead. ④Effectiveness not detailed due to missing abstract.
- **核心贡献**: 提出轻量级NAS方法DONNAv2，降低视觉任务架构搜索成本。
- **创新点**: 轻量化设计可能引入高效搜索策略。
- **结果**: 效果未明确，因摘要缺失。

### InstaTune: Instantaneous Neural Architecture Search During Fine-Tuning. **⭐⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2308.15609](https://arxiv.org/abs/2308.15609) · 📚 被引 3
- **作者**: Sharath Nittur Sridhar, Souvik Kundu, Sairam Sundaresan, Maciej Szankin, Anthony Sarah
- **🏷️ 机构**: Intel Labs,San Diego,USA
- **会议**: ICCV 2023
- **摘要（中）**: ①针对One-Shot NAS训练超网络耗时且需从头训练的问题。②提出InstaTune，在微调阶段利用预训练权重生成超网络，并提取子网络。③改进点在于无需从头训练，节省时间和计算资源，且子网络针对目标任务优化。④通过多目标进化搜索，但摘要未提供具体性能数据。
- **摘要（英）**: ①Addresses the time-consuming training of super-networks in One-Shot NAS. ②Proposes InstaTune, which leverages pre-trained weights to generate super-networks during fine-tuning. ③Improves by avoiding scratch training and optimizing sub-networks for target tasks. ④Uses multi-objective evolutionary search, but specific results are not provided.
- **核心贡献**: 提出微调阶段生成超网络的NAS方法，降低计算开销。
- **创新点**: 利用预训练权重在微调中构建超网络，实现即插即用。
- **结果**: 具体效果未给出，但理论上节省大量资源。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> One-Shot Neural Architecture Search (NAS) algorithms often rely on training a hardware agnostic super-network for a domain specific task. Optimal sub-networks are then extracted from the trained super-network for different hardware platforms. However, training super-networks from scratch can be extremely time consuming and compute intensive especially for large models that rely on a two-stage training process of pre-training and fine-tuning. State of the art pre-trained models are available for a wide range of tasks, but their large sizes significantly limits their applicability on various hardware platforms. We propose InstaTune, a method that leverages off-the-shelf pre-trained weights for large models and generates a super-network during the fine-tuning stage. InstaTune has multiple benefits. Firstly, since the process happens during fine-tuning, it minimizes the overall time and compute resources required for NAS. Secondly, the sub-networks extracted are optimized for the target task, unlike prior work that optimizes on the pre-training objective. Finally, InstaTune is easy to "plug and play" in existing frameworks. By using multi-objective evolutionary search algorithms along with lightly trained predictors, we find Pareto-optimal sub-networks that outperform their respective baselines across different performance objectives such as accuracy and MACs. Specifically, we demonstrate that our approach performs well across both unimodal (ViT and BERT) and multi-modal (BEiT-3) transformer based architectures.

</details>

### Multi-task Graph Neural Architecture Search with Task-aware Collaboration and Curriculum. **⭐⭐⭐⭐** (相关度: 65%)
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/4e839c9c398c58c878a394633b806ccd-Abstract-Conference.html)
- **作者**: Yijian Qin, Xin Wang, Ziwei Zhang, Hong Chen, Wenwu Zhu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023
- **摘要（中）**: ①针对多任务图神经网络架构搜索中任务间冲突和搜索效率低的问题。②提出MTG-NAS，引入任务感知协作机制和课程学习策略，动态调整任务权重和搜索顺序。③相比单任务NAS，更好地平衡多任务性能。④在多个多任务图数据集上，MTG-NAS在各项任务上均优于现有方法。
- **摘要（英）**: ①Addresses task conflicts and low search efficiency in multi-task GNN architecture search. ②Proposes MTG-NAS with task-aware collaboration and curriculum learning to dynamically adjust task weights and search order. ③Better balances multi-task performance than single-task NAS. ④Outperforms existing methods on multiple multi-task graph datasets.
- **核心贡献**: 提出任务感知协作与课程学习的多任务GNN NAS。
- **创新点**: 动态任务权重和课程搜索策略。
- **结果**: 多任务性能全面优于现有方法。

### Construction of Hierarchical Neural Architecture Search Spaces based on Context-free Grammars. **⭐⭐⭐** (相关度: 55%)
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/4869f3f967dfe954439408dd92c50ee1-Abstract-Conference.html)
- **作者**: Simon Schrodi, Danny Stoll, Binxin Ru, Rhea Sanjay Sukthanker, Thomas Brox, Frank Hutter
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023
- **摘要（中）**: ①针对NAS搜索空间设计缺乏层次性和可扩展性的问题。②提出基于上下文无关文法的层次化搜索空间构建方法，通过文法规则生成结构化架构。③相比扁平搜索空间，支持更复杂和可解释的架构。④在图像分类任务上，搜索到的层次架构性能优于手工设计。
- **摘要（英）**: ①Addresses the lack of hierarchy and scalability in NAS search space design. ②Proposes a hierarchical search space construction based on context-free grammars, generating structured architectures via grammar rules. ③Supports more complex and interpretable architectures than flat spaces. ④On image classification, searched hierarchical architectures outperform manual designs.
- **核心贡献**: 提出基于文法的层次化NAS搜索空间构建方法。
- **创新点**: 用上下文无关文法定义层次化架构空间。
- **结果**: 搜索架构性能优于手工设计。

### Evolutionary Neural Architecture Search for Transformer in Knowledge Tracing. **⭐⭐** (相关度: 10%)
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/3e53d82a1113e3d240059a9195668edc-Abstract-Conference.html)
- **作者**: Shangshang Yang, Xiaoshan Yu, Ye Tian, Xueming Yan, Haiping Ma, Xingyi Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023
- **摘要（中）**: ①该论文针对知识追踪（Knowledge Tracing）任务中Transformer架构的人工设计依赖问题，提出使用进化神经架构搜索（NAS）自动搜索最优Transformer结构。②方法上，采用进化算法在搜索空间中迭代优化Transformer的层数、头数、维度等超参数，并利用代理模型加速评估。③相比手工设计的Transformer，该方法能自动适应知识追踪数据的特性，减少人工调参成本。④摘要未提供具体性能数据，但声称搜索到的架构在基准数据集上优于基线模型。
- **摘要（英）**: This paper addresses the manual design dependency of Transformer architectures in Knowledge Tracing by proposing an evolutionary neural architecture search (NAS) method to automatically discover optimal structures. It employs evolutionary algorithms to iteratively optimize hyperparameters like layer count, heads, and dimensions, with surrogate models for efficient evaluation. Compared to hand-crafted Transformers, it reduces tuning effort and adapts to data characteristics, though no specific numeric results are provided in the abstract.
- **核心贡献**: 提出将进化NAS应用于知识追踪的Transformer架构搜索。
- **创新点**: 将进化算法与Transformer架构搜索结合，实现自动化设计。
- **结果**: 声称在基准数据集上优于基线，但缺乏具体数据支撑。

### Unsupervised Graph Neural Architecture Search with Disentangled Self-Supervision.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/e78399fc43dbb2d87b7e1e6906ce5baf-Abstract-Conference.html) · 📚 被引 1
- **作者**: Zeyang Zhang, Xin Wang, Ziwei Zhang, Guangyao Shen, Shiqi Shen, Wenwu Zhu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

## 🆕 增量新增

### EA-HAS-Bench: Energy-aware Hyperparameter and Architecture Search Benchmark. **⭐⭐** (相关度: 30%)
- **链接**: [出版页](https://openreview.net/forum?id=n-bvaLSCC78)
- **作者**: Shuguang Dou, Xinyang Jiang, Cairong Zhao, Dongsheng Li
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023
- **摘要（中）**: ①这篇论文针对神经网络架构搜索（NAS）中忽略能耗约束的问题，提出一个能量感知的超参数和架构搜索基准。②论文构建了包含能耗指标的基准测试环境，用于评估不同架构和超参数组合的能耗效率。③相比现有NAS基准，该工作首次将能耗作为核心评估维度，强调绿色计算。④摘要未提供具体数据，但基准的建立为后续研究提供了标准化平台。
- **摘要（英）**: This paper addresses the lack of energy consumption constraints in neural architecture search (NAS) by proposing an energy-aware benchmark for hyperparameter and architecture search. It constructs a benchmark environment that includes energy metrics to evaluate the efficiency of different architectures and hyperparameters. Compared to existing NAS benchmarks, this work is the first to incorporate energy as a core evaluation dimension, emphasizing green computing. The abstract does not provide specific data, but the benchmark offers a standardized platform for future research.
- **核心贡献**: 提出了首个能量感知的NAS基准，推动能耗效率评估。
- **创新点**: 将能耗指标引入NAS基准设计。
- **结果**: 建立了标准化能耗评估平台，但具体效果未在摘要中量化。

### QAS-Bench: Rethinking Quantum Architecture Search and A Benchmark. **⭐⭐** (相关度: 20%)
- **链接**: [出版页](https://proceedings.mlr.press/v202/lu23f.html)
- **作者**: Xudong Lu, Kaisen Pan, Ge Yan, Jiaming Shan, Wenjie Wu, Junchi Yan
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023
- **摘要（中）**: ①这篇论文针对量子架构搜索（QAS）领域缺乏统一基准的问题，提出QAS-Bench基准。②论文重新思考了量子架构搜索的评估方法，并构建了一个包含多种量子架构的基准数据集。③相比现有工作，该基准提供了标准化的评估协议，促进量子计算与NAS的交叉研究。④摘要未提供具体性能数据，但基准的建立有助于比较不同QAS算法。
- **摘要（英）**: This paper addresses the lack of unified benchmarks in quantum architecture search (QAS) by proposing QAS-Bench. It rethinks evaluation methods for QAS and constructs a benchmark dataset containing various quantum architectures. Compared to existing work, this benchmark provides standardized evaluation protocols, promoting cross-disciplinary research between quantum computing and NAS. The abstract does not provide specific performance data, but the benchmark facilitates comparison of different QAS algorithms.
- **核心贡献**: 提出了量子架构搜索的标准化基准QAS-Bench。
- **创新点**: 重新定义QAS评估协议。
- **结果**: 提供了比较平台，但具体效果未量化。

### ElasticViT: Conflict-aware Supernet Training for Deploying Fast Vision Transformer on Diverse Mobile Devices. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2303.09730](https://arxiv.org/abs/2303.09730) · 📚 被引 18
- **作者**: Chen Tang, Li Lyna Zhang, Huiqiang Jiang, Jiahang Xu, Ting Cao, Quanlu Zhang et al.
- **🏷️ 机构**: Tsinghua University, Microsoft Research
- **会议**: ICCV 2023
- **摘要（中）**: ①针对在多样移动设备上设计轻量级低延迟ViT模型的挑战，现有NAS方法多关注高FLOPs模型。②提出了ElasticViT，一种两阶段NAS方法，先在大搜索空间上训练高质量ViT超网，再搜索最优子网直接部署。③针对均匀采样导致的梯度冲突问题，提出了复杂度感知采样和性能感知采样两种技术，前者限制相邻训练步骤中子网的FLOPs差异，后者选择高精度子网以减少冲突。④实验表明ElasticViT能高效搜索出适应不同移动设备的低延迟模型，在精度和延迟权衡上优于现有方法。
- **摘要（英）**: This paper tackles the challenge of designing lightweight ViT models for diverse mobile devices by proposing ElasticViT, a two-stage NAS approach with a large search space and optimal subnet search. It introduces complexity-aware and performance-aware sampling to mitigate gradient conflicts in supernet training, achieving superior accuracy-latency trade-offs across devices.
- **核心贡献**: 提出ElasticViT框架和两种采样技术，解决超网训练梯度冲突。
- **创新点**: 复杂度感知和性能感知采样策略，提升超网训练稳定性和子网质量。
- **结果**: 在多种移动设备上实现低延迟和高精度的ViT模型。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural Architecture Search (NAS) has shown promising performance in the automatic design of vision transformers (ViT) exceeding 1G FLOPs. However, designing lightweight and low-latency ViT models for diverse mobile devices remains a big challenge. In this work, we propose ElasticViT, a two-stage NAS approach that trains a high-quality ViT supernet over a very large search space that supports a wide range of mobile devices, and then searches an optimal sub-network (subnet) for direct deployment. However, prior supernet training methods that rely on uniform sampling suffer from the gradient conflict issue: the sampled subnets can have vastly different model sizes (e.g., 50M vs. 2G FLOPs), leading to different optimization directions and inferior performance. To address this challenge, we propose two novel sampling techniques: complexity-aware sampling and performance-aware sampling. Complexity-aware sampling limits the FLOPs difference among the subnets sampled across adjacent training steps, while covering different-sized subnets in the search space. Performance-aware sampling further selects subnets that have good accuracy, which can reduce gradient conflicts and improve supernet quality. Our discovered models, ElasticViT models, achieve top-1 accuracy from 67.2% to 80.0% on ImageNet from 60M to 800M FLOPs without extra retraining, outperforming all prior CNNs and ViTs in terms of accuracy and latency. Our tiny and small models are also the first ViT models that surpass state-of-the-art CNNs with significantly lower latency on mobile devices. For instance, ElasticViT-S1 runs 2.62x faster than EfficientNet-B0 with 0.1% higher accuracy.

</details>

### Enhancing Differentiable Architecture Search: A Study on Small Number of Cell Blocks in the Search Stage, and Important Branches-based Cells Selection. **⭐⭐** (相关度: 50%)
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00135)
- **作者**: Bedionita Soro, Chong Song
- **🏷️ 机构**: KAIST AI,South Korea
- **会议**: ICCV 2023
- **摘要（中）**: ①针对可微分架构搜索中搜索阶段使用少量单元块的问题，以及基于重要分支的单元选择方法。②摘要为空，无法获取具体方法细节。③缺乏具体信息，无法评估改进点。④无实验数据。
- **摘要（英）**: This paper discusses enhancing differentiable architecture search by using a small number of cell blocks in the search stage and important branches-based cell selection, but the abstract is empty, providing no details on methods or results.
- **核心贡献**: 未明确。
- **创新点**: 未明确。
- **结果**: 未提供。

### MixPath: A Unified Approach for One-shot Neural Architecture Search. **⭐⭐⭐⭐** (相关度: 55%)
- **链接**: [arXiv:2001.05887](https://arxiv.org/abs/2001.05887) · 📚 被引 15
- **作者**: Xiangxiang Chu, Shun Lu, Xudong Li, Bo Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023
- **摘要（中）**: ①针对现有单路径搜索空间限制，多路径结构模型搜索困难的问题。②提出了MixPath，一种统一的多路径one-shot NAS方法，训练一个多路径超网来准确评估候选架构。③发现多路径特征和与单路径特征存在倍数关系，导致超网训练不稳定，因此提出阴影批归一化（SBN）来正则化特征统计差异。④实验证明SBN能稳定优化并提升排序性能，生成的模型在ImageNet上达到最先进结果。
- **摘要（英）**: This paper proposes MixPath, a unified one-shot NAS approach for multi-path search spaces, addressing the challenge of searching multi-path structures. It introduces Shadow Batch Normalization to regularize disparate feature statistics, stabilizing supernet training and improving ranking, achieving state-of-the-art results on ImageNet.
- **核心贡献**: 提出MixPath和SBN，实现多路径one-shot NAS。
- **创新点**: 阴影批归一化解决多路径特征统计差异问题。
- **结果**: 在ImageNet上生成系列模型，达到最先进性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Blending multiple convolutional kernels is proved advantageous in neural architecture design. However, current two-stage neural architecture search methods are mainly limited to single-path search spaces. How to efficiently search models of multi-path structures remains a difficult problem. In this paper, we are motivated to train a one-shot multi-path supernet to accurately evaluate the candidate architectures. Specifically, we discover that in the studied search spaces, feature vectors summed from multiple paths are nearly multiples of those from a single path. Such disparity perturbs the supernet training and its ranking ability. Therefore, we propose a novel mechanism called Shadow Batch Normalization (SBN) to regularize the disparate feature statistics. Extensive experiments prove that SBNs are capable of stabilizing the optimization and improving ranking performance. We call our unified multi-path one-shot approach as MixPath, which generates a series of models that achieve state-of-the-art results on ImageNet.

</details>

### Improving Differentiable Neural Architecture Search by Encouraging Transferability. **⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://openreview.net/forum?id=Tl8OmiibP99)
- **作者**: Parth Sheth, Pengtao Xie
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023
- **摘要（中）**: ①针对可微分NAS（DARTS）搜索到的架构泛化性差、迁移性不足的问题。②提出了鼓励可迁移性的改进方法，可能通过正则化或约束搜索过程。③改进点在于提升架构在不同数据集或任务上的表现。④摘要未提供具体数据。
- **摘要（英）**: ①Addresses the poor generalization and transferability of architectures found by differentiable NAS. ②Proposes improvements to encourage transferability, possibly via regularization or search constraints. ③Aims to enhance performance across datasets/tasks. ④No specific results provided.
- **核心贡献**: 改进可微分NAS以提升架构可迁移性。
- **创新点**: 引入可迁移性鼓励机制。
- **结果**: 未提供具体数据。

### AutoGT: Automated Graph Transformer Architecture Search. **⭐⭐⭐** (相关度: 50%)
- **链接**: [出版页](https://openreview.net/forum?id=GcM7qfl5zY)
- **作者**: Zizhao Zhang, Xin Wang, Chaoyu Guan, Ziwei Zhang, Haoyang Li, Wenwu Zhu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023
- **摘要（中）**: ①针对图神经网络架构搜索（GAS）中手工设计依赖专家经验的问题。②提出了AutoGT，自动化图Transformer架构搜索方法。③改进点在于将NAS应用于图Transformer，扩展了搜索空间。④摘要未提供具体数据。
- **摘要（英）**: ①Addresses the reliance on expert knowledge in manual graph neural network design. ②Proposes AutoGT, an automated search method for graph Transformer architectures. ③Extends NAS to graph Transformers. ④No specific results provided.
- **核心贡献**: 提出图Transformer架构自动搜索方法。
- **创新点**: 将NAS应用于图Transformer。
- **结果**: 未提供具体数据。

### Meta-prediction Model for Distillation-Aware NAS on Unseen Datasets. **⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://openreview.net/forum?id=SEh5SfEQtqB)
- **作者**: Hayeon Lee, Sohyun An, Minseon Kim, Sung Ju Hwang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023
- **摘要（中）**: ①针对NAS在未见数据集上性能下降的问题。②提出了元预测模型，用于蒸馏感知的NAS，以预测架构在新数据集上的表现。③改进点在于利用元学习提升跨数据集泛化能力。④摘要未提供具体数据。
- **摘要（英）**: ①Addresses performance degradation of NAS on unseen datasets. ②Proposes a meta-prediction model for distillation-aware NAS to predict architecture performance. ③Improves cross-dataset generalization via meta-learning. ④No specific results provided.
- **核心贡献**: 提出元预测模型提升NAS在未见数据集上的表现。
- **创新点**: 结合元学习和蒸馏感知。
- **结果**: 未提供具体数据。

### Shortest Edit Path Crossover: A Theory-driven Solution to the Permutation Problem in Evolutionary Neural Architecture Search. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://proceedings.mlr.press/v202/qiu23b.html)
- **作者**: Xin Qiu, Risto Miikkulainen
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023
- **摘要（中）**: ①针对进化NAS中排列问题（permutation problem）导致交叉操作效率低的问题。②提出了最短编辑路径交叉（Shortest Edit Path Crossover），一种理论驱动的解决方案。③改进点在于通过理论分析设计交叉算子，避免排列问题，提升搜索效率。④摘要未提供具体数据，但强调理论驱动和有效性。
- **摘要（英）**: ①Addresses the permutation problem in evolutionary NAS that hinders effective crossover. ②Proposes Shortest Edit Path Crossover, a theory-driven solution. ③Improves search efficiency by designing a crossover operator that avoids permutation issues. ④No specific results, but emphasizes theoretical grounding.
- **核心贡献**: 提出理论驱动的交叉算子解决进化NAS排列问题。
- **创新点**: 最短编辑路径交叉设计。
- **结果**: 未提供具体数据，但强调效率提升。

### PreNAS: Preferred One-Shot Learning Towards Efficient Neural Architecture Search. **⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://proceedings.mlr.press/v202/wang23f.html)
- **作者**: Haibin Wang, Ce Ge, Hesen Chen, Xiuyu Sun
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023
- **摘要（中）**: ①针对传统one-shot NAS中搜索空间与训练策略不匹配、导致搜索到的最优架构性能不佳的问题。②提出PreNAS，通过偏好感知的one-shot训练，在超网络训练中优先优化高潜力架构，并采用渐进式采样策略。③相比标准one-shot方法，PreNAS在训练过程中动态调整架构分布，减少低质量架构的干扰。④在多个基准数据集上，PreNAS搜索到的架构在分类任务上取得了优于随机搜索和经典one-shot方法的准确率，且搜索成本显著降低。
- **摘要（英）**: This paper addresses the mismatch between search space and training strategy in one-shot NAS, which degrades the performance of searched architectures. It proposes PreNAS, a preference-aware one-shot training method that prioritizes high-potential architectures during supernet training via progressive sampling. Compared to standard one-shot approaches, PreNAS achieves higher accuracy on benchmark datasets with reduced search cost.
- **核心贡献**: 提出偏好感知的one-shot训练策略，提升搜索架构质量。
- **创新点**: 在超网络训练中动态调整架构采样分布，实现偏好引导。
- **结果**: 在多个基准上取得更优准确率，搜索成本降低。

### QuantumDARTS: Differentiable Quantum Architecture Search for Variational Quantum Algorithms. **⭐⭐** (相关度: 30%)
- **链接**: [出版页](https://proceedings.mlr.press/v202/wu23v.html)
- **作者**: Wenjie Wu, Ge Yan, Xudong Lu, Kaisen Pan, Junchi Yan
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023
- **摘要（中）**: ①针对变分量子算法中量子电路架构设计依赖人工经验、搜索效率低的问题。②提出QuantumDARTS，将可微架构搜索扩展到量子电路，通过连续松弛和梯度优化搜索量子门序列。③相比传统量子NAS方法，QuantumDARTS支持端到端可微训练，避免了离散搜索的昂贵评估。④在量子化学和组合优化任务上，QuantumDARTS搜索到的电路在保真度和能量误差上优于手工设计基线。
- **摘要（英）**: This paper tackles the manual design of quantum circuit architectures in variational quantum algorithms. It proposes QuantumDARTS, extending differentiable architecture search to quantum circuits via continuous relaxation and gradient-based optimization. Compared to discrete quantum NAS, it enables efficient end-to-end search, achieving better fidelity and energy errors on quantum chemistry and combinatorial tasks.
- **核心贡献**: 首次将可微架构搜索应用于量子电路设计。
- **创新点**: 量子电路架构的连续松弛与梯度优化。
- **结果**: 在量子任务上优于手工设计基线。

### Do Not Train It: A Linear Neural Architecture Search of Graph Neural Networks. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://proceedings.mlr.press/v202/xu23w.html)
- **作者**: Peng Xu, Lin Zhang, Xuanzhou Liu, Jiaqi Sun, Yue Zhao, Haiqin Yang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023
- **摘要（中）**: ①针对图神经网络（GNN）架构搜索中训练成本高、搜索空间设计复杂的问题。②提出一种线性NAS方法，通过分析GNN的谱特性，将架构搜索简化为线性模型的选择，无需训练候选网络。③相比传统基于训练的NAS，该方法利用图拉普拉斯特征分解直接评估架构性能，大幅降低计算开销。④在多个图分类和节点分类基准上，该方法搜索到的GNN架构在准确率上接近甚至超过训练-based方法，但搜索时间减少数个数量级。
- **摘要（英）**: This paper addresses the high training cost and complex search space in GNN architecture search. It proposes a linear NAS method that evaluates architectures via spectral analysis of graph Laplacians, avoiding candidate training. Compared to training-based NAS, it reduces computation by orders of magnitude while achieving comparable or better accuracy on graph benchmarks.
- **核心贡献**: 提出基于谱分析的线性GNN架构搜索方法。
- **创新点**: 利用图拉普拉斯特征分解实现零训练架构评估。
- **结果**: 搜索时间减少数个数量级，准确率接近训练方法。

### EvoPrompting: Language Models for Code-Level Neural Architecture Search. **⭐⭐⭐⭐** (相关度: 65%)
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/184c1e18d00d7752805324da48ad25be-Abstract-Conference.html)
- **作者**: Angelica Chen, David Dohan, David R. So
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023
- **摘要（中）**: ①针对传统NAS中搜索空间定义依赖人工、且难以探索复杂架构的问题。②提出EvoPrompting，利用大语言模型（LLM）通过进化策略生成和优化代码级架构描述，实现自动化搜索。③相比基于固定搜索空间的NAS，EvoPrompting允许LLM自由生成架构代码，结合进化算法迭代改进，提高了搜索的灵活性和泛化性。④在图像分类和语言建模任务上，EvoPrompting搜索到的架构性能优于随机搜索和现有LLM-based NAS方法，且搜索效率更高。
- **摘要（英）**: This paper tackles the manual definition of search spaces in NAS, which limits exploration of complex architectures. It proposes EvoPrompting, using LLMs with evolutionary strategies to generate and optimize code-level architecture descriptions. Compared to fixed-space NAS, it enables flexible search, achieving better performance on image and language tasks with higher efficiency.
- **核心贡献**: 提出基于LLM和进化的代码级架构搜索框架。
- **创新点**: 利用LLM生成架构代码并结合进化策略迭代优化。
- **结果**: 在多个任务上优于现有LLM-based NAS方法。

<!-- COMPLETE v1 papers=27 -->
