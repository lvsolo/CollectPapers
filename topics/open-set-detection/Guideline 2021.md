# Open-set Detection — 2021 Guideline

> 领域: 开放类检测总类（开放词表 OVD / 开放世界 OWOD / 开集 OOD / 未知类检测）
> 论文数: 1 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Open-Vocabulary Object Detection Using Captions.
- **链接**: [arXiv:2011.10678](https://arxiv.org/abs/2011.10678) · 📚 被引 404
- **作者**: Alireza Zareian, Kevin Dela Rosa, Derek Hao Hu, Shih-Fu Chang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite the remarkable accuracy of deep neural networks in object detection, they are costly to train and scale due to supervision requirements. Particularly, learning more object categories typically requires proportionally more bounding box annotations. Weakly supervised and zero-shot learning techniques have been explored to scale object detectors to more categories with less supervision, but they have not been as successful and widely adopted as supervised models. In this paper, we put forth a novel formulation of the object detection problem, namely open-vocabulary object detection, which is more general, more practical, and more effective than weakly supervised and zero-shot approaches. We propose a new method to train object detectors using bounding box annotations for a limited set of object categories, as well as image-caption pairs that cover a larger variety of objects at a significantly lower cost. We show that the proposed method can detect and localize objects for which no bounding box annotation is provided during training, at a significantly higher accuracy than zero-shot approaches. Meanwhile, objects with bounding box annotation can be detected almost as accurately as supervised methods, which is significantly better than weakly supervised baselines. Accordingly, we establish a new state of the art for scalable object detection.

</details>

## 🆕 增量新增

### Class-Aware Robust Adversarial Training for Object Detection. **⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2103.16148](https://arxiv.org/abs/2103.16148) · 📚 被引 52
- **作者**: Pin-Chun Chen, Bo-Han Kung, Jun-Cheng Chen
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: ①针对目标检测任务在对抗攻击下的鲁棒性不足问题。②提出了一种类感知鲁棒对抗训练范式，通过生成通用对抗扰动同时攻击图像中所有目标，并将总损失分解为类级损失并按类归一化。③相比以往仅关注分类任务的方法，该方法平衡了各类别的影响，均匀提升所有类别的鲁棒性。④摘要未提供具体数值，但声称相比先前防御方法有显著改进。
- **摘要（英）**: This paper addresses adversarial robustness in object detection by proposing a class-aware robust adversarial training paradigm. It generates universal perturbations to attack all objects and decomposes loss into class-wise components for balanced robustness. The method improves robustness across classes compared to prior defenses, though specific metrics are not provided.
- **核心贡献**: 提出类感知对抗训练方法提升目标检测鲁棒性。
- **创新点**: 类级损失归一化实现均匀鲁棒性提升。
- **结果**: 声称优于先前方法，但无具体数据。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Object detection is an important computer vision task with plenty of real-world applications; therefore, how to enhance its robustness against adversarial attacks has emerged as a crucial issue. However, most of the previous defense methods focused on the classification task and had few analysis in the context of the object detection task. In this work, to address the issue, we present a novel class-aware robust adversarial training paradigm for the object detection task. For a given image, the proposed approach generates an universal adversarial perturbation to simultaneously attack all the occurred objects in the image through jointly maximizing the respective loss for each object. Meanwhile, instead of normalizing the total loss with the number of objects, the proposed approach decomposes the total loss into class-wise losses and normalizes each class loss using the number of objects for the class. The adversarial training based on the class weighted loss can not only balances the influence of each class but also effectively and evenly improves the adversarial robustness of trained models for all the object classes as compared with the previous defense methods. Furthermore, with the recent development of fast adversarial training, we provide a fast version of the proposed algorithm which can be trained faster than the traditional adversarial training while keeping comparable performance. With extensive experiments on the challenging PASCAL-VOC and MS-COCO datasets, the evaluation results demonstrate that the proposed defense methods can effectively enhance the robustness of the object detection models.

</details>

### Dense Relation Distillation With Context-Aware Aggregation for Few-Shot Object Detection. **⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2103.17115](https://arxiv.org/abs/2103.17115) · 📚 被引 192
- **作者**: Hanzhe Hu, Shuai Bai, Aoxue Li, Jinshi Cui, Liwei Wang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: 针对小样本目标检测中仅靠少量标注难以捕捉新类细粒度特征的问题，提出DCNet。方法基于元学习框架，包含密集关系蒸馏模块，将支持特征与查询特征在空间位置上密集匹配，以充分利用支持信息；并引入上下文感知聚合模块，自适应融合多尺度特征。相比已有方法，该工作更全面地利用支持特征，增强了对外观变化和遮挡的鲁棒性。实验表明在多个小样本检测基准上取得了显著性能提升。
- **摘要（英）**: To address the challenge of capturing fine-grained features of novel classes with limited annotations in few-shot object detection, this paper proposes DCNet, built on a meta-learning framework. It introduces a dense relation distillation module for dense spatial matching between support and query features, and a context-aware aggregation module for adaptive multi-scale feature fusion. This approach more fully exploits support features, improving robustness to appearance changes and occlusions, and achieves significant performance gains on benchmarks.
- **核心贡献**: 提出DCNet，通过密集关系蒸馏和上下文感知聚合解决小样本检测中支持特征利用不足的问题。
- **创新点**: 创新性地引入密集空间匹配的蒸馏机制和自适应多尺度聚合模块。
- **结果**: 在多个小样本检测基准上取得显著性能提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Conventional deep learning based methods for object detection require a large amount of bounding box annotations for training, which is expensive to obtain such high quality annotated data. Few-shot object detection, which learns to adapt to novel classes with only a few annotated examples, is very challenging since the fine-grained feature of novel object can be easily overlooked with only a few data available. In this work, aiming to fully exploit features of annotated novel object and capture fine-grained features of query object, we propose Dense Relation Distillation with Context-aware Aggregation (DCNet) to tackle the few-shot detection problem. Built on the meta-learning based framework, Dense Relation Distillation module targets at fully exploiting support features, where support features and query feature are densely matched, covering all spatial locations in a feed-forward fashion. The abundant usage of the guidance information endows model the capability to handle common challenges such as appearance changes and occlusions. Moreover, to better capture scale-aware features, Context-aware Aggregation module adaptively harnesses features from different scales for a more comprehensive feature representation. Extensive experiments illustrate that our proposed approach achieves state-of-the-art results on PASCAL VOC and MS COCO datasets. Code will be made available at https://github.com/hzhupku/DCNet.

</details>

### Beyond Max-Margin: Class Margin Equilibrium for Few-Shot Object Detection. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2103.04612](https://arxiv.org/abs/2103.04612) · 📚 被引 180
- **作者**: Bohao Li, Boyu Yang, Chang Liu, Feng Liu, Rongrong Ji, Qixiang Ye
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: 针对小样本目标检测中基类分类需最大间隔而新类表示需最小间隔的矛盾，提出类边界均衡（CME）方法。该方法将检测问题转化为分类问题，通过全连接层解耦定位特征，并引入类边界损失在特征学习中为新类保留足够间隔空间，最后通过对抗扰动新类实例特征实现边界均衡。相比已有工作，CME系统性地优化了特征空间划分和新类重建。实验表明在多个基准上优于现有方法。
- **摘要（英）**: This paper addresses the contradiction between max-margin for base class classification and min-margin for novel class representation in few-shot object detection. It proposes a class margin equilibrium (CME) approach that converts detection to classification via a fully connected layer, reserves margin space with a class margin loss, and achieves equilibrium through adversarial feature perturbation. CME systematically optimizes feature space partitioning and novel class reconstruction, outperforming existing methods on benchmarks.
- **核心贡献**: 提出类边界均衡方法，解决小样本检测中分类与表示之间的间隔矛盾。
- **创新点**: 创新性地引入对抗扰动实现类边界均衡。
- **结果**: 在多个基准上优于现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Few-shot object detection has made substantial progressby representing novel class objects using the feature representation learned upon a set of base class objects. However,an implicit contradiction between novel class classification and representation is unfortunately ignored. On the one hand, to achieve accurate novel class classification, the distributions of either two base classes must be far away fromeach other (max-margin). On the other hand, to precisely represent novel classes, the distributions of base classes should be close to each other to reduce the intra-class distance of novel classes (min-margin). In this paper, we propose a class margin equilibrium (CME) approach, with the aim to optimize both feature space partition and novel class reconstruction in a systematic way. CME first converts the few-shot detection problem to the few-shot classification problem by using a fully connected layer to decouple localization features. CME then reserves adequate margin space for novel classes by introducing simple-yet-effective class margin loss during feature learning. Finally, CME pursues margin equilibrium by disturbing the features of novel class instances in an adversarial min-max fashion. Experiments on Pascal VOC and MS-COCO datasets show that CME significantly improves upon two baseline detectors (up to $3\sim 5\%$ in average), achieving state-of-the-art performance. Code is available at https://github.com/Bohao-Lee/CME .

</details>

### MeGA-CDA: Memory Guided Attention for Category-Aware Unsupervised Domain Adaptive Object Detection. **⭐⭐⭐** (相关度: 65%)
- **链接**: [arXiv:2103.04224](https://arxiv.org/abs/2103.04224) · 📚 被引 160
- **作者**: Vibashan VS, Vikram Gupta, Poojan Oza, Vishwanath A. Sindagi, Vishal M. Patel
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: 针对无监督域自适应目标检测中类别无关对齐导致负迁移的问题，提出MeGA-CDA方法。该方法采用类别判别器实现类别感知的特征对齐，并利用记忆引导的类别特定注意力图将目标特征路由到对应判别器。相比已有对抗训练方法，MeGA-CDA有效整合了类别信息，避免了负迁移。在多个基准数据集上评估，性能优于现有方法。
- **摘要（英）**: To address negative transfer from category-agnostic alignment in unsupervised domain adaptive object detection, this paper proposes MeGA-CDA, which employs category-wise discriminators and memory-guided category-specific attention maps to route features appropriately. This approach incorporates category information into domain adaptation, avoiding negative transfer and outperforming existing methods on benchmarks.
- **核心贡献**: 提出记忆引导注意力实现类别感知的域自适应目标检测。
- **创新点**: 创新性地使用记忆引导注意力生成类别特定特征路由。
- **结果**: 在多个基准上优于现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing approaches for unsupervised domain adaptive object detection perform feature alignment via adversarial training. While these methods achieve reasonable improvements in performance, they typically perform category-agnostic domain alignment, thereby resulting in negative transfer of features. To overcome this issue, in this work, we attempt to incorporate category information into the domain adaptation process by proposing Memory Guided Attention for Category-Aware Domain Adaptation (MeGA-CDA). The proposed method consists of employing category-wise discriminators to ensure category-aware feature alignment for learning domain-invariant discriminative features. However, since the category information is not available for the target samples, we propose to generate memory-guided category-specific attention maps which are then used to route the features appropriately to the corresponding category discriminator. The proposed method is evaluated on several benchmark datasets and is shown to outperform existing approaches.

</details>

### Hallucination Improves Few-Shot Object Detection. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2105.01294](https://arxiv.org/abs/2105.01294) · 📚 被引 115
- **作者**: Weilin Zhang, Yu-Xiong Wang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: 针对极少量样本（少于三个）下小样本检测中训练数据缺乏多样性的问题，提出幻觉网络生成额外的训练样本。该方法学习从基类迁移共享的类内变化，在RoI特征空间中生成有用的训练示例，并集成到现代检测模型中。相比已有方法，该工作有效解决了数据稀缺问题。在COCO基准的极少量样本场景下取得了新的最先进性能。
- **摘要（英）**: To address the lack of variation in extremely few-shot detection (less than three examples), this paper proposes a hallucinator network that transfers shared within-class variation from base classes to generate additional training examples in RoI feature space. Integrated into modern detectors, this approach significantly improves performance, achieving state-of-the-art results in the extremely-few-shot regime on COCO.
- **核心贡献**: 提出幻觉网络生成RoI特征空间中的额外训练样本，提升极少量样本检测性能。
- **创新点**: 创新性地利用基类类内变化生成新类样本。
- **结果**: 在COCO极少量样本场景下取得新的最先进性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Learning to detect novel objects from few annotated examples is of great practical importance. A particularly challenging yet common regime occurs when there are extremely limited examples (less than three). One critical factor in improving few-shot detection is to address the lack of variation in training data. We propose to build a better model of variation for novel classes by transferring the shared within-class variation from base classes. To this end, we introduce a hallucinator network that learns to generate additional, useful training examples in the region of interest (RoI) feature space, and incorporate it into a modern object detection model. Our approach yields significant performance improvements on two state-of-the-art few-shot detectors with different proposal generation procedures. In particular, we achieve new state of the art in the extremely-few-shot regime on the challenging COCO benchmark.

</details>

### Semantic Relation Reasoning for Shot-Stable Few-Shot Object Detection. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2103.01903](https://arxiv.org/abs/2103.01903) · 📚 被引 205
- **作者**: Chenchen Zhu, Fangyi Chen, Uzair Ahmed, Zhiqiang Shen, Marios Savvides
- **🏷️ 机构**: Carnegie Mellon University
- **会议**: CVPR 2021
- **摘要（中）**: 针对小样本检测中数据稀缺且性能受样本数影响大的问题，提出利用新类与基类间语义关系的方法。该方法将每个类别表示为从文本语料学习的语义嵌入，训练检测器将图像特征投影到该嵌入空间，并引入动态关系图增强嵌入。相比直接使用原始嵌入和启发式知识图谱，该方法更鲁棒和稳定。实验表明在较高样本数下取得竞争性结果，在较低样本数下性能显著提升。
- **摘要（英）**: This paper addresses data scarcity in few-shot detection by leveraging semantic relations between novel and base classes. It represents classes with semantic embeddings from text corpora, trains detectors to project image features into this space, and augments embeddings with a dynamic relation graph. This approach is robust to shot variations, achieving competitive results at higher shots and significantly better performance at lower shots.
- **核心贡献**: 提出基于语义关系推理的小样本检测器，利用动态关系图增强类表示。
- **创新点**: 创新性地将语义嵌入和动态关系图结合用于检测。
- **结果**: 在低样本数下性能显著提升，高样本数下保持竞争性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Few-shot object detection is an imperative and long-lasting problem due to the inherent long-tail distribution of real-world data. Its performance is largely affected by the data scarcity of novel classes. But the semantic relation between the novel classes and the base classes is constant regardless of the data availability. In this work, we investigate utilizing this semantic relation together with the visual information and introduce explicit relation reasoning into the learning of novel object detection. Specifically, we represent each class concept by a semantic embedding learned from a large corpus of text. The detector is trained to project the image representations of objects into this embedding space. We also identify the problems of trivially using the raw embeddings with a heuristic knowledge graph and propose to augment the embeddings with a dynamic relation graph. As a result, our few-shot detector, termed SRR-FSD, is robust and stable to the variation of shots of novel objects. Experiments show that SRR-FSD can achieve competitive results at higher shots, and more importantly, a significantly better performance given both lower explicit and implicit shots. The benchmark protocol with implicit shots removed from the pretrained classification dataset can serve as a more realistic setting for future research.

</details>

### Few-Shot Object Detection via Association and DIscrimination. **⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2111.11656](https://arxiv.org/abs/2111.11656)
- **作者**: Yuhang Cao, Jiaqi Wang, Ying Jin, Tong Wu, Kai Chen, Ziwei Liu et al.
- **🏷️ 机构**: CUHK
- **会议**: NeurIPS 2021
- **摘要（中）**: ①针对少样本目标检测中微调阶段新类特征空间分散、类间可分性差的问题。②提出两阶段微调框架FADI，包含关联步骤（显式模仿特定基类特征空间构建紧凑新类特征）和判别步骤（增强类间区分）。③相比现有整体微调范式，通过显式关联而非隐式利用多基类知识，改善特征空间结构。④在标准少样本检测基准上验证了有效性，但摘要未提供具体数值。
- **摘要（英）**: This paper addresses the issue of scattered feature spaces and poor inter-class separability for novel classes in few-shot object detection during fine-tuning. It proposes a two-step fine-tuning framework FADI with an association step to construct compact novel class features by imitating specific base classes, and a discrimination step to enhance separability. The method improves over holistic fine-tuning paradigms by explicit association, with effectiveness demonstrated on benchmarks though no specific numbers are given in the abstract.
- **核心贡献**: 提出FADI两阶段微调框架，通过显式基类关联构建紧凑新类特征空间。
- **创新点**: 将隐式多基类知识利用改为显式单基类特征模仿，改善特征空间结构。
- **结果**: 在少样本检测基准上验证了有效性，但未提供具体数据。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Object detection has achieved substantial progress in the last decade. However, detecting novel classes with only few samples remains challenging, since deep learning under low data regime usually leads to a degraded feature space. Existing works employ a holistic fine-tuning paradigm to tackle this problem, where the model is first pre-trained on all base classes with abundant samples, and then it is used to carve the novel class feature space. Nonetheless, this paradigm is still imperfect. Durning fine-tuning, a novel class may implicitly leverage the knowledge of multiple base classes to construct its feature space, which induces a scattered feature space, hence violating the inter-class separability. To overcome these obstacles, we propose a two-step fine-tuning framework, Few-shot object detection via Association and DIscrimination (FADI), which builds up a discriminative feature space for each novel class with two integral steps. 1) In the association step, in contrast to implicitly leveraging multiple base classes, we construct a compact novel class feature space via explicitly imitating a specific base class feature space. Specifically, we associate each novel class with a base class according to their semantic similarity. After that, the feature space of a novel class can readily imitate the well-trained feature space of the associated base class. 2) In the discrimination step, to ensure the separability between the novel classes and associated base classes, we disentangle the classification branches for base and novel classes. To further enlarge the inter-class separability between all classes, a set-specialized margin loss is imposed. Extensive experiments on Pascal VOC and MS-COCO datasets demonstrate FADI achieves new SOTA performance, significantly improving the baseline in any shot/split by +18.7. Notably, the advantage is most announced on extremely few-shot scenarios.

