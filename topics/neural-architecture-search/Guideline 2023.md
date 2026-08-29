# Neural Architecture Search — 2023 Guideline

> 领域: 神经架构搜索（NAS、Zero-Cost、搜索空间）
> 论文数: 5 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### MDL-NAS: A Joint Multi-domain Learning Framework for Vision Transformer.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01924) · 📚 被引 16
- **作者**: Shiguang Wang, Tao Xie, Jian Cheng, Xingcheng Zhang, Haijun Liu
- **🏷️ 机构**: University of Electronic Science and Technology of China, Harbin Institute of Technology, SenseTime Research
- **会议**: CVPR 2023

### DisWOT: Student Architecture Search for Distillation WithOut Training.
- **链接**: [arXiv:2303.15678](https://arxiv.org/abs/2303.15678) · 📚 被引 60
- **作者**: Peijie Dong, Lujun Li, Zimian Wei
- **🏷️ 机构**: National University of Defense Technology, Chinese Academy of Sciences
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Knowledge distillation (KD) is an effective training strategy to improve the lightweight student models under the guidance of cumbersome teachers. However, the large architecture difference across the teacher-student pairs limits the distillation gains. In contrast to previous adaptive distillation methods to reduce the teacher-student gap, we explore a novel training-free framework to search for the best student architectures for a given teacher. Our work first empirically show that the optimal model under vanilla training cannot be the winner in distillation. Secondly, we find that the similarity of feature semantics and sample relations between random-initialized teacher-student networks have good correlations with final distillation performances. Thus, we efficiently measure similarity matrixs conditioned on the semantic activation maps to select the optimal student via an evolutionary algorithm without any training. In this way, our student architecture search for Distillation WithOut Training (DisWOT) significantly improves the performance of the model in the distillation stage with at least 180$\times$ training acceleration. Additionally, we extend similarity metrics in DisWOT as new distillers and KD-based zero-proxies. Our experiments on CIFAR, ImageNet and NAS-Bench-201 demonstrate that our technique achieves state-of-the-art results on different search spaces. Our project and code are available at https://lilujunai.github.io/DisWOT-CVPR2023/.

</details>

### Adversarially Robust Neural Architecture Search for Graph Neural Networks.
- **链接**: [arXiv:2304.04168](https://arxiv.org/abs/2304.04168) · 📚 被引 21
- **作者**: Beini Xie, Heng Chang, Ziwei Zhang, Xin Wang, Daixin Wang, Zhiqiang Zhang et al.
- **🏷️ 机构**: Tsinghua University, Ant Group, Yale University
- **会议**: CVPR 2023

### Evolutionary Neural Architecture Search for Transformer in Knowledge Tracing.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/3e53d82a1113e3d240059a9195668edc-Abstract-Conference.html) · 📚 被引 6
- **作者**: Shangshang Yang, Xiaoshan Yu, Ye Tian, Xueming Yan, Haiping Ma, Xingyi Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

> Neural Architecture Search (NAS) has shown promising performance in the automatic design of vision transformers (ViT) exceeding 1G FLOPs. However, designing lightweight and low-latency ViT models for diverse mobile devices remains a big challenge. In this work, we propose ElasticViT, a two-stage NAS approach that trains a high-quality ViT supernet over a very large search space that supports a wide range of mobile devices, and then searches an optimal sub-network (subnet) for direct deployment. However, prior supernet training methods that rely on uniform sampling suffer from the gradient conflict issue: the sampled subnets can have vastly different model sizes (e.g., 50M vs. 2G FLOPs), leading to different optimization directions and inferior performance. To address this challenge, we propose two novel sampling techniques: complexity-aware sampling and performance-aware sampling. Complexity-aware sampling limits the FLOPs difference among the subnets sampled across adjacent training steps, while covering different-sized subnets in the search space. Performance-aware sampling further selects subnets that have good accuracy, which can reduce gradient conflicts and improve supernet quality. Our discovered models, ElasticViT models, achieve top-1 accuracy from 67.2% to 80.0% on ImageNet from 60M to 800M FLOPs without extra retraining, outperforming all prior CNNs and ViTs in terms of accuracy and latency. Our tiny and small models are also the first ViT models that surpass state-of-the-art CNNs with significantly lower latency on mobile devices. For instance, ElasticViT-S1 runs 2.62x faster than EfficientNet-B0 with 0.1% higher accuracy.

</details>

### HOTNAS: Hierarchical Optimal Transport for Neural Architecture Search.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01154) · 📚 被引 15
- **作者**: Jiechao Yang, Yong Liu, Hongteng Xu
- **🏷️ 机构**: Gaoling School of Artificial Intelligence, Renmin University of China,Beijing,China
- **会议**: CVPR 2023

### Differentiable Architecture Search with Random Features.
- **链接**: [arXiv:2208.08835](https://arxiv.org/abs/2208.08835) · 📚 被引 19
- **作者**: Xuanyang Zhang, Yonggang Li, Xiangyu Zhang, Yongtao Wang, Jian Sun
- **🏷️ 机构**: MEGVII Technology, Peking University
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Blending multiple convolutional kernels is proved advantageous in neural architecture design. However, current two-stage neural architecture search methods are mainly limited to single-path search spaces. How to efficiently search models of multi-path structures remains a difficult problem. In this paper, we are motivated to train a one-shot multi-path supernet to accurately evaluate the candidate architectures. Specifically, we discover that in the studied search spaces, feature vectors summed from multiple paths are nearly multiples of those from a single path. Such disparity perturbs the supernet training and its ranking ability. Therefore, we propose a novel mechanism called Shadow Batch Normalization (SBN) to regularize the disparate feature statistics. Extensive experiments prove that SBNs are capable of stabilizing the optimization and improving ranking performance. We call our unified multi-path one-shot approach as MixPath, which generates a series of models that achieve state-of-the-art results on ImageNet.

</details>

### Extensible and Efficient Proxy for Neural Architecture Search.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00570) · 📚 被引 11
- **作者**: Yuhong Li, Jiajie Li, Cong Hao, Pan Li, Jinjun Xiong, Deming Chen
- **🏷️ 机构**: University of Illinois at Urbana-Champaign, University at Buffalo, Georgia Institute of Technology
- **会议**: ICCV 2023

### An Experimental Protocol for Neural Architecture Search in Super-Resolution.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00447) · 📚 被引 2
- **作者**: Jesús Leopoldo Llano García, Raúl Monroy, Víctor Adrián Sosa-Hernández
- **🏷️ 机构**: School of Engineering and Sciences,Tecnologico de Monterrey,Mexico,52926
- **会议**: ICCV 2023

### DONNAv2 - Lightweight Neural Architecture Search for Vision tasks.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00149) · 📚 被引 3
- **作者**: Sweta Priyadarshi, Tianyu Jiang, Hsin-Pai Cheng, Sendil Krishna, Viswanath Ganapathy, Chirag Patel
- **🏷️ 机构**: Qualcomm AI Research,San Diego,CA,USA,92121
- **会议**: ICCV 2023

### InstaTune: Instantaneous Neural Architecture Search During Fine-Tuning.
- **链接**: [arXiv:2308.15609](https://arxiv.org/abs/2308.15609) · 📚 被引 3
- **作者**: Sharath Nittur Sridhar, Souvik Kundu, Sairam Sundaresan, Maciej Szankin, Anthony Sarah
- **🏷️ 机构**: Intel Labs,San Diego,USA
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> One-Shot Neural Architecture Search (NAS) algorithms often rely on training a hardware agnostic super-network for a domain specific task. Optimal sub-networks are then extracted from the trained super-network for different hardware platforms. However, training super-networks from scratch can be extremely time consuming and compute intensive especially for large models that rely on a two-stage training process of pre-training and fine-tuning. State of the art pre-trained models are available for a wide range of tasks, but their large sizes significantly limits their applicability on various hardware platforms. We propose InstaTune, a method that leverages off-the-shelf pre-trained weights for large models and generates a super-network during the fine-tuning stage. InstaTune has multiple benefits. Firstly, since the process happens during fine-tuning, it minimizes the overall time and compute resources required for NAS. Secondly, the sub-networks extracted are optimized for the target task, unlike prior work that optimizes on the pre-training objective. Finally, InstaTune is easy to "plug and play" in existing frameworks. By using multi-objective evolutionary search algorithms along with lightly trained predictors, we find Pareto-optimal sub-networks that outperform their respective baselines across different performance objectives such as accuracy and MACs. Specifically, we demonstrate that our approach performs well across both unimodal (ViT and BERT) and multi-modal (BEiT-3) transformer based architectures.

</details>

### Multi-task Graph Neural Architecture Search with Task-aware Collaboration and Curriculum.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/4e839c9c398c58c878a394633b806ccd-Abstract-Conference.html) · 📚 被引 3
- **作者**: Yijian Qin, Xin Wang, Ziwei Zhang, Hong Chen, Wenwu Zhu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Construction of Hierarchical Neural Architecture Search Spaces based on Context-free Grammars.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/4869f3f967dfe954439408dd92c50ee1-Abstract-Conference.html) · 📚 被引 2
- **作者**: Simon Schrodi, Danny Stoll, Binxin Ru, Rhea Sanjay Sukthanker, Thomas Brox, Frank Hutter
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Evolutionary Neural Architecture Search for Transformer in Knowledge Tracing.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/3e53d82a1113e3d240059a9195668edc-Abstract-Conference.html) · 📚 被引 6
- **作者**: Shangshang Yang, Xiaoshan Yu, Ye Tian, Xueming Yan, Haiping Ma, Xingyi Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

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
