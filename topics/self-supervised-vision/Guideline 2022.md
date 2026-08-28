# Self-supervised Vision — 2022 Guideline

> 领域: 视觉自监督学习（对比学习、MAE、DINO 系）
> 论文数: 13 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### The Close Relationship Between Contrastive Learning and Meta-Learning.
- **链接**: [出版页](https://openreview.net/forum?id=gICys3ITSmj)
- **作者**: Renkun Ni, Manli Shu, Hossein Souri, Micah Goldblum, Tom Goldstein
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

### Learning Disentangled Representation by Exploiting Pretrained Generative Models: A Contrastive Learning View.
- **链接**: [出版页](https://openreview.net/forum?id=j-63FSNcO5a)
- **作者**: Xuanchi Ren, Tao Yang, Yuwang Wang, Wenjun Zeng
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

### Chaos is a Ladder: A New Theoretical Understanding of Contrastive Learning via Augmentation Overlap.
- **链接**: [arXiv:2203.13457](https://arxiv.org/abs/2203.13457) · [代码](https://github.com/zhangq327/ARC)
- **作者**: Yifei Wang, Qi Zhang, Yisen Wang, Jiansheng Yang, Zhouchen Lin
- **🏷️ 机构**: Peking University
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, contrastive learning has risen to be a promising approach for large-scale self-supervised learning. However, theoretical understanding of how it works is still unclear. In this paper, we propose a new guarantee on the downstream performance without resorting to the conditional independence assumption that is widely adopted in previous work but hardly holds in practice. Our new theory hinges on the insight that the support of different intra-class samples will become more overlapped under aggressive data augmentations, thus simply aligning the positive samples (augmented views of the same sample) could make contrastive learning cluster intra-class samples together. Based on this augmentation overlap perspective, theoretically, we obtain asymptotically closed bounds for downstream performance under weaker assumptions, and empirically, we propose an unsupervised model selection metric ARC that aligns well with downstream accuracy. Our theory suggests an alternative understanding of contrastive learning: the role of aligning positive samples is more like a surrogate task than an ultimate goal, and the overlapped augmented views (i.e., the chaos) create a ladder for contrastive learning to gradually learn class-separated representations. The code for computing ARC is available at https://github.com/zhangq327/ARC.

</details>

### Scarf: Self-Supervised Contrastive Learning using Random Feature Corruption.
- **链接**: [出版页](https://openreview.net/forum?id=CuV_qYkmKb3)
- **作者**: Dara Bahri, Heinrich Jiang, Yi Tay, Donald Metzler
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

### Poisoning and Backdooring Contrastive Learning.
- **链接**: [arXiv:2106.09667](https://arxiv.org/abs/2106.09667)
- **作者**: Nicholas Carlini, Andreas Terzis
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal contrastive learning methods like CLIP train on noisy and uncurated training datasets. This is cheaper than labeling datasets manually, and even improves out-of-distribution robustness. We show that this practice makes backdoor and poisoning attacks a significant threat. By poisoning just 0.01% of a dataset (e.g., just 300 images of the 3 million-example Conceptual Captions dataset), we can cause the model to misclassify test images by overlaying a small patch. Targeted poisoning attacks, whereby the model misclassifies a particular test input with an adversarially-desired label, are even easier requiring control of 0.0001% of the dataset (e.g., just three out of the 3 million images). Our attacks call into question whether training on noisy and uncurated Internet scrapes is desirable.

</details>

### Incremental False Negative Detection for Contrastive Learning.
- **链接**: [arXiv:2106.03719](https://arxiv.org/abs/2106.03719)
- **作者**: Tsai-Shien Chen, Wei-Chih Hung, Hung-Yu Tseng, Shao-Yi Chien, Ming-Hsuan Yang
- **🏷️ 机构**: UC Merced
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning has recently shown great potential in vision tasks through contrastive learning, which aims to discriminate each image, or instance, in the dataset. However, such instance-level learning ignores the semantic relationship among instances and sometimes undesirably repels the anchor from the semantically similar samples, termed as "false negatives". In this work, we show that the unfavorable effect from false negatives is more significant for the large-scale datasets with more semantic concepts. To address the issue, we propose a novel self-supervised contrastive learning framework that incrementally detects and explicitly removes the false negative samples. Specifically, following the training process, our method dynamically detects increasing high-quality false negatives considering that the encoder gradually improves and the embedding space becomes more semantically structural. Next, we discuss two strategies to explicitly remove the detected false negatives during contrastive learning. Extensive experiments show that our framework outperforms other self-supervised contrastive learning methods on multiple benchmarks in a limited resource setup.

</details>

### Understanding Dimensional Collapse in Contrastive Self-supervised Learning.
- **链接**: [arXiv:2110.09348](https://arxiv.org/abs/2110.09348)
- **作者**: Li Jing, Pascal Vincent, Yann LeCun, Yuandong Tian
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised visual representation learning aims to learn useful representations without relying on human annotations. Joint embedding approach bases on maximizing the agreement between embedding vectors from different views of the same image. Various methods have been proposed to solve the collapsing problem where all embedding vectors collapse to a trivial constant solution. Among these methods, contrastive learning prevents collapse via negative sample pairs. It has been shown that non-contrastive methods suffer from a lesser collapse problem of a different nature: dimensional collapse, whereby the embedding vectors end up spanning a lower-dimensional subspace instead of the entire available embedding space. Here, we show that dimensional collapse also happens in contrastive learning. In this paper, we shed light on the dynamics at play in contrastive learning that leads to dimensional collapse. Inspired by our theory, we propose a novel contrastive learning method, called DirectCLR, which directly optimizes the representation space without relying on an explicit trainable projector. Experiments show that DirectCLR outperforms SimCLR with a trainable linear projector on ImageNet.

</details>

### Anomaly Detection for Tabular Data with Internal Contrastive Learning.
- **链接**: [出版页](https://openreview.net/forum?id=_hszZbt46bT)
- **作者**: Tom Shenkar, Lior Wolf
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

### Conditional Contrastive Learning with Kernel.
- **链接**: [arXiv:2202.05458](https://arxiv.org/abs/2202.05458)
- **作者**: Yao-Hung Hubert Tsai, Tianqin Li, Martin Q. Ma, Han Zhao, Kun Zhang, Louis-Philippe Morency et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Conditional contrastive learning frameworks consider the conditional sampling procedure that constructs positive or negative data pairs conditioned on specific variables. Fair contrastive learning constructs negative pairs, for example, from the same gender (conditioning on sensitive information), which in turn reduces undesirable information from the learned representations; weakly supervised contrastive learning constructs positive pairs with similar annotative attributes (conditioning on auxiliary information), which in turn are incorporated into the representations. Although conditional contrastive learning enables many applications, the conditional sampling procedure can be challenging if we cannot obtain sufficient data pairs for some values of the conditioning variable. This paper presents Conditional Contrastive Learning with Kernel (CCL-K) that converts existing conditional contrastive objectives into alternative forms that mitigate the insufficient data problem. Instead of sampling data according to the value of the conditioning variable, CCL-K uses the Kernel Conditional Embedding Operator that samples data from all available data and assigns weights to each sampled data given the kernel similarity between the values of the conditioning variable. We conduct experiments using weakly supervised, fair, and hard negatives contrastive learning, showing CCL-K outperforms state-of-the-art baselines.

</details>

### CoST: Contrastive Learning of Disentangled Seasonal-Trend Representations for Time Series Forecasting.
- **链接**: [出版页](https://openreview.net/forum?id=PilZY3omXV2)
- **作者**: Gerald Woo, Chenghao Liu, Doyen Sahoo, Akshat Kumar, Steven C. H. Hoi
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

### Towards Better Understanding and Better Generalization of Low-shot Classification in Histology Images with Contrastive Learning.
- **链接**: [出版页](https://openreview.net/forum?id=kQ2SOflIOVC)
- **作者**: Jiawei Yang, Hanbo Chen, Jiangpeng Yan, Xiaoyu Chen, Jianhua Yao
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

### Zero-CL: Instance and Feature decorrelation for negative-free symmetric contrastive learning.
- **链接**: [出版页](https://openreview.net/forum?id=RAW9tCdVxLj)
- **作者**: Shaofeng Zhang, Feng Zhu, Junchi Yan, Rui Zhao, Xiaokang Yang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

### How Does SimSiam Avoid Collapse Without Negative Samples? A Unified Understanding with Self-supervised Contrastive Learning.
- **链接**: [arXiv:2203.16262](https://arxiv.org/abs/2203.16262)
- **作者**: Chaoning Zhang, Kang Zhang, Chenshuang Zhang, Trung X. Pham, Chang D. Yoo, In So Kweon
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> To avoid collapse in self-supervised learning (SSL), a contrastive loss is widely used but often requires a large number of negative samples. Without negative samples yet achieving competitive performance, a recent work has attracted significant attention for providing a minimalist simple Siamese (SimSiam) method to avoid collapse. However, the reason for how it avoids collapse without negative samples remains not fully clear and our investigation starts by revisiting the explanatory claims in the original SimSiam. After refuting their claims, we introduce vector decomposition for analyzing the collapse based on the gradient analysis of the $l_2$-normalized representation vector. This yields a unified perspective on how negative samples and SimSiam alleviate collapse. Such a unified perspective comes timely for understanding the recent progress in SSL.

</details>
