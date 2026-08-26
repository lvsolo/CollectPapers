# Neural Architecture Search — 2025 Guideline

> 领域: 神经架构搜索（NAS、Zero-Cost、搜索空间）
> 论文数: 3 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### L-SWAG: Layer-Sample Wise Activation with Gradients Information for Zero-Shot NAS on Vision Transformers.
- **链接**: [arXiv:2505.07300](https://arxiv.org/abs/2505.07300) · 📚 被引 2
- **作者**: Sofia Casarin, Sergio Escalera, Oswald Lanz
- **🏷️ 机构**: Free University of Bozen-Bolzano,Bolzano,Italy, Computer Vision Center,Barcelona,Spain
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > Training-free Neural Architecture Search (NAS) efficiently identifies high-performing neural networks using zero-cost (ZC) proxies. Unlike multi-shot and one-shot NAS approaches, ZC-NAS is both (i) time-efficient, eliminating the need for model training, and (ii) interpretable, with proxy designs often theoretically grounded. Despite rapid developments in the field, current SOTA ZC proxies are typically constrained to well-established convolutional search spaces. With the rise of Large Language Models shaping the future of deep learning, this work extends ZC proxy applicability to Vision Transformers (ViTs). We present a new benchmark using the Autoformer search space evaluated on 6 distinct tasks and propose Layer-Sample Wise Activation with Gradients information (L-SWAG), a novel, generalizable metric that characterizes both convolutional and transformer architectures across 14 tasks. Additionally, previous works highlighted how different proxies contain complementary information, motivating the need for a ML model to identify useful combinations. To further enhance ZC-NAS, we therefore introduce LIBRA-NAS (Low Information gain and Bias Re-Alignment), a method that strategically combines proxies to best represent a specific benchmark. Integrated into the NAS search, LIBRA-NAS outperforms evolution and gradient-based NAS techniques by identifying an architecture with a 17.0% test error on ImageNet1k in just 0.1 GPU days.

### Subnet-Aware Dynamic Supernet Training for Neural Architecture Search.
- **链接**: [arXiv:2503.10740](https://arxiv.org/abs/2503.10740) · 📚 被引 6
- **作者**: Jeimin Jeon, Youngmin Oh, Junghyup Lee, Donghyeon Baek, Dohyung Kim, Chanho Eom et al.
- **🏷️ 机构**: Yonsei University, Samsung Research, Samsung Advanced Institute of Technology
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > N-shot neural architecture search (NAS) exploits a supernet containing all candidate subnets for a given search space. The subnets are typically trained with a static training strategy (e.g., using the same learning rate (LR) scheduler and optimizer for all subnets). This, however, does not consider that individual subnets have distinct characteristics, leading to two problems: (1) The supernet training is biased towards the low-complexity subnets (unfairness); (2) the momentum update in the supernet is noisy (noisy momentum). We present a dynamic supernet training technique to address these problems by adjusting the training strategy adaptive to the subnets. Specifically, we introduce a complexity-aware LR scheduler (CaLR) that controls the decay ratio of LR adaptive to the complexities of subnets, which alleviates the unfairness problem. We also present a momentum separation technique (MS). It groups the subnets with similar structural characteristics and uses a separate momentum for each group, avoiding the noisy momentum problem. Our approach can be applicable to various N-shot NAS methods with marginal cost, while improving the search performance drastically. We validate the effectiveness of our approach on various search spaces (e.g., NAS-Bench-201, Mobilenet spaces) and datasets (e.g., CIFAR-10/100, ImageNet).

### Training-free Neural Architecture Search through Variance of Knowledge of Deep Network Weights.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Tybl_Training-free_Neural_Architecture_Search_through_Variance_of_Knowledge_of_Deep_CVPR_2025_paper.html) · 📚 被引 4
- **作者**: Ondrej Týbl, Lukás Neumann
- **🏷️ 机构**: Czech Technical University in Prague,CMP Visual Recognition Group, Faculty of Electrical Engineering
- **会议**: CVPR 2025
