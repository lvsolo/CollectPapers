# Continual Learning — 2021 Guideline

> 领域: 持续学习 / 增量学习（含 VLM/多模态场景）
> 论文数: 14 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Wanderlust: Online Continual Object Detection in the Real World.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01065) · 📚 75 citations
- **作者**: Jianren Wang, Xin Wang, Yue Shang-Guan, Abhinav Gupta
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### Class-Incremental Learning for Action Recognition in Videos.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01344) · 📚 70 citations
- **作者**: Jaeyoo Park, Minsoo Kang, Bohyung Han
- **🏷️ 机构**: Seoul National University
- **会议**: ICCV 2021

### Online Continual Learning with Natural Distribution Shifts: An Empirical Study with Visual Data.
- **链接**: [arXiv:2108.09020](https://arxiv.org/abs/2108.09020) · [出版页](https://doi.org/10.1109/ICCV48922.2021.00817) · [代码](https://github.com/IntelLabs/continuallearning) · 📚 105 citations
- **作者**: Zhipeng Cai, Ozan Sener, Vladlen Koltun
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

- **摘要（英，原文）**:

  > Continual learning is the problem of learning and retaining knowledge through time over multiple tasks and environments. Research has primarily focused on the incremental classification setting, where new tasks/classes are added at discrete time intervals. Such an "offline" setting does not evaluate the ability of agents to learn effectively and efficiently, since an agent can perform multiple learning epochs without any time limitation when a task is added. We argue that "online" continual learning, where data is a single continuous stream without task boundaries, enables evaluating both information retention and online learning efficacy. In online continual learning, each incoming small batch of data is first used for testing and then added to the training set, making the problem truly online. Trained models are later evaluated on historical data to assess information retention. We introduce a new benchmark for online continual visual learning that exhibits large scale and natural distribution shifts. Through a large-scale analysis, we identify critical and previously unobserved phenomena of gradient-based optimization in continual learning, and propose effective strategies for improving gradient-based online continual learning with real data. The source code and dataset are available in: https://github.com/IntelLabs/continuallearning.

### Co2L: Contrastive Continual Learning.
- **链接**: [arXiv:2106.14413](https://arxiv.org/abs/2106.14413) · [出版页](https://doi.org/10.1109/ICCV48922.2021.00938) · 📚 412 citations
- **作者**: Hyuntak Cha, Jaeho Lee, Jinwoo Shin
- **🏷️ 机构**: POSTECH
- **会议**: ICCV 2021

- **摘要（英，原文）**:

  > Recent breakthroughs in self-supervised learning show that such algorithms learn visual representations that can be transferred better to unseen tasks than joint-training methods relying on task-specific supervision. In this paper, we found that the similar holds in the continual learning con-text: contrastively learned representations are more robust against the catastrophic forgetting than jointly trained representations. Based on this novel observation, we propose a rehearsal-based continual learning algorithm that focuses on continually learning and maintaining transferable representations. More specifically, the proposed scheme (1) learns representations using the contrastive learning objective, and (2) preserves learned representations using a self-supervised distillation step. We conduct extensive experimental validations under popular benchmark image classification datasets, where our method sets the new state-of-the-art performance.

### Continual Learning on Noisy Data Streams via Self-Purified Replay.
- **链接**: [arXiv:2110.07735](https://arxiv.org/abs/2110.07735) · [出版页](https://doi.org/10.1109/ICCV48922.2021.00058) · 📚 59 citations
- **作者**: Chris Dongjoo Kim, Jinseo Jeong, Sangwoo Moon, Gunhee Kim
- **🏷️ 机构**: Seoul National University
- **会议**: ICCV 2021

- **摘要（英，原文）**:

  > Continually learning in the real world must overcome many challenges, among which noisy labels are a common and inevitable issue. In this work, we present a repla-ybased continual learning framework that simultaneously addresses both catastrophic forgetting and noisy labels for the first time. Our solution is based on two observations; (i) forgetting can be mitigated even with noisy labels via self-supervised learning, and (ii) the purity of the replay buffer is crucial. Building on this regard, we propose two key components of our method: (i) a self-supervised replay technique named Self-Replay which can circumvent erroneous training signals arising from noisy labeled data, and (ii) the Self-Centered filter that maintains a purified replay buffer via centrality-based stochastic graph ensembles. The empirical results on MNIST, CIFAR-10, CIFAR-100, and WebVision with real-world noise demonstrate that our framework can maintain a highly pure replay buffer amidst noisy streamed data while greatly outperforming the combinations of the state-of-the-art continual learning and noisy label learning methods. The source code is available at http://vision.snu.ac.kr/projects/SPR

### Few-Shot and Continual Learning with Attentive Independent Mechanisms.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00932) · 📚 34 citations
- **作者**: Eugene Lee, Cheng-Han Huang, Chen-Yi Lee
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### RECALL: Replay-based Continual Learning in Semantic Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00694) · 📚 159 citations
- **作者**: Andrea Maracani, Umberto Michieli, Marco Toldo, Pietro Zanuttigh
- **🏷️ 机构**: UniGE, IIT
- **会议**: ICCV 2021

### Detection and Continual Learning of Novel Face Presentation Attacks.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01458) · 📚 59 citations
- **作者**: Mohammad Rostami, Leonidas Spinoulas, Mohamed E. Hussein, Joe Mathai, Wael Abd-Almageed
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### Rehearsal revealed: The limits and merits of revisiting samples in continual learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00925) · 📚 126 citations
- **作者**: Eli Verwimp, Matthias De Lange, Tinne Tuytelaars
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### Continual Learning for Image-Based Camera Localization.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00324) · 📚 32 citations
- **作者**: Shuzhe Wang, Zakaria Laskar, Iaroslav Melekhov, Xiaotian Li, Juho Kannala
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### SS-IL: Separated Softmax for Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00088) · 📚 220 citations
- **作者**: Hongjoon Ahn, Jihwan Kwak, Subin Lim, Hyeonsu Bang, Hyojun Kim, Taesup Moon
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### Synthesized Feature based Few-Shot Class-Incremental Learning on a Mixture of Subspaces.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00854) · 📚 82 citations
- **作者**: Ali Cheraghian, Shafin Rahman, Sameera Ramasinghe, Pengfei Fang, Christian Simon, Lars Petersson et al.
- **🏷️ 机构**: North South University, Bangladesh
- **会议**: ICCV 2021

### Always Be Dreaming: A New Approach for Data-Free Class-Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00924) · 📚 217 citations
- **作者**: James Seale Smith, Yen-Chang Hsu, Jonathan C. Balloch, Yilin Shen, Hongxia Jin, Zsolt Kira
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### Striking a Balance between Stability and Plasticity for Class-Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00116) · 📚 65 citations
- **作者**: Guile Wu, Shaogang Gong, Pan Li
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021
