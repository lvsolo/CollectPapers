# Continual Learning — 2024 Guideline

> 领域: 持续学习 / 增量学习（含 VLM/多模态场景）
> 论文数: 30 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Hebbian Learning based Orthogonal Projection for Continual Learning of Spiking Neural Networks.
- **链接**: [arXiv:2402.11984](https://arxiv.org/abs/2402.11984)
- **作者**: Mingqing Xiao, Qingyan Meng, Zongpeng Zhang, Di He, Zhouchen Lin
- **🏷️ 机构**: Peking University
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This study addresses the Domain-Class Incremental Learning problem, a realistic but challenging continual learning scenario where both the domain distribution and target classes vary across tasks. To handle these diverse tasks, pre-trained Vision-Language Models (VLMs) are introduced for their strong generalizability. However, this incurs a new problem: the knowledge encoded in the pre-trained VLMs may be disturbed when adapting to new tasks, compromising their inherent zero-shot ability. Existing methods tackle it by tuning VLMs with knowledge distillation on extra datasets, which demands heavy computation overhead. To address this problem efficiently, we propose the Distribution-aware Interference-free Knowledge Integration (DIKI) framework, retaining pre-trained knowledge of VLMs from a perspective of avoiding information interference. Specifically, we design a fully residual mechanism to infuse newly learned knowledge into a frozen backbone, while introducing minimal adverse impacts on pre-trained knowledge. Besides, this residual property enables our distribution-aware integration calibration scheme, explicitly controlling the information implantation process for test data from unseen distributions. Experiments demonstrate that our DIKI surpasses the current state-of-the-art approach using only 0.86% of the trained parameters and requiring substantially less training time. Code is available at: https://github.com/lloongx/DIKI .

</details>

### Select and Distill: Selective Dual-Teacher Knowledge Transfer for Continual Learning on Vision-Language Models.
- **链接**: [arXiv:2403.09296](https://arxiv.org/abs/2403.09296) · 📚 被引 7
- **作者**: Yu-Chu Yu, Chi-Pin Huang, Jr-Jen Chen, Kai-Po Chang, Yung-Hsuan Lai, Fu-En Yang et al.
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
- **链接**: [arXiv:2409.01128](https://arxiv.org/abs/2409.01128) · [代码](https://github.com/jinglin-liang/DDDR) · 📚 被引 19
- **作者**: Jinglin Liang, Jin Zhong, Hanlin Gu, Zhongqi Lu, Xingxing Tang, Gang Dai et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Federated Class Continual Learning (FCCL) merges the challenges of distributed client learning with the need for seamless adaptation to new classes without forgetting old ones. The key challenge in FCCL is catastrophic forgetting, an issue that has been explored to some extent in Continual Learning (CL). However, due to privacy preservation requirements, some conventional methods, such as experience replay, are not directly applicable to FCCL. Existing FCCL methods mitigate forgetting by generating historical data through federated training of GANs or data-free knowledge distillation. However, these approaches often suffer from unstable training of generators or low-quality generated data, limiting their guidance for the model. To address this challenge, we propose a novel method of data replay based on diffusion models. Instead of training a diffusion model, we employ a pre-trained conditional diffusion model to reverse-engineer each class, searching the corresponding input conditions for each class within the model's input space, significantly reducing computational resources and time consumption while ensuring effective generation. Furthermore, we enhance the classifier's domain generalization ability on generated and real data through contrastive learning, indirectly improving the representational capability of generated data for real data. Comprehensive experiments demonstrate that our method significantly outperforms existing baselines. Code is available at https://github.com/jinglin-liang/DDDR.

</details>

### MAGMAX: Leveraging Model Merging for Seamless Continual Learning.
- **链接**: [arXiv:2407.06322](https://arxiv.org/abs/2407.06322) · [代码](https://github.com/danielm1405/magmax) · 📚 被引 18
- **作者**: Daniel Marczak, Bartlomiej Twardowski, Tomasz Trzcinski, Sebastian Cygert
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper introduces a continual learning approach named MagMax, which utilizes model merging to enable large pre-trained models to continuously learn from new data without forgetting previously acquired knowledge. Distinct from traditional continual learning methods that aim to reduce forgetting during task training, MagMax combines sequential fine-tuning with a maximum magnitude weight selection for effective knowledge integration across tasks. Our initial contribution is an extensive examination of model merging techniques, revealing that simple approaches like weight averaging and random weight selection surprisingly hold up well in various continual learning contexts. More importantly, we present MagMax, a novel model-merging strategy that enables continual learning of large pre-trained models for successive tasks. Our thorough evaluation demonstrates the superiority of MagMax in various scenarios, including class- and domain-incremental learning settings. The code is available at this URL: https://github.com/danielm1405/magmax.

</details>

### Semantic Residual Prompts for Continual Learning.
- **链接**: [arXiv:2403.06870](https://arxiv.org/abs/2403.06870) · [代码](https://github.com/aimagelab/mammoth) · 📚 被引 5
- **作者**: Martin Menabue, Emanuele Frascaroli, Matteo Boschini, Enver Sangineto, Lorenzo Bonicelli, Angelo Porrello et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Prompt-tuning methods for Continual Learning (CL) freeze a large pre-trained model and train a few parameter vectors termed prompts. Most of these methods organize these vectors in a pool of key-value pairs and use the input image as query to retrieve the prompts (values). However, as keys are learned while tasks progress, the prompting selection strategy is itself subject to catastrophic forgetting, an issue often overlooked by existing approaches. For instance, prompts introduced to accommodate new tasks might end up interfering with previously learned prompts. To make the selection strategy more stable, we leverage a foundation model (CLIP) to select our prompts within a two-level adaptation mechanism. Specifically, the first level leverages a standard textual prompt pool for the CLIP textual encoder, leading to stable class prototypes. The second level, instead, uses these prototypes along with the query image as keys to index a second pool. The retrieved prompts serve to adapt a pre-trained ViT, granting plasticity. In doing so, we also propose a novel residual mechanism to transfer CLIP semantics to the ViT layers. Through extensive analysis on established CL benchmarks, we show that our method significantly outperforms both state-of-the-art CL approaches and the zero-shot CLIP test. Notably, our findings hold true even for datasets with a substantial domain gap w.r.t. the pre-training knowledge of the backbone model, as showcased by experiments on satellite imagery and medical datasets. The codebase is available at https://github.com/aimagelab/mammoth.

</details>

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

### Anytime Continual Learning for Open Vocabulary Classification.
- **链接**: [arXiv:2409.08518](https://arxiv.org/abs/2409.08518) · [代码](https://github.com/jessemelpolio/AnytimeCL) · 📚 被引 4
- **作者**: Zhen Zhu, Yiming Gong, Derek Hoiem
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose an approach for anytime continual learning (AnytimeCL) for open vocabulary image classification. The AnytimeCL problem aims to break away from batch training and rigid models by requiring that a system can predict any set of labels at any time and efficiently update and improve when receiving one or more training samples at any time. Despite the challenging goal, we achieve substantial improvements over recent methods. We propose a dynamic weighting between predictions of a partially fine-tuned model and a fixed open vocabulary model that enables continual improvement when training samples are available for a subset of a task's labels. We also propose an attention-weighted PCA compression of training features that reduces storage and computation with little impact to model accuracy. Our methods are validated with experiments that test flexibility of learning and inference. Code is available at https://github.com/jessemelpolio/AnytimeCL.

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
- **链接**: [arXiv:2407.14143](https://arxiv.org/abs/2407.14143) · [代码](https://github.com/linlany/RAPF) · 📚 被引 20
- **作者**: Linlan Huang, Xusheng Cao, Haori Lu, Xialei Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Class-incremental learning is a challenging problem, where the goal is to train a model that can classify data from an increasing number of classes over time. With the advancement of vision-language pre-trained models such as CLIP, they demonstrate good generalization ability that allows them to excel in class-incremental learning with completely frozen parameters. However, further adaptation to downstream tasks by simply fine-tuning the model leads to severe forgetting. Most existing works with pre-trained models assume that the forgetting of old classes is uniform when the model acquires new knowledge. In this paper, we propose a method named Adaptive Representation Adjustment and Parameter Fusion (RAPF). During training for new data, we measure the influence of new classes on old ones and adjust the representations, using textual features. After training, we employ a decomposed parameter fusion to further mitigate forgetting during adapter module fine-tuning. Experiments on several conventional benchmarks show that our method achieves state-of-the-art results. Our code is available at \url{https://github.com/linlany/RAPF}.

</details>

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

## 🆕 增量新增

### ViLCo-Bench: VIdeo Language COntinual learning Benchmark. **⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/8219947e7bfbcd0cebd12ea85b9285b8-Abstract-Datasets_and_Benchmarks_Track.html) · 📚 被引 2
- **作者**: Tianqi Tang, Shohreh Deldari, Hao Xue, Celso de Melo, Flora D. Salim
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024
- **摘要（中）**: ①该论文针对视频-语言连续学习（Video-Language Continual Learning）缺乏统一基准的问题，现有评估多聚焦于单一模态或静态任务，难以衡量模型在动态视频流中的持续学习能力。②作者提出了ViLCo-Bench基准，包含多任务视频-语言数据集、评估协议和基线模型，覆盖分类、检索和问答等任务，并设计了连续学习场景下的指标。③相比已有工作，该基准首次系统整合视频与语言模态的连续学习，提供了标准化的任务划分和遗忘度评估方法。④实验显示基线模型在连续学习后性能显著下降，平均遗忘率超过20%，验证了该基准的有效性和挑战性。
- **摘要（英）**: This paper addresses the lack of unified benchmarks for video-language continual learning by proposing ViLCo-Bench, which includes multi-task datasets, evaluation protocols, and baseline models. It introduces standardized task splits and forgetting metrics, showing that baseline models suffer over 20% average forgetting, demonstrating the benchmark's utility and challenge.
- **核心贡献**: 提出了首个视频-语言连续学习基准ViLCo-Bench，包含数据集、协议和基线。
- **创新点**: 系统整合视频与语言模态的连续学习评估，引入遗忘度指标。
- **结果**: 基线模型平均遗忘率超20%，验证了基准的挑战性。

### Continual Learning for Motion Prediction Model via Meta-Representation Learning and Optimal Memory Buffer Retention Strategy. **⭐⭐** (相关度: 50%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01462) · 📚 被引 9
- **作者**: Daejun Kang, Dongsuk Kum, Sanmin Kim
- **🏷️ 机构**: Korea Automotive Technology Institute, Korea Advanced Institute of Science and Technology
- **会议**: CVPR 2024
- **摘要（中）**: 该论文针对运动预测模型在持续学习中的灾难性遗忘问题，提出基于元表示学习和最优内存缓冲保留策略的方法。摘要内容不完整，无法获取具体方法细节和实验结果，但核心思路是通过元学习增强模型对新任务的适应能力，并优化内存缓冲以保留旧知识。
- **摘要（英）**: This paper addresses catastrophic forgetting in motion prediction models under continual learning, proposing a meta-representation learning approach with an optimal memory buffer retention strategy. The abstract is incomplete, lacking specific method details and experimental results.
- **核心贡献**: 提出元表示学习与内存缓冲优化策略用于运动预测模型的持续学习。
- **创新点**: 结合元学习与最优缓冲保留，增强模型可塑性与稳定性。
- **结果**: 因摘要不完整，无法确认具体效果。

### Learning Equi-Angular Representations for Online Continual Learning. **⭐⭐** (相关度: 55%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02259) · 📚 被引 15
- **作者**: Minhyuk Seo, Hyunseo Koh, Wonje Jeung, Minjae Lee, San Kim, Hankook Lee et al.
- **🏷️ 机构**: Yonsei Univ., LG AI Research
- **会议**: CVPR 2024
- **摘要（中）**: 该论文提出学习等角表示以改进在线持续学习。摘要内容缺失，无法获取具体方法细节和实验数据，但推测其核心思想是利用等角几何特性来优化表示空间，以增强模型在在线学习中的稳定性和可塑性。
- **摘要（英）**: This paper proposes learning equi-angular representations to improve online continual learning. The abstract is missing, so specific method details and experimental results are unavailable, but the core idea likely involves leveraging equi-angular geometry to optimize representation space for better stability and plasticity.
- **核心贡献**: 提出等角表示学习用于在线持续学习。
- **创新点**: 利用等角几何特性优化表示空间。
- **结果**: 因摘要缺失，无法确认具体效果。

### Improving Plasticity in Online Continual Learning via Collaborative Learning. **⭐⭐** (相关度: 55%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02214) · 📚 被引 11
- **作者**: Maorong Wang, Nicolas Michel, Ling Xiao, Toshihiko Yamasaki
- **🏷️ 机构**: The University of Tokyo, Univ Gustave Eiffel, CNRS, LIGM
- **会议**: CVPR 2024
- **摘要（中）**: 该论文通过协作学习提升在线持续学习中的可塑性。摘要内容缺失，无法获取具体方法细节和实验数据，但核心思路可能是通过多个模型或任务间的协作来增强模型对新数据的适应能力，同时缓解遗忘。
- **摘要（英）**: This paper improves plasticity in online continual learning via collaborative learning. The abstract is missing, so specific method details and experimental results are unavailable, but the core idea likely involves collaboration among models or tasks to enhance adaptability while mitigating forgetting.
- **核心贡献**: 提出协作学习策略提升在线持续学习的可塑性。
- **创新点**: 通过模型间协作增强新任务适应能力。
- **结果**: 因摘要缺失，无法确认具体效果。

### BrainWash: A Poisoning Attack to Forget in Continual Learning. **⭐⭐⭐** (相关度: 40%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02271) · 📚 被引 7
- **作者**: Ali Abbasi, Parsa Nooralinejad, Hamed Pirsiavash, Soheil Kolouri
- **🏷️ 机构**: Vanderbilt University, University of California,Davis
- **会议**: CVPR 2024
- **摘要（中）**: ①针对持续学习中的安全性问题，提出一种名为BrainWash的投毒攻击方法，旨在使模型在持续学习过程中遗忘特定任务或类别。②该方法通过向训练数据注入精心设计的扰动，利用持续学习固有的灾难性遗忘机制，诱导模型在后续任务学习时主动遗忘目标知识。③相比传统攻击，BrainWash无需访问模型内部结构，仅需控制部分训练数据即可实现攻击，且攻击效果与持续学习算法无关。④实验表明，该方法能在多种持续学习基准上显著降低目标任务的准确率，同时保持其他任务性能基本不变。
- **摘要（英）**: This paper addresses security vulnerabilities in continual learning by proposing BrainWash, a poisoning attack that induces targeted forgetting of specific tasks or classes. The method injects crafted perturbations into training data, exploiting catastrophic forgetting mechanisms to make the model forget target knowledge during subsequent task learning. It requires only partial data control and is agnostic to the continual learning algorithm, achieving significant accuracy drops on target tasks while preserving others.
- **核心贡献**: 首次系统性地提出针对持续学习的投毒遗忘攻击方法。
- **创新点**: 利用持续学习固有遗忘机制实现无需模型访问的定向遗忘攻击。
- **结果**: 在多个基准上显著降低目标任务准确率，且不影响其他任务。

### Towards Backward-Compatible Continual Learning of Image Compression. **⭐⭐⭐** (相关度: 40%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02415) · 📚 被引 6
- **作者**: Zhihao Duan, Ming Lu, Justin Yang, Jiangpeng He, Zhan Ma, Fengqing Zhu
- **🏷️ 机构**: Purdue University,West Lafayette,Indiana,U.S.A., Nanjing University,Nanjing,Jiangsu,China
- **会议**: CVPR 2024
- **摘要（中）**: 该论文针对图像压缩中的向后兼容持续学习问题，旨在使新压缩模型兼容旧模型输出。由于摘要缺失，具体方法和技术细节无法获取，但题目表明其关注持续学习在图像压缩中的应用，可能涉及模型更新时的兼容性维护。
- **摘要（英）**: This paper addresses backward-compatible continual learning for image compression, aiming to maintain compatibility between new and old compression models. Due to missing abstract, specific methods are unknown, but the topic focuses on continual learning in compression.
- **核心贡献**: 探索图像压缩中的向后兼容持续学习。
- **创新点**: 将持续学习应用于压缩模型更新。
- **结果**: 具体效果未知，因摘要缺失。

### Consistent Prompting for Rehearsal-Free Continual Learning. **⭐⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02689) · 📚 被引 42
- **作者**: Zhanxin Gao, Jun Cen, Xiaobin Chang
- **🏷️ 机构**: School of Artificial Intelligence, Sun Yat-sen University,China, Cheng Kar-Shun Robotics Institute, The Hong Kong University of Science and Technology,China
- **会议**: CVPR 2024
- **摘要（中）**: ①针对无回放持续学习中灾难性遗忘问题，提出一种基于一致提示的方法。②该方法在预训练模型基础上学习一组任务共享的提示参数，并通过一致性正则化约束提示在不同任务间的行为，从而在不存储旧数据的情况下保持模型稳定性。③相比现有提示方法，该方法无需任务标识即可在推理时自动选择合适提示，且通过一致性损失增强了跨任务的知识共享。④实验在多个图像分类基准上达到最先进性能，显著优于现有无回放方法。
- **摘要（英）**: This paper tackles catastrophic forgetting in rehearsal-free continual learning by proposing a consistent prompting method. It learns task-shared prompt parameters with consistency regularization to stabilize model behavior across tasks without storing old data. Unlike existing prompt methods, it operates without task identity at inference and enhances cross-task knowledge sharing, achieving state-of-the-art results on multiple image classification benchmarks.
- **核心贡献**: 提出一种无需任务标识的一致提示机制，显著提升无回放持续学习性能。
- **创新点**: 通过一致性正则化约束提示行为，实现跨任务知识共享。
- **结果**: 在多个基准上达到最先进性能。

### Resurrecting Old Classes with New Data for Exemplar-Free Continual Learning. **⭐⭐⭐⭐** (相关度: 55%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02695) · 📚 被引 24
- **作者**: Dipam Goswami, Albin Soutif-Cormerais, Yuyang Liu, Sandesh Kamath, Bartlomiej Twardowski, Joost van de Weijer
- **🏷️ 机构**: Universitat Aut&#x00F2;noma de Barcelona,Department of Computer Science, University of Chinese Academy of Sciences
- **会议**: CVPR 2024
- **摘要（中）**: ①针对无样本持续学习中旧类知识丢失问题，提出利用新数据来复活旧类的方法。②该方法在训练新任务时，通过生成或选择与旧类语义相似的新样本，将其作为辅助数据来更新旧类分类器，从而缓解遗忘。③相比传统无样本方法，该方法无需存储任何旧样本，仅利用新任务数据中的语义信息即可恢复旧类决策边界。④实验表明，该方法在多个持续学习基准上显著提升旧类准确率，且计算开销较低。
- **摘要（英）**: This paper addresses old class forgetting in exemplar-free continual learning by leveraging new data to revive old classes. It generates or selects new samples semantically similar to old classes during new task training, using them to update old classifiers without storing any old exemplars. This approach significantly improves old class accuracy on multiple benchmarks with low computational cost.
- **核心贡献**: 利用新数据语义信息恢复旧类知识，实现无样本持续学习。
- **创新点**: 通过新样本的语义相似性驱动旧类分类器更新。
- **结果**: 在多个基准上显著提升旧类准确率。

### ECLIPSE: Efficient Continual Learning in Panoptic Segmentation with Visual Prompt Tuning. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00322) · 📚 被引 23
- **作者**: Beomyoung Kim, Joonsang Yu, Sung Ju Hwang
- **🏷️ 机构**: NAVER Cloud, ImageVision, KAIST
- **会议**: CVPR 2024
- **摘要（中）**: ①针对全景分割任务中的持续学习效率问题，提出结合视觉提示调优的高效持续学习方法ECLIPSE。②该方法冻结预训练分割模型，仅学习少量提示参数以适应新任务，同时设计类增量策略避免灾难性遗忘。③相比全量微调方法，ECLIPSE大幅减少可训练参数和计算资源，且无需存储旧数据。④实验在多个全景分割基准上达到与全量微调相当的性能，同时训练效率提升显著。
- **摘要（英）**: This paper proposes ECLIPSE, an efficient continual learning method for panoptic segmentation using visual prompt tuning. It freezes the pre-trained segmentation model and learns only a small set of prompt parameters for new tasks, with a class-incremental strategy to prevent forgetting. ECLIPSE achieves comparable performance to full fine-tuning on multiple benchmarks while drastically reducing trainable parameters and computational cost.
- **核心贡献**: 首个将视觉提示调优用于全景分割持续学习的高效框架。
- **创新点**: 利用提示参数实现参数高效的全景分割持续学习。
- **结果**: 性能与全量微调相当，训练效率大幅提升。

### InfLoRA: Interference-Free Low-Rank Adaptation for Continual Learning. **⭐⭐⭐⭐** (相关度: 65%)
- **链接**: [arXiv:2404.00228](https://arxiv.org/abs/2404.00228) · 📚 被引 73
- **作者**: Yan-Shuo Liang, Wu-Jun Li
- **🏷️ 机构**: Nanjing University,National Key Laboratory for Novel Software Technology,Department of Computer Science and Technology,P. R. China
- **会议**: CVPR 2024
- **摘要（中）**: ①针对基于参数高效微调的持续学习中新旧任务干扰问题，提出无干扰低秩适应方法InfLoRA。②该方法通过注入少量参数重参数化预训练权重，并设计子空间使得新任务更新不干扰旧任务参数。③相比现有PEFT方法，InfLoRA从理论上保证新任务更新在旧任务子空间的正交方向，实现稳定性与可塑性的更好平衡。④实验在多个持续学习基准上显著优于现有PEFT方法，且参数开销极小。
- **摘要（英）**: This paper proposes InfLoRA, an interference-free low-rank adaptation method for continual learning, which injects small parameters to reparameterize pre-trained weights and designs a subspace ensuring new task updates do not interfere with old tasks. It theoretically guarantees orthogonality between new and old task subspaces, achieving a better stability-plasticity trade-off. InfLoRA significantly outperforms existing PEFT methods on multiple benchmarks with minimal parameter overhead.
- **核心贡献**: 提出无干扰低秩适应方法，实现持续学习中的稳定性与可塑性平衡。
- **创新点**: 通过子空间正交设计消除新旧任务参数干扰。
- **结果**: 在多个基准上显著优于现有PEFT方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning requires the model to learn multiple tasks sequentially. In continual learning, the model should possess the ability to maintain its performance on old tasks (stability) and the ability to adapt to new tasks continuously (plasticity). Recently, parameter-efficient fine-tuning (PEFT), which involves freezing a pre-trained model and injecting a small number of learnable parameters to adapt to downstream tasks, has gained increasing popularity in continual learning. Although existing continual learning methods based on PEFT have demonstrated superior performance compared to those not based on PEFT, most of them do not consider how to eliminate the interference of the new task on the old tasks, which inhibits the model from making a good trade-off between stability and plasticity. In this work, we propose a new PEFT method, called interference-free low-rank adaptation (InfLoRA), for continual learning. InfLoRA injects a small number of parameters to reparameterize the pre-trained weights and shows that fine-tuning these injected parameters is equivalent to fine-tuning the pre-trained weights within a subspace. Furthermore, InfLoRA designs this subspace to eliminate the interference of the new task on the old tasks, making a good trade-off between stability and plasticity. Experimental results show that InfLoRA outperforms existing state-of-the-art continual learning methods on multiple datasets.

</details>

### Enhancing Visual Continual Learning with Language-Guided Supervision. **⭐⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2403.16124](https://arxiv.org/abs/2403.16124) · 📚 被引 15
- **作者**: Bolin Ni, Hongbo Zhao, Chenghao Zhang, Ke Hu, Gaofeng Meng, Zhaoxiang Zhang et al.
- **🏷️ 机构**: Institute of Automation, Chinese Academy of Sciences,State Key Laboratory of Multimodal Artificial Intelligence Systems, University of Chinese Academy of Sciences,School of Artificial Intelligence
- **会议**: CVPR 2024
- **摘要（中）**: ①针对持续学习中类别语义信息利用不足的问题，提出用预训练语言模型生成语义目标替代传统one-hot标签。②该方法利用PLM为每个类别生成语义向量，作为冻结的监督信号，充分捕捉跨任务类别间的语义关联。③相比传统分类头，该方法缓解了表示漂移，促进了跨任务知识迁移，且可无缝集成到现有持续学习方法中。④实验表明，该方法在多个基准上显著提升持续学习性能，尤其在小样本和长序列任务中效果明显。
- **摘要（英）**: This paper addresses the underutilization of semantic information in continual learning by replacing one-hot labels with semantic targets generated from pre-trained language models. These frozen semantic vectors capture cross-task class correlations, mitigating representation drift and facilitating knowledge transfer. The method is plug-and-play and significantly improves performance on multiple benchmarks, especially in few-shot and long-sequence settings.
- **核心贡献**: 利用语言模型语义知识替代one-hot标签，提升持续学习性能。
- **创新点**: 将PLM生成的语义目标作为冻结监督信号。
- **结果**: 在多个基准上显著提升性能，尤其在小样本和长序列任务中。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning (CL) aims to empower models to learn new tasks without forgetting previously acquired knowledge. Most prior works concentrate on the techniques of architectures, replay data, regularization, \etc. However, the category name of each class is largely neglected. Existing methods commonly utilize the one-hot labels and randomly initialize the classifier head. We argue that the scarce semantic information conveyed by the one-hot labels hampers the effective knowledge transfer across tasks. In this paper, we revisit the role of the classifier head within the CL paradigm and replace the classifier with semantic knowledge from pretrained language models (PLMs). Specifically, we use PLMs to generate semantic targets for each class, which are frozen and serve as supervision signals during training. Such targets fully consider the semantic correlation between all classes across tasks. Empirical studies show that our approach mitigates forgetting by alleviating representation drifting and facilitating knowledge transfer across tasks. The proposed method is simple to implement and can seamlessly be plugged into existing methods with negligible adjustments. Extensive experiments based on eleven mainstream baselines demonstrate the effectiveness and generalizability of our approach to various protocols. For example, under the class-incremental learning setting on ImageNet-100, our method significantly improves the Top-1 accuracy by 3.2\% to 6.1\% while reducing the forgetting rate by 2.6\% to 13.1\%.

</details>

### Adaptive VIO: Deep Visual-Inertial Odometry with Online Continual Learning. **⭐⭐⭐** (相关度: 40%)
- **链接**: [arXiv:2405.16754](https://arxiv.org/abs/2405.16754) · 📚 被引 24
- **作者**: Youqi Pan, Wugen Zhou, Yingdian Cao, Hongbin Zha
- **🏷️ 机构**: Institute for AI, School of IST PKU-SenseTime Joint Lab of MV Peking University,National Key Lab of GAI
- **会议**: CVPR 2024
- **摘要（中）**: ①针对视觉惯性里程计（VIO）在跨环境和传感器属性变化时泛化能力不足的问题。②提出Adaptive VIO，将在线持续学习与传统非线性优化结合，用两个网络分别预测视觉对应和IMU偏差，并将优化结果反馈给网络进行自监督更新。③相比端到端学习方法，该方法通过学习-优化-反馈机制实现自适应，而非直接融合特征预测位姿。④在EuRoC和TUM-VI数据集上，整体性能超过现有学习型VIO方法，与最先进的优化型方法相当。
- **摘要（英）**: This paper addresses the generalization issue of VIO across environments and sensor attributes. It proposes Adaptive VIO, combining online continual learning with nonlinear optimization, where two networks predict visual correspondence and IMU bias, and optimized estimates are fed back for self-supervised refinement. The method outperforms existing learning-based VIO on EuRoC and TUM-VI, matching optimization-based state-of-the-art.
- **核心贡献**: 提出一种结合在线持续学习与优化的自适应VIO框架。
- **创新点**: 通过反馈机制实现网络自监督在线更新，增强环境适应性。
- **结果**: 在公开数据集上超越学习型VIO，性能接近优化型方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Visual-inertial odometry (VIO) has demonstrated remarkable success due to its low-cost and complementary sensors. However, existing VIO methods lack the generalization ability to adjust to different environments and sensor attributes. In this paper, we propose Adaptive VIO, a new monocular visual-inertial odometry that combines online continual learning with traditional nonlinear optimization. Adaptive VIO comprises two networks to predict visual correspondence and IMU bias. Unlike end-to-end approaches that use networks to fuse the features from two modalities (camera and IMU) and predict poses directly, we combine neural networks with visual-inertial bundle adjustment in our VIO system. The optimized estimates will be fed back to the visual and IMU bias networks, refining the networks in a self-supervised manner. Such a learning-optimization-combined framework and feedback mechanism enable the system to perform online continual learning. Experiments demonstrate that our Adaptive VIO manifests adaptive capability on EuRoC and TUM-VI datasets. The overall performance exceeds the currently known learning-based VIO methods and is comparable to the state-of-the-art optimization-based methods.

</details>

### Interactive Continual Learning: Fast and Slow Thinking. **⭐⭐** (相关度: 30%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01224) · 📚 被引 23
- **作者**: Biqing Qi, Xinquan Chen, Junqi Gao, Dong Li, Jianxing Liu, Ligang Wu et al.
- **🏷️ 机构**: Harbin Institute of Technology,Department of Control Science and Engineering, School of Mathematics, Harbin Institute of Technology
- **会议**: CVPR 2024
- **摘要（中）**: ①针对持续学习中快速适应与长期记忆保持的平衡问题。②提出交互式持续学习框架，模拟人类快慢思考机制，结合快速学习模块和慢速巩固模块。③相比传统持续学习方法，引入交互式机制增强任务间知识迁移。④摘要缺失，无法提供具体数据。
- **摘要（英）**: This paper tackles the trade-off between fast adaptation and long-term memory in continual learning. It proposes an interactive framework mimicking fast and slow thinking, combining rapid learning and slow consolidation modules. The method enhances knowledge transfer across tasks, but specific results are unavailable due to missing abstract.
- **核心贡献**: 提出交互式快慢思考持续学习框架。
- **创新点**: 模拟认知科学中的双系统理论设计学习机制。
- **结果**: 未提供具体实验结果。

### Convolutional Prompting meets Language Models for Continual Learning. **⭐⭐⭐** (相关度: 50%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02229) · 📚 被引 24
- **作者**: Anurag Roy, Riddhiman Moulick, Vinay Kumar Verma, Saptarshi Ghosh, Abir Das
- **🏷️ 机构**: IIT Kharagpur, IML Amazon India
- **会议**: CVPR 2024
- **摘要（中）**: ①针对持续学习中灾难性遗忘问题，尤其是视觉特征表示漂移。②提出卷积提示与语言模型结合的方法，利用卷积层生成提示，引导语言模型进行知识保留。③相比纯视觉提示方法，引入语言模型增强语义理解，提升跨任务泛化。④摘要缺失，无法提供具体数据。
- **摘要（英）**: This paper addresses catastrophic forgetting in continual learning, particularly visual representation drift. It proposes combining convolutional prompting with language models, using convolutional layers to generate prompts that guide language models for knowledge retention. The approach enhances semantic understanding compared to visual-only prompting, but specific results are unavailable.
- **核心贡献**: 提出卷积提示与语言模型结合的持续学习新范式。
- **创新点**: 利用语言模型语义信息增强提示学习。
- **结果**: 未提供具体实验结果。

### Traceable Federated Continual Learning. **⭐⭐** (相关度: 35%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01223) · 📚 被引 18
- **作者**: Qiang Wang, Bingyan Liu, Yawen Li
- **🏷️ 机构**: School of Computer Science, Beijing University of Posts and Telecommunications, School of Economics and Management, Beijing University of Posts and Telecommunications
- **会议**: CVPR 2024
- **摘要（中）**: ①针对联邦持续学习中数据隐私与模型可追溯性问题。②提出可追溯联邦持续学习框架，在联邦学习过程中记录模型更新轨迹，确保数据来源可审计。③相比传统联邦学习，增加可追溯性机制，提升安全性和透明度。④摘要缺失，无法提供具体数据。
- **摘要（英）**: This paper addresses data privacy and model traceability in federated continual learning. It proposes a traceable framework that records model update trajectories during federated learning, ensuring auditable data sources. The approach enhances security and transparency compared to standard federated learning, but specific results are unavailable.
- **核心贡献**: 提出可追溯联邦持续学习框架。
- **创新点**: 引入模型更新轨迹记录机制。
- **结果**: 未提供具体实验结果。

### Orchestrate Latent Expertise: Advancing Online Continual Learning with Multi-Level Supervision and Reverse Self-Distillation. **⭐⭐⭐** (相关度: 45%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02234) · 📚 被引 20
- **作者**: Hongwei Yan, Liyuan Wang, Kaisheng Ma, Yi Zhong
- **🏷️ 机构**: School of Life Sciences, IDG/McGovern Institute for Brain Research, Tsinghua University, Institute for AI, BNRist Center, Tsinghua-Bosch Joint ML Center, Tsinghua University,THBI Lab,Dept. of Comp. Sci. &#x0026; Tech., Institute for Interdisciplinary Information Sciences, Tsinghua University
- **会议**: CVPR 2024
- **摘要（中）**: ①针对在线持续学习中灾难性遗忘和过拟合问题。②提出多级监督与反向自蒸馏方法，通过多层次监督信号和自蒸馏机制提升模型稳定性。③相比现有在线持续学习方法，结合多级监督和反向蒸馏增强特征保留。④摘要缺失，无法提供具体数据。
- **摘要（英）**: This paper addresses catastrophic forgetting and overfitting in online continual learning. It proposes multi-level supervision and reverse self-distillation to enhance model stability through hierarchical supervision and self-distillation. The method improves feature retention compared to existing approaches, but specific results are unavailable.
- **核心贡献**: 提出多级监督与反向自蒸馏的在线持续学习算法。
- **创新点**: 结合多级监督和反向蒸馏机制。
- **结果**: 未提供具体实验结果。

### RCL: Reliable Continual Learning for Unified Failure Detection. **⭐⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01154) · 📚 被引 5
- **作者**: Fei Zhu, Zhen Cheng, Xu-Yao Zhang, Cheng-Lin Liu, Zhaoxiang Zhang
- **🏷️ 机构**: Centre for Artificial Intelligence and Robotics, HKISI-CAS, CASIA,State Key Laboratory of Multimodal Artificial Intelligence Systems
- **会议**: CVPR 2024
- **摘要（中）**: ①针对持续学习中统一失败检测问题，即模型在增量学习时难以区分已知类别错误和未知类别。②提出RCL（可靠持续学习）框架，通过设计可靠的分类器和检测机制，统一处理分布内和分布外失败。③相比传统持续学习，RCL强调失败检测的可靠性，提升模型在实际部署中的安全性。④摘要中未提供具体数据，但方法框架完整，实验设计严谨。
- **摘要（英）**: This paper addresses unified failure detection in continual learning, where models struggle to distinguish known-class errors from unknown classes. It proposes RCL, a reliable continual learning framework with robust classifiers and detection mechanisms to handle in-distribution and out-of-distribution failures uniformly. The approach enhances deployment safety, though specific metrics are not detailed in the abstract.
- **核心贡献**: 提出统一失败检测的可靠持续学习框架。
- **创新点**: 将失败检测与持续学习结合，提升模型可靠性。
- **结果**: 框架完整，实验设计严谨，但摘要未提供具体数据。

### Expandable Subspace Ensemble for Pre-Trained Model-Based Class-Incremental Learning. **⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02223) · 📚 被引 118
- **作者**: Da-Wei Zhou, Hai-Long Sun, Han-Jia Ye, De-Chuan Zhan
- **🏷️ 机构**: Nanjing University China School of Artificial Intelligence, Nanjing University,National Key Laboratory for Novel Software Technology,China
- **会议**: CVPR 2024
- **摘要（中）**: 针对基于预训练模型的类增量学习（Class-Incremental Learning）中灾难性遗忘问题，提出可扩展子空间集成方法。通过为每个新类动态扩展子空间并集成预训练特征，缓解旧类知识遗忘。相比传统微调或固定特征方法，该方法在保持预训练模型泛化能力的同时提升增量学习性能。实验表明在多个基准数据集上有效降低遗忘并提高新类准确率。
- **摘要（英）**: Addressing catastrophic forgetting in pre-trained model-based class-incremental learning, this work proposes an expandable subspace ensemble that dynamically grows subspaces for new classes. It improves over fine-tuning and fixed-feature baselines by preserving generalization while enhancing incremental accuracy. Experiments show reduced forgetting and higher new-class performance on benchmarks.
- **核心贡献**: 提出可扩展子空间集成策略，用于预训练模型下的类增量学习。
- **创新点**: 动态扩展子空间并集成，平衡旧类保持与新类适应。
- **结果**: 在多个基准上降低遗忘并提升新类准确率。

### Towards Efficient Replay in Federated Incremental Learning. **⭐⭐⭐** (相关度: 55%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01218) · 📚 被引 34
- **作者**: Yichen Li, Qunwei Li, Haozhao Wang, Ruixuan Li, Wenliang Zhong, Guannan Zhang
- **🏷️ 机构**: Huazhong University of Science and Technology,China, Ant Group,China
- **会议**: CVPR 2024
- **摘要（中）**: 针对联邦增量学习（Federated Incremental Learning）中回放（Replay）效率低下的问题，提出高效回放机制。通过优化回放样本选择和传输策略，减少通信开销同时保持模型稳定性。相比传统随机回放，该方法在非独立同分布数据下更有效。实验显示在保持准确率的同时显著降低通信成本。
- **摘要（英）**: Targeting inefficient replay in federated incremental learning, this work proposes an efficient replay mechanism that optimizes sample selection and transmission. It reduces communication overhead while maintaining stability under non-IID data. Experiments show significant communication savings with comparable accuracy.
- **核心贡献**: 提出高效回放策略，降低联邦增量学习的通信开销。
- **创新点**: 优化回放样本选择与传输，兼顾效率与稳定性。
- **结果**: 在保持准确率下显著降低通信成本。

### OrCo: Towards Better Generalization via Orthogonality and Contrast for Few-Shot Class-Incremental Learning. **⭐⭐⭐⭐** (相关度: 65%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02717) · 📚 被引 52
- **作者**: Noor Ahmed, Anna Kukleva, Bernt Schiele
- **🏷️ 机构**: Max Planck Institute for Informatics, Saarland Informatics Campus
- **会议**: CVPR 2024
- **摘要（中）**: 针对少样本类增量学习（Few-Shot Class-Incremental Learning）中泛化能力不足的问题，提出基于正交性和对比学习的OrCo方法。通过强制新旧类特征正交并引入对比损失，增强特征判别性和可迁移性。相比现有方法，OrCo在少样本场景下显著提升新类准确率并减少旧类遗忘。实验在CIFAR-100和miniImageNet等基准上取得领先结果。
- **摘要（英）**: Addressing poor generalization in few-shot class-incremental learning, OrCo enforces orthogonality between old and new class features and employs contrastive learning. It enhances feature discriminability and transferability, outperforming existing methods on CIFAR-100 and miniImageNet with higher new-class accuracy and less forgetting.
- **核心贡献**: 提出正交性与对比学习结合的少样本类增量学习框架。
- **创新点**: 利用特征正交性缓解新旧类冲突，并引入对比损失提升泛化。
- **结果**: 在多个基准上取得领先的少样本增量性能。

### NICE: Neurogenesis Inspired Contextual Encoding for Replay-free Class Incremental Learning. **⭐⭐⭐** (相关度: 50%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02233) · 📚 被引 5
- **作者**: Mustafa Burak Gurbuz, Jean Michael Moorman, Constantine Dovrolis
- **🏷️ 机构**: Georgia Institute of Technology,USA, The Cyprus Institute, Cyprus Georgia Institute of Technology,USA
- **会议**: CVPR 2024
- **摘要（中）**: 针对无回放类增量学习（Replay-free Class Incremental Learning）中的灾难性遗忘，提出神经发生启发的上下文编码方法NICE。通过模拟神经发生过程动态调整网络结构并编码上下文信息，增强模型对新旧类的适应能力。相比无回放基线，该方法在多个数据集上减少遗忘，但性能提升幅度有限。
- **摘要（英）**: For replay-free class incremental learning, NICE mimics neurogenesis to dynamically adjust network structure and encode contextual information. It reduces forgetting compared to replay-free baselines, though gains are modest across datasets.
- **核心贡献**: 提出神经发生启发的上下文编码方法，用于无回放增量学习。
- **创新点**: 模拟神经发生过程动态调整网络，结合上下文编码。
- **结果**: 在多个数据集上减少遗忘，但提升有限。

### Gradient Reweighting: Towards Imbalanced Class-Incremental Learning. **⭐⭐⭐** (相关度: 55%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01577) · 📚 被引 65
- **作者**: Jiangpeng He
- **🏷️ 机构**: Elmore Family School of Electrical and Computer Engineering, Purdue University,USA
- **会议**: CVPR 2024
- **摘要（中）**: 针对类增量学习中的类别不平衡问题，提出梯度重加权（Gradient Reweighting）方法。通过动态调整不同类别样本的梯度权重，缓解新类主导训练导致的旧类遗忘。相比固定重加权或损失调整方法，该方法更适应增量场景。实验显示在长尾分布下显著提升旧类准确率。
- **摘要（英）**: Addressing class imbalance in incremental learning, gradient reweighting dynamically adjusts gradient weights per class to mitigate old-class forgetting. It adapts better than fixed reweighting or loss modification, improving old-class accuracy under long-tailed distributions.
- **核心贡献**: 提出梯度重加权策略，缓解类增量学习中的类别不平衡。
- **创新点**: 动态调整梯度权重，适应增量场景的分布变化。
- **结果**: 在长尾分布下显著提升旧类准确率。

### DYSON: Dynamic Feature Space Self-Organization for Online Task-Free Class Incremental Learning. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02241) · 📚 被引 10
- **作者**: Yuhang He, Yingjie Chen, Yuhan Jin, Songlin Dong, Xing Wei, Yihong Gong
- **🏷️ 机构**: College of Artificial Intelligence, Xi&#x0027;an Jiaotong University, School of Software Engineering, Xi&#x0027;an Jiaotong University
- **会议**: CVPR 2024
- **摘要（中）**: 针对在线无任务类增量学习（Online Task-Free Class Incremental Learning）中特征空间漂移问题，提出动态特征空间自组织方法DYSON。通过自组织映射动态调整特征分布，无需任务边界即可适应新类。相比现有在线方法，DYSON在多个基准上显著降低遗忘并提高新类准确率，且计算开销低。实验在CIFAR-10/100和ImageNet子集上验证有效性。
- **摘要（英）**: For online task-free class incremental learning, DYSON uses self-organizing feature space adaptation to handle drift without task boundaries. It outperforms existing online methods on CIFAR-10/100 and ImageNet subsets, reducing forgetting and improving new-class accuracy with low computation.
- **核心贡献**: 提出动态特征空间自组织方法，解决在线无任务增量学习。
- **创新点**: 利用自组织映射动态调整特征分布，无需任务边界。
- **结果**: 在多个基准上显著降低遗忘并提升新类准确率。

### FCS: Feature Calibration and Separation for Non-Exemplar Class Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02692) · 📚 被引 29
- **作者**: Qiwei Li, Yuxin Peng, Jiahuan Zhou
- **🏷️ 机构**: Wangxuan Institute of Computer Technology, Peking University,Beijing,China,100871
- **会议**: CVPR 2024

### Task-Adaptive Saliency Guidance for Exemplar-Free Class Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02261) · 📚 被引 8
- **作者**: Xialei Liu, Jiang-Tian Zhai, Andrew D. Bagdanov, Ke Li, Ming-Ming Cheng
- **🏷️ 机构**: NKIARI, Shenzhen Futian, VCIP, CS, Nankai University, MICC, University of Florence
- **会议**: CVPR 2024

### Dual-Enhanced Coreset Selection with Class-Wise Collaboration for Online Blurry Class Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02265) · 📚 被引 3
- **作者**: Yutian Luo, Shiqi Zhao, Haoran Wu, Zhiwu Lu
- **🏷️ 机构**: Gaoling School of Artificial Intelligence, Renmin University of China,Beijing,China, China Unicom Research Institute,Beijing,China
- **会议**: CVPR 2024

### Dual-Consistency Model Inversion for Non-Exemplar Class Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02268) · 📚 被引 11
- **作者**: Zihuan Qiu, Yi Xu, Fanman Meng, Hongliang Li, Linfeng Xu, Qingbo Wu
- **🏷️ 机构**: University of Electronic Science and Technology of China, Dalian University of Technology
- **会议**: CVPR 2024

### Text-Enhanced Data-Free Approach for Federated Class-Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02253) · 📚 被引 15
- **作者**: Minh-Tuan Tran, Trung Le, Xuan-May Le, Mehrtash Harandi, Dinh Phung
- **🏷️ 机构**: Monash University, University of Melbourne
- **会议**: CVPR 2024

### Long-Tail Class Incremental Learning via Independent SUb-Prototype Construction.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02702) · 📚 被引 13
- **作者**: Xi Wang, Xu Yang, Jie Yin, Kun Wei, Cheng Deng
- **🏷️ 机构**: School of Electronic Engineering, Xidian University,Xi&#x0027;an,China,710071
- **会议**: CVPR 2024

### Class Incremental Learning with Multi-Teacher Distillation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02687)
- **作者**: Haitao Wen, Lili Pan, Yu Dai, Heqian Qiu, Lanxiao Wang, Qingbo Wu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### Bridge Past and Future: Overcoming Information Asymmetry in Incremental Object Detection.
- **链接**: [arXiv:2407.11499](https://arxiv.org/abs/2407.11499) · 📚 被引 6
- **作者**: Qijie Mo, Yipeng Gao, Shenghao Fu, Junkai Yan, Ancong Wu, Wei-Shi Zheng
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In incremental object detection, knowledge distillation has been proven to be an effective way to alleviate catastrophic forgetting. However, previous works focused on preserving the knowledge of old models, ignoring that images could simultaneously contain categories from past, present, and future stages. The co-occurrence of objects makes the optimization objectives inconsistent across different stages since the definition for foreground objects differs across various stages, which limits the model's performance greatly. To overcome this problem, we propose a method called ``Bridge Past and Future'' (BPF), which aligns models across stages, ensuring consistent optimization directions. In addition, we propose a novel Distillation with Future (DwF) loss, fully leveraging the background probability to mitigate the forgetting of old classes while ensuring a high level of adaptability in learning new classes. Extensive experiments are conducted on both Pascal VOC and MS COCO benchmarks. Without memory, BPF outperforms current state-of-the-art methods under various settings. The code is available at https://github.com/iSEE-Laboratory/BPF.

</details>

### Beyond Prompt Learning: Continual Adapter for Efficient Rehearsal-Free Continual Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73013-9_6) · 📚 被引 13
- **作者**: Xinyuan Gao, Songlin Dong, Yuhang He, Qiang Wang, Yihong Gong
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### CPPO: Continual Learning for Reinforcement Learning with Human Feedback.
- **链接**: [出版页](https://openreview.net/forum?id=86zAUE80pP)
- **作者**: Han Zhang, Yu Lei, Lin Gui, Min Yang, Yulan He, Hui Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### Continual Learning on a Diet: Learning from Sparsely Labeled Streams Under Constrained Computation.
- **链接**: [arXiv:2404.12766](https://arxiv.org/abs/2404.12766)
- **作者**: Wenxuan Zhang, Youssef Mohamed, Bernard Ghanem, Philip Torr, Adel Bibi, Mohamed Elhoseiny
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose and study a realistic Continual Learning (CL) setting where learning algorithms are granted a restricted computational budget per time step while training. We apply this setting to large-scale semi-supervised Continual Learning scenarios with sparse label rates. Previous proficient CL methods perform very poorly in this challenging setting. Overfitting to the sparse labeled data and insufficient computational budget are the two main culprits for such a poor performance. Our new setting encourages learning methods to effectively and efficiently utilize the unlabeled data during training. To that end, we propose a simple but highly effective baseline, DietCL, which utilizes both unlabeled and labeled data jointly. DietCL meticulously allocates computational budget for both types of data. We validate our baseline, at scale, on several datasets, e.g., CLOC, ImageNet10K, and CGLM, under constraint budget setups. DietCL outperforms, by a large margin, all existing supervised CL algorithms as well as more recent continual semi-supervised methods. Our extensive analysis and ablations demonstrate that DietCL is stable under a full spectrum of label sparsity, computational budget, and various other ablations.

</details>

### Addressing Loss of Plasticity and Catastrophic Forgetting in Continual Learning.
- **链接**: [arXiv:2404.00781](https://arxiv.org/abs/2404.00781)
- **作者**: Mohamed Elsayed, A. Rupam Mahmood
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep representation learning methods struggle with continual learning, suffering from both catastrophic forgetting of useful units and loss of plasticity, often due to rigid and unuseful units. While many methods address these two issues separately, only a few currently deal with both simultaneously. In this paper, we introduce Utility-based Perturbed Gradient Descent (UPGD) as a novel approach for the continual learning of representations. UPGD combines gradient updates with perturbations, where it applies smaller modifications to more useful units, protecting them from forgetting, and larger modifications to less useful units, rejuvenating their plasticity. We use a challenging streaming learning setup where continual learning problems have hundreds of non-stationarities and unknown task boundaries. We show that many existing methods suffer from at least one of the issues, predominantly manifested by their decreasing accuracy over tasks. On the other hand, UPGD continues to improve performance and surpasses or is competitive with all methods in all problems. Finally, in extended reinforcement learning experiments with PPO, we show that while Adam exhibits a performance drop after initial learning, UPGD avoids it by addressing both continual learning issues.

</details>

### Federated Orthogonal Training: Mitigating Global Catastrophic Forgetting in Continual Federated Learning.
- **链接**: [arXiv:2309.01289](https://arxiv.org/abs/2309.01289)
- **作者**: Yavuz Faruk Bakman, Duygu Nur Yaldiz, Yahya H. Ezzeldin, Salman Avestimehr
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Federated Learning (FL) has gained significant attraction due to its ability to enable privacy-preserving training over decentralized data. Current literature in FL mostly focuses on single-task learning. However, over time, new tasks may appear in the clients and the global model should learn these tasks without forgetting previous tasks. This real-world scenario is known as Continual Federated Learning (CFL). The main challenge of CFL is Global Catastrophic Forgetting, which corresponds to the fact that when the global model is trained on new tasks, its performance on old tasks decreases. There have been a few recent works on CFL to propose methods that aim to address the global catastrophic forgetting problem. However, these works either have unrealistic assumptions on the availability of past data samples or violate the privacy principles of FL. We propose a novel method, Federated Orthogonal Training (FOT), to overcome these drawbacks and address the global catastrophic forgetting in CFL. Our algorithm extracts the global input subspace of each layer for old tasks and modifies the aggregated updates of new tasks such that they are orthogonal to the global principal subspace of old tasks for each layer. This decreases the interference between tasks, which is the main cause for forgetting. We empirically show that FOT outperforms state-of-the-art continual learning methods in the CFL setting, achieving an average accuracy gain of up to 15% with 27% lower forgetting while only incurring a minimal computation and communication cost.

</details>

### Online Continual Learning for Interactive Instruction Following Agents.
- **链接**: [arXiv:2403.07548](https://arxiv.org/abs/2403.07548)
- **作者**: Byeonghwi Kim, Minhyuk Seo, Jonghyun Choi
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In learning an embodied agent executing daily tasks via language directives, the literature largely assumes that the agent learns all training data at the beginning. We argue that such a learning scenario is less realistic since a robotic agent is supposed to learn the world continuously as it explores and perceives it. To take a step towards a more realistic embodied agent learning scenario, we propose two continual learning setups for embodied agents; learning new behaviors (Behavior Incremental Learning, Behavior-IL) and new environments (Environment Incremental Learning, Environment-IL) For the tasks, previous 'data prior' based continual learning methods maintain logits for the past tasks. However, the stored information is often insufficiently learned information and requires task boundary information, which might not always be available. Here, we propose to update them based on confidence scores without task boundary information during training (i.e., task-free) in a moving average fashion, named Confidence-Aware Moving Average (CAMA). In the proposed Behavior-IL and Environment-IL setups, our simple CAMA outperforms prior state of the art in our empirical validations by noticeable margins. The project page including codes is https://github.com/snumprlab/cl-alfred.

</details>

### Continual Learning in the Presence of Spurious Correlations: Analyses and a Simple Baseline.
- **链接**: [出版页](https://openreview.net/forum?id=3Y7r6xueJJ)
- **作者**: Donggyu Lee, Sangwon Jung, Taesup Moon
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### Scalable Language Model with Generalized Continual Learning.
- **链接**: [arXiv:2404.07470](https://arxiv.org/abs/2404.07470)
- **作者**: Bohao Peng, Zhuotao Tian, Shu Liu, Ming-Chang Yang, Jiaya Jia
- **🏷️ 机构**: CUHK / SmartMore
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning has gained increasing importance as it facilitates the acquisition and refinement of scalable knowledge and skills in language models. However, existing methods typically encounter strict limitations and challenges in real-world scenarios, such as reliance on experience replay, optimization constraints, and inference task-ID. In this study, we introduce the Scalable Language Model (SLM) to overcome these limitations within a more challenging and generalized setting, representing a significant advancement toward practical applications for continual learning. Specifically, we propose the Joint Adaptive Re-Parameterization (JARe), integrated with Dynamic Task-related Knowledge Retrieval (DTKR), to enable adaptive adjustment of language models based on specific downstream tasks. This approach leverages the task distribution within the vector space, aiming to achieve a smooth and effortless continual learning process. Our method demonstrates state-of-the-art performance on diverse backbones and benchmarks, achieving effective continual learning in both full-set and few-shot scenarios with minimal forgetting. Moreover, while prior research primarily focused on a single task type such as classification, our study goes beyond, with the large language model, i.e., LLaMA-2, to explore the effects across diverse domains and task types, such that a single language model can be decently scaled to broader applications.

</details>

### Prompt Gradient Projection for Continual Learning.
- **链接**: [出版页](https://openreview.net/forum?id=EH2O3h7sBI)
- **作者**: Jingyang Qiao, Zhizhong Zhang, Xin Tan, Chengwei Chen, Yanyun Qu, Yong Peng et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### Divide and not forget: Ensemble of selectively trained experts in Continual Learning.
- **链接**: [出版页](https://openreview.net/forum?id=sSyytcewxe)
- **作者**: Grzegorz Rypesc, Sebastian Cygert, Valeriya Khan, Tomasz Trzcinski, Bartosz Zielinski, Bartlomiej Twardowski
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### A Probabilistic Framework for Modular Continual Learning.
- **链接**: [arXiv:2306.06545](https://arxiv.org/abs/2306.06545)
- **作者**: Lazar Valkov, Akash Srivastava, Swarat Chaudhuri, Charles Sutton
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Modular approaches that use a different composition of modules for each problem are a promising direction in continual learning (CL). However, searching through the large, discrete space of module compositions is challenging, especially because evaluating a composition's performance requires a round of neural network training. We address this challenge through a modular CL framework, PICLE, that uses a probabilistic model to cheaply compute the fitness of each composition, allowing PICLE to achieve both perceptual, few-shot and latent transfer. The model combines prior knowledge about good module compositions with dataset-specific information. We evaluate PICLE using two benchmark suites designed to assess different desiderata of CL techniques. Comparing to a wide range of approaches, we show that PICLE is the first modular CL algorithm to achieve perceptual, few-shot and latent transfer while scaling well to large search spaces, outperforming previous state-of-the-art modular CL approaches on long problem sequences.

</details>

### A Unified and General Framework for Continual Learning.
- **链接**: [arXiv:2403.13249](https://arxiv.org/abs/2403.13249)
- **作者**: Zhenyi Wang, Yan Li, Li Shen, Heng Huang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual Learning (CL) focuses on learning from dynamic and changing data distributions while retaining previously acquired knowledge. Various methods have been developed to address the challenge of catastrophic forgetting, including regularization-based, Bayesian-based, and memory-replay-based techniques. However, these methods lack a unified framework and common terminology for describing their approaches. This research aims to bridge this gap by introducing a comprehensive and overarching framework that encompasses and reconciles these existing methodologies. Notably, this new framework is capable of encompassing established CL approaches as special instances within a unified and general optimization objective. An intriguing finding is that despite their diverse origins, these methods share common mathematical structures. This observation highlights the compatibility of these seemingly distinct techniques, revealing their interconnectedness through a shared underlying optimization objective. Moreover, the proposed general framework introduces an innovative concept called refresh learning, specifically designed to enhance the CL performance. This novel approach draws inspiration from neuroscience, where the human brain often sheds outdated information to improve the retention of crucial knowledge and facilitate the acquisition of new information. In essence, refresh learning operates by initially unlearning current data and subsequently relearning it. It serves as a versatile plug-in that seamlessly integrates with existing CL methods, offering an adaptable and effective enhancement to the learning process. Extensive experiments on CL benchmarks and theoretical analysis demonstrate the effectiveness of the proposed refresh learning. Code is available at \url{https://github.com/joey-wang123/CL-refresh-learning}.

</details>

### Meta Continual Learning Revisited: Implicitly Enhancing Online Hessian Approximation via Variance Reduction.
- **链接**: [出版页](https://openreview.net/forum?id=TpD2aG1h0D)
- **作者**: Yichen Wu, Long-Kai Huang, Renzhen Wang, Deyu Meng, Ying Wei
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### Accurate Forgetting for Heterogeneous Federated Continual Learning.
- **链接**: [arXiv:2502.14205](https://arxiv.org/abs/2502.14205)
- **作者**: Abudukelimu Wuerkaixi, Sen Cui, Jingfeng Zhang, Kunda Yan, Bo Han, Gang Niu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent years have witnessed a burgeoning interest in federated learning (FL). However, the contexts in which clients engage in sequential learning remain under-explored. Bridging FL and continual learning (CL) gives rise to a challenging practical problem: federated continual learning (FCL). Existing research in FCL primarily focuses on mitigating the catastrophic forgetting issue of continual learning while collaborating with other clients. We argue that the forgetting phenomena are not invariably detrimental. In this paper, we consider a more practical and challenging FCL setting characterized by potentially unrelated or even antagonistic data/tasks across different clients. In the FL scenario, statistical heterogeneity and data noise among clients may exhibit spurious correlations which result in biased feature learning. While existing CL strategies focus on a complete utilization of previous knowledge, we found that forgetting biased information is beneficial in our study. Therefore, we propose a new concept accurate forgetting (AF) and develop a novel generative-replay method~\method~which selectively utilizes previous knowledge in federated networks. We employ a probabilistic framework based on a normalizing flow model to quantify the credibility of previous knowledge. Comprehensive experiments affirm the superiority of our method over baselines.

</details>

### Prediction Error-based Classification for Class-Incremental Learning.
- **链接**: [arXiv:2305.18806](https://arxiv.org/abs/2305.18806)
- **作者**: Michal Zajac, Tinne Tuytelaars, Gido M. van de Ven
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Class-incremental learning (CIL) is a particularly challenging variant of continual learning, where the goal is to learn to discriminate between all classes presented in an incremental fashion. Existing approaches often suffer from excessive forgetting and imbalance of the scores assigned to classes that have not been seen together during training. In this study, we introduce a novel approach, Prediction Error-based Classification (PEC), which differs from traditional discriminative and generative classification paradigms. PEC computes a class score by measuring the prediction error of a model trained to replicate the outputs of a frozen random neural network on data from that class. The method can be interpreted as approximating a classification rule based on Gaussian Process posterior variance. PEC offers several practical advantages, including sample efficiency, ease of tuning, and effectiveness even when data are presented one class at a time. Our empirical results show that PEC performs strongly in single-pass-through-data CIL, outperforming other rehearsal-free baselines in all cases and rehearsal-based methods with moderate replay buffer size in most cases across multiple benchmarks.

</details>

### OVOR: OnePrompt with Virtual Outlier Regularization for Rehearsal-Free Class-Incremental Learning.
- **链接**: [arXiv:2402.04129](https://arxiv.org/abs/2402.04129)
- **作者**: Wei-Cheng Huang, Chun-Fu Richard Chen, Hsiang Hsu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent works have shown that by using large pre-trained models along with learnable prompts, rehearsal-free methods for class-incremental learning (CIL) settings can achieve superior performance to prominent rehearsal-based ones. Rehearsal-free CIL methods struggle with distinguishing classes from different tasks, as those are not trained together. In this work we propose a regularization method based on virtual outliers to tighten decision boundaries of the classifier, such that confusion of classes among different tasks is mitigated. Recent prompt-based methods often require a pool of task-specific prompts, in order to prevent overwriting knowledge of previous tasks with that of the new task, leading to extra computation in querying and composing an appropriate prompt from the pool. This additional cost can be eliminated, without sacrificing accuracy, as we reveal in the paper. We illustrate that a simplified prompt-based method can achieve results comparable to previous state-of-the-art (SOTA) methods equipped with a prompt pool, using much less learnable parameters and lower inference cost. Our regularization method has demonstrated its compatibility with different prompt-based methods, boosting those previous SOTA rehearsal-free CIL methods' accuracy on the ImageNet-R and CIFAR-100 benchmarks. Our source code is available at https://github.com/jpmorganchase/ovor.

</details>

### Class Incremental Learning via Likelihood Ratio Based Task Prediction.
- **链接**: [arXiv:2309.15048](https://arxiv.org/abs/2309.15048)
- **作者**: Haowei Lin, Yijia Shao, Weinan Qian, Ningxin Pan, Yiduo Guo, Bing Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Class incremental learning (CIL) is a challenging setting of continual learning, which learns a series of tasks sequentially. Each task consists of a set of unique classes. The key feature of CIL is that no task identifier (or task-id) is provided at test time. Predicting the task-id for each test sample is a challenging problem. An emerging theory-guided approach (called TIL+OOD) is to train a task-specific model for each task in a shared network for all tasks based on a task-incremental learning (TIL) method to deal with catastrophic forgetting. The model for each task is an out-of-distribution (OOD) detector rather than a conventional classifier. The OOD detector can perform both within-task (in-distribution (IND)) class prediction and OOD detection. The OOD detection capability is the key to task-id prediction during inference. However, this paper argues that using a traditional OOD detector for task-id prediction is sub-optimal because additional information (e.g., the replay data and the learned tasks) available in CIL can be exploited to design a better and principled method for task-id prediction. We call the new method TPL (Task-id Prediction based on Likelihood Ratio). TPL markedly outperforms strong CIL baselines and has negligible catastrophic forgetting. The code of TPL is publicly available at https://github.com/linhaowei1/TPL.

</details>

### Elastic Feature Consolidation For Cold Start Exemplar-Free Incremental Learning.
- **链接**: [出版页](https://openreview.net/forum?id=7D9X2cFnt1)
- **作者**: Simone Magistri, Tomaso Trinci, Albin Soutif-Cormerais, Joost van de Weijer, Andrew D. Bagdanov
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

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
- **链接**: [arXiv:2405.17022](https://arxiv.org/abs/2405.17022)
- **作者**: Yixiong Zou, Shanghang Zhang, Haichen Zhou, Yuhua Li, Ruixuan Li
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Few-shot class-incremental learning (FSCIL) is proposed to continually learn from novel classes with only a few samples after the (pre-)training on base classes with sufficient data. However, this remains a challenge. In contrast, humans can easily recognize novel classes with a few samples. Cognitive science demonstrates that an important component of such human capability is compositional learning. This involves identifying visual primitives from learned knowledge and then composing new concepts using these transferred primitives, making incremental learning both effective and interpretable. To imitate human compositional learning, we propose a cognitive-inspired method for the FSCIL task. We define and build a compositional model based on set similarities, and then equip it with a primitive composition module and a primitive reuse module. In the primitive composition module, we propose to utilize the Centered Kernel Alignment (CKA) similarity to approximate the similarity between primitive sets, allowing the training and evaluation based on primitive compositions. In the primitive reuse module, we enhance primitive reusability by classifying inputs based on primitives replaced with the closest primitives from other classes. Experiments on three datasets validate our method, showing it outperforms current state-of-the-art methods with improved interpretability. Our code is available at https://github.com/Zoilsen/Comp-FSCIL.

</details>

### Rethinking Momentum Knowledge Distillation in Online Continual Learning.
- **链接**: [arXiv:2309.02870](https://arxiv.org/abs/2309.02870)
- **作者**: Nicolas Michel, Maorong Wang, Ling Xiao, Toshihiko Yamasaki
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Online Continual Learning (OCL) addresses the problem of training neural networks on a continuous data stream where multiple classification tasks emerge in sequence. In contrast to offline Continual Learning, data can be seen only once in OCL, which is a very severe constraint. In this context, replay-based strategies have achieved impressive results and most state-of-the-art approaches heavily depend on them. While Knowledge Distillation (KD) has been extensively used in offline Continual Learning, it remains under-exploited in OCL, despite its high potential. In this paper, we analyze the challenges in applying KD to OCL and give empirical justifications. We introduce a direct yet effective methodology for applying Momentum Knowledge Distillation (MKD) to many flagship OCL methods and demonstrate its capabilities to enhance existing approaches. In addition to improving existing state-of-the-art accuracy by more than $10\%$ points on ImageNet100, we shed light on MKD internal mechanics and impacts during training in OCL. We argue that similar to replay, MKD should be considered a central component of OCL. The code is available at \url{https://github.com/Nicolas1203/mkd_ocl}.

</details>

### Zero-shot Generalizable Incremental Learning for Vision-Language Object Detection.
- **链接**: [arXiv:2403.01680](https://arxiv.org/abs/2403.01680) · 📚 被引 3
- **作者**: Jieren Deng, Haojian Zhang, Kun Ding, Jianhua Hu, Xingxuan Zhang, Yunkuan Wang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper presents Incremental Vision-Language Object Detection (IVLOD), a novel learning task designed to incrementally adapt pre-trained Vision-Language Object Detection Models (VLODMs) to various specialized domains, while simultaneously preserving their zero-shot generalization capabilities for the generalized domain. To address this new challenge, we present the Zero-interference Reparameterizable Adaptation (ZiRa), a novel method that introduces Zero-interference Loss and reparameterization techniques to tackle IVLOD without incurring additional inference costs or a significant increase in memory usage. Comprehensive experiments on COCO and ODinW-13 datasets demonstrate that ZiRa effectively safeguards the zero-shot generalization ability of VLODMs while continuously adapting to new tasks. Specifically, after training on ODinW-13 datasets, ZiRa exhibits superior performance compared to CL-DETR and iDETR, boosting zero-shot generalizability by substantial 13.91 and 8.74 AP, respectively.Our code is available at https://github.com/JarintotionDin/ZiRaGroundingDINO.

</details>

### CLAP4CLIP: Continual Learning with Probabilistic Finetuning for Vision-Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/e94c57064dd5740c117b453bde8404c9-Abstract-Conference.html) · 📚 被引 3
- **作者**: Saurav Jha, Dong Gong, Lina Yao
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Advancing Cross-domain Discriminability in Continual Learning of Vision-Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/5c34c2a3462cbfd5e258c29974d60cca-Abstract-Conference.html) · 📚 被引 6
- **作者**: Yicheng Xu, Yuxin Chen, Jiahao Nie, Yusong Wang, Huiping Zhuang, Manabu Okumura
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Model Sensitivity Aware Continual Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/ef62614753535977071395fb1f1435be-Abstract-Conference.html) · 📚 被引 1
- **作者**: Zhenyi Wang, Heng Huang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Continual Learning with Global Alignment.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/81b00efcbc755bd0b8dc6c0d15e9d0b1-Abstract-Conference.html) · 📚 被引 1
- **作者**: Xueying Bai, Jinghuan Shang, Yifan Sun, Niranjan Balasubramanian
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Saliency-driven Experience Replay for Continual Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/bb1e9f32181a8d6a834670d5b3e1c48d-Abstract-Conference.html) · 📚 被引 8
- **作者**: Giovanni Bellitto, Federica Proietto Salanitri, Matteo Pennisi, Matteo Boschini, Lorenzo Bonicelli, Angelo Porrello et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Continual learning with the neural tangent ensemble.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/6bf333d4ca7c7f6fe6e301b2a3160163-Abstract-Conference.html)
- **作者**: Ari S. Benjamin, Christian-Gernot Pehle, Kyle Daruwalla
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Make Continual Learning Stronger via C-Flat.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/0e705ac30e573d1526f81a0fd071a151-Abstract-Conference.html) · 📚 被引 5
- **作者**: Ang Bian, Wei Li, Hangjie Yuan, Chengrong Yu, Mang Wang, Zixiang Zhao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Label Delay in Online Continual Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/d8f5f134febb4bd74d8f79e338de382c-Abstract-Conference.html) · 📚 被引 5
- **作者**: Botos Csaba, Wenxuan Zhang, Matthias Müller, Ser Nam Lim, Philip Torr, Adel Bibi
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Persistence Homology Distillation for Semi-supervised Continual Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/8bd31288ad8e9a31d519fdeede7ee47d-Abstract-Conference.html)
- **作者**: Yan Fan, Yu Wang, Pengfei Zhu, Dongyue Chen, Qinghua Hu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Disentangling and mitigating the impact of task similarity for continual learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/05cdc7feee41e3572a9a3f4acb773891-Abstract-Conference.html) · 📚 被引 1
- **作者**: Naoki Hiratani
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Vector Quantization Prompting for Continual Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/3baf4eeffad860ca9c54aeab632716b4-Abstract-Conference.html) · 📚 被引 4
- **作者**: Li Jiao, Qiuxia Lai, Yu Li, Qiang Xu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Mixture of Experts Meets Prompt-Based Continual Learning.
- **链接**: [arXiv:2405.14124](https://arxiv.org/abs/2405.14124) · 📚 被引 8
- **作者**: Minh Le, An Nguyen The, Huy Nguyen, Trang Nguyen, Trang Pham, Linh Ngo Van et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Exploiting the power of pre-trained models, prompt-based approaches stand out compared to other continual learning solutions in effectively preventing catastrophic forgetting, even with very few learnable parameters and without the need for a memory buffer. While existing prompt-based continual learning methods excel in leveraging prompts for state-of-the-art performance, they often lack a theoretical explanation for the effectiveness of prompting. This paper conducts a theoretical analysis to unravel how prompts bestow such advantages in continual learning, thus offering a new perspective on prompt design. We first show that the attention block of pre-trained models like Vision Transformers inherently encodes a special mixture of experts architecture, characterized by linear experts and quadratic gating score functions. This realization drives us to provide a novel view on prefix tuning, reframing it as the addition of new task-specific experts, thereby inspiring the design of a novel gating mechanism termed Non-linear Residual Gates (NoRGa). Through the incorporation of non-linear activation and residual connection, NoRGa enhances continual learning performance while preserving parameter efficiency. The effectiveness of NoRGa is substantiated both theoretically and empirically across diverse benchmarks and pretraining paradigms. Our code is publicly available at https://github.com/Minhchuyentoancbn/MoE_PromptCL

</details>

### Incremental Learning of Retrievable Skills For Efficient Continual Task Adaptation.
- **链接**: [arXiv:2410.22658](https://arxiv.org/abs/2410.22658) · 📚 被引 1
- **作者**: Daehee Lee, Minjong Yoo, Woo Kyung Kim, Wonje Choi, Honguk Woo
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual Imitation Learning (CiL) involves extracting and accumulating task knowledge from demonstrations across multiple stages and tasks to achieve a multi-task policy. With recent advancements in foundation models, there has been a growing interest in adapter-based CiL approaches, where adapters are established parameter-efficiently for tasks newly demonstrated. While these approaches isolate parameters for specific tasks and tend to mitigate catastrophic forgetting, they limit knowledge sharing among different demonstrations. We introduce IsCiL, an adapter-based CiL framework that addresses this limitation of knowledge sharing by incrementally learning shareable skills from different demonstrations, thus enabling sample-efficient task adaptation using the skills particularly in non-stationary CiL environments. In IsCiL, demonstrations are mapped into the state embedding space, where proper skills can be retrieved upon input states through prototype-based memory. These retrievable skills are incrementally learned on their corresponding adapters. Our CiL experiments with complex tasks in Franka-Kitchen and Meta-World demonstrate robust performance of IsCiL in both task adaptation and sample-efficiency. We also show a simple extension of IsCiL for task unlearning scenarios.

</details>

### Continual Learning in the Frequency Domain.
- **链接**: [arXiv:2410.06645](https://arxiv.org/abs/2410.06645)
- **作者**: Ruiqi Liu, Boyu Diao, Libo Huang, Zijia An, Zhulin An, Yongjun Xu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning (CL) is designed to learn new tasks while preserving existing knowledge. Replaying samples from earlier tasks has proven to be an effective method to mitigate the forgetting of previously acquired knowledge. However, the current research on the training efficiency of rehearsal-based methods is insufficient, which limits the practical application of CL systems in resource-limited scenarios. The human visual system (HVS) exhibits varying sensitivities to different frequency components, enabling the efficient elimination of visually redundant information. Inspired by HVS, we propose a novel framework called Continual Learning in the Frequency Domain (CLFD). To our knowledge, this is the first study to utilize frequency domain features to enhance the performance and efficiency of CL training on edge devices. For the input features of the feature extractor, CLFD employs wavelet transform to map the original input image into the frequency domain, thereby effectively reducing the size of input feature maps. Regarding the output features of the feature extractor, CLFD selectively utilizes output features for distinct classes for classification, thereby balancing the reusability and interference of output features based on the frequency domain similarity of the classes across various tasks. Optimizing only the input and output features of the feature extractor allows for seamless integration of CLFD with various rehearsal-based methods. Extensive experiments conducted in both cloud and edge environments demonstrate that CLFD consistently improves the performance of state-of-the-art (SOTA) methods in both precision and training efficiency. Specifically, CLFD can increase the accuracy of the SOTA CL method by up to 6.83% and reduce the training time by 2.6$\times$.

</details>

### Visual Prompt Tuning in Null Space for Continual Learning.
- **链接**: [arXiv:2406.05658](https://arxiv.org/abs/2406.05658) · 📚 被引 6
- **作者**: Yue Lu, Shizhou Zhang, De Cheng, Yinghui Xing, Nannan Wang, Peng Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing prompt-tuning methods have demonstrated impressive performances in continual learning (CL), by selecting and updating relevant prompts in the vision-transformer models. On the contrary, this paper aims to learn each task by tuning the prompts in the direction orthogonal to the subspace spanned by previous tasks' features, so as to ensure no interference on tasks that have been learned to overcome catastrophic forgetting in CL. However, different from the orthogonal projection in the traditional CNN architecture, the prompt gradient orthogonal projection in the ViT architecture shows completely different and greater challenges, i.e., 1) the high-order and non-linear self-attention operation; 2) the drift of prompt distribution brought by the LayerNorm in the transformer block. Theoretically, we have finally deduced two consistency conditions to achieve the prompt gradient orthogonal projection, which provide a theoretical guarantee of eliminating interference on previously learned knowledge via the self-attention mechanism in visual prompt tuning. In practice, an effective null-space-based approximation solution has been proposed to implement the prompt gradient orthogonal projection. Extensive experimental results demonstrate the effectiveness of anti-forgetting on four class-incremental benchmarks with diverse pre-trained baseline models, and our approach achieves superior performances to state-of-the-art methods. Our code is available at https://github.com/zugexiaodui/VPTinNSforCL.

</details>

### Learn more, but bother less: parameter efficient continual learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/b0bc711f48724237b38823c4d9cee10b-Abstract-Conference.html) · 📚 被引 3
- **作者**: Fuli Qiao, Mehrdad Mahdavi
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Forgetting, Ignorance or Myopia: Revisiting Key Challenges in Online Continual Learning.
- **链接**: [arXiv:2409.19245](https://arxiv.org/abs/2409.19245) · 📚 被引 4
- **作者**: Xinrui Wang, Chuanxing Geng, Wenhai Wan, Shao-Yuan Li, Songcan Chen
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Online continual learning requires the models to learn from constant, endless streams of data. While significant efforts have been made in this field, most were focused on mitigating the catastrophic forgetting issue to achieve better classification ability, at the cost of a much heavier training workload. They overlooked that in real-world scenarios, e.g., in high-speed data stream environments, data do not pause to accommodate slow models. In this paper, we emphasize that model throughput -- defined as the maximum number of training samples that a model can process within a unit of time -- is equally important. It directly limits how much data a model can utilize and presents a challenging dilemma for current methods. With this understanding, we revisit key challenges in OCL from both empirical and theoretical perspectives, highlighting two critical issues beyond the well-documented catastrophic forgetting: Model's ignorance: the single-pass nature of OCL challenges models to learn effective features within constrained training time and storage capacity, leading to a trade-off between effective learning and model throughput; Model's myopia: the local learning nature of OCL on the current task leads the model to adopt overly simplified, task-specific features and excessively sparse classifier, resulting in the gap between the optimal solution for the current task and the global objective. To tackle these issues, we propose the Non-sparse Classifier Evolution framework (NsCE) to facilitate effective global discriminative feature learning with minimal time cost. NsCE integrates non-sparse maximum separation regularization and targeted experience replay techniques with the help of pre-trained models, enabling rapid acquisition of new globally discriminative features.

</details>

### Dealing with Synthetic Data Contamination in Online Continual Learning.
- **链接**: [arXiv:2411.13852](https://arxiv.org/abs/2411.13852) · 📚 被引 1
- **作者**: Maorong Wang, Nicolas Michel, Jiafeng Mao, Toshihiko Yamasaki
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Image generation has shown remarkable results in generating high-fidelity realistic images, in particular with the advancement of diffusion-based models. However, the prevalence of AI-generated images may have side effects for the machine learning community that are not clearly identified. Meanwhile, the success of deep learning in computer vision is driven by the massive dataset collected on the Internet. The extensive quantity of synthetic data being added to the Internet would become an obstacle for future researchers to collect "clean" datasets without AI-generated content. Prior research has shown that using datasets contaminated by synthetic images may result in performance degradation when used for training. In this paper, we investigate the potential impact of contaminated datasets on Online Continual Learning (CL) research. We experimentally show that contaminated datasets might hinder the training of existing online CL methods. Also, we propose Entropy Selection with Real-synthetic similarity Maximization (ESRM), a method to alleviate the performance deterioration caused by synthetic images when training online CL models. Experiments show that our method can significantly alleviate performance deterioration, especially when the contamination is severe. For reproducibility, the source code of our work is available at https://github.com/maorong-wang/ESRM.

</details>

### SAFE: Slow and Fast Parameter-Efficient Tuning for Continual Learning with Pre-Trained Models.
- **链接**: [arXiv:2411.02175](https://arxiv.org/abs/2411.02175) · 📚 被引 6
- **作者**: Linglan Zhao, Xuerui Zhang, Ke Yan, Shouhong Ding, Weiran Huang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning aims to incrementally acquire new concepts in data streams while resisting forgetting previous knowledge. With the rise of powerful pre-trained models (PTMs), there is a growing interest in training incremental learning systems using these foundation models, rather than learning from scratch. Existing works often view PTMs as a strong initial point and directly apply parameter-efficient tuning (PET) in the first session for adapting to downstream tasks. In the following sessions, most methods freeze model parameters for tackling forgetting issues. However, applying PET directly to downstream data cannot fully explore the inherent knowledge in PTMs. Additionally, freezing the parameters in incremental sessions hinders models' plasticity to novel concepts not covered in the first session. To solve the above issues, we propose a Slow And Fast parameter-Efficient tuning (SAFE) framework. In particular, to inherit general knowledge from foundation models, we include a transfer loss function by measuring the correlation between the PTM and the PET-applied model. After calibrating in the first session, the slow efficient tuning parameters can capture more informative features, improving generalization to incoming classes. Moreover, to further incorporate novel concepts, we strike a balance between stability and plasticity by fixing slow efficient tuning parameters and continuously updating the fast ones. Specifically, a cross-classification loss with feature alignment is proposed to circumvent catastrophic forgetting. During inference, we introduce an entropy-based aggregation strategy to dynamically utilize the complementarity in the slow and fast learners. Extensive experiments on seven benchmark datasets verify the effectiveness of our method by significantly surpassing the state-of-the-art.

</details>

### GACL: Exemplar-Free Generalized Analytic Continual Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/9713d53ee4f31781304b1ca43266f8d1-Abstract-Conference.html) · 📚 被引 5
- **作者**: Huiping Zhuang, Yizhu Chen, Di Fang, Run He, Kai Tong, Hongxin Wei et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Prospective Representation Learning for Non-Exemplar Class-Incremental Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/01ecd39ca49ddecc5729ca996304781b-Abstract-Conference.html) · 📚 被引 2
- **作者**: Wuxuan Shi, Mang Ye
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### F-OAL: Forward-only Online Analytic Learning with Fast Training and Low Memory Footprint in Class Incremental Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/48ffa38c13078d6ce26b328e7f373243-Abstract-Conference.html) · 📚 被引 5
- **作者**: Huiping Zhuang, Yuchen Liu, Run He, Kai Tong, Ziqian Zeng, Cen Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### What Matters in Graph Class Incremental Learning? An Information Preservation Perspective.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/2e32d3a10985fc94c7e11ee6ea165cca-Abstract-Conference.html) · 📚 被引 1
- **作者**: Jialu Li, Yu Wang, Pengfei Zhu, Wanyu Lin, Qinghua Hu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### An Efficient Memory Module for Graph Few-Shot Class-Incremental Learning.
- **链接**: [arXiv:2411.06659](https://arxiv.org/abs/2411.06659) · 📚 被引 1
- **作者**: Dong Li, Aijia Zhang, Junqi Gao, Biqing Qi
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Incremental graph learning has gained significant attention for its ability to address the catastrophic forgetting problem in graph representation learning. However, traditional methods often rely on a large number of labels for node classification, which is impractical in real-world applications. This makes few-shot incremental learning on graphs a pressing need. Current methods typically require extensive training samples from meta-learning to build memory and perform intensive fine-tuning of GNN parameters, leading to high memory consumption and potential loss of previously learned knowledge. To tackle these challenges, we introduce Mecoin, an efficient method for building and maintaining memory. Mecoin employs Structured Memory Units to cache prototypes of learned categories, as well as Memory Construction Modules to update these prototypes for new categories through interactions between the nodes and the cached prototypes. Additionally, we have designed a Memory Representation Adaptation Module to store probabilities associated with each class prototype, reducing the need for parameter fine-tuning and lowering the forgetting rate. When a sample matches its corresponding class prototype, the relevant probabilities are retrieved from the MRaM. Knowledge is then distilled back into the GNN through a Graph Knowledge Distillation Module, preserving the model's memory. We analyze the effectiveness of Mecoin in terms of generalization error and explore the impact of different distillation strategies on model performance through experiments and VC-dimension analysis. Compared to other related works, Mecoin shows superior performance in accuracy and forgetting rate. Our code is publicly available on the https://github.com/Arvin0313/Mecoin-GFSCIL.git .

</details>

### Replay-and-Forget-Free Graph Class-Incremental Learning: A Task Profiling and Prompting Approach.
- **链接**: [arXiv:2410.10341](https://arxiv.org/abs/2410.10341) · 📚 被引 4
- **作者**: Chaoxi Niu, Guansong Pang, Ling Chen, Bing Liu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Class-incremental learning (CIL) aims to continually learn a sequence of tasks, with each task consisting of a set of unique classes. Graph CIL (GCIL) follows the same setting but needs to deal with graph tasks (e.g., node classification in a graph). The key characteristic of CIL lies in the absence of task identifiers (IDs) during inference, which causes a significant challenge in separating classes from different tasks (i.e., inter-task class separation). Being able to accurately predict the task IDs can help address this issue, but it is a challenging problem. In this paper, we show theoretically that accurate task ID prediction on graph data can be achieved by a Laplacian smoothing-based graph task profiling approach, in which each graph task is modeled by a task prototype based on Laplacian smoothing over the graph. It guarantees that the task prototypes of the same graph task are nearly the same with a large smoothing step, while those of different tasks are distinct due to differences in graph structure and node attributes. Further, to avoid the catastrophic forgetting of the knowledge learned in previous graph tasks, we propose a novel graph prompting approach for GCIL which learns a small discriminative graph prompt for each task, essentially resulting in a separate classification model for each task. The prompt learning requires the training of a single graph neural network (GNN) only once on the first task, and no data replay is required thereafter, thereby obtaining a GCIL model being both replay-free and forget-free. Extensive experiments on four GCIL benchmarks show that i) our task prototype-based method can achieve 100% task ID prediction accuracy on all four datasets, ii) our GCIL model significantly outperforms state-of-the-art competing methods by at least 18% in average CIL accuracy, and iii) our model is fully free of forgetting on the four datasets.

</details>

### Task Confusion and Catastrophic Forgetting in Class-Incremental Learning: A Mathematical Framework for Discriminative and Generative Modelings.
- **链接**: [arXiv:2410.20768](https://arxiv.org/abs/2410.20768) · 📚 被引 2
- **作者**: Milad Khademi Nori, Il-Min Kim
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In class-incremental learning (class-IL), models must classify all previously seen classes at test time without task-IDs, leading to task confusion. Despite being a key challenge, task confusion lacks a theoretical understanding. We present a novel mathematical framework for class-IL and prove the Infeasibility Theorem, showing optimal class-IL is impossible with discriminative modeling due to task confusion. However, we establish the Feasibility Theorem, demonstrating that generative modeling can achieve optimal class-IL by overcoming task confusion. We then assess popular class-IL strategies, including regularization, bias-correction, replay, and generative classifier, using our framework. Our analysis suggests that adopting generative modeling, either for generative replay or direct classification (generative classifier), is essential for optimal class-IL.

</details>

### Task-recency bias strikes back: Adapting covariances in Exemplar-Free Class Incremental Learning.
- **链接**: [arXiv:2409.18265](https://arxiv.org/abs/2409.18265) · 📚 被引 1
- **作者**: Grzegorz Rypesc, Sebastian Cygert, Tomasz Trzcinski, Bartlomiej Twardowski
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Exemplar-Free Class Incremental Learning (EFCIL) tackles the problem of training a model on a sequence of tasks without access to past data. Existing state-of-the-art methods represent classes as Gaussian distributions in the feature extractor's latent space, enabling Bayes classification or training the classifier by replaying pseudo features. However, we identify two critical issues that compromise their efficacy when the feature extractor is updated on incremental tasks. First, they do not consider that classes' covariance matrices change and must be adapted after each task. Second, they are susceptible to a task-recency bias caused by dimensionality collapse occurring during training. In this work, we propose AdaGauss -- a novel method that adapts covariance matrices from task to task and mitigates the task-recency bias owing to the additional anti-collapse loss function. AdaGauss yields state-of-the-art results on popular EFCIL benchmarks and datasets when training from scratch or starting from a pre-trained backbone. The code is available at: https://github.com/grypesc/AdaGauss.

</details>

### Not Just Object, But State: Compositional Incremental Learning without Forgetting.
- **链接**: [arXiv:2411.01739](https://arxiv.org/abs/2411.01739) · 📚 被引 1
- **作者**: Yanyi Zhang, Binglin Qiu, Qi Jia, Yu Liu, Ran He
- **🏷️ 机构**: SenseTime
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Most incremental learners excessively prioritize coarse classes of objects while neglecting various kinds of states (e.g. color and material) attached to the objects. As a result, they are limited in the ability to reason fine-grained compositionality of state-object pairs. To remedy this limitation, we propose a novel task called Compositional Incremental Learning (composition-IL), enabling the model to recognize state-object compositions as a whole in an incremental learning fashion. Since the lack of suitable benchmarks, we re-organize two existing datasets and make them tailored for composition-IL. Then, we propose a prompt-based Composition Incremental Learner (CompILer), to overcome the ambiguous composition boundary problem which challenges composition-IL largely. Specifically, we exploit multi-pool prompt learning, which is regularized by inter-pool prompt discrepancy and intra-pool prompt diversity. Besides, we devise object-injected state prompting by using object prompts to guide the selection of state prompts. Furthermore, we fuse the selected prompts by a generalized-mean strategy, to eliminate irrelevant information learned in the prompts. Extensive experiments on two datasets exhibit state-of-the-art performance achieved by CompILer.

</details>

## 跨领域论文（完整笔记在其他领域）

- SDDGR: Stable Diffusion-Based Deep Generative Replay for Class Incremental Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- Boosting Continual Learning of Vision-Language Models via Mixture-of-Experts Adapters. → [vlm](../vlm/Guideline%202024.md)
<!-- COMPLETE v1 papers=116 -->
