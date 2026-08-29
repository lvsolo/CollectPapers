# Continual Learning — 2024 Guideline

> 领域: 持续学习 / 增量学习（含 VLM/多模态场景）
> 论文数: 16 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Provable Contrastive Continual Learning.
- **链接**: [arXiv:2405.18756](https://arxiv.org/abs/2405.18756)
- **作者**: Yichen Wen, Zhiquan Tan, Kaipeng Zheng, Chuanlong Xie, Weiran Huang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning requires learning incremental tasks with dynamic data distributions. So far, it has been observed that employing a combination of contrastive loss and distillation loss for training in continual learning yields strong performance. To the best of our knowledge, however, this contrastive continual learning framework lacks convincing theoretical explanations. In this work, we fill this gap by establishing theoretical performance guarantees, which reveal how the performance of the model is bounded by training losses of previous tasks in the contrastive continual learning framework. Our theoretical explanations further support the idea that pre-training can benefit continual learning. Inspired by our theoretical analysis of these guarantees, we propose a novel contrastive continual learning algorithm called CILA, which uses adaptive distillation coefficients for different tasks. These distillation coefficients are easily computed by the ratio between average distillation losses and average contrastive losses from previous tasks. Our method shows great improvement on standard benchmarks and achieves new state-of-the-art performance.

</details>

### Understanding Forgetting in Continual Learning with Linear Regression.
- **链接**: [arXiv:2405.17583](https://arxiv.org/abs/2405.17583)
- **作者**: Meng Ding, Kaiyi Ji, Di Wang, Jinhui Xu
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning, focused on sequentially learning multiple tasks, has gained significant attention recently. Despite the tremendous progress made in the past, the theoretical understanding, especially factors contributing to catastrophic forgetting, remains relatively unexplored. In this paper, we provide a general theoretical analysis of forgetting in the linear regression model via Stochastic Gradient Descent (SGD) applicable to both underparameterized and overparameterized regimes. Our theoretical framework reveals some interesting insights into the intricate relationship between task sequence and algorithmic parameters, an aspect not fully captured in previous studies due to their restrictive assumptions. Specifically, we demonstrate that, given a sufficiently large data size, the arrangement of tasks in a sequence, where tasks with larger eigenvalues in their population data covariance matrices are trained later, tends to result in increased forgetting. Additionally, our findings highlight that an appropriate choice of step size will help mitigate forgetting in both underparameterized and overparameterized settings. To validate our theoretical analysis, we conducted simulation experiments on both linear regression models and Deep Neural Networks (DNNs). Results from these simulations substantiate our theoretical findings.

</details>

### On the Diminishing Returns of Width for Continual Learning.
- **链接**: [arXiv:2403.06398](https://arxiv.org/abs/2403.06398)
- **作者**: Etash Kumar Guha, Vihan Lakshman
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While deep neural networks have demonstrated groundbreaking performance in various settings, these models often suffer from \emph{catastrophic forgetting} when trained on new tasks in sequence. Several works have empirically demonstrated that increasing the width of a neural network leads to a decrease in catastrophic forgetting but have yet to characterize the exact relationship between width and continual learning. We design one of the first frameworks to analyze Continual Learning Theory and prove that width is directly related to forgetting in Feed-Forward Networks (FFN). Specifically, we demonstrate that increasing network widths to reduce forgetting yields diminishing returns. We empirically verify our claims at widths hitherto unexplored in prior studies where the diminishing returns are clearly observed as predicted by our theory.

</details>

### Task-aware Orthogonal Sparse Network for Exploring Shared Knowledge in Continual Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v235/hu24b.html)
- **作者**: Yusong Hu, De Cheng, Dingwen Zhang, Nannan Wang, Tongliang Liu, Xinbo Gao
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### One Size Fits All for Semantic Shifts: Adaptive Prompt Tuning for Continual Learning.
- **链接**: [arXiv:2311.12048](https://arxiv.org/abs/2311.12048)
- **作者**: Doyoung Kim, Susik Yoon, Dongmin Park, Youngjun Lee, Hwanjun Song, Jihwan Bang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In real-world continual learning (CL) scenarios, tasks often exhibit intricate and unpredictable semantic shifts, posing challenges for fixed prompt management strategies which are tailored to only handle semantic shifts of uniform degree (i.e., uniformly mild or uniformly abrupt). To address this limitation, we propose an adaptive prompting approach that effectively accommodates semantic shifts of varying degree where mild and abrupt shifts are mixed. AdaPromptCL employs the assign-and-refine semantic grouping mechanism that dynamically manages prompt groups in accordance with the semantic similarity between tasks, enhancing the quality of grouping through continuous refinement. Our experiment results demonstrate that AdaPromptCL outperforms existing prompting methods by up to 21.3%, especially in the benchmark datasets with diverse semantic shifts between tasks.

</details>

### An Effective Dynamic Gradient Calibration Method for Continual Learning.
- **链接**: [arXiv:2407.20956](https://arxiv.org/abs/2407.20956)
- **作者**: Weichen Lin, Jiaxiang Chen, Ruomin Huang, Hu Ding
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning (CL) is a fundamental topic in machine learning, where the goal is to train a model with continuously incoming data and tasks. Due to the memory limit, we cannot store all the historical data, and therefore confront the ``catastrophic forgetting'' problem, i.e., the performance on the previous tasks can substantially decrease because of the missing information in the latter period. Though a number of elegant methods have been proposed, the catastrophic forgetting phenomenon still cannot be well avoided in practice. In this paper, we study the problem from the gradient perspective, where our aim is to develop an effective algorithm to calibrate the gradient in each updating step of the model; namely, our goal is to guide the model to be updated in the right direction under the situation that a large amount of historical data are unavailable. Our idea is partly inspired by the seminal stochastic variance reduction methods (e.g., SVRG and SAGA) for reducing the variance of gradient estimation in stochastic gradient descent algorithms. Another benefit is that our approach can be used as a general tool, which is able to be incorporated with several existing popular CL methods to achieve better performance. We also conduct a set of experiments on several benchmark datasets to evaluate the performance in practice.

</details>

### Rethinking Momentum Knowledge Distillation in Online Continual Learning.
- **链接**: [arXiv:2309.02870](https://arxiv.org/abs/2309.02870) · [代码](https://github.com/Nicolas1203/mkd_ocl)
- **作者**: Nicolas Michel, Maorong Wang, Ling Xiao, Toshihiko Yamasaki
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Online Continual Learning (OCL) addresses the problem of training neural networks on a continuous data stream where multiple classification tasks emerge in sequence. In contrast to offline Continual Learning, data can be seen only once in OCL, which is a very severe constraint. In this context, replay-based strategies have achieved impressive results and most state-of-the-art approaches heavily depend on them. While Knowledge Distillation (KD) has been extensively used in offline Continual Learning, it remains under-exploited in OCL, despite its high potential. In this paper, we analyze the challenges in applying KD to OCL and give empirical justifications. We introduce a direct yet effective methodology for applying Momentum Knowledge Distillation (MKD) to many flagship OCL methods and demonstrate its capabilities to enhance existing approaches. In addition to improving existing state-of-the-art accuracy by more than $10\%$ points on ImageNet100, we shed light on MKD internal mechanics and impacts during training in OCL. We argue that similar to replay, MKD should be considered a central component of OCL. The code is available at \url{https://github.com/Nicolas1203/mkd_ocl}.

</details>

### Federated Continual Learning via Prompt-based Dual Knowledge Transfer.
- **链接**: [出版页](https://proceedings.mlr.press/v235/piao24a.html)
- **作者**: Hongming Piao, Yichen Wu, Dapeng Wu, Ying Wei
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### Bayesian Adaptation of Network Depth and Width for Continual Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v235/thapa24b.html)
- **作者**: Jeevan Thapa, Rui Li
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### Mitigating Catastrophic Forgetting in Online Continual Learning by Modeling Previous Task Interrelations via Pareto Optimization.
- **链接**: [出版页](https://proceedings.mlr.press/v235/wu24ab.html)
- **作者**: Yichen Wu, Hong Wang, Peilin Zhao, Yefeng Zheng, Ying Wei, Long-Kai Huang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### Layerwise Proximal Replay: A Proximal Point Method for Online Continual Learning.
- **链接**: [arXiv:2402.09542](https://arxiv.org/abs/2402.09542)
- **作者**: Jinsoo Yoo, Yunpeng Liu, Frank Wood, Geoff Pleiss
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In online continual learning, a neural network incrementally learns from a non-i.i.d. data stream. Nearly all online continual learning methods employ experience replay to simultaneously prevent catastrophic forgetting and underfitting on past data. Our work demonstrates a limitation of this approach: neural networks trained with experience replay tend to have unstable optimization trajectories, impeding their overall accuracy. Surprisingly, these instabilities persist even when the replay buffer stores all previous training examples, suggesting that this issue is orthogonal to catastrophic forgetting. We minimize these instabilities through a simple modification of the optimization geometry. Our solution, Layerwise Proximal Replay (LPR), balances learning from new and replay data while only allowing for gradual changes in the hidden activation of past data. We demonstrate that LPR consistently improves replay-based online continual learning methods across multiple problem settings, regardless of the amount of available replay memory.

</details>

### A Statistical Theory of Regularization-Based Continual Learning.
- **链接**: [arXiv:2406.06213](https://arxiv.org/abs/2406.06213)
- **作者**: Xuyang Zhao, Huiyuan Wang, Weiran Huang, Wei Lin
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We provide a statistical analysis of regularization-based continual learning on a sequence of linear regression tasks, with emphasis on how different regularization terms affect the model performance. We first derive the convergence rate for the oracle estimator obtained as if all data were available simultaneously. Next, we consider a family of generalized $\ell_2$-regularization algorithms indexed by matrix-valued hyperparameters, which includes the minimum norm estimator and continual ridge regression as special cases. As more tasks are introduced, we derive an iterative update formula for the estimation error of generalized $\ell_2$-regularized estimators, from which we determine the hyperparameters resulting in the optimal algorithm. Interestingly, the choice of hyperparameters can effectively balance the trade-off between forward and backward knowledge transfer and adjust for data heterogeneity. Moreover, the estimation error of the optimal algorithm is derived explicitly, which is of the same order as that of the oracle estimator. In contrast, our lower bounds for the minimum norm estimator and continual ridge regression show their suboptimality. A byproduct of our theoretical analysis is the equivalence between early stopping and generalized $\ell_2$-regularization in continual learning, which may be of independent interest. Finally, we conduct experiments to complement our theory.

</details>

### Harnessing Neural Unit Dynamics for Effective and Scalable Class-Incremental Learning.
- **链接**: [arXiv:2406.02428](https://arxiv.org/abs/2406.02428)
- **作者**: Depeng Li, Tianqi Wang, Junwei Chen, Wei Dai, Zhigang Zeng
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Class-incremental learning (CIL) aims to train a model to learn new classes from non-stationary data streams without forgetting old ones. In this paper, we propose a new kind of connectionist model by tailoring neural unit dynamics that adapt the behavior of neural networks for CIL. In each training session, it introduces a supervisory mechanism to guide network expansion whose growth size is compactly commensurate with the intrinsic complexity of a newly arriving task. This constructs a near-minimal network while allowing the model to expand its capacity when cannot sufficiently hold new classes. At inference time, it automatically reactivates the required neural units to retrieve knowledge and leaves the remaining inactivated to prevent interference. We name our model AutoActivator, which is effective and scalable. To gain insights into the neural unit dynamics, we theoretically analyze the model's convergence property via a universal approximation theorem on learning sequential mappings, which is under-explored in the CIL community. Experiments show that our method achieves strong CIL performance in rehearsal-free and minimal-expansion settings with different backbones.

</details>

### Gradual Divergence for Seamless Adaptation: A Novel Domain Incremental Learning Method.
- **链接**: [arXiv:2406.16231](https://arxiv.org/abs/2406.16231)
- **作者**: Kishaan Jeeveswaran, Elahe Arani, Bahram Zonooz
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Domain incremental learning (DIL) poses a significant challenge in real-world scenarios, as models need to be sequentially trained on diverse domains over time, all the while avoiding catastrophic forgetting. Mitigating representation drift, which refers to the phenomenon of learned representations undergoing changes as the model adapts to new tasks, can help alleviate catastrophic forgetting. In this study, we propose a novel DIL method named DARE, featuring a three-stage training process: Divergence, Adaptation, and REfinement. This process gradually adapts the representations associated with new tasks into the feature space spanned by samples from previous tasks, simultaneously integrating task-specific decision boundaries. Additionally, we introduce a novel strategy for buffer sampling and demonstrate the effectiveness of our proposed method, combined with this sampling strategy, in reducing representation drift within the feature encoder. This contribution effectively alleviates catastrophic forgetting across multiple DIL benchmarks. Furthermore, our approach prevents sudden representation drift at task boundaries, resulting in a well-calibrated DIL model that maintains the performance on previous tasks.

</details>

### Multi-layer Rehearsal Feature Augmentation for Class-Incremental Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v235/zheng24p.html)
- **作者**: Bowen Zheng, Da-Wei Zhou, Han-Jia Ye, De-Chuan Zhan
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### Compositional Few-Shot Class-Incremental Learning.
- **链接**: [arXiv:2405.17022](https://arxiv.org/abs/2405.17022) · [代码](https://github.com/Zoilsen/Comp-FSCIL)
- **作者**: Yixiong Zou, Shanghang Zhang, Haichen Zhou, Yuhua Li, Ruixuan Li
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Few-shot class-incremental learning (FSCIL) is proposed to continually learn from novel classes with only a few samples after the (pre-)training on base classes with sufficient data. However, this remains a challenge. In contrast, humans can easily recognize novel classes with a few samples. Cognitive science demonstrates that an important component of such human capability is compositional learning. This involves identifying visual primitives from learned knowledge and then composing new concepts using these transferred primitives, making incremental learning both effective and interpretable. To imitate human compositional learning, we propose a cognitive-inspired method for the FSCIL task. We define and build a compositional model based on set similarities, and then equip it with a primitive composition module and a primitive reuse module. In the primitive composition module, we propose to utilize the Centered Kernel Alignment (CKA) similarity to approximate the similarity between primitive sets, allowing the training and evaluation based on primitive compositions. In the primitive reuse module, we enhance primitive reusability by classifying inputs based on primitives replaced with the closest primitives from other classes. Experiments on three datasets validate our method, showing it outperforms current state-of-the-art methods with improved interpretability. Our code is available at https://github.com/Zoilsen/Comp-FSCIL.

</details>
