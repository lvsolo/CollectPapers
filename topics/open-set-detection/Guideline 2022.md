# Open-set Detection — 2022 Guideline

> 领域: 开放类检测总类（开放词表 OVD / 开放世界 OWOD / 开集 OOD / 未知类检测）
> 论文数: 6 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Open-Vocabulary One-Stage Detection with Hierarchical Visual-Language Knowledge Distillation.
- **链接**: [arXiv:2203.10593](https://arxiv.org/abs/2203.10593) · 📚 被引 39
- **作者**: Zongyang Ma, Guan Luo, Jin Gao, Liang Li, Yuxin Chen, Shaoru Wang et al.
- **🏷️ 机构**: Institute of Automation, Chinese Academy of Sciences,NLPR, Beijing Institute of Basic Medical Sciences,Brain Science Center, Nanchana Hangkong University
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-vocabulary object detection aims to detect novel object categories beyond the training set. The advanced open-vocabulary two-stage detectors employ instance-level visual-to-visual knowledge distillation to align the visual space of the detector with the semantic space of the Pre-trained Visual-Language Model (PVLM). However, in the more efficient one-stage detector, the absence of class-agnostic object proposals hinders the knowledge distillation on unseen objects, leading to severe performance degradation. In this paper, we propose a hierarchical visual-language knowledge distillation method, i.e., HierKD, for open-vocabulary one-stage detection. Specifically, a global-level knowledge distillation is explored to transfer the knowledge of unseen categories from the PVLM to the detector. Moreover, we combine the proposed global-level knowledge distillation and the common instance-level knowledge distillation to learn the knowledge of seen and unseen categories simultaneously. Extensive experiments on MS-COCO show that our method significantly surpasses the previous best one-stage detector with 11.9\% and 6.7\% $AP_{50}$ gains under the zero-shot detection and generalized zero-shot detection settings, and reduces the $AP_{50}$ performance gap from 14\% to 7.3\% compared to the best two-stage detector.

</details>

### C2 AM: Contrastive learning of Class-agnostic Activation Map for Weakly Supervised Object Localization and Semantic Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00106) · 📚 被引 144
- **作者**: Jinheng Xie, Jianfeng Xiang, Junliang Chen, Xianxu Hou, Xiaodong Zhao, Linlin Shen
- **🏷️ 机构**: School of Computer Science &#x0026; Software Engineering, Shenzhen University,China
- **会议**: CVPR 2022

> Existing open-vocabulary object detectors typically enlarge their vocabulary sizes by leveraging different forms of weak supervision. This helps generalize to novel objects at inference. Two popular forms of weak-supervision used in open-vocabulary detection (OVD) include pretrained CLIP model and image-level supervision. We note that both these modes of supervision are not optimally aligned for the detection task: CLIP is trained with image-text pairs and lacks precise localization of objects while the image-level supervision has been used with heuristics that do not accurately specify local object regions. In this work, we propose to address this problem by performing object-centric alignment of the language embeddings from the CLIP model. Furthermore, we visually ground the objects with only image-level supervision using a pseudo-labeling process that provides high-quality object proposals and helps expand the vocabulary during training. We establish a bridge between the above two object-alignment strategies via a novel weight transfer function that aggregates their complimentary strengths. In essence, the proposed model seeks to minimize the gap between object and image-centric representations in the OVD setting. On the COCO benchmark, our proposed approach achieves 36.6 AP50 on novel classes, an absolute 8.2 gain over the previous best performance. For LVIS, we surpass the state-of-the-art ViLD model by 5.0 mask AP for rare categories and 3.4 overall. Code: https://github.com/hanoonaR/object-centric-ovd.

- Unknown-Aware Object Detection: Learning What You Don't Know from Videos in the Wild. → [object-detection](../object-detection/Guideline%202022.md)
- Learning to Prompt for Open-Vocabulary Object Detection with Vision-Language Model. → [object-detection](../object-detection/Guideline%202022.md)
- Expanding Low-Density Latent Regions for Open-Set Object Detection. → [object-detection](../object-detection/Guideline%202022.md)
- Open-Vocabulary Instance Segmentation via Robust Cross-Modal Pseudo-Labeling. → [multimodal](../multimodal/Guideline%202022.md)

## 🆕 增量新增

### Open-Vocabulary DETR with Conditional Matching. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20077-9_7) · 📚 被引 191
- **作者**: Yuhang Zang, Wei Li, Kaiyang Zhou, Chen Huang, Chen Change Loy
- **🏷️ 机构**: NTU S-Lab
- **会议**: ECCV 2022
- **摘要（中）**: 该论文针对开放词汇DETR中匹配策略的局限性，提出了条件匹配方法，以改善模型对未见类别的泛化能力。通过引入条件匹配机制，使模型在训练和推理时更灵活地处理开放词汇。摘要缺失，但该方法有望提升开放词汇检测的性能。
- **摘要（英）**: This paper proposes conditional matching for open-vocabulary DETR to improve generalization to unseen categories, addressing limitations in standard matching strategies. The method likely enhances flexibility in training and inference for open-vocabulary detection.
- **核心贡献**: 提出了开放词汇DETR的条件匹配方法。
- **创新点**: 将条件匹配引入开放词汇检测框架。
- **结果**: 未提供具体实验结果。

### Prototypical VoteNet for Few-Shot 3D Point Cloud Object Detection. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2210.05593](https://arxiv.org/abs/2210.05593) · 📚 被引 3
- **作者**: Shizhen Zhao, Xiaojuan Qi
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022
- **摘要（中）**: 针对3D点云目标检测依赖大量标注数据的问题，本文提出Prototypical VoteNet用于少样本3D检测。方法引入原型投票模块和原型头模块，利用基类学习到的几何原型增强新类别的局部和全局特征。通过情景训练策略，模型能有效识别和定位新类实例。实验在FS-ScanNet和FS-SUNRGBD基准上验证了有效性，性能优于现有方法。
- **摘要（英）**: This paper addresses the heavy annotation requirement in 3D point cloud detection by proposing Prototypical VoteNet for few-shot detection. It introduces prototypical vote and head modules to leverage geometric prototypes from base classes, enhancing novel class features. Extensive experiments on FS-ScanNet and FS-SUNRGBD demonstrate superior performance.
- **核心贡献**: 提出首个基于原型学习的少样本3D点云检测方法。
- **创新点**: 利用类不可知几何原型和情景训练增强新类特征。
- **结果**: 在FS-ScanNet和FS-SUNRGBD上性能优于现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Most existing 3D point cloud object detection approaches heavily rely on large amounts of labeled training data. However, the labeling process is costly and time-consuming. This paper considers few-shot 3D point cloud object detection, where only a few annotated samples of novel classes are needed with abundant samples of base classes. To this end, we propose Prototypical VoteNet to recognize and localize novel instances, which incorporates two new modules: Prototypical Vote Module (PVM) and Prototypical Head Module (PHM). Specifically, as the 3D basic geometric structures can be shared among categories, PVM is designed to leverage class-agnostic geometric prototypes, which are learned from base classes, to refine local features of novel categories.Then PHM is proposed to utilize class prototypes to enhance the global feature of each object, facilitating subsequent object localization and classification, which is trained by the episodic training strategy. To evaluate the model in this new setting, we contribute two new benchmark datasets, FS-ScanNet and FS-SUNRGBD. We conduct extensive experiments to demonstrate the effectiveness of Prototypical VoteNet, and our proposed method shows significant and consistent improvements compared to baselines on two benchmark datasets.

</details>

### Unknown-Aware Object Detection: Learning What You Don't Know from Videos in the Wild. **⭐⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2203.03800](https://arxiv.org/abs/2203.03800) · 📚 被引 70
- **作者**: Xuefeng Du, Xin Wang, Gabriel Gozum, Yixuan Li
- **🏷️ 机构**: University of Wisconsin-Madison, Microsoft Research
- **会议**: CVPR 2022
- **摘要（中）**: ①针对开放集目标检测中模型对未知对象过度自信的问题。②提出时空未知蒸馏框架STUD，从视频中提取未知对象候选，并通过能量不确定性正则化塑造决策边界。③相比现有方法，STUD利用时空信息生成多样未知样本，提升OOD检测能力。④在OOD检测任务上取得SOTA，FPR95降低超过10%。
- **摘要（英）**: This paper proposes STUD, a spatial-temporal unknown distillation framework for open-set detection, reducing FPR95 by over 10% and achieving state-of-the-art performance.
- **核心贡献**: 提出时空未知蒸馏框架，提升OOD检测性能。
- **创新点**: 从视频中蒸馏未知对象和能量正则化。
- **结果**: FPR95降低超10%，刷新SOTA。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Building reliable object detectors that can detect out-of-distribution (OOD) objects is critical yet underexplored. One of the key challenges is that models lack supervision signals from unknown data, producing overconfident predictions on OOD objects. We propose a new unknown-aware object detection framework through Spatial-Temporal Unknown Distillation (STUD), which distills unknown objects from videos in the wild and meaningfully regularizes the model's decision boundary. STUD first identifies the unknown candidate object proposals in the spatial dimension, and then aggregates the candidates across multiple video frames to form a diverse set of unknown objects near the decision boundary. Alongside, we employ an energy-based uncertainty regularization loss, which contrastively shapes the uncertainty space between the in-distribution and distilled unknown objects. STUD establishes the state-of-the-art performance on OOD detection tasks for object detection, reducing the FPR95 score by over 10% compared to the previous best method. Code is available at https://github.com/deeplearning-wisc/stud.

</details>

### Learning to Prompt for Open-Vocabulary Object Detection with Vision-Language Model. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2203.14940](https://arxiv.org/abs/2203.14940) · 📚 被引 324
- **作者**: Yu Du, Fangyun Wei, Zihe Zhang, Miaojing Shi, Yue Gao, Guoqi Li
- **🏷️ 机构**: Tsinghua University, Microsoft Research Asia, King&#x0027;s College London
- **会议**: CVPR 2022
- **摘要（中）**: ①该论文针对开放词汇目标检测中提示词（prompt）人工设计繁琐且难以优化的问题，现有提示学习方法多面向图像分类，直接应用于检测任务时效果次优。②提出了DetPro方法，通过学习连续提示表示来适配检测任务，包含两个关键设计：背景解释方案（将图像背景中的候选框纳入提示训练）和上下文分级方案（区分不同候选框的上下文重要性）。③相比分类导向的提示学习方法，DetPro首次将检测特有的背景和候选框信息融入提示学习，提升了提示对检测任务的适应性。④在开放词汇检测基准上，DetPro显著提升了新类别的检测性能，例如在LVIS数据集上相比基线有较大幅度提升，具体数值需参考原文。
- **摘要（英）**: This paper addresses the challenge of manual prompt engineering in open-vocabulary object detection by proposing DetPro, a method that learns continuous prompt representations tailored for detection tasks. It introduces background interpretation and context grading schemes to leverage detection-specific information, outperforming classification-oriented prompt learning methods on benchmarks like LVIS.
- **核心贡献**: 提出了首个面向开放词汇目标检测的连续提示学习方法DetPro，有效提升新类别检测性能。
- **创新点**: 创新性地将背景候选框和上下文分级机制引入提示学习，使提示表示更贴合检测任务特性。
- **结果**: 在开放词汇检测基准上显著优于现有提示学习方法，验证了方法的有效性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, vision-language pre-training shows great potential in open-vocabulary object detection, where detectors trained on base classes are devised for detecting new classes. The class text embedding is firstly generated by feeding prompts to the text encoder of a pre-trained vision-language model. It is then used as the region classifier to supervise the training of a detector. The key element that leads to the success of this model is the proper prompt, which requires careful words tuning and ingenious design. To avoid laborious prompt engineering, there are some prompt representation learning methods being proposed for the image classification task, which however can only be sub-optimal solutions when applied to the detection task. In this paper, we introduce a novel method, detection prompt (DetPro), to learn continuous prompt representations for open-vocabulary object detection based on the pre-trained vision-language model. Different from the previous classification-oriented methods, DetPro has two highlights: 1) a background interpretation scheme to include the proposals in image background into the prompt training; 2) a context grading scheme to separate proposals in image foreground for tailored prompt training. We assemble DetPro with ViLD, a recent state-of-the-art open-world object detector, and conduct experiments on the LVIS as well as transfer learning on the Pascal VOC, COCO, Objects365 datasets. Experimental results show that our DetPro outperforms the baseline ViLD in all settings, e.g., +3.4 APbox and +3.0 APmask improvements on the novel classes of LVIS. Code and models are available at https://github.com/dyabel/detpro.

