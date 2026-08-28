# Open-set Detection — 2024 Guideline

> 领域: 开放类检测总类（开放词表 OVD / 开放世界 OWOD / 开集 OOD / 未知类检测）
> 论文数: 42 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Scene-Graph ViT: End-to-End Open-Vocabulary Visual Relationship Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72907-2_12)
- **作者**: Tim Salzmann, Markus Ryll, Alex Bewley, Matthias Minderer
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### CLIP-DINOiser: Teaching CLIP a Few DINO Tricks for Open-Vocabulary Semantic Segmentation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73030-6_18)
- **作者**: Monika Wysoczanska, Oriane Siméoni, Michaël Ramamonjisoa, Andrei Bursuc, Tomasz Trzcinski, Patrick Pérez
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Global-Local Collaborative Inference with LLM for Lidar-Based Open-Vocabulary Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72761-0_21) · 📚 被引 4
- **作者**: Xingyu Peng, Yan Bai, Chen Gao, Lirong Yang, Fei Xia, Beipeng Mu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### OpenIns3D: Snap and Lookup for 3D Open-Vocabulary Instance Segmentation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73033-7_10) · 📚 被引 49
- **作者**: Zhening Huang, Xiaoyang Wu, Xi Chen, Hengshuang Zhao, Lei Zhu, Joan Lasenby
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Expanding Scene Graph Boundaries: Fully Open-Vocabulary Scene Graph Generation via Visual-Concept Alignment and Retention.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72848-8_7) · 📚 被引 15
- **作者**: Zuyao Chen, Jinlin Wu, Zhen Lei, Zhaoxiang Zhang, Chang Wen Chen
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Textual Grounding for Open-Vocabulary Visual Information Extraction in Layout-Diversified Documents.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72995-9_27) · 📚 被引 1
- **作者**: Mengjun Cheng, Chengquan Zhang, Chang Liu, Yuke Li, Bohan Li, Kun Yao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Unified Embedding Alignment for Open-Vocabulary Video Instance Segmentation.
- **链接**: [arXiv:2407.07427](https://arxiv.org/abs/2407.07427) · [代码](https://github.com/fanghaook/OVFormer)
- **作者**: Hao Fang, Peng Wu, Yawei Li, Xinxin Zhang, Xiankai Lu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-Vocabulary Video Instance Segmentation (VIS) is attracting increasing attention due to its ability to segment and track arbitrary objects. However, the recent Open-Vocabulary VIS attempts obtained unsatisfactory results, especially in terms of generalization ability of novel categories. We discover that the domain gap between the VLM features (e.g., CLIP) and the instance queries and the underutilization of temporal consistency are two central causes. To mitigate these issues, we design and train a novel Open-Vocabulary VIS baseline called OVFormer. OVFormer utilizes a lightweight module for unified embedding alignment between query embeddings and CLIP image embeddings to remedy the domain gap. Unlike previous image-based training methods, we conduct video-based model training and deploy a semi-online inference scheme to fully mine the temporal consistency in the video. Without bells and whistles, OVFormer achieves 21.9 mAP with a ResNet-50 backbone on LV-VIS, exceeding the previous state-of-the-art performance by 7.7. Extensive experiments on some Close-Vocabulary VIS datasets also demonstrate the strong zero-shot generalization ability of OVFormer (+ 7.6 mAP on YouTube-VIS 2019, + 3.9 mAP on OVIS). Code is available at https://github.com/fanghaook/OVFormer.

</details>

### AnyHome: Open-Vocabulary Generation of Structured and Textured 3D Homes.
- **链接**: [arXiv:2312.06644](https://arxiv.org/abs/2312.06644) · 📚 被引 22
- **作者**: Rao Fu, Zehao Wen, Zichen Liu, Srinath Sridhar
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Inspired by cognitive theories, we introduce AnyHome, a framework that translates any text into well-structured and textured indoor scenes at a house-scale. By prompting Large Language Models (LLMs) with designed templates, our approach converts provided textual narratives into amodal structured representations. These representations guarantee consistent and realistic spatial layouts by directing the synthesis of a geometry mesh within defined constraints. A Score Distillation Sampling process is then employed to refine the geometry, followed by an egocentric inpainting process that adds lifelike textures to it. AnyHome stands out with its editability, customizability, diversity, and realism. The structured representations for scenes allow for extensive editing at varying levels of granularity. Capable of interpreting texts ranging from simple labels to detailed narratives, AnyHome generates detailed geometries and textures that outperform existing methods in both quantitative and qualitative measures.

</details>

### Open Vocabulary Multi-label Video Classification.
- **链接**: [arXiv:2407.09073](https://arxiv.org/abs/2407.09073)
- **作者**: Rohit Gupta, Mamshad Nayeem Rizve, Jayakrishnan Unnikrishnan, Ashish Tawari, Son Tran, Mubarak Shah et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pre-trained vision-language models (VLMs) have enabled significant progress in open vocabulary computer vision tasks such as image classification, object detection and image segmentation. Some recent works have focused on extending VLMs to open vocabulary single label action classification in videos. However, previous methods fall short in holistic video understanding which requires the ability to simultaneously recognize multiple actions and entities e.g., objects in the video in an open vocabulary setting. We formulate this problem as open vocabulary multilabel video classification and propose a method to adapt a pre-trained VLM such as CLIP to solve this task. We leverage large language models (LLMs) to provide semantic guidance to the VLM about class labels to improve its open vocabulary performance with two key contributions. First, we propose an end-to-end trainable architecture that learns to prompt an LLM to generate soft attributes for the CLIP text-encoder to enable it to recognize novel classes. Second, we integrate a temporal modeling module into CLIP's vision encoder to effectively model the spatio-temporal dynamics of video concepts as well as propose a novel regularized finetuning technique to ensure strong open vocabulary classification performance in the video domain. Our extensive experimentation showcases the efficacy of our approach on multiple benchmark datasets.

</details>

### Collaborative Vision-Text Representation Optimizing for Open-Vocabulary Segmentation.
- **链接**: [arXiv:2408.00744](https://arxiv.org/abs/2408.00744) · [代码](https://github.com/jiaosiyu1999/MAFT-Plus.git) · 📚 被引 24
- **作者**: Siyu Jiao, Hongguang Zhu, Jiannan Huang, Yao Zhao, Yunchao Wei, Humphrey Shi
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pre-trained vision-language models, e.g. CLIP, have been increasingly used to address the challenging Open-Vocabulary Segmentation (OVS) task, benefiting from their well-aligned vision-text embedding space. Typical solutions involve either freezing CLIP during training to unilaterally maintain its zero-shot capability, or fine-tuning CLIP vision encoder to achieve perceptual sensitivity to local regions. However, few of them incorporate vision-text collaborative optimization. Based on this, we propose the Content-Dependent Transfer to adaptively enhance each text embedding by interacting with the input image, which presents a parameter-efficient way to optimize the text representation. Besides, we additionally introduce a Representation Compensation strategy, reviewing the original CLIP-V representation as compensation to maintain the zero-shot capability of CLIP. In this way, the vision and text representation of CLIP are optimized collaboratively, enhancing the alignment of the vision-text feature space. To the best of our knowledge, we are the first to establish the collaborative vision-text optimizing mechanism within the OVS field. Extensive experiments demonstrate our method achieves superior performance on popular OVS benchmarks. In open-vocabulary semantic segmentation, our method outperforms the previous state-of-the-art approaches by +0.5, +2.3, +3.4, +0.4 and +1.1 mIoU, respectively on A-847, A-150, PC-459, PC-59 and PAS-20. Furthermore, in a panoptic setting on ADE20K, we achieve the performance of 27.1 PQ, 73.5 SQ, and 32.9 RQ. Code will be available at https://github.com/jiaosiyu1999/MAFT-Plus.git .

</details>

### In Defense of Lazy Visual Grounding for Open-Vocabulary Semantic Segmentation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72940-9_9)
- **作者**: Dahyun Kang, Minsu Cho
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Diffusion Models for Open-Vocabulary Segmentation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72652-1_18)
- **作者**: Laurynas Karazija, Iro Laina, Andrea Vedaldi, Christian Rupprecht
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Region-Centric Image-Language Pretraining for Open-Vocabulary Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73036-8_10) · 📚 被引 3
- **作者**: Dahun Kim, Anelia Angelova, Weicheng Kuo
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### ProxyCLIP: Proxy Attention Improves CLIP for Open-Vocabulary Segmentation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73113-6_5)
- **作者**: Mengcheng Lan, Chaofeng Chen, Yiping Ke, Xinjiang Wang, Litong Feng, Wayne Zhang
- **🏷️ 机构**: CUHK / SenseTime
- **会议**: ECCV 2024

### SLAck: Semantic, Location, and Appearance Aware Open-Vocabulary Tracking.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73383-3_1) · 📚 被引 7
- **作者**: Siyuan Li, Lei Ke, Yung-Hsu Yang, Luigi Piccinelli, Mattia Segù, Martin Danelljan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Plan, Posture and Go: Towards Open-Vocabulary Text-to-Motion Generation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73383-3_26) · 📚 被引 8
- **作者**: Jinpeng Liu, Wenxun Dai, Chunyu Wang, Yiji Cheng, Yansong Tang, Xin Tong
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Open-Vocabulary Camouflaged Object Segmentation.
- **链接**: [arXiv:2311.11241](https://arxiv.org/abs/2311.11241) · [代码](https://github.com/lartpang/OVCamo)
- **作者**: Youwei Pang, Xiaoqi Zhao, Jiaming Zuo, Lihe Zhang, Huchuan Lu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, the emergence of the large-scale vision-language model (VLM), such as CLIP, has opened the way towards open-world object perception. Many works have explored the utilization of pre-trained VLM for the challenging open-vocabulary dense prediction task that requires perceiving diverse objects with novel classes at inference time. Existing methods construct experiments based on the public datasets of related tasks, which are not tailored for open vocabulary and rarely involve imperceptible objects camouflaged in complex scenes due to data collection bias and annotation costs. To fill in the gaps, we introduce a new task, open-vocabulary camouflaged object segmentation (OVCOS), and construct a large-scale complex scene dataset (\textbf{OVCamo}) containing 11,483 hand-selected images with fine annotations and corresponding object classes. Further, we build a strong single-stage open-vocabulary \underline{c}amouflaged \underline{o}bject \underline{s}egmentation transform\underline{er} baseline \textbf{OVCoser} attached to the parameter-fixed CLIP with iterative semantic guidance and structure enhancement. By integrating the guidance of class semantic knowledge and the supplement of visual structure cues from the edge and depth information, the proposed method can efficiently capture camouflaged objects. Moreover, this effective framework also surpasses previous state-of-the-arts of open-vocabulary semantic image segmentation by a large margin on our OVCamo dataset. With the proposed dataset and baseline, we hope that this new task with more practical value can further expand the research on open-vocabulary dense prediction tasks. Our code and data can be found in the \href{https://github.com/lartpang/OVCamo}{link}.

</details>

### Text Motion Translator: A Bi-directional Model for Enhanced 3D Human Motion Generation from Open-Vocabulary Descriptions.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73036-8_23) · 📚 被引 2
- **作者**: Yijun Qian, Jack Urbanek, Alex Hauptmann, Jungdam Won
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Explore the Potential of CLIP for Training-Free Open Vocabulary Semantic Segmentation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73016-0_9)
- **作者**: Tong Shao, Zhuotao Tian, Hang Zhao, Jingyong Su
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Explain via Any Concept: Concept Bottleneck Model with Open Vocabulary Concepts.
- **链接**: [arXiv:2408.02265](https://arxiv.org/abs/2408.02265) · 📚 被引 6
- **作者**: Andong Tan, Fengtao Zhou, Hao Chen
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The concept bottleneck model (CBM) is an interpretable-by-design framework that makes decisions by first predicting a set of interpretable concepts, and then predicting the class label based on the given concepts. Existing CBMs are trained with a fixed set of concepts (concepts are either annotated by the dataset or queried from language models). However, this closed-world assumption is unrealistic in practice, as users may wonder about the role of any desired concept in decision-making after the model is deployed. Inspired by the large success of recent vision-language pre-trained models such as CLIP in zero-shot classification, we propose "OpenCBM" to equip the CBM with open vocabulary concepts via: (1) Aligning the feature space of a trainable image feature extractor with that of a CLIP's image encoder via a prototype based feature alignment; (2) Simultaneously training an image classifier on the downstream dataset; (3) Reconstructing the trained classification head via any set of user-desired textual concepts encoded by CLIP's text encoder. To reveal potentially missing concepts from users, we further propose to iteratively find the closest concept embedding to the residual parameters during the reconstruction until the residual is small enough. To the best of our knowledge, our "OpenCBM" is the first CBM with concepts of open vocabularies, providing users the unique benefit such as removing, adding, or replacing any desired concept to explain the model's prediction even after a model is trained. Moreover, our model significantly outperforms the previous state-of-the-art CBM by 9% in the classification accuracy on the benchmark dataset CUB-200-2011.

</details>

### O 2V-Mapping: Online Open-Vocabulary Mapping with Neural Implicit Representation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73021-4_19)
- **作者**: Muer Tie, Julong Wei, Ke Wu, Zhengjun Wang, Shanshuai Yuan, Kaizhao Zhang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Open Vocabulary 3D Scene Understanding via Geometry Guided Self-Distillation.
- **链接**: [arXiv:2407.13362](https://arxiv.org/abs/2407.13362) · 📚 被引 5
- **作者**: Pengfei Wang, Yuxi Wang, Shuai Li, Zhaoxiang Zhang, Zhen Lei, Lei Zhang
- **🏷️ 机构**: PolyU / OPPO
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The scarcity of large-scale 3D-text paired data poses a great challenge on open vocabulary 3D scene understanding, and hence it is popular to leverage internet-scale 2D data and transfer their open vocabulary capabilities to 3D models through knowledge distillation. However, the existing distillation-based 3D scene understanding approaches rely on the representation capacity of 2D models, disregarding the exploration of geometric priors and inherent representational advantages offered by 3D data. In this paper, we propose an effective approach, namely Geometry Guided Self-Distillation (GGSD), to learn superior 3D representations from 2D pre-trained models. Specifically, we first design a geometry guided distillation module to distill knowledge from 2D models, and then leverage the 3D geometric priors to alleviate the inherent noise in 2D models and enhance the representation learning process. Due to the advantages of 3D representation, the performance of the distilled 3D student model can significantly surpass that of the 2D teacher model. This motivates us to further leverage the representation advantages of 3D data through self-distillation. As a result, our proposed GGSD approach outperforms the existing open vocabulary 3D scene understanding methods by a large margin, as demonstrated by our experiments on both indoor and outdoor benchmark datasets.

</details>

### 3D Open-Vocabulary Panoptic Segmentation with 2D-3D Vision-Language Distillation.
- **链接**: [arXiv:2401.02402](https://arxiv.org/abs/2401.02402) · 📚 被引 5
- **作者**: Zihao Xiao, Longlong Jing, Shangxuan Wu, Alex Zihao Zhu, Jingwei Ji, Chiyu Max Jiang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D panoptic segmentation is a challenging perception task, especially in autonomous driving. It aims to predict both semantic and instance annotations for 3D points in a scene. Although prior 3D panoptic segmentation approaches have achieved great performance on closed-set benchmarks, generalizing these approaches to unseen things and unseen stuff categories remains an open problem. For unseen object categories, 2D open-vocabulary segmentation has achieved promising results that solely rely on frozen CLIP backbones and ensembling multiple classification outputs. However, we find that simply extending these 2D models to 3D does not guarantee good performance due to poor per-mask classification quality, especially for novel stuff categories. In this paper, we propose the first method to tackle 3D open-vocabulary panoptic segmentation. Our model takes advantage of the fusion between learnable LiDAR features and dense frozen vision CLIP features, using a single classification head to make predictions for both base and novel classes. To further improve the classification performance on novel classes and leverage the CLIP model, we propose two novel loss functions: object-level distillation loss and voxel-level distillation loss. Our experiments on the nuScenes and SemanticKITTI datasets show that our method outperforms the strong baseline by a large margin.

</details>

### Open-Vocabulary SAM: Segment and Recognize Twenty-Thousand Classes Interactively.
- **链接**: [arXiv:2401.02955](https://arxiv.org/abs/2401.02955) · 📚 被引 58
- **作者**: Haobo Yuan, Xiangtai Li, Chong Zhou, Yining Li, Kai Chen, Chen Change Loy
- **🏷️ 机构**: NTU S-Lab
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The CLIP and Segment Anything Model (SAM) are remarkable vision foundation models (VFMs). SAM excels in segmentation tasks across diverse domains, whereas CLIP is renowned for its zero-shot recognition capabilities. This paper presents an in-depth exploration of integrating these two models into a unified framework. Specifically, we introduce the Open-Vocabulary SAM, a SAM-inspired model designed for simultaneous interactive segmentation and recognition, leveraging two unique knowledge transfer modules: SAM2CLIP and CLIP2SAM. The former adapts SAM's knowledge into the CLIP via distillation and learnable transformer adapters, while the latter transfers CLIP knowledge into SAM, enhancing its recognition capabilities. Extensive experiments on various datasets and detectors show the effectiveness of Open-Vocabulary SAM in both segmentation and recognition tasks, significantly outperforming the naïve baselines of simply combining SAM and CLIP. Furthermore, aided with image classification data training, our method can segment and recognize approximately 22,000 classes.

</details>

### Open-Vocabulary RGB-Thermal Semantic Segmentation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72904-1_18)
- **作者**: Guoqiang Zhao, Junjie Huang, Xiaoyun Yan, Zhaojing Wang, Junwei Tang, Yangjun Ou et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Open-Vocabulary 3D Semantic Segmentation with Text-to-Image Diffusion Models.
- **链接**: [arXiv:2407.13642](https://arxiv.org/abs/2407.13642)
- **作者**: Xiaoyu Zhu, Hao Zhou, Pengfei Xing, Long Zhao, Hao Xu, Junwei Liang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we investigate the use of diffusion models which are pre-trained on large-scale image-caption pairs for open-vocabulary 3D semantic understanding. We propose a novel method, namely Diff2Scene, which leverages frozen representations from text-image generative models, along with salient-aware and geometric-aware masks, for open-vocabulary 3D semantic segmentation and visual grounding tasks. Diff2Scene gets rid of any labeled 3D data and effectively identifies objects, appearances, materials, locations and their compositions in 3D scenes. We show that it outperforms competitive baselines and achieves significant improvements over state-of-the-art methods. In particular, Diff2Scene improves the state-of-the-art method on ScanNet200 by 12%.

</details>

### Self-cooperation Knowledge Distillation for Novel Class Discovery.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72897-6_26) · 📚 被引 4
- **作者**: Yuzheng Wang, Zhaoyu Chen, Dingkang Yang, Yunquan Sun, Lizhe Qi
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

## 跨领域论文（完整笔记在其他领域）

- Grounding DINO: Marrying DINO with Grounded Pre-training for Open-Set Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- LaMI-DETR: Open-Vocabulary Detection with Language Model Instruction. → [object-detection](../object-detection/Guideline%202024.md)
- Cross-Domain Few-Shot Object Detection via Enhanced Open-Set Object Detector. → [object-detection](../object-detection/Guideline%202024.md)
- MarvelOVD: Marrying Object Recognition and Vision-Language Models for Robust Open-Vocabulary Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- Find n' Propagate: Open-Vocabulary 3D Object Detection in Urban Environments. → [3d-detection](../3d-detection/Guideline%202024.md)
- Unlocking Textual and Visual Wisdom: Open-Vocabulary 3D Object Detection Enhanced by Comprehensive Guidance from Text and Image. → [3d-detection](../3d-detection/Guideline%202024.md)
- Toward Open Vocabulary Aerial Object Detection with CLIP-Activated Student-Teacher Learning. → [object-detection](../object-detection/Guideline%202024.md)
- CLIFF: Continual Latent Diffusion for Open-Vocabulary Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- OV-Uni3DETR: Towards Unified Open-Vocabulary 3D Object Detection via Cycle-Modality Propagation. → [3d-detection](../3d-detection/Guideline%202024.md)
- OpenSight: A Simple Open-Vocabulary Framework for LiDAR-Based Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- Dense Multimodal Alignment for Open-Vocabulary 3D Scene Understanding. → [multimodal](../multimodal/Guideline%202024.md)
- Anytime Continual Learning for Open Vocabulary Classification. → [continual-learning](../continual-learning/Guideline%202024.md)
- Towards Multimodal Open-Set Domain Generalization and Adaptation Through Self-supervision. → [multimodal](../multimodal/Guideline%202024.md)
- OpenPSG: Open-Set Panoptic Scene Graph Generation via Large Multimodal Models. → [multimodal](../multimodal/Guideline%202024.md)
- Continual Learning and Unknown Object Discovery in 3D Scenes via Self-distillation. → [continual-learning](../continual-learning/Guideline%202024.md)
