# Neural Architecture Search — 2021 Guideline

> 领域: 神经架构搜索（NAS、Zero-Cost、搜索空间）
> 论文数: 7 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### HW-NAS-Bench: Hardware-Aware Neural Architecture Search Benchmark.
- **链接**: [arXiv:2103.10584](https://arxiv.org/abs/2103.10584) · [代码](https://github.com/RICE-EIC/HW-NAS-Bench)
- **作者**: Chaojian Li, Zhongzhi Yu, Yonggan Fu, Yongan Zhang, Yang Zhao, Haoran You et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> HardWare-aware Neural Architecture Search (HW-NAS) has recently gained tremendous attention by automating the design of DNNs deployed in more resource-constrained daily life devices. Despite its promising performance, developing optimal HW-NAS solutions can be prohibitively challenging as it requires cross-disciplinary knowledge in the algorithm, micro-architecture, and device-specific compilation. First, to determine the hardware-cost to be incorporated into the NAS process, existing works mostly adopt either pre-collected hardware-cost look-up tables or device-specific hardware-cost models. Both of them limit the development of HW-NAS innovations and impose a barrier-to-entry to non-hardware experts. Second, similar to generic NAS, it can be notoriously difficult to benchmark HW-NAS algorithms due to their significant required computational resources and the differences in adopted search spaces, hyperparameters, and hardware devices. To this end, we develop HW-NAS-Bench, the first public dataset for HW-NAS research which aims to democratize HW-NAS research to non-hardware experts and make HW-NAS research more reproducible and accessible. To design HW-NAS-Bench, we carefully collected the measured/estimated hardware performance of all the networks in the search spaces of both NAS-Bench-201 and FBNet, on six hardware devices that fall into three categories (i.e., commercial edge devices, FPGA, and ASIC). Furthermore, we provide a comprehensive analysis of the collected measurements in HW-NAS-Bench to provide insights for HW-NAS research. Finally, we demonstrate exemplary user cases to (1) show that HW-NAS-Bench allows non-hardware experts to perform HW-NAS by simply querying it and (2) verify that dedicated device-specific HW-NAS can indeed lead to optimal accuracy-cost trade-offs. The codes and all collected data are available at https://github.com/RICE-EIC/HW-NAS-Bench.

</details>

### Neural Architecture Search on ImageNet in Four GPU Hours: A Theoretically Inspired Perspective.
- **链接**: [出版页](https://openreview.net/forum?id=Cnon5ezMHtu)
- **作者**: Wuyang Chen, Xinyu Gong, Zhangyang Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

### DrNAS: Dirichlet Neural Architecture Search.
- **链接**: [arXiv:2006.10355](https://arxiv.org/abs/2006.10355)
- **作者**: Xiangning Chen, Ruochen Wang, Minhao Cheng, Xiaocheng Tang, Cho-Jui Hsieh
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper proposes a novel differentiable architecture search method by formulating it into a distribution learning problem. We treat the continuously relaxed architecture mixing weight as random variables, modeled by Dirichlet distribution. With recently developed pathwise derivatives, the Dirichlet parameters can be easily optimized with gradient-based optimizer in an end-to-end manner. This formulation improves the generalization ability and induces stochasticity that naturally encourages exploration in the search space. Furthermore, to alleviate the large memory consumption of differentiable NAS, we propose a simple yet effective progressive learning scheme that enables searching directly on large-scale tasks, eliminating the gap between search and evaluation phases. Extensive experiments demonstrate the effectiveness of our method. Specifically, we obtain a test error of 2.46% for CIFAR-10, 23.7% for ImageNet under the mobile setting. On NAS-Bench-201, we also achieve state-of-the-art results on all three datasets and provide insights for the effective design of neural architecture search algorithms.

</details>

### Rapid Neural Architecture Search by Learning to Generate Graphs from Datasets.
- **链接**: [出版页](https://openreview.net/forum?id=rkQuFUmUOg3)
- **作者**: Hayeon Lee, Eunyoung Hyung, Sung Ju Hwang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

### Geometry-Aware Gradient Algorithms for Neural Architecture Search.
- **链接**: [arXiv:2004.07802](https://arxiv.org/abs/2004.07802)
- **作者**: Liam Li, Mikhail Khodak, Nina Balcan, Ameet Talwalkar
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent state-of-the-art methods for neural architecture search (NAS) exploit gradient-based optimization by relaxing the problem into continuous optimization over architectures and shared-weights, a noisy process that remains poorly understood. We argue for the study of single-level empirical risk minimization to understand NAS with weight-sharing, reducing the design of NAS methods to devising optimizers and regularizers that can quickly obtain high-quality solutions to this problem. Invoking the theory of mirror descent, we present a geometry-aware framework that exploits the underlying structure of this optimization to return sparse architectural parameters, leading to simple yet novel algorithms that enjoy fast convergence guarantees and achieve state-of-the-art accuracy on the latest NAS benchmarks in computer vision. Notably, we exceed the best published results for both CIFAR and ImageNet on both the DARTS search space and NAS-Bench201; on the latter we achieve near-oracle-optimal performance on CIFAR-10 and CIFAR-100. Together, our theory and experiments demonstrate a principled way to co-design optimizers and continuous relaxations of discrete NAS search spaces.

</details>

### NAS-Bench-ASR: Reproducible Neural Architecture Search for Speech Recognition.
- **链接**: [出版页](https://openreview.net/forum?id=CU0APx9LMaL)
- **作者**: Abhinav Mehrotra, Alberto Gil C. P. Ramos, Sourav Bhattacharya, Lukasz Dudziak, Ravichander Vipperla, Thomas Chau et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

### Interpretable Neural Architecture Search via Bayesian Optimisation with Weisfeiler-Lehman Kernels.
- **链接**: [出版页](https://openreview.net/forum?id=j9Rv7qdXjd)
- **作者**: Bin Xin Ru, Xingchen Wan, Xiaowen Dong, Michael A. Osborne
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021
