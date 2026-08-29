# Continual Learning — 2022 Guideline

> 领域: 持续学习 / 增量学习（含 VLM/多模态场景）
> 论文数: 29 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Meta-attention for ViT-backed Continual Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00025)
- **作者**: Mengqi Xue, Haofei Zhang, Jie Song, Mingli Song
- **🏷️ 机构**: ZJU
- **会议**: CVPR 2022

### vCLIMB: A Novel Video Class Incremental Learning Benchmark.
- **链接**: [arXiv:2201.09381](https://arxiv.org/abs/2201.09381) · 📚 被引 35
- **作者**: Andrés Villa, Kumail Alhamoud, Victor Escorcia, Fabian Caba Heilbron, Juan León Alcázar, Bernard Ghanem
- **🏷️ 机构**: Pontificia Universidad Cat&#x00F3;lica de Chile, King Abdullah University of Science and Technology (KAUST), Samsung AI Center Cambridge
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning (CL) is under-explored in the video domain. The few existing works contain splits with imbalanced class distributions over the tasks, or study the problem in unsuitable datasets. We introduce vCLIMB, a novel video continual learning benchmark. vCLIMB is a standardized test-bed to analyze catastrophic forgetting of deep models in video continual learning. In contrast to previous work, we focus on class incremental continual learning with models trained on a sequence of disjoint tasks, and distribute the number of classes uniformly across the tasks. We perform in-depth evaluations of existing CL methods in vCLIMB, and observe two unique challenges in video data. The selection of instances to store in episodic memory is performed at the frame level. Second, untrimmed training data influences the effectiveness of frame sampling strategies. We address these two challenges by proposing a temporal consistency regularization that can be applied on top of memory-based continual learning methods. Our approach significantly improves the baseline, by up to 24% on the untrimmed continual learning task.

</details>

### Overcoming Catastrophic Forgetting in Incremental Object Detection via Elastic Response Distillation.
- **链接**: [arXiv:2204.02136](https://arxiv.org/abs/2204.02136) · 📚 被引 117
- **作者**: Tao Feng, Mang Wang, Hangjie Yuan
- **🏷️ 机构**: Alibaba Group, Zhejiang University
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Traditional object detectors are ill-equipped for incremental learning. However, fine-tuning directly on a well-trained detection model with only new data will lead to catastrophic forgetting. Knowledge distillation is a flexible way to mitigate catastrophic forgetting. In Incremental Object Detection (IOD), previous work mainly focuses on distilling for the combination of features and responses. However, they under-explore the information that contains in responses. In this paper, we propose a response-based incremental distillation method, dubbed Elastic Response Distillation (ERD), which focuses on elastically learning responses from the classification head and the regression head. Firstly, our method transfers category knowledge while equipping student detector with the ability to retain localization information during incremental learning. In addition, we further evaluate the quality of all locations and provide valuable responses by the Elastic Response Selection (ERS) strategy. Finally, we elucidate that the knowledge from different responses should be assigned with different importance during incremental distillation. Extensive experiments conducted on MS COCO demonstrate our method achieves state-of-the-art result, which substantially narrows the performance gap towards full training.

</details>

### Continual Learning with Lifelong Vision Transformer.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00027)
- **作者**: Zhen Wang, Liu Liu, Yiqun Duan, Yajing Kong, Dacheng Tao
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2022

### Learning to Prompt for Continual Learning.
- **链接**: [arXiv:2112.08654](https://arxiv.org/abs/2112.08654) · [代码](https://github.com/google-research/l2p)
- **作者**: Zifeng Wang, Zizhao Zhang, Chen-Yu Lee, Han Zhang, Ruoxi Sun, Xiaoqi Ren et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The mainstream paradigm behind continual learning has been to adapt the model parameters to non-stationary data distributions, where catastrophic forgetting is the central challenge. Typical methods rely on a rehearsal buffer or known task identity at test time to retrieve learned knowledge and address forgetting, while this work presents a new paradigm for continual learning that aims to train a more succinct memory system without accessing task identity at test time. Our method learns to dynamically prompt (L2P) a pre-trained model to learn tasks sequentially under different task transitions. In our proposed framework, prompts are small learnable parameters, which are maintained in a memory space. The objective is to optimize prompts to instruct the model prediction and explicitly manage task-invariant and task-specific knowledge while maintaining model plasticity. We conduct comprehensive experiments under popular image classification benchmarks with different challenging continual learning settings, where L2P consistently outperforms prior state-of-the-art methods. Surprisingly, L2P achieves competitive results against rehearsal-based methods even without a rehearsal buffer and is directly applicable to challenging task-agnostic continual learning. Source code is available at https://github.com/google-research/l2p.

</details>

### Learning Bayesian Sparse Networks with Full Experience Replay for Continual Learning.
- **链接**: [arXiv:2202.10203](https://arxiv.org/abs/2202.10203) · 📚 被引 35
- **作者**: Qingsen Yan, Dong Gong, Yuhang Liu, Anton van den Hengel, Javen Qinfeng Shi
- **🏷️ 机构**: The Australian Institute for Machine Learning, The University of Adelaide,Australia
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual Learning (CL) methods aim to enable machine learning models to learn new tasks without catastrophic forgetting of those that have been previously mastered. Existing CL approaches often keep a buffer of previously-seen samples, perform knowledge distillation, or use regularization techniques towards this goal. Despite their performance, they still suffer from interference across tasks which leads to catastrophic forgetting. To ameliorate this problem, we propose to only activate and select sparse neurons for learning current and past tasks at any stage. More parameters space and model capacity can thus be reserved for the future tasks. This minimizes the interference between parameters for different tasks. To do so, we propose a Sparse neural Network for Continual Learning (SNCL), which employs variational Bayesian sparsity priors on the activations of the neurons in all layers. Full Experience Replay (FER) provides effective supervision in learning the sparse activations of the neurons in different layers. A loss-aware reservoir-sampling strategy is developed to maintain the memory buffer. The proposed method is agnostic as to the network structures and the task boundaries. Experiments on different datasets show that our approach achieves state-of-the-art performance for mitigating forgetting.

</details>

### Online Continual Learning on a Contaminated Data Stream with Blurry Task Boundaries.
- **链接**: [arXiv:2203.15355](https://arxiv.org/abs/2203.15355) · [代码](https://github.com/clovaai/puridiver) · 📚 被引 23
- **作者**: Jihwan Bang, Hyunseo Koh, Seulki Park, Hwanjun Song, Jung-Woo Ha, Jonghyun Choi
- **🏷️ 机构**: NAVER CLOVA, NAVER AI Lab
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Learning under a continuously changing data distribution with incorrect labels is a desirable real-world problem yet challenging. A large body of continual learning (CL) methods, however, assumes data streams with clean labels, and online learning scenarios under noisy data streams are yet underexplored. We consider a more practical CL task setup of an online learning from blurry data stream with corrupted labels, where existing CL methods struggle. To address the task, we first argue the importance of both diversity and purity of examples in the episodic memory of continual learning models. To balance diversity and purity in the episodic memory, we propose a novel strategy to manage and use the memory by a unified approach of label noise aware diverse sampling and robust learning with semi-supervised learning. Our empirical validations on four real-world or synthetic noise datasets (CIFAR10 and 100, mini-WebVision, and Food-101N) exhibit that our method significantly outperforms prior arts in this realistic and challenging continual learning scenario. Code and data splits are available in https://github.com/clovaai/puridiver.

</details>

### Probing Representation Forgetting in Supervised and Unsupervised Continual Learning.
- **链接**: [arXiv:2203.13381](https://arxiv.org/abs/2203.13381) · 📚 被引 46
- **作者**: MohammadReza Davari, Nader Asadi, Sudhir P. Mudur, Rahaf Aljundi, Eugene Belilovsky
- **🏷️ 机构**: Concordia University, Toyota Motor Europe
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual Learning research typically focuses on tackling the phenomenon of catastrophic forgetting in neural networks. Catastrophic forgetting is associated with an abrupt loss of knowledge previously learned by a model when the task, or more broadly the data distribution, being trained on changes. In supervised learning problems this forgetting, resulting from a change in the model's representation, is typically measured or observed by evaluating the decrease in old task performance. However, a model's representation can change without losing knowledge about prior tasks. In this work we consider the concept of representation forgetting, observed by using the difference in performance of an optimal linear classifier before and after a new task is introduced. Using this tool we revisit a number of standard continual learning benchmarks and observe that, through this lens, model representations trained without any explicit control for forgetting often experience small representation forgetting and can sometimes be comparable to methods which explicitly control for forgetting, especially in longer task sequences. We also show that representation forgetting can lead to new insights on the effect of model capacity and loss function used in continual learning. Based on our results, we show that a simple yet competitive approach is to learn representations continually with standard supervised contrastive learning while constructing prototypes of class samples when queried on old samples.

</details>

### DyTox: Transformers for Continual Learning with DYnamic TOken eXpansion.
- **链接**: [arXiv:2111.11326](https://arxiv.org/abs/2111.11326) · 📚 被引 319
- **作者**: Arthur Douillard, Alexandre Ramé, Guillaume Couairon, Matthieu Cord
- **🏷️ 机构**: Sorbonne Universite
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep network architectures struggle to continually learn new tasks without forgetting the previous tasks. A recent trend indicates that dynamic architectures based on an expansion of the parameters can reduce catastrophic forgetting efficiently in continual learning. However, existing approaches often require a task identifier at test-time, need complex tuning to balance the growing number of parameters, and barely share any information across tasks. As a result, they struggle to scale to a large number of tasks without significant overhead. In this paper, we propose a transformer architecture based on a dedicated encoder/decoder framework. Critically, the encoder and decoder are shared among all tasks. Through a dynamic expansion of special tokens, we specialize each forward of our decoder network on a task distribution. Our strategy scales to a large number of tasks while having negligible memory and time overheads due to strict control of the parameters expansion. Moreover, this efficient strategy doesn't need any hyperparameter tuning to control the network's expansion. Our model reaches excellent results on CIFAR100 and state-of-the-art performances on the large-scale ImageNet100 and ImageNet1000 while having less parameters than concurrent dynamic frameworks.

</details>

### Not Just Selection, but Exploration: Online Class-Incremental Continual Learning via Dual View Consistency.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00729) · 📚 被引 73
- **作者**: Yanan Gu, Xu Yang, Kun Wei, Cheng Deng
- **🏷️ 机构**: School of Electronic Engineering, Xidian University,Xi&#x0027;an,China,710071
- **会议**: CVPR 2022

### On Generalizing Beyond Domains in Cross-Domain Continual Learning.
- **链接**: [arXiv:2203.03970](https://arxiv.org/abs/2203.03970) · 📚 被引 30
- **作者**: Christian Simon, Masoud Faraki, Yi-Hsuan Tsai, Xiang Yu, Samuel Schulter, Yumin Suh et al.
- **🏷️ 机构**: The Australian National University, Phiar Technologies, Monash University
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Humans have the ability to accumulate knowledge of new tasks in varying conditions, but deep neural networks often suffer from catastrophic forgetting of previously learned knowledge after learning a new task. Many recent methods focus on preventing catastrophic forgetting under the assumption of train and test data following similar distributions. In this work, we consider a more realistic scenario of continual learning under domain shifts where the model must generalize its inference to an unseen domain. To this end, we encourage learning semantically meaningful features by equipping the classifier with class similarity metrics as learning parameters which are obtained through Mahalanobis similarity computations. Learning of the backbone representation along with these extra parameters is done seamlessly in an end-to-end manner. In addition, we propose an approach based on the exponential moving average of the parameters for better knowledge distillation. We demonstrate that, to a great extent, existing continual learning algorithms fail to handle the forgetting issue under multiple distributions, while our proposed approach learns new tasks under domain shift with accuracy boosts up to 10% on challenging datasets such as DomainNet and OfficeHome.

</details>

### GCR: Gradient Coreset based Replay Buffer Selection for Continual Learning.
- **链接**: [arXiv:2111.11210](https://arxiv.org/abs/2111.11210) · 📚 被引 105
- **作者**: Rishabh Tiwari, KrishnaTeja Killamsetty, Rishabh K. Iyer, Pradeep Shenoy
- **🏷️ 机构**: Indian Institute of Technology (ISM),Department of Physics,Dhanbad, University of Texas at Dallas,Department of Computer Science, Google Research,India
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning (CL) aims to develop techniques by which a single model adapts to an increasing number of tasks encountered sequentially, thereby potentially leveraging learnings across tasks in a resource-efficient manner. A major challenge for CL systems is catastrophic forgetting, where earlier tasks are forgotten while learning a new task. To address this, replay-based CL approaches maintain and repeatedly retrain on a small buffer of data selected across encountered tasks. We propose Gradient Coreset Replay (GCR), a novel strategy for replay buffer selection and update using a carefully designed optimization criterion. Specifically, we select and maintain a "coreset" that closely approximates the gradient of all the data seen so far with respect to current model parameters, and discuss key strategies needed for its effective application to the continual learning setting. We show significant gains (2%-4% absolute) over the state-of-the-art in the well-studied offline continual learning setting. Our findings also effectively transfer to online / streaming CL settings, showing upto 5% gains over existing approaches. Finally, we demonstrate the value of supervised contrastive loss for continual learning, which yields a cumulative gain of up to 5% accuracy when combined with our subset selection strategy.

</details>

### Continual Learning for Visual Search with Backward Consistent Feature Embedding.
- **链接**: [arXiv:2205.13384](https://arxiv.org/abs/2205.13384) · 📚 被引 27
- **作者**: Timmy S. T. Wan, Jun-Cheng Chen, Tzer-Yi Wu, Chu-Song Chen
- **🏷️ 机构**: National Taiwan University, Academia Sinica, Ucfunnel Co. Ltd.
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In visual search, the gallery set could be incrementally growing and added to the database in practice. However, existing methods rely on the model trained on the entire dataset, ignoring the continual updating of the model. Besides, as the model updates, the new model must re-extract features for the entire gallery set to maintain compatible feature space, imposing a high computational cost for a large gallery set. To address the issues of long-term visual search, we introduce a continual learning (CL) approach that can handle the incrementally growing gallery set with backward embedding consistency. We enforce the losses of inter-session data coherence, neighbor-session model coherence, and intra-session discrimination to conduct a continual learner. In addition to the disjoint setup, our CL solution also tackles the situation of increasingly adding new classes for the blurry boundary without assuming all categories known in the beginning and during model update. To our knowledge, this is the first CL method both tackling the issue of backward-consistent feature embedding and allowing novel classes to occur in the new sessions. Extensive experiments on various benchmarks show the efficacy of our approach under a wide range of setups.

</details>

### MetaFSCIL: A Meta-Learning Approach for Few-Shot Class Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01377) · 📚 被引 155
- **作者**: Zhixiang Chi, Li Gu, Huan Liu, Yang Wang, Yuanhao Yu, Jin Tang
- **🏷️ 机构**: Noah&#x0027;s Ark Lab, Huawei Technologies
- **会议**: CVPR 2022

### Learning to Imagine: Diversify Memory for Incremental Learning using Unlabeled Data.
- **链接**: [arXiv:2204.08932](https://arxiv.org/abs/2204.08932) · 📚 被引 38
- **作者**: Yu-Ming Tang, Yi-Xing Peng, Wei-Shi Zheng
- **🏷️ 机构**: Sun Yat-sen University,School of Computer Science and Engineering,China
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep neural network (DNN) suffers from catastrophic forgetting when learning incrementally, which greatly limits its applications. Although maintaining a handful of samples (called `exemplars`) of each task could alleviate forgetting to some extent, existing methods are still limited by the small number of exemplars since these exemplars are too few to carry enough task-specific knowledge, and therefore the forgetting remains. To overcome this problem, we propose to `imagine` diverse counterparts of given exemplars referring to the abundant semantic-irrelevant information from unlabeled data. Specifically, we develop a learnable feature generator to diversify exemplars by adaptively generating diverse counterparts of exemplars based on semantic information from exemplars and semantically-irrelevant information from unlabeled data. We introduce semantic contrastive learning to enforce the generated samples to be semantic consistent with exemplars and perform semanticdecoupling contrastive learning to encourage diversity of generated samples. The diverse generated samples could effectively prevent DNN from forgetting when learning new tasks. Our method does not bring any extra inference cost and outperforms state-of-the-art methods on two benchmarks CIFAR-100 and ImageNet-Subset by a clear margin.

</details>

### Forward Compatible Few-Shot Class-Incremental Learning.
- **链接**: [arXiv:2203.06953](https://arxiv.org/abs/2203.06953) · [代码](https://github.com/zhoudw-zdw/CVPR22-Fact)
- **作者**: Da-Wei Zhou, Fu-Yun Wang, Han-Jia Ye, Liang Ma, Shiliang Pu, De-Chuan Zhan
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Novel classes frequently arise in our dynamically changing world, e.g., new users in the authentication system, and a machine learning model should recognize new classes without forgetting old ones. This scenario becomes more challenging when new class instances are insufficient, which is called few-shot class-incremental learning (FSCIL). Current methods handle incremental learning retrospectively by making the updated model similar to the old one. By contrast, we suggest learning prospectively to prepare for future updates, and propose ForwArd Compatible Training (FACT) for FSCIL. Forward compatibility requires future new classes to be easily incorporated into the current model based on the current stage data, and we seek to realize it by reserving embedding space for future new classes. In detail, we assign virtual prototypes to squeeze the embedding of known classes and reserve for new ones. Besides, we forecast possible new classes and prepare for the updating process. The virtual prototypes allow the model to accept possible updates in the future, which act as proxies scattered among embedding space to build a stronger classifier during inference. FACT efficiently incorporates new classes with forward compatibility and meanwhile resists forgetting of old ones. Extensive experiments validate FACT's state-of-the-art performance. Code is available at: https://github.com/zhoudw-zdw/CVPR22-Fact

</details>

### Self-Sustaining Representation Expansion for Non-Exemplar Class-Incremental Learning.
- **链接**: [arXiv:2203.06359](https://arxiv.org/abs/2203.06359) · 📚 被引 153
- **作者**: Kai Zhu, Wei Zhai, Yang Cao, Jiebo Luo, Zhengjun Zha
- **🏷️ 机构**: University of Science and Technology of China, University of Rochester
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Non-exemplar class-incremental learning is to recognize both the old and new classes when old class samples cannot be saved. It is a challenging task since representation optimization and feature retention can only be achieved under supervision from new classes. To address this problem, we propose a novel self-sustaining representation expansion scheme. Our scheme consists of a structure reorganization strategy that fuses main-branch expansion and side-branch updating to maintain the old features, and a main-branch distillation scheme to transfer the invariant knowledge. Furthermore, a prototype selection mechanism is proposed to enhance the discrimination between the old and new classes by selectively incorporating new samples into the distillation process. Extensive experiments on three benchmarks demonstrate significant incremental performance, outperforming the state-of-the-art methods by a margin of 3%, 3% and 6%, respectively.

</details>

### Doodle It Yourself: Class Incremental Learning by Drawing a Few Sketches.
- **链接**: [arXiv:2203.14843](https://arxiv.org/abs/2203.14843) · 📚 被引 26
- **作者**: Ayan Kumar Bhunia, Viswanatha Reddy Gajjala, Subhadeep Koley, Rohit Kundu, Aneeshan Sain, Tao Xiang et al.
- **🏷️ 机构**: University of Surrey,SketchX, CVSSP,United Kingdom
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The human visual system is remarkable in learning new visual concepts from just a few examples. This is precisely the goal behind few-shot class incremental learning (FSCIL), where the emphasis is additionally placed on ensuring the model does not suffer from "forgetting". In this paper, we push the boundary further for FSCIL by addressing two key questions that bottleneck its ubiquitous application (i) can the model learn from diverse modalities other than just photo (as humans do), and (ii) what if photos are not readily accessible (due to ethical and privacy constraints). Our key innovation lies in advocating the use of sketches as a new modality for class support. The product is a "Doodle It Yourself" (DIY) FSCIL framework where the users can freely sketch a few examples of a novel class for the model to learn to recognize photos of that class. For that, we present a framework that infuses (i) gradient consensus for domain invariant learning, (ii) knowledge distillation for preserving old class information, and (iii) graph attention networks for message passing between old and novel classes. We experimentally show that sketches are better class support than text in the context of FSCIL, echoing findings elsewhere in the sketching literature.

</details>

### Incremental Learning in Semantic Segmentation from Image Labels.
- **链接**: [arXiv:2112.01882](https://arxiv.org/abs/2112.01882) · [代码](https://github.com/fcdl94/WILSON) · 📚 被引 58
- **作者**: Fabio Cermelli, Dario Fontanel, Antonio Tavera, Marco Ciccone, Barbara Caputo
- **🏷️ 机构**: Politecnico di Torino
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Although existing semantic segmentation approaches achieve impressive results, they still struggle to update their models incrementally as new categories are uncovered. Furthermore, pixel-by-pixel annotations are expensive and time-consuming. This paper proposes a novel framework for Weakly Incremental Learning for Semantic Segmentation, that aims at learning to segment new classes from cheap and largely available image-level labels. As opposed to existing approaches, that need to generate pseudo-labels offline, we use an auxiliary classifier, trained with image-level labels and regularized by the segmentation model, to obtain pseudo-supervision online and update the model incrementally. We cope with the inherent noise in the process by using soft-labels generated by the auxiliary classifier. We demonstrate the effectiveness of our approach on the Pascal VOC and COCO datasets, outperforming offline weakly-supervised methods and obtaining results comparable with incremental learning methods with full supervision. Code can be found at https://github.com/fcdl94/WILSON.

</details>

### Few-Shot Incremental Learning for Label-to-Image Translation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00368) · 📚 被引 9
- **作者**: Pei Chen, Yangkang Zhang, Zejian Li, Lingyun Sun
- **🏷️ 机构**: Alibaba-Zhejiang University Joint Institute of Frontier Technologies, Zhejiang University
- **会议**: CVPR 2022

### Federated Class-Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00992)
- **作者**: Jiahua Dong, Lixu Wang, Zhen Fang, Gan Sun, Shichao Xu, Xiao Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2022

### Constrained Few-shot Class-incremental Learning.
- **链接**: [arXiv:2203.16588](https://arxiv.org/abs/2203.16588) · [代码](https://github.com/IBM/constrained-FSCIL)
- **作者**: Michael Hersche, Geethan Karunaratne, Giovanni Cherubini, Luca Benini, Abu Sebastian, Abbas Rahimi
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continually learning new classes from fresh data without forgetting previous knowledge of old classes is a very challenging research problem. Moreover, it is imperative that such learning must respect certain memory and computational constraints such as (i) training samples are limited to only a few per class, (ii) the computational cost of learning a novel class remains constant, and (iii) the memory footprint of the model grows at most linearly with the number of classes observed. To meet the above constraints, we propose C-FSCIL, which is architecturally composed of a frozen meta-learned feature extractor, a trainable fixed-size fully connected layer, and a rewritable dynamically growing memory that stores as many vectors as the number of encountered classes. C-FSCIL provides three update modes that offer a trade-off between accuracy and compute-memory cost of learning novel classes. C-FSCIL exploits hyperdimensional embedding that allows to continually express many more classes than the fixed dimensions in the vector space, with minimal interference. The quality of class vector representations is further improved by aligning them quasi-orthogonally to each other by means of novel loss functions. Experiments on the CIFAR100, miniImageNet, and Omniglot datasets show that C-FSCIL outperforms the baselines with remarkable accuracy and compression. It also scales up to the largest problem size ever tried in this few-shot setting by learning 423 novel classes on top of 1200 base classes with less than 1.6% accuracy drop. Our code is available at https://github.com/IBM/constrained-FSCIL.

</details>

### Energy-based Latent Aligner for Incremental Learning.
- **链接**: [arXiv:2203.14952](https://arxiv.org/abs/2203.14952) · 📚 被引 37
- **作者**: K. J. Joseph, Salman Khan, Fahad Shahbaz Khan, Rao Muhammad Anwer, Vineeth N. Balasubramanian
- **🏷️ 机构**: Indian Institute of Technology,Hyderabad,India, Mohamed bin Zayed University of AI,UAE
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep learning models tend to forget their earlier knowledge while incrementally learning new tasks. This behavior emerges because the parameter updates optimized for the new tasks may not align well with the updates suitable for older tasks. The resulting latent representation mismatch causes forgetting. In this work, we propose ELI: Energy-based Latent Aligner for Incremental Learning, which first learns an energy manifold for the latent representations such that previous task latents will have low energy and the current task latents have high energy values. This learned manifold is used to counter the representational shift that happens during incremental learning. The implicit regularization that is offered by our proposed methodology can be used as a plug-and-play module in existing incremental learning methodologies. We validate this through extensive evaluation on CIFAR-100, ImageNet subset, ImageNet 1k and Pascal VOC datasets. We observe consistent improvement when ELI is added to three prominent methodologies in class-incremental learning, across multiple incremental settings. Further, when added to the state-of-the-art incremental object detector, ELI provides over 5% improvement in detection accuracy, corroborating its effectiveness and complementary advantage to existing art.

</details>

### Class-Incremental Learning by Knowledge Distillation with Adaptive Feature Consolidation.
- **链接**: [arXiv:2204.00895](https://arxiv.org/abs/2204.00895) · 📚 被引 197
- **作者**: Minsoo Kang, Jaeyoo Park, Bohyung Han
- **🏷️ 机构**: ECE, ASRI, &#x0026; IPAI, Seoul National University
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a novel class incremental learning approach based on deep neural networks, which continually learns new tasks with limited memory for storing examples in the previous tasks. Our algorithm is based on knowledge distillation and provides a principled way to maintain the representations of old models while adjusting to new tasks effectively. The proposed method estimates the relationship between the representation changes and the resulting loss increases incurred by model updates. It minimizes the upper bound of the loss increases using the representations, which exploits the estimated importance of each feature map within a backbone model. Based on the importance, the model restricts updates of important features for robustness while allowing changes in less critical features for flexibility. This optimization strategy effectively alleviates the notorious catastrophic forgetting problem despite the limited accessibility of data in the previous tasks. The experimental results show significant accuracy improvement of the proposed algorithm over the existing methods on the standard datasets. Code is available.

</details>

### Towards Better Plasticity-Stability Trade-off in Incremental Learning: A Simple Linear Connector.
- **链接**: [arXiv:2110.07905](https://arxiv.org/abs/2110.07905) · [代码](https://github.com/lingl1024/Connector) · 📚 被引 52
- **作者**: Guoliang Lin, Hanlu Chu, Hanjiang Lai
- **🏷️ 机构**: Sun Yat-sen University,Guangdong,China, South China Normal University,Guangdong,China
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Plasticity-stability dilemma is a main problem for incremental learning, where plasticity is referring to the ability to learn new knowledge, and stability retains the knowledge of previous tasks. Many methods tackle this problem by storing previous samples, while in some applications, training data from previous tasks cannot be legally stored. In this work, we propose to employ mode connectivity in loss landscapes to achieve better plasticity-stability trade-off without any previous samples. We give an analysis of why and how to connect two independently optimized optima of networks, null-space projection for previous tasks and simple SGD for the current task, can attain a meaningful balance between preserving already learned knowledge and granting sufficient flexibility for learning a new task. This analysis of mode connectivity also provides us a new perspective and technology to control the trade-off between plasticity and stability. We evaluate the proposed method on several benchmark datasets. The results indicate our simple method can achieve notable improvement, and perform well on both the past and current tasks. On 10-split-CIFAR-100 task, our method achieves 79.79% accuracy, which is 6.02% higher. Our method also achieves 6.33% higher accuracy on TinyImageNet. Code is available at https://github.com/lingl1024/Connector.

</details>

### Mimicking the Oracle: An Initial Phase Decorrelation Approach for Class Incremental Learning.
- **链接**: [arXiv:2112.04731](https://arxiv.org/abs/2112.04731) · 📚 被引 61
- **作者**: Yujun Shi, Kuangqi Zhou, Jian Liang, Zihang Jiang, Jiashi Feng, Philip H. S. Torr et al.
- **🏷️ 机构**: National University of Singapore, Institute of Automation, Chinese Academy of Sciences (CAS), ByteDance Inc
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Class Incremental Learning (CIL) aims at learning a multi-class classifier in a phase-by-phase manner, in which only data of a subset of the classes are provided at each phase. Previous works mainly focus on mitigating forgetting in phases after the initial one. However, we find that improving CIL at its initial phase is also a promising direction. Specifically, we experimentally show that directly encouraging CIL Learner at the initial phase to output similar representations as the model jointly trained on all classes can greatly boost the CIL performance. Motivated by this, we study the difference between a naïvely-trained initial-phase model and the oracle model. Specifically, since one major difference between these two models is the number of training classes, we investigate how such difference affects the model representations. We find that, with fewer training classes, the data representations of each class lie in a long and narrow region; with more training classes, the representations of each class scatter more uniformly. Inspired by this observation, we propose Class-wise Decorrelation (CwD) that effectively regularizes representations of each class to scatter more uniformly, thus mimicking the model jointly trained with all classes (i.e., the oracle model). Our CwD is simple to implement and easy to plug into existing methods. Extensive experiments on various benchmark datasets show that CwD consistently and significantly improves the performance of existing state-of-the-art methods by around 1\% to 3\%. Code will be released.

</details>

### Bring Evanescent Representations to Life in Lifelong Class Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01623) · 📚 被引 36
- **作者**: Marco Toldo, Mete Ozay
- **🏷️ 机构**: Samsung Research UK
- **会议**: CVPR 2022

### Class-Incremental Learning with Strong Pre-trained Models.
- **链接**: [arXiv:2204.03634](https://arxiv.org/abs/2204.03634) · [代码](https://github.com/amazon-research/sp-cil) · 📚 被引 65
- **作者**: Tz-Ying Wu, Gurumurthy Swaminathan, Zhizhong Li, Avinash Ravichandran, Nuno Vasconcelos, Rahul Bhotika et al.
- **🏷️ 机构**: AWS AI Labs, UC San Diego
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Class-incremental learning (CIL) has been widely studied under the setting of starting from a small number of classes (base classes). Instead, we explore an understudied real-world setting of CIL that starts with a strong model pre-trained on a large number of base classes. We hypothesize that a strong base model can provide a good representation for novel classes and incremental learning can be done with small adaptations. We propose a 2-stage training scheme, i) feature augmentation -- cloning part of the backbone and fine-tuning it on the novel data, and ii) fusion -- combining the base and novel classifiers into a unified classifier. Experiments show that the proposed method significantly outperforms state-of-the-art CIL methods on the large-scale ImageNet dataset (e.g. +10% overall accuracy than the best). We also propose and analyze understudied practical CIL scenarios, such as base-novel overlap with distribution shift. Our proposed method is robust and generalizes to all analyzed CIL settings. Code is available at https://github.com/amazon-research/sp-cil.

</details>

### General Incremental Learning with Domain-aware Categorical Representations.
- **链接**: [arXiv:2204.04078](https://arxiv.org/abs/2204.04078) · 📚 被引 34
- **作者**: Jiangwei Xie, Shipeng Yan, Xuming He
- **🏷️ 机构**: School of Information Science and Technology, ShanghaiTech University
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning is an important problem for achieving human-level intelligence in real-world applications as an agent must continuously accumulate knowledge in response to streaming data/tasks. In this work, we consider a general and yet under-explored incremental learning problem in which both the class distribution and class-specific domain distribution change over time. In addition to the typical challenges in class incremental learning, this setting also faces the intra-class stability-plasticity dilemma and intra-class domain imbalance problems. To address above issues, we develop a novel domain-aware continual learning method based on the EM framework. Specifically, we introduce a flexible class representation based on the von Mises-Fisher mixture model to capture the intra-class structure, using an expansion-and-reduction strategy to dynamically increase the number of components according to the class complexity. Moreover, we design a bi-level balanced memory to cope with data imbalances within and across classes, which combines with a distillation loss to achieve better inter- and intra-class stability-plasticity trade-off. We conduct exhaustive experiments on three benchmarks: iDigits, iDomainNet and iCIFAR-20. The results show that our approach consistently outperforms previous methods by a significant margin, demonstrating its superiority.

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
