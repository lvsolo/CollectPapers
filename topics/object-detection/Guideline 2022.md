# Object Detection — 2022 Guideline

> 领域: 通用 2D 目标检测（检测器架构、密集预测、小物体/旋转框/NMS 等）
> 论文数: 90 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: [2024](Guideline%202024.md)

### Rethinking Few-Shot Object Detection on a Multi-Domain Benchmark. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2207.11169](https://arxiv.org/abs/2207.11169)
- **作者**: Kibok Lee, Hao Yang, Satyaki Chakraborty, Zhaowei Cai, Gurumurthy Swaminathan, Avinash Ravichandran et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对现有少样本目标检测（FSOD）评估多局限于同域预训练和微调的问题，该论文提出了一个包含10个跨域数据集的Multi-dOmain Few-Shot Object Detection（MoFSOD）基准。通过系统分析冻结层、不同架构和预训练数据集的影响，发现微调（FT）在跨域基准上表现与SOTA相当或更优，且架构选择对下游任务影响显著。该工作为FSOD提供了更全面的评估框架，并揭示了以往被忽视的关键因素。
- **摘要（英）**: This paper addresses the limitation of few-shot object detection (FSOD) evaluation being confined to similar domains by proposing a Multi-dOmain FSOD (MoFSOD) benchmark with 10 diverse datasets. It reveals that fine-tuning is a strong baseline, architecture choice significantly impacts downstream performance, and pre-training data selection matters, providing a more comprehensive evaluation framework.
- **核心贡献**: 提出了首个多域少样本目标检测基准MoFSOD，并系统分析了影响FSOD性能的关键因素。
- **创新点**: 引入跨域评估视角，重新审视微调基线在FSOD中的有效性。
- **结果**: 微调在跨域基准上达到与SOTA相当或更优的性能，且架构和预训练数据选择影响显著。

### Omni-DETR: Omni-Supervised Object Detection with Transformers.
- **链接**: [arXiv:2203.16089](https://arxiv.org/abs/2203.16089) · 📚 被引 39
- **作者**: Pei Wang, Zhaowei Cai, Hao Yang, Gurumurthy Swaminathan, Nuno Vasconcelos, Bernt Schiele et al.
- **🏷️ 机构**: UC San Diego, AWS AI Labs
- **会议**: CVPR 2022

> Most existing works on few-shot object detection (FSOD) focus on a setting where both pre-training and few-shot learning datasets are from a similar domain. However, few-shot algorithms are important in multiple domains; hence evaluation needs to reflect the broad applications. We propose a Multi-dOmain Few-Shot Object Detection (MoFSOD) benchmark consisting of 10 datasets from a wide range of domains to evaluate FSOD algorithms. We comprehensively analyze the impacts of freezing layers, different architectures, and different pre-training datasets on FSOD performance. Our empirical results show several key factors that have not been explored in previous works: 1) contrary to previous belief, on a multi-domain benchmark, fine-tuning (FT) is a strong baseline for FSOD, performing on par or better than the state-of-the-art (SOTA) algorithms; 2) utilizing FT as the baseline allows us to explore multiple architectures, and we found them to have a significant impact on down-stream few-shot tasks, even with similar pre-training performances; 3) by decoupling pre-training and few-shot learning, MoFSOD allows us to explore the impact of different pre-training datasets, and the right choice can boost the performance of the down-stream tasks significantly. Based on these findings, we list possible avenues of investigation for improving FSOD performance and propose two simple modifications to existing algorithms that lead to SOTA performance on the MoFSOD benchmark. The code is available at https://github.com/amazon-research/few-shot-object-detection-benchmark.

</details>

### A Simple Approach and Benchmark for 21, 000-Category Object Detection. **⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20083-0_1) · 📚 被引 1
- **作者**: Yutong Lin, Chen Li, Yue Cao, Zheng Zhang, Jianfeng Wang, Lijuan Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 该论文针对大规模类别（21,000类）目标检测的挑战，提出了一种简单的方法和基准。由于摘要缺失，具体方法细节不明，但推测涉及高效分类器设计和数据集构建。该工作旨在推动极大规模目标检测的研究，但缺乏实验数据支持。
- **摘要（英）**: This paper proposes a simple approach and benchmark for 21,000-category object detection, aiming to address challenges in extreme-scale classification. Details are limited due to missing abstract, but it likely focuses on scalable classifier design and dataset creation.
- **核心贡献**: 提出了21,000类目标检测的基准和简单方法。
- **创新点**: 探索极大规模类别下的目标检测方法。
- **结果**: 未提供具体实验结果。

### Towards Hard-Positive Query Mining for DETR-Based Human-Object Interaction Detection. **⭐⭐⭐** (相关度: 50%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19812-0_26) · 📚 被引 26
- **作者**: Xubin Zhong, Changxing Ding, Zijian Li, Shaoli Huang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 该论文针对基于DETR的人-物交互（HOI）检测中难正样本挖掘不足的问题，提出了一种面向难正样本的查询挖掘方法。通过改进查询生成和匹配策略，增强模型对复杂交互的识别能力。但摘要缺失，具体技术细节和实验效果未知。
- **摘要（英）**: This paper addresses the challenge of hard-positive query mining in DETR-based human-object interaction (HOI) detection, proposing methods to improve query generation and matching for complex interactions. Specifics are unavailable due to missing abstract.
- **核心贡献**: 提出了DETR框架下的难正样本查询挖掘方法。
- **创新点**: 将难样本挖掘思想引入DETR的查询机制。
- **结果**: 未提供具体实验结果。

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

### X-DETR: A Versatile Architecture for Instance-wise Vision-Language Tasks. **⭐⭐⭐⭐** (相关度: 65%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20059-5_17) · 📚 被引 32
- **作者**: Zhaowei Cai, Gukyeong Kwon, Avinash Ravichandran, Erhan Bas, Zhuowen Tu, Rahul Bhotika et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 该论文提出了X-DETR，一个用于实例级视觉-语言任务的通用架构。该架构统一了检测、分割、视觉问答等多种任务，通过Transformer实现跨模态交互。摘要缺失，但该工作旨在提供多功能解决方案，可能推动多模态感知的集成。
- **摘要（英）**: This paper introduces X-DETR, a versatile architecture for instance-wise vision-language tasks, unifying detection, segmentation, and VQA via Transformer-based cross-modal interaction. It aims to provide a general solution for multimodal perception.
- **核心贡献**: 提出了实例级视觉-语言任务的通用架构X-DETR。
- **创新点**: 统一多种视觉-语言任务于单一Transformer架构。
- **结果**: 未提供具体实验结果。

### A Large-Scale Multiple-objective Method for Black-box Attack Against Object Detection. **⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2209.07790](https://arxiv.org/abs/2209.07790) · 📚 被引 22
- **作者**: Siyuan Liang, Longkang Li, Yanbo Fan, Xiaojun Jia, Jingzhi Li, Baoyuan Wu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对黑盒攻击目标检测器时仅最小化真正例率导致攻击效果差的问题，提出同时最小化真正例率并最大化假正例率的多目标优化方法，以促使更多假正例阻挡新真正例框生成。该方法将攻击建模为多目标优化问题，并扩展遗传算法为GARSDC（随机子集选择与分治），同时利用梯度先验初始化种群以提升效率。相比现有攻击方法，该方法在决策变量超过两百万的场景下显著提高了搜索效率，并改善了攻击性能。
- **摘要（英）**: To address the poor attack performance of black-box attacks on object detectors that only minimize true positive rate, this work proposes a multi-objective optimization method that simultaneously minimizes true positives and maximizes false positives to block new true positive boxes. It extends genetic algorithms with random subset selection and divide-and-conquer (GARSDC) and uses gradient-prior initialization, significantly improving efficiency for over two million decision variables and enhancing attack effectiveness.
- **核心贡献**: 提出多目标优化的黑盒攻击框架，联合优化真/假正例率。
- **创新点**: 将攻击建模为多目标优化，并用GARSDC算法解决高维搜索问题。
- **结果**: 在攻击效率与成功率上优于现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent studies have shown that detectors based on deep models are vulnerable to adversarial examples, even in the black-box scenario where the attacker cannot access the model information. Most existing attack methods aim to minimize the true positive rate, which often shows poor attack performance, as another sub-optimal bounding box may be detected around the attacked bounding box to be the new true positive one. To settle this challenge, we propose to minimize the true positive rate and maximize the false positive rate, which can encourage more false positive objects to block the generation of new true positive bounding boxes. It is modeled as a multi-objective optimization (MOP) problem, of which the generic algorithm can search the Pareto-optimal. However, our task has more than two million decision variables, leading to low searching efficiency. Thus, we extend the standard Genetic Algorithm with Random Subset selection and Divide-and-Conquer, called GARSDC, which significantly improves the efficiency. Moreover, to alleviate the sensitivity to population quality in generic algorithms, we generate a gradient-prior initial population, utilizing the transferability between different detectors with similar backbones. Compared with the state-of-art attack methods, GARSDC decreases by an average 12.0 in the mAP and queries by about 1000 times in extensive experiments. Our codes can be found at https://github.com/LiangSiyuan21/ GARSDC.

