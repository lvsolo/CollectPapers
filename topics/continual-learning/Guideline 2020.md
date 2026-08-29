# Continual Learning — 2020 Guideline

> 领域: 持续学习 / 增量学习（含 VLM/多模态场景）
> 论文数: 9 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Continual Learning with Adaptive Weights (CLAW).
- **链接**: [arXiv:1911.09514](https://arxiv.org/abs/1911.09514)
- **作者**: Tameem Adel, Han Zhao, Richard E. Turner
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Approaches to continual learning aim to successfully learn a set of related tasks that arrive in an online manner. Recently, several frameworks have been developed which enable deep learning to be deployed in this learning scenario. A key modelling decision is to what extent the architecture should be shared across tasks. On the one hand, separately modelling each task avoids catastrophic forgetting but it does not support transfer learning and leads to large models. On the other hand, rigidly specifying a shared component and a task-specific part enables task transfer and limits the model size, but it is vulnerable to catastrophic forgetting and restricts the form of task-transfer that can occur. Ideally, the network should adaptively identify which parts of the network to share in a data driven way. Here we introduce such an approach called Continual Learning with Adaptive Weights (CLAW), which is based on probabilistic modelling and variational inference. Experiments show that CLAW achieves state-of-the-art performance on six benchmarks in terms of overall continual learning performance, as measured by classification accuracy, and in terms of addressing catastrophic forgetting.

</details>

### Uncertainty-guided Continual Learning with Bayesian Neural Networks.
- **链接**: [arXiv:1906.02425](https://arxiv.org/abs/1906.02425)
- **作者**: Sayna Ebrahimi, Mohamed Elhoseiny, Trevor Darrell, Marcus Rohrbach
- **🏷️ 机构**: UC Berkeley
- **会议**: ICLR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning aims to learn new tasks without forgetting previously learned ones. This is especially challenging when one cannot access data from previous tasks and when the model has a fixed capacity. Current regularization-based continual learning algorithms need an external representation and extra computation to measure the parameters' \textit{importance}. In contrast, we propose Uncertainty-guided Continual Bayesian Neural Networks (UCB), where the learning rate adapts according to the uncertainty defined in the probability distribution of the weights in networks. Uncertainty is a natural way to identify \textit{what to remember} and \textit{what to change} as we continually learn, and thus mitigate catastrophic forgetting. We also show a variant of our model, which uses uncertainty for weight pruning and retains task performance after pruning by saving binary masks per tasks. We evaluate our UCB approach extensively on diverse object classification datasets with short and long sequences of tasks and report superior or on-par performance compared to existing approaches. Additionally, we show that our model does not necessarily need task information at test time, i.e. it does not presume knowledge of which task a sample belongs to.

</details>

### Continual Learning with Bayesian Neural Networks for Non-Stationary Data.
- **链接**: [出版页](https://openreview.net/forum?id=SJlsFpVtDB)
- **作者**: Richard Kurle, Botond Cseke, Alexej Klushyn, Patrick van der Smagt, Stephan Günnemann
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2020

### A Neural Dirichlet Process Mixture Model for Task-Free Continual Learning.
- **链接**: [arXiv:2001.00689](https://arxiv.org/abs/2001.00689)
- **作者**: Soochan Lee, Junsoo Ha, Dongsu Zhang, Gunhee Kim
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite the growing interest in continual learning, most of its contemporary works have been studied in a rather restricted setting where tasks are clearly distinguishable, and task boundaries are known during training. However, if our goal is to develop an algorithm that learns as humans do, this setting is far from realistic, and it is essential to develop a methodology that works in a task-free manner. Meanwhile, among several branches of continual learning, expansion-based methods have the advantage of eliminating catastrophic forgetting by allocating new resources to learn new data. In this work, we propose an expansion-based approach for task-free continual learning. Our model, named Continual Neural Dirichlet Process Mixture (CN-DPM), consists of a set of neural network experts that are in charge of a subset of the data. CN-DPM expands the number of experts in a principled way under the Bayesian nonparametric framework. With extensive experiments, we show that our model successfully performs task-free continual learning for both discriminative and generative tasks such as image classification and image generation.

</details>

### Compositional Language Continual Learning.
- **链接**: [出版页](https://openreview.net/forum?id=rklnDgHtDS)
- **作者**: Yuanpeng Li, Liang Zhao, Kenneth Church, Mohamed Elhoseiny
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2020

### Continual learning with hypernetworks.
- **链接**: [arXiv:1906.00695](https://arxiv.org/abs/1906.00695)
- **作者**: Johannes von Oswald, Christian Henning, João Sacramento, Benjamin F. Grewe
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Artificial neural networks suffer from catastrophic forgetting when they are sequentially trained on multiple tasks. To overcome this problem, we present a novel approach based on task-conditioned hypernetworks, i.e., networks that generate the weights of a target model based on task identity. Continual learning (CL) is less difficult for this class of models thanks to a simple key feature: instead of recalling the input-output relations of all previously seen data, task-conditioned hypernetworks only require rehearsing task-specific weight realizations, which can be maintained in memory using a simple regularizer. Besides achieving state-of-the-art performance on standard CL benchmarks, additional experiments on long task sequences reveal that task-conditioned hypernetworks display a very large capacity to retain previous memories. Notably, such long memory lifetimes are achieved in a compressive regime, when the number of trainable hypernetwork weights is comparable or smaller than target network size. We provide insight into the structure of low-dimensional task embedding spaces (the input space of the hypernetwork) and show that task-conditioned hypernetworks demonstrate transfer learning. Finally, forward information transfer is further supported by empirical results on a challenging CL benchmark based on the CIFAR-10/100 image datasets.

</details>

### Functional Regularisation for Continual Learning with Gaussian Processes.
- **链接**: [出版页](https://openreview.net/forum?id=HkxCzeHFDB)
- **作者**: Michalis K. Titsias, Jonathan Schwarz, Alexander G. de G. Matthews, Razvan Pascanu, Yee Whye Teh
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2020

### Scalable and Order-robust Continual Learning with Additive Parameter Decomposition.
- **链接**: [出版页](https://openreview.net/forum?id=r1gdj2EKPB)
- **作者**: Jaehong Yoon, Saehoon Kim, Eunho Yang, Sung Ju Hwang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2020

### The Implicit Bias of Depth: How Incremental Learning Drives Generalization.
- **链接**: [arXiv:1909.12051](https://arxiv.org/abs/1909.12051)
- **作者**: Daniel Gissin, Shai Shalev-Shwartz, Amit Daniely
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> A leading hypothesis for the surprising generalization of neural networks is that the dynamics of gradient descent bias the model towards simple solutions, by searching through the solution space in an incremental order of complexity. We formally define the notion of incremental learning dynamics and derive the conditions on depth and initialization for which this phenomenon arises in deep linear models. Our main theoretical contribution is a dynamical depth separation result, proving that while shallow models can exhibit incremental learning dynamics, they require the initialization to be exponentially small for these dynamics to present themselves. However, once the model becomes deeper, the dependence becomes polynomial and incremental learning can arise in more natural settings. We complement our theoretical findings by experimenting with deep matrix sensing, quadratic neural networks and with binary classification using diagonal and convolutional linear networks, showing all of these models exhibit incremental learning.

</details>
