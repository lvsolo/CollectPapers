# Object Detection — 2024 Guideline

> 领域: 通用 2D 目标检测（检测器架构、密集预测、小物体/旋转框/NMS 等）
> 论文数: 77 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Relation DETR: Exploring Explicit Position Relation Prior for Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72973-7_6) · 📚 被引 68
- **作者**: Xiuquan Hou, Meiqin Liu, Senlin Zhang, Ping Wei, Badong Chen, Xuguang Lan
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### DQ-DETR: DETR with Dynamic Query for Tiny Object Detection.
- **链接**: [arXiv:2404.03507](https://arxiv.org/abs/2404.03507) · [代码](https://github.com/hoiliu-0801/DQ-DETR) · 📚 被引 85
- **作者**: Yi-Xin Huang, Hou-I Liu, Hong-Han Shuai, Wen-Huang Cheng
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

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

> The tasks of object detection and trajectory forecasting play a crucial role in understanding the scene for autonomous driving. These tasks are typically executed in a cascading manner, making them prone to compounding errors. Furthermore, there is usually a very thin interface between the two tasks, creating a lossy information bottleneck. To address these challenges, our approach formulates the union of the two tasks as a trajectory refinement problem, where the first pose is the detection (current time), and the subsequent poses are the waypoints of the multiple forecasts (future time). To tackle this unified task, we design a refinement transformer that infers the presence, pose, and multi-modal future behaviors of objects directly from LiDAR point clouds and high-definition maps. We call this model DeTra, short for object Detection and Trajectory forecasting. In our experiments, we observe that \ourmodel{} outperforms the state-of-the-art on Argoverse 2 Sensor and Waymo Open Dataset by a large margin, across a broad range of metrics. Last but not least, we perform extensive ablation studies that show the value of refinement for this task, that every proposed component contributes positively to its performance, and that key design choices were made.

</details>

### Self-supervised Co-salient Object Detection via Feature Correspondences at Multiple Scales.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72673-6_13)
- **作者**: Souradeep Chakraborty, Dimitris Samaras
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Just a Hint: Point-Supervised Camouflaged Object Detection.
- **链接**: [arXiv:2408.10777](https://arxiv.org/abs/2408.10777) · 📚 被引 21
- **作者**: Huafeng Chen, Dian Shao, Guangqian Guo, Shan Gao
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Camouflaged Object Detection (COD) demands models to expeditiously and accurately distinguish objects which conceal themselves seamlessly in the environment. Owing to the subtle differences and ambiguous boundaries, COD is not only a remarkably challenging task for models but also for human annotators, requiring huge efforts to provide pixel-wise annotations. To alleviate the heavy annotation burden, we propose to fulfill this task with the help of only one point supervision. Specifically, by swiftly clicking on each object, we first adaptively expand the original point-based annotation to a reasonable hint area. Then, to avoid partial localization around discriminative parts, we propose an attention regulator to scatter model attention to the whole object through partially masking labeled regions. Moreover, to solve the unstable feature representation of camouflaged objects under only point-based annotation, we perform unsupervised contrastive learning based on differently augmented image pairs (e.g. changing color or doing translation). On three mainstream COD benchmarks, experimental results show that our model outperforms several weakly-supervised methods by a large margin across various metrics.

</details>

### SAM-COD: SAM-Guided Unified Framework for Weakly-Supervised Camouflaged Object Detection.
- **链接**: [arXiv:2408.10760](https://arxiv.org/abs/2408.10760) · 📚 被引 19
- **作者**: Huafeng Chen, Pengxu Wei, Guangqian Guo, Shan Gao
- **🏷️ 机构**: Unmanned System Research Institute, Northwestern Polytechnical University, Xi&#x2019;an, China, School of Computer Science and Engineering, Sun Yat-sen University, Guangzhou, China
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Most Camouflaged Object Detection (COD) methods heavily rely on mask annotations, which are time-consuming and labor-intensive to acquire. Existing weakly-supervised COD approaches exhibit significantly inferior performance compared to fully-supervised methods and struggle to simultaneously support all the existing types of camouflaged object labels, including scribbles, bounding boxes, and points. Even for Segment Anything Model (SAM), it is still problematic to handle the weakly-supervised COD and it typically encounters challenges of prompt compatibility of the scribble labels, extreme response, semantically erroneous response, and unstable feature representations, producing unsatisfactory results in camouflaged scenes. To mitigate these issues, we propose a unified COD framework in this paper, termed SAM-COD, which is capable of supporting arbitrary weakly-supervised labels. Our SAM-COD employs a prompt adapter to handle scribbles as prompts based on SAM. Meanwhile, we introduce response filter and semantic matcher modules to improve the quality of the masks obtained by SAM under COD prompts. To alleviate the negative impacts of inaccurate mask predictions, a new strategy of prompt-adaptive knowledge distillation is utilized to ensure a reliable feature representation. To validate the effectiveness of our approach, we have conducted extensive empirical experiments on three mainstream COD benchmarks. The results demonstrate the superiority of our method against state-of-the-art weakly-supervised and even fully-supervised methods.

</details>

### Simplifying Source-Free Domain Adaptation for Object Detection: Effective Self-training Strategies and Performance Insights.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72949-2_12) · 📚 被引 14
- **作者**: Yan Hao, Florent Forest, Olga Fink
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### CoLA: Conditional Dropout and Language-Driven Robust Dual-Modal Salient Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72633-0_20) · 📚 被引 6
- **作者**: Shuang Hao, Chunlin Zhong, He Tang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Equivariant Spatio-temporal Self-supervision for LiDAR Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73347-5_27) · 📚 被引 0
- **作者**: Deepti Hegde, Suhas Lohit, Kuan-Chuan Peng, Michael J. Jones, Vishal M. Patel
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Weighting Pseudo-labels via High-Activation Feature Index Similarity and Object Detection for Semi-supervised Segmentation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73226-3_26) · 📚 被引 4
- **作者**: Prantik Howlader, Hieu Le, Dimitris Samaras
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### MutDet: Mutually Optimizing Pre-training for Remote Sensing Object Detection.
- **链接**: [arXiv:2407.09920](https://arxiv.org/abs/2407.09920) · [代码](https://github.com/floatingstarZ/MutDet) · 📚 被引 10
- **作者**: Ziyue Huang, Yongchao Feng, Qingjie Liu, Yunhong Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Detection pre-training methods for the DETR series detector have been extensively studied in natural scenes, e.g., DETReg. However, the detection pre-training remains unexplored in remote sensing scenes. In existing pre-training methods, alignment between object embeddings extracted from a pre-trained backbone and detector features is significant. However, due to differences in feature extraction methods, a pronounced feature discrepancy still exists and hinders the pre-training performance. The remote sensing images with complex environments and more densely distributed objects exacerbate the discrepancy. In this work, we propose a novel Mutually optimizing pre-training framework for remote sensing object Detection, dubbed as MutDet. In MutDet, we propose a systemic solution against this challenge. Firstly, we propose a mutual enhancement module, which fuses the object embeddings and detector features bidirectionally in the last encoder layer, enhancing their information interaction.Secondly, contrastive alignment loss is employed to guide this alignment process softly and simultaneously enhances detector features' discriminativity. Finally, we design an auxiliary siamese head to mitigate the task gap arising from the introduction of enhancement module. Comprehensive experiments on various settings show new state-of-the-art transfer performance. The improvement is particularly pronounced when data quantity is limited. When using 10% of the DIOR-R data, MutDet improves DetReg by 6.1% in AP50. Codes and models are available at: https://github.com/floatingstarZ/MutDet.

</details>

### BugNIST a Large Volumetric Dataset for Object Detection Under Domain Shift.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73411-3_2) · 📚 被引 0
- **作者**: Patrick Møller Jensen, Vedrana Andersen Dahl, Rebecca Engberg, Carsten Gundlach, Hans Martin Kjer, Anders Bjorholm Dahl
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### T-Rex2: Towards Generic Object Detection via Text-Visual Prompt Synergy.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73414-4_3) · 📚 被引 42
- **作者**: Qing Jiang, Feng Li, Zhaoyang Zeng, Tianhe Ren, Shilong Liu, Lei Zhang
- **🏷️ 机构**: PolyU / OPPO
- **会议**: ECCV 2024

### Dynamic Retraining-Updating Mean Teacher for Source-Free Object Detection.
- **链接**: [arXiv:2407.16497](https://arxiv.org/abs/2407.16497) · [代码](https://github.com/lbktrinh/DRU) · 📚 被引 13
- **作者**: Trinh Le Ba Khanh, Huy-Hung Nguyen, Long Hoang Pham, Duong Nguyen-Ngoc Tran, Jae Wook Jeon
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In object detection, unsupervised domain adaptation (UDA) aims to transfer knowledge from a labeled source domain to an unlabeled target domain. However, UDA's reliance on labeled source data restricts its adaptability in privacy-related scenarios. This study focuses on source-free object detection (SFOD), which adapts a source-trained detector to an unlabeled target domain without using labeled source data. Recent advancements in self-training, particularly with the Mean Teacher (MT) framework, show promise for SFOD deployment. However, the absence of source supervision significantly compromises the stability of these approaches. We identify two primary issues, (1) uncontrollable degradation of the teacher model due to inopportune updates from the student model, and (2) the student model's tendency to replicate errors from incorrect pseudo labels, leading to it being trapped in a local optimum. Both factors contribute to a detrimental circular dependency, resulting in rapid performance degradation in recent self-training frameworks. To tackle these challenges, we propose the Dynamic Retraining-Updating (DRU) mechanism, which actively manages the student training and teacher updating processes to achieve co-evolutionary training. Additionally, we introduce Historical Student Loss to mitigate the influence of incorrect pseudo labels. Our method achieves state-of-the-art performance in the SFOD setting on multiple domain adaptation benchmarks, comparable to or even surpassing advanced UDA methods. The code will be released at https://github.com/lbktrinh/DRU

</details>

### CamoTeacher: Dual-Rotation Consistency Learning for Semi-supervised Camouflaged Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72995-9_25) · 📚 被引 10
- **作者**: Xunfa Lai, Zhiyu Yang, Jie Hu, Shengchuan Zhang, Liujuan Cao, Guannan Jiang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Rethinking Features-Fused-Pyramid-Neck for Object Detection.
- **链接**: [arXiv:2505.12820](https://arxiv.org/abs/2505.12820) · [代码](https://github.com/AlanLi1997/rethinking-fpn) · 📚 被引 31
- **作者**: Hulin Li
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-head detectors typically employ a features-fused-pyramid-neck for multi-scale detection and are widely adopted in the industry. However, this approach faces feature misalignment when representations from different hierarchical levels of the feature pyramid are forcibly fused point-to-point. To address this issue, we designed an independent hierarchy pyramid (IHP) architecture to evaluate the effectiveness of the features-unfused-pyramid-neck for multi-head detectors. Subsequently, we introduced soft nearest neighbor interpolation (SNI) with a weight downscaling factor to mitigate the impact of feature fusion at different hierarchies while preserving key textures. Furthermore, we present a features adaptive selection method for down sampling in extended spatial windows (ESD) to retain spatial features and enhance lightweight convolutional techniques (GSConvE). These advancements culminate in our secondary features alignment solution (SA) for real-time detection, achieving state-of-the-art results on Pascal VOC and MS COCO. Code will be released at https://github.com/AlanLi1997/rethinking-fpn. This paper has been accepted by ECCV2024 and published on Springer Nature.

</details>

### A Simple Background Augmentation Method for Object Detection with Diffusion Model.
- **链接**: [arXiv:2408.00350](https://arxiv.org/abs/2408.00350) · 📚 被引 11
- **作者**: Yuhang Li, Xin Dong, Chen Chen, Weiming Zhuang, Lingjuan Lyu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In computer vision, it is well-known that a lack of data diversity will impair model performance. In this study, we address the challenges of enhancing the dataset diversity problem in order to benefit various downstream tasks such as object detection and instance segmentation. We propose a simple yet effective data augmentation approach by leveraging advancements in generative models, specifically text-to-image synthesis technologies like Stable Diffusion. Our method focuses on generating variations of labeled real images, utilizing generative object and background augmentation via inpainting to augment existing training data without the need for additional annotations. We find that background augmentation, in particular, significantly improves the models' robustness and generalization capabilities. We also investigate how to adjust the prompt and mask to ensure the generated content comply with the existing annotations. The efficacy of our augmentation techniques is validated through comprehensive evaluations of the COCO dataset and several other key object detection benchmarks, demonstrating notable enhancements in model performance across diverse scenarios. This approach offers a promising solution to the challenges of dataset enhancement, contributing to the development of more accurate and robust computer vision models.

</details>

### Toward Open Vocabulary Aerial Object Detection with CLIP-Activated Student-Teacher Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73016-0_25)
- **作者**: Yan Li, Weiwei Guo, Xue Yang, Ning Liao, Dunyun He, Jiaqi Zhou et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### CLIFF: Continual Latent Diffusion for Open-Vocabulary Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73001-6_15)
- **作者**: Wuyang Li, Xinyu Liu, Jiayi Ma, Yixuan Yuan
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### CONDA: Condensed Deep Association Learning for Co-salient Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72973-7_17) · 📚 被引 8
- **作者**: Long Li, Nian Liu, Dingwen Zhang, Zhongyu Li, Salman Khan, Rao Muhammad Anwer et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Distilling Knowledge from Large-Scale Image Models for Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72907-2_9) · 📚 被引 5
- **作者**: Gang Li, Wenhai Wang, Xiang Li, Ziheng Li, Jian Yang, Jifeng Dai et al.
- **🏷️ 机构**: Shanghai AI Lab, Tsinghua / Shanghai AI Lab
- **会议**: ECCV 2024

### Integer-Valued Training and Spike-Driven Inference Spiking Neural Network for High-Performance and Energy-Efficient Object Detection.
- **链接**: [arXiv:2407.20708](https://arxiv.org/abs/2407.20708) · [代码](https://github.com/BICLab/SpikeYOLO) · 📚 被引 63
- **作者**: Xinhao Luo, Man Yao, Yuhong Chou, Bo Xu, Guoqi Li
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Brain-inspired Spiking Neural Networks (SNNs) have bio-plausibility and low-power advantages over Artificial Neural Networks (ANNs). Applications of SNNs are currently limited to simple classification tasks because of their poor performance. In this work, we focus on bridging the performance gap between ANNs and SNNs on object detection. Our design revolves around network architecture and spiking neuron. First, the overly complex module design causes spike degradation when the YOLO series is converted to the corresponding spiking version. We design a SpikeYOLO architecture to solve this problem by simplifying the vanilla YOLO and incorporating meta SNN blocks. Second, object detection is more sensitive to quantization errors in the conversion of membrane potentials into binary spikes by spiking neurons. To address this challenge, we design a new spiking neuron that activates Integer values during training while maintaining spike-driven by extending virtual timesteps during inference. The proposed method is validated on both static and neuromorphic object detection datasets. On the static COCO dataset, we obtain 66.2% mAP@50 and 48.9% mAP@50:95, which is +15.0% and +18.7% higher than the prior state-of-the-art SNN, respectively. On the neuromorphic Gen1 dataset, we achieve 67.2% mAP@50, which is +2.5% greater than the ANN with equivalent architecture, and the energy efficiency is improved by 5.7*. Code: https://github.com/BICLab/SpikeYOLO

</details>

### SMILe: Leveraging Submodular Mutual Information For Robust Few-Shot Object Detection.
- **链接**: [arXiv:2407.02665](https://arxiv.org/abs/2407.02665) · 📚 被引 6
- **作者**: Anay Majee, Ryan Sharp, Rishabh K. Iyer
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Confusion and forgetting of object classes have been challenges of prime interest in Few-Shot Object Detection (FSOD). To overcome these pitfalls in metric learning based FSOD techniques, we introduce a novel Submodular Mutual Information Learning (SMILe) framework which adopts combinatorial mutual information functions to enforce the creation of tighter and discriminative feature clusters in FSOD. Our proposed approach generalizes to several existing approaches in FSOD, agnostic of the backbone architecture demonstrating elevated performance gains. A paradigm shift from instance based objective functions to combinatorial objectives in SMILe naturally preserves the diversity within an object class resulting in reduced forgetting when subjected to few training examples. Furthermore, the application of mutual information between the already learnt (base) and newly added (novel) objects ensures sufficient separation between base and novel classes, minimizing the effect of class confusion. Experiments on popular FSOD benchmarks, PASCAL-VOC and MS-COCO show that our approach generalizes to State-of-the-Art (SoTA) approaches improving their novel class performance by up to 5.7% (3.3 mAP points) and 5.4% (2.6 mAP points) on the 10-shot setting of VOC (split 3) and 30-shot setting of COCO datasets respectively. Our experiments also demonstrate better retention of base class performance and up to 2x faster convergence over existing approaches agnostic of the underlying architecture.

</details>

### Modality Translation for Object Detection Adaptation Without Forgetting Prior Knowledge.
- **链接**: [arXiv:2404.01492](https://arxiv.org/abs/2404.01492) · [代码](https://github.com/heitorrapela/ModTr) · 📚 被引 5
- **作者**: Heitor Rapela Medeiros, Masih Aminbeidokhti, Fidel Alejandro Guerrero Peña, David Latortue, Eric Granger, Marco Pedersoli
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> A common practice in deep learning involves training large neural networks on massive datasets to achieve high accuracy across various domains and tasks. While this approach works well in many application areas, it often fails drastically when processing data from a new modality with a significant distribution shift from the data used to pre-train the model. This paper focuses on adapting a large object detection model trained on RGB images to new data extracted from IR images with a substantial modality shift. We propose Modality Translator (ModTr) as an alternative to the common approach of fine-tuning a large model to the new modality. ModTr adapts the IR input image with a small transformation network trained to directly minimize the detection loss. The original RGB model can then work on the translated inputs without any further changes or fine-tuning to its parameters. Experimental results on translating from IR to RGB images on two well-known datasets show that our simple approach provides detectors that perform comparably or better than standard fine-tuning, without forgetting the knowledge of the original model. This opens the door to a more flexible and efficient service-based detection pipeline, where a unique and unaltered server, such as an RGB detector, runs constantly while being queried by different modalities, such as IR with the corresponding translations model. Our code is available at: https://github.com/heitorrapela/ModTr.

</details>

### Bridge Past and Future: Overcoming Information Asymmetry in Incremental Object Detection.
- **链接**: [arXiv:2407.11499](https://arxiv.org/abs/2407.11499) · [代码](https://github.com/iSEE-Laboratory/BPF) · 📚 被引 6
- **作者**: Qijie Mo, Yipeng Gao, Shenghao Fu, Junkai Yan, Ancong Wu, Wei-Shi Zheng
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In incremental object detection, knowledge distillation has been proven to be an effective way to alleviate catastrophic forgetting. However, previous works focused on preserving the knowledge of old models, ignoring that images could simultaneously contain categories from past, present, and future stages. The co-occurrence of objects makes the optimization objectives inconsistent across different stages since the definition for foreground objects differs across various stages, which limits the model's performance greatly. To overcome this problem, we propose a method called ``Bridge Past and Future'' (BPF), which aligns models across stages, ensuring consistent optimization directions. In addition, we propose a novel Distillation with Future (DwF) loss, fully leveraging the background probability to mitigate the forgetting of old classes while ensuring a high level of adaptability in learning new classes. Extensive experiments are conducted on both Pascal VOC and MS COCO benchmarks. Without memory, BPF outperforms current state-of-the-art methods under various settings. The code is available at https://github.com/iSEE-Laboratory/BPF.

</details>

### LEROjD: Lidar Extended Radar-Only Object Detection.
- **链接**: [arXiv:2409.05564](https://arxiv.org/abs/2409.05564) · [代码](https://github.com/rst-tu-dortmund/lerojd) · 📚 被引 6
- **作者**: Patrick Palmer, Martin Krüger, Stefan Schütte, Richard Altendorfer, Ganesh Adam, Torsten Bertram
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Accurate 3D object detection is vital for automated driving. While lidar sensors are well suited for this task, they are expensive and have limitations in adverse weather conditions. 3+1D imaging radar sensors offer a cost-effective, robust alternative but face challenges due to their low resolution and high measurement noise. Existing 3+1D imaging radar datasets include radar and lidar data, enabling cross-modal model improvements. Although lidar should not be used during inference, it can aid the training of radar-only object detectors. We explore two strategies to transfer knowledge from the lidar to the radar domain and radar-only object detectors: 1. multi-stage training with sequential lidar point cloud thin-out, and 2. cross-modal knowledge distillation. In the multi-stage process, three thin-out methods are examined. Our results show significant performance gains of up to 4.2 percentage points in mean Average Precision with multi-stage training and up to 3.9 percentage points with knowledge distillation by initializing the student with the teacher's weights. The main benefit of these approaches is their applicability to other 3D object detection networks without altering their architecture, as we show by analyzing it on two different object detectors. Our code is available at https://github.com/rst-tu-dortmund/lerojd

</details>

### Weak-to-Strong Compositional Learning from Generative Models for Language-Based Object Detection.
- **链接**: [arXiv:2407.15296](https://arxiv.org/abs/2407.15296) · 📚 被引 3
- **作者**: Kwanyong Park, Kuniaki Saito, Donghyun Kim
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-language (VL) models often exhibit a limited understanding of complex expressions of visual objects (e.g., attributes, shapes, and their relations), given complex and diverse language queries. Traditional approaches attempt to improve VL models using hard negative synthetic text, but their effectiveness is limited. In this paper, we harness the exceptional compositional understanding capabilities of generative foundational models. We introduce a novel method for structured synthetic data generation aimed at enhancing the compositional understanding of VL models in language-based object detection. Our framework generates densely paired positive and negative triplets (image, text descriptions, and bounding boxes) in both image and text domains. By leveraging these synthetic triplets, we transform 'weaker' VL models into 'stronger' models in terms of compositional understanding, a process we call "Weak-to-Strong Compositional Learning" (WSCL). To achieve this, we propose a new compositional contrastive learning formulation that discovers semantics and structures in complex descriptions from synthetic triplets. As a result, VL models trained with our synthetic data generation exhibit a significant performance boost in the Omnilabel benchmark by up to +5AP and the D3 benchmark by +6.9AP upon existing baselines.

</details>

### Adaptive Multi-task Learning for Few-Shot Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72667-5_17) · 📚 被引 5
- **作者**: Yan Ren, Yanling Li, Adams Wai-Kin Kong
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Look Around and Learn: Self-training Object Detection by Exploration.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72992-8_5) · 📚 被引 5
- **作者**: Gianluca Scarpellini, Stefano Rosa, Pietro Morerio, Lorenzo Natale, Alessio Del Bue
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Frequency-Spatial Entanglement Learning for Camouflaged Object Detection.
- **链接**: [arXiv:2409.01686](https://arxiv.org/abs/2409.01686) · [代码](https://github.com/CSYSI/FSEL)
- **作者**: Yanguang Sun, Chunyan Xu, Jian Yang, Hanyu Xuan, Lei Luo
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Camouflaged object detection has attracted a lot of attention in computer vision. The main challenge lies in the high degree of similarity between camouflaged objects and their surroundings in the spatial domain, making identification difficult. Existing methods attempt to reduce the impact of pixel similarity by maximizing the distinguishing ability of spatial features with complicated design, but often ignore the sensitivity and locality of features in the spatial domain, leading to sub-optimal results. In this paper, we propose a new approach to address this issue by jointly exploring the representation in the frequency and spatial domains, introducing the Frequency-Spatial Entanglement Learning (FSEL) method. This method consists of a series of well-designed Entanglement Transformer Blocks (ETB) for representation learning, a Joint Domain Perception Module for semantic enhancement, and a Dual-domain Reverse Parser for feature integration in the frequency and spatial domains. Specifically, the ETB utilizes frequency self-attention to effectively characterize the relationship between different frequency bands, while the entanglement feed-forward network facilitates information interaction between features of different domains through entanglement learning. Our extensive experiments demonstrate the superiority of our FSEL over 21 state-of-the-art methods, through comprehensive quantitative and qualitative comparisons in three widely-used datasets. The source code is available at: https://github.com/CSYSI/FSEL.

</details>

### Bayesian Detector Combination for Object Detection with Crowdsourced Annotations.
- **链接**: [arXiv:2407.07958](https://arxiv.org/abs/2407.07958) · [代码](https://github.com/zhiqin1998/bdc) · 📚 被引 5
- **作者**: Zhi Qin Tan, Olga Isupova, Gustavo Carneiro, Xiatian Zhu, Yunpeng Li
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Acquiring fine-grained object detection annotations in unconstrained images is time-consuming, expensive, and prone to noise, especially in crowdsourcing scenarios. Most prior object detection methods assume accurate annotations; A few recent works have studied object detection with noisy crowdsourced annotations, with evaluation on distinct synthetic crowdsourced datasets of varying setups under artificial assumptions. To address these algorithmic limitations and evaluation inconsistency, we first propose a novel Bayesian Detector Combination (BDC) framework to more effectively train object detectors with noisy crowdsourced annotations, with the unique ability of automatically inferring the annotators' label qualities. Unlike previous approaches, BDC is model-agnostic, requires no prior knowledge of the annotators' skill level, and seamlessly integrates with existing object detection models. Due to the scarcity of real-world crowdsourced datasets, we introduce large synthetic datasets by simulating varying crowdsourcing scenarios. This allows consistent evaluation of different models at scale. Extensive experiments on both real and synthetic crowdsourced datasets show that BDC outperforms existing state-of-the-art methods, demonstrating its superiority in leveraging crowdsourced data for object detection. Our code and data are available at https://github.com/zhiqin1998/bdc.

</details>

### Multi-Scale Cross Distillation for Object Detection in Aerial Images.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72967-6_25)
- **作者**: Kun Wang, Zi Wang, Zhang Li, Xichao Teng, Yang Li
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Co-Student: Collaborating Strong and Weak Students for Sparsely Annotated Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72970-6_26) · 📚 被引 3
- **作者**: Lianjun Wu, Jiangxiao Han, Zengqiang Zheng, Xinggang Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Enhancing Source-Free Domain Adaptive Object Detection with Low-Confidence Pseudo Label Distillation.
- **链接**: [arXiv:2407.13524](https://arxiv.org/abs/2407.13524) · [代码](https://github.com/junia3/LPLD) · 📚 被引 19
- **作者**: Ilhoon Yoon, Hyeongjun Kwon, Jin Kim, Junyoung Park, Hyunsung Jang, Kwanghoon Sohn
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Source-Free domain adaptive Object Detection (SFOD) is a promising strategy for deploying trained detectors to new, unlabeled domains without accessing source data, addressing significant concerns around data privacy and efficiency. Most SFOD methods leverage a Mean-Teacher (MT) self-training paradigm relying heavily on High-confidence Pseudo Labels (HPL). However, these HPL often overlook small instances that undergo significant appearance changes with domain shifts. Additionally, HPL ignore instances with low confidence due to the scarcity of training samples, resulting in biased adaptation toward familiar instances from the source domain. To address this limitation, we introduce the Low-confidence Pseudo Label Distillation (LPLD) loss within the Mean-Teacher based SFOD framework. This novel approach is designed to leverage the proposals from Region Proposal Network (RPN), which potentially encompasses hard-to-detect objects in unfamiliar domains. Initially, we extract HPL using a standard pseudo-labeling technique and mine a set of Low-confidence Pseudo Labels (LPL) from proposals generated by RPN, leaving those that do not overlap significantly with HPL. These LPL are further refined by leveraging class-relation information and reducing the effect of inherent noise for the LPLD loss calculation. Furthermore, we use feature distance to adaptively weight the LPLD loss to focus on LPL containing a larger foreground area. Our method outperforms previous SFOD methods on four cross-domain object detection benchmarks. Extensive experiments demonstrate that our LPLD loss leads to effective adaptation by reducing false negatives and facilitating the use of domain-invariant knowledge from the source model. Code is available at https://github.com/junia3/LPLD.

</details>

### Category-Level Object Detection, Pose Estimation and Reconstruction from Stereo Images.
- **链接**: [arXiv:2407.06984](https://arxiv.org/abs/2407.06984) · 📚 被引 5
- **作者**: Chuanrui Zhang, Yonggen Ling, Minglei Lu, Minghan Qin, Haoqian Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We study the 3D object understanding task for manipulating everyday objects with different material properties (diffuse, specular, transparent and mixed). Existing monocular and RGB-D methods suffer from scale ambiguity due to missing or imprecise depth measurements. We present CODERS, a one-stage approach for Category-level Object Detection, pose Estimation and Reconstruction from Stereo images. The base of our pipeline is an implicit stereo matching module that combines stereo image features with 3D position information. Concatenating this presented module and the following transform-decoder architecture leads to end-to-end learning of multiple tasks required by robot manipulation. Our approach significantly outperforms all competing methods in the public TOD dataset. Furthermore, trained on simulated data, CODERS generalize well to unseen category-level object instances in real-world robot manipulation experiments. Our dataset, code, and demos will be available on our project page.

</details>

### OpenSight: A Simple Open-Vocabulary Framework for LiDAR-Based Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72907-2_1)
- **作者**: Hu Zhang, Jianhua Xu, Tao Tang, Haiyang Sun, Xin Yu, Zi Huang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Learning Camouflaged Object Detection from Noisy Pseudo Label.
- **链接**: [arXiv:2407.13157](https://arxiv.org/abs/2407.13157) · 📚 被引 14
- **作者**: Jin Zhang, Ruiheng Zhang, Yanjiao Shi, Zhe Cao, Nian Liu, Fahad Shahbaz Khan
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing Camouflaged Object Detection (COD) methods rely heavily on large-scale pixel-annotated training sets, which are both time-consuming and labor-intensive. Although weakly supervised methods offer higher annotation efficiency, their performance is far behind due to the unclear visual demarcations between foreground and background in camouflaged images. In this paper, we explore the potential of using boxes as prompts in camouflaged scenes and introduce the first weakly semi-supervised COD method, aiming for budget-efficient and high-precision camouflaged object segmentation with an extremely limited number of fully labeled images. Critically, learning from such limited set inevitably generates pseudo labels with serious noisy pixels. To address this, we propose a noise correction loss that facilitates the model's learning of correct pixels in the early learning stage, and corrects the error risk gradients dominated by noisy pixels in the memorization stage, ultimately achieving accurate segmentation of camouflaged objects from noisy labels. When using only 20% of fully labeled data, our method shows superior performance over the state-of-the-art methods.

</details>

### FocusDiffuser: Perceiving Local Disparities for Camouflaged Object Detection.
- **链接**: [arXiv:2407.13133](https://arxiv.org/abs/2407.13133) · 📚 被引 21
- **作者**: Jianwei Zhao, Xin Li, Fan Yang, Qiang Zhai, Ao Luo, Zicheng Jiao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Detecting objects seamlessly blended into their surroundings represents a complex task for both human cognitive capabilities and advanced artificial intelligence algorithms. Currently, the majority of methodologies for detecting camouflaged objects mainly focus on utilizing discriminative models with various unique designs. However, it has been observed that generative models, such as Stable Diffusion, possess stronger capabilities for understanding various objects in complex environments; Yet their potential for the cognition and detection of camouflaged objects has not been extensively explored. In this study, we present a novel denoising diffusion model, namely FocusDiffuser, to investigate how generative models can enhance the detection and interpretation of camouflaged objects. We believe that the secret to spotting camouflaged objects lies in catching the subtle nuances in details. Consequently, our FocusDiffuser innovatively integrates specialized enhancements, notably the Boundary-Driven LookUp (BDLU) module and Cyclic Positioning (CP) module, to elevate standard diffusion models, significantly boosting the detail-oriented analytical capabilities. Our experiments demonstrate that FocusDiffuser, from a generative perspective, effectively addresses the challenge of camouflaged object detection, surpassing leading models on benchmarks like CAMO, COD10K and NC4K.

</details>

### Projecting Points to Axes: Oriented Object Detection via Point-Axis Representation.
- **链接**: [arXiv:2407.08489](https://arxiv.org/abs/2407.08489) · 📚 被引 17
- **作者**: Zeyang Zhao, Qilong Xue, Yuhang He, Yifan Bai, Xing Wei, Yihong Gong
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper introduces the point-axis representation for oriented object detection, emphasizing its flexibility and geometrically intuitive nature with two key components: points and axes. 1) Points delineate the spatial extent and contours of objects, providing detailed shape descriptions. 2) Axes define the primary directionalities of objects, providing essential orientation cues crucial for precise detection. The point-axis representation decouples location and rotation, addressing the loss discontinuity issues commonly encountered in traditional bounding box-based approaches. For effective optimization without introducing additional annotations, we propose the max-projection loss to supervise point set learning and the cross-axis loss for robust axis representation learning. Further, leveraging this representation, we present the Oriented DETR model, seamlessly integrating the DETR framework for precise point-axis prediction and end-to-end detection. Experimental results demonstrate significant performance improvements in oriented object detection tasks.

</details>

### Revisiting Domain-Adaptive Object Detection in Adverse Weather by the Generation and Composition of High-Quality Pseudo-labels.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72764-1_16) · 📚 被引 5
- **作者**: Rui Zhao, Huibin Yan, Shuoyao Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Rectify the Regression Bias in Long-Tailed Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73390-1_12) · 📚 被引 1
- **作者**: Ke Zhu, Minghao Fu, Jie Shao, Tianyu Liu, Jianxin Wu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

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
