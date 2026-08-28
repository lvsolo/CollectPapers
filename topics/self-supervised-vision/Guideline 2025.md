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
- **链接**: [arXiv:2502.09252](https://arxiv.org/abs/2502.09252)
- **作者**: Andrew Draganov, Sharvaree Vadgama, Sebastian Damrich, Jan Niklas Böhm, Lucas Maes, Dmitry Kobak et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning (SSL) allows training data representations without a supervised signal and has become an important paradigm in machine learning. Most SSL methods employ the cosine similarity between embedding vectors and hence effectively embed data on a hypersphere. While this seemingly implies that embedding norms cannot play any role in SSL, a few recent works have suggested that embedding norms have properties related to network convergence and confidence. In this paper, we resolve this apparent contradiction and systematically establish the embedding norm's role in SSL training. Using theoretical analysis, simulations, and experiments, we show that embedding norms (i) govern SSL convergence rates and (ii) encode network confidence, with smaller norms corresponding to unexpected samples. Additionally, we show that manipulating embedding norms can have large effects on convergence speed. Our findings demonstrate that SSL embedding norms are integral to understanding and optimizing network behavior.

</details>

### The Brain's Bitter Lesson: Scaling Speech Decoding With Self-Supervised Learning.
- **链接**: [arXiv:2406.04328](https://arxiv.org/abs/2406.04328)
- **作者**: Dulhan Jayalath, Gilad Landau, Brendan Shillingford, Mark W. Woolrich, Oiwi Parker Jones
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The past few years have seen remarkable progress in the decoding of speech from brain activity, primarily driven by large single-subject datasets. However, due to individual variation, such as anatomy, and differences in task design and scanning hardware, leveraging data across subjects and datasets remains challenging. In turn, the field has not benefited from the growing number of open neural data repositories to exploit large-scale deep learning. To address this, we develop neuroscience-informed self-supervised objectives, together with an architecture, for learning from heterogeneous brain recordings. Scaling to nearly 400 hours of MEG data and 900 subjects, our approach shows generalisation across participants, datasets, tasks, and even to novel subjects. It achieves improvements of 15-27% over state-of-the-art models and matches surgical decoding performance with non-invasive data. These advances unlock the potential for scaling speech decoding models beyond the current frontier.

</details>

### Self-supervised Adversarial Purification for Graph Neural Networks.
- **链接**: [arXiv:2605.23239](https://arxiv.org/abs/2605.23239)
- **作者**: Woohyun Lee, Hogun Park
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Defending Graph Neural Networks (GNNs) against adversarial attacks requires balancing accuracy and robustness, a trade-off often mishandled by traditional methods like adversarial training that intertwine these conflicting objectives within a single classifier. To overcome this limitation, we propose a self-supervised adversarial purification framework. We separate robustness from the classifier by introducing a dedicated purifier, which cleanses the input data before classification. In contrast to prior adversarial purification methods, we propose GPR-GAE, a novel graph auto-encoder (GAE), as a specialized purifier trained with a self-supervised strategy, adapting to diverse graph structures in a data-driven manner. Utilizing multiple Generalized PageRank (GPR) filters, GPR-GAE captures diverse structural representations for robust and effective purification. Our multi-step purification process further facilitates GPR-GAE to achieve precise graph recovery and robust defense against structural perturbations. Experiments across diverse datasets and attack scenarios demonstrate the state-of-the-art robustness of GPR-GAE, showcasing it as an independent plug-and-play purifier for GNN classifiers.

</details>

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
- **链接**: [arXiv:2505.22028](https://arxiv.org/abs/2505.22028) · [代码](https://github.com/Speechless-10308/WSC)
- **作者**: Zi-Hao Zhou, Junjie Wang, Tong Wei, Min-Ling Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Contrastive learning has achieved remarkable success in learning effective representations, with supervised contrastive learning often outperforming self-supervised approaches. However, in real-world scenarios, data annotations are often ambiguous or inaccurate, meaning that class labels may not reliably indicate whether two examples belong to the same class. This limitation restricts the applicability of supervised contrastive learning. To address this challenge, we introduce the concept of ``continuous semantic similarity'' to define positive and negative pairs. Instead of directly relying on imprecise class labels, we measure the semantic similarity between example pairs, which quantifies how closely they belong to the same category by iteratively refining weak supervisory signals. Based on this concept, we propose a graph-theoretic framework for weakly-supervised contrastive learning, where semantic similarity serves as the graph weights. Our framework is highly versatile and can be applied to many weakly-supervised learning scenarios. We demonstrate its effectiveness through experiments in two common settings, i.e., noisy label and partial label learning, where existing methods can be easily integrated to significantly improve performance. Theoretically, we establish an error bound for our approach, showing that it can approximate supervised contrastive learning under mild conditions. The implementation code is available at https://github.com/Speechless-10308/WSC.

</details>

### Effective and Efficient Masked Image Generation Models.
- **链接**: [arXiv:2503.07197](https://arxiv.org/abs/2503.07197) · [代码](https://github.com/ML-GSAI/eMIGM)
- **作者**: Zebin You, Jingyang Ou, Xiaolu Zhang, Jun Hu, Jun Zhou, Chongxuan Li
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Although masked image generation models and masked diffusion models are designed with different motivations and objectives, we observe that they can be unified within a single framework. Building upon this insight, we carefully explore the design space of training and sampling, identifying key factors that contribute to both performance and efficiency. Based on the improvements observed during this exploration, we develop our model, referred to as \textbf{eMIGM}. Empirically, eMIGM demonstrates strong performance on ImageNet generation, as measured by Fréchet Inception Distance (FID). In particular, on ImageNet $256\times256$, with similar number of function evaluations (NFEs) and model parameters, eMIGM outperforms the seminal VAR. Moreover, as NFE and model parameters increase, eMIGM achieves performance comparable to the state-of-the-art continuous diffusion model REPA while requiring less than 45\% of the NFE. Additionally, on ImageNet $512\times512$, eMIGM outperforms the strong continuous diffusion model EDM2. Code is available at https://github.com/ML-GSAI/eMIGM.

</details>

## 跨领域论文（完整笔记在其他领域）

- Self-Supervised Learning of Intertwined Content and Positional Features for Object Detection. → [object-detection](../object-detection/Guideline%202025.md)
- PROTOCOL: Partial Optimal Transport-enhanced Contrastive Learning for Imbalanced Multi-view Clustering. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
- Contradiction Retrieval via Contrastive Learning with Sparsity. → [network-pruning](../network-pruning/Guideline%202025.md)
