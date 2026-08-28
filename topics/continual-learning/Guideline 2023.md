# Continual Learning — 2023 Guideline

> 领域: 持续学习 / 增量学习（含 VLM/多模态场景）
> 论文数: 29 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Geometry and Uncertainty-Aware 3D Point Cloud Class-Incremental Semantic Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02084) · 📚 被引 29
- **作者**: Yuwei Yang, Munawar Hayat, Zhao Jin, Chao Ren, Yinjie Lei
- **🏷️ 机构**: Sichuan University, Monash University
- **会议**: CVPR 2023

### Learning with Fantasy: Semantic-Aware Virtual Contrastive Constraint for Few-Shot Class-Incremental Learning.
- **链接**: [arXiv:2304.00426](https://arxiv.org/abs/2304.00426) · [代码](https://github.com/zysong0113/SAVC) · 📚 被引 119
- **作者**: Zeyin Song, Yifan Zhao, Yujun Shi, Peixi Peng, Li Yuan, Yonghong Tian
- **🏷️ 机构**: School of Electronic and Computer Engineering, Peking University, School of Computer Science, Peking University, National University of Singapore
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Few-shot class-incremental learning (FSCIL) aims at learning to classify new classes continually from limited samples without forgetting the old classes. The mainstream framework tackling FSCIL is first to adopt the cross-entropy (CE) loss for training at the base session, then freeze the feature extractor to adapt to new classes. However, in this work, we find that the CE loss is not ideal for the base session training as it suffers poor class separation in terms of representations, which further degrades generalization to novel classes. One tempting method to mitigate this problem is to apply an additional naive supervised contrastive learning (SCL) in the base session. Unfortunately, we find that although SCL can create a slightly better representation separation among different base classes, it still struggles to separate base classes and new classes. Inspired by the observations made, we propose Semantic-Aware Virtual Contrastive model (SAVC), a novel method that facilitates separation between new classes and base classes by introducing virtual classes to SCL. These virtual classes, which are generated via pre-defined transformations, not only act as placeholders for unseen classes in the representation space, but also provide diverse semantic information. By learning to recognize and contrast in the fantasy space fostered by virtual classes, our SAVC significantly boosts base class separation and novel class generalization, achieving new state-of-the-art performance on the three widely-used FSCIL benchmark datasets. Code is available at: https://github.com/zysong0113/SAVC.

</details>

### PCR: Proxy-Based Contrastive Replay for Online Class-Incremental Continual Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02322) · 📚 被引 74
- **作者**: Huiwei Lin, Baoquan Zhang, Shanshan Feng, Xutao Li, Yunming Ye
- **🏷️ 机构**: Harbin Institute of Technology,Shenzhen
- **会议**: CVPR 2023

### CODA-Prompt: COntinual Decomposed Attention-Based Prompting for Rehearsal-Free Continual Learning.
- **链接**: [arXiv:2211.13218](https://arxiv.org/abs/2211.13218) · [代码](https://github.com/GT-RIPL/CODA-Prompt) · 📚 被引 320
- **作者**: James Seale Smith, Leonid Karlinsky, Vyshnavi Gutta, Paola Cascante-Bonilla, Donghyun Kim, Assaf Arbelle et al.
- **🏷️ 机构**: Georgia Institute of Technology, MIT-IBM Watson AI Lab, IBM Research
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Computer vision models suffer from a phenomenon known as catastrophic forgetting when learning novel concepts from continuously shifting training data. Typical solutions for this continual learning problem require extensive rehearsal of previously seen data, which increases memory costs and may violate data privacy. Recently, the emergence of large-scale pre-trained vision transformer models has enabled prompting approaches as an alternative to data-rehearsal. These approaches rely on a key-query mechanism to generate prompts and have been found to be highly resistant to catastrophic forgetting in the well-established rehearsal-free continual learning setting. However, the key mechanism of these methods is not trained end-to-end with the task sequence. Our experiments show that this leads to a reduction in their plasticity, hence sacrificing new task accuracy, and inability to benefit from expanded parameter capacity. We instead propose to learn a set of prompt components which are assembled with input-conditioned weights to produce input-conditioned prompts, resulting in a novel attention-based end-to-end key-query scheme. Our experiments show that we outperform the current SOTA method DualPrompt on established benchmarks by as much as 4.5% in average final accuracy. We also outperform the state of art by as much as 4.4% accuracy on a continual learning benchmark which contains both class-incremental and domain-incremental task shifts, corresponding to many practical settings. Our code is available at https://github.com/GT-RIPL/CODA-Prompt

</details>

### Regularizing Second-Order Influences for Continual Learning.
- **链接**: [arXiv:2304.10177](https://arxiv.org/abs/2304.10177) · [代码](https://github.com/feifeiobama/InfluenceCL) · 📚 被引 22
- **作者**: Zhicheng Sun, Yadong Mu, Gang Hua
- **🏷️ 机构**: Peking University, Wormpex AI Research
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning aims to learn on non-stationary data streams without catastrophically forgetting previous knowledge. Prevalent replay-based methods address this challenge by rehearsing on a small buffer holding the seen data, for which a delicate sample selection strategy is required. However, existing selection schemes typically seek only to maximize the utility of the ongoing selection, overlooking the interference between successive rounds of selection. Motivated by this, we dissect the interaction of sequential selection steps within a framework built on influence functions. We manage to identify a new class of second-order influences that will gradually amplify incidental bias in the replay buffer and compromise the selection process. To regularize the second-order effects, a novel selection objective is proposed, which also has clear connections to two widely adopted criteria. Furthermore, we present an efficient implementation for optimizing the proposed criterion. Experiments on multiple continual learning benchmarks demonstrate the advantage of our approach over state-of-the-art methods. Code is available at https://github.com/feifeiobama/InfluenceCL.

</details>

### CoMFormer: Continual Learning in Semantic and Panoptic Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00294) · 📚 被引 33
- **作者**: Fabio Cermelli, Matthieu Cord, Arthur Douillard
- **🏷️ 机构**: Politecnico di Torino, Sorbonne Universit&#x00E9;
- **会议**: CVPR 2023

### Exploring Data Geometry for Continual Learning.
- **链接**: [arXiv:2304.03931](https://arxiv.org/abs/2304.03931) · 📚 被引 12
- **作者**: Zhi Gao, Chen Xu, Feng Li, Yunde Jia, Mehrtash Harandi, Yuwei Wu
- **🏷️ 机构**: School of Computer Science &#x0026; Technology, Beijing Institute of Technology,Beijing Key Laboratory of Intelligent Information Technology,China, Shenzhen MSU-BIT University,Guangdong Laboratory of Machine Perception and Intelligent Computing,China, Monash University, and Data61,Department of Electrical and Computer Systems Eng.,Australia
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning aims to efficiently learn from a non-stationary stream of data while avoiding forgetting the knowledge of old data. In many practical applications, data complies with non-Euclidean geometry. As such, the commonly used Euclidean space cannot gracefully capture non-Euclidean geometric structures of data, leading to inferior results. In this paper, we study continual learning from a novel perspective by exploring data geometry for the non-stationary stream of data. Our method dynamically expands the geometry of the underlying space to match growing geometric structures induced by new data, and prevents forgetting by keeping geometric structures of old data into account. In doing so, making use of the mixed curvature space, we propose an incremental search scheme, through which the growing geometric structures are encoded. Then, we introduce an angular-regularization loss and a neighbor-robustness loss to train the model, capable of penalizing the change of global geometric structures and local geometric structures. Experiments show that our method achieves better performance than baseline methods designed in Euclidean space.

</details>

### Real-Time Evaluation in Online Continual Learning: A New Hope.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01144) · 📚 被引 35
- **作者**: Yasir Ghunaim, Adel Bibi, Kumail Alhamoud, Motasem Alfarra, Hasan Abed Al Kader Hammoud, Ameya Prabhu et al.
- **🏷️ 机构**: King Abdullah University of Science and Technology (KAUST), University of Oxford
- **会议**: CVPR 2023

### Preserving Linear Separability in Continual Learning by Backward Feature Projection.
- **链接**: [arXiv:2303.14595](https://arxiv.org/abs/2303.14595) · [代码](https://github.com/rvl-lab-utoronto/BFP) · 📚 被引 12
- **作者**: Qiao Gu, Dongsub Shim, Florian Shkurti
- **🏷️ 机构**: University of Toronto, LG AI Research
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Catastrophic forgetting has been a major challenge in continual learning, where the model needs to learn new tasks with limited or no access to data from previously seen tasks. To tackle this challenge, methods based on knowledge distillation in feature space have been proposed and shown to reduce forgetting. However, most feature distillation methods directly constrain the new features to match the old ones, overlooking the need for plasticity. To achieve a better stability-plasticity trade-off, we propose Backward Feature Projection (BFP), a method for continual learning that allows the new features to change up to a learnable linear transformation of the old features. BFP preserves the linear separability of the old classes while allowing the emergence of new feature directions to accommodate new classes. BFP can be integrated with existing experience replay methods and boost performance by a significant margin. We also demonstrate that BFP helps learn a better representation space, in which linear separability is well preserved during continual learning and linear probing achieves high classification accuracy. The code can be found at https://github.com/rvl-lab-utoronto/BFP

</details>

### Dealing with Cross-Task Class Discrimination in Online Continual Learning.
- **链接**: [arXiv:2305.14657](https://arxiv.org/abs/2305.14657) · 📚 被引 17
- **作者**: Yiduo Guo, Bing Liu, Dongyan Zhao
- **🏷️ 机构**: Wangxuan Institute of Computer Technology, Peking University, University of Illinois Chicago,Department of Computer Science
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing continual learning (CL) research regards catastrophic forgetting (CF) as almost the only challenge. This paper argues for another challenge in class-incremental learning (CIL), which we call cross-task class discrimination (CTCD),~i.e., how to establish decision boundaries between the classes of the new task and old tasks with no (or limited) access to the old task data. CTCD is implicitly and partially dealt with by replay-based methods. A replay method saves a small amount of data (replay data) from previous tasks. When a batch of current task data arrives, the system jointly trains the new data and some sampled replay data. The replay data enables the system to partially learn the decision boundaries between the new classes and the old classes as the amount of the saved data is small. However, this paper argues that the replay approach also has a dynamic training bias issue which reduces the effectiveness of the replay data in solving the CTCD problem. A novel optimization objective with a gradient-based adaptive method is proposed to dynamically deal with the problem in the online CL process. Experimental results show that the new method achieves much better results in online CL.

</details>

### Achieving a Better Stability-Plasticity Trade-off via Auxiliary Networks in Continual Learning.
- **链接**: [arXiv:2303.09483](https://arxiv.org/abs/2303.09483) · 📚 被引 41
- **作者**: Sanghwan Kim, Lorenzo Noci, Antonio Orvieto, Thomas Hofmann
- **🏷️ 机构**: ETH Z&#x00FC;rich,Z&#x00FC;rich,Switzerland
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In contrast to the natural capabilities of humans to learn new tasks in a sequential fashion, neural networks are known to suffer from catastrophic forgetting, where the model's performances on old tasks drop dramatically after being optimized for a new task. Since then, the continual learning (CL) community has proposed several solutions aiming to equip the neural network with the ability to learn the current task (plasticity) while still achieving high accuracy on the previous tasks (stability). Despite remarkable improvements, the plasticity-stability trade-off is still far from being solved and its underlying mechanism is poorly understood. In this work, we propose Auxiliary Network Continual Learning (ANCL), a novel method that applies an additional auxiliary network which promotes plasticity to the continually learned model which mainly focuses on stability. More concretely, the proposed framework materializes in a regularizer that naturally interpolates between plasticity and stability, surpassing strong baselines on task incremental and class incremental scenarios. Through extensive analyses on ANCL solutions, we identify some essential principles beneath the stability-plasticity trade-off.

</details>

### Adaptive Plasticity Improvement for Continual Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00755) · 📚 被引 17
- **作者**: Yan-Shuo Liang, Wu-Jun Li
- **🏷️ 机构**: Nanjing University,National Key Laboratory for Novel Software Technology,Department of Computer Science and Technology,P. R. China
- **会议**: CVPR 2023

### Heterogeneous Continual Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01534)
- **作者**: Divyam Madaan, Hongxu Yin, Wonmin Byeon, Jan Kautz, Pavlo Molchanov
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### Bilateral Memory Consolidation for Continual Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01538) · 📚 被引 16
- **作者**: Xing Nie, Shixiong Xu, Xiyan Liu, Gaofeng Meng, Chunlei Huo, Shiming Xiang
- **🏷️ 机构**: Institute of Automation, Chinese Academy of Sciences,State Key Laboratory of Multimodal Artificial Intelligence Systems, Baidu Inc.,China
- **会议**: CVPR 2023

### Computationally Budgeted Continual Learning: What Does Matter?
- **链接**: [arXiv:2303.11165](https://arxiv.org/abs/2303.11165) · [代码](https://github.com/drimpossible/BudgetCL) · 📚 被引 33
- **作者**: Ameya Prabhu, Hasan Abed Al Kader Hammoud, Puneet K. Dokania, Philip H. S. Torr, Ser-Nam Lim, Bernard Ghanem et al.
- **🏷️ 机构**: University of Oxford, King Abdullah University of Science and Technology (KAUST), Meta AI
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual Learning (CL) aims to sequentially train models on streams of incoming data that vary in distribution by preserving previous knowledge while adapting to new data. Current CL literature focuses on restricted access to previously seen data, while imposing no constraints on the computational budget for training. This is unreasonable for applications in-the-wild, where systems are primarily constrained by computational and time budgets, not storage. We revisit this problem with a large-scale benchmark and analyze the performance of traditional CL approaches in a compute-constrained setting, where effective memory samples used in training can be implicitly restricted as a consequence of limited computation. We conduct experiments evaluating various CL sampling strategies, distillation losses, and partial fine-tuning on two large-scale datasets, namely ImageNet2K and Continual Google Landmarks V2 in data incremental, class incremental, and time incremental settings. Through extensive experiments amounting to a total of over 1500 GPU-hours, we find that, under compute-constrained setting, traditional CL approaches, with no exception, fail to outperform a simple minimal baseline that samples uniformly from memory. Our conclusions are consistent in a different number of stream time steps, e.g., 20 to 200, and under several computational budgets. This suggests that most existing CL methods are particularly too computationally expensive for realistic budgeted deployment. Code for this project is available at: https://github.com/drimpossible/BudgetCL.

</details>

### PIVOT: Prompting for Video Continual Learning.
- **链接**: [arXiv:2212.04842](https://arxiv.org/abs/2212.04842) · 📚 被引 44
- **作者**: Andrés Villa, Juan León Alcázar, Motasem Alfarra, Kumail Alhamoud, Julio Hurtado, Fabian Caba Heilbron et al.
- **🏷️ 机构**: Pontificia Universidad Cat&#x00F3;lica de Chile, King Abdullah University of Science and Technology (KAUST), University of Pisa
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Modern machine learning pipelines are limited due to data availability, storage quotas, privacy regulations, and expensive annotation processes. These constraints make it difficult or impossible to train and update large-scale models on such dynamic annotated sets. Continual learning directly approaches this problem, with the ultimate goal of devising methods where a deep neural network effectively learns relevant patterns for new (unseen) classes, without significantly altering its performance on previously learned ones. In this paper, we address the problem of continual learning for video data. We introduce PIVOT, a novel method that leverages extensive knowledge in pre-trained models from the image domain, thereby reducing the number of trainable parameters and the associated forgetting. Unlike previous methods, ours is the first approach that effectively uses prompting mechanisms for continual learning without any in-domain pre-training. Our experiments show that PIVOT improves state-of-the-art methods by a significant 27% on the 20-task ActivityNet setup.

</details>

### MetaMix: Towards Corruption-Robust Continual Learning with Temporally Self-Adaptive Data Transformation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02349) · 📚 被引 6
- **作者**: Zhenyi Wang, Li Shen, Donglin Zhan, Qiuling Suo, Yanjun Zhu, Tiehang Duan et al.
- **🏷️ 机构**: State University of New York at Buffalo,USA, JD Explore Academy,China, Columbia University,USA
- **会议**: CVPR 2023

### VQACL: A Novel Visual Question Answering Continual Learning Setting.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01831) · 📚 被引 31
- **作者**: Xi Zhang, Feifei Zhang, Changsheng Xu
- **🏷️ 机构**: Institute of Automation, Chinese Academy of Sciences,State Key Laboratory of Multimodal Artificial Intelligence Systems, School of Computer Science and Engineering, Tianjin University of Technology
- **会议**: CVPR 2023

### Rethinking Gradient Projection Continual Learning: Stability/Plasticity Feature Space Decoupling.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00362) · 📚 被引 24
- **作者**: Zhen Zhao, Zhizhong Zhang, Xin Tan, Jun Liu, Yanyun Qu, Yuan Xie et al.
- **🏷️ 机构**: School of Computer Science and Technology, East China Normal University,Shanghai,China, Tencent Youtu Lab, School of Informatics, Xiamen University,Fujian,China
- **会议**: CVPR 2023

### Class-Incremental Exemplar Compression for Class-Incremental Learning.
- **链接**: [arXiv:2303.14042](https://arxiv.org/abs/2303.14042) · [代码](https://github.com/xfflzl/CIM-CIL) · 📚 被引 71
- **作者**: Zilin Luo, Yaoyao Liu, Bernt Schiele, Qianru Sun
- **🏷️ 机构**: Singapore Management University, Saarland Informatics Campus,Max Planck Institute for Informatics
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Exemplar-based class-incremental learning (CIL) finetunes the model with all samples of new classes but few-shot exemplars of old classes in each incremental phase, where the "few-shot" abides by the limited memory budget. In this paper, we break this "few-shot" limit based on a simple yet surprisingly effective idea: compressing exemplars by downsampling non-discriminative pixels and saving "many-shot" compressed exemplars in the memory. Without needing any manual annotation, we achieve this compression by generating 0-1 masks on discriminative pixels from class activation maps (CAM). We propose an adaptive mask generation model called class-incremental masking (CIM) to explicitly resolve two difficulties of using CAM: 1) transforming the heatmaps of CAM to 0-1 masks with an arbitrary threshold leads to a trade-off between the coverage on discriminative pixels and the quantity of exemplars, as the total memory is fixed; and 2) optimal thresholds vary for different object classes, which is particularly obvious in the dynamic environment of CIL. We optimize the CIM model alternatively with the conventional CIL model through a bilevel optimization problem. We conduct extensive experiments on high-resolution CIL benchmarks including Food-101, ImageNet-100, and ImageNet-1000, and show that using the compressed exemplars by CIM can achieve a new state-of-the-art CIL accuracy, e.g., 4.8 percentage points higher than FOSTER on 10-Phase ImageNet-1000. Our code is available at https://github.com/xfflzl/CIM-CIL.

</details>

### Decoupling Learning and Remembering: a Bilevel Memory Framework with Knowledge Projection for Task-Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01933) · 📚 被引 11
- **作者**: Wenju Sun, Qingyong Li, Jing Zhang, Wen Wang, Yangli-ao Geng
- **🏷️ 机构**: Beijing Jiaotong University,Beijing Key Lab of Traffic Data Analysis and Mining
- **会议**: CVPR 2023

### Rebalancing Batch Normalization for Exemplar-Based Class-Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01927) · 📚 被引 21
- **作者**: Sungmin Cha, Sungjun Cho, Dasol Hwang, Sunwon Hong, Moontae Lee, Taesup Moon
- **🏷️ 机构**: Seoul National University,Department of ECE, LG AI Research
- **会议**: CVPR 2023

### DKT: Diverse Knowledge Transfer Transformer for Class Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02321) · 📚 被引 21
- **作者**: Xinyuan Gao, Yuhang He, Songlin Dong, Jie Cheng, Xing Wei, Yihong Gong
- **🏷️ 机构**: School of Software Engineering, Xi&#x0027;an Jiaotong University, Institute of Artificial Intelligence and Robotics, Xi&#x0027;an Jiaotong University, Huawei Technologies,ACS Lab,Shenzhen,China
- **会议**: CVPR 2023

### Dense Network Expansion for Class Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01141) · 📚 被引 68
- **作者**: Zhiyuan Hu, Yunsheng Li, Jiancheng Lyu, Dashan Gao, Nuno Vasconcelos
- **🏷️ 机构**: UC San Diego, Microsoft Cloud &#x002B; AI, Qualcomm AI Research
- **会议**: CVPR 2023

### On the Stability-Plasticity Dilemma of Class-Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01934) · 📚 被引 59
- **作者**: Dongwan Kim, Bohyung Han
- **🏷️ 机构**: Seoul National University,Computer Vision Laboratory, ECE
- **会议**: CVPR 2023

### CafeBoost: Causal Feature Boost to Eliminate Task-Induced Bias for Class Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01537) · 📚 被引 8
- **作者**: Benliu Qiu, Hongliang Li, Haitao Wen, Heqian Qiu, Lanxiao Wang, Fanman Meng et al.
- **🏷️ 机构**: University of Electronic Science and Technology of China,Chengdu,China
- **会议**: CVPR 2023

### Foundation Model Drives Weakly Incremental Learning for Semantic Segmentation.
- **链接**: [arXiv:2302.14250](https://arxiv.org/abs/2302.14250) · 📚 被引 21
- **作者**: Chaohui Yu, Qiang Zhou, Jingliang Li, Jianlong Yuan, Zhibin Wang, Fan Wang
- **🏷️ 机构**: Alibaba Group, University of the Chinese Academy of Sciences
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Modern incremental learning for semantic segmentation methods usually learn new categories based on dense annotations. Although achieve promising results, pixel-by-pixel labeling is costly and time-consuming. Weakly incremental learning for semantic segmentation (WILSS) is a novel and attractive task, which aims at learning to segment new classes from cheap and widely available image-level labels. Despite the comparable results, the image-level labels can not provide details to locate each segment, which limits the performance of WILSS. This inspires us to think how to improve and effectively utilize the supervision of new classes given image-level labels while avoiding forgetting old ones. In this work, we propose a novel and data-efficient framework for WILSS, named FMWISS. Specifically, we propose pre-training based co-segmentation to distill the knowledge of complementary foundation models for generating dense pseudo labels. We further optimize the noisy pseudo masks with a teacher-student architecture, where a plug-in teacher is optimized with a proposed dense contrastive loss. Moreover, we introduce memory-based copy-paste augmentation to improve the catastrophic forgetting problem of old classes. Extensive experiments on Pascal VOC and COCO datasets demonstrate the superior performance of our framework, e.g., FMWISS achieves 70.7% and 73.3% in the 15-5 VOC setting, outperforming the state-of-the-art method by 3.4% and 6.1%, respectively.

</details>

### Few-Shot Class-Incremental Learning via Class-Aware Bilateral Distillation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01139) · 📚 被引 110
- **作者**: Linglan Zhao, Jing Lu, Yunlu Xu, Zhanzhan Cheng, Dashan Guo, Yi Niu et al.
- **🏷️ 机构**: Shanghai Jiao Tong University,Department of Electronic Engineering, Hikvision Research Institute
- **会议**: CVPR 2023

### Incrementer: Transformer for Class-Incremental Semantic Segmentation with Knowledge Distillation Focusing on Old Class.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00697) · 📚 被引 40
- **作者**: Chao Shang, Hongliang Li, Fanman Meng, Qingbo Wu, Heqian Qiu, Lanxiao Wang
- **🏷️ 机构**: University of Electronic Science and Technology of China
- **会议**: CVPR 2023