</details>

### Expanding Low-Density Latent Regions for Open-Set Object Detection. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2203.14911](https://arxiv.org/abs/2203.14911) · 📚 被引 89
- **作者**: Jiaming Han, Yuqiang Ren, Jian Ding, Xingjia Pan, Ke Yan, Gui-Song Xia
- **🏷️ 机构**: School of Computer Science, Wuhan University,NERCMS, YouTuLab,Tencent
- **会议**: CVPR 2022
- **摘要（中）**: 针对开放集目标检测中未知类别物体常被误分类为已知类别的问题，提出OpenDet检测器，通过分离潜在空间中的高/低密度区域来识别未知物体。方法包含对比特征学习器（CFL）和未知概率学习器（UPL），CFL通过实例级对比学习使已知类特征更紧凑，为未知类留出更多低密度区域；UPL基于预测不确定性优化未知概率，进一步划分低密度区域。相比传统阈值方法仅维持有限低密度区域，该方法扩展了低密度区域覆盖范围，能更全面地识别未知物体。实验表明该方法在开放集检测基准上有效提升了未知类检测性能。
- **摘要（英）**: This paper addresses open-set object detection by proposing OpenDet, which separates high/low-density latent regions to identify unknown objects. It employs a Contrastive Feature Learner (CFL) for compact known-class features and an Unknown Probability Learner (UPL) to expand low-density regions via uncertainty optimization. Compared to threshold-based methods, it covers more low-density regions, improving unknown object detection performance on benchmarks.
- **核心贡献**: 提出OpenDet框架，通过扩展低密度潜在区域实现更有效的未知物体检测。
- **创新点**: 结合对比学习和不确定性估计，动态扩展低密度区域以覆盖更多未知类别。
- **结果**: 在开放集检测基准上显著提升了未知类检测的召回率和准确率。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Modern object detectors have achieved impressive progress under the close-set setup. However, open-set object detection (OSOD) remains challenging since objects of unknown categories are often misclassified to existing known classes. In this work, we propose to identify unknown objects by separating high/low-density regions in the latent space, based on the consensus that unknown objects are usually distributed in low-density latent regions. As traditional threshold-based methods only maintain limited low-density regions, which cannot cover all unknown objects, we present a novel Open-set Detector (OpenDet) with expanded low-density regions. To this aim, we equip OpenDet with two learners, Contrastive Feature Learner (CFL) and Unknown Probability Learner (UPL). CFL performs instance-level contrastive learning to encourage compact features of known classes, leaving more low-density regions for unknown classes; UPL optimizes unknown probability based on the uncertainty of predictions, which further divides more low-density regions around the cluster of known classes. Thus, unknown objects in low-density regions can be easily identified with the learned unknown probability. Extensive experiments demonstrate that our method can significantly improve the OSOD performance, e.g., OpenDet reduces the Absolute Open-Set Errors by 25%-35% on six OSOD benchmarks. Code is available at: https://github.com/csuhan/opendet2.

