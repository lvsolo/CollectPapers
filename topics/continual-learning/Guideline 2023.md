# Continual Learning — 2023 Guideline

> 领域: 持续学习 / 增量学习（含 VLM/多模态场景）
> 论文数: 14 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### BiRT: Bio-inspired Replay in Vision Transformers for Continual Learning.
- **链接**: [arXiv:2305.04769](https://arxiv.org/abs/2305.04769)
- **作者**: Kishaan Jeeveswaran, Prashant Shivaram Bhat, Bahram Zonooz, Elahe Arani
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The ability of deep neural networks to continually learn and adapt to a sequence of tasks has remained challenging due to catastrophic forgetting of previously learned tasks. Humans, on the other hand, have a remarkable ability to acquire, assimilate, and transfer knowledge across tasks throughout their lifetime without catastrophic forgetting. The versatility of the brain can be attributed to the rehearsal of abstract experiences through a complementary learning system. However, representation rehearsal in vision transformers lacks diversity, resulting in overfitting and consequently, performance drops significantly compared to raw image rehearsal. Therefore, we propose BiRT, a novel representation rehearsal-based continual learning approach using vision transformers. Specifically, we introduce constructive noises at various stages of the vision transformer and enforce consistency in predictions with respect to an exponential moving average of the working model. Our method provides consistent performance gain over raw image and vanilla representation rehearsal on several challenging CL benchmarks, while being memory efficient and robust to natural and adversarial corruptions.

</details>

### DualHSIC: HSIC-Bottleneck and Alignment for Continual Learning.
- **链接**: [arXiv:2305.00380](https://arxiv.org/abs/2305.00380)
- **作者**: Zifeng Wang, Zheng Zhan, Yifan Gong, Yucai Shao, Stratis Ioannidis, Yanzhi Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Rehearsal-based approaches are a mainstay of continual learning (CL). They mitigate the catastrophic forgetting problem by maintaining a small fixed-size buffer with a subset of data from past tasks. While most rehearsal-based approaches study how to effectively exploit the knowledge from the buffered past data, little attention is paid to the inter-task relationships with the critical task-specific and task-invariant knowledge. By appropriately leveraging inter-task relationships, we propose a novel CL method named DualHSIC to boost the performance of existing rehearsal-based methods in a simple yet effective way. DualHSIC consists of two complementary components that stem from the so-called Hilbert Schmidt independence criterion (HSIC): HSIC-Bottleneck for Rehearsal (HBR) lessens the inter-task interference and HSIC Alignment (HA) promotes task-invariant knowledge sharing. Extensive experiments show that DualHSIC can be seamlessly plugged into existing rehearsal-based methods for consistent performance improvements, and also outperforms recent state-of-the-art regularization-enhanced rehearsal methods. Source code will be released.

</details>

### Prototype-Sample Relation Distillation: Towards Replay-Free Continual Learning.
- **链接**: [arXiv:2303.14771](https://arxiv.org/abs/2303.14771)
- **作者**: Nader Asadi, MohammadReza Davari, Sudhir P. Mudur, Rahaf Aljundi, Eugene Belilovsky
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In Continual learning (CL) balancing effective adaptation while combating catastrophic forgetting is a central challenge. Many of the recent best-performing methods utilize various forms of prior task data, e.g. a replay buffer, to tackle the catastrophic forgetting problem. Having access to previous task data can be restrictive in many real-world scenarios, for example when task data is sensitive or proprietary. To overcome the necessity of using previous tasks' data, in this work, we start with strong representation learning methods that have been shown to be less prone to forgetting. We propose a holistic approach to jointly learn the representation and class prototypes while maintaining the relevance of old class prototypes and their embedded similarities. Specifically, samples are mapped to an embedding space where the representations are learned using a supervised contrastive loss. Class prototypes are evolved continually in the same latent space, enabling learning and prediction at any point. To continually adapt the prototypes without keeping any prior task data, we propose a novel distillation loss that constrains class prototypes to maintain relative similarities as compared to new task data. This method yields state-of-the-art performance in the task-incremental setting, outperforming methods relying on large amounts of data, and provides strong performance in the class-incremental setting without using any stored data points.

</details>

### Continual Learning in Linear Classification on Separable Data.
- **链接**: [arXiv:2306.03534](https://arxiv.org/abs/2306.03534)
- **作者**: Itay Evron, Edward Moroshko, Gon Buzaglo, Maroun Khriesh, Badea Marjieh, Nathan Srebro et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We analyze continual learning on a sequence of separable linear classification tasks with binary labels. We show theoretically that learning with weak regularization reduces to solving a sequential max-margin problem, corresponding to a special case of the Projection Onto Convex Sets (POCS) framework. We then develop upper bounds on the forgetting and other quantities of interest under various settings with recurring tasks, including cyclic and random orderings of tasks. We discuss several practical implications to popular training practices like regularization scheduling and weighting. We point out several theoretical differences between our continual classification setting and a recently studied continual regression setting.

</details>

### DDGR: Continual Learning with Deep Diffusion-based Generative Replay.
- **链接**: [出版页](https://proceedings.mlr.press/v202/gao23e.html)
- **作者**: Rui Gao, Weiwei Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Poisoning Generative Replay in Continual Learning to Promote Forgetting.
- **链接**: [出版页](https://proceedings.mlr.press/v202/kang23c.html)
- **作者**: Siteng Kang, Zhan Shi, Xinhua Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Learnability and Algorithm for Continual Learning.
- **链接**: [arXiv:2306.12646](https://arxiv.org/abs/2306.12646)
- **作者**: Gyuhak Kim, Changnan Xiao, Tatsuya Konishi, Bing Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper studies the challenging continual learning (CL) setting of Class Incremental Learning (CIL). CIL learns a sequence of tasks consisting of disjoint sets of concepts or classes. At any time, a single model is built that can be applied to predict/classify test instances of any classes learned thus far without providing any task related information for each test instance. Although many techniques have been proposed for CIL, they are mostly empirical. It has been shown recently that a strong CIL system needs a strong within-task prediction (WP) and a strong out-of-distribution (OOD) detection for each task. However, it is still not known whether CIL is actually learnable. This paper shows that CIL is learnable. Based on the theory, a new CIL algorithm is also proposed. Experimental results demonstrate its effectiveness.

</details>

### Parameter-Level Soft-Masking for Continual Learning.
- **链接**: [arXiv:2306.14775](https://arxiv.org/abs/2306.14775)
- **作者**: Tatsuya Konishi, Mori Kurokawa, Chihiro Ono, Zixuan Ke, Gyuhak Kim, Bing Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing research on task incremental learning in continual learning has primarily focused on preventing catastrophic forgetting (CF). Although several techniques have achieved learning with no CF, they attain it by letting each task monopolize a sub-network in a shared network, which seriously limits knowledge transfer (KT) and causes over-consumption of the network capacity, i.e., as more tasks are learned, the performance deteriorates. The goal of this paper is threefold: (1) overcoming CF, (2) encouraging KT, and (3) tackling the capacity problem. A novel technique (called SPG) is proposed that soft-masks (partially blocks) parameter updating in training based on the importance of each parameter to old tasks. Each task still uses the full network, i.e., no monopoly of any part of the network by any task, which enables maximum KT and reduction in capacity usage. To our knowledge, this is the first work that soft-masks a model at the parameter-level for continual learning. Extensive experiments demonstrate the effectiveness of SPG in achieving all three objectives. More notably, it attains significant transfer of knowledge not only among similar tasks (with shared knowledge) but also among dissimilar tasks (with little shared knowledge) while mitigating CF.

</details>

### Theory on Forgetting and Generalization of Continual Learning.
- **链接**: [arXiv:2302.05836](https://arxiv.org/abs/2302.05836)
- **作者**: Sen Lin, Peizhong Ju, Yingbin Liang, Ness B. Shroff
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning (CL), which aims to learn a sequence of tasks, has attracted significant recent attention. However, most work has focused on the experimental performance of CL, and theoretical studies of CL are still limited. In particular, there is a lack of understanding on what factors are important and how they affect "catastrophic forgetting" and generalization performance. To fill this gap, our theoretical analysis, under overparameterized linear models, provides the first-known explicit form of the expected forgetting and generalization error. Further analysis of such a key result yields a number of theoretical explanations about how overparameterization, task similarity, and task ordering affect both forgetting and generalization error of CL. More interestingly, by conducting experiments on real datasets using deep neural networks (DNNs), we show that some of these insights even go beyond the linear models and can be carried over to practical setups. In particular, we use concrete examples to show that our results not only explain some interesting empirical observations in recent studies, but also motivate better practical algorithm designs of CL.

</details>

### Neuro-Symbolic Continual Learning: Knowledge, Reasoning Shortcuts and Concept Rehearsal.
- **链接**: [出版页](https://proceedings.mlr.press/v202/marconato23a.html)
- **作者**: Emanuele Marconato, Gianpaolo Bontempo, Elisa Ficarra, Simone Calderara, Andrea Passerini, Stefano Teso
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Does Continual Learning Equally Forget All Parameters?
- **链接**: [arXiv:2304.04158](https://arxiv.org/abs/2304.04158)
- **作者**: Haiyan Zhao, Tianyi Zhou, Guodong Long, Jing Jiang, Chengqi Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Distribution shift (e.g., task or domain shift) in continual learning (CL) usually results in catastrophic forgetting of neural networks. Although it can be alleviated by repeatedly replaying buffered data, the every-step replay is time-consuming. In this paper, we study which modules in neural networks are more prone to forgetting by investigating their training dynamics during CL. Our proposed metrics show that only a few modules are more task-specific and sensitively alter between tasks, while others can be shared across tasks as common knowledge. Hence, we attribute forgetting mainly to the former and find that finetuning them only on a small buffer at the end of any CL method can bring non-trivial improvement. Due to the small number of finetuned parameters, such ``Forgetting Prioritized Finetuning (FPF)'' is efficient in computation. We further propose a more efficient and simpler method that entirely removes the every-step replay and replaces them by only $k$-times of FPF periodically triggered during CL. Surprisingly, this ``$k$-FPF'' performs comparably to FPF and outperforms the SOTA CL methods but significantly reduces their computational overhead and cost. In experiments on several benchmarks of class- and domain-incremental CL, FPF consistently improves existing CL methods by a large margin, and $k$-FPF further excels in efficiency without degrading the accuracy. We also empirically studied the impact of buffer size, epochs per task, and finetuning modules on the cost and accuracy of our methods.

</details>

### Understanding Incremental Learning of Gradient Descent: A Fine-grained Analysis of Matrix Sensing.
- **链接**: [arXiv:2301.11500](https://arxiv.org/abs/2301.11500)
- **作者**: Jikai Jin, Zhiyuan Li, Kaifeng Lyu, Simon Shaolei Du, Jason D. Lee
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> It is believed that Gradient Descent (GD) induces an implicit bias towards good generalization in training machine learning models. This paper provides a fine-grained analysis of the dynamics of GD for the matrix sensing problem, whose goal is to recover a low-rank ground-truth matrix from near-isotropic linear measurements. It is shown that GD with small initialization behaves similarly to the greedy low-rank learning heuristics (Li et al., 2020) and follows an incremental learning procedure (Gissin et al., 2019): GD sequentially learns solutions with increasing ranks until it recovers the ground truth matrix. Compared to existing works which only analyze the first learning phase for rank-1 solutions, our result provides characterizations for the whole learning process. Moreover, besides the over-parameterized regime that many prior works focused on, our analysis of the incremental learning procedure also applies to the under-parameterized regime. Finally, we conduct numerical experiments to confirm our theoretical findings.

</details>

### Towards Robust Graph Incremental Learning on Evolving Graphs.
- **链接**: [arXiv:2402.12987](https://arxiv.org/abs/2402.12987)
- **作者**: Junwei Su, Difan Zou, Zijun Zhang, Chuan Wu
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Incremental learning is a machine learning approach that involves training a model on a sequence of tasks, rather than all tasks at once. This ability to learn incrementally from a stream of tasks is crucial for many real-world applications. However, incremental learning is a challenging problem on graph-structured data, as many graph-related problems involve prediction tasks for each individual node, known as Node-wise Graph Incremental Learning (NGIL). This introduces non-independent and non-identically distributed characteristics in the sample data generation process, making it difficult to maintain the performance of the model as new tasks are added. In this paper, we focus on the inductive NGIL problem, which accounts for the evolution of graph structure (structural shift) induced by emerging tasks. We provide a formal formulation and analysis of the problem, and propose a novel regularization-based technique called Structural-Shift-Risk-Mitigation (SSRM) to mitigate the impact of the structural shift on catastrophic forgetting of the inductive NGIL problem. We show that the structural shift can lead to a shift in the input distribution for the existing tasks, and further lead to an increased risk of catastrophic forgetting. Through comprehensive empirical studies with several benchmark datasets, we demonstrate that our proposed method, Structural-Shift-Risk-Mitigation (SSRM), is flexible and easy to adapt to improve the performance of state-of-the-art GNN incremental learning frameworks in the inductive setting.

</details>

### Optimizing Mode Connectivity for Class Incremental Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v202/wen23b.html)
- **作者**: Haitao Wen, Haoyang Cheng, Heqian Qiu, Lanxiao Wang, Lili Pan, Hongliang Li
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023
