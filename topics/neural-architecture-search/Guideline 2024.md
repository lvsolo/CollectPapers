# Neural Architecture Search — 2024 Guideline

> 领域: 神经架构搜索（NAS、Zero-Cost、搜索空间）
> 论文数: 5 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: [2022](Guideline%202022.md)

### Boosting Order-Preserving and Transferability for Neural Architecture Search: A Joint Architecture Refined Search and Fine-Tuning Approach. **⭐⭐⭐** (相关度: 30%)
- **链接**: [arXiv:2403.11380](https://arxiv.org/abs/2403.11380) · 📚 被引 5
- **作者**: Beichen Zhang, Xiaoxing Wang, Xiaohan Qin, Junchi Yan
- **🏷️ 机构**: Shanghai Jiao Tong University,Department of Computer Science and Engineering &#x0026; MoE Key Lab of AI
- **会议**: CVPR 2024
- **摘要（中）**: ①针对两阶段NAS方法中超级网络对候选架构排序的局部保序性不足，导致搜索到的最优架构并非真正最优的问题。②提出Supernet Shifting概念，将架构搜索与超级网络微调相结合，在搜索过程中累积训练损失并每轮更新超级网络，使搜索偏向于高性能架构。③相比传统两阶段方法，通过动态调整超级网络权重，提升了对顶级架构的局部排序一致性。④实验表明该方法在多个数据集上提升了搜索架构的性能和排序质量。
- **摘要（英）**: This paper addresses the issue of insufficient local order-preserving ability in two-stage NAS methods, where supernet rankings of top architectures may not align with true performance. It proposes Supernet Shifting, a strategy that integrates architecture search with supernet fine-tuning by accumulating training loss and updating the supernet during search, thereby improving local ranking consistency. Experiments demonstrate enhanced performance and ranking quality on multiple benchmarks.
- **核心贡献**: 提出Supernet Shifting方法，通过联合搜索与微调提升超级网络的局部保序能力。
- **创新点**: 将架构搜索与超级网络微调动态结合，使搜索过程自适应聚焦于高性能架构。
- **结果**: 在多个数据集上提升了架构搜索的排序质量和最终性能。

### Towards Accurate and Robust Architectures via Neural Architecture Search. **⭐⭐⭐** (相关度: 25%)
- **链接**: [arXiv:2405.05502](https://arxiv.org/abs/2405.05502) · 📚 被引 11
- **作者**: Yuwei Ou, Yuqi Feng, Yanan Sun
- **🏷️ 机构**: College of Computer Science, Sichuan University
- **会议**: CVPR 2024
- **摘要（中）**: ①针对对抗训练中模型架构限制了准确性和鲁棒性的问题，现有方法仅调整权重连接而忽略架构影响。②提出ARNAS方法，设计准确且鲁棒的搜索空间，并采用可微分的多目标搜索策略，同时优化自然损失和对抗损失。③相比传统对抗训练，通过架构搜索在敏感位置部署合适结构，同时提升准确性和鲁棒性。④在白盒攻击、黑盒攻击和迁移性实验中均取得优于基线方法的结果。
- **摘要（英）**: This work tackles the limitation that adversarial training performance is constrained by the network architecture, proposing ARNAS to search for accurate and robust architectures. It designs a specialized search space and uses a differentiable multi-objective strategy to optimize both natural and adversarial losses. Experiments show improved accuracy and robustness under white-box, black-box, and transfer attacks.
- **核心贡献**: 提出ARNAS方法，通过架构搜索同时优化模型的准确性和鲁棒性。
- **创新点**: 设计多目标可微分搜索策略，联合优化自然损失和对抗损失。
- **结果**: 在多种攻击场景下显著提升了模型的准确性和鲁棒性。

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
