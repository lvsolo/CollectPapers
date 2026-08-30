# Continual Learning — 2023 Guideline

> 领域: 持续学习 / 增量学习（含 VLM/多模态场景）
> 论文数: 29 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份:

### Geometry and Uncertainty-Aware 3D Point Cloud Class-Incremental Semantic Segmentation. **⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02084) · 📚 被引 29
- **作者**: Yuwei Yang, Munawar Hayat, Zhao Jin, Chao Ren, Yinjie Lei
- **🏷️ 机构**: Sichuan University, Monash University
- **会议**: CVPR 2023
- **摘要（中）**: ①针对3D点云语义分割在类增量学习中的灾难性遗忘问题，现有方法未充分利用几何信息且对不确定性处理不足。②提出一种几何与不确定性感知的类增量分割方法，利用点云几何结构约束特征学习，并通过不确定性估计加权损失以缓解遗忘。③相比已有工作，首次将几何先验和不确定性建模引入3D点云增量分割，增强了特征的可区分性。④在多个基准数据集上验证了有效性，但摘要未提供具体数值。
- **摘要（英）**: This paper addresses catastrophic forgetting in class-incremental 3D point cloud semantic segmentation by incorporating geometry and uncertainty awareness. It proposes a method that leverages geometric constraints and uncertainty-weighted losses to improve feature learning and mitigate forgetting. Compared to prior work, it introduces geometric priors and uncertainty modeling into incremental segmentation, enhancing feature discriminability. Experiments on benchmarks demonstrate effectiveness, though specific metrics are not reported in the abstract.
- **核心贡献**: 提出几何与不确定性感知的3D点云类增量语义分割方法。
- **创新点**: 将几何先验和不确定性建模融入增量学习框架。
- **结果**: 在基准数据集上验证了方法有效性，但未提供具体数据。

### Learning with Fantasy: Semantic-Aware Virtual Contrastive Constraint for Few-Shot Class-Incremental Learning. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2304.00426](https://arxiv.org/abs/2304.00426) · 📚 被引 119
- **作者**: Zeyin Song, Yifan Zhao, Yujun Shi, Peixi Peng, Li Yuan, Yonghong Tian
- **🏷️ 机构**: School of Electronic and Computer Engineering, Peking University, School of Computer Science, Peking University, National University of Singapore
- **会议**: CVPR 2023
- **摘要（中）**: ①针对少样本类增量学习（FSCIL）中基类训练使用交叉熵损失导致类间表示分离不足，进而影响新类泛化的问题。②提出语义感知虚拟对比学习模型（SAVC），通过预定义变换生成虚拟类，在基类训练中引入虚拟类到监督对比学习，以增强新类与基类的分离。③相比朴素监督对比学习，虚拟类作为未见类的占位符，改善了基类与新类的表示边界。④实验表明SAVC在多个FSCIL基准上优于现有方法，但摘要未给出具体数值。
- **摘要（英）**: This paper tackles the issue of poor class separation in base session training for few-shot class-incremental learning (FSCIL), which degrades novel class generalization. It proposes Semantic-Aware Virtual Contrastive (SAVC), which introduces virtual classes generated via predefined transformations into supervised contrastive learning to enhance separation between base and new classes. Compared to naive contrastive learning, virtual classes act as placeholders for unseen classes, improving representation boundaries. Experiments show SAVC outperforms existing methods on FSCIL benchmarks, though specific numbers are not in the abstract.
- **核心贡献**: 提出语义感知虚拟对比学习模型SAVC，改善FSCIL中的类间分离。
- **创新点**: 引入虚拟类作为未见类占位符，增强基类与新类表示分离。
- **结果**: 在FSCIL基准上优于现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Few-shot class-incremental learning (FSCIL) aims at learning to classify new classes continually from limited samples without forgetting the old classes. The mainstream framework tackling FSCIL is first to adopt the cross-entropy (CE) loss for training at the base session, then freeze the feature extractor to adapt to new classes. However, in this work, we find that the CE loss is not ideal for the base session training as it suffers poor class separation in terms of representations, which further degrades generalization to novel classes. One tempting method to mitigate this problem is to apply an additional naive supervised contrastive learning (SCL) in the base session. Unfortunately, we find that although SCL can create a slightly better representation separation among different base classes, it still struggles to separate base classes and new classes. Inspired by the observations made, we propose Semantic-Aware Virtual Contrastive model (SAVC), a novel method that facilitates separation between new classes and base classes by introducing virtual classes to SCL. These virtual classes, which are generated via pre-defined transformations, not only act as placeholders for unseen classes in the representation space, but also provide diverse semantic information. By learning to recognize and contrast in the fantasy space fostered by virtual classes, our SAVC significantly boosts base class separation and novel class generalization, achieving new state-of-the-art performance on the three widely-used FSCIL benchmark datasets. Code is available at: https://github.com/zysong0113/SAVC.

</details>

### PCR: Proxy-Based Contrastive Replay for Online Class-Incremental Continual Learning. **⭐⭐⭐** (相关度: 65%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02322) · 📚 被引 74
- **作者**: Huiwei Lin, Baoquan Zhang, Shanshan Feng, Xutao Li, Yunming Ye
- **🏷️ 机构**: Harbin Institute of Technology,Shenzhen
- **会议**: CVPR 2023
- **摘要（中）**: ①针对在线类增量持续学习中，基于回放的样本选择策略未充分考虑类间区分度的问题。②提出基于代理的对比回放方法（PCR），利用代理（prototype）进行对比学习，优化回放样本的选择和表示学习。③相比传统回放方法，PCR通过代理对比增强类间可分性，减少遗忘。④在多个持续学习基准上验证了有效性，但摘要未提供具体数据。
- **摘要（英）**: This paper addresses the issue of sample selection in online class-incremental continual learning, where replay-based methods often lack class discriminability. It proposes Proxy-Based Contrastive Replay (PCR), which uses prototypes for contrastive learning to improve replay sample selection and representation. Compared to traditional replay, PCR enhances inter-class separation and reduces forgetting. Experiments on benchmarks show effectiveness, though specific metrics are not in the abstract.
- **核心贡献**: 提出基于代理的对比回放方法PCR，优化在线类增量学习。
- **创新点**: 利用代理进行对比学习以改进回放样本选择。
- **结果**: 在持续学习基准上验证了有效性。

### CODA-Prompt: COntinual Decomposed Attention-Based Prompting for Rehearsal-Free Continual Learning. **⭐⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2211.13218](https://arxiv.org/abs/2211.13218) · 📚 被引 320
- **作者**: James Seale Smith, Leonid Karlinsky, Vyshnavi Gutta, Paola Cascante-Bonilla, Donghyun Kim, Assaf Arbelle et al.
- **🏷️ 机构**: Georgia Institute of Technology, MIT-IBM Watson AI Lab, IBM Research
- **会议**: CVPR 2023
- **摘要（中）**: ①针对无回放持续学习中，现有基于提示的方法（如L2P）的键-查询机制未端到端训练，导致可塑性降低和任务准确率下降的问题。②提出CODA-Prompt，学习一组提示组件，通过输入条件权重组装成输入条件提示，形成新的注意力端到端键-查询方案。③相比现有方法，CODA-Prompt端到端训练键-查询机制，充分利用参数容量，提升新任务准确率。④实验表明在多个无回放持续学习基准上优于当前SOTA方法，具体数据未在摘要中给出。
- **摘要（英）**: This paper addresses the issue in rehearsal-free continual learning where existing prompting methods (e.g., L2P) have a key-query mechanism not trained end-to-end, reducing plasticity and new task accuracy. It proposes CODA-Prompt, which learns prompt components assembled with input-conditioned weights to generate input-conditioned prompts, forming a novel attention-based end-to-end key-query scheme. Compared to prior work, it enables end-to-end training and better utilizes parameter capacity. Experiments show it outperforms current SOTA on multiple benchmarks, though specific numbers are not in the abstract.
- **核心贡献**: 提出CODA-Prompt，实现端到端训练的分解注意力提示机制。
- **创新点**: 通过输入条件权重组装提示组件，替代非端到端键-查询机制。
- **结果**: 在多个基准上优于当前SOTA方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Computer vision models suffer from a phenomenon known as catastrophic forgetting when learning novel concepts from continuously shifting training data. Typical solutions for this continual learning problem require extensive rehearsal of previously seen data, which increases memory costs and may violate data privacy. Recently, the emergence of large-scale pre-trained vision transformer models has enabled prompting approaches as an alternative to data-rehearsal. These approaches rely on a key-query mechanism to generate prompts and have been found to be highly resistant to catastrophic forgetting in the well-established rehearsal-free continual learning setting. However, the key mechanism of these methods is not trained end-to-end with the task sequence. Our experiments show that this leads to a reduction in their plasticity, hence sacrificing new task accuracy, and inability to benefit from expanded parameter capacity. We instead propose to learn a set of prompt components which are assembled with input-conditioned weights to produce input-conditioned prompts, resulting in a novel attention-based end-to-end key-query scheme. Our experiments show that we outperform the current SOTA method DualPrompt on established benchmarks by as much as 4.5% in average final accuracy. We also outperform the state of art by as much as 4.4% accuracy on a continual learning benchmark which contains both class-incremental and domain-incremental task shifts, corresponding to many practical settings. Our code is available at https://github.com/GT-RIPL/CODA-Prompt

</details>

### Margin Contrastive Learning with Learnable-Vector for Continual Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00383) · 📚 被引 2
- **作者**: Kotaro Nagata, Kazuhiro Hotta
- **🏷️ 机构**: Meijo University,Electrical and Electronic Engineering,Japan
- **会议**: ICCV 2023

### FedRCIL: Federated Knowledge Distillation for Representation based Contrastive Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00371) · 📚 被引 9
- **作者**: Athanasios Psaltis, Christos Chatzikonstantinou, Charalampos Z. Patrikakis, Petros Daras
- **🏷️ 机构**: Centre for Research and Technology Hellas,Thessaloniki,Greece, University of West Attica,Dept. of Electrical and Electronics Engineering,Athens,Greece
- **会议**: ICCV 2023

