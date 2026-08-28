# Self-supervised Vision — 2025 Guideline

> 领域: 视觉自监督学习（对比学习、MAE、DINO 系）
> 论文数: 35 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### SelfCite: Self-Supervised Alignment for Context Attribution in Large Language Models.
- **链接**: [arXiv:2502.09604](https://arxiv.org/abs/2502.09604) · [代码](https://github.com/facebookresearch/SelfCite)
- **作者**: Yung-Sung Chuang, Benjamin Cohen-Wang, Zejiang Shen, Zhaofeng Wu, Hu Xu, Xi Victoria Lin et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce SelfCite, a novel self-supervised approach that aligns LLMs to generate high-quality, fine-grained, sentence-level citations for the statements in their generated responses. Instead of only relying on costly and labor-intensive annotations, SelfCite leverages a reward signal provided by the LLM itself through context ablation: If a citation is necessary, removing the cited text from the context should prevent the same response; if sufficient, retaining the cited text alone should preserve the same response. This reward can guide the inference-time best-of-N sampling strategy to improve citation quality significantly, as well as be used in preference optimization to directly fine-tune the models for generating better citations. The effectiveness of SelfCite is demonstrated by increasing citation F1 up to 5.3 points on the LongBench-Cite benchmark across five long-form question answering tasks. The source code is available at https://github.com/facebookresearch/SelfCite

</details>

### Self-supervised Masked Graph Autoencoder via Structure-aware Curriculum.
- **链接**: [出版页](https://proceedings.mlr.press/v267/li25ct.html)
- **作者**: Haoyang Li, Xin Wang, Zeyang Zhang, Zongyuan Wu, Linxin Xiao, Wenwu Zhu
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Self-Supervised Transformers as Iterative Solution Improvers for Constraint Satisfaction.
- **链接**: [arXiv:2502.15794](https://arxiv.org/abs/2502.15794)
- **作者**: Yudong Xu, Wenhao Li, Scott Sanner, Elias Boutros Khalil
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a Transformer-based framework for Constraint Satisfaction Problems (CSPs). CSPs find use in many applications and thus accelerating their solution with machine learning is of wide interest. Most existing approaches rely on supervised learning from feasible solutions or reinforcement learning, paradigms that require either feasible solutions to these NP-Complete CSPs or large training budgets and a complex expert-designed reward signal. To address these challenges, we propose ConsFormer, a self-supervised framework that leverages a Transformer as a solution refiner. ConsFormer constructs a solution to a CSP iteratively in a process that mimics local search. Instead of using feasible solutions as labeled data, we devise differentiable approximations to the discrete constraints of a CSP to guide model training. Our model is trained to improve random assignments for a single step but is deployed iteratively at test time, circumventing the bottlenecks of supervised and reinforcement learning. Experiments on Sudoku, Graph Coloring, Nurse Rostering, and MAXCUT demonstrate that our method can tackle out-of-distribution CSPs simply through additional iterations.

</details>

### Discovering Global False Negatives On the Fly for Self-supervised Contrastive Learning.
- **链接**: [arXiv:2502.20612](https://arxiv.org/abs/2502.20612) · [代码](https://github.com/vibalcam/GloFND)
- **作者**: Vicente Balmaseda, Bokun Wang, Ching-Long Lin, Tianbao Yang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In self-supervised contrastive learning, negative pairs are typically constructed using an anchor image and a sample drawn from the entire dataset, excluding the anchor. However, this approach can result in the creation of negative pairs with similar semantics, referred to as "false negatives", leading to their embeddings being falsely pushed apart. To address this issue, we introduce GloFND, an optimization-based approach that automatically learns on the fly the threshold for each anchor data to identify its false negatives during training. In contrast to previous methods for false negative discovery, our approach globally detects false negatives across the entire dataset rather than locally within the mini-batch. Moreover, its per-iteration computation cost remains independent of the dataset size. Experimental results on image and image-text data demonstrate the effectiveness of the proposed method. Our implementation is available at https://github.com/vibalcam/GloFND.

</details>

### An Augmentation-Aware Theory for Self-Supervised Contrastive Learning.
- **链接**: [arXiv:2505.22196](https://arxiv.org/abs/2505.22196)
- **作者**: Jingyi Cui, Hongwei Wen, Yisen Wang
- **🏷️ 机构**: Peking University
- **会议**: ICML 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised contrastive learning has emerged as a powerful tool in machine learning and computer vision to learn meaningful representations from unlabeled data. Meanwhile, its empirical success has encouraged many theoretical studies to reveal the learning mechanisms. However, in the existing theoretical research, the role of data augmentation is still under-exploited, especially the effects of specific augmentation types. To fill in the blank, we for the first time propose an augmentation-aware error bound for self-supervised contrastive learning, showing that the supervised risk is bounded not only by the unsupervised risk, but also explicitly by a trade-off induced by data augmentation. Then, under a novel semantic label assumption, we discuss how certain augmentation methods affect the error bound. Lastly, we conduct both pixel- and representation-level experiments to verify our proposed theoretical results.

</details>

### On the Importance of Embedding Norms in Self-Supervised Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v267/draganov25a.html)
- **作者**: Andrew Draganov, Sharvaree Vadgama, Sebastian Damrich, Jan Niklas Böhm, Lucas Maes, Dmitry Kobak et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### The Brain's Bitter Lesson: Scaling Speech Decoding With Self-Supervised Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v267/jayalath25a.html)
- **作者**: Dulhan Jayalath, Gilad Landau, Brendan Shillingford, Mark W. Woolrich, Oiwi Parker Jones
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Self-supervised Adversarial Purification for Graph Neural Networks.
- **链接**: [出版页](https://proceedings.mlr.press/v267/lee25af.html)
- **作者**: Woohyun Lee, Hogun Park
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### HGOT: Self-supervised Heterogeneous Graph Neural Network with Optimal Transport.
- **链接**: [出版页](https://proceedings.mlr.press/v267/liu25bw.html)
- **作者**: Yanbei Liu, Chongxu Wang, Zhitao Xiao, Lei Geng, Yanwei Pang, Xiao Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### LOCATE 3D: Real-World Object Localization via Self-Supervised Learning in 3D.
- **链接**: [出版页](https://proceedings.mlr.press/v267/mcvay25a.html)
- **作者**: Paul McVay, Sergio Arnaud, Ada Martin, Arjun Majumdar, Krishna Murthy Jatavallabhula, Phillip Thomas et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### scSSL-Bench: Benchmarking Self-Supervised Learning for Single-Cell Data.
- **链接**: [出版页](https://proceedings.mlr.press/v267/ovcharenko25a.html) · 📚 被引 0
- **作者**: Olga Ovcharenko, Florian Barkmann, Philip Toma, Imant Daunhawer, Julia E. Vogt, Sebastian Schelter et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### On the Out-of-Distribution Generalization of Self-Supervised Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v267/qiang25a.html)
- **作者**: Wenwen Qiang, Jingyao Wang, Zeen Song, Jiangmeng Li, Changwen Zheng
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Collapse-Proof Non-Contrastive Self-Supervised Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v267/sansone25a.html)
- **作者**: Emanuele Sansone, Tim Lebailly, Tinne Tuytelaars
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Clustering via Self-Supervised Diffusion.
- **链接**: [出版页](https://proceedings.mlr.press/v267/uziel25a.html)
- **作者**: Roy Uziel, Irit Chelly, Oren Freifeld, Ari Pakman
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### TimeDART: A Diffusion Autoregressive Transformer for Self-Supervised Time Series Representation.
- **链接**: [出版页](https://proceedings.mlr.press/v267/wang25r.html)
- **作者**: Daoyu Wang, Mingyue Cheng, Zhiding Liu, Qi Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Equivalence is All: A Unified View for Self-supervised Graph Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v267/wang25ez.html)
- **作者**: Yejiang Wang, Yuhai Zhao, Zhengkui Wang, Ling Li, Jiapu Wang, Fangting Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### TimePoint: Accelerated Time Series Alignment via Self-Supervised Keypoint and Descriptor Learning.
- **链接**: [arXiv:2505.23475](https://arxiv.org/abs/2505.23475) · [代码](https://github.com/BGU-CS-VIL/TimePoint)
- **作者**: Ron Shapira Weber, Shahar Ben Ishay, Andrey Lavrinenko, Shahaf E. Finder, Oren Freifeld
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Fast and scalable alignment of time series is a fundamental challenge in many domains. The standard solution, Dynamic Time Warping (DTW), struggles with poor scalability and sensitivity to noise. We introduce TimePoint, a self-supervised method that dramatically accelerates DTW-based alignment while typically improving alignment accuracy by learning keypoints and descriptors from synthetic data. Inspired by 2D keypoint detection but carefully adapted to the unique challenges of 1D signals, TimePoint leverages efficient 1D diffeomorphisms, which effectively model nonlinear time warping, to generate realistic training data. This approach, along with fully convolutional and wavelet convolutional architectures, enables the extraction of informative keypoints and descriptors. Applying DTW to these sparse representations yield major speedups and typically higher alignment accuracy than standard DTW applied to the full signals. TimePoint demonstrates strong generalization to real-world time series when trained solely on synthetic data, and further improves with fine-tuning on real data. Extensive experiments demonstrate that TimePoint consistently achieves faster and more accurate alignments than standard DTW, making it a scalable solution for time-series analysis. Our code is available at https://github.com/BGU-CS-VIL/TimePoint

</details>

### Clustering Properties of Self-Supervised Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v267/weng25a.html)
- **作者**: Xi Weng, Jianing An, Xudong Ma, Binhang Qi, Jie Luo, Xi Yang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### ML2-GCL: Manifold Learning Inspired Lightweight Graph Contrastive Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v267/liang25h.html)
- **作者**: Jianqing Liang, Zhiqiang Li, Xinkai Wei, Yuan Liu, Zhiqiang Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### How does Labeling Error Impact Contrastive Learning? A Perspective from Data Dimensionality Reduction.
- **链接**: [出版页](https://proceedings.mlr.press/v267/chen25k.html)
- **作者**: Jun Chen, Hong Chen, Yonghua Yu, Yiming Ying
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Causality-Aware Contrastive Learning for Robust Multivariate Time-Series Anomaly Detection.
- **链接**: [出版页](https://proceedings.mlr.press/v267/kim25aa.html)
- **作者**: HyunGi Kim, Jisoo Mok, Dongjun Lee, Jaihyun Lew, Sungjae Kim, Sungroh Yoon
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### On the Similarities of Embeddings in Contrastive Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v267/lee25v.html)
- **作者**: Chungpa Lee, Sehee Lim, Kibok Lee, Jy-yong Sohn
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Contrastive Learning with Simplicial Convolutional Networks for Short-Text Classification.
- **链接**: [出版页](https://proceedings.mlr.press/v267/liang25g.html)
- **作者**: Huang Liang, Benedict Lee, Daniel Hui Loong Ng, Kelin Xia
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Mitigating Local Cohesion and Global Sparseness in Graph Contrastive Learning with Fuzzy Boundaries.
- **链接**: [出版页](https://proceedings.mlr.press/v267/lin25b.html)
- **作者**: Yuena Lin, Haichun Cai, Jun-Yi Hang, Haobo Wang, Zhen Yang, Gengyu Lyu
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### RealRAG: Retrieval-augmented Realistic Image Generation via Self-reflective Contrastive Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v267/lyu25c.html)
- **作者**: Yuanhuiyi Lyu, Xu Zheng, Lutao Jiang, Yibo Yan, Xin Zou, Huiyu Zhou et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Supervised Contrastive Learning from Weakly-Labeled Audio Segments for Musical Version Matching.
- **链接**: [出版页](https://proceedings.mlr.press/v267/serra25a.html)
- **作者**: Joan Serrà, Recep Oguz Araz, Dmitry Bogdanov, Yuki Mitsufuji
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Enhancing Graph Contrastive Learning for Protein Graphs from Perspective of Invariance.
- **链接**: [出版页](https://proceedings.mlr.press/v267/wang25cv.html)
- **作者**: Yusong Wang, Shiyin Tan, Jialun Shen, Yicheng Xu, Haobo Song, Qi Xu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### One Leaf Reveals the Season: Occlusion-Based Contrastive Learning with Semantic-Aware Views for Efficient Visual Representation.
- **链接**: [出版页](https://proceedings.mlr.press/v267/yang25ao.html)
- **作者**: Xiaoyu Yang, Lijian Xu, Hongsheng Li, Shaoting Zhang
- **🏷️ 机构**: CUHK
- **会议**: ICML 2025

### Causal Invariance-aware Augmentation for Brain Graph Contrastive Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v267/yu25o.html)
- **作者**: Minqi Yu, Jinduo Liu, Junzhong Ji
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Counterfactual Contrastive Learning with Normalizing Flows for Robust Treatment Effect Estimation.
- **链接**: [出版页](https://proceedings.mlr.press/v267/zhang25r.html)
- **作者**: Jiaxuan Zhang, Emadeldeen Eldele, Fuyuan Cao, Yang Wang, Xiaoli Li, Jiye Liang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Weakly-Supervised Contrastive Learning for Imprecise Class Labels.
- **链接**: [出版页](https://proceedings.mlr.press/v267/zhou25ab.html)
- **作者**: Zi-Hao Zhou, Junjie Wang, Tong Wei, Min-Ling Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Effective and Efficient Masked Image Generation Models.
- **链接**: [出版页](https://proceedings.mlr.press/v267/you25d.html)
- **作者**: Zebin You, Jingyang Ou, Xiaolu Zhang, Jun Hu, Jun Zhou, Chongxuan Li
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

## 跨领域论文（完整笔记在其他领域）

- Self-Supervised Learning of Intertwined Content and Positional Features for Object Detection. → [object-detection](../object-detection/Guideline%202025.md)
- Contradiction Retrieval via Contrastive Learning with Sparsity. → [network-pruning](../network-pruning/Guideline%202025.md)
- PROTOCOL: Partial Optimal Transport-enhanced Contrastive Learning for Imbalanced Multi-view Clustering. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