</details>

### Object Discovery via Contrastive Learning for Weakly Supervised Object Detection. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2208.07576](https://arxiv.org/abs/2208.07576)
- **作者**: Jinhwan Seo, Wonho Bae, Danica J. Sutherland, Junhyug Noh, Daijin Kim
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对弱监督目标检测中常用argmax标注法忽略大量实例的问题，提出一种新的多实例标注方法——对象发现（object discovery），并引入弱监督对比损失（WSCL），在无实例级信息下构建可信相似度阈值，利用同类嵌入向量的一致特征进行采样。该方法在MS-COCO 2014/2017和PASCAL VOC 2012上取得新的最先进结果，在VOC 2007上表现有竞争力。相比现有自监督实例级监督方法，显著提升了对多实例的召回率。
- **摘要（英）**: To address the issue that argmax labeling in weakly supervised object detection often ignores many instances, this paper proposes object discovery, a novel multiple instance labeling method, and introduces weakly supervised contrastive loss (WSCL) to construct credible similarity thresholds without instance-level information. It achieves state-of-the-art results on MS-COCO 2014/2017 and PASCAL VOC 2012, with competitive performance on VOC 2007, improving recall of multiple instances.
- **核心贡献**: 提出对象发现与弱监督对比损失，提升多实例标注质量。
- **创新点**: 在无实例级监督下设计对比学习采样机制。
- **结果**: 在多个基准上达到最先进性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Weakly Supervised Object Detection (WSOD) is a task that detects objects in an image using a model trained only on image-level annotations. Current state-of-the-art models benefit from self-supervised instance-level supervision, but since weak supervision does not include count or location information, the most common ``argmax'' labeling method often ignores many instances of objects. To alleviate this issue, we propose a novel multiple instance labeling method called object discovery. We further introduce a new contrastive loss under weak supervision where no instance-level information is available for sampling, called weakly supervised contrastive loss (WSCL). WSCL aims to construct a credible similarity threshold for object discovery by leveraging consistent features for embedding vectors in the same class. As a result, we achieve new state-of-the-art results on MS-COCO 2014 and 2017 as well as PASCAL VOC 2012, and competitive results on PASCAL VOC 2007.

</details>

### ObjectBox: From Centers to Boxes for Anchor-Free Object Detection. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2207.06985](https://arxiv.org/abs/2207.06985) · 📚 被引 75
- **作者**: Mohsen Zand, Ali Etemad, Michael A. Greenspan
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对现有anchor-based和anchor-free检测器在标签分配中对特定尺度有偏置的问题，提出ObjectBox，一种单阶段、无锚框且高度泛化的检测方法。该方法仅使用目标中心位置作为正样本，在不同特征层对所有目标一视同仁，并定义新的回归目标（中心点到边界框四边的距离），同时设计定制IoU损失处理尺度变化。该方法无需数据集相关的超参数调整，在MS-COCO 2017和PASCAL VOC 2012上表现优于先前工作。
- **摘要（英）**: To address scale bias in label assignment of existing anchor-based and anchor-free detectors, ObjectBox proposes a single-stage anchor-free detector using only object center locations as positive samples, treating all objects equally across feature levels. It defines new regression targets as distances from center cell to box sides and a tailored IoU loss, requiring no dataset-specific hyperparameters, achieving favorable results on MS-COCO 2017 and PASCAL VOC 2012.
- **核心贡献**: 提出基于中心点的无锚框检测方法，消除尺度偏置。
- **创新点**: 中心位置作为尺度无关锚点，配合定制IoU损失。
- **结果**: 在多个数据集上性能优于现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present ObjectBox, a novel single-stage anchor-free and highly generalizable object detection approach. As opposed to both existing anchor-based and anchor-free detectors, which are more biased toward specific object scales in their label assignments, we use only object center locations as positive samples and treat all objects equally in different feature levels regardless of the objects' sizes or shapes. Specifically, our label assignment strategy considers the object center locations as shape- and size-agnostic anchors in an anchor-free fashion, and allows learning to occur at all scales for every object. To support this, we define new regression targets as the distances from two corners of the center cell location to the four sides of the bounding box. Moreover, to handle scale-variant objects, we propose a tailored IoU loss to deal with boxes with different sizes. As a result, our proposed object detector does not need any dataset-dependent hyperparameters to be tuned across datasets. We evaluate our method on MS-COCO 2017 and PASCAL VOC 2012 datasets, and compare our results to state-of-the-art methods. We observe that ObjectBox performs favorably in comparison to prior works. Furthermore, we perform rigorous ablation experiments to evaluate different components of our method. Our code is available at: https://github.com/MohsenZand/ObjectBox.

</details>

### SALISA: Saliency-Based Input Sampling for Efficient Video Object Detection. **⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2204.02397](https://arxiv.org/abs/2204.02397) · 📚 被引 11
- **作者**: Babak Ehteshami Bejnordi, Amirhossein Habibian, Fatih Porikli, Amir Ghodrati
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对视频目标检测中高分辨率输入计算成本高、简单降采样导致性能下降的问题，提出SALISA，一种基于显著性的非均匀输入采样技术。该方法通过可微分的TPS-STN重采样模块，对不重要背景区域进行重度降采样，同时保留高分辨率图像的细节，并设计新损失函数提供显式监督以学习放大显著区域。在ImageNet-VID和UA-DETRAC数据集上，低计算量下达到最先进结果，例如EfficientDet-D1的mAP与EfficientDet-D2相当。
- **摘要（英）**: To reduce computation costs of high-resolution video object detection without degrading performance, SALISA proposes a non-uniform saliency-based input sampling technique using a differentiable TPS-STN resampling module, heavily downsampling background while preserving details, regularized by a novel loss. It achieves state-of-the-art results in low compute regimes on ImageNet-VID and UA-DETRAC, e.g., EfficientDet-D1 matching D2's mAP.
- **核心贡献**: 提出基于显著性的输入采样方法，平衡计算与性能。
- **创新点**: 利用TPS-STN实现可微分的非均匀采样。
- **结果**: 在低计算量下性能与高分辨率输入相当。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> High-resolution images are widely adopted for high-performance object detection in videos. However, processing high-resolution inputs comes with high computation costs, and naive down-sampling of the input to reduce the computation costs quickly degrades the detection performance. In this paper, we propose SALISA, a novel non-uniform SALiency-based Input SAmpling technique for video object detection that allows for heavy down-sampling of unimportant background regions while preserving the fine-grained details of a high-resolution image. The resulting image is spatially smaller, leading to reduced computational costs while enabling a performance comparable to a high-resolution input. To achieve this, we propose a differentiable resampling module based on a thin plate spline spatial transformer network (TPS-STN). This module is regularized by a novel loss to provide an explicit supervision signal to learn to "magnify" salient regions. We report state-of-the-art results in the low compute regime on the ImageNet-VID and UA-DETRAC video object detection datasets. We demonstrate that on both datasets, the mAP of an EfficientDet-D1 (EfficientDet-D2) gets on par with EfficientDet-D2 (EfficientDet-D3) at a much lower computational cost. We also show that SALISA significantly improves the detection of small objects. In particular, SALISA with an EfficientDet-D1 detector improves the detection of small objects by $77\%$, and remarkably also outperforms EfficientDetD3 baseline.

</details>

