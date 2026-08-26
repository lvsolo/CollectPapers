# Continual Learning — 2020 Guideline

> 领域: 持续学习 / 增量学习（含 VLM/多模态场景）
> 论文数: 8 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Conditional Channel Gated Networks for Task-Aware Continual Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Abati_Conditional_Channel_Gated_Networks_for_Task-Aware_Continual_Learning_CVPR_2020_paper.html) · 📚 被引 140
- **作者**: Davide Abati, Jakub M. Tomczak, Tijmen Blankevoort, Simone Calderara, Rita Cucchiara, Babak Ehteshami Bejnordi
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Continual Learning With Extended Kronecker-Factored Approximate Curvature.
- **链接**: [arXiv:2004.07507](https://arxiv.org/abs/2004.07507) · 📚 被引 44
- **作者**: Janghyeon Lee, Hyeong Gwon Hong, Donggyu Joo, Junmo Kim
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

- **摘要（英，原文）**:

  > We propose a quadratic penalty method for continual learning of neural networks that contain batch normalization (BN) layers. The Hessian of a loss function represents the curvature of the quadratic penalty function, and a Kronecker-factored approximate curvature (K-FAC) is used widely to practically compute the Hessian of a neural network. However, the approximation is not valid if there is dependence between examples, typically caused by BN layers in deep network architectures. We extend the K-FAC method so that the inter-example relations are taken into account and the Hessian of deep neural networks can be properly approximated under practical assumptions. We also propose a method of weight merging and reparameterization to properly handle statistical parameters of BN, which plays a critical role for continual learning with BN, and a method that selects hyperparameters without source task data. Our method shows better performance than baselines in the permuted MNIST task with BN layers and in sequential learning from the ImageNet classification task to fine-grained classification tasks with ResNet-50, without any explicit or implicit use of source task data for hyperparameter selection.

### Semantic Drift Compensation for Class-Incremental Learning.
- **链接**: [arXiv:2004.00440](https://arxiv.org/abs/2004.00440) · 📚 被引 268
- **作者**: Lu Yu, Bartlomiej Twardowski, Xialei Liu, Luis Herranz, Kai Wang, Yongmei Cheng et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

- **摘要（英，原文）**:

  > Class-incremental learning of deep networks sequentially increases the number of classes to be classified. During training, the network has only access to data of one task at a time, where each task contains several classes. In this setting, networks suffer from catastrophic forgetting which refers to the drastic drop in performance on previous tasks. The vast majority of methods have studied this scenario for classification networks, where for each new task the classification layer of the network must be augmented with additional weights to make room for the newly added classes. Embedding networks have the advantage that new classes can be naturally included into the network without adding new weights. Therefore, we study incremental learning for embedding networks. In addition, we propose a new method to estimate the drift, called semantic drift, of features and compensate for it without the need of any exemplars. We approximate the drift of previous tasks based on the drift that is experienced by current task data. We perform experiments on fine-grained datasets, CIFAR100 and ImageNet-Subset. We demonstrate that embedding networks suffer significantly less from catastrophic forgetting. We outperform existing methods which do not require exemplars and obtain competitive results compared to methods which store exemplars. Furthermore, we show that our proposed SDC when combined with existing methods to prevent forgetting consistently improves results.

### Modeling the Background for Incremental Learning in Semantic Segmentation.
- **链接**: [arXiv:2002.00718](https://arxiv.org/abs/2002.00718) · 📚 被引 308
- **作者**: Fabio Cermelli, Massimiliano Mancini, Samuel Rota Bulò, Elisa Ricci, Barbara Caputo
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

- **摘要（英，原文）**:

  > Despite their effectiveness in a wide range of tasks, deep architectures suffer from some important limitations. In particular, they are vulnerable to catastrophic forgetting, i.e. they perform poorly when they are required to update their model as new classes are available but the original training set is not retained. This paper addresses this problem in the context of semantic segmentation. Current strategies fail on this task because they do not consider a peculiar aspect of semantic segmentation: since each training step provides annotation only for a subset of all possible classes, pixels of the background class (i.e. pixels that do not belong to any other classes) exhibit a semantic distribution shift. In this work we revisit classical incremental learning methods, proposing a new distillation-based framework which explicitly accounts for this shift. Furthermore, we introduce a novel strategy to initialize classifier's parameters, thus preventing biased predictions toward the background class. We demonstrate the effectiveness of our approach with an extensive evaluation on the Pascal-VOC 2012 and ADE20K datasets, significantly outperforming state of the art incremental learning methods.

### Incremental Learning in Online Scenario.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/He_Incremental_Learning_in_Online_Scenario_CVPR_2020_paper.html) · 📚 被引 139
- **作者**: Jiangpeng He, Runyu Mao, Zeman Shao, Fengqing Zhu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Mnemonics Training: Multi-Class Incremental Learning Without Forgetting.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Liu_Mnemonics_Training_Multi-Class_Incremental_Learning_Without_Forgetting_CVPR_2020_paper.html) · 📚 被引 273
- **作者**: Yaoyao Liu, Yuting Su, An-An Liu, Bernt Schiele, Qianru Sun
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Few-Shot Class-Incremental Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Tao_Few-Shot_Class-Incremental_Learning_CVPR_2020_paper.html)
- **作者**: Xiaoyu Tao, Xiaopeng Hong, Xinyuan Chang, Songlin Dong, Xing Wei, Yihong Gong
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Maintaining Discrimination and Fairness in Class Incremental Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Zhao_Maintaining_Discrimination_and_Fairness_in_Class_Incremental_Learning_CVPR_2020_paper.html) · 📚 被引 430
- **作者**: Bowen Zhao, Xi Xiao, Guojun Gan, Bin Zhang, Shu-Tao Xia
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
