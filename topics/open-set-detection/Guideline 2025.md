# Open-set Detection — 2025 Guideline

> 领域: 开放类检测总类（开放词表 OVD / 开放世界 OWOD / 开集 OOD / 未知类检测）
> 论文数: 47 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Talking to DINO: Bridging Self-Supervised Vision Backbones with Language for Open-Vocabulary Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02045)
- **作者**: Luca Barsellotti, Lorenzo Bianchi, Nicola Messina, Fabio Carrara, Marcella Cornia, Lorenzo Baraldi et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### Bilateral Collaboration with Large Vision-Language Models for Open Vocabulary Human-Object Interaction Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01872)
- **作者**: Yupeng Hu, Changxing Ding, Chang Sun, Shaoli Huang, Xiangmin Xu
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### Attention to Trajectory: Trajectory-Aware Open-Vocabulary Tracking.
- **链接**: [arXiv:2503.08145](https://arxiv.org/abs/2503.08145) · 📚 被引 0
- **作者**: Yunhao Li, Yifan Jiao, Dan Meng, Heng Fan, Libo Zhang
- **🏷️ 机构**: Institute of Software Chinese Academy of Sciences, OPPO Research Institute, University of North Texas
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-Vocabulary Multi-Object Tracking (OV-MOT) aims to enable approaches to track objects without being limited to a predefined set of categories. Current OV-MOT methods typically rely primarily on instance-level detection and association, often overlooking trajectory information that is unique and essential for object tracking tasks. Utilizing trajectory information can enhance association stability and classification accuracy, especially in cases of occlusion and category ambiguity, thereby improving adaptability to novel classes. Thus motivated, in this paper we propose \textbf{TRACT}, an open-vocabulary tracker that leverages trajectory information to improve both object association and classification in OV-MOT. Specifically, we introduce a \textit{Trajectory Consistency Reinforcement} (\textbf{TCR}) strategy, that benefits tracking performance by improving target identity and category consistency. In addition, we present \textbf{TraCLIP}, a plug-and-play trajectory classification module. It integrates \textit{Trajectory Feature Aggregation} (\textbf{TFA}) and \textit{Trajectory Semantic Enrichment} (\textbf{TSE}) strategies to fully leverage trajectory information from visual and language perspectives for enhancing the classification results. Extensive experiments on OV-TAO show that our TRACT significantly improves tracking performance, highlighting trajectory information as a valuable asset for OV-MOT. Code will be released.

</details>

### VOVTrack: Exploring the Potentiality in Raw Videos for Open-Vocabulary Multi-Object Tracking.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00701)
- **作者**: Zekun Qian, Ruize Han, Junhui Hou, Linqi Song, Wei Feng
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### COVTrack: Continuous Open-Vocabulary Tracking via Adaptive Multi-Cue Fusion.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00937) · 📚 被引 0
- **作者**: Zekun Qian, Ruize Han, Zhixiang Wang, Junhui Hou, Wei Feng
- **🏷️ 机构**: College of Intelligence and Computing, Tianjin University, Shenzhen University of Advanced Technology, City University of Hong Kong
- **会议**: ICCV 2025

### FLOSS: Free Lunch in Open-Vocabulary Semantic Segmentation.
- **链接**: [arXiv:2504.10487](https://arxiv.org/abs/2504.10487) · [代码](https://github.com/yasserben/FLOSS) · 📚 被引 2
- **作者**: Yasser Benigmim, Mohammad Fahes, Tuan-Hung Vu, Andrei Bursuc, Raoul de Charette
- **🏷️ 机构**: Inria
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we challenge the conventional practice in Open-Vocabulary Semantic Segmentation (OVSS) of using averaged class-wise text embeddings, which are typically obtained by encoding each class name with multiple templates (e.g., a photo of <class>, a sketch of a <class>). We investigate the impact of templates for OVSS, and find that for each class, there exist single-template classifiers--which we refer to as class-experts--that significantly outperform the conventional averaged classifier. First, to identify these class-experts, we introduce a novel approach that estimates them without any labeled data or training. By leveraging the class-wise prediction entropy of single-template classifiers, we select those yielding the lowest entropy as the most reliable class-experts. Second, we combine the outputs of class-experts in a new fusion process. Our plug-and-play method, coined FLOSS, is orthogonal and complementary to existing OVSS methods, offering an improvement without the need for additional labels or training. Extensive experiments show that FLOSS consistently enhances state-of-the-art OVSS models, generalizes well across datasets with different distribution shifts, and delivers substantial improvements in low-data scenarios where only a few unlabeled images are available. Our code is available at https://github.com/yasserben/FLOSS .

</details>

### Training-Free Class Purification for Open-Vocabulary Semantic Segmentation.
- **链接**: [arXiv:2508.00557](https://arxiv.org/abs/2508.00557) · 📚 被引 2
- **作者**: Qi Chen, Lingxiao Yang, Yun Chen, Nailong Zhao, Jianhuang Lai, Jie Shao et al.
- **🏷️ 机构**: Sun Yat-sen University, University of Surrey, Alibaba Cloud Computing
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Fine-tuning pre-trained vision-language models has emerged as a powerful approach for enhancing open-vocabulary semantic segmentation (OVSS). However, the substantial computational and resource demands associated with training on large datasets have prompted interest in training-free methods for OVSS. Existing training-free approaches primarily focus on modifying model architectures and generating prototypes to improve segmentation performance. However, they often neglect the challenges posed by class redundancy, where multiple categories are not present in the current test image, and visual-language ambiguity, where semantic similarities among categories create confusion in class activation. These issues can lead to suboptimal class activation maps and affinity-refined activation maps. Motivated by these observations, we propose FreeCP, a novel training-free class purification framework designed to address these challenges. FreeCP focuses on purifying semantic categories and rectifying errors caused by redundancy and ambiguity. The purified class representations are then leveraged to produce final segmentation predictions. We conduct extensive experiments across eight benchmarks to validate FreeCP's effectiveness. Results demonstrate that FreeCP, as a plug-and-play module, significantly boosts segmentation performance when combined with other OVSS methods.

</details>

### Plug-in Feedback Self-Adaptive Attention in CLIP for Training-Free Open-Vocabulary Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02118)
- **作者**: Zhixiang Chi, Yanan Wu, Li Gu, Huan Liu, Ziqiang Wang, Yang Zhang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### 풟ℐℋ-CLIP: Unleashing the Diversity of Multi-Head Self-Attention for Training-Free Open-Vocabulary Semantic Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02116)
- **作者**: Songsong Duan, Xi Yang, Nannan Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### Superpowering Open-Vocabulary Object Detectors for X-ray Vision.
- **链接**: [arXiv:2503.17071](https://arxiv.org/abs/2503.17071) · [代码](https://github.com/PAGF188/RAXO) · 📚 被引 1
- **作者**: Pablo Garcia-Fernandez, Lorenzo Vaquero, Mingxuan Liu, Feng Xue, Daniel Cores, Nicu Sebe et al.
- **🏷️ 机构**: University of Santiago de Compostela,Spain, University of Trento,Italy, Fondazione Bruno Kessler,Italy
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-vocabulary object detection (OvOD) is set to revolutionize security screening by enabling systems to recognize any item in X-ray scans. However, developing effective OvOD models for X-ray imaging presents unique challenges due to data scarcity and the modality gap that prevents direct adoption of RGB-based solutions. To overcome these limitations, we propose RAXO, a training-free framework that repurposes off-the-shelf RGB OvOD detectors for robust X-ray detection. RAXO builds high-quality X-ray class descriptors using a dual-source retrieval strategy. It gathers relevant RGB images from the web and enriches them via a novel X-ray material transfer mechanism, eliminating the need for labeled databases. These visual descriptors replace text-based classification in OvOD, leveraging intra-modal feature distances for robust detection. Extensive experiments demonstrate that RAXO consistently improves OvOD performance, providing an average mAP increase of up to 17.0 points over base detectors. To further support research in this emerging field, we also introduce DET-COMPASS, a new benchmark featuring bounding box annotations for over 300 object categories, enabling large-scale evaluation of OvOD in X-ray. Code and dataset available at: https://github.com/PAGF188/RAXO.

</details>

### CLIP-Adapted Region-to-Text Learning for Generative Open-Vocabulary Semantic Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02228)
- **作者**: Jiannan Ge, Lingxi Xie, Hongtao Xie, Pandeng Li, Sun-Ao Liu, Xiaopeng Zhang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### SPADE: Spatial-Aware Denoising Network for Open-Vocabulary Panoptic Scene Graph Generation with Long- and Local-Range Context Reasoning.
- **链接**: [arXiv:2507.05798](https://arxiv.org/abs/2507.05798) · 📚 被引 1
- **作者**: Xin Hu, Ke Qin, Guiduo Duan, Ming Li, Yuan-Fang Li, Tao He
- **🏷️ 机构**: The Laboratory of Intelligent Collaborative Computing of UESTC, Guangdong Laboratory of Artificial Intelligence and Digital Economy (SZ), Monash University
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Panoptic Scene Graph Generation (PSG) integrates instance segmentation with relation understanding to capture pixel-level structural relationships in complex scenes. Although recent approaches leveraging pre-trained vision-language models (VLMs) have significantly improved performance in the open-vocabulary setting, they commonly ignore the inherent limitations of VLMs in spatial relation reasoning, such as difficulty in distinguishing object relative positions, which results in suboptimal relation prediction. Motivated by the denoising diffusion model's inversion process in preserving the spatial structure of input images, we propose SPADE (SPatial-Aware Denoising-nEtwork) framework -- a novel approach for open-vocabulary PSG. SPADE consists of two key steps: (1) inversion-guided calibration for the UNet adaptation, and (2) spatial-aware context reasoning. In the first step, we calibrate a general pre-trained teacher diffusion model into a PSG-specific denoising network with cross-attention maps derived during inversion through a lightweight LoRA-based fine-tuning strategy. In the second step, we develop a spatial-aware relation graph transformer that captures both local and long-range contextual information, facilitating the generation of high-quality relation queries. Extensive experiments on benchmark PSG and Visual Genome datasets demonstrate that SPADE outperforms state-of-the-art methods in both closed- and open-set scenarios, particularly for spatial relationship prediction.

</details>

### SCORE: Scene Context Matters in Open-Vocabulary Remote Sensing Instance Segmentation.
- **链接**: [arXiv:2507.12857](https://arxiv.org/abs/2507.12857) · [代码](https://github.com/HuangShiqi128/SCORE) · 📚 被引 1
- **作者**: Shiqi Huang, Shuting He, Huaiyuan Qin, Bihan Wen
- **🏷️ 机构**: School of Electrical and Electronic Engineering, Nanyang Technological University, Shanghai University of Finance and Economics,MoE Key Laboratory of Interdisciplinary Research of Computation and Economics, Institute for Infocomm Research (IR), A*STAR,Singapore
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Most existing remote sensing instance segmentation approaches are designed for close-vocabulary prediction, limiting their ability to recognize novel categories or generalize across datasets. This restricts their applicability in diverse Earth observation scenarios. To address this, we introduce open-vocabulary (OV) learning for remote sensing instance segmentation. While current OV segmentation models perform well on natural image datasets, their direct application to remote sensing faces challenges such as diverse landscapes, seasonal variations, and the presence of small or ambiguous objects in aerial imagery. To overcome these challenges, we propose $\textbf{SCORE}$ ($\textbf{S}$cene $\textbf{C}$ontext matters in $\textbf{O}$pen-vocabulary $\textbf{RE}$mote sensing instance segmentation), a framework that integrates multi-granularity scene context, i.e., regional context and global context, to enhance both visual and textual representations. Specifically, we introduce Region-Aware Integration, which refines class embeddings with regional context to improve object distinguishability. Additionally, we propose Global Context Adaptation, which enriches naive text embeddings with remote sensing global context, creating a more adaptable and expressive linguistic latent space for the classifier. We establish new benchmarks for OV remote sensing instance segmentation across diverse datasets. Experimental results demonstrate that, our proposed method achieves SOTA performance, which provides a robust solution for large-scale, real-world geospatial analysis. Our code is available at https://github.com/HuangShiqi128/SCORE.

</details>

### Identity-Aware Language Gaussian Splatting for Open-Vocabulary 3D Semantic Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01903) · 📚 被引 1
- **作者**: SungMin Jang, Wonjun Kim
- **🏷️ 机构**: Konkuk University
- **会议**: ICCV 2025

### Feature Purification Matters: Suppressing Outlier Propagation for Training-Free Open-Vocabulary Semantic Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01887) · 📚 被引 0
- **作者**: Shuo Jin, Siyue Yu, Bingfeng Zhang, Mingjie Sun, Yi Dong, Jimin Xiao
- **🏷️ 机构**: Xi&#x0027;an Jiaotong-Liverpool University, China University of Petroleum (East China), Soochow University
- **会议**: ICCV 2025

### Details Matter for Indoor Open-Vocabulary 3D Instance Segmentation.
- **链接**: [arXiv:2507.23134](https://arxiv.org/abs/2507.23134) · 📚 被引 0
- **作者**: Sanghun Jung, Jingjing Zheng, Ke Zhang, Nan Qiao, Albert Y. C. Chen, Lu Xia et al.
- **🏷️ 机构**: University of Washington, Amazon Lab126
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Unlike closed-vocabulary 3D instance segmentation that is often trained end-to-end, open-vocabulary 3D instance segmentation (OV-3DIS) often leverages vision-language models (VLMs) to generate 3D instance proposals and classify them. While various concepts have been proposed from existing research, we observe that these individual concepts are not mutually exclusive but complementary. In this paper, we propose a new state-of-the-art solution for OV-3DIS by carefully designing a recipe to combine the concepts together and refining them to address key challenges. Our solution follows the two-stage scheme: 3D proposal generation and instance classification. We employ robust 3D tracking-based proposal aggregation to generate 3D proposals and remove overlapped or partial proposals by iterative merging/removal. For the classification stage, we replace the standard CLIP model with Alpha-CLIP, which incorporates object masks as an alpha channel to reduce background noise and obtain object-centric representation. Additionally, we introduce the standardized maximum similarity (SMS) score to normalize text-to-proposal similarity, effectively filtering out false positives and boosting precision. Our framework achieves state-of-the-art performance on ScanNet200 and S3DIS across all AP and AR metrics, even surpassing an end-to-end closed-vocabulary method.

</details>

### Open-Vocabulary Hoi Detection With Interaction-Aware Prompt and Concept Calibration.
- **链接**: [arXiv:2508.03207](https://arxiv.org/abs/2508.03207) · [代码](https://github.com/ltttpku/INP-CC) · 📚 被引 3
- **作者**: Ting Lei, Shaofeng Yin, Qingchao Chen, Yuxin Peng, Yang Liu
- **🏷️ 机构**: Wangxuan Institute of Computer Technology,Peking University, National Institute of Health Data Science,Peking University
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open Vocabulary Human-Object Interaction (HOI) detection aims to detect interactions between humans and objects while generalizing to novel interaction classes beyond the training set. Current methods often rely on Vision and Language Models (VLMs) but face challenges due to suboptimal image encoders, as image-level pre-training does not align well with the fine-grained region-level interaction detection required for HOI. Additionally, effectively encoding textual descriptions of visual appearances remains difficult, limiting the model's ability to capture detailed HOI relationships. To address these issues, we propose INteraction-aware Prompting with Concept Calibration (INP-CC), an end-to-end open-vocabulary HOI detector that integrates interaction-aware prompts and concept calibration. Specifically, we propose an interaction-aware prompt generator that dynamically generates a compact set of prompts based on the input scene, enabling selective sharing among similar interactions. This approach directs the model's attention to key interaction patterns rather than generic image-level semantics, enhancing HOI detection. Furthermore, we refine HOI concept representations through language model-guided calibration, which helps distinguish diverse HOI concepts by investigating visual similarities across categories. A negative sampling strategy is also employed to improve inter-modal similarity modeling, enabling the model to better differentiate visually similar but semantically distinct actions. Extensive experimental results demonstrate that INP-CC significantly outperforms state-of-the-art models on the SWIG-HOI and HICO-DET datasets. Code is available at https://github.com/ltttpku/INP-CC.

</details>

### Unbiased Region-Language Alignment for Open-Vocabulary Dense Prediction.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02209) · 📚 被引 2
- **作者**: Yunheng Li, Yuxuan Li, Quan-Sheng Zeng, Wenhai Wang, Qibin Hou, Ming-Ming Cheng
- **🏷️ 机构**: Nankai University,VCIP, CS, Shanghai AI Laboratory,OpenGVLab
- **会议**: ICCV 2025

### Images as Noisy Labels: Unleashing the Potential of the Diffusion Model for Open-Vocabulary Semantic Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02248) · 📚 被引 0
- **作者**: Fan Li, Xuanbin Wang, Xuan Wang, Zhaoxiang Zhang, Yuelei Xu
- **🏷️ 机构**: Northwestern Polytechnical University
- **会议**: ICCV 2025

### Stepping Out of Similar Semantic Space for Open-Vocabulary Segmentation.
- **链接**: [arXiv:2506.16058](https://arxiv.org/abs/2506.16058) · 📚 被引 1
- **作者**: Yong Liu, Song-Li Wu, Sule Bai, Jiahao Wang, Yitong Wang, Yansong Tang
- **🏷️ 机构**: Tsinghua Shenzhen International Graduate School, The University of Hong Kong, ByteDance Inc.
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-vocabulary segmentation aims to achieve segmentation of arbitrary categories given unlimited text inputs as guidance. To achieve this, recent works have focused on developing various technical routes to exploit the potential of large-scale pre-trained vision-language models and have made significant progress on existing benchmarks. However, we find that existing test sets are limited in measuring the models' comprehension of ``open-vocabulary" concepts, as their semantic space closely resembles the training space, even with many overlapping categories. To this end, we present a new benchmark named OpenBench that differs significantly from the training semantics. It is designed to better assess the model's ability to understand and segment a wide range of real-world concepts. When testing existing methods on OpenBench, we find that their performance diverges from the conclusions drawn on existing test sets. In addition, we propose a method named OVSNet to improve the segmentation performance for diverse and open scenarios. Through elaborate fusion of heterogeneous features and cost-free expansion of the training space, OVSNet achieves state-of-the-art results on both existing datasets and our proposed OpenBench. Corresponding analysis demonstrate the soundness and effectiveness of our proposed benchmark and method.

</details>

### Vision-Language Interactive Relation Mining for Open-Vocabulary Scene Graph Generation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01556) · 📚 被引 1
- **作者**: Yukuan Min, Muli Yang, Jinhao Zhang, Yuxuan Wang, Aming Wu, Cheng Deng
- **🏷️ 机构**: Xidian University,China, A*STAR,Singapore
- **会议**: ICCV 2025

### Understanding Personal Concept in Open-Vocabulary Semantic Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01856) · 📚 被引 1
- **作者**: Sunghyun Park, Jungsoo Lee, Shubhankar Borse, Munawar Hayat, Sungha Choi, Kyuwoong Hwang et al.
- **🏷️ 机构**: Qualcomm AI Research
- **会议**: ICCV 2025

### ROVI: A VLM-LLM Re-Captioned Dataset for Open-Vocabulary Instance-Grounded Text-to-Image Generation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01879)
- **作者**: Cihang Peng, Qiming Hou, Zhong Ren, Kun Zhou
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### DiSCO-3D : Discovering and Segmenting Sub-Concepts from Open-Vocabulary Queries in NeRF.
- **链接**: [arXiv:2507.14596](https://arxiv.org/abs/2507.14596) · 📚 被引 0
- **作者**: Doriand Petit, Steve Bourgeois, Vincent Gay-Bellile, Florian Chabot, Loïc Barthe
- **🏷️ 机构**: Universit&#x00E9; Paris-Saclay,CEA, List,Palaiseau,France,F-91120, IRIT Universit&#x00E9; de Toulouse CNRS,France
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D semantic segmentation provides high-level scene understanding for applications in robotics, autonomous systems, \textit{etc}. Traditional methods adapt exclusively to either task-specific goals (open-vocabulary segmentation) or scene content (unsupervised semantic segmentation). We propose DiSCO-3D, the first method addressing the broader problem of 3D Open-Vocabulary Sub-concepts Discovery, which aims to provide a 3D semantic segmentation that adapts to both the scene and user queries. We build DiSCO-3D on Neural Fields representations, combining unsupervised segmentation with weak open-vocabulary guidance. Our evaluations demonstrate that DiSCO-3D achieves effective performance in Open-Vocabulary Sub-concepts Discovery and exhibits state-of-the-art results in the edge cases of both open-vocabulary and unsupervised segmentation.

</details>

### Sliced Wasserstein Bridge for Open-Vocabulary Video Instance Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01159) · 📚 被引 6
- **作者**: Zheyun Qin, Deng Yu, Chuanchen Luo, Zhumin Chen
- **🏷️ 机构**: School of Computer Science and Technology, Shandong University, School of Artificial Intelligence, Shandong University
- **会议**: ICCV 2025

### Seeing the Unseen: A Semantic Alignment and Context-Aware Prompt Framework for Open-Vocabulary Camouflaged Object Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02196) · 📚 被引 2
- **作者**: Peng Ren, Tian Bai, Jing Sun, Fuming Sun
- **🏷️ 机构**: College of Computer Science and Technology, Jilin University, School of Information and Communication Engineering, Dalian Minzu University
- **会议**: ICCV 2025

### Harnessing Vision Foundation Models for High-Performance, Training-Free Open Vocabulary Segmentation.
- **链接**: [arXiv:2411.09219](https://arxiv.org/abs/2411.09219) · [代码](https://github.com/YuHengsss/Trident) · 📚 被引 4
- **作者**: Yuheng Shi, Minjing Dong, Chang Xu
- **🏷️ 机构**: University of Sydney, City University of Hong Kong
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While Contrastive Language-Image Pre-training (CLIP) has advanced open-vocabulary predictions, its performance on semantic segmentation remains suboptimal. This shortfall primarily stems from its spatial-invariant semantic features and constrained resolution. While previous adaptations addressed spatial invariance semantic by modifying the self-attention in CLIP's image encoder, the issue of limited resolution remains unexplored. Different from previous segment-then-splice methods that segment sub-images via a sliding window and splice the results, we introduce a splice-then-segment paradigm that incorporates Segment-Anything Model (SAM) to tackle the resolution issue since SAM excels at extracting fine-grained semantic correlations from high-resolution images. Specifically, we introduce Trident, a training-free framework that first splices features extracted by CLIP and DINO from sub-images, then leverages SAM's encoder to create a correlation matrix for global aggregation, enabling a broadened receptive field for effective segmentation. Besides, we propose a refinement strategy for CLIP's coarse segmentation outputs by transforming them into prompts for SAM, further enhancing the segmentation performance. Trident achieves a significant improvement in the mIoU across eight benchmarks compared with the current SOTA, increasing from 44.4 to 48.6.Code is available at https://github.com/YuHengsss/Trident.

</details>

### OVA-Fields: Weakly Supervised Open-Vocabulary Affordance Fields for Robot Operational Part Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00602) · 📚 被引 2
- **作者**: Heng Su, Mengying Xie, Nieqing Cao, Yan Ding, Beichen Shao, Xianlei Long et al.
- **🏷️ 机构**: Chongqing University, Xi&#x0027;an Jiaotong-Liverpool University, Shanghai AI Lab
- **会议**: ICCV 2025

### CLIPeR: Hierarchically Improving Spatial Representation of CLIP for Open-Vocabulary Semantic Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02154)
- **作者**: Lin Sun, Jiale Cao, Jin Xie, Xiaoheng Jiang, Yanwei Pang
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### Open-Vocabulary Octree-Graph for 3D Scene Understanding.
- **链接**: [arXiv:2411.16253](https://arxiv.org/abs/2411.16253) · [代码](https://github.com/yifeisu/OV-Octree-Graph) · 📚 被引 0
- **作者**: Zhigang Wang, Yifei Su, Chenhui Li, Dong Wang, Yan Huang, Xuelong Li et al.
- **🏷️ 机构**: Northwestern Polytechnical University, University of Chinese Academy of Sciences, Shanghai AI Laboratory
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-vocabulary 3D scene understanding is indispensable for embodied agents. Recent works leverage pretrained vision-language models (VLMs) for object segmentation and project them to point clouds to build 3D maps. Despite progress, a point cloud is a set of unordered coordinates that requires substantial storage space and does not directly convey occupancy information or spatial relation, making existing methods inefficient for downstream tasks, e.g., path planning and text-based object retrieval. To address these issues, we propose \textbf{Octree-Graph}, a novel scene representation for open-vocabulary 3D scene understanding. Specifically, a Chronological Group-wise Segment Merging (CGSM) strategy and an Instance Feature Aggregation (IFA) algorithm are first designed to get 3D instances and corresponding semantic features. Subsequently, an adaptive-octree structure is developed that stores semantics and depicts the occupancy of an object adjustably according to its shape. Finally, the Octree-Graph is constructed where each adaptive-octree acts as a graph node, and edges describe the spatial relations among nodes. Extensive experiments on various tasks are conducted on several widely-used datasets, demonstrating the versatility and effectiveness of our method. Code is available \href{https://github.com/yifeisu/OV-Octree-Graph}{here}.

</details>

### ReME: A Data-Centric Framework for Training-Free Open-Vocabulary Segmentation.
- **链接**: [arXiv:2506.21233](https://arxiv.org/abs/2506.21233) · [代码](https://github.com/xiweix/ReME) · 📚 被引 2
- **作者**: Xiwei Xuan, Ziquan Deng, Kwan-Liu Ma
- **🏷️ 机构**: University of California, Davis
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Training-free open-vocabulary semantic segmentation (OVS) aims to segment images given a set of arbitrary textual categories without costly model fine-tuning. Existing solutions often explore attention mechanisms of pre-trained models, such as CLIP, or generate synthetic data and design complex retrieval processes to perform OVS. However, their performance is limited by the capability of reliant models or the suboptimal quality of reference sets. In this work, we investigate the largely overlooked data quality problem for this challenging dense scene understanding task, and identify that a high-quality reference set can significantly benefit training-free OVS. With this observation, we introduce a data-quality-oriented framework, comprising a data pipeline to construct a reference set with well-paired segment-text embeddings and a simple similarity-based retrieval to unveil the essential effect of data. Remarkably, extensive evaluations on ten benchmark datasets demonstrate that our method outperforms all existing training-free OVS approaches, highlighting the importance of data-centric design for advancing OVS without training. Our code is available at https://github.com/xiweix/ReME .

</details>

### ATAS: Any-to-Any Self-Distillation for Enhanced Open-Vocabulary Dense Prediction.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01896) · 📚 被引 0
- **作者**: Juan Yeo, Soonwoo Cha, Jiwoo Song, Hyunbin Jin, Taesup Kim
- **🏷️ 机构**: Gradudate School of Data Science, Seoul National University
- **会议**: ICCV 2025

### Learning to Generalize Without Bias for Open-Vocabulary Action Recognition.
- **链接**: [arXiv:2502.20158](https://arxiv.org/abs/2502.20158) · [代码](https://github.com/Mia-YatingYu/Open-MeDe) · 📚 被引 1
- **作者**: Yating Yu, Congqi Cao, Yifan Zhang, Yanning Zhang
- **🏷️ 机构**: Northwestern Polytechnical University, Institute of Automation, Chinese Academy of Sciences
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Leveraging the effective visual-text alignment and static generalizability from CLIP, recent video learners adopt CLIP initialization with further regularization or recombination for generalization in open-vocabulary action recognition in-context. However, due to the static bias of CLIP, such video learners tend to overfit on shortcut static features, thereby compromising their generalizability, especially to novel out-of-context actions. To address this issue, we introduce Open-MeDe, a novel Meta-optimization framework with static Debiasing for Open-vocabulary action recognition. From a fresh perspective of generalization, Open-MeDe adopts a meta-learning approach to improve known-to-open generalizing and image-to-video debiasing in a cost-effective manner. Specifically, Open-MeDe introduces a cross-batch meta-optimization scheme that explicitly encourages video learners to quickly generalize to arbitrary subsequent data via virtual evaluation, steering a smoother optimization landscape. In effect, the free of CLIP regularization during optimization implicitly mitigates the inherent static bias of the video meta-learner. We further apply self-ensemble over the optimization trajectory to obtain generic optimal parameters that can achieve robust generalization to both in-context and out-of-context novel data. Extensive evaluations show that Open-MeDe not only surpasses state-of-the-art regularization methods tailored for in-context open-vocabulary action recognition but also substantially excels in out-of-context scenarios.Code is released at https://github.com/Mia-YatingYu/Open-MeDe.

</details>

### DanceEditor: Towards Iterative Editable Music-Driven Dance Generation with Open-Vocabulary Descriptions.
- **链接**: [arXiv:2508.17342](https://arxiv.org/abs/2508.17342) · 📚 被引 3
- **作者**: Hengyuan Zhang, Zhe Li, Xingqun Qi, Mengze Li, Muyi Sun, Siye Wang et al.
- **🏷️ 机构**: Peking University, The Hong Kong University of Science and Technology, Beijing University of Posts and Telecommunications
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Generating coherent and diverse human dances from music signals has gained tremendous progress in animating virtual avatars. While existing methods support direct dance synthesis, they fail to recognize that enabling users to edit dance movements is far more practical in real-world choreography scenarios. Moreover, the lack of high-quality dance datasets incorporating iterative editing also limits addressing this challenge. To achieve this goal, we first construct DanceRemix, a large-scale multi-turn editable dance dataset comprising the prompt featuring over 25.3M dance frames and 84.5K pairs. In addition, we propose a novel framework for iterative and editable dance generation coherently aligned with given music signals, namely DanceEditor. Considering the dance motion should be both musical rhythmic and enable iterative editing by user descriptions, our framework is built upon a prediction-then-editing paradigm unifying multi-modal conditions. At the initial prediction stage, our framework improves the authority of generated results by directly modeling dance movements from tailored, aligned music. Moreover, at the subsequent iterative editing stages, we incorporate text descriptions as conditioning information to draw the editable results through a specifically designed Cross-modality Editing Module (CEM). Specifically, CEM adaptively integrates the initial prediction with music and text prompts as temporal motion cues to guide the synthesized sequences. Thereby, the results display music harmonics while preserving fine-grained semantic alignment with text descriptions. Extensive experiments demonstrate that our method outperforms the state-of-the-art models on our newly collected DanceRemix dataset. Code is available at https://lzvsdy.github.io/DanceEditor/.

</details>

### CorrCLIP: Reconstructing Patch Correlations in CLIP for Open-Vocabulary Semantic Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02288)
- **作者**: Dengke Zhang, Fagui Liu, Quan Tang
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### OV3D-CG: Open-Vocabulary 3D Instance Segmentation with Contextual Guidance.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00504) · 📚 被引 0
- **作者**: Mingquan Zhou, Chen He, Ruiping Wang, Xilin Chen
- **🏷️ 机构**: Institute of Computing Technology, Chinese Academy of Sciences,China
- **会议**: ICCV 2025

## 跨领域论文（完整笔记在其他领域）

- Dynamic-DINO: Fine-Grained Mixture of Experts Tuning for Real-Time Open-Vocabulary Object Detection. → [object-detection](../object-detection/Guideline%202025.md)
- OV-SCAN: Semantically Consistent Alignment for Novel Object Discovery in Open-Vocabulary 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202025.md)
- OpenM3D: Open Vocabulary Multi-View Indoor 3D Object Detection without Human Annotations. → [3d-detection](../3d-detection/Guideline%202025.md)
- Benefit from Seen: Enhancing Open-Vocabulary Object Detection by Bridging Visual and Textual Co-Occurrence Knowledge. → [object-detection](../object-detection/Guideline%202025.md)
- SFUOD: Source-Free Unknown Object Detection. → [object-detection](../object-detection/Guideline%202025.md)
- 3D-MOOD: Lifting 2D to 3D for Monocular Open-Set Object Detection. → [object-detection](../object-detection/Guideline%202025.md)
- ASGS: Single-Domain Generalizable Open-Set Object Detection via Adaptive Subgraph Searching. → [object-detection](../object-detection/Guideline%202025.md)
- SAMPLE: Semantic Alignment through Temporal-Adaptive Multimodal Prompt Learning for Event-Based Open-Vocabulary Action Recognition. → [multimodal](../multimodal/Guideline%202025.md)
- Open-Set Cross Modal Generalization via Multimodal Unified Representation. → [multimodal](../multimodal/Guideline%202025.md)
- CapeLLM: Support-Free Category-Agnostic Pose Estimation with Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- MPBR: Multimodal Progressive Bidirectional Reasoning for Open-Set Fine-Grained Recognition. → [multimodal](../multimodal/Guideline%202025.md)