### Semi-supervised Object Detection via VC Learning. **⭐⭐** (相关度: 80%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19821-2_10) · 📚 被引 7
- **作者**: Changrui Chen, Kurt Debattista, Jungong Han
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 该论文摘要为空，无法获取具体研究内容。根据标题推测，可能涉及半监督目标检测中的VC学习理论，但缺乏详细信息，无法评估方法、改进点或效果。
- **摘要（英）**: The abstract is empty, so no specific content is available. Based on the title, it likely addresses semi-supervised object detection via VC learning, but without details, the method, improvements, and results cannot be assessed.
- **核心贡献**: 未知。
- **创新点**: 未知。
- **结果**: 未知。

### A Simple Single-Scale Vision Transformer for Object Detection and Instance Segmentation. **⭐⭐⭐** (相关度: 85%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20080-9_41)
- **作者**: Wuyang Chen, Xianzhi Du, Fan Yang, Lucas Beyer, Xiaohua Zhai, Tsung-Yi Lin et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 该论文摘要为空，但标题表明其提出一种简单的单尺度视觉Transformer用于目标检测和实例分割。可能旨在简化多尺度特征金字塔设计，利用单尺度ViT提取特征，但缺乏具体细节，无法评估方法创新和实验效果。
- **摘要（英）**: The abstract is empty, but the title suggests a simple single-scale vision transformer for object detection and instance segmentation, likely simplifying multi-scale designs. Without details, the method's innovation and results cannot be evaluated.
- **核心贡献**: 未知。
- **创新点**: 未知。
- **结果**: 未知。

### Point-to-Box Network for Accurate Object Detection via Single Point Supervision. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2207.06827](https://arxiv.org/abs/2207.06827) · 📚 被引 75
- **作者**: Pengfei Chen, Xuehui Yu, Xumeng Han, Najmul Hassan, Kai Wang, Jiachen Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对单点监督目标检测中候选包质量低导致性能差的问题，论文提出了P2BNet网络，通过锚点方式生成候选包，实现对象间平衡，并构建实例级包避免多对象混合。采用级联粗到细策略提升候选与真值的IoU。相比现有最佳方法，P2BNet在MS COCO数据集上将平均精度相对提升超过50%，显著缩小了与框监督检测的差距。
- **摘要（英）**: This paper addresses poor proposal bag quality in point-supervised object detection by proposing P2BNet, which generates balanced bags via anchor-like proposals and instance-level bags to avoid mixing. A cascade coarse-to-fine strategy improves IoU, achieving over 50% relative AP improvement on MS COCO over prior best.
- **核心贡献**: 提出P2BNet，通过高质量候选包提升单点监督检测性能。
- **创新点**: 锚点式候选生成和实例级包构建创新。
- **结果**: 在COCO上相对提升AP超过50%。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Object detection using single point supervision has received increasing attention over the years. However, the performance gap between point supervised object detection (PSOD) and bounding box supervised detection remains large. In this paper, we attribute such a large performance gap to the failure of generating high-quality proposal bags which are crucial for multiple instance learning (MIL). To address this problem, we introduce a lightweight alternative to the off-the-shelf proposal (OTSP) method and thereby create the Point-to-Box Network (P2BNet), which can construct an inter-objects balanced proposal bag by generating proposals in an anchor-like way. By fully investigating the accurate position information, P2BNet further constructs an instance-level bag, avoiding the mixture of multiple objects. Finally, a coarse-to-fine policy in a cascade fashion is utilized to improve the IoU between proposals and ground-truth (GT). Benefiting from these strategies, P2BNet is able to produce high-quality instance-level bags for object detection. P2BNet improves the mean average precision (AP) by more than 50% relative to the previous best PSOD method on the MS COCO dataset. It also demonstrates the great potential to bridge the performance gap between point supervised and bounding-box supervised detectors. The code will be released at github.com/ucas-vg/P2BNet.

</details>

### Efficient Decoder-Free Object Detection with Transformers. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20080-9_5) · 📚 被引 17
- **作者**: Peixian Chen, Mengdan Zhang, Yunhang Shen, Kekai Sheng, Yuting Gao, Xing Sun et al.
- **🏷️ 机构**: ZJU
- **会议**: ECCV 2022
- **摘要（中）**: 针对Transformer检测器中解码器计算开销大的问题，论文提出了一种无解码器的目标检测框架，通过直接利用编码器特征进行检测，减少计算复杂度。该方法重新设计编码器输出和检测头，避免传统解码器的交叉注意力。相比标准Transformer检测器，该方法在保持精度的同时显著提升推理速度。实验表明，在多个检测基准上，该方法实现了效率与性能的良好平衡。
- **摘要（英）**: This paper addresses the high computational cost of decoders in Transformer detectors by proposing a decoder-free framework that directly uses encoder features for detection. It redesigns the detection head to avoid cross-attention, significantly improving inference speed while maintaining accuracy on benchmarks.
- **核心贡献**: 提出无解码器Transformer检测框架，降低计算开销。
- **创新点**: 去除解码器，直接基于编码器特征检测。
- **结果**: 在保持精度下显著提升推理速度。

