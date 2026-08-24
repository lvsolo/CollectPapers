# Continual Learning — 2023 Guideline

> 领域: 持续学习 / 增量学习（含 VLM/多模态场景）
> 论文数: 19 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### CODA-Prompt: COntinual Decomposed Attention-Based Prompting for Rehearsal-Free Continual Learning.
- **链接**: [arXiv:2211.13218](https://arxiv.org/abs/2211.13218) · [出版页](https://doi.org/10.1109/CVPR52729.2023.01146) · [代码](https://github.com/GT-RIPL/CODA-Prompt) · 📚 被引 319
- **作者**: James Seale Smith, Leonid Karlinsky, Vyshnavi Gutta, Paola Cascante-Bonilla, Donghyun Kim, Assaf Arbelle et al.
- **🏷️ 机构**: Georgia Institute of Technology, MIT-IBM Watson AI Lab, IBM Research
- **会议**: CVPR 2023

- **摘要（英，原文）**:

  > Computer vision models suffer from a phenomenon known as catastrophic forgetting when learning novel concepts from continuously shifting training data. Typical solutions for this continual learning problem require extensive rehearsal of previously seen data, which increases memory costs and may violate data privacy. Recently, the emergence of large-scale pre-trained vision transformer models has enabled prompting approaches as an alternative to data-rehearsal. These approaches rely on a key-query mechanism to generate prompts and have been found to be highly resistant to catastrophic forgetting in the well-established rehearsal-free continual learning setting. However, the key mechanism of these methods is not trained end-to-end with the task sequence. Our experiments show that this leads to a reduction in their plasticity, hence sacrificing new task accuracy, and inability to benefit from expanded parameter capacity. We instead propose to learn a set of prompt components which are assembled with input-conditioned weights to produce input-conditioned prompts, resulting in a novel attention-based end-to-end key-query scheme. Our experiments show that we outperform the current SOTA method DualPrompt on established benchmarks by as much as 4.5% in average final accuracy. We also outperform the state of art by as much as 4.4% accuracy on a continual learning benchmark which contains both class-incremental and domain-incremental task shifts, corresponding to many practical settings. Our code is available at https://github.com/GT-RIPL/CODA-Prompt

### Regularizing Second-Order Influences for Continual Learning.
- **链接**: [arXiv:2304.10177](https://arxiv.org/abs/2304.10177) · [出版页](https://doi.org/10.1109/CVPR52729.2023.01931) · [代码](https://github.com/feifeiobama/InfluenceCL) · 📚 被引 22
- **作者**: Zhicheng Sun, Yadong Mu, Gang Hua
- **🏷️ 机构**: Peking University, Wormpex AI Research
- **会议**: CVPR 2023

- **摘要（英，原文）**:

  > Continual learning aims to learn on non-stationary data streams without catastrophically forgetting previous knowledge. Prevalent replay-based methods address this challenge by rehearsing on a small buffer holding the seen data, for which a delicate sample selection strategy is required. However, existing selection schemes typically seek only to maximize the utility of the ongoing selection, overlooking the interference between successive rounds of selection. Motivated by this, we dissect the interaction of sequential selection steps within a framework built on influence functions. We manage to identify a new class of second-order influences that will gradually amplify incidental bias in the replay buffer and compromise the selection process. To regularize the second-order effects, a novel selection objective is proposed, which also has clear connections to two widely adopted criteria. Furthermore, we present an efficient implementation for optimizing the proposed criterion. Experiments on multiple continual learning benchmarks demonstrate the advantage of our approach over state-of-the-art methods. Code is available at https://github.com/feifeiobama/InfluenceCL.

### CoMFormer: Continual Learning in Semantic and Panoptic Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00294) · 📚 被引 33
- **作者**: Fabio Cermelli, Matthieu Cord, Arthur Douillard
- **🏷️ 机构**: Politecnico di Torino, Sorbonne Universit&#x00E9;
- **会议**: CVPR 2023

### Exploring Data Geometry for Continual Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02330) · 📚 被引 12
- **作者**: Zhi Gao, Chen Xu, Feng Li, Yunde Jia, Mehrtash Harandi, Yuwei Wu
- **🏷️ 机构**: School of Computer Science &#x0026; Technology, Beijing Institute of Technology,Beijing Key Laboratory of Intelligent Information Technology,China, Shenzhen MSU-BIT University,Guangdong Laboratory of Machine Perception and Intelligent Computing,China, Monash University, and Data61,Department of Electrical and Computer Systems Eng.,Australia
- **会议**: CVPR 2023

### Real-Time Evaluation in Online Continual Learning: A New Hope.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01144) · 📚 被引 35
- **作者**: Yasir Ghunaim, Adel Bibi, Kumail Alhamoud, Motasem Alfarra, Hasan Abed Al Kader Hammoud, Ameya Prabhu et al.
- **🏷️ 机构**: King Abdullah University of Science and Technology (KAUST), University of Oxford
- **会议**: CVPR 2023

### Preserving Linear Separability in Continual Learning by Backward Feature Projection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02326) · 📚 被引 12
- **作者**: Qiao Gu, Dongsub Shim, Florian Shkurti
- **🏷️ 机构**: University of Toronto, LG AI Research
- **会议**: CVPR 2023

### Dealing with Cross-Task Class Discrimination in Online Continual Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01143) · 📚 被引 17
- **作者**: Yiduo Guo, Bing Liu, Dongyan Zhao
- **🏷️ 机构**: Wangxuan Institute of Computer Technology, Peking University, University of Illinois Chicago,Department of Computer Science
- **会议**: CVPR 2023

### Achieving a Better Stability-Plasticity Trade-off via Auxiliary Networks in Continual Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01148) · 📚 被引 40
- **作者**: Sanghwan Kim, Lorenzo Noci, Antonio Orvieto, Thomas Hofmann
- **🏷️ 机构**: ETH Z&#x00FC;rich,Z&#x00FC;rich,Switzerland
- **会议**: CVPR 2023

### Adaptive Plasticity Improvement for Continual Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00755) · 📚 被引 17
- **作者**: Yan-Shuo Liang, Wu-Jun Li
- **🏷️ 机构**: Nanjing University,National Key Laboratory for Novel Software Technology,Department of Computer Science and Technology,P. R. China
- **会议**: CVPR 2023

### PCR: Proxy-Based Contrastive Replay for Online Class-Incremental Continual Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02322) · 📚 被引 74
- **作者**: Huiwei Lin, Baoquan Zhang, Shanshan Feng, Xutao Li, Yunming Ye
- **🏷️ 机构**: Harbin Institute of Technology,Shenzhen
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
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00360) · 📚 被引 33
- **作者**: Ameya Prabhu, Hasan Abed Al Kader Hammoud, Puneet K. Dokania, Philip H. S. Torr, Ser-Nam Lim, Bernard Ghanem et al.
- **🏷️ 机构**: University of Oxford, King Abdullah University of Science and Technology (KAUST), Meta AI
- **会议**: CVPR 2023

### PIVOT: Prompting for Video Continual Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02319) · 📚 被引 44
- **作者**: Andrés Villa, Juan León Alcázar, Motasem Alfarra, Kumail Alhamoud, Julio Hurtado, Fabian Caba Heilbron et al.
- **🏷️ 机构**: Pontificia Universidad Cat&#x00F3;lica de Chile, King Abdullah University of Science and Technology (KAUST), University of Pisa
- **会议**: CVPR 2023

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

### Incrementer: Transformer for Class-Incremental Semantic Segmentation with Knowledge Distillation Focusing on Old Class.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00697) · 📚 被引 40
- **作者**: Chao Shang, Hongliang Li, Fanman Meng, Qingbo Wu, Heqian Qiu, Lanxiao Wang
- **🏷️ 机构**: University of Electronic Science and Technology of China
- **会议**: CVPR 2023

### Few-Shot Class-Incremental Learning via Class-Aware Bilateral Distillation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01139) · 📚 被引 110
- **作者**: Linglan Zhao, Jing Lu, Yunlu Xu, Zhanzhan Cheng, Dashan Guo, Yi Niu et al.
- **🏷️ 机构**: Shanghai Jiao Tong University,Department of Electronic Engineering, Hikvision Research Institute
- **会议**: CVPR 2023
