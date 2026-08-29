# Self-supervised Vision — 2025 Guideline

> 领域: 视觉自监督学习（对比学习、MAE、DINO 系）
> 论文数: 42 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### A Theoretical Analysis of Self-Supervised Learning for Vision Transformers.
- **链接**: [出版页](https://openreview.net/forum?id=Antib6Uovh)
- **作者**: Yu Huang, Zixin Wen, Yuejie Chi, Yingbin Liang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Predicting the Energy Landscape of Stochastic Dynamical System via Physics-informed Self-supervised Learning.
- **链接**: [arXiv:2502.16828](https://arxiv.org/abs/2502.16828) · [代码](https://github.com/tsinghua-fib-lab/PESLA)
- **作者**: Ruikun Li, Huandong Wang, Qingmin Liao, Yong Li
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Energy landscapes play a crucial role in shaping dynamics of many real-world complex systems. System evolution is often modeled as particles moving on a landscape under the combined effect of energy-driven drift and noise-induced diffusion, where the energy governs the long-term motion of the particles. Estimating the energy landscape of a system has been a longstanding interdisciplinary challenge, hindered by the high operational costs or the difficulty of obtaining supervisory signals. Therefore, the question of how to infer the energy landscape in the absence of true energy values is critical. In this paper, we propose a physics-informed self-supervised learning method to learn the energy landscape from the evolution trajectories of the system. It first maps the system state from the observation space to a discrete landscape space by an adaptive codebook, and then explicitly integrates energy into the graph neural Fokker-Planck equation, enabling the joint learning of energy estimation and evolution prediction. Experimental results across interdisciplinary systems demonstrate that our estimated energy has a correlation coefficient above 0.9 with the ground truth, and evolution prediction accuracy exceeds the baseline by an average of 17.65\%. The code is available at github.com/tsinghua-fib-lab/PESLA.

</details>

### Dataset Distillation via Knowledge Distillation: Towards Efficient Self-Supervised Pre-training of Deep Networks.
- **链接**: [arXiv:2410.02116](https://arxiv.org/abs/2410.02116) · [代码](https://github.com/BigML-CS-UCLA/MKDT)
- **作者**: Siddharth Joshi, Jiayi Ni, Baharan Mirzasoleiman
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Dataset distillation (DD) generates small synthetic datasets that can efficiently train deep networks with a limited amount of memory and compute. Despite the success of DD methods for supervised learning, DD for self-supervised pre-training of deep models has remained unaddressed. Pre-training on unlabeled data is crucial for efficiently generalizing to downstream tasks with limited labeled data. In this work, we propose the first effective DD method for SSL pre-training. First, we show, theoretically and empirically, that naive application of supervised DD methods to SSL fails, due to the high variance of the SSL gradient. Then, we address this issue by relying on insights from knowledge distillation (KD) literature. Specifically, we train a small student model to match the representations of a larger teacher model trained with SSL. Then, we generate a small synthetic dataset by matching the training trajectories of the student models. As the KD objective has considerably lower variance than SSL, our approach can generate synthetic datasets that can successfully pre-train high-quality encoders. Through extensive experiments, we show that our distilled sets lead to up to 13% higher accuracy than prior work, on a variety of downstream tasks, in the presence of limited labeled data. Code at https://github.com/BigML-CS-UCLA/MKDT.

</details>

### SSLAM: Enhancing Self-Supervised Models with Audio Mixtures for Polyphonic Soundscapes.
- **链接**: [arXiv:2506.12222](https://arxiv.org/abs/2506.12222)
- **作者**: Tony Alex, Sara Atito, Armin Mustafa, Muhammad Awais, Philip J. B. Jackson
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised pre-trained audio networks have seen widespread adoption in real-world systems, particularly in multi-modal large language models. These networks are often employed in a frozen state, under the assumption that the SSL pre-training has sufficiently equipped them to handle real-world audio. However, a critical question remains: how well do these models actually perform in real-world conditions, where audio is typically polyphonic and complex, involving multiple overlapping sound sources? Current audio SSL methods are often benchmarked on datasets predominantly featuring monophonic audio, such as environmental sounds, and speech. As a result, the ability of SSL models to generalize to polyphonic audio, a common characteristic in natural scenarios, remains underexplored. This limitation raises concerns about the practical robustness of SSL models in more realistic audio settings. To address this gap, we introduce Self-Supervised Learning from Audio Mixtures (SSLAM), a novel direction in audio SSL research, designed to improve, designed to improve the model's ability to learn from polyphonic data while maintaining strong performance on monophonic data. We thoroughly evaluate SSLAM on standard audio SSL benchmark datasets which are predominantly monophonic and conduct a comprehensive comparative analysis against SOTA methods using a range of high-quality, publicly available polyphonic datasets. SSLAM not only improves model performance on polyphonic audio, but also maintains or exceeds performance on standard audio SSL benchmarks. Notably, it achieves up to a 3.9\% improvement on the AudioSet-2M (AS-2M), reaching a mean average precision (mAP) of 50.2. For polyphonic datasets, SSLAM sets new SOTA in both linear evaluation and fine-tuning regimes with performance improvements of up to 9.1\% (mAP).

</details>

### Deconstructing Denoising Diffusion Models for Self-Supervised Learning.
- **链接**: [arXiv:2401.14404](https://arxiv.org/abs/2401.14404)
- **作者**: Xinlei Chen, Zhuang Liu, Saining Xie, Kaiming He
- **🏷️ 机构**: MIT
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this study, we examine the representation learning abilities of Denoising Diffusion Models (DDM) that were originally purposed for image generation. Our philosophy is to deconstruct a DDM, gradually transforming it into a classical Denoising Autoencoder (DAE). This deconstructive procedure allows us to explore how various components of modern DDMs influence self-supervised representation learning. We observe that only a very few modern components are critical for learning good representations, while many others are nonessential. Our study ultimately arrives at an approach that is highly simplified and to a large extent resembles a classical DAE. We hope our study will rekindle interest in a family of classical methods within the realm of modern self-supervised learning.

</details>

### ASTrA: Adversarial Self-supervised Training with Adaptive-Attacks.
- **链接**: [出版页](https://openreview.net/forum?id=ZbkqhKbggH)
- **作者**: Prakash Chandra Chhipa, Gautam Vashishtha, Settur Jithamanyu, Rajkumar Saini, Mubarak Shah, Marcus Liwicki
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### SCOPE: A Self-supervised Framework for Improving Faithfulness in Conditional Text Generation.
- **链接**: [arXiv:2502.13674](https://arxiv.org/abs/2502.13674)
- **作者**: Song Duong, Florian Le Bronnec, Alexandre Allauzen, Vincent Guigue, Alberto Lumbreras, Laure Soulier et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large Language Models (LLMs), when used for conditional text generation, often produce hallucinations, i.e., information that is unfaithful or not grounded in the input context. This issue arises in typical conditional text generation tasks, such as text summarization and data-to-text generation, where the goal is to produce fluent text based on contextual input. When fine-tuned on specific domains, LLMs struggle to provide faithful answers to a given context, often adding information or generating errors. One underlying cause of this issue is that LLMs rely on statistical patterns learned from their training data. This reliance can interfere with the model's ability to stay faithful to a provided context, leading to the generation of ungrounded information. We build upon this observation and introduce a novel self-supervised method for generating a training set of unfaithful samples. We then refine the model using a training process that encourages the generation of grounded outputs over unfaithful ones, drawing on preference-based training. Our approach leads to significantly more grounded text generation, outperforming existing self-supervised techniques in faithfulness, as evaluated through automatic metrics, LLM-based assessments, and human evaluations.

</details>

### SSOLE: Rethinking Orthogonal Low-rank Embedding for Self-Supervised Learning.
- **链接**: [出版页](https://openreview.net/forum?id=zBgiCWCxJB)
- **作者**: Lun Huang, Qiang Qiu, Guillermo Sapiro
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Self-supervised contrastive learning performs non-linear system identification.
- **链接**: [arXiv:2410.14673](https://arxiv.org/abs/2410.14673)
- **作者**: Rodrigo González Laiz, Tobias Schmidt, Steffen Schneider
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning (SSL) approaches have brought tremendous success across many tasks and domains. It has been argued that these successes can be attributed to a link between SSL and identifiable representation learning: Temporal structure and auxiliary variables ensure that latent representations are related to the true underlying generative factors of the data. Here, we deepen this connection and show that SSL can perform system identification in latent space. We propose dynamics contrastive learning, a framework to uncover linear, switching linear and non-linear dynamics under a non-linear observation model, give theoretical guarantees and validate them empirically.

</details>

### Frequency-Guided Masking for Enhanced Vision Self-Supervised Learning.
- **链接**: [arXiv:2409.10362](https://arxiv.org/abs/2409.10362)
- **作者**: Amin Karimi Monsefi, Mengxi Zhou, Nastaran Karimi Monsefi, Ser-Nam Lim, Wei-Lun Chao, Rajiv Ramnath
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a novel frequency-based Self-Supervised Learning (SSL) approach that significantly enhances its efficacy for pre-training. Prior work in this direction masks out pre-defined frequencies in the input image and employs a reconstruction loss to pre-train the model. While achieving promising results, such an implementation has two fundamental limitations as identified in our paper. First, using pre-defined frequencies overlooks the variability of image frequency responses. Second, pre-trained with frequency-filtered images, the resulting model needs relatively more data to adapt to naturally looking images during fine-tuning. To address these drawbacks, we propose FOurier transform compression with seLf-Knowledge distillation (FOLK), integrating two dedicated ideas. First, inspired by image compression, we adaptively select the masked-out frequencies based on image frequency responses, creating more suitable SSL tasks for pre-training. Second, we employ a two-branch framework empowered by knowledge distillation, enabling the model to take both the filtered and original images as input, largely reducing the burden of downstream tasks. Our experimental results demonstrate the effectiveness of FOLK in achieving competitive performance to many state-of-the-art SSL methods across various downstream tasks, including image classification, few-shot learning, and semantic segmentation.

</details>

### Self-Supervised Diffusion Models for Electron-Aware Molecular Representation Learning.
- **链接**: [出版页](https://openreview.net/forum?id=UQ0RqfhgCk)
- **作者**: Gyoung S. Na, Chanyoung Park
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Simple, Good, Fast: Self-Supervised World Models Free of Baggage.
- **链接**: [arXiv:2506.02612](https://arxiv.org/abs/2506.02612)
- **作者**: Jan Robine, Marc Höftmann, Stefan Harmeling
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> What are the essential components of world models? How far do we get with world models that are not employing RNNs, transformers, discrete representations, and image reconstructions? This paper introduces SGF, a Simple, Good, and Fast world model that uses self-supervised representation learning, captures short-time dependencies through frame and action stacking, and enhances robustness against model errors through data augmentation. We extensively discuss SGF's connections to established world models, evaluate the building blocks in ablation studies, and demonstrate good performance through quantitative comparisons on the Atari 100k benchmark.

</details>

### Towards Self-Supervised Covariance Estimation in Deep Heteroscedastic Regression.
- **链接**: [arXiv:2502.10587](https://arxiv.org/abs/2502.10587)
- **作者**: Megh Shukla, Aziz Shameem, Mathieu Salzmann, Alexandre Alahi
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep heteroscedastic regression models the mean and covariance of the target distribution through neural networks. The challenge arises from heteroscedasticity, which implies that the covariance is sample dependent and is often unknown. Consequently, recent methods learn the covariance through unsupervised frameworks, which unfortunately yield a trade-off between computational complexity and accuracy. While this trade-off could be alleviated through supervision, obtaining labels for the covariance is non-trivial. Here, we study self-supervised covariance estimation in deep heteroscedastic regression. We address two questions: (1) How should we supervise the covariance assuming ground truth is available? (2) How can we obtain pseudo labels in the absence of the ground-truth? We address (1) by analysing two popular measures: the KL Divergence and the 2-Wasserstein distance. Subsequently, we derive an upper bound on the 2-Wasserstein distance between normal distributions with non-commutative covariances that is stable to optimize. We address (2) through a simple neighborhood based heuristic algorithm which results in surprisingly effective pseudo labels for the covariance. Our experiments over a wide range of synthetic and real datasets demonstrate that the proposed 2-Wasserstein bound coupled with pseudo label annotations results in a computationally cheaper yet accurate deep heteroscedastic regression.

</details>

### UNSURE: self-supervised learning with Unknown Noise level and Stein's Unbiased Risk Estimate.
- **链接**: [出版页](https://openreview.net/forum?id=ScVnYBaSEw)
- **作者**: Julián Tachella, Mike E. Davies, Laurent Jacques
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### T-JEPA: Augmentation-Free Self-Supervised Learning for Tabular Data.
- **链接**: [arXiv:2410.05016](https://arxiv.org/abs/2410.05016)
- **作者**: Hugo Thimonier, José Lucas De Melo Costa, Fabrice Popineau, Arpad Rimmel, Bich-Liên Doan
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervision is often used for pre-training to foster performance on a downstream task by constructing meaningful representations of samples. Self-supervised learning (SSL) generally involves generating different views of the same sample and thus requires data augmentations that are challenging to construct for tabular data. This constitutes one of the main challenges of self-supervision for structured data. In the present work, we propose a novel augmentation-free SSL method for tabular data. Our approach, T-JEPA, relies on a Joint Embedding Predictive Architecture (JEPA) and is akin to mask reconstruction in the latent space. It involves predicting the latent representation of one subset of features from the latent representation of a different subset within the same sample, thereby learning rich representations without augmentations. We use our method as a pre-training technique and train several deep classifiers on the obtained representation. Our experimental results demonstrate a substantial improvement in both classification and regression tasks, outperforming models trained directly on samples in their original data space. Moreover, T-JEPA enables some methods to consistently outperform or match the performance of traditional methods likes Gradient Boosted Decision Trees. To understand why, we extensively characterize the obtained representations and show that T-JEPA effectively identifies relevant features for downstream tasks without access to the labels. Additionally, we introduce regularization tokens, a novel regularization method critical for training of JEPA-based models on structured data.

</details>

### Score-based Self-supervised MRI Denoising.
- **链接**: [arXiv:2505.05631](https://arxiv.org/abs/2505.05631)
- **作者**: Jiachen Tu, Yaokun Shi, Fan Lam
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Magnetic resonance imaging (MRI) is a powerful noninvasive diagnostic imaging tool that provides unparalleled soft tissue contrast and anatomical detail. Noise contamination, especially in accelerated and/or low-field acquisitions, can significantly degrade image quality and diagnostic accuracy. Supervised learning based denoising approaches have achieved impressive performance but require high signal-to-noise ratio (SNR) labels, which are often unavailable. Self-supervised learning holds promise to address the label scarcity issue, but existing self-supervised denoising methods tend to oversmooth fine spatial features and often yield inferior performance than supervised methods. We introduce Corruption2Self (C2S), a novel score-based self-supervised framework for MRI denoising. At the core of C2S is a generalized denoising score matching (GDSM) loss, which extends denoising score matching to work directly with noisy observations by modeling the conditional expectation of higher-SNR images given further corrupted observations. This allows the model to effectively learn denoising across multiple noise levels directly from noisy data. Additionally, we incorporate a reparameterization of noise levels to stabilize training and enhance convergence, and introduce a detail refinement extension to balance noise reduction with the preservation of fine spatial features. Moreover, C2S can be extended to multi-contrast denoising by leveraging complementary information across different MRI contrasts. We demonstrate that our method achieves state-of-the-art performance among self-supervised methods and competitive results compared to supervised counterparts across varying noise conditions and MRI contrasts on the M4Raw and fastMRI dataset.

</details>

### PooDLe🐩: Pooled and dense self-supervised learning from naturalistic videos.
- **链接**: [出版页](https://openreview.net/forum?id=dEg5SdGaiq)
- **作者**: Alex N. Wang, Christopher Hoang, Yuwen Xiong, Yann LeCun, Mengye Ren
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### On Discriminative Probabilistic Modeling for Self-Supervised Representation Learning.
- **链接**: [arXiv:2410.09156](https://arxiv.org/abs/2410.09156) · [代码](https://github.com/bokun-wang/NUCLR)
- **作者**: Bokun Wang, Yunwen Lei, Yiming Ying, Tianbao Yang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We study the discriminative probabilistic modeling on a continuous domain for the data prediction task of (multimodal) self-supervised representation learning. To address the challenge of computing the integral in the partition function for each anchor data, we leverage the multiple importance sampling (MIS) technique for robust Monte Carlo integration, which can recover InfoNCE-based contrastive loss as a special case. Within this probabilistic modeling framework, we conduct generalization error analysis to reveal the limitation of current InfoNCE-based contrastive loss for self-supervised representation learning and derive insights for developing better approaches by reducing the error of Monte Carlo integration. To this end, we propose a novel non-parametric method for approximating the sum of conditional probability densities required by MIS through convex optimization, yielding a new contrastive objective for self-supervised representation learning. Moreover, we design an efficient algorithm for solving the proposed objective. We empirically compare our algorithm to representative baselines on the contrastive image-language pretraining task. Experimental results on the CC3M and CC12M datasets demonstrate the superior overall performance of our algorithm. Our code is available at https://github.com/bokun-wang/NUCLR.

</details>

### Self-Supervised Diffusion MRI Denoising via Iterative and Stable Refinement.
- **链接**: [arXiv:2501.13514](https://arxiv.org/abs/2501.13514) · [代码](https://github.com/FouierL/Di-Fusion)
- **作者**: Chenxu Wu, Qingpeng Kong, Zihang Jiang, S. Kevin Zhou
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Magnetic Resonance Imaging (MRI), including diffusion MRI (dMRI), serves as a ``microscope'' for anatomical structures and routinely mitigates the influence of low signal-to-noise ratio scans by compromising temporal or spatial resolution. However, these compromises fail to meet clinical demands for both efficiency and precision. Consequently, denoising is a vital preprocessing step, particularly for dMRI, where clean data is unavailable. In this paper, we introduce Di-Fusion, a fully self-supervised denoising method that leverages the latter diffusion steps and an adaptive sampling process. Unlike previous approaches, our single-stage framework achieves efficient and stable training without extra noise model training and offers adaptive and controllable results in the sampling process. Our thorough experiments on real and simulated data demonstrate that Di-Fusion achieves state-of-the-art performance in microstructure modeling, tractography tracking, and other downstream tasks. Code is available at https://github.com/FouierL/Di-Fusion.

</details>

### ST-GCond: Self-supervised and Transferable Graph Dataset Condensation.
- **链接**: [出版页](https://openreview.net/forum?id=wYWJFLQov9)
- **作者**: Beining Yang, Qingyun Sun, Cheng Ji, Xingcheng Fu, Jianxin Li
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Boost Self-Supervised Dataset Distillation via Parameterization, Predefined Augmentation, and Approximation.
- **链接**: [arXiv:2507.21455](https://arxiv.org/abs/2507.21455)
- **作者**: Sheng-Feng Yu, Jia-Jiun Yao, Wei-Chen Chiu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Although larger datasets are crucial for training large deep models, the rapid growth of dataset size has brought a significant challenge in terms of considerable training costs, which even results in prohibitive computational expenses. Dataset Distillation becomes a popular technique recently to reduce the dataset size via learning a highly compact set of representative exemplars, where the model trained with these exemplars ideally should have comparable performance with respect to the one trained with the full dataset. While most of existing works upon dataset distillation focus on supervised datasets, we instead aim to distill images and their self-supervisedly trained representations into a distilled set. This procedure, named as Self-Supervised Dataset Distillation, effectively extracts rich information from real datasets, yielding the distilled sets with enhanced cross-architecture generalizability. Particularly, in order to preserve the key characteristics of original dataset more faithfully and compactly, several novel techniques are proposed: 1) we introduce an innovative parameterization upon images and representations via distinct low-dimensional bases, where the base selection for parameterization is experimentally shown to play a crucial role; 2) we tackle the instability induced by the randomness of data augmentation -- a key component in self-supervised learning but being underestimated in the prior work of self-supervised dataset distillation -- by utilizing predetermined augmentations; 3) we further leverage a lightweight network to model the connections among the representations of augmented views from the same image, leading to more compact pairs of distillation. Extensive experiments conducted on various datasets validate the superiority of our approach in terms of distillation efficiency, cross-architecture generalization, and transfer learning performance.

</details>

### Vevo: Controllable Zero-Shot Voice Imitation with Self-Supervised Disentanglement.
- **链接**: [arXiv:2502.07243](https://arxiv.org/abs/2502.07243)
- **作者**: Xueyao Zhang, Xiaohui Zhang, Kainan Peng, Zhenyu Tang, Vimal Manohar, Yingru Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The imitation of voice, targeted on specific speech attributes such as timbre and speaking style, is crucial in speech generation. However, existing methods rely heavily on annotated data, and struggle with effectively disentangling timbre and style, leading to challenges in achieving controllable generation, especially in zero-shot scenarios. To address these issues, we propose Vevo, a versatile zero-shot voice imitation framework with controllable timbre and style. Vevo operates in two core stages: (1) Content-Style Modeling: Given either text or speech's content tokens as input, we utilize an autoregressive transformer to generate the content-style tokens, which is prompted by a style reference; (2) Acoustic Modeling: Given the content-style tokens as input, we employ a flow-matching transformer to produce acoustic representations, which is prompted by a timbre reference. To obtain the content and content-style tokens of speech, we design a fully self-supervised approach that progressively decouples the timbre, style, and linguistic content of speech. Specifically, we adopt VQ-VAE as the tokenizer for the continuous hidden features of HuBERT. We treat the vocabulary size of the VQ-VAE codebook as the information bottleneck, and adjust it carefully to obtain the disentangled speech representations. Solely self-supervised trained on 60K hours of audiobook speech data, without any fine-tuning on style-specific corpora, Vevo matches or surpasses existing methods in accent and emotion conversion tasks. Additionally, Vevo's effectiveness in zero-shot voice conversion and text-to-speech tasks further demonstrates its strong generalization and versatility. Audio samples are available at https://versavoice.github.io.

</details>

### X-Sample Contrastive Loss: Improving Contrastive Learning with Sample Similarity Graphs.
- **链接**: [出版页](https://openreview.net/forum?id=c1Ng0f8ivn)
- **作者**: Vlad Sobal, Mark Ibrahim, Randall Balestriero, Vivien Cabannes, Diane Bouchacourt, Pietro Astolfi et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Discovering Clone Negatives via Adaptive Contrastive Learning for Image-Text Matching.
- **链接**: [出版页](https://openreview.net/forum?id=My9MBsO41H)
- **作者**: Renjie Pan, Jihao Dong, Hua Yang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Aligning Visual Contrastive learning models via Preference Optimization.
- **链接**: [arXiv:2411.08923](https://arxiv.org/abs/2411.08923)
- **作者**: Amirabbas Afzali, Borna Khodabandeh, Ali Rasekh, Mahyar JafariNodeh, Sepehr Kazemi Ranjbar, Simon Gottschalk
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Contrastive learning models have demonstrated impressive abilities to capture semantic similarities by aligning representations in the embedding space. However, their performance can be limited by the quality of the training data and its inherent biases. While Preference Optimization (PO) methods such as Reinforcement Learning from Human Feedback (RLHF) and Direct Preference Optimization (DPO) have been applied to align generative models with human preferences, their use in contrastive learning has yet to be explored. This paper introduces a novel method for training contrastive learning models using different PO methods to break down complex concepts. Our method systematically aligns model behavior with desired preferences, enhancing performance on the targeted task. In particular, we focus on enhancing model robustness against typographic attacks and inductive biases, commonly seen in contrastive vision-language models like CLIP. Our experiments demonstrate that models trained using PO outperform standard contrastive learning techniques while retaining their ability to handle adversarial challenges and maintain accuracy on other downstream tasks. This makes our method well-suited for tasks requiring fairness, robustness, and alignment with specific preferences. We evaluate our method for tackling typographic attacks on images and explore its ability to disentangle gender concepts and mitigate gender bias, showcasing the versatility of our approach.

</details>

### MIM-Refiner: A Contrastive Learning Boost from Intermediate Pre-Trained Masked Image Modeling Representations.
- **链接**: [出版页](https://openreview.net/forum?id=0PxLpVURTl)
- **作者**: Benedikt Alkin, Lukas Miklautz, Sepp Hochreiter, Johannes Brandstetter
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Contrastive Learning from Synthetic Audio Doppelgängers.
- **链接**: [出版页](https://openreview.net/forum?id=XRtyVELwr6)
- **作者**: Manuel Cherep, Nikhil Singh
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### PhiNets: Brain-inspired Non-contrastive Learning Based on Temporal Prediction Hypothesis.
- **链接**: [arXiv:2405.14650](https://arxiv.org/abs/2405.14650)
- **作者**: Satoki Ishikawa, Makoto Yamada, Han Bao, Yuki Takezawa
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Predictive coding is a theory which hypothesises that cortex predicts sensory inputs at various levels of abstraction to minimise prediction errors. Inspired by predictive coding, Chen et al. (2024) proposed another theory, temporal prediction hypothesis, to claim that sequence memory residing in hippocampus has emerged through predicting input signals from the past sensory inputs. Specifically, they supposed that the CA3 predictor in hippocampus creates synaptic delay between input signals, which is compensated by the following CA1 predictor. Though recorded neural activities were replicated based on the temporal prediction hypothesis, its validity has not been fully explored. In this work, we aim to explore the temporal prediction hypothesis from the perspective of self-supervised learning. Specifically, we focus on non-contrastive learning, which generates two augmented views of an input image and predicts one from another. Non-contrastive learning is intimately related to the temporal prediction hypothesis because the synaptic delay is implicitly created by StopGradient. Building upon a popular non-contrastive learner, SimSiam, we propose PhiNet, an extension of SimSiam to have two predictors explicitly corresponding to the CA3 and CA1, respectively. Through studying the PhiNet model, we discover two findings. First, meaningful data representations emerge in PhiNet more stably than in SimSiam. This is initially supported by our learning dynamics analysis: PhiNet is more robust to the representational collapse. Second, PhiNet adapts more quickly to newly incoming patterns in online and continual learning scenarios. For practitioners, we additionally propose an extension called X-PhiNet integrated with a momentum encoder, excelling in continual learning. All in all, our work reveals that the temporal prediction hypothesis is a reasonable model in terms of the robustness and adaptivity.

</details>

### Nova: Generative Language Models for Assembly Code with Hierarchical Attention and Contrastive Learning.
- **链接**: [出版页](https://openreview.net/forum?id=4ytRL3HJrq)
- **作者**: Nan Jiang, Chengxiao Wang, Kevin Liu, Xiangzhe Xu, Lin Tan, Xiangyu Zhang et al.
- **🏷️ 机构**: MEGVII
- **会议**: ICLR 2025

### Refine Knowledge of Large Language Models via Adaptive Contrastive Learning.
- **链接**: [arXiv:2502.07184](https://arxiv.org/abs/2502.07184)
- **作者**: Yinghui Li, Haojing Huang, Jiayi Kuang, Yangning Li, Shu-Yu Guo, Chao Qu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> How to alleviate the hallucinations of Large Language Models (LLMs) has always been the fundamental goal pursued by the LLMs research community. Looking through numerous hallucination-related studies, a mainstream category of methods is to reduce hallucinations by optimizing the knowledge representation of LLMs to change their output. Considering that the core focus of these works is the knowledge acquired by models, and knowledge has long been a central theme in human societal progress, we believe that the process of models refining knowledge can greatly benefit from the way humans learn. In our work, by imitating the human learning process, we design an Adaptive Contrastive Learning strategy. Our method flexibly constructs different positive and negative samples for contrastive learning based on LLMs' actual mastery of knowledge. This strategy helps LLMs consolidate the correct knowledge they already possess, deepen their understanding of the correct knowledge they have encountered but not fully grasped, forget the incorrect knowledge they previously learned, and honestly acknowledge the knowledge they lack. Extensive experiments and detailed analyses on widely used datasets demonstrate the effectiveness of our method.

</details>

### ContraDiff: Planning Towards High Return States via Contrastive Learning.
- **链接**: [出版页](https://openreview.net/forum?id=XMOaOigOQo)
- **作者**: Yixiang Shan, Zhengbang Zhu, Ting Long, Qifan Liang, Yi Chang, Weinan Zhang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Neuron Platonic Intrinsic Representation From Dynamics Using Contrastive Learning.
- **链接**: [arXiv:2502.10425](https://arxiv.org/abs/2502.10425)
- **作者**: Wei Wu, Can Liao, Zizhen Deng, Zhengrui Guo, Jinzhuo Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The Platonic Representation Hypothesis suggests a universal, modality-independent reality representation behind different data modalities. Inspired by this, we view each neuron as a system and detect its multi-segment activity data under various peripheral conditions. We assume there's a time-invariant representation for the same neuron, reflecting its intrinsic properties like molecular profiles, location, and morphology. The goal of obtaining these intrinsic neuronal representations has two criteria: (I) segments from the same neuron should have more similar representations than those from different neurons; (II) the representations must generalize well to out-of-domain data. To meet these, we propose the NeurPIR (Neuron Platonic Intrinsic Representation) framework. It uses contrastive learning, with segments from the same neuron as positive pairs and those from different neurons as negative pairs. In implementation, we use VICReg, which focuses on positive pairs and separates dissimilar samples via regularization. We tested our method on Izhikevich model-simulated neuronal population dynamics data. The results accurately identified neuron types based on preset hyperparameters. We also applied it to two real-world neuron dynamics datasets with neuron type annotations from spatial transcriptomics and neuron locations. Our model's learned representations accurately predicted neuron types and locations and were robust on out-of-domain data (from unseen animals). This shows the potential of our approach for understanding neuronal systems and future neuroscience research.

</details>

### RelCon: Relative Contrastive Learning for a Motion Foundation Model for Wearable Data.
- **链接**: [arXiv:2411.18822](https://arxiv.org/abs/2411.18822)
- **作者**: Maxwell A. Xu, Jaya Narain, Gregory Darnell, Haraldur Tómas Hallgrímsson, Hyewon Jeong, Darren Forde et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present RelCon, a novel self-supervised Relative Contrastive learning approach for training a motion foundation model from wearable accelerometry sensors. First, a learnable distance measure is trained to capture motif similarity and domain-specific semantic information such as rotation invariance. Then, the learned distance provides a measurement of semantic similarity between a pair of accelerometry time-series, which we use to train our foundation model to model relative relationships across time and across subjects. The foundation model is trained on 1 billion segments from 87,376 participants, and achieves state-of-the-art performance across multiple downstream tasks, including human activity recognition and gait metric regression. To our knowledge, we are the first to show the generalizability of a foundation model with motion data from wearables across distinct evaluation tasks.

</details>

### A Non-Contrastive Learning Framework for Sequential Recommendation with Preference-Preserving Profile Generation.
- **链接**: [出版页](https://openreview.net/forum?id=Ke2BEL4csm)
- **作者**: Huimin Zeng, Xiaojie Wang, Anoop Jain, Zhicheng Dou, Dong Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Morphing Tokens Draw Strong Masked Image Models.
- **链接**: [出版页](https://openreview.net/forum?id=d7q9IGj2p0)
- **作者**: Taekyung Kim, Byeongho Heo, Dongyoon Han
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Learning Mask Invariant Mutual Information for Masked Image Modeling.
- **链接**: [arXiv:2502.19718](https://arxiv.org/abs/2502.19718)
- **作者**: Tao Huang, Yanxiang Ma, Shan You, Chang Xu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Masked autoencoders (MAEs) represent a prominent self-supervised learning paradigm in computer vision. Despite their empirical success, the underlying mechanisms of MAEs remain insufficiently understood. Recent studies have attempted to elucidate the functioning of MAEs through contrastive learning and feature representation analysis, yet these approaches often provide only implicit insights. In this paper, we propose a new perspective for understanding MAEs by leveraging the information bottleneck principle in information theory. Our theoretical analyses reveal that optimizing the latent features to balance relevant and irrelevant information is key to improving MAE performance. Building upon our proofs, we introduce MI-MAE, a novel method that optimizes MAEs through mutual information maximization and minimization. By enhancing latent features to retain maximal relevant information between them and the output, and minimizing irrelevant information between them and the input, our approach achieves better performance. Extensive experiments on standard benchmarks show that MI-MAE significantly outperforms MAE models in tasks such as image classification, object detection, and semantic segmentation. Our findings validate the theoretical framework and highlight the practical advantages of applying the information bottleneck principle to MAEs, offering deeper insights for developing more powerful self-supervised learning models.

</details>

## 跨领域论文（完整笔记在其他领域）

- Self-supervised Monocular Depth Estimation Robust to Reflective Surface Leveraged by Triplet Mining. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
- What to align in multimodal contrastive learning? → [multimodal](../multimodal/Guideline%202025.md)
- Weighted Point Set Embedding for Multimodal Contrastive Learning Toward Optimal Similarity Metric. → [multimodal](../multimodal/Guideline%202025.md)
- In vivo cell-type and brain region classification via multimodal contrastive learning. → [multimodal](../multimodal/Guideline%202025.md)
- CL-MFAP: A Contrastive Learning-Based Multimodal Foundation Model for Molecular Property Prediction and Antibiotic Screening. → [multimodal](../multimodal/Guideline%202025.md)
- Mutual Effort for Efficiency: A Similarity-based Token Pruning for Vision Transformers in Self-Supervised Learning. → [network-pruning](../network-pruning/Guideline%202025.md)
