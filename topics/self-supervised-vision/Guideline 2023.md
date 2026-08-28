# Self-supervised Vision — 2023 Guideline

> 领域: 视觉自监督学习（对比学习、MAE、DINO 系）
> 论文数: 30 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### A Closer Look at Self-Supervised Lightweight Vision Transformers.
- **链接**: [arXiv:2205.14443](https://arxiv.org/abs/2205.14443) · [代码](https://github.com/wangsr126/mae-lite)
- **作者**: Shaoru Wang, Jin Gao, Zeming Li, Xiaoqin Zhang, Weiming Hu
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning on large-scale Vision Transformers (ViTs) as pre-training methods has achieved promising downstream performance. Yet, how much these pre-training paradigms promote lightweight ViTs' performance is considerably less studied. In this work, we develop and benchmark several self-supervised pre-training methods on image classification tasks and some downstream dense prediction tasks. We surprisingly find that if proper pre-training is adopted, even vanilla lightweight ViTs show comparable performance to previous SOTA networks with delicate architecture design. It breaks the recently popular conception that vanilla ViTs are not suitable for vision tasks in lightweight regimes. We also point out some defects of such pre-training, e.g., failing to benefit from large-scale pre-training data and showing inferior performance on data-insufficient downstream tasks. Furthermore, we analyze and clearly show the effect of such pre-training by analyzing the properties of the layer representation and attention maps for related models. Finally, based on the above analyses, a distillation strategy during pre-training is developed, which leads to further downstream performance improvement for MAE-based pre-training. Code is available at https://github.com/wangsr126/mae-lite.

</details>

### Improving Visual Prompt Tuning for Self-supervised Vision Transformers.
- **链接**: [arXiv:2306.05067](https://arxiv.org/abs/2306.05067) · [代码](https://github.com/ryongithub/GatedPromptTuning)
- **作者**: Seungryong Yoo, Eunji Kim, Dahuin Jung, Jungbeom Lee, Sungroh Yoon
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Visual Prompt Tuning (VPT) is an effective tuning method for adapting pretrained Vision Transformers (ViTs) to downstream tasks. It leverages extra learnable tokens, known as prompts, which steer the frozen pretrained ViTs. Although VPT has demonstrated its applicability with supervised vision transformers, it often underperforms with self-supervised ones. Through empirical observations, we deduce that the effectiveness of VPT hinges largely on the ViT blocks with which the prompt tokens interact. Specifically, VPT shows improved performance on image classification tasks for MAE and MoCo v3 when the prompt tokens are inserted into later blocks rather than the first block. These observations suggest that there exists an optimal location of blocks for the insertion of prompt tokens. Unfortunately, identifying the optimal blocks for prompts within each self-supervised ViT for diverse future scenarios is a costly process. To mitigate this problem, we propose a simple yet effective method that learns a gate for each ViT block to adjust its intervention into the prompt tokens. With our method, prompt tokens are selectively influenced by blocks that require steering for task adaptation. Our method outperforms VPT variants in FGVC and VTAB image classification and ADE20K semantic segmentation. The code is available at https://github.com/ryongithub/GatedPromptTuning.

</details>

### Data-Efficient Contrastive Self-supervised Learning: Most Beneficial Examples for Supervised Learning Contribute the Least.
- **链接**: [出版页](https://proceedings.mlr.press/v202/joshi23b.html)
- **作者**: Siddharth Joshi, Baharan Mirzasoleiman
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Self-supervised Neural Factor Analysis for Disentangling Utterance-level Speech Representations.
- **链接**: [arXiv:2305.08099](https://arxiv.org/abs/2305.08099)
- **作者**: Weiwei Lin, Chenhang He, Man-Wai Mak, Youzhi Tu
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning (SSL) speech models such as wav2vec and HuBERT have demonstrated state-of-the-art performance on automatic speech recognition (ASR) and proved to be extremely useful in low label-resource settings. However, the success of SSL models has yet to transfer to utterance-level tasks such as speaker, emotion, and language recognition, which still require supervised fine-tuning of the SSL models to obtain good performance. We argue that the problem is caused by the lack of disentangled representations and an utterance-level learning objective for these tasks. Inspired by how HuBERT uses clustering to discover hidden acoustic units, we formulate a factor analysis (FA) model that uses the discovered hidden acoustic units to align the SSL features. The underlying utterance-level representations are disentangled from the content of speech using probabilistic inference on the aligned features. Furthermore, the variational lower bound derived from the FA model provides an utterance-level objective, allowing error gradients to be backpropagated to the Transformer layers to learn highly discriminative acoustic units. When used in conjunction with HuBERT's masked prediction training, our models outperform the current best model, WavLM, on all utterance-level non-semantic tasks on the SUPERB benchmark with only 20% of labeled data.

</details>

### Efficient Self-supervised Learning with Contextualized Target Representations for Vision, Speech and Language.
- **链接**: [arXiv:2212.07525](https://arxiv.org/abs/2212.07525)
- **作者**: Alexei Baevski, Arun Babu, Wei-Ning Hsu, Michael Auli
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Current self-supervised learning algorithms are often modality-specific and require large amounts of computational resources. To address these issues, we increase the training efficiency of data2vec, a learning objective that generalizes across several modalities. We do not encode masked tokens, use a fast convolutional decoder and amortize the effort to build teacher representations. data2vec 2.0 benefits from the rich contextualized target representations introduced in data2vec which enable a fast self-supervised learner. Experiments on ImageNet-1K image classification show that data2vec 2.0 matches the accuracy of Masked Autoencoders in 16.4x lower pre-training time, on Librispeech speech recognition it performs as well as wav2vec 2.0 in 10.6x less time, and on GLUE natural language understanding it matches a retrained RoBERTa model in half the time. Trading some speed for accuracy results in ImageNet-1K top-1 accuracy of 86.8\% with a ViT-L model trained for 150 epochs.

</details>

### Evaluating Self-Supervised Learning via Risk Decomposition.
- **链接**: [arXiv:2302.03068](https://arxiv.org/abs/2302.03068) · [代码](https://github.com/YannDubs/SSL-Risk-Decomposition)
- **作者**: Yann Dubois, Tatsunori Hashimoto, Percy Liang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning (SSL) pipelines differ in many design choices such as the architecture, augmentations, or pretraining data. Yet SSL is typically evaluated using a single metric: linear probing on ImageNet. This does not provide much insight into why or when a model is better, now how to improve it. To address this, we propose an SSL risk decomposition, which generalizes the classical supervised approximation-estimation decomposition by considering errors arising from the representation learning step. Our decomposition consists of four error components: approximation, representation usability, probe generalization, and encoder generalization. We provide efficient estimators for each component and use them to analyze the effect of 30 design choices on 169 SSL vision models evaluated on ImageNet. Our analysis gives valuable insights for designing and using SSL models. For example, it highlights the main sources of error and shows how to improve SSL in specific settings (full- vs few-shot) by trading off error components. All results and pretrained models are at https://github.com/YannDubs/SSL-Risk-Decomposition.

</details>

### RankMe: Assessing the Downstream Performance of Pretrained Self-Supervised Representations by Their Rank.
- **链接**: [arXiv:2210.02885](https://arxiv.org/abs/2210.02885)
- **作者**: Quentin Garrido, Randall Balestriero, Laurent Najman, Yann LeCun
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Joint-Embedding Self Supervised Learning (JE-SSL) has seen a rapid development, with the emergence of many method variations but only few principled guidelines that would help practitioners to successfully deploy them. The main reason for that pitfall comes from JE-SSL's core principle of not employing any input reconstruction therefore lacking visual cues of unsuccessful training. Adding non informative loss values to that, it becomes difficult to deploy SSL on a new dataset for which no labels can help to judge the quality of the learned representation. In this study, we develop a simple unsupervised criterion that is indicative of the quality of the learned JE-SSL representations: their effective rank. Albeit simple and computationally friendly, this method -- coined RankMe -- allows one to assess the performance of JE-SSL representations, even on different downstream datasets, without requiring any labels. A further benefit of RankMe is that it does not have any training or hyper-parameters to tune. Through thorough empirical experiments involving hundreds of training episodes, we demonstrate how RankMe can be used for hyperparameter selection with nearly no reduction in final performance compared to the current selection method that involve a dataset's labels. We hope that RankMe will facilitate the deployment of JE-SSL towards domains that do not have the opportunity to rely on labels for representations' quality assessment.

</details>

### Self-supervised learning of Split Invariant Equivariant representations.
- **链接**: [出版页](https://proceedings.mlr.press/v202/garrido23b.html)
- **作者**: Quentin Garrido, Laurent Najman, Yann LeCun
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### CSP: Self-Supervised Contrastive Spatial Pre-Training for Geospatial-Visual Representations.
- **链接**: [出版页](https://proceedings.mlr.press/v202/mai23a.html)
- **作者**: Gengchen Mai, Ni Lao, Yutong He, Jiaming Song, Stefano Ermon
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Not All Semantics are Created Equal: Contrastive Self-supervised Learning with Automatic Temperature Individualization.
- **链接**: [arXiv:2305.11965](https://arxiv.org/abs/2305.11965)
- **作者**: Zi-Hao Qiu, Quanqi Hu, Zhuoning Yuan, Denny Zhou, Lijun Zhang, Tianbao Yang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we aim to optimize a contrastive loss with individualized temperatures in a principled and systematic manner for self-supervised learning. The common practice of using a global temperature parameter $τ$ ignores the fact that ``not all semantics are created equal", meaning that different anchor data may have different numbers of samples with similar semantics, especially when data exhibits long-tails. First, we propose a new robust contrastive loss inspired by distributionally robust optimization (DRO), providing us an intuition about the effect of $τ$ and a mechanism for automatic temperature individualization. Then, we propose an efficient stochastic algorithm for optimizing the robust contrastive loss with a provable convergence guarantee without using large mini-batch sizes. Theoretical and experimental results show that our algorithm automatically learns a suitable $τ$ for each sample. Specifically, samples with frequent semantics use large temperatures to keep local semantic structures, while samples with rare semantics use small temperatures to induce more separable features. Our method not only outperforms prior strong baselines (e.g., SimCLR, CLIP) on unimodal and bimodal datasets with larger improvements on imbalanced data but also is less sensitive to hyper-parameters. To our best knowledge, this is the first methodical approach to optimizing a contrastive loss with individualized temperatures.

</details>

### Sequential Multi-Dimensional Self-Supervised Learning for Clinical Time Series.
- **链接**: [arXiv:2307.10923](https://arxiv.org/abs/2307.10923)
- **作者**: Aniruddh Raghu, Payal Chandak, Ridwan Alam, John V. Guttag, Collin M. Stultz
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning (SSL) for clinical time series data has received significant attention in recent literature, since these data are highly rich and provide important information about a patient's physiological state. However, most existing SSL methods for clinical time series are limited in that they are designed for unimodal time series, such as a sequence of structured features (e.g., lab values and vitals signs) or an individual high-dimensional physiological signal (e.g., an electrocardiogram). These existing methods cannot be readily extended to model time series that exhibit multimodality, with structured features and high-dimensional data being recorded at each timestep in the sequence. In this work, we address this gap and propose a new SSL method -- Sequential Multi-Dimensional SSL -- where a SSL loss is applied both at the level of the entire sequence and at the level of the individual high-dimensional data points in the sequence in order to better capture information at both scales. Our strategy is agnostic to the specific form of loss function used at each level -- it can be contrastive, as in SimCLR, or non-contrastive, as in VICReg. We evaluate our method on two real-world clinical datasets, where the time series contains sequences of (1) high-frequency electrocardiograms and (2) structured data from lab values and vitals signs. Our experimental results indicate that pre-training with our method and then fine-tuning on downstream tasks improves performance over baselines on both datasets, and in several settings, can lead to improvements across different self-supervised loss functions.

</details>

### On the Stepwise Nature of Self-Supervised Learning.
- **链接**: [arXiv:2303.15438](https://arxiv.org/abs/2303.15438)
- **作者**: James B. Simon, Maksis Knutins, Liu Ziyin, Daniel Geisz, Abraham J. Fetterman, Joshua Albrecht
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a simple picture of the training process of joint embedding self-supervised learning methods. We find that these methods learn their high-dimensional embeddings one dimension at a time in a sequence of discrete, well-separated steps. We arrive at this conclusion via the study of a linearized model of Barlow Twins applicable to the case in which the trained network is infinitely wide. We solve the training dynamics of this model from small initialization, finding that the model learns the top eigenmodes of a certain contrastive kernel in a stepwise fashion, and obtain a closed-form expression for the final learned representations. Remarkably, we then see the same stepwise learning phenomenon when training deep ResNets using the Barlow Twins, SimCLR, and VICReg losses. Our theory suggests that, just as kernel regression can be thought of as a model of supervised learning, kernel PCA may serve as a useful model of self-supervised learning.

</details>

### Boosting Graph Contrastive Learning via Graph Contrastive Saliency.
- **链接**: [出版页](https://proceedings.mlr.press/v202/wei23c.html)
- **作者**: Chunyu Wei, Yu Wang, Bing Bai, Kai Ni, David Brady, Lu Fang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Rethinking Weak Supervision in Helping Contrastive Learning.
- **链接**: [arXiv:2306.04160](https://arxiv.org/abs/2306.04160)
- **作者**: Jingyi Cui, Weiran Huang, Yifei Wang, Yisen Wang
- **🏷️ 机构**: Peking University
- **会议**: ICML 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Contrastive learning has shown outstanding performances in both supervised and unsupervised learning, and has recently been introduced to solve weakly supervised learning problems such as semi-supervised learning and noisy label learning. Despite the empirical evidence showing that semi-supervised labels improve the representations of contrastive learning, it remains unknown if noisy supervised information can be directly used in training instead of after manual denoising. Therefore, to explore the mechanical differences between semi-supervised and noisy-labeled information in helping contrastive learning, we establish a unified theoretical framework of contrastive learning under weak supervision. Specifically, we investigate the most intuitive paradigm of jointly training supervised and unsupervised contrastive losses. By translating the weakly supervised information into a similarity graph under the framework of spectral clustering based on the posterior probability of weak labels, we establish the downstream classification error bound. We prove that semi-supervised labels improve the downstream error bound whereas noisy labels have limited effects under such a paradigm. Our theoretical findings here provide new insights for the community to rethink the role of weak supervision in helping contrastive learning.

</details>

### Integrating Prior Knowledge in Contrastive Learning with Kernel.
- **链接**: [出版页](https://proceedings.mlr.press/v202/dufumier23a.html)
- **作者**: Benoit Dufumier, Carlo Alberto Barbano, Robin Louiset, Edouard Duchesnay, Pietro Gori
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Contrastive Learning Meets Homophily: Two Birds with One Stone.
- **链接**: [出版页](https://proceedings.mlr.press/v202/he23c.html)
- **作者**: Dongxiao He, Jitao Zhao, Rui Guo, Zhiyong Feng, Di Jin, Yuxiao Huang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Model-Aware Contrastive Learning: Towards Escaping the Dilemmas.
- **链接**: [出版页](https://proceedings.mlr.press/v202/huang23c.html)
- **作者**: Zizheng Huang, Haoxing Chen, Ziqi Wen, Chao Zhang, Huaxiong Li, Bo Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Searching Large Neighborhoods for Integer Linear Programs with Contrastive Learning.
- **链接**: [arXiv:2302.01578](https://arxiv.org/abs/2302.01578)
- **作者**: Taoan Huang, Aaron M. Ferber, Yuandong Tian, Bistra Dilkina, Benoit Steiner
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Integer Linear Programs (ILPs) are powerful tools for modeling and solving a large number of combinatorial optimization problems. Recently, it has been shown that Large Neighborhood Search (LNS), as a heuristic algorithm, can find high quality solutions to ILPs faster than Branch and Bound. However, how to find the right heuristics to maximize the performance of LNS remains an open problem. In this paper, we propose a novel approach, CL-LNS, that delivers state-of-the-art anytime performance on several ILP benchmarks measured by metrics including the primal gap, the primal integral, survival rates and the best performing rate. Specifically, CL-LNS collects positive and negative solution samples from an expert heuristic that is slow to compute and learns a new one with a contrastive loss. We use graph attention networks and a richer set of features to further improve its performance.

</details>

### SOM-CPC: Unsupervised Contrastive Learning with Self-Organizing Maps for Structured Representations of High-Rate Time Series.
- **链接**: [arXiv:2205.15875](https://arxiv.org/abs/2205.15875)
- **作者**: Iris A. M. Huijben, Arthur Andreas Nijdam, Sebastiaan Overeem, Merel M. van Gilst, Ruud van Sloun
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continuous monitoring with an ever-increasing number of sensors has become ubiquitous across many application domains. However, acquired time series are typically high-dimensional and difficult to interpret. Expressive deep learning (DL) models have gained popularity for dimensionality reduction, but the resulting latent space often remains difficult to interpret. In this work we propose SOM-CPC, a model that visualizes data in an organized 2D manifold, while preserving higher-dimensional information. We address a largely unexplored and challenging set of scenarios comprising high-rate time series, and show on both synthetic and real-life data (physiological data and audio recordings) that SOM-CPC outperforms strong baselines like DL-based feature extraction, followed by conventional dimensionality reduction techniques, and models that jointly optimize a DL model and a Self-Organizing Map (SOM). SOM-CPC has great potential to acquire a better understanding of latent patterns in high-rate data streams.

</details>

### Probabilistic Contrastive Learning Recovers the Correct Aleatoric Uncertainty of Ambiguous Inputs.
- **链接**: [arXiv:2302.02865](https://arxiv.org/abs/2302.02865) · [代码](https://github.com/mkirchhof/Probabilistic_Contrastive_Learning)
- **作者**: Michael Kirchhof, Enkelejda Kasneci, Seong Joon Oh
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Contrastively trained encoders have recently been proven to invert the data-generating process: they encode each input, e.g., an image, into the true latent vector that generated the image (Zimmermann et al., 2021). However, real-world observations often have inherent ambiguities. For instance, images may be blurred or only show a 2D view of a 3D object, so multiple latents could have generated them. This makes the true posterior for the latent vector probabilistic with heteroscedastic uncertainty. In this setup, we extend the common InfoNCE objective and encoders to predict latent distributions instead of points. We prove that these distributions recover the correct posteriors of the data-generating process, including its level of aleatoric uncertainty, up to a rotation of the latent space. In addition to providing calibrated uncertainty estimates, these posteriors allow the computation of credible intervals in image retrieval. They comprise images with the same latent as a given query, subject to its uncertainty. Code is available at https://github.com/mkirchhof/Probabilistic_Contrastive_Learning

</details>

### Randomized Schur Complement Views for Graph Contrastive Learning.
- **链接**: [arXiv:2306.04004](https://arxiv.org/abs/2306.04004)
- **作者**: Vignesh Kothapalli
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce a randomized topological augmentor based on Schur complements for Graph Contrastive Learning (GCL). Given a graph laplacian matrix, the technique generates unbiased approximations of its Schur complements and treats the corresponding graphs as augmented views. We discuss the benefits of our approach, provide theoretical justifications and present connections with graph diffusion. Unlike previous efforts, we study the empirical effectiveness of the augmentor in a controlled fashion by varying the design choices for subsequent GCL phases, such as encoding and contrasting. Extensive experiments on node and graph classification benchmarks demonstrate that our technique consistently outperforms pre-defined and adaptive augmentation approaches to achieve state-of-the-art results.

</details>

### Understanding and Generalizing Contrastive Learning from the Inverse Optimal Transport Perspective.
- **链接**: [出版页](https://proceedings.mlr.press/v202/shi23j.html)
- **作者**: Liangliang Shi, Gu Zhang, Haoyu Zhen, Jintao Fan, Junchi Yan
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Flexible Phase Dynamics for Bio-Plausible Contrastive Learning.
- **链接**: [arXiv:2302.12431](https://arxiv.org/abs/2302.12431)
- **作者**: Ezekiel Williams, Colin Bredenberg, Guillaume Lajoie
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Many learning algorithms used as normative models in neuroscience or as candidate approaches for learning on neuromorphic chips learn by contrasting one set of network states with another. These Contrastive Learning (CL) algorithms are traditionally implemented with rigid, temporally non-local, and periodic learning dynamics that could limit the range of physical systems capable of harnessing CL. In this study, we build on recent work exploring how CL might be implemented by biological or neurmorphic systems and show that this form of learning can be made temporally local, and can still function even if many of the dynamical requirements of standard training procedures are relaxed. Thanks to a set of general theorems corroborated by numerical experiments across several CL models, our results provide theoretical foundations for the study and development of CL methods for biological and neuromorphic neural networks.

</details>

### SEGA: Structural Entropy Guided Anchor View for Graph Contrastive Learning.
- **链接**: [arXiv:2305.04501](https://arxiv.org/abs/2305.04501)
- **作者**: Junran Wu, Xueyuan Chen, Bowen Shi, Shangzhe Li, Ke Xu
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In contrastive learning, the choice of ``view'' controls the information that the representation captures and influences the performance of the model. However, leading graph contrastive learning methods generally produce views via random corruption or learning, which could lead to the loss of essential information and alteration of semantic information. An anchor view that maintains the essential information of input graphs for contrastive learning has been hardly investigated. In this paper, based on the theory of graph information bottleneck, we deduce the definition of this anchor view; put differently, \textit{the anchor view with essential information of input graph is supposed to have the minimal structural uncertainty}. Furthermore, guided by structural entropy, we implement the anchor view, termed \textbf{SEGA}, for graph contrastive learning. We extensively validate the proposed anchor view on various benchmarks regarding graph classification under unsupervised, semi-supervised, and transfer learning and achieve significant performance boosts compared to the state-of-the-art methods.

</details>

### Which Features are Learnt by Contrastive Learning? On the Role of Simplicity Bias in Class Collapse and Feature Suppression.
- **链接**: [arXiv:2305.16536](https://arxiv.org/abs/2305.16536)
- **作者**: Yihao Xue, Siddharth Joshi, Eric Gan, Pin-Yu Chen, Baharan Mirzasoleiman
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Contrastive learning (CL) has emerged as a powerful technique for representation learning, with or without label supervision. However, supervised CL is prone to collapsing representations of subclasses within a class by not capturing all their features, and unsupervised CL may suppress harder class-relevant features by focusing on learning easy class-irrelevant features; both significantly compromise representation quality. Yet, there is no theoretical understanding of \textit{class collapse} or \textit{feature suppression} at \textit{test} time. We provide the first unified theoretically rigorous framework to determine \textit{which} features are learnt by CL. Our analysis indicate that, perhaps surprisingly, bias of (stochastic) gradient descent towards finding simpler solutions is a key factor in collapsing subclass representations and suppressing harder class-relevant features. Moreover, we present increasing embedding dimensionality and improving the quality of data augmentations as two theoretically motivated solutions to {feature suppression}. We also provide the first theoretical explanation for why employing supervised and unsupervised CL together yields higher-quality representations, even when using commonly-used stochastic gradient methods.

</details>

### Behavior Contrastive Learning for Unsupervised Skill Discovery.
- **链接**: [arXiv:2305.04477](https://arxiv.org/abs/2305.04477)
- **作者**: Rushuai Yang, Chenjia Bai, Hongyi Guo, Siyuan Li, Bin Zhao, Zhen Wang et al.
- **🏷️ 机构**: Shanghai University,Shanghai,China,200444
- **会议**: ICML 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In reinforcement learning, unsupervised skill discovery aims to learn diverse skills without extrinsic rewards. Previous methods discover skills by maximizing the mutual information (MI) between states and skills. However, such an MI objective tends to learn simple and static skills and may hinder exploration. In this paper, we propose a novel unsupervised skill discovery method through contrastive learning among behaviors, which makes the agent produce similar behaviors for the same skill and diverse behaviors for different skills. Under mild assumptions, our objective maximizes the MI between different behaviors based on the same skill, which serves as an upper bound of the previous MI objective. Meanwhile, our method implicitly increases the state entropy to obtain better state coverage. We evaluate our method on challenging mazes and continuous control tasks. The results show that our method generates diverse and far-reaching skills, and also obtains competitive performance in downstream tasks compared to the state-of-the-art methods.

</details>

### ConCerNet: A Contrastive Learning Based Framework for Automated Conservation Law Discovery and Trustworthy Dynamical System Prediction.
- **链接**: [arXiv:2302.05783](https://arxiv.org/abs/2302.05783)
- **作者**: Wang Zhang, Tsui-Wei Weng, Subhro Das, Alexandre Megretski, Luca Daniel, Lam M. Nguyen
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep neural networks (DNN) have shown great capacity of modeling a dynamical system; nevertheless, they usually do not obey physics constraints such as conservation laws. This paper proposes a new learning framework named ConCerNet to improve the trustworthiness of the DNN based dynamics modeling to endow the invariant properties. ConCerNet consists of two steps: (i) a contrastive learning method to automatically capture the system invariants (i.e. conservation properties) along the trajectory observations; (ii) a neural projection layer to guarantee that the learned dynamics models preserve the learned invariants. We theoretically prove the functional relationship between the learned latent representation and the unknown system invariant function. Experiments show that our method consistently outperforms the baseline neural networks in both coordinate error and conservation metrics by a large margin. With neural network based parameterization and no dependence on prior knowledge, our method can be extended to complex and large-scale dynamics by leveraging an autoencoder.

</details>

### Patch-level Contrastive Learning via Positional Query for Visual Pre-training.
- **链接**: [出版页](https://proceedings.mlr.press/v202/zhang23bd.html)
- **作者**: Shaofeng Zhang, Qiang Zhou, Zhibin Wang, Fan Wang, Junchi Yan
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

## 跨领域论文（完整笔记在其他领域）

- The Role of Entropy and Reconstruction in Multi-View Self-Supervised Learning. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- On the Generalization of Multi-modal Contrastive Learning. → [multimodal](../multimodal/Guideline%202023.md)
