# Continual Learning — 2022 Guideline

> 领域: 持续学习 / 增量学习（含 VLM/多模态场景）
> 论文数: 18 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### CLiMB: A Continual Learning Benchmark for Vision-and-Language Tasks.
- **链接**: [arXiv:2206.09059](https://arxiv.org/abs/2206.09059)
- **作者**: Tejas Srinivasan, Ting-Yun Chang, Leticia Leonor Pinto Alva, Georgios Chochlakis, Mohammad Rostami, Jesse Thomason
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Current state-of-the-art vision-and-language models are evaluated on tasks either individually or in a multi-task setting, overlooking the challenges of continually learning (CL) tasks as they arrive. Existing CL benchmarks have facilitated research on task adaptation and mitigating "catastrophic forgetting", but are limited to vision-only and language-only tasks. We present CLiMB, a benchmark to study the challenge of learning multimodal tasks in a CL setting, and to systematically evaluate how upstream continual learning can rapidly generalize to new multimodal and unimodal tasks. CLiMB includes implementations of several CL algorithms and a modified Vision-Language Transformer (ViLT) model that can be deployed on both multimodal and unimodal tasks. We find that common CL methods can help mitigate forgetting during multimodal task learning, but do not enable cross-task knowledge transfer. We envision that CLiMB will facilitate research on a new class of CL algorithms for this challenging multimodal setting.

</details>

### Task-Free Continual Learning via Online Discrepancy Distance Learning.
- **链接**: [arXiv:2210.06579](https://arxiv.org/abs/2210.06579) · 📚 被引 6
- **作者**: Fei Ye, Adrian G. Bors
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Learning from non-stationary data streams, also called Task-Free Continual Learning (TFCL) remains challenging due to the absence of explicit task information. Although recently some methods have been proposed for TFCL, they lack theoretical guarantees. Moreover, forgetting analysis during TFCL was not studied theoretically before. This paper develops a new theoretical analysis framework which provides generalization bounds based on the discrepancy distance between the visited samples and the entire information made available for training the model. This analysis gives new insights into the forgetting behaviour in classification tasks. Inspired by this theoretical model, we propose a new approach enabled by the dynamic component expansion mechanism for a mixture model, namely the Online Discrepancy Distance Learning (ODDL). ODDL estimates the discrepancy between the probabilistic representation of the current memory buffer and the already accumulated knowledge and uses it as the expansion signal to ensure a compact network architecture with optimal performance. We then propose a new sample selection approach that selectively stores the most relevant samples into the memory buffer through the discrepancy-based measure, further improving the performance. We perform several TFCL experiments with the proposed methodology, which demonstrate that the proposed approach achieves the state of the art performance.

</details>

### SparCL: Sparse Continual Learning on the Edge.
- **链接**: [arXiv:2209.09476](https://arxiv.org/abs/2209.09476) · 📚 被引 6
- **作者**: Zifeng Wang, Zheng Zhan, Yifan Gong, Geng Yuan, Wei Niu, Tong Jian et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing work in continual learning (CL) focuses on mitigating catastrophic forgetting, i.e., model performance deterioration on past tasks when learning a new task. However, the training efficiency of a CL system is under-investigated, which limits the real-world application of CL systems under resource-limited scenarios. In this work, we propose a novel framework called Sparse Continual Learning(SparCL), which is the first study that leverages sparsity to enable cost-effective continual learning on edge devices. SparCL achieves both training acceleration and accuracy preservation through the synergy of three aspects: weight sparsity, data efficiency, and gradient sparsity. Specifically, we propose task-aware dynamic masking (TDM) to learn a sparse network throughout the entire CL process, dynamic data removal (DDR) to remove less informative training data, and dynamic gradient masking (DGM) to sparsify the gradient updates. Each of them not only improves efficiency, but also further mitigates catastrophic forgetting. SparCL consistently improves the training efficiency of existing state-of-the-art (SOTA) CL methods by at most 23X less training FLOPs, and, surprisingly, further improves the SOTA accuracy by at most 1.7%. SparCL also outperforms competitive baselines obtained from adapting SOTA sparse training methods to the CL setting in both efficiency and accuracy. We also evaluate the effectiveness of SparCL on a real mobile phone, further indicating the practical potential of our method.

</details>

### On the Effectiveness of Lipschitz-Driven Rehearsal in Continual Learning.
- **链接**: [arXiv:2210.06443](https://arxiv.org/abs/2210.06443) · [代码](https://github.com/aimagelab/LiDER) · 📚 被引 6
- **作者**: Lorenzo Bonicelli, Matteo Boschini, Angelo Porrello, Concetto Spampinato, Simone Calderara
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Rehearsal approaches enjoy immense popularity with Continual Learning (CL) practitioners. These methods collect samples from previously encountered data distributions in a small memory buffer; subsequently, they repeatedly optimize on the latter to prevent catastrophic forgetting. This work draws attention to a hidden pitfall of this widespread practice: repeated optimization on a small pool of data inevitably leads to tight and unstable decision boundaries, which are a major hindrance to generalization. To address this issue, we propose Lipschitz-DrivEn Rehearsal (LiDER), a surrogate objective that induces smoothness in the backbone network by constraining its layer-wise Lipschitz constants w.r.t. replay examples. By means of extensive experiments, we show that applying LiDER delivers a stable performance gain to several state-of-the-art rehearsal CL methods across multiple datasets, both in the presence and absence of pre-training. Through additional ablative experiments, we highlight peculiar aspects of buffer overfitting in CL and better characterize the effect produced by LiDER. Code is available at https://github.com/aimagelab/LiDER

</details>

### Memory Efficient Continual Learning with Transformers.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/4522de4178bddb36b49aa26efad537cf-Abstract-Conference.html) · 📚 被引 2
- **作者**: Beyza Ermis, Giovanni Zappella, Martin Wistuba, Aditya Rawal, Cédric Archambeau
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### A Theoretical Study on Solving Continual Learning.
- **链接**: [arXiv:2211.02633](https://arxiv.org/abs/2211.02633) · 📚 被引 8
- **作者**: Gyuhak Kim, Changnan Xiao, Tatsuya Konishi, Zixuan Ke, Bing Liu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning (CL) learns a sequence of tasks incrementally. There are two popular CL settings, class incremental learning (CIL) and task incremental learning (TIL). A major challenge of CL is catastrophic forgetting (CF). While a number of techniques are already available to effectively overcome CF for TIL, CIL remains to be highly challenging. So far, little theoretical study has been done to provide a principled guidance on how to solve the CIL problem. This paper performs such a study. It first shows that probabilistically, the CIL problem can be decomposed into two sub-problems: Within-task Prediction (WP) and Task-id Prediction (TP). It further proves that TP is correlated with out-of-distribution (OOD) detection, which connects CIL and OOD detection. The key conclusion of this study is that regardless of whether WP and TP or OOD detection are defined explicitly or implicitly by a CIL algorithm, good WP and good TP or OOD detection are necessary and sufficient for good CIL performances. Additionally, TIL is simply WP. Based on the theoretical result, new CIL methods are also designed, which outperform strong baselines in both CIL and TIL settings by a large margin.

</details>

### Retrospective Adversarial Replay for Continual Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/b6ffbbacbe2e56f2ec9a0da907382b4a-Abstract-Conference.html) · 📚 被引 5
- **作者**: Lilly Kumari, Shengjie Wang, Tianyi Zhou, Jeff A. Bilmes
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Continual Learning with Evolving Class Ontologies.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/3255a7554605a88800f4e120b3a929e1-Abstract-Conference.html) · 📚 被引 2
- **作者**: Zhiqiu Lin, Deepak Pathak, Yu-Xiong Wang, Deva Ramanan, Shu Kong
- **🏷️ 机构**: CMU
- **会议**: NeurIPS 2022

### Beyond Not-Forgetting: Continual Learning with Backward Knowledge Transfer.
- **链接**: [arXiv:2211.00789](https://arxiv.org/abs/2211.00789) · 📚 被引 4
- **作者**: Sen Lin, Li Yang, Deliang Fan, Junshan Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> By learning a sequence of tasks continually, an agent in continual learning (CL) can improve the learning performance of both a new task and `old' tasks by leveraging the forward knowledge transfer and the backward knowledge transfer, respectively. However, most existing CL methods focus on addressing catastrophic forgetting in neural networks by minimizing the modification of the learnt model for old tasks. This inevitably limits the backward knowledge transfer from the new task to the old tasks, because judicious model updates could possibly improve the learning performance of the old tasks as well. To tackle this problem, we first theoretically analyze the conditions under which updating the learnt model of old tasks could be beneficial for CL and also lead to backward knowledge transfer, based on the gradient projection onto the input subspaces of old tasks. Building on the theoretical analysis, we next develop a ContinUal learning method with Backward knowlEdge tRansfer (CUBER), for a fixed capacity neural network without data replay. In particular, CUBER first characterizes the task correlation to identify the positively correlated old tasks in a layer-wise manner, and then selectively modifies the learnt model of the old tasks when learning the new task. Experimental studies show that CUBER can even achieve positive backward knowledge transfer on several existing CL benchmarks for the first time without data replay, where the related baselines still suffer from catastrophic forgetting (negative backward knowledge transfer). The superior performance of CUBER on the backward knowledge transfer also leads to higher accuracy accordingly.

</details>

### Navigating Memory Construction by Global Pseudo-Task Simulation for Continual Learning.
- **链接**: [arXiv:2210.08442](https://arxiv.org/abs/2210.08442) · 📚 被引 0
- **作者**: Yejia Liu, Wang Zhu, Shaolei Ren
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning faces a crucial challenge of catastrophic forgetting. To address this challenge, experience replay (ER) that maintains a tiny subset of samples from previous tasks has been commonly used. Existing ER works usually focus on refining the learning objective for each task with a static memory construction policy. In this paper, we formulate the dynamic memory construction in ER as a combinatorial optimization problem, which aims at directly minimizing the global loss across all experienced tasks. We first apply three tactics to solve the problem in the offline setting as a starting point. To provide an approximate solution to this problem in the online continual learning setting, we further propose the Global Pseudo-task Simulation (GPS), which mimics future catastrophic forgetting of the current task by permutation. Our empirical results and analyses suggest that the GPS consistently improves accuracy across four commonly used vision benchmarks. We have also shown that our GPS can serve as the unified framework for integrating various memory construction policies in existing ER works.

</details>

### Continual learning: a feature extraction formalization, an efficient algorithm, and fundamental obstructions.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/b63a24a1832bd14fa945c71f535c0095-Abstract-Conference.html) · 📚 被引 0
- **作者**: Binghui Peng, Andrej Risteski
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Continual Learning In Environments With Polynomial Mixing Times.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/89c61fce5a8b73871d1c4073f486b134-Abstract-Conference.html) · 📚 被引 0
- **作者**: Matthew Riemer, Sharath Chandra Raparthy, Ignacio Cases, Gopeshh Subbaraj, Maximilian Puelma Touzel, Irina Rish
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Exploring Example Influence in Continual Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/ad2fa437f7c23e4e9875599c6065d18a-Abstract-Conference.html) · 📚 被引 4
- **作者**: Qing Sun, Fan Lyu, Fanhua Shang, Wei Feng, Liang Wan
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### A simple but strong baseline for online continual learning: Repeated Augmented Rehearsal.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/5ebbbac62b968254093023f1c95015d3-Abstract-Conference.html) · 📚 被引 5
- **作者**: Yaqian Zhang, Bernhard Pfahringer, Eibe Frank, Albert Bifet, Nick Jin Sean Lim, Yunzhe Jia
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Learning a Condensed Frame for Memory-Efficient Video Class-Incremental Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/c8ac22c0d4b263618f2a4f4657948912-Abstract-Conference.html) · 📚 被引 1
- **作者**: Yixuan Pei, Zhiwu Qing, Jun Cen, Xiang Wang, Shiwei Zhang, Yaxiong Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### S-Prompts Learning with Pre-trained Transformers: An Occam's Razor for Domain Incremental Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/25886d7a7cf4e33fd44072a0cd81bf30-Abstract-Conference.html) · 📚 被引 34
- **作者**: Yabin Wang, Zhiwu Huang, Xiaopeng Hong
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### ACIL: Analytic Class-Incremental Learning with Absolute Memorization and Privacy Protection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/4b74a42fc81fc7ee252f6bcb6e26c8be-Abstract-Conference.html) · 📚 被引 12
- **作者**: Huiping Zhuang, Zhenyu Weng, Hongxin Wei, Renchunzi Xie, Kar-Ann Toh, Zhiping Lin
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Margin-Based Few-Shot Class-Incremental Learning with Class-Level Overfitting Mitigation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/ae817e85f71ef86d5c9566598e185b89-Abstract-Conference.html) · 📚 被引 4
- **作者**: Yixiong Zou, Shanghang Zhang, Yuhua Li, Ruixuan Li
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022
