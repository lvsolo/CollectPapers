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
- **链接**: [arXiv:2402.12259](https://arxiv.org/abs/2402.12259)
- **作者**: Sebastian Koch, Narunas Vaskevicius, Mirco Colosi, Pedro Hermosilla, Timo Ropinski
- **🏷️ 机构**: Bosch Center for Artificial Intelligence, Robert Bosch Corporate Research, TU Vienna
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Current approaches for 3D scene graph prediction rely on labeled datasets to train models for a fixed set of known object classes and relationship categories. We present Open3DSG, an alternative approach to learn 3D scene graph prediction in an open world without requiring labeled scene graph data. We co-embed the features from a 3D scene graph prediction backbone with the feature space of powerful open world 2D vision language foundation models. This enables us to predict 3D scene graphs from 3D point clouds in a zero-shot manner by querying object classes from an open vocabulary and predicting the inter-object relationships from a grounded LLM with scene graph features and queried object classes as context. Open3DSG is the first 3D point cloud method to predict not only explicit open-vocabulary object classes, but also open-set relationships that are not limited to a predefined label set, making it possible to express rare as well as specific objects and relationships in the predicted 3D scene graph. Our experiments show that Open3DSG is effective at predicting arbitrary object classes as well as their complex inter-object relationships describing spatial, supportive, semantic and comparative relationships.

### Open3DIS: Open-Vocabulary 3D Instance Segmentation with 2D Mask Guidance.
- **链接**: [arXiv:2312.10671](https://arxiv.org/abs/2312.10671)
- **作者**: Phuc D. A. Nguyen, Tuan Duc Ngo, Evangelos Kalogerakis, Chuang Gan, Anh Tuan Tran, Cuong Pham et al.
- **🏷️ 机构**: VinAI Research, UMass Amherst, MIT-IBM Watson AI Lab
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > We introduce Open3DIS, a novel solution designed to tackle the problem of Open-Vocabulary Instance Segmentation within 3D scenes. Objects within 3D environments exhibit diverse shapes, scales, and colors, making precise instance-level identification a challenging task. Recent advancements in Open-Vocabulary scene understanding have made significant strides in this area by employing class-agnostic 3D instance proposal networks for object localization and learning queryable features for each 3D mask. While these methods produce high-quality instance proposals, they struggle with identifying small-scale and geometrically ambiguous objects. The key idea of our method is a new module that aggregates 2D instance masks across frames and maps them to geometrically coherent point cloud regions as high-quality object proposals addressing the above limitations. These are then combined with 3D class-agnostic instance proposals to include a wide range of objects in the real world. To validate our approach, we conducted experiments on three prominent datasets, including ScanNet200, S3DIS, and Replica, demonstrating significant performance gains in segmenting objects with diverse categories over the state-of-the-art approaches.

### Open-Vocabulary 3D Semantic Segmentation with Foundation Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02011)
- **作者**: Li Jiang, Shaoshuai Shi, Bernt Schiele
- **🏷️ 机构**: Max Planck Institute for Informatics, Saarland Informatics Campus
- **会议**: CVPR 2024

### Training-Free Open-Vocabulary Segmentation with Offline Diffusion-Augmented Prototype Generation.
- **链接**: [arXiv:2404.06542](https://arxiv.org/abs/2404.06542)
- **作者**: Luca Barsellotti, Roberto Amoroso, Marcella Cornia, Lorenzo Baraldi, Rita Cucchiara
- **🏷️ 机构**: University of Modena and Reggio Emilia,Italy
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Open-vocabulary semantic segmentation aims at segmenting arbitrary categories expressed in textual form. Previous works have trained over large amounts of image-caption pairs to enforce pixel-level multimodal alignments. However, captions provide global information about the semantics of a given image but lack direct localization of individual concepts. Further, training on large-scale datasets inevitably brings significant computational costs. In this paper, we propose FreeDA, a training-free diffusion-augmented method for open-vocabulary semantic segmentation, which leverages the ability of diffusion models to visually localize generated concepts and local-global similarities to match class-agnostic regions with semantic classes. Our approach involves an offline stage in which textual-visual reference embeddings are collected, starting from a large set of captions and leveraging visual and semantic contexts. At test time, these are queried to support the visual matching process, which is carried out by jointly considering class-agnostic regions and global semantic similarities. Extensive analyses demonstrate that FreeDA achieves state-of-the-art performance on five datasets, surpassing previous methods by more than 7.0 average points in terms of mIoU and without requiring any training.

### The Devil is in the Fine-Grained Details: Evaluating open-Vocabulary Object Detectors for Fine-Grained Understanding.
- **链接**: [arXiv:2311.17518](https://arxiv.org/abs/2311.17518)
- **作者**: Lorenzo Bianchi, Fabio Carrara, Nicola Messina, Claudio Gennaro, Fabrizio Falchi
- **🏷️ 机构**: CNR-ISTI,Pisa,Italy
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Recent advancements in large vision-language models enabled visual object detection in open-vocabulary scenarios, where object classes are defined in free-text formats during inference. In this paper, we aim to probe the state-of-the-art methods for open-vocabulary object detection to determine to what extent they understand fine-grained properties of objects and their parts. To this end, we introduce an evaluation protocol based on dynamic vocabulary generation to test whether models detect, discern, and assign the correct fine-grained description to objects in the presence of hard-negative classes. We contribute with a benchmark suite of increasing difficulty and probing different properties like color, pattern, and material. We further enhance our investigation by evaluating several state-of-the-art open-vocabulary object detectors using the proposed protocol and find that most existing solutions, which shine in standard open-vocabulary benchmarks, struggle to accurately capture and distinguish finer object details. We conclude the paper by highlighting the limitations of current methodologies and exploring promising research directions to overcome the discovered drawbacks. Data and code are available at https://lorebianchi98.github.io/FG-OVD/.

### Open Vocabulary Semantic Scene Sketch Understanding.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00400)
- **作者**: Ahmed Bourouis, Judith Ellen Fan, Yulia Gryaditskaya
- **🏷️ 机构**: Surrey Institute for People-Centered AI and CVSSP, University of Surrey,UK, Stanford University,Department of Psychology,USA
- **会议**: CVPR 2024

### CLIP-Driven Open-Vocabulary 3D Scene Graph Generation via Cross-Modality Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02632)
- **作者**: Lianggangxu Chen, Xuejiao Wang, Jiale Lu, Shaohui Lin, Changbo Wang, Gaoqi He
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### CAT-Seg: Cost Aggregation for Open-Vocabulary Semantic Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00394)
- **作者**: Seokju Cho, Heeseong Shin, Sunghwan Hong, Anurag Arnab, Paul Hongsuck Seo, Seungryong Kim
- **🏷️ 机构**: Korea University, Google Research
- **会议**: CVPR 2024

### Open-vocabulary object 6D pose estimation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01711)
- **作者**: Jaime Corsetti, Davide Boscaini, Changjae Oh, Andrea Cavallaro, Fabio Poiesi
- **🏷️ 机构**: Fondazione, Queen Mary University, Idiap Research Institute
- **会议**: CVPR 2024

### AnySkill: Learning Open-Vocabulary Physical Skill for Interactive Agents.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00087)
- **作者**: Jieming Cui, Tengyu Liu, Nian Liu, Yaodong Yang, Yixin Zhu, Siyuan Huang
- **🏷️ 机构**: Institute for Artificial Intelligence, Peking University, BIGAI,National Key Laboratory of General Artificial Intelligence
- **会议**: CVPR 2024

### Active Open-Vocabulary Recognition: Let Intelligent Moving Mitigate CLIP Limitations.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01551)
- **作者**: Lei Fan, Jianxiong Zhou, Xiaoying Xing, Ying Wu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### Exploring the Potential of Large Foundation Models for Open-Vocabulary HOI Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01576)
- **作者**: Ting Lei, Shaofeng Yin, Yang Liu
- **🏷️ 机构**: Wangxuan Institute of Computer Technology, Peking University
- **会议**: CVPR 2024

### From Pixels to Graphs: Open-Vocabulary Scene Graph Generation with Vision-Language Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02652)
- **作者**: Rongjie Li, Songyang Zhang, Dahua Lin, Kai Chen, Xuming He
- **🏷️ 机构**: CUHK
- **会议**: CVPR 2024

### OMG: Towards Open-vocabulary Motion Generation via Mixture of Controllers.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00053)
- **作者**: Han Liang, Jiacheng Bao, Ruichi Zhang, Sihan Ren, Yuecheng Xu, Sibei Yang et al.
- **🏷️ 机构**: ShanghaiTecn University, Tencent PCG
- **会议**: CVPR 2024

### Open-Vocabulary Segmentation with Semantic-Assisted Calibration.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00335)
- **作者**: Yong Liu, Sule Bai, Guanbin Li, Yitong Wang, Yansong Tang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### Emergent Open-Vocabulary Semantic Segmentation from Off-the-Shelf Vision-Language Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00386)
- **作者**: Jiayun Luo, Siddhesh Khandelwal, Leonid Sigal, Boyang Li
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### Open-Vocabulary Attention Maps with Token Optimization for Semantic Segmentation in Diffusion Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00883)
- **作者**: Pablo Marcos-Manchón, Roberto Alcover-Couso, Juan C. SanMiguel, Jose M. Martínez
- **🏷️ 机构**: VPULab, University of Madrid,Spain
- **会议**: CVPR 2024

### Open-Vocabulary Semantic Segmentation with Image Embedding Balancing.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02684)
- **作者**: Xiangheng Shan, Dongyue Wu, Guilin Zhu, Yuanjie Shao, Nong Sang, Changxin Gao
- **🏷️ 机构**: National Key Laboratory of Multispectral Information Intelligent Processing Technology, School of Artificial Intelligence and Automation, Huazhong University of Science and Technology
- **会议**: CVPR 2024

### Language Embedded 3D Gaussians for Open-Vocabulary Scene Understanding.
- **链接**: [arXiv:2311.18482](https://arxiv.org/abs/2311.18482) · 📚 被引 0
- **作者**: Jin-Chuan Shi, Miao Wang, Hao-Bin Duan, Shao-Hua Guan
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Open-vocabulary querying in 3D space is challenging but essential for scene understanding tasks such as object localization and segmentation. Language-embedded scene representations have made progress by incorporating language features into 3D spaces. However, their efficacy heavily depends on neural networks that are resource-intensive in training and rendering. Although recent 3D Gaussians offer efficient and high-quality novel view synthesis, directly embedding language features in them leads to prohibitive memory usage and decreased performance. In this work, we introduce Language Embedded 3D Gaussians, a novel scene representation for open-vocabulary query tasks. Instead of embedding high-dimensional raw semantic features on 3D Gaussians, we propose a dedicated quantization scheme that drastically alleviates the memory requirement, and a novel embedding procedure that achieves smoother yet high accuracy query, countering the multi-view feature inconsistencies and the high-frequency inductive bias in point-based representations. Our comprehensive experiments show that our representation achieves the best visual quality and language querying accuracy across current language-embedded representations, while maintaining real-time rendering frame rates on a single desktop GPU.

### GOV-NeSF: Generalizable Open-Vocabulary Neural Semantic Fields.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01932)
- **作者**: Yunsong Wang, Hanlin Chen, Gim Hee Lee
- **🏷️ 机构**: National University of Singapore,Department of Computer Science
- **会议**: CVPR 2024

### USE: Universal Segment Embeddings for Open-Vocabulary Image Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00401)
- **作者**: Xiaoqi Wang, Wenbin He, Xiwei Xuan, Clint Sebastian, Jorge Piazentin Ono, Xin Li et al.
- **🏷️ 机构**: Bosch Research North America, Bosch Center for Artificial Intelligence (BCAI)
- **会议**: CVPR 2024

### Image-to-Image Matching via Foundation Models: A New Perspective for Open-Vocabulary Semantic Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00379)
- **作者**: Yuan Wang, Rui Sun, Naisong Luo, Yuwen Pan, Tianzhu Zhang
- **🏷️ 机构**: University of Science and Technology of China
- **会议**: CVPR 2024

### OVFoodSeg: Elevating Open-Vocabulary Food Image Segmentation via Image-Informed Textual Representation.
- **链接**: [arXiv:2404.01409](https://arxiv.org/abs/2404.01409)
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
- **链接**: [arXiv:2311.15537](https://arxiv.org/abs/2311.15537) · [代码](https://github.com/xb534/SED.git)
- **作者**: Bin Xie, Jiale Cao, Jin Xie, Fahad Shahbaz Khan, Yanwei Pang
- **🏷️ 机构**: Tianjin University, Chongqing University, Mohamed bin Zayed University of Artificial Intelligence
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Open-vocabulary semantic segmentation strives to distinguish pixels into different semantic groups from an open set of categories. Most existing methods explore utilizing pre-trained vision-language models, in which the key is to adopt the image-level model for pixel-level segmentation task. In this paper, we propose a simple encoder-decoder, named SED, for open-vocabulary semantic segmentation, which comprises a hierarchical encoder-based cost map generation and a gradual fusion decoder with category early rejection. The hierarchical encoder-based cost map generation employs hierarchical backbone, instead of plain transformer, to predict pixel-level image-text cost map. Compared to plain transformer, hierarchical backbone better captures local spatial information and has linear computational complexity with respect to input size. Our gradual fusion decoder employs a top-down structure to combine cost map and the feature maps of different backbone levels for segmentation. To accelerate inference speed, we introduce a category early rejection scheme in the decoder that rejects many no-existing categories at the early layer of decoder, resulting in at most 4.7 times acceleration without accuracy degradation. Experiments are performed on multiple open-vocabulary semantic segmentation datasets, which demonstrates the efficacy of our SED method. When using ConvNeXt-B, our SED method achieves mIoU score of 31.6\% on ADE20K with 150 categories at 82 millisecond ($ms$) per image on a single A6000. We will release it at \url{https://github.com/xb534/SED.git}.

### Transferable and Principled Efficiency for Open-Vocabulary Segmentation.
- **链接**: [arXiv:2404.07448](https://arxiv.org/abs/2404.07448) · [代码](https://github.com/Xujxyang/OpenTrans)
- **作者**: Jingxuan Xu, Wuyang Chen, Yao Zhao, Yunchao Wei
- **🏷️ 机构**: Beijing Jiaotong University, Simon Fraser University
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Recent success of pre-trained foundation vision-language models makes Open-Vocabulary Segmentation (OVS) possible. Despite the promising performance, this approach introduces heavy computational overheads for two challenges: 1) large model sizes of the backbone; 2) expensive costs during the fine-tuning. These challenges hinder this OVS strategy from being widely applicable and affordable in real-world scenarios. Although traditional methods such as model compression and efficient fine-tuning can address these challenges, they often rely on heuristics. This means that their solutions cannot be easily transferred and necessitate re-training on different models, which comes at a cost. In the context of efficient OVS, we target achieving performance that is comparable to or even better than prior OVS works based on large vision-language foundation models, by utilizing smaller models that incur lower training costs. The core strategy is to make our efficiency principled and thus seamlessly transferable from one OVS framework to others without further customization. Comprehensive experiments on diverse OVS benchmarks demonstrate our superior trade-off between segmentation accuracy and computation costs over previous works. Our code is available on https://github.com/Xujxyang/OpenTrans

### MaskClustering: View Consensus Based Mask Graph Clustering for Open-Vocabulary 3D Instance Segmentation.
- **链接**: [arXiv:2401.07745](https://arxiv.org/abs/2401.07745)
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
- **链接**: [arXiv:2403.17334](https://arxiv.org/abs/2403.17334)
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
