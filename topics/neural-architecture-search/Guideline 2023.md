# Neural Architecture Search — 2023 Guideline

> 领域: 神经架构搜索（NAS、Zero-Cost、搜索空间）
> 论文数: 7 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### ElasticViT: Conflict-aware Supernet Training for Deploying Fast Vision Transformer on Diverse Mobile Devices.
- **链接**: [arXiv:2303.09730](https://arxiv.org/abs/2303.09730) · 📚 被引 18
- **作者**: Chen Tang, Li Lyna Zhang, Huiqiang Jiang, Jiahang Xu, Ting Cao, Quanlu Zhang et al.
- **🏷️ 机构**: Tsinghua University, Microsoft Research
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural Architecture Search (NAS) has shown promising performance in the automatic design of vision transformers (ViT) exceeding 1G FLOPs. However, designing lightweight and low-latency ViT models for diverse mobile devices remains a big challenge. In this work, we propose ElasticViT, a two-stage NAS approach that trains a high-quality ViT supernet over a very large search space that supports a wide range of mobile devices, and then searches an optimal sub-network (subnet) for direct deployment. However, prior supernet training methods that rely on uniform sampling suffer from the gradient conflict issue: the sampled subnets can have vastly different model sizes (e.g., 50M vs. 2G FLOPs), leading to different optimization directions and inferior performance. To address this challenge, we propose two novel sampling techniques: complexity-aware sampling and performance-aware sampling. Complexity-aware sampling limits the FLOPs difference among the subnets sampled across adjacent training steps, while covering different-sized subnets in the search space. Performance-aware sampling further selects subnets that have good accuracy, which can reduce gradient conflicts and improve supernet quality. Our discovered models, ElasticViT models, achieve top-1 accuracy from 67.2% to 80.0% on ImageNet from 60M to 800M FLOPs without extra retraining, outperforming all prior CNNs and ViTs in terms of accuracy and latency. Our tiny and small models are also the first ViT models that surpass state-of-the-art CNNs with significantly lower latency on mobile devices. For instance, ElasticViT-S1 runs 2.62x faster than EfficientNet-B0 with 0.1% higher accuracy.

</details>

### Enhancing Differentiable Architecture Search: A Study on Small Number of Cell Blocks in the Search Stage, and Important Branches-based Cells Selection.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00135) · 📚 被引 0
- **作者**: Bedionita Soro, Chong Song
- **🏷️ 机构**: KAIST AI,South Korea
- **会议**: ICCV 2023

### MixPath: A Unified Approach for One-shot Neural Architecture Search.
- **链接**: [arXiv:2001.05887](https://arxiv.org/abs/2001.05887) · 📚 被引 15
- **作者**: Xiangxiang Chu, Shun Lu, Xudong Li, Bo Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

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