</details>

### Mixed Supervised Object Detection by Transferring Mask Prior and Semantic Similarity. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2110.14191](https://arxiv.org/abs/2110.14191)
- **作者**: Yan Liu, Zhijie Zhang, Li Niu, Junjie Chen, Liqing Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021
- **摘要（中）**: ①针对混合监督目标检测中仅用弱标注学习新类、全标注基类辅助的问题，现有方法仅迁移类不可知目标性。②提出迁移掩码先验和语义相似性：掩码先验帮助检测目标，语义相似性用于去噪伪全标注。③相比现有工作，额外利用掩码和语义信息缩小新类与基类差距。④在三个基准数据集上实验证明优于现有方法，代码已开源。
- **摘要（英）**: This paper tackles mixed supervised object detection where novel categories are learned with weak annotations aided by fully annotated base categories. It transfers mask prior and semantic similarity from base to novel categories, using mask prior to improve detection and semantic similarity to denoise pseudo full annotations. Experiments on three benchmarks show superiority over existing methods, with code released.
- **核心贡献**: 提出TraMaS方法，迁移掩码先验和语义相似性以增强混合监督目标检测。
- **创新点**: 首次在混合监督检测中同时利用掩码先验和语义相似性进行知识迁移和伪标注去噪。
- **结果**: 在三个基准数据集上优于现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Object detection has achieved promising success, but requires large-scale fully-annotated data, which is time-consuming and labor-extensive. Therefore, we consider object detection with mixed supervision, which learns novel object categories using weak annotations with the help of full annotations of existing base object categories. Previous works using mixed supervision mainly learn the class-agnostic objectness from fully-annotated categories, which can be transferred to upgrade the weak annotations to pseudo full annotations for novel categories. In this paper, we further transfer mask prior and semantic similarity to bridge the gap between novel categories and base categories. Specifically, the ability of using mask prior to help detect objects is learned from base categories and transferred to novel categories. Moreover, the semantic similarity between objects learned from base categories is transferred to denoise the pseudo full annotations for novel categories. Experimental results on three benchmark datasets demonstrate the effectiveness of our method over existing methods. Codes are available at https://github.com/bcmi/TraMaS-Weak-Shot-Object-Detection.

</details>

## 跨领域论文（完整笔记在其他领域）

- Self-Supervised Pillar Motion Learning for Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202021.md)
<!-- COMPLETE v1 papers=9 -->