</details>

### Open Vocabulary Object Detection with Pseudo Bounding-Box Labels. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20080-9_16) · 📚 被引 76
- **作者**: Mingfei Gao, Chen Xing, Juan Carlos Niebles, Junnan Li, Ran Xu, Wenhao Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对开放词汇目标检测中缺乏边界框标注的问题，提出利用伪边界框标签进行训练。②方法可能通过生成或挖掘伪标签来扩展检测器的词汇覆盖范围，无需人工标注。③改进点在于降低了对精细标注的依赖，提升了可扩展性。④由于摘要缺失，具体性能数据未知，但该方向在开放世界检测中具有重要价值。
- **摘要（英）**: This paper addresses open vocabulary object detection by leveraging pseudo bounding-box labels, reducing reliance on manual annotations. The approach likely enhances scalability and vocabulary coverage. Specific results are unavailable due to missing abstract.
- **核心贡献**: 利用伪边界框标签实现开放词汇目标检测。
- **创新点**: 减少对人工标注的依赖，提升检测器的词汇泛化能力。
- **结果**: 未知，因摘要缺失。

### Open-Set Semi-Supervised Object Detection. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2208.13722](https://arxiv.org/abs/2208.13722)
- **作者**: Yen-Cheng Liu, Chih-Yao Ma, Xiaoliang Dai, Junjiao Tian, Peter Vajda, Zijian He et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对半监督目标检测（SSOD）在开放集条件下性能下降的问题，本文首次提出开放集半监督目标检测（OSSOD）任务。研究发现性能下降源于语义扩展，即OOD目标被误判为分布内伪标签。为此，作者设计了在线和离线OOD检测模块，并发现基于自监督ViT的离线OOD检测器因对伪标签干扰更鲁棒而表现更优。实验表明该方法能有效缓解语义扩展问题，并在多个OSSOD基准上取得一致提升。
- **摘要（英）**: This paper introduces Open-Set Semi-Supervised Object Detection (OSSOD), addressing the performance degradation of SSOD methods under open-set conditions caused by semantic expansion. The authors propose integrating online and offline OOD detection modules, finding that an offline detector based on a self-supervised ViT is more robust to pseudo-label noise. The framework consistently improves performance on multiple OSSOD benchmarks.
- **核心贡献**: 首次提出并形式化OSSOD问题，并给出有效的基线解决方案。
- **创新点**: 将离线自监督OOD检测器与SSOD结合，有效抑制语义扩展。
- **结果**: 在多个OSSOD基准上取得一致性能提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent developments for Semi-Supervised Object Detection (SSOD) have shown the promise of leveraging unlabeled data to improve an object detector. However, thus far these methods have assumed that the unlabeled data does not contain out-of-distribution (OOD) classes, which is unrealistic with larger-scale unlabeled datasets. In this paper, we consider a more practical yet challenging problem, Open-Set Semi-Supervised Object Detection (OSSOD). We first find the existing SSOD method obtains a lower performance gain in open-set conditions, and this is caused by the semantic expansion, where the distracting OOD objects are mispredicted as in-distribution pseudo-labels for the semi-supervised training. To address this problem, we consider online and offline OOD detection modules, which are integrated with SSOD methods. With the extensive studies, we found that leveraging an offline OOD detector based on a self-supervised vision transformer performs favorably against online OOD detectors due to its robustness to the interference of pseudo-labeling. In the experiment, our proposed framework effectively addresses the semantic expansion issue and shows consistent improvements on many OSSOD benchmarks, including large-scale COCO-OpenImages. We also verify the effectiveness of our framework under different OSSOD conditions, including varying numbers of in-distribution classes, different degrees of supervision, and different combinations of unlabeled sets.

