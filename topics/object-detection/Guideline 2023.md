# Object Detection — 2023 Guideline

> 领域: 通用 2D 目标检测（检测器架构、密集预测、小物体/旋转框/NMS 等）
> 论文数: 101 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份:

### DINO: DETR with Improved DeNoising Anchor Boxes for End-to-End Object Detection. **⭐⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [出版页](https://openreview.net/forum?id=3mRwyG5one)
- **作者**: Hao Zhang, Feng Li, Shilong Liu, Lei Zhang, Hang Su, Jun Zhu et al.
- **🏷️ 机构**: PolyU / OPPO
- **会议**: ICLR 2023
- **摘要（中）**: DINO提出改进的去噪锚框机制，通过对比去噪训练和混合查询选择，增强DETR的收敛性和检测精度。该方法在COCO上达到SOTA性能，成为后续研究的重要基线。
- **摘要（英）**: DINO introduces improved denoising anchor boxes with contrastive denoising training and mixed query selection, enhancing convergence and accuracy of DETR. It achieves state-of-the-art results on COCO and serves as a key baseline.
- **核心贡献**: 提出改进的去噪锚框机制，显著提升DETR检测性能。
- **创新点**: 结合对比去噪和混合查询选择，优化训练稳定性和精度。
- **结果**: 在COCO上达到SOTA，并成为广泛使用的基线。

### Learning Object-Language Alignments for Open-Vocabulary Object Detection.
- **链接**: [出版页](https://openreview.net/forum?id=mjHlitXvReu)
- **作者**: Chuang Lin, Peize Sun, Yi Jiang, Ping Luo, Lizhen Qu, Gholamreza Haffari et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### Continual Detection Transformer for Incremental Object Detection. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2304.03110](https://arxiv.org/abs/2304.03110) · 📚 被引 93
- **作者**: Yaoyao Liu, Bernt Schiele, Andrea Vedaldi, Christian Rupprecht
- **🏷️ 机构**: Max Planck Institute for Informatics, Saarland Informatics Campus, University of Oxford,Visual Geometry Group,Department of Engineering Science
- **会议**: CVPR 2023
- **摘要（中）**: 针对增量目标检测中灾难性遗忘问题，提出连续检测Transformer，通过检测器知识蒸馏损失和校准策略，有效利用知识蒸馏和示例回放。在COCO上达到SOTA性能。
- **摘要（英）**: This paper proposes Continual Detection Transformer (CL-DETR) for incremental object detection, addressing catastrophic forgetting via detector knowledge distillation loss and calibration strategy. It achieves state-of-the-art results on COCO.
- **核心贡献**: 提出适用于Transformer检测器的增量学习框架。
- **创新点**: 设计检测器知识蒸馏损失和标签分布校准策略。
- **结果**: 在COCO上达到SOTA性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Incremental object detection (IOD) aims to train an object detector in phases, each with annotations for new object categories. As other incremental settings, IOD is subject to catastrophic forgetting, which is often addressed by techniques such as knowledge distillation (KD) and exemplar replay (ER). However, KD and ER do not work well if applied directly to state-of-the-art transformer-based object detectors such as Deformable DETR and UP-DETR. In this paper, we solve these issues by proposing a ContinuaL DEtection TRansformer (CL-DETR), a new method for transformer-based IOD which enables effective usage of KD and ER in this context. First, we introduce a Detector Knowledge Distillation (DKD) loss, focusing on the most informative and reliable predictions from old versions of the model, ignoring redundant background predictions, and ensuring compatibility with the available ground-truth labels. We also improve ER by proposing a calibration strategy to preserve the label distribution of the training set, therefore better matching training and testing statistics. We conduct extensive experiments on COCO 2017 and demonstrate that CL-DETR achieves state-of-the-art results in the IOD setting.

</details>

### 3D Video Object Detection with Learnable Object-Centric Global Optimization. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2303.15416](https://arxiv.org/abs/2303.15416) · 📚 被引 10
- **作者**: Jiawei He, Yuntao Chen, Naiyan Wang, Zhaoxiang Zhang
- **🏷️ 机构**: Institute of Automation, Chinese Academy of Sciences (CASIA),CRIPAC, HKISI_CAS,Centre for Artificial Intelligence and Robotics, TuSimple
- **会议**: CVPR 2023
- **摘要（中）**: 针对3D视频目标检测中运动物体违反多视图几何约束的问题，提出BA-Det，将物体作为一等公民进行基于对应关系的优化。通过物体中心时序对应学习和特征度量束调整，实现端到端优化。在Waymo数据集上达到SOTA性能，且计算开销小。
- **摘要（英）**: This paper proposes BA-Det for 3D video object detection, treating objects as first-class citizens in correspondence-based optimization. It introduces object-centric temporal correspondence learning and featuremetric bundle adjustment, achieving SOTA on Waymo with marginal computation cost.
- **核心贡献**: 提出物体中心束调整框架，提升3D视频检测精度。
- **创新点**: 将物体作为优化主体，解决运动物体几何约束问题。
- **结果**: 在Waymo上达到SOTA，计算开销小。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We explore long-term temporal visual correspondence-based optimization for 3D video object detection in this work. Visual correspondence refers to one-to-one mappings for pixels across multiple images. Correspondence-based optimization is the cornerstone for 3D scene reconstruction but is less studied in 3D video object detection, because moving objects violate multi-view geometry constraints and are treated as outliers during scene reconstruction. We address this issue by treating objects as first-class citizens during correspondence-based optimization. In this work, we propose BA-Det, an end-to-end optimizable object detector with object-centric temporal correspondence learning and featuremetric object bundle adjustment. Empirically, we verify the effectiveness and efficiency of BA-Det for multiple baseline 3D detectors under various setups. Our BA-Det achieves SOTA performance on the large-scale Waymo Open Dataset (WOD) with only marginal computation cost. Our code is available at https://github.com/jiaweihe1996/BA-Det.

</details>

### Unknown Sniffer for Object Detection: Don't Turn a Blind Eye to Unknown Objects.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00315)
- **作者**: Wenteng Liang, Feng Xue, Yihao Liu, Guofeng Zhong, Anlong Ming
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### CAT: LoCalization and IdentificAtion Cascade Detection Transformer for Open-World Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01885)
- **作者**: Shuailei Ma, Yuefeng Wang, Ying Wei, Jiaqi Fan, Thomas H. Li, Hongli Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### Detection Hub: Unifying Object Detection Datasets via Query Adaptation on Language Embedding. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2206.03484](https://arxiv.org/abs/2206.03484) · 📚 被引 10
- **作者**: Lingchen Meng, Xiyang Dai, Yinpeng Chen, Pengchuan Zhang, Dongdong Chen, Mengchen Liu et al.
- **🏷️ 机构**: School of CS, Fudan University,Shanghai Key Lab of Intell. Info. Processing, Microsoft
- **会议**: CVPR 2023
- **摘要（中）**: ①针对多数据集联合训练中类别差异和域间隙导致性能下降的问题，提出Detection Hub框架。②通过数据集感知设计（学习数据集嵌入以调整查询和卷积核）和类别语义对齐（用词嵌入替代one-hot表示）实现统一检测。③相比现有方法，有效缓解数据集不一致性，实现跨数据集学习。④实验表明联合训练显著优于单独训练，并在UODB基准上达到SoTA性能。
- **摘要（英）**: This paper addresses taxonomy and domain inconsistencies in multi-dataset object detection by proposing Detection Hub, which uses dataset-aware query adaptation and semantic category alignment via word embeddings. It enables effective joint training, achieving significant gains over single-dataset training and SoTA on UODB benchmark.
- **核心贡献**: 提出Detection Hub，实现多数据集统一检测并提升性能。
- **创新点**: 数据集感知的查询和卷积核适应，以及语言嵌入类别对齐。
- **结果**: 在UODB基准上达到SoTA。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Combining multiple datasets enables performance boost on many computer vision tasks. But similar trend has not been witnessed in object detection when combining multiple datasets due to two inconsistencies among detection datasets: taxonomy difference and domain gap. In this paper, we address these challenges by a new design (named Detection Hub) that is dataset-aware and category-aligned. It not only mitigates the dataset inconsistency but also provides coherent guidance for the detector to learn across multiple datasets. In particular, the dataset-aware design is achieved by learning a dataset embedding that is used to adapt object queries as well as convolutional kernels in detection heads. The categories across datasets are semantically aligned into a unified space by replacing one-hot category representations with word embedding and leveraging the semantic coherence of language embedding. Detection Hub fulfills the benefits of large data on object detection. Experiments demonstrate that joint training on multiple datasets achieves significant performance gains over training on each dataset alone. Detection Hub further achieves SoTA performance on UODB benchmark with wide variety of datasets.

</details>

### Pixels, Regions, and Objects: Multiple Enhancement for Salient Object Detection. **⭐⭐** (相关度: 40%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00967) · 📚 被引 132
- **作者**: Yi Wang, Ruili Wang, Xin Fan, Tianzhu Wang, Xiangjian He
- **🏷️ 机构**: DUT-RU International School of Information Science and Engineering, Dalian University of Technology,China, School of Mathematical and Computational Sciences, Massey University,New Zealand, School of Computer Science, University of Nottingham Ningbo China,Ningbo,China
- **会议**: CVPR 2023
- **摘要（中）**: ①针对显著目标检测中像素、区域和对象多层次信息利用不足的问题，提出多重增强方法。②方法结合像素级、区域级和对象级增强策略，提升显著目标检测性能。③相比现有方法，更全面地利用多尺度信息。④摘要未提供具体实验数据，效果未知。
- **摘要（英）**: This paper addresses insufficient multi-level information utilization in salient object detection by proposing multiple enhancement strategies at pixel, region, and object levels. It aims to improve performance, but no experimental details are provided in the abstract.
- **核心贡献**: 提出多层次增强的显著目标检测方法。
- **创新点**: 结合像素、区域和对象级增强。
- **结果**: 未提供具体效果。

### Curricular Object Manipulation in LiDAR-based Object Detection. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2304.04248](https://arxiv.org/abs/2304.04248) · 📚 被引 15
- **作者**: Ziyue Zhu, Qiang Meng, Xiao Wang, Ke Wang, Liujiang Yan, Jian Yang
- **🏷️ 机构**: College of Computer Science, Nankai University,Tianjin Key Laboratory of Visual Computing and Intelligent Perception, Didi Chuxing
- **会议**: CVPR 2023
- **摘要（中）**: ①针对LiDAR 3D目标检测中训练样本难度分布不均的问题，提出课程学习框架COM。②设计COMLoss动态预测目标难度并调整损失权重，以及COMAug策略在GT-Aug基础上按难度聚类和渐进增强。③相比现有方法，通过课程学习提升模型性能和泛化能力。④实验和消融研究验证了框架的有效性和通用性，代码已开源。
- **摘要（英）**: This paper explores curriculum learning in LiDAR-based 3D detection by proposing COM, which includes COMLoss for dynamic difficulty-based loss weighting and COMAug for progressive augmentation. It improves model performance and generalization, validated by extensive experiments, with code available.
- **核心贡献**: 提出课程学习框架COM，提升LiDAR 3D检测性能。
- **创新点**: 动态难度预测和渐进增强策略。
- **结果**: 实验验证了有效性和通用性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper explores the potential of curriculum learning in LiDAR-based 3D object detection by proposing a curricular object manipulation (COM) framework. The framework embeds the curricular training strategy into both the loss design and the augmentation process. For the loss design, we propose the COMLoss to dynamically predict object-level difficulties and emphasize objects of different difficulties based on training stages. On top of the widely-used augmentation technique called GT-Aug in LiDAR detection tasks, we propose a novel COMAug strategy which first clusters objects in ground-truth database based on well-designed heuristics. Group-level difficulties rather than individual ones are then predicted and updated during training for stable results. Model performance and generalization capabilities can be improved by sampling and augmenting progressively more difficult objects into the training samples. Extensive experiments and ablation studies reveal the superior and generality of the proposed framework. The code is available at https://github.com/ZZY816/COM.

</details>

### PROB: Probabilistic Objectness for Open World Object Detection.
- **链接**: [arXiv:2212.01424](https://arxiv.org/abs/2212.01424) · [代码](https://github.com/orrzohar/PROB) · 📚 被引 110
- **作者**: Orr Zohar, Kuan-Chieh Wang, Serena Yeung
- **🏷️ 机构**: Stanford University
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open World Object Detection (OWOD) is a new and challenging computer vision task that bridges the gap between classic object detection (OD) benchmarks and object detection in the real world. In addition to detecting and classifying seen/labeled objects, OWOD algorithms are expected to detect novel/unknown objects - which can be classified and incrementally learned. In standard OD, object proposals not overlapping with a labeled object are automatically classified as background. Therefore, simply applying OD methods to OWOD fails as unknown objects would be predicted as background. The challenge of detecting unknown objects stems from the lack of supervision in distinguishing unknown objects and background object proposals. Previous OWOD methods have attempted to overcome this issue by generating supervision using pseudo-labeling - however, unknown object detection has remained low. Probabilistic/generative models may provide a solution for this challenge. Herein, we introduce a novel probabilistic framework for objectness estimation, where we alternate between probability distribution estimation and objectness likelihood maximization of known objects in the embedded feature space - ultimately allowing us to estimate the objectness probability of different proposals. The resulting Probabilistic Objectness transformer-based open-world detector, PROB, integrates our framework into traditional object detection models, adapting them for the open-world setting. Comprehensive experiments on OWOD benchmarks show that PROB outperforms all existing OWOD methods in both unknown object detection ($\sim 2\times$ unknown recall) and known object detection ($\sim 10\%$ mAP). Our code will be made available upon publication at https://github.com/orrzohar/PROB.

</details>

### Detecting Everything in the Open World: Towards Universal Object Detection.
- **链接**: [arXiv:2303.11749](https://arxiv.org/abs/2303.11749) · 📚 被引 96
- **作者**: Zhenyu Wang, Yali Li, Xi Chen, Ser-Nam Lim, Antonio Torralba, Hengshuang Zhao et al.
- **🏷️ 机构**: Tsinghua University,Department of Electronic Engineering, The University of Hong Kong, Meta AI
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we formally address universal object detection, which aims to detect every scene and predict every category. The dependence on human annotations, the limited visual information, and the novel categories in the open world severely restrict the universality of traditional detectors. We propose UniDetector, a universal object detector that has the ability to recognize enormous categories in the open world. The critical points for the universality of UniDetector are: 1) it leverages images of multiple sources and heterogeneous label spaces for training through the alignment of image and text spaces, which guarantees sufficient information for universal representations. 2) it generalizes to the open world easily while keeping the balance between seen and unseen classes, thanks to abundant information from both vision and language modalities. 3) it further promotes the generalization ability to novel categories through our proposed decoupling training manner and probability calibration. These contributions allow UniDetector to detect over 7k categories, the largest measurable category size so far, with only about 500 classes participating in training. Our UniDetector behaves the strong zero-shot generalization ability on large-vocabulary datasets like LVIS, ImageNetBoxes, and VisualGenome - it surpasses the traditional supervised baselines by more than 4\% on average without seeing any corresponding images. On 13 public detection datasets with various scenes, UniDetector also achieves state-of-the-art performance with only a 3\% amount of training data.

