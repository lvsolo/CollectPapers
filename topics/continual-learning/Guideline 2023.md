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
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02316) · 📚 被引 119
- **作者**: Zeyin Song, Yifan Zhao, Yujun Shi, Peixi Peng, Li Yuan, Yonghong Tian
- **🏷️ 机构**: School of Electronic and Computer Engineering, Peking University, School of Computer Science, Peking University, National University of Singapore
- **会议**: CVPR 2023

### PCR: Proxy-Based Contrastive Replay for Online Class-Incremental Continual Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02322)
- **作者**: Huiwei Lin, Baoquan Zhang, Shanshan Feng, Xutao Li, Yunming Ye
- **🏷️ 机构**: Harbin Institute of Technology,Shenzhen
- **会议**: CVPR 2023

### CODA-Prompt: COntinual Decomposed Attention-Based Prompting for Rehearsal-Free Continual Learning.
- **链接**: [arXiv:2211.13218](https://arxiv.org/abs/2211.13218) · [代码](https://github.com/GT-RIPL/CODA-Prompt)
- **作者**: James Seale Smith, Leonid Karlinsky, Vyshnavi Gutta, Paola Cascante-Bonilla, Donghyun Kim, Assaf Arbelle et al.
- **🏷️ 机构**: Georgia Institute of Technology, MIT-IBM Watson AI Lab, IBM Research
- **会议**: CVPR 2023

- **摘要（英，原文）**:

  > Computer vision models suffer from a phenomenon known as catastrophic forgetting when learning novel concepts from continuously shifting training data. Typical solutions for this continual learning problem require extensive rehearsal of previously seen data, which increases memory costs and may violate data privacy. Recently, the emergence of large-scale pre-trained vision transformer models has enabled prompting approaches as an alternative to data-rehearsal. These approaches rely on a key-query mechanism to generate prompts and have been found to be highly resistant to catastrophic forgetting in the well-established rehearsal-free continual learning setting. However, the key mechanism of these methods is not trained end-to-end with the task sequence. Our experiments show that this leads to a reduction in their plasticity, hence sacrificing new task accuracy, and inability to benefit from expanded parameter capacity. We instead propose to learn a set of prompt components which are assembled with input-conditioned weights to produce input-conditioned prompts, resulting in a novel attention-based end-to-end key-query scheme. Our experiments show that we outperform the current SOTA method DualPrompt on established benchmarks by as much as 4.5% in average final accuracy. We also outperform the state of art by as much as 4.4% accuracy on a continual learning benchmark which contains both class-incremental and domain-incremental task shifts, corresponding to many practical settings. Our code is available at https://github.com/GT-RIPL/CODA-Prompt

### Regularizing Second-Order Influences for Continual Learning.
- **链接**: [arXiv:2304.10177](https://arxiv.org/abs/2304.10177) · [代码](https://github.com/feifeiobama/InfluenceCL)
- **作者**: Zhicheng Sun, Yadong Mu, Gang Hua
- **🏷️ 机构**: Peking University, Wormpex AI Research
- **会议**: CVPR 2023

- **摘要（英，原文）**:

  > Continual learning aims to learn on non-stationary data streams without catastrophically forgetting previous knowledge. Prevalent replay-based methods address this challenge by rehearsing on a small buffer holding the seen data, for which a delicate sample selection strategy is required. However, existing selection schemes typically seek only to maximize the utility of the ongoing selection, overlooking the interference between successive rounds of selection. Motivated by this, we dissect the interaction of sequential selection steps within a framework built on influence functions. We manage to identify a new class of second-order influences that will gradually amplify incidental bias in the replay buffer and compromise the selection process. To regularize the second-order effects, a novel selection objective is proposed, which also has clear connections to two widely adopted criteria. Furthermore, we present an efficient implementation for optimizing the proposed criterion. Experiments on multiple continual learning benchmarks demonstrate the advantage of our approach over state-of-the-art methods. Code is available at https://github.com/feifeiobama/InfluenceCL.

### CoMFormer: Continual Learning in Semantic and Panoptic Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00294)
- **作者**: Fabio Cermelli, Matthieu Cord, Arthur Douillard
- **🏷️ 机构**: Politecnico di Torino, Sorbonne Universit&#x00E9;
- **会议**: CVPR 2023

### Exploring Data Geometry for Continual Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02330)
- **作者**: Zhi Gao, Chen Xu, Feng Li, Yunde Jia, Mehrtash Harandi, Yuwei Wu
- **🏷️ 机构**: School of Computer Science &#x0026; Technology, Beijing Institute of Technology,Beijing Key Laboratory of Intelligent Information Technology,China, Shenzhen MSU-BIT University,Guangdong Laboratory of Machine Perception and Intelligent Computing,China, Monash University, and Data61,Department of Electrical and Computer Systems Eng.,Australia
- **会议**: CVPR 2023

### Real-Time Evaluation in Online Continual Learning: A New Hope.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01144)
- **作者**: Yasir Ghunaim, Adel Bibi, Kumail Alhamoud, Motasem Alfarra, Hasan Abed Al Kader Hammoud, Ameya Prabhu et al.
- **🏷️ 机构**: King Abdullah University of Science and Technology (KAUST), University of Oxford
- **会议**: CVPR 2023

### Preserving Linear Separability in Continual Learning by Backward Feature Projection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02326)
- **作者**: Qiao Gu, Dongsub Shim, Florian Shkurti
- **🏷️ 机构**: University of Toronto, LG AI Research
- **会议**: CVPR 2023

### Dealing with Cross-Task Class Discrimination in Online Continual Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01143)
- **作者**: Yiduo Guo, Bing Liu, Dongyan Zhao
- **🏷️ 机构**: Wangxuan Institute of Computer Technology, Peking University, University of Illinois Chicago,Department of Computer Science
- **会议**: CVPR 2023

### Achieving a Better Stability-Plasticity Trade-off via Auxiliary Networks in Continual Learning.
- **链接**: [arXiv:2303.09483](https://arxiv.org/abs/2303.09483)
- **作者**: Sanghwan Kim, Lorenzo Noci, Antonio Orvieto, Thomas Hofmann
- **🏷️ 机构**: ETH Z&#x00FC;rich,Z&#x00FC;rich,Switzerland
- **会议**: CVPR 2023

- **摘要（英，原文）**:

  > In contrast to the natural capabilities of humans to learn new tasks in a sequential fashion, neural networks are known to suffer from catastrophic forgetting, where the model's performances on old tasks drop dramatically after being optimized for a new task. Since then, the continual learning (CL) community has proposed several solutions aiming to equip the neural network with the ability to learn the current task (plasticity) while still achieving high accuracy on the previous tasks (stability). Despite remarkable improvements, the plasticity-stability trade-off is still far from being solved and its underlying mechanism is poorly understood. In this work, we propose Auxiliary Network Continual Learning (ANCL), a novel method that applies an additional auxiliary network which promotes plasticity to the continually learned model which mainly focuses on stability. More concretely, the proposed framework materializes in a regularizer that naturally interpolates between plasticity and stability, surpassing strong baselines on task incremental and class incremental scenarios. Through extensive analyses on ANCL solutions, we identify some essential principles beneath the stability-plasticity trade-off.

### Adaptive Plasticity Improvement for Continual Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00755)
- **作者**: Yan-Shuo Liang, Wu-Jun Li
- **🏷️ 机构**: Nanjing University,National Key Laboratory for Novel Software Technology,Department of Computer Science and Technology,P. R. China
- **会议**: CVPR 2023

### Heterogeneous Continual Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01534)
- **作者**: Divyam Madaan, Hongxu Yin, Wonmin Byeon, Jan Kautz, Pavlo Molchanov
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### Bilateral Memory Consolidation for Continual Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01538)
- **作者**: Xing Nie, Shixiong Xu, Xiyan Liu, Gaofeng Meng, Chunlei Huo, Shiming Xiang
- **🏷️ 机构**: Institute of Automation, Chinese Academy of Sciences,State Key Laboratory of Multimodal Artificial Intelligence Systems, Baidu Inc.,China
- **会议**: CVPR 2023

### Computationally Budgeted Continual Learning: What Does Matter?
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00360)
- **作者**: Ameya Prabhu, Hasan Abed Al Kader Hammoud, Puneet K. Dokania, Philip H. S. Torr, Ser-Nam Lim, Bernard Ghanem et al.
- **🏷️ 机构**: University of Oxford, King Abdullah University of Science and Technology (KAUST), Meta AI
- **会议**: CVPR 2023

### PIVOT: Prompting for Video Continual Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02319)
- **作者**: Andrés Villa, Juan León Alcázar, Motasem Alfarra, Kumail Alhamoud, Julio Hurtado, Fabian Caba Heilbron et al.
- **🏷️ 机构**: Pontificia Universidad Cat&#x00F3;lica de Chile, King Abdullah University of Science and Technology (KAUST), University of Pisa
- **会议**: CVPR 2023

### MetaMix: Towards Corruption-Robust Continual Learning with Temporally Self-Adaptive Data Transformation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02349)
- **作者**: Zhenyi Wang, Li Shen, Donglin Zhan, Qiuling Suo, Yanjun Zhu, Tiehang Duan et al.
- **🏷️ 机构**: State University of New York at Buffalo,USA, JD Explore Academy,China, Columbia University,USA
- **会议**: CVPR 2023

### VQACL: A Novel Visual Question Answering Continual Learning Setting.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01831)
- **作者**: Xi Zhang, Feifei Zhang, Changsheng Xu
- **🏷️ 机构**: Institute of Automation, Chinese Academy of Sciences,State Key Laboratory of Multimodal Artificial Intelligence Systems, School of Computer Science and Engineering, Tianjin University of Technology
- **会议**: CVPR 2023

### Rethinking Gradient Projection Continual Learning: Stability/Plasticity Feature Space Decoupling.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00362)
- **作者**: Zhen Zhao, Zhizhong Zhang, Xin Tan, Jun Liu, Yanyun Qu, Yuan Xie et al.
- **🏷️ 机构**: School of Computer Science and Technology, East China Normal University,Shanghai,China, Tencent Youtu Lab, School of Informatics, Xiamen University,Fujian,China
- **会议**: CVPR 2023

### Class-Incremental Exemplar Compression for Class-Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01094) · 📚 被引 71
- **作者**: Zilin Luo, Yaoyao Liu, Bernt Schiele, Qianru Sun
- **🏷️ 机构**: Singapore Management University, Saarland Informatics Campus,Max Planck Institute for Informatics
- **会议**: CVPR 2023

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
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01141) · 📚 被引 67
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
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02268) · 📚 被引 21
- **作者**: Chaohui Yu, Qiang Zhou, Jingliang Li, Jianlong Yuan, Zhibin Wang, Fan Wang
- **🏷️ 机构**: Alibaba Group, University of the Chinese Academy of Sciences
- **会议**: CVPR 2023

### Few-Shot Class-Incremental Learning via Class-Aware Bilateral Distillation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01139)
- **作者**: Linglan Zhao, Jing Lu, Yunlu Xu, Zhanzhan Cheng, Dashan Guo, Yi Niu et al.
- **🏷️ 机构**: Shanghai Jiao Tong University,Department of Electronic Engineering, Hikvision Research Institute
- **会议**: CVPR 2023

### Incrementer: Transformer for Class-Incremental Semantic Segmentation with Knowledge Distillation Focusing on Old Class.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00697)
- **作者**: Chao Shang, Hongliang Li, Fanman Meng, Qingbo Wu, Heqian Qiu, Lanxiao Wang
- **🏷️ 机构**: University of Electronic Science and Technology of China
- **会议**: CVPR 2023