</details>

### Simple Open-Vocabulary Object Detection. **⭐⭐⭐** (相关度: 75%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20080-9_42)
- **作者**: Matthias Minderer, Alexey A. Gritsenko, Austin Stone, Maxim Neumann, Dirk Weissenborn, Alexey Dosovitskiy et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 该论文提出一种简单的开放词汇目标检测方法，旨在利用预训练的视觉-语言模型（如CLIP）实现对未见类别的检测。方法通过将区域提议与文本嵌入对齐，无需额外标注即可检测开放词汇目标。其简洁性使得方法易于复现和集成。摘要未提供具体实验数据，但强调方法的简单性和有效性。
- **摘要（英）**: This paper presents a simple open-vocabulary object detection method that leverages pre-trained vision-language models to detect unseen categories. By aligning region proposals with text embeddings, the method avoids extra annotations. Its simplicity facilitates reproduction and integration, though specific experimental results are not provided in the abstract.
- **核心贡献**: 提出一种简单的开放词汇检测框架。
- **创新点**: 利用预训练VLM实现无需额外标注的检测。
- **结果**: 未提供具体数据，但声称有效。

### Few-Shot Object Detection by Knowledge Distillation Using Bag-of-Visual-Words Representations. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2207.12049](https://arxiv.org/abs/2207.12049)
- **作者**: Wenjie Pei, Shuang Wu, Dianwen Mei, Fanglin Chen, Jiandong Tian, Guangming Lu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对小样本目标检测中基类过拟合和新类样本过拟合的问题，本文提出一种基于视觉词袋（BoVW）表示的知识蒸馏框架。首先设计位置感知的BoVW模型从有限图像中学习代表性视觉词，然后利用图像在不同特征空间中BoVW表示的一致性进行蒸馏，以指导检测器学习。该方法在预训练和微调阶段均能有效抑制过拟合，提升检测性能。
- **摘要（英）**: This paper addresses overfitting in few-shot object detection by proposing a knowledge distillation framework using Position-Aware Bag-of-Visual-Words (BoVW). The method learns representative visual words and distills consistent BoVW representations across feature spaces to guide detector training. It effectively mitigates both base-class and novel-class overfitting, improving detection performance.
- **核心贡献**: 提出基于BoVW的知识蒸馏框架以抑制小样本检测中的过拟合。
- **创新点**: 利用跨特征空间的BoVW一致性进行知识迁移。
- **结果**: 有效提升小样本检测性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While fine-tuning based methods for few-shot object detection have achieved remarkable progress, a crucial challenge that has not been addressed well is the potential class-specific overfitting on base classes and sample-specific overfitting on novel classes. In this work we design a novel knowledge distillation framework to guide the learning of the object detector and thereby restrain the overfitting in both the pre-training stage on base classes and fine-tuning stage on novel classes. To be specific, we first present a novel Position-Aware Bag-of-Visual-Words model for learning a representative bag of visual words (BoVW) from a limited size of image set, which is used to encode general images based on the similarities between the learned visual words and an image. Then we perform knowledge distillation based on the fact that an image should have consistent BoVW representations in two different feature spaces. To this end, we pre-learn a feature space independently from the object detection, and encode images using BoVW in this space. The obtained BoVW representation for an image can be considered as distilled knowledge to guide the learning of object detector: the extracted features by the object detector for the same image are expected to derive the consistent BoVW representations with the distilled knowledge. Extensive experiments validate the effectiveness of our method and demonstrate the superiority over other state-of-the-art methods.