</details>

### Bi-LRFusion: Bi-Directional LiDAR-Radar Fusion for 3D Dynamic Object Detection.
- **链接**: [arXiv:2306.01438](https://arxiv.org/abs/2306.01438) · [代码](https://github.com/JessieW0806/BiLRFusion) · 📚 被引 48
- **作者**: Yingjie Wang, Jiajun Deng, Yao Li, Jinshui Hu, Cong Liu, Yu Zhang et al.
- **🏷️ 机构**: University of Science and Technology of China, University of Sydney, iFLYTEK
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> LiDAR and Radar are two complementary sensing approaches in that LiDAR specializes in capturing an object's 3D shape while Radar provides longer detection ranges as well as velocity hints. Though seemingly natural, how to efficiently combine them for improved feature representation is still unclear. The main challenge arises from that Radar data are extremely sparse and lack height information. Therefore, directly integrating Radar features into LiDAR-centric detection networks is not optimal. In this work, we introduce a bi-directional LiDAR-Radar fusion framework, termed Bi-LRFusion, to tackle the challenges and improve 3D detection for dynamic objects. Technically, Bi-LRFusion involves two steps: first, it enriches Radar's local features by learning important details from the LiDAR branch to alleviate the problems caused by the absence of height information and extreme sparsity; second, it combines LiDAR features with the enhanced Radar features in a unified bird's-eye-view representation. We conduct extensive experiments on nuScenes and ORR datasets, and show that our Bi-LRFusion achieves state-of-the-art performance for detecting dynamic objects. Notably, Radar data in these two datasets have different formats, which demonstrates the generalizability of our method. Codes are available at https://github.com/JessieW0806/BiLRFusion.

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> LiDAR and Radar are two complementary sensing approaches in that LiDAR specializes in capturing an object's 3D shape while Radar provides longer detection ranges as well as velocity hints. Though seemingly natural, how to efficiently combine them for improved feature representation is still unclear. The main challenge arises from that Radar data are extremely sparse and lack height information. Therefore, directly integrating Radar features into LiDAR-centric detection networks is not optimal. In this work, we introduce a bi-directional LiDAR-Radar fusion framework, termed Bi-LRFusion, to tackle the challenges and improve 3D detection for dynamic objects. Technically, Bi-LRFusion involves two steps: first, it enriches Radar's local features by learning important details from the LiDAR branch to alleviate the problems caused by the absence of height information and extreme sparsity; second, it combines LiDAR features with the enhanced Radar features in a unified bird's-eye-view representation. We conduct extensive experiments on nuScenes and ORR datasets, and show that our Bi-LRFusion achieves state-of-the-art performance for detecting dynamic objects. Notably, Radar data in these two datasets have different formats, which demonstrates the generalizability of our method. Codes are available at https://github.com/JessieW0806/BiLRFusion.

</details>

### Normalizing Flow based Feature Synthesis for Outlier-Aware Object Detection.
- **链接**: [arXiv:2302.07106](https://arxiv.org/abs/2302.07106) · [代码](https://github.com/nish03/FFS) · 📚 被引 14
- **作者**: Nishant Kumar, Sinisa Segvic, Abouzar Eslami, Stefan Gumhold
- **🏷️ 机构**: TU Dresden, University of Zagreb - FER, Carl Zeiss Meditec AG
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Real-world deployment of reliable object detectors is crucial for applications such as autonomous driving. However, general-purpose object detectors like Faster R-CNN are prone to providing overconfident predictions for outlier objects. Recent outlier-aware object detection approaches estimate the density of instance-wide features with class-conditional Gaussians and train on synthesized outlier features from their low-likelihood regions. However, this strategy does not guarantee that the synthesized outlier features will have a low likelihood according to the other class-conditional Gaussians. We propose a novel outlier-aware object detection framework that distinguishes outliers from inlier objects by learning the joint data distribution of all inlier classes with an invertible normalizing flow. The appropriate sampling of the flow model ensures that the synthesized outliers have a lower likelihood than inliers of all object classes, thereby modeling a better decision boundary between inlier and outlier objects. Our approach significantly outperforms the state-of-the-art for outlier-aware object detection on both image and video datasets. Code available at https://github.com/nish03/FFS

</details>

### Cut and Learn for Unsupervised Object Detection and Instance Segmentation.
- **链接**: [arXiv:2301.11320](https://arxiv.org/abs/2301.11320) · 📚 被引 182
- **作者**: Xudong Wang, Rohit Girdhar, Stella X. Yu, Ishan Misra
- **🏷️ 机构**: FAIR, Meta AI, UC Berkeley / ICSI
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose Cut-and-LEaRn (CutLER), a simple approach for training unsupervised object detection and segmentation models. We leverage the property of self-supervised models to 'discover' objects without supervision and amplify it to train a state-of-the-art localization model without any human labels. CutLER first uses our proposed MaskCut approach to generate coarse masks for multiple objects in an image and then learns a detector on these masks using our robust loss function. We further improve the performance by self-training the model on its predictions. Compared to prior work, CutLER is simpler, compatible with different detection architectures, and detects multiple objects. CutLER is also a zero-shot unsupervised detector and improves detection performance AP50 by over 2.7 times on 11 benchmarks across domains like video frames, paintings, sketches, etc. With finetuning, CutLER serves as a low-shot detector surpassing MoCo-v2 by 7.3% APbox and 6.6% APmask on COCO when training with 5% labels.

</details>

### Phase-Shifting Coder: Predicting Accurate Orientation in Oriented Object Detection.
- **链接**: [arXiv:2211.06368](https://arxiv.org/abs/2211.06368) · [代码](https://github.com/open-mmlab/mmrotate) · 📚 被引 173
- **作者**: Yi Yu, Feipeng Da
- **🏷️ 机构**: School of Automation, Southeast University,Nanjing,China
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> With the vigorous development of computer vision, oriented object detection has gradually been featured. In this paper, a novel differentiable angle coder named phase-shifting coder (PSC) is proposed to accurately predict the orientation of objects, along with a dual-frequency version (PSCD). By mapping the rotational periodicity of different cycles into the phase of different frequencies, we provide a unified framework for various periodic fuzzy problems caused by rotational symmetry in oriented object detection. Upon such a framework, common problems in oriented object detection such as boundary discontinuity and square-like problems are elegantly solved in a unified form. Visual analysis and experiments on three datasets prove the effectiveness and the potentiality of our approach. When facing scenarios requiring high-quality bounding boxes, the proposed methods are expected to give a competitive performance. The codes are publicly available at https://github.com/open-mmlab/mmrotate.

</details>

### Enhanced Training of Query-Based Object Detection via Selective Query Recollection.
- **链接**: [arXiv:2212.07593](https://arxiv.org/abs/2212.07593) · 📚 被引 64
- **作者**: Fangyi Chen, Han Zhang, Kai Hu, Yu-Kai Huang, Chenchen Zhu, Marios Savvides
- **🏷️ 机构**: Carnegie Mellon University, Meta AI
- **会议**: CVPR 2023

### STDLens: Model Hijacking-Resilient Federated Learning for Object Detection.
- **链接**: [arXiv:2303.11511](https://arxiv.org/abs/2303.11511) · 📚 被引 13
- **作者**: Ka-Ho Chow, Ling Liu, Wenqi Wei, Fatih Ilhan, Yanzhao Wu
- **🏷️ 机构**: Georgia Instutite of Technology,Atlanta,GA,USA
- **会议**: CVPR 2023

### What Can Human Sketches Do for Object Detection?
- **链接**: [arXiv:2303.15149](https://arxiv.org/abs/2303.15149) · 📚 被引 41
- **作者**: Pinaki Nath Chowdhury, Ayan Kumar Bhunia, Aneeshan Sain, Subhadeep Koley, Tao Xiang, Yi-Zhe Song
- **🏷️ 机构**: SketchX, CVSSP, University of Surrey,United Kingdom
- **会议**: CVPR 2023

### The Differentiable Lens: Compound Lens Search over Glass Surfaces and Materials for Object Detection.
- **链接**: [arXiv:2212.04441](https://arxiv.org/abs/2212.04441) · 📚 被引 18
- **作者**: Geoffroi Côté, Fahim Mannan, Simon Thibault, Jean-François Lalonde, Felix Heide
- **🏷️ 机构**: Universit&#x00E9; Laval, Algolux, Princeton University
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Most camera lens systems are designed in isolation, separately from downstream computer vision methods. Recently, joint optimization approaches that design lenses alongside other components of the image acquisition and processing pipeline -- notably, downstream neural networks -- have achieved improved imaging quality or better performance on vision tasks. However, these existing methods optimize only a subset of lens parameters and cannot optimize glass materials given their categorical nature. In this work, we develop a differentiable spherical lens simulation model that accurately captures geometrical aberrations. We propose an optimization strategy to address the challenges of lens design -- notorious for non-convex loss function landscapes and many manufacturing constraints -- that are exacerbated in joint optimization tasks. Specifically, we introduce quantized continuous glass variables to facilitate the optimization and selection of glass materials in an end-to-end design context, and couple this with carefully designed constraints to support manufacturability. In automotive object detection, we report improved detection performance over existing designs even when simplifying designs to two- or three-element lenses, despite significantly degrading the image quality.

</details>

### Meta-Tuning Loss Functions and Data Augmentation for Few-Shot Object Detection.
- **链接**: [arXiv:2304.12161](https://arxiv.org/abs/2304.12161) · 📚 被引 32
- **作者**: Berkan Demirel, Orhun Bugra Baran, Ramazan Gokberk Cinbis
- **🏷️ 机构**: Middle East Technical University
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Few-shot object detection, the problem of modelling novel object detection categories with few training instances, is an emerging topic in the area of few-shot learning and object detection. Contemporary techniques can be divided into two groups: fine-tuning based and meta-learning based approaches. While meta-learning approaches aim to learn dedicated meta-models for mapping samples to novel class models, fine-tuning approaches tackle few-shot detection in a simpler manner, by adapting the detection model to novel classes through gradient based optimization. Despite their simplicity, fine-tuning based approaches typically yield competitive detection results. Based on this observation, we focus on the role of loss functions and augmentations as the force driving the fine-tuning process, and propose to tune their dynamics through meta-learning principles. The proposed training scheme, therefore, allows learning inductive biases that can boost few-shot detection, while keeping the advantages of fine-tuning based approaches. In addition, the proposed approach yields interpretable loss functions, as opposed to highly parametric and complex few-shot meta-models. The experimental results highlight the merits of the proposed scheme, with significant improvements over the strong fine-tuning based few-shot detection baselines on benchmark Pascal VOC and MS-COCO datasets, in terms of both standard and generalized few-shot performance metrics.

</details>

### Harmonious Teacher for Cross-Domain Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02282) · 📚 被引 71
- **作者**: Jinhong Deng, Dongli Xu, Wen Li, Lixin Duan
- **🏷️ 机构**: University of Electronic Science and Technology of China, University of Sydney, Shenzhen Institute for Advanced Study, UESTC
- **会议**: CVPR 2023

### Adaptive Sparse Convolutional Networks with Global Context Enhancement for Faster Object Detection on Drone Images.
- **链接**: [arXiv:2303.14488](https://arxiv.org/abs/2303.14488) · [代码](https://github.com/Cuogeihong/CEASC) · 📚 被引 238
- **作者**: Bowei Du, Yecheng Huang, Jiaxin Chen, Di Huang
- **🏷️ 机构**: Beihang University,State Key Laboratory of Software Development Environment,Beijing,China, School of Computer Science and Engineering, Beihang University,Beijing,China
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Object detection on drone images with low-latency is an important but challenging task on the resource-constrained unmanned aerial vehicle (UAV) platform. This paper investigates optimizing the detection head based on the sparse convolution, which proves effective in balancing the accuracy and efficiency. Nevertheless, it suffers from inadequate integration of contextual information of tiny objects as well as clumsy control of the mask ratio in the presence of foreground with varying scales. To address the issues above, we propose a novel global context-enhanced adaptive sparse convolutional network (CEASC). It first develops a context-enhanced group normalization (CE-GN) layer, by replacing the statistics based on sparsely sampled features with the global contextual ones, and then designs an adaptive multi-layer masking strategy to generate optimal mask ratios at distinct scales for compact foreground coverage, promoting both the accuracy and efficiency. Extensive experimental results on two major benchmarks, i.e. VisDrone and UAVDT, demonstrate that CEASC remarkably reduces the GFLOPs and accelerates the inference procedure when plugging into the typical state-of-the-art detection frameworks (e.g. RetinaNet and GFL V1) with competitive performance. Code is available at https://github.com/Cuogeihong/CEASC.

</details>

### Weak-shot Object Detection through Mutual Knowledge Transfer.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01884) · 📚 被引 1
- **作者**: Xuanyi Du, Weitao Wan, Chong Sun, Chen Li
- **🏷️ 机构**: WeChat, Tencent
- **会议**: CVPR 2023

### AsyFOD: An Asymmetric Adaptation Paradigm for Few-Shot Domain Adaptive Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00318) · 📚 被引 30
- **作者**: Yipeng Gao, Kun-Yu Lin, Junkai Yan, Yaowei Wang, Wei-Shi Zheng
- **🏷️ 机构**: School of Computer Science and Engineering, Sun Yat-sen University,China, Pengcheng Lab
- **会议**: CVPR 2023

### Recurrent Vision Transformers for Object Detection with Event Cameras.
- **链接**: [arXiv:2212.05598](https://arxiv.org/abs/2212.05598) · 📚 被引 188
- **作者**: Mathias Gehrig, Davide Scaramuzza
- **🏷️ 机构**: Robotics and Perception Group, University of Zurich,Switzerland
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present Recurrent Vision Transformers (RVTs), a novel backbone for object detection with event cameras. Event cameras provide visual information with sub-millisecond latency at a high-dynamic range and with strong robustness against motion blur. These unique properties offer great potential for low-latency object detection and tracking in time-critical scenarios. Prior work in event-based vision has achieved outstanding detection performance but at the cost of substantial inference time, typically beyond 40 milliseconds. By revisiting the high-level design of recurrent vision backbones, we reduce inference time by a factor of 6 while retaining similar performance. To achieve this, we explore a multi-stage design that utilizes three key concepts in each stage: First, a convolutional prior that can be regarded as a conditional positional embedding. Second, local and dilated global self-attention for spatial feature interaction. Third, recurrent temporal feature aggregation to minimize latency while retaining temporal information. RVTs can be trained from scratch to reach state-of-the-art performance on event-based object detection - achieving an mAP of 47.2% on the Gen1 automotive dataset. At the same time, RVTs offer fast inference (<12 ms on a T4 GPU) and favorable parameter efficiency (5 times fewer than prior art). Our study brings new insights into effective design choices that can be fruitful for research beyond event-based vision.

</details>

### Learned Two-Plane Perspective Prior based Image Resampling for Efficient Object Detection.
- **链接**: [arXiv:2303.14311](https://arxiv.org/abs/2303.14311) · 📚 被引 6
- **作者**: Anurag Ghosh, N. Dinesh Reddy, Christoph Mertz, Srinivasa G. Narasimhan
- **🏷️ 机构**: Carnegie Mellon University
- **会议**: CVPR 2023

### NIFF: Alleviating Forgetting in Generalized Few-Shot Object Detection via Neural Instance Feature Forging.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02317) · 📚 被引 23
- **作者**: Karim Guirguis, Johannes Meier, George Eskandar, Matthias Kayser, Bin Yang, Jürgen Beyerer
- **🏷️ 机构**: Robert Bosch GmbH, University of Stuttgart, Karlsruhe Institute of Technology
- **会议**: CVPR 2023

### Camouflaged Object Detection with Feature Decomposition and Edge Reconstruction.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02111) · 📚 被引 364
- **作者**: Chunming He, Kai Li, Yachao Zhang, Longxiang Tang, Yulun Zhang, Zhenhua Guo et al.
- **🏷️ 机构**: Shenzhen International Graduate School, Tsinghua University, NEC Laboratories America, ETH Z&#x00FC;rich
- **会议**: CVPR 2023

### NeRF-RPN: A general framework for object detection in NeRFs.
- **链接**: [arXiv:2211.11646](https://arxiv.org/abs/2211.11646) · [代码](https://github.com/lyclyc52/NeRF_RPN) · 📚 被引 54
- **作者**: Benran Hu, Junkai Huang, Yichen Liu, Yu-Wing Tai, Chi-Keung Tang
- **🏷️ 机构**: The Hong Kong University of Science and Technology
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper presents the first significant object detection framework, NeRF-RPN, which directly operates on NeRF. Given a pre-trained NeRF model, NeRF-RPN aims to detect all bounding boxes of objects in a scene. By exploiting a novel voxel representation that incorporates multi-scale 3D neural volumetric features, we demonstrate it is possible to regress the 3D bounding boxes of objects in NeRF directly without rendering the NeRF at any viewpoint. NeRF-RPN is a general framework and can be applied to detect objects without class labels. We experimented NeRF-RPN with various backbone architectures, RPN head designs and loss functions. All of them can be trained in an end-to-end manner to estimate high quality 3D bounding boxes. To facilitate future research in object detection for NeRF, we built a new benchmark dataset which consists of both synthetic and real-world data with careful labeling and clean up. Code and dataset are available at https://github.com/lyclyc52/NeRF_RPN.

</details>

### SOOD: Towards Semi-Supervised Oriented Object Detection.
- **链接**: [arXiv:2304.04515](https://arxiv.org/abs/2304.04515) · 📚 被引 70
- **作者**: Wei Hua, Dingkang Liang, Jingyu Li, Xiaolong Liu, Zhikang Zou, Xiaoqing Ye et al.
- **🏷️ 机构**: Huazhong University of Science and Technology, Baidu Inc.,China
- **会议**: CVPR 2023

### T-SEA: Transfer-Based Self-Ensemble Attack on Object Detection.
- **链接**: [arXiv:2211.09773](https://arxiv.org/abs/2211.09773) · 📚 被引 72
- **作者**: Hao Huang, Ziyan Chen, Huanran Chen, Yongtao Wang, Kevin Zhang
- **🏷️ 机构**: Peking University,Beijing,China
- **会议**: CVPR 2023

### Feature Shrinkage Pyramid for Camouflaged Object Detection with Transformers.
- **链接**: [arXiv:2303.14816](https://arxiv.org/abs/2303.14816) · [代码](https://github.com/ZhouHuang23/FSPNet) · 📚 被引 273
- **作者**: Zhou Huang, Hang Dai, Tian-Zhu Xiang, Shuo Wang, Huai-Xin Chen, Jie Qin et al.
- **🏷️ 机构**: Sichuan Changhong Electric Co., Ltd, University of Glasgow, G42
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision transformers have recently shown strong global context modeling capabilities in camouflaged object detection. However, they suffer from two major limitations: less effective locality modeling and insufficient feature aggregation in decoders, which are not conducive to camouflaged object detection that explores subtle cues from indistinguishable backgrounds. To address these issues, in this paper, we propose a novel transformer-based Feature Shrinkage Pyramid Network (FSPNet), which aims to hierarchically decode locality-enhanced neighboring transformer features through progressive shrinking for camouflaged object detection. Specifically, we propose a nonlocal token enhancement module (NL-TEM) that employs the non-local mechanism to interact neighboring tokens and explore graph-based high-order relations within tokens to enhance local representations of transformers. Moreover, we design a feature shrinkage decoder (FSD) with adjacent interaction modules (AIM), which progressively aggregates adjacent transformer features through a layer-bylayer shrinkage pyramid to accumulate imperceptible but effective cues as much as possible for object information decoding. Extensive quantitative and qualitative experiments demonstrate that the proposed model significantly outperforms the existing 24 competitors on three challenging COD benchmark datasets under six widely-used evaluation metrics. Our code is publicly available at https://github.com/ZhouHuang23/FSPNet.

</details>

### 2PCNet: Two-Phase Consistency Training for Day-to-Night Unsupervised Domain Adaptive Object Detection.
- **链接**: [arXiv:2303.13853](https://arxiv.org/abs/2303.13853) · 📚 被引 73
- **作者**: Mikhail Kennerley, Jian-Gang Wang, Bharadwaj Veeravalli, Robby T. Tan
- **🏷️ 机构**: National University of Singapore,Department of Electrical and Computer Engineering, Institute for Infocomm Research, A*STAR
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Object detection at night is a challenging problem due to the absence of night image annotations. Despite several domain adaptation methods, achieving high-precision results remains an issue. False-positive error propagation is still observed in methods using the well-established student-teacher framework, particularly for small-scale and low-light objects. This paper proposes a two-phase consistency unsupervised domain adaptation network, 2PCNet, to address these issues. The network employs high-confidence bounding-box predictions from the teacher in the first phase and appends them to the student's region proposals for the teacher to re-evaluate in the second phase, resulting in a combination of high and low confidence pseudo-labels. The night images and pseudo-labels are scaled-down before being used as input to the student, providing stronger small-scale pseudo-labels. To address errors that arise from low-light regions and other night-related attributes in images, we propose a night-specific augmentation pipeline called NightAug. This pipeline involves applying random augmentations, such as glare, blur, and noise, to daytime images. Experiments on publicly available datasets demonstrate that our method achieves superior results to state-of-the-art methods by 20\%, and to supervised models trained directly on the target data.

</details>

### Region-Aware Pretraining for Open-Vocabulary Object Detection with Vision Transformers.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01072)
- **作者**: Dahun Kim, Anelia Angelova, Weicheng Kuo
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### Discriminative Co-Saliency and Background Mining Transformer for Co-Salient Object Detection.
- **链接**: [arXiv:2305.00514](https://arxiv.org/abs/2305.00514) · [代码](https://github.com/dragonlee258079/DMT) · 📚 被引 42
- **作者**: Long Li, Junwei Han, Ni Zhang, Nian Liu, Salman H. Khan, Hisham Cholakkal et al.
- **🏷️ 机构**: Northwestern Polytechnical University, Mohamed bin Zayed University of Artificial Intelligence
- **会议**: CVPR 2023

### FeatEnHancer: Enhancing Hierarchical Features for Object Detection and Beyond Under Low-Light Vision.
- **链接**: [arXiv:2308.03594](https://arxiv.org/abs/2308.03594) · 📚 被引 93
- **作者**: Khurram Azeem Hashmi, Goutham Kallempudi, Didier Stricker, Muhammad Zeshan Afzal
- **🏷️ 机构**: German Research Center for Artificial Intelligence,DFKI, RPTU Kaiserslautern
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent research on remote sensing object detection has largely focused on improving the representation of oriented bounding boxes but has overlooked the unique prior knowledge presented in remote sensing scenarios. Such prior knowledge can be useful because tiny remote sensing objects may be mistakenly detected without referencing a sufficiently long-range context, and the long-range context required by different types of objects can vary. In this paper, we take these priors into account and propose the Large Selective Kernel Network (LSKNet). LSKNet can dynamically adjust its large spatial receptive field to better model the ranging context of various objects in remote sensing scenarios. To the best of our knowledge, this is the first time that large and selective kernel mechanisms have been explored in the field of remote sensing object detection. Without bells and whistles, LSKNet sets new state-of-the-art scores on standard benchmarks, i.e., HRSC2016 (98.46\% mAP), DOTA-v1.0 (81.85\% mAP) and FAIR1M-v1.0 (47.87\% mAP). Based on a similar technique, we rank 2nd place in 2022 the Greater Bay Area International Algorithm Competition. Code is available at https://github.com/zcablii/Large-Selective-Kernel-Network.

</details>

### DynamicDet: A Unified Dynamic Architecture for Object Detection.
- **链接**: [arXiv:2304.05552](https://arxiv.org/abs/2304.05552) · 📚 被引 53
- **作者**: Zhihao Lin, Yongtao Wang, Jinhe Zhang, Xiaojie Chu
- **🏷️ 机构**: Wangxuan Institute of Computer Technology, Peking University
- **会议**: CVPR 2023

### Hierarchical Supervision and Shuffle Data Augmentation for 3D Semi-Supervised Object Detection.
- **链接**: [arXiv:2304.01464](https://arxiv.org/abs/2304.01464) · 📚 被引 31
- **作者**: Chuandong Liu, Chenqiang Gao, Fangcen Liu, Pengcheng Li, Deyu Meng, Xinbo Gao
- **🏷️ 机构**: School of Communication and Information Engineering, Chongqing University of Posts and Telecommunications,Chongqing,China, Xi&#x0027;an Jiaotong University,Xi&#x0027;an,China
- **会议**: CVPR 2023

### CIGAR: Cross-Modality Graph Reasoning for Domain Adaptive Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02277) · 📚 被引 47
- **作者**: Yabo Liu, Jinghua Wang, Chao Huang, Yaowei Wang, Yong Xu
- **🏷️ 机构**: Harbin Institute of Technology,Shenzhen, School of Cyber Science and Technology, Shenzhen Campus of Sun Yat-sen University, Peng Cheng Laboratory
- **会议**: CVPR 2023

### Ambiguity-Resistant Semi-Supervised Learning for Dense Object Detection.
- **链接**: [arXiv:2303.14960](https://arxiv.org/abs/2303.14960) · [代码](https://github.com/PaddlePaddle/PaddleDetection) · 📚 被引 67
- **作者**: Chang Liu, Weiming Zhang, Xiangru Lin, Wei Zhang, Xiao Tan, Junyu Han et al.
- **🏷️ 机构**: Shanghai University, Baidu Inc
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> With basic Semi-Supervised Object Detection (SSOD) techniques, one-stage detectors generally obtain limited promotions compared with two-stage clusters. We experimentally find that the root lies in two kinds of ambiguities: (1) Selection ambiguity that selected pseudo labels are less accurate, since classification scores cannot properly represent the localization quality. (2) Assignment ambiguity that samples are matched with improper labels in pseudo-label assignment, as the strategy is misguided by missed objects and inaccurate pseudo boxes. To tackle these problems, we propose a Ambiguity-Resistant Semi-supervised Learning (ARSL) for one-stage detectors. Specifically, to alleviate the selection ambiguity, Joint-Confidence Estimation (JCE) is proposed to jointly quantifies the classification and localization quality of pseudo labels. As for the assignment ambiguity, Task-Separation Assignment (TSA) is introduced to assign labels based on pixel-level predictions rather than unreliable pseudo boxes. It employs a "divide-and-conquer" strategy and separately exploits positives for the classification and localization task, which is more robust to the assignment ambiguity. Comprehensive experiments demonstrate that ARSL effectively mitigates the ambiguities and achieves state-of-the-art SSOD performance on MS COCO and PASCAL VOC. Codes can be found at https://github.com/PaddlePaddle/PaddleDetection.

</details>

### MixTeacher: Mining Promising Labels with Mixed Scale Teacher for Semi-Supervised Object Detection.
- **链接**: [arXiv:2303.09061](https://arxiv.org/abs/2303.09061) · [代码](https://github.com/lliuz/MixTeacher) · 📚 被引 58
- **作者**: Liang Liu, Boshen Zhang, Jiangning Zhang, Wuhao Zhang, Zhenye Gan, Guanzhong Tian et al.
- **🏷️ 机构**: Youtu Lab,Tencent, Ningbo Research Institute, Zhejiang University, Rongcheer Co., Ltd
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Scale variation across object instances remains a key challenge in object detection task. Despite the remarkable progress made by modern detection models, this challenge is particularly evident in the semi-supervised case. While existing semi-supervised object detection methods rely on strict conditions to filter high-quality pseudo labels from network predictions, we observe that objects with extreme scale tend to have low confidence, resulting in a lack of positive supervision for these objects. In this paper, we propose a novel framework that addresses the scale variation problem by introducing a mixed scale teacher to improve pseudo label generation and scale-invariant learning. Additionally, we propose mining pseudo labels using score promotion of predictions across scales, which benefits from better predictions from mixed scale features. Our extensive experiments on MS COCO and PASCAL VOC benchmarks under various semi-supervised settings demonstrate that our method achieves new state-of-the-art performance. The code and models are available at \url{https://github.com/lliuz/MixTeacher}.

</details>

### Open-Vocabulary Point-Cloud Object Detection without 3D Annotation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00121)
- **作者**: Yuheng Lu, Chenfeng Xu, Xiaobao Wei, Xiaodong Xie, Masayoshi Tomizuka, Kurt Keutzer et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### Annealing-based Label-Transfer Learning for Open World Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01102) · 📚 被引 34
- **作者**: Yuqing Ma, Hainan Li, Zhange Zhang, Jinyang Guo, Shanghang Zhang, Ruihao Gong et al.
- **🏷️ 机构**: Beihang University,SKLSDE Lab, Institute of Data Space,Hefei Comprehensive National Science Center, Peking University,National Key Laboratory for Multimedia Information Processing
- **会议**: CVPR 2023

### DiGeo: Discriminative Geometry-Aware Learning for Generalized Few-Shot Object Detection.
- **链接**: [arXiv:2303.09674](https://arxiv.org/abs/2303.09674) · 📚 被引 68
- **作者**: Jiawei Ma, Yulei Niu, Jincheng Xu, Shiyuan Huang, Guangxing Han, Shih-Fu Chang
- **🏷️ 机构**: Columbia University
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Current semi-supervised object detection (SSOD) algorithms typically assume class balanced datasets (PASCAL VOC etc.) or slightly class imbalanced datasets (MS-COCO, etc). This assumption can be easily violated since real world datasets can be extremely class imbalanced in nature, thus making the performance of semi-supervised object detectors far from satisfactory. Besides, the research for this problem in SSOD is severely under-explored. To bridge this research gap, we comprehensively study the class imbalance problem for SSOD under more challenging scenarios, thus forming the first experimental setting for class imbalanced SSOD (CI-SSOD). Moreover, we propose a simple yet effective gradient-based sampling framework that tackles the class imbalance problem from the perspective of two types of confirmation biases. To tackle confirmation bias towards majority classes, the gradient-based reweighting and gradient-based thresholding modules leverage the gradients from each class to fully balance the influence of the majority and minority classes. To tackle the confirmation bias from incorrect pseudo labels of minority classes, the class-rebalancing sampling module resamples unlabeled data following the guidance of the gradient-based reweighting module. Experiments on three proposed sub-tasks, namely MS-COCO, MS-COCO to Object365 and LVIS, suggest that our method outperforms current class imbalanced object detectors by clear margins, serving as a baseline for future research in CI-SSOD. Code will be available at https://github.com/nightkeepers/CI-SSOD.

</details>

### Bridging Precision and Confidence: A Train-Time Loss for Calibrating Object Detection.
- **链接**: [arXiv:2303.14404](https://arxiv.org/abs/2303.14404) · [代码](https://github.com/akhtarvision/bpc_calibration) · 📚 被引 18
- **作者**: Muhammad Akhtar Munir, Muhammad Haris Khan, Salman H. Khan, Fahad Shahbaz Khan
- **🏷️ 机构**: Mohamed bin Zayed University of AI
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep neural networks (DNNs) have enabled astounding progress in several vision-based problems. Despite showing high predictive accuracy, recently, several works have revealed that they tend to provide overconfident predictions and thus are poorly calibrated. The majority of the works addressing the miscalibration of DNNs fall under the scope of classification and consider only in-domain predictions. However, there is little to no progress in studying the calibration of DNN-based object detection models, which are central to many vision-based safety-critical applications. In this paper, inspired by the train-time calibration methods, we propose a novel auxiliary loss formulation that explicitly aims to align the class confidence of bounding boxes with the accurateness of predictions (i.e. precision). Since the original formulation of our loss depends on the counts of true positives and false positives in a minibatch, we develop a differentiable proxy of our loss that can be used during training with other application-specific loss functions. We perform extensive experiments on challenging in-domain and out-domain scenarios with six benchmark datasets including MS-COCO, Cityscapes, Sim10k, and BDD100k. Our results reveal that our train-time loss surpasses strong calibration baselines in reducing calibration error for both in and out-domain scenarios. Our source code and pre-trained models are available at https://github.com/akhtarvision/bpc_calibration

</details>

### Multiclass Confidence and Localization Calibration for Object Detection.
- **链接**: [arXiv:2306.08271](https://arxiv.org/abs/2306.08271) · [代码](https://github.com/bimsarapathiraja/MCCL) · 📚 被引 25
- **作者**: Bimsara Pathiraja, Malitha Gunawardhana, Muhammad Haris Khan
- **🏷️ 机构**: Mohamed bin Zayed University of Artificial Intelligence,UAE
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Albeit achieving high predictive accuracy across many challenging computer vision problems, recent studies suggest that deep neural networks (DNNs) tend to make overconfident predictions, rendering them poorly calibrated. Most of the existing attempts for improving DNN calibration are limited to classification tasks and restricted to calibrating in-domain predictions. Surprisingly, very little to no attempts have been made in studying the calibration of object detection methods, which occupy a pivotal space in vision-based security-sensitive, and safety-critical applications. In this paper, we propose a new train-time technique for calibrating modern object detection methods. It is capable of jointly calibrating multiclass confidence and box localization by leveraging their predictive uncertainties. We perform extensive experiments on several in-domain and out-of-domain detection benchmarks. Results demonstrate that our proposed train-time calibration method consistently outperforms several baselines in reducing calibration error for both in-domain and out-of-domain predictions. Our code and models are available at https://github.com/bimsarapathiraja/MCCL.

</details>

### Unbalanced Optimal Transport: A Unified Framework for Object Detection.
- **链接**: [arXiv:2307.02402](https://arxiv.org/abs/2307.02402) · 📚 被引 12
- **作者**: Henri De Plaen, Pierre-François De Plaen, Johan A. K. Suykens, Marc Proesmans, Tinne Tuytelaars, Luc Van Gool
- **🏷️ 机构**: ESAT-STADIUS, KU,Leuven,Belgium, ESAT-PSI, KU,Leuven,Belgium
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The paradigm of large-scale pre-training followed by downstream fine-tuning has been widely employed in various object detection algorithms. In this paper, we reveal discrepancies in data, model, and task between the pre-training and fine-tuning procedure in existing practices, which implicitly limit the detector's performance, generalization ability, and convergence speed. To this end, we propose AlignDet, a unified pre-training framework that can be adapted to various existing detectors to alleviate the discrepancies. AlignDet decouples the pre-training process into two stages, i.e., image-domain and box-domain pre-training. The image-domain pre-training optimizes the detection backbone to capture holistic visual abstraction, and box-domain pre-training learns instance-level semantics and task-aware concepts to initialize the parts out of the backbone. By incorporating the self-supervised pre-trained backbones, we can pre-train all modules for various detectors in an unsupervised paradigm. As depicted in Figure 1, extensive experiments demonstrate that AlignDet can achieve significant improvements across diverse protocols, such as detection algorithm, model backbone, data setting, and training schedule. For example, AlignDet improves FCOS by 5.3 mAP, RetinaNet by 2.1 mAP, Faster R-CNN by 3.3 mAP, and DETR by 2.3 mAP under fewer epochs.

</details>

### Modeling the Distributional Uncertainty for Salient Object Detection Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01883) · 📚 被引 32
- **作者**: Xinyu Tian, Jing Zhang, Mochu Xiang, Yuchao Dai
- **🏷️ 机构**: Northwestern Polytechnical University,China, Australian National University,Australia
- **会议**: CVPR 2023

### Instance Relation Graph Guided Source-Free Domain Adaptive Object Detection.
- **链接**: [arXiv:2203.15793](https://arxiv.org/abs/2203.15793) · 📚 被引 94
- **作者**: Vibashan VS, Poojan Oza, Vishal M. Patel
- **🏷️ 机构**: Johns Hopkins University,Baltimore,MD,USA
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Unsupervised Domain Adaptation (UDA) is an effective approach to tackle the issue of domain shift. Specifically, UDA methods try to align the source and target representations to improve the generalization on the target domain. Further, UDA methods work under the assumption that the source data is accessible during the adaptation process. However, in real-world scenarios, the labelled source data is often restricted due to privacy regulations, data transmission constraints, or proprietary data concerns. The Source-Free Domain Adaptation (SFDA) setting aims to alleviate these concerns by adapting a source-trained model for the target domain without requiring access to the source data. In this paper, we explore the SFDA setting for the task of adaptive object detection. To this end, we propose a novel training strategy for adapting a source-trained object detector to the target domain without source data. More precisely, we design a novel contrastive loss to enhance the target representations by exploiting the objects relations for a given target domain input. These object instance relations are modelled using an Instance Relation Graph (IRG) network, which are then used to guide the contrastive representation learning. In addition, we utilize a student-teacher based knowledge distillation strategy to avoid overfitting to the noisy pseudo-labels generated by the source-trained model. Extensive experiments on multiple object detection benchmark datasets show that the proposed approach is able to efficiently adapt source-trained object detectors to the target domain, outperforming previous state-of-the-art domain adaptive detection methods. Code and models are provided in \href{https://viudomain.github.io/irg-sfda-web/}{https://viudomain.github.io/irg-sfda-web/}.

</details>

### Test Time Adaptation with Regularized Loss for Weakly Supervised Salient Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00711) · 📚 被引 16
- **作者**: Olga Veksler
- **🏷️ 机构**: University of Waterloo,Canada
- **会议**: CVPR 2023

### CLIP the Gap: A Single Domain Generalization Approach for Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00314)
- **作者**: Vidit Vidit, Martin Engilberge, Mathieu Salzmann
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### Learning Transformations to Reduce the Geometric Shift in Object Detection.
- **链接**: [arXiv:2301.05496](https://arxiv.org/abs/2301.05496) · 📚 被引 2
- **作者**: Vidit Vidit, Martin Engilberge, Mathieu Salzmann
- **🏷️ 机构**: EPFL,CVLab
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In incremental learning, replaying stored samples from previous tasks together with current task samples is one of the most efficient approaches to address catastrophic forgetting. However, unlike incremental classification, image replay has not been successfully applied to incremental object detection (IOD). In this paper, we identify the overlooked problem of foreground shift as the main reason for this. Foreground shift only occurs when replaying images of previous tasks and refers to the fact that their background might contain foreground objects of the current task. To overcome this problem, a novel and efficient Augmented Box Replay (ABR) method is developed that only stores and replays foreground objects and thereby circumvents the foreground shift problem. In addition, we propose an innovative Attentive RoI Distillation loss that uses spatial attention from region-of-interest (RoI) features to constrain current model to focus on the most important information from old model. ABR significantly reduces forgetting of previous classes while maintaining high plasticity in current classes. Moreover, it considerably reduces the storage requirements when compared to standard image replay. Comprehensive experiments on Pascal-VOC and COCO datasets support the state-of-the-art performance of our model.

</details>

### Learning to Detect and Segment for Open Vocabulary Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00681)
- **作者**: Tao Wang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### SAFE: Sensitivity-Aware Features for Out-of-Distribution Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.02154) · 📚 被引 36
- **作者**: Samuel Wilson, Tobias Fischer, Feras Dayoub, Dimity Miller, Niko Sünderhauf
- **🏷️ 机构**: Queensland University of Technology,QUT Centre for Robotics, University of Adelaide,Australian Institute for Machine Learning
- **会议**: ICCV 2023

### Consistent-Teacher: Towards Reducing Inconsistent Pseudo-Targets in Semi-Supervised Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00316) · 📚 被引 115
- **作者**: Xinjiang Wang, Xingyi Yang, Shilong Zhang, Yijiang Li, Litong Feng, Shijie Fang et al.
- **🏷️ 机构**: SenseTime Research, National University of Singapore, Shanghai AI Laboratory
- **会议**: CVPR 2023

### Co-Salient Object Detection with Uncertainty-Aware Group Exchange-Masking.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01881) · 📚 被引 24
- **作者**: Yang Wu, Huihui Song, Bo Liu, Kaihua Zhang, Dong Liu
- **🏷️ 机构**: Nanjing University of Information Science and Technology,B-DAT and CICAEET,Nanjing,China, Walmart Global Tech,Sunnyvale,CA,USA,94086, Netflix Inc,Los Gatos,CA,USA,95032
- **会议**: CVPR 2023

### Aligning Bag of Regions for Open-Vocabulary Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01464)
- **作者**: Size Wu, Wenwei Zhang, Sheng Jin, Wentao Liu, Chen Change Loy
- **🏷️ 机构**: NTU S-Lab
- **会议**: CVPR 2023

### LSTFE-Net: Long Short-Term Feature Enhancement Network for Video Small Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01404) · 📚 被引 36
- **作者**: Jinsheng Xiao, Yuanxu Wu, Yunhua Chen, Shurui Wang, Zhongyuan Wang, Jiayi Ma
- **🏷️ 机构**: Wuhan University,China, Guangdong University of Technology,China
- **会议**: CVPR 2023

### Dynamic Coarse-to-Fine Learning for Oriented Tiny Object Detection.
- **链接**: [arXiv:2304.08876](https://arxiv.org/abs/2304.08876) · [代码](https://github.com/Chasel-Tsui/mmrotate-dcfl) · 📚 被引 166
- **作者**: Chang Xu, Jian Ding, Jinwang Wang, Wen Yang, Huai Yu, Lei Yu et al.
- **🏷️ 机构**: School of Electronic Information, Wuhan University, School of Computer Science, Wuhan University
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Detecting arbitrarily oriented tiny objects poses intense challenges to existing detectors, especially for label assignment. Despite the exploration of adaptive label assignment in recent oriented object detectors, the extreme geometry shape and limited feature of oriented tiny objects still induce severe mismatch and imbalance issues. Specifically, the position prior, positive sample feature, and instance are mismatched, and the learning of extreme-shaped objects is biased and unbalanced due to little proper feature supervision. To tackle these issues, we propose a dynamic prior along with the coarse-to-fine assigner, dubbed DCFL. For one thing, we model the prior, label assignment, and object representation all in a dynamic manner to alleviate the mismatch issue. For another, we leverage the coarse prior matching and finer posterior constraint to dynamically assign labels, providing appropriate and relatively balanced supervision for diverse instances. Extensive experiments on six datasets show substantial improvements to the baseline. Notably, we obtain the state-of-the-art performance for one-stage detectors on the DOTA-v1.5, DOTA-v2.0, and DIOR-R datasets under single-scale training and testing. Codes are available at https://github.com/Chasel-Tsui/mmrotate-dcfl.

</details>

### Gaussian Label Distribution Learning for Spherical Image Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00106) · 📚 被引 10
- **作者**: Hang Xu, Xinyuan Liu, Qiang Zhao, Yike Ma, Chenggang Yan, Feng Dai
- **🏷️ 机构**: Hangzhou Dianzi University,Hangzhou,China, Institute of Computing Technology, Chinese Academy of Sciences,Key Laboratory of Intelligent Information Processing of Chinese Academy of Sciences,Beijing,China
- **会议**: CVPR 2023

### DetCLIPv2: Scalable Open-Vocabulary Object Detection Pre-training via Word-Region Alignment.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02250)
- **作者**: Lewei Yao, Jianhua Han, Xiaodan Liang, Dan Xu, Wei Zhang, Zhenguo Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### Object Detection with Self-Supervised Scene Adaptation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02068)
- **作者**: Zekun Zhang, Minh Hoai
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### Dense Distinct Query for End-to-End Object Detection.
- **链接**: [arXiv:2303.12776](https://arxiv.org/abs/2303.12776) · [代码](https://github.com/jshilong/DDQ) · 📚 被引 311
- **作者**: Shilong Zhang, Xinjiang Wang, Jiaqi Wang, Jiangmiao Pang, Chengqi Lyu, Wenwei Zhang et al.
- **🏷️ 机构**: Shanghai AI Laboratory, SenseTime Research, The University of Hong Kong
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> One-to-one label assignment in object detection has successfully obviated the need for non-maximum suppression (NMS) as postprocessing and makes the pipeline end-to-end. However, it triggers a new dilemma as the widely used sparse queries cannot guarantee a high recall, while dense queries inevitably bring more similar queries and encounter optimization difficulties. As both sparse and dense queries are problematic, then what are the expected queries in end-to-end object detection? This paper shows that the solution should be Dense Distinct Queries (DDQ). Concretely, we first lay dense queries like traditional detectors and then select distinct ones for one-to-one assignments. DDQ blends the advantages of traditional and recent end-to-end detectors and significantly improves the performance of various detectors including FCN, R-CNN, and DETRs. Most impressively, DDQ-DETR achieves 52.1 AP on MS-COCO dataset within 12 epochs using a ResNet-50 backbone, outperforming all existing detectors in the same setting. DDQ also shares the benefit of end-to-end detectors in crowded scenes and achieves 93.8 AP on CrowdHuman. We hope DDQ can inspire researchers to consider the complementarity between traditional methods and end-to-end detectors. The source code can be found at \url{https://github.com/jshilong/DDQ}.

</details>

### Towards Unsupervised Object Detection from LiDAR Point Clouds.
- **链接**: [arXiv:2311.02007](https://arxiv.org/abs/2311.02007) · 📚 被引 39
- **作者**: Lunjun Zhang, Anqi Joyce Yang, Yuwen Xiong, Sergio Casas, Bin Yang, Mengye Ren et al.
- **🏷️ 机构**: Waabi, University of Toronto
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we study the problem of unsupervised object detection from 3D point clouds in self-driving scenes. We present a simple yet effective method that exploits (i) point clustering in near-range areas where the point clouds are dense, (ii) temporal consistency to filter out noisy unsupervised detections, (iii) translation equivariance of CNNs to extend the auto-labels to long range, and (iv) self-supervision for improving on its own. Our approach, OYSTER (Object Discovery via Spatio-Temporal Refinement), does not impose constraints on data collection (such as repeated traversals of the same location), is able to detect objects in a zero-shot manner without supervised finetuning (even in sparse, distant regions), and continues to self-improve given more rounds of iterative self-training. To better measure model performance in self-driving scenarios, we propose a new planning-centric perception metric based on distance-to-collision. We demonstrate that our unsupervised object detector significantly outperforms unsupervised baselines on PandaSet and Argoverse 2 Sensor dataset, showing promise that self-supervision combined with object priors can enable object discovery in the wild. For more information, visit the project website: https://waabi.ai/research/oyster

</details>

### Class-aware Memory Guided Unbiased Weighting for Universal Domain Adaptive Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00469) · 📚 被引 2
- **作者**: Qinghai Lang, Zhenwei He, Xiaowei Fu, Lei Zhang
- **🏷️ 机构**: Chongqing University,School of Microelectronics and Communication Engineering,China
- **会议**: ICCV 2023

### Self-training and multi-task learning for limited data: evaluation study on object detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00107) · 📚 被引 1
- **作者**: Hoàng-Ân Lê, Minh-Tan Pham
- **🏷️ 机构**: Universit&#x00E9; Bretagne Sud, UMR 6074,IRISA,Vannes,France,56000
- **会议**: ICCV 2023

### DetOFA: Efficient Training of Once-for-All Networks for Object Detection using Path Filter.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00143) · 📚 被引 3
- **作者**: Yuiko Sakuma, Masato Ishii, Takuya Narihira
- **🏷️ 机构**: Sony Group Corporation,Tokyo,Japan
- **会议**: ICCV 2023

### Identification of Novel Classes for Improving Few-Shot Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00360)
- **作者**: Zeyu Shangguan, Mohammad Rostami
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### InterAug: A Tuning-Free Augmentation Policy for Data-Efficient and Robust Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00033) · 📚 被引 0
- **作者**: Kowshik Thopalli, Devi S, Jayaraman J. Thiagarajan
- **🏷️ 机构**: Lawrence Livermore National Labs,USA, SRM Institute of Science and Technology,India
- **会议**: ICCV 2023

### Fast Object Detection in High-Resolution Videos.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00159) · 📚 被引 0
- **作者**: Ryan Tran, Atul Kanaujia, Vasu Parameswaran
- **🏷️ 机构**: Percipient.ai,Santa Clara,CA
- **会议**: ICCV 2023

### Adaptive Self-Training for Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00098)
- **作者**: Renaud Vandeghen, Gilles Louppe, Marc Van Droogenbroeck
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### Comparative Study of Natural Replay and Experience Replay in Online Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00386) · 📚 被引 0
- **作者**: Baptiste Wagner, Denis Pellerin, Sylvain Huet
- **🏷️ 机构**: Univ. Grenoble Alpes,CNRS, Grenoble INP, GIPSA-lab,Grenoble,France,38000
- **会议**: ICCV 2023

### Prototypical Variational Autoencoder for 3D Few-shot Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/076a93fd42aa85f5ccee921a01d77dd5-Abstract-Conference.html) · 📚 被引 0
- **作者**: Weiliang Tang, Biqi Yang, Xianzhi Li, Yun-Hui Liu, Pheng-Ann Heng, Chi-Wing Fu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we study the problem of unsupervised object detection from 3D point clouds in self-driving scenes. We present a simple yet effective method that exploits (i) point clustering in near-range areas where the point clouds are dense, (ii) temporal consistency to filter out noisy unsupervised detections, (iii) translation equivariance of CNNs to extend the auto-labels to long range, and (iv) self-supervision for improving on its own. Our approach, OYSTER (Object Discovery via Spatio-Temporal Refinement), does not impose constraints on data collection (such as repeated traversals of the same location), is able to detect objects in a zero-shot manner without supervised finetuning (even in sparse, distant regions), and continues to self-improve given more rounds of iterative self-training. To better measure model performance in self-driving scenarios, we propose a new planning-centric perception metric based on distance-to-collision. We demonstrate that our unsupervised object detector significantly outperforms unsupervised baselines on PandaSet and Argoverse 2 Sensor dataset, showing promise that self-supervision combined with object priors can enable object discovery in the wild. For more information, visit the project website: https://waabi.ai/research/oyster

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Object detection via inaccurate bounding boxes supervision has boosted a broad interest due to the expensive high-quality annotation data or the occasional inevitability of low annotation quality (\eg tiny objects). The previous works usually utilize multiple instance learning (MIL), which highly depends on category information, to select and refine a low-quality box. Those methods suffer from object drift, group prediction and part domination problems without exploring spatial information. In this paper, we heuristically propose a \textbf{Spatial Self-Distillation based Object Detector (SSD-Det)} to mine spatial information to refine the inaccurate box in a self-distillation fashion. SSD-Det utilizes a Spatial Position Self-Distillation \textbf{(SPSD)} module to exploit spatial information and an interactive structure to combine spatial information and category information, thus constructing a high-quality proposal bag. To further improve the selection procedure, a Spatial Identity Self-Distillation \textbf{(SISD)} module is introduced in SSD-Det to obtain spatial confidence to help select the best proposals. Experiments on MS-COCO and VOC datasets with noisy box annotation verify our method's effectiveness and achieve state-of-the-art performance. The code is available at https://github.com/ucas-vg/PointTinyBenchmark/tree/SSD-Det.

</details>

### Bridging Cross-task Protocol Inconsistency for Distillation in Dense Object Detection.
- **链接**: [arXiv:2308.14286](https://arxiv.org/abs/2308.14286) · [代码](https://github.com/TinyTigerPan/BCKD) · 📚 被引 68
- **作者**: Longrong Yang, Xianpan Zhou, Xuewei Li, Liang Qiao, Zheyang Li, Ziwei Yang et al.
- **🏷️ 机构**: Zhejiang University,College of Computer Science &#x0026; Technology, Zhejiang University,Polytechnic Institute, Hikvision Research Institute
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Knowledge distillation (KD) has shown potential for learning compact models in dense object detection. However, the commonly used softmax-based distillation ignores the absolute classification scores for individual categories. Thus, the optimum of the distillation loss does not necessarily lead to the optimal student classification scores for dense object detectors. This cross-task protocol inconsistency is critical, especially for dense object detectors, since the foreground categories are extremely imbalanced. To address the issue of protocol differences between distillation and classification, we propose a novel distillation method with cross-task consistent protocols, tailored for the dense object detection. For classification distillation, we address the cross-task protocol inconsistency problem by formulating the classification logit maps in both teacher and student models as multiple binary-classification maps and applying a binary-classification distillation loss to each map. For localization distillation, we design an IoU-based Localization Distillation Loss that is free from specific network structures and can be compared with existing localization distillation losses. Our proposed method is simple but effective, and experimental results demonstrate its superiority over existing methods. Code is available at https://github.com/TinyTigerPan/BCKD.

</details>

### Cyclic-Bootstrap Labeling for Weakly Supervised Object Detection.
- **链接**: [arXiv:2308.05991](https://arxiv.org/abs/2308.05991) · [代码](https://github.com/Yinyf0804/WSOD-CBL) · 📚 被引 17
- **作者**: Yufei Yin, Jiajun Deng, Wengang Zhou, Li Li, Houqiang Li
- **🏷️ 机构**: University of Science and Technology of China,CAS Key Laboratory of Technology in GIPAS,EEIS Department, The University of Sydney
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent progress in weakly supervised object detection is featured by a combination of multiple instance detection networks (MIDN) and ordinal online refinement. However, with only image-level annotation, MIDN inevitably assigns high scores to some unexpected region proposals when generating pseudo labels. These inaccurate high-scoring region proposals will mislead the training of subsequent refinement modules and thus hamper the detection performance. In this work, we explore how to ameliorate the quality of pseudo-labeling in MIDN. Formally, we devise Cyclic-Bootstrap Labeling (CBL), a novel weakly supervised object detection pipeline, which optimizes MIDN with rank information from a reliable teacher network. Specifically, we obtain this teacher network by introducing a weighted exponential moving average strategy to take advantage of various refinement modules. A novel class-specific ranking distillation algorithm is proposed to leverage the output of weighted ensembled teacher network for distilling MIDN with rank information. As a result, MIDN is guided to assign higher scores to accurate proposals among their neighboring ones, thus benefiting the subsequent pseudo labeling. Extensive experiments on the prevalent PASCAL VOC 2007 \& 2012 and COCO datasets demonstrate the superior performance of our CBL framework. Code will be available at https://github.com/Yinyf0804/WSOD-CBL/.

</details>

### Small Object Detection via Coarse-to-fine Proposal Generation and Imitation Learning.
- **链接**: [arXiv:2308.09534](https://arxiv.org/abs/2308.09534) · 📚 被引 135
- **作者**: Xiang Yuan, Gong Cheng, Kebing Yan, Qinghua Zeng, Junwei Han
- **🏷️ 机构**: Northwestern Polytechnical University,School of Automation,Xi&#x2019;an,China
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The past few years have witnessed the immense success of object detection, while current excellent detectors struggle on tackling size-limited instances. Concretely, the well-known challenge of low overlaps between the priors and object regions leads to a constrained sample pool for optimization, and the paucity of discriminative information further aggravates the recognition. To alleviate the aforementioned issues, we propose CFINet, a two-stage framework tailored for small object detection based on the Coarse-to-fine pipeline and Feature Imitation learning. Firstly, we introduce Coarse-to-fine RPN (CRPN) to ensure sufficient and high-quality proposals for small objects through the dynamic anchor selection strategy and cascade regression. Then, we equip the conventional detection head with a Feature Imitation (FI) branch to facilitate the region representations of size-limited instances that perplex the model in an imitation manner. Moreover, an auxiliary imitation loss following supervised contrastive learning paradigm is devised to optimize this branch. When integrated with Faster RCNN, CFINet achieves state-of-the-art performance on the large-scale small object detection benchmarks, SODA-D and SODA-A, underscoring its superiority over baseline detector and other mainstream detection approaches.

</details>

### A Dynamic Dual-Processing Object Detection Framework Inspired by the Brain's Recognition Mechanism.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00576) · 📚 被引 3
- **作者**: Minying Zhang, Tianpeng Bu, Lulu Hu
- **🏷️ 机构**: Alibaba Group,Hangzhou,China
- **会议**: ICCV 2023

### RecursiveDet: End-to-End Region-based Recursive Object Detection.
- **链接**: [arXiv:2307.13619](https://arxiv.org/abs/2307.13619) · [代码](https://github.com/bravezzzzzz/RecursiveDet) · 📚 被引 7
- **作者**: Jing Zhao, Li Sun, Qingli Li
- **🏷️ 机构**: East China Normal University,Shanghai Key Laboratory of Multidimensional Information Processing,Shanghai,China
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> End-to-end region-based object detectors like Sparse R-CNN usually have multiple cascade bounding box decoding stages, which refine the current predictions according to their previous results. Model parameters within each stage are independent, evolving a huge cost. In this paper, we find the general setting of decoding stages is actually redundant. By simply sharing parameters and making a recursive decoder, the detector already obtains a significant improvement. The recursive decoder can be further enhanced by positional encoding (PE) of the proposal box, which makes it aware of the exact locations and sizes of input bounding boxes, thus becoming adaptive to proposals from different stages during the recursion. Moreover, we also design centerness-based PE to distinguish the RoI feature element and dynamic convolution kernels at different positions within the bounding box. To validate the effectiveness of the proposed method, we conduct intensive ablations and build the full model on three recent mainstream region-based detectors. The RecusiveDet is able to achieve obvious performance boosts with even fewer model parameters and slightly increased computation cost. Codes are available at https://github.com/bravezzzzzz/RecursiveDet.

</details>

### Class-aware Memory Guided Unbiased Weighting for Universal Domain Adaptive Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00469) · 📚 被引 2
- **作者**: Qinghai Lang, Zhenwei He, Xiaowei Fu, Lei Zhang
- **🏷️ 机构**: Chongqing University,School of Microelectronics and Communication Engineering,China
- **会议**: ICCV 2023

### Self-training and multi-task learning for limited data: evaluation study on object detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00107) · 📚 被引 1
- **作者**: Hoàng-Ân Lê, Minh-Tan Pham
- **🏷️ 机构**: Universit&#x00E9; Bretagne Sud, UMR 6074,IRISA,Vannes,France,56000
- **会议**: ICCV 2023

### DetOFA: Efficient Training of Once-for-All Networks for Object Detection using Path Filter.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00143) · 📚 被引 3
- **作者**: Yuiko Sakuma, Masato Ishii, Takuya Narihira
- **🏷️ 机构**: Sony Group Corporation,Tokyo,Japan
- **会议**: ICCV 2023

### Identification of Novel Classes for Improving Few-Shot Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00360)
- **作者**: Zeyu Shangguan, Mohammad Rostami
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Long-tailed object detection (LTOD) aims to handle the extreme data imbalance in real-world datasets, where many tail classes have scarce instances. One popular strategy is to explore extra data with image-level labels, yet it produces limited results due to (1) semantic ambiguity -- an image-level label only captures a salient part of the image, ignoring the remaining rich semantics within the image; and (2) location sensitivity -- the label highly depends on the locations and crops of the original image, which may change after data transformations like random cropping. To remedy this, we propose RichSem, a simple but effective method, which is robust to learn rich semantics from coarse locations without the need of accurate bounding boxes. RichSem leverages rich semantics from images, which are then served as additional soft supervision for training detectors. Specifically, we add a semantic branch to our detector to learn these soft semantics and enhance feature representations for long-tailed object detection. The semantic branch is only used for training and is removed during inference. RichSem achieves consistent improvements on both overall and rare-category of LVIS under different backbones and detectors. Our method achieves state-of-the-art performance without requiring complex training and testing procedures. Moreover, we show the effectiveness of our method on other long-tailed datasets with additional experiments. Code is available at \url{https://github.com/MengLcool/RichSem}.

</details>

### Scaling Open-Vocabulary Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/e6d58fc68c0f3c36ae6e0e64478a69c0-Abstract-Conference.html)
- **作者**: Matthias Minderer, Alexey A. Gritsenko, Neil Houlsby
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Django: Detecting Trojans in Object Detection Models via Gaussian Focus Calibration.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/a102d6cb996be3482c059c1e18bbe523-Abstract-Conference.html) · 📚 被引 4
- **作者**: Guangyu Shen, Siyuan Cheng, Guanhong Tao, Kaiyuan Zhang, Yingqi Liu, Shengwei An et al.
- **🏷️ 机构**: MEGVII
- **会议**: NeurIPS 2023

### Introspection of 2D Object Detection using Processed Neural Activation Patterns in Automated Driving Systems.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00437) · 📚 被引 3
- **作者**: Hakan Yekta Yatbaz, Mehrdad Dianati, Konstantinos Koufos, Roger Woodman
- **🏷️ 机构**: University of Warwick,WMG
- **会议**: ICCV 2023

## 跨领域论文（完整笔记在其他领域）

- Omni3D: A Large Benchmark and Model for 3D Object Detection in the Wild. → [3d-detection](../3d-detection/Guideline%202023.md)
- ConQueR: Query Contrast Voxel-DETR for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- AShapeFormer : Semantics-Guided Object-Level Active Shape Encoding for 3D Object Detection via Transformers. → [3d-detection](../3d-detection/Guideline%202023.md)
- Viewpoint Equivariance for Multi-View 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- VoxelNeXt: Fully Sparse VoxelNet for 3D Object Detection and Tracking. → [3d-detection](../3d-detection/Guideline%202023.md)
- PiMAE: Point Cloud and Image Interactive Masked Autoencoders for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- BEV-SAN: Accurate BEV 3D Object Detection via Slice Attention Networks. → [3d-detection](../3d-detection/Guideline%202023.md)
- itKD: Interchange Transfer-based Knowledge Distillation for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Benchmarking Robustness of 3D Object Detection to Common Corruptions in Autonomous Driving. → [3d-detection](../3d-detection/Guideline%202023.md)
- AeDet: Azimuth-Invariant Multi-View 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- MSF: Motion-guided Sequential Fusion for Efficient 3D Object Detection from Point Cloud Sequences. → [3d-detection](../3d-detection/Guideline%202023.md)
- Density-Insensitive Unsupervised Domain Adaption on 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- MSMDFusion: Fusing LiDAR and Camera at Multiple Scales with Multi-Depth Seeds for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- X3KD: Knowledge Distillation Across Modalities, Tasks and Stages for Multi-Camera 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- LoGoNet: Towards Accurate 3D Object Detection with Local-to-Global Cross- Modal Fusion. → [3d-detection](../3d-detection/Guideline%202023.md)
- PillarNeXt: Rethinking Network Designs for 3D Object Detection in LiDAR Point Clouds. → [3d-detection](../3d-detection/Guideline%202023.md)
- MoDAR: Using Motion Forecasting for 3D Object Detection in Point Cloud Sequences. → [3d-detection](../3d-detection/Guideline%202023.md)
- Deep Dive into Gradients: Better Optimization for 3D Object Detection with Gradient-Corrected IoU Supervision. → [3d-detection](../3d-detection/Guideline%202023.md)
- Weakly Supervised Monocular 3D Object Detection Using Multi-View Projection and Direction Consistency. → [3d-detection](../3d-detection/Guideline%202023.md)
- Towards Domain Generalization for Multi-view 3D Object Detection in Bird-Eye-View. → [3d-detection](../3d-detection/Guideline%202023.md)
- Semi-Supervised Stereo-Based 3D Object Detection via Cross-View Consensus. → [3d-detection](../3d-detection/Guideline%202023.md)
- Virtual Sparse Convolution for Multimodal 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- CAPE: Camera View Position Embedding for Multi-View 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Multi-view Adversarial Discriminator: Mine the Non-causal Factors for Object Detection in Unseen Domains. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- BEVHeight: A Robust Framework for Vision-based Roadside 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Bi3D: Bi-Domain Active Learning for Cross-Domain 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Distilling Focal Knowledge from Imperfect Expert for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Uni3D: A Unified Baseline for Multi-Dataset 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- OcTr: Octree-Based Transformer for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- UniDistill: A Universal Cross-Modality Knowledge Distillation Framework for 3D Object Detection in Bird's-Eye View. → [3d-detection](../3d-detection/Guideline%202023.md)
- MonoATT: Online Monocular 3D Object Detection with Adaptive Token Transformer. → [3d-detection](../3d-detection/Guideline%202023.md)
- Understanding the Robustness of 3D Object Detection with Bird'View Representations in Autonomous Driving. → [3d-detection](../3d-detection/Guideline%202023.md)

## 🆕 增量新增

### Semi-DETR: Semi-Supervised Object Detection with Detection Transformers. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2307.08095](https://arxiv.org/abs/2307.08095) · 📚 被引 78
- **作者**: Jiacheng Zhang, Xiangru Lin, Wei Zhang, Kuo Wang, Xiao Tan, Junyu Han et al.
- **🏷️ 机构**: School of Computer Science and Engineering, Sun Yat-sen University,Guangzhou,China, Baidu Inc.,Department of Computer Vision Technology (VIS),China
- **会议**: CVPR 2023
- **摘要（中）**: 针对DETR框架在半监督目标检测中的两个问题：一对一匹配在不准确伪标签下导致训练效率低下，以及查询与预测间缺乏确定性对应关系，限制了基于一致性的正则化方法。提出了Semi-DETR，首个基于Transformer的端到端半监督检测器，包含阶段式混合匹配策略结合一对多和一对一分配，以及跨视图查询一致性方法学习语义特征不变性，并引入基于代价的伪标签挖掘模块。相比现有SSOD方法，有效提升了训练效率和伪标签质量，在COCO等基准上取得了显著性能提升。
- **摘要（英）**: This paper addresses two issues in DETR-based semi-supervised object detection: inefficient training due to one-to-one assignment with inaccurate pseudo labels, and lack of deterministic query-prediction correspondence hindering consistency regularization. It proposes Semi-DETR, the first transformer-based end-to-end semi-supervised detector, with a stage-wise hybrid matching strategy, cross-view query consistency, and cost-based pseudo label mining. These innovations improve training efficiency and pseudo label quality, achieving significant performance gains on benchmarks like COCO.
- **核心贡献**: 首个针对DETR框架的半监督目标检测方法，解决了匹配和一致性问题。
- **创新点**: 提出阶段式混合匹配和跨视图查询一致性机制。
- **结果**: 在COCO等数据集上显著提升半监督检测性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We analyze the DETR-based framework on semi-supervised object detection (SSOD) and observe that (1) the one-to-one assignment strategy generates incorrect matching when the pseudo ground-truth bounding box is inaccurate, leading to training inefficiency; (2) DETR-based detectors lack deterministic correspondence between the input query and its prediction output, which hinders the applicability of the consistency-based regularization widely used in current SSOD methods. We present Semi-DETR, the first transformer-based end-to-end semi-supervised object detector, to tackle these problems. Specifically, we propose a Stage-wise Hybrid Matching strategy that combines the one-to-many assignment and one-to-one assignment strategies to improve the training efficiency of the first stage and thus provide high-quality pseudo labels for the training of the second stage. Besides, we introduce a Crossview Query Consistency method to learn the semantic feature invariance of object queries from different views while avoiding the need to find deterministic query correspondence. Furthermore, we propose a Cost-based Pseudo Label Mining module to dynamically mine more pseudo boxes based on the matching cost of pseudo ground truth bounding boxes for consistency training. Extensive experiments on all SSOD settings of both COCO and Pascal VOC benchmark datasets show that our Semi-DETR method outperforms all state-of-the-art methods by clear margins. The PaddlePaddle version code1 is at https://github.com/PaddlePaddle/PaddleDetection/tree/develop/configs/semi_det/semi_detr.

</details>

### Mask DINO: Towards A Unified Transformer-based Framework for Object Detection and Segmentation. **⭐⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00297) · 📚 被引 494
- **作者**: Feng Li, Hao Zhang, Huaizhe Xu, Shilong Liu, Lei Zhang, Lionel M. Ni et al.
- **🏷️ 机构**: The Hong Kong University of Science and Technology, Institute for AI, Tsinghua University,BNRist Center,Dept. of CST., International Digital Economy Academy (IDEA)
- **会议**: CVPR 2023
- **摘要（中）**: 针对目标检测和分割任务分离的问题，提出了Mask DINO，一个统一的基于Transformer的框架，将检测和分割任务整合到同一模型中。通过扩展DINO的查询机制，支持掩码预测，并利用统一的损失函数联合优化。相比已有方法，Mask DINO在COCO和ADE20K等基准上同时取得了检测和分割的领先性能，展示了统一模型的优势。
- **摘要（英）**: This paper addresses the separation of object detection and segmentation tasks by proposing Mask DINO, a unified transformer-based framework that integrates both tasks into one model. It extends DINO's query mechanism to support mask prediction and uses a unified loss for joint optimization. Mask DINO achieves state-of-the-art performance on both detection and segmentation benchmarks like COCO and ADE20K, demonstrating the benefit of unification.
- **核心贡献**: 提出了统一的检测与分割Transformer框架。
- **创新点**: 扩展查询机制以支持掩码预测和联合优化。
- **结果**: 在多个基准上取得领先性能。

### DETR with Additional Global Aggregation for Cross-domain Weakly Supervised Object Detection. **⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2304.07082](https://arxiv.org/abs/2304.07082) · 📚 被引 15
- **作者**: Zongheng Tang, Yifan Sun, Si Liu, Yi Yang
- **🏷️ 机构**: Institute of Artificial Intelligence, Beihang University, Baidu Inc, CCAI, Zhejiang University
- **会议**: CVPR 2023
- **摘要（中）**: 针对跨域弱监督目标检测中域适应困难的问题，提出了DETR-GA，一种基于DETR的检测器，通过额外的全局聚合机制实现图像级预测，利用弱监督进行域对齐。在编码器和解码器中分别添加类查询和前景查询，聚合语义信息。相比已有方法，DETR-GA能有效利用弱监督信息，在跨域场景中提升检测性能。
- **摘要（英）**: This paper addresses cross-domain weakly supervised object detection by proposing DETR-GA, a DETR-based detector with additional global aggregation for image-level predictions, leveraging weak supervision for domain alignment. It adds class queries in the encoder and a foreground query in the decoder to aggregate semantics. DETR-GA effectively utilizes weak supervision, improving detection performance in cross-domain scenarios.
- **核心贡献**: 提出基于全局聚合的DETR跨域弱监督检测方法。
- **创新点**: 利用查询聚合实现图像级预测和域对齐。
- **结果**: 在跨域检测任务中取得性能提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper presents a DETR-based method for cross-domain weakly supervised object detection (CDWSOD), aiming at adapting the detector from source to target domain through weak supervision. We think DETR has strong potential for CDWSOD due to an insight: the encoder and the decoder in DETR are both based on the attention mechanism and are thus capable of aggregating semantics across the entire image. The aggregation results, i.e., image-level predictions, can naturally exploit the weak supervision for domain alignment. Such motivated, we propose DETR with additional Global Aggregation (DETR-GA), a CDWSOD detector that simultaneously makes "instance-level + image-level" predictions and utilizes "strong + weak" supervisions. The key point of DETR-GA is very simple: for the encoder / decoder, we respectively add multiple class queries / a foreground query to aggregate the semantics into image-level predictions. Our query-based aggregation has two advantages. First, in the encoder, the weakly-supervised class queries are capable of roughly locating the corresponding positions and excluding the distraction from non-relevant regions. Second, through our design, the object queries and the foreground query in the decoder share consensus on the class semantics, therefore making the strong and weak supervision mutually benefit each other for domain alignment. Extensive experiments on four popular cross-domain benchmarks show that DETR-GA significantly improves CSWSOD and advances the states of the art (e.g., 29.0% --> 79.4% mAP on PASCAL VOC --> Clipart_all dataset).

</details>

### Toward RAW Object Detection: A New Benchmark and A New Model. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01286) · 📚 被引 31
- **作者**: Ruikang Xu, Chang Chen, Jingyang Peng, Cheng Li, Yibin Huang, Fenglong Song et al.
- **🏷️ 机构**: University of Science and Technology of China, Huawei Noah&#x0027;s Ark Lab
- **会议**: CVPR 2023
- **摘要（中）**: 针对现有目标检测依赖sRGB图像而忽略RAW图像信息的问题，提出了一个新的RAW目标检测基准和模型。该模型直接处理RAW传感器数据，利用原始图像的高动态范围和低光照优势，提升检测鲁棒性。相比传统方法，在低光等挑战性条件下取得了显著性能提升。
- **摘要（英）**: This paper addresses the reliance of object detection on sRGB images, ignoring RAW sensor data, by introducing a new benchmark and model for RAW object detection. The model processes RAW data directly, leveraging high dynamic range and low-light advantages for improved robustness. It achieves significant performance gains in challenging conditions like low light.
- **核心贡献**: 构建了RAW检测基准并提出了直接处理RAW数据的模型。
- **创新点**: 利用RAW图像特性提升检测鲁棒性。
- **结果**: 在低光条件下取得显著性能提升。

### ConQueR: Query Contrast Voxel-DETR for 3D Object Detection. **⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2212.07289](https://arxiv.org/abs/2212.07289) · 📚 被引 30
- **作者**: Benjin Zhu, Zhe Wang, Shaoshuai Shi, Hang Xu, Lanqing Hong, Hongsheng Li
- **🏷️ 机构**: The Chinese University of Hong Kong,Multimedia Laboratory, Max Planck Institute for Informatics, Huawei Noah&#x0027;s Ark Lab
- **会议**: CVPR 2023
- **摘要（中）**: 针对DETR-based 3D检测器中大量查询导致假阳性问题，提出了ConQueR，一种基于查询对比的稀疏3D检测器。通过查询对比机制，显式增强查询与其最佳匹配GT的区分度，构建正负GT-查询对并应用对比损失。相比已有方法，ConQueR减少了约60%的假阳性，缩小了稀疏与密集检测器的性能差距。
- **摘要（英）**: This paper addresses the false positive issue in DETR-based 3D detectors caused by excessive queries, proposing ConQueR, a sparse 3D detector with a query contrast mechanism. It explicitly enhances queries towards best-matched GTs using contrastive loss with positive and negative pairs. ConQueR reduces false positives by up to 60%, closing the gap with dense detectors.
- **核心贡献**: 提出了查询对比机制以消除3D检测中的假阳性。
- **创新点**: 利用对比学习增强查询与GT的匹配。
- **结果**: 减少约60%假阳性，性能接近密集检测器。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Although DETR-based 3D detectors can simplify the detection pipeline and achieve direct sparse predictions, their performance still lags behind dense detectors with post-processing for 3D object detection from point clouds. DETRs usually adopt a larger number of queries than GTs (e.g., 300 queries v.s. 40 objects in Waymo) in a scene, which inevitably incur many false positives during inference. In this paper, we propose a simple yet effective sparse 3D detector, named Query Contrast Voxel-DETR (ConQueR), to eliminate the challenging false positives, and achieve more accurate and sparser predictions. We observe that most false positives are highly overlapping in local regions, caused by the lack of explicit supervision to discriminate locally similar queries. We thus propose a Query Contrast mechanism to explicitly enhance queries towards their best-matched GTs over all unmatched query predictions. This is achieved by the construction of positive and negative GT-query pairs for each GT, and a contrastive loss to enhance positive GT-query pairs against negative ones based on feature similarities. ConQueR closes the gap of sparse and dense 3D detectors, and reduces up to ~60% false positives. Our single-frame ConQueR achieves new state-of-the-art (sota) 71.6 mAPH/L2 on the challenging Waymo Open Dataset validation set, outperforming previous sota methods (e.g., PV-RCNN++) by over 2.0 mAPH/L2.

</details>

### Cascade-DETR: Delving into High-Quality Universal Object Detection. **⭐⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2307.11035](https://arxiv.org/abs/2307.11035) · 📚 被引 54
- **作者**: Mingqiao Ye, Lei Ke, Siyuan Li, Yu-Wing Tai, Chi-Keung Tang, Martin Danelljan et al.
- **🏷️ 机构**: ETH Z&#x00FC;rich, Dartmouth College, HKUST
- **会议**: ICCV 2023
- **摘要（中）**: 针对Transformer检测器在多样化领域泛化能力弱和定位精度不足的问题，该论文提出Cascade-DETR，通过级联注意力层将目标中心信息集成到解码器，限制注意力于先前框预测，提升定位精度。同时，用预测IoU替代分类分数作为查询置信度，使置信度更校准。引入包含10个多样化数据集的UDB10基准，实验表明Cascade-DETR在COCO上提升SOTA，并在UDB10所有数据集上显著优于DETR基线，部分提升超10 mAP。
- **摘要（英）**: This paper proposes Cascade-DETR for high-quality universal object detection, using cascade attention and IoU prediction to improve localization and calibration. It introduces the UDB10 benchmark and achieves SOTA on COCO while substantially improving DETR on all UDB10 datasets, with gains over 10 mAP in some cases.
- **核心贡献**: 提出级联注意力机制和IoU预测策略，并构建UDB10多域检测基准。
- **创新点**: 级联注意力限制于先前框预测，提升定位精度。
- **结果**: 在COCO和UDB10上均取得显著性能提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Object localization in general environments is a fundamental part of vision systems. While dominating on the COCO benchmark, recent Transformer-based detection methods are not competitive in diverse domains. Moreover, these methods still struggle to very accurately estimate the object bounding boxes in complex environments. We introduce Cascade-DETR for high-quality universal object detection. We jointly tackle the generalization to diverse domains and localization accuracy by proposing the Cascade Attention layer, which explicitly integrates object-centric information into the detection decoder by limiting the attention to the previous box prediction. To further enhance accuracy, we also revisit the scoring of queries. Instead of relying on classification scores, we predict the expected IoU of the query, leading to substantially more well-calibrated confidences. Lastly, we introduce a universal object detection benchmark, UDB10, that contains 10 datasets from diverse domains. While also advancing the state-of-the-art on COCO, Cascade-DETR substantially improves DETR-based detectors on all datasets in UDB10, even by over 10 mAP in some cases. The improvements under stringent quality requirements are even more pronounced. Our code and models will be released at https://github.com/SysCV/cascade-detr.

</details>

### Decoupled DETR: Spatially Disentangling Localization and Classification for Improved End-to-End Object Detection. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2310.15955](https://arxiv.org/abs/2310.15955) · 📚 被引 28
- **作者**: Manyuan Zhang, Guanglu Song, Yu Liu, Hongsheng Li
- **🏷️ 机构**: The Chinese University of HongKong,Multimedia Laboratory, SenseTime Research
- **会议**: ICCV 2023
- **摘要（中）**: 针对DETR中分类和定位任务在空间上耦合导致优化冲突的问题，该论文提出解耦DETR，将定位和分类在空间上分离。方法通过设计解耦注意力机制，使分类和回归分支关注不同区域，减少任务冲突。相比标准DETR，该方法在保持端到端简洁性的同时，提升了检测精度和收敛速度。在COCO基准上取得了优于现有DETR变体的性能。
- **摘要（英）**: This paper proposes Decoupled DETR to spatially disentangle localization and classification, reducing task conflicts in DETR. The method improves accuracy and convergence speed while maintaining end-to-end simplicity, achieving superior performance on COCO.
- **核心贡献**: 提出空间解耦的DETR架构，分离定位和分类任务。
- **创新点**: 解耦注意力机制使分类和回归关注不同空间区域。
- **结果**: 在COCO上取得优于现有DETR变体的性能。

### DETRDistill: A Universal Knowledge Distillation Framework for DETR-families. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2211.10156](https://arxiv.org/abs/2211.10156) · 📚 被引 39
- **作者**: Jiahao Chang, Shuo Wang, Hai-Ming Xu, Zehui Chen, Chenhongyi Yang, Feng Zhao
- **🏷️ 机构**: University of Science and Technology of China, University of Adelaide, University of Edinburgh
- **会议**: ICCV 2023
- **摘要（中）**: 针对DETR系列检测器模型大、推理慢的问题，提出了一种通用的知识蒸馏框架DETRDistill。该方法设计了匈牙利匹配logits蒸馏、目标感知特征蒸馏和查询先验分配蒸馏三个模块，分别促进学生模型预测对齐、学习目标中心特征和加速收敛。在COCO数据集上的实验表明，该方法能有效压缩DETR模型并保持检测性能。
- **摘要（英）**: This paper addresses the deployment challenges of DETR-based detectors by proposing DETRDistill, a universal knowledge distillation framework. It introduces Hungarian-matching logits distillation, target-aware feature distillation, and query-prior assignment distillation to improve prediction alignment, feature learning, and convergence. Experiments on COCO demonstrate effective model compression with maintained detection performance.
- **核心贡献**: 提出了首个专门针对DETR系列检测器的通用知识蒸馏框架。
- **创新点**: 设计了三种针对DETR特性的蒸馏策略，包括logits、特征和查询先验。
- **结果**: 在COCO数据集上实现了有效的模型压缩，性能接近教师模型。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Transformer-based detectors (DETRs) are becoming popular for their simple framework, but the large model size and heavy time consumption hinder their deployment in the real world. While knowledge distillation (KD) can be an appealing technique to compress giant detectors into small ones for comparable detection performance and low inference cost. Since DETRs formulate object detection as a set prediction problem, existing KD methods designed for classic convolution-based detectors may not be directly applicable. In this paper, we propose DETRDistill, a novel knowledge distillation method dedicated to DETR-families. Specifically, we first design a Hungarian-matching logits distillation to encourage the student model to have the exact predictions as that of teacher DETRs. Next, we propose a target-aware feature distillation to help the student model learn from the object-centric features of the teacher model. Finally, in order to improve the convergence rate of the student DETR, we introduce a query-prior assignment distillation to speed up the student model learning from well-trained queries and stable assignment of the teacher model. Extensive experimental results on the COCO dataset validate the effectiveness of our approach. Notably, DETRDistill consistently improves various DETRs by more than 2.0 mAP, even surpassing their teacher models.

</details>

### Rank-DETR for High Quality Object Detection. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/34074479ee2186a9f236b8fd03635372-Abstract-Conference.html)
- **作者**: Yifan Pu, Weicong Liang, Yiduo Hao, Yuhui Yuan, Yukang Yang, Chao Zhang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023
- **摘要（中）**: Rank-DETR针对DETR系列检测器在高质量检测（如高IoU阈值）下性能不佳的问题，提出了一种基于排序的查询机制。该方法通过引入排序损失和排序感知的查询设计，使模型更关注高IoU的预测。在COCO等数据集上，该方法在保持实时性的同时显著提升了高精度检测性能。
- **摘要（英）**: Rank-DETR addresses the issue of suboptimal performance at high IoU thresholds in DETR detectors. It introduces a ranking-based query mechanism with ranking loss to prioritize high-quality predictions. Achieves significant improvements in high-accuracy detection on COCO while maintaining real-time efficiency.
- **核心贡献**: 提出了排序感知的查询机制，提升DETR在高IoU下的检测性能。
- **创新点**: 将排序学习引入DETR查询设计，优化了预测质量分布。
- **结果**: 在COCO上实现了高精度检测性能的提升。

### BEV-SAN: Accurate BEV 3D Object Detection via Slice Attention Networks.
- **链接**: [arXiv:2212.01231](https://arxiv.org/abs/2212.01231) · 📚 被引 33
- **作者**: Xiaowei Chi, Jiaming Liu, Ming Lu, Rongyu Zhang, Zhaoqing Wang, Yandong Guo et al.
- **🏷️ 机构**: School of Computer Science, Peking University,National Key Laboratory for Multimedia Information Processing, The University of Sydney, AI2Robotics
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Bird's-Eye-View (BEV) 3D Object Detection is a crucial multi-view technique for autonomous driving systems. Recently, plenty of works are proposed, following a similar paradigm consisting of three essential components, i.e., camera feature extraction, BEV feature construction, and task heads. Among the three components, BEV feature construction is BEV-specific compared with 2D tasks. Existing methods aggregate the multi-view camera features to the flattened grid in order to construct the BEV feature. However, flattening the BEV space along the height dimension fails to emphasize the informative features of different heights. For example, the barrier is located at a low height while the truck is located at a high height. In this paper, we propose a novel method named BEV Slice Attention Network (BEV-SAN) for exploiting the intrinsic characteristics of different heights. Instead of flattening the BEV space, we first sample along the height dimension to build the global and local BEV slices. Then, the features of BEV slices are aggregated from the camera features and merged by the attention mechanism. Finally, we fuse the merged local and global BEV features by a transformer to generate the final feature map for task heads. The purpose of local BEV slices is to emphasize informative heights. In order to find them, we further propose a LiDAR-guided sampling strategy to leverage the statistical distribution of LiDAR to determine the heights of local slices. Compared with uniform sampling, LiDAR-guided sampling can determine more informative heights. We conduct detailed experiments to demonstrate the effectiveness of BEV-SAN. Code will be released.

</details>

### AeDet: Azimuth-Invariant Multi-View 3D Object Detection.
- **链接**: [arXiv:2211.12501](https://arxiv.org/abs/2211.12501) · 📚 被引 25
- **作者**: Chengjian Feng, Zequn Jie, Yujie Zhong, Xiangxiang Chu, Lin Ma
- **🏷️ 机构**: Meituan Inc.
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent LSS-based multi-view 3D object detection has made tremendous progress, by processing the features in Brid-Eye-View (BEV) via the convolutional detector. However, the typical convolution ignores the radial symmetry of the BEV features and increases the difficulty of the detector optimization. To preserve the inherent property of the BEV features and ease the optimization, we propose an azimuth-equivariant convolution (AeConv) and an azimuth-equivariant anchor. The sampling grid of AeConv is always in the radial direction, thus it can learn azimuth-invariant BEV features. The proposed anchor enables the detection head to learn predicting azimuth-irrelevant targets. In addition, we introduce a camera-decoupled virtual depth to unify the depth prediction for the images with different camera intrinsic parameters. The resultant detector is dubbed Azimuth-equivariant Detector (AeDet). Extensive experiments are conducted on nuScenes, and AeDet achieves a 62.0% NDS, surpassing the recent multi-view 3D object detectors such as PETRv2 and BEVDepth by a large margin. Project page: https://fcjian.github.io/aedet.

</details>

### Generalized UAV Object Detection via Frequency Domain Disentanglement.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00109) · 📚 被引 74
- **作者**: Kunyu Wang, Xueyang Fu, Yukun Huang, Chengzhi Cao, Gege Shi, Zheng-Jun Zha
- **🏷️ 机构**: University of Science and Technology of China,China
- **会议**: CVPR 2023

### Towards Domain Generalization for Multi-view 3D Object Detection in Bird-Eye-View.
- **链接**: [arXiv:2303.01686](https://arxiv.org/abs/2303.01686) · 📚 被引 25
- **作者**: Shuo Wang, Xinhai Zhao, Hai-Ming Xu, Zehui Chen, Dameng Yu, Jiahao Chang et al.
- **🏷️ 机构**: University of Science and Technology of China, Huawei Noah&#x0027;s Ark Lab, University of Adelaide
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-view 3D object detection (MV3D-Det) in Bird-Eye-View (BEV) has drawn extensive attention due to its low cost and high efficiency. Although new algorithms for camera-only 3D object detection have been continuously proposed, most of them may risk drastic performance degradation when the domain of input images differs from that of training. In this paper, we first analyze the causes of the domain gap for the MV3D-Det task. Based on the covariate shift assumption, we find that the gap mainly attributes to the feature distribution of BEV, which is determined by the quality of both depth estimation and 2D image's feature representation. To acquire a robust depth prediction, we propose to decouple the depth estimation from the intrinsic parameters of the camera (i.e. the focal length) through converting the prediction of metric depth to that of scale-invariant depth and perform dynamic perspective augmentation to increase the diversity of the extrinsic parameters (i.e. the camera poses) by utilizing homography. Moreover, we modify the focal length values to create multiple pseudo-domains and construct an adversarial training loss to encourage the feature representation to be more domain-agnostic. Without bells and whistles, our approach, namely DG-BEV, successfully alleviates the performance drop on the unseen target domain without impairing the accuracy of the source domain. Extensive experiments on various public datasets, including Waymo, nuScenes, and Lyft, demonstrate the generalization and effectiveness of our approach. To the best of our knowledge, this is the first systematic study to explore a domain generalization method for MV3D-Det.

</details>

### BEVHeight: A Robust Framework for Vision-based Roadside 3D Object Detection.
- **链接**: [arXiv:2303.08498](https://arxiv.org/abs/2303.08498) · 📚 被引 122
- **作者**: Lei Yang, Kaicheng Yu, Tao Tang, Jun Li, Kun Yuan, Li Wang et al.
- **🏷️ 机构**: Tsinghua University,State Key Laboratory of Automotive Safety and Energy, Autonomous Driving Lab, Alibaba Group, Sun Yat-sen University,Shenzhen Campus
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While most recent autonomous driving system focuses on developing perception methods on ego-vehicle sensors, people tend to overlook an alternative approach to leverage intelligent roadside cameras to extend the perception ability beyond the visual range. We discover that the state-of-the-art vision-centric bird's eye view detection methods have inferior performances on roadside cameras. This is because these methods mainly focus on recovering the depth regarding the camera center, where the depth difference between the car and the ground quickly shrinks while the distance increases. In this paper, we propose a simple yet effective approach, dubbed BEVHeight, to address this issue. In essence, instead of predicting the pixel-wise depth, we regress the height to the ground to achieve a distance-agnostic formulation to ease the optimization process of camera-only perception methods. On popular 3D detection benchmarks of roadside cameras, our method surpasses all previous vision-centric methods by a significant margin. The code is available at {\url{https://github.com/ADLab-AutoDrive/BEVHeight}}.

</details>

### MetaFusion: Infrared and Visible Image Fusion via Meta-Feature Embedding from Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01341) · 📚 被引 241
- **作者**: Wenda Zhao, Shigeng Xie, Fan Zhao, You He, Huchuan Lu
- **🏷️ 机构**: Dalian University of Technology,China, Liaoning Normal University,China, Tsinghua University,China
- **会议**: CVPR 2023

### Texture-Guided Saliency Distilling for Unsupervised Salient Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00701) · 📚 被引 74
- **作者**: Huajun Zhou, Bo Qiao, Lingxiao Yang, Jianhuang Lai, Xiaohua Xie
- **🏷️ 机构**: School of Computer Science and Engineering, Sun Yat-sen University,China
- **会议**: CVPR 2023

### Implicit Occupancy Flow Fields for Perception and Prediction in Self-Driving.
- **链接**: [arXiv:2308.01471](https://arxiv.org/abs/2308.01471) · 📚 被引 27
- **作者**: Ben Agro, Quinlan Sykora, Sergio Casas, Raquel Urtasun
- **🏷️ 机构**: Waabi, University of Toronto
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> A self-driving vehicle (SDV) must be able to perceive its surroundings and predict the future behavior of other traffic participants. Existing works either perform object detection followed by trajectory forecasting of the detected objects, or predict dense occupancy and flow grids for the whole scene. The former poses a safety concern as the number of detections needs to be kept low for efficiency reasons, sacrificing object recall. The latter is computationally expensive due to the high-dimensionality of the output grid, and suffers from the limited receptive field inherent to fully convolutional networks. Furthermore, both approaches employ many computational resources predicting areas or objects that might never be queried by the motion planner. This motivates our unified approach to perception and future prediction that implicitly represents occupancy and flow over time with a single neural network. Our method avoids unnecessary computation, as it can be directly queried by the motion planner at continuous spatio-temporal locations. Moreover, we design an architecture that overcomes the limited receptive field of previous explicit occupancy prediction methods by adding an efficient yet effective global attention mechanism. Through extensive experiments in both urban and highway settings, we demonstrate that our implicit model outperforms the current state-of-the-art. For more information, visit the project website: https://waabi.ai/research/implicito.

</details>

### Objects do not disappear: Video object detection by single-frame object location anticipation.
- **链接**: [arXiv:2308.04770](https://arxiv.org/abs/2308.04770) · 📚 被引 11
- **作者**: Xin Liu, Fatemeh Karimi Nejadasl, Jan C. van Gemert, Olaf Booij, Silvia L. Pintea
- **🏷️ 机构**: Delft University of Technology,Computer Vision Lab, University of Amsterdam,Institute for Biodiversity and Ecosystem Dynamics
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Objects in videos are typically characterized by continuous smooth motion. We exploit continuous smooth motion in three ways. 1) Improved accuracy by using object motion as an additional source of supervision, which we obtain by anticipating object locations from a static keyframe. 2) Improved efficiency by only doing the expensive feature computations on a small subset of all frames. Because neighboring video frames are often redundant, we only compute features for a single static keyframe and predict object locations in subsequent frames. 3) Reduced annotation cost, where we only annotate the keyframe and use smooth pseudo-motion between keyframes. We demonstrate computational efficiency, annotation efficiency, and improved mean average precision compared to the state-of-the-art on four datasets: ImageNet VID, EPIC KITCHENS-55, YouTube-BoundingBoxes, and Waymo Open dataset. Our source code is available at https://github.com/L-KID/Videoobject-detection-by-location-anticipation.

</details>

## 跨领域论文（完整笔记在其他领域）

- Omni3D: A Large Benchmark and Model for 3D Object Detection in the Wild. → [3d-detection](../3d-detection/Guideline%202023.md)
- Distilling DETR with Visual-Linguistic Knowledge for Open-Vocabulary Object Detection. → [open-set-detection](../open-set-detection/Guideline%202023.md)
- OmniLabel: A Challenging Benchmark for Language-Based Object Detection. → [open-set-detection](../open-set-detection/Guideline%202023.md)
- T-FFTRadNet: Object Detection with Swin Vision Transformers from Raw ADC Radar Signals. → [vision-transformer](../vision-transformer/Guideline%202023.md)
- Transformer-Based Sensor Fusion for Autonomous Driving: A Survey. → [autonomous-driving](../autonomous-driving/Guideline%202023.md)
- Object-Aware Distillation Pyramid for Open-Vocabulary Object Detection. → [open-set-detection](../open-set-detection/Guideline%202023.md)
- AShapeFormer : Semantics-Guided Object-Level Active Shape Encoding for 3D Object Detection via Transformers. → [3d-detection](../3d-detection/Guideline%202023.md)
- Unknown Sniffer for Object Detection: Don't Turn a Blind Eye to Unknown Objects. → [open-set-detection](../open-set-detection/Guideline%202023.md)
- CAT: LoCalization and IdentificAtion Cascade Detection Transformer for Open-World Object Detection. → [open-set-detection](../open-set-detection/Guideline%202023.md)
- PROB: Probabilistic Objectness for Open World Object Detection. → [open-set-detection](../open-set-detection/Guideline%202023.md)
- Viewpoint Equivariance for Multi-View 3D Object Detection. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- VoxelNeXt: Fully Sparse VoxelNet for 3D Object Detection and Tracking. → [3d-detection](../3d-detection/Guideline%202023.md)
- PiMAE: Point Cloud and Image Interactive Masked Autoencoders for 3D Object Detection. → [self-supervised-vision](../self-supervised-vision/Guideline%202023.md)
- itKD: Interchange Transfer-based Knowledge Distillation for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Benchmarking Robustness of 3D Object Detection to Common Corruptions in Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202023.md)
- MSF: Motion-guided Sequential Fusion for Efficient 3D Object Detection from Point Cloud Sequences. → [3d-detection](../3d-detection/Guideline%202023.md)
- Density-Insensitive Unsupervised Domain Adaption on 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- MSMDFusion: Fusing LiDAR and Camera at Multiple Scales with Multi-Depth Seeds for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Region-Aware Pretraining for Open-Vocabulary Object Detection with Vision Transformers. → [open-set-detection](../open-set-detection/Guideline%202023.md)
- X3KD: Knowledge Distillation Across Modalities, Tasks and Stages for Multi-Camera 3D Object Detection. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- LoGoNet: Towards Accurate 3D Object Detection with Local-to-Global Cross- Modal Fusion. → [3d-detection](../3d-detection/Guideline%202023.md)
- PillarNeXt: Rethinking Network Designs for 3D Object Detection in LiDAR Point Clouds. → [3d-detection](../3d-detection/Guideline%202023.md)
- MoDAR: Using Motion Forecasting for 3D Object Detection in Point Cloud Sequences. → [3d-detection](../3d-detection/Guideline%202023.md)
- Open-Vocabulary Point-Cloud Object Detection without 3D Annotation. → [open-set-detection](../open-set-detection/Guideline%202023.md)
- DiGeo: Discriminative Geometry-Aware Learning for Generalized Few-Shot Object Detection. → [open-set-detection](../open-set-detection/Guideline%202023.md)
- Deep Dive into Gradients: Better Optimization for 3D Object Detection with Gradient-Corrected IoU Supervision. → [3d-detection](../3d-detection/Guideline%202023.md)
- Weakly Supervised Monocular 3D Object Detection Using Multi-View Projection and Direction Consistency. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- CLIP the Gap: A Single Domain Generalization Approach for Object Detection. → [vlm](../vlm/Guideline%202023.md)
- Learning to Detect and Segment for Open Vocabulary Object Detection. → [open-set-detection](../open-set-detection/Guideline%202023.md)
- Semi-Supervised Stereo-Based 3D Object Detection via Cross-View Consensus. → [3d-detection](../3d-detection/Guideline%202023.md)
- Virtual Sparse Convolution for Multimodal 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Aligning Bag of Regions for Open-Vocabulary Object Detection. → [vlm](../vlm/Guideline%202023.md)
- CAPE: Camera View Position Embedding for Multi-View 3D Object Detection. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- Multi-view Adversarial Discriminator: Mine the Non-causal Factors for Object Detection in Unseen Domains. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- DetCLIPv2: Scalable Open-Vocabulary Object Detection Pre-training via Word-Region Alignment. → [vlm](../vlm/Guideline%202023.md)
- Bi3D: Bi-Domain Active Learning for Cross-Domain 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Distilling Focal Knowledge from Imperfect Expert for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Uni3D: A Unified Baseline for Multi-Dataset 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- OcTr: Octree-Based Transformer for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- UniDistill: A Universal Cross-Modality Knowledge Distillation Framework for 3D Object Detection in Bird's-Eye View. → [bev](../bev/Guideline%202023.md)
- MonoATT: Online Monocular 3D Object Detection with Adaptive Token Transformer. → [3d-detection](../3d-detection/Guideline%202023.md)
- Understanding the Robustness of 3D Object Detection with Bird'View Representations in Autonomous Driving. → [3d-detection](../3d-detection/Guideline%202023.md)
- GeoMAE: Masked Geometric Target Prediction for Self-supervised Point Cloud Pre-Training. → [self-supervised-vision](../self-supervised-vision/Guideline%202023.md)
- CORA: Adapting CLIP for Open-Vocabulary Detection with Region Prompting and Anchor Pre-Matching. → [open-set-detection](../open-set-detection/Guideline%202023.md)
- Visual Exemplar Driven Task-Prompting for Unified Perception in Autonomous Driving. → [fod-detection](../fod-detection/Guideline%202023.md)
- HOICLIP: Efficient Knowledge Transfer for HOI Detection with Vision-Language Models. → [vlm](../vlm/Guideline%202023.md)
- SparseViT: Revisiting Activation Sparsity for Efficient High-Resolution Vision Transformer. → [vision-transformer](../vision-transformer/Guideline%202023.md)
- Hyperbolic Contrastive Learning for Visual Representations beyond Objects. → [self-supervised-vision](../self-supervised-vision/Guideline%202023.md)
- ObjectFusion: Multi-modal 3D Object Detection with Object-Centric Fusion. → [3d-detection](../3d-detection/Guideline%202023.md)
- Object as Query: Lifting any 2D Object Detector to 3D Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Exploring Object-Centric Temporal Modeling for Efficient Multi-View 3D Object Detection. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)

<!-- COMPLETE v1 papers=103 -->
