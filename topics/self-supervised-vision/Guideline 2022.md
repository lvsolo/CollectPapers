# Self-supervised Vision — 2022 Guideline

> 领域: 视觉自监督学习（对比学习、MAE、DINO 系）
> 论文数: 33 · 按重要性排序（引用数/标题信号启发式）

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
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/850e8063d902e0825d3c5504d183bafe-Abstract-Conference.html)
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
- **链接**: [arXiv:2210.01571](https://arxiv.org/abs/2210.01571) · [代码](https://github.com/facebookresearch/VICRegL)
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

### Contrastive Learning as Goal-Conditioned Reinforcement Learning.
- **链接**: [arXiv:2206.07568](https://arxiv.org/abs/2206.07568) · 📚 被引 18
- **作者**: Benjamin Eysenbach, Tianjun Zhang, Sergey Levine, Ruslan Salakhutdinov
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In reinforcement learning (RL), it is easier to solve a task if given a good representation. While deep RL should automatically acquire such good representations, prior work often finds that learning representations in an end-to-end fashion is unstable and instead equip RL algorithms with additional representation learning parts (e.g., auxiliary losses, data augmentation). How can we design RL algorithms that directly acquire good representations? In this paper, instead of adding representation learning parts to an existing RL algorithm, we show (contrastive) representation learning methods can be cast as RL algorithms in their own right. To do this, we build upon prior work and apply contrastive representation learning to action-labeled trajectories, in such a way that the (inner product of) learned representations exactly corresponds to a goal-conditioned value function. We use this idea to reinterpret a prior RL method as performing contrastive learning, and then use the idea to propose a much simpler method that achieves similar performance. Across a range of goal-conditioned RL tasks, we demonstrate that contrastive RL methods achieve higher success rates than prior non-contrastive methods, including in the offline RL setting. We also show that contrastive RL outperforms prior methods on image-based tasks, without using data augmentation or auxiliary objectives.

</details>

### Federated Learning from Pre-Trained Models: A Contrastive Learning Approach.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/7aa320d2b4b8f6400b18f6f77b6c1535-Abstract-Conference.html) · 📚 被引 30
- **作者**: Yue Tan, Guodong Long, Jie Ma, Lu Liu, Tianyi Zhou, Jing Jiang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### An Empirical Study on Disentanglement of Negative-free Contrastive Learning.
- **链接**: [arXiv:2206.04756](https://arxiv.org/abs/2206.04756) · [代码](https://github.com/noahcao/disentanglement_lib_med) · 📚 被引 1
- **作者**: Jinkun Cao, Ruiqian Nai, Qing Yang, Jialei Huang, Yang Gao
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Negative-free contrastive learning methods have attracted a lot of attention with simplicity and impressive performances for large-scale pretraining. However, its disentanglement property remains unexplored. In this paper, we examine negative-free contrastive learning methods to study the disentanglement property empirically. We find that existing disentanglement metrics fail to make meaningful measurements for high-dimensional representation models, so we propose a new disentanglement metric based on Mutual Information between latent representations and data factors. With this proposed metric, we benchmark the disentanglement property of negative-free contrastive learning on both popular synthetic datasets and a real-world dataset CelebA. Our study shows that the investigated methods can learn a well-disentangled subset of representation. As far as we know, we are the first to extend the study of disentangled representation learning to high-dimensional representation space and introduce negative-free contrastive learning methods into this area. The source code of this paper is available at \url{https://github.com/noahcao/disentanglement_lib_med}.

</details>

### TreeMoCo: Contrastive Neuron Morphology Representation Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/9f989633ffbd47a83caddacad0f0261f-Abstract-Conference.html) · 📚 被引 4
- **作者**: Hanbo Chen, Jiawei Yang, Daniel Maxim Iascone, Lijuan Liu, Lei He, Hanchuan Peng et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Why do We Need Large Batchsizes in Contrastive Learning? A Gradient-Bias Perspective.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/db174d373133dcc6bf83bc98e4b681f8-Abstract-Conference.html) · 📚 被引 14
- **作者**: Changyou Chen, Jianyi Zhang, Yi Xu, Liqun Chen, Jiali Duan, Yiran Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Non-Linguistic Supervision for Contrastive Learning of Sentence Embeddings.
- **链接**: [arXiv:2209.09433](https://arxiv.org/abs/2209.09433) · 📚 被引 1
- **作者**: Yiren Jian, Chongyang Gao, Soroush Vosoughi
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Semantic representation learning for sentences is an important and well-studied problem in NLP. The current trend for this task involves training a Transformer-based sentence encoder through a contrastive objective with text, i.e., clustering sentences with semantically similar meanings and scattering others. In this work, we find the performance of Transformer models as sentence encoders can be improved by training with multi-modal multi-task losses, using unpaired examples from another modality (e.g., sentences and unrelated image/audio data). In particular, besides learning by the contrastive loss on text, our model clusters examples from a non-linguistic domain (e.g., visual/audio) with a similar contrastive loss at the same time. The reliance of our framework on unpaired non-linguistic data makes it language-agnostic, enabling it to be widely applicable beyond English NLP. Experiments on 7 semantic textual similarity benchmarks reveal that models trained with the additional non-linguistic (images/audio) contrastive objective lead to higher quality sentence embeddings. This indicates that Transformer models are able to generalize better by doing a similar task (i.e., clustering) with unpaired examples from different modalities in a multi-task fashion.

</details>

### Expectation-Maximization Contrastive Learning for Compact Video-and-Language Representations.
- **链接**: [arXiv:2211.11427](https://arxiv.org/abs/2211.11427) · 📚 被引 10
- **作者**: Peng Jin, Jinfa Huang, Fenglin Liu, Xian Wu, Shen Ge, Guoli Song et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Most video-and-language representation learning approaches employ contrastive learning, e.g., CLIP, to project the video and text features into a common latent space according to the semantic similarities of text-video pairs. However, such learned shared latent spaces are not often optimal, and the modality gap between visual and textual representation can not be fully eliminated. In this paper, we propose Expectation-Maximization Contrastive Learning (EMCL) to learn compact video-and-language representations. Specifically, we use the Expectation-Maximization algorithm to find a compact set of bases for the latent space, where the features could be concisely represented as the linear combinations of these bases. Such feature decomposition of video-and-language representations reduces the rank of the latent space, resulting in increased representing power for the semantics. Extensive experiments on three benchmark text-video retrieval datasets prove that our EMCL can learn more discriminative video-and-language representations than previous methods, and significantly outperform previous state-of-the-art methods across all metrics. More encouragingly, the proposed method can be applied to boost the performance of existing approaches either as a jointly training layer or an out-of-the-box inference module with no extra training, making it easy to be incorporated into any existing methods.

</details>

### Energy-Based Contrastive Learning of Visual Representations.
- **链接**: [arXiv:2202.04933](https://arxiv.org/abs/2202.04933) · [代码](https://github.com/1202kbs/EBCLR) · 📚 被引 0
- **作者**: Beomsu Kim, Jong Chul Ye
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Contrastive learning is a method of learning visual representations by training Deep Neural Networks (DNNs) to increase the similarity between representations of positive pairs (transformations of the same image) and reduce the similarity between representations of negative pairs (transformations of different images). Here we explore Energy-Based Contrastive Learning (EBCLR) that leverages the power of generative learning by combining contrastive learning with Energy-Based Models (EBMs). EBCLR can be theoretically interpreted as learning the joint distribution of positive pairs, and it shows promising results on small and medium-scale datasets such as MNIST, Fashion-MNIST, CIFAR-10, and CIFAR-100. Specifically, we find EBCLR demonstrates from X4 up to X20 acceleration compared to SimCLR and MoCo v2 in terms of training epochs. Furthermore, in contrast to SimCLR, we observe EBCLR achieves nearly the same performance with 254 negative pairs (batch size 128) and 30 negative pairs (batch size 16) per positive pair, demonstrating the robustness of EBCLR to small numbers of negative pairs. Hence, EBCLR provides a novel avenue for improving contrastive learning methods that usually require large datasets with a significant number of negative pairs per iteration to achieve reasonable performance on downstream tasks. Code: https://github.com/1202kbs/EBCLR

</details>

### Optimal Positive Generation via Latent Transformation for Contrastive Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/74a31a3b862eb7f01defbbed8e5f0c69-Abstract-Conference.html) · 📚 被引 2
- **作者**: Yinqi Li, Hong Chang, Bingpeng Ma, Shiguang Shan, Xilin Chen
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Revisiting Graph Contrastive Learning from the Perspective of Graph Spectrum.
- **链接**: [arXiv:2210.02330](https://arxiv.org/abs/2210.02330) · 📚 被引 6
- **作者**: Nian Liu, Xiao Wang, Deyu Bo, Chuan Shi, Jian Pei
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Graph Contrastive Learning (GCL), learning the node representations by augmenting graphs, has attracted considerable attentions. Despite the proliferation of various graph augmentation strategies, some fundamental questions still remain unclear: what information is essentially encoded into the learned representations by GCL? Are there some general graph augmentation rules behind different augmentations? If so, what are they and what insights can they bring? In this paper, we answer these questions by establishing the connection between GCL and graph spectrum. By an experimental investigation in spectral domain, we firstly find the General grAph augMEntation (GAME) rule for GCL, i.e., the difference of the high-frequency parts between two augmented graphs should be larger than that of low-frequency parts. This rule reveals the fundamental principle to revisit the current graph augmentations and design new effective graph augmentations. Then we theoretically prove that GCL is able to learn the invariance information by contrastive invariance theorem, together with our GAME rule, for the first time, we uncover that the learned representations by GCL essentially encode the low-frequency information, which explains why GCL works. Guided by this rule, we propose a spectral graph contrastive learning module (SpCo), which is a general and GCL-friendly plug-in. We combine it with different existing GCL models, and extensive experiments well demonstrate that it can further improve the performances of a wide variety of different GCL methods.

</details>

### Bridging the Gap from Asymmetry Tricks to Decorrelation Principles in Non-contrastive Self-supervised Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/7d535a224c8ae54ba75bac0457b6b279-Abstract-Conference.html) · 📚 被引 2
- **作者**: Kang-Jun Liu, Masanori Suganuma, Takayuki Okatani
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Co-Modality Graph Contrastive Learning for Imbalanced Node Classification.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/65cbe3e21ac62553111d9ecf7d60c18e-Abstract-Conference.html) · 📚 被引 4
- **作者**: Yiyue Qian, Chunhui Zhang, Yiming Zhang, Qianlong Wen, Yanfang Ye, Chuxu Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Understanding Deep Contrastive Learning via Coordinate-wise Optimization.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/7b5c9cc08960df40615c1d858961eb8b-Abstract-Conference.html) · 📚 被引 2
- **作者**: Yuandong Tian
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Analyzing Data-Centric Properties for Graph Contrastive Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/5adac7be735715604e8a4b0b2924a7e4-Abstract-Conference.html) · 📚 被引 0
- **作者**: Puja Trivedi, Ekdeep Singh Lubana, Mark Heimann, Danai Koutra, Jayaraman J. Thiagarajan
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Uncovering the Structural Fairness in Graph Contrastive Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/d13565c82d1e44eda2da3bd00b35ca11-Abstract-Conference.html) · 📚 被引 4
- **作者**: Ruijia Wang, Xiao Wang, Chuan Shi, Le Song
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### SCL-WC: Cross-Slide Contrastive Learning for Weakly-Supervised Whole-Slide Image Classification.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/726204cea3ec27790a644e5b379175e3-Abstract-Conference.html) · 📚 被引 7
- **作者**: Xiyue Wang, Jinxi Xiang, Jun Zhang, Sen Yang, Zhongyi Yang, Ming-Hui Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Augmentations in Hypergraph Contrastive Learning: Fabricated and Generative.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/0cd1eec0eeaf5ce1bf6d8875a7c1d095-Abstract-Conference.html) · 📚 被引 6
- **作者**: Tianxin Wei, Yuning You, Tianlong Chen, Yang Shen, Jingrui He, Zhangyang Wang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### The Mechanism of Prediction Head in Non-contrastive Self-supervised Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/9d276b0a087efdd2404f3295b26c24c1-Abstract-Conference.html) · 📚 被引 0
- **作者**: Zixin Wen, Yuanzhi Li
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Divide and Contrast: Source-free Domain Adaptation via Adaptive Contrastive Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/215aeb07b5996c969c0123c3c6ee8f54-Abstract-Conference.html) · 📚 被引 14
- **作者**: Ziyi Zhang, Weikai Chen, Hui Cheng, Zhen Li, Siyuan Li, Liang Lin et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Rethinking and Scaling Up Graph Contrastive Learning: An Extremely Efficient Approach with Group Discrimination.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/46027e3de0db3617a911f1a647def3bf-Abstract-Conference.html) · 📚 被引 3
- **作者**: Yizhen Zheng, Shirui Pan, Vincent C. S. Lee, Yu Zheng, Philip S. Yu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

## 跨领域论文（完整笔记在其他领域）

- Multimodal Contrastive Learning with LIMoE: the Language-Image Mixture of Experts. → [multimodal](../multimodal/Guideline%202022.md)
- Long-Form Video-Language Pre-Training with Multimodal Temporal Contrastive Learning. → [multimodal](../multimodal/Guideline%202022.md)
