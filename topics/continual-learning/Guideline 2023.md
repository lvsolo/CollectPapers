# Continual Learning — 2023 Guideline

> 领域: 持续学习 / 增量学习（含 VLM/多模态场景）
> 论文数: 16 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Online Bias Correction for Task-Free Continual Learning.
- **链接**: [出版页](https://openreview.net/forum?id=18XzeuYZh_)
- **作者**: Aristotelis Chrysakis, Marie-Francine Moens
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Building a Subspace of Policies for Scalable Continual Learning.
- **链接**: [arXiv:2211.10445](https://arxiv.org/abs/2211.10445)
- **作者**: Jean-Baptiste Gaya, Thang Doan, Lucas Caccia, Laure Soulier, Ludovic Denoyer, Roberta Raileanu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The ability to continuously acquire new knowledge and skills is crucial for autonomous agents. Existing methods are typically based on either fixed-size models that struggle to learn a large number of diverse behaviors, or growing-size models that scale poorly with the number of tasks. In this work, we aim to strike a better balance between an agent's size and performance by designing a method that grows adaptively depending on the task sequence. We introduce Continual Subspace of Policies (CSP), a new approach that incrementally builds a subspace of policies for training a reinforcement learning agent on a sequence of tasks. The subspace's high expressivity allows CSP to perform well for many different tasks while growing sublinearly with the number of tasks. Our method does not suffer from forgetting and displays positive transfer to new tasks. CSP outperforms a number of popular baselines on a wide range of scenarios from two challenging domains, Brax (locomotion) and Continual World (manipulation).

</details>

### Thalamus: a brain-inspired algorithm for biologically-plausible continual learning and disentangled representations.
- **链接**: [出版页](https://openreview.net/forum?id=6orC5MvgPBK)
- **作者**: Ali Hummos
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### New Insights for the Stability-Plasticity Dilemma in Online Continual Learning.
- **链接**: [arXiv:2302.08741](https://arxiv.org/abs/2302.08741) · [代码](https://github.com/whitesnowdrop/MuFAN)
- **作者**: Dahuin Jung, Dongjin Lee, Sunwon Hong, Hyemi Jang, Ho Bae, Sungroh Yoon
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The aim of continual learning is to learn new tasks continuously (i.e., plasticity) without forgetting previously learned knowledge from old tasks (i.e., stability). In the scenario of online continual learning, wherein data comes strictly in a streaming manner, the plasticity of online continual learning is more vulnerable than offline continual learning because the training signal that can be obtained from a single data point is limited. To overcome the stability-plasticity dilemma in online continual learning, we propose an online continual learning framework named multi-scale feature adaptation network (MuFAN) that utilizes a richer context encoding extracted from different levels of a pre-trained network. Additionally, we introduce a novel structure-wise distillation loss and replace the commonly used batch normalization layer with a newly proposed stability-plasticity normalization module to train MuFAN that simultaneously maintains high plasticity and stability. MuFAN outperforms other state-of-the-art continual learning methods on the SVHN, CIFAR100, miniImageNet, and CORe50 datasets. Extensive experiments and ablation studies validate the significance and scalability of each proposed component: 1) multi-scale feature maps from a pre-trained encoder, 2) the structure-wise distillation loss, and 3) the stability-plasticity normalization module in MuFAN. Code is publicly available at https://github.com/whitesnowdrop/MuFAN.

</details>

### Online Boundary-Free Continual Learning by Scheduled Data Prior.
- **链接**: [出版页](https://openreview.net/forum?id=qco4ekz2Epm)
- **作者**: Hyunseo Koh, Minhyuk Seo, Jihwan Bang, Hwanjun Song, Deokki Hong, Seulki Park et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Continual evaluation for lifelong learning: Identifying the stability gap.
- **链接**: [arXiv:2205.13452](https://arxiv.org/abs/2205.13452)
- **作者**: Matthias De Lange, Gido M. van de Ven, Tinne Tuytelaars
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Time-dependent data-generating distributions have proven to be difficult for gradient-based training of neural networks, as the greedy updates result in catastrophic forgetting of previously learned knowledge. Despite the progress in the field of continual learning to overcome this forgetting, we show that a set of common state-of-the-art methods still suffers from substantial forgetting upon starting to learn new tasks, except that this forgetting is temporary and followed by a phase of performance recovery. We refer to this intriguing but potentially problematic phenomenon as the stability gap. The stability gap had likely remained under the radar due to standard practice in the field of evaluating continual learning models only after each task. Instead, we establish a framework for continual evaluation that uses per-iteration evaluation and we define a new set of metrics to quantify worst-case performance. Empirically we show that experience replay, constraint-based replay, knowledge-distillation, and parameter regularization methods are all prone to the stability gap; and that the stability gap can be observed in class-, task-, and domain-incremental learning benchmarks. Additionally, a controlled experiment shows that the stability gap increases when tasks are more dissimilar. Finally, by disentangling gradients into plasticity and stability components, we propose a conceptual explanation for the stability gap.

</details>

### Progressive Prompts: Continual Learning for Language Models.
- **链接**: [arXiv:2301.12314](https://arxiv.org/abs/2301.12314)
- **作者**: Anastasia Razdaibiedina, Yuning Mao, Rui Hou, Madian Khabsa, Mike Lewis, Amjad Almahairi
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce Progressive Prompts - a simple and efficient approach for continual learning in language models. Our method allows forward transfer and resists catastrophic forgetting, without relying on data replay or a large number of task-specific parameters. Progressive Prompts learns a new soft prompt for each task and sequentially concatenates it with the previously learned prompts, while keeping the base model frozen. Experiments on standard continual learning benchmarks show that our approach outperforms state-of-the-art methods, with an improvement >20% in average test accuracy over the previous best-preforming method on T5 model. We also explore a more challenging continual learning setup with longer sequences of tasks and show that Progressive Prompts significantly outperforms prior methods.

</details>

### Error Sensitivity Modulation based Experience Replay: Mitigating Abrupt Representation Drift in Continual Learning.
- **链接**: [arXiv:2302.11344](https://arxiv.org/abs/2302.11344)
- **作者**: Fahad Sarfraz, Elahe Arani, Bahram Zonooz
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Humans excel at lifelong learning, as the brain has evolved to be robust to distribution shifts and noise in our ever-changing environment. Deep neural networks (DNNs), however, exhibit catastrophic forgetting and the learned representations drift drastically as they encounter a new task. This alludes to a different error-based learning mechanism in the brain. Unlike DNNs, where learning scales linearly with the magnitude of the error, the sensitivity to errors in the brain decreases as a function of their magnitude. To this end, we propose \textit{ESMER} which employs a principled mechanism to modulate error sensitivity in a dual-memory rehearsal-based system. Concretely, it maintains a memory of past errors and uses it to modify the learning dynamics so that the model learns more from small consistent errors compared to large sudden errors. We also propose \textit{Error-Sensitive Reservoir Sampling} to maintain episodic memory, which leverages the error history to pre-select low-loss samples as candidates for the buffer, which are better suited for retaining information. Empirical results show that ESMER effectively reduces forgetting and abrupt drift in representations at the task boundary by gradually adapting to the new task while consolidating knowledge. Remarkably, it also enables the model to learn under high levels of label noise, which is ubiquitous in real-world data streams.

</details>

### Optimizing Spca-based Continual Learning: A Theoretical Approach.
- **链接**: [出版页](https://openreview.net/forum?id=Vf6WcUDnY7c)
- **作者**: Chunchun Yang, Malik Tiomoko, Zengfu Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

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
