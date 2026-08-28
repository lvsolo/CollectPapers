# Self-supervised Vision — 2024 Guideline

> 领域: 视觉自监督学习（对比学习、MAE、DINO 系）
> 论文数: 44 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Self-Supervised Adversarial Training via Diverse Augmented Queries and Self-Supervised Double Perturbation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/4d65fc9de1051c382fd258dbafd8cde9-Abstract-Conference.html) · 📚 被引 0
- **作者**: Ruize Zhang, Sheng Tang, Juan Cao
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Understanding the Role of Equivariance in Self-supervised Learning.
- **链接**: [arXiv:2411.06508](https://arxiv.org/abs/2411.06508) · [代码](https://github.com/kaotty/Understanding-ESSL) · 📚 被引 4
- **作者**: Yifei Wang, Kaiwen Hu, Sharut Gupta, Ziyu Ye, Yisen Wang, Stefanie Jegelka
- **🏷️ 机构**: Peking University
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Contrastive learning has been a leading paradigm for self-supervised learning, but it is widely observed that it comes at the price of sacrificing useful features (\eg colors) by being invariant to data augmentations. Given this limitation, there has been a surge of interest in equivariant self-supervised learning (E-SSL) that learns features to be augmentation-aware. However, even for the simplest rotation prediction method, there is a lack of rigorous understanding of why, when, and how E-SSL learns useful features for downstream tasks. To bridge this gap between practice and theory, we establish an information-theoretic perspective to understand the generalization ability of E-SSL. In particular, we identify a critical explaining-away effect in E-SSL that creates a synergy between the equivariant and classification tasks. This synergy effect encourages models to extract class-relevant features to improve its equivariant prediction, which, in turn, benefits downstream tasks requiring semantic features. Based on this perspective, we theoretically analyze the influence of data transformations and reveal several principles for practical designs of E-SSL. Our theory not only aligns well with existing E-SSL methods but also sheds light on new directions by exploring the benefits of model equivariance. We believe that a theoretically grounded understanding on the role of equivariance would inspire more principled and advanced designs in this field. Code is available at https://github.com/kaotty/Understanding-ESSL.

</details>

### Learning from Pattern Completion: Self-supervised Controllable Generation.
- **链接**: [arXiv:2409.18694](https://arxiv.org/abs/2409.18694) · 📚 被引 1
- **作者**: Zhiqiang Chen, Guofan Fan, Jinying Gao, Lei Ma, Bo Lei, Tiejun Huang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The human brain exhibits a strong ability to spontaneously associate different visual attributes of the same or similar visual scene, such as associating sketches and graffiti with real-world visual objects, usually without supervising information. In contrast, in the field of artificial intelligence, controllable generation methods like ControlNet heavily rely on annotated training datasets such as depth maps, semantic segmentation maps, and poses, which limits the method's scalability. Inspired by the neural mechanisms that may contribute to the brain's associative power, specifically the cortical modularization and hippocampal pattern completion, here we propose a self-supervised controllable generation (SCG) framework. Firstly, we introduce an equivariant constraint to promote inter-module independence and intra-module correlation in a modular autoencoder network, thereby achieving functional specialization. Subsequently, based on these specialized modules, we employ a self-supervised pattern completion approach for controllable generation training. Experimental results demonstrate that the proposed modular autoencoder effectively achieves functional specialization, including the modular processing of color, brightness, and edge detection, and exhibits brain-like features including orientation selectivity, color antagonism, and center-surround receptive fields. Through self-supervised training, associative generation capabilities spontaneously emerge in SCG, demonstrating excellent generalization ability to various tasks such as associative generation on painting, sketches, and ancient graffiti. Compared to the previous representative method ControlNet, our proposed approach not only demonstrates superior robustness in more challenging high-noise scenarios but also possesses more promising scalability potential due to its self-supervised manner.Codes are released on Github and Gitee.

</details>

### Self-Supervised Alignment with Mutual Information: Learning to Follow Principles without Preference Labels.
- **链接**: [arXiv:2404.14313](https://arxiv.org/abs/2404.14313) · 📚 被引 4
- **作者**: Jan-Philipp Fränken, Eric Zelikman, Rafael Rafailov, Kanishk Gandhi, Tobias Gerstenberg, Noah D. Goodman
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> When prompting a language model (LM), users often expect the model to adhere to a set of behavioral principles across diverse tasks, such as producing insightful content while avoiding harmful or biased language. Instilling such principles (i.e., a constitution) into a model is resource-intensive, technically challenging, and generally requires human preference labels or examples. We introduce SAMI, an iterative algorithm that finetunes a pretrained language model (without requiring preference labels or demonstrations) to increase the conditional mutual information between constitutions and self-generated responses given queries from a dataset. On single-turn dialogue and summarization, a SAMI-trained mistral-7b outperforms the initial pretrained model, with win rates between 66% and 77%. Strikingly, it also surpasses an instruction-finetuned baseline (mistral-7b-instruct) with win rates between 55% and 57% on single-turn dialogue. SAMI requires a model that writes the principles. To avoid dependence on strong models for writing principles, we align a strong pretrained model (mixtral-8x7b) using constitutions written by a weak instruction-finetuned model (mistral-7b-instruct), achieving a 65% win rate on summarization. Finally, we investigate whether SAMI generalizes to diverse summarization principles (e.g., "summaries should be scientific") and scales to stronger models (llama3-70b), finding that it achieves win rates of up to 68% for learned and 67% for held-out principles compared to the base model. Our results show that a pretrained LM can learn to follow constitutions without using preference labels, demonstrations, or human oversight.

</details>

### In-Context Symmetries: Self-Supervised Learning through Contextual World Models.
- **链接**: [arXiv:2405.18193](https://arxiv.org/abs/2405.18193) · 📚 被引 0
- **作者**: Sharut Gupta, Chenyu Wang, Yifei Wang, Tommi S. Jaakkola, Stefanie Jegelka
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> At the core of self-supervised learning for vision is the idea of learning invariant or equivariant representations with respect to a set of data transformations. This approach, however, introduces strong inductive biases, which can render the representations fragile in downstream tasks that do not conform to these symmetries. In this work, drawing insights from world models, we propose to instead learn a general representation that can adapt to be invariant or equivariant to different transformations by paying attention to context -- a memory module that tracks task-specific states, actions, and future states. Here, the action is the transformation, while the current and future states respectively represent the input's representation before and after the transformation. Our proposed algorithm, Contextual Self-Supervised Learning (ContextSSL), learns equivariance to all transformations (as opposed to invariance). In this way, the model can learn to encode all relevant features as general representations while having the versatility to tail down to task-wise symmetries when given a few examples as the context. Empirically, we demonstrate significant performance gains over existing methods on equivariance-related tasks, supported by both qualitative and quantitative evaluations.

</details>

### Preventing Dimensional Collapse in Self-Supervised Learning via Orthogonality Regularization.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/ad7922fd4650f8aba5d8b067e622ca84-Abstract-Conference.html) · 📚 被引 4
- **作者**: Junlin He, Jinxiao Du, Wei Ma
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Flexible mapping of abstract domains by grid cells via self-supervised extraction and projection of generalized velocity signals.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/9b333cc1c9eb36e479b27f8c19f0873c-Abstract-Conference.html) · 📚 被引 1
- **作者**: Abhiram Iyer, Sarthak Chandra, Sugandha Sharma, Ila Fiete
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Med-Real2Sim: Non-Invasive Medical Digital Twins using Physics-Informed Self-Supervised Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/0b081a44ed0b8c0c4aa6bd886a60bea4-Abstract-Conference.html)
- **作者**: Keying Kuang, Frances Dean, Jack B. Jedlicki, David Ouyang, Anthony Philippakis, David A. Sontag et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Resource-Aware Federated Self-Supervised Learning with Global Class Representations.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/13707aad517ddd6c09ea02e0f55e1e7a-Abstract-Conference.html) · 📚 被引 5
- **作者**: Mingyi Li, Xiao Zhang, Qi Wang, Tengfei Liu, Ruofan Wu, Weiqiang Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Return of Unconditional Generation: A Self-supervised Representation Generation Method.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/e304d374c85e385eb217ed4a025b6b63-Abstract-Conference.html) · 📚 被引 5
- **作者**: Tianhong Li, Dina Katabi, Kaiming He
- **🏷️ 机构**: MIT
- **会议**: NeurIPS 2024

