# Continual Learning — 2022 Guideline

> 领域: 持续学习 / 增量学习（含 VLM/多模态场景）
> 论文数: 29 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Meta-attention for ViT-backed Continual Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00025)
- **作者**: Mengqi Xue, Haofei Zhang, Jie Song, Mingli Song
- **🏷️ 机构**: ZJU
- **会议**: CVPR 2022

### vCLIMB: A Novel Video Class Incremental Learning Benchmark.
- **链接**: [arXiv:2201.09381](https://arxiv.org/abs/2201.09381)
- **作者**: Andrés Villa, Kumail Alhamoud, Victor Escorcia, Fabian Caba Heilbron, Juan León Alcázar, Bernard Ghanem
- **🏷️ 机构**: Pontificia Universidad Cat&#x00F3;lica de Chile, King Abdullah University of Science and Technology (KAUST), Samsung AI Center Cambridge
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > Continual learning (CL) is under-explored in the video domain. The few existing works contain splits with imbalanced class distributions over the tasks, or study the problem in unsuitable datasets. We introduce vCLIMB, a novel video continual learning benchmark. vCLIMB is a standardized test-bed to analyze catastrophic forgetting of deep models in video continual learning. In contrast to previous work, we focus on class incremental continual learning with models trained on a sequence of disjoint tasks, and distribute the number of classes uniformly across the tasks. We perform in-depth evaluations of existing CL methods in vCLIMB, and observe two unique challenges in video data. The selection of instances to store in episodic memory is performed at the frame level. Second, untrimmed training data influences the effectiveness of frame sampling strategies. We address these two challenges by proposing a temporal consistency regularization that can be applied on top of memory-based continual learning methods. Our approach significantly improves the baseline, by up to 24% on the untrimmed continual learning task.

### Overcoming Catastrophic Forgetting in Incremental Object Detection via Elastic Response Distillation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00921)
- **作者**: Tao Feng, Mang Wang, Hangjie Yuan
- **🏷️ 机构**: Alibaba Group, Zhejiang University
- **会议**: CVPR 2022

### Learning to Prompt for Continual Learning.
- **链接**: [arXiv:2112.08654](https://arxiv.org/abs/2112.08654) · [代码](https://github.com/google-research/l2p)
- **作者**: Zifeng Wang, Zizhao Zhang, Chen-Yu Lee, Han Zhang, Ruoxi Sun, Xiaoqi Ren et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > The mainstream paradigm behind continual learning has been to adapt the model parameters to non-stationary data distributions, where catastrophic forgetting is the central challenge. Typical methods rely on a rehearsal buffer or known task identity at test time to retrieve learned knowledge and address forgetting, while this work presents a new paradigm for continual learning that aims to train a more succinct memory system without accessing task identity at test time. Our method learns to dynamically prompt (L2P) a pre-trained model to learn tasks sequentially under different task transitions. In our proposed framework, prompts are small learnable parameters, which are maintained in a memory space. The objective is to optimize prompts to instruct the model prediction and explicitly manage task-invariant and task-specific knowledge while maintaining model plasticity. We conduct comprehensive experiments under popular image classification benchmarks with different challenging continual learning settings, where L2P consistently outperforms prior state-of-the-art methods. Surprisingly, L2P achieves competitive results against rehearsal-based methods even without a rehearsal buffer and is directly applicable to challenging task-agnostic continual learning. Source code is available at https://github.com/google-research/l2p.

### Learning Bayesian Sparse Networks with Full Experience Replay for Continual Learning.
- **链接**: [arXiv:2202.10203](https://arxiv.org/abs/2202.10203)
- **作者**: Qingsen Yan, Dong Gong, Yuhang Liu, Anton van den Hengel, Javen Qinfeng Shi
- **🏷️ 机构**: The Australian Institute for Machine Learning, The University of Adelaide,Australia
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > Continual Learning (CL) methods aim to enable machine learning models to learn new tasks without catastrophic forgetting of those that have been previously mastered. Existing CL approaches often keep a buffer of previously-seen samples, perform knowledge distillation, or use regularization techniques towards this goal. Despite their performance, they still suffer from interference across tasks which leads to catastrophic forgetting. To ameliorate this problem, we propose to only activate and select sparse neurons for learning current and past tasks at any stage. More parameters space and model capacity can thus be reserved for the future tasks. This minimizes the interference between parameters for different tasks. To do so, we propose a Sparse neural Network for Continual Learning (SNCL), which employs variational Bayesian sparsity priors on the activations of the neurons in all layers. Full Experience Replay (FER) provides effective supervision in learning the sparse activations of the neurons in different layers. A loss-aware reservoir-sampling strategy is developed to maintain the memory buffer. The proposed method is agnostic as to the network structures and the task boundaries. Experiments on different datasets show that our approach achieves state-of-the-art performance for mitigating forgetting.

### Continual Learning with Lifelong Vision Transformer.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00027)
- **作者**: Zhen Wang, Liu Liu, Yiqun Duan, Yajing Kong, Dacheng Tao
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2022

### Online Continual Learning on a Contaminated Data Stream with Blurry Task Boundaries.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00906)
- **作者**: Jihwan Bang, Hyunseo Koh, Seulki Park, Hwanjun Song, Jung-Woo Ha, Jonghyun Choi
- **🏷️ 机构**: NAVER CLOVA, NAVER AI Lab
- **会议**: CVPR 2022

### Probing Representation Forgetting in Supervised and Unsupervised Continual Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01621)
- **作者**: MohammadReza Davari, Nader Asadi, Sudhir P. Mudur, Rahaf Aljundi, Eugene Belilovsky
- **🏷️ 机构**: Concordia University, Toyota Motor Europe
- **会议**: CVPR 2022

### DyTox: Transformers for Continual Learning with DYnamic TOken eXpansion.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00907)
- **作者**: Arthur Douillard, Alexandre Ramé, Guillaume Couairon, Matthieu Cord
- **🏷️ 机构**: Sorbonne Universite
- **会议**: CVPR 2022

### Not Just Selection, but Exploration: Online Class-Incremental Continual Learning via Dual View Consistency.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00729)
- **作者**: Yanan Gu, Xu Yang, Kun Wei, Cheng Deng
- **🏷️ 机构**: School of Electronic Engineering, Xidian University,Xi&#x0027;an,China,710071
- **会议**: CVPR 2022

### On Generalizing Beyond Domains in Cross-Domain Continual Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00905)
- **作者**: Christian Simon, Masoud Faraki, Yi-Hsuan Tsai, Xiang Yu, Samuel Schulter, Yumin Suh et al.
- **🏷️ 机构**: The Australian National University, Phiar Technologies, Monash University
- **会议**: CVPR 2022

### GCR: Gradient Coreset based Replay Buffer Selection for Continual Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00020)
- **作者**: Rishabh Tiwari, KrishnaTeja Killamsetty, Rishabh K. Iyer, Pradeep Shenoy
- **🏷️ 机构**: Indian Institute of Technology (ISM),Department of Physics,Dhanbad, University of Texas at Dallas,Department of Computer Science, Google Research,India
- **会议**: CVPR 2022

### Continual Learning for Visual Search with Backward Consistent Feature Embedding.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01620)
- **作者**: Timmy S. T. Wan, Jun-Cheng Chen, Tzer-Yi Wu, Chu-Song Chen
- **🏷️ 机构**: National Taiwan University, Academia Sinica, Ucfunnel Co. Ltd.
- **会议**: CVPR 2022

### MetaFSCIL: A Meta-Learning Approach for Few-Shot Class Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01377)
- **作者**: Zhixiang Chi, Li Gu, Huan Liu, Yang Wang, Yuanhao Yu, Jin Tang
- **🏷️ 机构**: Noah&#x0027;s Ark Lab, Huawei Technologies
- **会议**: CVPR 2022

### Learning to Imagine: Diversify Memory for Incremental Learning using Unlabeled Data.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00933)
- **作者**: Yu-Ming Tang, Yi-Xing Peng, Wei-Shi Zheng
- **🏷️ 机构**: Sun Yat-sen University,School of Computer Science and Engineering,China
- **会议**: CVPR 2022

### Forward Compatible Few-Shot Class-Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00884)
- **作者**: Da-Wei Zhou, Fu-Yun Wang, Han-Jia Ye, Liang Ma, Shiliang Pu, De-Chuan Zhan
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2022

### Self-Sustaining Representation Expansion for Non-Exemplar Class-Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00908)
- **作者**: Kai Zhu, Wei Zhai, Yang Cao, Jiebo Luo, Zhengjun Zha
- **🏷️ 机构**: University of Science and Technology of China, University of Rochester
- **会议**: CVPR 2022

### Doodle It Yourself: Class Incremental Learning by Drawing a Few Sketches.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00233)
- **作者**: Ayan Kumar Bhunia, Viswanatha Reddy Gajjala, Subhadeep Koley, Rohit Kundu, Aneeshan Sain, Tao Xiang et al.
- **🏷️ 机构**: University of Surrey,SketchX, CVSSP,United Kingdom
- **会议**: CVPR 2022

### Incremental Learning in Semantic Segmentation from Image Labels.
- **链接**: [arXiv:2112.01882](https://arxiv.org/abs/2112.01882) · [代码](https://github.com/fcdl94/WILSON)
- **作者**: Fabio Cermelli, Dario Fontanel, Antonio Tavera, Marco Ciccone, Barbara Caputo
- **🏷️ 机构**: Politecnico di Torino
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > Although existing semantic segmentation approaches achieve impressive results, they still struggle to update their models incrementally as new categories are uncovered. Furthermore, pixel-by-pixel annotations are expensive and time-consuming. This paper proposes a novel framework for Weakly Incremental Learning for Semantic Segmentation, that aims at learning to segment new classes from cheap and largely available image-level labels. As opposed to existing approaches, that need to generate pseudo-labels offline, we use an auxiliary classifier, trained with image-level labels and regularized by the segmentation model, to obtain pseudo-supervision online and update the model incrementally. We cope with the inherent noise in the process by using soft-labels generated by the auxiliary classifier. We demonstrate the effectiveness of our approach on the Pascal VOC and COCO datasets, outperforming offline weakly-supervised methods and obtaining results comparable with incremental learning methods with full supervision. Code can be found at https://github.com/fcdl94/WILSON.

### Few-Shot Incremental Learning for Label-to-Image Translation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00368)
- **作者**: Pei Chen, Yangkang Zhang, Zejian Li, Lingyun Sun
- **🏷️ 机构**: Alibaba-Zhejiang University Joint Institute of Frontier Technologies, Zhejiang University
- **会议**: CVPR 2022

### Federated Class-Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00992)
- **作者**: Jiahua Dong, Lixu Wang, Zhen Fang, Gan Sun, Shichao Xu, Xiao Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2022

### Constrained Few-shot Class-incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00885)
- **作者**: Michael Hersche, Geethan Karunaratne, Giovanni Cherubini, Luca Benini, Abu Sebastian, Abbas Rahimi
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2022

### Energy-based Latent Aligner for Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00730)
- **作者**: K. J. Joseph, Salman Khan, Fahad Shahbaz Khan, Rao Muhammad Anwer, Vineeth N. Balasubramanian
- **🏷️ 机构**: Indian Institute of Technology,Hyderabad,India, Mohamed bin Zayed University of AI,UAE
- **会议**: CVPR 2022

### Class-Incremental Learning by Knowledge Distillation with Adaptive Feature Consolidation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01560)
- **作者**: Minsoo Kang, Jaeyoo Park, Bohyung Han
- **🏷️ 机构**: ECE, ASRI, &#x0026; IPAI, Seoul National University
- **会议**: CVPR 2022

### Towards Better Plasticity-Stability Trade-off in Incremental Learning: A Simple Linear Connector.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00019)
- **作者**: Guoliang Lin, Hanlu Chu, Hanjiang Lai
- **🏷️ 机构**: Sun Yat-sen University,Guangdong,China, South China Normal University,Guangdong,China
- **会议**: CVPR 2022

### Mimicking the Oracle: An Initial Phase Decorrelation Approach for Class Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01622) · 📚 被引 61
- **作者**: Yujun Shi, Kuangqi Zhou, Jian Liang, Zihang Jiang, Jiashi Feng, Philip H. S. Torr et al.
- **🏷️ 机构**: National University of Singapore, Institute of Automation, Chinese Academy of Sciences (CAS), ByteDance Inc
- **会议**: CVPR 2022

### Bring Evanescent Representations to Life in Lifelong Class Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01623)
- **作者**: Marco Toldo, Mete Ozay
- **🏷️ 机构**: Samsung Research UK
- **会议**: CVPR 2022

### Class-Incremental Learning with Strong Pre-trained Models.
- **链接**: [arXiv:2204.03634](https://arxiv.org/abs/2204.03634) · [代码](https://github.com/amazon-research/sp-cil)
- **作者**: Tz-Ying Wu, Gurumurthy Swaminathan, Zhizhong Li, Avinash Ravichandran, Nuno Vasconcelos, Rahul Bhotika et al.
- **🏷️ 机构**: AWS AI Labs, UC San Diego
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > Class-incremental learning (CIL) has been widely studied under the setting of starting from a small number of classes (base classes). Instead, we explore an understudied real-world setting of CIL that starts with a strong model pre-trained on a large number of base classes. We hypothesize that a strong base model can provide a good representation for novel classes and incremental learning can be done with small adaptations. We propose a 2-stage training scheme, i) feature augmentation -- cloning part of the backbone and fine-tuning it on the novel data, and ii) fusion -- combining the base and novel classifiers into a unified classifier. Experiments show that the proposed method significantly outperforms state-of-the-art CIL methods on the large-scale ImageNet dataset (e.g. +10% overall accuracy than the best). We also propose and analyze understudied practical CIL scenarios, such as base-novel overlap with distribution shift. Our proposed method is robust and generalizes to all analyzed CIL settings. Code is available at https://github.com/amazon-research/sp-cil.

### General Incremental Learning with Domain-aware Categorical Representations.
- **链接**: [arXiv:2204.04078](https://arxiv.org/abs/2204.04078)
- **作者**: Jiangwei Xie, Shipeng Yan, Xuming He
- **🏷️ 机构**: School of Information Science and Technology, ShanghaiTech University
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > Continual learning is an important problem for achieving human-level intelligence in real-world applications as an agent must continuously accumulate knowledge in response to streaming data/tasks. In this work, we consider a general and yet under-explored incremental learning problem in which both the class distribution and class-specific domain distribution change over time. In addition to the typical challenges in class incremental learning, this setting also faces the intra-class stability-plasticity dilemma and intra-class domain imbalance problems. To address above issues, we develop a novel domain-aware continual learning method based on the EM framework. Specifically, we introduce a flexible class representation based on the von Mises-Fisher mixture model to capture the intra-class structure, using an expansion-and-reduction strategy to dynamically increase the number of components according to the class complexity. Moreover, we design a bi-level balanced memory to cope with data imbalances within and across classes, which combines with a distillation loss to achieve better inter- and intra-class stability-plasticity trade-off. We conduct exhaustive experiments on three benchmarks: iDigits, iDomainNet and iCIFAR-20. The results show that our approach consistently outperforms previous methods by a significant margin, demonstrating its superiority.
