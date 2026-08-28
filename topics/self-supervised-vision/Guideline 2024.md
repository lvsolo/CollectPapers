# Self-supervised Vision — 2024 Guideline

> 领域: 视觉自监督学习（对比学习、MAE、DINO 系）
> 论文数: 51 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### SOHES: Self-supervised Open-world Hierarchical Entity Segmentation.
- **链接**: [arXiv:2404.12386](https://arxiv.org/abs/2404.12386)
- **作者**: Shengcao Cao, Jiuxiang Gu, Jason Kuen, Hao Tan, Ruiyi Zhang, Handong Zhao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-world entity segmentation, as an emerging computer vision task, aims at segmenting entities in images without being restricted by pre-defined classes, offering impressive generalization capabilities on unseen images and concepts. Despite its promise, existing entity segmentation methods like Segment Anything Model (SAM) rely heavily on costly expert annotators. This work presents Self-supervised Open-world Hierarchical Entity Segmentation (SOHES), a novel approach that eliminates the need for human annotations. SOHES operates in three phases: self-exploration, self-instruction, and self-correction. Given a pre-trained self-supervised representation, we produce abundant high-quality pseudo-labels through visual feature clustering. Then, we train a segmentation model on the pseudo-labels, and rectify the noises in pseudo-labels via a teacher-student mutual-learning procedure. Beyond segmenting entities, SOHES also captures their constituent parts, providing a hierarchical understanding of visual entities. Using raw images as the sole training data, our method achieves unprecedented performance in self-supervised open-world segmentation, marking a significant milestone towards high-quality open-world entity segmentation in the absence of human-annotated masks. Project page: https://SOHES-ICLR.github.io.

</details>

### Self-Guided Masked Autoencoders for Domain-Agnostic Self-Supervised Learning.
- **链接**: [arXiv:2402.14789](https://arxiv.org/abs/2402.14789)
- **作者**: Johnathan Xie, Yoonho Lee, Annie S. Chen, Chelsea Finn
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning excels in learning representations from large amounts of unlabeled data, demonstrating success across multiple data modalities. Yet, extending self-supervised learning to new modalities is non-trivial because the specifics of existing methods are tailored to each domain, such as domain-specific augmentations which reflect the invariances in the target task. While masked modeling is promising as a domain-agnostic framework for self-supervised learning because it does not rely on input augmentations, its mask sampling procedure remains domain-specific. We present Self-guided Masked Autoencoders (SMA), a fully domain-agnostic masked modeling method. SMA trains an attention based model using a masked modeling objective, by learning masks to sample without any domain-specific assumptions. We evaluate SMA on three self-supervised learning benchmarks in protein biology, chemical property prediction, and particle physics. We find SMA is capable of learning representations without domain-specific knowledge and achieves state-of-the-art performance on these three benchmarks.

</details>

### Waxing-and-Waning: a Generic Similarity-based Framework for Efficient Self-Supervised Learning.
- **链接**: [出版页](https://openreview.net/forum?id=TilcG5C8bN)
- **作者**: Sheng Li, Chao Wu, Ao Li, Yanzhi Wang, Xulong Tang, Geng Yuan
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### Neural Spectral Methods: Self-supervised learning in the spectral domain.
- **链接**: [出版页](https://openreview.net/forum?id=2DbVeuoa6a)
- **作者**: Yiheng Du, Nithin Chalapathi, Aditi S. Krishnapriyan
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### Rethinking the Uniformity Metric in Self-Supervised Learning.
- **链接**: [出版页](https://openreview.net/forum?id=3pf2hEdu8B)
- **作者**: Xianghong Fang, Jian Li, Qiang Sun, Benyou Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### Self-Supervised Speech Quality Estimation and Enhancement Using Only Clean Speech.
- **链接**: [出版页](https://openreview.net/forum?id=ale56Ya59q)
- **作者**: Szu-Wei Fu, Kuo-Hsuan Hung, Yu Tsao, Yu-Chiang Frank Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### Self-supervised Pocket Pretraining via Protein Fragment-Surroundings Alignment.
- **链接**: [出版页](https://openreview.net/forum?id=uMAujpVi9m)
- **作者**: Bowen Gao, Yinjun Jia, Yuanle Mo, Yuyan Ni, Wei-Ying Ma, Zhi-Ming Ma et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### LDReg: Local Dimensionality Regularized Self-Supervised Learning.
- **链接**: [出版页](https://openreview.net/forum?id=oZyAqjAjJW)
- **作者**: Hanxun Huang, Ricardo J. G. B. Campello, Sarah Monazam Erfani, Xingjun Ma, Michael E. Houle, James Bailey
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### HypeBoy: Generative Self-Supervised Representation Learning on Hypergraphs.
- **链接**: [arXiv:2404.00638](https://arxiv.org/abs/2404.00638)
- **作者**: Sunwoo Kim, Shinhwan Kang, Fanchen Bu, Soo Yong Lee, Jaemin Yoo, Kijung Shin
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Hypergraphs are marked by complex topology, expressing higher-order interactions among multiple nodes with hyperedges, and better capturing the topology is essential for effective representation learning. Recent advances in generative self-supervised learning (SSL) suggest that hypergraph neural networks learned from generative self supervision have the potential to effectively encode the complex hypergraph topology. Designing a generative SSL strategy for hypergraphs, however, is not straightforward. Questions remain with regard to its generative SSL task, connection to downstream tasks, and empirical properties of learned representations. In light of the promises and challenges, we propose a novel generative SSL strategy for hypergraphs. We first formulate a generative SSL task on hypergraphs, hyperedge filling, and highlight its theoretical connection to node classification. Based on the generative SSL task, we propose a hypergraph SSL method, HypeBoy. HypeBoy learns effective general-purpose hypergraph representations, outperforming 16 baseline methods across 11 benchmark datasets.

</details>

### CrIBo: Self-Supervised Learning via Cross-Image Object-Level Bootstrapping.
- **链接**: [arXiv:2310.07855](https://arxiv.org/abs/2310.07855) · [代码](https://github.com/tileb1/CrIBo)
- **作者**: Tim Lebailly, Thomas Stegmüller, Behzad Bozorgtabar, Jean-Philippe Thiran, Tinne Tuytelaars
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Leveraging nearest neighbor retrieval for self-supervised representation learning has proven beneficial with object-centric images. However, this approach faces limitations when applied to scene-centric datasets, where multiple objects within an image are only implicitly captured in the global representation. Such global bootstrapping can lead to undesirable entanglement of object representations. Furthermore, even object-centric datasets stand to benefit from a finer-grained bootstrapping approach. In response to these challenges, we introduce a novel Cross-Image Object-Level Bootstrapping method tailored to enhance dense visual representation learning. By employing object-level nearest neighbor bootstrapping throughout the training, CrIBo emerges as a notably strong and adequate candidate for in-context learning, leveraging nearest neighbor retrieval at test time. CrIBo shows state-of-the-art performance on the latter task while being highly competitive in more standard downstream segmentation tasks. Our code and pretrained models are publicly available at https://github.com/tileb1/CrIBo.

</details>

### Self-Supervised Dataset Distillation for Transfer Learning.
- **链接**: [arXiv:2310.06511](https://arxiv.org/abs/2310.06511)
- **作者**: Dong Bok Lee, Seanie Lee, Joonho Ko, Kenji Kawaguchi, Juho Lee, Sung Ju Hwang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Dataset distillation methods have achieved remarkable success in distilling a large dataset into a small set of representative samples. However, they are not designed to produce a distilled dataset that can be effectively used for facilitating self-supervised pre-training. To this end, we propose a novel problem of distilling an unlabeled dataset into a set of small synthetic samples for efficient self-supervised learning (SSL). We first prove that a gradient of synthetic samples with respect to a SSL objective in naive bilevel optimization is \textit{biased} due to the randomness originating from data augmentations or masking. To address this issue, we propose to minimize the mean squared error (MSE) between a model's representations of the synthetic examples and their corresponding learnable target feature representations for the inner objective, which does not introduce any randomness. Our primary motivation is that the model obtained by the proposed inner optimization can mimic the \textit{self-supervised target model}. To achieve this, we also introduce the MSE between representations of the inner model and the self-supervised target model on the original full dataset for outer optimization. Lastly, assuming that a feature extractor is fixed, we only optimize a linear head on top of the feature extractor, which allows us to reduce the computational cost and obtain a closed-form solution of the head with kernel ridge regression. We empirically validate the effectiveness of our method on various applications involving transfer learning.

</details>

### MERT: Acoustic Music Understanding Model with Large-Scale Self-supervised Training.
- **链接**: [出版页](https://openreview.net/forum?id=w3YZ9MSlBu)
- **作者**: Yizhi Li, Ruibin Yuan, Ge Zhang, Yinghao Ma, Xingran Chen, Hanzhi Yin et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### Self-Supervised Heterogeneous Graph Learning: a Homophily and Heterogeneity View.
- **链接**: [出版页](https://openreview.net/forum?id=3FJOKjooIj)
- **作者**: Yujie Mo, Feiping Nie, Ping Hu, Heng Tao Shen, Zheng Zhang, Xinchao Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### Self-Supervised Contrastive Learning for Long-term Forecasting.
- **链接**: [出版页](https://openreview.net/forum?id=nBCuRzjqK7)
- **作者**: Junwoo Park, Daehoon Gwak, Jaegul Choo, Edward Choi
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### Mind Your Augmentation: The Key to Decoupling Dense Self-Supervised Learning.
- **链接**: [出版页](https://openreview.net/forum?id=WQYHbr36Fo)
- **作者**: Congpei Qiu, Tong Zhang, Yanhao Wu, Wei Ke, Mathieu Salzmann, Sabine Süsstrunk
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### Towards domain-invariant Self-Supervised Learning with Batch Styles Standardization.
- **链接**: [出版页](https://openreview.net/forum?id=qtE9K23ISq)
- **作者**: Marin Scalbert, Maria Vakalopoulou, Florent Couzinie-Devy
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### AUC-CL: A Batchsize-Robust Framework for Self-Supervised Contrastive Representation Learning.
- **链接**: [出版页](https://openreview.net/forum?id=YgMdDQB09U)
- **作者**: Rohan Sharma, Kaiyi Ji, Zhiqiang Xu, Changyou Chen
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### Multi-resolution HuBERT: Multi-resolution Speech Self-Supervised Learning with Masked Unit Prediction.
- **链接**: [arXiv:2310.02720](https://arxiv.org/abs/2310.02720)
- **作者**: Jiatong Shi, Hirofumi Inaguma, Xutai Ma, Ilia Kulikov, Anna Y. Sun
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing Self-Supervised Learning (SSL) models for speech typically process speech signals at a fixed resolution of 20 milliseconds. This approach overlooks the varying informational content present at different resolutions in speech signals. In contrast, this paper aims to incorporate multi-resolution information into speech self-supervised representation learning. We introduce a SSL model that leverages a hierarchical Transformer architecture, complemented by HuBERT-style masked prediction objectives, to process speech at multiple resolutions. Experimental results indicate that the proposed model not only achieves more efficient inference but also exhibits superior or comparable performance to the original HuBERT model over various tasks. Specifically, significant performance improvements over the original HuBERT have been observed in fine-tuning experiments on the LibriSpeech speech recognition benchmark as well as in evaluations using the Speech Universal PERformance Benchmark (SUPERB) and Multilingual SUPERB (ML-SUPERB).

</details>

### Self-supervised Representation Learning from Random Data Projectors.
- **链接**: [arXiv:2310.07756](https://arxiv.org/abs/2310.07756)
- **作者**: Yi Sui, Tongzi Wu, Jesse C. Cresswell, Ga Wu, George Stein, Xiao Shi Huang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised representation learning~(SSRL) has advanced considerably by exploiting the transformation invariance assumption under artificially designed data augmentations. While augmentation-based SSRL algorithms push the boundaries of performance in computer vision and natural language processing, they are often not directly applicable to other data modalities, and can conflict with application-specific data augmentation constraints. This paper presents an SSRL approach that can be applied to any data modality and network architecture because it does not rely on augmentations or masking. Specifically, we show that high-quality data representations can be learned by reconstructing random data projections. We evaluate the proposed approach on a wide range of representation learning tasks that span diverse modalities and real-world applications. We show that it outperforms multiple state-of-the-art SSRL baselines. Due to its wide applicability and strong empirical results, we argue that learning from randomness is a fruitful research direction worthy of attention and further study.

</details>

### Probabilistic Self-supervised Representation Learning via Scoring Rules Minimization.
- **链接**: [出版页](https://openreview.net/forum?id=skcTCdJz0f)
- **作者**: Amirhossein Vahidi, Simon Schoßer, Lisa Wimmer, Yawei Li, Bernd Bischl, Eyke Hüllermeier et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### Memorization in Self-Supervised Learning Improves Downstream Generalization.
- **链接**: [arXiv:2401.12233](https://arxiv.org/abs/2401.12233)
- **作者**: Wenhao Wang, Muhammad Ahmad Kaleem, Adam Dziedzic, Michael Backes, Nicolas Papernot, Franziska Boenisch
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning (SSL) has recently received significant attention due to its ability to train high-performance encoders purely on unlabeled data-often scraped from the internet. This data can still be sensitive and empirical evidence suggests that SSL encoders memorize private information of their training data and can disclose them at inference time. Since existing theoretical definitions of memorization from supervised learning rely on labels, they do not transfer to SSL. To address this gap, we propose SSLMem, a framework for defining memorization within SSL. Our definition compares the difference in alignment of representations for data points and their augmented views returned by both encoders that were trained on these data points and encoders that were not. Through comprehensive empirical analysis on diverse encoder architectures and datasets we highlight that even though SSL relies on large datasets and strong augmentations-both known in supervised learning as regularization techniques that reduce overfitting-still significant fractions of training data points experience high memorization. Through our empirical results, we show that this memorization is essential for encoders to achieve higher generalization performance on different downstream tasks.

</details>

### Modulate Your Spectrum in Self-Supervised Learning.
- **链接**: [arXiv:2305.16789](https://arxiv.org/abs/2305.16789) · [代码](https://github.com/winci-ai/INTL)
- **作者**: Xi Weng, Yunhao Ni, Tengwei Song, Jie Luo, Rao Muhammad Anwer, Salman Khan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Whitening loss offers a theoretical guarantee against feature collapse in self-supervised learning (SSL) with joint embedding architectures. Typically, it involves a hard whitening approach, transforming the embedding and applying loss to the whitened output. In this work, we introduce Spectral Transformation (ST), a framework to modulate the spectrum of embedding and to seek for functions beyond whitening that can avoid dimensional collapse. We show that whitening is a special instance of ST by definition, and our empirical investigations unveil other ST instances capable of preventing collapse. Additionally, we propose a novel ST instance named IterNorm with trace loss (INTL). Theoretical analysis confirms INTL's efficacy in preventing collapse and modulating the spectrum of embedding toward equal-eigenvalues during optimization. Our experiments on ImageNet classification and COCO object detection demonstrate INTL's potential in learning superior representations. The code is available at https://github.com/winci-ai/INTL.

</details>

### Understanding Augmentation-based Self-Supervised Representation Learning via RKHS Approximation and Regression.
- **链接**: [出版页](https://openreview.net/forum?id=Ax2yRhCQr1)
- **作者**: Runtian Zhai, Bingbin Liu, Andrej Risteski, J. Zico Kolter, Pradeep Kumar Ravikumar
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### Self-Supervised High Dynamic Range Imaging with Multi-Exposure Images in Dynamic Scenes.
- **链接**: [arXiv:2310.01840](https://arxiv.org/abs/2310.01840) · [代码](https://github.com/cszhilu1998/SelfHDR)
- **作者**: Zhilu Zhang, Haoyu Wang, Shuai Liu, Xiaotao Wang, Lei Lei, Wangmeng Zuo
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Merging multi-exposure images is a common approach for obtaining high dynamic range (HDR) images, with the primary challenge being the avoidance of ghosting artifacts in dynamic scenes. Recent methods have proposed using deep neural networks for deghosting. However, the methods typically rely on sufficient data with HDR ground-truths, which are difficult and costly to collect. In this work, to eliminate the need for labeled data, we propose SelfHDR, a self-supervised HDR reconstruction method that only requires dynamic multi-exposure images during training. Specifically, SelfHDR learns a reconstruction network under the supervision of two complementary components, which can be constructed from multi-exposure images and focus on HDR color as well as structure, respectively. The color component is estimated from aligned multi-exposure images, while the structure one is generated through a structure-focused network that is supervised by the color component and an input reference (\eg, medium-exposure) image. During testing, the learned reconstruction network is directly deployed to predict an HDR image. Experiments on real-world images demonstrate our SelfHDR achieves superior results against the state-of-the-art self-supervised methods, and comparable performance to supervised ones. Codes are available at https://github.com/cszhilu1998/SelfHDR

</details>

### Learning Multi-Agent Communication with Contrastive Learning.
- **链接**: [出版页](https://openreview.net/forum?id=vZZ4hhniJU)
- **作者**: Yat Long Lo, Biswa Sengupta, Jakob Nicolaus Foerster, Michael Noukhovitch
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### Towards Enhancing Time Series Contrastive Learning: A Dynamic Bad Pair Mining Approach.
- **链接**: [出版页](https://openreview.net/forum?id=K2c04ulKXn)
- **作者**: Xiang Lan, Hanshu Yan, Shenda Hong, Mengling Feng
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### Optimal Sample Complexity of Contrastive Learning.
- **链接**: [出版页](https://openreview.net/forum?id=NU9AYHJvYe)
- **作者**: Noga Alon, Dmitrii Avdiukhin, Dor Elboim, Orr Fischer, Grigory Yaroslavtsev
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### PolyGCL: GRAPH CONTRASTIVE LEARNING via Learnable Spectral Polynomial Filters.
- **链接**: [出版页](https://openreview.net/forum?id=y21ZO6M86t)
- **作者**: Jingyu Chen, Runlin Lei, Zhewei Wei
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### Dictionary Contrastive Learning for Efficient Local Supervision without Auxiliary Networks.
- **链接**: [出版页](https://openreview.net/forum?id=Gg7cXo3S8l)
- **作者**: Suhwan Choi, Myeongho Jeon, Yeonjung Hwang, Jeonglyul Oh, Sungjun Lim, Joonseok Lee et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### Structuring Representation Geometry with Rotationally Equivariant Contrastive Learning.
- **链接**: [arXiv:2306.13924](https://arxiv.org/abs/2306.13924) · [代码](https://github.com/Sharut/CARE)
- **作者**: Sharut Gupta, Joshua Robinson, Derek Lim, Soledad Villar, Stefanie Jegelka
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning converts raw perceptual data such as images to a compact space where simple Euclidean distances measure meaningful variations in data. In this paper, we extend this formulation by adding additional geometric structure to the embedding space by enforcing transformations of input space to correspond to simple (i.e., linear) transformations of embedding space. Specifically, in the contrastive learning setting, we introduce an equivariance objective and theoretically prove that its minima forces augmentations on input space to correspond to rotations on the spherical embedding space. We show that merely combining our equivariant loss with a non-collapse term results in non-trivial representations, without requiring invariance to data augmentations. Optimal performance is achieved by also encouraging approximate invariance, where input augmentations correspond to small rotations. Our method, CARE: Contrastive Augmentation-induced Rotational Equivariance, leads to improved performance on downstream tasks, and ensures sensitivity in embedding space to important variations in data (e.g., color) that standard contrastive methods do not achieve. Code is available at https://github.com/Sharut/CARE.

</details>

### Soft Contrastive Learning for Time Series.
- **链接**: [arXiv:2312.16424](https://arxiv.org/abs/2312.16424) · [代码](https://github.com/seunghan96/softclt)
- **作者**: Seunghan Lee, Taeyoung Park, Kibok Lee
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Contrastive learning has shown to be effective to learn representations from time series in a self-supervised way. However, contrasting similar time series instances or values from adjacent timestamps within a time series leads to ignore their inherent correlations, which results in deteriorating the quality of learned representations. To address this issue, we propose SoftCLT, a simple yet effective soft contrastive learning strategy for time series. This is achieved by introducing instance-wise and temporal contrastive loss with soft assignments ranging from zero to one. Specifically, we define soft assignments for 1) instance-wise contrastive loss by the distance between time series on the data space, and 2) temporal contrastive loss by the difference of timestamps. SoftCLT is a plug-and-play method for time series contrastive learning that improves the quality of learned representations without bells and whistles. In experiments, we demonstrate that SoftCLT consistently improves the performance in various downstream tasks including classification, semi-supervised learning, transfer learning, and anomaly detection, showing state-of-the-art performance. Code is available at this repository: https://github.com/seunghan96/softclt.

</details>

### A Graph is Worth 1-bit Spikes: When Graph Contrastive Learning Meets Spiking Neural Networks.
- **链接**: [arXiv:2305.19306](https://arxiv.org/abs/2305.19306)
- **作者**: Jintang Li, Huizhe Zhang, Ruofan Wu, Zulun Zhu, Baokun Wang, Changhua Meng et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While contrastive self-supervised learning has become the de-facto learning paradigm for graph neural networks, the pursuit of higher task accuracy requires a larger hidden dimensionality to learn informative and discriminative full-precision representations, raising concerns about computation, memory footprint, and energy consumption burden (largely overlooked) for real-world applications. This work explores a promising direction for graph contrastive learning (GCL) with spiking neural networks (SNNs), which leverage sparse and binary characteristics to learn more biologically plausible and compact representations. We propose SpikeGCL, a novel GCL framework to learn binarized 1-bit representations for graphs, making balanced trade-offs between efficiency and performance. We provide theoretical guarantees to demonstrate that SpikeGCL has comparable expressiveness with its full-precision counterparts. Experimental results demonstrate that, with nearly 32x representation storage compression, SpikeGCL is either comparable to or outperforms many fancy state-of-the-art supervised and self-supervised methods across several graph benchmarks.

</details>

### CAMBranch: Contrastive Learning with Augmented MILPs for Branching.
- **链接**: [arXiv:2402.03647](https://arxiv.org/abs/2402.03647)
- **作者**: Jiacheng Lin, Meng Xu, Zhihua Xiong, Huangang Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advancements have introduced machine learning frameworks to enhance the Branch and Bound (B\&B) branching policies for solving Mixed Integer Linear Programming (MILP). These methods, primarily relying on imitation learning of Strong Branching, have shown superior performance. However, collecting expert samples for imitation learning, particularly for Strong Branching, is a time-consuming endeavor. To address this challenge, we propose \textbf{C}ontrastive Learning with \textbf{A}ugmented \textbf{M}ILPs for \textbf{Branch}ing (CAMBranch), a framework that generates Augmented MILPs (AMILPs) by applying variable shifting to limited expert data from their original MILPs. This approach enables the acquisition of a considerable number of labeled expert samples. CAMBranch leverages both MILPs and AMILPs for imitation learning and employs contrastive learning to enhance the model's ability to capture MILP features, thereby improving the quality of branching decisions. Experimental results demonstrate that CAMBranch, trained with only 10\% of the complete dataset, exhibits superior performance. Ablation studies further validate the effectiveness of our method.

</details>

### SetCSE: Set Operations using Contrastive Learning of Sentence Embeddings.
- **链接**: [arXiv:2404.17606](https://arxiv.org/abs/2404.17606)
- **作者**: Kang Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Taking inspiration from Set Theory, we introduce SetCSE, an innovative information retrieval framework. SetCSE employs sets to represent complex semantics and incorporates well-defined operations for structured information querying under the provided context. Within this framework, we introduce an inter-set contrastive learning objective to enhance comprehension of sentence embedding models concerning the given semantics. Furthermore, we present a suite of operations, including SetCSE intersection, difference, and operation series, that leverage sentence embeddings of the enhanced model for complex sentence retrieval tasks. Throughout this paper, we demonstrate that SetCSE adheres to the conventions of human language expressions regarding compounded semantics, provides a significant enhancement in the discriminatory capability of underlying sentence embedding models, and enables numerous information retrieval tasks involving convoluted and intricate prompts which cannot be achieved using existing querying methods.

</details>

### A Mutual Information Perspective on Federated Contrastive Learning.
- **链接**: [arXiv:2405.02081](https://arxiv.org/abs/2405.02081)
- **作者**: Christos Louizos, Matthias Reisser, Denis Korzhenkov
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We investigate contrastive learning in the federated setting through the lens of SimCLR and multi-view mutual information maximization. In doing so, we uncover a connection between contrastive representation learning and user verification; by adding a user verification loss to each client's local SimCLR loss we recover a lower bound to the global multi-view mutual information. To accommodate for the case of when some labelled data are available at the clients, we extend our SimCLR variant to the federated semi-supervised setting. We see that a supervised SimCLR objective can be obtained with two changes: a) the contrastive loss is computed between datapoints that share the same label and b) we require an additional auxiliary head that predicts the correct labels from either of the two views. Along with the proposed SimCLR extensions, we also study how different sources of non-i.i.d.-ness can impact the performance of federated unsupervised learning through global mutual information maximization; we find that a global objective is beneficial for some sources of non-i.i.d.-ness but can be detrimental for others. We empirically evaluate our proposed extensions in various tasks to validate our claims and furthermore demonstrate that our proposed modifications generalize to other pretraining methods.

</details>

### An Investigation of Representation and Allocation Harms in Contrastive Learning.
- **链接**: [arXiv:2310.01583](https://arxiv.org/abs/2310.01583)
- **作者**: Subha Maity, Mayank Agarwal, Mikhail Yurochkin, Yuekai Sun
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The effect of underrepresentation on the performance of minority groups is known to be a serious problem in supervised learning settings; however, it has been underexplored so far in the context of self-supervised learning (SSL). In this paper, we demonstrate that contrastive learning (CL), a popular variant of SSL, tends to collapse representations of minority groups with certain majority groups. We refer to this phenomenon as representation harm and demonstrate it on image and text datasets using the corresponding popular CL methods. Furthermore, our causal mediation analysis of allocation harm on a downstream classification task reveals that representation harm is partly responsible for it, thus emphasizing the importance of studying and mitigating representation harm. Finally, we provide a theoretical explanation for representation harm using a stochastic block model that leads to a representational neural collapse in a contrastive learning setting.

</details>

### Poly-View Contrastive Learning.
- **链接**: [出版页](https://openreview.net/forum?id=iHcTLIor0m)
- **作者**: Amitis Shidani, R. Devon Hjelm, Jason Ramapuram, Russell Webb, Eeshan Gunesh Dhekane, Dan Busbridge
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### Backdoor Contrastive Learning via Bi-level Trigger Optimization.
- **链接**: [arXiv:2404.07863](https://arxiv.org/abs/2404.07863) · [代码](https://github.com/SWY666/SSL-backdoor-BLTO)
- **作者**: Weiyu Sun, Xinyu Zhang, Hao Lu, Ying-Cong Chen, Ting Wang, Jinghui Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Contrastive Learning (CL) has attracted enormous attention due to its remarkable capability in unsupervised representation learning. However, recent works have revealed the vulnerability of CL to backdoor attacks: the feature extractor could be misled to embed backdoored data close to an attack target class, thus fooling the downstream predictor to misclassify it as the target. Existing attacks usually adopt a fixed trigger pattern and poison the training set with trigger-injected data, hoping for the feature extractor to learn the association between trigger and target class. However, we find that such fixed trigger design fails to effectively associate trigger-injected data with target class in the embedding space due to special CL mechanisms, leading to a limited attack success rate (ASR). This phenomenon motivates us to find a better backdoor trigger design tailored for CL framework. In this paper, we propose a bi-level optimization approach to achieve this goal, where the inner optimization simulates the CL dynamics of a surrogate victim, and the outer optimization enforces the backdoor trigger to stay close to the target throughout the surrogate CL procedure. Extensive experiments show that our attack can achieve a higher attack success rate (e.g., $99\%$ ASR on ImageNet-100) with a very low poisoning rate ($1\%$). Besides, our attack can effectively evade existing state-of-the-art defenses. Code is available at: https://github.com/SWY666/SSL-backdoor-BLTO.

</details>

### Contrastive Learning is Spectral Clustering on Similarity Graph.
- **链接**: [arXiv:2303.15103](https://arxiv.org/abs/2303.15103) · [代码](https://github.com/yifanzhang-pro/Kernel-InfoNCE)
- **作者**: Zhiquan Tan, Yifan Zhang, Jingqin Yang, Yang Yuan
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Contrastive learning is a powerful self-supervised learning method, but we have a limited theoretical understanding of how it works and why it works. In this paper, we prove that contrastive learning with the standard InfoNCE loss is equivalent to spectral clustering on the similarity graph. Using this equivalence as the building block, we extend our analysis to the CLIP model and rigorously characterize how similar multi-modal objects are embedded together. Motivated by our theoretical insights, we introduce the Kernel-InfoNCE loss, incorporating mixtures of kernel functions that outperform the standard Gaussian kernel on several vision datasets. The code is available at https://github.com/yifanzhang-pro/Kernel-InfoNCE.

</details>

### Do Generated Data Always Help Contrastive Learning?
- **链接**: [arXiv:2403.12448](https://arxiv.org/abs/2403.12448) · [代码](https://github.com/PKU-ML/adainf)
- **作者**: Yifei Wang, Jizhe Zhang, Yisen Wang
- **🏷️ 机构**: Peking University
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Contrastive Learning (CL) has emerged as one of the most successful paradigms for unsupervised visual representation learning, yet it often depends on intensive manual data augmentations. With the rise of generative models, especially diffusion models, the ability to generate realistic images close to the real data distribution has been well recognized. These generated high-equality images have been successfully applied to enhance contrastive representation learning, a technique termed ``data inflation''. However, we find that the generated data (even from a good diffusion model like DDPM) may sometimes even harm contrastive learning. We investigate the causes behind this failure from the perspective of both data inflation and data augmentation. For the first time, we reveal the complementary roles that stronger data inflation should be accompanied by weaker augmentations, and vice versa. We also provide rigorous theoretical explanations for these phenomena via deriving its generalization bounds under data inflation. Drawing from these insights, we propose Adaptive Inflation (AdaInf), a purely data-centric strategy without introducing any extra computation cost. On benchmark datasets, AdaInf can bring significant improvements for various contrastive learning methods. Notably, without using external data, AdaInf obtains 94.70% linear accuracy on CIFAR-10 with SimCLR, setting a new record that surpasses many sophisticated methods. Code is available at https://github.com/PKU-ML/adainf.

</details>

### Non-negative Contrastive Learning.
- **链接**: [arXiv:2403.12459](https://arxiv.org/abs/2403.12459) · [代码](https://github.com/PKU-ML/non_neg)
- **作者**: Yifei Wang, Qi Zhang, Yaoyu Guo, Yisen Wang
- **🏷️ 机构**: Peking University
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep representations have shown promising performance when transferred to downstream tasks in a black-box manner. Yet, their inherent lack of interpretability remains a significant challenge, as these features are often opaque to human understanding. In this paper, we propose Non-negative Contrastive Learning (NCL), a renaissance of Non-negative Matrix Factorization (NMF) aimed at deriving interpretable features. The power of NCL lies in its enforcement of non-negativity constraints on features, reminiscent of NMF's capability to extract features that align closely with sample clusters. NCL not only aligns mathematically well with an NMF objective but also preserves NMF's interpretability attributes, resulting in a more sparse and disentangled representation compared to standard contrastive learning (CL). Theoretically, we establish guarantees on the identifiability and downstream generalization of NCL. Empirically, we show that these advantages enable NCL to outperform CL significantly on feature disentanglement, feature selection, as well as downstream classification tasks. At last, we show that NCL can be easily extended to other learning scenarios and benefit supervised learning as well. Code is available at https://github.com/PKU-ML/non_neg.

</details>

### REBAR: Retrieval-Based Reconstruction for Time-series Contrastive Learning.
- **链接**: [出版页](https://openreview.net/forum?id=3zQo5oUvia)
- **作者**: Maxwell A. Xu, Alexander Moreno, Hui Wei, Benjamin M. Marlin, James Matthew Rehg
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### Parametric Augmentation for Time Series Contrastive Learning.
- **链接**: [arXiv:2402.10434](https://arxiv.org/abs/2402.10434)
- **作者**: Xu Zheng, Tianchun Wang, Wei Cheng, Aitian Ma, Haifeng Chen, Mo Sha et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Modern techniques like contrastive learning have been effectively used in many areas, including computer vision, natural language processing, and graph-structured data. Creating positive examples that assist the model in learning robust and discriminative representations is a crucial stage in contrastive learning approaches. Usually, preset human intuition directs the selection of relevant data augmentations. Due to patterns that are easily recognized by humans, this rule of thumb works well in the vision and language domains. However, it is impractical to visually inspect the temporal structures in time series. The diversity of time series augmentations at both the dataset and instance levels makes it difficult to choose meaningful augmentations on the fly. In this study, we address this gap by analyzing time series data augmentation using information theory and summarizing the most commonly adopted augmentations in a unified format. We then propose a contrastive learning framework with parametric augmentation, AutoTCL, which can be adaptively employed to support time series representation learning. The proposed approach is encoder-agnostic, allowing it to be seamlessly integrated with different backbone encoders. Experiments on univariate forecasting tasks demonstrate the highly competitive results of our method, with an average 6.5\% reduction in MSE and 4.7\% in MAE over the leading baselines. In classification tasks, AutoTCL achieves a $1.2\%$ increase in average accuracy.

</details>

### Enhancing Contrastive Learning for Ordinal Regression via Ordinal Content Preserved Data Augmentation.
- **链接**: [出版页](https://openreview.net/forum?id=kx2XZlmgB1)
- **作者**: Jiyang Zheng, Yu Yao, Bo Han, Dadong Wang, Tongliang Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### Zero-Mean Regularized Spectral Contrastive Learning: Implicitly Mitigating Wrong Connections in Positive-Pair Graphs.
- **链接**: [出版页](https://openreview.net/forum?id=RZBy8oHTz4)
- **作者**: Xiong Zhou, Xianming Liu, Feilong Zhang, Gang Wu, Deming Zhai, Junjun Jiang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### Hybrid Distillation: Connecting Masked Autoencoders with Contrastive Learners.
- **链接**: [arXiv:2306.15876](https://arxiv.org/abs/2306.15876)
- **作者**: Bowen Shi, Xiaopeng Zhang, Yaoming Wang, Jin Li, Wenrui Dai, Junni Zou et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Representation learning has been evolving from traditional supervised training to Contrastive Learning (CL) and Masked Image Modeling (MIM). Previous works have demonstrated their pros and cons in specific scenarios, i.e., CL and supervised pre-training excel at capturing longer-range global patterns and enabling better feature discrimination, while MIM can introduce more local and diverse attention across all transformer layers. In this paper, we explore how to obtain a model that combines their strengths. We start by examining previous feature distillation and mask feature reconstruction methods and identify their limitations. We find that their increasing diversity mainly derives from the asymmetric designs, but these designs may in turn compromise the discrimination ability. In order to better obtain both discrimination and diversity, we propose a simple but effective Hybrid Distillation strategy, which utilizes both the supervised/CL teacher and the MIM teacher to jointly guide the student model. Hybrid Distill imitates the token relations of the MIM teacher to alleviate attention collapse, as well as distills the feature maps of the supervised/CL teacher to enable discrimination. Furthermore, a progressive redundant token masking strategy is also utilized to reduce the distilling costs and avoid falling into local optima. Experiment results prove that Hybrid Distill can achieve superior performance on different benchmarks.

</details>

## 跨领域论文（完整笔记在其他领域）

- CALICO: Self-Supervised Camera-LiDAR Contrastive Pre-training for BEV Perception. → [bev](../bev/Guideline%202024.md)
- Unconstrained Stochastic CCA: Unifying Multiview and Self-Supervised Learning. → [multi-camera-perception](../multi-camera-perception/Guideline%202024.md)
- Masked Distillation Advances Self-Supervised Transformer Architecture Search. → [neural-architecture-search](../neural-architecture-search/Guideline%202024.md)
- Understanding the Robustness of Multi-modal Contrastive Learning to Distribution Shift. → [multimodal](../multimodal/Guideline%202024.md)
- StructComp: Substituting propagation with Structural Compression in Training Graph Contrastive Learning. → [network-pruning](../network-pruning/Guideline%202024.md)
