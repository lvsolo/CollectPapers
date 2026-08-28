# Continual Learning — 2023 Guideline

> 领域: 持续学习 / 增量学习（含 VLM/多模态场景）
> 论文数: 17 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Fairness Continual Learning Approach to Semantic Scene Understanding in Open-World Environments.
- **链接**: [arXiv:2305.15700](https://arxiv.org/abs/2305.15700) · 📚 被引 3
- **作者**: Thanh-Dat Truong, Hoang-Quan Nguyen, Bhiksha Raj, Khoa Luu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual semantic segmentation aims to learn new classes while maintaining the information from the previous classes. Although prior studies have shown impressive progress in recent years, the fairness concern in the continual semantic segmentation needs to be better addressed. Meanwhile, fairness is one of the most vital factors in deploying the deep learning model, especially in human-related or safety applications. In this paper, we present a novel Fairness Continual Learning approach to the semantic segmentation problem. In particular, under the fairness objective, a new fairness continual learning framework is proposed based on class distributions. Then, a novel Prototypical Contrastive Clustering loss is proposed to address the significant challenges in continual learning, i.e., catastrophic forgetting and background shift. Our proposed loss has also been proven as a novel, generalized learning paradigm of knowledge distillation commonly used in continual learning. Moreover, the proposed Conditional Structural Consistency loss further regularized the structural constraint of the predicted segmentation. Our proposed approach has achieved State-of-the-Art performance on three standard scene understanding benchmarks, i.e., ADE20K, Cityscapes, and Pascal VOC, and promoted the fairness of the segmentation model.

</details>

### Augmented Memory Replay-based Continual Learning Approaches for Network Intrusion Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/3755a02b1035fbadd5f93a022170e46f-Abstract-Conference.html) · 📚 被引 9
- **作者**: Suresh Kumar Amalapuram, Sumohana S. Channappayya, Bheemarjuna Reddy Tamma
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### FeCAM: Exploiting the Heterogeneity of Class Distributions in Exemplar-Free Continual Learning.
- **链接**: [arXiv:2309.14062](https://arxiv.org/abs/2309.14062) · [代码](https://github.com/dipamgoswami/FeCAM)
- **作者**: Dipam Goswami, Yuyang Liu, Bartlomiej Twardowski, Joost van de Weijer
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Exemplar-free class-incremental learning (CIL) poses several challenges since it prohibits the rehearsal of data from previous tasks and thus suffers from catastrophic forgetting. Recent approaches to incrementally learning the classifier by freezing the feature extractor after the first task have gained much attention. In this paper, we explore prototypical networks for CIL, which generate new class prototypes using the frozen feature extractor and classify the features based on the Euclidean distance to the prototypes. In an analysis of the feature distributions of classes, we show that classification based on Euclidean metrics is successful for jointly trained features. However, when learning from non-stationary data, we observe that the Euclidean metric is suboptimal and that feature distributions are heterogeneous. To address this challenge, we revisit the anisotropic Mahalanobis distance for CIL. In addition, we empirically show that modeling the feature covariance relations is better than previous attempts at sampling features from normal distributions and training a linear classifier. Unlike existing methods, our approach generalizes to both many- and few-shot CIL settings, as well as to domain-incremental settings. Interestingly, without updating the backbone network, our method obtains state-of-the-art results on several standard continual learning benchmarks. Code is available at https://github.com/dipamgoswami/FeCAM.

</details>

### Bilevel Coreset Selection in Continual Learning: A New Formulation and Algorithm.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/a0251e494a7e75d59e06d37e646f46b7-Abstract-Conference.html)
- **作者**: Jie Hao, Kaiyi Ji, Mingrui Liu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Selective Amnesia: A Continual Learning Approach to Forgetting in Deep Generative Models.
- **链接**: [arXiv:2305.10120](https://arxiv.org/abs/2305.10120) · [代码](https://github.com/clear-nus/selective-amnesia)
- **作者**: Alvin Heng, Harold Soh
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The recent proliferation of large-scale text-to-image models has led to growing concerns that such models may be misused to generate harmful, misleading, and inappropriate content. Motivated by this issue, we derive a technique inspired by continual learning to selectively forget concepts in pretrained deep generative models. Our method, dubbed Selective Amnesia, enables controllable forgetting where a user can specify how a concept should be forgotten. Selective Amnesia can be applied to conditional variational likelihood models, which encompass a variety of popular deep generative frameworks, including variational autoencoders and large-scale text-to-image diffusion models. Experiments across different models demonstrate that our approach induces forgetting on a variety of concepts, from entire classes in standard datasets to celebrity and nudity prompts in text-to-image models. Our code is publicly available at https://github.com/clear-nus/selective-amnesia.

</details>

### NPCL: Neural Processes for Uncertainty-Aware Continual Learning.
- **链接**: [arXiv:2310.19272](https://arxiv.org/abs/2310.19272) · [代码](https://github.com/srvCodes/NPCL) · 📚 被引 1
- **作者**: Saurav Jha, Dong Gong, He Zhao, Lina Yao
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning (CL) aims to train deep neural networks efficiently on streaming data while limiting the forgetting caused by new tasks. However, learning transferable knowledge with less interference between tasks is difficult, and real-world deployment of CL models is limited by their inability to measure predictive uncertainties. To address these issues, we propose handling CL tasks with neural processes (NPs), a class of meta-learners that encode different tasks into probabilistic distributions over functions all while providing reliable uncertainty estimates. Specifically, we propose an NP-based CL approach (NPCL) with task-specific modules arranged in a hierarchical latent variable model. We tailor regularizers on the learned latent distributions to alleviate forgetting. The uncertainty estimation capabilities of the NPCL can also be used to handle the task head/module inference challenge in CL. Our experiments show that the NPCL outperforms previous CL approaches. We validate the effectiveness of uncertainty estimation in the NPCL for identifying novel data and evaluating instance-level model confidence. Code is available at \url{https://github.com/srvCodes/NPCL}.

</details>

### CLeAR: Continual Learning on Algorithmic Reasoning for Human-like Intelligence.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/986e0caad271b59417287737416d8594-Abstract-Conference.html) · 📚 被引 0
- **作者**: Bong Gyun Kang, HyunGi Kim, Dahuin Jung, Sungroh Yoon
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Recasting Continual Learning as Sequence Modeling.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/dee254cdacbab59f17dc6a8fbdffa59f-Abstract-Conference.html)
- **作者**: Soochan Lee, Jaehyeon Son, Gunhee Kim
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Loss Decoupling for Task-Agnostic Continual Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/249f73e01f0a2bb6c8d971b565f159a7-Abstract-Conference.html) · 📚 被引 2
- **作者**: Yan-Shuo Liang, Wu-Jun Li
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Does Continual Learning Meet Compositionality? New Benchmarks and An Evaluation Framework.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/6a42b45af2b72e6e5b5e3a6fe695809f-Abstract-Datasets_and_Benchmarks.html) · 📚 被引 0
- **作者**: Weiduo Liao, Ying Wei, Mingchen Jiang, Qingfu Zhang, Hisao Ishibuchi
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Overcoming Recency Bias of Normalization Statistics in Continual Learning: Balance and Adaptation.
- **链接**: [arXiv:2310.08855](https://arxiv.org/abs/2310.08855) · [代码](https://github.com/lvyilin/AdaB2N) · 📚 被引 3
- **作者**: Yilin Lyu, Liyuan Wang, Xingxing Zhang, Zicheng Sun, Hang Su, Jun Zhu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning entails learning a sequence of tasks and balancing their knowledge appropriately. With limited access to old training samples, much of the current work in deep neural networks has focused on overcoming catastrophic forgetting of old tasks in gradient-based optimization. However, the normalization layers provide an exception, as they are updated interdependently by the gradient and statistics of currently observed training samples, which require specialized strategies to mitigate recency bias. In this work, we focus on the most popular Batch Normalization (BN) and provide an in-depth theoretical analysis of its sub-optimality in continual learning. Our analysis demonstrates the dilemma between balance and adaptation of BN statistics for incremental tasks, which potentially affects training stability and generalization. Targeting on these particular challenges, we propose Adaptive Balance of BN (AdaB$^2$N), which incorporates appropriately a Bayesian-based strategy to adapt task-wise contributions and a modified momentum to balance BN statistics, corresponding to the training and testing stages. By implementing BN in a continual learning fashion, our approach achieves significant performance gains across a wide range of benchmarks, particularly for the challenging yet realistic online scenarios (e.g., up to 7.68%, 6.86% and 4.26% on Split CIFAR-10, Split CIFAR-100 and Split Mini-ImageNet, respectively). Our code is available at https://github.com/lvyilin/AdaB2N.

</details>

### RanPAC: Random Projections and Pre-trained Models for Continual Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/2793dc35e14003dd367684d93d236847-Abstract-Conference.html)
- **作者**: Mark D. McDonnell, Dong Gong, Amin Parvaneh, Ehsan Abbasnejad, Anton van den Hengel
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Continual Learning for Instruction Following from Realtime Feedback.
- **链接**: [arXiv:2212.09710](https://arxiv.org/abs/2212.09710)
- **作者**: Alane Suhr, Yoav Artzi
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose and deploy an approach to continually train an instruction-following agent from feedback provided by users during collaborative interactions. During interaction, human users instruct an agent using natural language, and provide realtime binary feedback as they observe the agent following their instructions. We design a contextual bandit learning approach, converting user feedback to immediate reward. We evaluate through thousands of human-agent interactions, demonstrating 15.4% absolute improvement in instruction execution accuracy over time. We also show our approach is robust to several design variations, and that the feedback signal is roughly equivalent to the learning signal of supervised demonstration data.

</details>

### Temporal Continual Learning with Prior Compensation for Human Motion Prediction.
- **链接**: [arXiv:2507.04060](https://arxiv.org/abs/2507.04060) · [代码](https://github.com/hyqlat/TCL) · 📚 被引 0
- **作者**: Jianwei Tang, Jiangxin Sun, Xiaotong Lin, Lifang Zhang, Wei-Shi Zheng, Jian-Fang Hu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Human Motion Prediction (HMP) aims to predict future poses at different moments according to past motion sequences. Previous approaches have treated the prediction of various moments equally, resulting in two main limitations: the learning of short-term predictions is hindered by the focus on long-term predictions, and the incorporation of prior information from past predictions into subsequent predictions is limited. In this paper, we introduce a novel multi-stage training framework called Temporal Continual Learning (TCL) to address the above challenges. To better preserve prior information, we introduce the Prior Compensation Factor (PCF). We incorporate it into the model training to compensate for the lost prior information. Furthermore, we derive a more reasonable optimization objective through theoretical derivation. It is important to note that our TCL framework can be easily integrated with different HMP backbone models and adapted to various datasets and applications. Extensive experiments on four HMP benchmark datasets demonstrate the effectiveness and flexibility of TCL. The code is available at https://github.com/hyqlat/TCL.

</details>

### Hierarchical Decomposition of Prompt-Based Continual Learning: Rethinking Obscured Sub-optimality.
- **链接**: [arXiv:2310.07234](https://arxiv.org/abs/2310.07234) · [代码](https://github.com/thu-ml/HiDe-Prompt) · 📚 被引 17
- **作者**: Liyuan Wang, Jingyi Xie, Xingxing Zhang, Mingyi Huang, Hang Su, Jun Zhu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Prompt-based continual learning is an emerging direction in leveraging pre-trained knowledge for downstream continual learning, and has almost reached the performance pinnacle under supervised pre-training. However, our empirical research reveals that the current strategies fall short of their full potential under the more realistic self-supervised pre-training, which is essential for handling vast quantities of unlabeled data in practice. This is largely due to the difficulty of task-specific knowledge being incorporated into instructed representations via prompt parameters and predicted by uninstructed representations at test time. To overcome the exposed sub-optimality, we conduct a theoretical analysis of the continual learning objective in the context of pre-training, and decompose it into hierarchical components: within-task prediction, task-identity inference, and task-adaptive prediction. Following these empirical and theoretical insights, we propose Hierarchical Decomposition (HiDe-)Prompt, an innovative approach that explicitly optimizes the hierarchical components with an ensemble of task-specific prompts and statistics of both uninstructed and instructed representations, further with the coordination of a contrastive regularization strategy. Our extensive experiments demonstrate the superior performance of HiDe-Prompt and its robustness to pre-training paradigms in continual learning (e.g., up to 15.01% and 9.61% lead on Split CIFAR-100 and Split ImageNet-R, respectively). Our code is available at \url{https://github.com/thu-ml/HiDe-Prompt}.

</details>

### CL-NeRF: Continual Learning of Neural Radiance Fields for Evolving Scene Representation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/6c7154e394e24c69409256ccf8bf0804-Abstract-Conference.html)
- **作者**: Xiuzhe Wu, Peng Dai, Weipeng Deng, Handi Chen, Yang Wu, Yan-Pei Cao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### An Efficient Dataset Condensation Plugin and Its Application to Continual Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/d5f34e7e70d80f5037ab16a48e2d186e-Abstract-Conference.html) · 📚 被引 1
- **作者**: Enneng Yang, Li Shen, Zhenyi Wang, Tongliang Liu, Guibing Guo
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023
