# Object Detection — 2024 Guideline

> 领域: 通用 2D 目标检测（检测器架构、密集预测、小物体/旋转框/NMS 等）
> 论文数: 8 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### LLMs Meet VLMs: Boost Open Vocabulary Object Detection with Fine-grained Descriptors.
- **链接**: [出版页](https://openreview.net/forum?id=usrChqw6yK)
- **作者**: Sheng Jin, Xueying Jiang, Jiaxing Huang, Lewei Lu, Shijian Lu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we address the limitations of the DETR-based semi-supervised object detection (SSOD) framework, particularly focusing on the challenges posed by the quality of object queries. In DETR-based SSOD, the one-to-one assignment strategy provides inaccurate pseudo-labels, while the one-to-many assignments strategy leads to overlapping predictions. These issues compromise training efficiency and degrade model performance, especially in detecting small or occluded objects. We introduce Sparse Semi-DETR, a novel transformer-based, end-to-end semi-supervised object detection solution to overcome these challenges. Sparse Semi-DETR incorporates a Query Refinement Module to enhance the quality of object queries, significantly improving detection capabilities for small and partially obscured objects. Additionally, we integrate a Reliable Pseudo-Label Filtering Module that selectively filters high-quality pseudo-labels, thereby enhancing detection accuracy and consistency. On the MS-COCO and Pascal VOC object detection benchmarks, Sparse Semi-DETR achieves a significant improvement over current state-of-the-art methods that highlight Sparse Semi-DETR's effectiveness in semi-supervised object detection, particularly in challenging scenarios involving small or partially obscured objects.

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised landmark estimation is a challenging task that demands the formation of locally distinct feature representations to identify sparse facial landmarks in the absence of annotated data. To tackle this task, existing state-of-the-art (SOTA) methods (1) extract coarse features from backbones that are trained with instance-level self-supervised learning (SSL) paradigms, which neglect the dense prediction nature of the task, (2) aggregate them into memory-intensive hypercolumn formations, and (3) supervise lightweight projector networks to naively establish full local correspondences among all pairs of spatial features. In this paper, we introduce SCE-MAE, a framework that (1) leverages the MAE, a region-level SSL method that naturally better suits the landmark prediction task, (2) operates on the vanilla feature map instead of on expensive hypercolumns, and (3) employs a Correspondence Approximation and Refinement Block (CARB) that utilizes a simple density peak clustering algorithm and our proposed Locality-Constrained Repellence Loss to directly hone only select local correspondences. We demonstrate through extensive experiments that SCE-MAE is highly effective and robust, outperforming existing SOTA methods by large margins of approximately 20%-44% on the landmark matching and approximately 9%-15% on the landmark detection tasks.

</details>

### KD-DETR: Knowledge Distillation for Detection Transformer with Consistent Distillation Points Sampling. **⭐⭐⭐** (相关度: 80%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01516) · 📚 被引 22
- **作者**: Yu Wang, Xin Li, Shengzhao Weng, Gang Zhang, Haixiao Yue, Haocheng Feng et al.
- **🏷️ 机构**: Baidu VIS
- **会议**: CVPR 2024
- **摘要（中）**: 针对检测Transformer中知识蒸馏的蒸馏点采样不一致问题，提出了KD-DETR方法。该方法通过一致的蒸馏点采样策略，提升蒸馏效率。相比现有蒸馏方法，改善了检测性能。实验验证了其有效性。
- **摘要（英）**: This paper addresses the inconsistent distillation point sampling in knowledge distillation for detection transformers by proposing KD-DETR. It introduces a consistent sampling strategy to improve distillation efficiency and detection performance. Experiments validate its effectiveness.
- **核心贡献**: 提出了KD-DETR，通过一致蒸馏点采样提升检测Transformer的蒸馏效果。
- **创新点**: 设计了蒸馏点采样一致性策略，优化知识传递。
- **结果**: 实验表明KD-DETR在检测任务上有效提升性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose InstructDET, a data-centric method for referring object detection (ROD) that localizes target objects based on user instructions. While deriving from referring expressions (REC), the instructions we leverage are greatly diversified to encompass common user intentions related to object detection. For one image, we produce tremendous instructions that refer to every single object and different combinations of multiple objects. Each instruction and its corresponding object bounding boxes (bbxs) constitute one training data pair. In order to encompass common detection expressions, we involve emerging vision-language model (VLM) and large language model (LLM) to generate instructions guided by text prompts and object bbxs, as the generalizations of foundation models are effective to produce human-like expressions (e.g., describing object property, category, and relationship). We name our constructed dataset as InDET. It contains images, bbxs and generalized instructions that are from foundation models. Our InDET is developed from existing REC datasets and object detection datasets, with the expanding potential that any image with object bbxs can be incorporated through using our InstructDET method. By using our InDET dataset, we show that a conventional ROD model surpasses existing methods on standard REC datasets and our InDET test set. Our data-centric method InstructDET, with automatic data expansion by leveraging foundation models, directs a promising field that ROD can be greatly diversified to execute common object detection instructions.

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In recent research, significant attention has been devoted to the open-vocabulary object detection task, aiming to generalize beyond the limited number of classes labeled during training and detect objects described by arbitrary category names at inference. Compared with conventional object detection, open vocabulary object detection largely extends the object detection categories. However, it relies on calculating the similarity between image regions and a set of arbitrary category names with a pretrained vision-and-language model. This implies that, despite its open-set nature, the task still needs the predefined object categories during the inference stage. This raises the question: What if we do not have exact knowledge of object categories during inference? In this paper, we call such a new setting as generative open-ended object detection, which is a more general and practical problem. To address it, we formulate object detection as a generative problem and propose a simple framework named GenerateU, which can detect dense objects and generate their names in a free-form way. Particularly, we employ Deformable DETR as a region proposal generator with a language model translating visual regions to object names. To assess the free-form object detection task, we introduce an evaluation method designed to quantitatively measure the performance of generative outcomes. Extensive experiments demonstrate strong zero-shot detection performance of our GenerateU. For example, on the LVIS dataset, our GenerateU achieves comparable results to the open-vocabulary object detection method GLIP, even though the category names are not seen by GenerateU during inference. Code is available at: https:// github.com/FoundationVision/GenerateU .

</details>

### GLOW: Global Layout Aware Attacks on Object Detection. **⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01146) · 📚 被引 1
- **作者**: Jun Bao, Buyu Liu, Kui Ren, Jun Yu
- **🏷️ 机构**: The State Key Laboratory of Blockchain and Data Security, Zhejiang University, Hangzhou Dianzi University
- **会议**: CVPR 2024
- **摘要（中）**: ①该论文针对目标检测模型对全局布局感知不足的鲁棒性问题，提出了全局布局感知攻击方法。②通过考虑场景的全局布局信息生成对抗样本，以攻击目标检测器。③相比局部攻击方法，该方法更全面地利用场景上下文，可能提高攻击的有效性。④由于摘要缺失，具体效果未提及。
- **摘要（英）**: This paper addresses the robustness of object detection models by proposing global layout aware attacks. It generates adversarial examples considering the global scene layout to attack detectors. Compared to local attacks, this method leverages scene context more comprehensively. Specific results are unavailable due to missing abstract.
- **核心贡献**: 提出全局布局感知的对抗攻击方法，用于评估目标检测器的鲁棒性。
- **创新点**: 利用全局场景布局信息生成更有效的对抗样本。
- **结果**: 具体效果未在摘要中提及。

### Overload: Latency Attacks on Object Detection for Edge Devices. **⭐⭐** (相关度: 30%)
- **链接**: [arXiv:2304.05370](https://arxiv.org/abs/2304.05370) · 📚 被引 17
- **作者**: Erh-Chung Chen, Pin-Yu Chen, I-Hsin Chung, Che-Rung Lee
- **🏷️ 机构**: National Tsing Hua University, IBM Research
- **会议**: CVPR 2024
- **摘要（中）**: 针对深度学习目标检测模型在边缘设备上的推理延迟攻击问题，提出Overload框架，通过优化问题与空间注意力技术生成延迟攻击样本，增加推理计算量。相比现有攻击方法更简单有效，实验在Nvidia NX上使用YOLOv5验证，能显著延长推理时间。
- **摘要（英）**: This paper addresses latency attacks on object detection for edge devices, proposing the Overload framework with a novel optimization and spatial attention to escalate inference cost. Experiments on YOLOv5 with Nvidia NX show simpler and more effective attacks compared to existing methods.
- **核心贡献**: 提出首个针对边缘设备目标检测的延迟攻击框架Overload。
- **创新点**: 将延迟攻击建模为优化问题并引入空间注意力机制。
- **结果**: 在YOLOv5上显著增加推理时间，优于现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Nowadays, the deployment of deep learning-based applications is an essential task owing to the increasing demands on intelligent services. In this paper, we investigate latency attacks on deep learning applications. Unlike common adversarial attacks for misclassification, the goal of latency attacks is to increase the inference time, which may stop applications from responding to the requests within a reasonable time. This kind of attack is ubiquitous for various applications, and we use object detection to demonstrate how such kind of attacks work. We also design a framework named Overload to generate latency attacks at scale. Our method is based on a newly formulated optimization problem and a novel technique, called spatial attention. This attack serves to escalate the required computing costs during the inference time, consequently leading to an extended inference time for object detection. It presents a significant threat, especially to systems with limited computing resources. We conducted experiments using YOLOv5 models on Nvidia NX. Compared to existing methods, our method is simpler and more effective. The experimental results show that with latency attacks, the inference time of a single image can be increased ten times longer in reference to the normal setting. Moreover, our findings pose a potential new threat to all object detection tasks requiring non-maximum suppression (NMS), as our attack is NMS-agnostic.

</details>

### YOLO-World: Real-Time Open-Vocabulary Object Detection. **⭐⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2401.17270](https://arxiv.org/abs/2401.17270) · 📚 被引 708
- **作者**: Tianheng Cheng, Lin Song, Yixiao Ge, Wenyu Liu, Xinggang Wang, Ying Shan
- **🏷️ 机构**: School of EIC, Huazhong University of Science &#x0026; Technology, Tencent AI Lab
- **会议**: CVPR 2024
- **摘要（中）**: 针对YOLO系列检测器依赖预定义类别、无法适应开放场景的问题，提出YOLO-World，通过视觉语言建模和大规模预训练增强开放词汇检测能力。提出可重参数化视觉语言路径聚合网络（RepVL-PAN）和区域文本对比损失，实现视觉与语言信息交互。在LVIS数据集上达到35.4 AP和52.0 FPS（V100），优于多种SOTA方法，并在下游任务中表现优异。
- **摘要（英）**: YOLO-World enhances YOLO with open-vocabulary detection via vision-language modeling and large-scale pretraining, introducing RepVL-PAN and region-text contrastive loss. It achieves 35.4 AP with 52.0 FPS on LVIS, outperforming many SOTA methods in accuracy and speed.
- **核心贡献**: 提出YOLO-World，首个高效开放词汇目标检测框架。
- **创新点**: 设计RepVL-PAN和区域文本对比损失实现视觉语言融合。
- **结果**: 在LVIS上达到35.4 AP和52.0 FPS，优于SOTA。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The You Only Look Once (YOLO) series of detectors have established themselves as efficient and practical tools. However, their reliance on predefined and trained object categories limits their applicability in open scenarios. Addressing this limitation, we introduce YOLO-World, an innovative approach that enhances YOLO with open-vocabulary detection capabilities through vision-language modeling and pre-training on large-scale datasets. Specifically, we propose a new Re-parameterizable Vision-Language Path Aggregation Network (RepVL-PAN) and region-text contrastive loss to facilitate the interaction between visual and linguistic information. Our method excels in detecting a wide range of objects in a zero-shot manner with high efficiency. On the challenging LVIS dataset, YOLO-World achieves 35.4 AP with 52.0 FPS on V100, which outperforms many state-of-the-art methods in terms of both accuracy and speed. Furthermore, the fine-tuned YOLO-World achieves remarkable performance on several downstream tasks, including object detection and open-vocabulary instance segmentation.

</details>

### Improving Single Domain-Generalized Object Detection: A Focus on Diversification and Alignment. **⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2405.14497](https://arxiv.org/abs/2405.14497) · 📚 被引 27
- **作者**: Muhammad Sohail Danish, Muhammad Haris Khan, Muhammad Akhtar Munir, M. Saquib Sarfraz, Mohsen Ali
- **🏷️ 机构**: Mohamed bin Zayed University of Artificial Intelligence, Mercedes-Benz Tech Innovation, Information Technology, University of Punjab
- **会议**: CVPR 2024
- **摘要（中）**: 针对单源域泛化目标检测问题，提出通过多样化源域和基于类别置信度与定位的检测对齐方法。通过精心选择增强集，基础检测器即可超越现有单域泛化方法；对齐多视图检测结果提升泛化性和校准性。方法检测器无关，适用于单阶段和两阶段检测器，在多个域偏移场景中验证有效性。
- **摘要（英）**: This paper addresses single domain-generalized object detection by diversifying the source domain and aligning detections based on class confidence and localization. The approach improves generalization and calibration, outperforming existing methods and being detector-agnostic.
- **核心贡献**: 提出结合数据增强和检测对齐的单域泛化检测方法。
- **创新点**: 利用增强选择和检测对齐提升泛化性。
- **结果**: 在多个域偏移场景中优于现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this work, we tackle the problem of domain generalization for object detection, specifically focusing on the scenario where only a single source domain is available. We propose an effective approach that involves two key steps: diversifying the source domain and aligning detections based on class prediction confidence and localization. Firstly, we demonstrate that by carefully selecting a set of augmentations, a base detector can outperform existing methods for single domain generalization by a good margin. This highlights the importance of domain diversification in improving the performance of object detectors. Secondly, we introduce a method to align detections from multiple views, considering both classification and localization outputs. This alignment procedure leads to better generalized and well-calibrated object detector models, which are crucial for accurate decision-making in safety-critical applications. Our approach is detector-agnostic and can be seamlessly applied to both single-stage and two-stage detectors. To validate the effectiveness of our proposed methods, we conduct extensive experiments and ablations on challenging domain-shift scenarios. The results consistently demonstrate the superiority of our approach compared to existing methods. Our code and models are available at: https://github.com/msohaildanish/DivAlign

</details>

### D3T: Distinctive Dual-Domain Teacher Zigzagging Across RGB-Thermal Gap for Domain-Adaptive Object Detection. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2403.09359](https://arxiv.org/abs/2403.09359) · 📚 被引 18
- **作者**: Dinh Phat Do, Taehoon Kim, Jaemin Na, Jiwon Kim, Keonho Lee, Kyunghwan Cho et al.
- **🏷️ 机构**: Ajou University,Korea, Hyundai Motor Company,Robotics Lab
- **会议**: CVPR 2024
- **摘要（中）**: 针对可见光到热红外域自适应目标检测中域差距过大的问题，提出D3T框架，采用双域教师和不同训练范式。分离源和目标训练集构建双教师，分别对每个域应用指数移动平均，并引入双教师间的zigzag学习方法，实现从可见光到热红外的渐进过渡。在FLIR和KAIST数据集上验证了方法的优越性。
- **摘要（英）**: D3T addresses visible-to-thermal domain adaptation for object detection by proposing a dual-teacher framework with distinct training paradigms and zigzag learning. It effectively bridges the large domain gap, validated on FLIR and KAIST datasets.
- **核心贡献**: 提出D3T双域教师框架用于可见光到热红外的域自适应检测。
- **创新点**: 采用双教师和zigzag学习实现渐进域迁移。
- **结果**: 在FLIR和KAIST上优于现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Domain adaptation for object detection typically entails transferring knowledge from one visible domain to another visible domain. However, there are limited studies on adapting from the visible to the thermal domain, because the domain gap between the visible and thermal domains is much larger than expected, and traditional domain adaptation can not successfully facilitate learning in this situation. To overcome this challenge, we propose a Distinctive Dual-Domain Teacher (D3T) framework that employs distinct training paradigms for each domain. Specifically, we segregate the source and target training sets for building dual-teachers and successively deploy exponential moving average to the student model to individual teachers of each domain. The framework further incorporates a zigzag learning method between dual teachers, facilitating a gradual transition from the visible to thermal domains during training. We validate the superiority of our method through newly designed experimental protocols with well-known thermal datasets, i.e., FLIR and KAIST. Source code is available at https://github.com/EdwardDo69/D3T .

</details>

### Boosting Object Detection with Zero-Shot Day-Night Domain Adaptation. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2312.01220](https://arxiv.org/abs/2312.01220) · 📚 被引 70
- **作者**: Zhipeng Du, Miaojing Shi, Jiankang Deng
- **🏷️ 机构**: King&#x0027;s College,Department of Informatics,London, College of Electronic and Information Engineering, Tongji University, Imperial College,Department of Computing,London
- **会议**: CVPR 2024
- **摘要（中）**: 针对低光环境下目标检测性能显著下降且真实低光数据难以收集标注的问题，提出零样本昼夜域自适应方法，旨在无需真实低光数据即可将检测器从良好光照泛化到低光场景。方法上，重新审视Retinex理论，设计反射率表示学习模块，通过光照不变性强化策略学习图像中的Retinex基础光照不变性，并引入互换-重分解-一致性流程改进传统Retinex分解，包括两次顺序分解和重分解一致性损失。相比已有依赖真实低光数据或图像增强的方法，该方法避免了数据收集成本，在ExDark和DARK FACE等数据集上验证了有效性。
- **摘要（英）**: This paper addresses the challenge of low-light object detection by proposing a zero-shot day-night domain adaptation method that generalizes detectors from well-lit to low-light scenarios without real low-light data. It introduces a reflectance representation learning module with illumination invariance reinforcement and an interchange-redecomposition-coherence procedure to improve Retinex-based image decomposition, validated on ExDark and DARK FACE datasets.
- **核心贡献**: 提出首个零样本昼夜域自适应框架，无需真实低光数据即可提升低光目标检测性能。
- **创新点**: 设计光照不变性强化策略和重分解一致性损失，改进Retinex分解过程。
- **结果**: 在ExDark和DARK FACE数据集上显著提升低光检测性能，优于现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Detecting objects in low-light scenarios presents a persistent challenge, as detectors trained on well-lit data exhibit significant performance degradation on low-light data due to low visibility. Previous methods mitigate this issue by exploring image enhancement or object detection techniques with real low-light image datasets. However, the progress is impeded by the inherent difficulties about collecting and annotating low-light images. To address this challenge, we propose to boost low-light object detection with zero-shot day-night domain adaptation, which aims to generalize a detector from well-lit scenarios to low-light ones without requiring real low-light data. Revisiting Retinex theory in the low-level vision, we first design a reflectance representation learning module to learn Retinex-based illumination invariance in images with a carefully designed illumination invariance reinforcement strategy. Next, an interchange-redecomposition-coherence procedure is introduced to improve over the vanilla Retinex image decomposition process by performing two sequential image decompositions and introducing a redecomposition cohering loss. Extensive experiments on ExDark, DARK FACE, and CODaN datasets show strong low-light generalizability of our method. Our code is available at https://github.com/ZPDu/DAI-Net.

</details>

### InstaGen: Enhancing Object Detection by Training on Synthetic Dataset. **⭐⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2402.05937](https://arxiv.org/abs/2402.05937) · 📚 被引 27
- **作者**: Chengjian Feng, Yujie Zhong, Zequn Jie, Weidi Xie, Lin Ma
- **🏷️ 机构**: Meituan Inc., CMIC, Shanghai Jiao Tong University
- **会议**: CVPR 2024
- **摘要（中）**: 针对扩散模型生成数据难以直接用于目标检测训练的问题，提出InstaGen范式，通过集成实例级定位头到预训练扩散模型中，增强其生成图像中的实例定位能力。方法上，利用现成检测器监督对齐类别文本嵌入与区域视觉特征，并设计自训练方案处理检测器未覆盖的新类别。相比现有数据合成方法，InstaGen在开放词汇场景提升4.5 AP，数据稀疏场景提升1.2至5.2 AP，展示了扩散模型作为数据合成器的潜力。
- **摘要（英）**: This paper presents InstaGen, a paradigm that enhances object detection by training on synthetic data from diffusion models, integrating an instance-level grounding head to localize objects in generated images. It uses an off-the-shelf detector for supervision and a self-training scheme for novel categories, achieving +4.5 AP in open-vocabulary and +1.2 to 5.2 AP in data-sparse scenarios.
- **核心贡献**: 提出基于扩散模型的数据合成框架，增强检测器在开放词汇和数据稀疏场景的性能。
- **创新点**: 集成实例级定位头到扩散模型，并设计自训练方案处理新类别。
- **结果**: 在开放词汇和数据稀疏场景分别提升4.5 AP和1.2至5.2 AP。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we present a novel paradigm to enhance the ability of object detector, e.g., expanding categories or improving detection performance, by training on synthetic dataset generated from diffusion models. Specifically, we integrate an instance-level grounding head into a pre-trained, generative diffusion model, to augment it with the ability of localising instances in the generated images. The grounding head is trained to align the text embedding of category names with the regional visual feature of the diffusion model, using supervision from an off-the-shelf object detector, and a novel self-training scheme on (novel) categories not covered by the detector. We conduct thorough experiments to show that, this enhanced version of diffusion model, termed as InstaGen, can serve as a data synthesizer, to enhance object detectors by training on its generated samples, demonstrating superior performance over existing state-of-the-art methods in open-vocabulary (+4.5 AP) and data-sparse (+1.2 to 5.2 AP) scenarios. Project page with code: https://fcjian.github.io/InstaGen.

</details>

### Few-Shot Object Detection with Foundation Models. **⭐⭐⭐** (相关度: 80%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02703) · 📚 被引 63
- **作者**: Guangxing Han, Ser-Nam Lim
- **🏷️ 机构**: Columbia University, University of Central Florida
- **会议**: CVPR 2024
- **摘要（中）**: 该论文摘要为空，无法获取具体内容。基于标题推测，论文探讨利用基础模型（如预训练视觉语言模型）进行少样本目标检测，旨在解决标注数据稀缺问题。方法可能涉及微调或提示学习，但缺乏细节。相比传统少样本检测方法，基础模型可能提供更强的泛化能力，但效果未知。
- **摘要（英）**: This paper likely addresses few-shot object detection using foundation models, aiming to overcome annotation scarcity. The abstract is unavailable, so specific methods and results cannot be assessed, but the approach may leverage pre-trained models for improved generalization.
- **核心贡献**: 探索基础模型在少样本目标检测中的应用。
- **创新点**: 利用基础模型的预训练知识提升少样本泛化。
- **结果**: 未提供具体数据。

### Endow SAM with Keen Eyes: Temporal-Spatial Prompt Learning for Video Camouflaged Object Detection. **⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01803) · 📚 被引 22
- **作者**: Wenjun Hui, Zhenfeng Zhu, Shuai Zheng, Yao Zhao
- **🏷️ 机构**: Institute of Information Science, Beijing Jiaotong University
- **会议**: CVPR 2024
- **摘要（中）**: 该论文摘要为空，无法获取具体内容。基于标题推测，论文旨在增强SAM（Segment Anything Model）在视频伪装目标检测中的能力，通过时间-空间提示学习。方法可能涉及设计提示模块利用视频帧间信息，但缺乏细节。相比静态图像方法，视频伪装检测需处理动态变化，但效果未知。
- **摘要（英）**: This paper likely enhances SAM for video camouflaged object detection via temporal-spatial prompt learning, addressing dynamic camouflage challenges. The abstract is unavailable, so specific methods and results cannot be assessed.
- **核心贡献**: 探索SAM在视频伪装目标检测中的应用。
- **创新点**: 利用时间-空间提示学习增强视频分割能力。
- **结果**: 未提供具体数据。

### CAT: Exploiting Inter-Class Dynamics for Domain Adaptive Object Detection. **⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2403.19278](https://arxiv.org/abs/2403.19278) · 📚 被引 46
- **作者**: Mikhail Kennerley, Jian-Gang Wang, Bharadwaj Veeravalli, Robby T. Tan
- **🏷️ 机构**: National University of Singapore,Department of Electrical and Computer Engineering, Institute for Infocomm Research,A*STAR, ASUS Intelligent Cloud Services
- **会议**: CVPR 2024
- **摘要（中）**: ①该论文针对域自适应目标检测中因标注数据类别不平衡导致的伪标签不准确和类别偏差问题。②提出了类感知教师（CAT）框架，包含类间关系模块（ICRm）来近似类间关系，并利用该关系对高度相关的类（跨域和域内）应用增强，以提升少数类性能同时最小化对多数类的影响；此外，在分类损失中引入类关系权重进一步减少偏差。③相比现有半监督师生框架，创新性地显式建模类间动态关系来缓解类别不平衡，而非仅依赖伪标签质量。④在多个数据集上的实验和消融研究验证了该方法能有效解决域适应中的类别偏差问题，但摘要未提供具体数值。
- **摘要（英）**: This paper addresses class bias in domain adaptive object detection caused by imbalanced labeled data, which leads to inaccurate pseudo-labels. The proposed Class-Aware Teacher (CAT) introduces an Inter-Class Relation module (ICRm) to model class relationships and applies augmentations to related classes across domains, along with a class-relation weighted classification loss, to boost minority class performance while preserving majority classes. Experiments on multiple datasets demonstrate effectiveness in mitigating class bias, though specific metrics are not reported in the abstract.
- **核心贡献**: 提出了CAT框架，通过显式建模类间关系并应用于增强和损失加权，缓解域适应目标检测中的类别偏差。
- **创新点**: 创新性地利用类间动态关系模块（ICRm）指导数据增强和损失设计，以平衡多数类和少数类的影响。
- **结果**: 在多个数据集上验证了方法能有效减少类别偏差，但未给出具体性能数值。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Domain adaptive object detection aims to adapt detection models to domains where annotated data is unavailable. Existing methods have been proposed to address the domain gap using the semi-supervised student-teacher framework. However, a fundamental issue arises from the class imbalance in the labelled training set, which can result in inaccurate pseudo-labels. The relationship between classes, especially where one class is a majority and the other minority, has a large impact on class bias. We propose Class-Aware Teacher (CAT) to address the class bias issue in the domain adaptation setting. In our work, we approximate the class relationships with our Inter-Class Relation module (ICRm) and exploit it to reduce the bias within the model. In this way, we are able to apply augmentations to highly related classes, both inter- and intra-domain, to boost the performance of minority classes while having minimal impact on majority classes. We further reduce the bias by implementing a class-relation weight to our classification loss. Experiments conducted on various datasets and ablation studies show that our method is able to address the class bias in the domain adaptation setting. On the Cityscapes to Foggy Cityscapes dataset, we attained a 52.5 mAP, a substantial improvement over the 51.2 mAP achieved by the state-of-the-art method.

</details>

### Retrieval-Augmented Open-Vocabulary Object Detection.
- **链接**: [arXiv:2404.05687](https://arxiv.org/abs/2404.05687) · 📚 被引 23
- **作者**: Jooyeon Kim, Eulrang Cho, Sehyung Kim, Hyunwoo J. Kim
- **🏷️ 机构**: Korea University,Department of Computer Science and Engineering, Samsung Research
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-vocabulary object detection (OVD) has been studied with Vision-Language Models (VLMs) to detect novel objects beyond the pre-trained categories. Previous approaches improve the generalization ability to expand the knowledge of the detector, using 'positive' pseudo-labels with additional 'class' names, e.g., sock, iPod, and alligator. To extend the previous methods in two aspects, we propose Retrieval-Augmented Losses and visual Features (RALF). Our method retrieves related 'negative' classes and augments loss functions. Also, visual features are augmented with 'verbalized concepts' of classes, e.g., worn on the feet, handheld music player, and sharp teeth. Specifically, RALF consists of two modules: Retrieval Augmented Losses (RAL) and Retrieval-Augmented visual Features (RAF). RAL constitutes two losses reflecting the semantic similarity with negative vocabularies. In addition, RAF augments visual features with the verbalized concepts from a large language model (LLM). Our experiments demonstrate the effectiveness of RALF on COCO and LVIS benchmark datasets. We achieve improvement up to 3.4 box AP$_{50}^{\text{N}}$ on novel categories of the COCO dataset and 3.6 mask AP$_{\text{r}}$ gains on the LVIS dataset. Code is available at https://github.com/mlvlab/RALF .

</details>

### Unleashing Channel Potential: Space-Frequency Selection Convolution for SAR Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01640) · 📚 被引 78
- **作者**: Ke Li, Di Wang, Zhangyuan Hu, Wenxuan Zhu, Shaofeng Li, Quan Wang
- **🏷️ 机构**: School of Computer Science and Technology, Xidian University,Xi&#x2019; an,China
- **会议**: CVPR 2024

### Learning Background Prompts to Discover Implicit Knowledge for Open Vocabulary Object Detection.
- **链接**: [arXiv:2406.00510](https://arxiv.org/abs/2406.00510) · 📚 被引 27
- **作者**: Jiaming Li, Jiacheng Zhang, Jichang Li, Ge Li, Si Liu, Liang Lin et al.
- **🏷️ 机构**: School of Computer Science and Engineering, Sun Yat-sen University,Guangzhou,China, Shenzhen Graduate School, Peking University,SECE,Shenzhen,China, Institute of Artificial Intelligence, Beihang University,China
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open vocabulary object detection (OVD) aims at seeking an optimal object detector capable of recognizing objects from both base and novel categories. Recent advances leverage knowledge distillation to transfer insightful knowledge from pre-trained large-scale vision-language models to the task of object detection, significantly generalizing the powerful capabilities of the detector to identify more unknown object categories. However, these methods face significant challenges in background interpretation and model overfitting and thus often result in the loss of crucial background knowledge, giving rise to sub-optimal inference performance of the detector. To mitigate these issues, we present a novel OVD framework termed LBP to propose learning background prompts to harness explored implicit background knowledge, thus enhancing the detection performance w.r.t. base and novel categories. Specifically, we devise three modules: Background Category-specific Prompt, Background Object Discovery, and Inference Probability Rectification, to empower the detector to discover, represent, and leverage implicit object knowledge explored from background proposals. Evaluation on two benchmark datasets, OV-COCO and OV-LVIS, demonstrates the superiority of our proposed method over existing state-of-the-art approaches in handling the OVD tasks.

</details>

### SHiNe: Semantic Hierarchy Nexus for Open-Vocabulary Object Detection.
- **链接**: [arXiv:2405.10053](https://arxiv.org/abs/2405.10053) · 📚 被引 14
- **作者**: Mingxuan Liu, Tyler L. Hayes, Elisa Ricci, Gabriela Csurka, Riccardo Volpi
- **🏷️ 机构**: University of Trento, NAVER LABS Europe
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-vocabulary object detection (OvOD) has transformed detection into a language-guided task, empowering users to freely define their class vocabularies of interest during inference. However, our initial investigation indicates that existing OvOD detectors exhibit significant variability when dealing with vocabularies across various semantic granularities, posing a concern for real-world deployment. To this end, we introduce Semantic Hierarchy Nexus (SHiNe), a novel classifier that uses semantic knowledge from class hierarchies. It runs offline in three steps: i) it retrieves relevant super-/sub-categories from a hierarchy for each target class; ii) it integrates these categories into hierarchy-aware sentences; iii) it fuses these sentence embeddings to generate the nexus classifier vector. Our evaluation on various detection benchmarks demonstrates that SHiNe enhances robustness across diverse vocabulary granularities, achieving up to +31.9% mAP50 with ground truth hierarchies, while retaining improvements using hierarchies generated by large language models. Moreover, when applied to open-vocabulary classification on ImageNet-1k, SHiNe improves the CLIP zero-shot baseline by +2.8% accuracy. SHiNe is training-free and can be seamlessly integrated with any off-the-shelf OvOD detector, without incurring additional computational overhead during inference. The code is open source.

</details>

### Unbiased Faster R-CNN for Single-source Domain Generalized Object Detection.
- **链接**: [arXiv:2405.15225](https://arxiv.org/abs/2405.15225) · 📚 被引 50
- **作者**: Yajing Liu, Shijun Zhou, Xiyao Liu, Chunhui Hao, Baojie Fan, Jiandong Tian
- **🏷️ 机构**: Shenyang Institute of Automation, Chinese Academy of Sciences,State Key Laboratory of Robotics, Nanjing University of Posts and Telecommunications
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Single-source domain generalization (SDG) for object detection is a challenging yet essential task as the distribution bias of the unseen domain degrades the algorithm performance significantly. However, existing methods attempt to extract domain-invariant features, neglecting that the biased data leads the network to learn biased features that are non-causal and poorly generalizable. To this end, we propose an Unbiased Faster R-CNN (UFR) for generalizable feature learning. Specifically, we formulate SDG in object detection from a causal perspective and construct a Structural Causal Model (SCM) to analyze the data bias and feature bias in the task, which are caused by scene confounders and object attribute confounders. Based on the SCM, we design a Global-Local Transformation module for data augmentation, which effectively simulates domain diversity and mitigates the data bias. Additionally, we introduce a Causal Attention Learning module that incorporates a designed attention invariance loss to learn image-level features that are robust to scene confounders. Moreover, we develop a Causal Prototype Learning module with an explicit instance constraint and an implicit prototype constraint, which further alleviates the negative impact of object attribute confounders. Experimental results on five scenes demonstrate the prominent generalization ability of our method, with an improvement of 3.9% mAP on the Night-Clear scene.

</details>

### VSCode: General Visual Salient and Camouflaged Object Detection with 2D Prompt Learning.
- **链接**: [arXiv:2311.15011](https://arxiv.org/abs/2311.15011) · 📚 被引 128
- **作者**: Ziyang Luo, Nian Liu, Wangbo Zhao, Xuguang Yang, Dingwen Zhang, Deng-Ping Fan et al.
- **🏷️ 机构**: Northwestern Polytechnical University, Mohamed bin Zayed University of Artificial Intelligence, National University of Singapore
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Salient object detection (SOD) and camouflaged object detection (COD) are related yet distinct binary mapping tasks. These tasks involve multiple modalities, sharing commonalities and unique cues. Existing research often employs intricate task-specific specialist models, potentially leading to redundancy and suboptimal results. We introduce VSCode, a generalist model with novel 2D prompt learning, to jointly address four SOD tasks and three COD tasks. We utilize VST as the foundation model and introduce 2D prompts within the encoder-decoder architecture to learn domain and task-specific knowledge on two separate dimensions. A prompt discrimination loss helps disentangle peculiarities to benefit model optimization. VSCode outperforms state-of-the-art methods across six tasks on 26 datasets and exhibits zero-shot generalization to unseen tasks by combining 2D prompts, such as RGB-D COD. Source code has been available at https://github.com/Sssssuperior/VSCode.

</details>

### Active Domain Adaptation with False Negative Prediction for Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02719) · 📚 被引 10
- **作者**: Yuzuru Nakamura, Yasunori Ishii, Takayoshi Yamashita
- **🏷️ 机构**: Panasonic Holdings Corporation, Chubu University
- **会议**: CVPR 2024

### Neural Exposure Fusion for High-Dynamic Range Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01663) · 📚 被引 12
- **作者**: Emmanuel Onzon, Maximilian Bömer, Fahim Mannan, Felix Heide
- **🏷️ 机构**: Torc Robotics
- **会议**: CVPR 2024

### CrossKD: Cross-Head Knowledge Distillation for Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01563) · 📚 被引 119
- **作者**: Jiabao Wang, Yuming Chen, Zhaohui Zheng, Xiang Li, Ming-Ming Cheng, Qibin Hou
- **🏷️ 机构**: College of Computer Science, Nankai University,VCIP, NKIARI,Shenzhen Futian
- **会议**: CVPR 2024

### A-Teacher: Asymmetric Network for 3D Semi-Supervised Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01419) · 📚 被引 8
- **作者**: Hanshi Wang, Zhipeng Zhang, Jin Gao, Weiming Hu
- **🏷️ 机构**: CASIA,State Key Laboratory of Multimodal Artificial Intelligence Systems (MAIS), KargoBot
- **会议**: CVPR 2024

### SNIDA: Unlocking Few-Shot Object Detection with Non-Linear Semantic Decoupling Augmentation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01192) · 📚 被引 31
- **作者**: Yanjie Wang, Xu Zou, Luxin Yan, Sheng Zhong, Jiahuan Zhou
- **🏷️ 机构**: Huazhong University of Science and Technology,Wuhan,China,430074, Wangxuan Institute of Computer Technology, Peking University,Beijing,China,100871
- **会议**: CVPR 2024

> 同领域其他年份: 

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Object detection with event cameras benefits from the sensor's low latency and high dynamic range. However, it is costly to fully label event streams for supervised training due to their high temporal resolution. To reduce this cost, we present LEOD, the first method for label-efficient event-based detection. Our approach unifies weakly- and semi-supervised object detection with a self-training mechanism. We first utilize a detector pre-trained on limited labels to produce pseudo ground truth on unlabeled events. Then, the detector is re-trained with both real and generated labels. Leveraging the temporal consistency of events, we run bi-directional inference and apply tracking-based post-processing to enhance the quality of pseudo labels. To stabilize training against label noise, we further design a soft anchor assignment strategy. We introduce new experimental protocols to evaluate the task of label-efficient event-based detection on Gen1 and 1Mpx datasets. LEOD consistently outperforms supervised baselines across various labeling ratios. For example, on Gen1, it improves mAP by 8.6% and 7.8% for RVT-S trained with 1% and 2% labels. On 1Mpx, RVT-S with 10% labels even surpasses its fully-supervised counterpart using 100% labels. LEOD maintains its effectiveness even when all labeled data are available, reaching new state-of-the-art results. Finally, we show that our method readily scales to improve larger detectors as well. Code is released at https://github.com/Wuziyi616/LEOD

</details>

> Despite previous DETR-like methods having performed successfully in generic object detection, tiny object detection is still a challenging task for them since the positional information of object queries is not customized for detecting tiny objects, whose scale is extraordinarily smaller than general objects. Also, DETR-like methods using a fixed number of queries make them unsuitable for aerial datasets, which only contain tiny objects, and the numbers of instances are imbalanced between different images. Thus, we present a simple yet effective model, named DQ-DETR, which consists of three different components: categorical counting module, counting-guided feature enhancement, and dynamic query selection to solve the above-mentioned problems. DQ-DETR uses the prediction and density maps from the categorical counting module to dynamically adjust the number of object queries and improve the positional information of queries. Our model DQ-DETR outperforms previous CNN-based and DETR-like methods, achieving state-of-the-art mAP 30.2% on the AI-TOD-V2 dataset, which mostly consists of tiny objects. Our code will be available at https://github.com/hoiliu-0801/DQ-DETR.

</details>

### Grounding DINO: Marrying DINO with Grounded Pre-training for Open-Set Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72970-6_3)
- **作者**: Shilong Liu, Zhaoyang Zeng, Tianhe Ren, Feng Li, Hao Zhang, Jie Yang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### SEED: A Simple and Effective 3D DETR in Point Clouds.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73247-8_7) · 📚 被引 14
- **作者**: Zhe Liu, Jinghua Hou, Xiaoqing Ye, Tong Wang, Jingdong Wang, Xiang Bai
- **🏷️ 机构**: HUAST
- **会议**: ECCV 2024

### Cross-Domain Few-Shot Object Detection via Enhanced Open-Set Object Detector.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73636-0_15)
- **作者**: Yuqian Fu, Yu Wang, Yixuan Pan, Lian Huai, Xingyu Qiu, Zeyu Shangguan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### MarvelOVD: Marrying Object Recognition and Vision-Language Models for Robust Open-Vocabulary Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72643-9_7)
- **作者**: Kuo Wang, Lechao Cheng, Weikai Chen, Pingping Zhang, Liang Lin, Fan Zhou et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### CSOT: Cross-scan Object Transfer for Semi-Supervised LiDAR Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72643-9_20) · 📚 被引 1
- **作者**: Jinglin Zhan, Tiejun Liu, Rengang Li, Zhaoxiang Zhang, Yuntao Chen
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Crowd-SAM: SAM as a Smart Annotator for Object Detection in Crowded Scenes.
- **链接**: [arXiv:2407.11464](https://arxiv.org/abs/2407.11464) · [代码](https://github.com/FelixCaae/CrowdSAM) · 📚 被引 15
- **作者**: Zhi Cai, Yingjie Gao, Yaoyan Zheng, Nan Zhou, Di Huang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In computer vision, object detection is an important task that finds its application in many scenarios. However, obtaining extensive labels can be challenging, especially in crowded scenes. Recently, the Segment Anything Model (SAM) has been proposed as a powerful zero-shot segmenter, offering a novel approach to instance segmentation tasks. However, the accuracy and efficiency of SAM and its variants are often compromised when handling objects in crowded and occluded scenes. In this paper, we introduce Crowd-SAM, a SAM-based framework designed to enhance SAM's performance in crowded and occluded scenes with the cost of few learnable parameters and minimal labeled images. We introduce an efficient prompt sampler (EPS) and a part-whole discrimination network (PWD-Net), enhancing mask selection and accuracy in crowded scenes. Despite its simplicity, Crowd-SAM rivals state-of-the-art (SOTA) fully-supervised object detection methods on several benchmarks including CrowdHuman and CityPersons. Our code is available at https://github.com/FelixCaae/CrowdSAM.

</details>

### Embracing Events and Frames with Hierarchical Feature Refinement Network for Object Detection.
- **链接**: [arXiv:2407.12582](https://arxiv.org/abs/2407.12582) · [代码](https://github.com/HuCaoFighting/FRN) · 📚 被引 19
- **作者**: Hu Cao, Zehua Zhang, Yan Xia, Xinyi Li, Jiahao Xia, Guang Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In frame-based vision, object detection faces substantial performance degradation under challenging conditions due to the limited sensing capability of conventional cameras. Event cameras output sparse and asynchronous events, providing a potential solution to solve these problems. However, effectively fusing two heterogeneous modalities remains an open issue. In this work, we propose a novel hierarchical feature refinement network for event-frame fusion. The core concept is the design of the coarse-to-fine fusion module, denoted as the cross-modality adaptive feature refinement (CAFR) module. In the initial phase, the bidirectional cross-modality interaction (BCI) part facilitates information bridging from two distinct sources. Subsequently, the features are further refined by aligning the channel-level mean and variance in the two-fold adaptive feature refinement (TAFR) part. We conducted extensive experiments on two benchmarks: the low-resolution PKU-DDD17-Car dataset and the high-resolution DSEC dataset. Experimental results show that our method surpasses the state-of-the-art by an impressive margin of $\textbf{8.0}\%$ on the DSEC dataset. Besides, our method exhibits significantly better robustness (\textbf{69.5}\% versus \textbf{38.7}\%) when introducing 15 different corruption types to the frame images. The code can be found at the link (https://github.com/HuCaoFighting/FRN).

</details>

### DeTra: A Unified Model for Object Detection and Trajectory Forecasting.
- **链接**: [arXiv:2406.04426](https://arxiv.org/abs/2406.04426) · 📚 被引 8
- **作者**: Sergio Casas, Ben Agro, Jiageng Mao, Thomas Gilles, Alexander Cui, Thomas Li et al.
- **🏷️ 机构**: Waabi / University of Toronto
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Oriented object detection has been developed rapidly in the past few years, where rotation equivariance is crucial for detectors to predict rotated boxes. It is expected that the prediction can maintain the corresponding rotation when objects rotate, but severe mutation in angular prediction is sometimes observed when objects rotate near the boundary angle, which is well-known boundary discontinuity problem. The problem has been long believed to be caused by the sharp loss increase at the angular boundary, and widely used joint-optim IoU-like methods deal with this problem by loss-smoothing. However, we experimentally find that even state-of-the-art IoU-like methods actually fail to solve the problem. On further analysis, we find that the key to solution lies in encoding mode of the smoothing function rather than in joint or independent optimization. In existing IoU-like methods, the model essentially attempts to fit the angular relationship between box and object, where the break point at angular boundary makes the predictions highly unstable.To deal with this issue, we propose a dual-optimization paradigm for angles. We decouple reversibility and joint-optim from single smoothing function into two distinct entities, which for the first time achieves the objectives of both correcting angular boundary and blending angle with other parameters.Extensive experiments on multiple datasets show that boundary discontinuity problem is well-addressed. Moreover, typical IoU-like methods are improved to the same level without obvious performance gap. The code is available at https://github.com/hangxu-cv/cvpr24acm.

</details>

### Just a Hint: Point-Supervised Camouflaged Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72761-0_19) · 📚 被引 21
- **作者**: Huafeng Chen, Dian Shao, Guangqian Guo, Shan Gao
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Annotating datasets for object detection is an expensive and time-consuming endeavor. To minimize this burden, active learning (AL) techniques are employed to select the most informative samples for annotation within a constrained "annotation budget". Traditional AL strategies typically rely on model uncertainty or sample diversity for query sampling, while more advanced methods have focused on developing AL-specific object detector architectures to enhance performance. However, these specialized approaches are not readily adaptable to different object detectors due to the significant engineering effort required for integration. To overcome this challenge, we introduce Plug and Play Active Learning (PPAL), a simple and effective AL strategy for object detection. PPAL is a two-stage method comprising uncertainty-based and diversity-based sampling phases. In the first stage, our Difficulty Calibrated Uncertainty Sampling leverage a category-wise difficulty coefficient that combines both classification and localisation difficulties to re-weight instance uncertainties, from which we sample a candidate pool for the subsequent diversity-based sampling. In the second stage, we propose Category Conditioned Matching Similarity to better compute the similarities of multi-instance images as ensembles of their instance similarities, which is used by the k-Means++ algorithm to sample the final AL queries. PPAL makes no change to model architectures or detector training pipelines; hence it can be easily generalized to different object detectors. We benchmark PPAL on the MS-COCO and Pascal VOC datasets using different detector architectures and show that our method outperforms prior work by a large margin. Code is available at https://github.com/ChenhongyiYang/PPAL

</details>

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Accurately detecting active objects undergoing state changes is essential for comprehending human interactions and facilitating decision-making. The existing methods for active object detection (AOD) primarily rely on visual appearance of the objects within input, such as changes in size, shape and relationship with hands. However, these visual changes can be subtle, posing challenges, particularly in scenarios with multiple distracting no-change instances of the same category. We observe that the state changes are often the result of an interaction being performed upon the object, thus propose to use informed priors about object related plausible interactions (including semantics and visual appearance) to provide more reliable cues for AOD. Specifically, we propose a knowledge aggregation procedure to integrate the aforementioned informed priors into oracle queries within the teacher decoder, offering more object affordance commonsense to locate the active object. To streamline the inference process and reduce extra knowledge inputs, we propose a knowledge distillation approach that encourages the student decoder to mimic the detection capabilities of the teacher decoder using the oracle query by replicating its predictions and attention. Our proposed framework achieves state-of-the-art performance on four datasets, namely Ego4D, Epic-Kitchens, MECCANO, and 100DOH, which demonstrates the effectiveness of our approach in improving AOD.

</details>

### Dynamic Retraining-Updating Mean Teacher for Source-Free Object Detection.
- **链接**: [arXiv:2407.16497](https://arxiv.org/abs/2407.16497) · [代码](https://github.com/lbktrinh/DRU) · 📚 被引 13
- **作者**: Trinh Le Ba Khanh, Huy-Hung Nguyen, Long Hoang Pham, Duong Nguyen-Ngoc Tran, Jae Wook Jeon
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing open-vocabulary object detectors typically require a predefined set of categories from users, significantly confining their application scenarios. In this paper, we introduce DetCLIPv3, a high-performing detector that excels not only at both open-vocabulary object detection, but also generating hierarchical labels for detected objects. DetCLIPv3 is characterized by three core designs: 1. Versatile model architecture: we derive a robust open-set detection framework which is further empowered with generation ability via the integration of a caption head. 2. High information density data: we develop an auto-annotation pipeline leveraging visual large language model to refine captions for large-scale image-text pairs, providing rich, multi-granular object labels to enhance the training. 3. Efficient training strategy: we employ a pre-training stage with low-resolution inputs that enables the object captioner to efficiently learn a broad spectrum of visual concepts from extensive image-text paired data. This is followed by a fine-tuning stage that leverages a small number of high-resolution samples to further enhance detection performance. With these effective designs, DetCLIPv3 demonstrates superior open-vocabulary detection performance, \eg, our Swin-T backbone model achieves a notable 47.0 zero-shot fixed AP on the LVIS minival benchmark, outperforming GLIPv2, GroundingDINO, and DetCLIPv2 by 18.0/19.6/6.6 AP, respectively. DetCLIPv3 also achieves a state-of-the-art 19.7 AP in dense captioning task on VG dataset, showcasing its strong generative capability.

</details>

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> With the rapidly increasing demand for oriented object detection (OOD), recent research involving weakly-supervised detectors for learning rotated box (RBox) from the horizontal box (HBox) has attracted more and more attention. In this paper, we explore a more challenging yet label-efficient setting, namely single point-supervised OOD, and present our approach called Point2RBox. Specifically, we propose to leverage two principles: 1) Synthetic pattern knowledge combination: By sampling around each labeled point on the image, we spread the object feature to synthetic visual patterns with known boxes to provide the knowledge for box regression. 2) Transform self-supervision: With a transformed input image (e.g. scaled/rotated), the output RBoxes are trained to follow the same transformation so that the network can perceive the relative size/rotation between objects. The detector is further enhanced by a few devised techniques to cope with peripheral issues, e.g. the anchor/layer assignment as the size of the object is not available in our point supervision setting. To our best knowledge, Point2RBox is the first end-to-end solution for point-supervised OOD. In particular, our method uses a lightweight paradigm, yet it achieves a competitive performance among point-supervised alternatives, 41.05%/27.62%/80.01% on DOTA/DIOR/HRSC datasets.

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-head detectors typically employ a features-fused-pyramid-neck for multi-scale detection and are widely adopted in the industry. However, this approach faces feature misalignment when representations from different hierarchical levels of the feature pyramid are forcibly fused point-to-point. To address this issue, we designed an independent hierarchy pyramid (IHP) architecture to evaluate the effectiveness of the features-unfused-pyramid-neck for multi-head detectors. Subsequently, we introduced soft nearest neighbor interpolation (SNI) with a weight downscaling factor to mitigate the impact of feature fusion at different hierarchies while preserving key textures. Furthermore, we present a features adaptive selection method for down sampling in extended spatial windows (ESD) to retain spatial features and enhance lightweight convolutional techniques (GSConvE). These advancements culminate in our secondary features alignment solution (SA) for real-time detection, achieving state-of-the-art results on Pascal VOC and MS COCO. Code will be released at https://github.com/AlanLi1997/rethinking-fpn. This paper has been accepted by ECCV2024 and published on Springer Nature.

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The YOLO series has become the most popular framework for real-time object detection due to its reasonable trade-off between speed and accuracy. However, we observe that the speed and accuracy of YOLOs are negatively affected by the NMS. Recently, end-to-end Transformer-based detectors (DETRs) have provided an alternative to eliminating NMS. Nevertheless, the high computational cost limits their practicality and hinders them from fully exploiting the advantage of excluding NMS. In this paper, we propose the Real-Time DEtection TRansformer (RT-DETR), the first real-time end-to-end object detector to our best knowledge that addresses the above dilemma. We build RT-DETR in two steps, drawing on the advanced DETR: first we focus on maintaining accuracy while improving speed, followed by maintaining speed while improving accuracy. Specifically, we design an efficient hybrid encoder to expeditiously process multi-scale features by decoupling intra-scale interaction and cross-scale fusion to improve speed. Then, we propose the uncertainty-minimal query selection to provide high-quality initial queries to the decoder, thereby improving accuracy. In addition, RT-DETR supports flexible speed tuning by adjusting the number of decoder layers to adapt to various scenarios without retraining. Our RT-DETR-R50 / R101 achieves 53.1% / 54.3% AP on COCO and 108 / 74 FPS on T4 GPU, outperforming previously advanced YOLOs in both speed and accuracy. We also develop scaled RT-DETRs that outperform the lighter YOLO detectors (S and M models). Furthermore, RT-DETR-R50 outperforms DINO-R50 by 2.2% AP in accuracy and about 21 times in FPS. After pre-training with Objects365, RT-DETR-R50 / R101 achieves 55.3% / 56.2% AP. The project page: https://zhao-yian.github.io/RTDETR.

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In computer vision, it is well-known that a lack of data diversity will impair model performance. In this study, we address the challenges of enhancing the dataset diversity problem in order to benefit various downstream tasks such as object detection and instance segmentation. We propose a simple yet effective data augmentation approach by leveraging advancements in generative models, specifically text-to-image synthesis technologies like Stable Diffusion. Our method focuses on generating variations of labeled real images, utilizing generative object and background augmentation via inpainting to augment existing training data without the need for additional annotations. We find that background augmentation, in particular, significantly improves the models' robustness and generalization capabilities. We also investigate how to adjust the prompt and mask to ensure the generated content comply with the existing annotations. The efficacy of our augmentation techniques is validated through comprehensive evaluations of the COCO dataset and several other key object detection benchmarks, demonstrating notable enhancements in model performance across diverse scenarios. This approach offers a promising solution to the challenges of dataset enhancement, contributing to the development of more accurate and robust computer vision models.

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advancements in large vision-language models enabled visual object detection in open-vocabulary scenarios, where object classes are defined in free-text formats during inference. In this paper, we aim to probe the state-of-the-art methods for open-vocabulary object detection to determine to what extent they understand fine-grained properties of objects and their parts. To this end, we introduce an evaluation protocol based on dynamic vocabulary generation to test whether models detect, discern, and assign the correct fine-grained description to objects in the presence of hard-negative classes. We contribute with a benchmark suite of increasing difficulty and probing different properties like color, pattern, and material. We further enhance our investigation by evaluating several state-of-the-art open-vocabulary object detectors using the proposed protocol and find that most existing solutions, which shine in standard open-vocabulary benchmarks, struggle to accurately capture and distinguish finer object details. We conclude the paper by highlighting the limitations of current methodologies and exploring promising research directions to overcome the discovered drawbacks. Data and code are available at https://lorebianchi98.github.io/FG-OVD/.

</details>

### CLIFF: Continual Latent Diffusion for Open-Vocabulary Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73001-6_15)
- **作者**: Wuyang Li, Xinyu Liu, Jiayi Ma, Yixuan Yuan
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-vocabulary human-object interaction (HOI) detection, which is concerned with the problem of detecting novel HOIs guided by natural language, is crucial for understanding human-centric scenes. However, prior zero-shot HOI detectors often employ the same levels of feature maps to model HOIs with varying distances, leading to suboptimal performance in scenes containing human-object pairs with a wide range of distances. In addition, these detectors primarily rely on category names and overlook the rich contextual information that language can provide, which is essential for capturing open vocabulary concepts that are typically rare and not well-represented by category names alone. In this paper, we introduce a novel end-to-end open vocabulary HOI detection framework with conditional multi-level decoding and fine-grained semantic enhancement (CMD-SE), harnessing the potential of Visual-Language Models (VLMs). Specifically, we propose to model human-object pairs with different distances with different levels of feature maps by incorporating a soft constraint during the bipartite matching process. Furthermore, by leveraging large language models (LLMs) such as GPT models, we exploit their extensive world knowledge to generate descriptions of human body part states for various interactions. Then we integrate the generalizable and fine-grained semantics of human body parts to improve interaction recognition. Experimental results on two datasets, SWIG-HOI and HICO-DET, demonstrate that our proposed method achieves state-of-the-art results in open vocabulary HOI detection. The code and models are available at https://github.com/ltttpku/CMD-SE-release.

</details>

### Integer-Valued Training and Spike-Driven Inference Spiking Neural Network for High-Performance and Energy-Efficient Object Detection.
- **链接**: [arXiv:2407.20708](https://arxiv.org/abs/2407.20708) · [代码](https://github.com/BICLab/SpikeYOLO) · 📚 被引 63
- **作者**: Xinhao Luo, Man Yao, Yuhong Chou, Bo Xu, Guoqi Li
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, efficient Vision Transformers have shown great performance with low latency on resource-constrained devices. Conventionally, they use 4x4 patch embeddings and a 4-stage structure at the macro level, while utilizing sophisticated attention with multi-head configuration at the micro level. This paper aims to address computational redundancy at all design levels in a memory-efficient manner. We discover that using larger-stride patchify stem not only reduces memory access costs but also achieves competitive performance by leveraging token representations with reduced spatial redundancy from the early stages. Furthermore, our preliminary analyses suggest that attention layers in the early stages can be substituted with convolutions, and several attention heads in the latter stages are computationally redundant. To handle this, we introduce a single-head attention module that inherently prevents head redundancy and simultaneously boosts accuracy by parallelly combining global and local information. Building upon our solutions, we introduce SHViT, a Single-Head Vision Transformer that obtains the state-of-the-art speed-accuracy tradeoff. For example, on ImageNet-1k, our SHViT-S4 is 3.3x, 8.1x, and 2.4x faster than MobileViTv2 x1.0 on GPU, CPU, and iPhone12 mobile device, respectively, while being 1.3% more accurate. For object detection and instance segmentation on MS COCO using Mask-RCNN head, our model achieves performance comparable to FastViT-SA12 while exhibiting 3.8x and 2.0x lower backbone latency on GPU and mobile device, respectively.

</details>

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Segment Anything Model (SAM) has emerged as a powerful tool for numerous vision applications. A key component that drives the impressive performance for zero-shot transfer and high versatility is a super large Transformer model trained on the extensive high-quality SA-1B dataset. While beneficial, the huge computation cost of SAM model has limited its applications to wider real-world applications. To address this limitation, we propose EfficientSAMs, light-weight SAM models that exhibits decent performance with largely reduced complexity. Our idea is based on leveraging masked image pretraining, SAMI, which learns to reconstruct features from SAM image encoder for effective visual representation learning. Further, we take SAMI-pretrained light-weight image encoders and mask decoder to build EfficientSAMs, and finetune the models on SA-1B for segment anything task. We perform evaluations on multiple vision tasks including image classification, object detection, instance segmentation, and semantic object detection, and find that our proposed pretraining method, SAMI, consistently outperforms other masked image pretraining methods. On segment anything task such as zero-shot instance segmentation, our EfficientSAMs with SAMI-pretrained lightweight image encoders perform favorably with a significant gain (e.g., ~4 AP on COCO/LVIS) over other fast SAM models.

</details>

## 跨领域论文（完整笔记在其他领域）

- OPEN: Object-Wise Position Embedding for Multi-view 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- LISO: Lidar-Only Self-supervised 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- LiDAR-Based All-Weather 3D Object Detection via Prompting and Distilling 4D Radar. → [3d-detection](../3d-detection/Guideline%202024.md)
- Learning High-Resolution Vector Representation from Multi-camera Images for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- Diff3DETR: Agent-Based Diffusion Model for Semi-supervised 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- CMD: A Cross Mechanism Domain Adaptation Dataset for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- Find n' Propagate: Open-Vocabulary 3D Object Detection in Urban Environments. → [3d-detection](../3d-detection/Guideline%202024.md)
- Weakly Supervised 3D Object Detection via Multi-level Visual Guidance. → [3d-detection](../3d-detection/Guideline%202024.md)
- Detecting as Labeling: Rethinking LiDAR-Camera Fusion in 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- FSD-BEV: Foreground Self-distillation for Multi-view 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- Unlocking Textual and Visual Wisdom: Open-Vocabulary 3D Object Detection Enhanced by Comprehensive Guidance from Text and Image. → [3d-detection](../3d-detection/Guideline%202024.md)
- LabelDistill: Label-Guided Cross-Modal Knowledge Distillation for Camera-Based 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- Diffusion Model for Robust Multi-sensor Fusion in 3D Object Detection and BEV Segmentation. → [3d-detection](../3d-detection/Guideline%202024.md)
- Domain Generalization of 3D Object Detection by Density-Resampling. → [3d-detection](../3d-detection/Guideline%202024.md)
- MonoTTA: Fully Test-Time Adaptation for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- Ray Denoising: Depth-Aware Hard Negative Sampling for Multi-view 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- MonoWAD: Weather-Adaptive Diffusion Model for Robust Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- SAMFusion: Sensor-Adaptive Multimodal Fusion for 3D Object Detection in Adverse Weather. → [3d-detection](../3d-detection/Guideline%202024.md)
- GraphBEV: Towards Robust BEV Feature Alignment for Multi-modal 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- SimPB: A Single Model for 2D and 3D Object Detection from Multiple Cameras. → [3d-detection](../3d-detection/Guideline%202024.md)
- OV-Uni3DETR: Towards Unified Open-Vocabulary 3D Object Detection via Cycle-Modality Propagation. → [3d-detection](../3d-detection/Guideline%202024.md)
- Towards Stable 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- DSPDet3D: 3D Small Object Detection with Dynamic Spatial Pruning. → [network-pruning](../network-pruning/Guideline%202024.md)
- Reg-TTA3D: Better Regression Makes Better Test-Time Adaptive 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- General Geometry-Aware Weakly Supervised 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- Interactive 3D Object Detection with Prompts. → [3d-detection](../3d-detection/Guideline%202024.md)
- SparseLIF: High-Performance Sparse LiDAR-Camera Fusion for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- Approaching Outside: Scaling Unsupervised 3D Object Detection from 2D Scene. → [3d-detection](../3d-detection/Guideline%202024.md)
- LayoutDETR: Detection Transformer Is a Good Multimodal Layout Designer. → [multimodal](../multimodal/Guideline%202024.md)
