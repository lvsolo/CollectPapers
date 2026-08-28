# Continual Learning — 2024 Guideline

> 领域: 持续学习 / 增量学习（含 VLM/多模态场景）
> 论文数: 30 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Anytime Continual Learning for Open Vocabulary Classification.
- **链接**: [arXiv:2409.08518](https://arxiv.org/abs/2409.08518) · [代码](https://github.com/jessemelpolio/AnytimeCL) · 📚 被引 4
- **作者**: Zhen Zhu, Yiming Gong, Derek Hoiem
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose an approach for anytime continual learning (AnytimeCL) for open vocabulary image classification. The AnytimeCL problem aims to break away from batch training and rigid models by requiring that a system can predict any set of labels at any time and efficiently update and improve when receiving one or more training samples at any time. Despite the challenging goal, we achieve substantial improvements over recent methods. We propose a dynamic weighting between predictions of a partially fine-tuned model and a fixed open vocabulary model that enables continual improvement when training samples are available for a subset of a task's labels. We also propose an attention-weighted PCA compression of training features that reduces storage and computation with little impact to model accuracy. Our methods are validated with experiments that test flexibility of learning and inference. Code is available at https://github.com/jessemelpolio/AnytimeCL.

</details>

### Beyond Prompt Learning: Continual Adapter for Efficient Rehearsal-Free Continual Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73013-9_6) · 📚 被引 13
- **作者**: Xinyuan Gao, Songlin Dong, Yuhang He, Qiang Wang, Yihong Gong
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### RCS-Prompt: Learning Prompt to Rearrange Class Space for Prompt-Based Continual Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72970-6_1) · 📚 被引 7
- **作者**: Longrong Yang, Hanbin Zhao, Yunlong Yu, Xiaodong Zeng, Xi Li
- **🏷️ 机构**: ZJU
- **会议**: ECCV 2024

### Continual Learning and Unknown Object Discovery in 3D Scenes via Self-distillation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73464-9_25) · 📚 被引 0
- **作者**: Mohamed El Amine Boudjoghra, Jean Lahoud, Hisham Cholakkal, Rao Muhammad Anwer, Salman Khan, Fahad Shahbaz Khan
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### PromptFusion: Decoupling Stability and Plasticity for Continual Learning.
- **链接**: [arXiv:2303.07223](https://arxiv.org/abs/2303.07223) · 📚 被引 13
- **作者**: Haoran Chen, Zuxuan Wu, Xintong Han, Menglin Jia, Yu-Gang Jiang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Current research on continual learning mainly focuses on relieving catastrophic forgetting, and most of their success is at the cost of limiting the performance of newly incoming tasks. Such a trade-off is referred to as the stability-plasticity dilemma and is a more general and challenging problem for continual learning. However, the inherent conflict between these two concepts makes it seemingly impossible to devise a satisfactory solution to both of them simultaneously. Therefore, we ask, "is it possible to divide them into two separate problems to conquer them independently?". To this end, we propose a prompt-tuning-based method termed PromptFusion to enable the decoupling of stability and plasticity. Specifically, PromptFusion consists of a carefully designed \stab module that deals with catastrophic forgetting and a \boo module to learn new knowledge concurrently. Furthermore, to address the computational overhead brought by the additional architecture, we propose PromptFusion-Lite which improves PromptFusion by dynamically determining whether to activate both modules for each input image. Extensive experiments show that both PromptFusion and PromptFusion-Lite achieve promising results on popular continual learning datasets for class-incremental and domain-incremental settings. Especially on Split-Imagenet-R, one of the most challenging datasets for class-incremental learning, our method can exceed state-of-the-art prompt-based methods by more than 5\% in accuracy, with PromptFusion-Lite using 14.8\% less computational resources than PromptFusion.

</details>

### Information Bottleneck Based Data Correction in Continual Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73021-4_16)
- **作者**: Shuai Chen, Mingyi Zhang, Junge Zhang, Kaiqi Huang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### One-Stage Prompt-Based Continual Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72624-8_10)
- **作者**: Youngeun Kim, Yuhang Li, Priyadarshini Panda
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Learn to Memorize and to Forget: A Continual Learning Perspective of Dynamic SLAM.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72980-5_3) · 📚 被引 3
- **作者**: Baicheng Li, Zike Yan, Dong Wu, Hanqing Jiang, Hongbin Zha
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Continual Learning for Remote Physiological Measurement: Minimize Forgetting and Simplify Inference.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72764-1_8) · 📚 被引 4
- **作者**: Qian Liang, Yan Chen, Yang Hu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Diffusion-Driven Data Replay: A Novel Approach to Combat Forgetting in Federated Class Continual Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73404-5_18) · 📚 被引 19
- **作者**: Jinglin Liang, Jin Zhong, Hanlin Gu, Zhongqi Lu, Xingxing Tang, Gang Dai et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### MAGMAX: Leveraging Model Merging for Seamless Continual Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73013-9_22) · 📚 被引 18
- **作者**: Daniel Marczak, Bartlomiej Twardowski, Tomasz Trzcinski, Sebastian Cygert
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Semantic Residual Prompts for Continual Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73030-6_1) · 📚 被引 5
- **作者**: Martin Menabue, Emanuele Frascaroli, Matteo Boschini, Enver Sangineto, Lorenzo Bonicelli, Angelo Porrello et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### CLEO: Continual Learning of Evolving Ontologies.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72949-2_19)
- **作者**: Shishir Muralidhara, Saqib Bukhari, Georg Schneider, Didier Stricker, René Schuster
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Mind the Interference: Retaining Pre-trained Knowledge in Parameter Efficient Continual Learning of Vision-Language Models.
- **链接**: [arXiv:2407.05342](https://arxiv.org/abs/2407.05342) · [代码](https://github.com/lloongx/DIKI) · 📚 被引 12
- **作者**: Longxiang Tang, Zhuotao Tian, Kai Li, Chunming He, Hantao Zhou, Hengshuang Zhao et al.
- **🏷️ 机构**: CUHK / SmartMore
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This study addresses the Domain-Class Incremental Learning problem, a realistic but challenging continual learning scenario where both the domain distribution and target classes vary across tasks. To handle these diverse tasks, pre-trained Vision-Language Models (VLMs) are introduced for their strong generalizability. However, this incurs a new problem: the knowledge encoded in the pre-trained VLMs may be disturbed when adapting to new tasks, compromising their inherent zero-shot ability. Existing methods tackle it by tuning VLMs with knowledge distillation on extra datasets, which demands heavy computation overhead. To address this problem efficiently, we propose the Distribution-aware Interference-free Knowledge Integration (DIKI) framework, retaining pre-trained knowledge of VLMs from a perspective of avoiding information interference. Specifically, we design a fully residual mechanism to infuse newly learned knowledge into a frozen backbone, while introducing minimal adverse impacts on pre-trained knowledge. Besides, this residual property enables our distribution-aware integration calibration scheme, explicitly controlling the information implantation process for test data from unseen distributions. Experiments demonstrate that our DIKI surpasses the current state-of-the-art approach using only 0.86% of the trained parameters and requiring substantially less training time. Code is available at: https://github.com/lloongx/DIKI .

</details>

### Pick-a-Back: Selective Device-to-Device Knowledge Transfer in Federated Continual Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73030-6_10) · 📚 被引 4
- **作者**: JinYi Yoon, HyungJune Lee
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Select and Distill: Selective Dual-Teacher Knowledge Transfer for Continual Learning on Vision-Language Models.
- **链接**: [arXiv:2403.09296](https://arxiv.org/abs/2403.09296) · 📚 被引 7
- **作者**: Yu-Chu Yu, Chi-Pin Huang, Jr-Jen Chen, Kai-Po Chang, Yung-Hsuan Lai, Fu-En Yang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large-scale vision-language models (VLMs) have shown a strong zero-shot generalization capability on unseen-domain data. However, adapting pre-trained VLMs to a sequence of downstream tasks often leads to the forgetting of previously learned knowledge and a reduction in zero-shot classification performance. To tackle this problem, we propose a unique Selective Dual-Teacher Knowledge Transfer framework that leverages the most recent fine-tuned and the original pre-trained VLMs as dual teachers to preserve the previously learned knowledge and zero-shot capabilities, respectively. With only access to an unlabeled reference dataset, our proposed framework performs a selective knowledge distillation mechanism by measuring the feature discrepancy from the dual-teacher VLMs. Consequently, our selective dual-teacher knowledge distillation mitigates catastrophic forgetting of previously learned knowledge while preserving the zero-shot capabilities of pre-trained VLMs. Extensive experiments on benchmark datasets demonstrate that our framework is favorable against state-of-the-art continual learning approaches for preventing catastrophic forgetting and zero-shot degradation. Project page: https://chuyu.org/research/snd

</details>

### Versatile Incremental Learning: Towards Class and Domain-Agnostic Incremental Learning.
- **链接**: [arXiv:2409.10956](https://arxiv.org/abs/2409.10956) · [代码](https://github.com/KHU-AGI/VIL) · 📚 被引 6
- **作者**: Min-Yeong Park, Jae-Ho Lee, Gyeong-Moon Park
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Incremental Learning (IL) aims to accumulate knowledge from sequential input tasks while overcoming catastrophic forgetting. Existing IL methods typically assume that an incoming task has only increments of classes or domains, referred to as Class IL (CIL) or Domain IL (DIL), respectively. In this work, we consider a more challenging and realistic but under-explored IL scenario, named Versatile Incremental Learning (VIL), in which a model has no prior of which of the classes or domains will increase in the next task. In the proposed VIL scenario, the model faces intra-class domain confusion and inter-domain class confusion, which makes the model fail to accumulate new knowledge without interference with learned knowledge. To address these issues, we propose a simple yet effective IL framework, named Incremental Classifier with Adaptation Shift cONtrol (ICON). Based on shifts of learnable modules, we design a novel regularization method called Cluster-based Adaptation Shift conTrol (CAST) to control the model to avoid confusion with the previously learned knowledge and thereby accumulate the new knowledge more effectively. Moreover, we introduce an Incremental Classifier (IC) which expands its output nodes to address the overwriting issue from different domains corresponding to a single class while maintaining the previous knowledge. We conducted extensive experiments on three benchmarks, showcasing the effectiveness of our method across all the scenarios, particularly in cases where the next task can be randomly altered. Our implementation code is available at https://github.com/KHU-AGI/VIL.

</details>

### iNeMo: Incremental Neural Mesh Models for Robust Class-Incremental Learning.
- **链接**: [arXiv:2407.09271](https://arxiv.org/abs/2407.09271) · [代码](https://github.com/Fischer-Tom/iNeMo) · 📚 被引 3
- **作者**: Tom Fischer, Yaoyao Liu, Artur Jesslen, Noor Ahmed, Prakhar Kaushik, Angtian Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Different from human nature, it is still common practice today for vision tasks to train deep learning models only initially and on fixed datasets. A variety of approaches have recently addressed handling continual data streams. However, extending these methods to manage out-of-distribution (OOD) scenarios has not effectively been investigated. On the other hand, it has recently been shown that non-continual neural mesh models exhibit strong performance in generalizing to such OOD scenarios. To leverage this decisive property in a continual learning setting, we propose incremental neural mesh models that can be extended with new meshes over time. In addition, we present a latent space initialization strategy that enables us to allocate feature space for future unseen classes in advance and a positional regularization term that forces the features of the different classes to consistently stay in respective latent space regions. We demonstrate the effectiveness of our method through extensive experiments on the Pascal3D and ObjectNet3D datasets and show that our approach outperforms the baselines for classification by $2-6\%$ in the in-domain and by $6-50\%$ in the OOD setting. Our work also presents the first incremental learning approach for pose estimation. Our code and model can be found at https://github.com/Fischer-Tom/iNeMo.

</details>

### PILoRA: Prototype Guided Incremental LoRA for Federated Class-Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73650-6_9) · 📚 被引 13
- **作者**: Haiyang Guo, Fei Zhu, Wenzhuo Liu, Xu-Yao Zhang, Cheng-Lin Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Learning from the Web: Language Drives Weakly-Supervised Incremental Learning for Semantic Segmentation.
- **链接**: [arXiv:2407.13363](https://arxiv.org/abs/2407.13363)
- **作者**: Chang Liu, Giulia Rizzoli, Pietro Zanuttigh, Fu Li, Yi Niu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Current weakly-supervised incremental learning for semantic segmentation (WILSS) approaches only consider replacing pixel-level annotations with image-level labels, while the training images are still from well-designed datasets. In this work, we argue that widely available web images can also be considered for the learning of new classes. To achieve this, firstly we introduce a strategy to select web images which are similar to previously seen examples in the latent space using a Fourier-based domain discriminator. Then, an effective caption-driven reharsal strategy is proposed to preserve previously learnt classes. To our knowledge, this is the first work to rely solely on web images for both the learning of new concepts and the preservation of the already learned ones in WILSS. Experimental results show that the proposed approach can reach state-of-the-art performances without using manually selected and annotated data in the incremental steps.

</details>

### CLOSER: Towards Better Representation Learning for Few-Shot Class-Incremental Learning.
- **链接**: [arXiv:2410.05627](https://arxiv.org/abs/2410.05627) · [代码](https://github.com/JungHunOh/CLOSER_ECCV2024) · 📚 被引 17
- **作者**: Junghun Oh, Sungyong Baik, Kyoung Mu Lee
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Aiming to incrementally learn new classes with only few samples while preserving the knowledge of base (old) classes, few-shot class-incremental learning (FSCIL) faces several challenges, such as overfitting and catastrophic forgetting. Such a challenging problem is often tackled by fixing a feature extractor trained on base classes to reduce the adverse effects of overfitting and forgetting. Under such formulation, our primary focus is representation learning on base classes to tackle the unique challenge of FSCIL: simultaneously achieving the transferability and the discriminability of the learned representation. Building upon the recent efforts for enhancing transferability, such as promoting the spread of features, we find that trying to secure the spread of features within a more confined feature space enables the learned representation to strike a better balance between transferability and discriminability. Thus, in stark contrast to prior beliefs that the inter-class distance should be maximized, we claim that the closer different classes are, the better for FSCIL. The empirical results and analysis from the perspective of information bottleneck theory justify our simple yet seemingly counter-intuitive representation learning method, raising research questions and suggesting alternative research directions. The code is available at https://github.com/JungHunOh/CLOSER_ECCV2024.

</details>

### Rethinking Few-Shot Class-Incremental Learning: Learning from Yourself.
- **链接**: [arXiv:2407.07468](https://arxiv.org/abs/2407.07468) · [代码](https://github.com/iSEE-Laboratory/Revisting_FSCIL)
- **作者**: Yu-Ming Tang, Yi-Xing Peng, Jingke Meng, Wei-Shi Zheng
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Few-shot class-incremental learning (FSCIL) aims to learn sequential classes with limited samples in a few-shot fashion. Inherited from the classical class-incremental learning setting, the popular benchmark of FSCIL uses averaged accuracy (aAcc) and last-task averaged accuracy (lAcc) as the evaluation metrics. However, we reveal that such evaluation metrics may not provide adequate emphasis on the novel class performance, and the continual learning ability of FSCIL methods could be ignored under this benchmark. In this work, as a complement to existing metrics, we offer a new metric called generalized average accuracy (gAcc) which is designed to provide an extra equitable evaluation by incorporating different perspectives of the performance under the guidance of a parameter $α$. We also present an overall metric in the form of the area under the curve (AUC) along the $α$. Under the guidance of gAcc, we release the potential of intermediate features of the vision transformers to boost the novel-class performance. Taking information from intermediate layers which are less class-specific and more generalizable, we manage to rectify the final features, leading to a more generalizable transformer-based FSCIL framework. Without complex network designs or cumbersome training procedures, our method outperforms existing FSCIL methods at aAcc and gAcc on three datasets. See codes at https://github.com/iSEE-Laboratory/Revisting_FSCIL

</details>

### Scene Coordinate Reconstruction: Posing of Image Collections via Incremental Learning of a Relocalizer.
- **链接**: [arXiv:2404.14351](https://arxiv.org/abs/2404.14351) · 📚 被引 48
- **作者**: Eric Brachmann, Jamie Wynn, Shuai Chen, Tommaso Cavallari, Áron Monszpart, Daniyar Turmukhambetov et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We address the task of estimating camera parameters from a set of images depicting a scene. Popular feature-based structure-from-motion (SfM) tools solve this task by incremental reconstruction: they repeat triangulation of sparse 3D points and registration of more camera views to the sparse point cloud. We re-interpret incremental structure-from-motion as an iterated application and refinement of a visual relocalizer, that is, of a method that registers new views to the current state of the reconstruction. This perspective allows us to investigate alternative visual relocalizers that are not rooted in local feature matching. We show that scene coordinate regression, a learning-based relocalization approach, allows us to build implicit, neural scene representations from unposed images. Different from other learning-based reconstruction methods, we do not require pose priors nor sequential inputs, and we optimize efficiently over thousands of images. In many cases, our method, ACE0, estimates camera poses with an accuracy close to feature-based SfM, as demonstrated by novel view synthesis. Project page: https://nianticlabs.github.io/acezero/

</details>

### STSP: Spatial-Temporal Subspace Projection for Video Class-Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73390-1_22) · 📚 被引 6
- **作者**: Hao Cheng, Siyuan Yang, Chong Wang, Joey Tianyi Zhou, Alex C. Kot, Bihan Wen
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Canonical Shape Projection Is All You Need for 3D Few-Shot Class Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72940-9_3) · 📚 被引 3
- **作者**: Ali Cheraghian, Zeeshan Hayder, Sameera Ramasinghe, Shafin Rahman, Javad Jafaryahya, Lars Petersson et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Confidence Self-calibration for Multi-label Class-Incremental Learning.
- **链接**: [arXiv:2403.12559](https://arxiv.org/abs/2403.12559) · 📚 被引 2
- **作者**: Kaile Du, Yifan Zhou, Fan Lyu, Yuyang Li, Chen Lu, Guangcan Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The partial label challenge in Multi-Label Class-Incremental Learning (MLCIL) arises when only the new classes are labeled during training, while past and future labels remain unavailable. This issue leads to a proliferation of false-positive errors due to erroneously high confidence multi-label predictions, exacerbating catastrophic forgetting within the disjoint label space. In this paper, we aim to refine multi-label confidence calibration in MLCIL and propose a Confidence Self-Calibration (CSC) approach. Firstly, for label relationship calibration, we introduce a class-incremental graph convolutional network that bridges the isolated label spaces by constructing learnable, dynamically extended label relationship graph. Then, for confidence calibration, we present a max-entropy regularization for each multi-label increment, facilitating confidence self-calibration through the penalization of over-confident output distributions. Our approach attains new state-of-the-art results in MLCIL tasks on both MS-COCO and PASCAL VOC datasets, with the calibration of label confidences confirmed through our methodology.

</details>

### Class-Incremental Learning with CLIP: Adaptive Representation Adjustment and Parameter Fusion.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72949-2_13) · 📚 被引 20
- **作者**: Linlan Huang, Xusheng Cao, Haori Lu, Xialei Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Personalized Federated Domain-Incremental Learning Based on Adaptive Knowledge Matching.
- **链接**: [arXiv:2407.05005](https://arxiv.org/abs/2407.05005) · 📚 被引 6
- **作者**: Yichen Li, Wenchao Xu, Haozhao Wang, Yining Qi, Jingcai Guo, Ruixuan Li
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper focuses on Federated Domain-Incremental Learning (FDIL) where each client continues to learn incremental tasks where their domain shifts from each other. We propose a novel adaptive knowledge matching-based personalized FDIL approach (pFedDIL) which allows each client to alternatively utilize appropriate incremental task learning strategy on the correlation with the knowledge from previous tasks. More specifically, when a new task arrives, each client first calculates its local correlations with previous tasks. Then, the client can choose to adopt a new initial model or a previous model with similar knowledge to train the new task and simultaneously migrate knowledge from previous tasks based on these correlations. Furthermore, to identify the correlations between the new task and previous tasks for each client, we separately employ an auxiliary classifier to each target classification model and propose sharing partial parameters between the target classification model and the auxiliary classifier to condense model parameters. We conduct extensive experiments on several datasets of which results demonstrate that pFedDIL outperforms state-of-the-art methods by up to 14.35\% in terms of average accuracy of all tasks.

</details>

### Few-Shot Class Incremental Learning with Attention-Aware Self-adaptive Prompt.
- **链接**: [arXiv:2403.09857](https://arxiv.org/abs/2403.09857)
- **作者**: Chenxi Liu, Zhenyi Wang, Tianyi Xiong, Ruibo Chen, Yihan Wu, Junfeng Guo et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Few-Shot Class-Incremental Learning (FSCIL) models aim to incrementally learn new classes with scarce samples while preserving knowledge of old ones. Existing FSCIL methods usually fine-tune the entire backbone, leading to overfitting and hindering the potential to learn new classes. On the other hand, recent prompt-based CIL approaches alleviate forgetting by training prompts with sufficient data in each task. In this work, we propose a novel framework named Attention-aware Self-adaptive Prompt (ASP). ASP encourages task-invariant prompts to capture shared knowledge by reducing specific information from the attention aspect. Additionally, self-adaptive task-specific prompts in ASP provide specific information and transfer knowledge from old classes to new classes with an Information Bottleneck learning objective. In summary, ASP prevents overfitting on base task and does not require enormous data in few-shot incremental tasks. Extensive experiments on three benchmark datasets validate that ASP consistently outperforms state-of-the-art FSCIL and prompt-based CIL methods in terms of both learning new classes and mitigating forgetting.

</details>

### DiffClass: Diffusion-Based Class Incremental Learning.
- **链接**: [arXiv:2403.05016](https://arxiv.org/abs/2403.05016) · 📚 被引 19
- **作者**: Zichong Meng, Jie Zhang, Changdi Yang, Zheng Zhan, Pu Zhao, Yanzhi Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Class Incremental Learning (CIL) is challenging due to catastrophic forgetting. On top of that, Exemplar-free Class Incremental Learning is even more challenging due to forbidden access to previous task data. Recent exemplar-free CIL methods attempt to mitigate catastrophic forgetting by synthesizing previous task data. However, they fail to overcome the catastrophic forgetting due to the inability to deal with the significant domain gap between real and synthetic data. To overcome these issues, we propose a novel exemplar-free CIL method. Our method adopts multi-distribution matching (MDM) diffusion models to unify quality and bridge domain gaps among all domains of training data. Moreover, our approach integrates selective synthetic image augmentation (SSIA) to expand the distribution of the training data, thereby improving the model's plasticity and reinforcing the performance of our method's ultimate component, multi-domain adaptation (MDA). With the proposed integrations, our method then reformulates exemplar-free CIL into a multi-domain adaptation problem to implicitly address the domain gap problem to enhance model stability during incremental training. Extensive experiments on benchmark class incremental datasets and settings demonstrate that our method excels previous exemplar-free CIL methods and achieves state-of-the-art performance.

</details>

### Non-exemplar Domain Incremental Learning via Cross-Domain Concept Integration.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72967-6_9) · 📚 被引 9
- **作者**: Qiang Wang, Yuhang He, Songlin Dong, Xinyuan Gao, Shaokun Wang, Yihong Gong
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### On the Approximation Risk of Few-Shot Class-Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72983-6_10)
- **作者**: Xuan Wang, Zhong Ji, Xiyao Liu, Yanwei Pang, Jungong Han
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024