</details>

### UC-OWOD: Unknown-Classified Open World Object Detection. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2207.11455](https://arxiv.org/abs/2207.11455) · 📚 被引 64
- **作者**: Zhiheng Wu, Yue Lu, Xingyu Chen, Zhengxing Wu, Liwen Kang, Junzhi Yu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对开放世界目标检测（OWOD）无法区分未知实例为多个未知类别的问题，本文提出未知分类开放世界目标检测（UC-OWOD）任务。方法采用两阶段检测器，首先通过未知标签感知提议和未知判别分类头检测已知和未知目标，然后利用基于相似度的未知分类和聚类细化模块区分多个未知类别。此外，设计了两个新评估协议，实验证明方法有效性。
- **摘要（英）**: This paper introduces Unknown-Classified Open World Object Detection (UC-OWOD), extending OWOD to distinguish multiple unknown classes. A two-stage detector is proposed with unknown-aware proposals and discriminative heads, followed by similarity-based classification and clustering refinement. New evaluation protocols are designed, and experiments demonstrate effectiveness.
- **核心贡献**: 首次提出UC-OWOD任务并给出完整解决方案。
- **创新点**: 通过聚类细化实现未知类别的区分。
- **结果**: 实验证明能有效检测和分类未知目标。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open World Object Detection (OWOD) is a challenging computer vision problem that requires detecting unknown objects and gradually learning the identified unknown classes. However, it cannot distinguish unknown instances as multiple unknown classes. In this work, we propose a novel OWOD problem called Unknown-Classified Open World Object Detection (UC-OWOD). UC-OWOD aims to detect unknown instances and classify them into different unknown classes. Besides, we formulate the problem and devise a two-stage object detector to solve UC-OWOD. First, unknown label-aware proposal and unknown-discriminative classification head are used to detect known and unknown objects. Then, similarity-based unknown classification and unknown clustering refinement modules are constructed to distinguish multiple unknown classes. Moreover, two novel evaluation protocols are designed to evaluate unknown-class detection. Abundant experiments and visualizations prove the effectiveness of the proposed method. Code is available at https://github.com/JohnWuzh/UC-OWOD.

</details>

### Multi-faceted Distillation of Base-Novel Commonality for Few-Shot Object Detection. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2207.11184](https://arxiv.org/abs/2207.11184) · 📚 被引 44
- **作者**: Shuang Wu, Wenjie Pei, Dianwen Mei, Fanglin Chen, Jiandong Tian, Guangming Lu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对小样本目标检测中基类和新类之间类不可知知识难以显式迁移的问题，本文提出学习三类类不可知共性：识别相关语义共性、定位相关语义共性和分布共性。设计基于记忆库的统一蒸馏框架，可联合高效地蒸馏这三类共性。该方法能轻松集成到现有微调方法中，并大幅提升性能。
- **摘要（英）**: This paper proposes learning three types of class-agnostic commonalities between base and novel classes in few-shot object detection: recognition-related, localization-related, and distribution commonalities. A unified memory-bank-based distillation framework jointly distills these commonalities, and can be readily integrated into existing fine-tuning methods, consistently improving performance by a large margin.
- **核心贡献**: 提出多面共性蒸馏框架，显式迁移类不可知知识。
- **创新点**: 统一蒸馏三类共性，并利用记忆库高效实现。
- **结果**: 集成到现有方法后性能大幅提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Most of existing methods for few-shot object detection follow the fine-tuning paradigm, which potentially assumes that the class-agnostic generalizable knowledge can be learned and transferred implicitly from base classes with abundant samples to novel classes with limited samples via such a two-stage training strategy. However, it is not necessarily true since the object detector can hardly distinguish between class-agnostic knowledge and class-specific knowledge automatically without explicit modeling. In this work we propose to learn three types of class-agnostic commonalities between base and novel classes explicitly: recognition-related semantic commonalities, localization-related semantic commonalities and distribution commonalities. We design a unified distillation framework based on a memory bank, which is able to perform distillation of all three types of commonalities jointly and efficiently. Extensive experiments demonstrate that our method can be readily integrated into most of existing fine-tuning based methods and consistently improve the performance by a large margin.

