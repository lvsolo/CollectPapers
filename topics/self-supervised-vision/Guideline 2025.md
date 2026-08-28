# Self-supervised Vision — 2025 Guideline

> 领域: 视觉自监督学习（对比学习、MAE、DINO 系）
> 论文数: 61 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Complete Structure Guided Point Cloud Completion via Cluster- and Instance-Level Contrastive Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/f79f4461463f1cd6a4b6849239829002-Abstract-Conference.html) · 📚 被引 0
- **作者**: Yang Chen, Yirun Zhou, Weizhong Zhang, Cheng Jin
- **🏷️ 机构**: Shanghai AI Lab, Fudan University, The Hong Kong University of Science and Technology
- **会议**: NeurIPS 2025

### Understanding the Gain from Data Filtering in Multimodal Contrastive Learning.
- **链接**: [arXiv:2512.14230](https://arxiv.org/abs/2512.14230) · 📚 被引 0
- **作者**: Divyansh Pareek, Sewoong Oh, Simon S. Du
- **🏷️ 机构**: University of Washington
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The success of modern multimodal representation learning relies on internet-scale datasets. Due to the low quality of a large fraction of raw web data, data curation has become a critical step in the training pipeline. Filtering using a trained model (i.e., teacher-based filtering) has emerged as a successful solution, leveraging a pre-trained model to compute quality scores. To explain the empirical success of teacher-based filtering, we characterize the performance of filtered contrastive learning under the standard bimodal data generation model. Denoting $η\in(0,1]$ as the fraction of data with correctly matched modalities among $n$ paired samples, we utilize a linear contrastive learning setup to show a provable benefit of data filtering: $(i)$ the error without filtering is upper and lower bounded by $\frac{1}{η\sqrt{n}}$, and $(ii)$ the error with teacher-based filtering is upper bounded by $\frac{1}{\sqrt{ηn}}$ in the large $η$ regime, and by $\frac{1}{\sqrt{n}}$ in the small $η$ regime.

</details>

### Asymmetric Dual Self-Distillation for 3D Self-Supervised Representation Learning.
- **链接**: [arXiv:2506.21724](https://arxiv.org/abs/2506.21724) · 📚 被引 0
- **作者**: Remco F. Leijenaar, Hamidreza Kasaei
- **🏷️ 机构**: University of Groningen, Dept. of AI, University of Groningen
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Learning semantically meaningful representations from unstructured 3D point clouds remains a central challenge in computer vision, especially in the absence of large-scale labeled datasets. While masked point modeling (MPM) is widely used in self-supervised 3D learning, its reconstruction-based objective can limit its ability to capture high-level semantics. We propose AsymDSD, an Asymmetric Dual Self-Distillation framework that unifies masked modeling and invariance learning through prediction in the latent space rather than the input space. AsymDSD builds on a joint embedding architecture and introduces several key design choices: an efficient asymmetric setup, disabling attention between masked queries to prevent shape leakage, multi-mask sampling, and a point cloud adaptation of multi-crop. AsymDSD achieves state-of-the-art results on ScanObjectNN (90.53%) and further improves to 93.72% when pretrained on 930k shapes, surpassing prior methods.

</details>

### Self-Supervised Contrastive Learning is Approximately Supervised Contrastive Learning.
- **链接**: [arXiv:2506.04411](https://arxiv.org/abs/2506.04411) · [代码](https://github.com/DLFundamentals/understanding-ssl) · 📚 被引 0
- **作者**: Achleshwar Luthra, Tianbao Yang, Tomer Galanti
- **🏷️ 机构**: Texas A&amp;M University, Texas A&amp;M university
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite its empirical success, the theoretical foundations of self-supervised contrastive learning (CL) are not yet fully established. In this work, we address this gap by showing that standard CL objectives implicitly approximate a supervised variant we call the negatives-only supervised contrastive loss (NSCL), which excludes same-class contrasts. We prove that the gap between the CL and NSCL losses vanishes as the number of semantic classes increases, under a bound that is both label-agnostic and architecture-independent. We characterize the geometric structure of the global minimizers of the NSCL loss: the learned representations exhibit augmentation collapse, within-class collapse, and class centers that form a simplex equiangular tight frame. We further introduce a new bound on the few-shot error of linear-probing. This bound depends on two measures of feature variability--within-class dispersion and variation along the line between class centers. We show that directional variation dominates the bound and that the within-class dispersion's effect diminishes as the number of labeled samples increases. These properties enable CL and NSCL-trained representations to support accurate few-shot label recovery using simple linear probes. Finally, we empirically validate our theoretical findings: the gap between CL and NSCL losses decays at a rate of $\mathcal{O}(\frac{1}{\#\text{classes}})$; the two losses are highly correlated; minimizing the CL loss implicitly brings the NSCL loss close to the value achieved by direct minimization; and the proposed few-shot error bound provides a tight estimate of probing performance in practice. The code and project page of the paper are available at [\href{https://github.com/DLFundamentals/understanding-ssl}{code}, \href{https://dlfundamentals.github.io/ssl-is-approximately-sl/}{project page}].

</details>

### OSKAR: Omnimodal Self-supervised Knowledge Abstraction and Representation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/010ca5a0ccb09cfb554ed637758a08da-Abstract-Conference.html) · 📚 被引 0
- **作者**: Mohamed Abdelfattah, Kaouther Messaoud, Alexandre Alahi
- **🏷️ 机构**: Cornell University, EPFL Ecole Polytechnique Federale de Lausanne, EPFL
- **会议**: NeurIPS 2025

### Joint-Embedding vs Reconstruction: Provable Benefits of Latent Space Prediction for Self-Supervised Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/1fa81061d6d4d7fea88f803d89ae9d6e-Abstract-Conference.html) · 📚 被引 0
- **作者**: Hugues Van Assel, Mark Ibrahim, Tommaso Biancalani, Aviv Regev, Randall Balestriero
- **🏷️ 机构**: Genentech, Fundamental AI Research (FAIR) at Meta, Brown University Meta FAIR
- **会议**: NeurIPS 2025

### CG-SSL: Concept-Guided Self-Supervised Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/d4557f8bbe5f51f0f6b74fb8d74e9341-Abstract-Conference.html) · 📚 被引 0
- **作者**: Sara Atito, Josef Kittler, Imran Razzak, Muhammad Awais
- **🏷️ 机构**: University of Surrey, Mohamed bin Zayed University of Artificial Intelligence, CVSSP, University of Surrey
- **会议**: NeurIPS 2025

### VESSA: Video-based objEct-centric Self-Supervised Adaptation for Visual Foundation Models.
- **链接**: [arXiv:2510.20994](https://arxiv.org/abs/2510.20994) · [代码](https://github.com/jesimonbarreto/VESSA) · 📚 被引 0
- **作者**: Jesimon Barreto, Carlos Caetano, André Araújo, William Schwartz
- **🏷️ 机构**: Universidade Federal de Minas Gerais, Universidade Federal de Minas Gerais, Recod.ai - Universidade Estadual de Campinas (UNICAMP), Google Research
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Foundation models have advanced computer vision by enabling strong performance across diverse tasks through large-scale pretraining and supervised fine-tuning. However, they may underperform in domains with distribution shifts and scarce labels, where supervised fine-tuning may be infeasible. While continued self-supervised learning for model adaptation is common for generative language models, this strategy has not proven effective for vision-centric encoder models. To address this challenge, we introduce a novel formulation of self-supervised fine-tuning for vision foundation models, where the model is adapted to a new domain without requiring annotations, leveraging only short multi-view object-centric videos. Our method is referred to as VESSA: Video-based objEct-centric Self-Supervised Adaptation for visual foundation models. VESSA's training technique is based on a self-distillation paradigm, where it is critical to carefully tune prediction heads and deploy parameter-efficient adaptation techniques - otherwise, the model may quickly forget its pretrained knowledge and reach a degraded state. VESSA benefits significantly from multi-view object observations sourced from different frames in an object-centric video, efficiently learning robustness to varied capture conditions, without the need of annotations. Through comprehensive experiments with 3 vision foundation models on 2 datasets, VESSA demonstrates consistent improvements in downstream classification tasks, compared to the base models and previous adaptation methods. Code is publicly available at https://github.com/jesimonbarreto/VESSA.

</details>

### Dataset Distillation for Pre-Trained Self-Supervised Vision Models.
- **链接**: [arXiv:2511.16674](https://arxiv.org/abs/2511.16674) · 📚 被引 0
- **作者**: George Cazenavette, Antonio Torralba, Vincent Sitzmann
- **🏷️ 机构**: MIT
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The task of dataset distillation aims to find a small set of synthetic images such that training a model on them reproduces the performance of the same model trained on a much larger dataset of real samples. Existing distillation methods focus on synthesizing datasets that enable training randomly initialized models. In contrast, state-of-the-art vision approaches are increasingly building on large, pre-trained self-supervised models rather than training from scratch. In this paper, we investigate the problem of distilling datasets that enable us to optimally train linear probes on top of such large, pre-trained vision models. We introduce a method of dataset distillation for this task called Linear Gradient Matching that optimizes the synthetic images such that, when passed through a pre-trained feature extractor, they induce gradients in the linear classifier similar to those produced by the real data. Our method yields synthetic data that outperform all real-image baselines and, remarkably, generalize across pre-trained vision models, enabling us, for instance, to train a linear CLIP probe that performs competitively using a dataset distilled via a DINO backbone. Further, we show that our distilled datasets are exceptionally effective for fine-grained classification and provide a valuable tool for model interpretability, predicting, among other things, how similar two models' embedding spaces are under the platonic representation hypothesis or whether a model is sensitive to spurious correlations in adversarial datasets.

</details>

### Exploring Structural Degradation in Dense Representations for Self-supervised Learning.
- **链接**: [arXiv:2510.17299](https://arxiv.org/abs/2510.17299) · [代码](https://github.com/EldercatSAM/SSL-Degradation) · 📚 被引 0
- **作者**: Siran Dai, Qianqian Xu, Peisong Wen, Yang Liu, Qingming Huang
- **🏷️ 机构**: University of Chinese Academic of Science, Key Laboratory of Intelligent Information Processing, Institute of Computing Technology, Chinese Academy of Sciences, University of the Chinese Academy of Sciences
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this work, we observe a counterintuitive phenomenon in self-supervised learning (SSL): longer training may impair the performance of dense prediction tasks (e.g., semantic segmentation). We refer to this phenomenon as Self-supervised Dense Degradation (SDD) and demonstrate its consistent presence across sixteen state-of-the-art SSL methods with various losses, architectures, and datasets. When the model performs suboptimally on dense tasks at the end of training, measuring the performance during training becomes essential. However, evaluating dense performance effectively without annotations remains an open challenge. To tackle this issue, we introduce a Dense representation Structure Estimator (DSE), composed of a class-relevance measure and an effective dimensionality measure. The proposed DSE is both theoretically grounded and empirically validated to be closely correlated with the downstream performance. Based on this metric, we introduce a straightforward yet effective model selection strategy and a DSE-based regularization method. Experiments on sixteen SSL methods across four benchmarks confirm that model selection improves mIoU by $3.0\%$ on average with negligible computational cost. Additionally, DSE regularization consistently mitigates the effects of dense degradation. Code is available at https://github.com/EldercatSAM/SSL-Degradation.

</details>

### Tabula: A Tabular Self-Supervised Foundation Model for Single-Cell Transcriptomics.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/95d590995a8722259c61e094b62b25ac-Abstract-Conference.html) · 📚 被引 0
- **作者**: Jiayuan Ding, Jianhui Lin, Shiyu Jiang, Yixin Wang, Ziyang Miao, Zhaoyu Fang et al.
- **🏷️ 机构**: Stanford University, Central South University, University of Southern California
- **会议**: NeurIPS 2025

### Adv-SSL: Adversarial Self-Supervised Representation Learning with Theoretical Guarantees.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/b216ce49d808157ba14adec9453983a4-Abstract-Conference.html) · 📚 被引 0
- **作者**: Chenguang Duan, Yuling Jiao, Huazhen Lin, Wensen Ma, Jerry Zhijian Yang
- **🏷️ 机构**: Rheinisch Westfälische Technische Hochschule Aachen, Wuhan University, Southwest University of Finance and Economics
- **会议**: NeurIPS 2025

### How Different from the Past? Spatio-Temporal Time Series Forecasting with Self-Supervised Deviation Learning.
- **链接**: [arXiv:2510.04908](https://arxiv.org/abs/2510.04908) · [代码](https://github.com/Jimmy-7664/ST-SSDL) · 📚 被引 0
- **作者**: Haotian Gao, Zheng Dong, Jiawei Yong, Shintaro Fukushima, Kenjiro Taura, Renhe Jiang
- **🏷️ 机构**: The University of Tokyo, Southern University of Science and Technology, Toyota Motor Corporation
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Spatio-temporal forecasting is essential for real-world applications such as traffic management and urban computing. Although recent methods have shown improved accuracy, they often fail to account for dynamic deviations between current inputs and historical patterns. These deviations contain critical signals that can significantly affect model performance. To fill this gap, we propose ST-SSDL, a Spatio-Temporal time series forecasting framework that incorporates a Self-Supervised Deviation Learning scheme to capture and utilize such deviations. ST-SSDL anchors each input to its historical average and discretizes the latent space using learnable prototypes that represent typical spatio-temporal patterns. Two auxiliary objectives are proposed to refine this structure: a contrastive loss that enhances inter-prototype discriminability and a deviation loss that regularizes the distance consistency between input representations and corresponding prototypes to quantify deviation. Optimized jointly with the forecasting objective, these components guide the model to organize its hidden space and improve generalization across diverse input conditions. Experiments on six benchmark datasets show that ST-SSDL consistently outperforms state-of-the-art baselines across multiple metrics. Visualizations further demonstrate its ability to adaptively respond to varying levels of deviation in complex spatio-temporal scenarios. Our code and datasets are available at https://github.com/Jimmy-7664/ST-SSDL.

</details>

### Self-Supervised Learning of Graph Representations for Network Intrusion Detection.
- **链接**: [arXiv:2509.16625](https://arxiv.org/abs/2509.16625) · 📚 被引 2
- **作者**: Lorenzo Guerra, Thomas Chapuis, Guillaume Duc, Pavlo Mozharovskyi, Van-Tam Nguyen
- **🏷️ 机构**: Télécom Paris / Renault, Ampere, Télécom Paris
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Detecting intrusions in network traffic is a challenging task, particularly under limited supervision and constantly evolving attack patterns. While recent works have leveraged graph neural networks for network intrusion detection, they often decouple representation learning from anomaly detection, limiting the utility of the embeddings for identifying attacks. We propose GraphIDS, a self-supervised intrusion detection model that unifies these two stages by learning local graph representations of normal communication patterns through a masked autoencoder. An inductive graph neural network embeds each flow with its local topological context to capture typical network behavior, while a Transformer-based encoder-decoder reconstructs these embeddings, implicitly learning global co-occurrence patterns via self-attention without requiring explicit positional information. During inference, flows with unusually high reconstruction errors are flagged as potential intrusions. This end-to-end framework ensures that embeddings are directly optimized for the downstream task, facilitating the recognition of malicious traffic. On diverse NetFlow benchmarks, GraphIDS achieves strong performance, reaching up to 99.98% PR-AUC and 99.61% macro F1-score.

</details>

### Self-Supervised Selective-Guided Diffusion Model for Old-Photo Face Restoration.
- **链接**: [arXiv:2510.12114](https://arxiv.org/abs/2510.12114) · [代码](https://github.com/PRIS-CV/SSDiff) · 📚 被引 1
- **作者**: Wenjie Li, Xiangyi Wang, Heng Guo, Guangwei Gao, Zhanyu Ma
- **🏷️ 机构**: The Hong Kong Polytechnic University, Beijing University of Posts and Telecommunications, Nanjing University of Posts and Telecommunications
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Old-photo face restoration poses significant challenges due to compounded degradations such as breakage, fading, and severe blur. Existing pre-trained diffusion-guided methods either rely on explicit degradation priors or global statistical guidance, which struggle with localized artifacts or face color. We propose Self-Supervised Selective-Guided Diffusion (SSDiff), which leverages pseudo-reference faces generated by a pre-trained diffusion model under weak guidance. These pseudo-labels exhibit structurally aligned contours and natural colors, enabling region-specific restoration via staged supervision: structural guidance applied throughout the denoising process and color refinement in later steps, aligned with the coarse-to-fine nature of diffusion. By incorporating face parsing maps and scratch masks, our method selectively restores breakage regions while avoiding identity mismatch. We further construct VintageFace, a 300-image benchmark of real old face photos with varying degradation levels. SSDiff outperforms existing GAN-based and diffusion-based methods in perceptual quality, fidelity, and regional controllability. Code link: https://github.com/PRIS-CV/SSDiff.

</details>

### SSTAG: Structure-Aware Self-Supervised Learning Method for Text-Attributed Graphs.
- **链接**: [arXiv:2510.01248](https://arxiv.org/abs/2510.01248) · 📚 被引 1
- **作者**: Ruyue Liu, Rong Yin, Xiangzhen Bo, Xiaoshuai Hao, Yong Liu, Jinwen Zhong et al.
- **🏷️ 机构**: Institute of Information Engineering Chinese Academy of Sciences, Beihang University, Wuhan University of Technology
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large scale pretrained models have revolutionized Natural Language Processing (NLP) and Computer Vision (CV), showcasing remarkable cross domain generalization abilities. However, in graph learning, models are typically trained on individual graph datasets, limiting their capacity to transfer knowledge across different graphs and tasks. This approach also heavily relies on large volumes of annotated data, which presents a significant challenge in resource-constrained settings. Unlike NLP and CV, graph structured data presents unique challenges due to its inherent heterogeneity, including domain specific feature spaces and structural diversity across various applications. To address these challenges, we propose a novel structure aware self supervised learning method for Text Attributed Graphs (SSTAG). By leveraging text as a unified representation medium for graph learning, SSTAG bridges the gap between the semantic reasoning of Large Language Models (LLMs) and the structural modeling capabilities of Graph Neural Networks (GNNs). Our approach introduces a dual knowledge distillation framework that co-distills both LLMs and GNNs into structure-aware multilayer perceptrons (MLPs), enhancing the scalability of large-scale TAGs. Additionally, we introduce an in-memory mechanism that stores typical graph representations, aligning them with memory anchors in an in-memory repository to integrate invariant knowledge, thereby improving the model's generalization ability. Extensive experiments demonstrate that SSTAG outperforms state-of-the-art models on cross-domain transfer learning tasks, achieves exceptional scalability, and reduces inference costs while maintaining competitive performance.

</details>

### Ditch the Denoiser: Emergence of Noise Robustness in Self-Supervised Learning from Data Curriculum.
- **链接**: [arXiv:2505.12191](https://arxiv.org/abs/2505.12191) · [代码](https://github.com/wenquanlu/noisy_dinov2) · 📚 被引 0
- **作者**: Wenquan Lu, Jiaqi Zhang, Hugues Van Assel, Randall Balestriero
- **🏷️ 机构**: Brown University, Chongqing University, Genentech
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-Supervised Learning (SSL) has become a powerful solution to extract rich representations from unlabeled data. Yet, SSL research is mostly focused on clean, curated and high-quality datasets. As a result, applying SSL on noisy data remains a challenge, despite being crucial to applications such as astrophysics, medical imaging, geophysics or finance. In this work, we present a fully self-supervised framework that enables noise-robust representation learning without requiring a denoiser at inference or downstream fine-tuning. Our method first trains an SSL denoiser on noisy data, then uses it to construct a denoised-to-noisy data curriculum (i.e., training first on denoised, then noisy samples) for pretraining a SSL backbone (e.g., DINOv2), combined with a teacher-guided regularization that anchors noisy embeddings to their denoised counterparts. This process encourages the model to internalize noise robustness. Notably, the denoiser can be discarded after pretraining, simplifying deployment. On ImageNet-1k with ViT-B under extreme Gaussian noise ($σ=255$, SNR = 0.72 dB), our method improves linear probing accuracy by 4.8% over DINOv2, demonstrating that denoiser-free robustness can emerge from noise-aware pretraining. The code is available at https://github.com/wenquanlu/noisy_dinov2.

</details>

### Self-supervised Blending Structural Context of Visual Molecules for Robust Drug Interaction Prediction.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/c0ebffad509ae02bd60340690b1fdd5d-Abstract-Conference.html) · 📚 被引 0
- **作者**: Tengfei Ma, Kun Chen, Yongsheng Zang, Yujie Chen, Xuanbai Ren, Bosheng Song et al.
- **🏷️ 机构**: Hunan University
- **会议**: NeurIPS 2025

### Self-supervised Learning of Echocardiographic Video Representations via Online Cluster Distillation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/581e1a06fa20f2c079dc5fb2db236335-Abstract-Conference.html)
- **作者**: Divyanshu Mishra, Mohammadreza Salehi, Pramit Saha, Olga Patey, Aris T. Papageorghiou, Yuki Asano et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

### T-REGS: Minimum Spanning Tree Regularization for Self-Supervised Learning.
- **链接**: [arXiv:2510.23484](https://arxiv.org/abs/2510.23484) · 📚 被引 0
- **作者**: Julie Mordacq, David Loiseaux, Vicky Kalogeiton, Steve Oudot
- **🏷️ 机构**: Inria Saclay, Ecole Polytechnique, Lawrence Berkeley National Lab, Ecole polytechnique, IP Paris
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning (SSL) has emerged as a powerful paradigm for learning representations without labeled data, often by enforcing invariance to input transformations such as rotations or blurring. Recent studies have highlighted two pivotal properties for effective representations: (i) avoiding dimensional collapse-where the learned features occupy only a low-dimensional subspace, and (ii) enhancing uniformity of the induced distribution. In this work, we introduce T-REGS, a simple regularization framework for SSL based on the length of the Minimum Spanning Tree (MST) over the learned representation. We provide theoretical analysis demonstrating that T-REGS simultaneously mitigates dimensional collapse and promotes distribution uniformity on arbitrary compact Riemannian manifolds. Several experiments on synthetic data and on classical SSL benchmarks validate the effectiveness of our approach at enhancing representation quality.

</details>

### MoE-Gyro: Self-Supervised Over-Range Reconstruction and Denoising for MEMS Gyroscopes.
- **链接**: [arXiv:2506.06318](https://arxiv.org/abs/2506.06318) · 📚 被引 0
- **作者**: Feiyang Pan, Shenghe Zheng, Chunyan Yin, Guangbin Dou
- **🏷️ 机构**: Huawei Technologies Ltd., Shanghai Artificial Intelligence Laboratory, Southeast University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> MEMS gyroscopes play a critical role in inertial navigation and motion control applications but typically suffer from a fundamental trade-off between measurement range and noise performance. Existing hardware-based solutions aimed at mitigating this issue introduce additional complexity, cost, and scalability challenges. Deep-learning methods primarily focus on noise reduction and typically require precisely aligned ground-truth signals, making them difficult to deploy in practical scenarios and leaving the fundamental trade-off unresolved. To address these challenges, we introduce Mixture of Experts for MEMS Gyroscopes (MoE-Gyro), a novel self-supervised framework specifically designed for simultaneous over-range signal reconstruction and noise suppression. MoE-Gyro employs two experts: an Over-Range Reconstruction Expert (ORE), featuring a Gaussian-Decay Attention mechanism for reconstructing saturated segments; and a Denoise Expert (DE), utilizing dual-branch complementary masking combined with FFT-guided augmentation for robust noise reduction. A lightweight gating module dynamically routes input segments to the appropriate expert. Furthermore, existing evaluation lack a comprehensive standard for assessing multi-dimensional signal enhancement. To bridge this gap, we introduce IMU Signal Enhancement Benchmark (ISEBench), an open-source benchmarking platform comprising the GyroPeak-100 dataset and a unified evaluation of IMU signal enhancement methods. We evaluate MoE-Gyro using our proposed ISEBench, demonstrating that our framework significantly extends the measurable range from 450 deg/s to 1500 deg/s, reduces Bias Instability by 98.4%, and achieves state-of-the-art performance, effectively addressing the long-standing trade-off in inertial sensing.

</details>

### Self-Supervised Direct Preference Optimization for Text-to-Image Diffusion Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/03600ae6c3392fd65ad7c3a90c6f7ce8-Abstract-Conference.html) · 📚 被引 0
- **作者**: Liang Peng, Boxi Wu, Haoran Cheng, Yibo Zhao, Xiaofei He
- **🏷️ 机构**: FABU Inc, Zhejiang University, College of Computer Science and Technology, Zhejiang University
- **会议**: NeurIPS 2025

### ShapeEmbed: a self-supervised learning framework for 2D contour quantification.
- **链接**: [arXiv:2507.01009](https://arxiv.org/abs/2507.01009) · 📚 被引 0
- **作者**: Anna Foix Romero, Craig Russell, Alexander Krull, Virginie Uhlmann
- **🏷️ 机构**: EMBL's European Bioinformatics Institute, European Bioinformatics Institute - EMBL, Birmingham University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The shape of objects is an important source of visual information in a wide range of applications. One of the core challenges of shape quantification is to ensure that the extracted measurements remain invariant to transformations that preserve an object's intrinsic geometry, such as changing its size, orientation, and position in the image. In this work, we introduce ShapeEmbed, a self-supervised representation learning framework designed to encode the contour of objects in 2D images, represented as a Euclidean distance matrix, into a shape descriptor that is invariant to translation, scaling, rotation, reflection, and point indexing. Our approach overcomes the limitations of traditional shape descriptors while improving upon existing state-of-the-art autoencoder-based approaches. We demonstrate that the descriptors learned by our framework outperform their competitors in shape classification tasks on natural and biological images. We envision our approach to be of particular relevance to biological imaging applications.

</details>

### Self-Supervised Learning of Motion Concepts by Optimizing Counterfactuals.
- **链接**: [arXiv:2503.19953](https://arxiv.org/abs/2503.19953) · 📚 被引 0
- **作者**: Stefan Stojanov, David Wendt, Seungwoo Kim, Rahul Mysore Venkatesh, Kevin T. Feigelis, Klemen Kotar et al.
- **🏷️ 机构**: Georgia Institute of Technology, GLMX, Stanford University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Estimating motion in videos is an essential computer vision problem with many downstream applications, including controllable video generation and robotics. Current solutions are primarily trained using synthetic data or require tuning of situation-specific heuristics, which inherently limits these models' capabilities in real-world contexts. Despite recent developments in large-scale self-supervised learning from videos, leveraging such representations for motion estimation remains relatively underexplored. In this work, we develop Opt-CWM, a self-supervised technique for flow and occlusion estimation from a pre-trained next-frame prediction model. Opt-CWM works by learning to optimize counterfactual probes that extract motion information from a base video model, avoiding the need for fixed heuristics while training on unrestricted video inputs. We achieve state-of-the-art performance for motion estimation on real-world videos while requiring no labeled data.

</details>

### 1000 Layer Networks for Self-Supervised RL: Scaling Depth Can Enable New Goal-Reaching Capabilities.
- **链接**: [arXiv:2503.14858](https://arxiv.org/abs/2503.14858) · 📚 被引 0
- **作者**: Kevin Wang, Ishaan Javali, Michal Bortkiewicz, Tomasz Trzcinski, Benjamin Eysenbach
- **🏷️ 机构**: Princeton University, Warsaw University of Technology, Warsaw University of Technology, Tooploox, IDEAS, Jagiellonian University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Scaling up self-supervised learning has driven breakthroughs in language and vision, yet comparable progress has remained elusive in reinforcement learning (RL). In this paper, we study building blocks for self-supervised RL that unlock substantial improvements in scalability, with network depth serving as a critical factor. Whereas most RL papers in recent years have relied on shallow architectures (around 2 - 5 layers), we demonstrate that increasing the depth up to 1024 layers can significantly boost performance. Our experiments are conducted in an unsupervised goal-conditioned setting, where no demonstrations or rewards are provided, so an agent must explore (from scratch) and learn how to maximize the likelihood of reaching commanded goals. Evaluated on simulated locomotion and manipulation tasks, our approach increases performance on the self-supervised contrastive RL algorithm by $2\times$ - $50\times$, outperforming other goal-conditioned baselines. Increasing the model depth not only increases success rates but also qualitatively changes the behaviors learned. The project webpage and code can be found here: https://wang-kevin3290.github.io/scaling-crl/.

</details>

### Not All Data are Good Labels: On the Self-supervised Labeling for Time Series Forecasting.
- **链接**: [arXiv:2502.14704](https://arxiv.org/abs/2502.14704) · [代码](https://github.com/SuDIS-ZJU/SCAM) · 📚 被引 0
- **作者**: Yuxuan Yang, Dalin Zhang, Yuxuan Liang, Hua Lu, Gang Chen, Huan Li
- **🏷️ 机构**: Zhejiang University, Hangzhou Dianzi University, The Hong Kong University of Science and Technology (Guangzhou)
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Time Series Forecasting (TSF) is a crucial task in various domains, yet existing TSF models rely heavily on high-quality data and insufficiently exploit all available data. This paper explores a novel self-supervised approach to re-label time series datasets by inherently constructing candidate datasets. During the optimization of a simple reconstruction network, intermediates are used as pseudo labels in a self-supervised paradigm, improving generalization for any predictor. We introduce the Self-Correction with Adaptive Mask (SCAM), which discards overfitted components and selectively replaces them with pseudo labels generated from reconstructions. Additionally, we incorporate Spectral Norm Regularization (SNR) to further suppress overfitting from a loss landscape perspective. Our experiments on eleven real-world datasets demonstrate that SCAM consistently improves the performance of various backbone models. This work offers a new perspective on constructing datasets and enhancing the generalization of TSF models through self-supervised learning. The code is available at https://github.com/SuDIS-ZJU/SCAM.

</details>

### Self-Supervised Discovery of Neural Circuits in Spatially Patterned Neural Responses with Graph Neural Networks.
- **链接**: [arXiv:2509.17174](https://arxiv.org/abs/2509.17174) · 📚 被引 0
- **作者**: Kijung Yoon
- **🏷️ 机构**: Hanyang University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Inferring synaptic connectivity from neural population activity is a fundamental challenge in computational neuroscience, complicated by partial observability and mismatches between inference models and true circuit dynamics. In this study, we propose a graph-based neural inference model that simultaneously predicts neural activity and infers latent connectivity by modeling neurons as interacting nodes in a graph. The architecture features two distinct modules: one for learning structural connectivity and another for predicting future spiking activity via a graph neural network (GNN). Our model accommodates unobserved neurons through auxiliary nodes, allowing for inference in partially observed circuits. We evaluate this approach using synthetic data generated from ring attractor network models and real spike recordings from head direction cells in mice. Across a wide range of conditions, including varying recurrent connectivity, external inputs, and incomplete observations, our model reliably resolves spurious correlations and recovers accurate weight profiles. When applied to real data, the inferred connectivity aligns with theoretical predictions of continuous attractor models. These results highlight the potential of GNN-based models to infer latent neural circuitry through self-supervised structure learning, while leveraging the spike prediction task to flexibly link connectivity and dynamics across both simulated and biological neural systems.

</details>

### Contrastive Self-Supervised Learning As Neural Manifold Packing.
- **链接**: [arXiv:2506.13717](https://arxiv.org/abs/2506.13717) · 📚 被引 0
- **作者**: Guanming Zhang, David J. Heeger, Stefano Martiniani
- **🏷️ 机构**: New York University, NYU
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Contrastive self-supervised learning based on point-wise comparisons has been widely studied for vision tasks. In the visual cortex of the brain, neuronal responses to distinct stimulus classes are organized into geometric structures known as neural manifolds. Accurate classification of stimuli can be achieved by effectively separating these manifolds, akin to solving a packing problem. We introduce Contrastive Learning As Manifold Packing (CLAMP), a self-supervised framework that recasts representation learning as a manifold packing problem. CLAMP introduces a loss function inspired by the potential energy of short-range repulsive particle systems, such as those encountered in the physics of simple liquids and jammed packings. In this framework, each class consists of sub-manifolds embedding multiple augmented views of a single image. The sizes and positions of the sub-manifolds are dynamically optimized by following the gradient of a packing loss. This approach yields interpretable dynamics in the embedding space that parallel jamming physics, and introduces geometrically meaningful hyperparameters within the loss function. Under the standard linear evaluation protocol, which freezes the backbone and trains only a linear classifier, CLAMP achieves competitive performance with state-of-the-art self-supervised models. Furthermore, our analysis reveals that neural manifolds corresponding to different categories emerge naturally and are effectively separated in the learned representation space, highlighting the potential of CLAMP to bridge insights from physics, neural science, and machine learning.

</details>

### Concerto: Joint 2D-3D Self-Supervised Learning Emerges Spatial Representations.
- **链接**: [arXiv:2510.23607](https://arxiv.org/abs/2510.23607) · 📚 被引 0
- **作者**: Yujia Zhang, Xiaoyang Wu, Yixing Lao, Chengyao Wang, Zhuotao Tian, Naiyan Wang et al.
- **🏷️ 机构**: The University of Hong Kong, the University of Hong Kong, The Chinese University of Hong Kong
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Humans learn abstract concepts through multisensory synergy, and once formed, such representations can often be recalled from a single modality. Inspired by this principle, we introduce Concerto, a minimalist simulation of human concept learning for spatial cognition, combining 3D intra-modal self-distillation with 2D-3D cross-modal joint embedding. Despite its simplicity, Concerto learns more coherent and informative spatial features, as demonstrated by zero-shot visualizations. It outperforms both standalone SOTA 2D and 3D self-supervised models by 14.2% and 4.8%, respectively, as well as their feature concatenation, in linear probing for 3D scene perception. With full fine-tuning, Concerto sets new SOTA results across multiple scene understanding benchmarks (e.g., 80.7% mIoU on ScanNet). We further present a variant of Concerto tailored for video-lifted point cloud spatial understanding, and a translator that linearly projects Concerto representations into CLIP's language space, enabling open-world perception. These results highlight that Concerto emerges spatial representations with superior fine-grained geometric and semantic consistency.

</details>

### UniMRSeg: Unified Modality-Relax Segmentation via Hierarchical Self-Supervised Compensation.
- **链接**: [arXiv:2509.16170](https://arxiv.org/abs/2509.16170) · [代码](https://github.com/Xiaoqi-Zhao-DLUT/UniMRSeg) · 📚 被引 1
- **作者**: Xiaoqi Zhao, Youwei Pang, Chenyang Yu, Lihe Zhang, Huchuan Lu, Shijian Lu et al.
- **🏷️ 机构**: Yale University, Dalian University of Technology, Nanyang Technological University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-modal image segmentation faces real-world deployment challenges from incomplete/corrupted modalities degrading performance. While existing methods address training-inference modality gaps via specialized per-combination models, they introduce high deployment costs by requiring exhaustive model subsets and model-modality matching. In this work, we propose a unified modality-relax segmentation network (UniMRSeg) through hierarchical self-supervised compensation (HSSC). Our approach hierarchically bridges representation gaps between complete and incomplete modalities across input, feature and output levels. % First, we adopt modality reconstruction with the hybrid shuffled-masking augmentation, encouraging the model to learn the intrinsic modality characteristics and generate meaningful representations for missing modalities through cross-modal fusion. % Next, modality-invariant contrastive learning implicitly compensates the feature space distance among incomplete-complete modality pairs. Furthermore, the proposed lightweight reverse attention adapter explicitly compensates for the weak perceptual semantics in the frozen encoder. Last, UniMRSeg is fine-tuned under the hybrid consistency constraint to ensure stable prediction under all modality combinations without large performance fluctuations. Without bells and whistles, UniMRSeg significantly outperforms the state-of-the-art methods under diverse missing modality scenarios on MRI-based brain tumor segmentation, RGB-D semantic segmentation, RGB-D/T salient object segmentation. The code will be released at https://github.com/Xiaoqi-Zhao-DLUT/UniMRSeg.

</details>

### CellCLIP - Learning Perturbation Effects in Cell Painting via Text-Guided Contrastive Learning.
- **链接**: [arXiv:2506.06290](https://arxiv.org/abs/2506.06290) · 📚 被引 0
- **作者**: Mingyu Lu, Ethan Weinberger, Chanwoo Kim, Su-In Lee
- **🏷️ 机构**: University of Washington
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> High-content screening (HCS) assays based on high-throughput microscopy techniques such as Cell Painting have enabled the interrogation of cells' morphological responses to perturbations at an unprecedented scale. The collection of such data promises to facilitate a better understanding of the relationships between different perturbations and their effects on cellular state. Towards achieving this goal, recent advances in cross-modal contrastive learning could, in theory, be leveraged to learn a unified latent space that aligns perturbations with their corresponding morphological effects. However, the application of such methods to HCS data is not straightforward due to substantial differences in the semantics of Cell Painting images compared to natural images, and the difficulty of representing different classes of perturbations (e.g., small molecule vs CRISPR gene knockout) in a single latent space. In response to these challenges, here we introduce CellCLIP, a cross-modal contrastive learning framework for HCS data. CellCLIP leverages pre-trained image encoders coupled with a novel channel encoding scheme to better capture relationships between different microscopy channels in image embeddings, along with natural language encoders for representing perturbations. Our framework outperforms current open-source models, demonstrating the best performance in both cross-modal retrieval and biologically meaningful downstream tasks while also achieving significant reductions in computation time.

</details>

### Understanding Contrastive Learning via Gaussian Mixture Models.
- **链接**: [arXiv:2411.03517](https://arxiv.org/abs/2411.03517) · 📚 被引 0
- **作者**: Parikshit Bansal, Ali Kavis, Sujay Sanghavi
- **🏷️ 机构**: The University of Texas at Austin, UT Austin, UT-Austin
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning attempts to learn representations from un-labeled data; it does so via a loss function that encourages the embedding of a point to be close to that of its augmentations. This simple idea performs remarkably well, yet it is not precisely theoretically understood why this is the case. In this paper we analyze self-supervised learning in a natural context: dimensionality reduction in Gaussian Mixture Models. Crucially, we define an augmentation of a data point as being another independent draw from the same underlying mixture component. We show that vanilla contrastive learning (specifically, the InfoNCE loss) is able to find the optimal lower-dimensional subspace even when the Gaussians are not isotropic -- something that vanilla spectral techniques cannot do. We also prove a similar result for "non-contrastive" self-supervised learning (i.e., SimSiam loss). We further extend our analyses to multi-modal contrastive learning algorithms (e.g., CLIP). In this setting we show that contrastive learning learns the subset of fisher-optimal subspace, effectively filtering out all the noise from the learnt representations. Finally, we corroborate our theoretical finding through synthetic data experiments.

</details>

### Enhancing Contrastive Learning with Variable Similarity.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/1ee39118e5c1780659ce228e88d3b164-Abstract-Conference.html) · 📚 被引 0
- **作者**: Haowen Cui, Shuo Chen, Jun Li, Jian Yang
- **🏷️ 机构**: Nanjing University of Science and Technology, RIKEN, Chinese Academy of Sciences
- **会议**: NeurIPS 2025

### Semantic Retrieval Augmented Contrastive Learning for Sequential Recommendation.
- **链接**: [arXiv:2503.04162](https://arxiv.org/abs/2503.04162) · 📚 被引 1
- **作者**: Ziqiang Cui, Yunpeng Weng, Xing Tang, Xiaokun Zhang, Shiwei Li, Peiyang Liu et al.
- **🏷️ 机构**: TENCENT, FiT,Tencent, Dalian University of Technology
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Contrastive learning has shown effectiveness in improving sequential recommendation models. However, existing methods still face challenges in generating high-quality contrastive pairs: they either rely on random perturbations that corrupt user preference patterns or depend on sparse collaborative data that generates unreliable contrastive pairs. Furthermore, existing approaches typically require predefined selection rules that impose strong assumptions, limiting the model's ability to autonomously learn optimal contrastive pairs. To address these limitations, we propose a novel approach named Semantic Retrieval Augmented Contrastive Learning (SRA-CL). SRA-CL leverages the semantic understanding and reasoning capabilities of LLMs to generate expressive embeddings that capture both user preferences and item characteristics. These semantic embeddings enable the construction of candidate pools for inter-user and intra-user contrastive learning through semantic-based retrieval. To further enhance the quality of the contrastive samples, we introduce a learnable sample synthesizer that optimizes the contrastive sample generation process during model training. SRA-CL adopts a plug-and-play design, enabling seamless integration with existing sequential recommendation architectures. Extensive experiments on four public datasets demonstrate the effectiveness and model-agnostic nature of our approach.

</details>

### Mitigating Spurious Features in Contrastive Learning with Spectral Regularization.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/9aeabac8f13e3ea49eef15cf1154b3c4-Abstract-Conference.html) · 📚 被引 0
- **作者**: Naghmeh Ghanooni, Waleed Mustafa, Dennis Wagner, Sophie Fellenz, Anthony W. Lin, Marius Kloft
- **🏷️ 机构**: RPTU, Kaiserslautern, Universität Kaiserslautern, RPTU Kaiserslautern
- **会议**: NeurIPS 2025

### BioCLIP 2: Emergent Properties from Scaling Hierarchical Contrastive Learning.
- **链接**: [arXiv:2505.23883](https://arxiv.org/abs/2505.23883) · 📚 被引 1
- **作者**: Jianyang Gu, Sam Stevens, Elizabeth G. Campolongo, Matthew J. Thompson, Net Zhang, Jiaman Wu et al.
- **🏷️ 机构**: The Ohio State University, Ohio State University, Columbus, The Ohio State University, Columbus
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Foundation models trained at scale exhibit remarkable emergent behaviors, learning new capabilities beyond their initial training objectives. We find such emergent behaviors in biological vision models via large-scale contrastive vision-language training. To achieve this, we first curate TreeOfLife-200M, comprising 214 million images of living organisms, the largest and most diverse biological organism image dataset to date. We then train BioCLIP 2 on TreeOfLife-200M to distinguish different species. Despite the narrow training objective, BioCLIP 2 yields extraordinary accuracy when applied to various biological visual tasks such as habitat classification and trait prediction. We identify emergent properties in the learned embedding space of BioCLIP 2. At the inter-species level, the embedding distribution of different species aligns closely with functional and ecological meanings (e.g., beak sizes and habitats). At the intra-species level, instead of being diminished, the intra-species variations (e.g., life stages and sexes) are preserved and better separated in subspaces orthogonal to inter-species distinctions. We provide formal proof and analyses to explain why hierarchical supervision and contrastive objectives encourage these emergent properties. Crucially, our results reveal that these properties become increasingly significant with larger-scale training data, leading to a biologically meaningful embedding space.

</details>

### Multi-modal contrastive learning adapts to intrinsic dimensions of shared latent variables.
- **链接**: [arXiv:2505.12473](https://arxiv.org/abs/2505.12473) · 📚 被引 0
- **作者**: Yu Gui, Cong Ma, Zongming Ma
- **🏷️ 机构**: The Wharton School, University of Pennsylvania, University of California Berkeley, Yale University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-modal contrastive learning as a self-supervised representation learning technique has achieved great success in foundation model training, such as CLIP~\citep{radford2021learning}. In this paper, we study the theoretical properties of the learned representations from multi-modal contrastive learning beyond linear representations and specific data distributions. Our analysis reveals that, enabled by temperature optimization, multi-modal contrastive learning not only maximizes mutual information between modalities but also adapts to intrinsic dimensions of data, which can be much lower than user-specified dimensions for representation vectors. Experiments on both synthetic and real-world datasets demonstrate the ability of contrastive learning to learn low-dimensional and informative representations, bridging theoretical insights and practical performance.

</details>

### Adaptive and Multi-scale Affinity Alignment for Hierarchical Contrastive Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/74d63276e24d3c8af73219a0d6c28e10-Abstract-Conference.html) · 📚 被引 0
- **作者**: Jiawei Huang, Minming Li, Hu Ding
- **🏷️ 机构**: university of science and technology of china; city university of Hong Kong, City University of Hong Kong, University of Science and Technology of China
- **会议**: NeurIPS 2025

### CoUn: Empowering Machine Unlearning via Contrastive Learning.
- **链接**: [arXiv:2509.16391](https://arxiv.org/abs/2509.16391) · 📚 被引 0
- **作者**: Yasser H. Khalil, Mehdi Setayesh, Hongliang Li
- **🏷️ 机构**: Noah's Ark Lab, Huawei, Huawei Technologies Ltd.
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Machine unlearning (MU) aims to remove the influence of specific "forget" data from a trained model while preserving its knowledge of the remaining "retain" data. Existing MU methods based on label manipulation or model weight perturbations often achieve limited unlearning effectiveness. To address this, we introduce CoUn, a novel MU framework inspired by the observation that a model retrained from scratch using only retain data classifies forget data based on their semantic similarity to the retain data. CoUn emulates this behavior by adjusting learned data representations through contrastive learning (CL) and supervised learning, applied exclusively to retain data. Specifically, CoUn (1) leverages semantic similarity between data samples to indirectly adjust forget representations using CL, and (2) maintains retain representations within their respective clusters through supervised learning. Extensive experiments across various datasets and model architectures show that CoUn consistently outperforms state-of-the-art MU baselines in unlearning effectiveness. Additionally, integrating our CL module into existing baselines empowers their unlearning effectiveness.

</details>

### A Statistical Theory of Contrastive Learning via Approximate Sufficient Statistics.
- **链接**: [arXiv:2503.17538](https://arxiv.org/abs/2503.17538) · 📚 被引 0
- **作者**: Licong Lin, Song Mei
- **🏷️ 机构**: University of California, Berkeley
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Contrastive learning -- a modern approach to extract useful representations from unlabeled data by training models to distinguish similar samples from dissimilar ones -- has driven significant progress in foundation models. In this work, we develop a new theoretical framework for analyzing data augmentation-based contrastive learning, with a focus on SimCLR as a representative example. Our approach is based on the concept of \emph{approximate sufficient statistics}, which we extend beyond its original definition in \cite{oko2025statistical} for contrastive language-image pretraining (CLIP) using KL-divergence. We generalize it to equivalent forms and general f-divergences, and show that minimizing SimCLR and other contrastive losses yields encoders that are approximately sufficient. Furthermore, we demonstrate that these near-sufficient encoders can be effectively adapted to downstream regression and classification tasks, with performance depending on their sufficiency and the error induced by data augmentation in contrastive learning. Concrete examples in linear regression and topic classification are provided to illustrate the broad applicability of our results.

</details>

### CaliGCL: Calibrated Graph Contrastive Learning via Partitioned Similarity and Consistency Discrimination.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/b84cbefc3bebbb88811e2ead03c9ef0c-Abstract-Conference.html) · 📚 被引 0
- **作者**: Yuena Lin, Hao Wei, Hai-Chun Cai, Bohang Sun, Tao Yang, Zhen Yang et al.
- **🏷️ 机构**: Beijing University of Technology, Technical University of Munich, Fuzhou University
- **会议**: NeurIPS 2025

### Diversity Is All You Need for Contrastive Learning: Spectral Bounds on Gradient Magnitudes.
- **链接**: [arXiv:2510.05767](https://arxiv.org/abs/2510.05767) · 📚 被引 0
- **作者**: Peter Ochieng
- **🏷️ 机构**: university of cambridge
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We derive non-asymptotic spectral bands that bound the squared InfoNCE gradient norm via alignment, temperature, and batch spectrum, recovering the \(1/τ^{2}\) law and closely tracking batch-mean gradients on synthetic data and ImageNet. Using effective rank \(R_{\mathrm{eff}}\) as an anisotropy proxy, we design spectrum-aware batch selection, including a fast greedy builder. On ImageNet-100, Greedy-64 cuts time-to-67.5\% top-1 by 15\% vs.\ random (24\% vs.\ Pool--P3) at equal accuracy; CIFAR-10 shows similar gains. In-batch whitening promotes isotropy and reduces 50-step gradient variance by \(1.37\times\), matching our theoretical upper bound.

</details>

### TRACE: Contrastive learning for multi-trial time series data in neuroscience.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/728e11c3b1d0fc7e13f85f661b62dcbb-Abstract-Conference.html) · 📚 被引 0
- **作者**: Lisa Schmors, Dominic Gonschorek, Jan Niklas Böhm, Yongrong Qiu, Na Zhou, Dmitry Kobak et al.
- **🏷️ 机构**: Eberhard-Karls-Universität Tübingen, University of Tuebingen, University of Tübingen
- **会议**: NeurIPS 2025

### Path-Enhanced Contrastive Learning for Recommendation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/7cb33a355bbe68305e02a080ad4eb86a-Abstract-Conference.html) · 📚 被引 0
- **作者**: Haoran Sun, Fei Xiong, Yuanzhe Hu, Liang Wang
- **🏷️ 机构**: Beijing Jiaotong University, Chinese Academy of Sciences, NLPR, China
- **会议**: NeurIPS 2025

### Contrastive Learning with Data Misalignment: Feature Purity, Training Dynamics and Theoretical Generalization Guarantees.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/6c312b18a9ced18ca46d13c69b45d514-Abstract-Conference.html) · 📚 被引 0
- **作者**: Jiawei Sun, Shuai Zhang, Hongkang Li, Meng Wang
- **🏷️ 机构**: Rensselaer Polytechnic Institute, New Jersey Institute of Technology, University of Pennsylvania
- **会议**: NeurIPS 2025

### Breaking the Batch Barrier (B3) of Contrastive Learning via Smart Batch Mining.
- **链接**: [arXiv:2505.11293](https://arxiv.org/abs/2505.11293) · 📚 被引 1
- **作者**: Raghuveer Thirukovalluru, Rui Meng, Ye Liu, Karthikeyan K, Mingyi Su, Ping Nie et al.
- **🏷️ 机构**: PhD@Duke University                        Part time @ FAIR, Meta AI, Google Cloud AI Research, South China University of Technology
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Contrastive learning (CL) is a prevalent technique for training embedding models, which pulls semantically similar examples (positives) closer in the representation space while pushing dissimilar ones (negatives) further apart. A key source of negatives are 'in-batch' examples, i.e., positives from other examples in the batch. Effectiveness of such models is hence strongly influenced by the size and quality of training batches. In this work, we propose 'Breaking the Batch Barrier' (B3), a novel batch construction strategy designed to curate high-quality batches for CL. Our approach begins by using a pretrained teacher embedding model to rank all examples in the dataset, from which a sparse similarity graph is constructed. A community detection algorithm is then applied to this graph to identify clusters of examples that serve as strong negatives for one another. The clusters are then used to construct batches that are rich in in-batch negatives. Empirical results on the MMEB multimodal embedding benchmark (36 tasks) demonstrate that our method sets a new state of the art, outperforming previous best methods by +1.3 and +2.9 points at the 7B and 2B model scales, respectively. Notably, models trained with B3 surpass existing state-of-the-art results even with a batch size as small as 64, which is 4-16x smaller than that required by other methods. Moreover, experiments show that B3 generalizes well across domains and tasks, maintaining strong performance even when trained with considerably weaker teachers.

</details>

### DAAC: Discrepancy-Aware Adaptive Contrastive Learning for Medical Time series.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/f36a180277bd3d5781dc02245f9d5f52-Abstract-Conference.html) · 📚 被引 0
- **作者**: Yifan Wang, Hongfeng Ai, Ruiqi Li, Maowei Jiang, Quangao Liu, Jiahua Dong et al.
- **🏷️ 机构**: The Chinese University of Hong Kong, Shenzhen, ByteDance Inc., University of the Chinese Academy of Sciences
- **会议**: NeurIPS 2025

### Variational Supervised Contrastive Learning.
- **链接**: [arXiv:2506.07413](https://arxiv.org/abs/2506.07413)
- **作者**: Ziwen Wang, Jiajun Fan, Thao Nguyen, Heng Ji, Ge Liu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Contrastive learning has proven to be highly efficient and adaptable in shaping representation spaces across diverse modalities by pulling similar samples together and pushing dissimilar ones apart. However, two key limitations persist: (1) Without explicit regulation of the embedding distribution, semantically related instances can inadvertently be pushed apart unless complementary signals guide pair selection, and (2) excessive reliance on large in-batch negatives and tailored augmentations hinders generalization. To address these limitations, we propose Variational Supervised Contrastive Learning (VarCon), which reformulates supervised contrastive learning as variational inference over latent class variables and maximizes a posterior-weighted evidence lower bound (ELBO) that replaces exhaustive pair-wise comparisons for efficient class-aware matching and grants fine-grained control over intra-class dispersion in the embedding space. Trained exclusively on image data, our experiments on CIFAR-10, CIFAR-100, ImageNet-100, and ImageNet-1K show that VarCon (1) achieves state-of-the-art performance for contrastive learning frameworks, reaching 79.36% Top-1 accuracy on ImageNet-1K and 78.29% on CIFAR-100 with a ResNet-50 encoder while converging in just 200 epochs; (2) yields substantially clearer decision boundaries and semantic organization in the embedding space, as evidenced by KNN classification, hierarchical clustering results, and transfer-learning assessments; and (3) demonstrates superior performance in few-shot learning than supervised baseline and superior robustness across various augmentation strategies. Our code is available at https://github.com/ziwenwang28/VarContrast.

</details>

### PCA++: How Uniformity Induces Robustness to Background Noise in Contrastive Learning.
- **链接**: [arXiv:2511.12278](https://arxiv.org/abs/2511.12278) · 📚 被引 0
- **作者**: Mingqi Wu, Qiang Sun, Archer Y. Yang
- **🏷️ 机构**: McGill University, University of Toronto
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> High-dimensional data often contain low-dimensional signals obscured by structured background noise, which limits the effectiveness of standard PCA. Motivated by contrastive learning, we address the problem of recovering shared signal subspaces from positive pairs, paired observations sharing the same signal but differing in background. Our baseline, PCA+, uses alignment-only contrastive learning and succeeds when background variation is mild, but fails under strong noise or high-dimensional regimes. To address this, we introduce PCA++, a hard uniformity-constrained contrastive PCA that enforces identity covariance on projected features. PCA++ has a closed-form solution via a generalized eigenproblem, remains stable in high dimensions, and provably regularizes against background interference. We provide exact high-dimensional asymptotics in both fixed-aspect-ratio and growing-spike regimes, showing uniformity's role in robust signal recovery. Empirically, PCA++ outperforms standard PCA and alignment-only PCA+ on simulations, corrupted-MNIST, and single-cell transcriptomics, reliably recovering condition-invariant structure. More broadly, we clarify uniformity's role in contrastive learning, showing that explicit feature dispersion defends against structured noise and enhances robustness.

</details>

### The Complexity of Finding Local Optima in Contrastive Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/4c3f699b53a3b49982a8d7c99c161a2a-Abstract-Conference.html) · 📚 被引 0
- **作者**: Jingming Yan, Yiyuan Luo, Vaggos Chatziafratis, Ioannis Panageas, Parnian Shahkar, Stelios Stavroulakis
- **🏷️ 机构**: University of California, Irvine, University of California, Santa Cruz, UC Irvine
- **会议**: NeurIPS 2025

### Orthogonal Contrastive Learning for Multi-Representation fMRI Analysis.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/a81a1eabfb6cbece73ddd0e6a1645d67-Abstract-Conference.html) · 📚 被引 0
- **作者**: Tony Yousefnezhad
- **🏷️ 机构**: Learning by Machine
- **会议**: NeurIPS 2025

### DecoyDB: A Dataset for Graph Contrastive Learning in Protein-Ligand Binding Affinity Prediction.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/5482008bd0d451bb3ec69f966c925704-Abstract-Datasets_and_Benchmarks_Track.html) · 📚 被引 1
- **作者**: Yupu Zhang, Zelin Xu, Tingsong Xiao, Gustavo de M. Seabra, Yanjun Li, Chenglong Li et al.
- **🏷️ 机构**: University of Florida, Anhui University
- **会议**: NeurIPS 2025

### Negative Feedback Really Matters: Signed Dual-Channel Graph Contrastive Learning Framework for Recommendation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/9a92ea37efa0d290bd7015558166c056-Abstract-Conference.html) · 📚 被引 1
- **作者**: Leqi Zheng, Chaokun Wang, Zixin Song, Cheng Wu, Shannan Yan, Jiajun Zhang et al.
- **🏷️ 机构**: Tsinghua University, Tsinghua University, Tsinghua University, Institute of automation, Chinese academy of science, Chinese Academy of Sciences
- **会议**: NeurIPS 2025

## 跨领域论文（完整笔记在其他领域）

- CQ-DINO: Mitigating Gradient Dilution via Category Queries for Vast Vocabulary Object Detection. → [object-detection](../object-detection/Guideline%202025.md)
- CSPCL: Category Semantic Prior Contrastive Learning for Deformable DETR-Based Prohibited Item Detectors. → [object-detection](../object-detection/Guideline%202025.md)
- Hypergraph-Enhanced Contrastive Learning for Multi-View Clustering with Hyper-Laplacian Regularization. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
- SynCL: A Synergistic Training Strategy with Instance-Aware Contrastive Learning for End-to-End Multi-Camera 3D Tracking. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
- Generalized Contrastive Learning for Universal Multimodal Retrieval. → [multimodal](../multimodal/Guideline%202025.md)
- Continual Multimodal Contrastive Learning. → [multimodal](../multimodal/Guideline%202025.md)
- Confusion-Driven Self-Supervised Progressively Weighted Ensemble Learning for Non-Exemplar Class Incremental Learning. → [continual-learning](../continual-learning/Guideline%202025.md)
- Jasmine: Harnessing Diffusion Prior for Self-supervised Depth Estimation. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