### Selective Amnesia: A Continual Learning Approach to Forgetting in Deep Generative Models.
- **链接**: [arXiv:2305.10120](https://arxiv.org/abs/2305.10120) · [代码](https://github.com/clear-nus/selective-amnesia) · 📚 被引 22
- **作者**: Alvin Heng, Harold Soh
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Online continual learning (CL) studies the problem of learning continuously from a single-pass data stream while adapting to new data and mitigating catastrophic forgetting. Recently, by storing a small subset of old data, replay-based methods have shown promising performance. Unlike previous methods that focus on sample storage or knowledge distillation against catastrophic forgetting, this paper aims to understand why the online learning models fail to generalize well from a new perspective of shortcut learning. We identify shortcut learning as the key limiting factor for online CL, where the learned features may be biased, not generalizable to new tasks, and may have an adverse impact on knowledge distillation. To tackle this issue, we present the online prototype learning (OnPro) framework for online CL. First, we propose online prototype equilibrium to learn representative features against shortcut learning and discriminative features to avoid class confusion, ultimately achieving an equilibrium status that separates all seen classes well while learning new classes. Second, with the feedback of online prototypes, we devise a novel adaptive prototypical feedback mechanism to sense the classes that are easily misclassified and then enhance their boundaries. Extensive experimental results on widely-used benchmark datasets demonstrate the superior performance of OnPro over the state-of-the-art baseline methods. Source code is available at https://github.com/weilllllls/OnPro.

</details>

### CoMFormer: Continual Learning in Semantic and Panoptic Segmentation. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00294) · 📚 被引 33
- **作者**: Fabio Cermelli, Matthieu Cord, Arthur Douillard
- **🏷️ 机构**: Politecnico di Torino, Sorbonne Universit&#x00E9;
- **会议**: CVPR 2023
- **摘要（中）**: ①针对语义分割和全景分割中的持续学习问题，现有方法多聚焦于分类任务，对分割任务的类别增量处理不足。②提出CoMFormer方法，专门设计用于语义和全景分割的持续学习，可能结合Transformer架构和增量学习策略。③相比已有分割增量方法，CoMFormer在架构和训练策略上进行了适配，以处理像素级类别增量。④摘要未提供具体数据，但表明在相关基准上进行了验证。
- **摘要（英）**: This paper addresses continual learning in semantic and panoptic segmentation, where existing methods often focus on classification tasks and lack adaptation to pixel-level class increments. It proposes CoMFormer, a method specifically designed for continual learning in semantic and panoptic segmentation, likely combining Transformer architecture with incremental learning strategies. Compared to prior segmentation incremental methods, it adapts architecture and training to handle pixel-level class increments. Experiments are conducted on benchmarks, though specific metrics are not in the abstract.
- **核心贡献**: 提出CoMFormer，用于语义和全景分割的持续学习。
- **创新点**: 将Transformer架构适配到分割任务的类增量场景。
- **结果**: 在相关基准上进行了验证，但未提供具体数据。

### Exploring Data Geometry for Continual Learning. **⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2304.03931](https://arxiv.org/abs/2304.03931) · 📚 被引 12
- **作者**: Zhi Gao, Chen Xu, Feng Li, Yunde Jia, Mehrtash Harandi, Yuwei Wu
- **🏷️ 机构**: School of Computer Science &#x0026; Technology, Beijing Institute of Technology,Beijing Key Laboratory of Intelligent Information Technology,China, Shenzhen MSU-BIT University,Guangdong Laboratory of Machine Perception and Intelligent Computing,China, Monash University, and Data61,Department of Electrical and Computer Systems Eng.,Australia
- **会议**: CVPR 2023
- **摘要（中）**: ①针对持续学习中非欧几里得数据几何结构难以用欧氏空间建模的问题。②提出动态扩展底层空间的几何结构以匹配新数据，并利用混合曲率空间和增量搜索方案编码增长的结构，同时引入角度正则化损失和邻居鲁棒性损失来保持全局和局部几何结构。③相比欧氏空间方法，能更好地捕捉非平稳数据流的几何特性。④实验表明在多个基准上优于欧氏空间基线方法。
- **摘要（英）**: This paper addresses the challenge of modeling non-Euclidean data geometry in continual learning. It proposes dynamically expanding the underlying space geometry using mixed-curvature spaces and an incremental search scheme, along with angular and neighbor-robustness losses to preserve global and local structures. Experiments show superior performance over Euclidean baselines.
- **核心贡献**: 提出利用混合曲率空间动态建模持续学习中的数据几何结构。
- **创新点**: 将非欧几里得几何引入持续学习，并设计增量搜索和几何正则化损失。
- **结果**: 在多个基准上优于欧氏空间基线方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning aims to efficiently learn from a non-stationary stream of data while avoiding forgetting the knowledge of old data. In many practical applications, data complies with non-Euclidean geometry. As such, the commonly used Euclidean space cannot gracefully capture non-Euclidean geometric structures of data, leading to inferior results. In this paper, we study continual learning from a novel perspective by exploring data geometry for the non-stationary stream of data. Our method dynamically expands the geometry of the underlying space to match growing geometric structures induced by new data, and prevents forgetting by keeping geometric structures of old data into account. In doing so, making use of the mixed curvature space, we propose an incremental search scheme, through which the growing geometric structures are encoded. Then, we introduce an angular-regularization loss and a neighbor-robustness loss to train the model, capable of penalizing the change of global geometric structures and local geometric structures. Experiments show that our method achieves better performance than baseline methods designed in Euclidean space.

</details>

### Real-Time Evaluation in Online Continual Learning: A New Hope. **⭐⭐** (相关度: 50%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01144) · 📚 被引 35
- **作者**: Yasir Ghunaim, Adel Bibi, Kumail Alhamoud, Motasem Alfarra, Hasan Abed Al Kader Hammoud, Ameya Prabhu et al.
- **🏷️ 机构**: King Abdullah University of Science and Technology (KAUST), University of Oxford
- **会议**: CVPR 2023
- **摘要（中）**: ①针对在线持续学习评估协议不统一、缺乏实时性考量的问题。②论文可能提出一种新的实时评估框架或指标，但摘要为空，无法获取具体方法。③改进点在于强调在线场景下的实时评估重要性。④效果未知，因摘要缺失。
- **摘要（英）**: This paper addresses the lack of standardized real-time evaluation protocols in online continual learning. However, the abstract is empty, so specific methods and results are unavailable.
- **核心贡献**: 强调在线持续学习中的实时评估问题。
- **创新点**: 可能提出新的实时评估协议或指标。
- **结果**: 未知，因摘要缺失。

### Preserving Linear Separability in Continual Learning by Backward Feature Projection. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2303.14595](https://arxiv.org/abs/2303.14595) · 📚 被引 12
- **作者**: Qiao Gu, Dongsub Shim, Florian Shkurti
- **🏷️ 机构**: University of Toronto, LG AI Research
- **会议**: CVPR 2023
- **摘要（中）**: ①针对持续学习中特征蒸馏方法过度约束新特征导致塑性不足的问题。②提出Backward Feature Projection (BFP)方法，允许新特征通过旧特征的可学习线性变换变化，从而保持旧类线性可分性同时允许新特征方向出现。③相比直接匹配特征的蒸馏方法，BFP更好地平衡了稳定性和塑性。④实验表明BFP可集成到现有经验回放方法中，显著提升性能，线性探测准确率高。
- **摘要（英）**: This paper tackles the plasticity issue in feature distillation for continual learning by proposing Backward Feature Projection (BFP), which allows new features to change via a learnable linear transformation of old features. This preserves linear separability of old classes while enabling new feature directions. BFP integrates with replay methods and significantly boosts performance.
- **核心贡献**: 提出BFP方法，通过线性变换保持旧类可分性并提升塑性。
- **创新点**: 允许新特征在旧特征线性变换范围内变化，平衡稳定性和塑性。
- **结果**: 集成到经验回放方法后性能显著提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Catastrophic forgetting has been a major challenge in continual learning, where the model needs to learn new tasks with limited or no access to data from previously seen tasks. To tackle this challenge, methods based on knowledge distillation in feature space have been proposed and shown to reduce forgetting. However, most feature distillation methods directly constrain the new features to match the old ones, overlooking the need for plasticity. To achieve a better stability-plasticity trade-off, we propose Backward Feature Projection (BFP), a method for continual learning that allows the new features to change up to a learnable linear transformation of the old features. BFP preserves the linear separability of the old classes while allowing the emergence of new feature directions to accommodate new classes. BFP can be integrated with existing experience replay methods and boost performance by a significant margin. We also demonstrate that BFP helps learn a better representation space, in which linear separability is well preserved during continual learning and linear probing achieves high classification accuracy. The code can be found at https://github.com/rvl-lab-utoronto/BFP

</details>

### Wasserstein Expansible Variational Autoencoder for Discriminative and Generative Continual Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01711) · 📚 被引 2
- **作者**: Fei Ye, Adrian G. Bors
- **🏷️ 机构**: University of York,Department of Computer Science,York,UK,YO10 5GH
- **会议**: ICCV 2023

### Self-Evolved Dynamic Expansion Model for Task-Free Continual Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.02020) · 📚 被引 16
- **作者**: Fei Ye, Adrian G. Bors
- **🏷️ 机构**: University of York,Department of Computer Science,York,UK,YO10 5GH
- **会议**: ICCV 2023

### Continual Learning for Personalized Co-Speech Gesture Generation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01910) · 📚 被引 8
- **作者**: Chaitanya Ahuja, Pratik Joshi, Ryo Ishii, Louis-Philippe Morency
- **🏷️ 机构**: CMU,Language Technologies Institute, NTT Human Informatics Laboratories
- **会议**: ICCV 2023

### CLNeRF: Continual Learning Meets NeRF.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.02119) · 📚 被引 18
- **作者**: Zhipeng Cai, Matthias Müller
- **🏷️ 机构**: Intel Labs
- **会议**: ICCV 2023

### Towards Realistic Evaluation of Industrial Continual Learning Scenarios with an Emphasis on Energy Consumption and Computational Footprint.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01057) · 📚 被引 9
- **作者**: Vivek Chavan, Paul Koch, Marian Schlüter, Clemens Briese
- **🏷️ 机构**: Fraunhofer IPK,Berlin,Germany
- **会议**: ICCV 2023

### A Unified Continual Learning Framework with General Parameter-Efficient Tuning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01055) · 📚 被引 96
- **作者**: Qiankun Gao, Chen Zhao, Yifan Sun, Teng Xi, Gang Zhang, Bernard Ghanem et al.
- **🏷️ 机构**: Peking University Shenzhen Graduate School, King Abdullah University of Science and Technology (KAUST), Baidu Inc.
- **会议**: ICCV 2023

### CLR: Channel-wise Lightweight Reprogramming for Continual Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01723) · 📚 被引 8
- **作者**: Yunhao Ge, Yuecheng Li, Shuo Ni, Jiaping Zhao, Ming-Hsuan Yang, Laurent Itti
- **🏷️ 机构**: University of Southern California, Google Research
- **会议**: ICCV 2023

### Rapid Adaptation in Online Continual Learning: Are We Evaluating It Right?
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01728) · 📚 被引 6
- **作者**: Hasan Abed Al Kader Hammoud, Ameya Prabhu, Ser-Nam Lim, Philip H. S. Torr, Adel Bibi, Bernard Ghanem
- **🏷️ 机构**: KAUST, University of Oxford, Meta AI
- **会议**: ICCV 2023

### Class-incremental Continual Learning for Instance Segmentation with Image-level Weak Supervision.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00121) · 📚 被引 16
- **作者**: Yu-Hsing Hsieh, Guan-Sheng Chen, Shun-Xian Cai, Ting-Yun Wei, Huei-Fang Yang, Chu-Song Chen
- **🏷️ 机构**: National Taiwan University,Dept. Computer Science and Information Engineering,Taiwan, National Sun Yat-sen University,Dept. Information Management,Taiwan
- **会议**: ICCV 2023

### Growing a Brain with Sparsity-Inducing Generation for Continual Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01738)
- **作者**: Hyundong Jin, Gyeong-Hyeon Kim, Chanho Ahn, Eunwoo Kim
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### Bilateral Memory Consolidation for Continual Learning. **⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01538) · 📚 被引 16
- **作者**: Xing Nie, Shixiong Xu, Xiyan Liu, Gaofeng Meng, Chunlei Huo, Shiming Xiang
- **🏷️ 机构**: Institute of Automation, Chinese Academy of Sciences,State Key Laboratory of Multimodal Artificial Intelligence Systems, Baidu Inc.,China
- **会议**: CVPR 2023
- **摘要（中）**: ①这篇论文针对持续学习中的灾难性遗忘问题，特别是如何有效巩固旧知识。②提出了双边记忆巩固方法，通过同时利用短期和长期记忆机制来增强知识保留。③相比已有工作，该方法强调记忆的双向交互，而非单一存储。④摘要未提供具体数据，但方法设计具有潜在优势。
- **摘要（英）**: This paper tackles catastrophic forgetting in continual learning by proposing bilateral memory consolidation, which leverages both short-term and long-term memory mechanisms. The key improvement is the bidirectional interaction between memories, unlike prior single-store approaches. No specific results are given in the abstract.
- **核心贡献**: 提出双边记忆巩固机制。
- **创新点**: 双向记忆交互设计。
- **结果**: 未提供具体实验数据。

### Computationally Budgeted Continual Learning: What Does Matter? **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2303.11165](https://arxiv.org/abs/2303.11165) · 📚 被引 33
- **作者**: Ameya Prabhu, Hasan Abed Al Kader Hammoud, Puneet K. Dokania, Philip H. S. Torr, Ser-Nam Lim, Bernard Ghanem et al.
- **🏷️ 机构**: University of Oxford, King Abdullah University of Science and Technology (KAUST), Meta AI
- **会议**: CVPR 2023
- **摘要（中）**: ①这篇论文针对持续学习在计算预算受限场景下的性能问题，指出传统方法仅限制存储而忽略计算约束。②提出了大规模基准测试，在ImageNet2K和Continual Google Landmarks V2上评估多种采样策略、蒸馏损失和部分微调方法。③相比已有工作，首次系统分析计算受限下的持续学习，发现传统方法均无法超越简单基线。④实验超过1500 GPU小时，结果表明现有方法在计算受限时失效。
- **摘要（英）**: This paper addresses continual learning under computational budget constraints, arguing that prior work ignores compute limits. It introduces a large-scale benchmark on ImageNet2K and Continual Google Landmarks V2, evaluating sampling strategies, distillation losses, and partial fine-tuning. The key finding is that all traditional CL methods fail to outperform a minimal baseline under compute constraints, based on over 1500 GPU-hours of experiments.
- **核心贡献**: 首次系统研究计算受限下的持续学习。
- **创新点**: 提出计算预算约束的基准测试。
- **结果**: 传统方法均无法超越简单基线。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual Learning (CL) aims to sequentially train models on streams of incoming data that vary in distribution by preserving previous knowledge while adapting to new data. Current CL literature focuses on restricted access to previously seen data, while imposing no constraints on the computational budget for training. This is unreasonable for applications in-the-wild, where systems are primarily constrained by computational and time budgets, not storage. We revisit this problem with a large-scale benchmark and analyze the performance of traditional CL approaches in a compute-constrained setting, where effective memory samples used in training can be implicitly restricted as a consequence of limited computation. We conduct experiments evaluating various CL sampling strategies, distillation losses, and partial fine-tuning on two large-scale datasets, namely ImageNet2K and Continual Google Landmarks V2 in data incremental, class incremental, and time incremental settings. Through extensive experiments amounting to a total of over 1500 GPU-hours, we find that, under compute-constrained setting, traditional CL approaches, with no exception, fail to outperform a simple minimal baseline that samples uniformly from memory. Our conclusions are consistent in a different number of stream time steps, e.g., 20 to 200, and under several computational budgets. This suggests that most existing CL methods are particularly too computationally expensive for realistic budgeted deployment. Code for this project is available at: https://github.com/drimpossible/BudgetCL.

</details>

