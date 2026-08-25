# Neural Architecture Search — 2024 Guideline

> 领域: 神经架构搜索（NAS、Zero-Cost、搜索空间）
> 论文数: 5 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Boosting Order-Preserving and Transferability for Neural Architecture Search: A Joint Architecture Refined Search and Fine-Tuning Approach.
- **链接**: [arXiv:2403.11380](https://arxiv.org/abs/2403.11380)
- **作者**: Beichen Zhang, Xiaoxing Wang, Xiaohan Qin, Junchi Yan
- **🏷️ 机构**: Shanghai Jiao Tong University,Department of Computer Science and Engineering &#x0026; MoE Key Lab of AI
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Supernet is a core component in many recent Neural Architecture Search (NAS) methods. It not only helps embody the search space but also provides a (relative) estimation of the final performance of candidate architectures. Thus, it is critical that the top architectures ranked by a supernet should be consistent with those ranked by true performance, which is known as the order-preserving ability. In this work, we analyze the order-preserving ability on the whole search space (global) and a sub-space of top architectures (local), and empirically show that the local order-preserving for current two-stage NAS methods still need to be improved. To rectify this, we propose a novel concept of Supernet Shifting, a refined search strategy combining architecture searching with supernet fine-tuning. Specifically, apart from evaluating, the training loss is also accumulated in searching and the supernet is updated every iteration. Since superior architectures are sampled more frequently in evolutionary searching, the supernet is encouraged to focus on top architectures, thus improving local order-preserving. Besides, a pre-trained supernet is often un-reusable for one-shot methods. We show that Supernet Shifting can fulfill transferring supernet to a new dataset. Specifically, the last classifier layer will be unset and trained through evolutionary searching. Comprehensive experiments show that our method has better order-preserving ability and can find a dominating architecture. Moreover, the pre-trained supernet can be easily transferred into a new dataset with no loss of performance.

### Towards Accurate and Robust Architectures via Neural Architecture Search.
- **链接**: [arXiv:2405.05502](https://arxiv.org/abs/2405.05502)
- **作者**: Yuwei Ou, Yuqi Feng, Yanan Sun
- **🏷️ 机构**: College of Computer Science, Sichuan University
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > To defend deep neural networks from adversarial attacks, adversarial training has been drawing increasing attention for its effectiveness. However, the accuracy and robustness resulting from the adversarial training are limited by the architecture, because adversarial training improves accuracy and robustness by adjusting the weight connection affiliated to the architecture. In this work, we propose ARNAS to search for accurate and robust architectures for adversarial training. First we design an accurate and robust search space, in which the placement of the cells and the proportional relationship of the filter numbers are carefully determined. With the design, the architectures can obtain both accuracy and robustness by deploying accurate and robust structures to their sensitive positions, respectively. Then we propose a differentiable multi-objective search strategy, performing gradient descent towards directions that are beneficial for both natural loss and adversarial loss, thus the accuracy and robustness can be guaranteed at the same time. We conduct comprehensive experiments in terms of white-box attacks, black-box attacks, and transferability. Experimental results show that the searched architecture has the strongest robustness with the competitive accuracy, and breaks the traditional idea that NAS-based architectures cannot transfer well to complex tasks in robustness scenarios. By analyzing outstanding architectures searched, we also conclude that accurate and robust neural architectures tend to deploy different structures near the input and output, which has great practical significance on both hand-crafting and automatically designing of accurate and robust architectures.

### Insights from the Use of Previously Unseen Neural Architecture Search Datasets.
- **链接**: [arXiv:2404.02189](https://arxiv.org/abs/2404.02189)
- **作者**: Rob Geada, David Towers, Matthew Forshaw, Amir Atapour-Abarghouei, A. Stephen McGough
- **🏷️ 机构**: Newcastle University,UK-, Durham University,UK-
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > The boundless possibility of neural networks which can be used to solve a problem -- each with different performance -- leads to a situation where a Deep Learning expert is required to identify the best neural network. This goes against the hope of removing the need for experts. Neural Architecture Search (NAS) offers a solution to this by automatically identifying the best architecture. However, to date, NAS work has focused on a small set of datasets which we argue are not representative of real-world problems. We introduce eight new datasets created for a series of NAS Challenges: AddNIST, Language, MultNIST, CIFARTile, Gutenberg, Isabella, GeoClassing, and Chesseract. These datasets and challenges are developed to direct attention to issues in NAS development and to encourage authors to consider how their models will perform on datasets unknown to them at development time. We present experimentation using standard Deep Learning methods as well as the best results from challenge participants.

### AZ-NAS: Assembling Zero-Cost Proxies for Network Architecture Search.
- **链接**: [arXiv:2403.19232](https://arxiv.org/abs/2403.19232)
- **作者**: Junghyup Lee, Bumsub Ham
- **🏷️ 机构**: Yonsei University
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Training-free network architecture search (NAS) aims to discover high-performing networks with zero-cost proxies, capturing network characteristics related to the final performance. However, network rankings estimated by previous training-free NAS methods have shown weak correlations with the performance. To address this issue, we propose AZ-NAS, a novel approach that leverages the ensemble of various zero-cost proxies to enhance the correlation between a predicted ranking of networks and the ground truth substantially in terms of the performance. To achieve this, we introduce four novel zero-cost proxies that are complementary to each other, analyzing distinct traits of architectures in the views of expressivity, progressivity, trainability, and complexity. The proxy scores can be obtained simultaneously within a single forward and backward pass, making an overall NAS process highly efficient. In order to integrate the rankings predicted by our proxies effectively, we introduce a non-linear ranking aggregation method that highlights the networks highly-ranked consistently across all the proxies. Experimental results conclusively demonstrate the efficacy and efficiency of AZ-NAS, outperforming state-of-the-art methods on standard benchmarks, all while maintaining a reasonable runtime cost.

### SNED: Superposition Network Architecture Search for Efficient Video Diffusion Model.
- **链接**: [arXiv:2406.00195](https://arxiv.org/abs/2406.00195)
- **作者**: Zhengang Li, Yan Kang, Yuchen Liu, Difan Liu, Tobias Hinz, Feng Liu et al.
- **🏷️ 机构**: Northeastern University, Adobe Research, Adobe
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > While AI-generated content has garnered significant attention, achieving photo-realistic video synthesis remains a formidable challenge. Despite the promising advances in diffusion models for video generation quality, the complex model architecture and substantial computational demands for both training and inference create a significant gap between these models and real-world applications. This paper presents SNED, a superposition network architecture search method for efficient video diffusion model. Our method employs a supernet training paradigm that targets various model cost and resolution options using a weight-sharing method. Moreover, we propose the supernet training sampling warm-up for fast training optimization. To showcase the flexibility of our method, we conduct experiments involving both pixel-space and latent-space video diffusion models. The results demonstrate that our framework consistently produces comparable results across different model options with high efficiency. According to the experiment for the pixel-space video diffusion model, we can achieve consistent video generation results simultaneously across 64 x 64 to 256 x 256 resolutions with a large range of model sizes from 640M to 1.6B number of parameters for pixel-space video diffusion models.
