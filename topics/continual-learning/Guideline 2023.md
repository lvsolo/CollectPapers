# Continual Learning — 2023 Guideline

> 领域: 持续学习 / 增量学习（含 VLM/多模态场景）
> 论文数: 7 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### A Model or 603 Exemplars: Towards Memory-Efficient Class-Incremental Learning.
- **链接**: [arXiv:2205.13218](https://arxiv.org/abs/2205.13218) · [代码](https://github.com/wangkiw/ICLR23-MEMO)
- **作者**: Da-Wei Zhou, Qi-Wei Wang, Han-Jia Ye, De-Chuan Zhan
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Real-world applications require the classification model to adapt to new classes without forgetting old ones. Correspondingly, Class-Incremental Learning (CIL) aims to train a model with limited memory size to meet this requirement. Typical CIL methods tend to save representative exemplars from former classes to resist forgetting, while recent works find that storing models from history can substantially boost the performance. However, the stored models are not counted into the memory budget, which implicitly results in unfair comparisons. We find that when counting the model size into the total budget and comparing methods with aligned memory size, saving models do not consistently work, especially for the case with limited memory budgets. As a result, we need to holistically evaluate different CIL methods at different memory scales and simultaneously consider accuracy and memory size for measurement. On the other hand, we dive deeply into the construction of the memory buffer for memory efficiency. By analyzing the effect of different layers in the network, we find that shallow and deep layers have different characteristics in CIL. Motivated by this, we propose a simple yet effective baseline, denoted as MEMO for Memory-efficient Expandable MOdel. MEMO extends specialized layers based on the shared generalized representations, efficiently extracting diverse representations with modest cost and maintaining representative exemplars. Extensive experiments on benchmark datasets validate MEMO's competitive performance. Code is available at: https://github.com/wangkiw/ICLR23-MEMO

</details>

### On the Soft-Subnetwork for Few-Shot Class Incremental Learning.
- **链接**: [arXiv:2209.07529](https://arxiv.org/abs/2209.07529)
- **作者**: Haeyong Kang, Jaehong Yoon, Sultan Rizky Hikmawan Madjid, Sung Ju Hwang, Chang D. Yoo
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Inspired by Regularized Lottery Ticket Hypothesis (RLTH), which hypothesizes that there exist smooth (non-binary) subnetworks within a dense network that achieve the competitive performance of the dense network, we propose a few-shot class incremental learning (FSCIL) method referred to as \emph{Soft-SubNetworks (SoftNet)}. Our objective is to learn a sequence of sessions incrementally, where each session only includes a few training instances per class while preserving the knowledge of the previously learned ones. SoftNet jointly learns the model weights and adaptive non-binary soft masks at a base training session in which each mask consists of the major and minor subnetwork; the former aims to minimize catastrophic forgetting during training, and the latter aims to avoid overfitting to a few samples in each new training session. We provide comprehensive empirical validations demonstrating that our SoftNet effectively tackles the few-shot incremental learning problem by surpassing the performance of state-of-the-art baselines over benchmark datasets.

</details>

### Warping the Space: Weight Space Rotation for Class-Incremental Few-Shot Learning.
- **链接**: [出版页](https://openreview.net/forum?id=kPLzOfPfA2l)
- **作者**: Do-Yeon Kim, Dong-Jun Han, Jun Seo, Jaekyun Moon
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Progressive Voronoi Diagram Subdivision Enables Accurate Data-free Class-Incremental Learning.
- **链接**: [出版页](https://openreview.net/forum?id=zJXg_Wmob03)
- **作者**: Chunwei Ma, Zhanghexuan Ji, Ziyun Huang, Yan Shen, Mingchen Gao, Jinhui Xu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Incremental Learning of Structured Memory via Closed-Loop Transcription.
- **链接**: [arXiv:2202.05411](https://arxiv.org/abs/2202.05411) · [代码](https://github.com/tsb0601/i-CTRL)
- **作者**: Shengbang Tong, Xili Dai, Ziyang Wu, Mingyang Li, Brent Yi, Yi Ma
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This work proposes a minimal computational model for learning structured memories of multiple object classes in an incremental setting. Our approach is based on establishing a closed-loop transcription between the classes and a corresponding set of subspaces, known as a linear discriminative representation, in a low-dimensional feature space. Our method is simpler than existing approaches for incremental learning, and more efficient in terms of model size, storage, and computation: it requires only a single, fixed-capacity autoencoding network with a feature space that is used for both discriminative and generative purposes. Network parameters are optimized simultaneously without architectural manipulations, by solving a constrained minimax game between the encoding and decoding maps over a single rate reduction-based objective. Experimental results show that our method can effectively alleviate catastrophic forgetting, achieving significantly better performance than prior work of generative replay on MNIST, CIFAR-10, and ImageNet-50, despite requiring fewer resources. Source code can be found at https://github.com/tsb0601/i-CTRL

</details>

### BEEF: Bi-Compatible Class-Incremental Learning via Energy-Based Expansion and Fusion.
- **链接**: [出版页](https://openreview.net/forum?id=iP77_axu0h3)
- **作者**: Fu-Yun Wang, Da-Wei Zhou, Liu Liu, Han-Jia Ye, Yatao Bian, De-Chuan Zhan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Neural Collapse Inspired Feature-Classifier Alignment for Few-Shot Class-Incremental Learning.
- **链接**: [出版页](https://openreview.net/forum?id=y5W8tpojhtJ)
- **作者**: Yibo Yang, Haobo Yuan, Xiangtai Li, Zhouchen Lin, Philip H. S. Torr, Dacheng Tao
- **🏷️ 机构**: Peking University
- **会议**: ICLR 2023