</details>

### DenseHybrid: Hybrid Anomaly Detection for Dense Open-Set Recognition. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2207.02606](https://arxiv.org/abs/2207.02606) · 📚 被引 60
- **作者**: Matej Grcic, Petra Bevandic, Sinisa Segvic
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对密集异常检测中生成式与判别式方法各自失败模式不同的问题，该论文提出混合异常检测算法DenseHybrid，通过将判别式logits重新解释为未归一化联合分布的对数，在共享卷积表示上恢复三个密集预测：闭集类别后验、数据集后验和未归一化数据似然。方法在标准训练数据和通用负样本数据上训练后两个预测，并融合为混合异常分数，支持大尺寸自然图像上的密集开集识别。实验设计精心，但摘要未给出具体性能数据。
- **摘要（英）**: This paper tackles dense anomaly detection by proposing DenseHybrid, a hybrid algorithm that reinterprets discriminative logits as log of unnormalized joint distribution, recovering three dense predictions from a shared convolutional representation. It blends dataset posterior and data likelihood trained on both standard and negative data into a hybrid anomaly score, enabling dense open-set recognition on large images. The method addresses limitations of prior hybrid approaches but lacks quantitative results in the abstract.
- **核心贡献**: 提出DenseHybrid混合异常检测算法，实现密集开集识别。
- **创新点**: 将判别式logits重新解释为未归一化联合分布，融合生成式与判别式预测。
- **结果**: 支持大尺寸图像上的密集开集识别，但未提供具体性能数据。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Anomaly detection can be conceived either through generative modelling of regular training data or by discriminating with respect to negative training data. These two approaches exhibit different failure modes. Consequently, hybrid algorithms present an attractive research goal. Unfortunately, dense anomaly detection requires translational equivariance and very large input resolutions. These requirements disqualify all previous hybrid approaches to the best of our knowledge. We therefore design a novel hybrid algorithm based on reinterpreting discriminative logits as a logarithm of the unnormalized joint distribution $\hat{p}(\mathbf{x}, \mathbf{y})$. Our model builds on a shared convolutional representation from which we recover three dense predictions: i) the closed-set class posterior $P(\mathbf{y}|\mathbf{x})$, ii) the dataset posterior $P(d_{in}|\mathbf{x})$, iii) unnormalized data likelihood $\hat{p}(\mathbf{x})$. The latter two predictions are trained both on the standard training data and on a generic negative dataset. We blend these two predictions into a hybrid anomaly score which allows dense open-set recognition on large natural images. We carefully design a custom loss for the data likelihood in order to avoid backpropagation through the untractable normalizing constant $Z(θ)$. Experiments evaluate our contributions on standard dense anomaly detection benchmarks as well as in terms of open-mIoU - a novel metric for dense open-set performance. Our submissions achieve state-of-the-art performance despite neglectable computational overhead over the standard semantic segmentation baseline.

</details>

### PromptDet: Towards Open-Vocabulary Detection Using Uncurated Images. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20077-9_41) · 📚 被引 140
- **作者**: Chengjian Feng, Yujie Zhong, Zequn Jie, Xiangxiang Chu, Haibing Ren, Xiaolin Wei et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对开放词汇检测依赖人工标注数据的问题，该论文提出PromptDet方法，利用非精选图像（如网络爬取数据）进行训练，通过文本提示和区域级对比学习实现开放词汇检测。方法结合视觉-语言预训练模型，在无需人工标注的情况下学习新类别，并支持任意文本查询的检测。实验表明在多个基准上优于现有方法，但摘要未提供具体数值。
- **摘要（英）**: This paper addresses open-vocabulary detection by proposing PromptDet, which leverages uncurated images and text prompts with region-level contrastive learning to detect novel classes without manual annotations. It builds on vision-language pretraining and supports arbitrary text queries, outperforming prior methods on benchmarks, though no specific numbers are given in the abstract.
- **核心贡献**: 提出PromptDet方法，利用非精选图像实现开放词汇检测。
- **创新点**: 结合文本提示和区域级对比学习，无需人工标注即可学习新类别。
- **结果**: 在多个基准上优于现有方法，但未提供具体数据。

