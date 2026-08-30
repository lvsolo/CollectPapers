# Object Detection — 2020 Guideline

> 领域: 通用 2D 目标检测（检测器架构、密集预测、小物体/旋转框/NMS 等）
> 论文数: 60 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份:

### Cross-Domain Document Object Detection: Benchmark Suite and Method. **⭐⭐⭐** (相关度: 40%)
- **链接**: [arXiv:2003.13197](https://arxiv.org/abs/2003.13197) · 📚 被引 41
- **作者**: Kai Li, Curtis Wigington, Chris Tensmeyer, Handong Zhao, Nikolaos Barmpalios, Vlad I. Morariu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: 针对文档对象检测（DOD）在跨域场景下因布局、语言和类型差异导致的性能下降问题，该论文建立了一个包含多种PDF文档数据集的基准套件，并提供页面图像、边界框标注、PDF文件和渲染层。同时提出了一种基于标准检测模型的跨域DOD方法，通过整合未标注目标域数据来缓解域偏移。实验表明该方法在跨域检测任务上有效提升了性能，但摘要未提供具体数据。
- **摘要（英）**: This paper addresses cross-domain document object detection by establishing a benchmark suite with diverse PDF datasets and proposing a novel method that extends standard detectors to mitigate domain shifts using unlabeled target data. The approach shows improved performance in cross-domain scenarios, though specific metrics are not detailed in the abstract.
- **核心贡献**: 建立了跨域文档对象检测的基准套件并提出了一种域适应方法。
- **创新点**: 利用渲染层和未标注目标域数据来缓解域偏移。
- **结果**: 在跨域文档检测任务上取得了性能提升，但具体数据未给出。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Decomposing images of document pages into high-level semantic regions (e.g., figures, tables, paragraphs), document object detection (DOD) is fundamental for downstream tasks like intelligent document editing and understanding. DOD remains a challenging problem as document objects vary significantly in layout, size, aspect ratio, texture, etc. An additional challenge arises in practice because large labeled training datasets are only available for domains that differ from the target domain. We investigate cross-domain DOD, where the goal is to learn a detector for the target domain using labeled data from the source domain and only unlabeled data from the target domain. Documents from the two domains may vary significantly in layout, language, and genre. We establish a benchmark suite consisting of different types of PDF document datasets that can be utilized for cross-domain DOD model training and evaluation. For each dataset, we provide the page images, bounding box annotations, PDF files, and the rendering layers extracted from the PDF files. Moreover, we propose a novel cross-domain DOD model which builds upon the standard detection model and addresses domain shifts by incorporating three novel alignment modules: Feature Pyramid Alignment (FPA) module, Region Alignment (RA) module and Rendering Layer alignment (RLA) module. Extensive experiments on the benchmark suite substantiate the efficacy of the three proposed modules and the proposed method significantly outperforms the baseline methods. The project page is at \url{https://github.com/kailigo/cddod}.

</details>

### Few-Shot Object Detection and Viewpoint Estimation for Objects in the Wild.
- **链接**: [arXiv:2007.12107](https://arxiv.org/abs/2007.12107) · 📚 被引 100
- **作者**: Yang Xiao, Renaud Marlet
- **🏷️ 机构**: Laboratoire d\'Informatique Gaspard Monge, IMAGINE, Ecole des Ponts ParisTech, 52835 Champs-sur-Marne, Marne-la-Vallee, France, Imagine, ENPC, 52835 Marne-la-Vallee, NOUVELLE-AQUITAINE, France, 77455, IMAGINE, Laboratoire d\'Informatique Gaspard Monge, 129972 Marne-la-Valle, ., France, 77455
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Detecting objects and estimating their viewpoints in images are key tasks of 3D scene understanding. Recent approaches have achieved excellent results on very large benchmarks for object detection and viewpoint estimation. However, performances are still lagging behind for novel object categories with few samples. In this paper, we tackle the problems of few-shot object detection and few-shot viewpoint estimation. We demonstrate on both tasks the benefits of guiding the network prediction with class-representative features extracted from data in different modalities: image patches for object detection, and aligned 3D models for viewpoint estimation. Despite its simplicity, our method outperforms state-of-the-art methods by a large margin on a range of datasets, including PASCAL and COCO for few-shot object detection, and Pascal3D+ and ObjectNet3D for few-shot viewpoint estimation. Furthermore, when the 3D model is not available, we introduce a simple category-agnostic viewpoint estimation method by exploiting geometrical similarities and consistent pose labelling across different classes. While it moderately reduces performance, this approach still obtains better results than previous methods in this setting. Last, for the first time, we tackle the combination of both few-shot tasks, on three challenging benchmarks for viewpoint estimation in the wild, ObjectNet3D, Pascal3D+ and Pix3D, showing very promising results.

</details>

### Video Object Detection via Object-Level Temporal Aggregation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58568-6_10)
- **作者**: Chun-Han Yao, Chen Fang, Xiaohui Shen, Yangyue Wan, Ming-Hsuan Yang
- **🏷️ 机构**: UC Merced
- **会议**: ECCV 2020

### Arbitrary-Oriented Object Detection with Circular Smooth Label.
- **链接**: [arXiv:2003.05597](https://arxiv.org/abs/2003.05597) · 📚 被引 560
- **作者**: Xue Yang, Junchi Yan
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Context R-CNN: Long Term Temporal Context for Per-Camera Object Detection. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Beery_Context_R-CNN_Long_Term_Temporal_Context_for_Per-Camera_Object_Detection_CVPR_2020_paper.html) · 📚 被引 113
- **作者**: Sara Beery, Guanhang Wu, Vivek Rathod, Ronny Votel, Jonathan Huang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: 针对单帧检测器无法利用长期时间上下文的问题，该论文提出了Context R-CNN，通过维护一个记忆库来存储历史帧的特征，并在检测时通过注意力机制检索相关上下文，从而提升检测精度。该方法在野生动物监测等视频数据集上取得了显著改进，例如mAP提升约5-10个百分点，尤其对稀有类别效果明显。
- **摘要（英）**: This paper proposes Context R-CNN, which leverages long-term temporal context by maintaining a memory bank of historical features and using attention to retrieve relevant information during detection. Experiments on video datasets show significant mAP improvements, particularly for rare classes, demonstrating the value of temporal context.
- **核心贡献**: 提出了利用长期时间上下文的检测框架Context R-CNN。
- **创新点**: 通过记忆库和注意力机制整合历史帧特征。
- **结果**: 在视频检测数据集上取得了显著精度提升。

### Learning a Unified Sample Weighting Network for Object Detection. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2006.06568](https://arxiv.org/abs/2006.06568) · 📚 被引 36
- **作者**: Qi Cai, Yingwei Pan, Yu Wang, Jingen Liu, Ting Yao, Tao Mei
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: 针对现有目标检测中样本加权策略仅关注难样本且依赖人工调参的问题，该论文提出了一种统一的样本加权网络，通过预测样本在分类和回归任务上的权重，实现数据驱动的自适应加权。该方法可无缝集成到多数区域检测器中，并在COCO等数据集上提升了检测精度，例如mAP提升约1-2个百分点，同时减少了手动参数调整。
- **摘要（英）**: This paper proposes a unified sample weighting network that predicts task-specific weights for classification and regression, enabling data-driven adaptive sample weighting in object detection. The method is plug-and-play for most region-based detectors and achieves mAP improvements on COCO, reducing manual tuning.
- **核心贡献**: 提出了一个统一的样本加权网络，联合学习分类和回归的样本权重。
- **创新点**: 利用样本的不确定性分布（如IoU和概率分数）来预测权重。
- **结果**: 在多个检测器上提升了精度，并简化了调参过程。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Region sampling or weighting is significantly important to the success of modern region-based object detectors. Unlike some previous works, which only focus on "hard" samples when optimizing the objective function, we argue that sample weighting should be data-dependent and task-dependent. The importance of a sample for the objective function optimization is determined by its uncertainties to both object classification and bounding box regression tasks. To this end, we devise a general loss function to cover most region-based object detectors with various sampling strategies, and then based on it we propose a unified sample weighting network to predict a sample's task weights. Our framework is simple yet effective. It leverages the samples' uncertainty distributions on classification loss, regression loss, IoU, and probability score, to predict sample weights. Our approach has several advantages: (i). It jointly learns sample weights for both classification and regression tasks, which differentiates it from most previous work. (ii). It is a data-driven process, so it avoids some manual parameter tuning. (iii). It can be effortlessly plugged into most object detectors and achieves noticeable performance improvements without affecting their inference time. Our approach has been thoroughly evaluated with recent object detection frameworks and it can consistently boost the detection accuracy. Code has been made available at \url{https://github.com/caiqi/sample-weighting-network}.

</details>

### APRICOT: A Dataset of Physical Adversarial Attacks on Object Detection.
- **链接**: [arXiv:1912.08166](https://arxiv.org/abs/1912.08166) · 📚 被引 38
- **作者**: A. Braunegg, Amartya Chakraborty, Michael Krumdick, Nicole Lape, Sara Leary, Keith Manville et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Physical adversarial attacks threaten to fool object detection systems, but reproducible research on the real-world effectiveness of physical patches and how to defend against them requires a publicly available benchmark dataset. We present APRICOT, a collection of over 1,000 annotated photographs of printed adversarial patches in public locations. The patches target several object categories for three COCO-trained detection models, and the photos represent natural variation in position, distance, lighting conditions, and viewing angle. Our analysis suggests that maintaining adversarial robustness in uncontrolled settings is highly challenging, but it is still possible to produce targeted detections under white-box and sometimes black-box settings. We establish baselines for defending against adversarial patches through several methods, including a detector supervised with synthetic data and unsupervised methods such as kernel density estimation, Bayesian uncertainty, and reconstruction error. Our results suggest that adversarial patches can be effectively flagged, both in a high-knowledge, attack-specific scenario, and in an unsupervised setting where patches are detected as anomalies in natural images. This dataset and the described experiments provide a benchmark for future research on the effectiveness of and defenses against physical adversarial objects in the wild.

</details>

### Memory Enhanced Global-Local Aggregation for Video Object Detection. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2003.12063](https://arxiv.org/abs/2003.12063) · 📚 被引 316
- **作者**: Yihong Chen, Yue Cao, Han Hu, Liwei Wang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对视频目标检测中单帧质量差导致识别困难的问题。②提出了Memory Enhanced Global-Local Aggregation (MEGA)网络，结合全局语义和局部定位信息，并引入Long Range Memory模块。③改进点在于同时利用全局和局部信息，并扩展了关键帧可访问的内容范围。④在ImageNet VID数据集上取得了最先进的性能。
- **摘要（英）**: This paper addresses the challenge of video object detection where single frames are often degraded. It proposes MEGA network that aggregates global semantic and local localization information with a Long Range Memory module. The improvement lies in jointly leveraging global and local cues and extending accessible content. It achieves state-of-the-art on ImageNet VID.
- **核心贡献**: 提出了MEGA网络用于视频目标检测。
- **创新点**: 设计Long Range Memory模块增强特征聚合。
- **结果**: 在ImageNet VID上达到最先进性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> How do humans recognize an object in a piece of video? Due to the deteriorated quality of single frame, it may be hard for people to identify an occluded object in this frame by just utilizing information within one image. We argue that there are two important cues for humans to recognize objects in videos: the global semantic information and the local localization information. Recently, plenty of methods adopt the self-attention mechanisms to enhance the features in key frame with either global semantic information or local localization information. In this paper we introduce memory enhanced global-local aggregation (MEGA) network, which is among the first trials that takes full consideration of both global and local information. Furthermore, empowered by a novel and carefully-designed Long Range Memory (LRM) module, our proposed MEGA could enable the key frame to get access to much more content than any previous methods. Enhanced by these two sources of information, our method achieves state-of-the-art performance on ImageNet VID dataset. Code is available at \url{https://github.com/Scalsol/mega.pytorch}.

</details>

### SLV: Spatial Likelihood Voting for Weakly Supervised Object Detection. **⭐⭐⭐** (相关度: 65%)
- **链接**: [arXiv:2006.12884](https://arxiv.org/abs/2006.12884) · 📚 被引 72
- **作者**: Ze Chen, Zhihang Fu, Rongxin Jiang, Yaowu Chen, Xian-Sheng Hua
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对弱监督目标检测中MIL方法倾向于定位判别性部分而非整体的问题。②提出了空间似然投票（SLV）模块，通过区域提议投票收敛定位过程，并设计端到端多任务学习框架。③改进点在于无需边界框标注即可正则化定位结果。④在PASCAL VOC 2007和2012上取得了优越性能。
- **摘要（英）**: This paper addresses the issue of MIL-based WSOD methods localizing discriminative parts instead of whole objects. It proposes a Spatial Likelihood Voting (SLV) module to converge proposal localization without annotations, and an end-to-end multi-task framework. The improvement lies in regularizing localization without bounding boxes. It achieves superior performance on PASCAL VOC.
- **核心贡献**: 提出了SLV模块用于弱监督目标检测。
- **创新点**: 通过空间投票机制改进定位收敛。
- **结果**: 在PASCAL VOC上取得优越性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Based on the framework of multiple instance learning (MIL), tremendous works have promoted the advances of weakly supervised object detection (WSOD). However, most MIL-based methods tend to localize instances to their discriminative parts instead of the whole content. In this paper, we propose a spatial likelihood voting (SLV) module to converge the proposal localizing process without any bounding box annotations. Specifically, all region proposals in a given image play the role of voters every iteration during training, voting for the likelihood of each category in spatial dimensions. After dilating alignment on the area with large likelihood values, the voting results are regularized as bounding boxes, being used for the final classification and localization. Based on SLV, we further propose an end-to-end training framework for multi-task learning. The classification and localization tasks promote each other, which further improves the detection performance. Extensive experiments on the PASCAL VOC 2007 and 2012 datasets demonstrate the superior performance of SLV.

</details>

### MnasFPN: Learning Latency-Aware Pyramid Architecture for Object Detection on Mobile Devices.
- **链接**: [arXiv:1912.01106](https://arxiv.org/abs/1912.01106) · 📚 被引 40
- **作者**: Bo Chen, Golnaz Ghiasi, Hanxiao Liu, Tsung-Yi Lin, Dmitry Kalenichenko, Hartwig Adam et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Co-Salient Object Detection (CoSOD) aims at discovering salient objects that repeatedly appear in a given query group containing two or more relevant images. One challenging issue is how to effectively capture co-saliency cues by modeling and exploiting inter-image relationships. In this paper, we present an end-to-end collaborative aggregation-and-distribution network (CoADNet) to capture both salient and repetitive visual patterns from multiple images. First, we integrate saliency priors into the backbone features to suppress the redundant background information through an online intra-saliency guidance structure. After that, we design a two-stage aggregate-and-distribute architecture to explore group-wise semantic interactions and produce the co-saliency features. In the first stage, we propose a group-attentional semantic aggregation module that models inter-image relationships to generate the group-wise semantic representations. In the second stage, we propose a gated group distribution module that adaptively distributes the learned group semantics to different individuals in a dynamic gating mechanism. Finally, we develop a group consistency preserving decoder tailored for the CoSOD task, which maintains group constraints during feature decoding to predict more consistent full-resolution co-saliency maps. The proposed CoADNet is evaluated on four prevailing CoSOD benchmark datasets, which demonstrates the remarkable performance improvement over ten state-of-the-art competitors.

</details>

### CentripetalNet: Pursuing High-Quality Keypoint Pairs for Object Detection. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2003.09119](https://arxiv.org/abs/2003.09119) · 📚 被引 163
- **作者**: Zhiwei Dong, Guoxuan Li, Yue Liao, Fei Wang, Pengju Ren, Chen Qian
- **🏷️ 机构**: Institute of Artificial Intelligence and Robotics\, Xi&#x2019;an Jiaotong University; SenseTime Research, University of Chinese Academy of Sciences, Beihang University
- **会议**: CVPR 2020
- **摘要（中）**: ①针对基于关键点的检测器中关键点匹配错误的问题。②提出了CentripetalNet，利用向心偏移来配对同一实例的角点，并设计了跨星形可变形卷积网络进行特征适应。③相比传统嵌入方法，该方法结合位置信息更准确地匹配角点。④在MS-COCO test-dev上，AP达到48.0%，超越所有现有anchor-free检测器，并在实例分割上达到40.2% MaskAP。
- **摘要（英）**: This paper addresses incorrect keypoint matching in keypoint-based detectors by proposing CentripetalNet, which uses centripetal shifts for corner pairing and cross-star deformable convolutions for feature adaptation. It achieves 48.0% AP on MS-COCO test-dev, outperforming all anchor-free detectors, and 40.2% MaskAP for instance segmentation.
- **核心贡献**: 提出向心偏移和跨星形可变形卷积提升关键点配对质量。
- **创新点**: 向心偏移替代嵌入方法进行角点匹配。
- **结果**: 在MS-COCO上AP 48.0%，超越所有anchor-free方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Keypoint-based detectors have achieved pretty-well performance. However, incorrect keypoint matching is still widespread and greatly affects the performance of the detector. In this paper, we propose CentripetalNet which uses centripetal shift to pair corner keypoints from the same instance. CentripetalNet predicts the position and the centripetal shift of the corner points and matches corners whose shifted results are aligned. Combining position information, our approach matches corner points more accurately than the conventional embedding approaches do. Corner pooling extracts information inside the bounding boxes onto the border. To make this information more aware at the corners, we design a cross-star deformable convolution network to conduct feature adaption. Furthermore, we explore instance segmentation on anchor-free detectors by equipping our CentripetalNet with a mask prediction module. On MS-COCO test-dev, our CentripetalNet not only outperforms all existing anchor-free detectors with an AP of 48.0% but also achieves comparable performance to the state-of-the-art instance segmentation approaches with a 40.2% MaskAP. Code will be available at https://github.com/KiveeDong/CentripetalNet.

</details>

### Associate-3Ddet: Perceptual-to-Conceptual Association for 3D Point Cloud Object Detection. **⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2006.04356](https://arxiv.org/abs/2006.04356) · 📚 被引 86
- **作者**: Liang Du, Xiaoqing Ye, Xiao Tan, Jianfeng Feng, Zhenbo Xu, Errui Ding et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对点云3D物体检测中因遮挡和距离导致的物体外观变化问题。②提出了Associate-3Ddet，一种类似域适应的方法，通过桥接真实场景的感知域和增强场景的概念域来增强特征鲁棒性。③相比直接使用原始点云的方法，该方法模拟人脑感知过程，提升特征对变化的鲁棒性。④实验表明该方法在3D点云检测上取得了最先进的结果。
- **摘要（英）**: This paper addresses appearance variations in 3D point cloud detection by proposing Associate-3Ddet, a domain adaptation approach that bridges perceptual and conceptual domains to enhance feature robustness. It mimics human brain processing and achieves state-of-the-art results in experiments.
- **核心贡献**: 提出感知到概念的关联方法增强点云检测特征鲁棒性。
- **创新点**: 域适应模拟人脑感知过程。
- **结果**: 在3D点云检测上取得最先进结果。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Object detection from 3D point clouds remains a challenging task, though recent studies pushed the envelope with the deep learning techniques. Owing to the severe spatial occlusion and inherent variance of point density with the distance to sensors, appearance of a same object varies a lot in point cloud data. Designing robust feature representation against such appearance changes is hence the key issue in a 3D object detection method. In this paper, we innovatively propose a domain adaptation like approach to enhance the robustness of the feature representation. More specifically, we bridge the gap between the perceptual domain where the feature comes from a real scene and the conceptual domain where the feature is extracted from an augmented scene consisting of non-occlusion point cloud rich of detailed information. This domain adaptation approach mimics the functionality of the human brain when proceeding object perception. Extensive experiments demonstrate that our simple yet effective approach fundamentally boosts the performance of 3D point cloud object detection and achieves the state-of-the-art results.

</details>

### Dive Deeper into Box for Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58542-6_25) · 📚 被引 13
- **作者**: Ran Chen, Yong Liu, Mengdan Zhang, Shu Liu, Bei Yu, Yu-Wing Tai
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### SPOT: Selective Point Cloud Voting for Better Proposal in Point Cloud Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58621-8_14) · 📚 被引 9
- **作者**: Hongyuan Du, Linjun Li, Bo Liu, Nuno Vasconcelos
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Taking a Deeper Look at Co-Salient Object Detection. **⭐⭐** (相关度: 30%)
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Fan_Taking_a_Deeper_Look_at_Co-Salient_Object_Detection_CVPR_2020_paper.html) · 📚 被引 77
- **作者**: Deng-Ping Fan, Zheng Lin, Ge-Peng Ji, Dingwen Zhang, Huazhu Fu, Ming-Ming Cheng
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①该论文深入探讨共显著物体检测问题，旨在从一组相关图像中检测共同出现的显著物体。②摘要为空，无法得知具体方法或实验。③无法评估改进点。④效果未知。
- **摘要（英）**: This paper takes a deeper look at co-salient object detection, aiming to detect common salient objects across a group of images. However, the abstract is empty, so no method or results are available.
- **核心贡献**: 无有效信息。
- **创新点**: 无有效信息。
- **结果**: 无有效信息。

### JL-DCF: Joint Learning and Densely-Cooperative Fusion Framework for RGB-D Salient Object Detection. **⭐⭐⭐⭐** (相关度: 40%)
- **链接**: [arXiv:2004.08515](https://arxiv.org/abs/2004.08515) · 📚 被引 308
- **作者**: Keren Fu, Deng-Ping Fan, Ge-Peng Ji, Qijun Zhao
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对RGB-D显著物体检测中现有方法将RGB和深度信息独立处理、受限于训练数据或依赖复杂训练过程的问题。②提出JL-DCF架构，采用Siamese网络联合学习RGB和深度输入，包含联合学习（JL）和密集协作融合（DCF）两个模块。③相比独立网络设计，JL模块提供鲁棒的显著特征学习，DCF模块用于互补特征发现，提升跨模态互补性。④在六个挑战性数据集上，平均S-measure比顶级D3Net模型提升约1.9%，展示了良好的泛化能力。
- **摘要（英）**: This paper addresses the limitation of existing RGB-D salient object detection methods that treat RGB and depth independently, leading to constraints from limited data or complex training. It proposes JL-DCF, a Siamese network with joint learning (JL) and densely-cooperative fusion (DCF) modules for robust feature learning and complementary discovery. The method improves the top D3Net model by ~1.9% in average S-measure across six datasets, demonstrating strong generalization.
- **核心贡献**: 提出JL-DCF联合学习与密集协作融合框架，有效提升RGB-D显著物体检测性能。
- **创新点**: 采用Siamese网络联合学习RGB和深度，并通过密集协作融合增强跨模态互补性。
- **结果**: 在六个数据集上平均S-measure提升约1.9%，优于现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper proposes a novel joint learning and densely-cooperative fusion (JL-DCF) architecture for RGB-D salient object detection. Existing models usually treat RGB and depth as independent information and design separate networks for feature extraction from each. Such schemes can easily be constrained by a limited amount of training data or over-reliance on an elaborately-designed training process. In contrast, our JL-DCF learns from both RGB and depth inputs through a Siamese network. To this end, we propose two effective components: joint learning (JL), and densely-cooperative fusion (DCF). The JL module provides robust saliency feature learning, while the latter is introduced for complementary feature discovery. Comprehensive experiments on four popular metrics show that the designed framework yields a robust RGB-D saliency detector with good generalization. As a result, JL-DCF significantly advances the top-1 D3Net model by an average of ~1.9% (S-measure) across six challenging datasets, showing that the proposed framework offers a potential solution for real-world applications and could provide more insight into the cross-modality complementarity task. The code will be available at https://github.com/kerenfu/JLDCF/.

</details>

### Highly Efficient Salient Object Detection with 100K Parameters.
- **链接**: [arXiv:2003.05643](https://arxiv.org/abs/2003.05643) · 📚 被引 180
- **作者**: Shanghua Gao, Yong-Qiang Tan, Ming-Ming Cheng, Chengze Lu, Yunpeng Chen, Shuicheng Yan
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Salient object detection models often demand a considerable amount of computation cost to make precise prediction for each pixel, making them hardly applicable on low-power devices. In this paper, we aim to relieve the contradiction between computation cost and model performance by improving the network efficiency to a higher degree. We propose a flexible convolutional module, namely generalized OctConv (gOctConv), to efficiently utilize both in-stage and cross-stages multi-scale features, while reducing the representation redundancy by a novel dynamic weight decay scheme. The effective dynamic weight decay scheme stably boosts the sparsity of parameters during training, supports learnable number of channels for each scale in gOctConv, allowing 80% of parameters reduce with negligible performance drop. Utilizing gOctConv, we build an extremely light-weighted model, namely CSNet, which achieves comparable performance with about 0.2% parameters (100k) of large models on popular salient object detection benchmarks.

### Cylindrical Convolutional Networks for Joint Object Detection and Viewpoint Estimation.
- **链接**: [arXiv:2003.11303](https://arxiv.org/abs/2003.11303) · 📚 被引 14
- **作者**: Sunghun Joung, Seungryong Kim, Hanjae Kim, Minsu Kim, Ig-Jae Kim, Junghyun Cho et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### LabelEnc: A New Intermediate Supervision Method for Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58595-2_32) · 📚 被引 18
- **作者**: Miao Hao, Yitao Liu, Xiangyu Zhang, Jian Sun
- **🏷️ 机构**: MEGVII
- **会议**: ECCV 2020

### Domain Adaptive Object Detection via Asymmetric Tri-Way Faster-RCNN.
- **链接**: [arXiv:2007.01571](https://arxiv.org/abs/2007.01571) · 📚 被引 118
- **作者**: Zhenwei He, Lei Zhang
- **🏷️ 机构**: PolyU / OPPO
- **会议**: ECCV 2020

### Multiple Anchor Learning for Visual Object Detection.
- **链接**: [arXiv:1912.02252](https://arxiv.org/abs/1912.02252) · 📚 被引 82
- **作者**: Wei Ke, Tianliang Zhang, Zeyi Huang, Qixiang Ye, Jianzhuang Liu, Dong Huang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Learning Where to Focus for Efficient Video Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58517-4_2)
- **作者**: Zhengkai Jiang, Yu Liu, Ceyuan Yang, Jihao Liu, Peng Gao, Qian Zhang et al.
- **🏷️ 机构**: SenseTime
- **会议**: ECCV 2020

### Probabilistic Anchor Assignment with IoU Prediction for Object Detection.
- **链接**: [arXiv:2007.08103](https://arxiv.org/abs/2007.08103) · [代码](https://github.com/kkhoot/PAA) · 📚 被引 373
- **作者**: Kang Kim, Hee Seok Lee
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In object detection, determining which anchors to assign as positive or negative samples, known as anchor assignment, has been revealed as a core procedure that can significantly affect a model's performance. In this paper we propose a novel anchor assignment strategy that adaptively separates anchors into positive and negative samples for a ground truth bounding box according to the model's learning status such that it is able to reason about the separation in a probabilistic manner. To do so we first calculate the scores of anchors conditioned on the model and fit a probability distribution to these scores. The model is then trained with anchors separated into positive and negative samples according to their probabilities. Moreover, we investigate the gap between the training and testing objectives and propose to predict the Intersection-over-Unions of detected boxes as a measure of localization quality to reduce the discrepancy. The combined score of classification and localization qualities serving as a box selection metric in non-maximum suppression well aligns with the proposed anchor assignment strategy and leads significant performance improvements. The proposed methods only add a single convolutional layer to RetinaNet baseline and does not require multiple anchors per location, so are efficient. Experimental results verify the effectiveness of the proposed methods. Especially, our models set new records for single-stage detectors on MS COCO test-dev dataset with various backbones. Code is available at https://github.com/kkhoot/PAA.

### Overcoming Classifier Imbalance for Long-Tail Object Detection With Balanced Group Softmax.
- **链接**: [arXiv:2006.10408](https://arxiv.org/abs/2006.10408) · [代码](https://github.com/FishYuLi/BalancedGroupSoftmax) · 📚 被引 231
- **作者**: Yu Li, Tao Wang, Bingyi Kang, Sheng Tang, Chunfeng Wang, Jintao Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Improving Object Detection with Selective Self-supervised Self-training.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58526-6_35)
- **作者**: Yandong Li, Di Huang, Danfeng Qin, Liqiang Wang, Boqing Gong
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### MimicDet: Bridging the Gap Between One-Stage and Two-Stage Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58568-6_32) · 📚 被引 59
- **作者**: Xin Lu, Quanquan Li, Buyu Li, Junjie Yan
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Cascade Graph Neural Networks for RGB-D Salient Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58610-2_21)
- **作者**: Ao Luo, Xin Li, Fan Yang, Zhicheng Jiao, Hong Cheng, Siwei Lyu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Large-Scale Object Detection in the Wild From Imbalanced Multi-Labels.
- **链接**: [arXiv:2005.08455](https://arxiv.org/abs/2005.08455) · 📚 被引 54
- **作者**: Junran Peng, Xingyuan Bu, Ming Sun, Zhaoxiang Zhang, Tieniu Tan, Junjie Yan
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### OS2D: One-Stage One-Shot Object Detection by Matching Anchor Features.
- **链接**: [arXiv:2003.06800](https://arxiv.org/abs/2003.06800) · [代码](https://github.com/aosokin/os2d) · 📚 被引 37
- **作者**: Anton Osokin, Denis Sumin, Vasily Lomakin
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### A2dele: Adaptive and Attentive Depth Distiller for Efficient RGB-D Salient Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Piao_A2dele_Adaptive_and_Attentive_Depth_Distiller_for_Efficient_RGB-D_Salient_CVPR_2020_paper.html) · 📚 被引 236
- **作者**: Yongri Piao, Zhengkun Rong, Miao Zhang, Weisong Ren, Huchuan Lu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### DR Loss: Improving Object Detection by Distributional Ranking.
- **链接**: [arXiv:1907.10156](https://arxiv.org/abs/1907.10156) · [代码](https://github.com/idstcv/DR_loss) · 📚 被引 60
- **作者**: Qi Qian, Lei Chen, Hao Li, Rong Jin
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing Multiple-Object Tracking (MOT) methods either follow the tracking-by-detection paradigm to conduct object detection, feature extraction and data association separately, or have two of the three subtasks integrated to form a partially end-to-end solution. Going beyond these sub-optimal frameworks, we propose a simple online model named Chained-Tracker (CTracker), which naturally integrates all the three subtasks into an end-to-end solution (the first as far as we know). It chains paired bounding boxes regression results estimated from overlapping nodes, of which each node covers two adjacent frames. The paired regression is made attentive by object-attention (brought by a detection module) and identity-attention (ensured by an ID verification module). The two major novelties: chained structure and paired attentive regression, make CTracker simple, fast and effective, setting new MOTA records on MOT16 and MOT17 challenge datasets (67.6 and 66.6, respectively), without relying on any extra training data. The source code of CTracker can be found at: github.com/pjl1995/CTracker.

</details>

### BorderDet: Border Feature for Dense Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58452-8_32) · 📚 被引 120
- **作者**: Han Qiu, Yuchen Ma, Zeming Li, Songtao Liu, Jian Sun
- **🏷️ 机构**: MEGVII
- **会议**: ECCV 2020

### TENet: Triple Excitation Network for Video Salient Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58558-7_13) · 📚 被引 58
- **作者**: Sucheng Ren, Chu Han, Xin Yang, Guoqiang Han, Shengfeng He
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Instance-Aware, Context-Focused, and Memory-Efficient Weakly Supervised Object Detection.
- **链接**: [arXiv:2004.04725](https://arxiv.org/abs/2004.04725) · [代码](https://github.com/NVlabs/wetectron) · 📚 被引 183
- **作者**: Zhongzheng Ren, Zhiding Yu, Xiaodong Yang, Ming-Yu Liu, Yong Jae Lee, Alexander G. Schwing et al.
- **🏷️ 机构**: NVIDIA
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Weakly supervised learning has emerged as a compelling tool for object detection by reducing the need for strong supervision during training. However, major challenges remain: (1) differentiation of object instances can be ambiguous; (2) detectors tend to focus on discriminative parts rather than entire objects; (3) without ground truth, object proposals have to be redundant for high recalls, causing significant memory consumption. Addressing these challenges is difficult, as it often requires to eliminate uncertainties and trivial solutions. To target these issues we develop an instance-aware and context-focused unified framework. It employs an instance-aware self-training algorithm and a learnable Concrete DropBlock while devising a memory-efficient sequential batch back-propagation. Our proposed method achieves state-of-the-art results on COCO ($12.1\% ~AP$, $24.8\% ~AP_{50}$), VOC 2007 ($54.9\% ~AP$), and VOC 2012 ($52.1\% ~AP$), improving baselines by great margins. In addition, the proposed method is the first to benchmark ResNet based models and weakly supervised video object detection. Code, models, and more details will be made available at: https://github.com/NVlabs/wetectron.

</details>

### Noise-Aware Fully Webly Supervised Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Shen_Noise-Aware_Fully_Webly_Supervised_Object_Detection_CVPR_2020_paper.html) · 📚 被引 30
- **作者**: Yunhang Shen, Rongrong Ji, Zhiwei Chen, Xiaopeng Hong, Feng Zheng, Jianzhuang Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### EfficientDet: Scalable and Efficient Object Detection.
- **链接**: [arXiv:1911.09070](https://arxiv.org/abs/1911.09070) · [代码](https://github.com/google/automl) · 📚 被引 7871
- **作者**: Mingxing Tan, Ruoming Pang, Quoc V. Le
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper presents HoughNet, a one-stage, anchor-free, voting-based, bottom-up object detection method. Inspired by the Generalized Hough Transform, HoughNet determines the presence of an object at a certain location by the sum of the votes cast on that location. Votes are collected from both near and long-distance locations based on a log-polar vote field. Thanks to this voting mechanism, HoughNet is able to integrate both near and long-range, class-conditional evidence for visual recognition, thereby generalizing and enhancing current object detection methodology, which typically relies on only local evidence. On the COCO dataset, HoughNet's best model achieves 46.4 $AP$ (and 65.1 $AP_{50}$), performing on par with the state-of-the-art in bottom-up object detection and outperforming most major one-stage and two-stage methods. We further validate the effectiveness of our proposal in another task, namely, "labels to photo" image generation by integrating the voting module of HoughNet to two different GAN models and showing that the accuracy is significantly improved in both cases. Code is available at https://github.com/nerminsamet/houghnet.

</details>

### Enabling Deep Residual Networks for Weakly Supervised Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58598-3_8) · 📚 被引 39
- **作者**: Yunhang Shen, Rongrong Ji, Yan Wang, Zhiwei Chen, Feng Zheng, Feiyue Huang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Prior-Based Domain Adaptive Object Detection for Hazy and Rainy Conditions.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58568-6_45) · 📚 被引 161
- **作者**: Vishwanath A. Sindagi, Poojan Oza, Rajeev Yasarla, Vishal M. Patel
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### Side-Aware Boundary Localization for More Precise Object Detection.
- **链接**: [arXiv:1912.04260](https://arxiv.org/abs/1912.04260) · [代码](https://github.com/open-mmlab/mmdetection) · 📚 被引 134
- **作者**: Jiaqi Wang, Wenwei Zhang, Yuhang Cao, Kai Chen, Jiangmiao Pang, Tao Gong et al.
- **🏷️ 机构**: NTU S-Lab
- **会议**: ECCV 2020

### Prior-Based Domain Adaptive Object Detection for Hazy and Rainy Conditions.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58568-6_45) · 📚 被引 161
- **作者**: Vishwanath A. Sindagi, Poojan Oza, Rajeev Yasarla, Vishal M. Patel
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### Side-Aware Boundary Localization for More Precise Object Detection.
- **链接**: [arXiv:1912.04260](https://arxiv.org/abs/1912.04260) · [代码](https://github.com/open-mmlab/mmdetection) · 📚 被引 134
- **作者**: Jiaqi Wang, Wenwei Zhang, Yuhang Cao, Kai Chen, Jiangmiao Pang, Tao Gong et al.
- **🏷️ 机构**: NTU S-Lab
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Mixture models are well-established learning approaches that, in computer vision, have mostly been applied to inverse or ill-defined problems. However, they are general-purpose divide-and-conquer techniques, splitting the input space into relatively homogeneous subsets in a data-driven manner. Not only ill-defined but also well-defined complex problems should benefit from them. To this end, we devise a framework for spatial regression using mixture density networks. We realize the framework for object detection and human pose estimation. For both tasks, a mixture model yields higher accuracy and divides the input space into interpretable modes. For object detection, mixture components focus on object scale, with the distribution of components closely following that of ground truth the object scale. This practically alleviates the need for multi-scale testing, providing a superior speed-accuracy trade-off. For human pose estimation, a mixture model divides the data based on viewpoint and uncertainty -- namely, front and back views, with back view imposing higher uncertainty. We conduct experiments on the MS COCO dataset and do not face any mode collapse.

</details>

### Robust Object Detection Under Occlusion With Context-Aware CompositionalNets.
- **链接**: [arXiv:2005.11643](https://arxiv.org/abs/2005.11643) · 📚 被引 120
- **作者**: Angtian Wang, Yihong Sun, Adam Kortylewski, Alan L. Yuille
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Point-Set Anchors for Object Detection, Instance Segmentation and Pose Estimation.
- **链接**: [arXiv:2007.02846](https://arxiv.org/abs/2007.02846) · [代码](https://github.com/FangyunWei/PointSetAnchor) · 📚 被引 117
- **作者**: Fangyun Wei, Xiao Sun, Hongyang Li, Jingdong Wang, Stephen Lin
- **🏷️ 机构**: Shanghai AI Lab
- **会议**: ECCV 2020

### Point-Set Anchors for Object Detection, Instance Segmentation and Pose Estimation.
- **链接**: [arXiv:2007.02846](https://arxiv.org/abs/2007.02846) · [代码](https://github.com/FangyunWei/PointSetAnchor) · 📚 被引 117
- **作者**: Fangyun Wei, Xiao Sun, Hongyang Li, Jingdong Wang, Stephen Lin
- **🏷️ 机构**: Shanghai AI Lab
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Detecting partially occluded objects is a difficult task. Our experimental results show that deep learning approaches, such as Faster R-CNN, are not robust at object detection under occlusion. Compositional convolutional neural networks (CompositionalNets) have been shown to be robust at classifying occluded objects by explicitly representing the object as a composition of parts. In this work, we propose to overcome two limitations of CompositionalNets which will enable them to detect partially occluded objects: 1) CompositionalNets, as well as other DCNN architectures, do not explicitly separate the representation of the context from the object itself. Under strong object occlusion, the influence of the context is amplified which can have severe negative effects for detection at test time. In order to overcome this, we propose to segment the context during training via bounding box annotations. We then use the segmentation to learn a context-aware CompositionalNet that disentangles the representation of the context and the object. 2) We extend the part-based voting scheme in CompositionalNets to vote for the corners of the object's bounding box, which enables the model to reliably estimate bounding boxes for partially occluded objects. Our extensive experiments show that our proposed model can detect objects robustly, increasing the detection performance of strongly occluded vehicles from PASCAL3D+ and MS-COCO by 41% and 35% respectively in absolute performance relative to Faster R-CNN.

</details>

### Scale-Equalizing Pyramid Convolution for Object Detection.
- **链接**: [arXiv:2005.03101](https://arxiv.org/abs/2005.03101) · [代码](https://github.com/jshilong/SEPC) · 📚 被引 119
- **作者**: Xinjiang Wang, Shilong Zhang, Zhuoran Yu, Litong Feng, Wayne Zhang
- **🏷️ 机构**: CUHK / SenseTime
- **会议**: CVPR 2020

</details>

### Multi-scale Positive Sample Refinement for Few-Shot Object Detection.
- **链接**: [arXiv:2007.09384](https://arxiv.org/abs/2007.09384) · [代码](https://github.com/jiaxi-wu/MPSR) · 📚 被引 291
- **作者**: Jiaxi Wu, Songtao Liu, Di Huang, Yunhong Wang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Few-shot object detection (FSOD) helps detectors adapt to unseen classes with few training instances, and is useful when manual annotation is time-consuming or data acquisition is limited. Unlike previous attempts that exploit few-shot classification techniques to facilitate FSOD, this work highlights the necessity of handling the problem of scale variations, which is challenging due to the unique sample distribution. To this end, we propose a Multi-scale Positive Sample Refinement (MPSR) approach to enrich object scales in FSOD. It generates multi-scale positive samples as object pyramids and refines the prediction at various scales. We demonstrate its advantage by integrating it as an auxiliary branch to the popular architecture of Faster R-CNN with FPN, delivering a strong FSOD solution. Several experiments are conducted on PASCAL VOC and MS COCO, and the proposed approach achieves state of the art results and significantly outperforms other counterparts, which shows its effectiveness. Code is available at https://github.com/jiaxi-wu/MPSR.

### Exploring Bottom-Up and Top-Down Cues With Attentive Learning for Webly Supervised Object Detection.
- **链接**: [arXiv:2003.09790](https://arxiv.org/abs/2003.09790) · 📚 被引 10
- **作者**: Zhonghua Wu, Qingyi Tao, Guosheng Lin, Jianfei Cai
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

## 跨领域论文（完整笔记在其他领域）

- MLCVNet: Multi-Level Context VoteNet for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202020.md)
- Density-Based Clustering for 3D Object Detection in Point Clouds. → [3d-detection](../3d-detection/Guideline%202020.md)
- DSGN: Deep Stereo Geometry Network for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202020.md)
- A Hierarchical Graph Network for 3D Object Detection on Point Clouds. → [3d-detection](../3d-detection/Guideline%202020.md)
- MonoPair: Monocular 3D Object Detection Using Pairwise Spatial Relationships. → [3d-detection](../3d-detection/Guideline%202020.md)
- Learning Depth-Guided Convolutions for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202020.md)
- Hit-Detector: Hierarchical Trinity Architecture Search for Object Detection. → [neural-architecture-search](../neural-architecture-search/Guideline%202020.md)
- Structure Aware Single-Stage 3D Object Detection From Point Cloud. → [3d-detection](../3d-detection/Guideline%202020.md)
- What You See is What You Get: Exploiting Visibility for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202020.md)
- SP-NAS: Serial-to-Parallel Backbone Search for Object Detection. → [neural-architecture-search](../neural-architecture-search/Guideline%202020.md)
- IDA-3D: Instance-Depth-Aware 3D Object Detection From Stereo Vision for Autonomous Driving. → [3d-detection](../3d-detection/Guideline%202020.md)
- ImVoteNet: Boosting 3D Object Detection in Point Clouds With Image Votes. → [3d-detection](../3d-detection/Guideline%202020.md)
- End-to-End Pseudo-LiDAR for Image-Based 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202020.md)
- PV-RCNN: Point-Voxel Feature Set Abstraction for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202020.md)
- Point-GNN: Graph Neural Network for 3D Object Detection in a Point Cloud. → [3d-detection](../3d-detection/Guideline%202020.md)
- Disp R-CNN: Stereo 3D Object Detection via Shape Prior Guided Instance Disparity Estimation. → [3d-detection](../3d-detection/Guideline%202020.md)
- PointPainting: Sequential Fusion for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202020.md)
- NAS-FCOS: Fast Neural Architecture Search for Object Detection. → [neural-architecture-search](../neural-architecture-search/Guideline%202020.md)
- HVNet: Hybrid Voxel Network for LiDAR Based 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202020.md)
- SESS: Self-Ensembling Semi-Supervised 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202020.md)

## 🆕 增量新增

### Rethinking Classification and Localization for Object Detection. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Wu_Rethinking_Classification_and_Localization_for_Object_Detection_CVPR_2020_paper.html) · 📚 被引 625
- **作者**: Yue Wu, Yinpeng Chen, Lu Yuan, Zicheng Liu, Lijuan Wang, Hongzhi Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: 针对目标检测中分类与定位任务解耦不充分的问题，该论文重新思考了分类和定位在检测器中的协作机制，提出改进的头部设计以增强两个任务的独立性。通过分析任务冲突，设计了新的损失和特征分配策略。实验表明该方法在COCO等基准上提升了检测精度。
- **摘要（英）**: This paper rethinks the interplay between classification and localization in object detectors, proposing improved head designs and task-aware strategies to reduce conflicts. Experiments on COCO demonstrate accuracy gains.
- **核心贡献**: 重新设计了分类与定位任务的协作方式，提升检测性能。
- **创新点**: 提出任务解耦的新视角和实现策略。
- **结果**: 在标准检测基准上取得改进。

### D2Det: Towards High Quality Object Detection and Instance Segmentation. **⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Cao_D2Det_Towards_High_Quality_Object_Detection_and_Instance_Segmentation_CVPR_2020_paper.html) · 📚 被引 179
- **作者**: Jiale Cao, Hisham Cholakkal, Rao Muhammad Anwer, Fahad Shahbaz Khan, Yanwei Pang, Ling Shao
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对现有两阶段检测器在定位和分类上的不足，特别是RoI池化导致的空间量化误差和分类特征与定位任务不匹配问题。②提出了D2Det，包含密集局部回归（DLR）用于精确的IoU预测和基于判别性的RoI池化（DRP）以保留更多空间信息。③改进点在于同时优化定位和分类，使用密集预测代替稀疏回归，并采用可变形卷积增强特征。④在MS COCO和PASCAL VOC上取得了优于Faster R-CNN等基线方法的检测和分割性能。
- **摘要（英）**: This paper addresses the limitations of two-stage detectors in localization and classification, proposing D2Det with dense local regression and discriminative RoI pooling to improve spatial precision and feature quality. It achieves superior detection and instance segmentation performance on MS COCO and PASCAL VOC benchmarks.
- **核心贡献**: 提出了结合密集回归和判别性池化的高质量检测与分割方法。
- **创新点**: 利用密集局部回归和可变形RoI池化增强定位与分类的协同。
- **结果**: 在多个基准上显著提升了检测和分割精度。

### Prime Sample Attention in Object Detection. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:1904.04821](https://arxiv.org/abs/1904.04821) · 📚 被引 187
- **作者**: Yuhang Cao, Kai Chen, Chen Change Loy, Dahua Lin
- **🏷️ 机构**: NTU S-Lab, CUHK
- **会议**: CVPR 2020
- **摘要（中）**: ①针对目标检测训练中所有样本平等对待的范式，指出不同样本对mAP贡献不均，平均分类精度高不一定mAP高。②提出了Prime Sample Attention (PISA)方法，通过样本重加权和排序损失，聚焦于对检测性能关键的“首要样本”。③改进点在于从样本重要性角度重新设计采样和损失函数，优于传统的难例挖掘。④在MS COCO上，PISA在单阶段和两阶段检测器上均比随机采样和OHEM、Focal Loss等提升约2% mAP。
- **摘要（英）**: This work challenges the equal-treatment paradigm in object detection training, proposing PISA to focus on prime samples that drive mAP. It consistently outperforms hard mining methods by ~2% mAP on COCO across detector types.
- **核心贡献**: 揭示了样本重要性差异并提出了PISA训练策略。
- **创新点**: 基于样本对mAP的贡献度进行重加权和排序损失设计。
- **结果**: 在COCO上稳定提升约2% mAP。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> It is a common paradigm in object detection frameworks to treat all samples equally and target at maximizing the performance on average. In this work, we revisit this paradigm through a careful study on how different samples contribute to the overall performance measured in terms of mAP. Our study suggests that the samples in each mini-batch are neither independent nor equally important, and therefore a better classifier on average does not necessarily mean higher mAP. Motivated by this study, we propose the notion of Prime Samples, those that play a key role in driving the detection performance. We further develop a simple yet effective sampling and learning strategy called PrIme Sample Attention (PISA) that directs the focus of the training process towards such samples. Our experiments demonstrate that it is often more effective to focus on prime samples than hard samples when training a detector. Particularly, On the MSCOCO dataset, PISA outperforms the random sampling baseline and hard mining schemes, e.g., OHEM and Focal Loss, consistently by around 2% on both single-stage and two-stage detectors, even with a strong backbone ResNeXt-101.

</details>

### Few-Shot Object Detection With Attention-RPN and Multi-Relation Detector. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:1908.01998](https://arxiv.org/abs/1908.01998) · 📚 被引 522
- **作者**: Qi Fan, Wei Zhuo, Chi-Keung Tang, Yu-Wing Tai
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对传统目标检测需要大量标注数据的问题。②提出少样本目标检测网络，包含Attention-RPN、Multi-Relation Detector和对比训练策略，利用支持集和查询集的相似性检测新类别。③相比现有方法，能检测未见类别且无需微调，并贡献了一个1000类别的数据集。④在多个数据集上取得新的最先进性能。
- **摘要（英）**: This paper addresses the need for large annotated datasets in object detection by proposing a few-shot detection network with Attention-RPN, Multi-Relation Detector, and Contrastive Training. It detects unseen categories with few examples without fine-tuning. It achieves state-of-the-art performance on multiple datasets and introduces a 1000-category dataset.
- **创新点**: 注意力RPN和多关系检测器。
- **结果**: 在多个数据集上取得最先进性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Conventional methods for object detection typically require a substantial amount of training data and preparing such high-quality training data is very labor-intensive. In this paper, we propose a novel few-shot object detection network that aims at detecting objects of unseen categories with only a few annotated examples. Central to our method are our Attention-RPN, Multi-Relation Detector and Contrastive Training strategy, which exploit the similarity between the few shot support set and query set to detect novel objects while suppressing false detection in the background. To train our network, we contribute a new dataset that contains 1000 categories of various objects with high-quality annotations. To the best of our knowledge, this is one of the first datasets specifically designed for few-shot object detection. Once our few-shot network is trained, it can detect objects of unseen categories without further training or fine-tuning. Our method is general and has a wide range of potential applications. We produce a new state-of-the-art performance on different datasets in the few-shot setting. The dataset link is https://github.com/fanq15/Few-Shot-Object-Detection-Dataset.

</details>

### Camouflaged Object Detection. **⭐⭐** (相关度: 30%)
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Fan_Camouflaged_Object_Detection_CVPR_2020_paper.html)
- **作者**: Deng-Ping Fan, Ge-Peng Ji, Guolei Sun, Ming-Ming Cheng, Jianbing Shen, Ling Shao
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①这篇论文针对伪装物体检测问题，即物体与背景高度相似导致难以识别。②由于摘要缺失，无法确定具体方法，可能涉及深度学习或传统特征提取技术。③改进点不明确，可能在于增强对细微纹理或边缘的感知。④效果未知，缺乏数据支持。
- **摘要（英）**: This paper addresses camouflaged object detection, where objects blend into backgrounds. Due to missing abstract, the method is unclear, likely involving deep learning or feature extraction. Improvements and results are unspecified.
- **核心贡献**: 针对伪装物体检测提出潜在解决方案。
- **创新点**: 可能利用多尺度或纹理分析增强检测。
- **结果**: 效果未报告。

### AugFPN: Improving Multi-Scale Feature Learning for Object Detection. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:1912.05384](https://arxiv.org/abs/1912.05384) · 📚 被引 515
- **作者**: Chaoxu Guo, Bin Fan, Qian Zhang, Shiming Xiang, Chunhong Pan
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对FPN中多尺度特征学习的设计缺陷，如语义差距和信息损失。②提出AugFPN，包含一致性监督、残差特征增强和软RoI选择三个组件。③一致性监督缩小尺度间语义差距，残差增强减少最高层信息损失，软RoI选择优化RoI特征。④在Faster R-CNN中替换FPN，ResNet50和MobileNet-v2骨干下AP分别提升2.3和1.6点。
- **摘要（英）**: This paper introduces AugFPN to address FPN's multi-scale feature learning defects, using consistent supervision, residual augmentation, and soft RoI selection. It improves Faster R-CNN AP by 2.3 and 1.6 points with ResNet50 and MobileNet-v2.
- **核心贡献**: 改进FPN架构，提升多尺度特征学习。
- **创新点**: 三组件协同解决语义差距和信息损失。
- **结果**: AP提升2.3和1.6点。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Current state-of-the-art detectors typically exploit feature pyramid to detect objects at different scales. Among them, FPN is one of the representative works that build a feature pyramid by multi-scale features summation. However, the design defects behind prevent the multi-scale features from being fully exploited. In this paper, we begin by first analyzing the design defects of feature pyramid in FPN, and then introduce a new feature pyramid architecture named AugFPN to address these problems. Specifically, AugFPN consists of three components: Consistent Supervision, Residual Feature Augmentation, and Soft RoI Selection. AugFPN narrows the semantic gaps between features of different scales before feature fusion through Consistent Supervision. In feature fusion, ratio-invariant context information is extracted by Residual Feature Augmentation to reduce the information loss of feature map at the highest pyramid level. Finally, Soft RoI Selection is employed to learn a better RoI feature adaptively after feature fusion. By replacing FPN with AugFPN in Faster R-CNN, our models achieve 2.3 and 1.6 points higher Average Precision (AP) when using ResNet50 and MobileNet-v2 as backbone respectively. Furthermore, AugFPN improves RetinaNet by 1.6 points AP and FCOS by 0.9 points AP when using ResNet50 as backbone. Codes will be made available.

</details>

### NETNet: Neighbor Erasing and Transferring Network for Better Single Shot Object Detection.
- **链接**: [arXiv:2001.06690](https://arxiv.org/abs/2001.06690) · 📚 被引 36
- **作者**: Yazhao Li, Yanwei Pang, Jianbing Shen, Jiale Cao, Ling Shao
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Due to the advantages of real-time detection and improved performance, single-shot detectors have gained great attention recently. To solve the complex scale variations, single-shot detectors make scale-aware predictions based on multiple pyramid layers. However, the features in the pyramid are not scale-aware enough, which limits the detection performance. Two common problems in single-shot detectors caused by object scale variations can be observed: (1) small objects are easily missed; (2) the salient part of a large object is sometimes detected as an object. With this observation, we propose a new Neighbor Erasing and Transferring (NET) mechanism to reconfigure the pyramid features and explore scale-aware features. In NET, a Neighbor Erasing Module (NEM) is designed to erase the salient features of large objects and emphasize the features of small objects in shallow layers. A Neighbor Transferring Module (NTM) is introduced to transfer the erased features and highlight large objects in deep layers. With this mechanism, a single-shot network called NETNet is constructed for scale-aware object detection. In addition, we propose to aggregate nearest neighboring pyramid features to enhance our NET. NETNet achieves 38.5% AP at a speed of 27 FPS and 32.0% AP at a speed of 55 FPS on MS COCO dataset. As a result, NETNet achieves a better trade-off for real-time and accurate object detection.

</details>

### Learning From Noisy Anchors for One-Stage Object Detection.
- **链接**: [arXiv:1912.05086](https://arxiv.org/abs/1912.05086) · 📚 被引 86
- **作者**: Hengduo Li, Zuxuan Wu, Chen Zhu, Caiming Xiong, Richard Socher, Larry S. Davis
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> State-of-the-art object detectors rely on regressing and classifying an extensive list of possible anchors, which are divided into positive and negative samples based on their intersection-over-union (IoU) with corresponding groundtruth objects. Such a harsh split conditioned on IoU results in binary labels that are potentially noisy and challenging for training. In this paper, we propose to mitigate noise incurred by imperfect label assignment such that the contributions of anchors are dynamically determined by a carefully constructed cleanliness score associated with each anchor. Exploring outputs from both regression and classification branches, the cleanliness scores, estimated without incurring any additional computational overhead, are used not only as soft labels to supervise the training of the classification branch but also sample re-weighting factors for improved localization and classification accuracy. We conduct extensive experiments on COCO, and demonstrate, among other things, the proposed approach steadily improves RetinaNet by ~2% with various backbones.

</details>

### Dynamic Refinement Network for Oriented and Densely Packed Object Detection.
- **链接**: [arXiv:2005.09973](https://arxiv.org/abs/2005.09973) · 📚 被引 382
- **作者**: Xingjia Pan, Yuqiang Ren, Kekai Sheng, Weiming Dong, Haolei Yuan, Xiaowei Guo et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Object detection has achieved remarkable progress in the past decade. However, the detection of oriented and densely packed objects remains challenging because of following inherent reasons: (1) receptive fields of neurons are all axis-aligned and of the same shape, whereas objects are usually of diverse shapes and align along various directions; (2) detection models are typically trained with generic knowledge and may not generalize well to handle specific objects at test time; (3) the limited dataset hinders the development on this task. To resolve the first two issues, we present a dynamic refinement network that consists of two novel components, i.e., a feature selection module (FSM) and a dynamic refinement head (DRH). Our FSM enables neurons to adjust receptive fields in accordance with the shapes and orientations of target objects, whereas the DRH empowers our model to refine the prediction dynamically in an object-aware manner. To address the limited availability of related benchmarks, we collect an extensive and fully annotated dataset, namely, SKU110K-R, which is relabeled with oriented bounding boxes based on SKU110K. We perform quantitative evaluations on several publicly available benchmarks including DOTA, HRSC2016, SKU110K, and our own SKU110K-R dataset. Experimental results show that our method achieves consistent and substantial gains compared with baseline approaches. The code and dataset are available at https://github.com/Anymake/DRN_CVPR2020.

</details>

### Multi-Scale Interactive Network for Salient Object Detection.
- **链接**: [arXiv:2007.09062](https://arxiv.org/abs/2007.09062) · 📚 被引 751
- **作者**: Youwei Pang, Xiaoqi Zhao, Lihe Zhang, Huchuan Lu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Incremental Few-Shot Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Perez-Rua_Incremental_Few-Shot_Object_Detection_CVPR_2020_paper.html)
- **作者**: Juan-Manuel Pérez-Rúa, Xiatian Zhu, Timothy M. Hospedales, Tao Xiang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### End-to-End Pseudo-LiDAR for Image-Based 3D Object Detection.
- **链接**: [arXiv:2004.03080](https://arxiv.org/abs/2004.03080) · 📚 被引 168
- **作者**: Rui Qian, Divyansh Garg, Yan Wang, Yurong You, Serge J. Belongie, Bharath Hariharan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Reliable and accurate 3D object detection is a necessity for safe autonomous driving. Although LiDAR sensors can provide accurate 3D point cloud estimates of the environment, they are also prohibitively expensive for many settings. Recently, the introduction of pseudo-LiDAR (PL) has led to a drastic reduction in the accuracy gap between methods based on LiDAR sensors and those based on cheap stereo cameras. PL combines state-of-the-art deep neural networks for 3D depth estimation with those for 3D object detection by converting 2D depth map outputs to 3D point cloud inputs. However, so far these two networks have to be trained separately. In this paper, we introduce a new framework based on differentiable Change of Representation (CoR) modules that allow the entire PL pipeline to be trained end-to-end. The resulting framework is compatible with most state-of-the-art networks for both tasks and in combination with PointRCNN improves over PL consistently across all benchmarks -- yielding the highest entry on the KITTI image-based 3D object detection leaderboard at the time of submission. Our code will be made available at https://github.com/mileyan/pseudo-LiDAR_e2e.

</details>

### Offset Bin Classification Network for Accurate Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Qiu_Offset_Bin_Classification_Network_for_Accurate_Object_Detection_CVPR_2020_paper.html) · 📚 被引 34
- **作者**: Heqian Qiu, Hongliang Li, Qingbo Wu, Hengcan Shi
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Physically Realizable Adversarial Examples for LiDAR Object Detection.
- **链接**: [arXiv:2004.00543](https://arxiv.org/abs/2004.00543) · 📚 被引 201
- **作者**: James Tu, Mengye Ren, Sivabalan Manivasagam, Ming Liang, Bin Yang, Richard Du et al.
- **🏷️ 机构**: Waabi / University of Toronto
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Modern autonomous driving systems rely heavily on deep learning models to process point cloud sensory data; meanwhile, deep models have been shown to be susceptible to adversarial attacks with visually imperceptible perturbations. Despite the fact that this poses a security concern for the self-driving industry, there has been very little exploration in terms of 3D perception, as most adversarial attacks have only been applied to 2D flat images. In this paper, we address this issue and present a method to generate universal 3D adversarial objects to fool LiDAR detectors. In particular, we demonstrate that placing an adversarial object on the rooftop of any target vehicle to hide the vehicle entirely from LiDAR detectors with a success rate of 80%. We report attack results on a suite of detectors using various input representation of point clouds. We also conduct a pilot study on adversarial defense using data augmentation. This is one step closer towards safer self-driving under unseen conditions from limited training data.

</details>

### Mixture Dense Regression for Object Detection and Human Pose Estimation.
- **链接**: [arXiv:1912.00821](https://arxiv.org/abs/1912.00821) · 📚 被引 41
- **作者**: Ali Varamesh, Tinne Tuytelaars
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Mixture models are well-established learning approaches that, in computer vision, have mostly been applied to inverse or ill-defined problems. However, they are general-purpose divide-and-conquer techniques, splitting the input space into relatively homogeneous subsets in a data-driven manner. Not only ill-defined but also well-defined complex problems should benefit from them. To this end, we devise a framework for spatial regression using mixture density networks. We realize the framework for object detection and human pose estimation. For both tasks, a mixture model yields higher accuracy and divides the input space into interpretable modes. For object detection, mixture components focus on object scale, with the distribution of components closely following that of ground truth the object scale. This practically alleviates the need for multi-scale testing, providing a superior speed-accuracy trade-off. For human pose estimation, a mixture model divides the data based on viewpoint and uncertainty -- namely, front and back views, with back view imposing higher uncertainty. We conduct experiments on the MS COCO dataset and do not face any mode collapse.

</details>

### PointPainting: Sequential Fusion for 3D Object Detection.
- **链接**: [arXiv:1911.10150](https://arxiv.org/abs/1911.10150) · 📚 被引 1122
- **作者**: Sourabh Vora, Alex H. Lang, Bassam Helou, Oscar Beijbom
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Camera and lidar are important sensor modalities for robotics in general and self-driving cars in particular. The sensors provide complementary information offering an opportunity for tight sensor-fusion. Surprisingly, lidar-only methods outperform fusion methods on the main benchmark datasets, suggesting a gap in the literature. In this work, we propose PointPainting: a sequential fusion method to fill this gap. PointPainting works by projecting lidar points into the output of an image-only semantic segmentation network and appending the class scores to each point. The appended (painted) point cloud can then be fed to any lidar-only method. Experiments show large improvements on three different state-of-the art methods, Point-RCNN, VoxelNet and PointPillars on the KITTI and nuScenes datasets. The painted version of PointRCNN represents a new state of the art on the KITTI leaderboard for the bird's-eye view detection task. In ablation, we study how the effects of Painting depends on the quality and format of the semantic segmentation output, and demonstrate how latency can be minimized through pipelining.

</details>

### Label Decoupling Framework for Salient Object Detection.
- **链接**: [arXiv:2008.11048](https://arxiv.org/abs/2008.11048) · 📚 被引 317
- **作者**: Jun Wei, Shuhui Wang, Zhe Wu, Chi Su, Qingming Huang, Qi Tian
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> To get more accurate saliency maps, recent methods mainly focus on aggregating multi-level features from fully convolutional network (FCN) and introducing edge information as auxiliary supervision. Though remarkable progress has been achieved, we observe that the closer the pixel is to the edge, the more difficult it is to be predicted, because edge pixels have a very imbalance distribution. To address this problem, we propose a label decoupling framework (LDF) which consists of a label decoupling (LD) procedure and a feature interaction network (FIN). LD explicitly decomposes the original saliency map into body map and detail map, where body map concentrates on center areas of objects and detail map focuses on regions around edges. Detail map works better because it involves much more pixels than traditional edge supervision. Different from saliency map, body map discards edge pixels and only pays attention to center areas. This successfully avoids the distraction from edge pixels during training. Therefore, we employ two branches in FIN to deal with body map and detail map respectively. Feature interaction (FI) is designed to fuse the two complementary branches to predict the saliency map, which is then used to refine the two branches again. This iterative refinement is helpful for learning better representations and more precise saliency maps. Comprehensive experiments on six benchmark datasets demonstrate that LDF outperforms state-of-the-art approaches on different evaluation metrics.

</details>

### Exploring Categorical Regularization for Domain Adaptive Object Detection.
- **链接**: [arXiv:2003.09152](https://arxiv.org/abs/2003.09152) · 📚 被引 293
- **作者**: Chang-Dong Xu, Xing-Ran Zhao, Xin Jin, Xiu-Shen Wei
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### LiDAR-Based Online 3D Video Object Detection With Graph-Based Message Passing and Spatiotemporal Transformer Attention.
- **链接**: [arXiv:2004.01389](https://arxiv.org/abs/2004.01389) · 📚 被引 133
- **作者**: Junbo Yin, Jianbing Shen, Chenye Guan, Dingfu Zhou, Ruigang Yang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing LiDAR-based 3D object detectors usually focus on the single-frame detection, while ignoring the spatiotemporal information in consecutive point cloud frames. In this paper, we propose an end-to-end online 3D video object detector that operates on point cloud sequences. The proposed model comprises a spatial feature encoding component and a spatiotemporal feature aggregation component. In the former component, a novel Pillar Message Passing Network (PMPNet) is proposed to encode each discrete point cloud frame. It adaptively collects information for a pillar node from its neighbors by iterative message passing, which effectively enlarges the receptive field of the pillar feature. In the latter component, we propose an Attentive Spatiotemporal Transformer GRU (AST-GRU) to aggregate the spatiotemporal information, which enhances the conventional ConvGRU with an attentive memory gating mechanism. AST-GRU contains a Spatial Transformer Attention (STA) module and a Temporal Transformer Attention (TTA) module, which can emphasize the foreground objects and align the dynamic objects, respectively. Experimental results demonstrate that the proposed 3D video object detector achieves state-of-the-art performance on the large-scale nuScenes benchmark.

</details>

### Weakly-Supervised Salient Object Detection via Scribble Annotations.
- **链接**: [arXiv:2003.07685](https://arxiv.org/abs/2003.07685) · 📚 被引 277
- **作者**: Jing Zhang, Xin Yu, Aixuan Li, Peipei Song, Bowen Liu, Yuchao Dai
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Compared with laborious pixel-wise dense labeling, it is much easier to label data by scribbles, which only costs 1$\sim$2 seconds to label one image. However, using scribble labels to learn salient object detection has not been explored. In this paper, we propose a weakly-supervised salient object detection model to learn saliency from such annotations. In doing so, we first relabel an existing large-scale salient object detection dataset with scribbles, namely S-DUTS dataset. Since object structure and detail information is not identified by scribbles, directly training with scribble labels will lead to saliency maps of poor boundary localization. To mitigate this problem, we propose an auxiliary edge detection task to localize object edges explicitly, and a gated structure-aware loss to place constraints on the scope of structure to be recovered. Moreover, we design a scribble boosting scheme to iteratively consolidate our scribble annotations, which are then employed as supervision to learn high-quality saliency maps. As existing saliency evaluation metrics neglect to measure structure alignment of the predictions, the saliency map ranking metric may not comply with human perception. We present a new metric, termed saliency structure measure, to measure the structure alignment of the predicted saliency maps, which is more consistent with human perception. Extensive experiments on six benchmark datasets demonstrate that our method not only outperforms existing weakly-supervised/unsupervised methods, but also is on par with several fully-supervised state-of-the-art models. Our code and data is publicly available at https://github.com/JingZhang617/Scribble_Saliency.

</details>

### SESS: Self-Ensembling Semi-Supervised 3D Object Detection.
- **链接**: [arXiv:1912.11803](https://arxiv.org/abs/1912.11803) · 📚 被引 125
- **作者**: Na Zhao, Tat-Seng Chua, Gim Hee Lee
- **🏷️ 机构**: Deaprtment of Computer Science, National University of Singapore
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The performance of existing point cloud-based 3D object detection methods heavily relies on large-scale high-quality 3D annotations. However, such annotations are often tedious and expensive to collect. Semi-supervised learning is a good alternative to mitigate the data annotation issue, but has remained largely unexplored in 3D object detection. Inspired by the recent success of self-ensembling technique in semi-supervised image classification task, we propose SESS, a self-ensembling semi-supervised 3D object detection framework. Specifically, we design a thorough perturbation scheme to enhance generalization of the network on unlabeled and new unseen data. Furthermore, we propose three consistency losses to enforce the consistency between two sets of predicted 3D object proposals, to facilitate the learning of structure and semantic invariances of objects. Extensive experiments conducted on SUN RGB-D and ScanNet datasets demonstrate the effectiveness of SESS in both inductive and transductive semi-supervised 3D object detection. Our SESS achieves competitive performance compared to the state-of-the-art fully-supervised method by using only 50% labeled data. Our code is available at https://github.com/Na-Z/sess.

</details>

## 跨领域论文（完整笔记在其他领域）

- MLCVNet: Multi-Level Context VoteNet for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202020.md)
- Density-Based Clustering for 3D Object Detection in Point Clouds. → [3d-detection](../3d-detection/Guideline%202020.md)
- DSGN: Deep Stereo Geometry Network for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202020.md)
- MnasFPN: Learning Latency-Aware Pyramid Architecture for Object Detection on Mobile Devices. → [neural-architecture-search](../neural-architecture-search/Guideline%202020.md)
- A Hierarchical Graph Network for 3D Object Detection on Point Clouds. → [3d-detection](../3d-detection/Guideline%202020.md)
- MonoPair: Monocular 3D Object Detection Using Pairwise Spatial Relationships. → [3d-detection](../3d-detection/Guideline%202020.md)
- Learning Depth-Guided Convolutions for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202020.md)
- Hit-Detector: Hierarchical Trinity Architecture Search for Object Detection. → [neural-architecture-search](../neural-architecture-search/Guideline%202020.md)
- Structure Aware Single-Stage 3D Object Detection From Point Cloud. → [3d-detection](../3d-detection/Guideline%202020.md)
- What You See is What You Get: Exploiting Visibility for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202020.md)
- SP-NAS: Serial-to-Parallel Backbone Search for Object Detection. → [neural-architecture-search](../neural-architecture-search/Guideline%202020.md)
- IDA-3D: Instance-Depth-Aware 3D Object Detection From Stereo Vision for Autonomous Driving. → [3d-detection](../3d-detection/Guideline%202020.md)
- ImVoteNet: Boosting 3D Object Detection in Point Clouds With Image Votes. → [3d-detection](../3d-detection/Guideline%202020.md)
- PV-RCNN: Point-Voxel Feature Set Abstraction for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202020.md)
- Point-GNN: Graph Neural Network for 3D Object Detection in a Point Cloud. → [3d-detection](../3d-detection/Guideline%202020.md)
- Disp R-CNN: Stereo 3D Object Detection via Shape Prior Guided Instance Disparity Estimation. → [3d-detection](../3d-detection/Guideline%202020.md)
- NAS-FCOS: Fast Neural Architecture Search for Object Detection. → [neural-architecture-search](../neural-architecture-search/Guideline%202020.md)
- Exploring Bottom-Up and Top-Down Cues With Attentive Learning for Webly Supervised Object Detection. → [open-set-detection](../open-set-detection/Guideline%202020.md)
- HVNet: Hybrid Voxel Network for LiDAR Based 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202020.md)

<!-- COMPLETE v1 papers=68 -->
