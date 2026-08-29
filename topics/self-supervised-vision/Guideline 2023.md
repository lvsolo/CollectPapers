# Self-supervised Vision — 2023 Guideline

> 领域: 视觉自监督学习（对比学习、MAE、DINO 系）
> 论文数: 67 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### What Do Self-Supervised Vision Transformers Learn?
- **链接**: [arXiv:2305.00729](https://arxiv.org/abs/2305.00729) · [代码](https://github.com/naver-ai/cl-vs-mim)
- **作者**: Namuk Park, Wonjae Kim, Byeongho Heo, Taekyung Kim, Sangdoo Yun
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a comparative study on how and why contrastive learning (CL) and masked image modeling (MIM) differ in their representations and in their performance of downstream tasks. In particular, we demonstrate that self-supervised Vision Transformers (ViTs) have the following properties: (1) CL trains self-attentions to capture longer-range global patterns than MIM, such as the shape of an object, especially in the later layers of the ViT architecture. This CL property helps ViTs linearly separate images in their representation spaces. However, it also makes the self-attentions collapse into homogeneity for all query tokens and heads. Such homogeneity of self-attention reduces the diversity of representations, worsening scalability and dense prediction performance. (2) CL utilizes the low-frequency signals of the representations, but MIM utilizes high-frequencies. Since low- and high-frequency information respectively represent shapes and textures, CL is more shape-oriented and MIM more texture-oriented. (3) CL plays a crucial role in the later layers, while MIM mainly focuses on the early layers. Upon these analyses, we find that CL and MIM can complement each other and observe that even the simplest harmonization can help leverage the advantages of both methods. The code is available at https://github.com/naver-ai/cl-vs-mim.

</details>

### Hyperbolic Self-paced Learning for Self-supervised Skeleton-based Action Representations.
- **链接**: [arXiv:2303.06242](https://arxiv.org/abs/2303.06242) · [代码](https://github.com/paolomandica/HYSP)
- **作者**: Luca Franco, Paolo Mandica, Bharti Munjal, Fabio Galasso
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-paced learning has been beneficial for tasks where some initial knowledge is available, such as weakly supervised learning and domain adaptation, to select and order the training sample sequence, from easy to complex. However its applicability remains unexplored in unsupervised learning, whereby the knowledge of the task matures during training. We propose a novel HYperbolic Self-Paced model (HYSP) for learning skeleton-based action representations. HYSP adopts self-supervision: it uses data augmentations to generate two views of the same sample, and it learns by matching one (named online) to the other (the target). We propose to use hyperbolic uncertainty to determine the algorithmic learning pace, under the assumption that less uncertain samples should be more strongly driving the training, with a larger weight and pace. Hyperbolic uncertainty is a by-product of the adopted hyperbolic neural networks, it matures during training and it comes with no extra cost, compared to the established Euclidean SSL framework counterparts. When tested on three established skeleton-based action recognition datasets, HYSP outperforms the state-of-the-art on PKU-MMD I, as well as on 2 out of 3 downstream tasks on NTU-60 and NTU-120. Additionally, HYSP only uses positive pairs and bypasses therefore the complex and computationally-demanding mining procedures required for the negatives in contrastive techniques. Code is available at https://github.com/paolomandica/HYSP.

</details>

### MAST: Masked Augmentation Subspace Training for Generalizable Self-Supervised Priors.
- **链接**: [arXiv:2303.03679](https://arxiv.org/abs/2303.03679)
- **作者**: Chen Huang, Hanlin Goh, Jiatao Gu, Joshua M. Susskind
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent Self-Supervised Learning (SSL) methods are able to learn feature representations that are invariant to different data augmentations, which can then be transferred to downstream tasks of interest. However, different downstream tasks require different invariances for their best performance, so the optimal choice of augmentations for SSL depends on the target task. In this paper, we aim to learn self-supervised features that generalize well across a variety of downstream tasks (e.g., object classification, detection and instance segmentation) without knowing any task information beforehand. We do so by Masked Augmentation Subspace Training (or MAST) to encode in the single feature space the priors from different data augmentations in a factorized way. Specifically, we disentangle the feature space into separate subspaces, each induced by a learnable mask that selects relevant feature dimensions to model invariance to a specific augmentation. We show the success of MAST in jointly capturing generalizable priors from different augmentations, using both unique and shared features across the subspaces. We further show that MAST benefits from uncertainty modeling to reweight ambiguous samples from strong augmentations that may cause similarity mismatch in each subspace. Experiments demonstrate that MAST consistently improves generalization on various downstream tasks, while being task-agnostic and efficient during SSL. We also provide interesting insights about how different augmentations are related and how uncertainty reflects learning difficulty.

</details>

### Towards the Generalization of Contrastive Self-Supervised Learning.
- **链接**: [arXiv:2111.00743](https://arxiv.org/abs/2111.00743)
- **作者**: Weiran Huang, Mingyang Yi, Xuyang Zhao, Zihao Jiang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Masked Frequency Modeling for Self-Supervised Visual Pre-Training.
- **链接**: [arXiv:2206.07706](https://arxiv.org/abs/2206.07706)
- **作者**: Jiahao Xie, Wei Li, Xiaohang Zhan, Ziwei Liu, Yew-Soon Ong, Chen Change Loy
- **🏷️ 机构**: NTU S-Lab
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present Masked Frequency Modeling (MFM), a unified frequency-domain-based approach for self-supervised pre-training of visual models. Instead of randomly inserting mask tokens to the input embeddings in the spatial domain, in this paper, we shift the perspective to the frequency domain. Specifically, MFM first masks out a portion of frequency components of the input image and then predicts the missing frequencies on the frequency spectrum. Our key insight is that predicting masked components in the frequency domain is more ideal to reveal underlying image patterns rather than predicting masked patches in the spatial domain, due to the heavy spatial redundancy. Our findings suggest that with the right configuration of mask-and-predict strategy, both the structural information within high-frequency components and the low-level statistics among low-frequency counterparts are useful in learning good representations. For the first time, MFM demonstrates that, for both ViT and CNN, a simple non-Siamese framework can learn meaningful representations even using none of the following: (i) extra data, (ii) extra model, (iii) mask token. Experimental results on image classification and semantic segmentation, as well as several robustness benchmarks show the competitive performance and advanced robustness of MFM compared with recent masked image modeling approaches. Furthermore, we also comprehensively investigate the effectiveness of classical image restoration tasks for representation learning from a unified frequency perspective and reveal their intriguing relations with our MFM approach.

</details>

### The hidden uniform cluster prior in self-supervised learning.
- **链接**: [arXiv:2210.07277](https://arxiv.org/abs/2210.07277)
- **作者**: Mido Assran, Randall Balestriero, Quentin Duval, Florian Bordes, Ishan Misra, Piotr Bojanowski et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> A successful paradigm in representation learning is to perform self-supervised pretraining using tasks based on mini-batch statistics (e.g., SimCLR, VICReg, SwAV, MSN). We show that in the formulation of all these methods is an overlooked prior to learn features that enable uniform clustering of the data. While this prior has led to remarkably semantic representations when pretraining on class-balanced data, such as ImageNet, we demonstrate that it can hamper performance when pretraining on class-imbalanced data. By moving away from conventional uniformity priors and instead preferring power-law distributed feature clusters, we show that one can improve the quality of the learned representations on real-world class-imbalanced datasets. To demonstrate this, we develop an extension of the Masked Siamese Networks (MSN) method to support the use of arbitrary features priors.

</details>

### Time to augment self-supervised visual representation learning.
- **链接**: [出版页](https://openreview.net/forum?id=o8xdgmwCP8l)
- **作者**: Arthur Aubret, Markus Roland Ernst, Céline Teulière, Jochen Triesch
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### On the Effectiveness of Out-of-Distribution Data in Self-Supervised Long-Tail Learning.
- **链接**: [arXiv:2306.04934](https://arxiv.org/abs/2306.04934) · [代码](https://github.com/JianhongBai/COLT)
- **作者**: Jianhong Bai, Zuozhu Liu, Hualiang Wang, Jin Hao, Yang Feng, Huanpeng Chu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Though Self-supervised learning (SSL) has been widely studied as a promising technique for representation learning, it doesn't generalize well on long-tailed datasets due to the majority classes dominating the feature space. Recent work shows that the long-tailed learning performance could be boosted by sampling extra in-domain (ID) data for self-supervised training, however, large-scale ID data which can rebalance the minority classes are expensive to collect. In this paper, we propose an alternative but easy-to-use and effective solution, Contrastive with Out-of-distribution (OOD) data for Long-Tail learning (COLT), which can effectively exploit OOD data to dynamically re-balance the feature space. We empirically identify the counter-intuitive usefulness of OOD samples in SSL long-tailed learning and principally design a novel SSL method. Concretely, we first localize the `head' and `tail' samples by assigning a tailness score to each OOD sample based on its neighborhoods in the feature space. Then, we propose an online OOD sampling strategy to dynamically re-balance the feature space. Finally, we enforce the model to be capable of distinguishing ID and OOD samples by a distribution-level supervised contrastive loss. Extensive experiments are conducted on various datasets and several state-of-the-art SSL frameworks to verify the effectiveness of the proposed method. The results show that our method significantly improves the performance of SSL on long-tailed datasets by a large margin, and even outperforms previous work which uses external ID data. Our code is available at https://github.com/JianhongBai/COLT.

</details>

### Rethinking Self-Supervised Visual Representation Learning in Pre-training for 3D Human Pose and Shape Estimation.
- **链接**: [arXiv:2303.05370](https://arxiv.org/abs/2303.05370)
- **作者**: Hongsuk Choi, Hyeongjin Nam, Taeryung Lee, Gyeongsik Moon, Kyoung Mu Lee
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, a few self-supervised representation learning (SSL) methods have outperformed the ImageNet classification pre-training for vision tasks such as object detection. However, its effects on 3D human body pose and shape estimation (3DHPSE) are open to question, whose target is fixed to a unique class, the human, and has an inherent task gap with SSL. We empirically study and analyze the effects of SSL and further compare it with other pre-training alternatives for 3DHPSE. The alternatives are 2D annotation-based pre-training and synthetic data pre-training, which share the motivation of SSL that aims to reduce the labeling cost. They have been widely utilized as a source of weak-supervision or fine-tuning, but have not been remarked as a pre-training source. SSL methods underperform the conventional ImageNet classification pre-training on multiple 3DHPSE benchmarks by 7.7% on average. In contrast, despite a much less amount of pre-training data, the 2D annotation-based pre-training improves accuracy on all benchmarks and shows faster convergence during fine-tuning. Our observations challenge the naive application of the current SSL pre-training to 3DHPSE and relight the value of other data types in the pre-training aspect.

</details>

### NeRF-SOS: Any-View Self-supervised Object Segmentation on Complex Scenes.
- **链接**: [arXiv:2209.08776](https://arxiv.org/abs/2209.08776)
- **作者**: Zhiwen Fan, Peihao Wang, Yifan Jiang, Xinyu Gong, Dejia Xu, Zhangyang Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural volumetric representations have shown the potential that Multi-layer Perceptrons (MLPs) can be optimized with multi-view calibrated images to represent scene geometry and appearance, without explicit 3D supervision. Object segmentation can enrich many downstream applications based on the learned radiance field. However, introducing hand-crafted segmentation to define regions of interest in a complex real-world scene is non-trivial and expensive as it acquires per view annotation. This paper carries out the exploration of self-supervised learning for object segmentation using NeRF for complex real-world scenes. Our framework, called NeRF with Self-supervised Object Segmentation NeRF-SOS, couples object segmentation and neural radiance field to segment objects in any view within a scene. By proposing a novel collaborative contrastive loss in both appearance and geometry levels, NeRF-SOS encourages NeRF models to distill compact geometry-aware segmentation clusters from their density fields and the self-supervised pre-trained 2D visual features. The self-supervised object segmentation framework can be applied to various NeRF models that both lead to photo-realistic rendering results and convincing segmentation maps for both indoor and outdoor scenarios. Extensive results on the LLFF, Tank & Temple, and BlendedMVS datasets validate the effectiveness of NeRF-SOS. It consistently surpasses other 2D-based self-supervised baselines and predicts finer semantics masks than existing supervised counterparts. Please refer to the video on our project page for more details:https://zhiwenfan.github.io/NeRF-SOS.

</details>

### Corrupted Image Modeling for Self-Supervised Visual Pre-Training.
- **链接**: [arXiv:2202.03382](https://arxiv.org/abs/2202.03382) · 📚 被引 13
- **作者**: Yuxin Fang, Li Dong, Hangbo Bao, Xinggang Wang, Furu Wei
- **🏷️ 机构**: Nanyang Technological University,S-Lab
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce Corrupted Image Modeling (CIM) for self-supervised visual pre-training. CIM uses an auxiliary generator with a small trainable BEiT to corrupt the input image instead of using artificial [MASK] tokens, where some patches are randomly selected and replaced with plausible alternatives sampled from the BEiT output distribution. Given this corrupted image, an enhancer network learns to either recover all the original image pixels, or predict whether each visual token is replaced by a generator sample or not. The generator and the enhancer are simultaneously trained and synergistically updated. After pre-training, the enhancer can be used as a high-capacity visual encoder for downstream tasks. CIM is a general and flexible visual pre-training framework that is suitable for various network architectures. For the first time, CIM demonstrates that both ViT and CNN can learn rich visual representations using a unified, non-Siamese framework. Experimental results show that our approach achieves compelling results in vision benchmarks, such as ImageNet classification and ADE20K semantic segmentation.

</details>

### On the duality between contrastive and non-contrastive self-supervised learning.
- **链接**: [arXiv:2206.02574](https://arxiv.org/abs/2206.02574)
- **作者**: Quentin Garrido, Yubei Chen, Adrien Bardes, Laurent Najman, Yann LeCun
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent approaches in self-supervised learning of image representations can be categorized into different families of methods and, in particular, can be divided into contrastive and non-contrastive approaches. While differences between the two families have been thoroughly discussed to motivate new approaches, we focus more on the theoretical similarities between them. By designing contrastive and covariance based non-contrastive criteria that can be related algebraically and shown to be equivalent under limited assumptions, we show how close those families can be. We further study popular methods and introduce variations of them, allowing us to relate this theoretical result to current practices and show the influence (or lack thereof) of design choices on downstream performance. Motivated by our equivalence result, we investigate the low performance of SimCLR and show how it can match VICReg's with careful hyperparameter tuning, improving significantly over known baselines. We also challenge the popular assumption that non-contrastive methods need large output dimensions. Our theoretical and quantitative results suggest that the numerical gaps between contrastive and non-contrastive methods in certain regimes can be closed given better network design choices and hyperparameter tuning. The evidence shows that unifying different SOTA methods is an important direction to build a better understanding of self-supervised learning.

</details>

### Multi-task Self-supervised Graph Neural Networks Enable Stronger Task Generalization.
- **链接**: [arXiv:2210.02016](https://arxiv.org/abs/2210.02016) · [代码](https://github.com/jumxglhf/ParetoGNN)
- **作者**: Mingxuan Ju, Tong Zhao, Qianlong Wen, Wenhao Yu, Neil Shah, Yanfang Ye et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning (SSL) for graph neural networks (GNNs) has attracted increasing attention from the graph machine learning community in recent years, owing to its capability to learn performant node embeddings without costly label information. One weakness of conventional SSL frameworks for GNNs is that they learn through a single philosophy, such as mutual information maximization or generative reconstruction. When applied to various downstream tasks, these frameworks rarely perform equally well for every task, because one philosophy may not span the extensive knowledge required for all tasks. To enhance the task generalization across tasks, as an important first step forward in exploring fundamental graph models, we introduce PARETOGNN, a multi-task SSL framework for node representation learning over graphs. Specifically, PARETOGNN is self-supervised by manifold pretext tasks observing multiple philosophies. To reconcile different philosophies, we explore a multiple-gradient descent algorithm, such that PARETOGNN actively learns from every pretext task while minimizing potential conflicts. We conduct comprehensive experiments over four downstream tasks (i.e., node classification, node clustering, link prediction, and partition prediction), and our proposal achieves the best overall performance across tasks on 11 widely adopted benchmark datasets. Besides, we observe that learning from multiple philosophies enhances not only the task generalization but also the single task performances, demonstrating that PARETOGNN achieves better task generalization via the disjoint yet complementary knowledge learned from different philosophies. Our code is publicly available at https://github.com/jumxglhf/ParetoGNN.

</details>

### Diffusion Adversarial Representation Learning for Self-supervised Vessel Segmentation.
- **链接**: [arXiv:2209.14566](https://arxiv.org/abs/2209.14566)
- **作者**: Boah Kim, Yujin Oh, Jong Chul Ye
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vessel segmentation in medical images is one of the important tasks in the diagnosis of vascular diseases and therapy planning. Although learning-based segmentation approaches have been extensively studied, a large amount of ground-truth labels are required in supervised methods and confusing background structures make neural networks hard to segment vessels in an unsupervised manner. To address this, here we introduce a novel diffusion adversarial representation learning (DARL) model that leverages a denoising diffusion probabilistic model with adversarial learning, and apply it to vessel segmentation. In particular, for self-supervised vessel segmentation, DARL learns the background signal using a diffusion module, which lets a generation module effectively provide vessel representations. Also, by adversarial learning based on the proposed switchable spatially-adaptive denormalization, our model estimates synthetic fake vessel images as well as vessel segmentation masks, which further makes the model capture vessel-relevant semantic information. Once the proposed model is trained, the model generates segmentation masks in a single step and can be applied to general vascular structure segmentation of coronary angiography and retinal images. Experimental results on various datasets show that our method significantly outperforms existing unsupervised and self-supervised vessel segmentation methods.

</details>

### Temperature Schedules for self-supervised contrastive methods on long-tail data.
- **链接**: [arXiv:2303.13664](https://arxiv.org/abs/2303.13664)
- **作者**: Anna Kukleva, Moritz Böhle, Bernt Schiele, Hilde Kuehne, Christian Rupprecht
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Most approaches for self-supervised learning (SSL) are optimised on curated balanced datasets, e.g. ImageNet, despite the fact that natural data usually exhibits long-tail distributions. In this paper, we analyse the behaviour of one of the most popular variants of SSL, i.e. contrastive methods, on long-tail data. In particular, we investigate the role of the temperature parameter $τ$ in the contrastive loss, by analysing the loss through the lens of average distance maximisation, and find that a large $τ$ emphasises group-wise discrimination, whereas a small $τ$ leads to a higher degree of instance discrimination. While $τ$ has thus far been treated exclusively as a constant hyperparameter, in this work, we propose to employ a dynamic $τ$ and show that a simple cosine schedule can yield significant improvements in the learnt representations. Such a schedule results in a constant `task switching' between an emphasis on instance discrimination and group-wise discrimination and thereby ensures that the model learns both group-wise features, as well as instance-specific details. Since frequent classes benefit from the former, while infrequent classes require the latter, we find this method to consistently improve separation between the classes in long-tail data without any additional computational cost.

</details>

### Simplicial Embeddings in Self-Supervised Learning and Downstream Classification.
- **链接**: [arXiv:2204.00616](https://arxiv.org/abs/2204.00616)
- **作者**: Samuel Lavoie, Christos Tsirigotis, Max Schwarzer, Ankit Vani, Michael Noukhovitch, Kenji Kawaguchi et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Simplicial Embeddings (SEM) are representations learned through self-supervised learning (SSL), wherein a representation is projected into $L$ simplices of $V$ dimensions each using a softmax operation. This procedure conditions the representation onto a constrained space during pretraining and imparts an inductive bias for group sparsity. For downstream classification, we formally prove that the SEM representation leads to better generalization than an unnormalized representation. Furthermore, we empirically demonstrate that SSL methods trained with SEMs have improved generalization on natural image datasets such as CIFAR-100 and ImageNet. Finally, when used in a downstream classification task, we show that SEM features exhibit emergent semantic coherence where small groups of learned features are distinctly predictive of semantically-relevant classes.

</details>

### Self-Supervised Set Representation Learning for Unsupervised Meta-Learning.
- **链接**: [出版页](https://openreview.net/forum?id=kIAx30hYi_p)
- **作者**: Dong Bok Lee, Seanie Lee, Kenji Kawaguchi, Yunji Kim, Jihwan Bang, Jung-Woo Ha et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Exploring The Role of Mean Teachers in Self-supervised Masked Auto-Encoders.
- **链接**: [arXiv:2210.02077](https://arxiv.org/abs/2210.02077)
- **作者**: Youngwan Lee, Jeffrey Ryan Willette, Jonghee Kim, Juho Lee, Sung Ju Hwang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Masked image modeling (MIM) has become a popular strategy for self-supervised learning~(SSL) of visual representations with Vision Transformers. A representative MIM model, the masked auto-encoder (MAE), randomly masks a subset of image patches and reconstructs the masked patches given the unmasked patches. Concurrently, many recent works in self-supervised learning utilize the student/teacher paradigm which provides the student with an additional target based on the output of a teacher composed of an exponential moving average (EMA) of previous students. Although common, relatively little is known about the dynamics of the interaction between the student and teacher. Through analysis on a simple linear model, we find that the teacher conditionally removes previous gradient directions based on feature similarities which effectively acts as a conditional momentum regularizer. From this analysis, we present a simple SSL method, the Reconstruction-Consistent Masked Auto-Encoder (RC-MAE) by adding an EMA teacher to MAE. We find that RC-MAE converges faster and requires less memory usage than state-of-the-art self-distillation methods during pre-training, which may provide a way to enhance the practicality of prohibitively expensive self-supervised learning of Vision Transformer models. Additionally, we show that RC-MAE achieves more robustness and better performance compared to MAE on downstream tasks such as ImageNet-1K classification, object detection, and instance segmentation.

</details>

### MocoSFL: enabling cross-client collaborative self-supervised learning.
- **链接**: [出版页](https://openreview.net/forum?id=2QGJXyMNoPz)
- **作者**: Jingtao Li, Lingjuan Lyu, Daisuke Iso, Chaitali Chakrabarti, Michael Spranger
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Progressively Compressed Auto-Encoder for Self-supervised Representation Learning.
- **链接**: [出版页](https://openreview.net/forum?id=8T4qmZbTkW7)
- **作者**: Jin Li, Yaoming Wang, Xiaopeng Zhang, Yabo Chen, Dongsheng Jiang, Wenrui Dai et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Spectral Augmentation for Self-Supervised Learning on Graphs.
- **链接**: [arXiv:2210.00643](https://arxiv.org/abs/2210.00643)
- **作者**: Lu Lin, Jinghui Chen, Hongning Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Graph contrastive learning (GCL), as an emerging self-supervised learning technique on graphs, aims to learn representations via instance discrimination. Its performance heavily relies on graph augmentation to reflect invariant patterns that are robust to small perturbations; yet it still remains unclear about what graph invariance GCL should capture. Recent studies mainly perform topology augmentations in a uniformly random manner in the spatial domain, ignoring its influence on the intrinsic structural properties embedded in the spectral domain. In this work, we aim to find a principled way for topology augmentations by exploring the invariance of graphs from the spectral perspective. We develop spectral augmentation which guides topology augmentations by maximizing the spectral change. Extensive experiments on both graph and node classification tasks demonstrate the effectiveness of our method in self-supervised representation learning. The proposed method also brings promising generalization capability in transfer learning, and is equipped with intriguing robustness property under adversarial attacks. Our study sheds light on a general principle for graph topology augmentation.

</details>

### Self-Supervised Category-Level Articulated Object Pose Estimation with Part-Level SE(3) Equivariance.
- **链接**: [arXiv:2302.14268](https://arxiv.org/abs/2302.14268)
- **作者**: Xueyi Liu, Ji Zhang, Ruizhen Hu, Haibin Huang, He Wang, Li Yi
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Category-level articulated object pose estimation aims to estimate a hierarchy of articulation-aware object poses of an unseen articulated object from a known category. To reduce the heavy annotations needed for supervised learning methods, we present a novel self-supervised strategy that solves this problem without any human labels. Our key idea is to factorize canonical shapes and articulated object poses from input articulated shapes through part-level equivariant shape analysis. Specifically, we first introduce the concept of part-level SE(3) equivariance and devise a network to learn features of such property. Then, through a carefully designed fine-grained pose-shape disentanglement strategy, we expect that canonical spaces to support pose estimation could be induced automatically. Thus, we could further predict articulated object poses as per-part rigid transformations describing how parts transform from their canonical part spaces to the camera space. Extensive experiments demonstrate the effectiveness of our method on both complete and partial point clouds from synthetic and real articulated object datasets.

</details>

### Understanding The Robustness of Self-supervised Learning Through Topic Modeling.
- **链接**: [出版页](https://openreview.net/forum?id=7Cb7Faxa1OB)
- **作者**: Zeping Luo, Shiyou Wu, Cindy Weng, Mo Zhou, Rong Ge
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Weighted Ensemble Self-Supervised Learning.
- **链接**: [arXiv:2211.09981](https://arxiv.org/abs/2211.09981)
- **作者**: Yangjun Ruan, Saurabh Singh, Warren Richard Morningstar, Alexander A. Alemi, Sergey Ioffe, Ian Fischer et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Ensembling has proven to be a powerful technique for boosting model performance, uncertainty estimation, and robustness in supervised learning. Advances in self-supervised learning (SSL) enable leveraging large unlabeled corpora for state-of-the-art few-shot and supervised learning performance. In this paper, we explore how ensemble methods can improve recent SSL techniques by developing a framework that permits data-dependent weighted cross-entropy losses. We refrain from ensembling the representation backbone; this choice yields an efficient ensemble method that incurs a small training cost and requires no architectural changes or computational overhead to downstream evaluation. The effectiveness of our method is demonstrated with two state-of-the-art SSL methods, DINO (Caron et al., 2021) and MSN (Assran et al., 2022). Our method outperforms both in multiple evaluation metrics on ImageNet-1K, particularly in the few-shot setting. We explore several weighting schemes and find that those which increase the diversity of ensemble heads lead to better downstream evaluation results. Thorough experiments yield improved prior art baselines which our method still surpasses; e.g., our overall improvement with MSN ViT-B/16 is 3.9 p.p. for 1-shot learning.

</details>

### SMART: Self-supervised Multi-task pretrAining with contRol Transformers.
- **链接**: [arXiv:2301.09816](https://arxiv.org/abs/2301.09816)
- **作者**: Yanchao Sun, Shuang Ma, Ratnesh Madaan, Rogerio Bonatti, Furong Huang, Ashish Kapoor
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised pretraining has been extensively studied in language and vision domains, where a unified model can be easily adapted to various downstream tasks by pretraining representations without explicit labels. When it comes to sequential decision-making tasks, however, it is difficult to properly design such a pretraining approach that can cope with both high-dimensional perceptual information and the complexity of sequential control over long interaction horizons. The challenge becomes combinatorially more complex if we want to pretrain representations amenable to a large variety of tasks. To tackle this problem, in this work, we formulate a general pretraining-finetuning pipeline for sequential decision making, under which we propose a generic pretraining framework \textit{Self-supervised Multi-task pretrAining with contRol Transformer (SMART)}. By systematically investigating pretraining regimes, we carefully design a Control Transformer (CT) coupled with a novel control-centric pretraining objective in a self-supervised manner. SMART encourages the representation to capture the common essential information relevant to short-term control and long-term control, which is transferrable across tasks. We show by extensive experiments in DeepMind Control Suite that SMART significantly improves the learning efficiency among seen and unseen downstream tasks and domains under different learning scenarios including Imitation Learning (IL) and Reinforcement Learning (RL). Benefiting from the proposed control-centric objective, SMART is resilient to distribution shift between pretraining and finetuning, and even works well with low-quality pretraining datasets that are randomly collected.

</details>

### Effective Self-supervised Pre-training on Low-compute Networks without Distillation.
- **链接**: [arXiv:2210.02808](https://arxiv.org/abs/2210.02808)
- **作者**: Fuwen Tan, Fatemeh Sadat Saleh, Brais Martínez
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite the impressive progress of self-supervised learning (SSL), its applicability to low-compute networks has received limited attention. Reported performance has trailed behind standard supervised pre-training by a large margin, barring self-supervised learning from making an impact on models that are deployed on device. Most prior works attribute this poor performance to the capacity bottleneck of the low-compute networks and opt to bypass the problem through the use of knowledge distillation (KD). In this work, we revisit SSL for efficient neural networks, taking a closer at what are the detrimental factors causing the practical limitations, and whether they are intrinsic to the self-supervised low-compute setting. We find that, contrary to accepted knowledge, there is no intrinsic architectural bottleneck, we diagnose that the performance bottleneck is related to the model complexity vs regularization strength trade-off. In particular, we start by empirically observing that the use of local views can have a dramatic impact on the effectiveness of the SSL methods. This hints at view sampling being one of the performance bottlenecks for SSL on low-capacity networks. We hypothesize that the view sampling strategy for large neural networks, which requires matching views in very diverse spatial scales and contexts, is too demanding for low-capacity architectures. We systematize the design of the view sampling mechanism, leading to a new training methodology that consistently improves the performance across different SSL methods (e.g. MoCo-v2, SwAV, DINO), different low-size networks (e.g. MobileNetV2, ResNet18, ResNet34, ViT-Ti), and different tasks (linear probe, object detection, instance segmentation and semi-supervised learning). Our best models establish a new state-of-the-art for SSL methods on low-compute networks despite not using a KD loss term.

</details>

### Mosaic Representation Learning for Self-supervised Visual Pre-training.
- **链接**: [出版页](https://openreview.net/forum?id=JAezPMehaUu)
- **作者**: Zhaoqing Wang, Ziyu Chen, Yaqian Li, Yandong Guo, Jun Yu, Mingming Gong et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### BrainBERT: Self-supervised representation learning for intracranial recordings.
- **链接**: [arXiv:2302.14367](https://arxiv.org/abs/2302.14367)
- **作者**: Christopher Wang, Vighnesh Subramaniam, Adam Uri Yaari, Gabriel Kreiman, Boris Katz, Ignacio Cases et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We create a reusable Transformer, BrainBERT, for intracranial recordings bringing modern representation learning approaches to neuroscience. Much like in NLP and speech recognition, this Transformer enables classifying complex concepts, i.e., decoding neural data, with higher accuracy and with much less data by being pretrained in an unsupervised manner on a large corpus of unannotated neural recordings. Our approach generalizes to new subjects with electrodes in new positions and to unrelated tasks showing that the representations robustly disentangle the neural signal. Just like in NLP where one can study language by investigating what a language model learns, this approach opens the door to investigating the brain by what a model of the brain learns. As a first step along this path, we demonstrate a new analysis of the intrinsic dimensionality of the computations in different areas of the brain. To construct these representations, we combine a technique for producing super-resolution spectrograms of neural data with an approach designed for generating contextual representations of audio by masking. In the future, far more concepts will be decodable from neural recordings by using representation learning, potentially unlocking the brain like language models unlocked language.

</details>

### Energy-Inspired Self-Supervised Pretraining for Vision Models.
- **链接**: [arXiv:2302.01384](https://arxiv.org/abs/2302.01384)
- **作者**: Ze Wang, Jiang Wang, Zicheng Liu, Qiang Qiu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Motivated by the fact that forward and backward passes of a deep network naturally form symmetric mappings between input and output representations, we introduce a simple yet effective self-supervised vision model pretraining framework inspired by energy-based models (EBMs). In the proposed framework, we model energy estimation and data restoration as the forward and backward passes of a single network without any auxiliary components, e.g., an extra decoder. For the forward pass, we fit a network to an energy function that assigns low energy scores to samples that belong to an unlabeled dataset, and high energy otherwise. For the backward pass, we restore data from corrupted versions iteratively using gradient-based optimization along the direction of energy minimization. In this way, we naturally fold the encoder-decoder architecture widely used in masked image modeling into the forward and backward passes of a single vision model. Thus, our framework now accepts a wide range of pretext tasks with different data corruption methods, and permits models to be pretrained from masked image modeling, patch sorting, and image restoration, including super-resolution, denoising, and colorization. We support our findings with extensive experiments, and show the proposed method delivers comparable and even better performance with remarkably fewer epochs of training compared to the state-of-the-art self-supervised vision model pretraining methods. Our findings shed light on further exploring self-supervised vision model pretraining and pretext tasks beyond masked image modeling.

</details>

### DDM2: Self-Supervised Diffusion MRI Denoising with Generative Diffusion Models.
- **链接**: [arXiv:2302.03018](https://arxiv.org/abs/2302.03018)
- **作者**: Tiange Xiang, Mahmut Yurt, Ali B. Syed, Kawin Setsompop, Akshay Chaudhari
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Magnetic resonance imaging (MRI) is a common and life-saving medical imaging technique. However, acquiring high signal-to-noise ratio MRI scans requires long scan times, resulting in increased costs and patient discomfort, and decreased throughput. Thus, there is great interest in denoising MRI scans, especially for the subtype of diffusion MRI scans that are severely SNR-limited. While most prior MRI denoising methods are supervised in nature, acquiring supervised training datasets for the multitude of anatomies, MRI scanners, and scan parameters proves impractical. Here, we propose Denoising Diffusion Models for Denoising Diffusion MRI (DDM$^2$), a self-supervised denoising method for MRI denoising using diffusion denoising generative models. Our three-stage framework integrates statistic-based denoising theory into diffusion models and performs denoising through conditional generation. During inference, we represent input noisy measurements as a sample from an intermediate posterior distribution within the diffusion Markov chain. We conduct experiments on 4 real-world in-vivo diffusion MRI datasets and show that our DDM$^2$ demonstrates superior denoising performances ascertained with clinically-relevant visual qualitative and quantitative metrics.

</details>

### SimPer: Simple Self-Supervised Learning of Periodic Targets.
- **链接**: [arXiv:2210.03115](https://arxiv.org/abs/2210.03115) · [代码](https://github.com/YyzHarry/SimPer)
- **作者**: Yuzhe Yang, Xin Liu, Jiang Wu, Silviu Borac, Dina Katabi, Ming-Zher Poh et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> From human physiology to environmental evolution, important processes in nature often exhibit meaningful and strong periodic or quasi-periodic changes. Due to their inherent label scarcity, learning useful representations for periodic tasks with limited or no supervision is of great benefit. Yet, existing self-supervised learning (SSL) methods overlook the intrinsic periodicity in data, and fail to learn representations that capture periodic or frequency attributes. In this paper, we present SimPer, a simple contrastive SSL regime for learning periodic information in data. To exploit the periodic inductive bias, SimPer introduces customized augmentations, feature similarity measures, and a generalized contrastive loss for learning efficient and robust periodic representations. Extensive experiments on common real-world tasks in human behavior analysis, environmental sensing, and healthcare domains verify the superior performance of SimPer compared to state-of-the-art SSL methods, highlighting its intriguing properties including better data efficiency, robustness to spurious correlations, and generalization to distribution shifts. Code and data are available at: https://github.com/YyzHarry/SimPer.

</details>

### Unsupervised Semantic Segmentation with Self-supervised Object-centric Representations.
- **链接**: [arXiv:2207.05027](https://arxiv.org/abs/2207.05027)
- **作者**: Andrii Zadaianchuk, Matthäus Kleindessner, Yi Zhu, Francesco Locatello, Thomas Brox
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we show that recent advances in self-supervised feature learning enable unsupervised object discovery and semantic segmentation with a performance that matches the state of the field on supervised semantic segmentation 10 years ago. We propose a methodology based on unsupervised saliency masks and self-supervised feature clustering to kickstart object discovery followed by training a semantic segmentation network on pseudo-labels to bootstrap the system on images with multiple objects. We present results on PASCAL VOC that go far beyond the current state of the art (50.0 mIoU), and we report for the first time results on MS COCO for the whole set of 81 classes: our method discovers 34 categories with more than $20\%$ IoU, while obtaining an average IoU of 19.6 for all 81 categories.

</details>

### Self-Supervised Geometric Correspondence for Category-Level 6D Object Pose Estimation in the Wild.
- **链接**: [arXiv:2210.07199](https://arxiv.org/abs/2210.07199)
- **作者**: Kaifeng Zhang, Yang Fu, Shubhankar Borse, Hong Cai, Fatih Porikli, Xiaolong Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While 6D object pose estimation has wide applications across computer vision and robotics, it remains far from being solved due to the lack of annotations. The problem becomes even more challenging when moving to category-level 6D pose, which requires generalization to unseen instances. Current approaches are restricted by leveraging annotations from simulation or collected from humans. In this paper, we overcome this barrier by introducing a self-supervised learning approach trained directly on large-scale real-world object videos for category-level 6D pose estimation in the wild. Our framework reconstructs the canonical 3D shape of an object category and learns dense correspondences between input images and the canonical shape via surface embedding. For training, we propose novel geometrical cycle-consistency losses which construct cycles across 2D-3D spaces, across different instances and different time steps. The learned correspondence can be applied for 6D pose estimation and other downstream tasks such as keypoint transfer. Surprisingly, our method, without any human annotations or simulators, can achieve on-par or even better performance than previous supervised or semi-supervised methods on in-the-wild images. Our project page is: https://kywind.github.io/self-pose .

</details>

### Self-supervised learning with rotation-invariant kernels.
- **链接**: [arXiv:2208.00789](https://arxiv.org/abs/2208.00789)
- **作者**: Léon Zheng, Gilles Puy, Elisa Riccietti, Patrick Pérez, Rémi Gribonval
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce a regularization loss based on kernel mean embeddings with rotation-invariant kernels on the hypersphere (also known as dot-product kernels) for self-supervised learning of image representations. Besides being fully competitive with the state of the art, our method significantly reduces time and memory complexity for self-supervised training, making it implementable for very large embedding dimensions on existing devices and more easily adjustable than previous methods to settings with limited resources. Our work follows the major paradigm where the model learns to be invariant to some predefined image transformations (cropping, blurring, color jittering, etc.), while avoiding a degenerate solution by regularizing the embedding distribution. Our particular contribution is to propose a loss family promoting the embedding distribution to be close to the uniform distribution on the hypersphere, with respect to the maximum mean discrepancy pseudometric. We demonstrate that this family encompasses several regularizers of former methods, including uniformity-based and information-maximization methods, which are variants of our flexible regularization loss with different kernels. Beyond its practical consequences for state-of-the-art self-supervised learning with limited resources, the proposed generic regularization approach opens perspectives to leverage more widely the literature on kernel methods in order to improve self-supervised learning methods.

</details>

### Planckian Jitter: countering the color-crippling effects of color jitter on self-supervised training.
- **链接**: [出版页](https://openreview.net/forum?id=Pia70sP2Oi1)
- **作者**: Simone Zini, Alex Gomez-Villa, Marco Buzzelli, Bartlomiej Twardowski, Andrew D. Bagdanov, Joost van de Weijer
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### A Message Passing Perspective on Learning Dynamics of Contrastive Learning.
- **链接**: [arXiv:2303.04435](https://arxiv.org/abs/2303.04435) · [代码](https://github.com/PKU-ML/Message-Passing-Contrastive-Learning)
- **作者**: Yifei Wang, Qi Zhang, Tianqi Du, Jiansheng Yang, Zhouchen Lin, Yisen Wang
- **🏷️ 机构**: Peking University
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In recent years, contrastive learning achieves impressive results on self-supervised visual representation learning, but there still lacks a rigorous understanding of its learning dynamics. In this paper, we show that if we cast a contrastive objective equivalently into the feature space, then its learning dynamics admits an interpretable form. Specifically, we show that its gradient descent corresponds to a specific message passing scheme on the corresponding augmentation graph. Based on this perspective, we theoretically characterize how contrastive learning gradually learns discriminative features with the alignment update and the uniformity update. Meanwhile, this perspective also establishes an intriguing connection between contrastive learning and Message Passing Graph Neural Networks (MP-GNNs). This connection not only provides a unified understanding of many techniques independently developed in each community, but also enables us to borrow techniques from MP-GNNs to design new contrastive learning variants, such as graph attention, graph rewiring, jumpy knowledge techniques, etc. We believe that our message passing perspective not only provides a new theoretical understanding of contrastive learning dynamics, but also bridges the two seemingly independent areas together, which could inspire more interleaving studies to benefit from each other. The code is available at https://github.com/PKU-ML/Message-Passing-Contrastive-Learning.

</details>

### Unsupervised Meta-learning via Few-shot Pseudo-supervised Contrastive Learning.
- **链接**: [arXiv:2303.00996](https://arxiv.org/abs/2303.00996)
- **作者**: Huiwon Jang, Hankook Lee, Jinwoo Shin
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Unsupervised meta-learning aims to learn generalizable knowledge across a distribution of tasks constructed from unlabeled data. Here, the main challenge is how to construct diverse tasks for meta-learning without label information; recent works have proposed to create, e.g., pseudo-labeling via pretrained representations or creating synthetic samples via generative models. However, such a task construction strategy is fundamentally limited due to heavy reliance on the immutable pseudo-labels during meta-learning and the quality of the representations or the generated samples. To overcome the limitations, we propose a simple yet effective unsupervised meta-learning framework, coined Pseudo-supervised Contrast (PsCo), for few-shot classification. We are inspired by the recent self-supervised learning literature; PsCo utilizes a momentum network and a queue of previous batches to improve pseudo-labeling and construct diverse tasks in a progressive manner. Our extensive experiments demonstrate that PsCo outperforms existing unsupervised meta-learning methods under various in-domain and cross-domain few-shot classification benchmarks. We also validate that PsCo is easily scalable to a large-scale benchmark, while recent prior-art meta-schemes are not.

</details>

### Contrastive Learning Can Find An Optimal Basis For Approximately View-Invariant Functions.
- **链接**: [arXiv:2210.01883](https://arxiv.org/abs/2210.01883)
- **作者**: Daniel D. Johnson, Ayoub El Hanchi, Chris J. Maddison
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Contrastive learning is a powerful framework for learning self-supervised representations that generalize well to downstream supervised tasks. We show that multiple existing contrastive learning methods can be reinterpreted as learning kernel functions that approximate a fixed positive-pair kernel. We then prove that a simple representation obtained by combining this kernel with PCA provably minimizes the worst-case approximation error of linear predictors, under a straightforward assumption that positive pairs have similar labels. Our analysis is based on a decomposition of the target function in terms of the eigenfunctions of a positive-pair Markov chain, and a surprising equivalence between these eigenfunctions and the output of Kernel PCA. We give generalization bounds for downstream linear prediction using our Kernel PCA representation, and show empirically on a set of synthetic tasks that applying Kernel PCA to contrastive learning models can indeed approximately recover the Markov chain eigenfunctions, although the accuracy depends on the kernel parameterization as well as on the augmentation strength.

</details>

### Edge Guided GANs with Contrastive Learning for Semantic Image Synthesis.
- **链接**: [出版页](https://openreview.net/forum?id=qcJmsP3oE9) · 📚 被引 18
- **作者**: Hao Tang, Xiaojuan Qi, Guolei Sun, Dan Xu, Nicu Sebe, Radu Timofte et al.
- **🏷️ 机构**: Department of Information Technology and Electrical Engineering, ETH Zurich, Zurich, Switzerland, Department of Information Engineering and Computer Science (DISI), University of Trento, Trento, Italy
- **会议**: ICLR 2023

### Indiscriminate Poisoning Attacks on Unsupervised Contrastive Learning.
- **链接**: [arXiv:2202.11202](https://arxiv.org/abs/2202.11202)
- **作者**: Hao He, Kaiwen Zha, Dina Katabi
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Optimizing Bi-Encoder for Named Entity Recognition via Contrastive Learning.
- **链接**: [arXiv:2208.14565](https://arxiv.org/abs/2208.14565)
- **作者**: Sheng Zhang, Hao Cheng, Jianfeng Gao, Hoifung Poon
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Unbiased Supervised Contrastive Learning.
- **链接**: [arXiv:2211.05568](https://arxiv.org/abs/2211.05568)
- **作者**: Carlo Alberto Barbano, Benoit Dufumier, Enzo Tartaglione, Marco Grangetto, Pietro Gori
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Unsupervised visualization of image datasets using contrastive learning.
- **链接**: [arXiv:2210.09879](https://arxiv.org/abs/2210.09879)
- **作者**: Jan Niklas Böhm, Philipp Berens, Dmitry Kobak
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### LightGCL: Simple Yet Effective Graph Contrastive Learning for Recommendation.
- **链接**: [arXiv:2302.08191](https://arxiv.org/abs/2302.08191) · 📚 被引 2
- **作者**: Xuheng Cai, Chao Huang, Lianghao Xia, Xubin Ren
- **🏷️ 机构**: School of Computer Science and Technology, Anhui University, Hefei, China
- **会议**: ICLR 2023

### LiftedCL: Lifting Contrastive Learning for Human-Centric Perception.
- **链接**: [出版页](https://openreview.net/forum?id=WHlt5tLz12T)
- **作者**: Ziwei Chen, Qiang Li, Xiaofeng Wang, Wankou Yang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### From $t$-SNE to UMAP with contrastive learning.
- **链接**: [出版页](https://openreview.net/forum?id=B8a1FcY0vi)
- **作者**: Sebastian Damrich, Jan Niklas Böhm, Fred A. Hamprecht, Dmitry Kobak
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### ContraNorm: A Contrastive Learning Perspective on Oversmoothing and Beyond.
- **链接**: [arXiv:2303.06562](https://arxiv.org/abs/2303.06562)
- **作者**: Xiaojun Guo, Yifei Wang, Tianqi Du, Yisen Wang
- **🏷️ 机构**: Peking University
- **会议**: ICLR 2023

### A theoretical study of inductive biases in contrastive learning.
- **链接**: [arXiv:2211.14699](https://arxiv.org/abs/2211.14699)
- **作者**: Jeff Z. HaoChen, Tengyu Ma
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Your Contrastive Learning Is Secretly Doing Stochastic Neighbor Embedding.
- **链接**: [arXiv:2205.14814](https://arxiv.org/abs/2205.14814)
- **作者**: Tianyang Hu, Zhili Liu, Fengwei Zhou, Wenjia Wang, Weiran Huang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Graph Contrastive Learning for Skeleton-based Action Recognition.
- **链接**: [arXiv:2301.10900](https://arxiv.org/abs/2301.10900)
- **作者**: Xiaohu Huang, Hao Zhou, Jian Wang, Haocheng Feng, Junyu Han, Errui Ding et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Layer Grafted Pre-training: Bridging Contrastive Learning And Masked Image Modeling For Label-Efficient Representations.
- **链接**: [arXiv:2302.14138](https://arxiv.org/abs/2302.14138)
- **作者**: Ziyu Jiang, Yinpeng Chen, Mengchen Liu, Dongdong Chen, Xiyang Dai, Lu Yuan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Rethinking the Effect of Data Augmentation in Adversarial Contrastive Learning.
- **链接**: [arXiv:2303.01289](https://arxiv.org/abs/2303.01289)
- **作者**: Rundong Luo, Yifei Wang, Yisen Wang
- **🏷️ 机构**: Peking University
- **会议**: ICLR 2023

### On The Inadequacy of Optimizing Alignment and Uniformity in Contrastive Learning of Sentence Representations.
- **链接**: [出版页](https://openreview.net/forum?id=MxvHVNukama)
- **作者**: Zhijie Nie, Richong Zhang, Yongyi Mao
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Contrastive Learning for Unsupervised Domain Adaptation of Time Series.
- **链接**: [arXiv:2206.06243](https://arxiv.org/abs/2206.06243)
- **作者**: Yilmazcan Özyurt, Stefan Feuerriegel, Ce Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### The Trade-off between Universality and Label Efficiency of Representations from Contrastive Learning.
- **链接**: [arXiv:2303.00106](https://arxiv.org/abs/2303.00106)
- **作者**: Zhenmei Shi, Jiefeng Chen, Kunyang Li, Jayaram Raghuram, Xi Wu, Yingyu Liang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Link Prediction with Non-Contrastive Learning.
- **链接**: [arXiv:2211.14394](https://arxiv.org/abs/2211.14394)
- **作者**: William Shiao, Zhichun Guo, Tong Zhao, Evangelos E. Papalexakis, Yozen Liu, Neil Shah
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Understanding the Role of Nonlinearity in Training Dynamics of Contrastive Learning.
- **链接**: [arXiv:2206.01342](https://arxiv.org/abs/2206.01342)
- **作者**: Yuandong Tian
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### TempCLR: Temporal Alignment Representation with Contrastive Learning.
- **链接**: [arXiv:2212.13738](https://arxiv.org/abs/2212.13738)
- **作者**: Yuncong Yang, Jiawei Ma, Shiyuan Huang, Long Chen, Xudong Lin, Guangxing Han et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Video representation learning has been successful in video-text pre-training for zero-shot transfer, where each sentence is trained to be close to the paired video clips in a common feature space. For long videos, given a paragraph of description where the sentences describe different segments of the video, by matching all sentence-clip pairs, the paragraph and the full video are aligned implicitly. However, such unit-level comparison may ignore global temporal context, which inevitably limits the generalization ability. In this paper, we propose a contrastive learning framework TempCLR to compare the full video and the paragraph explicitly. As the video/paragraph is formulated as a sequence of clips/sentences, under the constraint of their temporal order, we use dynamic time warping to compute the minimum cumulative cost over sentence-clip pairs as the sequence-level distance. To explore the temporal dynamics, we break the consistency of temporal succession by shuffling video clips w.r.t. temporal granularity. Then, we obtain the representations for clips/sentences, which perceive the temporal information and thus facilitate the sequence alignment. In addition to pre-training on the video and paragraph, our approach can also generalize on the matching between video instances. We evaluate our approach on video retrieval, action step localization, and few-shot action recognition, and achieve consistent performance gain over all three tasks. Detailed ablation studies are provided to justify the approach design.

</details>

### Fairness-aware Contrastive Learning with Partially Annotated Sensitive Attributes.
- **链接**: [出版页](https://openreview.net/forum?id=woa783QMul)
- **作者**: Fengda Zhang, Kun Kuang, Long Chen, Yuxuan Liu, Chao Wu, Jun Xiao
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### ArCL: Enhancing Contrastive Learning with Augmentation-Robust Representations.
- **链接**: [arXiv:2303.01092](https://arxiv.org/abs/2303.01092)
- **作者**: Xuyang Zhao, Tianqi Du, Yisen Wang, Jun Yao, Weiran Huang
- **🏷️ 机构**: Peking University
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-Supervised Learning (SSL) is a paradigm that leverages unlabeled data for model training. Empirical studies show that SSL can achieve promising performance in distribution shift scenarios, where the downstream and training distributions differ. However, the theoretical understanding of its transferability remains limited. In this paper, we develop a theoretical framework to analyze the transferability of self-supervised contrastive learning, by investigating the impact of data augmentation on it. Our results reveal that the downstream performance of contrastive learning depends largely on the choice of data augmentation. Moreover, we show that contrastive learning fails to learn domain-invariant features, which limits its transferability. Based on these theoretical insights, we propose a novel method called Augmentation-robust Contrastive Learning (ArCL), which guarantees to learn domain-invariant features and can be easily integrated with existing contrastive learning algorithms. We conduct experiments on several datasets and show that ArCL significantly improves the transferability of contrastive learning.

</details>

### Towards a Unified Theoretical Understanding of Non-contrastive Learning via Rank Differential Mechanism.
- **链接**: [arXiv:2303.02387](https://arxiv.org/abs/2303.02387) · [代码](https://github.com/PKU-ML/Rank-Differential-Mechanism)
- **作者**: Zhijian Zhuo, Yifei Wang, Jinwen Ma, Yisen Wang
- **🏷️ 机构**: Peking University
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, a variety of methods under the name of non-contrastive learning (like BYOL, SimSiam, SwAV, DINO) show that when equipped with some asymmetric architectural designs, aligning positive pairs alone is sufficient to attain good performance in self-supervised visual learning. Despite some understandings of some specific modules (like the predictor in BYOL), there is yet no unified theoretical understanding of how these seemingly different asymmetric designs can all avoid feature collapse, particularly considering methods that also work without the predictor (like DINO). In this work, we propose a unified theoretical understanding for existing variants of non-contrastive learning. Our theory named Rank Differential Mechanism (RDM) shows that all these asymmetric designs create a consistent rank difference in their dual-branch output features. This rank difference will provably lead to an improvement of effective dimensionality and alleviate either complete or dimensional feature collapse. Different from previous theories, our RDM theory is applicable to different asymmetric designs (with and without the predictor), and thus can serve as a unified understanding of existing non-contrastive learning methods. Besides, our RDM theory also provides practical guidelines for designing many new non-contrastive variants. We show that these variants indeed achieve comparable performance to existing methods on benchmark datasets, and some of them even outperform the baselines. Our code is available at \url{https://github.com/PKU-ML/Rank-Differential-Mechanism}.

</details>

### Masked Image Modeling with Denoising Contrast.
- **链接**: [arXiv:2205.09616](https://arxiv.org/abs/2205.09616)
- **作者**: Kun Yi, Yixiao Ge, Xiaotong Li, Shusheng Yang, Dian Li, Jianping Wu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Since the development of self-supervised visual representation learning from contrastive learning to masked image modeling (MIM), there is no significant difference in essence, that is, how to design proper pretext tasks for vision dictionary look-up. MIM recently dominates this line of research with state-of-the-art performance on vision Transformers (ViTs), where the core is to enhance the patch-level visual context capturing of the network via denoising auto-encoding mechanism. Rather than tailoring image tokenizers with extra training stages as in previous works, we unleash the great potential of contrastive learning on denoising auto-encoding and introduce a pure MIM method, ConMIM, to produce simple intra-image inter-patch contrastive constraints as the sole learning objectives for masked patch prediction. We further strengthen the denoising mechanism with asymmetric designs, including image perturbations and model progress rates, to improve the network pre-training. ConMIM-pretrained models with various scales achieve competitive results on downstream image classification, semantic segmentation, object detection, and instance segmentation tasks, e.g., on ImageNet-1K classification, we achieve 83.9% top-1 accuracy with ViT-Small and 85.3% with ViT-Base without extra data for pre-training.

</details>

## 跨领域论文（完整笔记在其他领域）

- DINO: DETR with Improved DeNoising Anchor Boxes for End-to-End Object Detection. → [object-detection](../object-detection/Guideline%202023.md)
- Adversarial Training of Self-supervised Monocular Depth Estimation against Physical-World Attacks. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- Policy Pre-training for Autonomous Driving via Self-supervised Geometric Modeling. → [autonomous-driving](../autonomous-driving/Guideline%202023.md)
- Identifiability Results for Multimodal Contrastive Learning. → [multimodal](../multimodal/Guideline%202023.md)
- MIMT: Masked Image Modeling Transformer for Video Compression. → [network-pruning](../network-pruning/Guideline%202023.md)
