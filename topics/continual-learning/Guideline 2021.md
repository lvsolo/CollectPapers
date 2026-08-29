# Continual Learning — 2021 Guideline

> 领域: 持续学习 / 增量学习（含 VLM/多模态场景）
> 论文数: 9 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### EEC: Learning to Encode and Regenerate Images for Continual Learning.
- **链接**: [arXiv:2101.04904](https://arxiv.org/abs/2101.04904)
- **作者**: Ali Ayub, Alan R. Wagner
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The two main impediments to continual learning are catastrophic forgetting and memory limitations on the storage of data. To cope with these challenges, we propose a novel, cognitively-inspired approach which trains autoencoders with Neural Style Transfer to encode and store images. During training on a new task, reconstructed images from encoded episodes are replayed in order to avoid catastrophic forgetting. The loss function for the reconstructed images is weighted to reduce its effect during classifier training to cope with image degradation. When the system runs out of memory the encoded episodes are converted into centroids and covariance matrices, which are used to generate pseudo-images during classifier training, keeping classifier performance stable while using less memory. Our approach increases classification accuracy by 13-17% over state-of-the-art methods on benchmark datasets, while requiring 78% less storage space.

</details>

### CPR: Classifier-Projection Regularization for Continual Learning.
- **链接**: [arXiv:2006.07326](https://arxiv.org/abs/2006.07326) · [代码](https://github.com/csm9493/CPR_CL)
- **作者**: Sungmin Cha, Hsiang Hsu, Taebaek Hwang, Flávio P. Calmon, Taesup Moon
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose a general, yet simple patch that can be applied to existing regularization-based continual learning methods called classifier-projection regularization (CPR). Inspired by both recent results on neural networks with wide local minima and information theory, CPR adds an additional regularization term that maximizes the entropy of a classifier's output probability. We demonstrate that this additional term can be interpreted as a projection of the conditional probability given by a classifier's output to the uniform distribution. By applying the Pythagorean theorem for KL divergence, we then prove that this projection may (in theory) improve the performance of continual learning methods. In our extensive experimental results, we apply CPR to several state-of-the-art regularization-based continual learning methods and benchmark performance on popular image recognition datasets. Our results demonstrate that CPR indeed promotes a wide local minima and significantly improves both accuracy and plasticity while simultaneously mitigating the catastrophic forgetting of baseline continual learning methods. The codes and scripts for this work are available at https://github.com/csm9493/CPR_CL.

</details>

### Continual learning in recurrent neural networks.
- **链接**: [出版页](https://openreview.net/forum?id=8xeBUgD8u9)
- **作者**: Benjamin Ehret, Christian Henning, Maria R. Cervera, Alexander Meulemans, Johannes von Oswald, Benjamin F. Grewe
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

### Generalized Variational Continual Learning.
- **链接**: [arXiv:2011.12328](https://arxiv.org/abs/2011.12328)
- **作者**: Noel Loo, Siddharth Swaroop, Richard E. Turner
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning deals with training models on new tasks and datasets in an online fashion. One strand of research has used probabilistic regularization for continual learning, with two of the main approaches in this vein being Online Elastic Weight Consolidation (Online EWC) and Variational Continual Learning (VCL). VCL employs variational inference, which in other settings has been improved empirically by applying likelihood-tempering. We show that applying this modification to VCL recovers Online EWC as a limiting case, allowing for interpolation between the two approaches. We term the general algorithm Generalized VCL (GVCL). In order to mitigate the observed overpruning effect of VI, we take inspiration from a common multi-task architecture, neural networks with task-specific FiLM layers, and find that this addition leads to significant performance gains, specifically for variational methods. In the small-data regime, GVCL strongly outperforms existing baselines. In larger datasets, GVCL with FiLM layers outperforms or is competitive with existing baselines in terms of accuracy, whilst also providing significantly better calibration.

</details>

### Linear Mode Connectivity in Multitask and Continual Learning.
- **链接**: [arXiv:2010.04495](https://arxiv.org/abs/2010.04495)
- **作者**: Seyed-Iman Mirzadeh, Mehrdad Farajtabar, Dilan Görür, Razvan Pascanu, Hassan Ghasemzadeh
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual (sequential) training and multitask (simultaneous) training are often attempting to solve the same overall objective: to find a solution that performs well on all considered tasks. The main difference is in the training regimes, where continual learning can only have access to one task at a time, which for neural networks typically leads to catastrophic forgetting. That is, the solution found for a subsequent task does not perform well on the previous ones anymore. However, the relationship between the different minima that the two training regimes arrive at is not well understood. What sets them apart? Is there a local structure that could explain the difference in performance achieved by the two different schemes? Motivated by recent work showing that different minima of the same task are typically connected by very simple curves of low error, we investigate whether multitask and continual solutions are similarly connected. We empirically find that indeed such connectivity can be reliably achieved and, more interestingly, it can be done by a linear path, conditioned on having the same initialization for both. We thoroughly analyze this observation and discuss its significance for the continual learning process. Furthermore, we exploit this finding to propose an effective algorithm that constrains the sequentially learned minima to behave as the multitask solution. We show that our method outperforms several state of the art continual learning algorithms on various vision benchmarks.

</details>

### Contextual Transformation Networks for Online Continual Learning.
- **链接**: [出版页](https://openreview.net/forum?id=zx_uX-BO7CH)
- **作者**: Quang Pham, Chenghao Liu, Doyen Sahoo, Steven C. H. Hoi
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

### Gradient Projection Memory for Continual Learning.
- **链接**: [arXiv:2103.09762](https://arxiv.org/abs/2103.09762)
- **作者**: Gobinda Saha, Isha Garg, Kaushik Roy
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The ability to learn continually without forgetting the past tasks is a desired attribute for artificial learning systems. Existing approaches to enable such learning in artificial neural networks usually rely on network growth, importance based weight update or replay of old data from the memory. In contrast, we propose a novel approach where a neural network learns new tasks by taking gradient steps in the orthogonal direction to the gradient subspaces deemed important for the past tasks. We find the bases of these subspaces by analyzing network representations (activations) after learning each task with Singular Value Decomposition (SVD) in a single shot manner and store them in the memory as Gradient Projection Memory (GPM). With qualitative and quantitative analyses, we show that such orthogonal gradient descent induces minimum to no interference with the past tasks, thereby mitigates forgetting. We evaluate our algorithm on diverse image classification datasets with short and long sequences of tasks and report better or on-par performance compared to the state-of-the-art approaches.

</details>

### Graph-Based Continual Learning.
- **链接**: [出版页](https://openreview.net/forum?id=HHSEKOnPvaO)
- **作者**: Binh Tang, David S. Matteson
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

### Efficient Continual Learning with Modular Networks and Task-Driven Priors.
- **链接**: [arXiv:2012.12631](https://arxiv.org/abs/2012.12631)
- **作者**: Tom Veniat, Ludovic Denoyer, Marc'Aurelio Ranzato
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing literature in Continual Learning (CL) has focused on overcoming catastrophic forgetting, the inability of the learner to recall how to perform tasks observed in the past. There are however other desirable properties of a CL system, such as the ability to transfer knowledge from previous tasks and to scale memory and compute sub-linearly with the number of tasks. Since most current benchmarks focus only on forgetting using short streams of tasks, we first propose a new suite of benchmarks to probe CL algorithms across these new axes. Finally, we introduce a new modular architecture, whose modules represent atomic skills that can be composed to perform a certain task. Learning a task reduces to figuring out which past modules to re-use, and which new modules to instantiate to solve the current task. Our learning algorithm leverages a task-driven prior over the exponential search space of all possible ways to combine modules, enabling efficient learning on long streams of tasks. Our experiments show that this modular architecture and learning algorithm perform competitively on widely used CL benchmarks while yielding superior performance on the more challenging benchmarks we introduce in this work.

</details>
