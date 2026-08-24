# 📚 arXiv 每日论文报告（我的领域）

**报告日期**: 2026-08-24  
**论文来源**: [arXiv cs.CV Recent](https://arxiv.org/list/cs.CV/recent)  
**关注论文数**: 38 篇（关键词匹配模式，未配置 LLM）

> 匹配领域: 3D Detection、BEV、Occupancy、Multi-camera Perception、Tracking、Open Vocabulary Detection、FOD Detection、VLM、Vision Transformer、Self-supervised Vision、Video Understanding、Multimodal、Continual Learning、Neural Architecture Search、Network Pruning、Knowledge Distillation

## 📑 目录

- [VLM](#vlm) (8篇)
- [Multimodal](#multimodal) (8篇)
- [Multi-camera Perception](#multi-camera-perception) (6篇)
- [Network Pruning](#network-pruning) (5篇)
- [Video Understanding](#video-understanding) (3篇)
- [Vision Transformer](#vision-transformer) (3篇)
- [Open Vocabulary Detection](#open-vocabulary-detection) (2篇)
- [Knowledge Distillation](#knowledge-distillation) (1篇)
- [BEV](#bev) (1篇)
- [Self-supervised Vision](#self-supervised-vision) (1篇)

## VLM

### 1. Is Visual Prompting All You Need? Studying VLM Spatial Reasoning under Progressive Visual Scaffolds

- **arXiv ID**: [2608.21170](https://arxiv.org/abs/2608.21170)  · [📄 PDF](https://arxiv.org/pdf/2608.21170)
- **作者**: Lars Benedikt Kaesberg, Tianyu Yang, Florian Valentin Wunderlich et al. (7 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV, cs.AI
- **摘要摘录**: Vision-language models (VLMs) have advanced rapidly in multimodal reasoning, yet recent work shows that their failures often reflect an interaction between visual grounding and downstream reasoning. What remains less clear is how the visual presentation of a task shapes model performance and failure modes when the underlying reasoning problem is unchanged.

### 2. CARD: Diagnosing Belief to Action Routing Failures in Vision Language Models

- **arXiv ID**: [2608.20763](https://arxiv.org/abs/2608.20763)  · [📄 PDF](https://arxiv.org/pdf/2608.20763)
- **作者**: Souptik Kumar Majumdar, Fabian Kögel, Andreas Bulling
- **提交日期**: 2026-08-21 · **分类**: cs.CV, cs.AI
- **摘要摘录**: Linear probes and activation steering have uncovered that vision-language models (VLMs) internally represent mental states such as agents' beliefs, knowledge, and intentions. However, it is unclear whether and how these representations are used by downstream predictions along these axes.

### 3. A VLM Answer Is Not an Anomaly Score: Rank Compression in Training-Free Video Anomaly Detection

- **arXiv ID**: [2608.21244](https://arxiv.org/abs/2608.21244)  · [📄 PDF](https://arxiv.org/pdf/2608.21244)
- **作者**: Inpyo Song, Jangwon Lee
- **提交日期**: 2026-08-21 · **分类**: cs.CV
- **摘要摘录**: Vision-language models enable training-free video anomaly detection by answering questions about video segments. VAD benchmarks, however, require a scalar anomaly score for each segment and evaluate the resulting ranking using the AUROC or AP.

### 4. Llama-Mobile: Efficient 2.7-Bit Quantization of VLMs

- **arXiv ID**: [2608.21134](https://arxiv.org/abs/2608.21134)  · [📄 PDF](https://arxiv.org/pdf/2608.21134)
- **作者**: Luka Ribar, Jeevan Bhoot, Douglas Orr
- **提交日期**: 2026-08-21 · **分类**: cs.CV, cs.LG
- **摘要摘录**: Deploying vision-language models (VLMs) on mobile devices is challenging due to their significant memory and compute requirements. We present a framework for quantizing VLMs for efficient inference on resource-constrained hardware.

### 5. Re$^3$Cap: Retrieval-Guided Refinement for Image Captioning Enhancement via Reinforcement Learning

- **arXiv ID**: [2608.21305](https://arxiv.org/abs/2608.21305)  · [📄 PDF](https://arxiv.org/pdf/2608.21305)
- **作者**: Haonan Jia, Shichao Dong, Zenghui Sun et al. (10 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV, cs.AI
- **摘要摘录**: Reinforcement Learning (RL) has demonstrated significant gains in image captioning, yet it is still limited in encouraging Large Vision-Language Models (LVLMs) to explore novel reasoning strategies. This limitation leads to a performance gap between RL and Supervised Fine-Tuning (SFT).

### 6. Toward Vision Language Model-based Assessment of Clinical Quality and Usability of LGE-MR Images for Cardiac Ablation Planning

- **arXiv ID**: [2608.21180](https://arxiv.org/abs/2608.21180)  · [📄 PDF](https://arxiv.org/pdf/2608.21180)
- **作者**: Bipasha Kundu, Abhishek Chaturvedi, Axel W. E. Wismueller et al. (5 authors)
- **提交日期**: 2026-08-21 · **分类**: eess.IV, cs.CV
- **摘要摘录**: LGE cardiac MRI is widely used for left atrial fibrosis assessment and ablation planning in atrial fibrillation patients as knowledge of fibrotic tissue regions identified from LGE-MRI is critical for catheter ablation. Often, poor quality images used during ablation planning can cause mis-localization of ablation targets, directly impacting procedure safety and outcome.

### 7. COMET: Contrastive Motion-Enhanced Temporal Reasoning for Video Multimodal Large Language Models

- **arXiv ID**: [2608.21030](https://arxiv.org/abs/2608.21030)  · [📄 PDF](https://arxiv.org/pdf/2608.21030)
- **作者**: Chenghua Zhu, Zhaolu Kang, Qifan Shi et al. (11 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV, cs.CL, cs.LG
- **摘要摘录**: Video multimodal large language models have advanced significantly, yet fine-grained motion-temporal understanding remains fragile. The core bottleneck is not only sparse frame sampling, but also the lack of a complete temporal modeling pipeline for explicitly representing frame-to-frame change, enabling appearance-motion interaction, and optimizing temporal direction sensitivity.

### 8. A Modular Agent for Reliable and Auditable Spatial Relation Verification in CT Scans

- **arXiv ID**: [2608.21140](https://arxiv.org/abs/2608.21140)  · [📄 PDF](https://arxiv.org/pdf/2608.21140)
- **作者**: Simon Vincent Abel, Heiko Hillenhagen, Michael Götz et al. (6 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV, cs.AI
- **摘要摘录**: Reliable spatial understanding is an important prerequisite for future medical vision-language systems that aim to support radiological report generation and structured image understanding. While modern vision-language models (VLMs) show promising performance on many medical imaging tasks, recent evidence suggests they remain weak in controlled spatial reasoning and often fail to reliably ground spatial relations in image evidence.

---

## Multimodal

### 1. A Collaborative Multi-Modality Interaction for VLA-based End-to-End Autonomous Driving

- **arXiv ID**: [2608.20890](https://arxiv.org/abs/2608.20890)  · [📄 PDF](https://arxiv.org/pdf/2608.20890)
- **作者**: Jingtao Sun, Xiaohai He, Yike Zhang et al. (7 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV, cs.RO
- **摘要摘录**: Vision-Language-Action (VLA) models have emerged as a powerful paradigm for end-to-end autonomous driving by jointly integrating perception, reasoning, and decision making within a unified multimodal framework. However, most existing VLA models formulate end-to-end autonomous driving as a visual question answering task, leading to unreliable and less interpretable decision reasoning.

### 2. SuppreSensing: Expert-Guided Feature Recalibration and Discrepancy Augmentation for Multimodal Object Detection

- **arXiv ID**: [2608.20944](https://arxiv.org/abs/2608.20944)  · [📄 PDF](https://arxiv.org/pdf/2608.20944)
- **作者**: Xin Wu, Zhenyu Gao, Qiankun Zhang et al. (4 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV
- **摘要摘录**: Multimodal object detection in remote sensing faces challenges due to semantic heterogeneity and modality-specific noise interference. To this end, we propose SuppreSensing, which reformulates multimodal fusion as a selective collaboration process that jointly models shared information and modality-specific cues.

### 3. VT-MUSE: Multimodal Unified Sequential Visuotactile Representation Learning for Manipulation

- **arXiv ID**: [2608.21290](https://arxiv.org/abs/2608.21290)  · [📄 PDF](https://arxiv.org/pdf/2608.21290)
- **作者**: Congsheng Xu, Qiaochu Yang, Fangyuan Shi et al. (10 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.RO, cs.CV
- **摘要摘录**: We propose VT-MUSE, a Multimodal Unified SEquential representation learning framework for visuotactilemanipulation. Existing approaches often encode visual and tactile observations independently before fusion, limiting their ability to capture fine-grained cross-modal dependencies.

### 4. Masking Is Not Enough: Generative Restoration for Multimodal De-Identification in Medical AI

- **arXiv ID**: [2608.21133](https://arxiv.org/abs/2608.21133)  · [📄 PDF](https://arxiv.org/pdf/2608.21133)
- **作者**: Shiva Shrestha, Zongxing Xie, Chen Zhao et al. (6 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV, cs.CR
- **摘要摘录**: Medical image-text data can expose protected health information (PHI) through both visible image content as well as accompanying text, creating a barrier to privacy-preserving medical AI systems. This risk is especially prominent in multimodal systems, where images, questions, reports, and clinical context may enter training, evaluation, or inference pipelines.

### 5. A2DINOv3: Rethinking Multi-Modal Object Detection via Socialized Collaboration

- **arXiv ID**: [2608.21099](https://arxiv.org/abs/2608.21099)  · [📄 PDF](https://arxiv.org/pdf/2608.21099)
- **作者**: Jiekang Feng, Zhihe Fan, Yunqi Zhu et al. (8 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV, cs.AI
- **摘要摘录**: Multi-modal object detection is essential for robust scene understanding in challenging conditions, including low-light and adverse environments. Recent vision foundation models (e.g., DINOv3) have exhibited strong representation capabilities, yet adapting them to multi-modal scenarios remains challenging.

### 6. Kinematic Knowledge Maps for Pattern Alignment: Structured Latent Representational Learning in Multimodal Gait Analysis

- **arXiv ID**: [2608.20969](https://arxiv.org/abs/2608.20969)  · [📄 PDF](https://arxiv.org/pdf/2608.20969)
- **作者**: Chen Dong, He Zonglin, Cheung Kenneth M. C
- **提交日期**: 2026-08-21 · **分类**: cs.CV
- **摘要摘录**: Multimodal clinical AI is limited by weakly aligned inputs and the absence of domain-specific interpretable representations, particularly when learning from dense video stream, structured time-series, and template-based kinematic text. Here we present ScoliDetect, an explainable framework for adolescent idiopathic scoliosis screening from monocular gait video, built around a kinematic knowledge map (KKM) and complementary template-based kinematic text derived from per-sequence pose statics.

### 7. EmotionDialogCN: A Spontaneous Multimodal Dataset for Mandarin Emotional Dialogue

- **arXiv ID**: [2608.20905](https://arxiv.org/abs/2608.20905)  · [📄 PDF](https://arxiv.org/pdf/2608.20905)
- **作者**: Yi Zheng, Yifan Xu, Yan Zhou et al. (11 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV
- **摘要摘录**: Face-to-face audiovisual interaction is central to human communication, conveying rich emotional and social cues. However, existing multimodal dialogue datasets remain limited by inadequate emotion annotations, poor emotional diversity, and small scale.

### 8. Recognition-Conditioned Reasoning: A Training-Free Multimodal-LLM Pipeline for Fine-Grained Micro-Action Understanding

- **arXiv ID**: [2608.21022](https://arxiv.org/abs/2608.21022)  · [📄 PDF](https://arxiv.org/pdf/2608.21022)
- **作者**: Fengshun Wang, Jin'ang Han, Zhigang Tu
- **提交日期**: 2026-08-21 · **分类**: cs.CV, cs.MM
- **摘要摘录**: Micro-actions are subtle, short, low-amplitude body movements, such as a fidgeting hand or a slight head tilt, that humans perform with little conscious intent yet that reliably leak emotional and psychological state. Understanding them goes beyond assigning a label: a model must also describe which body parts move and reason, faithfully, about why a clip warrants a particular fine-grained category.

---

## Multi-camera Perception

### 1. M2Depth: Unifying Monocular Depth Foundation Priors with Multi-View Stereo

- **arXiv ID**: [2608.20788](https://arxiv.org/abs/2608.20788)  · [📄 PDF](https://arxiv.org/pdf/2608.20788)
- **作者**: Byeonggwon Lee, Sanggi Lee, Siwoo Lee et al. (5 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV
- **摘要摘录**: Deep learning-based Multi-View Stereo (MVS) has advanced significantly but often generalizes poorly to unseen scenes, particularly in occluded areas or regions with limited view overlap. To mitigate this, recent approaches integrate Depth Foundation Models (DFMs) into MVS pipelines to provide monocular depth priors.

### 2. Generating Multi-view Adversarial Examples for Visual Geometry Grounded Transformer

- **arXiv ID**: [2608.20748](https://arxiv.org/abs/2608.20748)  · [📄 PDF](https://arxiv.org/pdf/2608.20748)
- **作者**: Qi Song, Ziyuan Luo, Haoliang Han et al. (4 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV
- **摘要摘录**: The Visual Geometry Grounded Transformer (VGGT) enables unified feed-forward 3D reconstruction from multi-view images. However, deploying such a high-performance model may expose critical security vulnerabilities.

### 3. MV2GF: Multi-view Pedestrian Detection with a Visual Geometric Foundation Model

- **arXiv ID**: [2608.20639](https://arxiv.org/abs/2608.20639)  · [📄 PDF](https://arxiv.org/pdf/2608.20639)
- **作者**: Taiga Yamane, Satoshi Suzuki, Ryo Masumura et al. (7 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV
- **摘要摘录**: Multi-View Pedestrian Detection (MVPD) aims to detect pedestrians in the form of a bird's eye view map from multi-view images. Recent MVPD methods adopt a unified framework that projects 2D image features into a 3D world space and aggregates them into a single feature.

### 4. DiGS-Avatar: Single-Image Animatable 3D Human Reconstruction via UV-Space Diffusion

- **arXiv ID**: [2608.20759](https://arxiv.org/abs/2608.20759)  · [📄 PDF](https://arxiv.org/pdf/2608.20759)
- **作者**: Jiakun Li, Li Fang, Hao Zhu et al. (7 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV
- **摘要摘录**: Single-image 3D human reconstruction often suffers from over-smoothed textures and geometric inconsistencies. While diffusion models improve generative quality, their reliance on multi-view synthesis prior to 3D reconstruction is computationally expensive and prone to view inconsistency.

### 5. Identity-Aware Human-Object Interaction Motion Captioning

- **arXiv ID**: [2608.20690](https://arxiv.org/abs/2608.20690)  · [📄 PDF](https://arxiv.org/pdf/2608.20690)
- **作者**: Yiming Wang, Yonghao Dang, Huilai Li et al. (5 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV, cs.AI
- **摘要摘录**: Existing human-object interaction (HOI) motion captioning methods typically describe what happens while referring to the subject using generic terms such as "a person" or "someone", without grounding the caption in subject identity. To address this limitation, we introduce Identity-Aware Human-Object Interaction Motion Captioning task.

### 6. TopoSurfel: Closing the Loop between Gaussian Surfels and Meshes for Surface Reconstruction

- **arXiv ID**: [2608.20687](https://arxiv.org/abs/2608.20687)  · [📄 PDF](https://arxiv.org/pdf/2608.20687)
- **作者**: Chuanjin Fan, Wenjie Chang, Bohao Liao et al. (6 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV, cs.GR
- **摘要摘录**: 3D Gaussian Splatting has achieved remarkable success in novel view synthesis. However, extracting high-fidelity surfaces directly from 3DGS remains challenging due to its discrete and unstructured nature.

---

## Network Pruning

### 1. Just Noticeable Difference Modeling for Token Compression in Vision-Language-Action Models

- **arXiv ID**: [2608.21247](https://arxiv.org/abs/2608.21247)  · [📄 PDF](https://arxiv.org/pdf/2608.21247)
- **作者**: Zhuoyuan Li, Rui Zhao, Jin Wang et al. (8 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV, cs.RO
- **摘要摘录**: Token compression has become a key technique for reducing the inference cost of large foundation models, with approaches such as token pruning and KV-cache reuse widely adopted in vision-language models and recently explored for embodied agents. In embodied agents, tokens not only support perception and semantic understanding but also directly affect latency-sensitive closed-loop robot action prediction.

### 2. CubicSplat: Differentiable Vector Graphics via Error-Bounded Forward Relaxation

- **arXiv ID**: [2608.20803](https://arxiv.org/abs/2608.20803)  · [📄 PDF](https://arxiv.org/pdf/2608.20803)
- **作者**: Chenglong Liu, Xin Zhang, Yimeng Zhu et al. (8 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.GR, cs.CV, cs.LG
- **摘要摘录**: Vector graphics are prized for their resolution independence, compact storage, and direct editability, making differentiable optimization of their parametric primitives an attractive goal. Yet classical rasterization is discontinuous with respect to geometry, and existing remedies that smooth the forward pass demand increasingly elaborate heuristics as scene complexity grows.

### 3. Robust Validation to Geometric Perturbations for Autonomous Pose Estimation

- **arXiv ID**: [2608.21066](https://arxiv.org/abs/2608.21066)  · [📄 PDF](https://arxiv.org/pdf/2608.21066)
- **作者**: Gregoire Theau, Melanie Ducoffe
- **提交日期**: 2026-08-21 · **分类**: cs.CV
- **摘要摘录**: Deploying autonomous systems in safety-critical domains demands guaranteed robustness against physically plausible geometric perturbations rather than abstract pixel-wise noise. In vision-based navigation and autonomous landing, machine learning components require rigorous validation under dynamic operational conditions such as camera rotations and lighting shifts.

### 4. GAP-SAM: A Global Artifact Prior for Generalizable AI-Generated Image Manipulation Localization

- **arXiv ID**: [2608.20929](https://arxiv.org/abs/2608.20929)  · [📄 PDF](https://arxiv.org/pdf/2608.20929)
- **作者**: Haozhen Yan, Siyuan Shan, Zijian Yu et al. (7 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV
- **摘要摘录**: AI-generated image manipulation localization identifies edited pixels, but its OOD performance lags behind image-level detection partly because pixel supervision entangles forensic evidence with dataset-specific mask geometry and semantic boundaries. Extending image-level distribution alignment to localization, we construct COCO-ControlNet with source-image Canny edges and depth maps to align semantics and geometry, improving OOD performance across multiple localizers.

### 5. Aristotelian Manifolds: Leveraging Platonic Perceptual Features for Backpropagation Free Rapid Concept Learning

- **arXiv ID**: [2608.20682](https://arxiv.org/abs/2608.20682)  · [📄 PDF](https://arxiv.org/pdf/2608.20682)
- **作者**: Michael Karnes, Alper Yilmaz
- **提交日期**: 2026-08-21 · **分类**: cs.CV
- **摘要摘录**: This paper formalizes and systematically characterizes Aristotelian Manifolds, a generalized structural framework built upon the Platonic Representation Hypothesis. We position high-capacity foundation models as universal perceptual filters and conduct a comprehensive layer-wise investigation to map how knowledge is functionally synthesized within these latent subspaces.

---

## Video Understanding

### 1. Enhancing Localized Reasoning for Long Video Understanding via Efficient Segment-to-Video Supervision

- **arXiv ID**: [2608.20814](https://arxiv.org/abs/2608.20814)  · [📄 PDF](https://arxiv.org/pdf/2608.20814)
- **作者**: Beibei Zhang, Chao Xu, Jun Lan et al. (7 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV
- **摘要摘录**: Though Multimodal Large Language Models (MLLMs) have shown impressive potential in video understanding, long video understanding (LVU) remains challenging since distracting noise in complex and lengthy contexts can obscure localized details, misleading MLLMs to produce incorrect answers. Recent works mitigate these issues by incentivizing deep reasoning to include relevant evidence.

### 2. Routing Before Looking: Query-Adaptive Evidence Acquisition for Long-form Video Understanding

- **arXiv ID**: [2608.20805](https://arxiv.org/abs/2608.20805)  · [📄 PDF](https://arxiv.org/pdf/2608.20805)
- **作者**: Tianyue Wang, Xuying Wu, Yuxiang Ma et al. (10 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV
- **摘要摘录**: Long-form video understanding remains challenging for video agents due to the mismatch between query demands and evidence acquisition strategies. Although recent planning-before-perception methods outperform query-agnostic pipelines, they often rely on a single dominant strategy, either generation-based strategy or retrieval-based strategy, limiting their ability to handle diverse query demands.

### 3. OmniAssistBench: Assistant-style Interaction Benchmark for Omni-LLMs

- **arXiv ID**: [2608.21360](https://arxiv.org/abs/2608.21360)  · [📄 PDF](https://arxiv.org/pdf/2608.21360)
- **作者**: Xianyun Sun, Chaoyou Fu, Zhengye Zhang et al. (9 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV
- **摘要摘录**: Recent omni-modal large language models (Omni-LLMs) show great potential as real-time video assistants, which continuously perceive environments and guide users to achieve specific goals. Unlike traditional passive video understanding, interactive assistants should actively combine visual states, user goals, and prior knowledge to provide effective help.

---

## Vision Transformer

### 1. AT-ViT: Area-Targeted Multi-View Vision Transformer with Cross-Attention and Multi-Scale Patching for Plant Trait Recognition in Herbarium Images

- **arXiv ID**: [2608.21067](https://arxiv.org/abs/2608.21067)  · [📄 PDF](https://arxiv.org/pdf/2608.21067)
- **作者**: Amani Sedrat, Takieddine Chehhat, Youcef Sklab et al. (8 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV, cs.AI
- **摘要摘录**: Automated plant traits recognition from herbarium images is essential for plant sciences, yet remains challenging because background elements (e.g., textual labels, mounting artifacts, and color charts) can introduce shortcut learning, leading models to rely on spurious non-plant cues rather than plant morphology. This bias degrades both generalization and interpretability.

### 2. Privacy-Preserving Object Detection for Vision Transformer-Based Models

- **arXiv ID**: [2608.20712](https://arxiv.org/abs/2608.20712)  · [📄 PDF](https://arxiv.org/pdf/2608.20712)
- **作者**: Homare Sueyoshi, Kiyoshi Nishikawa, Hitoshi Kiya
- **提交日期**: 2026-08-21 · **分类**: cs.CR, cs.CV
- **摘要摘录**: We propose a novel object detection method that enables us to protect sensitive visual information of test images. Previous studies considering visual information protection focus on image classification tasks.

### 3. When does fusing hand-crafted knowledge with learned representations pay? A cost-normalized benchmark of stacking, substitution, and interference

- **arXiv ID**: [2608.21098](https://arxiv.org/abs/2608.21098)  · [📄 PDF](https://arxiv.org/pdf/2608.21098)
- **作者**: Ahmad AlMughrabi, Albert Clop, Benjamin Busam et al. (5 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV
- **摘要摘录**: Fusing prior knowledge with data-driven learning is attractive where data is scarce, yet no controlled account says when it helps, is redundant, or harms. We benchmark one fixed hand-crafted knowledge source, a pinned bank of Gabor targets injected only during training at $\sim$2\% overhead, against data-driven alternatives (SimCLR, SimSiam, DINO, ImageNet transfer, augmentation, learned teachers) under one frozen recipe with fixed subsets: 13 datasets, 9 backbones, 150 to 1.28M images, 32--224\

---

## Open Vocabulary Detection

### 1. Stream3Dv2: Geometric-Semantic Fusion Enhanced Streaming Zero-Shot 3D Scene Understanding

- **arXiv ID**: [2608.21136](https://arxiv.org/abs/2608.21136)  · [📄 PDF](https://arxiv.org/pdf/2608.21136)
- **作者**: Jie Xu, Na Zhao
- **提交日期**: 2026-08-21 · **分类**: cs.CV
- **摘要摘录**: Recently, open-vocabulary zero-shot 3D scene understanding using vision foundation models has emerged as a promising alternative to data-intensive supervised methods. However, deploying these models in real-world scenarios is severely hindered by their inability to efficiently handle streaming RGB-D inputs and their inherent vulnerability to noise 2D segmentation masks.

### 2. Lift, Associate, and Fuse: A Decision-Centric Framework for 2D-to-3D Foundation Model Transfer

- **arXiv ID**: [2608.20659](https://arxiv.org/abs/2608.20659)  · [📄 PDF](https://arxiv.org/pdf/2608.20659)
- **作者**: Wentao Sun, Yiping Chen, John S. Zelek et al. (4 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV
- **摘要摘录**: Methods that transfer predictions from two-dimensional foundation models into three-dimensional segmentation are commonly grouped by task or representation. Those groupings obscure the decisions that determine whether a system remains coherent across views: where image evidence is grounded, when observations become one identity, how semantic and granularity conflicts are handled, which information is fused, and what state survives for later queries.

---

## Knowledge Distillation

### 1. Semantically Compatible Knowledge Distillation for Cross-Domain Object Detection with Vision Foundation Models

- **arXiv ID**: [2608.20916](https://arxiv.org/abs/2608.20916)  · [📄 PDF](https://arxiv.org/pdf/2608.20916)
- **作者**: Qifeng Zhang, Ting Xiang, Zeyuan Bai et al. (4 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV
- **摘要摘录**: Vision foundation models (VFMs) offer strong generalization capabilities for domain-adaptive object detection (DAOD). However, existing VFM-based methods overlook the spatial-scale discrepancy between teacher and student feature maps, resulting in semantic incompatibility that weakens both feature alignment and pseudo-label learning.

---

## BEV

### 1. CoAnchor: Robust Collaborative Perception under Spatio-Temporal Misalignment via Object-Level Anchors

- **arXiv ID**: [2608.21055](https://arxiv.org/abs/2608.21055)  · [📄 PDF](https://arxiv.org/pdf/2608.21055)
- **作者**: Chi Li, Rui Lin, Aobo Ji et al. (4 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV, cs.AI
- **摘要摘录**: Collaborative perception extends the sensing range of a single vehicle by fusing observations from nearby agents, which improves the robustness of autonomous driving. In realistic deployments, however, the received collaborator messages are often affected by both communication delay and relative-pose noise, which jointly cause stale observations, spatial misalignment, and unstable feature fusion.

---

## Self-supervised Vision

### 1. Explainable Deepfake Detection with Feature-robust Augmentation and Evidence-grounded Explanation Optimization

- **arXiv ID**: [2608.20913](https://arxiv.org/abs/2608.20913)  · [📄 PDF](https://arxiv.org/pdf/2608.20913)
- **作者**: Zhu Xu, Jiaqi Tang, Pokai Chen et al. (5 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV, cs.AI
- **摘要摘录**: Explainable deepfake detection extends binary classification by requiring models to not only predict authenticity but also provide interpretable justifications. This expanded scope is critical in practice, where users like forensic analysts need insight into the rationale behind the detection.

---

## 📊 统计

| 领域 | 论文数 |
|------|--------|
| VLM | 8 |
| Multimodal | 8 |
| Multi-camera Perception | 6 |
| Network Pruning | 5 |
| Video Understanding | 3 |
| Vision Transformer | 3 |
| Open Vocabulary Detection | 2 |
| Knowledge Distillation | 1 |
| BEV | 1 |
| Self-supervised Vision | 1 |
| **总计** | **38** |