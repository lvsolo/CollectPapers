# Open-set Detection — 2024 Guideline

> 领域: 开放类检测总类（开放词表 OVD / 开放世界 OWOD / 开集 OOD / 未知类检测）
> 论文数: 40 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### VideoGrounding-DINO: Towards Open-Vocabulary Spatio- Temporal Video Grounding.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01789)
- **作者**: Syed Talal Wasim, Muzammal Naseer, Salman H. Khan, Ming-Hsuan Yang, Fahad Shahbaz Khan
- **🏷️ 机构**: UC Merced
- **会议**: CVPR 2024

### Open3DSG: Open-Vocabulary 3D Scene Graphs from Point Clouds with Queryable Objects and Open-Set Relationships.
- **链接**: [arXiv:2402.12259](https://arxiv.org/abs/2402.12259) · 📚 被引 50
- **作者**: Sebastian Koch, Narunas Vaskevicius, Mirco Colosi, Pedro Hermosilla, Timo Ropinski
- **🏷️ 机构**: Bosch Center for Artificial Intelligence, Robert Bosch Corporate Research, TU Vienna
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Current approaches for 3D scene graph prediction rely on labeled datasets to train models for a fixed set of known object classes and relationship categories. We present Open3DSG, an alternative approach to learn 3D scene graph prediction in an open world without requiring labeled scene graph data. We co-embed the features from a 3D scene graph prediction backbone with the feature space of powerful open world 2D vision language foundation models. This enables us to predict 3D scene graphs from 3D point clouds in a zero-shot manner by querying object classes from an open vocabulary and predicting the inter-object relationships from a grounded LLM with scene graph features and queried object classes as context. Open3DSG is the first 3D point cloud method to predict not only explicit open-vocabulary object classes, but also open-set relationships that are not limited to a predefined label set, making it possible to express rare as well as specific objects and relationships in the predicted 3D scene graph. Our experiments show that Open3DSG is effective at predicting arbitrary object classes as well as their complex inter-object relationships describing spatial, supportive, semantic and comparative relationships.

### Open3DIS: Open-Vocabulary 3D Instance Segmentation with 2D Mask Guidance.
- **链接**: [arXiv:2312.10671](https://arxiv.org/abs/2312.10671) · 📚 被引 72
- **作者**: Phuc D. A. Nguyen, Tuan Duc Ngo, Evangelos Kalogerakis, Chuang Gan, Anh Tuan Tran, Cuong Pham et al.
- **🏷️ 机构**: VinAI Research, UMass Amherst, MIT-IBM Watson AI Lab
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > We introduce Open3DIS, a novel solution designed to tackle the problem of Open-Vocabulary Instance Segmentation within 3D scenes. Objects within 3D environments exhibit diverse shapes, scales, and colors, making precise instance-level identification a challenging task. Recent advancements in Open-Vocabulary scene understanding have made significant strides in this area by employing class-agnostic 3D instance proposal networks for object localization and learning queryable features for each 3D mask. While these methods produce high-quality instance proposals, they struggle with identifying small-scale and geometrically ambiguous objects. The key idea of our method is a new module that aggregates 2D instance masks across frames and maps them to geometrically coherent point cloud regions as high-quality object proposals addressing the above limitations. These are then combined with 3D class-agnostic instance proposals to include a wide range of objects in the real world. To validate our approach, we conducted experiments on three prominent datasets, including ScanNet200, S3DIS, and Replica, demonstrating significant performance gains in segmenting objects with diverse categories over the state-of-the-art approaches.

### Open-Vocabulary 3D Semantic Segmentation with Foundation Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02011) · 📚 被引 28
- **作者**: Li Jiang, Shaoshuai Shi, Bernt Schiele
- **🏷️ 机构**: Max Planck Institute for Informatics, Saarland Informatics Campus
- **会议**: CVPR 2024

### Training-Free Open-Vocabulary Segmentation with Offline Diffusion-Augmented Prototype Generation.
- **链接**: [arXiv:2404.06542](https://arxiv.org/abs/2404.06542) · 📚 被引 30
- **作者**: Luca Barsellotti, Roberto Amoroso, Marcella Cornia, Lorenzo Baraldi, Rita Cucchiara
- **🏷️ 机构**: University of Modena and Reggio Emilia,Italy
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Open-vocabulary semantic segmentation aims at segmenting arbitrary categories expressed in textual form. Previous works have trained over large amounts of image-caption pairs to enforce pixel-level multimodal alignments. However, captions provide global information about the semantics of a given image but lack direct localization of individual concepts. Further, training on large-scale datasets inevitably brings significant computational costs. In this paper, we propose FreeDA, a training-free diffusion-augmented method for open-vocabulary semantic segmentation, which leverages the ability of diffusion models to visually localize generated concepts and local-global similarities to match class-agnostic regions with semantic classes. Our approach involves an offline stage in which textual-visual reference embeddings are collected, starting from a large set of captions and leveraging visual and semantic contexts. At test time, these are queried to support the visual matching process, which is carried out by jointly considering class-agnostic regions and global semantic similarities. Extensive analyses demonstrate that FreeDA achieves state-of-the-art performance on five datasets, surpassing previous methods by more than 7.0 average points in terms of mIoU and without requiring any training.

### The Devil is in the Fine-Grained Details: Evaluating open-Vocabulary Object Detectors for Fine-Grained Understanding.
- **链接**: [arXiv:2311.17518](https://arxiv.org/abs/2311.17518) · 📚 被引 16
- **作者**: Lorenzo Bianchi, Fabio Carrara, Nicola Messina, Claudio Gennaro, Fabrizio Falchi
- **🏷️ 机构**: CNR-ISTI,Pisa,Italy
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Recent advancements in large vision-language models enabled visual object detection in open-vocabulary scenarios, where object classes are defined in free-text formats during inference. In this paper, we aim to probe the state-of-the-art methods for open-vocabulary object detection to determine to what extent they understand fine-grained properties of objects and their parts. To this end, we introduce an evaluation protocol based on dynamic vocabulary generation to test whether models detect, discern, and assign the correct fine-grained description to objects in the presence of hard-negative classes. We contribute with a benchmark suite of increasing difficulty and probing different properties like color, pattern, and material. We further enhance our investigation by evaluating several state-of-the-art open-vocabulary object detectors using the proposed protocol and find that most existing solutions, which shine in standard open-vocabulary benchmarks, struggle to accurately capture and distinguish finer object details. We conclude the paper by highlighting the limitations of current methodologies and exploring promising research directions to overcome the discovered drawbacks. Data and code are available at https://lorebianchi98.github.io/FG-OVD/.

### Open Vocabulary Semantic Scene Sketch Understanding.
- **链接**: [arXiv:2312.12463](https://arxiv.org/abs/2312.12463) · 📚 被引 7
- **作者**: Ahmed Bourouis, Judith Ellen Fan, Yulia Gryaditskaya
- **🏷️ 机构**: Surrey Institute for People-Centered AI and CVSSP, University of Surrey,UK, Stanford University,Department of Psychology,USA
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > We study the underexplored but fundamental vision problem of machine understanding of abstract freehand scene sketches. We introduce a sketch encoder that results in semantically-aware feature space, which we evaluate by testing its performance on a semantic sketch segmentation task. To train our model we rely only on the availability of bitmap sketches with their brief captions and do not require any pixel-level annotations. To obtain generalization to a large set of sketches and categories, we build on a vision transformer encoder pretrained with the CLIP model. We freeze the text encoder and perform visual-prompt tuning of the visual encoder branch while introducing a set of critical modifications. Firstly, we augment the classical key-query (k-q) self-attention blocks with value-value (v-v) self-attention blocks. Central to our model is a two-level hierarchical network design that enables efficient semantic disentanglement: The first level ensures holistic scene sketch encoding, and the second level focuses on individual categories. We, then, in the second level of the hierarchy, introduce a cross-attention between textual and visual branches. Our method outperforms zero-shot CLIP pixel accuracy of segmentation results by 37 points, reaching an accuracy of $85.5\%$ on the FS-COCO sketch dataset. Finally, we conduct a user study that allows us to identify further improvements needed over our method to reconcile machine and human understanding of scene sketches.

### CLIP-Driven Open-Vocabulary 3D Scene Graph Generation via Cross-Modality Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02632)
- **作者**: Lianggangxu Chen, Xuejiao Wang, Jiale Lu, Shaohui Lin, Changbo Wang, Gaoqi He
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### CAT-Seg: Cost Aggregation for Open-Vocabulary Semantic Segmentation.
- **链接**: [arXiv:2303.11797](https://arxiv.org/abs/2303.11797) · 📚 被引 134
- **作者**: Seokju Cho, Heeseong Shin, Sunghwan Hong, Anurag Arnab, Paul Hongsuck Seo, Seungryong Kim
- **🏷️ 机构**: Korea University, Google Research
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Open-vocabulary semantic segmentation presents the challenge of labeling each pixel within an image based on a wide range of text descriptions. In this work, we introduce a novel cost-based approach to adapt vision-language foundation models, notably CLIP, for the intricate task of semantic segmentation. Through aggregating the cosine similarity score, i.e., the cost volume between image and text embeddings, our method potently adapts CLIP for segmenting seen and unseen classes by fine-tuning its encoders, addressing the challenges faced by existing methods in handling unseen classes. Building upon this, we explore methods to effectively aggregate the cost volume considering its multi-modal nature of being established between image and text embeddings. Furthermore, we examine various methods for efficiently fine-tuning CLIP.

### Open-vocabulary object 6D pose estimation.
- **链接**: [arXiv:2312.00690](https://arxiv.org/abs/2312.00690) · 📚 被引 20
- **作者**: Jaime Corsetti, Davide Boscaini, Changjae Oh, Andrea Cavallaro, Fabio Poiesi
- **🏷️ 机构**: Fondazione, Queen Mary University, Idiap Research Institute
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > We introduce the new setting of open-vocabulary object 6D pose estimation, in which a textual prompt is used to specify the object of interest. In contrast to existing approaches, in our setting (i) the object of interest is specified solely through the textual prompt, (ii) no object model (e.g., CAD or video sequence) is required at inference, and (iii) the object is imaged from two RGBD viewpoints of different scenes. To operate in this setting, we introduce a novel approach that leverages a Vision-Language Model to segment the object of interest from the scenes and to estimate its relative 6D pose. The key of our approach is a carefully devised strategy to fuse object-level information provided by the prompt with local image features, resulting in a feature space that can generalize to novel concepts. We validate our approach on a new benchmark based on two popular datasets, REAL275 and Toyota-Light, which collectively encompass 34 object instances appearing in four thousand image pairs. The results demonstrate that our approach outperforms both a well-established hand-crafted method and a recent deep learning-based baseline in estimating the relative 6D pose of objects in different scenes. Code and dataset are available at https://jcorsetti.github.io/oryon.

### AnySkill: Learning Open-Vocabulary Physical Skill for Interactive Agents.
- **链接**: [arXiv:2403.12835](https://arxiv.org/abs/2403.12835) · 📚 被引 21
- **作者**: Jieming Cui, Tengyu Liu, Nian Liu, Yaodong Yang, Yixin Zhu, Siyuan Huang
- **🏷️ 机构**: Institute for Artificial Intelligence, Peking University, BIGAI,National Key Laboratory of General Artificial Intelligence
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Traditional approaches in physics-based motion generation, centered around imitation learning and reward shaping, often struggle to adapt to new scenarios. To tackle this limitation, we propose AnySkill, a novel hierarchical method that learns physically plausible interactions following open-vocabulary instructions. Our approach begins by developing a set of atomic actions via a low-level controller trained via imitation learning. Upon receiving an open-vocabulary textual instruction, AnySkill employs a high-level policy that selects and integrates these atomic actions to maximize the CLIP similarity between the agent's rendered images and the text. An important feature of our method is the use of image-based rewards for the high-level policy, which allows the agent to learn interactions with objects without manual reward engineering. We demonstrate AnySkill's capability to generate realistic and natural motion sequences in response to unseen instructions of varying lengths, marking it the first method capable of open-vocabulary physical skill learning for interactive humanoid agents.

### Active Open-Vocabulary Recognition: Let Intelligent Moving Mitigate CLIP Limitations.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01551)
- **作者**: Lei Fan, Jianxiong Zhou, Xiaoying Xing, Ying Wu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### Exploring the Potential of Large Foundation Models for Open-Vocabulary HOI Detection.
- **链接**: [arXiv:2404.06194](https://arxiv.org/abs/2404.06194) · [代码](https://github.com/ltttpku/CMD-SE-release) · 📚 被引 20
- **作者**: Ting Lei, Shaofeng Yin, Yang Liu
- **🏷️ 机构**: Wangxuan Institute of Computer Technology, Peking University
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Open-vocabulary human-object interaction (HOI) detection, which is concerned with the problem of detecting novel HOIs guided by natural language, is crucial for understanding human-centric scenes. However, prior zero-shot HOI detectors often employ the same levels of feature maps to model HOIs with varying distances, leading to suboptimal performance in scenes containing human-object pairs with a wide range of distances. In addition, these detectors primarily rely on category names and overlook the rich contextual information that language can provide, which is essential for capturing open vocabulary concepts that are typically rare and not well-represented by category names alone. In this paper, we introduce a novel end-to-end open vocabulary HOI detection framework with conditional multi-level decoding and fine-grained semantic enhancement (CMD-SE), harnessing the potential of Visual-Language Models (VLMs). Specifically, we propose to model human-object pairs with different distances with different levels of feature maps by incorporating a soft constraint during the bipartite matching process. Furthermore, by leveraging large language models (LLMs) such as GPT models, we exploit their extensive world knowledge to generate descriptions of human body part states for various interactions. Then we integrate the generalizable and fine-grained semantics of human body parts to improve interaction recognition. Experimental results on two datasets, SWIG-HOI and HICO-DET, demonstrate that our proposed method achieves state-of-the-art results in open vocabulary HOI detection. The code and models are available at https://github.com/ltttpku/CMD-SE-release.

### From Pixels to Graphs: Open-Vocabulary Scene Graph Generation with Vision-Language Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02652)
- **作者**: Rongjie Li, Songyang Zhang, Dahua Lin, Kai Chen, Xuming He
- **🏷️ 机构**: CUHK
- **会议**: CVPR 2024

### OMG: Towards Open-vocabulary Motion Generation via Mixture of Controllers.
- **链接**: [arXiv:2312.08985](https://arxiv.org/abs/2312.08985) · 📚 被引 29
- **作者**: Han Liang, Jiacheng Bao, Ruichi Zhang, Sihan Ren, Yuecheng Xu, Sibei Yang et al.
- **🏷️ 机构**: ShanghaiTecn University, Tencent PCG
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > We have recently seen tremendous progress in realistic text-to-motion generation. Yet, the existing methods often fail or produce implausible motions with unseen text inputs, which limits the applications. In this paper, we present OMG, a novel framework, which enables compelling motion generation from zero-shot open-vocabulary text prompts. Our key idea is to carefully tailor the pretrain-then-finetune paradigm into the text-to-motion generation. At the pre-training stage, our model improves the generation ability by learning the rich out-of-domain inherent motion traits. To this end, we scale up a large unconditional diffusion model up to 1B parameters, so as to utilize the massive unlabeled motion data up to over 20M motion instances. At the subsequent fine-tuning stage, we introduce motion ControlNet, which incorporates text prompts as conditioning information, through a trainable copy of the pre-trained model and the proposed novel Mixture-of-Controllers (MoC) block. MoC block adaptively recognizes various ranges of the sub-motions with a cross-attention mechanism and processes them separately with the text-token-specific experts. Such a design effectively aligns the CLIP token embeddings of text prompts to various ranges of compact and expressive motion features. Extensive experiments demonstrate that our OMG achieves significant improvements over the state-of-the-art methods on zero-shot text-to-motion generation. Project page: https://tr3e.github.io/omg-page.

### Open-Vocabulary Segmentation with Semantic-Assisted Calibration.
- **链接**: [arXiv:2312.04089](https://arxiv.org/abs/2312.04089)
- **作者**: Yong Liu, Sule Bai, Guanbin Li, Yitong Wang, Yansong Tang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > This paper studies open-vocabulary segmentation (OVS) through calibrating in-vocabulary and domain-biased embedding space with generalized contextual prior of CLIP. As the core of open-vocabulary understanding, alignment of visual content with the semantics of unbounded text has become the bottleneck of this field. To address this challenge, recent works propose to utilize CLIP as an additional classifier and aggregate model predictions with CLIP classification results. Despite their remarkable progress, performance of OVS methods in relevant scenarios is still unsatisfactory compared with supervised counterparts. We attribute this to the in-vocabulary embedding and domain-biased CLIP prediction. To this end, we present a Semantic-assisted CAlibration Network (SCAN). In SCAN, we incorporate generalized semantic prior of CLIP into proposal embedding to avoid collapsing on known categories. Besides, a contextual shift strategy is applied to mitigate the lack of global context and unnatural background noise. With above designs, SCAN achieves state-of-the-art performance on all popular open-vocabulary segmentation benchmarks. Furthermore, we also focus on the problem of existing evaluation system that ignores semantic duplication across categories, and propose a new metric called Semantic-Guided IoU (SG-IoU).

### Emergent Open-Vocabulary Semantic Segmentation from Off-the-Shelf Vision-Language Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00386)
- **作者**: Jiayun Luo, Siddhesh Khandelwal, Leonid Sigal, Boyang Li
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### Open-Vocabulary Attention Maps with Token Optimization for Semantic Segmentation in Diffusion Models.
- **链接**: [arXiv:2403.14291](https://arxiv.org/abs/2403.14291) · 📚 被引 16
- **作者**: Pablo Marcos-Manchón, Roberto Alcover-Couso, Juan C. SanMiguel, Jose M. Martínez
- **🏷️ 机构**: VPULab, University of Madrid,Spain
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Diffusion models represent a new paradigm in text-to-image generation. Beyond generating high-quality images from text prompts, models such as Stable Diffusion have been successfully extended to the joint generation of semantic segmentation pseudo-masks. However, current extensions primarily rely on extracting attentions linked to prompt words used for image synthesis. This approach limits the generation of segmentation masks derived from word tokens not contained in the text prompt. In this work, we introduce Open-Vocabulary Attention Maps (OVAM)-a training-free method for text-to-image diffusion models that enables the generation of attention maps for any word. In addition, we propose a lightweight optimization process based on OVAM for finding tokens that generate accurate attention maps for an object class with a single annotation. We evaluate these tokens within existing state-of-the-art Stable Diffusion extensions. The best-performing model improves its mIoU from 52.1 to 86.6 for the synthetic images' pseudo-masks, demonstrating that our optimized tokens are an efficient way to improve the performance of existing methods without architectural changes or retraining.

### Open-Vocabulary Semantic Segmentation with Image Embedding Balancing.
- **链接**: [arXiv:2406.09829](https://arxiv.org/abs/2406.09829) · [代码](https://github.com/slonetime/EBSeg) · 📚 被引 26
- **作者**: Xiangheng Shan, Dongyue Wu, Guilin Zhu, Yuanjie Shao, Nong Sang, Changxin Gao
- **🏷️ 机构**: National Key Laboratory of Multispectral Information Intelligent Processing Technology, School of Artificial Intelligence and Automation, Huazhong University of Science and Technology
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Open-vocabulary semantic segmentation is a challenging task, which requires the model to output semantic masks of an image beyond a close-set vocabulary. Although many efforts have been made to utilize powerful CLIP models to accomplish this task, they are still easily overfitting to training classes due to the natural gaps in semantic information between training and new classes. To overcome this challenge, we propose a novel framework for openvocabulary semantic segmentation called EBSeg, incorporating an Adaptively Balanced Decoder (AdaB Decoder) and a Semantic Structure Consistency loss (SSC Loss). The AdaB Decoder is designed to generate different image embeddings for both training and new classes. Subsequently, these two types of embeddings are adaptively balanced to fully exploit their ability to recognize training classes and generalization ability for new classes. To learn a consistent semantic structure from CLIP, the SSC Loss aligns the inter-classes affinity in the image feature space with that in the text feature space of CLIP, thereby improving the generalization ability of our model. Furthermore, we employ a frozen SAM image encoder to complement the spatial information that CLIP features lack due to the low training image resolution and image-level supervision inherent in CLIP. Extensive experiments conducted across various benchmarks demonstrate that the proposed EBSeg outperforms the state-of-the-art methods. Our code and trained models will be here: https://github.com/slonetime/EBSeg.

### Language Embedded 3D Gaussians for Open-Vocabulary Scene Understanding.
- **链接**: [arXiv:2311.18482](https://arxiv.org/abs/2311.18482) · 📚 被引 0
- **作者**: Jin-Chuan Shi, Miao Wang, Hao-Bin Duan, Shao-Hua Guan
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Open-vocabulary querying in 3D space is challenging but essential for scene understanding tasks such as object localization and segmentation. Language-embedded scene representations have made progress by incorporating language features into 3D spaces. However, their efficacy heavily depends on neural networks that are resource-intensive in training and rendering. Although recent 3D Gaussians offer efficient and high-quality novel view synthesis, directly embedding language features in them leads to prohibitive memory usage and decreased performance. In this work, we introduce Language Embedded 3D Gaussians, a novel scene representation for open-vocabulary query tasks. Instead of embedding high-dimensional raw semantic features on 3D Gaussians, we propose a dedicated quantization scheme that drastically alleviates the memory requirement, and a novel embedding procedure that achieves smoother yet high accuracy query, countering the multi-view feature inconsistencies and the high-frequency inductive bias in point-based representations. Our comprehensive experiments show that our representation achieves the best visual quality and language querying accuracy across current language-embedded representations, while maintaining real-time rendering frame rates on a single desktop GPU.

### GOV-NeSF: Generalizable Open-Vocabulary Neural Semantic Fields.
- **链接**: [arXiv:2404.00931](https://arxiv.org/abs/2404.00931) · 📚 被引 3
- **作者**: Yunsong Wang, Hanlin Chen, Gim Hee Lee
- **🏷️ 机构**: National University of Singapore,Department of Computer Science
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Recent advancements in vision-language foundation models have significantly enhanced open-vocabulary 3D scene understanding. However, the generalizability of existing methods is constrained due to their framework designs and their reliance on 3D data. We address this limitation by introducing Generalizable Open-Vocabulary Neural Semantic Fields (GOV-NeSF), a novel approach offering a generalizable implicit representation of 3D scenes with open-vocabulary semantics. We aggregate the geometry-aware features using a cost volume, and propose a Multi-view Joint Fusion module to aggregate multi-view features through a cross-view attention mechanism, which effectively predicts view-specific blending weights for both colors and open-vocabulary features. Remarkably, our GOV-NeSF exhibits state-of-the-art performance in both 2D and 3D open-vocabulary semantic segmentation, eliminating the need for ground truth semantic labels or depth priors, and effectively generalize across scenes and datasets without fine-tuning.

### USE: Universal Segment Embeddings for Open-Vocabulary Image Segmentation.
- **链接**: [arXiv:2406.05271](https://arxiv.org/abs/2406.05271) · 📚 被引 20
- **作者**: Xiaoqi Wang, Wenbin He, Xiwei Xuan, Clint Sebastian, Jorge Piazentin Ono, Xin Li et al.
- **🏷️ 机构**: Bosch Research North America, Bosch Center for Artificial Intelligence (BCAI)
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > The open-vocabulary image segmentation task involves partitioning images into semantically meaningful segments and classifying them with flexible text-defined categories. The recent vision-based foundation models such as the Segment Anything Model (SAM) have shown superior performance in generating class-agnostic image segments. The main challenge in open-vocabulary image segmentation now lies in accurately classifying these segments into text-defined categories. In this paper, we introduce the Universal Segment Embedding (USE) framework to address this challenge. This framework is comprised of two key components: 1) a data pipeline designed to efficiently curate a large amount of segment-text pairs at various granularities, and 2) a universal segment embedding model that enables precise segment classification into a vast range of text-defined categories. The USE model can not only help open-vocabulary image segmentation but also facilitate other downstream tasks (e.g., querying and ranking). Through comprehensive experimental studies on semantic segmentation and part segmentation benchmarks, we demonstrate that the USE framework outperforms state-of-the-art open-vocabulary segmentation methods.

### Image-to-Image Matching via Foundation Models: A New Perspective for Open-Vocabulary Semantic Segmentation.
- **链接**: [arXiv:2404.00262](https://arxiv.org/abs/2404.00262) · 📚 被引 21
- **作者**: Yuan Wang, Rui Sun, Naisong Luo, Yuwen Pan, Tianzhu Zhang
- **🏷️ 机构**: University of Science and Technology of China
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Open-vocabulary semantic segmentation (OVS) aims to segment images of arbitrary categories specified by class labels or captions. However, most previous best-performing methods, whether pixel grouping methods or region recognition methods, suffer from false matches between image features and category labels. We attribute this to the natural gap between the textual features and visual features. In this work, we rethink how to mitigate false matches from the perspective of image-to-image matching and propose a novel relation-aware intra-modal matching (RIM) framework for OVS based on visual foundation models. RIM achieves robust region classification by firstly constructing diverse image-modal reference features and then matching them with region features based on relation-aware ranking distribution. The proposed RIM enjoys several merits. First, the intra-modal reference features are better aligned, circumventing potential ambiguities that may arise in cross-modal matching. Second, the ranking-based matching process harnesses the structure information implicit in the inter-class relationships, making it more robust than comparing individually. Extensive experiments on three benchmarks demonstrate that RIM outperforms previous state-of-the-art methods by large margins, obtaining a lead of more than 10% in mIoU on PASCAL VOC benchmark.

### OVFoodSeg: Elevating Open-Vocabulary Food Image Segmentation via Image-Informed Textual Representation.
- **链接**: [arXiv:2404.01409](https://arxiv.org/abs/2404.01409) · 📚 被引 10
- **作者**: Xiongwei Wu, Sicheng Yu, Ee-Peng Lim, Chong-Wah Ngo
- **🏷️ 机构**: Singapore Management University
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > In the realm of food computing, segmenting ingredients from images poses substantial challenges due to the large intra-class variance among the same ingredients, the emergence of new ingredients, and the high annotation costs associated with large food segmentation datasets. Existing approaches primarily utilize a closed-vocabulary and static text embeddings setting. These methods often fall short in effectively handling the ingredients, particularly new and diverse ones. In response to these limitations, we introduce OVFoodSeg, a framework that adopts an open-vocabulary setting and enhances text embeddings with visual context. By integrating vision-language models (VLMs), our approach enriches text embedding with image-specific information through two innovative modules, eg, an image-to-text learner FoodLearner and an Image-Informed Text Encoder. The training process of OVFoodSeg is divided into two stages: the pre-training of FoodLearner and the subsequent learning phase for segmentation. The pre-training phase equips FoodLearner with the capability to align visual information with corresponding textual representations that are specifically related to food, while the second phase adapts both the FoodLearner and the Image-Informed Text Encoder for the segmentation task. By addressing the deficiencies of previous models, OVFoodSeg demonstrates a significant improvement, achieving an 4.9\% increase in mean Intersection over Union (mIoU) on the FoodSeg103 dataset, setting a new milestone for food image segmentation.

### Open-Vocabulary Video Anomaly Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01732)
- **作者**: Peng Wu, Xuerong Zhou, Guansong Pang, Yujia Sun, Jing Liu, Peng Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### SED: A Simple Encoder-Decoder for Open-Vocabulary Semantic Segmentation.
- **链接**: [arXiv:2311.15537](https://arxiv.org/abs/2311.15537) · [代码](https://github.com/xb534/SED.git) · 📚 被引 90
- **作者**: Bin Xie, Jiale Cao, Jin Xie, Fahad Shahbaz Khan, Yanwei Pang
- **🏷️ 机构**: Tianjin University, Chongqing University, Mohamed bin Zayed University of Artificial Intelligence
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Open-vocabulary semantic segmentation strives to distinguish pixels into different semantic groups from an open set of categories. Most existing methods explore utilizing pre-trained vision-language models, in which the key is to adopt the image-level model for pixel-level segmentation task. In this paper, we propose a simple encoder-decoder, named SED, for open-vocabulary semantic segmentation, which comprises a hierarchical encoder-based cost map generation and a gradual fusion decoder with category early rejection. The hierarchical encoder-based cost map generation employs hierarchical backbone, instead of plain transformer, to predict pixel-level image-text cost map. Compared to plain transformer, hierarchical backbone better captures local spatial information and has linear computational complexity with respect to input size. Our gradual fusion decoder employs a top-down structure to combine cost map and the feature maps of different backbone levels for segmentation. To accelerate inference speed, we introduce a category early rejection scheme in the decoder that rejects many no-existing categories at the early layer of decoder, resulting in at most 4.7 times acceleration without accuracy degradation. Experiments are performed on multiple open-vocabulary semantic segmentation datasets, which demonstrates the efficacy of our SED method. When using ConvNeXt-B, our SED method achieves mIoU score of 31.6\% on ADE20K with 150 categories at 82 millisecond ($ms$) per image on a single A6000. We will release it at \url{https://github.com/xb534/SED.git}.

### Transferable and Principled Efficiency for Open-Vocabulary Segmentation.
- **链接**: [arXiv:2404.07448](https://arxiv.org/abs/2404.07448) · [代码](https://github.com/Xujxyang/OpenTrans) · 📚 被引 2
- **作者**: Jingxuan Xu, Wuyang Chen, Yao Zhao, Yunchao Wei
- **🏷️ 机构**: Beijing Jiaotong University, Simon Fraser University
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Recent success of pre-trained foundation vision-language models makes Open-Vocabulary Segmentation (OVS) possible. Despite the promising performance, this approach introduces heavy computational overheads for two challenges: 1) large model sizes of the backbone; 2) expensive costs during the fine-tuning. These challenges hinder this OVS strategy from being widely applicable and affordable in real-world scenarios. Although traditional methods such as model compression and efficient fine-tuning can address these challenges, they often rely on heuristics. This means that their solutions cannot be easily transferred and necessitate re-training on different models, which comes at a cost. In the context of efficient OVS, we target achieving performance that is comparable to or even better than prior OVS works based on large vision-language foundation models, by utilizing smaller models that incur lower training costs. The core strategy is to make our efficiency principled and thus seamlessly transferable from one OVS framework to others without further customization. Comprehensive experiments on diverse OVS benchmarks demonstrate our superior trade-off between segmentation accuracy and computation costs over previous works. Our code is available on https://github.com/Xujxyang/OpenTrans

### MaskClustering: View Consensus Based Mask Graph Clustering for Open-Vocabulary 3D Instance Segmentation.
- **链接**: [arXiv:2401.07745](https://arxiv.org/abs/2401.07745) · 📚 被引 41
- **作者**: Mi Yan, Jiazhao Zhang, Yan Zhu, He Wang
- **🏷️ 机构**: CFCS, School of CS, Peking University
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Open-vocabulary 3D instance segmentation is cutting-edge for its ability to segment 3D instances without predefined categories. However, progress in 3D lags behind its 2D counterpart due to limited annotated 3D data. To address this, recent works first generate 2D open-vocabulary masks through 2D models and then merge them into 3D instances based on metrics calculated between two neighboring frames. In contrast to these local metrics, we propose a novel metric, view consensus rate, to enhance the utilization of multi-view observations. The key insight is that two 2D masks should be deemed part of the same 3D instance if a significant number of other 2D masks from different views contain both these two masks. Using this metric as edge weight, we construct a global mask graph where each mask is a node. Through iterative clustering of masks showing high view consensus, we generate a series of clusters, each representing a distinct 3D instance. Notably, our model is training-free. Through extensive experiments on publicly available datasets, including ScanNet++, ScanNet200 and MatterPort3D, we demonstrate that our method achieves state-of-the-art performance in open-vocabulary 3D instance segmentation. Our project page is at https://pku-epic.github.io/MaskClustering.

### Visual Programming for Zero-Shot Open-Vocabulary 3D Visual Grounding.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01949)
- **作者**: Zhihao Yuan, Jinke Ren, Chun-Mei Feng, Hengshuang Zhao, Shuguang Cui, Zhen Li
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### OVER-NAV: Elevating Iterative Vision-and-Language Navigation with Open-Vocabulary Detection and StructurEd Representation.
- **链接**: [arXiv:2403.17334](https://arxiv.org/abs/2403.17334) · 📚 被引 14
- **作者**: Ganlong Zhao, Guanbin Li, Weikai Chen, Yizhou Yu
- **🏷️ 机构**: The University of Hong Kong, Sun Yat-sen University, Digital Content Technology Center, Tencent Games
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Recent advances in Iterative Vision-and-Language Navigation (IVLN) introduce a more meaningful and practical paradigm of VLN by maintaining the agent's memory across tours of scenes. Although the long-term memory aligns better with the persistent nature of the VLN task, it poses more challenges on how to utilize the highly unstructured navigation memory with extremely sparse supervision. Towards this end, we propose OVER-NAV, which aims to go over and beyond the current arts of IVLN techniques. In particular, we propose to incorporate LLMs and open-vocabulary detectors to distill key information and establish correspondence between multi-modal signals. Such a mechanism introduces reliable cross-modal supervision and enables on-the-fly generalization to unseen scenes without the need of extra annotation and re-training. To fully exploit the interpreted navigation data, we further introduce a structured representation, coded Omnigraph, to effectively integrate multi-modal information along the tour. Accompanied with a novel omnigraph fusion mechanism, OVER-NAV is able to extract the most relevant knowledge from omnigraph for a more accurate navigating action. In addition, OVER-NAV seamlessly supports both discrete and continuous environments under a unified framework. We demonstrate the superiority of OVER-NAV in extensive experiments.

### Self-Supervised Class-Agnostic Motion Prediction with Spatial and Temporal Consistency Regularizations.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01387)
- **作者**: Kewei Wang, Yizheng Wu, Jun Cen, Zhiyu Pan, Xingyi Li, Zhe Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

## 跨领域论文（完整笔记在其他领域）

- YOLO-World: Real-Time Open-Vocabulary Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- Retrieval-Augmented Open-Vocabulary Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- Learning Background Prompts to Discover Implicit Knowledge for Open Vocabulary Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- SHiNe: Semantic Hierarchy Nexus for Open-Vocabulary Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- DetCLIPv3: Towards Versatile Generative Open-Vocabulary Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- Exploring Region-Word Alignment in Built-in Detector for Open-Vocabulary Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- Scene-adaptive and Region-aware Multi-modal Prompt for Open Vocabulary Object Detection. → [multimodal](../multimodal/Guideline%202024.md)
- Taming Self-Training for Open-Vocabulary Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- OVMR: Open-Vocabulary Recognition with Multi-Modal References. → [multimodal](../multimodal/Guideline%202024.md)
