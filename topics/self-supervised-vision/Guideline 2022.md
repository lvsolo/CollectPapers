# Self-supervised Vision — 2022 Guideline

> 领域: 视觉自监督学习（对比学习、MAE、DINO 系）
> 论文数: 11 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Self-Supervised Pretraining for Large-Scale Point Clouds.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/f670ef96387d9a5a8a51e2ed80cb148d-Abstract-Conference.html) · 📚 被引 0
- **作者**: Zaiwei Zhang, Min Bai, Li Erran Li
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Green Hierarchical Vision Transformer for Masked Image Modeling.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/7e487c72fce6e45879a78ee0872d991d-Abstract-Conference.html)
- **作者**: Lang Huang, Shan You, Mingkai Zheng, Fei Wang, Chen Qian, Toshihiko Yamasaki
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Adapting Self-Supervised Vision Transformers by Probing Attention-Conditioned Masking Consistency.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/93b4d708976a1d9b1250c400e7fda811-Abstract-Conference.html) · 📚 被引 0
- **作者**: Viraj Prabhu, Sriram Yenamandra, Aaditya Singh, Judy Hoffman
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Self-supervised Heterogeneous Graph Pre-training Based on Structural Clustering.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/6c7297baffe5c85ea1d9e1ccb1222ab8-Abstract-Conference.html) · 📚 被引 4
- **作者**: Yaming Yang, Ziyu Guan, Zhe Wang, Wei Zhao, Cai Xu, Weigang Lu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### $\alpha$-ReQ : Assessing Representation Quality in Self-Supervised Learning by measuring eigenspectrum decay.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/70596d70542c51c8d9b4e423f4bf2736-Abstract-Conference.html) · 📚 被引 5
- **作者**: Kumar Krishna Agrawal, Arnab Kumar Mondal, Arna Ghosh, Blake A. Richards
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### RSA: Reducing Semantic Shift from Aggressive Augmentations for Self-supervised Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/850e8063d902e0825d3c5504d183bafe-Abstract-Conference.html) · 📚 被引 3
- **作者**: Yingbin Bai, Erkun Yang, Zhaoqing Wang, Yuxuan Du, Bo Han, Cheng Deng et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Contrastive and Non-Contrastive Self-Supervised Learning Recover Global and Local Spectral Embedding Methods.
- **链接**: [arXiv:2205.11508](https://arxiv.org/abs/2205.11508) · 📚 被引 5
- **作者**: Randall Balestriero, Yann LeCun
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-Supervised Learning (SSL) surmises that inputs and pairwise positive relationships are enough to learn meaningful representations. Although SSL has recently reached a milestone: outperforming supervised methods in many modalities\dots the theoretical foundations are limited, method-specific, and fail to provide principled design guidelines to practitioners. In this paper, we propose a unifying framework under the helm of spectral manifold learning to address those limitations. Through the course of this study, we will rigorously demonstrate that VICReg, SimCLR, BarlowTwins et al. correspond to eponymous spectral methods such as Laplacian Eigenmaps, Multidimensional Scaling et al. This unification will then allow us to obtain (i) the closed-form optimal representation for each method, (ii) the closed-form optimal network parameters in the linear regime for each method, (iii) the impact of the pairwise relations used during training on each of those quantities and on downstream task performances, and most importantly, (iv) the first theoretical bridge between contrastive and non-contrastive methods towards global and local spectral embedding methods respectively, hinting at the benefits and limitations of each. For example, (i) if the pairwise relation is aligned with the downstream task, any SSL method can be employed successfully and will recover the supervised method, but in the low data regime, VICReg's invariance hyper-parameter should be high; (ii) if the pairwise relation is misaligned with the downstream task, VICReg with small invariance hyper-parameter should be preferred over SimCLR or BarlowTwins.

</details>

### VICRegL: Self-Supervised Learning of Local Visual Features.
- **链接**: [arXiv:2210.01571](https://arxiv.org/abs/2210.01571) · [代码](https://github.com/facebookresearch/VICRegL) · 📚 被引 23
- **作者**: Adrien Bardes, Jean Ponce, Yann LeCun
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Most recent self-supervised methods for learning image representations focus on either producing a global feature with invariance properties, or producing a set of local features. The former works best for classification tasks while the latter is best for detection and segmentation tasks. This paper explores the fundamental trade-off between learning local and global features. A new method called VICRegL is proposed that learns good global and local features simultaneously, yielding excellent performance on detection and segmentation tasks while maintaining good performance on classification tasks. Concretely, two identical branches of a standard convolutional net architecture are fed two differently distorted versions of the same image. The VICReg criterion is applied to pairs of global feature vectors. Simultaneously, the VICReg criterion is applied to pairs of local feature vectors occurring before the last pooling layer. Two local feature vectors are attracted to each other if their l2-distance is below a threshold or if their relative locations are consistent with a known geometric transformation between the two input images. We demonstrate strong performance on linear classification and segmentation transfer tasks. Code and pretrained models are publicly available at: https://github.com/facebookresearch/VICRegL

</details>

### Self-Supervised Fair Representation Learning without Demographics.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/ad991bbc381626a8e44dc5414aa136a8-Abstract-Conference.html) · 📚 被引 2
- **作者**: Junyi Chai, Xiaoqian Wang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### S3GC: Scalable Self-Supervised Graph Clustering.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/15972a9575e0f03bf82f00aebeb40774-Abstract-Conference.html) · 📚 被引 9
- **作者**: Devvrit, Aditya Sinha, Inderjit S. Dhillon, Prateek Jain
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Improving Self-Supervised Learning by Characterizing Idealized Representations.
- **链接**: [arXiv:2209.06235](https://arxiv.org/abs/2209.06235) · 📚 被引 1
- **作者**: Yann Dubois, Stefano Ermon, Tatsunori B. Hashimoto, Percy Liang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite the empirical successes of self-supervised learning (SSL) methods, it is unclear what characteristics of their representations lead to high downstream accuracies. In this work, we characterize properties that SSL representations should ideally satisfy. Specifically, we prove necessary and sufficient conditions such that for any task invariant to given data augmentations, desired probes (e.g., linear or MLP) trained on that representation attain perfect accuracy. These requirements lead to a unifying conceptual framework for improving existing SSL methods and deriving new ones. For contrastive learning, our framework prescribes simple but significant improvements to previous methods such as using asymmetric projection heads. For non-contrastive learning, we use our framework to derive a simple and novel objective. Our resulting SSL algorithms outperform baselines on standard benchmarks, including SwAV+multicrops on linear probing of ImageNet.

</details>
