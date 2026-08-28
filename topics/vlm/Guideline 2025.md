# VLM — 2025 Guideline

> 领域: 视觉语言模型（多模态大模型、CLIP 系、grounding）
> 论文数: 60 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Generalized Few-shot 3D Point Cloud Segmentation with Vision-Language Model.
- **链接**: [arXiv:2503.16282](https://arxiv.org/abs/2503.16282) · [代码](https://github.com/ZhaochongAn/GFS-VL)
- **作者**: Zhaochong An, Guolei Sun, Yun Liu, Runjia Li, Junlin Han, Ender Konukoglu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Generalized few-shot 3D point cloud segmentation (GFS-PCS) adapts models to new classes with few support samples while retaining base class segmentation. Existing GFS-PCS methods enhance prototypes via interacting with support or query features but remain limited by sparse knowledge from few-shot samples. Meanwhile, 3D vision-language models (3D VLMs), generalizing across open-world novel classes, contain rich but noisy novel class knowledge. In this work, we introduce a GFS-PCS framework that synergizes dense but noisy pseudo-labels from 3D VLMs with precise yet sparse few-shot samples to maximize the strengths of both, named GFS-VL. Specifically, we present a prototype-guided pseudo-label selection to filter low-quality regions, followed by an adaptive infilling strategy that combines knowledge from pseudo-label contexts and few-shot samples to adaptively label the filtered, unlabeled areas. Additionally, we design a novel-base mix strategy to embed few-shot samples into training scenes, preserving essential context for improved novel class learning. Moreover, recognizing the limited diversity in current GFS-PCS benchmarks, we introduce two challenging benchmarks with diverse novel classes for comprehensive generalization evaluation. Experiments validate the effectiveness of our framework across models and datasets. Our approach and benchmarks provide a solid foundation for advancing GFS-PCS in the real world. The code is at https://github.com/ZhaochongAn/GFS-VL

</details>

### ProxyTransformation: Preshaping Point Cloud Manifold With Proxy Attention For 3D Visual Grounding.
- **链接**: [arXiv:2502.19247](https://arxiv.org/abs/2502.19247) · 📚 被引 0
- **作者**: Qihang Peng, Henry Zheng, Gao Huang
- **🏷️ 机构**: Tsinghua University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Embodied intelligence requires agents to interact with 3D environments in real time based on language instructions. A foundational task in this domain is ego-centric 3D visual grounding. However, the point clouds rendered from RGB-D images retain a large amount of redundant background data and inherent noise, both of which can interfere with the manifold structure of the target regions. Existing point cloud enhancement methods often require a tedious process to improve the manifold, which is not suitable for real-time tasks. We propose Proxy Transformation suitable for multimodal task to efficiently improve the point cloud manifold. Our method first leverages Deformable Point Clustering to identify the point cloud sub-manifolds in target regions. Then, we propose a Proxy Attention module that utilizes multimodal proxies to guide point cloud transformation. Built upon Proxy Attention, we design a submanifold transformation generation module where textual information globally guides translation vectors for different submanifolds, optimizing relative spatial relationships of target regions. Simultaneously, image information guides linear transformations within each submanifold, refining the local point cloud manifold of target regions. Extensive experiments demonstrate that Proxy Transformation significantly outperforms all existing methods, achieving an impressive improvement of 7.49% on easy targets and 4.60% on hard targets, while reducing the computational overhead of attention blocks by 40.6%. These results establish a new SOTA in ego-centric 3D visual grounding, showcasing the effectiveness and robustness of our approach.

</details>

### UPME: An Unsupervised Peer Review Framework for Multimodal Large Language Model Evaluation.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_UPME_An_Unsupervised_Peer_Review_Framework_for_Multimodal_Large_Language_CVPR_2025_paper.html) · 📚 被引 2
- **作者**: Qihui Zhang, Munan Ning, Zheyuan Liu, Yue Huang, Shuo Yang, Yanbo Wang et al.
- **🏷️ 机构**: Peking University,School of Electrical and Computer Engineering, University of Notre Dame, Tsinghua University
- **会议**: CVPR 2025

### Debiasing Multimodal Large Language Models via Noise-Aware Preference Optimization.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_Debiasing_Multimodal_Large_Language_Models_via_Noise-Aware_Preference_Optimization_CVPR_2025_paper.html) · 📚 被引 8
- **作者**: Zefeng Zhang, Hengzhu Tang, Jiawei Sheng, Zhenyu Zhang, Yiming Ren, Zhenyang Li et al.
- **🏷️ 机构**: Chinese Academy of Sciences,Institute of Information Engineering, Baidu Inc.
- **会议**: CVPR 2025

### Accelerating Multimodal Large Language Models by Searching Optimal Vision Token Reduction.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhao_Accelerating_Multimodal_Large_Language_Models_by_Searching_Optimal_Vision_Token_CVPR_2025_paper.html) · 📚 被引 4
- **作者**: Shiyu Zhao, Zhenting Wang, Felix Juefei-Xu, Xide Xia, Miao Liu, Xiaofang Wang et al.
- **🏷️ 机构**: Rutgers University, Meta
- **会议**: CVPR 2025

### SynTab-LLaVA: Enhancing Multimodal Table Understanding with Decoupled Synthesis.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhou_SynTab-LLaVA_Enhancing_Multimodal_Table_Understanding_with_Decoupled_Synthesis_CVPR_2025_paper.html) · 📚 被引 3
- **作者**: Bangbang Zhou, Zuan Gao, Zixiao Wang, Boqiang Zhang, Yuxin Wang, Zhineng Chen et al.
- **🏷️ 机构**: University of Science and Technology of China, Fudan Univeristy
- **会议**: CVPR 2025

### MotionBench: Benchmarking and Improving Fine-grained Video Motion Understanding for Vision Language Models.
- **链接**: [arXiv:2501.02955](https://arxiv.org/abs/2501.02955) · 📚 被引 9
- **作者**: Wenyi Hong, Yean Cheng, Zhuoyi Yang, Weihan Wang, Lefan Wang, Xiaotao Gu et al.
- **🏷️ 机构**: Tsinghua University, Zhipu AI
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In recent years, vision language models (VLMs) have made significant advancements in video understanding. However, a crucial capability - fine-grained motion comprehension - remains under-explored in current benchmarks. To address this gap, we propose MotionBench, a comprehensive evaluation benchmark designed to assess the fine-grained motion comprehension of video understanding models. MotionBench evaluates models' motion-level perception through six primary categories of motion-oriented question types and includes data collected from diverse sources, ensuring a broad representation of real-world video content. Experimental results reveal that existing VLMs perform poorly in understanding fine-grained motions. To enhance VLM's ability to perceive fine-grained motion within a limited sequence length of LLM, we conduct extensive experiments reviewing VLM architectures optimized for video feature compression and propose a novel and efficient Through-Encoder (TE) Fusion method. Experiments show that higher frame rate inputs and TE Fusion yield improvements in motion understanding, yet there is still substantial room for enhancement. Our benchmark aims to guide and motivate the development of more capable video understanding models, emphasizing the importance of fine-grained motion comprehension. Project page: https://motion-bench.github.io .

</details>

### Retaining Knowledge and Enhancing Long-Text Representations in CLIP through Dual-Teacher Distillation.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Feng_Retaining_Knowledge_and_Enhancing_Long-Text_Representations_in_CLIP_through_Dual-Teacher_CVPR_2025_paper.html) · 📚 被引 2
- **作者**: Yuheng Feng, Changsong Wen, Zelin Peng, Li jiaye, Siyu Zhu
- **🏷️ 机构**: Fudan University, Shanghai Jiao Tong University
- **会议**: CVPR 2025

### VL2Lite: Task-Specific Knowledge Distillation from Large Vision-Language Models to Lightweight Networks.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Jang_VL2Lite_Task-Specific_Knowledge_Distillation_from_Large_Vision-Language_Models_to_Lightweight_CVPR_2025_paper.html) · 📚 被引 11
- **作者**: Jinseong Jang, Chunfei Ma, Byeongwon Lee
- **🏷️ 机构**: Vision Lab, AI R&amp;D Center, SK Telecom
- **会议**: CVPR 2025

### Classifier-guided CLIP Distillation for Unsupervised Multi-label Classification.
- **链接**: [arXiv:2503.16873](https://arxiv.org/abs/2503.16873) · [代码](https://github.com/k0u-id/CCD) · 📚 被引 3
- **作者**: Dongseob Kim, Hyunjung Shim
- **🏷️ 机构**: Samsung Electronics,Republic of Korea, KAIST,Republic of Korea
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-label classification is crucial for comprehensive image understanding, yet acquiring accurate annotations is challenging and costly. To address this, a recent study suggests exploiting unsupervised multi-label classification leveraging CLIP, a powerful vision-language model. Despite CLIP's proficiency, it suffers from view-dependent predictions and inherent bias, limiting its effectiveness. We propose a novel method that addresses these issues by leveraging multiple views near target objects, guided by Class Activation Mapping (CAM) of the classifier, and debiasing pseudo-labels derived from CLIP predictions. Our Classifier-guided CLIP Distillation (CCD) enables selecting multiple local views without extra labels and debiasing predictions to enhance classification performance. Experimental results validate our method's superiority over existing techniques across diverse datasets. The code is available at https://github.com/k0u-id/CCD.

</details>

## 跨领域论文（完整笔记在其他领域）

- ROD-MLLM: Towards More Reliable Object Detection in Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- MIMO: A Medical Vision Language Model with Visual Referring Multimodal Input and Pixel Grounding Multimodal Output. → [multimodal](../multimodal/Guideline%202025.md)
- Bridging Modalities: Improving Universal Multimodal Retrieval by Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- LoRASculpt: Sculpting LoRA for Harmonizing General and Specialized Knowledge in Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- 4D LangSplat: 4D Language Gaussian Splatting via Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- RAP: Retrieval-Augmented Personalization for Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- S4-Driver: Scalable Self-Supervised Driving Multimodal Large Language Model with Spatio-Temporal Visual Representation. → [multimodal](../multimodal/Guideline%202025.md)
- XLRS-Bench: Could Your Multimodal LLMs Understand Extremely Large Ultra-High-Resolution Remote Sensing Imagery? → [multimodal](../multimodal/Guideline%202025.md)
- Cross-modal Information Flow in Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- CoMM: A Coherent Interleaved Image-Text Dataset for Multimodal Understanding and Generation. → [multimodal](../multimodal/Guideline%202025.md)
- Augmenting Multimodal LLMs with Self-Reflective Tokens for Knowledge-based Visual Question Answering. → [multimodal](../multimodal/Guideline%202025.md)
- Insight-V: Exploring Long-Chain Visual Reasoning with Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- AdaMMS: Model Merging for Heterogeneous Multimodal Large Language Models with Unsupervised Coefficient Optimization. → [multimodal](../multimodal/Guideline%202025.md)
- GroundingFace: Fine-grained Face Understanding via Pixel Grounding Multimodal Large Language Model. → [multimodal](../multimodal/Guideline%202025.md)
- CL-MoE: Enhancing Multimodal Large Language Model with Dual Momentum Mixture-of-Experts for Continual Visual Question Answering. → [multimodal](../multimodal/Guideline%202025.md)
- Playing the Fool: Jailbreaking LLMs and Multimodal LLMs with Out-of-Distribution Strategy. → [multimodal](../multimodal/Guideline%202025.md)
- Img-Diff: Contrastive Data Synthesis for Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- Is 'Right' Right? Enhancing Object Orientation Understanding in Multimodal Large Language Models through Egocentric Instruction Tuning. → [multimodal](../multimodal/Guideline%202025.md)
- LLaVA-ST: A Multimodal Large Language Model for Fine-Grained Spatial-Temporal Understanding. → [multimodal](../multimodal/Guideline%202025.md)
- VidHalluc: Evaluating Temporal Hallucinations in Multimodal Large Language Models for Video Understanding. → [multimodal](../multimodal/Guideline%202025.md)
- COUNTS: Benchmarking Object Detectors and Multimodal Large Language Models under Distribution Shifts. → [multimodal](../multimodal/Guideline%202025.md)
- Multi-Layer Visual Feature Fusion in Multimodal LLMs: Methods, Analysis, and Best Practices. → [multimodal](../multimodal/Guideline%202025.md)
- EventGPT: Event Stream Understanding with Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- BlueLM-V-3B: Algorithm and System Co-Design for Multimodal Large Language Models on Mobile Devices. → [multimodal](../multimodal/Guideline%202025.md)
- Mono-InternVL: Pushing the Boundaries of Monolithic Multimodal Large Language Models with Endogenous Visual Pre-training. → [multimodal](../multimodal/Guideline%202025.md)
- VideoGLaMM : A Large Multimodal Model for Pixel-Level Visual Grounding in Videos. → [multimodal](../multimodal/Guideline%202025.md)
- The Photographer's Eye: Teaching Multimodal Large Language Models to See, and Critique Like Photographers. → [multimodal](../multimodal/Guideline%202025.md)
- From Multimodal LLMs to Generalist Embodied Agents: Methods and Lessons. → [multimodal](../multimodal/Guideline%202025.md)
- FlashSloth : Lightning Multimodal Large Language Models via Embedded Visual Compression. → [multimodal](../multimodal/Guideline%202025.md)
- ODE: Open-Set Evaluation of Hallucinations in Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- LLaVA-Critic: Learning to Evaluate Multimodal Models. → [multimodal](../multimodal/Guideline%202025.md)
- Towards Zero-Shot Anomaly Detection and Reasoning with Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- Task Preference Optimization: Improving Multimodal Large Language Models with Vision Task Alignment. → [multimodal](../multimodal/Guideline%202025.md)
- Distraction is All You Need for Multimodal Large Language Model Jailbreaking. → [multimodal](../multimodal/Guideline%202025.md)
- TopV: Compatible Token Pruning with Inference Time Optimization for Fast and Low-Memory Multimodal Vision Language Model. → [multimodal](../multimodal/Guideline%202025.md)
- Thinking in Space: How Multimodal Large Language Models See, Remember, and Recall Spaces. → [multimodal](../multimodal/Guideline%202025.md)
- ClearSight: Visual Signal Enhancement for Object Hallucination Mitigation in Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- SeqAfford: Sequential 3D Affordance Reasoning via Multimodal Large Language Model. → [multimodal](../multimodal/Guideline%202025.md)
- Weakly Supervised Temporal Action Localization via Dual-Prior Collaborative Learning Guided by Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- Critic-V: VLM Critics Help Catch VLM Errors in Multimodal Reasoning. → [multimodal](../multimodal/Guideline%202025.md)
- Period-LLM: Extending the Periodic Capability of Multimodal Large Language Model. → [multimodal](../multimodal/Guideline%202025.md)
- Stealthy Backdoor Attack in Self-Supervised Learning Vision Encoders for Large Vision Language Models. → [self-supervised-vision](../self-supervised-vision/Guideline%202025.md)
- ImagineFSL: Self-Supervised Pretraining Matters on Imagined Base Set for VLM-based Few-shot Learning. → [self-supervised-vision](../self-supervised-vision/Guideline%202025.md)
- Anyattack: Towards Large-scale Self-supervised Adversarial Attacks on Vision-language Models. → [self-supervised-vision](../self-supervised-vision/Guideline%202025.md)
- Video-XL: Extra-Long Vision Language Model for Hour-Scale Video Understanding. → [video-understanding](../video-understanding/Guideline%202025.md)
- BOLT: Boost Large Vision-Language Model Without Training for Long-form Video Understanding. → [video-understanding](../video-understanding/Guideline%202025.md)
- Text-guided Sparse Voxel Pruning for Efficient 3D Visual Grounding. → [3d-detection](../3d-detection/Guideline%202025.md)
- EfficientLLaVA: Generalizable Auto-Pruning for Large Vision-language Models. → [network-pruning](../network-pruning/Guideline%202025.md)
- Libra-Merging: Importance-redundancy and Pruning-merging Trade-off for Acceleration Plug-in in Large Vision-Language Model. → [network-pruning](../network-pruning/Guideline%202025.md)
- ATP-LLaVA: Adaptive Token Pruning for Large Vision Language Models. → [network-pruning](../network-pruning/Guideline%202025.md)
