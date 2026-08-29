# Self-supervised Vision — 2024 Guideline

> 领域: 视觉自监督学习（对比学习、MAE、DINO 系）
> 论文数: 32 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Disentangled Graph Self-supervised Learning for Out-of-Distribution Generalization.
- **链接**: [出版页](https://proceedings.mlr.press/v235/li24br.html)
- **作者**: Haoyang Li, Xin Wang, Zeyang Zhang, Haibo Chen, Ziwei Zhang, Wenwu Zhu
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### Learning from Memory: Non-Parametric Memory Augmented Self-Supervised Learning of Visual Features.
- **链接**: [arXiv:2407.17486](https://arxiv.org/abs/2407.17486)
- **作者**: Thalles Silva, Hélio Pedrini, Adín Ramírez Rivera
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper introduces a novel approach to improving the training stability of self-supervised learning (SSL) methods by leveraging a non-parametric memory of seen concepts. The proposed method involves augmenting a neural network with a memory component to stochastically compare current image views with previously encountered concepts. Additionally, we introduce stochastic memory blocks to regularize training and enforce consistency between image views. We extensively benchmark our method on many vision tasks, such as linear probing, transfer learning, low-shot classification, and image retrieval on many datasets. The experimental results consolidate the effectiveness of the proposed approach in achieving stable SSL training without additional regularizers while learning highly transferable representations and requiring less computing time and resources.

</details>

### MagicLens: Self-Supervised Image Retrieval with Open-Ended Instructions.
- **链接**: [arXiv:2403.19651](https://arxiv.org/abs/2403.19651)
- **作者**: Kai Zhang, Yi Luan, Hexiang Hu, Kenton Lee, Siyuan Qiao, Wenhu Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Image retrieval, i.e., finding desired images given a reference image, inherently encompasses rich, multi-faceted search intents that are difficult to capture solely using image-based measures. Recent works leverage text instructions to allow users to more freely express their search intents. However, they primarily focus on image pairs that are visually similar and/or can be characterized by a small set of pre-defined relations. The core thesis of this paper is that text instructions can enable retrieving images with richer relations beyond visual similarity. To show this, we introduce MagicLens, a series of self-supervised image retrieval models that support open-ended instructions. MagicLens is built on a key novel insight: image pairs that naturally occur on the same web pages contain a wide range of implicit relations (e.g., inside view of), and we can bring those implicit relations explicit by synthesizing instructions via foundation models. Trained on 36.7M (query image, instruction, target image) triplets with rich semantic relations mined from the web, MagicLens achieves results comparable with or better than prior best on eight benchmarks of various image retrieval tasks, while maintaining high parameter efficiency with a significantly smaller model size. Additional human analyses on a 1.4M-image unseen corpus further demonstrate the diversity of search intents supported by MagicLens. Code and models are publicly available at https://open-vision-language.github.io/MagicLens/.

</details>

### Regularizing with Pseudo-Negatives for Continual Self-Supervised Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v235/cha24a.html)
- **作者**: Sungmin Cha, Kyunghyun Cho, Taesup Moon
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### Enhancing Trajectory Prediction through Self-Supervised Waypoint Distortion Prediction.
- **链接**: [出版页](https://proceedings.mlr.press/v235/chib24b.html)
- **作者**: Pranav Singh Chib, Pravendra Singh
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### Exploring Correlations of Self-Supervised Tasks for Graphs.
- **链接**: [arXiv:2405.04245](https://arxiv.org/abs/2405.04245)
- **作者**: Taoran Fang, Wei Chow, Yifei Sun, Kaiqiao Han, Lvbin Ma, Yang Yang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Graph self-supervised learning has sparked a research surge in training informative representations without accessing any labeled data. However, our understanding of graph self-supervised learning remains limited, and the inherent relationships between various self-supervised tasks are still unexplored. Our paper aims to provide a fresh understanding of graph self-supervised learning based on task correlations. Specifically, we evaluate the performance of the representations trained by one specific task on other tasks and define correlation values to quantify task correlations. Through this process, we unveil the task correlations between various self-supervised tasks and can measure their expressive capabilities, which are closely related to downstream performance. By analyzing the correlation values between tasks across various datasets, we reveal the complexity of task correlations and the limitations of existing multi-task learning methods. To obtain more capable representations, we propose Graph Task Correlation Modeling (GraphTCM) to illustrate the task correlations and utilize it to enhance graph self-supervised training. The experimental results indicate that our method significantly outperforms existing methods across various downstream tasks.

</details>

### Speech Self-Supervised Learning Using Diffusion Model Synthetic Data.
- **链接**: [出版页](https://proceedings.mlr.press/v235/gao24j.html)
- **作者**: Heting Gao, Kaizhi Qian, Junrui Ni, Chuang Gan, Mark A. Hasegawa-Johnson, Shiyu Chang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### Be Your Own Neighborhood: Detecting Adversarial Examples by the Neighborhood Relations Built on Self-Supervised Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v235/he24l.html)
- **作者**: Zhiyuan He, Yijun Yang, Pin-Yu Chen, Qiang Xu, Tsung-Yi Ho
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### FedSC: Provable Federated Self-supervised Learning with Spectral Contrastive Objective over Non-i.i.d. Data.
- **链接**: [arXiv:2405.03949](https://arxiv.org/abs/2405.03949)
- **作者**: Shusen Jing, Anlan Yu, Shuai Zhang, Songyang Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent efforts have been made to integrate self-supervised learning (SSL) with the framework of federated learning (FL). One unique challenge of federated self-supervised learning (FedSSL) is that the global objective of FedSSL usually does not equal the weighted sum of local SSL objectives. Consequently, conventional approaches, such as federated averaging (FedAvg), fail to precisely minimize the FedSSL global objective, often resulting in suboptimal performance, especially when data is non-i.i.d.. To fill this gap, we propose a provable FedSSL algorithm, named FedSC, based on the spectral contrastive objective. In FedSC, clients share correlation matrices of data representations in addition to model weights periodically, which enables inter-client contrast of data samples in addition to intra-client contrast and contraction, resulting in improved quality of data representations. Differential privacy (DP) protection is deployed to control the additional privacy leakage on local datasets when correlation matrices are shared. We also provide theoretical analysis on the convergence and extra privacy leakage. The experimental results validate the effectiveness of our proposed algorithm.

</details>

### Binning as a Pretext Task: Improving Self-Supervised Learning in Tabular Domains.
- **链接**: [arXiv:2405.07414](https://arxiv.org/abs/2405.07414) · [代码](https://github.com/kyungeun-lee/tabularbinning)
- **作者**: Kyungeun Lee, Ye Seul Sim, Hye-Seung Cho, Moonjung Eo, Suhee Yoon, Sanghyu Yoon et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The ability of deep networks to learn superior representations hinges on leveraging the proper inductive biases, considering the inherent properties of datasets. In tabular domains, it is critical to effectively handle heterogeneous features (both categorical and numerical) in a unified manner and to grasp irregular functions like piecewise constant functions. To address the challenges in the self-supervised learning framework, we propose a novel pretext task based on the classical binning method. The idea is straightforward: reconstructing the bin indices (either orders or classes) rather than the original values. This pretext task provides the encoder with an inductive bias to capture the irregular dependencies, mapping from continuous inputs to discretized bins, and mitigates the feature heterogeneity by setting all features to have category-type targets. Our empirical investigations ascertain several advantages of binning: capturing the irregular function, compatibility with encoder architecture and additional modifications, standardizing all features into equal sets, grouping similar values within a feature, and providing ordering information. Comprehensive evaluations across diverse tabular datasets corroborate that our method consistently improves tabular representation learning performance for a wide range of downstream tasks. The codes are available in https://github.com/kyungeun-lee/tabularbinning.

</details>

### Compress Clean Signal from Noisy Raw Image: A Self-Supervised Approach.
- **链接**: [出版页](https://proceedings.mlr.press/v235/li24bl.html)
- **作者**: Zhihao Li, Yufei Wang, Alex C. Kot, Bihan Wen
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### Self-Supervised Interpretable End-to-End Learning via Latent Functional Modularity.
- **链接**: [出版页](https://proceedings.mlr.press/v235/seong24a.html)
- **作者**: Hyunki Seong, David Hyunchul Shim
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### Self-Supervised Coarsening of Unstructured Grid with Automatic Differentiation.
- **链接**: [arXiv:2507.18297](https://arxiv.org/abs/2507.18297)
- **作者**: Sergei Shumilin, Alexander Ryabov, Nikolay B. Yavich, Evgeny Burnaev, Vladimir Vanovskiy
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Due to the high computational load of modern numerical simulation, there is a demand for approaches that would reduce the size of discrete problems while keeping the accuracy reasonable. In this work, we present an original algorithm to coarsen an unstructured grid based on the concepts of differentiable physics. We achieve this by employing k-means clustering, autodifferentiation and stochastic minimization algorithms. We demonstrate performance of the designed algorithm on two PDEs: a linear parabolic equation which governs slightly compressible fluid flow in porous media and the wave equation. Our results show that in the considered scenarios, we reduced the number of grid points up to 10 times while preserving the modeled variable dynamics in the points of interest. The proposed approach can be applied to the simulation of an arbitrary system described by evolutionary partial differential equations.

</details>

### Information Flow in Self-Supervised Learning.
- **链接**: [arXiv:2309.17281](https://arxiv.org/abs/2309.17281)
- **作者**: Zhiquan Tan, Jingqin Yang, Weiran Huang, Yang Yuan, Yifan Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we conduct a comprehensive analysis of two dual-branch (Siamese architecture) self-supervised learning approaches, namely Barlow Twins and spectral contrastive learning, through the lens of matrix mutual information. We prove that the loss functions of these methods implicitly optimize both matrix mutual information and matrix joint entropy. This insight prompts us to further explore the category of single-branch algorithms, specifically MAE and U-MAE, for which mutual information and joint entropy become the entropy. Building on this intuition, we introduce the Matrix Variational Masked Auto-Encoder (M-MAE), a novel method that leverages the matrix-based estimation of entropy as a regularizer and subsumes U-MAE as a special case. The empirical evaluations underscore the effectiveness of M-MAE compared with the state-of-the-art methods, including a 3.9% improvement in linear probing ViT-Base, and a 1% improvement in fine-tuning ViT-Large, both on ImageNet.

</details>

### Bootstrap AutoEncoders With Contrastive Paradigm for Self-supervised Gaze Estimation.
- **链接**: [出版页](https://proceedings.mlr.press/v235/wang24ah.html)
- **作者**: Yaoming Wang, Jin Li, Wenrui Dai, Bowen Shi, Xiaopeng Zhang, Chenglin Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### From Coarse to Fine: Enable Comprehensive Graph Self-supervised Learning with Multi-granular Semantic Ensemble.
- **链接**: [出版页](https://proceedings.mlr.press/v235/wen24e.html)
- **作者**: Qianlong Wen, Mingxuan Ju, Zhongyu Ouyang, Chuxu Zhang, Yanfang Ye
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### Matrix Information Theory for Self-Supervised Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v235/zhang24bi.html)
- **作者**: Yifan Zhang, Zhiquan Tan, Jingqin Yang, Weiran Huang, Yang Yuan
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### High-Order Contrastive Learning with Fine-grained Comparative Levels for Sparse Ordinal Tensor Completion.
- **链接**: [出版页](https://proceedings.mlr.press/v235/dai24c.html)
- **作者**: Yu Dai, Junchen Shen, Zijie Zhai, Danlin Liu, Jingyang Chen, Yu Sun et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### MF-CLR: Multi-Frequency Contrastive Learning Representation for Time Series.
- **链接**: [出版页](https://proceedings.mlr.press/v235/duan24b.html)
- **作者**: Jufang Duan, Wei Zheng, Yangzhou Du, Wenfa Wu, Haipeng Jiang, Hongsheng Qi
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### Bridging Mini-Batch and Asymptotic Analysis in Contrastive Learning: From InfoNCE to Kernel-Based Losses.
- **链接**: [arXiv:2405.18045](https://arxiv.org/abs/2405.18045)
- **作者**: Panagiotis Koromilas, Giorgos Bouritsas, Theodoros Giannakopoulos, Mihalis Nicolaou, Yannis Panagakis
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> What do different contrastive learning (CL) losses actually optimize for? Although multiple CL methods have demonstrated remarkable representation learning capabilities, the differences in their inner workings remain largely opaque. In this work, we analyse several CL families and prove that, under certain conditions, they admit the same minimisers when optimizing either their batch-level objectives or their expectations asymptotically. In both cases, an intimate connection with the hyperspherical energy minimisation (HEM) problem resurfaces. Drawing inspiration from this, we introduce a novel CL objective, coined Decoupled Hyperspherical Energy Loss (DHEL). DHEL simplifies the problem by decoupling the target hyperspherical energy from the alignment of positive examples while preserving the same theoretical guarantees. Going one step further, we show the same results hold for another relevant CL family, namely kernel contrastive learning (KCL), with the additional advantage of the expected loss being independent of batch size, thus identifying the minimisers in the non-asymptotic regime. Empirical results demonstrate improved downstream performance and robustness across combinations of different batch sizes and hyperparameters and reduced dimensionality collapse, on several computer vision datasets.

</details>

### Perfect Alignment May be Poisonous to Graph Contrastive Learning.
- **链接**: [arXiv:2310.03977](https://arxiv.org/abs/2310.03977) · [代码](https://github.com/somebodyhh1/GRACEIS)
- **作者**: Jingyu Liu, Huayi Tang, Yong Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Graph Contrastive Learning (GCL) aims to learn node representations by aligning positive pairs and separating negative ones. However, few of researchers have focused on the inner law behind specific augmentations used in graph-based learning. What kind of augmentation will help downstream performance, how does contrastive learning actually influence downstream tasks, and why the magnitude of augmentation matters so much? This paper seeks to address these questions by establishing a connection between augmentation and downstream performance. Our findings reveal that GCL contributes to downstream tasks mainly by separating different classes rather than gathering nodes of the same class. So perfect alignment and augmentation overlap which draw all intra-class samples the same can not fully explain the success of contrastive learning. Therefore, in order to understand how augmentation aids the contrastive learning process, we conduct further investigations into the generalization, finding that perfect alignment that draw positive pair the same could help contrastive loss but is poisonous to generalization, as a result, perfect alignment may not lead to best downstream performance, so specifically designed augmentation is needed to achieve appropriate alignment performance and improve downstream accuracy. We further analyse the result by information theory and graph spectrum theory and propose two simple but effective methods to verify the theories. The two methods could be easily applied to various GCL algorithms and extensive experiments are conducted to prove its effectiveness. The code is available at https://github.com/somebodyhh1/GRACEIS

</details>

### On the Effectiveness of Supervision in Asymmetric Non-Contrastive Learning.
- **链接**: [arXiv:2406.10815](https://arxiv.org/abs/2406.10815) · [代码](https://github.com/JH-Oh-23/Sup-ANCL)
- **作者**: Jeongheon Oh, Kibok Lee
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Supervised contrastive representation learning has been shown to be effective in various transfer learning scenarios. However, while asymmetric non-contrastive learning (ANCL) often outperforms its contrastive learning counterpart in self-supervised representation learning, the extension of ANCL to supervised scenarios is less explored. To bridge the gap, we study ANCL for supervised representation learning, coined SupSiam and SupBYOL, leveraging labels in ANCL to achieve better representations. The proposed supervised ANCL framework improves representation learning while avoiding collapse. Our analysis reveals that providing supervision to ANCL reduces intra-class variance, and the contribution of supervision should be adjusted to achieve the best performance. Experiments demonstrate the superiority of supervised ANCL across various datasets and tasks. The code is available at: https://github.com/JH-Oh-23/Sup-ANCL.

</details>

### Community-Invariant Graph Contrastive Learning.
- **链接**: [arXiv:2405.01350](https://arxiv.org/abs/2405.01350) · [代码](https://github.com/ShiyinTan/CI-GCL.git)
- **作者**: Shiyin Tan, Dongyuan Li, Renhe Jiang, Ying Zhang, Manabu Okumura
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Graph augmentation has received great attention in recent years for graph contrastive learning (GCL) to learn well-generalized node/graph representations. However, mainstream GCL methods often favor randomly disrupting graphs for augmentation, which shows limited generalization and inevitably leads to the corruption of high-level graph information, i.e., the graph community. Moreover, current knowledge-based graph augmentation methods can only focus on either topology or node features, causing the model to lack robustness against various types of noise. To address these limitations, this research investigated the role of the graph community in graph augmentation and figured out its crucial advantage for learnable graph augmentation. Based on our observations, we propose a community-invariant GCL framework to maintain graph community structure during learnable graph augmentation. By maximizing the spectral changes, this framework unifies the constraints of both topology and feature augmentation, enhancing the model's robustness. Empirical evidence on 21 benchmark datasets demonstrates the exclusive merits of our framework. Code is released on Github (https://github.com/ShiyinTan/CI-GCL.git).

</details>

### S3GCL: Spectral, Swift, Spatial Graph Contrastive Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v235/wan24g.html)
- **作者**: Guancheng Wan, Yijun Tian, Wenke Huang, Nitesh V. Chawla, Mang Ye
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### Confidence-aware Contrastive Learning for Selective Classification.
- **链接**: [arXiv:2406.04745](https://arxiv.org/abs/2406.04745)
- **作者**: Yu-Chang Wu, Shen-Huan Lyu, Haopu Shang, Xiangyu Wang, Chao Qian
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Selective classification enables models to make predictions only when they are sufficiently confident, aiming to enhance safety and reliability, which is important in high-stakes scenarios. Previous methods mainly use deep neural networks and focus on modifying the architecture of classification layers to enable the model to estimate the confidence of its prediction. This work provides a generalization bound for selective classification, disclosing that optimizing feature layers helps improve the performance of selective classification. Inspired by this theory, we propose to explicitly improve the selective classification model at the feature level for the first time, leading to a novel Confidence-aware Contrastive Learning method for Selective Classification, CCL-SC, which similarizes the features of homogeneous instances and differentiates the features of heterogeneous instances, with the strength controlled by the model's confidence. The experimental results on typical datasets, i.e., CIFAR-10, CIFAR-100, CelebA, and ImageNet, show that CCL-SC achieves significantly lower selective risk than state-of-the-art methods, across almost all coverage degrees. Moreover, it can be combined with existing methods to bring further improvement.

</details>

### Contrastive Learning for Clinical Outcome Prediction with Partial Data Sources.
- **链接**: [出版页](https://proceedings.mlr.press/v235/xia24e.html)
- **作者**: Meng Xia, Jonathan Wilson, Benjamin Goldstein, Ricardo Henao
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### Efficient Contrastive Learning for Fast and Accurate Inference on Graphs.
- **链接**: [出版页](https://proceedings.mlr.press/v235/xiao24g.html)
- **作者**: Teng Xiao, Huaisheng Zhu, Zhiwei Zhang, Zhimeng Guo, Charu C. Aggarwal, Suhang Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### EMC2: Efficient MCMC Negative Sampling for Contrastive Learning with Global Convergence.
- **链接**: [arXiv:2404.10575](https://arxiv.org/abs/2404.10575)
- **作者**: Chung-Yiu Yau, Hoi-To Wai, Parameswaran Raman, Soumajyoti Sarkar, Mingyi Hong
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> A key challenge in contrastive learning is to generate negative samples from a large sample set to contrast with positive samples, for learning better encoding of the data. These negative samples often follow a softmax distribution which are dynamically updated during the training process. However, sampling from this distribution is non-trivial due to the high computational costs in computing the partition function. In this paper, we propose an Efficient Markov Chain Monte Carlo negative sampling method for Contrastive learning (EMC$^2$). We follow the global contrastive learning loss as introduced in SogCLR, and propose EMC$^2$ which utilizes an adaptive Metropolis-Hastings subroutine to generate hardness-aware negative samples in an online fashion during the optimization. We prove that EMC$^2$ finds an $\mathcal{O}(1/\sqrt{T})$-stationary point of the global contrastive loss in $T$ iterations. Compared to prior works, EMC$^2$ is the first algorithm that exhibits global convergence (to stationarity) regardless of the choice of batch size while exhibiting low computation and memory cost. Numerical experiments validate that EMC$^2$ is effective with small batch training and achieves comparable or better performance than baseline algorithms. We report the results for pre-training image encoders on STL-10 and Imagenet-100.

</details>

### DiffAug: Enhance Unsupervised Contrastive Learning with Domain-Knowledge-Free Diffusion-based Data Augmentation.
- **链接**: [出版页](https://proceedings.mlr.press/v235/zang24a.html)
- **作者**: Zelin Zang, Hao Luo, Kai Wang, Panpan Zhang, Fan Wang, Stan Z. Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### Stochastic positional embeddings improve masked image modeling.
- **链接**: [出版页](https://proceedings.mlr.press/v235/bar24a.html)
- **作者**: Amir Bar, Florian Bordes, Assaf Shocher, Mido Assran, Pascal Vincent, Nicolas Ballas et al.
- **🏷️ 机构**: UC Berkeley
- **会议**: ICML 2024

## 跨领域论文（完整笔记在其他领域）

- UniCorn: A Unified Contrastive Learning Approach for Multi-view Molecular Representation Learning. → [multi-camera-perception](../multi-camera-perception/Guideline%202024.md)
- EquiAV: Leveraging Equivariance for Audio-Visual Contrastive Learning. → [multimodal](../multimodal/Guideline%202024.md)