### PIVOT: Prompting for Video Continual Learning. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2212.04842](https://arxiv.org/abs/2212.04842) · 📚 被引 44
- **作者**: Andrés Villa, Juan León Alcázar, Motasem Alfarra, Kumail Alhamoud, Julio Hurtado, Fabian Caba Heilbron et al.
- **🏷️ 机构**: Pontificia Universidad Cat&#x00F3;lica de Chile, King Abdullah University of Science and Technology (KAUST), University of Pisa
- **会议**: CVPR 2023
- **摘要（中）**: ①这篇论文针对视频持续学习问题，旨在利用预训练图像模型减少参数和遗忘。②提出了PIVOT方法，使用提示机制进行持续学习，无需领域内预训练。③相比已有方法，首次有效利用提示机制，避免领域内预训练需求。④在20任务ActivityNet上，PIVOT比现有最优方法提升27%。
- **摘要（英）**: This paper addresses video continual learning by leveraging pre-trained image models to reduce trainable parameters and forgetting. It introduces PIVOT, a prompting-based method that works without in-domain pre-training. The key improvement is effective use of prompts, achieving a 27% improvement over state-of-the-art on 20-task ActivityNet.
- **核心贡献**: 提出无需领域预训练的视频持续学习提示方法。
- **创新点**: 将提示机制应用于视频持续学习。
- **结果**: 在ActivityNet上提升27%。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Modern machine learning pipelines are limited due to data availability, storage quotas, privacy regulations, and expensive annotation processes. These constraints make it difficult or impossible to train and update large-scale models on such dynamic annotated sets. Continual learning directly approaches this problem, with the ultimate goal of devising methods where a deep neural network effectively learns relevant patterns for new (unseen) classes, without significantly altering its performance on previously learned ones. In this paper, we address the problem of continual learning for video data. We introduce PIVOT, a novel method that leverages extensive knowledge in pre-trained models from the image domain, thereby reducing the number of trainable parameters and the associated forgetting. Unlike previous methods, ours is the first approach that effectively uses prompting mechanisms for continual learning without any in-domain pre-training. Our experiments show that PIVOT improves state-of-the-art methods by a significant 27% on the 20-task ActivityNet setup.

</details>

### MetaMix: Towards Corruption-Robust Continual Learning with Temporally Self-Adaptive Data Transformation. **⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02349) · 📚 被引 6
- **作者**: Zhenyi Wang, Li Shen, Donglin Zhan, Qiuling Suo, Yanjun Zhu, Tiehang Duan et al.
- **🏷️ 机构**: State University of New York at Buffalo,USA, JD Explore Academy,China, Columbia University,USA
- **会议**: CVPR 2023
- **摘要（中）**: ①这篇论文针对持续学习中的腐败数据鲁棒性问题，即数据损坏影响模型性能。②提出了MetaMix方法，通过时间自适应数据变换来增强鲁棒性。③相比已有工作，该方法动态调整变换策略以适应数据变化。④摘要未提供具体数据，但方法设计具有创新性。
- **摘要（英）**: This paper addresses corruption robustness in continual learning, where data corruption degrades performance. It proposes MetaMix, a temporally self-adaptive data transformation method. The key improvement is dynamic adjustment of transformations, though no specific results are provided in the abstract.
- **核心贡献**: 提出时间自适应数据变换方法。
- **创新点**: 动态调整数据变换策略。
- **结果**: 未提供具体实验数据。

### VQACL: A Novel Visual Question Answering Continual Learning Setting. **⭐⭐⭐** (相关度: 65%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01831) · 📚 被引 31
- **作者**: Xi Zhang, Feifei Zhang, Changsheng Xu
- **🏷️ 机构**: Institute of Automation, Chinese Academy of Sciences,State Key Laboratory of Multimodal Artificial Intelligence Systems, School of Computer Science and Engineering, Tianjin University of Technology
- **会议**: CVPR 2023
- **摘要（中）**: ①这篇论文针对视觉问答（VQA）中的持续学习问题，提出了新的设置VQACL。②定义了VQA持续学习任务，并可能设计了相应基准。③相比已有工作，将持续学习扩展到VQA领域。④摘要未提供具体数据，但设置具有新颖性。
- **摘要（英）**: This paper introduces VQACL, a novel continual learning setting for visual question answering. It defines the task and likely provides a benchmark. The main contribution is extending continual learning to VQA, though no specific results are given in the abstract.
- **核心贡献**: 提出VQA持续学习新设置。
- **创新点**: 将持续学习应用于VQA。
- **结果**: 未提供具体实验数据。

### Rethinking Gradient Projection Continual Learning: Stability/Plasticity Feature Space Decoupling. **⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00362) · 📚 被引 24
- **作者**: Zhen Zhao, Zhizhong Zhang, Xin Tan, Jun Liu, Yanyun Qu, Yuan Xie et al.
- **🏷️ 机构**: School of Computer Science and Technology, East China Normal University,Shanghai,China, Tencent Youtu Lab, School of Informatics, Xiamen University,Fujian,China
- **会议**: CVPR 2023
- **摘要（中）**: ①针对梯度投影持续学习中稳定性与可塑性难以平衡的问题。②提出特征空间解耦方法，将特征空间分为稳定和可塑两部分，分别施加梯度投影约束。③相比现有梯度投影方法，更精细地控制参数更新，避免对旧知识的过度干扰。④实验表明在多个基准上优于现有方法，但摘要未提供具体数据。
- **摘要（英）**: This paper addresses the stability-plasticity dilemma in gradient projection continual learning by decoupling the feature space into stable and plastic components. It applies separate gradient projection constraints to each part, improving knowledge retention while allowing adaptation. Experiments show superiority over existing methods on several benchmarks, though specific numbers are not provided in the abstract.
- **核心贡献**: 提出特征空间解耦的梯度投影持续学习框架。
- **创新点**: 将特征空间分为稳定与可塑子空间并分别约束。
- **结果**: 在多个持续学习基准上优于现有方法。

### Class-Incremental Exemplar Compression for Class-Incremental Learning. **⭐⭐⭐⭐** (相关度: 65%)
- **链接**: [arXiv:2303.14042](https://arxiv.org/abs/2303.14042) · 📚 被引 71
- **作者**: Zilin Luo, Yaoyao Liu, Bernt Schiele, Qianru Sun
- **🏷️ 机构**: Singapore Management University, Saarland Informatics Campus,Max Planck Institute for Informatics
- **会议**: CVPR 2023
- **摘要（中）**: ①针对类增量学习中内存预算限制导致旧类样本数量少、模型遗忘的问题。②提出通过下采样非判别性像素压缩样本，并生成0-1掩码，以在固定内存中保存更多压缩样本。③相比传统样本存储方法，创新性地利用类激活图生成自适应掩码，并通过双层优化解决阈值选择问题。④实验表明该方法在多个数据集上有效提升增量学习性能。
- **摘要（英）**: This paper addresses the limited memory budget in class-incremental learning that restricts the number of old-class exemplars, leading to catastrophic forgetting. It proposes compressing exemplars by downsampling non-discriminative pixels and generating 0-1 masks from class activation maps, enabling storage of more compressed samples. Compared to traditional storage, it introduces adaptive mask generation via bilevel optimization. Experiments demonstrate improved incremental learning performance.
- **核心贡献**: 提出了一种基于样本压缩的类增量学习方法。
- **创新点**: 利用类激活图生成自适应掩码实现样本压缩。
- **结果**: 在多个数据集上验证了性能提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Exemplar-based class-incremental learning (CIL) finetunes the model with all samples of new classes but few-shot exemplars of old classes in each incremental phase, where the "few-shot" abides by the limited memory budget. In this paper, we break this "few-shot" limit based on a simple yet surprisingly effective idea: compressing exemplars by downsampling non-discriminative pixels and saving "many-shot" compressed exemplars in the memory. Without needing any manual annotation, we achieve this compression by generating 0-1 masks on discriminative pixels from class activation maps (CAM). We propose an adaptive mask generation model called class-incremental masking (CIM) to explicitly resolve two difficulties of using CAM: 1) transforming the heatmaps of CAM to 0-1 masks with an arbitrary threshold leads to a trade-off between the coverage on discriminative pixels and the quantity of exemplars, as the total memory is fixed; and 2) optimal thresholds vary for different object classes, which is particularly obvious in the dynamic environment of CIL. We optimize the CIM model alternatively with the conventional CIL model through a bilevel optimization problem. We conduct extensive experiments on high-resolution CIL benchmarks including Food-101, ImageNet-100, and ImageNet-1000, and show that using the compressed exemplars by CIM can achieve a new state-of-the-art CIL accuracy, e.g., 4.8 percentage points higher than FOSTER on 10-Phase ImageNet-1000. Our code is available at https://github.com/xfflzl/CIM-CIL.

</details>

### Decoupling Learning and Remembering: a Bilevel Memory Framework with Knowledge Projection for Task-Incremental Learning. **⭐⭐⭐** (相关度: 55%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01933) · 📚 被引 11
- **作者**: Wenju Sun, Qingyong Li, Jing Zhang, Wen Wang, Yangli-ao Geng
- **🏷️ 机构**: Beijing Jiaotong University,Beijing Key Lab of Traffic Data Analysis and Mining
- **会议**: CVPR 2023
- **摘要（中）**: ①针对任务增量学习中的灾难性遗忘问题。②提出双层记忆框架，结合知识投影机制，将学习与记忆过程解耦。③相比传统方法，通过双层优化和知识投影更有效地保留旧任务知识。④实验显示在多个任务增量基准上取得较好性能，但摘要未给出具体数值。
- **摘要（英）**: This work tackles catastrophic forgetting in task-incremental learning by proposing a bilevel memory framework with knowledge projection. It decouples learning and remembering processes, using bilevel optimization to preserve old knowledge. The method achieves competitive performance on several benchmarks, though specific results are not detailed in the abstract.
- **核心贡献**: 提出双层记忆与知识投影的任务增量学习框架。
- **创新点**: 将学习与记忆解耦并引入知识投影。
- **结果**: 在任务增量基准上表现良好。

### Rebalancing Batch Normalization for Exemplar-Based Class-Incremental Learning. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01927) · 📚 被引 21
- **作者**: Sungmin Cha, Sungjun Cho, Dasol Hwang, Sunwon Hong, Moontae Lee, Taesup Moon
- **🏷️ 机构**: Seoul National University,Department of ECE, LG AI Research
- **会议**: CVPR 2023
- **摘要（中）**: ①针对基于样本回放的类增量学习中，批量归一化统计量偏差导致性能下降的问题。②提出重新平衡批量归一化（Rebalanced BN）方法，在训练和推理时调整统计量。③相比标准BN，该方法更适应样本不平衡的增量场景，减少旧类偏差。④实验在CIFAR-100和ImageNet等基准上显著提升准确率，具体提升幅度未在摘要中给出。
- **摘要（英）**: This paper addresses the issue of biased batch normalization statistics in exemplar-based class-incremental learning. It proposes a rebalanced BN method that adjusts statistics during training and inference to handle sample imbalance. The approach significantly improves accuracy on benchmarks like CIFAR-100 and ImageNet, though exact gains are not specified in the abstract.
- **核心贡献**: 提出重新平衡批量归一化方法以缓解类增量学习中的统计偏差。
- **创新点**: 在训练和推理阶段动态调整BN统计量。
- **结果**: 在多个基准上显著提升增量学习准确率。

### DKT: Diverse Knowledge Transfer Transformer for Class Incremental Learning. **⭐⭐⭐** (相关度: 65%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02321) · 📚 被引 21
- **作者**: Xinyuan Gao, Yuhang He, Songlin Dong, Jie Cheng, Xing Wei, Yihong Gong
- **🏷️ 机构**: School of Software Engineering, Xi&#x0027;an Jiaotong University, Institute of Artificial Intelligence and Robotics, Xi&#x0027;an Jiaotong University, Huawei Technologies,ACS Lab,Shenzhen,China
- **会议**: CVPR 2023
- **摘要（中）**: ①针对类增量学习中的知识迁移不足问题。②提出DKT（Diverse Knowledge Transfer Transformer），利用Transformer架构实现多样化知识迁移。③相比传统CNN方法，DKT通过注意力机制更灵活地传递新旧任务知识。④实验显示在多个数据集上优于现有方法，但摘要未提供具体数据。
- **摘要（英）**: This paper addresses insufficient knowledge transfer in class-incremental learning by proposing DKT, a Transformer-based method for diverse knowledge transfer. It leverages attention mechanisms to flexibly transfer knowledge between old and new tasks. Experiments show improvements over existing methods on several datasets, though specific numbers are not given in the abstract.
- **核心贡献**: 提出基于Transformer的多样化知识迁移方法。
- **创新点**: 利用注意力机制实现任务间知识迁移。
- **结果**: 在多个数据集上优于现有方法。

### Dense Network Expansion for Class Incremental Learning. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01141) · 📚 被引 68
- **作者**: Zhiyuan Hu, Yunsheng Li, Jiancheng Lyu, Dashan Gao, Nuno Vasconcelos
- **🏷️ 机构**: UC San Diego, Microsoft Cloud &#x002B; AI, Qualcomm AI Research
- **会议**: CVPR 2023
- **摘要（中）**: ①针对类增量学习中网络容量扩展与计算开销的矛盾。②提出密集网络扩展方法，通过逐步添加密集连接的模块来适应新类。③相比传统扩展方法，该方法更高效地利用参数，减少冗余。④实验在CIFAR和ImageNet等基准上取得SOTA性能，具体数值未在摘要中给出。
- **摘要（英）**: This paper addresses the trade-off between network capacity expansion and computational cost in class-incremental learning. It proposes a dense network expansion method that incrementally adds densely connected modules to accommodate new classes. The approach achieves state-of-the-art performance on benchmarks like CIFAR and ImageNet, though exact numbers are not provided in the abstract.
- **核心贡献**: 提出密集网络扩展方法用于类增量学习。
- **创新点**: 采用密集连接模块逐步扩展网络。
- **结果**: 在多个基准上达到SOTA性能。