### Scaling Open-Vocabulary Image Segmentation with Image-Level Labels. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20059-5_31) · 📚 被引 339
- **作者**: Golnaz Ghiasi, Xiuye Gu, Yin Cui, Tsung-Yi Lin
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对开放词汇图像分割依赖像素级标注的问题，该论文提出利用图像级标签进行训练的方法，通过视觉-语言模型对齐图像和文本嵌入，实现开放词汇分割。方法在无需密集标注的情况下学习任意类别，并扩展到大规模数据集。实验表明在多个分割基准上达到与全监督方法相当的性能，但摘要未提供具体数值。
- **摘要（英）**: This paper addresses open-vocabulary image segmentation by proposing a method that trains with image-level labels, aligning visual and text embeddings via vision-language models to segment arbitrary categories without dense annotations. It scales to large datasets and achieves performance comparable to fully supervised methods on benchmarks, though no specific numbers are provided in the abstract.
- **核心贡献**: 提出利用图像级标签训练开放词汇分割模型的方法。
- **创新点**: 通过视觉-语言对齐实现无需像素级标注的开放词汇分割。
- **结果**: 在多个基准上达到与全监督方法相当的性能。

### Towards Open-Vocabulary Scene Graph Generation with Prompt-Based Finetuning.
- **链接**: [arXiv:2208.08165](https://arxiv.org/abs/2208.08165) · 📚 被引 46
- **作者**: Tao He, Lianli Gao, Jingkuan Song, Yuan-Fang Li
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Scene graph generation (SGG) is a fundamental task aimed at detecting visual relations between objects in an image. The prevailing SGG methods require all object classes to be given in the training set. Such a closed setting limits the practical application of SGG. In this paper, we introduce open-vocabulary scene graph generation, a novel, realistic and challenging setting in which a model is trained on a set of base object classes but is required to infer relations for unseen target object classes. To this end, we propose a two-step method that firstly pre-trains on large amounts of coarse-grained region-caption data and then leverages two prompt-based techniques to finetune the pre-trained model without updating its parameters. Moreover, our method can support inference over completely unseen object classes, which existing methods are incapable of handling. On extensive experiments on three benchmark datasets, Visual Genome, GQA, and Open-Image, our method significantly outperforms recent, strong SGG methods on the setting of Ov-SGG, as well as on the conventional closed SGG.

</details>

### Improving Closed and Open-Vocabulary Attribute Prediction Using Transformers.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19806-9_12) · 📚 被引 11
- **作者**: Khoi Pham, Kushal Kafle, Zhe Lin, Zhihong Ding, Scott Cohen, Quan Tran et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### A Simple Baseline for Open-Vocabulary Semantic Segmentation with Pre-trained Vision-Language Model.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19818-2_42) · 📚 被引 211
- **作者**: Mengde Xu, Zheng Zhang, Fangyun Wei, Yutong Lin, Yue Cao, Han Hu et al.
- **🏷️ 机构**: HUAST
- **会议**: ECCV 2022

### OpenLDN: Learning to Discover Novel Classes for Open-World Semi-Supervised Learning.
- **链接**: [arXiv:2207.02261](https://arxiv.org/abs/2207.02261) · 📚 被引 36
- **作者**: Mamshad Nayeem Rizve, Navid Kardan, Salman Khan, Fahad Shahbaz Khan, Mubarak Shah
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Semi-supervised learning (SSL) is one of the dominant approaches to address the annotation bottleneck of supervised learning. Recent SSL methods can effectively leverage a large repository of unlabeled data to improve performance while relying on a small set of labeled data. One common assumption in most SSL methods is that the labeled and unlabeled data are from the same data distribution. However, this is hardly the case in many real-world scenarios, which limits their applicability. In this work, instead, we attempt to solve the challenging open-world SSL problem that does not make such an assumption. In the open-world SSL problem, the objective is to recognize samples of known classes, and simultaneously detect and cluster samples belonging to novel classes present in unlabeled data. This work introduces OpenLDN that utilizes a pairwise similarity loss to discover novel classes. Using a bi-level optimization rule this pairwise similarity loss exploits the information available in the labeled set to implicitly cluster novel class samples, while simultaneously recognizing samples from known classes. After discovering novel classes, OpenLDN transforms the open-world SSL problem into a standard SSL problem to achieve additional performance gains using existing SSL methods. Our extensive experiments demonstrate that OpenLDN outperforms the current state-of-the-art methods on multiple popular classification benchmarks while providing a better accuracy/training time trade-off.

</details>

### Open-vocabulary Object Detection via Vision and Language Knowledge Distillation.
- **链接**: [出版页](https://openreview.net/forum?id=lL3lnMbR4WU)
- **作者**: Xiuye Gu, Tsung-Yi Lin, Weicheng Kuo, Yin Cui
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

### Decoupling Classifier for Boosting Few-shot Object Detection and Instance Segmentation.
- **链接**: [arXiv:2505.14239](https://arxiv.org/abs/2505.14239) · 📚 被引 6
- **作者**: Bin-Bin Gao, Xiaochen Chen, Zhongyi Huang, Congchong Nie, Jun Liu, Jinxiang Lai et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper focus on few-shot object detection~(FSOD) and instance segmentation~(FSIS), which requires a model to quickly adapt to novel classes with a few labeled instances. The existing methods severely suffer from bias classification because of the missing label issue which naturally exists in an instance-level few-shot scenario and is first formally proposed by us. Our analysis suggests that the standard classification head of most FSOD or FSIS models needs to be decoupled to mitigate the bias classification. Therefore, we propose an embarrassingly simple but effective method that decouples the standard classifier into two heads. Then, these two individual heads are capable of independently addressing clear positive samples and noisy negative samples which are caused by the missing label. In this way, the model can effectively learn novel classes while mitigating the effects of noisy negative samples. Without bells and whistles, our model without any additional computation cost and parameters consistently outperforms its baseline and state-of-the-art by a large margin on PASCAL VOC and MS-COCO benchmarks for FSOD and FSIS tasks. The Code is available at https://csgaobb.github.io/Projects/DCFS.

</details>

### Bridging the Gap between Object and Image-level Representations for Open-Vocabulary Detection.
- **链接**: [arXiv:2207.03482](https://arxiv.org/abs/2207.03482) · 📚 被引 13
- **作者**: Hanoona Abdul Rasheed, Muhammad Maaz, Muhammad Uzair Khattak, Salman H. Khan, Fahad Shahbaz Khan
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing open-vocabulary object detectors typically enlarge their vocabulary sizes by leveraging different forms of weak supervision. This helps generalize to novel objects at inference. Two popular forms of weak-supervision used in open-vocabulary detection (OVD) include pretrained CLIP model and image-level supervision. We note that both these modes of supervision are not optimally aligned for the detection task: CLIP is trained with image-text pairs and lacks precise localization of objects while the image-level supervision has been used with heuristics that do not accurately specify local object regions. In this work, we propose to address this problem by performing object-centric alignment of the language embeddings from the CLIP model. Furthermore, we visually ground the objects with only image-level supervision using a pseudo-labeling process that provides high-quality object proposals and helps expand the vocabulary during training. We establish a bridge between the above two object-alignment strategies via a novel weight transfer function that aggregates their complimentary strengths. In essence, the proposed model seeks to minimize the gap between object and image-centric representations in the OVD setting. On the COCO benchmark, our proposed approach achieves 36.6 AP50 on novel classes, an absolute 8.2 gain over the previous best performance. For LVIS, we surpass the state-of-the-art ViLD model by 5.0 mask AP for rare categories and 3.4 overall. Code: https://github.com/hanoonaR/object-centric-ovd.

</details>

### Patching open-vocabulary models by interpolating weights.
- **链接**: [arXiv:2208.05592](https://arxiv.org/abs/2208.05592) · 📚 被引 7
- **作者**: Gabriel Ilharco, Mitchell Wortsman, Samir Yitzhak Gadre, Shuran Song, Hannaneh Hajishirzi, Simon Kornblith et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-vocabulary models like CLIP achieve high accuracy across many image classification tasks. However, there are still settings where their zero-shot performance is far from optimal. We study model patching, where the goal is to improve accuracy on specific tasks without degrading accuracy on tasks where performance is already adequate. Towards this goal, we introduce PAINT, a patching method that uses interpolations between the weights of a model before fine-tuning and the weights after fine-tuning on a task to be patched. On nine tasks where zero-shot CLIP performs poorly, PAINT increases accuracy by 15 to 60 percentage points while preserving accuracy on ImageNet within one percentage point of the zero-shot model. PAINT also allows a single model to be patched on multiple tasks and improves with model scale. Furthermore, we identify cases of broad transfer, where patching on one task increases accuracy on other tasks even when the tasks have disjoint classes. Finally, we investigate applications beyond common benchmarks such as counting or reducing the impact of typographic attacks on CLIP. Our findings demonstrate that it is possible to expand the set of tasks on which open-vocabulary models achieve high accuracy without re-training them from scratch.

</details>

## 跨领域论文（完整笔记在其他领域）

- PointCLIP: Point Cloud Understanding by CLIP. → [vlm](../vlm/Guideline%202022.md)
- Continual Learning for Visual Search with Backward Consistent Feature Embedding. → [continual-learning](../continual-learning/Guideline%202022.md)
- Forward Compatible Few-Shot Class-Incremental Learning. → [continual-learning](../continual-learning/Guideline%202022.md)
- Doodle It Yourself: Class Incremental Learning by Drawing a Few Sketches. → [continual-learning](../continual-learning/Guideline%202022.md)
- Constrained Few-shot Class-incremental Learning. → [continual-learning](../continual-learning/Guideline%202022.md)
- Class-Incremental Learning by Knowledge Distillation with Adaptive Feature Consolidation. → [continual-learning](../continual-learning/Guideline%202022.md)
- Class-Incremental Learning with Strong Pre-trained Models. → [continual-learning](../continual-learning/Guideline%202022.md)
- Global Convergence of MAML and Theory-Inspired Neural Architecture Search for Few-Shot Learning. → [neural-architecture-search](../neural-architecture-search/Guideline%202022.md)
- Class-Agnostic Object Detection with Multi-modal Transformer. → [multimodal](../multimodal/Guideline%202022.md)
- Few-Shot Class-Incremental Learning for 3D Point Cloud Objects. → [continual-learning](../continual-learning/Guideline%202022.md)
- Motion Inspired Unsupervised Perception and Prediction in Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202022.md)
- Few-Shot Class-Incremental Learning from an Open-Set Perspective. → [continual-learning](../continual-learning/Guideline%202022.md)
<!-- COMPLETE v1 papers=24 -->
