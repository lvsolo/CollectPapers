# Neural Architecture Search — 2020 Guideline

> 领域: 神经架构搜索（NAS、Zero-Cost、搜索空间）
> 论文数: 19 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Angle-Based Search Space Shrinking for Neural Architecture Search.
- **链接**: [arXiv:2004.13431](https://arxiv.org/abs/2004.13431)
- **作者**: Yiming Hu, Yuding Liang, Zichao Guo, Ruosi Wan, Xiangyu Zhang, Yichen Wei et al.
- **🏷️ 机构**: MEGVII
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this work, we present a simple and general search space shrinking method, called Angle-Based search space Shrinking (ABS), for Neural Architecture Search (NAS). Our approach progressively simplifies the original search space by dropping unpromising candidates, thus can reduce difficulties for existing NAS methods to find superior architectures. In particular, we propose an angle-based metric to guide the shrinking process. We provide comprehensive evidences showing that, in weight-sharing supernet, the proposed metric is more stable and accurate than accuracy-based and magnitude-based metrics to predict the capability of child models. We also show that the angle-based metric can converge fast while training supernet, enabling us to get promising shrunk search spaces efficiently. ABS can easily apply to most of NAS approaches (e.g. SPOS, FairNAS, ProxylessNAS, DARTS and PDARTS). Comprehensive experiments show that ABS can dramatically enhance existing NAS approaches by providing a promising shrunk search space.

</details>

### TF-NAS: Rethinking Three Search Freedoms of Latency-Constrained Differentiable Neural Architecture Search.
- **链接**: [arXiv:2008.05314](https://arxiv.org/abs/2008.05314) · [代码](https://github.com/AberHu/TF-NAS) · 📚 被引 30
- **作者**: Yibo Hu, Xiang Wu, Ran He
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> With the flourish of differentiable neural architecture search (NAS), automatically searching latency-constrained architectures gives a new perspective to reduce human labor and expertise. However, the searched architectures are usually suboptimal in accuracy and may have large jitters around the target latency. In this paper, we rethink three freedoms of differentiable NAS, i.e. operation-level, depth-level and width-level, and propose a novel method, named Three-Freedom NAS (TF-NAS), to achieve both good classification accuracy and precise latency constraint. For the operation-level, we present a bi-sampling search algorithm to moderate the operation collapse. For the depth-level, we introduce a sink-connecting search space to ensure the mutual exclusion between skip and other candidate operations, as well as eliminate the architecture redundancy. For the width-level, we propose an elasticity-scaling strategy that achieves precise latency constraint in a progressively fine-grained manner. Experiments on ImageNet demonstrate the effectiveness of TF-NAS. Particularly, our searched TF-NAS-A obtains 76.9% top-1 accuracy, achieving state-of-the-art results with less latency. The total search time is only 1.8 days on 1 Titan RTX GPU. Code is available at https://github.com/AberHu/TF-NAS.

</details>

### BATS: Binary ArchitecTure Search.
- **链接**: [arXiv:2003.01711](https://arxiv.org/abs/2003.01711) · [代码](https://github.com/1adrianb/binary-nas) · 📚 被引 43
- **作者**: Adrian Bulat, Brais Martínez, Georgios Tzimiropoulos
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper proposes Binary ArchitecTure Search (BATS), a framework that drastically reduces the accuracy gap between binary neural networks and their real-valued counterparts by means of Neural Architecture Search (NAS). We show that directly applying NAS to the binary domain provides very poor results. To alleviate this, we describe, to our knowledge, for the first time, the 3 key ingredients for successfully applying NAS to the binary domain. Specifically, we (1) introduce and design a novel binary-oriented search space, (2) propose a new mechanism for controlling and stabilising the resulting searched topologies, (3) propose and validate a series of new search strategies for binary networks that lead to faster convergence and lower search times. Experimental results demonstrate the effectiveness of the proposed approach and the necessity of searching in the binary space directly. Moreover, (4) we set a new state-of-the-art for binary neural networks on CIFAR10, CIFAR100 and ImageNet datasets. Code will be made available https://github.com/1adrianb/binary-nas

</details>

### CATCH: Context-Based Meta Reinforcement Learning for Transferrable Architecture Search.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58529-7_12) · 📚 被引 14
- **作者**: Xin Chen, Yawen Duan, Zewei Chen, Hang Xu, Zihao Chen, Xiaodan Liang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### NAS-DIP: Learning Deep Image Prior with Neural Architecture Search.
- **链接**: [arXiv:2008.11713](https://arxiv.org/abs/2008.11713) · 📚 被引 43
- **作者**: Yun-Chun Chen, Chen Gao, Esther Robb, Jia-Bin Huang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent work has shown that the structure of deep convolutional neural networks can be used as a structured image prior for solving various inverse image restoration tasks. Instead of using hand-designed architectures, we propose to search for neural architectures that capture stronger image priors. Building upon a generic U-Net architecture, our core contribution lies in designing new search spaces for (1) an upsampling cell and (2) a pattern of cross-scale residual connections. We search for an improved network by leveraging an existing neural architecture search algorithm (using reinforcement learning with a recurrent neural network controller). We validate the effectiveness of our method via a wide variety of applications, including image restoration, dehazing, image-to-image translation, and matrix factorization. Extensive experimental results show that our algorithm performs favorably against state-of-the-art learning-free approaches and reaches competitive performance with existing learning-based methods in some cases.

</details>

### Anti-bandit Neural Architecture Search for Model Defense.
- **链接**: [arXiv:2008.00698](https://arxiv.org/abs/2008.00698)
- **作者**: Hanlin Chen, Baochang Zhang, Song Xue, Xuan Gong, Hong Liu, Rongrong Ji et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep convolutional neural networks (DCNNs) have dominated as the best performers in machine learning, but can be challenged by adversarial attacks. In this paper, we defend against adversarial attacks using neural architecture search (NAS) which is based on a comprehensive search of denoising blocks, weight-free operations, Gabor filters and convolutions. The resulting anti-bandit NAS (ABanditNAS) incorporates a new operation evaluation measure and search process based on the lower and upper confidence bounds (LCB and UCB). Unlike the conventional bandit algorithm using UCB for evaluation only, we use UCB to abandon arms for search efficiency and LCB for a fair competition between arms. Extensive experiments demonstrate that ABanditNAS is faster than other NAS methods, while achieving an $8.73\%$ improvement over prior arts on CIFAR-10 under PGD-$7$.

</details>

### Fair DARTS: Eliminating Unfair Advantages in Differentiable Architecture Search.
- **链接**: [arXiv:1911.12126](https://arxiv.org/abs/1911.12126) · [代码](https://github.com/xiaomi-automl/fairdarts) · 📚 被引 186
- **作者**: Xiangxiang Chu, Tianbao Zhou, Bo Zhang, Jixiang Li
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Differentiable Architecture Search (DARTS) is now a widely disseminated weight-sharing neural architecture search method. However, it suffers from well-known performance collapse due to an inevitable aggregation of skip connections. In this paper, we first disclose that its root cause lies in an unfair advantage in exclusive competition. Through experiments, we show that if either of two conditions is broken, the collapse disappears. Thereby, we present a novel approach called Fair DARTS where the exclusive competition is relaxed to be collaborative. Specifically, we let each operation's architectural weight be independent of others. Yet there is still an important issue of discretization discrepancy. We then propose a zero-one loss to push architectural weights towards zero or one, which approximates an expected multi-hot solution. Our experiments are performed on two mainstream search spaces, and we derive new state-of-the-art results on CIFAR-10 and ImageNet. Our code is available on https://github.com/xiaomi-automl/fairdarts .

</details>

### Single Path One-Shot Neural Architecture Search with Uniform Sampling.
- **链接**: [arXiv:1904.00420](https://arxiv.org/abs/1904.00420) · 📚 被引 480
- **作者**: Zichao Guo, Xiangyu Zhang, Haoyuan Mu, Wen Heng, Zechun Liu, Yichen Wei et al.
- **🏷️ 机构**: MEGVII
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We revisit the one-shot Neural Architecture Search (NAS) paradigm and analyze its advantages over existing NAS approaches. Existing one-shot method, however, is hard to train and not yet effective on large scale datasets like ImageNet. This work propose a Single Path One-Shot model to address the challenge in the training. Our central idea is to construct a simplified supernet, where all architectures are single paths so that weight co-adaption problem is alleviated. Training is performed by uniform path sampling. All architectures (and their weights) are trained fully and equally. Comprehensive experiments verify that our approach is flexible and effective. It is easy to train and fast to search. It effortlessly supports complex search spaces (e.g., building blocks, channel, mixed-precision quantization) and different search constraints (e.g., FLOPs, latency). It is thus convenient to use for various needs. It achieves start-of-the-art performance on the large dataset ImageNet.

</details>

### GroSS: Group-Size Series Decomposition for Grouped Architecture Search.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58574-7_2) · 📚 被引 0
- **作者**: Henry Howard-Jenkins, Yiwen Li, Victor Adrian Prisacariu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### NAS-Count: Counting-by-Density with Neural Architecture Search.
- **链接**: [arXiv:2003.00217](https://arxiv.org/abs/2003.00217) · 📚 被引 87
- **作者**: Yutao Hu, Xiaolong Jiang, Xuhui Liu, Baochang Zhang, Jungong Han, Xianbin Cao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Most of the recent advances in crowd counting have evolved from hand-designed density estimation networks, where multi-scale features are leveraged to address the scale variation problem, but at the expense of demanding design efforts. In this work, we automate the design of counting models with Neural Architecture Search (NAS) and introduce an end-to-end searched encoder-decoder architecture, Automatic Multi-Scale Network (AMSNet). Specifically, we utilize a counting-specific two-level search space. The encoder and decoder in AMSNet are composed of different cells discovered from micro-level search, while the multi-path architecture is explored through macro-level search. To solve the pixel-level isolation issue in MSE loss, AMSNet is optimized with an auto-searched Scale Pyramid Pooling Loss (SPPLoss) that supervises the multi-scale structural information. Extensive experiments on four datasets show AMSNet produces state-of-the-art results that outperform hand-designed models, fully demonstrating the efficacy of NAS-Count.

</details>

### Are Labels Necessary for Neural Architecture Search?
- **链接**: [arXiv:2003.12056](https://arxiv.org/abs/2003.12056)
- **作者**: Chenxi Liu, Piotr Dollár, Kaiming He, Ross B. Girshick, Alan L. Yuille, Saining Xie
- **🏷️ 机构**: Meta FAIR, MIT
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing neural network architectures in computer vision -- whether designed by humans or by machines -- were typically found using both images and their associated labels. In this paper, we ask the question: can we find high-quality neural architectures using only images, but no human-annotated labels? To answer this question, we first define a new setup called Unsupervised Neural Architecture Search (UnNAS). We then conduct two sets of experiments. In sample-based experiments, we train a large number (500) of diverse architectures with either supervised or unsupervised objectives, and find that the architecture rankings produced with and without labels are highly correlated. In search-based experiments, we run a well-established NAS algorithm (DARTS) using various unsupervised objectives, and report that the architectures searched without labels can be competitive to their counterparts searched with labels. Together, these results reveal the potentially surprising finding that labels are not necessary, and the image statistics alone may be sufficient to identify good neural architectures.

</details>

### NSGANetV2: Evolutionary Multi-objective Surrogate-Assisted Neural Architecture Search.
- **链接**: [arXiv:2007.10396](https://arxiv.org/abs/2007.10396) · [代码](https://github.com/mikelzc1990/nsganetv2) · 📚 被引 140
- **作者**: Zhichao Lu, Kalyanmoy Deb, Erik D. Goodman, Wolfgang Banzhaf, Vishnu Naresh Boddeti
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we propose an efficient NAS algorithm for generating task-specific models that are competitive under multiple competing objectives. It comprises of two surrogates, one at the architecture level to improve sample efficiency and one at the weights level, through a supernet, to improve gradient descent training efficiency. On standard benchmark datasets (C10, C100, ImageNet), the resulting models, dubbed NSGANetV2, either match or outperform models from existing approaches with the search being orders of magnitude more sample efficient. Furthermore, we demonstrate the effectiveness and versatility of the proposed method on six diverse non-standard datasets, e.g. STL-10, Flowers102, Oxford Pets, FGVC Aircrafts etc. In all cases, NSGANetV2s improve the state-of-the-art (under mobile setting), suggesting that NAS can be a viable alternative to conventional transfer learning approaches in handling diverse scenarios such as small-scale or fine-grained datasets. Code is available at https://github.com/mikelzc1990/nsganetv2

</details>

### Off-Policy Reinforcement Learning for Efficient and Effective GAN Architecture Search.
- **链接**: [arXiv:2007.09180](https://arxiv.org/abs/2007.09180) · [代码](https://github.com/Yuantian013/E2GAN) · 📚 被引 43
- **作者**: Yuan Tian, Qin Wang, Zhiwu Huang, Wen Li, Dengxin Dai, Minghao Yang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we introduce a new reinforcement learning (RL) based neural architecture search (NAS) methodology for effective and efficient generative adversarial network (GAN) architecture search. The key idea is to formulate the GAN architecture search problem as a Markov decision process (MDP) for smoother architecture sampling, which enables a more effective RL-based search algorithm by targeting the potential global optimal architecture. To improve efficiency, we exploit an off-policy GAN architecture search algorithm that makes efficient use of the samples generated by previous policies. Evaluation on two standard benchmark datasets (i.e., CIFAR-10 and STL-10) demonstrates that the proposed method is able to discover highly competitive architectures for generally better image generation results with a considerably reduced computational burden: 7 GPU hours. Our code is available at https://github.com/Yuantian013/E2GAN.

</details>

### Neural Predictor for Neural Architecture Search.
- **链接**: [arXiv:1912.00848](https://arxiv.org/abs/1912.00848)
- **作者**: Wei Wen, Hanxiao Liu, Yiran Chen, Hai Helen Li, Gabriel Bender, Pieter-Jan Kindermans
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural Architecture Search methods are effective but often use complex algorithms to come up with the best architecture. We propose an approach with three basic steps that is conceptually much simpler. First we train N random architectures to generate N (architecture, validation accuracy) pairs and use them to train a regression model that predicts accuracy based on the architecture. Next, we use this regression model to predict the validation accuracies of a large number of random architectures. Finally, we train the top-K predicted architectures and deploy the model with the best validation result. While this approach seems simple, it is more than 20 times as sample efficient as Regularized Evolution on the NASBench-101 benchmark and can compete on ImageNet with more complex approaches based on weight sharing, such as ProxylessNAS.

</details>

### CurveLane-NAS: Unifying Lane-Sensitive Architecture Search and Adaptive Point Blending.
- **链接**: [arXiv:2007.12147](https://arxiv.org/abs/2007.12147) · [代码](https://github.com/xbjxh/CurveLanes) · 📚 被引 191
- **作者**: Hang Xu, Shaoju Wang, Xinyue Cai, Wei Zhang, Xiaodan Liang, Zhenguo Li
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We address the curve lane detection problem which poses more realistic challenges than conventional lane detection for better facilitating modern assisted/autonomous driving systems. Current hand-designed lane detection methods are not robust enough to capture the curve lanes especially the remote parts due to the lack of modeling both long-range contextual information and detailed curve trajectory. In this paper, we propose a novel lane-sensitive architecture search framework named CurveLane-NAS to automatically capture both long-ranged coherent and accurate short-range curve information while unifying both architecture search and post-processing on curve lane predictions via point blending. It consists of three search modules: a) a feature fusion search module to find a better fusion of the local and global context for multi-level hierarchy features; b) an elastic backbone search module to explore an efficient feature extractor with good semantics and latency; c) an adaptive point blending module to search a multi-level post-processing refinement strategy to combine multi-scale head prediction. The unified framework ensures lane-sensitive predictions by the mutual guidance between NAS and adaptive point blending. Furthermore, we also steer forward to release a more challenging benchmark named CurveLanes for addressing the most difficult curve lanes. It consists of 150K images with 680K labels.The new dataset can be downloaded at github.com/xbjxh/CurveLanes (already anonymized for this submission). Experiments on the new CurveLanes show that the SOTA lane detection methods suffer substantial performance drop while our model can still reach an 80+% F1-score. Extensive experiments on traditional lane benchmarks such as CULane also demonstrate the superiority of our CurveLane-NAS, e.g. achieving a new SOTA 74.8% F1-score on CULane.

</details>

### BigNAS: Scaling up Neural Architecture Search with Big Single-Stage Models.
- **链接**: [arXiv:2003.11142](https://arxiv.org/abs/2003.11142) · 📚 被引 148
- **作者**: Jiahui Yu, Pengchong Jin, Hanxiao Liu, Gabriel Bender, Pieter-Jan Kindermans, Mingxing Tan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural architecture search (NAS) has shown promising results discovering models that are both accurate and fast. For NAS, training a one-shot model has become a popular strategy to rank the relative quality of different architectures (child models) using a single set of shared weights. However, while one-shot model weights can effectively rank different network architectures, the absolute accuracies from these shared weights are typically far below those obtained from stand-alone training. To compensate, existing methods assume that the weights must be retrained, finetuned, or otherwise post-processed after the search is completed. These steps significantly increase the compute requirements and complexity of the architecture search and model deployment. In this work, we propose BigNAS, an approach that challenges the conventional wisdom that post-processing of the weights is necessary to get good prediction accuracies. Without extra retraining or post-processing steps, we are able to train a single set of shared weights on ImageNet and use these weights to obtain child models whose sizes range from 200 to 1000 MFLOPs. Our discovered model family, BigNASModels, achieve top-1 accuracies ranging from 76.5% to 80.9%, surpassing state-of-the-art models in this range including EfficientNets and Once-for-All networks without extra retraining or post-processing. We present ablative study and analysis to further understand the proposed BigNASModels.

</details>

### S2DNAS: Transforming Static CNN Model for Dynamic Inference via Neural Architecture Search.
- **链接**: [arXiv:1911.07033](https://arxiv.org/abs/1911.07033) · 📚 被引 22
- **作者**: Zhihang Yuan, Bingzhe Wu, Guangyu Sun, Zheng Liang, Shiwan Zhao, Weichen Bi
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, dynamic inference has emerged as a promising way to reduce the computational cost of deep convolutional neural network (CNN). In contrast to static methods (e.g. weight pruning), dynamic inference adaptively adjusts the inference process according to each input sample, which can considerably reduce the computational cost on "easy" samples while maintaining the overall model performance. In this paper, we introduce a general framework, S2DNAS, which can transform various static CNN models to support dynamic inference via neural architecture search. To this end, based on a given CNN model, we first generate a CNN architecture space in which each architecture is a multi-stage CNN generated from the given model using some predefined transformations. Then, we propose a reinforcement learning based approach to automatically search for the optimal CNN architecture in the generated space. At last, with the searched multi-stage network, we can perform dynamic inference by adaptively choosing a stage to evaluate for each sample. Unlike previous works that introduce irregular computations or complex controllers in the inference or re-design a CNN model from scratch, our method can generalize to most of the popular CNN architectures and the searched dynamic network can be directly deployed using existing deep learning frameworks in various hardware devices.

</details>

## 跨领域论文（完整笔记在其他领域）

- Towards Part-Aware Monocular 3D Human Pose Estimation: An Architecture Search Approach. → [3d-detection](../3d-detection/Guideline%202020.md)
- DA-NAS: Data Adapted Pruning for Efficient Neural Architecture Search. → [network-pruning](../network-pruning/Guideline%202020.md)