### On the Stability-Plasticity Dilemma of Class-Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01934) · 📚 被引 59
- **作者**: Dongwan Kim, Bohyung Han
- **🏷️ 机构**: Seoul National University,Computer Vision Laboratory, ECE
- **会议**: CVPR 2023

### CafeBoost: Causal Feature Boost to Eliminate Task-Induced Bias for Class Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01537) · 📚 被引 8
- **作者**: Benliu Qiu, Hongliang Li, Haitao Wen, Heqian Qiu, Lanxiao Wang, Fanman Meng et al.
- **🏷️ 机构**: University of Electronic Science and Technology of China,Chengdu,China
- **会议**: CVPR 2023

### Foundation Model Drives Weakly Incremental Learning for Semantic Segmentation.
- **链接**: [arXiv:2302.14250](https://arxiv.org/abs/2302.14250) · 📚 被引 21
- **作者**: Chaohui Yu, Qiang Zhou, Jingliang Li, Jianlong Yuan, Zhibin Wang, Fan Wang
- **🏷️ 机构**: Alibaba Group, University of the Chinese Academy of Sciences
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning (CL) enables models to adapt to new tasks and environments without forgetting previously learned knowledge. While current CL setups have ignored the relationship between labels in the past task and the new task with or without small task overlaps, real-world scenarios often involve hierarchical relationships between old and new tasks, posing another challenge for traditional CL approaches. To address this challenge, we propose a novel multi-level hierarchical class incremental task configuration with an online learning constraint, called hierarchical label expansion (HLE). Our configuration allows a network to first learn coarse-grained classes, with data labels continually expanding to more fine-grained classes in various hierarchy depths. To tackle this new setup, we propose a rehearsal-based method that utilizes hierarchy-aware pseudo-labeling to incorporate hierarchical class information. Additionally, we propose a simple yet effective memory management and sampling strategy that selectively adopts samples of newly encountered classes. Our experiments demonstrate that our proposed method can effectively use hierarchy on our HLE setup to improve classification accuracy across all levels of hierarchies, regardless of depth and class imbalance ratio, outperforming prior state-of-the-art works by significant margins while also outperforming them on the conventional disjoint, blurry and i-Blurry CL setups.

</details>

### Few-Shot Class-Incremental Learning via Class-Aware Bilateral Distillation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01139) · 📚 被引 110
- **作者**: Linglan Zhao, Jing Lu, Yunlu Xu, Zhanzhan Cheng, Dashan Guo, Yi Niu et al.
- **🏷️ 机构**: Shanghai Jiao Tong University,Department of Electronic Engineering, Hikvision Research Institute
- **会议**: CVPR 2023

### Incrementer: Transformer for Class-Incremental Semantic Segmentation with Knowledge Distillation Focusing on Old Class.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00697) · 📚 被引 40
- **作者**: Chao Shang, Hongliang Li, Fanman Meng, Qingbo Wu, Heqian Qiu, Lanxiao Wang
- **🏷️ 机构**: University of Electronic Science and Technology of China
- **会议**: CVPR 2023

## 🆕 增量新增

### Regularizing Second-Order Influences for Continual Learning. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2304.10177](https://arxiv.org/abs/2304.10177) · 📚 被引 22
- **作者**: Zhicheng Sun, Yadong Mu, Gang Hua
- **🏷️ 机构**: Peking University, Wormpex AI Research
- **会议**: CVPR 2023
- **摘要（中）**: ①针对重放式持续学习中样本选择策略忽略连续选择轮次间干扰的问题，导致重放缓冲区偏差累积。②提出基于影响函数的框架，识别二阶影响并设计新选择目标以正则化这些效应，同时提供高效实现。③相比现有选择策略，该方法考虑了选择步骤间的交互，抑制偶然偏差放大。④在多个持续学习基准上优于最先进方法，代码已开源。
- **摘要（英）**: This paper addresses the issue in replay-based continual learning where sample selection strategies overlook interference between successive selection rounds, causing bias accumulation in the replay buffer. It proposes a framework based on influence functions to identify second-order influences and a novel selection objective to regularize them, with an efficient implementation. Compared to existing strategies, it accounts for interactions between selection steps and suppresses incidental bias. Experiments on multiple benchmarks show superiority over state-of-the-art methods.
- **核心贡献**: 提出基于二阶影响正则化的重放样本选择方法。
- **创新点**: 识别并正则化连续选择步骤间的二阶影响。
- **结果**: 在多个持续学习基准上优于最先进方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning aims to learn on non-stationary data streams without catastrophically forgetting previous knowledge. Prevalent replay-based methods address this challenge by rehearsing on a small buffer holding the seen data, for which a delicate sample selection strategy is required. However, existing selection schemes typically seek only to maximize the utility of the ongoing selection, overlooking the interference between successive rounds of selection. Motivated by this, we dissect the interaction of sequential selection steps within a framework built on influence functions. We manage to identify a new class of second-order influences that will gradually amplify incidental bias in the replay buffer and compromise the selection process. To regularize the second-order effects, a novel selection objective is proposed, which also has clear connections to two widely adopted criteria. Furthermore, we present an efficient implementation for optimizing the proposed criterion. Experiments on multiple continual learning benchmarks demonstrate the advantage of our approach over state-of-the-art methods. Code is available at https://github.com/feifeiobama/InfluenceCL.

</details>

### Dealing with Cross-Task Class Discrimination in Online Continual Learning. **⭐⭐⭐⭐** (相关度: 30%)
- **链接**: [arXiv:2305.14657](https://arxiv.org/abs/2305.14657) · 📚 被引 17
- **作者**: Yiduo Guo, Bing Liu, Dongyan Zhao
- **🏷️ 机构**: Wangxuan Institute of Computer Technology, Peking University, University of Illinois Chicago,Department of Computer Science
- **会议**: CVPR 2023
- **摘要（中）**: 该论文指出类增量学习中除灾难性遗忘外，还存在跨任务类判别（CTCD）问题，即新类与旧类间决策边界的建立受限于旧数据访问。回放方法虽部分解决此问题，但存在动态训练偏差，降低了回放数据的有效性。作者提出新的优化目标和基于梯度的自适应方法，动态处理在线持续学习中的CTCD问题，实验结果显示显著优于现有方法。
- **摘要（英）**: This paper identifies cross-task class discrimination (CTCD) as a key challenge in class-incremental learning, beyond catastrophic forgetting, and argues that replay methods suffer from dynamic training bias. It proposes a novel optimization objective with gradient-based adaptation to address CTCD online, achieving superior results.
- **核心贡献**: 提出CTCD问题并设计自适应优化方法解决在线持续学习中的类判别挑战。
- **创新点**: 识别动态训练偏差并引入梯度自适应机制。
- **结果**: 实验显示比现有方法有显著提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing continual learning (CL) research regards catastrophic forgetting (CF) as almost the only challenge. This paper argues for another challenge in class-incremental learning (CIL), which we call cross-task class discrimination (CTCD),~i.e., how to establish decision boundaries between the classes of the new task and old tasks with no (or limited) access to the old task data. CTCD is implicitly and partially dealt with by replay-based methods. A replay method saves a small amount of data (replay data) from previous tasks. When a batch of current task data arrives, the system jointly trains the new data and some sampled replay data. The replay data enables the system to partially learn the decision boundaries between the new classes and the old classes as the amount of the saved data is small. However, this paper argues that the replay approach also has a dynamic training bias issue which reduces the effectiveness of the replay data in solving the CTCD problem. A novel optimization objective with a gradient-based adaptive method is proposed to dynamically deal with the problem in the online CL process. Experimental results show that the new method achieves much better results in online CL.

</details>

### Achieving a Better Stability-Plasticity Trade-off via Auxiliary Networks in Continual Learning. **⭐⭐⭐⭐** (相关度: 30%)
- **链接**: [arXiv:2303.09483](https://arxiv.org/abs/2303.09483) · 📚 被引 41
- **作者**: Sanghwan Kim, Lorenzo Noci, Antonio Orvieto, Thomas Hofmann
- **🏷️ 机构**: ETH Z&#x00FC;rich,Z&#x00FC;rich,Switzerland
- **会议**: CVPR 2023
- **摘要（中）**: 该论文针对持续学习中稳定性-塑性权衡未解决且机制不明的问题，提出了辅助网络持续学习（ANCL）方法。ANCL通过附加辅助网络促进塑性，而主模型保持稳定性，并通过正则化器自然插值两者。在任务增量和类增量场景中，ANCL超越了强基线，并通过分析揭示了稳定性-塑性权衡的关键原则。
- **摘要（英）**: This paper proposes Auxiliary Network Continual Learning (ANCL) to address the stability-plasticity trade-off by using an auxiliary network to promote plasticity while the main model ensures stability. The method, implemented as a regularizer, surpasses strong baselines in task and class incremental scenarios and provides insights into the trade-off mechanism.
- **核心贡献**: 提出ANCL框架，通过辅助网络实现更好的稳定性-塑性平衡。
- **创新点**: 引入辅助网络作为塑性促进器，并自然插值正则化。
- **结果**: 在多个场景中超越强基线，并揭示关键原则。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In contrast to the natural capabilities of humans to learn new tasks in a sequential fashion, neural networks are known to suffer from catastrophic forgetting, where the model's performances on old tasks drop dramatically after being optimized for a new task. Since then, the continual learning (CL) community has proposed several solutions aiming to equip the neural network with the ability to learn the current task (plasticity) while still achieving high accuracy on the previous tasks (stability). Despite remarkable improvements, the plasticity-stability trade-off is still far from being solved and its underlying mechanism is poorly understood. In this work, we propose Auxiliary Network Continual Learning (ANCL), a novel method that applies an additional auxiliary network which promotes plasticity to the continually learned model which mainly focuses on stability. More concretely, the proposed framework materializes in a regularizer that naturally interpolates between plasticity and stability, surpassing strong baselines on task incremental and class incremental scenarios. Through extensive analyses on ANCL solutions, we identify some essential principles beneath the stability-plasticity trade-off.

</details>

### Adaptive Plasticity Improvement for Continual Learning. **⭐⭐⭐** (相关度: 25%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00755) · 📚 被引 17
- **作者**: Yan-Shuo Liang, Wu-Jun Li
- **🏷️ 机构**: Nanjing University,National Key Laboratory for Novel Software Technology,Department of Computer Science and Technology,P. R. China
- **会议**: CVPR 2023
- **摘要（中）**: 该论文标题为自适应塑性改进，但摘要为空，无法获取具体方法或实验细节。可能旨在动态调整模型塑性以适应不同任务，但缺乏信息无法评估其创新性和效果。
- **摘要（英）**: This paper, titled 'Adaptive Plasticity Improvement for Continual Learning,' has an empty abstract, so no methods or results are available. It likely focuses on dynamically adjusting plasticity, but its contribution cannot be assessed.
- **核心贡献**: 未明确。
- **创新点**: 未明确。
- **结果**: 未提供。

### Heterogeneous Continual Learning. **⭐⭐** (相关度: 40%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01534)
- **作者**: Divyam Madaan, Hongxu Yin, Wonmin Byeon, Jan Kautz, Pavlo Molchanov
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023
- **摘要（中）**: ①这篇论文针对异构持续学习问题，即不同任务间数据分布和任务结构差异大，导致模型灾难性遗忘严重。②由于摘要缺失，无法具体描述方法，推测可能提出了一种处理异构任务序列的持续学习框架或策略。③相比已有工作，可能强调了对任务异构性的适应能力，而非仅关注同构任务。④效果未知，因摘要缺失。
- **摘要（英）**: This paper addresses heterogeneous continual learning, where tasks differ significantly in data distribution and structure, exacerbating catastrophic forgetting. Due to missing abstract, the method is unclear, likely proposing a framework for heterogeneous task sequences. It may emphasize adaptability to task heterogeneity over homogeneous settings. Results are unknown due to missing abstract.
- **核心贡献**: 提出异构持续学习问题，可能引入新方法应对任务多样性。
- **创新点**: 聚焦任务异构性，区别于传统同构持续学习。
- **结果**: 未知，因摘要缺失。

### Alleviating Catastrophic Forgetting of Incremental Object Detection via Within-Class and Between-Class Knowledge Distillation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01732) · 📚 被引 18
- **作者**: Mengxue Kang, Jinpeng Zhang, Jinming Zhang, Xiashuang Wang, Yang Chen, Zhe Ma et al.
- **🏷️ 机构**: Intelligent Science &amp; Technology Academy of CASIC,Beijing,China,100043, Xinjiang University,Xinjiang,China,830046, The Second Academy of China Aerospace Science and Industry Corporation,Beijing,China,100854
- **会议**: ICCV 2023

### Augmented Box Replay: Overcoming Foreground Shift for Incremental Object Detection.
- **链接**: [arXiv:2307.12427](https://arxiv.org/abs/2307.12427) · 📚 被引 39
- **作者**: Yuyang Liu, Yang Cong, Dipam Goswami, Xialei Liu, Joost van de Weijer
- **🏷️ 机构**: Chinese Academy of Sciences,State Key Laboratory of Robotics, Shenyang Institute of Automation, South China University of Technology, Computer Vision Center, Barcelona
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In incremental learning, replaying stored samples from previous tasks together with current task samples is one of the most efficient approaches to address catastrophic forgetting. However, unlike incremental classification, image replay has not been successfully applied to incremental object detection (IOD). In this paper, we identify the overlooked problem of foreground shift as the main reason for this. Foreground shift only occurs when replaying images of previous tasks and refers to the fact that their background might contain foreground objects of the current task. To overcome this problem, a novel and efficient Augmented Box Replay (ABR) method is developed that only stores and replays foreground objects and thereby circumvents the foreground shift problem. In addition, we propose an innovative Attentive RoI Distillation loss that uses spatial attention from region-of-interest (RoI) features to constrain current model to focus on the most important information from old model. ABR significantly reduces forgetting of previous classes while maintaining high plasticity in current classes. Moreover, it considerably reduces the storage requirements when compared to standard image replay. Comprehensive experiments on Pascal-VOC and COCO datasets support the state-of-the-art performance of our model.

</details>

### Label-Efficient Online Continual Object Detection in Streaming Video.
- **链接**: [arXiv:2206.00309](https://arxiv.org/abs/2206.00309) · 📚 被引 15
- **作者**: Jay Zhangjie Wu, David Junhao Zhang, Wynne Hsu, Mengmi Zhang, Mike Zheng Shou
- **🏷️ 机构**: Show Lab, National University of Singapore, Nanyang Technological University,School of Computer Science and Engineering,Singapore
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Humans can watch a continuous video stream and effortlessly perform continual acquisition and transfer of new knowledge with minimal supervision yet retaining previously learnt experiences. In contrast, existing continual learning (CL) methods require fully annotated labels to effectively learn from individual frames in a video stream. Here, we examine a more realistic and challenging problem$\unicode{x2014}$Label-Efficient Online Continual Object Detection (LEOCOD) in streaming video. We propose a plug-and-play module, Efficient-CLS, that can be easily inserted into and improve existing continual learners for object detection in video streams with reduced data annotation costs and model retraining time. We show that our method has achieved significant improvement with minimal forgetting across all supervision levels on two challenging CL benchmarks for streaming real-world videos. Remarkably, with only 25% annotated video frames, our method still outperforms the base CL learners, which are trained with 100% annotations on all video frames. The data and source code will be publicly available at https://github.com/showlab/Efficient-CLS.

</details>

### On the Effectiveness of LayerNorm Tuning for Continual Learning in Vision Transformers.
- **链接**: [arXiv:2308.09610](https://arxiv.org/abs/2308.09610) · 📚 被引 9
- **作者**: Thomas De Min, Massimiliano Mancini, Karteek Alahari, Xavier Alameda-Pineda, Elisa Ricci
- **🏷️ 机构**: University of Trento, Inria, Univ. Grenoble Alpes,CNRS, Grenoble INP, LJK,Grenoble,France,38000
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> State-of-the-art rehearsal-free continual learning methods exploit the peculiarities of Vision Transformers to learn task-specific prompts, drastically reducing catastrophic forgetting. However, there is a tradeoff between the number of learned parameters and the performance, making such models computationally expensive. In this work, we aim to reduce this cost while maintaining competitive performance. We achieve this by revisiting and extending a simple transfer learning idea: learning task-specific normalization layers. Specifically, we tune the scale and bias parameters of LayerNorm for each continual learning task, selecting them at inference time based on the similarity between task-specific keys and the output of the pre-trained model. To make the classifier robust to incorrect selection of parameters during inference, we introduce a two-stage training procedure, where we first optimize the task-specific parameters and then train the classifier with the same selection procedure of the inference time. Experiments on ImageNet-R and CIFAR-100 show that our method achieves results that are either superior or on par with {the state of the art} while being computationally cheaper.

</details>

### Online Prototype Learning for Online Continual Learning.
- **链接**: [arXiv:2308.00301](https://arxiv.org/abs/2308.00301) · 📚 被引 64
- **作者**: Yujie Wei, Jiaxin Ye, Zhizhong Huang, Junping Zhang, Hongming Shan
- **🏷️ 机构**: Fudan University,Institute of Science and Technology for Brain-Inspired Intelligence, School of Computer Science Fudan University,Shanghai Key Lab of Intelligent Information Processing
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Online continual learning (CL) studies the problem of learning continuously from a single-pass data stream while adapting to new data and mitigating catastrophic forgetting. Recently, by storing a small subset of old data, replay-based methods have shown promising performance. Unlike previous methods that focus on sample storage or knowledge distillation against catastrophic forgetting, this paper aims to understand why the online learning models fail to generalize well from a new perspective of shortcut learning. We identify shortcut learning as the key limiting factor for online CL, where the learned features may be biased, not generalizable to new tasks, and may have an adverse impact on knowledge distillation. To tackle this issue, we present the online prototype learning (OnPro) framework for online CL. First, we propose online prototype equilibrium to learn representative features against shortcut learning and discriminative features to avoid class confusion, ultimately achieving an equilibrium status that separates all seen classes well while learning new classes. Second, with the feedback of online prototypes, we devise a novel adaptive prototypical feedback mechanism to sense the classes that are easily misclassified and then enhance their boundaries. Extensive experimental results on widely-used benchmark datasets demonstrate the superior performance of OnPro over the state-of-the-art baseline methods. Source code is available at https://github.com/weilllllls/OnPro.

</details>

### CBA: Improving Online Continual Learning via Continual Bias Adaptor.
- **链接**: [arXiv:2308.06925](https://arxiv.org/abs/2308.06925) · 📚 被引 24
- **作者**: Quanziang Wang, Renzhen Wang, Yichen Wu, Xixi Jia, Deyu Meng
- **🏷️ 机构**: Xi&#x2019;an Jiaotong University, City University of Hong Kong, Xidian University
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Online continual learning (CL) aims to learn new knowledge and consolidate previously learned knowledge from non-stationary data streams. Due to the time-varying training setting, the model learned from a changing distribution easily forgets the previously learned knowledge and biases toward the newly received task. To address this problem, we propose a Continual Bias Adaptor (CBA) module to augment the classifier network to adapt to catastrophic distribution change during training, such that the classifier network is able to learn a stable consolidation of previously learned tasks. In the testing stage, CBA can be removed which introduces no additional computation cost and memory overhead. We theoretically reveal the reason why the proposed method can effectively alleviate catastrophic distribution shifts, and empirically demonstrate its effectiveness through extensive experiments based on four rehearsal-based baselines and three public continual learning benchmarks.

</details>

### Generating Instance-level Prompts for Rehearsal-free Continual Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01088) · 📚 被引 60
- **作者**: Dahuin Jung, Dongyoon Han, Jihwan Bang, Hwanjun Song
- **🏷️ 机构**: Seoul National University,Department of Electrical and Computer Engineering,Seoul,Korea, NAVER AI Lab, NAVER Cloud
- **会议**: ICCV 2023

### Introducing Language Guidance in Prompt-based Continual Learning.
- **链接**: [arXiv:2308.15827](https://arxiv.org/abs/2308.15827) · 📚 被引 35
- **作者**: Muhammad Gul Zain Ali Khan, Muhammad Ferjad Naeem, Luc Van Gool, Didier Stricker, Federico Tombari, Muhammad Zeshan Afzal
- **🏷️ 机构**: RPTU, ETH Z&#x00FC;rich, TUM
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual Learning aims to learn a single model on a sequence of tasks without having access to data from previous tasks. The biggest challenge in the domain still remains catastrophic forgetting: a loss in performance on seen classes of earlier tasks. Some existing methods rely on an expensive replay buffer to store a chunk of data from previous tasks. This, while promising, becomes expensive when the number of tasks becomes large or data can not be stored for privacy reasons. As an alternative, prompt-based methods have been proposed that store the task information in a learnable prompt pool. This prompt pool instructs a frozen image encoder on how to solve each task. While the model faces a disjoint set of classes in each task in this setting, we argue that these classes can be encoded to the same embedding space of a pre-trained language encoder. In this work, we propose Language Guidance for Prompt-based Continual Learning (LGCL) as a plug-in for prompt-based methods. LGCL is model agnostic and introduces language guidance at the task level in the prompt pool and at the class level on the output feature of the vision encoder. We show with extensive experimentation that LGCL consistently improves the performance of prompt-based continual learning methods to set a new state-of-the art. LGCL achieves these performance improvements without needing any additional learnable parameters.

</details>

### Online Continual Learning on Hierarchical Label Expansion.
- **链接**: [arXiv:2308.14374](https://arxiv.org/abs/2308.14374) · 📚 被引 4
- **作者**: Byung Hyun Lee, Okchul Jung, Jonghyun Choi, Se Young Chun
- **🏷️ 机构**: Seoul National University,Dept. of ECE,Republic of Korea, Yonsei University,Republic of Korea
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning (CL) enables models to adapt to new tasks and environments without forgetting previously learned knowledge. While current CL setups have ignored the relationship between labels in the past task and the new task with or without small task overlaps, real-world scenarios often involve hierarchical relationships between old and new tasks, posing another challenge for traditional CL approaches. To address this challenge, we propose a novel multi-level hierarchical class incremental task configuration with an online learning constraint, called hierarchical label expansion (HLE). Our configuration allows a network to first learn coarse-grained classes, with data labels continually expanding to more fine-grained classes in various hierarchy depths. To tackle this new setup, we propose a rehearsal-based method that utilizes hierarchy-aware pseudo-labeling to incorporate hierarchical class information. Additionally, we propose a simple yet effective memory management and sampling strategy that selectively adopts samples of newly encountered classes. Our experiments demonstrate that our proposed method can effectively use hierarchy on our HLE setup to improve classification accuracy across all levels of hierarchies, regardless of depth and class imbalance ratio, outperforming prior state-of-the-art works by significant margins while also outperforming them on the conventional disjoint, blurry and i-Blurry CL setups.

</details>

### Measuring Asymmetric Gradient Discrepancy in Parallel Continual Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01048) · 📚 被引 9
- **作者**: Fan Lyu, Qing Sun, Fanhua Shang, Liang Wan, Wei Feng
- **🏷️ 机构**: Tianjin University,College of Intelligence and Computing
- **会议**: ICCV 2023

### NAPA-VQ: Neighborhood Aware Prototype Augmentation with Vector Quantization for Continual Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01072) · 📚 被引 16
- **作者**: Tamasha Malepathirana, Damith A. Senanayake, Saman K. Halgamuge
- **🏷️ 机构**: The University of Melbourne,Dept. of Mechanical Engineering
- **会议**: ICCV 2023

### Class-Incremental Grouping Network for Continual Audio-Visual Learning.
- **链接**: [arXiv:2309.05281](https://arxiv.org/abs/2309.05281) · 📚 被引 20
- **作者**: Shentong Mo, Weiguo Pian, Yapeng Tian
- **🏷️ 机构**: Carnegie Mellon University, University of Texas at Dallas
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning is a challenging problem in which models need to be trained on non-stationary data across sequential tasks for class-incremental learning. While previous methods have focused on using either regularization or rehearsal-based frameworks to alleviate catastrophic forgetting in image classification, they are limited to a single modality and cannot learn compact class-aware cross-modal representations for continual audio-visual learning. To address this gap, we propose a novel class-incremental grouping network (CIGN) that can learn category-wise semantic features to achieve continual audio-visual learning. Our CIGN leverages learnable audio-visual class tokens and audio-visual grouping to continually aggregate class-aware features. Additionally, it utilizes class tokens distillation and continual grouping to prevent forgetting parameters learned from previous tasks, thereby improving the model's ability to capture discriminative audio-visual categories. We conduct extensive experiments on VGGSound-Instruments, VGGSound-100, and VGG-Sound Sources benchmarks. Our experimental results demonstrate that the CIGN achieves state-of-the-art audio-visual class-incremental learning performance. Code is available at https://github.com/stoneMo/CIGN.

</details>

### ICICLE: Interpretable Class Incremental Continual Learning.
- **链接**: [arXiv:2303.07811](https://arxiv.org/abs/2303.07811) · 📚 被引 21
- **作者**: Dawid Rymarczyk, Joost van de Weijer, Bartosz Zielinski, Bartlomiej Twardowski
- **🏷️ 机构**: Jagiellonian University,Faculty of Mathematics and Computer Science, Autonomous University of Barcelona
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning enables incremental learning of new tasks without forgetting those previously learned, resulting in positive knowledge transfer that can enhance performance on both new and old tasks. However, continual learning poses new challenges for interpretability, as the rationale behind model predictions may change over time, leading to interpretability concept drift. We address this problem by proposing Interpretable Class-InCremental LEarning (ICICLE), an exemplar-free approach that adopts a prototypical part-based approach. It consists of three crucial novelties: interpretability regularization that distills previously learned concepts while preserving user-friendly positive reasoning; proximity-based prototype initialization strategy dedicated to the fine-grained setting; and task-recency bias compensation devoted to prototypical parts. Our experimental results demonstrate that ICICLE reduces the interpretability concept drift and outperforms the existing exemplar-free methods of common class-incremental learning when applied to concept-based models.

</details>

### Instance and Category Supervision are Alternate Learners for Continual Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00515) · 📚 被引 2
- **作者**: Xudong Tian, Zhizhong Zhang, Xin Tan, Jun Liu, Chengjie Wang, Yanyun Qu et al.
- **🏷️ 机构**: East China Normal University, Tencent YouTu Lab, Xiamen University
- **会议**: ICCV 2023

### Data Augmented Flatness-aware Gradient Projection for Continual Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00518) · 📚 被引 15
- **作者**: Enneng Yang, Li Shen, Zhenyi Wang, Shiwei Liu, Guibing Guo, Xingwei Wang
- **🏷️ 机构**: Northeastern University,China, JD Explore Academy,China, University of Maryland,USA
- **会议**: ICCV 2023

### TARGET: Federated Class-Continual Learning via Exemplar-Free Distillation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00441) · 📚 被引 71
- **作者**: Jie Zhang, Chen Chen, Weiming Zhuang, Lingjuan Lyu
- **🏷️ 机构**: ETH Zurich, Sony AI
- **会议**: ICCV 2023

### SLCA: Slow Learner with Classifier Alignment for Continual Learning on a Pre-trained Model.
- **链接**: [arXiv:2303.05118](https://arxiv.org/abs/2303.05118) · 📚 被引 113
- **作者**: Gengwei Zhang, Liyuan Wang, Guoliang Kang, Ling Chen, Yunchao Wei
- **🏷️ 机构**: University of Technology Sydney, Tsinghua University, Beihang University
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The goal of continual learning is to improve the performance of recognition models in learning sequentially arrived data. Although most existing works are established on the premise of learning from scratch, growing efforts have been devoted to incorporating the benefits of pre-training. However, how to adaptively exploit the pre-trained knowledge for each incremental task while maintaining its generalizability remains an open question. In this work, we present an extensive analysis for continual learning on a pre-trained model (CLPM), and attribute the key challenge to a progressive overfitting problem. Observing that selectively reducing the learning rate can almost resolve this issue in the representation layer, we propose a simple but extremely effective approach named Slow Learner with Classifier Alignment (SLCA), which further improves the classification layer by modeling the class-wise distributions and aligning the classification layers in a post-hoc fashion. Across a variety of scenarios, our proposal provides substantial improvements for CLPM (e.g., up to 49.76%, 50.05%, 44.69% and 40.16% on Split CIFAR-100, Split ImageNet-R, Split CUB-200 and Split Cars-196, respectively), and thus outperforms state-of-the-art approaches by a large margin. Based on such a strong baseline, critical factors and promising directions are analyzed in-depth to facilitate subsequent research. Code has been made available at: https://github.com/GengDavid/SLCA.

</details>

### Improving Replay Sample Selection and Storage for Less Forgetting in Continual Learning.
- **链接**: [arXiv:2308.01895](https://arxiv.org/abs/2308.01895) · 📚 被引 19
- **作者**: Daniel Brignac, Niels Lobo, Abhijit Mahalanobis
- **🏷️ 机构**: University of Arizona,Tucson,Arizona, University of Central Florida,Orlando,Florida
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning seeks to enable deep learners to train on a series of tasks of unknown length without suffering from the catastrophic forgetting of previous tasks. One effective solution is replay, which involves storing few previous experiences in memory and replaying them when learning the current task. However, there is still room for improvement when it comes to selecting the most informative samples for storage and determining the optimal number of samples to be stored. This study aims to address these issues with a novel comparison of the commonly used reservoir sampling to various alternative population strategies and providing a novel detailed analysis of how to find the optimal number of stored samples.

</details>

### Memory Population in Continual Learning via Outlier Elimination.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00373) · 📚 被引 1
- **作者**: Julio Hurtado, Alain Raymond-Saez, Vladimir Araujo, Vincenzo Lomonaco, Alvaro Soto, Davide Bacciu
- **🏷️ 机构**: University of Pisa, Pontificia Universidad Cat&#x00F3;lica de Chile
- **会议**: ICCV 2023

### Looking through the past: better knowledge retention for generative replay in continual learning.
- **链接**: [arXiv:2309.10012](https://arxiv.org/abs/2309.10012) · 📚 被引 2
- **作者**: Valeriya Khan, Sebastian Cygert, Bartlomiej Twardowski, Tomasz Trzcinski
- **🏷️ 机构**: IDEAS NCBR, Warsaw, Poland
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this work, we improve the generative replay in a continual learning setting to perform well on challenging scenarios. Current generative rehearsal methods are usually benchmarked on small and simple datasets as they are not powerful enough to generate more complex data with a greater number of classes. We notice that in VAE-based generative replay, this could be attributed to the fact that the generated features are far from the original ones when mapped to the latent space. Therefore, we propose three modifications that allow the model to learn and generate complex data. More specifically, we incorporate the distillation in latent space between the current and previous models to reduce feature drift. Additionally, a latent matching for the reconstruction and original data is proposed to improve generated features alignment. Further, based on the observation that the reconstructions are better for preserving knowledge, we add the cycling of generations through the previously trained model to make them closer to the original data. Our method outperforms other generative replay methods in various scenarios. Code available at https://github.com/valeriya-khan/looking-through-the-past.

</details>

### Continual Learning with Deep Streaming Regularized Discriminant Analysis.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00370) · 📚 被引 2
- **作者**: Joe Khawand, Peter Hanappe, David Colliaux
- **🏷️ 机构**: Ecole Polytechnique, Sony Computer Science Laboratories Paris
- **会议**: ICCV 2023

### Flashback for Continual Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00368) · 📚 被引 2
- **作者**: Leila Mahmoodi, Mehrtash Harandi, Peyman Moghadam
- **🏷️ 机构**: Monash University, CSIRO,Data61
- **会议**: ICCV 2023

### Instant Continual Learning of Neural Radiance Fields.
- **链接**: [arXiv:2309.01811](https://arxiv.org/abs/2309.01811) · 📚 被引 11
- **作者**: Ryan Po, Zhengyang Dong, Alexander W. Bergman, Gordon Wetzstein
- **🏷️ 机构**: Stanford University
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural radiance fields (NeRFs) have emerged as an effective method for novel-view synthesis and 3D scene reconstruction. However, conventional training methods require access to all training views during scene optimization. This assumption may be prohibitive in continual learning scenarios, where new data is acquired in a sequential manner and a continuous update of the NeRF is desired, as in automotive or remote sensing applications. When naively trained in such a continual setting, traditional scene representation frameworks suffer from catastrophic forgetting, where previously learned knowledge is corrupted after training on new data. Prior works in alleviating forgetting with NeRFs suffer from low reconstruction quality and high latency, making them impractical for real-world application. We propose a continual learning framework for training NeRFs that leverages replay-based methods combined with a hybrid explicit--implicit scene representation. Our method outperforms previous methods in reconstruction quality when trained in a continual setting, while having the additional benefit of being an order of magnitude faster.

</details>

### Selective Freezing for Efficient Continual Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00381) · 📚 被引 12
- **作者**: Amelia Sorrenti, Giovanni Bellitto, Federica Proietto Salanitri, Matteo Pennisi, Concetto Spampinato, Simone Palazzo
- **🏷️ 机构**: University of Catania,PeRCeiVe Lab,Catania,Italy
- **会议**: ICCV 2023

### A Comprehensive Empirical Evaluation on Online Continual Learning.
- **链接**: [arXiv:2308.10328](https://arxiv.org/abs/2308.10328) · 📚 被引 16
- **作者**: Albin Soutif-Cormerais, Antonio Carta, Andrea Cossu, Julio Hurtado, Vincenzo Lomonaco, Joost van de Weijer et al.
- **🏷️ 机构**: Universitat Aut&#x00F2;noma de Barcelona,Computer Vision Center,Barcelona,Spain, University of Pisa,Department of Computer Science,Pisa,Italy, Scuola Normale Superiore,Pisa,Italy
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Online continual learning aims to get closer to a live learning experience by learning directly on a stream of data with temporally shifting distribution and by storing a minimum amount of data from that stream. In this empirical evaluation, we evaluate various methods from the literature that tackle online continual learning. More specifically, we focus on the class-incremental setting in the context of image classification, where the learner must learn new classes incrementally from a stream of data. We compare these methods on the Split-CIFAR100 and Split-TinyImagenet benchmarks, and measure their average accuracy, forgetting, stability, and quality of the representations, to evaluate various aspects of the algorithm at the end but also during the whole training period. We find that most methods suffer from stability and underfitting issues. However, the learned representations are comparable to i.i.d. training under the same computational budget. No clear winner emerges from the results and basic experience replay, when properly tuned and implemented, is a very strong baseline. We release our modular and extensible codebase at https://github.com/AlbinSou/ocl_survey based on the avalanche framework to reproduce our results and encourage future research.

</details>

### Adapt Your Teacher: Improving Knowledge Distillation for Exemplar-free Continual Learning.
- **链接**: [arXiv:2308.09544](https://arxiv.org/abs/2308.09544) · 📚 被引 4
- **作者**: Filip Szatkowski, Mateusz Pyla, Marcin Przewiezlikowski, Sebastian Cygert, Bartlomiej Twardowski, Tomasz Trzcinski
- **🏷️ 机构**: Warsaw University of Technology, IDEAS NCBR
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this work, we investigate exemplar-free class incremental learning (CIL) with knowledge distillation (KD) as a regularization strategy, aiming to prevent forgetting. KD-based methods are successfully used in CIL, but they often struggle to regularize the model without access to exemplars of the training data from previous tasks. Our analysis reveals that this issue originates from substantial representation shifts in the teacher network when dealing with out-of-distribution data. This causes large errors in the KD loss component, leading to performance degradation in CIL models. Inspired by recent test-time adaptation methods, we introduce Teacher Adaptation (TA), a method that concurrently updates the teacher and the main models during incremental training. Our method seamlessly integrates with KD-based CIL approaches and allows for consistent enhancement of their performance across multiple exemplar-free CIL benchmarks. The source code for our method is available at https://github.com/fszatkowski/cl-teacher-adaptation.

</details>

### ScrollNet: Dynamic Weight Importance for Continual Learning.
- **链接**: [arXiv:2308.16567](https://arxiv.org/abs/2308.16567) · 📚 被引 6
- **作者**: Fei Yang, Kai Wang, Joost van de Weijer
- **🏷️ 机构**: Universitat Aut&#x00F2;noma de Barcelona,Computer Vision Center,Barcelona,Spain
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The principle underlying most existing continual learning (CL) methods is to prioritize stability by penalizing changes in parameters crucial to old tasks, while allowing for plasticity in other parameters. The importance of weights for each task can be determined either explicitly through learning a task-specific mask during training (e.g., parameter isolation-based approaches) or implicitly by introducing a regularization term (e.g., regularization-based approaches). However, all these methods assume that the importance of weights for each task is unknown prior to data exposure. In this paper, we propose ScrollNet as a scrolling neural network for continual learning. ScrollNet can be seen as a dynamic network that assigns the ranking of weight importance for each task before data exposure, thus achieving a more favorable stability-plasticity tradeoff during sequential task learning by reassigning this ranking for different tasks. Additionally, we demonstrate that ScrollNet can be combined with various CL methods, including regularization-based and replay-based approaches. Experimental results on CIFAR100 and TinyImagenet datasets show the effectiveness of our proposed method. We release our code at https://github.com/FireFYF/ScrollNet.git.

</details>

### Self-Organizing Pathway Expansion for Non-Exemplar Class-Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01759) · 📚 被引 8
- **作者**: Kai Zhu, Kecheng Zheng, Ruili Feng, Deli Zhao, Yang Cao, Zheng-Jun Zha
- **🏷️ 机构**: Alibaba Group, Zhejiang University, University of Science and Technology of China
- **会议**: ICCV 2023

### Dynamic Residual Classifier for Class Incremental Learning.
- **链接**: [arXiv:2308.13305](https://arxiv.org/abs/2308.13305) · 📚 被引 36
- **作者**: Xiuwei Chen, Xiaobin Chang
- **🏷️ 机构**: Sun Yat-sen University,School of Artificial Intelligence,China
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The rehearsal strategy is widely used to alleviate the catastrophic forgetting problem in class incremental learning (CIL) by preserving limited exemplars from previous tasks. With imbalanced sample numbers between old and new classes, the classifier learning can be biased. Existing CIL methods exploit the long-tailed (LT) recognition techniques, e.g., the adjusted losses and the data re-sampling methods, to handle the data imbalance issue within each increment task. In this work, the dynamic nature of data imbalance in CIL is shown and a novel Dynamic Residual Classifier (DRC) is proposed to handle this challenging scenario. Specifically, DRC is built upon a recent advance residual classifier with the branch layer merging to handle the model-growing problem. Moreover, DRC is compatible with different CIL pipelines and substantially improves them. Combining DRC with the model adaptation and fusion (MAF) pipeline, this method achieves state-of-the-art results on both the conventional CIL and the LT-CIL benchmarks. Extensive experiments are also conducted for a detailed analysis. The code is publicly available.

</details>

### Heterogeneous Forgetting Compensation for Class-Incremental Learning.
- **链接**: [arXiv:2308.03374](https://arxiv.org/abs/2308.03374) · 📚 被引 22
- **作者**: Jiahua Dong, Wenqi Liang, Yang Cong, Gan Sun
- **🏷️ 机构**: Chinese Academy of Sciences,State Key Laboratory of Robotics, Shenyang Institute of Automation,Shenyang,China,110016, South China University of Technology,Guangzhou,China,510640
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Class-incremental learning (CIL) has achieved remarkable successes in learning new classes consecutively while overcoming catastrophic forgetting on old categories. However, most existing CIL methods unreasonably assume that all old categories have the same forgetting pace, and neglect negative influence of forgetting heterogeneity among different old classes on forgetting compensation. To surmount the above challenges, we develop a novel Heterogeneous Forgetting Compensation (HFC) model, which can resolve heterogeneous forgetting of easy-to-forget and hard-to-forget old categories from both representation and gradient aspects. Specifically, we design a task-semantic aggregation block to alleviate heterogeneous forgetting from representation aspect. It aggregates local category information within each task to learn task-shared global representations. Moreover, we develop two novel plug-and-play losses: a gradient-balanced forgetting compensation loss and a gradient-balanced relation distillation loss to alleviate forgetting from gradient aspect. They consider gradient-balanced compensation to rectify forgetting heterogeneity of old categories and heterogeneous relation consistency. Experiments on several representative datasets illustrate effectiveness of our HFC model. The code is available at https://github.com/JiahuaDong/HFC.

</details>

### Knowledge Restore and Transfer for Multi-Label Class-Incremental Learning.
- **链接**: [arXiv:2302.13334](https://arxiv.org/abs/2302.13334) · 📚 被引 8
- **作者**: Songlin Dong, Haoyu Luo, Yuhang He, Xing Wei, Jie Cheng, Yihong Gong
- **🏷️ 机构**: Xi&#x2019;an Jiaotong University,College of Artificial Intelligence, Xi&#x2019;an Jiaotong University,School of Software Engineering, Huawei Technologies,ACS Lab,Shenzhen,China
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Current class-incremental learning research mainly focuses on single-label classification tasks while multi-label class-incremental learning (MLCIL) with more practical application scenarios is rarely studied. Although there have been many anti-forgetting methods to solve the problem of catastrophic forgetting in class-incremental learning, these methods have difficulty in solving the MLCIL problem due to label absence and information dilution. In this paper, we propose a knowledge restore and transfer (KRT) framework for MLCIL, which includes a dynamic pseudo-label (DPL) module to restore the old class knowledge and an incremental cross-attention(ICA) module to save session-specific knowledge and transfer old class knowledge to the new model sufficiently. Besides, we propose a token loss to jointly optimize the incremental cross-attention module. Experimental results on MS-COCO and PASCAL VOC datasets demonstrate the effectiveness of our method for improving recognition performance and mitigating forgetting on multi-label class-incremental learning tasks.

</details>

### Online Class Incremental Learning on Stochastic Blurry Task Boundary via Mask and Visual Prompt Tuning.
- **链接**: [arXiv:2308.09303](https://arxiv.org/abs/2308.09303) · 📚 被引 24
- **作者**: Jun-Yeong Moon, Keon-Hee Park, Jung Uk Kim, Gyeong-Moon Park
- **🏷️ 机构**: Kyung Hee University,Yongin,Republic of Korea
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning aims to learn a model from a continuous stream of data, but it mainly assumes a fixed number of data and tasks with clear task boundaries. However, in real-world scenarios, the number of input data and tasks is constantly changing in a statistical way, not a static way. Although recently introduced incremental learning scenarios having blurry task boundaries somewhat address the above issues, they still do not fully reflect the statistical properties of real-world situations because of the fixed ratio of disjoint and blurry samples. In this paper, we propose a new Stochastic incremental Blurry task boundary scenario, called Si-Blurry, which reflects the stochastic properties of the real-world. We find that there are two major challenges in the Si-Blurry scenario: (1) inter- and intra-task forgettings and (2) class imbalance problem. To alleviate them, we introduce Mask and Visual Prompt tuning (MVP). In MVP, to address the inter- and intra-task forgetting issues, we propose a novel instance-wise logit masking and contrastive visual prompt tuning loss. Both of them help our model discern the classes to be learned in the current batch. It results in consolidating the previous knowledge. In addition, to alleviate the class imbalance problem, we introduce a new gradient similarity-based focal loss and adaptive feature scaling to ease overfitting to the major classes and underfitting to the minor classes. Extensive experiments show that our proposed MVP significantly outperforms the existing state-of-the-art methods in our challenging Si-Blurry scenario.

</details>

### First Session Adaptation: A Strong Replay-Free Baseline for Class-Incremental Learning.
- **链接**: [arXiv:2303.13199](https://arxiv.org/abs/2303.13199) · 📚 被引 24
- **作者**: Aristeidis Panos, Yuriko Kobe, Daniel Olmeda Reino, Rahaf Aljundi, Richard E. Turner
- **🏷️ 机构**: University of Cambridge, Toyota Motor Europe
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In Class-Incremental Learning (CIL) an image classification system is exposed to new classes in each learning session and must be updated incrementally. Methods approaching this problem have updated both the classification head and the feature extractor body at each session of CIL. In this work, we develop a baseline method, First Session Adaptation (FSA), that sheds light on the efficacy of existing CIL approaches and allows us to assess the relative performance contributions from head and body adaption. FSA adapts a pre-trained neural network body only on the first learning session and fixes it thereafter; a head based on linear discriminant analysis (LDA), is then placed on top of the adapted body, allowing exact updates through CIL. FSA is replay-free i.e.~it does not memorize examples from previous sessions of continual learning. To empirically motivate FSA, we first consider a diverse selection of 22 image-classification datasets, evaluating different heads and body adaptation techniques in high/low-shot offline settings. We find that the LDA head performs well and supports CIL out-of-the-box. We also find that Featurewise Layer Modulation (FiLM) adapters are highly effective in the few-shot setting, and full-body adaption in the high-shot setting. Second, we empirically investigate various CIL settings including high-shot CIL and few-shot CIL, including settings that have previously been used in the literature. We show that FSA significantly improves over the state-of-the-art in 15 of the 16 settings considered. FSA with FiLM adapters is especially performant in the few-shot setting. These results indicate that current approaches to continuous body adaptation are not working as expected. Finally, we propose a measure that can be applied to a set of unlabelled inputs which is predictive of the benefits of body adaptation.

</details>

### Space-time Prompting for Video Class-incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01096) · 📚 被引 15
- **作者**: Yixuan Pei, Zhiwu Qing, Shiwei Zhang, Xiang Wang, Yingya Zhang, Deli Zhao et al.
- **🏷️ 机构**: Xi&#x2019;an Jiaotong University, Huazhong University of Science and Technology, Alibaba Group
- **会议**: ICCV 2023

### Audio-Visual Class-Incremental Learning.
- **链接**: [arXiv:2308.11073](https://arxiv.org/abs/2308.11073)
- **作者**: Weiguo Pian, Shentong Mo, Yunhui Guo, Yapeng Tian
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we introduce audio-visual class-incremental learning, a class-incremental learning scenario for audio-visual video recognition. We demonstrate that joint audio-visual modeling can improve class-incremental learning, but current methods fail to preserve semantic similarity between audio and visual features as incremental step grows. Furthermore, we observe that audio-visual correlations learned in previous tasks can be forgotten as incremental steps progress, leading to poor performance. To overcome these challenges, we propose AV-CIL, which incorporates Dual-Audio-Visual Similarity Constraint (D-AVSC) to maintain both instance-aware and class-aware semantic similarity between audio-visual modalities and Visual Attention Distillation (VAD) to retain previously learned audio-guided visual attentive ability. We create three audio-visual class-incremental datasets, AVE-Class-Incremental (AVE-CI), Kinetics-Sounds-Class-Incremental (K-S-CI), and VGGSound100-Class-Incremental (VS100-CI) based on the AVE, Kinetics-Sounds, and VGGSound datasets, respectively. Our experiments on AVE-CI, K-S-CI, and VS100-CI demonstrate that AV-CIL significantly outperforms existing class-incremental learning methods in audio-visual class-incremental learning. Code and data are available at: https://github.com/weiguoPian/AV-CIL_ICCV2023.

</details>

### Prototype Reminiscence and Augmented Asymmetric Knowledge Aggregation for Non-Exemplar Class-Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00170) · 📚 被引 48
- **作者**: Wuxuan Shi, Mang Ye
- **🏷️ 机构**: Wuhan University,School of Computer Science,Wuhan,China
- **会议**: ICCV 2023

### When Prompt-based Incremental Learning Does Not Meet Strong Pretraining.
- **链接**: [arXiv:2308.10445](https://arxiv.org/abs/2308.10445) · 📚 被引 39
- **作者**: Yu-Ming Tang, Yi-Xing Peng, Wei-Shi Zheng
- **🏷️ 机构**: Sun Yat-sen University,School of Computer Science and Engineering,China
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Incremental learning aims to overcome catastrophic forgetting when learning deep networks from sequential tasks. With impressive learning efficiency and performance, prompt-based methods adopt a fixed backbone to sequential tasks by learning task-specific prompts. However, existing prompt-based methods heavily rely on strong pretraining (typically trained on ImageNet-21k), and we find that their models could be trapped if the potential gap between the pretraining task and unknown future tasks is large. In this work, we develop a learnable Adaptive Prompt Generator (APG). The key is to unify the prompt retrieval and prompt learning processes into a learnable prompt generator. Hence, the whole prompting process can be optimized to reduce the negative effects of the gap between tasks effectively. To make our APG avoid learning ineffective knowledge, we maintain a knowledge pool to regularize APG with the feature distribution of each class. Extensive experiments show that our method significantly outperforms advanced methods in exemplar-free incremental learning without (strong) pretraining. Besides, under strong retraining, our method also has comparable performance to existing prompt-based models, showing that our method can still benefit from pretraining. Codes can be found at https://github.com/TOM-tym/APG

</details>

### Multimodal Parameter-Efficient Few-Shot Class Incremental Learning.
- **链接**: [arXiv:2303.04751](https://arxiv.org/abs/2303.04751) · 📚 被引 37
- **作者**: Marco D'Alessandro, Alberto Alonso, Enrique Calabrés, Mikel Galar
- **🏷️ 机构**: Neuraptic AI, Public University of Navarra
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Few-Shot Class Incremental Learning (FSCIL) is a challenging continual learning task, where limited training examples are available during several learning sessions. To succeed in this task, it is necessary to avoid over-fitting new classes caused by biased distributions in the few-shot training sets. The general approach to address this issue involves enhancing the representational capability of a pre-defined backbone architecture by adding special modules for backward compatibility with older classes. However, this approach has not yet solved the dilemma of ensuring high classification accuracy over time while reducing the gap between the performance obtained on larger training sets and the smaller ones. In this work, we propose an alternative approach called Continual Parameter-Efficient CLIP (CPE-CLIP) to reduce the loss of information between different learning sessions. Instead of adapting additional modules to address information loss, we leverage the vast knowledge acquired by CLIP in large-scale pre-training and its effectiveness in generalizing to new concepts. Our approach is multimodal and parameter-efficient, relying on learnable prompts for both the language and vision encoders to enable transfer learning across sessions. We also introduce prompt regularization to improve performance and prevent forgetting. Our experimental results demonstrate that CPE-CLIP significantly improves FSCIL performance compared to state-of-the-art proposals while also drastically reducing the number of learnable parameters and training costs.

</details>

### Class-Incremental Learning of Plant and Disease Detection: Growing Branches with Knowledge Distillation.
- **链接**: [arXiv:2304.06619](https://arxiv.org/abs/2304.06619) · 📚 被引 9
- **作者**: Mathieu Pagé Fortin
- **🏷️ 机构**: Laval University,Canada
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper investigates the problem of class-incremental object detection for agricultural applications where a model needs to learn new plant species and diseases incrementally without forgetting the previously learned ones. We adapt two public datasets to include new categories over time, simulating a more realistic and dynamic scenario. We then compare three class-incremental learning methods that leverage different forms of knowledge distillation to mitigate catastrophic forgetting. Our experiments show that all three methods suffer from catastrophic forgetting, but the Dynamic Y-KD approach, which additionally uses a dynamic architecture that grows new branches to learn new tasks, outperforms ILOD and Faster-ILOD in most settings both on new and old classes. These results highlight the challenges and opportunities of continual object detection for agricultural applications. In particular, we hypothesize that the large intra-class and small inter-class variability that is typical of plant images exacerbate the difficulty of learning new categories without interfering with previous knowledge. We publicly release our code to encourage future work.

</details>

### Decision Boundary Optimization for Few-shot Class-Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00376) · 📚 被引 7
- **作者**: Chenxu Guo, Qi Zhao, Shuchang Lyu, Binghao Liu, Chunlei Wang, Lijiang Chen et al.
- **🏷️ 机构**: Beihang University,Department of Electronic Information Engineering, University of Liverpool,Department of Computer Science
- **会议**: ICCV 2023

### Class-Incremental Learning using Diffusion Model for Distillation and Replay.
- **链接**: [arXiv:2306.17560](https://arxiv.org/abs/2306.17560) · 📚 被引 40
- **作者**: Quentin Jodelet, Xin Liu, Yin Jun Phua, Tsuyoshi Murata
- **🏷️ 机构**: Tokyo Institute of Technology,Department of Computer Science,Japan, AIST,Artificial Intelligence Research Center,Japan
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Class-incremental learning aims to learn new classes in an incremental fashion without forgetting the previously learned ones. Several research works have shown how additional data can be used by incremental models to help mitigate catastrophic forgetting. In this work, following the recent breakthrough in text-to-image generative models and their wide distribution, we propose the use of a pretrained Stable Diffusion model as a source of additional data for class-incremental learning. Compared to competitive methods that rely on external, often unlabeled, datasets of real images, our approach can generate synthetic samples belonging to the same classes as the previously encountered images. This allows us to use those additional data samples not only in the distillation loss but also for replay in the classification loss. Experiments on the competitive benchmarks CIFAR100, ImageNet-Subset, and ImageNet demonstrate how this new approach can be used to further improve the performance of state-of-the-art methods for class-incremental learning on large scale datasets.

</details>

### SATHUR: Self Augmenting Task Hallucinal Unified Representation for Generalized Class Incremental Learning.
- **链接**: [arXiv:2311.18630](https://arxiv.org/abs/2311.18630)
- **作者**: Sathursan Kanagarajah, Thanuja D. Ambegoda, Ranga Rodrigo
- **🏷️ 机构**: University of Moratuwa,Sri Lanka
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Class Incremental Learning (CIL) is inspired by the human ability to learn new classes without forgetting previous ones. CIL becomes more challenging in real-world scenarios when the samples in each incremental step are imbalanced. This creates another branch of problem, called Generalized Class Incremental Learning (GCIL) where each incremental step is structured more realistically. Grow When Required (GWR) network, a type of Self-Organizing Map (SOM), dynamically create and remove nodes and edges for adaptive learning. GWR performs incremental learning from feature vectors extracted by a Convolutional Neural Network (CNN), which acts as a feature extractor. The inherent ability of GWR to form distinct clusters, each corresponding to a class in the feature vector space, regardless of the order of samples or class imbalances, is well suited to achieving GCIL. To enhance GWR's classification performance, a high-quality feature extractor is required. However, when the convolutional layers are adapted at each incremental step, the GWR nodes corresponding to prior knowledge are subject to near-invalidation. This work introduces the Self Augmenting Task Hallucinal Unified Representation (SATHUR), which re-initializes the GWR network at each incremental step, aligning it with the current feature extractor. Comprehensive experimental results demonstrate that our proposed method significantly outperforms other state-of-the-art GCIL methods on CIFAR-100 and CORe50 datasets.

</details>

### Clustering-based Domain-Incremental Learning.
- **链接**: [arXiv:2309.12078](https://arxiv.org/abs/2309.12078)
- **作者**: Christiaan Lamers, René Vidal, Nabil Belbachir, Niki van Stein, Thomas Bäck, Paris Giampouras
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We consider the problem of learning multiple tasks in a continual learning setting in which data from different tasks is presented to the learner in a streaming fashion. A key challenge in this setting is the so-called "catastrophic forgetting problem", in which the performance of the learner in an "old task" decreases when subsequently trained on a "new task". Existing continual learning methods, such as Averaged Gradient Episodic Memory (A-GEM) and Orthogonal Gradient Descent (OGD), address catastrophic forgetting by minimizing the loss for the current task without increasing the loss for previous tasks. However, these methods assume the learner knows when the task changes, which is unrealistic in practice. In this paper, we alleviate the need to provide the algorithm with information about task changes by using an online clustering-based approach on a dynamically updated finite pool of samples or gradients. We thereby successfully counteract catastrophic forgetting in one of the hardest settings, namely: domain-incremental learning, a setting for which the problem was previously unsolved. We showcase the benefits of our approach by applying these ideas to projection-based methods, such as A-GEM and OGD, which lead to task-agnostic versions of them. Experiments on real datasets demonstrate the effectiveness of the proposed strategy and its promising performance compared to state-of-the-art methods.

</details>

### TKIL: Tangent Kernel Optimization for Class Balanced Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00379) · 📚 被引 12
- **作者**: Jinlin Xiang, Eli Shlizerman
- **🏷️ 机构**: University of Washington,Department of Electrical &#x0026; Computer Engineering,Seattle,USA, University of Washington,Department of Electrical &#x0026; Computer Engineering, Department of Applied Mathematics,Seattle,USA
- **会议**: ICCV 2023

### OpenIncrement: A Unified Framework for Open Set Recognition and Deep Class-Incremental Learning.
- **链接**: [arXiv:2310.03848](https://arxiv.org/abs/2310.03848) · 📚 被引 6
- **作者**: Jiawen Xu, Claas Grohnfeldt, Odej Kao
- **🏷️ 机构**: Technical University Berlin, Huawei Munich Research Center
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In most works on deep incremental learning research, it is assumed that novel samples are pre-identified for neural network retraining. However, practical deep classifiers often misidentify these samples, leading to erroneous predictions. Such misclassifications can degrade model performance. Techniques like open set recognition offer a means to detect these novel samples, representing a significant area in the machine learning domain. In this paper, we introduce a deep class-incremental learning framework integrated with open set recognition. Our approach refines class-incrementally learned features to adapt them for distance-based open set recognition. Experimental results validate that our method outperforms state-of-the-art incremental learning techniques and exhibits superior performance in open set recognition compared to baseline methods.

</details>

### A Model or 603 Exemplars: Towards Memory-Efficient Class-Incremental Learning.
- **链接**: [出版页](https://openreview.net/forum?id=S07feAlQHgM)
- **作者**: Da-Wei Zhou, Qi-Wei Wang, Han-Jia Ye, De-Chuan Zhan
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### On the Soft-Subnetwork for Few-Shot Class Incremental Learning.
- **链接**: [出版页](https://openreview.net/forum?id=z57WK5lGeHd)
- **作者**: Haeyong Kang, Jaehong Yoon, Sultan Rizky Hikmawan Madjid, Sung Ju Hwang, Chang D. Yoo
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Warping the Space: Weight Space Rotation for Class-Incremental Few-Shot Learning.
- **链接**: [出版页](https://openreview.net/forum?id=kPLzOfPfA2l)
- **作者**: Do-Yeon Kim, Dong-Jun Han, Jun Seo, Jaekyun Moon
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Progressive Voronoi Diagram Subdivision Enables Accurate Data-free Class-Incremental Learning.
- **链接**: [出版页](https://openreview.net/forum?id=zJXg_Wmob03)
- **作者**: Chunwei Ma, Zhanghexuan Ji, Ziyun Huang, Yan Shen, Mingchen Gao, Jinhui Xu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Incremental Learning of Structured Memory via Closed-Loop Transcription.
- **链接**: [出版页](https://openreview.net/forum?id=XrgjF5-M3xi)
- **作者**: Shengbang Tong, Xili Dai, Ziyang Wu, Mingyang Li, Brent Yi, Yi Ma
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### BEEF: Bi-Compatible Class-Incremental Learning via Energy-Based Expansion and Fusion.
- **链接**: [出版页](https://openreview.net/forum?id=iP77_axu0h3)
- **作者**: Fu-Yun Wang, Da-Wei Zhou, Liu Liu, Han-Jia Ye, Yatao Bian, De-Chuan Zhan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Neural Collapse Inspired Feature-Classifier Alignment for Few-Shot Class-Incremental Learning.
- **链接**: [出版页](https://openreview.net/forum?id=y5W8tpojhtJ)
- **作者**: Yibo Yang, Haobo Yuan, Xiangtai Li, Zhouchen Lin, Philip H. S. Torr, Dacheng Tao
- **🏷️ 机构**: Peking University
- **会议**: ICLR 2023

### BiRT: Bio-inspired Replay in Vision Transformers for Continual Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v202/jeeveswaran23a.html)
- **作者**: Kishaan Jeeveswaran, Prashant Shivaram Bhat, Bahram Zonooz, Elahe Arani
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### DualHSIC: HSIC-Bottleneck and Alignment for Continual Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v202/wang23ar.html)
- **作者**: Zifeng Wang, Zheng Zhan, Yifan Gong, Yucai Shao, Stratis Ioannidis, Yanzhi Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Prototype-Sample Relation Distillation: Towards Replay-Free Continual Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v202/asadi23a.html)
- **作者**: Nader Asadi, MohammadReza Davari, Sudhir P. Mudur, Rahaf Aljundi, Eugene Belilovsky
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Continual Learning in Linear Classification on Separable Data.
- **链接**: [出版页](https://proceedings.mlr.press/v202/evron23a.html)
- **作者**: Itay Evron, Edward Moroshko, Gon Buzaglo, Maroun Khriesh, Badea Marjieh, Nathan Srebro et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### DDGR: Continual Learning with Deep Diffusion-based Generative Replay.
- **链接**: [出版页](https://proceedings.mlr.press/v202/gao23e.html)
- **作者**: Rui Gao, Weiwei Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Poisoning Generative Replay in Continual Learning to Promote Forgetting.
- **链接**: [出版页](https://proceedings.mlr.press/v202/kang23c.html)
- **作者**: Siteng Kang, Zhan Shi, Xinhua Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Learnability and Algorithm for Continual Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v202/kim23x.html)
- **作者**: Gyuhak Kim, Changnan Xiao, Tatsuya Konishi, Bing Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Parameter-Level Soft-Masking for Continual Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v202/konishi23a.html)
- **作者**: Tatsuya Konishi, Mori Kurokawa, Chihiro Ono, Zixuan Ke, Gyuhak Kim, Bing Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Theory on Forgetting and Generalization of Continual Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v202/lin23f.html)
- **作者**: Sen Lin, Peizhong Ju, Yingbin Liang, Ness B. Shroff
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Neuro-Symbolic Continual Learning: Knowledge, Reasoning Shortcuts and Concept Rehearsal.
- **链接**: [出版页](https://proceedings.mlr.press/v202/marconato23a.html)
- **作者**: Emanuele Marconato, Gianpaolo Bontempo, Elisa Ficarra, Simone Calderara, Andrea Passerini, Stefano Teso
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Does Continual Learning Equally Forget All Parameters?
- **链接**: [出版页](https://proceedings.mlr.press/v202/zhao23n.html)
- **作者**: Haiyan Zhao, Tianyi Zhou, Guodong Long, Jing Jiang, Chengqi Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Understanding Incremental Learning of Gradient Descent: A Fine-grained Analysis of Matrix Sensing.
- **链接**: [出版页](https://proceedings.mlr.press/v202/jin23a.html)
- **作者**: Jikai Jin, Zhiyuan Li, Kaifeng Lyu, Simon Shaolei Du, Jason D. Lee
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Towards Robust Graph Incremental Learning on Evolving Graphs.
- **链接**: [出版页](https://proceedings.mlr.press/v202/su23a.html)
- **作者**: Junwei Su, Difan Zou, Zijun Zhang, Chuan Wu
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Optimizing Mode Connectivity for Class Incremental Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v202/wen23b.html)
- **作者**: Haitao Wen, Haoyang Cheng, Heqian Qiu, Lanxiao Wang, Lili Pan, Hongliang Li
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Fairness Continual Learning Approach to Semantic Scene Understanding in Open-World Environments.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/ce3cf998b7f59271e80ce03fb74a7115-Abstract-Conference.html)
- **作者**: Thanh-Dat Truong, Hoang-Quan Nguyen, Bhiksha Raj, Khoa Luu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Augmented Memory Replay-based Continual Learning Approaches for Network Intrusion Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/3755a02b1035fbadd5f93a022170e46f-Abstract-Conference.html)
- **作者**: Suresh Kumar Amalapuram, Sumohana S. Channappayya, Bheemarjuna Reddy Tamma
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### FeCAM: Exploiting the Heterogeneity of Class Distributions in Exemplar-Free Continual Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/15294ba2dcfb4521274f7aa1c26f4dd4-Abstract-Conference.html)
- **作者**: Dipam Goswami, Yuyang Liu, Bartlomiej Twardowski, Joost van de Weijer
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Bilevel Coreset Selection in Continual Learning: A New Formulation and Algorithm.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/a0251e494a7e75d59e06d37e646f46b7-Abstract-Conference.html)
- **作者**: Jie Hao, Kaiyi Ji, Mingrui Liu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### NPCL: Neural Processes for Uncertainty-Aware Continual Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/6c4a1a3cbe70ef36d7d6332166bba77d-Abstract-Conference.html)
- **作者**: Saurav Jha, Dong Gong, He Zhao, Lina Yao
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### CLeAR: Continual Learning on Algorithmic Reasoning for Human-like Intelligence.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/986e0caad271b59417287737416d8594-Abstract-Conference.html)
- **作者**: Bong Gyun Kang, HyunGi Kim, Dahuin Jung, Sungroh Yoon
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Recasting Continual Learning as Sequence Modeling.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/dee254cdacbab59f17dc6a8fbdffa59f-Abstract-Conference.html)
- **作者**: Soochan Lee, Jaehyeon Son, Gunhee Kim
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Loss Decoupling for Task-Agnostic Continual Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/249f73e01f0a2bb6c8d971b565f159a7-Abstract-Conference.html)
- **作者**: Yan-Shuo Liang, Wu-Jun Li
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Does Continual Learning Meet Compositionality? New Benchmarks and An Evaluation Framework.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/6a42b45af2b72e6e5b5e3a6fe695809f-Abstract-Datasets_and_Benchmarks.html)
- **作者**: Weiduo Liao, Ying Wei, Mingchen Jiang, Qingfu Zhang, Hisao Ishibuchi
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Overcoming Recency Bias of Normalization Statistics in Continual Learning: Balance and Adaptation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/50ca96a1a9ebe0b5e5688a504feb6107-Abstract-Conference.html)
- **作者**: Yilin Lyu, Liyuan Wang, Xingxing Zhang, Zicheng Sun, Hang Su, Jun Zhu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

## 跨领域论文（完整笔记在其他领域）

- Continual Detection Transformer for Incremental Object Detection. → [object-detection](../object-detection/Guideline%202023.md)
- Preventing Zero-Shot Transfer Degradation in Continual Learning of Vision-Language Models. → [vlm](../vlm/Guideline%202023.md)

<!-- COMPLETE v1 papers=118 -->
