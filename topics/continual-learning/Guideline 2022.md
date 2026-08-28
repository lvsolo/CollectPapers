# Continual Learning — 2022 Guideline

> 领域: 持续学习 / 增量学习（含 VLM/多模态场景）
> 论文数: 16 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Learning Fast, Learning Slow: A General Continual Learning Method based on Complementary Learning System.
- **链接**: [arXiv:2201.12604](https://arxiv.org/abs/2201.12604)
- **作者**: Elahe Arani, Fahad Sarfraz, Bahram Zonooz
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Humans excel at continually learning from an ever-changing environment whereas it remains a challenge for deep neural networks which exhibit catastrophic forgetting. The complementary learning system (CLS) theory suggests that the interplay between rapid instance-based learning and slow structured learning in the brain is crucial for accumulating and retaining knowledge. Here, we propose CLS-ER, a novel dual memory experience replay (ER) method which maintains short-term and long-term semantic memories that interact with the episodic memory. Our method employs an effective replay mechanism whereby new knowledge is acquired while aligning the decision boundaries with the semantic memories. CLS-ER does not utilize the task boundaries or make any assumption about the distribution of the data which makes it versatile and suited for "general continual learning". Our approach achieves state-of-the-art performance on standard benchmarks as well as more realistic general continual learning settings.

</details>

### Learning curves for continual learning in neural networks: Self-knowledge transfer and forgetting.
- **链接**: [出版页](https://openreview.net/forum?id=tFgdrQbbaa)
- **作者**: Ryo Karakida, Shotaro Akaho
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

### Continual Normalization: Rethinking Batch Normalization for Online Continual Learning.
- **链接**: [arXiv:2203.16102](https://arxiv.org/abs/2203.16102) · [代码](https://github.com/phquang/Continual-Normalization)
- **作者**: Quang Pham, Chenghao Liu, Steven C. H. Hoi
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing continual learning methods use Batch Normalization (BN) to facilitate training and improve generalization across tasks. However, the non-i.i.d and non-stationary nature of continual learning data, especially in the online setting, amplify the discrepancy between training and testing in BN and hinder the performance of older tasks. In this work, we study the cross-task normalization effect of BN in online continual learning where BN normalizes the testing data using moments biased towards the current task, resulting in higher catastrophic forgetting. This limitation motivates us to propose a simple yet effective method that we call Continual Normalization (CN) to facilitate training similar to BN while mitigating its negative effect. Extensive experiments on different continual learning algorithms and online scenarios show that CN is a direct replacement for BN and can provide substantial performance improvements. Our implementation is available at \url{https://github.com/phquang/Continual-Normalization}.

</details>

### New Insights on Reducing Abrupt Representation Change in Online Continual Learning.
- **链接**: [出版页](https://openreview.net/forum?id=N8MaByOzUfb)
- **作者**: Lucas Caccia, Rahaf Aljundi, Nader Asadi, Tinne Tuytelaars, Joelle Pineau, Eugene Belilovsky
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

### Online Continual Learning on Class Incremental Blurry Task Configuration with Anytime Inference.
- **链接**: [arXiv:2110.10031](https://arxiv.org/abs/2110.10031) · [代码](https://github.com/naver-ai/i-Blurry)
- **作者**: Hyunseo Koh, Dahyun Kim, Jung-Woo Ha, Jonghyun Choi
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite rapid advances in continual learning, a large body of research is devoted to improving performance in the existing setups. While a handful of work do propose new continual learning setups, they still lack practicality in certain aspects. For better practicality, we first propose a novel continual learning setup that is online, task-free, class-incremental, of blurry task boundaries and subject to inference queries at any moment. We additionally propose a new metric to better measure the performance of the continual learning methods subject to inference queries at any moment. To address the challenging setup and evaluation protocol, we propose an effective method that employs a new memory management scheme and novel learning techniques. Our empirical validation demonstrates that the proposed method outperforms prior arts by large margins. Code and data splits are available at https://github.com/naver-ai/i-Blurry.

</details>

### TRGP: Trust Region Gradient Projection for Continual Learning.
- **链接**: [arXiv:2202.02931](https://arxiv.org/abs/2202.02931)
- **作者**: Sen Lin, Li Yang, Deliang Fan, Junshan Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Catastrophic forgetting is one of the major challenges in continual learning. To address this issue, some existing methods put restrictive constraints on the optimization space of the new task for minimizing the interference to old tasks. However, this may lead to unsatisfactory performance for the new task, especially when the new task is strongly correlated with old tasks. To tackle this challenge, we propose Trust Region Gradient Projection (TRGP) for continual learning to facilitate the forward knowledge transfer based on an efficient characterization of task correlation. Particularly, we introduce a notion of `trust region' to select the most related old tasks for the new task in a layer-wise and single-shot manner, using the norm of gradient projection onto the subspace spanned by task inputs. Then, a scaled weight projection is proposed to cleverly reuse the frozen weights of the selected old tasks in the trust region through a layer-wise scaling matrix. By jointly optimizing the scaling matrices and the model, where the model is updated along the directions orthogonal to the subspaces of old tasks, TRGP can effectively prompt knowledge transfer without forgetting. Extensive experiments show that our approach achieves significant improvement over related state-of-the-art methods.

</details>

### Continual Learning with Recursive Gradient Optimization.
- **链接**: [arXiv:2201.12522](https://arxiv.org/abs/2201.12522)
- **作者**: Hao Liu, Huaping Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Learning multiple tasks sequentially without forgetting previous knowledge, called Continual Learning(CL), remains a long-standing challenge for neural networks. Most existing methods rely on additional network capacity or data replay. In contrast, we introduce a novel approach which we refer to as Recursive Gradient Optimization(RGO). RGO is composed of an iteratively updated optimizer that modifies the gradient to minimize forgetting without data replay and a virtual Feature Encoding Layer(FEL) that represents different long-term structures with only task descriptors. Experiments demonstrate that RGO has significantly better performance on popular continual classification benchmarks when compared to the baselines and achieves new state-of-the-art performance on 20-split-CIFAR100(82.22%) and 20-split-miniImageNet(72.63%). With higher average accuracy than Single-Task Learning(STL), this method is flexible and reliable to provide continual learning capabilities for learning models that rely on gradient descent.

</details>

### Representational Continuity for Unsupervised Continual Learning.
- **链接**: [出版页](https://openreview.net/forum?id=9Hrka5PA7LW)
- **作者**: Divyam Madaan, Jaehong Yoon, Yuanchun Li, Yunxin Liu, Sung Ju Hwang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

### Continual Learning with Filter Atom Swapping.
- **链接**: [出版页](https://openreview.net/forum?id=metRpM4Zrcb)
- **作者**: Zichen Miao, Ze Wang, Wei Chen, Qiang Qiu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

### CLEVA-Compass: A Continual Learning Evaluation Assessment Compass to Promote Research Transparency and Comparability.
- **链接**: [arXiv:2110.03331](https://arxiv.org/abs/2110.03331)
- **作者**: Martin Mundt, Steven Lang, Quentin Delfosse, Kristian Kersting
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> What is the state of the art in continual machine learning? Although a natural question for predominant static benchmarks, the notion to train systems in a lifelong manner entails a plethora of additional challenges with respect to set-up and evaluation. The latter have recently sparked a growing amount of critiques on prominent algorithm-centric perspectives and evaluation protocols being too narrow, resulting in several attempts at constructing guidelines in favor of specific desiderata or arguing against the validity of prevalent assumptions. In this work, we depart from this mindset and argue that the goal of a precise formulation of desiderata is an ill-posed one, as diverse applications may always warrant distinct scenarios. Instead, we introduce the Continual Learning EValuation Assessment Compass: the CLEVA-Compass. The compass provides the visual means to both identify how approaches are practically reported and how works can simultaneously be contextualized in the broader literature landscape. In addition to promoting compact specification in the spirit of recent replication trends, it thus provides an intuitive chart to understand the priorities of individual systems, where they resemble each other, and what elements are missing towards a fair comparison.

</details>

### Information-theoretic Online Memory Selection for Continual Learning.
- **链接**: [arXiv:2204.04763](https://arxiv.org/abs/2204.04763)
- **作者**: Shengyang Sun, Daniele Calandriello, Huiyi Hu, Ang Li, Michalis K. Titsias
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> A challenging problem in task-free continual learning is the online selection of a representative replay memory from data streams. In this work, we investigate the online memory selection problem from an information-theoretic perspective. To gather the most information, we propose the \textit{surprise} and the \textit{learnability} criteria to pick informative points and to avoid outliers. We present a Bayesian model to compute the criteria efficiently by exploiting rank-one matrix structures. We demonstrate that these criteria encourage selecting informative points in a greedy algorithm for online memory selection. Furthermore, by identifying the importance of \textit{the timing to update the memory}, we introduce a stochastic information-theoretic reservoir sampler (InfoRS), which conducts sampling among selective points with high information. Compared to reservoir sampling, InfoRS demonstrates improved robustness against data imbalance. Finally, empirical performances over continual learning benchmarks manifest its efficiency and efficacy.

</details>

### Memory Replay with Data Compression for Continual Learning.
- **链接**: [arXiv:2202.06592](https://arxiv.org/abs/2202.06592)
- **作者**: Liyuan Wang, Xingxing Zhang, Kuo Yang, Longhui Yu, Chongxuan Li, Lanqing Hong et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning needs to overcome catastrophic forgetting of the past. Memory replay of representative old training samples has been shown as an effective solution, and achieves the state-of-the-art (SOTA) performance. However, existing work is mainly built on a small memory buffer containing a few original data, which cannot fully characterize the old data distribution. In this work, we propose memory replay with data compression (MRDC) to reduce the storage cost of old training samples and thus increase their amount that can be stored in the memory buffer. Observing that the trade-off between the quality and quantity of compressed data is highly nontrivial for the efficacy of memory replay, we propose a novel method based on determinantal point processes (DPPs) to efficiently determine an appropriate compression quality for currently-arrived training samples. In this way, using a naive data compression algorithm with a properly selected quality can largely boost recent strong baselines by saving more compressed data in a limited storage space. We extensively validate this across several benchmarks of class-incremental learning and in a realistic scenario of object detection for autonomous driving.

</details>

### Pretrained Language Model in Continual Learning: A Comparative Study.
- **链接**: [出版页](https://openreview.net/forum?id=figzpGMrdD)
- **作者**: Tongtong Wu, Massimo Caccia, Zhuang Li, Yuan-Fang Li, Guilin Qi, Gholamreza Haffari
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

### Online Coreset Selection for Rehearsal-based Continual Learning.
- **链接**: [arXiv:2106.01085](https://arxiv.org/abs/2106.01085)
- **作者**: Jaehong Yoon, Divyam Madaan, Eunho Yang, Sung Ju Hwang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> A dataset is a shred of crucial evidence to describe a task. However, each data point in the dataset does not have the same potential, as some of the data points can be more representative or informative than others. This unequal importance among the data points may have a large impact in rehearsal-based continual learning, where we store a subset of the training examples (coreset) to be replayed later to alleviate catastrophic forgetting. In continual learning, the quality of the samples stored in the coreset directly affects the model's effectiveness and efficiency. The coreset selection problem becomes even more important under realistic settings, such as imbalanced continual learning or noisy data scenarios. To tackle this problem, we propose Online Coreset Selection (OCS), a simple yet effective method that selects the most representative and informative coreset at each iteration and trains them in an online manner. Our proposed method maximizes the model's adaptation to a current dataset while selecting high-affinity samples to past tasks, which directly inhibits catastrophic forgetting. We validate the effectiveness of our coreset selection mechanism over various standard, imbalanced, and noisy datasets against strong continual learning baselines, demonstrating that it improves task adaptation and prevents catastrophic forgetting in a sample-efficient manner.

</details>

### Subspace Regularizers for Few-Shot Class Incremental Learning.
- **链接**: [arXiv:2110.07059](https://arxiv.org/abs/2110.07059)
- **作者**: Afra Feyza Akyürek, Ekin Akyürek, Derry Wijaya, Jacob Andreas
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Few-shot class incremental learning -- the problem of updating a trained classifier to discriminate among an expanded set of classes with limited labeled data -- is a key challenge for machine learning systems deployed in non-stationary environments. Existing approaches to the problem rely on complex model architectures and training procedures that are difficult to tune and re-use. In this paper, we present an extremely simple approach that enables the use of ordinary logistic regression classifiers for few-shot incremental learning. The key to this approach is a new family of subspace regularization schemes that encourage weight vectors for new classes to lie close to the subspace spanned by the weights of existing classes. When combined with pretrained convolutional feature extractors, logistic regression models trained with subspace regularization outperform specialized, state-of-the-art approaches to few-shot incremental image classification by up to 22% on the miniImageNet dataset. Because of its simplicity, subspace regularization can be straightforwardly extended to incorporate additional background information about the new classes (including class names and descriptions specified in natural language); these further improve accuracy by up to 2%. Our results show that simple geometric regularization of class representations offers an effective tool for continual learning.

</details>

### Looking Back on Learned Experiences For Class/task Incremental Learning.
- **链接**: [出版页](https://openreview.net/forum?id=RxplU3vmBx)
- **作者**: Mozhgan PourKeshavarz, Guoying Zhao, Mohammad Sabokrou
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022
