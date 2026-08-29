# Continual Learning — 2020 Guideline

> 领域: 持续学习 / 增量学习（含 VLM/多模态场景）
> 论文数: 8 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Conditional Channel Gated Networks for Task-Aware Continual Learning.
- **链接**: [arXiv:2004.00070](https://arxiv.org/abs/2004.00070) · 📚 被引 140
- **作者**: Davide Abati, Jakub M. Tomczak, Tijmen Blankevoort, Simone Calderara, Rita Cucchiara, Babak Ehteshami Bejnordi
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Convolutional Neural Networks experience catastrophic forgetting when optimized on a sequence of learning problems: as they meet the objective of the current training examples, their performance on previous tasks drops drastically. In this work, we introduce a novel framework to tackle this problem with conditional computation. We equip each convolutional layer with task-specific gating modules, selecting which filters to apply on the given input. This way, we achieve two appealing properties. Firstly, the execution patterns of the gates allow to identify and protect important filters, ensuring no loss in the performance of the model for previously learned tasks. Secondly, by using a sparsity objective, we can promote the selection of a limited set of kernels, allowing to retain sufficient model capacity to digest new tasks.Existing solutions require, at test time, awareness of the task to which each example belongs to. This knowledge, however, may not be available in many practical scenarios. Therefore, we additionally introduce a task classifier that predicts the task label of each example, to deal with settings in which a task oracle is not available. We validate our proposal on four continual learning datasets. Results show that our model consistently outperforms existing methods both in the presence and the absence of a task oracle. Notably, on Split SVHN and Imagenet-50 datasets, our model yields up to 23.98% and 17.42% improvement in accuracy w.r.t. competing methods.

</details>

### Continual Learning With Extended Kronecker-Factored Approximate Curvature.
- **链接**: [arXiv:2004.07507](https://arxiv.org/abs/2004.07507) · 📚 被引 44
- **作者**: Janghyeon Lee, Hyeong Gwon Hong, Donggyu Joo, Junmo Kim
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose a quadratic penalty method for continual learning of neural networks that contain batch normalization (BN) layers. The Hessian of a loss function represents the curvature of the quadratic penalty function, and a Kronecker-factored approximate curvature (K-FAC) is used widely to practically compute the Hessian of a neural network. However, the approximation is not valid if there is dependence between examples, typically caused by BN layers in deep network architectures. We extend the K-FAC method so that the inter-example relations are taken into account and the Hessian of deep neural networks can be properly approximated under practical assumptions. We also propose a method of weight merging and reparameterization to properly handle statistical parameters of BN, which plays a critical role for continual learning with BN, and a method that selects hyperparameters without source task data. Our method shows better performance than baselines in the permuted MNIST task with BN layers and in sequential learning from the ImageNet classification task to fine-grained classification tasks with ResNet-50, without any explicit or implicit use of source task data for hyperparameter selection.

</details>

### Semantic Drift Compensation for Class-Incremental Learning.
- **链接**: [arXiv:2004.00440](https://arxiv.org/abs/2004.00440) · 📚 被引 268
- **作者**: Lu Yu, Bartlomiej Twardowski, Xialei Liu, Luis Herranz, Kai Wang, Yongmei Cheng et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Class-incremental learning of deep networks sequentially increases the number of classes to be classified. During training, the network has only access to data of one task at a time, where each task contains several classes. In this setting, networks suffer from catastrophic forgetting which refers to the drastic drop in performance on previous tasks. The vast majority of methods have studied this scenario for classification networks, where for each new task the classification layer of the network must be augmented with additional weights to make room for the newly added classes. Embedding networks have the advantage that new classes can be naturally included into the network without adding new weights. Therefore, we study incremental learning for embedding networks. In addition, we propose a new method to estimate the drift, called semantic drift, of features and compensate for it without the need of any exemplars. We approximate the drift of previous tasks based on the drift that is experienced by current task data. We perform experiments on fine-grained datasets, CIFAR100 and ImageNet-Subset. We demonstrate that embedding networks suffer significantly less from catastrophic forgetting. We outperform existing methods which do not require exemplars and obtain competitive results compared to methods which store exemplars. Furthermore, we show that our proposed SDC when combined with existing methods to prevent forgetting consistently improves results.

</details>

### Modeling the Background for Incremental Learning in Semantic Segmentation.
- **链接**: [arXiv:2002.00718](https://arxiv.org/abs/2002.00718) · 📚 被引 310
- **作者**: Fabio Cermelli, Massimiliano Mancini, Samuel Rota Bulò, Elisa Ricci, Barbara Caputo
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite their effectiveness in a wide range of tasks, deep architectures suffer from some important limitations. In particular, they are vulnerable to catastrophic forgetting, i.e. they perform poorly when they are required to update their model as new classes are available but the original training set is not retained. This paper addresses this problem in the context of semantic segmentation. Current strategies fail on this task because they do not consider a peculiar aspect of semantic segmentation: since each training step provides annotation only for a subset of all possible classes, pixels of the background class (i.e. pixels that do not belong to any other classes) exhibit a semantic distribution shift. In this work we revisit classical incremental learning methods, proposing a new distillation-based framework which explicitly accounts for this shift. Furthermore, we introduce a novel strategy to initialize classifier's parameters, thus preventing biased predictions toward the background class. We demonstrate the effectiveness of our approach with an extensive evaluation on the Pascal-VOC 2012 and ADE20K datasets, significantly outperforming state of the art incremental learning methods.

</details>

### Incremental Learning in Online Scenario.
- **链接**: [arXiv:2003.13191](https://arxiv.org/abs/2003.13191) · 📚 被引 140
- **作者**: Jiangpeng He, Runyu Mao, Zeman Shao, Fengqing Zhu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Modern deep learning approaches have achieved great success in many vision applications by training a model using all available task-specific data. However, there are two major obstacles making it challenging to implement for real life applications: (1) Learning new classes makes the trained model quickly forget old classes knowledge, which is referred to as catastrophic forgetting. (2) As new observations of old classes come sequentially over time, the distribution may change in unforeseen way, making the performance degrade dramatically on future data, which is referred to as concept drift. Current state-of-the-art incremental learning methods require a long time to train the model whenever new classes are added and none of them takes into consideration the new observations of old classes. In this paper, we propose an incremental learning framework that can work in the challenging online learning scenario and handle both new classes data and new observations of old classes. We address problem (1) in online mode by introducing a modified cross-distillation loss together with a two-step learning technique. Our method outperforms the results obtained from current state-of-the-art offline incremental learning methods on the CIFAR-100 and ImageNet-1000 (ILSVRC 2012) datasets under the same experiment protocol but in online scenario. We also provide a simple yet effective method to mitigate problem (2) by updating exemplar set using the feature of each new observation of old classes and demonstrate a real life application of online food image classification based on our complete framework using the Food-101 dataset.

</details>

### Mnemonics Training: Multi-Class Incremental Learning Without Forgetting.
- **链接**: [arXiv:2002.10211](https://arxiv.org/abs/2002.10211) · 📚 被引 273
- **作者**: Yaoyao Liu, Yuting Su, An-An Liu, Bernt Schiele, Qianru Sun
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-Class Incremental Learning (MCIL) aims to learn new concepts by incrementally updating a model trained on previous concepts. However, there is an inherent trade-off to effectively learning new concepts without catastrophic forgetting of previous ones. To alleviate this issue, it has been proposed to keep around a few examples of the previous concepts but the effectiveness of this approach heavily depends on the representativeness of these examples. This paper proposes a novel and automatic framework we call mnemonics, where we parameterize exemplars and make them optimizable in an end-to-end manner. We train the framework through bilevel optimizations, i.e., model-level and exemplar-level. We conduct extensive experiments on three MCIL benchmarks, CIFAR-100, ImageNet-Subset and ImageNet, and show that using mnemonics exemplars can surpass the state-of-the-art by a large margin. Interestingly and quite intriguingly, the mnemonics exemplars tend to be on the boundaries between different classes.

</details>

### Few-Shot Class-Incremental Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Tao_Few-Shot_Class-Incremental_Learning_CVPR_2020_paper.html)
- **作者**: Xiaoyu Tao, Xiaopeng Hong, Xinyuan Chang, Songlin Dong, Xing Wei, Yihong Gong
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Maintaining Discrimination and Fairness in Class Incremental Learning.
- **链接**: [arXiv:1911.07053](https://arxiv.org/abs/1911.07053) · 📚 被引 431
- **作者**: Bowen Zhao, Xi Xiao, Guojun Gan, Bin Zhang, Shu-Tao Xia
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep neural networks (DNNs) have been applied in class incremental learning, which aims to solve common real-world problems of learning new classes continually. One drawback of standard DNNs is that they are prone to catastrophic forgetting. Knowledge distillation (KD) is a commonly used technique to alleviate this problem. In this paper, we demonstrate it can indeed help the model to output more discriminative results within old classes. However, it cannot alleviate the problem that the model tends to classify objects into new classes, causing the positive effect of KD to be hidden and limited. We observed that an important factor causing catastrophic forgetting is that the weights in the last fully connected (FC) layer are highly biased in class incremental learning. In this paper, we propose a simple and effective solution motivated by the aforementioned observations to address catastrophic forgetting. Firstly, we utilize KD to maintain the discrimination within old classes. Then, to further maintain the fairness between old classes and new classes, we propose Weight Aligning (WA) that corrects the biased weights in the FC layer after normal training process. Unlike previous work, WA does not require any extra parameters or a validation set in advance, as it utilizes the information provided by the biased weights themselves. The proposed method is evaluated on ImageNet-1000, ImageNet-100, and CIFAR-100 under various settings. Experimental results show that the proposed method can effectively alleviate catastrophic forgetting and significantly outperform state-of-the-art methods.

</details>
