# Open-set Detection — 2024 Guideline

> 领域: 开放类检测总类（开放词表 OVD / 开放世界 OWOD / 开集 OOD / 未知类检测）
> 论文数: 20 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Global-Local Collaborative Inference with LLM for Lidar-Based Open-Vocabulary Detection.
- **链接**: [arXiv:2407.08931](https://arxiv.org/abs/2407.08931) · [代码](https://github.com/GradiusTwinbee/GLIS) · 📚 被引 4
- **作者**: Xingyu Peng, Yan Bai, Chen Gao, Lirong Yang, Fei Xia, Beipeng Mu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-Vocabulary Detection (OVD) is the task of detecting all interesting objects in a given scene without predefined object classes. Extensive work has been done to deal with the OVD for 2D RGB images, but the exploration of 3D OVD is still limited. Intuitively, lidar point clouds provide 3D information, both object level and scene level, to generate trustful detection results. However, previous lidar-based OVD methods only focus on the usage of object-level features, ignoring the essence of scene-level information. In this paper, we propose a Global-Local Collaborative Scheme (GLIS) for the lidar-based OVD task, which contains a local branch to generate object-level detection result and a global branch to obtain scene-level global feature. With the global-local information, a Large Language Model (LLM) is applied for chain-of-thought inference, and the detection result can be refined accordingly. We further propose Reflected Pseudo Labels Generation (RPLG) to generate high-quality pseudo labels for supervision and Background-Aware Object Localization (BAOL) to select precise object proposals. Extensive experiments on ScanNetV2 and SUN RGB-D demonstrate the superiority of our methods. Code is released at https://github.com/GradiusTwinbee/GLIS.

</details>

</details>

### Open-Vocabulary Attention Maps with Token Optimization for Semantic Segmentation in Diffusion Models.
- **链接**: [arXiv:2403.14291](https://arxiv.org/abs/2403.14291) · 📚 被引 16
- **作者**: Pablo Marcos-Manchón, Roberto Alcover-Couso, Juan C. SanMiguel, Jose M. Martínez
- **🏷️ 机构**: VPULab, University of Madrid,Spain
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Diffusion models represent a new paradigm in text-to-image generation. Beyond generating high-quality images from text prompts, models such as Stable Diffusion have been successfully extended to the joint generation of semantic segmentation pseudo-masks. However, current extensions primarily rely on extracting attentions linked to prompt words used for image synthesis. This approach limits the generation of segmentation masks derived from word tokens not contained in the text prompt. In this work, we introduce Open-Vocabulary Attention Maps (OVAM)-a training-free method for text-to-image diffusion models that enables the generation of attention maps for any word. In addition, we propose a lightweight optimization process based on OVAM for finding tokens that generate accurate attention maps for an object class with a single annotation. We evaluate these tokens within existing state-of-the-art Stable Diffusion extensions. The best-performing model improves its mIoU from 52.1 to 86.6 for the synthetic images' pseudo-masks, demonstrating that our optimized tokens are an efficient way to improve the performance of existing methods without architectural changes or retraining.

</details>

### Open-Vocabulary Semantic Segmentation with Image Embedding Balancing.
- **链接**: [arXiv:2406.09829](https://arxiv.org/abs/2406.09829) · 📚 被引 26
- **作者**: Xiangheng Shan, Dongyue Wu, Guilin Zhu, Yuanjie Shao, Nong Sang, Changxin Gao
- **🏷️ 机构**: National Key Laboratory of Multispectral Information Intelligent Processing Technology, School of Artificial Intelligence and Automation, Huazhong University of Science and Technology
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-vocabulary semantic segmentation is a challenging task, which requires the model to output semantic masks of an image beyond a close-set vocabulary. Although many efforts have been made to utilize powerful CLIP models to accomplish this task, they are still easily overfitting to training classes due to the natural gaps in semantic information between training and new classes. To overcome this challenge, we propose a novel framework for openvocabulary semantic segmentation called EBSeg, incorporating an Adaptively Balanced Decoder (AdaB Decoder) and a Semantic Structure Consistency loss (SSC Loss). The AdaB Decoder is designed to generate different image embeddings for both training and new classes. Subsequently, these two types of embeddings are adaptively balanced to fully exploit their ability to recognize training classes and generalization ability for new classes. To learn a consistent semantic structure from CLIP, the SSC Loss aligns the inter-classes affinity in the image feature space with that in the text feature space of CLIP, thereby improving the generalization ability of our model. Furthermore, we employ a frozen SAM image encoder to complement the spatial information that CLIP features lack due to the low training image resolution and image-level supervision inherent in CLIP. Extensive experiments conducted across various benchmarks demonstrate that the proposed EBSeg outperforms the state-of-the-art methods. Our code and trained models will be here: https://github.com/slonetime/EBSeg.

</details>

### USE: Universal Segment Embeddings for Open-Vocabulary Image Segmentation.
- **链接**: [arXiv:2406.05271](https://arxiv.org/abs/2406.05271) · 📚 被引 20
- **作者**: Xiaoqi Wang, Wenbin He, Xiwei Xuan, Clint Sebastian, Jorge Piazentin Ono, Xin Li et al.
- **🏷️ 机构**: Bosch Research North America, Bosch Center for Artificial Intelligence (BCAI)
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The open-vocabulary image segmentation task involves partitioning images into semantically meaningful segments and classifying them with flexible text-defined categories. The recent vision-based foundation models such as the Segment Anything Model (SAM) have shown superior performance in generating class-agnostic image segments. The main challenge in open-vocabulary image segmentation now lies in accurately classifying these segments into text-defined categories. In this paper, we introduce the Universal Segment Embedding (USE) framework to address this challenge. This framework is comprised of two key components: 1) a data pipeline designed to efficiently curate a large amount of segment-text pairs at various granularities, and 2) a universal segment embedding model that enables precise segment classification into a vast range of text-defined categories. The USE model can not only help open-vocabulary image segmentation but also facilitate other downstream tasks (e.g., querying and ranking). Through comprehensive experimental studies on semantic segmentation and part segmentation benchmarks, we demonstrate that the USE framework outperforms state-of-the-art open-vocabulary segmentation methods.

</details>

### OVFoodSeg: Elevating Open-Vocabulary Food Image Segmentation via Image-Informed Textual Representation.
- **链接**: [arXiv:2404.01409](https://arxiv.org/abs/2404.01409) · 📚 被引 10
- **作者**: Xiongwei Wu, Sicheng Yu, Ee-Peng Lim, Chong-Wah Ngo
- **🏷️ 机构**: Singapore Management University
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In the realm of food computing, segmenting ingredients from images poses substantial challenges due to the large intra-class variance among the same ingredients, the emergence of new ingredients, and the high annotation costs associated with large food segmentation datasets. Existing approaches primarily utilize a closed-vocabulary and static text embeddings setting. These methods often fall short in effectively handling the ingredients, particularly new and diverse ones. In response to these limitations, we introduce OVFoodSeg, a framework that adopts an open-vocabulary setting and enhances text embeddings with visual context. By integrating vision-language models (VLMs), our approach enriches text embedding with image-specific information through two innovative modules, eg, an image-to-text learner FoodLearner and an Image-Informed Text Encoder. The training process of OVFoodSeg is divided into two stages: the pre-training of FoodLearner and the subsequent learning phase for segmentation. The pre-training phase equips FoodLearner with the capability to align visual information with corresponding textual representations that are specifically related to food, while the second phase adapts both the FoodLearner and the Image-Informed Text Encoder for the segmentation task. By addressing the deficiencies of previous models, OVFoodSeg demonstrates a significant improvement, achieving an 4.9\% increase in mean Intersection over Union (mIoU) on the FoodSeg103 dataset, setting a new milestone for food image segmentation.

</details>

### Open-Vocabulary Video Anomaly Detection.
- **链接**: [arXiv:2311.07042](https://arxiv.org/abs/2311.07042)
- **作者**: Peng Wu, Xuerong Zhou, Guansong Pang, Yujia Sun, Jing Liu, Peng Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We tackle the novel class discovery in point cloud segmentation, which discovers novel classes based on the semantic knowledge of seen classes. Existing work proposes an online point-wise clustering method with a simplified equal class-size constraint on the novel classes to avoid degenerate solutions. However, the inherent imbalanced distribution of novel classes in point clouds typically violates the equal class-size constraint. Moreover, point-wise clustering ignores the rich spatial context information of objects, which results in less expressive representation for semantic segmentation. To address the above challenges, we propose a novel self-labeling strategy that adaptively generates high-quality pseudo-labels for imbalanced classes during model training. In addition, we develop a dual-level representation that incorporates regional consistency into the point-level classifier learning, reducing noise in generated segmentation. Finally, we conduct extensive experiments on two widely used datasets, SemanticKITTI and SemanticPOSS, and the results show our method outperforms the state of the art by a large margin.

</details>

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D panoptic segmentation is a challenging perception task, especially in autonomous driving. It aims to predict both semantic and instance annotations for 3D points in a scene. Although prior 3D panoptic segmentation approaches have achieved great performance on closed-set benchmarks, generalizing these approaches to unseen things and unseen stuff categories remains an open problem. For unseen object categories, 2D open-vocabulary segmentation has achieved promising results that solely rely on frozen CLIP backbones and ensembling multiple classification outputs. However, we find that simply extending these 2D models to 3D does not guarantee good performance due to poor per-mask classification quality, especially for novel stuff categories. In this paper, we propose the first method to tackle 3D open-vocabulary panoptic segmentation. Our model takes advantage of the fusion between learnable LiDAR features and dense frozen vision CLIP features, using a single classification head to make predictions for both base and novel classes. To further improve the classification performance on novel classes and leverage the CLIP model, we propose two novel loss functions: object-level distillation loss and voxel-level distillation loss. Our experiments on the nuScenes and SemanticKITTI datasets show that our method outperforms the strong baseline by a large margin.

</details>

### Open Vocabulary 3D Scene Understanding via Geometry Guided Self-Distillation.
- **链接**: [arXiv:2407.13362](https://arxiv.org/abs/2407.13362) · 📚 被引 5
- **作者**: Pengfei Wang, Yuxi Wang, Shuai Li, Zhaoxiang Zhang, Zhen Lei, Lei Zhang
- **🏷️ 机构**: PolyU / OPPO
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Names are essential to both human cognition and vision-language models. Open-vocabulary models utilize class names as text prompts to generalize to categories unseen during training. However, the precision of these names is often overlooked in existing datasets. In this paper, we address this underexplored problem by presenting a framework for "renovating" names in open-vocabulary segmentation benchmarks (RENOVATE). Our framework features a renaming model that enhances the quality of names for each visual segment. Through experiments, we demonstrate that our renovated names help train stronger open-vocabulary models with up to 15% relative improvement and significantly enhance training efficiency with improved data quality. We also show that our renovated names improve evaluation by better measuring misclassification and enabling fine-grained model analysis. We will provide our code and relabelings for several popular segmentation datasets (MS COCO, ADE20K, Cityscapes) to the research community.

</details>

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large-scale vision-language models like CLIP have demonstrated impressive open-vocabulary capabilities for image-level tasks, excelling in recognizing what objects are present. However, they struggle with pixel-level recognition tasks like semantic segmentation, which additionally require understanding where the objects are located. In this work, we propose a novel method, PixelCLIP, to adapt the CLIP image encoder for pixel-level understanding by guiding the model on where, which is achieved using unlabeled images and masks generated from vision foundation models such as SAM and DINO. To address the challenges of leveraging masks without semantic labels, we devise an online clustering algorithm using learnable class names to acquire general semantic concepts. PixelCLIP shows significant performance improvements over CLIP and competitive results compared to caption-supervised methods in open-vocabulary semantic segmentation. Project page is available at https://cvlab-kaist.github.io/PixelCLIP

</details>

### Does Video-Text Pretraining Help Open-Vocabulary Online Action Detection?
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/5598cf1b2905a26ddb863e6705588327-Abstract-Conference.html) · 📚 被引 3
- **作者**: Qingsong Zhao, Yi Wang, Jilan Xu, Yinan He, Zifan Song, Limin Wang et al.
- **🏷️ 机构**: Shanghai AI Lab
- **会议**: NeurIPS 2024

## 跨领域论文（完整笔记在其他领域）

- Grounding DINO: Marrying DINO with Grounded Pre-training for Open-Set Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- Cross-Domain Few-Shot Object Detection via Enhanced Open-Set Object Detector. → [object-detection](../object-detection/Guideline%202024.md)
- MarvelOVD: Marrying Object Recognition and Vision-Language Models for Robust Open-Vocabulary Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- Find n' Propagate: Open-Vocabulary 3D Object Detection in Urban Environments. → [3d-detection](../3d-detection/Guideline%202024.md)
- Unlocking Textual and Visual Wisdom: Open-Vocabulary 3D Object Detection Enhanced by Comprehensive Guidance from Text and Image. → [3d-detection](../3d-detection/Guideline%202024.md)
- Toward Open Vocabulary Aerial Object Detection with CLIP-Activated Student-Teacher Learning. → [object-detection](../object-detection/Guideline%202024.md)
- CLIFF: Continual Latent Diffusion for Open-Vocabulary Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- OV-Uni3DETR: Towards Unified Open-Vocabulary 3D Object Detection via Cycle-Modality Propagation. → [3d-detection](../3d-detection/Guideline%202024.md)
- OpenSight: A Simple Open-Vocabulary Framework for LiDAR-Based Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- Towards Multimodal Open-Set Domain Generalization and Adaptation Through Self-supervision. → [multimodal](../multimodal/Guideline%202024.md)
- Dense Multimodal Alignment for Open-Vocabulary 3D Scene Understanding. → [multimodal](../multimodal/Guideline%202024.md)
- OpenPSG: Open-Set Panoptic Scene Graph Generation via Large Multimodal Models. → [multimodal](../multimodal/Guideline%202024.md)
- Continual Learning and Unknown Object Discovery in 3D Scenes via Self-distillation. → [continual-learning](../continual-learning/Guideline%202024.md)
- Anytime Continual Learning for Open Vocabulary Classification. → [continual-learning](../continual-learning/Guideline%202024.md)

## 🆕 增量新增

### VideoGrounding-DINO: Towards Open-Vocabulary Spatio- Temporal Video Grounding. **⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01789) · 📚 被引 18
- **作者**: Syed Talal Wasim, Muzammal Naseer, Salman H. Khan, Ming-Hsuan Yang, Fahad Shahbaz Khan
- **🏷️ 机构**: Mohamed bin Zayed University of AI, University of California,Merced
- **会议**: CVPR 2024
- **摘要（中）**: ①针对开放词汇的时空视频定位问题，即给定文本查询，在视频中同时定位目标对象的时间和空间位置。②提出了VideoGrounding-DINO框架，结合DINO和视频 grounding 技术，利用时空解码器联合预测时间区间和空间框。③改进点在于将开放词汇能力扩展到视频领域，利用预训练视觉-语言模型对齐文本和视频特征。④摘要未提供具体数据，但预期在视频 grounding 基准上提升性能。
- **摘要（英）**: This paper addresses open-vocabulary spatio-temporal video grounding, proposing VideoGrounding-DINO to jointly localize objects in time and space via a spatio-temporal decoder. It extends open-vocabulary detection to video by leveraging vision-language models. The abstract lacks quantitative results, but the approach aims to improve video grounding benchmarks.
- **核心贡献**: 提出首个开放词汇时空视频定位框架VideoGrounding-DINO。
- **创新点**: 将开放词汇检测扩展到视频时空定位，结合DINO架构。
- **结果**: 未提供具体数据，预期提升视频定位性能。

### Grounding DINO: Marrying DINO with Grounded Pre-training for Open-Set Object Detection. **⭐⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72970-6_3) · 📚 被引 1673
- **作者**: Shilong Liu, Zhaoyang Zeng, Tianhe Ren, Feng Li, Hao Zhang, Jie Yang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024
- **摘要（中）**: ①该论文针对开放集目标检测中模型无法识别训练集外类别的问题。②提出了Grounding DINO，将DINO与基于文本的grounded预训练相结合，实现开放集检测。③相比已有方法，该方法统一了检测和 grounding 任务，利用文本-图像对齐增强泛化能力。④在多个基准上展示了强大的零样本检测性能，具体数据未在摘要中提供。
- **摘要（英）**: This paper addresses open-set object detection, where models fail on unseen categories. It proposes Grounding DINO, marrying DINO with grounded pre-training for open-set detection. The method unifies detection and grounding tasks, leveraging text-image alignment for better generalization. It demonstrates strong zero-shot performance on multiple benchmarks.
- **核心贡献**: 提出首个将DINO与grounded预训练结合的开放集检测框架。
- **创新点**: 统一检测与grounding任务，实现文本引导的开放集检测。
- **结果**: 在多个基准上实现领先的零样本检测性能。

### OVT-B: A New Large-Scale Benchmark for Open-Vocabulary Multi-Object Tracking. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2410.17534](https://arxiv.org/abs/2410.17534) · 📚 被引 2
- **作者**: Haiji Liang, Ruize Han
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024
- **摘要（中）**: ①该论文针对开放词汇多目标跟踪（OVT）领域缺乏大规模基准数据集的问题，现有OVTAO-val数据集规模有限（200+类别、900+视频），限制了该方向的研究进展。②作者构建了名为OVT-B的大规模基准，包含1,048个物体类别、1,973个视频和637,608个边界框标注，并开发了一个简单有效的基线方法，该方法在跟踪中整合了运动特征，而这一特征在之前的OVT方法中被忽略。③相比已有工作，OVT-B在类别数和视频数上显著更大，且基线方法通过引入运动特征提升了跟踪性能。④实验验证了基准的实用性和方法的有效性，但摘要中未提供具体数值结果。
- **摘要（英）**: This paper addresses the lack of large-scale benchmarks for open-vocabulary multi-object tracking (OVT) by introducing OVT-B, a new benchmark with 1,048 object categories, 1,973 videos, and 637,608 bounding box annotations, significantly larger than the existing OVTAO-val dataset. The authors also propose a simple yet effective baseline that integrates motion features for tracking, which was previously ignored in OVT methods. Experiments confirm the benchmark's usefulness and the method's effectiveness, though specific quantitative results are not detailed in the abstract.
- **核心贡献**: 构建了目前最大规模的开放词汇多目标跟踪基准OVT-B，并提出了整合运动特征的基线方法。
- **创新点**: 在开放词汇跟踪中引入运动特征，并创建了大规模、多类别的基准数据集。
- **结果**: 实验验证了基准的实用性和基线方法的有效性，但未报告具体性能数值。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-vocabulary object perception has become an important topic in artificial intelligence, which aims to identify objects with novel classes that have not been seen during training. Under this setting, open-vocabulary object detection (OVD) in a single image has been studied in many literature. However, open-vocabulary object tracking (OVT) from a video has been studied less, and one reason is the shortage of benchmarks. In this work, we have built a new large-scale benchmark for open-vocabulary multi-object tracking namely OVT-B. OVT-B contains 1,048 categories of objects and 1,973 videos with 637,608 bounding box annotations, which is much larger than the sole open-vocabulary tracking dataset, i.e., OVTAO-val dataset (200+ categories, 900+ videos). The proposed OVT-B can be used as a new benchmark to pave the way for OVT research. We also develop a simple yet effective baseline method for OVT. It integrates the motion features for object tracking, which is an important feature for MOT but is ignored in previous OVT methods. Experimental results have verified the usefulness of the proposed benchmark and the effectiveness of our method. We have released the benchmark to the public at https://github.com/Coo1Sea/OVT-B-Dataset.

</details>

### Generative Region-Language Pretraining for Open-Ended Object Detection. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2403.10191](https://arxiv.org/abs/2403.10191) · 📚 被引 15
- **作者**: Chuang Lin, Yi Jiang, Lizhen Qu, Zehuan Yuan, Jianfei Cai
- **🏷️ 机构**: Monash University, ByteDance Inc.
- **会议**: CVPR 2024
- **摘要（中）**: ①该论文针对开放词汇目标检测在推理时仍需预定义类别名称的限制，提出了生成式开放端目标检测的新设置。②提出了GenerateU框架，将目标检测建模为生成问题，使用Deformable DETR作为区域提议生成器，并结合语言模型实现自由形式的物体名称生成。③相比已有开放词汇检测方法，该方法无需预定义类别，更通用和实用。④摘要中未给出具体数据，但该框架在密集物体检测和名称生成方面展示了潜力。
- **摘要（英）**: This paper addresses the limitation of open-vocabulary object detection requiring predefined category names at inference. It proposes a new setting called generative open-ended object detection and introduces GenerateU, which formulates detection as a generative problem using Deformable DETR and a language model for free-form name generation. This approach is more general and practical than existing methods. Specific performance metrics are not provided in the abstract.
- **核心贡献**: 提出生成式开放端目标检测设置及GenerateU框架，实现无需预定义类别的物体检测与命名。
- **创新点**: 将目标检测转化为生成问题，结合区域提议与语言模型实现自由形式输出。
- **结果**: 摘要未提供具体数据，但展示了框架的可行性和潜力。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In recent research, significant attention has been devoted to the open-vocabulary object detection task, aiming to generalize beyond the limited number of classes labeled during training and detect objects described by arbitrary category names at inference. Compared with conventional object detection, open vocabulary object detection largely extends the object detection categories. However, it relies on calculating the similarity between image regions and a set of arbitrary category names with a pretrained vision-and-language model. This implies that, despite its open-set nature, the task still needs the predefined object categories during the inference stage. This raises the question: What if we do not have exact knowledge of object categories during inference? In this paper, we call such a new setting as generative open-ended object detection, which is a more general and practical problem. To address it, we formulate object detection as a generative problem and propose a simple framework named GenerateU, which can detect dense objects and generate their names in a free-form way. Particularly, we employ Deformable DETR as a region proposal generator with a language model translating visual regions to object names. To assess the free-form object detection task, we introduce an evaluation method designed to quantitatively measure the performance of generative outcomes. Extensive experiments demonstrate strong zero-shot detection performance of our GenerateU. For example, on the LVIS dataset, our GenerateU achieves comparable results to the open-vocabulary object detection method GLIP, even though the category names are not seen by GenerateU during inference. Code is available at: https:// github.com/FoundationVision/GenerateU .

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

### Learning Background Prompts to Discover Implicit Knowledge for Open Vocabulary Object Detection. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2406.00510](https://arxiv.org/abs/2406.00510) · 📚 被引 27
- **作者**: Jiaming Li, Jiacheng Zhang, Jichang Li, Ge Li, Si Liu, Liang Lin et al.
- **🏷️ 机构**: School of Computer Science and Engineering, Sun Yat-sen University,Guangzhou,China, Shenzhen Graduate School, Peking University,SECE,Shenzhen,China, Institute of Artificial Intelligence, Beihang University,China
- **会议**: CVPR 2024
- **摘要（中）**: ①针对开放词汇检测中背景解释不足和模型过拟合问题，导致背景知识丢失。②提出了LBP框架，包含背景类别提示、背景对象发现和推理概率校正三个模块，学习背景提示以挖掘隐式知识。③改进点在于显式建模背景知识，提升基类和新颖类的检测性能。④在基准数据集上评估，具体数据未在摘要中给出，但表明性能提升。
- **摘要（英）**: This paper addresses background interpretation and overfitting in OVD by proposing LBP, which learns background prompts to discover implicit knowledge. It includes three modules for background category prompts, object discovery, and probability rectification, enhancing detection on base and novel classes. Evaluation on benchmarks shows improvements, though specific numbers are not provided.
- **核心贡献**: 提出学习背景提示的LBP框架，挖掘隐式背景知识。
- **创新点**: 首次将背景提示学习引入OVD，解决背景知识丢失。
- **结果**: 在基准上提升基类和新颖类检测性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open vocabulary object detection (OVD) aims at seeking an optimal object detector capable of recognizing objects from both base and novel categories. Recent advances leverage knowledge distillation to transfer insightful knowledge from pre-trained large-scale vision-language models to the task of object detection, significantly generalizing the powerful capabilities of the detector to identify more unknown object categories. However, these methods face significant challenges in background interpretation and model overfitting and thus often result in the loss of crucial background knowledge, giving rise to sub-optimal inference performance of the detector. To mitigate these issues, we present a novel OVD framework termed LBP to propose learning background prompts to harness explored implicit background knowledge, thus enhancing the detection performance w.r.t. base and novel categories. Specifically, we devise three modules: Background Category-specific Prompt, Background Object Discovery, and Inference Probability Rectification, to empower the detector to discover, represent, and leverage implicit object knowledge explored from background proposals. Evaluation on two benchmark datasets, OV-COCO and OV-LVIS, demonstrates the superiority of our proposed method over existing state-of-the-art approaches in handling the OVD tasks.

</details>

### SHiNe: Semantic Hierarchy Nexus for Open-Vocabulary Object Detection. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2405.10053](https://arxiv.org/abs/2405.10053) · 📚 被引 14
- **作者**: Mingxuan Liu, Tyler L. Hayes, Elisa Ricci, Gabriela Csurka, Riccardo Volpi
- **🏷️ 机构**: University of Trento, NAVER LABS Europe
- **会议**: CVPR 2024
- **摘要（中）**: ①针对开放词汇检测中，不同语义粒度词汇导致检测器性能波动的问题。②提出了SHiNe分类器，利用类别层次结构，检索超/子类别并融合为层次感知句子，生成nexus分类器向量。③改进点在于增强跨粒度词汇的鲁棒性，无需重新训练。④在多个检测基准上，使用真实层次结构时mAP50提升高达31.9%，在ImageNet-1k分类上提升CLIP零样本基线2%以上。
- **摘要（英）**: This paper introduces SHiNe, a classifier that leverages semantic hierarchies to improve robustness across vocabulary granularities in OvOD. It retrieves super/sub-categories, integrates them into sentences, and fuses embeddings. It achieves up to +31.9% mAP50 with ground truth hierarchies and +2% on ImageNet-1k classification.
- **核心贡献**: 提出基于语义层次网络的SHiNe分类器，增强OVD鲁棒性。
- **创新点**: 利用类别层次结构生成nexus向量，无需训练即可提升性能。
- **结果**: mAP50提升31.9%，ImageNet-1k分类提升2%。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-vocabulary object detection (OvOD) has transformed detection into a language-guided task, empowering users to freely define their class vocabularies of interest during inference. However, our initial investigation indicates that existing OvOD detectors exhibit significant variability when dealing with vocabularies across various semantic granularities, posing a concern for real-world deployment. To this end, we introduce Semantic Hierarchy Nexus (SHiNe), a novel classifier that uses semantic knowledge from class hierarchies. It runs offline in three steps: i) it retrieves relevant super-/sub-categories from a hierarchy for each target class; ii) it integrates these categories into hierarchy-aware sentences; iii) it fuses these sentence embeddings to generate the nexus classifier vector. Our evaluation on various detection benchmarks demonstrates that SHiNe enhances robustness across diverse vocabulary granularities, achieving up to +31.9% mAP50 with ground truth hierarchies, while retaining improvements using hierarchies generated by large language models. Moreover, when applied to open-vocabulary classification on ImageNet-1k, SHiNe improves the CLIP zero-shot baseline by +2.8% accuracy. SHiNe is training-free and can be seamlessly integrated with any off-the-shelf OvOD detector, without incurring additional computational overhead during inference. The code is open source.

</details>

### DetCLIPv3: Towards Versatile Generative Open-Vocabulary Object Detection. **⭐⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2404.09216](https://arxiv.org/abs/2404.09216) · 📚 被引 40
- **作者**: Lewei Yao, Renjie Pi, Jianhua Han, Xiaodan Liang, Hang Xu, Wei Zhang et al.
- **🏷️ 机构**: Hong Kong University of Science and Technology, Huawei Noah&#x0027;s Ark Lab, Shenzhen Campus of Sun Yat-Sen University
- **会议**: CVPR 2024
- **摘要（中）**: ①针对现有开放词汇检测器需要预定义类别，限制应用场景的问题。②提出了DetCLIPv3，一个多功能检测器，支持开放词汇检测和生成层次化标签，集成caption头。③改进点包括：通用架构、高信息密度数据（利用视觉LLM自动标注）、高效训练策略（低分辨率预训练+高分辨率微调）。④在多个基准上表现优异，具体数据未在摘要中给出，但表明性能领先。
- **摘要（英）**: This paper presents DetCLIPv3, a versatile detector that performs open-vocabulary detection and generates hierarchical labels. It features a caption head, auto-annotation with visual LLMs, and a two-stage training strategy. It achieves state-of-the-art performance on benchmarks, though specific numbers are not provided.
- **核心贡献**: 提出DetCLIPv3，实现生成式开放词汇检测与层次标签生成。
- **创新点**: 集成caption头与视觉LLM自动标注，提升数据效率。
- **结果**: 在多个基准上达到领先性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing open-vocabulary object detectors typically require a predefined set of categories from users, significantly confining their application scenarios. In this paper, we introduce DetCLIPv3, a high-performing detector that excels not only at both open-vocabulary object detection, but also generating hierarchical labels for detected objects. DetCLIPv3 is characterized by three core designs: 1. Versatile model architecture: we derive a robust open-set detection framework which is further empowered with generation ability via the integration of a caption head. 2. High information density data: we develop an auto-annotation pipeline leveraging visual large language model to refine captions for large-scale image-text pairs, providing rich, multi-granular object labels to enhance the training. 3. Efficient training strategy: we employ a pre-training stage with low-resolution inputs that enables the object captioner to efficiently learn a broad spectrum of visual concepts from extensive image-text paired data. This is followed by a fine-tuning stage that leverages a small number of high-resolution samples to further enhance detection performance. With these effective designs, DetCLIPv3 demonstrates superior open-vocabulary detection performance, \eg, our Swin-T backbone model achieves a notable 47.0 zero-shot fixed AP on the LVIS minival benchmark, outperforming GLIPv2, GroundingDINO, and DetCLIPv2 by 18.0/19.6/6.6 AP, respectively. DetCLIPv3 also achieves a state-of-the-art 19.7 AP in dense captioning task on VG dataset, showcasing its strong generative capability.

</details>

### Exploring Region-Word Alignment in Built-in Detector for Open-Vocabulary Object Detection. **⭐⭐⭐** (相关度: 75%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01606) · 📚 被引 9
- **作者**: Heng Zhang, Qiuyu Zhao, Linyu Zheng, Hao Zeng, Zhiwei Ge, Tianhao Li et al.
- **🏷️ 机构**: JD.com
- **会议**: CVPR 2024
- **摘要（中）**: ①针对开放词汇检测中区域-词对齐问题，即检测器内置对齐不充分。②探索了内置检测器中的区域-词对齐方法，具体细节未在摘要中提供。③改进点可能在于优化对齐机制以提升新颖类检测。④摘要不完整，无法提供具体效果数据。
- **摘要（英）**: This paper explores region-word alignment in built-in detectors for open-vocabulary detection, aiming to improve alignment quality. The abstract is incomplete, lacking methodological details and results.
- **核心贡献**: 探索内置检测器中的区域-词对齐机制。
- **创新点**: 可能提出新的对齐策略，但细节未知。
- **结果**: 未提供具体数据。

### Taming Self-Training for Open-Vocabulary Object Detection. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01322) · 📚 被引 15
- **作者**: Shiyu Zhao, Samuel Schulter, Long Zhao, Zhixing Zhang, B. G. Vijay Kumar, Yumin Suh et al.
- **🏷️ 机构**: Rutgers University, NEC Laboratories America, Google Research
- **会议**: CVPR 2024
- **摘要（中）**: 针对开放词汇目标检测中自训练（self-training）方法易受伪标签噪声影响的问题，该论文提出一种驯服自训练的策略。方法通过设计可靠的伪标签筛选机制和稳健的训练目标，减少噪声传播，提升模型在未见类别上的检测能力。相比传统自训练，该方法在保持基类性能的同时显著改善新类召回率。实验在LVIS等数据集上验证了有效性。
- **摘要（英）**: This paper tackles the issue of noisy pseudo-labels in self-training for open-vocabulary object detection. It introduces a reliable pseudo-label filtering mechanism and robust training objectives to mitigate noise propagation, enhancing detection on unseen categories. Compared to standard self-training, it maintains base-class performance while significantly improving novel-class recall, validated on LVIS and other datasets.
- **核心贡献**: 提出驯服自训练的伪标签筛选与稳健训练方法，提升开放词汇检测性能。
- **创新点**: 设计噪声感知的伪标签过滤与损失加权策略。
- **结果**: 在LVIS等数据集上显著提升新类召回率。

### Open3DSG: Open-Vocabulary 3D Scene Graphs from Point Clouds with Queryable Objects and Open-Set Relationships. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2402.12259](https://arxiv.org/abs/2402.12259) · 📚 被引 50
- **作者**: Sebastian Koch, Narunas Vaskevicius, Mirco Colosi, Pedro Hermosilla, Timo Ropinski
- **🏷️ 机构**: Bosch Center for Artificial Intelligence, Robert Bosch Corporate Research, TU Vienna
- **会议**: CVPR 2024
- **摘要（中）**: 针对3D场景图预测依赖固定标签集训练的问题，该论文提出Open3DSG，一种无需标注场景图数据的开放世界3D场景图预测方法。方法将3D场景图预测骨干网络的特征与2D视觉语言基础模型的特征空间对齐，实现零样本预测开放词汇对象类别，并利用接地LLM预测开放集关系。相比现有方法，Open3DSG首次支持开放词汇对象和开放集关系预测。实验表明在预测任意对象类别和复杂关系上有效。
- **摘要（英）**: This paper presents Open3DSG, an open-world 3D scene graph prediction method that eliminates the need for labeled scene graph data. It co-embeds 3D backbone features with 2D vision-language foundation models for zero-shot open-vocabulary object querying and uses a grounded LLM for open-set relationship prediction. As the first method to predict both open-vocabulary objects and open-set relationships, it demonstrates effectiveness on arbitrary categories and complex inter-object relations.
- **核心贡献**: 首次实现3D点云中开放词汇对象和开放集关系的零样本场景图预测。
- **创新点**: 利用2D视觉语言模型和接地LLM实现3D场景图的开放世界预测。
- **结果**: 在预测任意对象类别和复杂关系上表现有效。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Current approaches for 3D scene graph prediction rely on labeled datasets to train models for a fixed set of known object classes and relationship categories. We present Open3DSG, an alternative approach to learn 3D scene graph prediction in an open world without requiring labeled scene graph data. We co-embed the features from a 3D scene graph prediction backbone with the feature space of powerful open world 2D vision language foundation models. This enables us to predict 3D scene graphs from 3D point clouds in a zero-shot manner by querying object classes from an open vocabulary and predicting the inter-object relationships from a grounded LLM with scene graph features and queried object classes as context. Open3DSG is the first 3D point cloud method to predict not only explicit open-vocabulary object classes, but also open-set relationships that are not limited to a predefined label set, making it possible to express rare as well as specific objects and relationships in the predicted 3D scene graph. Our experiments show that Open3DSG is effective at predicting arbitrary object classes as well as their complex inter-object relationships describing spatial, supportive, semantic and comparative relationships.

</details>

### Open3DIS: Open-Vocabulary 3D Instance Segmentation with 2D Mask Guidance. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2312.10671](https://arxiv.org/abs/2312.10671) · 📚 被引 72
- **作者**: Phuc D. A. Nguyen, Tuan Duc Ngo, Evangelos Kalogerakis, Chuang Gan, Anh Tuan Tran, Cuong Pham et al.
- **🏷️ 机构**: VinAI Research, UMass Amherst, MIT-IBM Watson AI Lab
- **会议**: CVPR 2024
- **摘要（中）**: 针对开放词汇3D实例分割中小尺度与几何模糊对象难以识别的问题，该论文提出Open3DIS方法。方法通过新模块聚合跨帧2D实例掩码并映射到几何一致的点云区域，生成高质量对象提议，再与3D类无关提议结合。相比现有方法，显著提升了对多样类别对象的分割性能。在ScanNet200、S3DIS和Replica三个数据集上验证了有效性。
- **摘要（英）**: This paper introduces Open3DIS to address the challenge of identifying small-scale and geometrically ambiguous objects in open-vocabulary 3D instance segmentation. It aggregates 2D instance masks across frames and maps them to coherent point cloud regions as high-quality proposals, combined with 3D class-agnostic proposals. Experiments on ScanNet200, S3DIS, and Replica show significant performance gains across diverse categories.
- **核心贡献**: 提出2D掩码引导的3D开放词汇实例分割方法，提升小物体识别能力。
- **创新点**: 跨帧2D掩码聚合与点云映射生成高质量提议。
- **结果**: 在三个数据集上显著提升分割性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce Open3DIS, a novel solution designed to tackle the problem of Open-Vocabulary Instance Segmentation within 3D scenes. Objects within 3D environments exhibit diverse shapes, scales, and colors, making precise instance-level identification a challenging task. Recent advancements in Open-Vocabulary scene understanding have made significant strides in this area by employing class-agnostic 3D instance proposal networks for object localization and learning queryable features for each 3D mask. While these methods produce high-quality instance proposals, they struggle with identifying small-scale and geometrically ambiguous objects. The key idea of our method is a new module that aggregates 2D instance masks across frames and maps them to geometrically coherent point cloud regions as high-quality object proposals addressing the above limitations. These are then combined with 3D class-agnostic instance proposals to include a wide range of objects in the real world. To validate our approach, we conducted experiments on three prominent datasets, including ScanNet200, S3DIS, and Replica, demonstrating significant performance gains in segmenting objects with diverse categories over the state-of-the-art approaches.

</details>

### Open-Vocabulary 3D Semantic Segmentation with Foundation Models. **⭐⭐⭐** (相关度: 65%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02011) · 📚 被引 28
- **作者**: Li Jiang, Shaoshuai Shi, Bernt Schiele
- **🏷️ 机构**: Max Planck Institute for Informatics, Saarland Informatics Campus
- **会议**: CVPR 2024
- **摘要（中）**: 针对开放词汇3D语义分割依赖标注数据的问题，该论文探索利用基础模型进行开放词汇3D语义分割。方法可能通过将3D特征与视觉语言模型对齐，实现零样本分割。相比传统监督方法，减少了对标注的依赖。但摘要缺失，具体方法和效果不明确。
- **摘要（英）**: This paper explores open-vocabulary 3D semantic segmentation using foundation models, likely by aligning 3D features with vision-language models for zero-shot segmentation. It reduces reliance on labeled data compared to supervised methods, but the abstract is missing, leaving details unclear.
- **核心贡献**: 探索基础模型在开放词汇3D语义分割中的应用。
- **创新点**: 利用视觉语言模型实现3D零样本分割。
- **结果**: 效果未明确。

### Training-Free Open-Vocabulary Segmentation with Offline Diffusion-Augmented Prototype Generation. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2404.06542](https://arxiv.org/abs/2404.06542) · 📚 被引 30
- **作者**: Luca Barsellotti, Roberto Amoroso, Marcella Cornia, Lorenzo Baraldi, Rita Cucchiara
- **🏷️ 机构**: University of Modena and Reggio Emilia,Italy
- **会议**: CVPR 2024
- **摘要（中）**: 针对开放词汇语义分割中训练成本高且定位不精确的问题，该论文提出FreeDA，一种无需训练的扩散增强方法。方法利用扩散模型视觉定位生成概念，结合局部-全局相似度匹配类无关区域与语义类别。离线阶段收集文本-视觉参考嵌入，测试时查询支持匹配。相比训练方法，FreeDA避免了大规模训练开销。在五个数据集上达到最先进性能。
- **摘要（英）**: This paper proposes FreeDA, a training-free diffusion-augmented method for open-vocabulary semantic segmentation, addressing high training costs and imprecise localization. It leverages diffusion models for visual localization and local-global similarities for region-class matching, with offline reference embedding collection. FreeDA achieves state-of-the-art performance on five datasets without large-scale training.
- **核心贡献**: 提出无需训练的扩散增强开放词汇分割方法，降低计算成本。
- **创新点**: 利用扩散模型生成参考嵌入并联合局部-全局匹配。
- **结果**: 在五个数据集上达到最先进性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-vocabulary semantic segmentation aims at segmenting arbitrary categories expressed in textual form. Previous works have trained over large amounts of image-caption pairs to enforce pixel-level multimodal alignments. However, captions provide global information about the semantics of a given image but lack direct localization of individual concepts. Further, training on large-scale datasets inevitably brings significant computational costs. In this paper, we propose FreeDA, a training-free diffusion-augmented method for open-vocabulary semantic segmentation, which leverages the ability of diffusion models to visually localize generated concepts and local-global similarities to match class-agnostic regions with semantic classes. Our approach involves an offline stage in which textual-visual reference embeddings are collected, starting from a large set of captions and leveraging visual and semantic contexts. At test time, these are queried to support the visual matching process, which is carried out by jointly considering class-agnostic regions and global semantic similarities. Extensive analyses demonstrate that FreeDA achieves state-of-the-art performance on five datasets, surpassing previous methods by more than 7.0 average points in terms of mIoU and without requiring any training.

</details>

### Open Vocabulary Semantic Scene Sketch Understanding. **⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2312.12463](https://arxiv.org/abs/2312.12463) · 📚 被引 7
- **作者**: Ahmed Bourouis, Judith Ellen Fan, Yulia Gryaditskaya
- **🏷️ 机构**: Surrey Institute for People-Centered AI and CVSSP, University of Surrey,UK, Stanford University,Department of Psychology,USA
- **会议**: CVPR 2024
- **摘要（中）**: 本文研究抽象手绘场景草图的机器理解问题，提出了一种基于CLIP预训练视觉Transformer的草图编码器，通过视觉提示调优和引入v-v自注意力块，实现语义感知的特征空间。模型采用两级层次设计，第一级编码整体场景，第二级聚焦单个类别，并引入文本-视觉交叉注意力。在语义草图分割任务上，该方法优于零样本CLIP基线，展示了无需像素级标注的泛化能力。
- **摘要（英）**: This paper tackles semantic understanding of abstract freehand scene sketches by proposing a CLIP-based vision transformer encoder with visual prompt tuning and v-v self-attention blocks. A two-level hierarchy enables holistic and category-specific encoding with cross-attention, achieving superior performance over zero-shot CLIP on semantic sketch segmentation without pixel-level annotations.
- **核心贡献**: 提出了一种无需像素标注的开放词汇草图语义分割方法。
- **创新点**: 在CLIP视觉编码器中引入v-v自注意力块和两级层次结构，实现语义解耦。
- **结果**: 在语义草图分割任务上优于零样本CLIP基线。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We study the underexplored but fundamental vision problem of machine understanding of abstract freehand scene sketches. We introduce a sketch encoder that results in semantically-aware feature space, which we evaluate by testing its performance on a semantic sketch segmentation task. To train our model we rely only on the availability of bitmap sketches with their brief captions and do not require any pixel-level annotations. To obtain generalization to a large set of sketches and categories, we build on a vision transformer encoder pretrained with the CLIP model. We freeze the text encoder and perform visual-prompt tuning of the visual encoder branch while introducing a set of critical modifications. Firstly, we augment the classical key-query (k-q) self-attention blocks with value-value (v-v) self-attention blocks. Central to our model is a two-level hierarchical network design that enables efficient semantic disentanglement: The first level ensures holistic scene sketch encoding, and the second level focuses on individual categories. We, then, in the second level of the hierarchy, introduce a cross-attention between textual and visual branches. Our method outperforms zero-shot CLIP pixel accuracy of segmentation results by 37 points, reaching an accuracy of $85.5\%$ on the FS-COCO sketch dataset. Finally, we conduct a user study that allows us to identify further improvements needed over our method to reconcile machine and human understanding of scene sketches.

</details>

### CLIP-Driven Open-Vocabulary 3D Scene Graph Generation via Cross-Modality Contrastive Learning. **⭐⭐** (相关度: 50%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02632) · 📚 被引 26
- **作者**: Lianggangxu Chen, Xuejiao Wang, Jiale Lu, Shaohui Lin, Changbo Wang, Gaoqi He
- **🏷️ 机构**: School of Computer Science and Technology, East China Normal University,Shanghai,China
- **会议**: CVPR 2024
- **摘要（中）**: 该论文摘要为空，无法获取具体内容。根据标题推测，其研究开放词汇3D场景图生成，利用跨模态对比学习驱动CLIP，但缺乏详细信息，难以评估其方法和效果。
- **摘要（英）**: The abstract is empty, so no specific details are available. Based on the title, it likely addresses open-vocabulary 3D scene graph generation via cross-modality contrastive learning with CLIP, but the lack of content prevents a thorough assessment.
- **核心贡献**: 未知，因摘要缺失。
- **创新点**: 未知，因摘要缺失。
- **结果**: 未知，因摘要缺失。

### CAT-Seg: Cost Aggregation for Open-Vocabulary Semantic Segmentation. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2303.11797](https://arxiv.org/abs/2303.11797) · 📚 被引 134
- **作者**: Seokju Cho, Heeseong Shin, Sunghwan Hong, Anurag Arnab, Paul Hongsuck Seo, Seungryong Kim
- **🏷️ 机构**: Korea University, Google Research
- **会议**: CVPR 2024
- **摘要（中）**: 针对开放词汇语义分割中处理未见类别的挑战，本文提出CAT-Seg方法，通过聚合图像与文本嵌入之间的余弦相似度（成本体积）来适配CLIP模型。该方法通过微调编码器，有效处理已见和未见类别，并探索了成本体积的聚合策略和CLIP的高效微调方式。实验表明，CAT-Seg在多个分割基准上优于现有方法，尤其在未见类别上表现突出。
- **摘要（英）**: CAT-Seg introduces a cost-based approach for open-vocabulary semantic segmentation by aggregating cosine similarity between image and text embeddings, adapting CLIP through encoder fine-tuning. It explores cost volume aggregation and efficient fine-tuning strategies, achieving superior performance on seen and unseen classes across benchmarks.
- **核心贡献**: 提出基于成本体积聚合的CLIP适配方法，解决开放词汇分割中的未见类别问题。
- **创新点**: 将成本体积概念引入CLIP微调，并系统研究聚合策略。
- **结果**: 在多个分割基准上超越现有方法，尤其提升未见类别性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-vocabulary semantic segmentation presents the challenge of labeling each pixel within an image based on a wide range of text descriptions. In this work, we introduce a novel cost-based approach to adapt vision-language foundation models, notably CLIP, for the intricate task of semantic segmentation. Through aggregating the cosine similarity score, i.e., the cost volume between image and text embeddings, our method potently adapts CLIP for segmenting seen and unseen classes by fine-tuning its encoders, addressing the challenges faced by existing methods in handling unseen classes. Building upon this, we explore methods to effectively aggregate the cost volume considering its multi-modal nature of being established between image and text embeddings. Furthermore, we examine various methods for efficiently fine-tuning CLIP.

</details>

### Open-vocabulary object 6D pose estimation. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2312.00690](https://arxiv.org/abs/2312.00690) · 📚 被引 20
- **作者**: Jaime Corsetti, Davide Boscaini, Changjae Oh, Andrea Cavallaro, Fabio Poiesi
- **🏷️ 机构**: Fondazione, Queen Mary University, Idiap Research Institute
- **会议**: CVPR 2024
- **摘要（中）**: 本文提出开放词汇物体6D姿态估计的新设置，其中物体仅通过文本提示指定，无需CAD模型或视频序列。方法利用视觉语言模型分割目标物体并估计相对6D姿态，通过融合提示的物体级信息与局部图像特征，实现对新概念的泛化。在REAL275和Toyota-Light数据集上，该方法优于手工方法和深度学习基线，展示了在跨场景中的有效性。
- **摘要（英）**: This paper introduces open-vocabulary object 6D pose estimation, where objects are specified by text prompts without CAD models. A VLM-based approach segments and estimates relative pose by fusing object-level prompt information with local features, outperforming baselines on REAL275 and Toyota-Light datasets.
- **核心贡献**: 首次定义开放词汇6D姿态估计任务，并提出基于VLM的解决方案。
- **创新点**: 利用文本提示融合物体级信息与局部特征，实现无需模型的新类别泛化。
- **结果**: 在34个物体实例上优于手工和深度学习方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce the new setting of open-vocabulary object 6D pose estimation, in which a textual prompt is used to specify the object of interest. In contrast to existing approaches, in our setting (i) the object of interest is specified solely through the textual prompt, (ii) no object model (e.g., CAD or video sequence) is required at inference, and (iii) the object is imaged from two RGBD viewpoints of different scenes. To operate in this setting, we introduce a novel approach that leverages a Vision-Language Model to segment the object of interest from the scenes and to estimate its relative 6D pose. The key of our approach is a carefully devised strategy to fuse object-level information provided by the prompt with local image features, resulting in a feature space that can generalize to novel concepts. We validate our approach on a new benchmark based on two popular datasets, REAL275 and Toyota-Light, which collectively encompass 34 object instances appearing in four thousand image pairs. The results demonstrate that our approach outperforms both a well-established hand-crafted method and a recent deep learning-based baseline in estimating the relative 6D pose of objects in different scenes. Code and dataset are available at https://jcorsetti.github.io/oryon.

</details>

### AnySkill: Learning Open-Vocabulary Physical Skill for Interactive Agents. **⭐⭐⭐** (相关度: 40%)
- **链接**: [arXiv:2403.12835](https://arxiv.org/abs/2403.12835) · 📚 被引 21
- **作者**: Jieming Cui, Tengyu Liu, Nian Liu, Yaodong Yang, Yixin Zhu, Siyuan Huang
- **🏷️ 机构**: Institute for Artificial Intelligence, Peking University, BIGAI,National Key Laboratory of General Artificial Intelligence
- **会议**: CVPR 2024
- **摘要（中）**: 针对物理仿真中运动生成难以适应新场景的问题，本文提出AnySkill，一种分层方法，通过低层控制器学习原子动作，高层策略根据开放词汇指令选择并组合动作，以最大化渲染图像与文本的CLIP相似度。该方法使用基于图像的奖励，无需手动设计奖励函数，能够生成响应未见指令的逼真运动序列，是首个实现开放词汇物理技能学习的交互式智能体方法。
- **摘要（英）**: AnySkill addresses adaptability in physics-based motion generation by using a hierarchical method with a low-level controller for atomic actions and a high-level policy that selects actions to maximize CLIP similarity between rendered images and text. It uses image-based rewards, enabling learning without manual reward engineering, and generates realistic motions for unseen instructions.
- **核心贡献**: 提出首个开放词汇物理技能学习方法，支持交互式智能体。
- **创新点**: 利用CLIP图像-文本相似度作为高层策略奖励，免去手动奖励设计。
- **结果**: 在未见指令上生成逼真运动序列，验证了方法的泛化能力。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Traditional approaches in physics-based motion generation, centered around imitation learning and reward shaping, often struggle to adapt to new scenarios. To tackle this limitation, we propose AnySkill, a novel hierarchical method that learns physically plausible interactions following open-vocabulary instructions. Our approach begins by developing a set of atomic actions via a low-level controller trained via imitation learning. Upon receiving an open-vocabulary textual instruction, AnySkill employs a high-level policy that selects and integrates these atomic actions to maximize the CLIP similarity between the agent's rendered images and the text. An important feature of our method is the use of image-based rewards for the high-level policy, which allows the agent to learn interactions with objects without manual reward engineering. We demonstrate AnySkill's capability to generate realistic and natural motion sequences in response to unseen instructions of varying lengths, marking it the first method capable of open-vocabulary physical skill learning for interactive humanoid agents.

</details>

### Active Open-Vocabulary Recognition: Let Intelligent Moving Mitigate CLIP Limitations. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2311.17938](https://arxiv.org/abs/2311.17938) · 📚 被引 7
- **作者**: Lei Fan, Jianxiong Zhou, Xiaoying Xing, Ying Wu
- **🏷️ 机构**: Northwestern University
- **会议**: CVPR 2024
- **摘要（中）**: ①针对主动开放词汇识别中CLIP模型受视角和遮挡影响导致性能下降，以及序列观测特征融合缺乏有效方法的问题。②提出了一种新的智能体，利用帧间信息进行主动感知和分类，并设计了特征融合策略以保持开放词汇分类的判别力。③相比直接使用CLIP，该方法通过主动移动缓解视角和遮挡问题，并改进了序列特征集成。④实验表明该方法在主动识别任务上显著优于现有基线，具体数据未在摘要中给出。
- **摘要（英）**: This paper addresses the challenges of active open-vocabulary recognition, where CLIP's performance degrades under viewpoint changes and occlusions, and sequential feature integration is inefficient. It proposes a novel agent that leverages inter-frame information for active perception and classification, with a feature fusion strategy to maintain discriminative power. The method outperforms existing baselines in active recognition tasks, though specific metrics are not detailed in the abstract.
- **核心贡献**: 提出了一个主动开放词汇识别框架，通过智能移动和帧间特征融合缓解CLIP的视角和遮挡限制。
- **创新点**: 创新性地利用主动移动策略和跨帧特征集成来增强开放词汇分类的鲁棒性。
- **结果**: 在主动识别任务上取得了优于现有方法的性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Active recognition, which allows intelligent agents to explore observations for better recognition performance, serves as a prerequisite for various embodied AI tasks, such as grasping, navigation and room arrangements. Given the evolving environment and the multitude of object classes, it is impractical to include all possible classes during the training stage. In this paper, we aim at advancing active open-vocabulary recognition, empowering embodied agents to actively perceive and classify arbitrary objects. However, directly adopting recent open-vocabulary classification models, like Contrastive Language Image Pretraining (CLIP), poses its unique challenges. Specifically, we observe that CLIP's performance is heavily affected by the viewpoint and occlusions, compromising its reliability in unconstrained embodied perception scenarios. Further, the sequential nature of observations in agent-environment interactions necessitates an effective method for integrating features that maintains discriminative strength for open-vocabulary classification. To address these issues, we introduce a novel agent for active open-vocabulary recognition. The proposed method leverages inter-frame and inter-concept similarities to navigate agent movements and to fuse features, without relying on class-specific knowledge. Compared to baseline CLIP model with 29.6% accuracy on ShapeNet dataset, the proposed agent could achieve 53.3% accuracy for open-vocabulary recognition, without any fine-tuning to the equipped CLIP model. Additional experiments conducted with the Habitat simulator further affirm the efficacy of our method.

</details>

### Exploring the Potential of Large Foundation Models for Open-Vocabulary HOI Detection. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2404.06194](https://arxiv.org/abs/2404.06194) · 📚 被引 20
- **作者**: Ting Lei, Shaofeng Yin, Yang Liu
- **🏷️ 机构**: Wangxuan Institute of Computer Technology, Peking University
- **会议**: CVPR 2024
- **摘要（中）**: ①针对开放词汇HOI检测中，现有零样本检测器使用相同特征图建模不同距离的人-物对，且仅依赖类别名称而忽略语言上下文信息的问题。②提出了CMD-SE框架，采用条件多级解码和细粒度语义增强，利用视觉-语言模型（VLMs）和大型语言模型（LLMs）如GPT来丰富语义。③通过软约束在二分匹配中为不同距离的交互分配不同级别的特征图，并利用LLM生成上下文描述。④实验表明该方法在开放词汇HOI检测上取得了显著性能提升，具体数据未在摘要中给出。
- **摘要（英）**: This paper tackles the limitations of zero-shot HOI detectors that use uniform feature maps for varying distances and overlook language context. It introduces CMD-SE, an end-to-end framework with conditional multi-level decoding and fine-grained semantic enhancement, leveraging VLMs and LLMs like GPT. The method improves performance in open-vocabulary HOI detection, though specific metrics are not provided in the abstract.
- **核心贡献**: 提出了CMD-SE框架，通过条件多级解码和LLM增强语义，提升了开放词汇HOI检测性能。
- **创新点**: 创新性地在二分匹配中引入软约束以适配不同距离的交互，并利用LLM生成细粒度语义描述。
- **结果**: 在开放词汇HOI检测任务上取得了优于现有方法的性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-vocabulary human-object interaction (HOI) detection, which is concerned with the problem of detecting novel HOIs guided by natural language, is crucial for understanding human-centric scenes. However, prior zero-shot HOI detectors often employ the same levels of feature maps to model HOIs with varying distances, leading to suboptimal performance in scenes containing human-object pairs with a wide range of distances. In addition, these detectors primarily rely on category names and overlook the rich contextual information that language can provide, which is essential for capturing open vocabulary concepts that are typically rare and not well-represented by category names alone. In this paper, we introduce a novel end-to-end open vocabulary HOI detection framework with conditional multi-level decoding and fine-grained semantic enhancement (CMD-SE), harnessing the potential of Visual-Language Models (VLMs). Specifically, we propose to model human-object pairs with different distances with different levels of feature maps by incorporating a soft constraint during the bipartite matching process. Furthermore, by leveraging large language models (LLMs) such as GPT models, we exploit their extensive world knowledge to generate descriptions of human body part states for various interactions. Then we integrate the generalizable and fine-grained semantics of human body parts to improve interaction recognition. Experimental results on two datasets, SWIG-HOI and HICO-DET, demonstrate that our proposed method achieves state-of-the-art results in open vocabulary HOI detection. The code and models are available at https://github.com/ltttpku/CMD-SE-release.

</details>

### OMG: Towards Open-vocabulary Motion Generation via Mixture of Controllers.
- **链接**: [arXiv:2312.08985](https://arxiv.org/abs/2312.08985) · 📚 被引 29
- **作者**: Han Liang, Jiacheng Bao, Ruichi Zhang, Sihan Ren, Yuecheng Xu, Sibei Yang et al.
- **🏷️ 机构**: ShanghaiTecn University, Tencent PCG
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We have recently seen tremendous progress in realistic text-to-motion generation. Yet, the existing methods often fail or produce implausible motions with unseen text inputs, which limits the applications. In this paper, we present OMG, a novel framework, which enables compelling motion generation from zero-shot open-vocabulary text prompts. Our key idea is to carefully tailor the pretrain-then-finetune paradigm into the text-to-motion generation. At the pre-training stage, our model improves the generation ability by learning the rich out-of-domain inherent motion traits. To this end, we scale up a large unconditional diffusion model up to 1B parameters, so as to utilize the massive unlabeled motion data up to over 20M motion instances. At the subsequent fine-tuning stage, we introduce motion ControlNet, which incorporates text prompts as conditioning information, through a trainable copy of the pre-trained model and the proposed novel Mixture-of-Controllers (MoC) block. MoC block adaptively recognizes various ranges of the sub-motions with a cross-attention mechanism and processes them separately with the text-token-specific experts. Such a design effectively aligns the CLIP token embeddings of text prompts to various ranges of compact and expressive motion features. Extensive experiments demonstrate that our OMG achieves significant improvements over the state-of-the-art methods on zero-shot text-to-motion generation. Project page: https://tr3e.github.io/omg-page.

</details>

### Open-Vocabulary Segmentation with Semantic-Assisted Calibration.
- **链接**: [arXiv:2312.04089](https://arxiv.org/abs/2312.04089)
- **作者**: Yong Liu, Sule Bai, Guanbin Li, Yitong Wang, Yansong Tang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper studies open-vocabulary segmentation (OVS) through calibrating in-vocabulary and domain-biased embedding space with generalized contextual prior of CLIP. As the core of open-vocabulary understanding, alignment of visual content with the semantics of unbounded text has become the bottleneck of this field. To address this challenge, recent works propose to utilize CLIP as an additional classifier and aggregate model predictions with CLIP classification results. Despite their remarkable progress, performance of OVS methods in relevant scenarios is still unsatisfactory compared with supervised counterparts. We attribute this to the in-vocabulary embedding and domain-biased CLIP prediction. To this end, we present a Semantic-assisted CAlibration Network (SCAN). In SCAN, we incorporate generalized semantic prior of CLIP into proposal embedding to avoid collapsing on known categories. Besides, a contextual shift strategy is applied to mitigate the lack of global context and unnatural background noise. With above designs, SCAN achieves state-of-the-art performance on all popular open-vocabulary segmentation benchmarks. Furthermore, we also focus on the problem of existing evaluation system that ignores semantic duplication across categories, and propose a new metric called Semantic-Guided IoU (SG-IoU).

</details>

### Language Embedded 3D Gaussians for Open-Vocabulary Scene Understanding.
- **链接**: [arXiv:2311.18482](https://arxiv.org/abs/2311.18482)
- **作者**: Jin-Chuan Shi, Miao Wang, Hao-Bin Duan, Shao-Hua Guan
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-vocabulary querying in 3D space is challenging but essential for scene understanding tasks such as object localization and segmentation. Language-embedded scene representations have made progress by incorporating language features into 3D spaces. However, their efficacy heavily depends on neural networks that are resource-intensive in training and rendering. Although recent 3D Gaussians offer efficient and high-quality novel view synthesis, directly embedding language features in them leads to prohibitive memory usage and decreased performance. In this work, we introduce Language Embedded 3D Gaussians, a novel scene representation for open-vocabulary query tasks. Instead of embedding high-dimensional raw semantic features on 3D Gaussians, we propose a dedicated quantization scheme that drastically alleviates the memory requirement, and a novel embedding procedure that achieves smoother yet high accuracy query, countering the multi-view feature inconsistencies and the high-frequency inductive bias in point-based representations. Our comprehensive experiments show that our representation achieves the best visual quality and language querying accuracy across current language-embedded representations, while maintaining real-time rendering frame rates on a single desktop GPU.

</details>

### GOV-NeSF: Generalizable Open-Vocabulary Neural Semantic Fields.
- **链接**: [arXiv:2404.00931](https://arxiv.org/abs/2404.00931) · 📚 被引 3
- **作者**: Yunsong Wang, Hanlin Chen, Gim Hee Lee
- **🏷️ 机构**: National University of Singapore,Department of Computer Science
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advancements in vision-language foundation models have significantly enhanced open-vocabulary 3D scene understanding. However, the generalizability of existing methods is constrained due to their framework designs and their reliance on 3D data. We address this limitation by introducing Generalizable Open-Vocabulary Neural Semantic Fields (GOV-NeSF), a novel approach offering a generalizable implicit representation of 3D scenes with open-vocabulary semantics. We aggregate the geometry-aware features using a cost volume, and propose a Multi-view Joint Fusion module to aggregate multi-view features through a cross-view attention mechanism, which effectively predicts view-specific blending weights for both colors and open-vocabulary features. Remarkably, our GOV-NeSF exhibits state-of-the-art performance in both 2D and 3D open-vocabulary semantic segmentation, eliminating the need for ground truth semantic labels or depth priors, and effectively generalize across scenes and datasets without fine-tuning.

</details>

### Image-to-Image Matching via Foundation Models: A New Perspective for Open-Vocabulary Semantic Segmentation.
- **链接**: [arXiv:2404.00262](https://arxiv.org/abs/2404.00262) · 📚 被引 21
- **作者**: Yuan Wang, Rui Sun, Naisong Luo, Yuwen Pan, Tianzhu Zhang
- **🏷️ 机构**: University of Science and Technology of China
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-vocabulary semantic segmentation (OVS) aims to segment images of arbitrary categories specified by class labels or captions. However, most previous best-performing methods, whether pixel grouping methods or region recognition methods, suffer from false matches between image features and category labels. We attribute this to the natural gap between the textual features and visual features. In this work, we rethink how to mitigate false matches from the perspective of image-to-image matching and propose a novel relation-aware intra-modal matching (RIM) framework for OVS based on visual foundation models. RIM achieves robust region classification by firstly constructing diverse image-modal reference features and then matching them with region features based on relation-aware ranking distribution. The proposed RIM enjoys several merits. First, the intra-modal reference features are better aligned, circumventing potential ambiguities that may arise in cross-modal matching. Second, the ranking-based matching process harnesses the structure information implicit in the inter-class relationships, making it more robust than comparing individually. Extensive experiments on three benchmarks demonstrate that RIM outperforms previous state-of-the-art methods by large margins, obtaining a lead of more than 10% in mIoU on PASCAL VOC benchmark.

</details>

### Transferable and Principled Efficiency for Open-Vocabulary Segmentation.
- **链接**: [arXiv:2404.07448](https://arxiv.org/abs/2404.07448) · 📚 被引 2
- **作者**: Jingxuan Xu, Wuyang Chen, Yao Zhao, Yunchao Wei
- **🏷️ 机构**: Beijing Jiaotong University, Simon Fraser University
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent success of pre-trained foundation vision-language models makes Open-Vocabulary Segmentation (OVS) possible. Despite the promising performance, this approach introduces heavy computational overheads for two challenges: 1) large model sizes of the backbone; 2) expensive costs during the fine-tuning. These challenges hinder this OVS strategy from being widely applicable and affordable in real-world scenarios. Although traditional methods such as model compression and efficient fine-tuning can address these challenges, they often rely on heuristics. This means that their solutions cannot be easily transferred and necessitate re-training on different models, which comes at a cost. In the context of efficient OVS, we target achieving performance that is comparable to or even better than prior OVS works based on large vision-language foundation models, by utilizing smaller models that incur lower training costs. The core strategy is to make our efficiency principled and thus seamlessly transferable from one OVS framework to others without further customization. Comprehensive experiments on diverse OVS benchmarks demonstrate our superior trade-off between segmentation accuracy and computation costs over previous works. Our code is available on https://github.com/Xujxyang/OpenTrans

</details>

### MaskClustering: View Consensus Based Mask Graph Clustering for Open-Vocabulary 3D Instance Segmentation.
- **链接**: [arXiv:2401.07745](https://arxiv.org/abs/2401.07745) · 📚 被引 41
- **作者**: Mi Yan, Jiazhao Zhang, Yan Zhu, He Wang
- **🏷️ 机构**: CFCS, School of CS, Peking University
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-vocabulary 3D instance segmentation is cutting-edge for its ability to segment 3D instances without predefined categories. However, progress in 3D lags behind its 2D counterpart due to limited annotated 3D data. To address this, recent works first generate 2D open-vocabulary masks through 2D models and then merge them into 3D instances based on metrics calculated between two neighboring frames. In contrast to these local metrics, we propose a novel metric, view consensus rate, to enhance the utilization of multi-view observations. The key insight is that two 2D masks should be deemed part of the same 3D instance if a significant number of other 2D masks from different views contain both these two masks. Using this metric as edge weight, we construct a global mask graph where each mask is a node. Through iterative clustering of masks showing high view consensus, we generate a series of clusters, each representing a distinct 3D instance. Notably, our model is training-free. Through extensive experiments on publicly available datasets, including ScanNet++, ScanNet200 and MatterPort3D, we demonstrate that our method achieves state-of-the-art performance in open-vocabulary 3D instance segmentation. Our project page is at https://pku-epic.github.io/MaskClustering.

</details>

### Visual Programming for Zero-Shot Open-Vocabulary 3D Visual Grounding.
- **链接**: [arXiv:2311.15383](https://arxiv.org/abs/2311.15383) · 📚 被引 39
- **作者**: Zhihao Yuan, Jinke Ren, Chun-Mei Feng, Hengshuang Zhao, Shuguang Cui, Zhen Li
- **🏷️ 机构**: FNii, CUHKSZ, IHPC, A*STAR,Singapore, HKU
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D Visual Grounding (3DVG) aims at localizing 3D object based on textual descriptions. Conventional supervised methods for 3DVG often necessitate extensive annotations and a predefined vocabulary, which can be restrictive. To address this issue, we propose a novel visual programming approach for zero-shot open-vocabulary 3DVG, leveraging the capabilities of large language models (LLMs). Our approach begins with a unique dialog-based method, engaging with LLMs to establish a foundational understanding of zero-shot 3DVG. Building on this, we design a visual program that consists of three types of modules, i.e., view-independent, view-dependent, and functional modules. These modules, specifically tailored for 3D scenarios, work collaboratively to perform complex reasoning and inference. Furthermore, we develop an innovative language-object correlation module to extend the scope of existing 3D object detectors into open-vocabulary scenarios. Extensive experiments demonstrate that our zero-shot approach can outperform some supervised baselines, marking a significant stride towards effective 3DVG.

</details>

### OVER-NAV: Elevating Iterative Vision-and-Language Navigation with Open-Vocabulary Detection and StructurEd Representation.
- **链接**: [arXiv:2403.17334](https://arxiv.org/abs/2403.17334) · 📚 被引 14
- **作者**: Ganlong Zhao, Guanbin Li, Weikai Chen, Yizhou Yu
- **🏷️ 机构**: The University of Hong Kong, Sun Yat-sen University, Digital Content Technology Center, Tencent Games
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advances in Iterative Vision-and-Language Navigation (IVLN) introduce a more meaningful and practical paradigm of VLN by maintaining the agent's memory across tours of scenes. Although the long-term memory aligns better with the persistent nature of the VLN task, it poses more challenges on how to utilize the highly unstructured navigation memory with extremely sparse supervision. Towards this end, we propose OVER-NAV, which aims to go over and beyond the current arts of IVLN techniques. In particular, we propose to incorporate LLMs and open-vocabulary detectors to distill key information and establish correspondence between multi-modal signals. Such a mechanism introduces reliable cross-modal supervision and enables on-the-fly generalization to unseen scenes without the need of extra annotation and re-training. To fully exploit the interpreted navigation data, we further introduce a structured representation, coded Omnigraph, to effectively integrate multi-modal information along the tour. Accompanied with a novel omnigraph fusion mechanism, OVER-NAV is able to extract the most relevant knowledge from omnigraph for a more accurate navigating action. In addition, OVER-NAV seamlessly supports both discrete and continuous environments under a unified framework. We demonstrate the superiority of OVER-NAV in extensive experiments.

</details>

### Self-Supervised Class-Agnostic Motion Prediction with Spatial and Temporal Consistency Regularizations.
- **链接**: [arXiv:2403.13261](https://arxiv.org/abs/2403.13261) · 📚 被引 5
- **作者**: Kewei Wang, Yizheng Wu, Jun Cen, Zhiyu Pan, Xingyi Li, Zhe Wang et al.
- **🏷️ 机构**: School of AIA, Huazhong University of Science and Technology, S-Lab, Nanyang Technological University, SenseTime Research
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The perception of motion behavior in a dynamic environment holds significant importance for autonomous driving systems, wherein class-agnostic motion prediction methods directly predict the motion of the entire point cloud. While most existing methods rely on fully-supervised learning, the manual labeling of point cloud data is laborious and time-consuming. Therefore, several annotation-efficient methods have been proposed to address this challenge. Although effective, these methods rely on weak annotations or additional multi-modal data like images, and the potential benefits inherent in the point cloud sequence are still underexplored. To this end, we explore the feasibility of self-supervised motion prediction with only unlabeled LiDAR point clouds. Initially, we employ an optimal transport solver to establish coarse correspondences between current and future point clouds as the coarse pseudo motion labels. Training models directly using such coarse labels leads to noticeable spatial and temporal prediction inconsistencies. To mitigate these issues, we introduce three simple spatial and temporal regularization losses, which facilitate the self-supervised training process effectively. Experimental results demonstrate the significant superiority of our approach over the state-of-the-art self-supervised methods.

</details>

### Cross-Domain Few-Shot Object Detection via Enhanced Open-Set Object Detector.
- **链接**: [arXiv:2402.03094](https://arxiv.org/abs/2402.03094) · 📚 被引 38
- **作者**: Yuqian Fu, Yu Wang, Yixuan Pan, Lian Huai, Xingyu Qiu, Zeyu Shangguan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper studies the challenging cross-domain few-shot object detection (CD-FSOD), aiming to develop an accurate object detector for novel domains with minimal labeled examples. While transformer-based open-set detectors, such as DE-ViT, show promise in traditional few-shot object detection, their generalization to CD-FSOD remains unclear: 1) can such open-set detection methods easily generalize to CD-FSOD? 2) If not, how can models be enhanced when facing huge domain gaps? To answer the first question, we employ measures including style, inter-class variance (ICV), and indefinable boundaries (IB) to understand the domain gap. Based on these measures, we establish a new benchmark named CD-FSOD to evaluate object detection methods, revealing that most of the current approaches fail to generalize across domains. Technically, we observe that the performance decline is associated with our proposed measures: style, ICV, and IB. Consequently, we propose several novel modules to address these issues. First, the learnable instance features align initial fixed instances with target categories, enhancing feature distinctiveness. Second, the instance reweighting module assigns higher importance to high-quality instances with slight IB. Third, the domain prompter encourages features resilient to different styles by synthesizing imaginary domains without altering semantic contents. These techniques collectively contribute to the development of the Cross-Domain Vision Transformer for CD-FSOD (CD-ViTO), significantly improving upon the base DE-ViT. Experimental results validate the efficacy of our model.

</details>

### MarvelOVD: Marrying Object Recognition and Vision-Language Models for Robust Open-Vocabulary Object Detection.
- **链接**: [arXiv:2407.21465](https://arxiv.org/abs/2407.21465) · 📚 被引 3
- **作者**: Kuo Wang, Lechao Cheng, Weikai Chen, Pingping Zhang, Liang Lin, Fan Zhou et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Learning from pseudo-labels that generated with VLMs~(Vision Language Models) has been shown as a promising solution to assist open vocabulary detection (OVD) in recent studies. However, due to the domain gap between VLM and vision-detection tasks, pseudo-labels produced by the VLMs are prone to be noisy, while the training design of the detector further amplifies the bias. In this work, we investigate the root cause of VLMs' biased prediction under the OVD context. Our observations lead to a simple yet effective paradigm, coded MarvelOVD, that generates significantly better training targets and optimizes the learning procedure in an online manner by marrying the capability of the detector with the vision-language model. Our key insight is that the detector itself can act as a strong auxiliary guidance to accommodate VLM's inability of understanding both the ``background'' and the context of a proposal within the image. Based on it, we greatly purify the noisy pseudo-labels via Online Mining and propose Adaptive Reweighting to effectively suppress the biased training boxes that are not well aligned with the target object. In addition, we also identify a neglected ``base-novel-conflict'' problem and introduce stratified label assignments to prevent it. Extensive experiments on COCO and LVIS datasets demonstrate that our method outperforms the other state-of-the-arts by significant margins. Codes are available at https://github.com/wkfdb/MarvelOVD

</details>

### Find n' Propagate: Open-Vocabulary 3D Object Detection in Urban Environments.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73661-2_8) · 📚 被引 3
- **作者**: Djamahl Etchegaray, Zi Huang, Tatsuya Harada, Yadan Luo
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Unlocking Textual and Visual Wisdom: Open-Vocabulary 3D Object Detection Enhanced by Comprehensive Guidance from Text and Image.
- **链接**: [arXiv:2407.05256](https://arxiv.org/abs/2407.05256) · 📚 被引 7
- **作者**: Pengkun Jiao, Na Zhao, Jingjing Chen, Yu-Gang Jiang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-vocabulary 3D object detection (OV-3DDet) aims to localize and recognize both seen and previously unseen object categories within any new 3D scene. While language and vision foundation models have achieved success in handling various open-vocabulary tasks with abundant training data, OV-3DDet faces a significant challenge due to the limited availability of training data. Although some pioneering efforts have integrated vision-language models (VLM) knowledge into OV-3DDet learning, the full potential of these foundational models has yet to be fully exploited. In this paper, we unlock the textual and visual wisdom to tackle the open-vocabulary 3D detection task by leveraging the language and vision foundation models. We leverage a vision foundation model to provide image-wise guidance for discovering novel classes in 3D scenes. Specifically, we utilize a object detection vision foundation model to enable the zero-shot discovery of objects in images, which serves as the initial seeds and filtering guidance to identify novel 3D objects. Additionally, to align the 3D space with the powerful vision-language space, we introduce a hierarchical alignment approach, where the 3D feature space is aligned with the vision-language feature space using a pre-trained VLM at the instance, category, and scene levels. Through extensive experimentation, we demonstrate significant improvements in accuracy and generalization, highlighting the potential of foundation models in advancing open-vocabulary 3D object detection in real-world scenarios.

</details>

### Toward Open Vocabulary Aerial Object Detection with CLIP-Activated Student-Teacher Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73016-0_25) · 📚 被引 17
- **作者**: Yan Li, Weiwei Guo, Xue Yang, Ning Liao, Dunyun He, Jiaqi Zhou et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### CLIFF: Continual Latent Diffusion for Open-Vocabulary Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73001-6_15) · 📚 被引 7
- **作者**: Wuyang Li, Xinyu Liu, Jiayi Ma, Yixuan Yuan
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### SMILe: Leveraging Submodular Mutual Information For Robust Few-Shot Object Detection.
- **链接**: [arXiv:2407.02665](https://arxiv.org/abs/2407.02665) · 📚 被引 6
- **作者**: Anay Majee, Ryan Sharp, Rishabh K. Iyer
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Confusion and forgetting of object classes have been challenges of prime interest in Few-Shot Object Detection (FSOD). To overcome these pitfalls in metric learning based FSOD techniques, we introduce a novel Submodular Mutual Information Learning (SMILe) framework which adopts combinatorial mutual information functions to enforce the creation of tighter and discriminative feature clusters in FSOD. Our proposed approach generalizes to several existing approaches in FSOD, agnostic of the backbone architecture demonstrating elevated performance gains. A paradigm shift from instance based objective functions to combinatorial objectives in SMILe naturally preserves the diversity within an object class resulting in reduced forgetting when subjected to few training examples. Furthermore, the application of mutual information between the already learnt (base) and newly added (novel) objects ensures sufficient separation between base and novel classes, minimizing the effect of class confusion. Experiments on popular FSOD benchmarks, PASCAL-VOC and MS-COCO show that our approach generalizes to State-of-the-Art (SoTA) approaches improving their novel class performance by up to 5.7% (3.3 mAP points) and 5.4% (2.6 mAP points) on the 10-shot setting of VOC (split 3) and 30-shot setting of COCO datasets respectively. Our experiments also demonstrate better retention of base class performance and up to 2x faster convergence over existing approaches agnostic of the underlying architecture.

</details>

### OV-Uni3DETR: Towards Unified Open-Vocabulary 3D Object Detection via Cycle-Modality Propagation.
- **链接**: [arXiv:2403.19580](https://arxiv.org/abs/2403.19580) · 📚 被引 10
- **作者**: Zhenyu Wang, Yali Li, Taichi Liu, Hengshuang Zhao, Shengjin Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In the current state of 3D object detection research, the severe scarcity of annotated 3D data, substantial disparities across different data modalities, and the absence of a unified architecture, have impeded the progress towards the goal of universality. In this paper, we propose \textbf{OV-Uni3DETR}, a unified open-vocabulary 3D detector via cycle-modality propagation. Compared with existing 3D detectors, OV-Uni3DETR offers distinct advantages: 1) Open-vocabulary 3D detection: During training, it leverages various accessible data, especially extensive 2D detection images, to boost training diversity. During inference, it can detect both seen and unseen classes. 2) Modality unifying: It seamlessly accommodates input data from any given modality, effectively addressing scenarios involving disparate modalities or missing sensor information, thereby supporting test-time modality switching. 3) Scene unifying: It provides a unified multi-modal model architecture for diverse scenes collected by distinct sensors. Specifically, we propose the cycle-modality propagation, aimed at propagating knowledge bridging 2D and 3D modalities, to support the aforementioned functionalities. 2D semantic knowledge from large-vocabulary learning guides novel class discovery in the 3D domain, and 3D geometric knowledge provides localization supervision for 2D detection images. OV-Uni3DETR achieves the state-of-the-art performance on various scenarios, surpassing existing methods by more than 6\% on average. Its performance using only RGB images is on par with or even surpasses that of previous point cloud based methods. Code and pre-trained models will be released later.

</details>

### OpenSight: A Simple Open-Vocabulary Framework for LiDAR-Based Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72907-2_1) · 📚 被引 12
- **作者**: Hu Zhang, Jianhua Xu, Tao Tang, Haiyang Sun, Xin Yu, Zi Huang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Dual-Level Adaptive Self-labeling for Novel Class Discovery in Point Cloud Segmentation.
- **链接**: [arXiv:2407.12489](https://arxiv.org/abs/2407.12489) · 📚 被引 4
- **作者**: Ruijie Xu, Chuyu Zhang, Hui Ren, Xuming He
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We tackle the novel class discovery in point cloud segmentation, which discovers novel classes based on the semantic knowledge of seen classes. Existing work proposes an online point-wise clustering method with a simplified equal class-size constraint on the novel classes to avoid degenerate solutions. However, the inherent imbalanced distribution of novel classes in point clouds typically violates the equal class-size constraint. Moreover, point-wise clustering ignores the rich spatial context information of objects, which results in less expressive representation for semantic segmentation. To address the above challenges, we propose a novel self-labeling strategy that adaptively generates high-quality pseudo-labels for imbalanced classes during model training. In addition, we develop a dual-level representation that incorporates regional consistency into the point-level classifier learning, reducing noise in generated segmentation. Finally, we conduct extensive experiments on two widely used datasets, SemanticKITTI and SemanticPOSS, and the results show our method outperforms the state of the art by a large margin.

</details>

### Zero-Shot Detection of AI-Generated Images.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72649-1_4)
- **作者**: Davide Cozzolino, Giovanni Poggi, Matthias Nießner, Luisa Verdoliva
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Towards Multimodal Open-Set Domain Generalization and Adaptation Through Self-supervision.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73202-7_16) · 📚 被引 10
- **作者**: Hao Dong, Eleni N. Chatzi, Olga Fink
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Dense Multimodal Alignment for Open-Vocabulary 3D Scene Understanding.
- **链接**: [arXiv:2407.09781](https://arxiv.org/abs/2407.09781) · 📚 被引 5
- **作者**: Ruihuang Li, Zhengqiang Zhang, Chenhang He, Zhiyuan Ma, Vishal M. Patel, Lei Zhang
- **🏷️ 机构**: PolyU / OPPO
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent vision-language pre-training models have exhibited remarkable generalization ability in zero-shot recognition tasks. Previous open-vocabulary 3D scene understanding methods mostly focus on training 3D models using either image or text supervision while neglecting the collective strength of all modalities. In this work, we propose a Dense Multimodal Alignment (DMA) framework to densely co-embed different modalities into a common space for maximizing their synergistic benefits. Instead of extracting coarse view- or region-level text prompts, we leverage large vision-language models to extract complete category information and scalable scene descriptions to build the text modality, and take image modality as the bridge to build dense point-pixel-text associations. Besides, in order to enhance the generalization ability of the 2D model for downstream 3D tasks without compromising the open-vocabulary capability, we employ a dual-path integration approach to combine frozen CLIP visual features and learnable mask features. Extensive experiments show that our DMA method produces highly competitive open-vocabulary segmentation performance on various indoor and outdoor tasks.

</details>

### MoMA: Multimodal LLM Adapter for Fast Personalized Image Generation.
- **链接**: [arXiv:2404.05674](https://arxiv.org/abs/2404.05674) · 📚 被引 20
- **作者**: Kunpeng Song, Yizhe Zhu, Bingchen Liu, Qing Yan, Ahmed Elgammal, Xiao Yang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we present MoMA: an open-vocabulary, training-free personalized image model that boasts flexible zero-shot capabilities. As foundational text-to-image models rapidly evolve, the demand for robust image-to-image translation grows. Addressing this need, MoMA specializes in subject-driven personalized image generation. Utilizing an open-source, Multimodal Large Language Model (MLLM), we train MoMA to serve a dual role as both a feature extractor and a generator. This approach effectively synergizes reference image and text prompt information to produce valuable image features, facilitating an image diffusion model. To better leverage the generated features, we further introduce a novel self-attention shortcut method that efficiently transfers image features to an image diffusion model, improving the resemblance of the target object in generated images. Remarkably, as a tuning-free plug-and-play module, our model requires only a single reference image and outperforms existing methods in generating images with high detail fidelity, enhanced identity-preservation and prompt faithfulness. Our work is open-source, thereby providing universal access to these advancements.

</details>

### FreeMotion: MoCap-Free Human Motion Synthesis with Multimodal Large Language Models.
- **链接**: [arXiv:2406.10740](https://arxiv.org/abs/2406.10740) · 📚 被引 4
- **作者**: Zhikai Zhang, Yitang Li, Haofeng Huang, Mingxian Lin, Li Yi
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Human motion synthesis is a fundamental task in computer animation. Despite recent progress in this field utilizing deep learning and motion capture data, existing methods are always limited to specific motion categories, environments, and styles. This poor generalizability can be partially attributed to the difficulty and expense of collecting large-scale and high-quality motion data. At the same time, foundation models trained with internet-scale image and text data have demonstrated surprising world knowledge and reasoning ability for various downstream tasks. Utilizing these foundation models may help with human motion synthesis, which some recent works have superficially explored. However, these methods didn't fully unveil the foundation models' potential for this task and only support several simple actions and environments. In this paper, we for the first time, without any motion data, explore open-set human motion synthesis using natural language instructions as user control signals based on MLLMs across any motion task and environment. Our framework can be split into two stages: 1) sequential keyframe generation by utilizing MLLMs as a keyframe designer and animator; 2) motion filling between keyframes through interpolation and motion tracking. Our method can achieve general human motion synthesis for many downstream tasks. The promising results demonstrate the worth of mocap-free human motion synthesis aided by MLLMs and pave the way for future research.

</details>

### OpenPSG: Open-Set Panoptic Scene Graph Generation via Large Multimodal Models.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72684-2_12) · 📚 被引 11
- **作者**: Zijian Zhou, Zheng Zhu, Holger Caesar, Miaojing Shi
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Self-cooperation Knowledge Distillation for Novel Class Discovery.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72897-6_26) · 📚 被引 4
- **作者**: Yuzheng Wang, Zhaoyu Chen, Dingkang Yang, Yunquan Sun, Lizhe Qi
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### 3D Open-Vocabulary Panoptic Segmentation with 2D-3D Vision-Language Distillation.
- **链接**: [arXiv:2401.02402](https://arxiv.org/abs/2401.02402) · 📚 被引 5
- **作者**: Zihao Xiao, Longlong Jing, Shangxuan Wu, Alex Zihao Zhu, Jingwei Ji, Chiyu Max Jiang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D panoptic segmentation is a challenging perception task, especially in autonomous driving. It aims to predict both semantic and instance annotations for 3D points in a scene. Although prior 3D panoptic segmentation approaches have achieved great performance on closed-set benchmarks, generalizing these approaches to unseen things and unseen stuff categories remains an open problem. For unseen object categories, 2D open-vocabulary segmentation has achieved promising results that solely rely on frozen CLIP backbones and ensembling multiple classification outputs. However, we find that simply extending these 2D models to 3D does not guarantee good performance due to poor per-mask classification quality, especially for novel stuff categories. In this paper, we propose the first method to tackle 3D open-vocabulary panoptic segmentation. Our model takes advantage of the fusion between learnable LiDAR features and dense frozen vision CLIP features, using a single classification head to make predictions for both base and novel classes. To further improve the classification performance on novel classes and leverage the CLIP model, we propose two novel loss functions: object-level distillation loss and voxel-level distillation loss. Our experiments on the nuScenes and SemanticKITTI datasets show that our method outperforms the strong baseline by a large margin.

</details>

### LLMs Meet VLMs: Boost Open Vocabulary Object Detection with Fine-grained Descriptors.
- **链接**: [arXiv:2402.04630](https://arxiv.org/abs/2402.04630)
- **作者**: Sheng Jin, Xueying Jiang, Jiaxing Huang, Lewei Lu, Shijian Lu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Inspired by the outstanding zero-shot capability of vision language models (VLMs) in image classification tasks, open-vocabulary object detection has attracted increasing interest by distilling the broad VLM knowledge into detector training. However, most existing open-vocabulary detectors learn by aligning region embeddings with categorical labels (e.g., bicycle) only, disregarding the capability of VLMs on aligning visual embeddings with fine-grained text description of object parts (e.g., pedals and bells). This paper presents DVDet, a Descriptor-Enhanced Open Vocabulary Detector that introduces conditional context prompts and hierarchical textual descriptors that enable precise region-text alignment as well as open-vocabulary detection training in general. Specifically, the conditional context prompt transforms regional embeddings into image-like representations that can be directly integrated into general open vocabulary detection training. In addition, we introduce large language models as an interactive and implicit knowledge repository which enables iterative mining and refining visually oriented textual descriptors for precise region-text alignment. Extensive experiments over multiple large-scale benchmarks show that DVDet outperforms the state-of-the-art consistently by large margins.

</details>

### TextField3D: Towards Enhancing Open-Vocabulary 3D Generation with Noisy Text Fields.
- **链接**: [arXiv:2309.17175](https://arxiv.org/abs/2309.17175)
- **作者**: Tianyu Huang, Yihan Zeng, Bowen Dong, Hang Xu, Songcen Xu, Rynson W. H. Lau et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent works learn 3D representation explicitly under text-3D guidance. However, limited text-3D data restricts the vocabulary scale and text control of generations. Generators may easily fall into a stereotype concept for certain text prompts, thus losing open-vocabulary generation ability. To tackle this issue, we introduce a conditional 3D generative model, namely TextField3D. Specifically, rather than using the text prompts as input directly, we suggest to inject dynamic noise into the latent space of given text prompts, i.e., Noisy Text Fields (NTFs). In this way, limited 3D data can be mapped to the appropriate range of textual latent space that is expanded by NTFs. To this end, an NTFGen module is proposed to model general text latent code in noisy fields. Meanwhile, an NTFBind module is proposed to align view-invariant image latent code to noisy fields, further supporting image-conditional 3D generation. To guide the conditional generation in both geometry and texture, multi-modal discrimination is constructed with a text-3D discriminator and a text-2.5D discriminator. Compared to previous methods, TextField3D includes three merits: 1) large vocabulary, 2) text consistency, and 3) low latency. Extensive experiments demonstrate that our method achieves a potential open-vocabulary 3D generation capability.

</details>

### FROSTER: Frozen CLIP is A Strong Teacher for Open-Vocabulary Action Recognition.
- **链接**: [arXiv:2402.03241](https://arxiv.org/abs/2402.03241)
- **作者**: Xiaohu Huang, Hao Zhou, Kun Yao, Kai Han
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we introduce FROSTER, an effective framework for open-vocabulary action recognition. The CLIP model has achieved remarkable success in a range of image-based tasks, benefiting from its strong generalization capability stemming from pretaining on massive image-text pairs. However, applying CLIP directly to the open-vocabulary action recognition task is challenging due to the absence of temporal information in CLIP's pretraining. Further, fine-tuning CLIP on action recognition datasets may lead to overfitting and hinder its generalizability, resulting in unsatisfactory results when dealing with unseen actions. To address these issues, FROSTER employs a residual feature distillation approach to ensure that CLIP retains its generalization capability while effectively adapting to the action recognition task. Specifically, the residual feature distillation treats the frozen CLIP model as a teacher to maintain the generalizability exhibited by the original CLIP and supervises the feature learning for the extraction of video-specific features to bridge the gap between images and videos. Meanwhile, it uses a residual sub-network for feature distillation to reach a balance between the two distinct objectives of learning generalizable and video-specific features. We extensively evaluate FROSTER on open-vocabulary action recognition benchmarks under both base-to-novel and cross-dataset settings. FROSTER consistently achieves state-of-the-art performance on all datasets across the board. Project page: https://visual-ai.github.io/froster.

</details>

### Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.
- **链接**: [arXiv:2310.05130](https://arxiv.org/abs/2310.05130)
- **作者**: Guangsheng Bao, Yanbin Zhao, Zhiyang Teng, Linyi Yang, Yue Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large language models (LLMs) have shown the ability to produce fluent and cogent content, presenting both productivity opportunities and societal risks. To build trustworthy AI systems, it is imperative to distinguish between machine-generated and human-authored content. The leading zero-shot detector, DetectGPT, showcases commendable performance but is marred by its intensive computational costs. In this paper, we introduce the concept of conditional probability curvature to elucidate discrepancies in word choices between LLMs and humans within a given context. Utilizing this curvature as a foundational metric, we present **Fast-DetectGPT**, an optimized zero-shot detector, which substitutes DetectGPT's perturbation step with a more efficient sampling step. Our evaluations on various datasets, source models, and test conditions indicate that Fast-DetectGPT not only surpasses DetectGPT by a relative around 75% in both the white-box and black-box settings but also accelerates the detection process by a factor of 340, as detailed in Table 1. See \url{https://github.com/baoguangsheng/fast-detect-gpt} for code, data, and results.

</details>

### Negative Label Guided OOD Detection with Pretrained Vision-Language Models.
- **链接**: [arXiv:2403.20078](https://arxiv.org/abs/2403.20078)
- **作者**: Xue Jiang, Feng Liu, Zhen Fang, Hong Chen, Tongliang Liu, Feng Zheng et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Out-of-distribution (OOD) detection aims at identifying samples from unknown classes, playing a crucial role in trustworthy models against errors on unexpected inputs. Extensive research has been dedicated to exploring OOD detection in the vision modality. Vision-language models (VLMs) can leverage both textual and visual information for various multi-modal applications, whereas few OOD detection methods take into account information from the text modality. In this paper, we propose a novel post hoc OOD detection method, called NegLabel, which takes a vast number of negative labels from extensive corpus databases. We design a novel scheme for the OOD score collaborated with negative labels. Theoretical analysis helps to understand the mechanism of negative labels. Extensive experiments demonstrate that our method NegLabel achieves state-of-the-art performance on various OOD detection benchmarks and generalizes well on multiple VLM architectures. Furthermore, our method NegLabel exhibits remarkable robustness against diverse domain shifts. The codes are available at https://github.com/tmlr-group/NegLabel.

</details>

### Overcoming the Pitfalls of Vision-Language Model Finetuning for OOD Generalization.
- **链接**: [arXiv:2401.15914](https://arxiv.org/abs/2401.15914)
- **作者**: Yuhang Zang, Hanlin Goh, Joshua M. Susskind, Chen Huang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing vision-language models exhibit strong generalization on a variety of visual domains and tasks. However, such models mainly perform zero-shot recognition in a closed-set manner, and thus struggle to handle open-domain visual concepts by design. There are recent finetuning methods, such as prompt learning, that not only study the discrimination between in-distribution (ID) and out-of-distribution (OOD) samples, but also show some improvements in both ID and OOD accuracies. In this paper, we first demonstrate that vision-language models, after long enough finetuning but without proper regularization, tend to overfit the known classes in the given dataset, with degraded performance on unknown classes. Then we propose a novel approach OGEN to address this pitfall, with the main focus on improving the OOD GENeralization of finetuned models. Specifically, a class-conditional feature generator is introduced to synthesize OOD features using just the class name of any unknown class. Such synthesized features will provide useful knowledge about unknowns and help regularize the decision boundary between ID and OOD data when optimized jointly. Equally important is our adaptive self-distillation mechanism to regularize our feature generation model during joint optimization, i.e., adaptively transferring knowledge between model states to further prevent overfitting. Experiments validate that our method yields convincing gains in OOD generalization performance in different settings. Code: https://github.com/apple/ml-ogen.

</details>

### Open-Vocabulary Calibration for Fine-tuned CLIP.
- **链接**: [出版页](https://proceedings.mlr.press/v235/wang24bw.html)
- **作者**: Shuoyuan Wang, Jindong Wang, Guoqing Wang, Bob Zhang, Kaiyang Zhou, Hongxin Wei
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### A Touch, Vision, and Language Dataset for Multimodal Alignment.
- **链接**: [arXiv:2402.13232](https://arxiv.org/abs/2402.13232)
- **作者**: Letian Fu, Gaurav Datta, Huang Huang, William Chung-Ho Panitch, Jaimyn Drake, Joseph Ortiz et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Touch is an important sensing modality for humans, but it has not yet been incorporated into a multimodal generative language model. This is partially due to the difficulty of obtaining natural language labels for tactile data and the complexity of aligning tactile readings with both visual observations and language descriptions. As a step towards bridging that gap, this work introduces a new dataset of 44K in-the-wild vision-touch pairs, with English language labels annotated by humans (10%) and textual pseudo-labels from GPT-4V (90%). We use this dataset to train a vision-language-aligned tactile encoder for open-vocabulary classification and a touch-vision-language (TVL) model for text generation using the trained encoder. Results suggest that by incorporating touch, the TVL model improves (+29% classification accuracy) touch-vision-language alignment over existing models trained on any pair of those modalities. Although only a small fraction of the dataset is human-labeled, the TVL model demonstrates improved visual-tactile understanding over GPT-4V (+12%) and open-source vision-language models (+32%) on a new touch-vision understanding benchmark. Code and data: https://tactile-vlm.github.io.

</details>

### Open-Vocabulary Object Detection via Language Hierarchy.
- **链接**: [arXiv:2410.20371](https://arxiv.org/abs/2410.20371) · 📚 被引 7
- **作者**: Jiaxing Huang, Jingyi Zhang, Kai Jiang, Shijian Lu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent studies on generalizable object detection have attracted increasing attention with additional weak supervision from large-scale datasets with image-level labels. However, weakly-supervised detection learning often suffers from image-to-box label mismatch, i.e., image-level labels do not convey precise object information. We design Language Hierarchical Self-training (LHST) that introduces language hierarchy into weakly-supervised detector training for learning more generalizable detectors. LHST expands the image-level labels with language hierarchy and enables co-regularization between the expanded labels and self-training. Specifically, the expanded labels regularize self-training by providing richer supervision and mitigating the image-to-box label mismatch, while self-training allows assessing and selecting the expanded labels according to the predicted reliability. In addition, we design language hierarchical prompt generation that introduces language hierarchy into prompt generation which helps bridge the vocabulary gaps between training and testing. Extensive experiments show that the proposed techniques achieve superior generalization performance consistently across 14 widely studied object detection datasets.

</details>

### DiPEx: Dispersing Prompt Expansion for Class-Agnostic Object Detection.
- **链接**: [arXiv:2406.14924](https://arxiv.org/abs/2406.14924) · 📚 被引 2
- **作者**: Jia Syuen Lim, Zhuoxiao Chen, Zhi Chen, Mahsa Baktashmotlagh, Xin Yu, Zi Huang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Class-agnostic object detection (OD) can be a cornerstone or a bottleneck for many downstream vision tasks. Despite considerable advancements in bottom-up and multi-object discovery methods that leverage basic visual cues to identify salient objects, consistently achieving a high recall rate remains difficult due to the diversity of object types and their contextual complexity. In this work, we investigate using vision-language models (VLMs) to enhance object detection via a self-supervised prompt learning strategy. Our initial findings indicate that manually crafted text queries often result in undetected objects, primarily because detection confidence diminishes when the query words exhibit semantic overlap. To address this, we propose a Dispersing Prompt Expansion (DiPEx) approach. DiPEx progressively learns to expand a set of distinct, non-overlapping hyperspherical prompts to enhance recall rates, thereby improving performance in downstream tasks such as out-of-distribution OD. Specifically, DiPEx initiates the process by self-training generic parent prompts and selecting the one with the highest semantic uncertainty for further expansion. The resulting child prompts are expected to inherit semantics from their parent prompts while capturing more fine-grained semantics. We apply dispersion losses to ensure high inter-class discrepancy among child prompts while preserving semantic consistency between parent-child prompt pairs. To prevent excessive growth of the prompt sets, we utilize the maximum angular coverage (MAC) of the semantic space as a criterion for early termination. We demonstrate the effectiveness of DiPEx through extensive class-agnostic OD and OOD-OD experiments on MS-COCO and LVIS, surpassing other prompting methods by up to 20.1\% in AR and achieving a 21.3\% AP improvement over SAM. The code is available at https://github.com/jason-lim26/DiPEx.

</details>

### UMB: Understanding Model Behavior for Open-World Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/8766fbc68e1ed1cdef712ce273e0a363-Abstract-Conference.html) · 📚 被引 2
- **作者**: Xing Xi, Yangyang Huang, Zhijie Zhong, Ronghua Luo
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### OpenGaussian: Towards Point-Level 3D Gaussian-based Open Vocabulary Understanding.
- **链接**: [arXiv:2406.02058](https://arxiv.org/abs/2406.02058) · 📚 被引 22
- **作者**: Yanmin Wu, Jiarui Meng, Haijie Li, Chenming Wu, Yahao Shi, Xinhua Cheng et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper introduces OpenGaussian, a method based on 3D Gaussian Splatting (3DGS) capable of 3D point-level open vocabulary understanding. Our primary motivation stems from observing that existing 3DGS-based open vocabulary methods mainly focus on 2D pixel-level parsing. These methods struggle with 3D point-level tasks due to weak feature expressiveness and inaccurate 2D-3D feature associations. To ensure robust feature presentation and 3D point-level understanding, we first employ SAM masks without cross-frame associations to train instance features with 3D consistency. These features exhibit both intra-object consistency and inter-object distinction. Then, we propose a two-stage codebook to discretize these features from coarse to fine levels. At the coarse level, we consider the positional information of 3D points to achieve location-based clustering, which is then refined at the fine level. Finally, we introduce an instance-level 3D-2D feature association method that links 3D points to 2D masks, which are further associated with 2D CLIP features. Extensive experiments, including open vocabulary-based 3D object selection, 3D point cloud understanding, click-based 3D object selection, and ablation studies, demonstrate the effectiveness of our proposed method. The source code is available at our project page: https://3d-aigc.github.io/OpenGaussian

</details>

### Understanding Multi-Granularity for Open-Vocabulary Part Segmentation.
- **链接**: [arXiv:2406.11384](https://arxiv.org/abs/2406.11384) · 📚 被引 3
- **作者**: Jiho Choi, Seonho Lee, Seungho Lee, Minhyun Lee, Hyunjung Shim
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-vocabulary part segmentation (OVPS) is an emerging research area focused on segmenting fine-grained entities using diverse and previously unseen vocabularies. Our study highlights the inherent complexities of part segmentation due to intricate boundaries and diverse granularity, reflecting the knowledge-based nature of part identification. To address these challenges, we propose PartCLIPSeg, a novel framework utilizing generalized parts and object-level contexts to mitigate the lack of generalization in fine-grained parts. PartCLIPSeg integrates competitive part relationships and attention control, alleviating ambiguous boundaries and underrepresented parts. Experimental results demonstrate that PartCLIPSeg outperforms existing state-of-the-art OVPS methods, offering refined segmentation and an advanced understanding of part relationships within images. Through extensive experiments, our model demonstrated a significant improvement over the state-of-the-art models on the Pascal-Part-116, ADE20K-Part-234, and PartImageNet datasets.

</details>

### Renovating Names in Open-Vocabulary Segmentation Benchmarks.
- **链接**: [arXiv:2403.09593](https://arxiv.org/abs/2403.09593) · 📚 被引 1
- **作者**: Haiwen Huang, Songyou Peng, Dan Zhang, Andreas Geiger
- **🏷️ 机构**: University of Tübingen
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Names are essential to both human cognition and vision-language models. Open-vocabulary models utilize class names as text prompts to generalize to categories unseen during training. However, the precision of these names is often overlooked in existing datasets. In this paper, we address this underexplored problem by presenting a framework for "renovating" names in open-vocabulary segmentation benchmarks (RENOVATE). Our framework features a renaming model that enhances the quality of names for each visual segment. Through experiments, we demonstrate that our renovated names help train stronger open-vocabulary models with up to 15% relative improvement and significantly enhance training efficiency with improved data quality. We also show that our renovated names improve evaluation by better measuring misclassification and enabling fine-grained model analysis. We will provide our code and relabelings for several popular segmentation datasets (MS COCO, ADE20K, Cityscapes) to the research community.

</details>

### Relationship Prompt Learning is Enough for Open-Vocabulary Semantic Segmentation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/8773cdaf02c5af3528e05f1cee816129-Abstract-Conference.html) · 📚 被引 4
- **作者**: Jiahao Li, Yang Lu, Yuan Xie, Yanyun Qu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Towards Open-Vocabulary Semantic Segmentation Without Semantic Labels.
- **链接**: [arXiv:2409.19846](https://arxiv.org/abs/2409.19846) · 📚 被引 6
- **作者**: Heeseong Shin, Chaehyun Kim, Sunghwan Hong, Seokju Cho, Anurag Arnab, Paul Hongsuck Seo et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large-scale vision-language models like CLIP have demonstrated impressive open-vocabulary capabilities for image-level tasks, excelling in recognizing what objects are present. However, they struggle with pixel-level recognition tasks like semantic segmentation, which additionally require understanding where the objects are located. In this work, we propose a novel method, PixelCLIP, to adapt the CLIP image encoder for pixel-level understanding by guiding the model on where, which is achieved using unlabeled images and masks generated from vision foundation models such as SAM and DINO. To address the challenges of leveraging masks without semantic labels, we devise an online clustering algorithm using learnable class names to acquire general semantic concepts. PixelCLIP shows significant performance improvements over CLIP and competitive results compared to caption-supervised methods in open-vocabulary semantic segmentation. Project page is available at https://cvlab-kaist.github.io/PixelCLIP

</details>

### XMask3D: Cross-modal Mask Reasoning for Open Vocabulary 3D Semantic Segmentation.
- **链接**: [arXiv:2411.13243](https://arxiv.org/abs/2411.13243)
- **作者**: Ziyi Wang, Yanbo Wang, Xumin Yu, Jie Zhou, Jiwen Lu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing methodologies in open vocabulary 3D semantic segmentation primarily concentrate on establishing a unified feature space encompassing 3D, 2D, and textual modalities. Nevertheless, traditional techniques such as global feature alignment or vision-language model distillation tend to impose only approximate correspondence, struggling notably with delineating fine-grained segmentation boundaries. To address this gap, we propose a more meticulous mask-level alignment between 3D features and the 2D-text embedding space through a cross-modal mask reasoning framework, XMask3D. In our approach, we developed a mask generator based on the denoising UNet from a pre-trained diffusion model, leveraging its capability for precise textual control over dense pixel representations and enhancing the open-world adaptability of the generated masks. We further integrate 3D global features as implicit conditions into the pre-trained 2D denoising UNet, enabling the generation of segmentation masks with additional 3D geometry awareness. Subsequently, the generated 2D masks are employed to align mask-level 3D representations with the vision-language feature space, thereby augmenting the open vocabulary capability of 3D geometry embeddings. Finally, we fuse complementary 2D and 3D mask features, resulting in competitive performance across multiple benchmarks for 3D open vocabulary semantic segmentation. Code is available at https://github.com/wangzy22/XMask3D.

</details>

### BendVLM: Test-Time Debiasing of Vision-Language Embeddings.
- **链接**: [arXiv:2411.04420](https://arxiv.org/abs/2411.04420) · 📚 被引 4
- **作者**: Walter Gerych, Haoran Zhang, Kimia Hamidieh, Eileen Pan, Maanas K. Sharma, Tom Hartvigsen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-language model (VLM) embeddings have been shown to encode biases present in their training data, such as societal biases that prescribe negative characteristics to members of various racial and gender identities. VLMs are being quickly adopted for a variety of tasks ranging from few-shot classification to text-guided image generation, making debiasing VLM embeddings crucial. Debiasing approaches that fine-tune the VLM often suffer from catastrophic forgetting. On the other hand, fine-tuning-free methods typically utilize a "one-size-fits-all" approach that assumes that correlation with the spurious attribute can be explained using a single linear direction across all possible inputs. In this work, we propose Bend-VLM, a nonlinear, fine-tuning-free approach for VLM embedding debiasing that tailors the debiasing operation to each unique input. This allows for a more flexible debiasing approach. Additionally, we do not require knowledge of the set of inputs a priori to inference time, making our method more appropriate for online, open-set tasks such as retrieval and text guided image generation.

</details>

## 跨领域论文（完整笔记在其他领域）

- Retrieval-Augmented Open-Vocabulary Object Detection. → [vlm](../vlm/Guideline%202024.md)
- Scene-adaptive and Region-aware Multi-modal Prompt for Open Vocabulary Object Detection. → [multimodal](../multimodal/Guideline%202024.md)
- The Devil is in the Fine-Grained Details: Evaluating open-Vocabulary Object Detectors for Fine-Grained Understanding. → [vlm](../vlm/Guideline%202024.md)
- From Pixels to Graphs: Open-Vocabulary Scene Graph Generation with Vision-Language Models. → [vlm](../vlm/Guideline%202024.md)
- Emergent Open-Vocabulary Semantic Segmentation from Off-the-Shelf Vision-Language Models. → [vlm](../vlm/Guideline%202024.md)
- OVMR: Open-Vocabulary Recognition with Multi-Modal References. → [multimodal](../multimodal/Guideline%202024.md)
- OVFoodSeg: Elevating Open-Vocabulary Food Image Segmentation via Image-Informed Textual Representation. → [vlm](../vlm/Guideline%202024.md)
- SED: A Simple Encoder-Decoder for Open-Vocabulary Semantic Segmentation. → [vlm](../vlm/Guideline%202024.md)
- RegionPLC: Regional Point-Language Contrastive Learning for Open-World 3D Scene Understanding. → [self-supervised-vision](../self-supervised-vision/Guideline%202024.md)
- ArGue: Attribute-Guided Prompt Tuning for Vision-Language Models. → [vlm](../vlm/Guideline%202024.md)
- OmniSeg3D: Omniversal 3D Segmentation via Hierarchical Contrastive Learning. → [self-supervised-vision](../self-supervised-vision/Guideline%202024.md)
- EfficientSAM: Leveraged Masked Image Pretraining for Efficient Segment Anything. → [self-supervised-vision](../self-supervised-vision/Guideline%202024.md)
- Continual Learning and Unknown Object Discovery in 3D Scenes via Self-distillation. → [continual-learning](../continual-learning/Guideline%202024.md)
- Anytime Continual Learning for Open Vocabulary Classification. → [continual-learning](../continual-learning/Guideline%202024.md)
- Rethinking Few-Shot Class-Incremental Learning: Learning from Yourself. → [continual-learning](../continual-learning/Guideline%202024.md)
- Open Vocabulary 3D Scene Understanding via Geometry Guided Self-Distillation. → [knowledge-distillation](../knowledge-distillation/Guideline%202024.md)
- CLIPSelf: Vision Transformer Distills Itself for Open-Vocabulary Dense Prediction. → [vision-transformer](../vision-transformer/Guideline%202024.md)
- Compositional Few-Shot Class-Incremental Learning. → [continual-learning](../continual-learning/Guideline%202024.md)
- ImOV3D: Learning Open Vocabulary Point Clouds 3D Object Detection from Only 2D Images. → [3d-detection](../3d-detection/Guideline%202024.md)
- Training an Open-Vocabulary Monocular 3D Detection Model without 3D Data. → [3d-detection](../3d-detection/Guideline%202024.md)


## 🆕 增量新增

### Retrieval-Augmented Open-Vocabulary Object Detection. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01650)
- **作者**: Jooyeon Kim, Eulrang Cho, Sehyung Kim, Hyunwoo J. Kim
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024
- **摘要（中）**: ①针对开放词汇目标检测中模型对未见类别泛化能力不足的问题。②提出了检索增强的开放词汇检测框架，通过外部知识库检索相关区域-文本对作为辅助监督信号，增强模型对未知类别的识别能力。③相比传统方法仅依赖预训练视觉-语言模型，该方法引入了动态检索机制，使模型能利用更丰富的语义上下文。④在LVIS和COCO等基准上显著提升了未见类别的检测精度，尤其在小样本类别上表现突出。
- **摘要（英）**: This work tackles limited generalization to unseen categories in open-vocabulary detection by introducing a retrieval-augmented framework that fetches relevant region-text pairs from external knowledge bases as auxiliary supervision. It outperforms methods relying solely on pretrained VLMs, notably improving rare-category detection on LVIS and COCO.
- **核心贡献**: 提出检索增强的开放词汇检测训练范式。
- **创新点**: 动态外部知识检索提供辅助监督。
- **结果**: 在LVIS/COCO上显著提升未见类别检测精度。

### The Devil is in the Fine-Grained Details: Evaluating open-Vocabulary Object Detectors for Fine-Grained Understanding. **⭐⭐⭐⭐** (相关度: 82%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02125)
- **作者**: Lorenzo Bianchi, Fabio Carrara, Nicola Messina, Claudio Gennaro, Fabrizio Falchi
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024
- **摘要（中）**: 针对开放词汇目标检测器在细粒度理解上的不足，系统评估了现有检测器在细粒度类别上的表现。通过构建细粒度评估基准，发现现有方法在区分相似类别时存在明显缺陷。提出了改进方向，强调细粒度特征的重要性。
- **摘要（英）**: Systematically evaluates open-vocabulary object detectors on fine-grained understanding. Constructs a fine-grained benchmark revealing significant weaknesses in distinguishing similar categories. Highlights the need for improved fine-grained feature learning.
- **核心贡献**: 构建了细粒度开放词汇检测评估基准，并分析现有方法缺陷。
- **创新点**: 创新性地聚焦细粒度评估，揭示检测器在相似类别上的性能瓶颈。
- **结果**: 发现现有检测器在细粒度任务上性能显著下降。

### SED: A Simple Encoder-Decoder for Open-Vocabulary Semantic Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00329)
- **作者**: Bin Xie, Jiale Cao, Jin Xie, Fahad Shahbaz Khan, Yanwei Pang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024
<!-- COMPLETE v1 papers=79 -->
