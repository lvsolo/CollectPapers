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

> Hyperspectral Imaging (HSI) plays an increasingly critical role in precise vision tasks within remote sensing, capturing a wide spectrum of visual data. Transformer architectures have significantly enhanced HSI task performance, while advancements in Transformer Architecture Search (TAS) have improved model discovery. To harness these advancements for HSI classification, we make the following contributions: i) We propose HyTAS, the first benchmark on transformer architecture search for Hyperspectral imaging, ii) We comprehensively evaluate 12 different methods to identify the optimal transformer over 5 different datasets, iii) We perform an extensive factor analysis on the Hyperspectral transformer search performance, greatly motivating future research in this direction. All benchmark materials are available at HyTAS.

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

### Auto-GAS: Automated Proxy Discovery for Training-Free Generative Architecture Search.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72652-1_3) · 📚 被引 14
- **作者**: Lujun Li, Haosen Sun, Shiwen Li, Peijie Dong, Wenhan Luo, Wei Xue et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Auto-DAS: Automated Proxy Discovery for Training-Free Distillation-Aware Architecture Search.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72652-1_4) · 📚 被引 5
- **作者**: Haosen Sun, Lujun Li, Peijie Dong, Zimian Wei, Shitong Shao
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The boundless possibility of neural networks which can be used to solve a problem -- each with different performance -- leads to a situation where a Deep Learning expert is required to identify the best neural network. This goes against the hope of removing the need for experts. Neural Architecture Search (NAS) offers a solution to this by automatically identifying the best architecture. However, to date, NAS work has focused on a small set of datasets which we argue are not representative of real-world problems. We introduce eight new datasets created for a series of NAS Challenges: AddNIST, Language, MultNIST, CIFARTile, Gutenberg, Isabella, GeoClassing, and Chesseract. These datasets and challenges are developed to direct attention to issues in NAS development and to encourage authors to consider how their models will perform on datasets unknown to them at development time. We present experimentation using standard Deep Learning methods as well as the best results from challenge participants.

</details>

</details>

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
