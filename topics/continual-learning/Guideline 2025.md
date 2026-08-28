# Continual Learning — 2025 Guideline

> 领域: 持续学习 / 增量学习（含 VLM/多模态场景）
> 论文数: 29 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Learning without Isolation: Pathway Protection for Continual Learning.
- **链接**: [arXiv:2505.18568](https://arxiv.org/abs/2505.18568)
- **作者**: Zhikang Chen, Abudukelimu Wuerkaixi, Sen Cui, Haoxuan Li, Ding Li, Jingfeng Zhang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep networks are prone to catastrophic forgetting during sequential task learning, i.e., losing the knowledge about old tasks upon learning new tasks. To this end, continual learning(CL) has emerged, whose existing methods focus mostly on regulating or protecting the parameters associated with the previous tasks. However, parameter protection is often impractical, since the size of parameters for storing the old-task knowledge increases linearly with the number of tasks, otherwise it is hard to preserve the parameters related to the old-task knowledge. In this work, we bring a dual opinion from neuroscience and physics to CL: in the whole networks, the pathways matter more than the parameters when concerning the knowledge acquired from the old tasks. Following this opinion, we propose a novel CL framework, learning without isolation(LwI), where model fusion is formulated as graph matching and the pathways occupied by the old tasks are protected without being isolated. Thanks to the sparsity of activation channels in a deep network, LwI can adaptively allocate available pathways for a new task, realizing pathway protection and addressing catastrophic forgetting in a parameter-efficient manner. Experiments on popular benchmark datasets demonstrate the superiority of the proposed LwI.

</details>

### A Selective Learning Method for Temporal Graph Continual Learning.
- **链接**: [arXiv:2503.01580](https://arxiv.org/abs/2503.01580)
- **作者**: Hanmo Liu, Shimin Di, Haoyang Li, Xun Jian, Yue Wang, Lei Chen
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Node classification is a key task in temporal graph learning (TGL). Real-life temporal graphs often introduce new node classes over time, but existing TGL methods assume a fixed set of classes. This assumption brings limitations, as updating models with full data is costly, while focusing only on new classes results in forgetting old ones. Graph continual learning (GCL) methods mitigate forgetting using old-class subsets but fail to account for their evolution. We define this novel problem as temporal graph continual learning (TGCL), which focuses on efficiently maintaining up-to-date knowledge of old classes. To tackle TGCL, we propose a selective learning framework that substitutes the old-class data with its subsets, Learning Towards the Future (LTF). We derive an upper bound on the error caused by such replacement and transform it into objectives for selecting and learning subsets that minimize classification error while preserving the distribution of the full old-class data. Experiments on three real-world datasets validate the effectiveness of LTF on TGCL.

</details>

### Understanding the Forgetting of (Replay-based) Continual Learning via Feature Learning: Angle Matters.
- **链接**: [出版页](https://proceedings.mlr.press/v267/wan25d.html)
- **作者**: Hongyi Wang, Shiyuan Ren, Wei Huang, Miao Zhang, Xiang Deng, Yixin Bao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### TreeLoRA: Efficient Continual Learning via Layer-Wise LoRAs Guided by a Hierarchical Gradient-Similarity Tree.
- **链接**: [出版页](https://proceedings.mlr.press/v267/qian25b.html)
- **作者**: Yu-Yang Qian, Yuan-Ze Xu, Zhen-Yu Zhang, Peng Zhao, Zhi-Hua Zhou
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Model Uncertainty Quantification by Conformal Prediction in Continual Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v267/gao25i.html)
- **作者**: Rui Gao, Weiwei Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Exploiting Presentative Feature Distributions for Parameter-Efficient Continual Learning of Large Language Models.
- **链接**: [出版页](https://proceedings.mlr.press/v267/cheng25j.html)
- **作者**: Xin Cheng, Jiabo Ye, Haiyang Xu, Ming Yan, Ji Zhang, Feng Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Unlocking the Power of Rehearsal in Continual Learning: A Theoretical Perspective.
- **链接**: [arXiv:2506.00205](https://arxiv.org/abs/2506.00205)
- **作者**: Junze Deng, Qinhang Wu, Peizhong Ju, Sen Lin, Yingbin Liang, Ness B. Shroff
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Rehearsal-based methods have shown superior performance in addressing catastrophic forgetting in continual learning (CL) by storing and training on a subset of past data alongside new data in current task. While such a concurrent rehearsal strategy is widely used, it remains unclear if this approach is always optimal. Inspired by human learning, where sequentially revisiting tasks helps mitigate forgetting, we explore whether sequential rehearsal can offer greater benefits for CL compared to standard concurrent rehearsal. To address this question, we conduct a theoretical analysis of rehearsal-based CL in overparameterized linear models, comparing two strategies: 1) Concurrent Rehearsal, where past and new data are trained together, and 2) Sequential Rehearsal, where new data is trained first, followed by revisiting past data sequentially. By explicitly characterizing forgetting and generalization error, we show that sequential rehearsal performs better when tasks are less similar. These insights further motivate a novel Hybrid Rehearsal method, which trains similar tasks concurrently and revisits dissimilar tasks sequentially. We characterize its forgetting and generalization performance, and our experiments with deep neural networks further confirm that the hybrid approach outperforms standard concurrent rehearsal. This work provides the first comprehensive theoretical analysis of rehearsal-based CL.

</details>

### The Importance of Being Lazy: Scaling Limits of Continual Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v267/graldi25a.html)
- **作者**: Jacopo Graldi, Alessandro Breccia, Giulia Lanzillotta, Thomas Hofmann, Lorenzo Noci
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### From RAG to Memory: Non-Parametric Continual Learning for Large Language Models.
- **链接**: [出版页](https://proceedings.mlr.press/v267/gutierrez25a.html)
- **作者**: Bernal Jiménez Gutiérrez, Yiheng Shu, Weijian Qi, Sizhe Zhou, Yu Su
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Measuring Representational Shifts in Continual Learning: A Linear Transformation Perspective.
- **链接**: [出版页](https://proceedings.mlr.press/v267/kim25p.html)
- **作者**: Joonkyu Kim, Yejin Kim, Jy-yong Sohn
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Optimal Task Order for Continual Learning of Multiple Tasks.
- **链接**: [arXiv:2502.03350](https://arxiv.org/abs/2502.03350)
- **作者**: Ziyan Li, Naoki Hiratani
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning of multiple tasks remains a major challenge for neural networks. Here, we investigate how task order influences continual learning and propose a strategy for optimizing it. Leveraging a linear teacher-student model with latent factors, we derive an analytical expression relating task similarity and ordering to learning performance. Our analysis reveals two principles that hold under a wide parameter range: (1) tasks should be arranged from the least representative to the most typical, and (2) adjacent tasks should be dissimilar. We validate these rules on both synthetic data and real-world image classification datasets (Fashion-MNIST, CIFAR-10, CIFAR-100), demonstrating consistent performance improvements in both multilayer perceptrons and convolutional neural networks. Our work thus presents a generalizable framework for task-order optimization in task-incremental continual learning.

</details>

### BECAME: Bayesian Continual Learning with Adaptive Model Merging.
- **链接**: [arXiv:2504.02666](https://arxiv.org/abs/2504.02666)
- **作者**: Mei Li, Yuxiang Lu, Qinyan Dai, Suizhi Huang, Yue Ding, Hongtao Lu
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual Learning (CL) strives to learn incrementally across tasks while mitigating catastrophic forgetting. A key challenge in CL is balancing stability (retaining prior knowledge) and plasticity (learning new tasks). While representative gradient projection methods ensure stability, they often limit plasticity. Model merging techniques offer promising solutions, but prior methods typically rely on empirical assumptions and carefully selected hyperparameters. In this paper, we explore the potential of model merging to enhance the stability-plasticity trade-off, providing theoretical insights that underscore its benefits. Specifically, we reformulate the merging mechanism using Bayesian continual learning principles and derive a closed-form solution for the optimal merging coefficient that adapts to the diverse characteristics of tasks. To validate our approach, we introduce a two-stage framework named BECAME, which synergizes the expertise of gradient projection and adaptive merging. Extensive experiments show that our approach outperforms state-of-the-art CL methods and existing merging strategies.

</details>

### Rethinking the Stability-Plasticity Trade-off in Continual Learning from an Architectural Perspective.
- **链接**: [arXiv:2506.03951](https://arxiv.org/abs/2506.03951) · [代码](https://github.com/byyx666/Dual-Arch)
- **作者**: Aojun Lu, Hangjie Yuan, Tao Feng, Yanan Sun
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The quest for Continual Learning (CL) seeks to empower neural networks with the ability to learn and adapt incrementally. Central to this pursuit is addressing the stability-plasticity dilemma, which involves striking a balance between two conflicting objectives: preserving previously learned knowledge and acquiring new knowledge. While numerous CL methods aim to achieve this trade-off, they often overlook the impact of network architecture on stability and plasticity, restricting the trade-off to the parameter level. In this paper, we delve into the conflict between stability and plasticity at the architectural level. We reveal that under an equal parameter constraint, deeper networks exhibit better plasticity, while wider networks are characterized by superior stability. To address this architectural-level dilemma, we introduce a novel framework denoted Dual-Arch, which serves as a plug-in component for CL. This framework leverages the complementary strengths of two distinct and independent networks: one dedicated to plasticity and the other to stability. Each network is designed with a specialized and lightweight architecture, tailored to its respective objective. Extensive experiments demonstrate that Dual-Arch enhances the performance of existing CL methods while being up to 87% more compact in terms of parameters. Code: https://github.com/byyx666/Dual-Arch.

</details>

### LADA: Scalable Label-Specific CLIP Adapter for Continual Learning.
- **链接**: [arXiv:2505.23271](https://arxiv.org/abs/2505.23271) · [代码](https://github.com/MaolinLuo/LADA)
- **作者**: Mao-Lin Luo, Zi-Hao Zhou, Tong Wei, Min-Ling Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning with vision-language models like CLIP offers a pathway toward scalable machine learning systems by leveraging its transferable representations. Existing CLIP-based methods adapt the pre-trained image encoder by adding multiple sets of learnable parameters, with each task using a partial set of parameters. This requires selecting the expected parameters for input images during inference, which is prone to error that degrades performance. To address this problem, we introduce LADA (Label-specific ADApter). Instead of partitioning parameters across tasks, LADA appends lightweight, label-specific memory units to the frozen CLIP image encoder, enabling discriminative feature generation by aggregating task-agnostic knowledge. To prevent catastrophic forgetting, LADA employs feature distillation for seen classes, preventing their features from being interfered with by new classes. Positioned after the image encoder, LADA prevents gradient flow to the frozen CLIP parameters, ensuring efficient training. Extensive results show that LADA achieves state-of-the-art performance in continual learning settings. The implementation code is available at https://github.com/MaolinLuo/LADA.

</details>

### Efficient Graph Continual Learning via Lightweight Graph Neural Tangent Kernels-based Dataset Distillation.
- **链接**: [出版页](https://proceedings.mlr.press/v267/qiu25f.html)
- **作者**: Rihong Qiu, Xinke Jiang, Yuchen Fang, Hongbin Lai, Hao Miao, Xu Chu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### CAN: Leveraging Clients As Navigators for Generative Replay in Federated Continual Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v267/rong25a.html)
- **作者**: Xuankun Rong, Jianshu Zhang, Kun He, Mang Ye
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Confounder-Free Continual Learning via Recursive Feature Normalization.
- **链接**: [出版页](https://proceedings.mlr.press/v267/shah25a.html)
- **作者**: Yash Shah, Camila González, Mohammad H. Abbasi, Qingyu Zhao, Kilian M. Pohl, Ehsan Adeli
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Improving Continual Learning Performance and Efficiency with Auxiliary Classifiers.
- **链接**: [出版页](https://proceedings.mlr.press/v267/szatkowski25a.html)
- **作者**: Filip Szatkowski, Yaoyue Zheng, Fei Yang, Tomasz Trzcinski, Bartlomiej Twardowski, Joost van de Weijer
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Online Curvature-Aware Replay: Leveraging 2nd Order Information for Online Continual Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v267/urettini25a.html)
- **作者**: Edoardo Urettini, Antonio Carta
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Cut out and Replay: A Simple yet Versatile Strategy for Multi-Label Online Continual Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v267/wang25bg.html)
- **作者**: Xinrui Wang, Shao-Yuan Li, Jiaqiang Zhang, Songcan Chen
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Addressing Imbalanced Domain-Incremental Learning through Dual-Balance Collaborative Experts.
- **链接**: [出版页](https://proceedings.mlr.press/v267/li25eb.html)
- **作者**: Lan Li, Da-Wei Zhou, Han-Jia Ye, De-Chuan Zhan
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Semantic Shift Estimation via Dual-Projection and Classifier Reconstruction for Exemplar-Free Class-Incremental Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v267/he25d.html)
- **作者**: Run He, Di Fang, Yicheng Xu, Yawen Cui, Ming Li, Cen Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Geometric Feature Embedding for Effective 3D Few-Shot Class Incremental Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v267/li25ad.html)
- **作者**: Xiangqi Li, Libo Huang, Zhulin An, Weilun Feng, Chuanguang Yang, Boyu Diao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Tensor Decomposition Based Memory-Efficient Incremental Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v267/li25dy.html)
- **作者**: Yuhang Li, Guoxu Zhou, Zhenhao Huang, Xinqi Chen, Yuning Qiu, Qibin Zhao
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Autoencoder-Based Hybrid Replay for Class-Incremental Learning.
- **链接**: [arXiv:2505.05926](https://arxiv.org/abs/2505.05926)
- **作者**: Milad Khademi Nori, Il-Min Kim, Guanghui Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In class-incremental learning (CIL), effective incremental learning strategies are essential to mitigate task confusion and catastrophic forgetting, especially as the number of tasks $t$ increases. Current exemplar replay strategies impose $\mathcal{O}(t)$ memory/compute complexities. We propose an autoencoder-based hybrid replay (AHR) strategy that leverages our new hybrid autoencoder (HAE) to function as a compressor to alleviate the requirement for large memory, achieving $\mathcal{O}(0.1 t)$ at the worst case with the computing complexity of $\mathcal{O}(t)$ while accomplishing state-of-the-art performance. The decoder later recovers the exemplar data stored in the latent space, rather than in raw format. Additionally, HAE is designed for both discriminative and generative modeling, enabling classification and replay capabilities, respectively. HAE adopts the charged particle system energy minimization equations and repulsive force algorithm for the incremental embedding and distribution of new class centroids in its latent space. Our results demonstrate that AHR consistently outperforms recent baselines across multiple benchmarks while operating with the same memory/compute budgets. The source code is included in the supplementary material and will be open-sourced upon publication.

</details>

### Probabilistic Group Mask Guided Discrete Optimization for Incremental Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v267/wan25h.html)
- **作者**: Fengqiang Wan, Yang Yang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Navigating Semantic Drift in Task-Agnostic Class-Incremental Learning.
- **链接**: [arXiv:2502.07560](https://arxiv.org/abs/2502.07560) · [代码](https://github.com/fwu11/MACIL.git)
- **作者**: Fangwen Wu, Lechao Cheng, Shengeng Tang, Xiaofeng Zhu, Chaowei Fang, Dingwen Zhang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Class-incremental learning (CIL) seeks to enable a model to sequentially learn new classes while retaining knowledge of previously learned ones. Balancing flexibility and stability remains a significant challenge, particularly when the task ID is unknown. To address this, our study reveals that the gap in feature distribution between novel and existing tasks is primarily driven by differences in mean and covariance moments. Building on this insight, we propose a novel semantic drift calibration method that incorporates mean shift compensation and covariance calibration. Specifically, we calculate each class's mean by averaging its sample embeddings and estimate task shifts using weighted embedding changes based on their proximity to the previous mean, effectively capturing mean shifts for all learned classes with each new task. We also apply Mahalanobis distance constraint for covariance calibration, aligning class-specific embedding covariances between old and current networks to mitigate the covariance shift. Additionally, we integrate a feature-level self-distillation approach to enhance generalization. Comprehensive experiments on commonly used datasets demonstrate the effectiveness of our approach. The source code is available at \href{https://github.com/fwu11/MACIL.git}{https://github.com/fwu11/MACIL.git}.

</details>

### Componential Prompt-Knowledge Alignment for Domain Incremental Learning.
- **链接**: [arXiv:2505.04575](https://arxiv.org/abs/2505.04575) · [代码](https://github.com/zhoujiahuan1991/ICML2025-KA-Prompt)
- **作者**: Kunlun Xu, Xu Zou, Gang Hua, Jiahuan Zhou
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Domain Incremental Learning (DIL) aims to learn from non-stationary data streams across domains while retaining and utilizing past knowledge. Although prompt-based methods effectively store multi-domain knowledge in prompt parameters and obtain advanced performance through cross-domain prompt fusion, we reveal an intrinsic limitation: component-wise misalignment between domain-specific prompts leads to conflicting knowledge integration and degraded predictions. This arises from the random positioning of knowledge components within prompts, where irrelevant component fusion introduces interference.To address this, we propose Componential Prompt-Knowledge Alignment (KA-Prompt), a novel prompt-based DIL method that introduces component-aware prompt-knowledge alignment during training, significantly improving both the learning and inference capacity of the model. KA-Prompt operates in two phases: (1) Initial Componential Structure Configuring, where a set of old prompts containing knowledge relevant to the new domain are mined via greedy search, which is then exploited to initialize new prompts to achieve reusable knowledge transfer and establish intrinsic alignment between new and old prompts. (2) Online Alignment Preservation, which dynamically identifies the target old prompts and applies adaptive componential consistency constraints as new prompts evolve. Extensive experiments on DIL benchmarks demonstrate the effectiveness of our KA-Prompt. Our source code is available at https://github.com/zhoujiahuan1991/ICML2025-KA-Prompt

</details>

### L3A: Label-Augmented Analytic Adaptation for Multi-Label Class Incremental Learning.
- **链接**: [arXiv:2506.00816](https://arxiv.org/abs/2506.00816) · [代码](https://github.com/scut-zx/L3A)
- **作者**: Xiang Zhang, Run He, Chen Jiao, Di Fang, Ming Li, Ziqian Zeng et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Class-incremental learning (CIL) enables models to learn new classes continually without forgetting previously acquired knowledge. Multi-label CIL (MLCIL) extends CIL to a real-world scenario where each sample may belong to multiple classes, introducing several challenges: label absence, which leads to incomplete historical information due to missing labels, and class imbalance, which results in the model bias toward majority classes. To address these challenges, we propose Label-Augmented Analytic Adaptation (L3A), an exemplar-free approach without storing past samples. L3A integrates two key modules. The pseudo-label (PL) module implements label augmentation by generating pseudo-labels for current phase samples, addressing the label absence problem. The weighted analytic classifier (WAC) derives a closed-form solution for neural networks. It introduces sample-specific weights to adaptively balance the class contribution and mitigate class imbalance. Experiments on MS-COCO and PASCAL VOC datasets demonstrate that L3A outperforms existing methods in MLCIL tasks. Our code is available at https://github.com/scut-zx/L3A.

</details>
