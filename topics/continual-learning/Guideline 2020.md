# Continual Learning — 2020 Guideline

> 领域: 持续学习 / 增量学习（含 VLM/多模态场景）
> 论文数: 12 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Look-ahead Meta Learning for Continual Learning.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/85b9a5ac91cd629bd3afe396ec07270a-Abstract.html)
- **作者**: Gunshi Gupta, Karmesh Yadav, Liam Paull
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### Coresets via Bilevel Optimization for Continual Learning and Streaming.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/aa2a77371374094fe9e0bc1de3f94ed9-Abstract.html)
- **作者**: Zalán Borsos, Mojmir Mutny, Andreas Krause
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### Dark Experience for General Continual Learning: a Strong, Simple Baseline.
- **链接**: [arXiv:2004.07211](https://arxiv.org/abs/2004.07211)
- **作者**: Pietro Buzzega, Matteo Boschini, Angelo Porrello, Davide Abati, Simone Calderara
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual Learning has inspired a plethora of approaches and evaluation settings; however, the majority of them overlooks the properties of a practical scenario, where the data stream cannot be shaped as a sequence of tasks and offline training is not viable. We work towards General Continual Learning (GCL), where task boundaries blur and the domain and class distributions shift either gradually or suddenly. We address it through mixing rehearsal with knowledge distillation and regularization; our simple baseline, Dark Experience Replay, matches the network's logits sampled throughout the optimization trajectory, thus promoting consistency with its past. By conducting an extensive analysis on both standard benchmarks and a novel GCL evaluation setting (MNIST-360), we show that such a seemingly simple baseline outperforms consolidated approaches and leverages limited resources. We further explore the generalization capabilities of our objective, showing its regularization being beneficial beyond mere performance.

</details>

### Online Fast Adaptation and Knowledge Accumulation (OSAKA): a New Approach to Continual Learning.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/c0a271bc0ecb776a094786474322cb82-Abstract.html)
- **作者**: Massimo Caccia, Pau Rodríguez, Oleksiy Ostapenko, Fabrice Normandin, Min Lin, Lucas Page-Caccia et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### Continual Learning in Low-rank Orthogonal Subspaces.
- **链接**: [arXiv:2010.11635](https://arxiv.org/abs/2010.11635)
- **作者**: Arslan Chaudhry, Naeemullah Khan, Puneet K. Dokania, Philip H. S. Torr
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In continual learning (CL), a learner is faced with a sequence of tasks, arriving one after the other, and the goal is to remember all the tasks once the continual learning experience is finished. The prior art in CL uses episodic memory, parameter regularization or extensible network structures to reduce interference among tasks, but in the end, all the approaches learn different tasks in a joint vector space. We believe this invariably leads to interference among different tasks. We propose to learn tasks in different (low-rank) vector subspaces that are kept orthogonal to each other in order to minimize interference. Further, to keep the gradients of different tasks coming from these subspaces orthogonal to each other, we learn isometric mappings by posing network training as an optimization problem over the Stiefel manifold. To the best of our understanding, we report, for the first time, strong results over experience-replay baseline with and without memory on standard classification benchmarks in continual learning. The code is made publicly available.

</details>

### Mitigating Forgetting in Online Continual Learning via Instance-Aware Parameterization.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/ca4b5656b7e193e6bb9064c672ac8dce-Abstract.html)
- **作者**: Hung-Jen Chen, An-Chieh Cheng, Da-Cheng Juan, Wei Wei, Min Sun
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### Organizing recurrent network dynamics by task-computation to enable continual learning.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/a576eafbce762079f7d1f77fca1c5cc2-Abstract.html)
- **作者**: Lea Duncker, Laura Driscoll, Krishna V. Shenoy, Maneesh Sahani, David Sussillo
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### Meta-Consolidation for Continual Learning.
- **链接**: [arXiv:2010.00352](https://arxiv.org/abs/2010.00352)
- **作者**: K. J. Joseph, Vineeth Nallure Balasubramanian
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The ability to continuously learn and adapt itself to new tasks, without losing grasp of already acquired knowledge is a hallmark of biological learning systems, which current deep learning systems fall short of. In this work, we present a novel methodology for continual learning called MERLIN: Meta-Consolidation for Continual Learning. We assume that weights of a neural network $\boldsymbol ψ$, for solving task $\boldsymbol t$, come from a meta-distribution $p(\boldsymbol{ψ|t})$. This meta-distribution is learned and consolidated incrementally. We operate in the challenging online continual learning setting, where a data point is seen by the model only once. Our experiments with continual learning benchmarks of MNIST, CIFAR-10, CIFAR-100 and Mini-ImageNet datasets show consistent improvement over five baselines, including a recent state-of-the-art, corroborating the promise of MERLIN.

</details>

### Continual Learning with Node-Importance based Adaptive Group Sparse Regularization.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/258be18e31c8188555c2ff05b4d542c3-Abstract.html)
- **作者**: Sangwon Jung, Hongjoon Ahn, Sungmin Cha, Taesup Moon
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### Continual Learning of a Mixed Sequence of Similar and Dissimilar Tasks.
- **链接**: [arXiv:2112.10017](https://arxiv.org/abs/2112.10017)
- **作者**: Zixuan Ke, Bing Liu, Xingchang Huang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing research on continual learning of a sequence of tasks focused on dealing with catastrophic forgetting, where the tasks are assumed to be dissimilar and have little shared knowledge. Some work has also been done to transfer previously learned knowledge to the new task when the tasks are similar and have shared knowledge. To the best of our knowledge, no technique has been proposed to learn a sequence of mixed similar and dissimilar tasks that can deal with forgetting and also transfer knowledge forward and backward. This paper proposes such a technique to learn both types of tasks in the same network. For dissimilar tasks, the algorithm focuses on dealing with forgetting, and for similar tasks, the algorithm focuses on selectively transferring the knowledge learned from some similar previous tasks to improve the new task learning. Additionally, the algorithm automatically detects whether a new task is similar to any previous tasks. Empirical evaluation using sequences of mixed tasks demonstrates the effectiveness of the proposed model.

</details>

### Understanding the Role of Training Regimes in Continual Learning.
- **链接**: [arXiv:2006.06958](https://arxiv.org/abs/2006.06958)
- **作者**: Seyed-Iman Mirzadeh, Mehrdad Farajtabar, Razvan Pascanu, Hassan Ghasemzadeh
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Catastrophic forgetting affects the training of neural networks, limiting their ability to learn multiple tasks sequentially. From the perspective of the well established plasticity-stability dilemma, neural networks tend to be overly plastic, lacking the stability necessary to prevent the forgetting of previous knowledge, which means that as learning progresses, networks tend to forget previously seen tasks. This phenomenon coined in the continual learning literature, has attracted much attention lately, and several families of approaches have been proposed with different degrees of success. However, there has been limited prior work extensively analyzing the impact that different training regimes -- learning rate, batch size, regularization method-- can have on forgetting. In this work, we depart from the typical approach of altering the learning algorithm to improve stability. Instead, we hypothesize that the geometrical properties of the local minima found for each task play an important role in the overall degree of forgetting. In particular, we study the effect of dropout, learning rate decay, and batch size, on forming training regimes that widen the tasks' local minima and consequently, on helping it not to forget catastrophically. Our study provides practical insights to improve stability via simple yet effective techniques that outperform alternative baselines.

</details>

### Continual Learning of Control Primitives : Skill Discovery via Reset-Games.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/3472ab80b6dff70c54758fd6dfc800c2-Abstract.html)
- **作者**: Kelvin Xu, Siddharth Verma, Chelsea Finn, Sergey Levine
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020
