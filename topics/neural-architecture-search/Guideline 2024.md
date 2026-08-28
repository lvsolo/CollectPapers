# Neural Architecture Search — 2024 Guideline

> 领域: 神经架构搜索（NAS、Zero-Cost、搜索空间）
> 论文数: 3 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### HyTAS: A Hyperspectral Image Transformer Architecture Search Benchmark and Analysis.
- **链接**: [arXiv:2407.16269](https://arxiv.org/abs/2407.16269) · 📚 被引 3
- **作者**: Fangqin Zhou, Mert Kilickaya, Joaquin Vanschoren, Ran Piao
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Supernet is a core component in many recent Neural Architecture Search (NAS) methods. It not only helps embody the search space but also provides a (relative) estimation of the final performance of candidate architectures. Thus, it is critical that the top architectures ranked by a supernet should be consistent with those ranked by true performance, which is known as the order-preserving ability. In this work, we analyze the order-preserving ability on the whole search space (global) and a sub-space of top architectures (local), and empirically show that the local order-preserving for current two-stage NAS methods still need to be improved. To rectify this, we propose a novel concept of Supernet Shifting, a refined search strategy combining architecture searching with supernet fine-tuning. Specifically, apart from evaluating, the training loss is also accumulated in searching and the supernet is updated every iteration. Since superior architectures are sampled more frequently in evolutionary searching, the supernet is encouraged to focus on top architectures, thus improving local order-preserving. Besides, a pre-trained supernet is often un-reusable for one-shot methods. We show that Supernet Shifting can fulfill transferring supernet to a new dataset. Specifically, the last classifier layer will be unset and trained through evolutionary searching. Comprehensive experiments show that our method has better order-preserving ability and can find a dominating architecture. Moreover, the pre-trained supernet can be easily transferred into a new dataset with no loss of performance.

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> To defend deep neural networks from adversarial attacks, adversarial training has been drawing increasing attention for its effectiveness. However, the accuracy and robustness resulting from the adversarial training are limited by the architecture, because adversarial training improves accuracy and robustness by adjusting the weight connection affiliated to the architecture. In this work, we propose ARNAS to search for accurate and robust architectures for adversarial training. First we design an accurate and robust search space, in which the placement of the cells and the proportional relationship of the filter numbers are carefully determined. With the design, the architectures can obtain both accuracy and robustness by deploying accurate and robust structures to their sensitive positions, respectively. Then we propose a differentiable multi-objective search strategy, performing gradient descent towards directions that are beneficial for both natural loss and adversarial loss, thus the accuracy and robustness can be guaranteed at the same time. We conduct comprehensive experiments in terms of white-box attacks, black-box attacks, and transferability. Experimental results show that the searched architecture has the strongest robustness with the competitive accuracy, and breaks the traditional idea that NAS-based architectures cannot transfer well to complex tasks in robustness scenarios. By analyzing outstanding architectures searched, we also conclude that accurate and robust neural architectures tend to deploy different structures near the input and output, which has great practical significance on both hand-crafting and automatically designing of accurate and robust architectures.

</details>

### Insights from the Use of Previously Unseen Neural Architecture Search Datasets. **⭐⭐** (相关度: 20%)
- **链接**: [arXiv:2404.02189](https://arxiv.org/abs/2404.02189)
- **作者**: Rob Geada, David Towers, Matthew Forshaw, Amir Atapour-Abarghouei, A. Stephen McGough
- **🏷️ 机构**: Newcastle University,UK-, Durham University,UK-
- **会议**: CVPR 2024
- **摘要（中）**: ①针对NAS研究过度依赖少数标准数据集，缺乏对真实世界问题的代表性。②引入八个新数据集（如AddNIST、Language等）用于NAS挑战，并报告标准深度学习方法和挑战参与者的最佳结果。③相比现有工作，这些数据集覆盖多样任务，鼓励开发者在未知数据集上评估模型泛化能力。④实验表明这些数据集能有效暴露NAS方法的不足，推动更鲁棒的方法发展。
- **摘要（英）**: This paper addresses the lack of diverse benchmarks in NAS research by introducing eight new datasets for NAS challenges, covering various tasks. It presents baseline results from standard deep learning methods and challenge participants, highlighting the need for models that generalize to unseen datasets. The datasets aim to steer NAS development toward more robust and practical solutions.
- **核心贡献**: 引入八个新NAS数据集，促进模型泛化能力评估。
- **创新点**: 设计多样化的挑战数据集，模拟真实世界问题。
- **结果**: 通过挑战赛揭示了现有NAS方法的局限性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The boundless possibility of neural networks which can be used to solve a problem -- each with different performance -- leads to a situation where a Deep Learning expert is required to identify the best neural network. This goes against the hope of removing the need for experts. Neural Architecture Search (NAS) offers a solution to this by automatically identifying the best architecture. However, to date, NAS work has focused on a small set of datasets which we argue are not representative of real-world problems. We introduce eight new datasets created for a series of NAS Challenges: AddNIST, Language, MultNIST, CIFARTile, Gutenberg, Isabella, GeoClassing, and Chesseract. These datasets and challenges are developed to direct attention to issues in NAS development and to encourage authors to consider how their models will perform on datasets unknown to them at development time. We present experimentation using standard Deep Learning methods as well as the best results from challenge participants.

</details>

### AZ-NAS: Assembling Zero-Cost Proxies for Network Architecture Search. **⭐⭐⭐** (相关度: 25%)
- **链接**: [arXiv:2403.19232](https://arxiv.org/abs/2403.19232) · 📚 被引 33
- **作者**: Junghyup Lee, Bumsub Ham
- **🏷️ 机构**: Yonsei University
- **会议**: CVPR 2024
- **摘要（中）**: ①针对训练-free NAS方法中零成本代理与最终性能相关性弱的问题。②提出AZ-NAS方法，集成多个零成本代理（表达性、进展性、可训练性、复杂性），通过非线性排序聚合方法提升排序相关性。③相比单一代理，多代理互补分析架构特征，且可在单次前向反向传播中同时获取。④实验表明AZ-NAS在多个搜索空间上显著提升了排序相关性和搜索效率。
- **摘要（英）**: This paper addresses the weak correlation between zero-cost proxies and final performance in training-free NAS. It proposes AZ-NAS, which ensembles four novel complementary proxies and uses a non-linear ranking aggregation method to improve ranking accuracy. Experiments show significant improvements in correlation and efficiency across multiple search spaces.
- **核心贡献**: 提出AZ-NAS，通过集成零成本代理提升NAS排序相关性。
- **创新点**: 设计四个互补代理并采用非线性聚合方法。
- **结果**: 在多个搜索空间上显著提升了排序相关性和搜索效率。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Training-free network architecture search (NAS) aims to discover high-performing networks with zero-cost proxies, capturing network characteristics related to the final performance. However, network rankings estimated by previous training-free NAS methods have shown weak correlations with the performance. To address this issue, we propose AZ-NAS, a novel approach that leverages the ensemble of various zero-cost proxies to enhance the correlation between a predicted ranking of networks and the ground truth substantially in terms of the performance. To achieve this, we introduce four novel zero-cost proxies that are complementary to each other, analyzing distinct traits of architectures in the views of expressivity, progressivity, trainability, and complexity. The proxy scores can be obtained simultaneously within a single forward and backward pass, making an overall NAS process highly efficient. In order to integrate the rankings predicted by our proxies effectively, we introduce a non-linear ranking aggregation method that highlights the networks highly-ranked consistently across all the proxies. Experimental results conclusively demonstrate the efficacy and efficiency of AZ-NAS, outperforming state-of-the-art methods on standard benchmarks, all while maintaining a reasonable runtime cost.

</details>

### SNED: Superposition Network Architecture Search for Efficient Video Diffusion Model. **⭐⭐** (相关度: 15%)
- **链接**: [arXiv:2406.00195](https://arxiv.org/abs/2406.00195)
- **作者**: Zhengang Li, Yan Kang, Yuchen Liu, Difan Liu, Tobias Hinz, Feng Liu et al.
- **🏷️ 机构**: Northeastern University, Adobe Research, Adobe
- **会议**: CVPR 2024
- **摘要（中）**: ①针对视频扩散模型架构复杂、计算需求高，难以应用于实际的问题。②提出SNED方法，采用超级网络训练范式，支持多种模型成本和分辨率选项，并引入训练采样预热优化。③相比现有视频扩散模型，通过权重共享实现高效架构搜索，适用于像素空间和潜空间模型。④实验表明SNED在不同分辨率和模型选项下均能生成一致的高质量视频，同时保持高效率。
- **摘要（英）**: This paper addresses the high computational cost of video diffusion models by proposing SNED, a superposition network architecture search method. It uses a supernet training paradigm with weight sharing and a sampling warm-up strategy to efficiently search across resolutions and model costs. Experiments demonstrate consistent video generation quality across 64x64 to 256x256 resolutions with high efficiency.
- **核心贡献**: 提出SNED方法，实现高效视频扩散模型的架构搜索。
- **创新点**: 采用超级网络和权重共享支持多分辨率视频生成。
- **结果**: 在多种分辨率下生成一致视频，显著提升效率。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While AI-generated content has garnered significant attention, achieving photo-realistic video synthesis remains a formidable challenge. Despite the promising advances in diffusion models for video generation quality, the complex model architecture and substantial computational demands for both training and inference create a significant gap between these models and real-world applications. This paper presents SNED, a superposition network architecture search method for efficient video diffusion model. Our method employs a supernet training paradigm that targets various model cost and resolution options using a weight-sharing method. Moreover, we propose the supernet training sampling warm-up for fast training optimization. To showcase the flexibility of our method, we conduct experiments involving both pixel-space and latent-space video diffusion models. The results demonstrate that our framework consistently produces comparable results across different model options with high efficiency. According to the experiment for the pixel-space video diffusion model, we can achieve consistent video generation results simultaneously across 64 x 64 to 256 x 256 resolutions with a large range of model sizes from 640M to 1.6B number of parameters for pixel-space video diffusion models.

</details>