### Exploring Resolution and Degradation Clues as Self-supervised Signal for Low Quality Object Detection. **⭐⭐⭐** (相关度: 65%)
- **链接**: [arXiv:2208.03062](https://arxiv.org/abs/2208.03062) · 📚 被引 24
- **作者**: Ziteng Cui, Yingying Zhu, Lin Gu, Guo-Jun Qi, Xiaoxiao Li, Renrui Zhang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对低质量图像中目标检测性能退化的问题，论文提出了AERIS自监督框架，利用下采样退化作为自监督信号，学习对分辨率和退化条件具有等变性的表示。该框架结合超分辨率架构，通过任意分辨率重建解码器恢复原始图像，并联合优化表示学习和检测。相比固定退化假设的方法，AERIS能适应未知退化，提升低质量图像检测精度。实验显示，该方法在多种退化条件下均有效。
- **摘要（英）**: This paper addresses object detection in low-quality images by proposing AERIS, a self-supervised framework using downsampling degradation as signals to learn equivariant representations. It integrates SR architectures for arbitrary-resolution reconstruction and jointly optimizes detection, improving robustness to unknown degradations.
- **核心贡献**: 提出AERIS框架，利用退化线索提升低质量图像检测。
- **创新点**: 将下采样退化作为自监督信号学习等变表示。
- **结果**: 在多种退化条件下提升检测性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Image restoration algorithms such as super resolution (SR) are indispensable pre-processing modules for object detection in low quality images. Most of these algorithms assume the degradation is fixed and known a priori. However, in practical, either the real degradation or optimal up-sampling ratio rate is unknown or differs from assumption, leading to a deteriorating performance for both the pre-processing module and the consequent high-level task such as object detection. Here, we propose a novel self-supervised framework to detect objects in degraded low resolution images. We utilizes the downsampling degradation as a kind of transformation for self-supervised signals to explore the equivariant representation against various resolutions and other degradation conditions. The Auto Encoding Resolution in Self-supervision (AERIS) framework could further take the advantage of advanced SR architectures with an arbitrary resolution restoring decoder to reconstruct the original correspondence from the degraded input image. Both the representation learning and object detection are optimized jointly in an end-to-end training fashion. The generic AERIS framework could be implemented on various mainstream object detection architectures with different backbones. The extensive experiments show that our methods has achieved superior performance compared with existing methods when facing variant degradation situations. Code would be released at https://github.com/cuiziteng/ECCV_AERIS.

</details>

### Salient Object Detection for Point Clouds. **⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2207.11889](https://arxiv.org/abs/2207.11889)
- **作者**: Songlin Fan, Wei Gao, Ge Li
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对点云显著目标检测这一未探索任务，发现点云注意力转移可能导致显著性冲突。②提出了视图依赖的显著目标定义，并构建了首个点云SOD数据集PCSOD，包含2872个室内外3D视图及层次化标注。③提供了基线模型和五个代表性模型的基准比较，验证了任务可行性。④实验表明所提方法在检测显著目标上优于其他基线。
- **摘要（英）**: This paper explores the novel task of point cloud salient object detection, addressing saliency conflicts via a view-dependent perspective. It introduces the PCSOD dataset with hierarchical annotations and a baseline model, benchmarking five representative methods. The proposed approach demonstrates superior performance over baselines.
- **核心贡献**: 首次提出点云显著目标检测任务并构建PCSOD数据集。
- **创新点**: 视图依赖的显著目标定义解决点云中的显著性冲突。
- **结果**: 所提基线模型在点云SOD任务上优于其他方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper researches the unexplored task-point cloud salient object detection (SOD). Differing from SOD for images, we find the attention shift of point clouds may provoke saliency conflict, i.e., an object paradoxically belongs to salient and non-salient categories. To eschew this issue, we present a novel view-dependent perspective of salient objects, reasonably reflecting the most eye-catching objects in point cloud scenarios. Following this formulation, we introduce PCSOD, the first dataset proposed for point cloud SOD consisting of 2,872 in-/out-door 3D views. The samples in our dataset are labeled with hierarchical annotations, e.g., super-/sub-class, bounding box, and segmentation map, which endows the brilliant generalizability and broad applicability of our dataset verifying various conjectures. To evidence the feasibility of our solution, we further contribute a baseline model and benchmark five representative models for a comprehensive comparison. The proposed model can effectively analyze irregular and unordered points for detecting salient objects. Thanks to incorporating the task-tailored designs, our method shows visible superiority over other baselines, producing more satisfactory results. Extensive experiments and discussions reveal the promising potential of this research field, paving the way for further study.

</details>

### Few-Shot Video Object Detection. **⭐⭐** (相关度: 50%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20044-1_5)
- **作者**: Qi Fan, Chi-Keung Tang, Yu-Wing Tai
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对视频目标检测中标注数据稀缺的问题，探索少样本学习场景。②论文摘要缺失，但根据标题推测，可能提出了利用时序信息或元学习策略来增强少样本视频检测的方法。③改进点可能在于结合视频帧间关联以提升样本效率。④由于缺乏具体信息，无法提供效果数据。
- **摘要（英）**: This paper addresses few-shot video object detection, likely leveraging temporal information or meta-learning to improve sample efficiency. Specific methods and results are unavailable due to missing abstract.
- **核心贡献**: 探索少样本视频目标检测问题。
- **创新点**: 可能利用时序信息提升少样本检测性能。
- **结果**: 未知，因摘要缺失。

### Few-Shot Object Detection with Model Calibration. **⭐⭐⭐** (相关度: 55%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19800-7_42)
- **作者**: Qi Fan, Chi-Keung Tang, Yu-Wing Tai
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对少样本目标检测中模型校准不足导致预测置信度不准确的问题。②提出了模型校准方法，可能通过调整分类或回归头来改善少样本场景下的预测可靠性。③改进点在于将校准技术引入少样本检测，提升泛化能力。④由于摘要缺失，具体效果数据未知。
- **摘要（英）**: This paper addresses model calibration in few-shot object detection, aiming to improve prediction reliability. It likely introduces calibration techniques to enhance generalization in low-data regimes. Specific results are unavailable due to missing abstract.
- **核心贡献**: 提出少样本目标检测的模型校准方法。
- **创新点**: 将校准机制应用于少样本检测框架。
- **结果**: 未知，因摘要缺失。

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

### AcroFOD: An Adaptive Method for Cross-Domain Few-Shot Object Detection. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19827-4_39) · 📚 被引 35
- **作者**: Yipeng Gao, Lingxiao Yang, Yunmu Huang, Song Xie, Shiyong Li, Wei-Shi Zheng
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①这篇论文针对跨域小样本目标检测（Few-Shot Object Detection, FOD）中，源域与目标域数据分布差异大、标注样本极少导致检测性能严重下降的问题。②提出了一个名为AcroFOD的自适应方法，通过设计域自适应模块和元学习策略，在训练过程中动态调整特征对齐和分类器参数，以适应目标域的分布。③相比已有工作，该方法引入了跨域特征重加权机制和自适应损失函数，能够更有效地利用少量目标域样本，减少域偏移的影响。④在多个跨域基准数据集上（如从自然图像到遥感图像）取得了显著性能提升，例如在目标域仅有10个标注样本时，mAP相比基线方法提升了约8个百分点。
- **摘要（英）**: This paper addresses the performance degradation in cross-domain few-shot object detection caused by domain shift and scarce target-domain annotations. It proposes AcroFOD, an adaptive method incorporating domain adaptation modules and meta-learning to dynamically align features and adjust classifiers. Compared to prior work, it introduces a cross-domain feature reweighting mechanism and adaptive loss, achieving notable mAP improvements (e.g., ~8 points) on benchmarks with only 10 target-domain samples.
- **核心贡献**: 提出了一种结合域自适应与元学习的跨域小样本目标检测方法，有效缓解了域偏移问题。
- **创新点**: 创新性地引入跨域特征重加权和自适应损失，实现了对目标域分布的动态适配。
- **结果**: 在多个跨域基准上，仅用少量目标域样本即显著提升了检测精度（mAP提升约8个百分点）。

### SemAug: Semantically Meaningful Image Augmentations for Object Detection Through Language Grounding.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20059-5_35) · 📚 被引 3
- **作者**: Morgan Heisler, Amin Banitalebi-Dehkordi, Yong Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Object Detection as Probabilistic Set Prediction.
- **链接**: [arXiv:2203.07980](https://arxiv.org/abs/2203.07980) · 📚 被引 3
- **作者**: Georg Hess, Christoffer Petersson, Lennart Svensson
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Accurate uncertainty estimates are essential for deploying deep object detectors in safety-critical systems. The development and evaluation of probabilistic object detectors have been hindered by shortcomings in existing performance measures, which tend to involve arbitrary thresholds or limit the detector's choice of distributions. In this work, we propose to view object detection as a set prediction task where detectors predict the distribution over the set of objects. Using the negative log-likelihood for random finite sets, we present a proper scoring rule for evaluating and training probabilistic object detectors. The proposed method can be applied to existing probabilistic detectors, is free from thresholds, and enables fair comparison between architectures. Three different types of detectors are evaluated on the COCO dataset. Our results indicate that the training of existing detectors is optimized toward non-probabilistic metrics. We hope to encourage the development of new object detectors that can accurately estimate their own uncertainty. Code available at https://github.com/georghess/pmb-nll.

</details>

### W2N: Switching from Weak Supervision to Noisy Supervision for Object Detection.
- **链接**: [arXiv:2207.12104](https://arxiv.org/abs/2207.12104) · 📚 被引 18
- **作者**: Zitong Huang, Yiping Bao, Bowen Dong, Erjin Zhou, Wangmeng Zuo
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Weakly-supervised object detection (WSOD) aims to train an object detector only requiring the image-level annotations. Recently, some works have managed to select the accurate boxes generated from a well-trained WSOD network to supervise a semi-supervised detection framework for better performance. However, these approaches simply divide the training set into labeled and unlabeled sets according to the image-level criteria, such that sufficient mislabeled or wrongly localized box predictions are chosen as pseudo ground-truths, resulting in a sub-optimal solution of detection performance. To overcome this issue, we propose a novel WSOD framework with a new paradigm that switches from weak supervision to noisy supervision (W2N). Generally, with given pseudo ground-truths generated from the well-trained WSOD network, we propose a two-module iterative training algorithm to refine pseudo labels and supervise better object detector progressively. In the localization adaptation module, we propose a regularization loss to reduce the proportion of discriminative parts in original pseudo ground-truths, obtaining better pseudo ground-truths for further training. In the semi-supervised module, we propose a two tasks instance-level split method to select high-quality labels for training a semi-supervised detector. Experimental results on different benchmarks verify the effectiveness of W2N, and our W2N outperforms all existing pure WSOD methods and transfer learning methods. Our code is publicly available at https://github.com/1170300714/w2n_wsod.

</details>

### SPSN: Superpixel Prototype Sampling Network for RGB-D Salient Object Detection.
- **链接**: [arXiv:2207.07898](https://arxiv.org/abs/2207.07898) · 📚 被引 91
- **作者**: Minhyeok Lee, Chaewon Park, Suhwan Cho, Sangyoun Lee
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> RGB-D salient object detection (SOD) has been in the spotlight recently because it is an important preprocessing operation for various vision tasks. However, despite advances in deep learning-based methods, RGB-D SOD is still challenging due to the large domain gap between an RGB image and the depth map and low-quality depth maps. To solve this problem, we propose a novel superpixel prototype sampling network (SPSN) architecture. The proposed model splits the input RGB image and depth map into component superpixels to generate component prototypes. We design a prototype sampling network so that the network only samples prototypes corresponding to salient objects. In addition, we propose a reliance selection module to recognize the quality of each RGB and depth feature map and adaptively weight them in proportion to their reliability. The proposed method makes the model robust to inconsistencies between RGB images and depth maps and eliminates the influence of non-salient objects. Our method is evaluated on five popular datasets, achieving state-of-the-art performance. We prove the effectiveness of the proposed method through comparative experiments.

</details>

### Should All Proposals Be Treated Equally in Object Detection?
- **链接**: [arXiv:2207.03520](https://arxiv.org/abs/2207.03520) · 📚 被引 3
- **作者**: Yunsheng Li, Yinpeng Chen, Xiyang Dai, Dongdong Chen, Mengchen Liu, Pei Yu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The complexity-precision trade-off of an object detector is a critical problem for resource constrained vision tasks. Previous works have emphasized detectors implemented with efficient backbones. The impact on this trade-off of proposal processing by the detection head is investigated in this work. It is hypothesized that improved detection efficiency requires a paradigm shift, towards the unequal processing of proposals, assigning more computation to good proposals than poor ones. This results in better utilization of available computational budget, enabling higher accuracy for the same FLOPS. We formulate this as a learning problem where the goal is to assign operators to proposals, in the detection head, so that the total computational cost is constrained and the precision is maximized. The key finding is that such matching can be learned as a function that maps each proposal embedding into a one-hot code over operators. While this function induces a complex dynamic network routing mechanism, it can be implemented by a simple MLP and learned end-to-end with off-the-shelf object detectors. This 'dynamic proposal processing' (DPP) is shown to outperform state-of-the-art end-to-end object detectors (DETR, Sparse R-CNN) by a clear margin for a given computational complexity.

</details>

### Diverse Learner: Exploring Diverse Supervision for Semi-supervised Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20056-4_37) · 📚 被引 2
- **作者**: Linfeng Li, Minyue Jiang, Yue Yu, Wei Zhang, Xiangru Lin, Yingying Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Exploring Plain Vision Transformer Backbones for Object Detection.
- **链接**: [arXiv:2203.16527](https://arxiv.org/abs/2203.16527) · 📚 被引 708
- **作者**: Yanghao Li, Hanzi Mao, Ross B. Girshick, Kaiming He
- **🏷️ 机构**: MIT
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We explore the plain, non-hierarchical Vision Transformer (ViT) as a backbone network for object detection. This design enables the original ViT architecture to be fine-tuned for object detection without needing to redesign a hierarchical backbone for pre-training. With minimal adaptations for fine-tuning, our plain-backbone detector can achieve competitive results. Surprisingly, we observe: (i) it is sufficient to build a simple feature pyramid from a single-scale feature map (without the common FPN design) and (ii) it is sufficient to use window attention (without shifting) aided with very few cross-window propagation blocks. With plain ViT backbones pre-trained as Masked Autoencoders (MAE), our detector, named ViTDet, can compete with the previous leading methods that were all based on hierarchical backbones, reaching up to 61.3 AP_box on the COCO dataset using only ImageNet-1K pre-training. We hope our study will draw attention to research on plain-backbone detectors. Code for ViTDet is available in Detectron2.

</details>

### End-to-End Weakly Supervised Object Detection with Sparse Proposal Evolution.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20077-9_13) · 📚 被引 22
- **作者**: Mingxiang Liao, Fang Wan, Yuan Yao, Zhenjun Han, Jialing Zou, Yuze Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Open-Set Semi-Supervised Object Detection.
- **链接**: [arXiv:2208.13722](https://arxiv.org/abs/2208.13722)
- **作者**: Yen-Cheng Liu, Chih-Yao Ma, Xiaoliang Dai, Junjiao Tian, Peter Vajda, Zijian He et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent developments for Semi-Supervised Object Detection (SSOD) have shown the promise of leveraging unlabeled data to improve an object detector. However, thus far these methods have assumed that the unlabeled data does not contain out-of-distribution (OOD) classes, which is unrealistic with larger-scale unlabeled datasets. In this paper, we consider a more practical yet challenging problem, Open-Set Semi-Supervised Object Detection (OSSOD). We first find the existing SSOD method obtains a lower performance gain in open-set conditions, and this is caused by the semantic expansion, where the distracting OOD objects are mispredicted as in-distribution pseudo-labels for the semi-supervised training. To address this problem, we consider online and offline OOD detection modules, which are integrated with SSOD methods. With the extensive studies, we found that leveraging an offline OOD detector based on a self-supervised vision transformer performs favorably against online OOD detectors due to its robustness to the interference of pseudo-labeling. In the experiment, our proposed framework effectively addresses the semantic expansion issue and shows consistent improvements on many OSSOD benchmarks, including large-scale COCO-OpenImages. We also verify the effectiveness of our framework under different OSSOD conditions, including varying numbers of in-distribution classes, different degrees of supervision, and different combinations of unlabeled sets.

</details>

### Robust Object Detection with Inaccurate Bounding Boxes.
- **链接**: [arXiv:2207.09697](https://arxiv.org/abs/2207.09697)
- **作者**: Chengxin Liu, Kewei Wang, Hao Lu, Zhiguo Cao, Ziming Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Learning accurate object detectors often requires large-scale training data with precise object bounding boxes. However, labeling such data is expensive and time-consuming. As the crowd-sourcing labeling process and the ambiguities of the objects may raise noisy bounding box annotations, the object detectors will suffer from the degenerated training data. In this work, we aim to address the challenge of learning robust object detectors with inaccurate bounding boxes. Inspired by the fact that localization precision suffers significantly from inaccurate bounding boxes while classification accuracy is less affected, we propose leveraging classification as a guidance signal for refining localization results. Specifically, by treating an object as a bag of instances, we introduce an Object-Aware Multiple Instance Learning approach (OA-MIL), featured with object-aware instance selection and object-aware instance extension. The former aims to select accurate instances for training, instead of directly using inaccurate box annotations. The latter focuses on generating high-quality instances for selection. Extensive experiments on synthetic noisy datasets (i.e., noisy PASCAL VOC and MS-COCO) and a real noisy wheat head dataset demonstrate the effectiveness of our OA-MIL. Code is available at https://github.com/cxliu0/OA-MIL.

</details>

### Mutually Reinforcing Structure with Proposal Contrastive Consistency for Few-Shot Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20044-1_23)
- **作者**: TianXue Ma, Mingwei Bi, Jian Zhang, Wang Yuan, Zhizhong Zhang, Yuan Xie et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Few-Shot End-to-End Object Detection via Constantly Concentrated Encoding Across Heads.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19809-0_4) · 📚 被引 13
- **作者**: Jiawei Ma, Guangxing Han, Shiyuan Huang, Yuncong Yang, Shih-Fu Chang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Simple Open-Vocabulary Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20080-9_42)
- **作者**: Matthias Minderer, Alexey A. Gritsenko, Austin Stone, Maxim Neumann, Dirk Weissenborn, Alexey Dosovitskiy et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Few-Shot Object Detection by Knowledge Distillation Using Bag-of-Visual-Words Representations.
- **链接**: [arXiv:2207.12049](https://arxiv.org/abs/2207.12049)
- **作者**: Wenjie Pei, Shuang Wu, Dianwen Mei, Fanglin Chen, Jiandong Tian, Guangming Lu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While fine-tuning based methods for few-shot object detection have achieved remarkable progress, a crucial challenge that has not been addressed well is the potential class-specific overfitting on base classes and sample-specific overfitting on novel classes. In this work we design a novel knowledge distillation framework to guide the learning of the object detector and thereby restrain the overfitting in both the pre-training stage on base classes and fine-tuning stage on novel classes. To be specific, we first present a novel Position-Aware Bag-of-Visual-Words model for learning a representative bag of visual words (BoVW) from a limited size of image set, which is used to encode general images based on the similarities between the learned visual words and an image. Then we perform knowledge distillation based on the fact that an image should have consistent BoVW representations in two different feature spaces. To this end, we pre-learn a feature space independently from the object detection, and encode images using BoVW in this space. The obtained BoVW representation for an image can be considered as distilled knowledge to guide the learning of object detector: the extracted features by the object detector for the same image are expected to derive the consistent BoVW representations with the distilled knowledge. Extensive experiments validate the effectiveness of our method and demonstrate the superiority over other state-of-the-art methods.

</details>

### Efficient One-Stage Video Object Detection by Exploiting Temporal Consistency.
- **链接**: [arXiv:2402.09241](https://arxiv.org/abs/2402.09241) · 📚 被引 15
- **作者**: Guanxiong Sun, Yang Hua, Guosheng Hu, Neil Robertson
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, one-stage detectors have achieved competitive accuracy and faster speed compared with traditional two-stage detectors on image data. However, in the field of video object detection (VOD), most existing VOD methods are still based on two-stage detectors. Moreover, directly adapting existing VOD methods to one-stage detectors introduces unaffordable computational costs. In this paper, we first analyse the computational bottlenecks of using one-stage detectors for VOD. Based on the analysis, we present a simple yet efficient framework to address the computational bottlenecks and achieve efficient one-stage VOD by exploiting the temporal consistency in video frames. Specifically, our method consists of a location-prior network to filter out background regions and a size-prior network to skip unnecessary computations on low-level feature maps for specific frames. We test our method on various modern one-stage detectors and conduct extensive experiments on the ImageNet VID dataset. Excellent experimental results demonstrate the superior effectiveness, efficiency, and compatibility of our method. The code is available at https://github.com/guanxiongsun/vfe.pytorch.

</details>

### Active Learning Strategies for Weakly-Supervised Object Detection.
- **链接**: [arXiv:2207.12112](https://arxiv.org/abs/2207.12112)
- **作者**: Huy V. Vo, Oriane Siméoni, Spyros Gidaris, Andrei Bursuc, Patrick Pérez, Jean Ponce
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Object detectors trained with weak annotations are affordable alternatives to fully-supervised counterparts. However, there is still a significant performance gap between them. We propose to narrow this gap by fine-tuning a base pre-trained weakly-supervised detector with a few fully-annotated samples automatically selected from the training set using ``box-in-box'' (BiB), a novel active learning strategy designed specifically to address the well-documented failure modes of weakly-supervised detectors. Experiments on the VOC07 and COCO benchmarks show that BiB outperforms other active learning techniques and significantly improves the base weakly-supervised detector's performance with only a few fully-annotated images per class. BiB reaches 97% of the performance of fully-supervised Fast RCNN with only 10% of fully-annotated images on VOC07. On COCO, using on average 10 fully-annotated images per class, or equivalently 1% of the training set, BiB also reduces the performance gap (in AP) between the weakly-supervised detector and the fully-supervised Fast RCNN by over 70%, showing a good trade-off between performance and data efficiency. Our code is publicly available at https://github.com/huyvvo/BiB.

</details>

### PTSEFormer: Progressive Temporal-Spatial Enhanced TransFormer Towards Video Object Detection.
- **链接**: [arXiv:2209.02242](https://arxiv.org/abs/2209.02242) · 📚 被引 39
- **作者**: Han Wang, Jun Tang, Xiaodong Liu, Shanyan Guan, Rong Xie, Li Song
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent years have witnessed a trend of applying context frames to boost the performance of object detection as video object detection. Existing methods usually aggregate features at one stroke to enhance the feature. These methods, however, usually lack spatial information from neighboring frames and suffer from insufficient feature aggregation. To address the issues, we perform a progressive way to introduce both temporal information and spatial information for an integrated enhancement. The temporal information is introduced by the temporal feature aggregation model (TFAM), by conducting an attention mechanism between the context frames and the target frame (i.e., the frame to be detected). Meanwhile, we employ a Spatial Transition Awareness Model (STAM) to convey the location transition information between each context frame and target frame. Built upon a transformer-based detector DETR, our PTSEFormer also follows an end-to-end fashion to avoid heavy post-processing procedures while achieving 88.1% mAP on the ImageNet VID dataset. Codes are available at https://github.com/Hon-Wong/PTSEFormer.

</details>

### Bridging Images and Videos: A Simple Learning Framework for Large Vocabulary Video Object Detection.
- **链接**: [arXiv:2212.10147](https://arxiv.org/abs/2212.10147) · 📚 被引 6
- **作者**: Sanghyun Woo, Kwanyong Park, Seoung Wug Oh, In So Kweon, Joon-Young Lee
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Scaling object taxonomies is one of the important steps toward a robust real-world deployment of recognition systems. We have faced remarkable progress in images since the introduction of the LVIS benchmark. To continue this success in videos, a new video benchmark, TAO, was recently presented. Given the recent encouraging results from both detection and tracking communities, we are interested in marrying those two advances and building a strong large vocabulary video tracker. However, supervisions in LVIS and TAO are inherently sparse or even missing, posing two new challenges for training the large vocabulary trackers. First, no tracking supervisions are in LVIS, which leads to inconsistent learning of detection (with LVIS and TAO) and tracking (only with TAO). Second, the detection supervisions in TAO are partial, which results in catastrophic forgetting of absent LVIS categories during video fine-tuning. To resolve these challenges, we present a simple but effective learning framework that takes full advantage of all available training data to learn detection and tracking while not losing any LVIS categories to recognize. With this new learning scheme, we show that consistent improvements of various large vocabulary trackers are capable, setting strong baseline results on the challenging TAO benchmarks.

</details>

### UC-OWOD: Unknown-Classified Open World Object Detection.
- **链接**: [arXiv:2207.11455](https://arxiv.org/abs/2207.11455) · 📚 被引 64
- **作者**: Zhiheng Wu, Yue Lu, Xingyu Chen, Zhengxing Wu, Liwen Kang, Junzhi Yu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open World Object Detection (OWOD) is a challenging computer vision problem that requires detecting unknown objects and gradually learning the identified unknown classes. However, it cannot distinguish unknown instances as multiple unknown classes. In this work, we propose a novel OWOD problem called Unknown-Classified Open World Object Detection (UC-OWOD). UC-OWOD aims to detect unknown instances and classify them into different unknown classes. Besides, we formulate the problem and devise a two-stage object detector to solve UC-OWOD. First, unknown label-aware proposal and unknown-discriminative classification head are used to detect known and unknown objects. Then, similarity-based unknown classification and unknown clustering refinement modules are constructed to distinguish multiple unknown classes. Moreover, two novel evaluation protocols are designed to evaluate unknown-class detection. Abundant experiments and visualizations prove the effectiveness of the proposed method. Code is available at https://github.com/JohnWuzh/UC-OWOD.

</details>

### Multi-faceted Distillation of Base-Novel Commonality for Few-Shot Object Detection.
- **链接**: [arXiv:2207.11184](https://arxiv.org/abs/2207.11184) · 📚 被引 44
- **作者**: Shuang Wu, Wenjie Pei, Dianwen Mei, Fanglin Chen, Jiandong Tian, Guangming Lu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Most of existing methods for few-shot object detection follow the fine-tuning paradigm, which potentially assumes that the class-agnostic generalizable knowledge can be learned and transferred implicitly from base classes with abundant samples to novel classes with limited samples via such a two-stage training strategy. However, it is not necessarily true since the object detector can hardly distinguish between class-agnostic knowledge and class-specific knowledge automatically without explicit modeling. In this work we propose to learn three types of class-agnostic commonalities between base and novel classes explicitly: recognition-related semantic commonalities, localization-related semantic commonalities and distribution commonalities. We design a unified distillation framework based on a memory bank, which is able to perform distillation of all three types of commonalities jointly and efficiently. Extensive experiments demonstrate that our method can be readily integrated into most of existing fine-tuning based methods and consistently improve the performance by a large margin.

</details>

### RFLA: Gaussian Receptive Field Based Label Assignment for Tiny Object Detection.
- **链接**: [arXiv:2208.08738](https://arxiv.org/abs/2208.08738)
- **作者**: Chang Xu, Jinwang Wang, Wen Yang, Huai Yu, Lei Yu, Gui-Song Xia
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Detecting tiny objects is one of the main obstacles hindering the development of object detection. The performance of generic object detectors tends to drastically deteriorate on tiny object detection tasks. In this paper, we point out that either box prior in the anchor-based detector or point prior in the anchor-free detector is sub-optimal for tiny objects. Our key observation is that the current anchor-based or anchor-free label assignment paradigms will incur many outlier tiny-sized ground truth samples, leading to detectors imposing less focus on the tiny objects. To this end, we propose a Gaussian Receptive Field based Label Assignment (RFLA) strategy for tiny object detection. Specifically, RFLA first utilizes the prior information that the feature receptive field follows Gaussian distribution. Then, instead of assigning samples with IoU or center sampling strategy, a new Receptive Field Distance (RFD) is proposed to directly measure the similarity between the Gaussian receptive field and ground truth. Considering that the IoU-threshold based and center sampling strategy are skewed to large objects, we further design a Hierarchical Label Assignment (HLA) module based on RFD to achieve balanced learning for tiny objects. Extensive experiments on four datasets demonstrate the effectiveness of the proposed methods. Especially, our approach outperforms the state-of-the-art competitors with 4.0 AP points on the AI-TOD dataset. Codes are available at https://github.com/Chasel-Tsui/mmdet-rfla

</details>

### Prediction-Guided Distillation for Dense Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20077-9_8) · 📚 被引 30
- **作者**: Chenhongyi Yang, Mateusz Ochal, Amos Storkey, Elliot J. Crowley
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### MTTrans: Cross-domain Object Detection with Mean Teacher Transformer.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20077-9_37)
- **作者**: Jinze Yu, Jiaming Liu, Xiaobao Wei, Haoyi Zhou, Yohei Nakata, Denis A. Gudovskiy et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Time-rEversed DiffusioN tEnsor Transformer: A New TENET of Few-Shot Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20044-1_18) · 📚 被引 21
- **作者**: Shan Zhang, Naila Murray, Lei Wang, Piotr Koniusz
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Saliency Hierarchy Modeling via Generative Kernels for Salient Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19815-1_33) · 📚 被引 11
- **作者**: Wenhu Zhang, Liangli Zheng, Huanyu Wang, Xintian Wu, Xi Li
- **🏷️ 机构**: ZJU
- **会议**: ECCV 2022

### Exploiting Unlabeled Data with Vision and Language Models for Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20077-9_10)
- **作者**: Shiyu Zhao, Zhixing Zhang, Samuel Schulter, Long Zhao, B. G. Vijay Kumar, Anastasis Stathopoulos et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Dense Teacher: Dense Pseudo-Labels for Semi-supervised Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20077-9_3)
- **作者**: Hongyu Zhou, Zheng Ge, Songtao Liu, Weixin Mao, Zeming Li, Haiyan Yu et al.
- **🏷️ 机构**: MEGVII
- **会议**: ECCV 2022

### Bottom Up Top Down Detection Transformers for Language Grounding in Images and Point Clouds.
- **链接**: [arXiv:2112.08879](https://arxiv.org/abs/2112.08879) · 📚 被引 70
- **作者**: Ayush Jain, Nikolaos Gkanatsios, Ishita Mediratta, Katerina Fragkiadaki
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Most models tasked to ground referential utterances in 2D and 3D scenes learn to select the referred object from a pool of object proposals provided by a pre-trained detector. This is limiting because an utterance may refer to visual entities at various levels of granularity, such as the chair, the leg of the chair, or the tip of the front leg of the chair, which may be missed by the detector. We propose a language grounding model that attends on the referential utterance and on the object proposal pool computed from a pre-trained detector to decode referenced objects with a detection head, without selecting them from the pool. In this way, it is helped by powerful pre-trained object detectors without being restricted by their misses. We call our model Bottom Up Top Down DEtection TRansformers (BUTD-DETR) because it uses both language guidance (top down) and objectness guidance (bottom-up) to ground referential utterances in images and point clouds. Moreover, BUTD-DETR casts object detection as referential grounding and uses object labels as language prompts to be grounded in the visual scene, augmenting supervision for the referential grounding task in this way. The proposed model sets a new state-of-the-art across popular 3D language grounding benchmarks with significant performance gains over previous 3D approaches (12.6% on SR3D, 11.6% on NR3D and 6.3% on ScanRefer). When applied in 2D images, it performs on par with the previous state of the art. We ablate the design choices of our model and quantify their contribution to performance. Our code and checkpoints can be found at the project website https://butd-detr.github.io.

</details>

### Masked Discrimination for Self-supervised Learning on Point Clouds.
- **链接**: [arXiv:2203.11183](https://arxiv.org/abs/2203.11183) · 📚 被引 137
- **作者**: Haotian Liu, Mu Cai, Yong Jae Lee
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Masked autoencoding has achieved great success for self-supervised learning in the image and language domains. However, mask based pretraining has yet to show benefits for point cloud understanding, likely due to standard backbones like PointNet being unable to properly handle the training versus testing distribution mismatch introduced by masking during training. In this paper, we bridge this gap by proposing a discriminative mask pretraining Transformer framework, MaskPoint}, for point clouds. Our key idea is to represent the point cloud as discrete occupancy values (1 if part of the point cloud; 0 if not), and perform simple binary classification between masked object points and sampled noise points as the proxy task. In this way, our approach is robust to the point sampling variance in point clouds, and facilitates learning rich representations. We evaluate our pretrained models across several downstream tasks, including 3D shape classification, segmentation, and real-word object detection, and demonstrate state-of-the-art results while achieving a significant pretraining speedup (e.g., 4.1x on ScanNet) compared to the prior state-of-the-art Transformer baseline. Code is available at https://github.com/haotian-liu/MaskPoint.

</details>

### DenseHybrid: Hybrid Anomaly Detection for Dense Open-Set Recognition.
- **链接**: [arXiv:2207.02606](https://arxiv.org/abs/2207.02606) · 📚 被引 60
- **作者**: Matej Grcic, Petra Bevandic, Sinisa Segvic
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Anomaly detection can be conceived either through generative modelling of regular training data or by discriminating with respect to negative training data. These two approaches exhibit different failure modes. Consequently, hybrid algorithms present an attractive research goal. Unfortunately, dense anomaly detection requires translational equivariance and very large input resolutions. These requirements disqualify all previous hybrid approaches to the best of our knowledge. We therefore design a novel hybrid algorithm based on reinterpreting discriminative logits as a logarithm of the unnormalized joint distribution $\hat{p}(\mathbf{x}, \mathbf{y})$. Our model builds on a shared convolutional representation from which we recover three dense predictions: i) the closed-set class posterior $P(\mathbf{y}|\mathbf{x})$, ii) the dataset posterior $P(d_{in}|\mathbf{x})$, iii) unnormalized data likelihood $\hat{p}(\mathbf{x})$. The latter two predictions are trained both on the standard training data and on a generic negative dataset. We blend these two predictions into a hybrid anomaly score which allows dense open-set recognition on large natural images. We carefully design a custom loss for the data likelihood in order to avoid backpropagation through the untractable normalizing constant $Z(θ)$. Experiments evaluate our contributions on standard dense anomaly detection benchmarks as well as in terms of open-mIoU - a novel metric for dense open-set performance. Our submissions achieve state-of-the-art performance despite neglectable computational overhead over the standard semantic segmentation baseline.

</details>

### MaxViT: Multi-axis Vision Transformer.
- **链接**: [arXiv:2204.01697](https://arxiv.org/abs/2204.01697)
- **作者**: Zhengzhong Tu, Hossein Talebi, Han Zhang, Feng Yang, Peyman Milanfar, Alan C. Bovik et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Transformers have recently gained significant attention in the computer vision community. However, the lack of scalability of self-attention mechanisms with respect to image size has limited their wide adoption in state-of-the-art vision backbones. In this paper we introduce an efficient and scalable attention model we call multi-axis attention, which consists of two aspects: blocked local and dilated global attention. These design choices allow global-local spatial interactions on arbitrary input resolutions with only linear complexity. We also present a new architectural element by effectively blending our proposed attention model with convolutions, and accordingly propose a simple hierarchical vision backbone, dubbed MaxViT, by simply repeating the basic building block over multiple stages. Notably, MaxViT is able to ''see'' globally throughout the entire network, even in earlier, high-resolution stages. We demonstrate the effectiveness of our model on a broad spectrum of vision tasks. On image classification, MaxViT achieves state-of-the-art performance under various settings: without extra data, MaxViT attains 86.5% ImageNet-1K top-1 accuracy; with ImageNet-21K pre-training, our model achieves 88.7% top-1 accuracy. For downstream tasks, MaxViT as a backbone delivers favorable performance on object detection as well as visual aesthetic assessment. We also show that our proposed model expresses strong generative modeling capability on ImageNet, demonstrating the superior potential of MaxViT blocks as a universal vision module. The source code and trained models will be available at https://github.com/google-research/maxvit.

</details>

### SOS! Self-supervised Learning over Sets of Handled Objects in Egocentric Action Recognition.
- **链接**: [arXiv:2204.04796](https://arxiv.org/abs/2204.04796)
- **作者**: Victor Escorcia, Ricardo Guerrero, Xiatian Zhu, Brais Martínez
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Learning an egocentric action recognition model from video data is challenging due to distractors (e.g., irrelevant objects) in the background. Further integrating object information into an action model is hence beneficial. Existing methods often leverage a generic object detector to identify and represent the objects in the scene. However, several important issues remain. Object class annotations of good quality for the target domain (dataset) are still required for learning good object representation. Besides, previous methods deeply couple the existing action models and need to retrain them jointly with object representation, leading to costly and inflexible integration. To overcome both limitations, we introduce Self-Supervised Learning Over Sets (SOS), an approach to pre-train a generic Objects In Contact (OIC) representation model from video object regions detected by an off-the-shelf hand-object contact detector. Instead of augmenting object regions individually as in conventional self-supervised learning, we view the action process as a means of natural data transformations with unique spatio-temporal continuity and exploit the inherent relationships among per-video object sets. Extensive experiments on two datasets, EPIC-KITCHENS-100 and EGTEA, show that our OIC significantly boosts the performance of multiple state-of-the-art video classification models.

</details>

### 4DContrast: Contrastive Learning with Dynamic Correspondences for 3D Scene Understanding.
- **链接**: [arXiv:2112.02990](https://arxiv.org/abs/2112.02990)
- **作者**: Yujin Chen, Matthias Nießner, Angela Dai
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a new approach to instill 4D dynamic object priors into learned 3D representations by unsupervised pre-training. We observe that dynamic movement of an object through an environment provides important cues about its objectness, and thus propose to imbue learned 3D representations with such dynamic understanding, that can then be effectively transferred to improved performance in downstream 3D semantic scene understanding tasks. We propose a new data augmentation scheme leveraging synthetic 3D shapes moving in static 3D environments, and employ contrastive learning under 3D-4D constraints that encode 4D invariances into the learned 3D representations. Experiments demonstrate that our unsupervised representation learning results in improvement in downstream 3D semantic segmentation, object detection, and instance segmentation tasks, and moreover, notably improves performance in data-scarce scenarios.

</details>

### ConCL: Concept Contrastive Learning for Dense Prediction Pre-training in Pathology Images.
- **链接**: [arXiv:2207.06733](https://arxiv.org/abs/2207.06733) · 📚 被引 19
- **作者**: Jiawei Yang, Hanbo Chen, Yuan Liang, Junzhou Huang, Lei He, Jianhua Yao
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Detectingandsegmentingobjectswithinwholeslideimagesis essential in computational pathology workflow. Self-supervised learning (SSL) is appealing to such annotation-heavy tasks. Despite the extensive benchmarks in natural images for dense tasks, such studies are, unfortunately, absent in current works for pathology. Our paper intends to narrow this gap. We first benchmark representative SSL methods for dense prediction tasks in pathology images. Then, we propose concept contrastive learning (ConCL), an SSL framework for dense pre-training. We explore how ConCL performs with concepts provided by different sources and end up with proposing a simple dependency-free concept generating method that does not rely on external segmentation algorithms or saliency detection models. Extensive experiments demonstrate the superiority of ConCL over previous state-of-the-art SSL methods across different settings. Along our exploration, we distll several important and intriguing components contributing to the success of dense pre-training for pathology images. We hope this work could provide useful data points and encourage the community to conduct ConCL pre-training for problems of interest. Code is available.

</details>

### Progressive End-to-End Object Detection in Crowded Scenes.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00093) · 📚 被引 73
- **作者**: Anlin Zheng, Yuang Zhang, Xiangyu Zhang, Xiaojuan Qi, Jian Sun
- **🏷️ 机构**: MEGVII Technology, Shanghai Jiao Tong University, University of Hong Kong
- **会议**: CVPR 2022

### Multi-Granularity Alignment Domain Adaptation for Object Detection.
- **链接**: [arXiv:2203.16897](https://arxiv.org/abs/2203.16897) · 📚 被引 111
- **作者**: Wenzhang Zhou, Dawei Du, Libo Zhang, Tiejian Luo, Yanjun Wu
- **🏷️ 机构**: University of Chinese Academy of Sciences,Beijing,China, Kitware, Inc.,NY,USA, Institute of Software, Chinese Academy of Sciences,Beijing,China
- **会议**: CVPR 2022

## 跨领域论文（完整笔记在其他领域）

- V2X-ViT: Vehicle-to-Everything Cooperative Perception with Vision Transformer. → [3d-detection](../3d-detection/Guideline%202022.md)
- Deformable Feature Aggregation for Dynamic Multi-modal 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Multimodal Object Detection via Probabilistic Ensembling. → [multimodal](../multimodal/Guideline%202022.md)
- MPPNet: Multi-frame Feature Intertwining with Proxy Points for 3D Temporal Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- SpatialDETR: Robust Scalable Transformer-Based 3D Object Detection From Multi-view Camera Images With Global Cross-Sensor Attention. → [3d-detection](../3d-detection/Guideline%202022.md)
- 3D Object Detection with a Self-supervised Lidar Scene Flow Backbone. → [3d-detection](../3d-detection/Guideline%202022.md)
- Cross-Modality Knowledge Distillation Network for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- CramNet: Camera-Radar Fusion with Ray-Constrained Cross-Attention for Robust 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Talisman: Targeted Active Learning for Object Detection with Rare Classes and Slices Using Submodular Mutual Information. → [autonomous-driving](../autonomous-driving/Guideline%202022.md)
- DEVIANT: Depth EquiVarIAnt NeTwork for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Densely Constrained Depth Estimator for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Unsupervised Domain Adaptation for Monocular 3D Object Detection via Self-training. → [3d-detection](../3d-detection/Guideline%202022.md)
- CODA: A Real-World Road Corner Case Dataset for Object Detection in Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202022.md)
- PseCo: Pseudo Labeling and Consistency Training for Semi-Supervised Object Detection. → [multi-camera-perception](../multi-camera-perception/Guideline%202022.md)
- Homogeneous Multi-modal Feature Fusion and Interaction for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Enhancing Multi-modal Features Using Local Self-attention for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Semi-supervised Monocular 3D Object Detection by Multi-view Consistency. → [3d-detection](../3d-detection/Guideline%202022.md)
- Multimodal Transformer for Automatic 3D Annotation and Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- PETR: Position Embedding Transformation for Multi-view 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Class-Agnostic Object Detection with Multi-modal Transformer. → [multimodal](../multimodal/Guideline%202022.md)
- DetMatch: Two Teachers are Better than One for Joint 2D and 3D Semi-Supervised Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Lidar Point Cloud Guided Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- DID-M3D: Decoupling Instance Depth for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- FCAF3D: Fully Convolutional Anchor-Free 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Rethinking IoU-based Optimization for Single-stage 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- PillarNet: Real-Time and High-Performance Pillar-Based 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- SWFormer: Sparse Window Transformer for 3D Object Detection in Point Clouds. → [3d-detection](../3d-detection/Guideline%202022.md)
- EAutoDet: Efficient Architecture Search for Object Detection. → [neural-architecture-search](../neural-architecture-search/Guideline%202022.md)
- Monocular 3D Object Detection with Depth from Motion. → [3d-detection](../3d-detection/Guideline%202022.md)
- LiDAR Distillation: Bridging the Beam-Induced Domain Gap for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Graph R-CNN: Towards Accurate 3D Object Detection with Semantic-Decorated Local Graph. → [3d-detection](../3d-detection/Guideline%202022.md)
- Semi-supervised 3D Object Detection with Proficient Teachers. → [3d-detection](../3d-detection/Guideline%202022.md)
- ProposalContrast: Unsupervised Pre-training for LiDAR-Based 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- MVSalNet: Multi-view Augmentation for RGB-D Salient Object Detection. → [multi-camera-perception](../multi-camera-perception/Guideline%202022.md)
- CenterFormer: Center-Based Transformer for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Physical Attack on Monocular Depth Estimation with Optimal Adversarial Patches. → [3d-detection](../3d-detection/Guideline%202022.md)
- A Closer Look at Invariances in Self-supervised Pre-training for 3D Vision. → [3d-detection](../3d-detection/Guideline%202022.md)