### bit2bit: 1-bit quanta video reconstruction via self-supervised photon prediction.
- **链接**: [arXiv:2410.23247](https://arxiv.org/abs/2410.23247) · 📚 被引 1
- **作者**: Yehe Liu, Alexander Krull, Hector Basevi, Ales Leonardis, Michael W. Jenkins
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Quanta image sensors, such as SPAD arrays, are an emerging sensor technology, producing 1-bit arrays representing photon detection events over exposures as short as a few nanoseconds. In practice, raw data are post-processed using heavy spatiotemporal binning to create more useful and interpretable images at the cost of degrading spatiotemporal resolution. In this work, we propose bit2bit, a new method for reconstructing high-quality image stacks at the original spatiotemporal resolution from sparse binary quanta image data. Inspired by recent work on Poisson denoising, we developed an algorithm that creates a dense image sequence from sparse binary photon data by predicting the photon arrival location probability distribution. However, due to the binary nature of the data, we show that the assumption of a Poisson distribution is inadequate. Instead, we model the process with a Bernoulli lattice process from the truncated Poisson. This leads to the proposal of a novel self-supervised solution based on a masked loss function. We evaluate our method using both simulated and real data. On simulated data from a conventional video, we achieve 34.35 mean PSNR with extremely photon-sparse binary input (<0.06 photons per pixel per frame). We also present a novel dataset containing a wide range of real SPAD high-speed videos under various challenging imaging conditions. The scenes cover strong/weak ambient light, strong motion, ultra-fast events, etc., which will be made available to the community, on which we demonstrate the promise of our approach. Both reconstruction quality and throughput substantially surpass the state-of-the-art methods (e.g., Quanta Burst Photography (QBP)). Our approach significantly enhances the visualization and usability of the data, enabling the application of existing analysis techniques.

</details>

### CA-SSLR: Condition-Aware Self-Supervised Learning Representation for Generalized Speech Processing.
- **链接**: [arXiv:2412.04425](https://arxiv.org/abs/2412.04425)
- **作者**: Yen-Ju Lu, Jing Liu, Thomas Thebaud, Laureano Moro-Velázquez, Ariya Rastrow, Najim Dehak et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce Condition-Aware Self-Supervised Learning Representation (CA-SSLR), a generalist conditioning model broadly applicable to various speech-processing tasks. Compared to standard fine-tuning methods that optimize for downstream models, CA-SSLR integrates language and speaker embeddings from earlier layers, making the SSL model aware of the current language and speaker context. This approach reduces the reliance on input audio features while preserving the integrity of the base SSLR. CA-SSLR improves the model's capabilities and demonstrates its generality on unseen tasks with minimal task-specific tuning. Our method employs linear modulation to dynamically adjust internal representations, enabling fine-grained adaptability without significantly altering the original model behavior. Experiments show that CA-SSLR reduces the number of trainable parameters, mitigates overfitting, and excels in under-resourced and unseen tasks. Specifically, CA-SSLR achieves a 10% relative reduction in LID errors, a 37% improvement in ASR CER on the ML-SUPERB benchmark, and a 27% decrease in SV EER on VoxCeleb-1, demonstrating its effectiveness.

</details>

### QueST: Self-Supervised Skill Abstractions for Learning Continuous Control.
- **链接**: [arXiv:2407.15840](https://arxiv.org/abs/2407.15840)
- **作者**: Atharva Mete, Haotian Xue, Albert Wilcox, Yongxin Chen, Animesh Garg
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Generalization capabilities, or rather a lack thereof, is one of the most important unsolved problems in the field of robot learning, and while several large scale efforts have set out to tackle this problem, unsolved it remains. In this paper, we hypothesize that learning temporal action abstractions using latent variable models (LVMs), which learn to map data to a compressed latent space and back, is a promising direction towards low-level skills that can readily be used for new tasks. Although several works have attempted to show this, they have generally been limited by architectures that do not faithfully capture shareable representations. To address this we present Quantized Skill Transformer (QueST), which learns a larger and more flexible latent encoding that is more capable of modeling the breadth of low-level skills necessary for a variety of tasks. To make use of this extra flexibility, QueST imparts causal inductive bias from the action sequence data into the latent space, leading to more semantically useful and transferable representations. We compare to state-of-the-art imitation learning and LVM baselines and see that QueST's architecture leads to strong performance on several multitask and few-shot learning benchmarks. Further results and videos are available at https://quest-model.github.io/

</details>

### Revisiting Self-Supervised Heterogeneous Graph Learning from Spectral Clustering Perspective.
- **链接**: [arXiv:2412.00742](https://arxiv.org/abs/2412.00742) · 📚 被引 3
- **作者**: Yujie Mo, Zhihe Lu, Runpeng Yu, Xiaofeng Zhu, Xinchao Wang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised heterogeneous graph learning (SHGL) has shown promising potential in diverse scenarios. However, while existing SHGL methods share a similar essential with clustering approaches, they encounter two significant limitations: (i) noise in graph structures is often introduced during the message-passing process to weaken node representations, and (ii) cluster-level information may be inadequately captured and leveraged, diminishing the performance in downstream tasks. In this paper, we address these limitations by theoretically revisiting SHGL from the spectral clustering perspective and introducing a novel framework enhanced by rank and dual consistency constraints. Specifically, our framework incorporates a rank-constrained spectral clustering method that refines the affinity matrix to exclude noise effectively. Additionally, we integrate node-level and cluster-level consistency constraints that concurrently capture invariant and clustering information to facilitate learning in downstream tasks. We theoretically demonstrate that the learned representations are divided into distinct partitions based on the number of classes and exhibit enhanced generalization ability across tasks. Experimental results affirm the superiority of our method, showcasing remarkable improvements in several downstream tasks compared to existing methods.

</details>

### Connecting Joint-Embedding Predictive Architecture with Contrastive Self-supervised Learning.
- **链接**: [arXiv:2410.19560](https://arxiv.org/abs/2410.19560) · 📚 被引 8
- **作者**: Shentong Mo, Peter Tong
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In recent advancements in unsupervised visual representation learning, the Joint-Embedding Predictive Architecture (JEPA) has emerged as a significant method for extracting visual features from unlabeled imagery through an innovative masking strategy. Despite its success, two primary limitations have been identified: the inefficacy of Exponential Moving Average (EMA) from I-JEPA in preventing entire collapse and the inadequacy of I-JEPA prediction in accurately learning the mean of patch representations. Addressing these challenges, this study introduces a novel framework, namely C-JEPA (Contrastive-JEPA), which integrates the Image-based Joint-Embedding Predictive Architecture with the Variance-Invariance-Covariance Regularization (VICReg) strategy. This integration is designed to effectively learn the variance/covariance for preventing entire collapse and ensuring invariance in the mean of augmented views, thereby overcoming the identified limitations. Through empirical and theoretical evaluations, our work demonstrates that C-JEPA significantly enhances the stability and quality of visual representation learning. When pre-trained on the ImageNet-1K dataset, C-JEPA exhibits rapid and improved convergence in both linear probing and fine-tuning performance metrics.

</details>

### You Don't Need Domain-Specific Data Augmentations When Scaling Self-Supervised Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/d2964af7bd4e891297a39dc9085fa754-Abstract-Conference.html) · 📚 被引 2
- **作者**: Théo Moutakanni, Maxime Oquab, Marc Szafraniec, Maria Vakalopoulou, Piotr Bojanowski
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Pseudo-Siamese Blind-spot Transformers for Self-Supervised Real-World Denoising.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/19305d2dbcc81c44d4a0120e7569856e-Abstract-Conference.html) · 📚 被引 3
- **作者**: Yuhui Quan, Tianxiang Zheng, Hui Ji
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### No Train, all Gain: Self-Supervised Gradients Improve Deep Frozen Representations.
- **链接**: [arXiv:2407.10964](https://arxiv.org/abs/2407.10964) · 📚 被引 1
- **作者**: Walter Simoncini, Andrei Bursuc, Spyridon Gidaris, Yuki M. Asano
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper introduces FUNGI, Features from UNsupervised GradIents, a method to enhance the features of transformer encoders by leveraging self-supervised gradients. Our method is simple: given any pretrained model, we first compute gradients from various self-supervised objectives for each input. These gradients are projected to a lower dimension and then concatenated with the model's output embedding. The resulting features are evaluated on k-nearest neighbor classification over 11 datasets from vision, 5 from natural language processing, and 2 from audio. Across backbones spanning various sizes and pretraining strategies, FUNGI features provide consistent performance improvements over the embeddings. We also show that using FUNGI features can benefit linear classification, clustering and image retrieval, and that they significantly improve the retrieval-based in-context scene understanding abilities of pretrained models, for example improving upon DINO by +17% for semantic segmentation - without any training.

</details>

### SHMT: Self-supervised Hierarchical Makeup Transfer via Latent Diffusion Models.
- **链接**: [arXiv:2412.11058](https://arxiv.org/abs/2412.11058) · [代码](https://github.com/Snowfallingplum/SHMT) · 📚 被引 5
- **作者**: Zhaoyang Sun, Shengwu Xiong, Yaxiong Chen, Fei Du, Weihua Chen, Fan Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper studies the challenging task of makeup transfer, which aims to apply diverse makeup styles precisely and naturally to a given facial image. Due to the absence of paired data, current methods typically synthesize sub-optimal pseudo ground truths to guide the model training, resulting in low makeup fidelity. Additionally, different makeup styles generally have varying effects on the person face, but existing methods struggle to deal with this diversity. To address these issues, we propose a novel Self-supervised Hierarchical Makeup Transfer (SHMT) method via latent diffusion models. Following a "decoupling-and-reconstruction" paradigm, SHMT works in a self-supervised manner, freeing itself from the misguidance of imprecise pseudo-paired data. Furthermore, to accommodate a variety of makeup styles, hierarchical texture details are decomposed via a Laplacian pyramid and selectively introduced to the content representation. Finally, we design a novel Iterative Dual Alignment (IDA) module that dynamically adjusts the injection condition of the diffusion model, allowing the alignment errors caused by the domain gap between content and makeup representations to be corrected. Extensive quantitative and qualitative analyses demonstrate the effectiveness of our method. Our code is available at \url{https://github.com/Snowfallingplum/SHMT}.

</details>

### DiffNorm: Self-Supervised Normalization for Non-autoregressive Speech-to-speech Translation.
- **链接**: [arXiv:2405.13274](https://arxiv.org/abs/2405.13274) · 📚 被引 1
- **作者**: Weiting Tan, Jingyu Zhang, Lingfeng Shen, Daniel Khashabi, Philipp Koehn
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Non-autoregressive Transformers (NATs) are recently applied in direct speech-to-speech translation systems, which convert speech across different languages without intermediate text data. Although NATs generate high-quality outputs and offer faster inference than autoregressive models, they tend to produce incoherent and repetitive results due to complex data distribution (e.g., acoustic and linguistic variations in speech). In this work, we introduce DiffNorm, a diffusion-based normalization strategy that simplifies data distributions for training NAT models. After training with a self-supervised noise estimation objective, DiffNorm constructs normalized target data by denoising synthetically corrupted speech features. Additionally, we propose to regularize NATs with classifier-free guidance, improving model robustness and translation quality by randomly dropping out source information during training. Our strategies result in a notable improvement of about +7 ASR-BLEU for English-Spanish (En-Es) and +2 ASR-BLEU for English-French (En-Fr) translations on the CVSS benchmark, while attaining over 14x speedup for En-Es and 5x speedup for En-Fr translations compared to autoregressive baselines.

</details>

### Uncovering the Redundancy in Graph Self-supervised Learning Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/b2c4b7d34b3d96b9dc12f7bce424b7ae-Abstract-Conference.html) · 📚 被引 1
- **作者**: Zhibiao Wang, Xiao Wang, Haoyue Deng, Nian Liu, Shirui Pan, Chunming Hu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Contrastive-Equivariant Self-Supervised Learning Improves Alignment with Primate Visual Area IT.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/ae28c7bc9414ffd8ffd2b3d454e6ef3e-Abstract-Conference.html) · 📚 被引 0
- **作者**: Thomas E. Yerxa, Jenelle Feather, Eero P. Simoncelli, SueYeon Chung
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Self-supervised Transformation Learning for Equivariant Representations.
- **链接**: [arXiv:2501.08712](https://arxiv.org/abs/2501.08712) · [代码](https://github.com/jaemyung-u/stl) · 📚 被引 1
- **作者**: Jaemyung Yu, Jaehyun Choi, Dong-Jae Lee, Hyeong Gwon Hong, Junmo Kim
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Unsupervised representation learning has significantly advanced various machine learning tasks. In the computer vision domain, state-of-the-art approaches utilize transformations like random crop and color jitter to achieve invariant representations, embedding semantically the same inputs despite transformations. However, this can degrade performance in tasks requiring precise features, such as localization or flower classification. To address this, recent research incorporates equivariant representation learning, which captures transformation-sensitive information. However, current methods depend on transformation labels and thus struggle with interdependency and complex transformations. We propose Self-supervised Transformation Learning (STL), replacing transformation labels with transformation representations derived from image pairs. The proposed method ensures transformation representation is image-invariant and learns corresponding equivariant transformations, enhancing performance without increased batch complexity. We demonstrate the approach's effectiveness across diverse classification and detection tasks, outperforming existing methods in 7 out of 11 benchmarks and excelling in detection. By integrating complex transformations like AugMix, unusable by prior equivariant methods, this approach enhances performance across tasks, underscoring its adaptability and resilience. Additionally, its compatibility with various base models highlights its flexibility and broad applicability. The code is available at https://github.com/jaemyung-u/stl.

</details>

### Cross-Scale Self-Supervised Blind Image Deblurring via Implicit Neural Representation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/0d67ec04032cccf4a21d04c0ae4ab268-Abstract-Conference.html) · 📚 被引 4
- **作者**: Tianjing Zhang, Yuhui Quan, Hui Ji
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### A probability contrastive learning framework for 3D molecular representation learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/6adaf0cbeba11705d4ea67a62044f63d-Abstract-Conference.html) · 📚 被引 1
- **作者**: Jiayu Qin, Jian Chen, Rohan Sharma, Jingchen Sun, Changyou Chen
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Leveraging Contrastive Learning for Enhanced Node Representations in Tokenized Graph Transformers.
- **链接**: [arXiv:2406.19258](https://arxiv.org/abs/2406.19258) · 📚 被引 5
- **作者**: Jinsong Chen, Hanpeng Liu, John E. Hopcroft, Kun He
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While tokenized graph Transformers have demonstrated strong performance in node classification tasks, their reliance on a limited subset of nodes with high similarity scores for constructing token sequences overlooks valuable information from other nodes, hindering their ability to fully harness graph information for learning optimal node representations. To address this limitation, we propose a novel graph Transformer called GCFormer. Unlike previous approaches, GCFormer develops a hybrid token generator to create two types of token sequences, positive and negative, to capture diverse graph information. And a tailored Transformer-based backbone is adopted to learn meaningful node representations from these generated token sequences. Additionally, GCFormer introduces contrastive learning to extract valuable information from both positive and negative token sequences, enhancing the quality of learned node representations. Extensive experimental results across various datasets, including homophily and heterophily graphs, demonstrate the superiority of GCFormer in node classification, when compared to representative graph neural networks (GNNs) and graph Transformers.

</details>

### Embedding Dimension of Contrastive Learning and k-Nearest Neighbors.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/487c9d6ef55e73aa9dfd4b48fe3713a6-Abstract-Conference.html) · 📚 被引 0
- **作者**: Dmitrii Avdiukhin, Vaggos Chatziafratis, Orr Fischer, Grigory Yaroslavtsev
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Causal Contrastive Learning for Counterfactual Regression Over Time.
- **链接**: [arXiv:2406.00535](https://arxiv.org/abs/2406.00535) · 📚 被引 0
- **作者**: Mouad El Bouchattaoui, Myriam Tami, Benoit Lepetit, Paul-Henry Cournède
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Estimating treatment effects over time holds significance in various domains, including precision medicine, epidemiology, economy, and marketing. This paper introduces a unique approach to counterfactual regression over time, emphasizing long-term predictions. Distinguishing itself from existing models like Causal Transformer, our approach highlights the efficacy of employing RNNs for long-term forecasting, complemented by Contrastive Predictive Coding (CPC) and Information Maximization (InfoMax). Emphasizing efficiency, we avoid the need for computationally expensive transformers. Leveraging CPC, our method captures long-term dependencies in the presence of time-varying confounders. Notably, recent models have disregarded the importance of invertible representation, compromising identification assumptions. To remedy this, we employ the InfoMax principle, maximizing a lower bound of mutual information between sequence data and its representation. Our method achieves state-of-the-art counterfactual estimation results using both synthetic and real-world data, marking the pioneering incorporation of Contrastive Predictive Encoding in causal inference.

</details>

### RouterDC: Query-Based Router by Dual Contrastive Learning for Assembling Large Language Models.
- **链接**: [arXiv:2409.19886](https://arxiv.org/abs/2409.19886) · [代码](https://github.com/shuhao02/RouterDC)
- **作者**: Shuhao Chen, Weisen Jiang, Baijiong Lin, James T. Kwok, Yu Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent works show that assembling multiple off-the-shelf large language models (LLMs) can harness their complementary abilities. To achieve this, routing is a promising method, which learns a router to select the most suitable LLM for each query. However, existing routing models are ineffective when multiple LLMs perform well for a query. To address this problem, in this paper, we propose a method called query-based Router by Dual Contrastive learning (RouterDC). The RouterDC model consists of an encoder and LLM embeddings, and we propose two contrastive learning losses to train the RouterDC model. Experimental results show that RouterDC is effective in assembling LLMs and largely outperforms individual top-performing LLMs as well as existing routing methods on both in-distribution (+2.76\%) and out-of-distribution (+1.90\%) tasks. Source code is available at https://github.com/shuhao02/RouterDC.

</details>

### Your contrastive learning problem is secretly a distribution alignment problem.
- **链接**: [arXiv:2502.20141](https://arxiv.org/abs/2502.20141) · 📚 被引 5
- **作者**: Zihao Chen, Chi-Heng Lin, Ran Liu, Jingyun Xiao, Eva L. Dyer
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite the success of contrastive learning (CL) in vision and language, its theoretical foundations and mechanisms for building representations remain poorly understood. In this work, we build connections between noise contrastive estimation losses widely used in CL and distribution alignment with entropic optimal transport (OT). This connection allows us to develop a family of different losses and multistep iterative variants for existing CL methods. Intuitively, by using more information from the distribution of latents, our approach allows a more distribution-aware manipulation of the relationships within augmented sample sets. We provide theoretical insights and experimental evidence demonstrating the benefits of our approach for {\em generalized contrastive alignment}. Through this framework, it is possible to leverage tools in OT to build unbalanced losses to handle noisy views and customize the representation space by changing the constraints on alignment. By reframing contrastive learning as an alignment problem and leveraging existing optimization tools for OT, our work provides new insights and connections between different self-supervised learning models in addition to new tools that can be more easily adapted to incorporate domain knowledge into learning.

</details>

### DeTeCtive: Detecting AI-generated Text via Multi-Level Contrastive Learning.
- **链接**: [arXiv:2410.20964](https://arxiv.org/abs/2410.20964) · [代码](https://github.com/heyongxin233/DeTeCtive) · 📚 被引 12
- **作者**: Xun Guo, Yongxin He, Shan Zhang, Ting Zhang, Wanquan Feng, Haibin Huang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Current techniques for detecting AI-generated text are largely confined to manual feature crafting and supervised binary classification paradigms. These methodologies typically lead to performance bottlenecks and unsatisfactory generalizability. Consequently, these methods are often inapplicable for out-of-distribution (OOD) data and newly emerged large language models (LLMs). In this paper, we revisit the task of AI-generated text detection. We argue that the key to accomplishing this task lies in distinguishing writing styles of different authors, rather than simply classifying the text into human-written or AI-generated text. To this end, we propose DeTeCtive, a multi-task auxiliary, multi-level contrastive learning framework. DeTeCtive is designed to facilitate the learning of distinct writing styles, combined with a dense information retrieval pipeline for AI-generated text detection. Our method is compatible with a range of text encoders. Extensive experiments demonstrate that our method enhances the ability of various text encoders in detecting AI-generated text across multiple benchmarks and achieves state-of-the-art results. Notably, in OOD zero-shot evaluation, our method outperforms existing approaches by a large margin. Moreover, we find our method boasts a Training-Free Incremental Adaptation (TFIA) capability towards OOD data, further enhancing its efficacy in OOD detection scenarios. We will open-source our code and models in hopes that our work will spark new thoughts in the field of AI-generated text detection, ensuring safe application of LLMs and enhancing compliance. Our code is available at https://github.com/heyongxin233/DeTeCtive.

</details>

### Exploitation of a Latent Mechanism in Graph Contrastive Learning: Representation Scattering.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/d0ffb35aaa7faa894afe5060c694d674-Abstract-Conference.html) · 📚 被引 9
- **作者**: Dongxiao He, Lianze Shan, Jitao Zhao, Hengrui Zhang, Zhen Wang, Weixiong Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Toward a Well-Calibrated Discrimination via Survival Outcome-Aware Contrastive Learning.
- **链接**: [arXiv:2410.11340](https://arxiv.org/abs/2410.11340) · 📚 被引 2
- **作者**: Dongjoon Lee, Hyeryn Park, Changhee Lee
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Previous deep learning approaches for survival analysis have primarily relied on ranking losses to improve discrimination performance, which often comes at the expense of calibration performance. To address such an issue, we propose a novel contrastive learning approach specifically designed to enhance discrimination \textit{without} sacrificing calibration. Our method employs weighted sampling within a contrastive learning framework, assigning lower penalties to samples with similar survival outcomes. This aligns well with the assumption that patients with similar event times share similar clinical statuses. Consequently, when augmented with the commonly used negative log-likelihood loss, our approach significantly improves discrimination performance without directly manipulating the model outputs, thereby achieving better calibration. Experiments on multiple real-world clinical datasets demonstrate that our method outperforms state-of-the-art deep survival models in both discrimination and calibration. Through comprehensive ablation studies, we further validate the effectiveness of our approach through quantitative and qualitative analyses.

</details>

### Hierarchical Object-Aware Dual-Level Contrastive Learning for Domain Generalized Stereo Matching.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/ee5bb72130c332c3d4bf8d231e617506-Abstract-Conference.html) · 📚 被引 3
- **作者**: Yikun Miao, Meiqing Wu, Siew Kei Lam, Changsheng Li, Thambipillai Srikanthan
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Easy Regional Contrastive Learning of Expressive Fashion Representations.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/2492288f6878e6f99124b362604e58f5-Abstract-Conference.html) · 📚 被引 1
- **作者**: Daiqing Qi, Handong Zhao, Sheng Li
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Efficient Availability Attacks against Supervised and Contrastive Learning Simultaneously.
- **链接**: [arXiv:2402.04010](https://arxiv.org/abs/2402.04010) · 📚 被引 1
- **作者**: Yihan Wang, Yifan Zhu, Xiao-Shan Gao
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Availability attacks can prevent the unauthorized use of private data and commercial datasets by generating imperceptible noise and making unlearnable examples before release. Ideally, the obtained unlearnability prevents algorithms from training usable models. When supervised learning (SL) algorithms have failed, a malicious data collector possibly resorts to contrastive learning (CL) algorithms to bypass the protection. Through evaluation, we have found that most of the existing methods are unable to achieve both supervised and contrastive unlearnability, which poses risks to data protection. Different from recent methods based on contrastive error minimization, we employ contrastive-like data augmentations in supervised error minimization or maximization frameworks to obtain attacks effective for both SL and CL. Our proposed AUE and AAP attacks achieve state-of-the-art worst-case unlearnability across SL and CL algorithms with less computation consumption, showcasing prospects in real-world applications.

</details>

### TrajCLIP: Pedestrian trajectory prediction method using contrastive learning and idempotent networks.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/8cd23ec650193ea59a249dbdfdde18cb-Abstract-Conference.html) · 📚 被引 1
- **作者**: Pengfei Yao, Yinglong Zhu, Huikun Bi, Tianlu Mao, Zhaoqi Wang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Continuous Contrastive Learning for Long-Tailed Semi-Supervised Recognition.
- **链接**: [arXiv:2410.06109](https://arxiv.org/abs/2410.06109) · [代码](https://github.com/zhouzihao11/CCL) · 📚 被引 3
- **作者**: Zi-Hao Zhou, Siyuan Fang, Zi-Jing Zhou, Tong Wei, Yuanyu Wan, Min-Ling Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Long-tailed semi-supervised learning poses a significant challenge in training models with limited labeled data exhibiting a long-tailed label distribution. Current state-of-the-art LTSSL approaches heavily rely on high-quality pseudo-labels for large-scale unlabeled data. However, these methods often neglect the impact of representations learned by the neural network and struggle with real-world unlabeled data, which typically follows a different distribution than labeled data. This paper introduces a novel probabilistic framework that unifies various recent proposals in long-tail learning. Our framework derives the class-balanced contrastive loss through Gaussian kernel density estimation. We introduce a continuous contrastive learning method, CCL, extending our framework to unlabeled data using reliable and smoothed pseudo-labels. By progressively estimating the underlying label distribution and optimizing its alignment with model predictions, we tackle the diverse distribution of unlabeled data in real-world scenarios. Extensive experiments across multiple datasets with varying unlabeled data distributions demonstrate that CCL consistently outperforms prior state-of-the-art methods, achieving over 4% improvement on the ImageNet-127 dataset. Our source code is available at https://github.com/zhouzihao11/CCL

</details>

### S-MolSearch: 3D Semi-supervised Contrastive Learning for Bioactive Molecule Search.
- **链接**: [arXiv:2409.07462](https://arxiv.org/abs/2409.07462) · 📚 被引 0
- **作者**: Gengmo Zhou, Zhen Wang, Feng Yu, Guolin Ke, Zhewei Wei, Zhifeng Gao
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Virtual Screening is an essential technique in the early phases of drug discovery, aimed at identifying promising drug candidates from vast molecular libraries. Recently, ligand-based virtual screening has garnered significant attention due to its efficacy in conducting extensive database screenings without relying on specific protein-binding site information. Obtaining binding affinity data for complexes is highly expensive, resulting in a limited amount of available data that covers a relatively small chemical space. Moreover, these datasets contain a significant amount of inconsistent noise. It is challenging to identify an inductive bias that consistently maintains the integrity of molecular activity during data augmentation. To tackle these challenges, we propose S-MolSearch, the first framework to our knowledge, that leverages molecular 3D information and affinity information in semi-supervised contrastive learning for ligand-based virtual screening. Drawing on the principles of inverse optimal transport, S-MolSearch efficiently processes both labeled and unlabeled data, training molecular structural encoders while generating soft labels for the unlabeled data. This design allows S-MolSearch to adaptively utilize unlabeled data within the learning process. Empirically, S-MolSearch demonstrates superior performance on widely-used benchmarks LIT-PCBA and DUD-E. It surpasses both structure-based and ligand-based virtual screening methods for AUROC, BEDROC and EF.

</details>

### Unified Graph Augmentations for Generalized Contrastive Learning on Graphs.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/41efc12982eca6f8bb5e48dc3a84b843-Abstract-Conference.html) · 📚 被引 3
- **作者**: Jiaming Zhuo, Yintong Lu, Hui Ning, Kun Fu, Bingxin Niu, Dongxiao He et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

## 跨领域论文（完整笔记在其他领域）

- QUEST: Quadruple Multimodal Contrastive Learning with Constraints and Self-Penalization. → [multimodal](../multimodal/Guideline%202024.md)
- CLIPLoss and Norm-Based Data Selection Methods for Multimodal Contrastive Learning. → [multimodal](../multimodal/Guideline%202024.md)
- Long-tailed Object Detection Pretraining: Dynamic Rebalancing Contrastive Learning with Dual Reconstruction. → [object-detection](../object-detection/Guideline%202024.md)
- On the Comparison between Multi-modal and Single-modal Contrastive Learning. → [multimodal](../multimodal/Guideline%202024.md)
