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
