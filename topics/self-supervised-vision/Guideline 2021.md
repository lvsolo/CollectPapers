# Self-supervised Vision — 2021 Guideline

> 领域: 视觉自监督学习（对比学习、MAE、DINO 系）
> 论文数: 15 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Self-supervised and Supervised Joint Training for Resource-rich Machine Translation.
- **链接**: [arXiv:2106.04060](https://arxiv.org/abs/2106.04060)
- **作者**: Yong Cheng, Wei Wang, Lu Jiang, Wolfgang Macherey
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised pre-training of text representations has been successfully applied to low-resource Neural Machine Translation (NMT). However, it usually fails to achieve notable gains on resource-rich NMT. In this paper, we propose a joint training approach, $F_2$-XEnDec, to combine self-supervised and supervised learning to optimize NMT models. To exploit complementary self-supervised signals for supervised learning, NMT models are trained on examples that are interbred from monolingual and parallel sentences through a new process called crossover encoder-decoder. Experiments on two resource-rich translation benchmarks, WMT'14 English-German and WMT'14 English-French, demonstrate that our approach achieves substantial improvements over several strong baseline methods and obtains a new state of the art of 46.19 BLEU on English-French when incorporating back translation. Results also show that our approach is capable of improving model robustness to input perturbations such as code-switching noise which frequently appears on social media.

</details>

### Whitening for Self-Supervised Representation Learning.
- **链接**: [arXiv:2007.06346](https://arxiv.org/abs/2007.06346) · [代码](https://github.com/htdt/self-supervised)
- **作者**: Aleksandr Ermolov, Aliaksandr Siarohin, Enver Sangineto, Nicu Sebe
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Most of the current self-supervised representation learning (SSL) methods are based on the contrastive loss and the instance-discrimination task, where augmented versions of the same image instance ("positives") are contrasted with instances extracted from other images ("negatives"). For the learning to be effective, many negatives should be compared with a positive pair, which is computationally demanding. In this paper, we propose a different direction and a new loss function for SSL, which is based on the whitening of the latent-space features. The whitening operation has a "scattering" effect on the batch samples, avoiding degenerate solutions where all the sample representations collapse to a single point. Our solution does not require asymmetric networks and it is conceptually simple. Moreover, since negatives are not needed, we can extract multiple positive pairs from the same image instance. The source code of the method and of all the experiments is available at: https://github.com/htdt/self-supervised.

</details>

### Causal Curiosity: RL Agents Discovering Self-supervised Experiments for Causal Representation Learning.
- **链接**: [arXiv:2010.03110](https://arxiv.org/abs/2010.03110)
- **作者**: Sumedh A. Sontakke, Arash Mehrjou, Laurent Itti, Bernhard Schölkopf
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Animals exhibit an innate ability to learn regularities of the world through interaction. By performing experiments in their environment, they are able to discern the causal factors of variation and infer how they affect the world's dynamics. Inspired by this, we attempt to equip reinforcement learning agents with the ability to perform experiments that facilitate a categorization of the rolled-out trajectories, and to subsequently infer the causal factors of the environment in a hierarchical manner. We introduce {\em causal curiosity}, a novel intrinsic reward, and show that it allows our agents to learn optimal sequences of actions and discover causal factors in the dynamics of the environment. The learned behavior allows the agents to infer a binary quantized representation for the ground-truth causal factors in every environment. Additionally, we find that these experimental behaviors are semantically meaningful (e.g., our agents learn to lift blocks to categorize them by weight), and are learnt in a self-supervised manner with approximately 2.5 times less data than conventional supervised planners. We show that these behaviors can be re-purposed and fine-tuned (e.g., from lifting to pushing or other downstream tasks). Finally, we show that the knowledge of causal factor representations aids zero-shot learning for more complex tasks. Visit https://sites.google.com/usc.edu/causal-curiosity/home for website.

</details>

### Understanding self-supervised learning dynamics without contrastive pairs.
- **链接**: [arXiv:2102.06810](https://arxiv.org/abs/2102.06810) · [代码](https://github.com/facebookresearch/luckmatters)
- **作者**: Yuandong Tian, Xinlei Chen, Surya Ganguli
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While contrastive approaches of self-supervised learning (SSL) learn representations by minimizing the distance between two augmented views of the same data point (positive pairs) and maximizing views from different data points (negative pairs), recent \emph{non-contrastive} SSL (e.g., BYOL and SimSiam) show remarkable performance {\it without} negative pairs, with an extra learnable predictor and a stop-gradient operation. A fundamental question arises: why do these methods not collapse into trivial representations? We answer this question via a simple theoretical study and propose a novel approach, DirectPred, that \emph{directly} sets the linear predictor based on the statistics of its inputs, without gradient training. On ImageNet, it performs comparably with more complex two-layer non-linear predictors that employ BatchNorm and outperforms a linear predictor by $2.5\%$ in 300-epoch training (and $5\%$ in 60-epoch). DirectPred is motivated by our theoretical study of the nonlinear learning dynamics of non-contrastive SSL in simple linear networks. Our study yields conceptual insights into how non-contrastive SSL methods learn, how they avoid representational collapse, and how multiple factors, like predictor networks, stop-gradients, exponential moving averages, and weight decay all come into play. Our simple theory recapitulates the results of real-world ablation studies in both STL-10 and ImageNet. Code is released https://github.com/facebookresearch/luckmatters/tree/master/ssl.

</details>

### Toward Understanding the Feature Learning Process of Self-supervised Contrastive Learning.
- **链接**: [arXiv:2105.15134](https://arxiv.org/abs/2105.15134)
- **作者**: Zixin Wen, Yuanzhi Li
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> How can neural networks trained by contrastive learning extract features from the unlabeled data? Why does contrastive learning usually need much stronger data augmentations than supervised learning to ensure good representations? These questions involve both the optimization and statistical aspects of deep learning, but can hardly be answered by analyzing supervised learning, where the target functions are the highest pursuit. Indeed, in self-supervised learning, it is inevitable to relate to the optimization/generalization of neural networks to how they can encode the latent structures in the data, which we refer to as the feature learning process. In this work, we formally study how contrastive learning learns the feature representations for neural networks by analyzing its feature learning process. We consider the case where our data are comprised of two types of features: the more semantically aligned sparse features which we want to learn from, and the other dense features we want to avoid. Theoretically, we prove that contrastive learning using $\mathbf{ReLU}$ networks provably learns the desired sparse features if proper augmentations are adopted. We present an underlying principle called $\textbf{feature decoupling}$ to explain the effects of augmentations, where we theoretically characterize how augmentations can reduce the correlations of dense features between positive samples while keeping the correlations of sparse features intact, thereby forcing the neural networks to learn from the self-supervision of sparse features. Empirically, we verified that the feature decoupling principle matches the underlying mechanism of contrastive learning in practice.

</details>

### Self-supervised Graph-level Representation Learning with Local and Global Structure.
- **链接**: [arXiv:2106.04113](https://arxiv.org/abs/2106.04113)
- **作者**: Minghao Xu, Hang Wang, Bingbing Ni, Hongyu Guo, Jian Tang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper studies unsupervised/self-supervised whole-graph representation learning, which is critical in many tasks such as molecule properties prediction in drug and material discovery. Existing methods mainly focus on preserving the local similarity structure between different graph instances but fail to discover the global semantic structure of the entire data set. In this paper, we propose a unified framework called Local-instance and Global-semantic Learning (GraphLoG) for self-supervised whole-graph representation learning. Specifically, besides preserving the local similarities, GraphLoG introduces the hierarchical prototypes to capture the global semantic clusters. An efficient online expectation-maximization (EM) algorithm is further developed for learning the model. We evaluate GraphLoG by pre-training it on massive unlabeled graphs followed by fine-tuning on downstream tasks. Extensive experiments on both chemical and biological benchmark data sets demonstrate the effectiveness of the proposed approach.

</details>

### Barlow Twins: Self-Supervised Learning via Redundancy Reduction.
- **链接**: [arXiv:2103.03230](https://arxiv.org/abs/2103.03230)
- **作者**: Jure Zbontar, Li Jing, Ishan Misra, Yann LeCun, Stéphane Deny
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning (SSL) is rapidly closing the gap with supervised methods on large computer vision benchmarks. A successful approach to SSL is to learn embeddings which are invariant to distortions of the input sample. However, a recurring issue with this approach is the existence of trivial constant solutions. Most current methods avoid such solutions by careful implementation details. We propose an objective function that naturally avoids collapse by measuring the cross-correlation matrix between the outputs of two identical networks fed with distorted versions of a sample, and making it as close to the identity matrix as possible. This causes the embedding vectors of distorted versions of a sample to be similar, while minimizing the redundancy between the components of these vectors. The method is called Barlow Twins, owing to neuroscientist H. Barlow's redundancy-reduction principle applied to a pair of identical networks. Barlow Twins does not require large batches nor asymmetry between the network twins such as a predictor network, gradient stopping, or a moving average on the weight updates. Intriguingly it benefits from very high-dimensional output vectors. Barlow Twins outperforms previous methods on ImageNet for semi-supervised classification in the low-data regime, and is on par with current state of the art for ImageNet classification with a linear classifier head, and for transfer tasks of classification and object detection.

</details>

### Large-Margin Contrastive Learning with Distance Polarization Regularizer.
- **链接**: [出版页](http://proceedings.mlr.press/v139/chen21n.html)
- **作者**: Shuo Chen, Gang Niu, Chen Gong, Jun Li, Jian Yang, Masashi Sugiyama
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2021

### Function Contrastive Learning of Transferable Meta-Representations.
- **链接**: [出版页](http://proceedings.mlr.press/v139/gondal21a.html)
- **作者**: Muhammad Waleed Gondal, Shruti Joshi, Nasim Rahaman, Stefan Bauer, Manuel Wuthrich, Bernhard Schölkopf
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2021

### Self-Damaging Contrastive Learning.
- **链接**: [arXiv:2106.02990](https://arxiv.org/abs/2106.02990) · [代码](https://github.com/VITA-Group/SDCLR)
- **作者**: Ziyu Jiang, Tianlong Chen, Bobak J. Mortazavi, Zhangyang Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The recent breakthrough achieved by contrastive learning accelerates the pace for deploying unsupervised training on real-world data applications. However, unlabeled data in reality is commonly imbalanced and shows a long-tail distribution, and it is unclear how robustly the latest contrastive learning methods could perform in the practical scenario. This paper proposes to explicitly tackle this challenge, via a principled framework called Self-Damaging Contrastive Learning (SDCLR), to automatically balance the representation learning without knowing the classes. Our main inspiration is drawn from the recent finding that deep models have difficult-to-memorize samples, and those may be exposed through network pruning. It is further natural to hypothesize that long-tail samples are also tougher for the model to learn well due to insufficient examples. Hence, the key innovation in SDCLR is to create a dynamic self-competitor model to contrast with the target model, which is a pruned version of the latter. During training, contrasting the two models will lead to adaptive online mining of the most easily forgotten samples for the current target model, and implicitly emphasize them more in the contrastive loss. Extensive experiments across multiple datasets and imbalance settings show that SDCLR significantly improves not only overall accuracies but also balancedness, in terms of linear evaluation on the full-shot and few-shot settings. Our code is available at: https://github.com/VITA-Group/SDCLR.

</details>

### CLOCS: Contrastive Learning of Cardiac Signals Across Space, Time, and Patients.
- **链接**: [出版页](http://proceedings.mlr.press/v139/kiyasseh21a.html)
- **作者**: Dani Kiyasseh, Tingting Zhu, David A. Clifton
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2021

### Towards Domain-Agnostic Contrastive Learning.
- **链接**: [arXiv:2011.04419](https://arxiv.org/abs/2011.04419)
- **作者**: Vikas Verma, Thang Luong, Kenji Kawaguchi, Hieu Pham, Quoc V. Le
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite recent success, most contrastive self-supervised learning methods are domain-specific, relying heavily on data augmentation techniques that require knowledge about a particular domain, such as image cropping and rotation. To overcome such limitation, we propose a novel domain-agnostic approach to contrastive learning, named DACL, that is applicable to domains where invariances, and thus, data augmentation techniques, are not readily available. Key to our approach is the use of Mixup noise to create similar and dissimilar examples by mixing data samples differently either at the input or hidden-state levels. To demonstrate the effectiveness of DACL, we conduct experiments across various domains such as tabular data, images, and graphs. Our results show that DACL not only outperforms other domain-agnostic noising methods, such as Gaussian-noise, but also combines well with domain-specific methods, such as SimCLR, to improve self-supervised visual representation learning. Finally, we theoretically analyze our method and show advantages over the Gaussian-noise based contrastive learning approach.

</details>

### Neighborhood Contrastive Learning Applied to Online Patient Monitoring.
- **链接**: [arXiv:2106.05142](https://arxiv.org/abs/2106.05142)
- **作者**: Hugo Yèche, Gideon Dresdner, Francesco Locatello, Matthias Hüser, Gunnar Rätsch
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Intensive care units (ICU) are increasingly looking towards machine learning for methods to provide online monitoring of critically ill patients. In machine learning, online monitoring is often formulated as a supervised learning problem. Recently, contrastive learning approaches have demonstrated promising improvements over competitive supervised benchmarks. These methods rely on well-understood data augmentation techniques developed for image data which do not apply to online monitoring. In this work, we overcome this limitation by supplementing time-series data augmentation techniques with a novel contrastive learning objective which we call neighborhood contrastive learning (NCL). Our objective explicitly groups together contiguous time segments from each patient while maintaining state-specific information. Our experiments demonstrate a marked improvement over existing work applying contrastive methods to medical time-series.

</details>

### Graph Contrastive Learning Automated.
- **链接**: [出版页](http://proceedings.mlr.press/v139/you21a.html)
- **作者**: Yuning You, Tianlong Chen, Yang Shen, Zhangyang Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2021

### Contrastive Learning Inverts the Data Generating Process.
- **链接**: [arXiv:2102.08850](https://arxiv.org/abs/2102.08850)
- **作者**: Roland S. Zimmermann, Yash Sharma, Steffen Schneider, Matthias Bethge, Wieland Brendel
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Contrastive learning has recently seen tremendous success in self-supervised learning. So far, however, it is largely unclear why the learned representations generalize so effectively to a large variety of downstream tasks. We here prove that feedforward models trained with objectives belonging to the commonly used InfoNCE family learn to implicitly invert the underlying generative model of the observed data. While the proofs make certain statistical assumptions about the generative model, we observe empirically that our findings hold even if these assumptions are severely violated. Our theory highlights a fundamental connection between contrastive learning, generative modeling, and nonlinear independent component analysis, thereby furthering our understanding of the learned representations as well as providing a theoretical foundation to derive more effective contrastive losses.

</details>
