# Neural Architecture Search — 2022 Guideline

> 领域: 神经架构搜索（NAS、Zero-Cost、搜索空间）
> 论文数: 11 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### EAutoDet: Efficient Architecture Search for Object Detection.
- **链接**: [arXiv:2203.10747](https://arxiv.org/abs/2203.10747) · 📚 被引 24
- **作者**: Xiaoxing Wang, Jiale Lin, Juanping Zhao, Xiaokang Yang, Junchi Yan
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

- **摘要（英，原文）**:

  > Training CNN for detection is time-consuming due to the large dataset and complex network modules, making it hard to search architectures on detection datasets directly, which usually requires vast search costs (usually tens and even hundreds of GPU-days). In contrast, this paper introduces an efficient framework, named EAutoDet, that can discover practical backbone and FPN architectures for object detection in 1.4 GPU-days. Specifically, we construct a supernet for both backbone and FPN modules and adopt the differentiable method. To reduce the GPU memory requirement and computational cost, we propose a kernel reusing technique by sharing the weights of candidate operations on one edge and consolidating them into one convolution. A dynamic channel refinement strategy is also introduced to search channel numbers. Extensive experiments show significant efficacy and efficiency of our method. In particular, the discovered architectures surpass state-of-the-art object detection NAS methods and achieve 40.1 mAP with 120 FPS and 49.2 mAP with 41.3 FPS on COCO test-dev set. We also transfer the discovered architectures to rotation detection task, which achieve 77.05 mAP$_{\text{50}}$ on DOTA-v1.0 test set with 21.1M parameters.

### ViTAS: Vision Transformer Architecture Search.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19803-8_9)
- **作者**: Xiu Su, Shan You, Jiyang Xie, Mingkai Zheng, Fei Wang, Chen Qian et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Spectrum-Aware and Transferable Architecture Search for Hyperspectral Image Restoration.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19800-7_2) · 📚 被引 14
- **作者**: Wei He, Quanming Yao, Naoto Yokoya, Tatsumi Uezato, Hongyan Zhang, Liangpei Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Neural Architecture Search for Spiking Neural Networks.
- **链接**: [arXiv:2201.10355](https://arxiv.org/abs/2201.10355)
- **作者**: Youngeun Kim, Yuhang Li, Hyoungseob Park, Yeshwanth Venkatesha, Priyadarshini Panda
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

- **摘要（英，原文）**:

  > Spiking Neural Networks (SNNs) have gained huge attention as a potential energy-efficient alternative to conventional Artificial Neural Networks (ANNs) due to their inherent high-sparsity activation. However, most prior SNN methods use ANN-like architectures (e.g., VGG-Net or ResNet), which could provide sub-optimal performance for temporal sequence processing of binary information in SNNs. To address this, in this paper, we introduce a novel Neural Architecture Search (NAS) approach for finding better SNN architectures. Inspired by recent NAS approaches that find the optimal architecture from activation patterns at initialization, we select the architecture that can represent diverse spike activation patterns across different data samples without training. Moreover, to further leverage the temporal information among the spikes, we search for feed forward connections as well as backward connections (i.e., temporal feedback connections) between layers. Interestingly, SNASNet found by our search algorithm achieves higher performance with backward connections, demonstrating the importance of designing SNN architecture for suitably using temporal information. We conduct extensive experiments on three image recognition benchmarks where we show that SNASNet achieves state-of-the-art performance with significantly lower timesteps (5 timesteps). Code is available at Github.

### UniNet: Unified Architecture Search with Convolution, Transformer, and MLP.
- **链接**: [arXiv:2207.05420](https://arxiv.org/abs/2207.05420) · [代码](https://github.com/Sense-X/UniNet) · 📚 被引 21
- **作者**: Jihao Liu, Xin Huang, Guanglu Song, Hongsheng Li, Yu Liu
- **🏷️ 机构**: CUHK, SenseTime
- **会议**: ECCV 2022

- **摘要（英，原文）**:

  > Recently, transformer and multi-layer perceptron (MLP) architectures have achieved impressive results on various vision tasks. However, how to effectively combine those operators to form high-performance hybrid visual architectures still remains a challenge. In this work, we study the learnable combination of convolution, transformer, and MLP by proposing a novel unified architecture search approach. Our approach contains two key designs to achieve the search for high-performance networks. First, we model the very different searchable operators in a unified form, and thus enable the operators to be characterized with the same set of configuration parameters. In this way, the overall search space size is significantly reduced, and the total search cost becomes affordable. Second, we propose context-aware downsampling modules (DSMs) to mitigate the gap between the different types of operators. Our proposed DSMs are able to better adapt features from different types of operators, which is important for identifying high-performance hybrid architectures. Finally, we integrate configurable operators and DSMs into a unified search space and search with a Reinforcement Learning-based search algorithm to fully explore the optimal combination of the operators. To this end, we search a baseline network and scale it up to obtain a family of models, named UniNets, which achieve much better accuracy and efficiency than previous ConvNets and Transformers. In particular, our UniNet-B5 achieves 84.9% top-1 accuracy on ImageNet, outperforming EfficientNet-B7 and BoTNet-T7 with 44% and 55% fewer FLOPs respectively. By pretraining on the ImageNet-21K, our UniNet-B6 achieves 87.4%, outperforming Swin-L with 51% fewer FLOPs and 41% fewer parameters. Code is available at https://github.com/Sense-X/UniNet.

### Data-Free Neural Architecture Search via Recursive Label Calibration.
- **链接**: [arXiv:2112.02086](https://arxiv.org/abs/2112.02086) · 📚 被引 5
- **作者**: Zechun Liu, Zhiqiang Shen, Yun Long, Eric P. Xing, Kwang-Ting Cheng, Chas Leichner
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

- **摘要（英，原文）**:

  > This paper aims to explore the feasibility of neural architecture search (NAS) given only a pre-trained model without using any original training data. This is an important circumstance for privacy protection, bias avoidance, etc., in real-world scenarios. To achieve this, we start by synthesizing usable data through recovering the knowledge from a pre-trained deep neural network. Then we use the synthesized data and their predicted soft-labels to guide neural architecture search. We identify that the NAS task requires the synthesized data (we target at image domain here) with enough semantics, diversity, and a minimal domain gap from the natural images. For semantics, we propose recursive label calibration to produce more informative outputs. For diversity, we propose a regional update strategy to generate more diverse and semantically-enriched synthetic data. For minimal domain gap, we use input and feature-level regularization to mimic the original data distribution in latent space. We instantiate our proposed framework with three popular NAS algorithms: DARTS, ProxylessNAS and SPOS. Surprisingly, our results demonstrate that the architectures discovered by searching with our synthetic data achieve accuracy that is comparable to, or even higher than, architectures discovered by searching from the original ones, for the first time, deriving the conclusion that NAS can be done effectively with no need of access to the original or called natural data if the synthesis method is well designed.

### Robust Network Architecture Search via Feature Distortion Restraining.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20065-6_8) · 📚 被引 6
- **作者**: Yaguan Qian, Shenghui Huang, Bin Wang, Xiang Ling, Xiaohui Guan, Zhaoquan Gu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Compiler-Aware Neural Architecture Search for On-Mobile Real-time Super-Resolution.
- **链接**: [arXiv:2207.12577](https://arxiv.org/abs/2207.12577) · 📚 被引 25
- **作者**: Yushu Wu, Yifan Gong, Pu Zhao, Yanyu Li, Zheng Zhan, Wei Niu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

- **摘要（英，原文）**:

  > Deep learning-based super-resolution (SR) has gained tremendous popularity in recent years because of its high image quality performance and wide application scenarios. However, prior methods typically suffer from large amounts of computations and huge power consumption, causing difficulties for real-time inference, especially on resource-limited platforms such as mobile devices. To mitigate this, we propose a compiler-aware SR neural architecture search (NAS) framework that conducts depth search and per-layer width search with adaptive SR blocks. The inference speed is directly taken into the optimization along with the SR loss to derive SR models with high image quality while satisfying the real-time inference requirement. Instead of measuring the speed on mobile devices at each iteration during the search process, a speed model incorporated with compiler optimizations is leveraged to predict the inference latency of the SR block with various width configurations for faster convergence. With the proposed framework, we achieve real-time SR inference for implementing 720p resolution with competitive SR performance (in terms of PSNR and SSIM) on GPU/DSP of mobile platforms (Samsung Galaxy S21).

### A Max-Flow Based Approach for Neural Architecture Search.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20044-1_39)
- **作者**: Chao Xue, Xiaoxing Wang, Junchi Yan, Chun-Guang Li
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### EAGAN: Efficient Two-Stage Evolutionary Architecture Search for GANs.
- **链接**: [arXiv:2111.15097](https://arxiv.org/abs/2111.15097) · [代码](https://github.com/marsggbo/EAGAN) · 📚 被引 22
- **作者**: Guohao Ying, Xin He, Bin Gao, Bo Han, Xiaowen Chu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

- **摘要（英，原文）**:

  > Generative adversarial networks (GANs) have proven successful in image generation tasks. However, GAN training is inherently unstable. Although many works try to stabilize it by manually modifying GAN architecture, it requires much expertise. Neural architecture search (NAS) has become an attractive solution to search GANs automatically. The early NAS-GANs search only generators to reduce search complexity but lead to a sub-optimal GAN. Some recent works try to search both generator (G) and discriminator (D), but they suffer from the instability of GAN training. To alleviate the instability, we propose an efficient two-stage evolutionary algorithm-based NAS framework to search GANs, namely EAGAN. We decouple the search of G and D into two stages, where stage-1 searches G with a fixed D and adopts the many-to-one training strategy, and stage-2 searches D with the optimal G found in stage-1 and adopts the one-to-one training and weight-resetting strategies to enhance the stability of GAN training. Both stages use the non-dominated sorting method to produce Pareto-front architectures under multiple objectives (e.g., model size, Inception Score (IS), and Fréchet Inception Distance (FID)). EAGAN is applied to the unconditional image generation task and can efficiently finish the search on the CIFAR-10 dataset in 1.2 GPU days. Our searched GANs achieve competitive results (IS=8.81$\pm$0.10, FID=9.91) on the CIFAR-10 dataset and surpass prior NAS-GANs on the STL-10 dataset (IS=10.44$\pm$0.087, FID=22.18). Source code: https://github.com/marsggbo/EAGAN.

### U-Boost NAS: Utilization-Boosted Differentiable Neural Architecture Search.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19775-8_11) · 📚 被引 3
- **作者**: Ahmet Caner Yüzügüler, Nikolaos Dimitriadis, Pascal Frossard
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
