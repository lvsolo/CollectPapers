# VLM — 2025 Guideline

> 领域: 视觉语言模型（多模态大模型、CLIP 系、grounding）
> 论文数: 66 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Exploiting Vision Language Model for Training-Free 3D Point Cloud OOD Detection via Graph Score Propagation.
- **链接**: [arXiv:2506.22375](https://arxiv.org/abs/2506.22375) · 📚 被引 0
- **作者**: Tiankai Chen, Yushu Li, Adam Goodge, Fei Teng, Xulei Yang, Tianrui Li et al.
- **🏷️ 机构**: Southwest Jiaotong University, South China University of Technology, Institute for infocomm research(IR), A*STAR
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Out-of-distribution (OOD) detection in 3D point cloud data remains a challenge, particularly in applications where safe and robust perception is critical. While existing OOD detection methods have shown progress for 2D image data, extending these to 3D environments involves unique obstacles. This paper introduces a training-free framework that leverages Vision-Language Models (VLMs) for effective OOD detection in 3D point clouds. By constructing a graph based on class prototypes and testing data, we exploit the data manifold structure to enhancing the effectiveness of VLMs for 3D OOD detection. We propose a novel Graph Score Propagation (GSP) method that incorporates prompt clustering and self-training negative prompting to improve OOD scoring with VLM. Our method is also adaptable to few-shot scenarios, providing options for practical applications. We demonstrate that GSP consistently outperforms state-of-the-art methods across synthetic and real-world datasets 3D point cloud OOD detection.

</details>

### FE-CLIP: Frequency Enhanced CLIP Model for Zero-Shot Anomaly Detection and Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01971) · 📚 被引 5
- **作者**: Tao Gong, Qi Chu, Bin Liu, Wei Zhou, Nenghai Yu
- **🏷️ 机构**: School of Cyber Science and Technology, University of Science and Technology of China, Ling Yang Industrial Internet Co., Ltd.
- **会议**: ICCV 2025

### HOLa: Zero-Shot HOI Detection with Low-Rank Decomposed VLM Feature Adaptation.
- **链接**: [arXiv:2507.15542](https://arxiv.org/abs/2507.15542) · [代码](https://github.com/ChelsieLei/HOLa) · 📚 被引 3
- **作者**: Qinqian Lei, Bo Wang, Robby T. Tan
- **🏷️ 机构**: National University of Singapore, University of Mississippi
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Zero-shot human-object interaction (HOI) detection remains a challenging task, particularly in generalizing to unseen actions. Existing methods address this challenge by tapping Vision-Language Models (VLMs) to access knowledge beyond the training data. However, they either struggle to distinguish actions involving the same object or demonstrate limited generalization to unseen classes. In this paper, we introduce HOLa (Zero-Shot HOI Detection with Low-Rank Decomposed VLM Feature Adaptation), a novel approach that both enhances generalization to unseen classes and improves action distinction. In training, HOLa decomposes VLM text features for given HOI classes via low-rank factorization, producing class-shared basis features and adaptable weights. These features and weights form a compact HOI representation that preserves shared information across classes, enhancing generalization to unseen classes. Subsequently, we refine action distinction by adapting weights for each HOI class and introducing human-object tokens to enrich visual interaction representations. To further distinguish unseen actions, we guide the weight adaptation with LLM-derived action regularization. Experimental results show that our method sets a new state-of-the-art across zero-shot HOI settings on HICO-DET, achieving an unseen-class mAP of 27.91 in the unseen-verb setting. Our code is available at https://github.com/ChelsieLei/HOLa.

</details>

### Dynamic Multimodal Prototype Learning in Vision-Language Models.
- **链接**: [arXiv:2507.03657](https://arxiv.org/abs/2507.03657) · 📚 被引 0
- **作者**: Xingyu Zhu, Shuo Wang, Beier Zhu, Miaoge Li, Yunfan Li, Junfeng Fang et al.
- **🏷️ 机构**: University of Science and Technology of China, Nanyang Technological University, The Hong Kong Polytechnic University
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> With the increasing attention to pre-trained vision-language models (VLMs), \eg, CLIP, substantial efforts have been devoted to many downstream tasks, especially in test-time adaptation (TTA). However, previous works focus on learning prototypes only in the textual modality while overlooking the ambiguous semantics in class names. These ambiguities lead to textual prototypes that are insufficient to capture visual concepts, resulting in limited performance. To address this issue, we introduce \textbf{ProtoMM}, a training-free framework that constructs multimodal prototypes to adapt VLMs during the test time. By viewing the prototype as a discrete distribution over the textual descriptions and visual particles, ProtoMM has the ability to combine the multimodal features for comprehensive prototype learning. More importantly, the visual particles are dynamically updated as the testing stream flows. This allows our multimodal prototypes to continually learn from the data, enhancing their generalizability in unseen scenarios. In addition, we quantify the importance of the prototypes and test images by formulating their semantic distance as an optimal transport problem. Extensive experiments on 15 zero-shot benchmarks demonstrate the effectiveness of our method, achieving a 1.03\% average accuracy improvement over state-of-the-art methods on ImageNet and its variant datasets.

</details>

### MaTVLM: Hybrid Mamba-Transformer for Efficient Vision-Language Modeling.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01941) · 📚 被引 2
- **作者**: Yingyue Li, Bencheng Liao, Wenyu Liu, Xinggang Wang
- **🏷️ 机构**: School of EIC, Huazhong University of Science &#x0026; Technology, Institute of Artificial Intelligence, Huazhong University of Science &#x0026; Technology
- **会议**: ICCV 2025

### TAB: Transformer Attention Bottlenecks Enable User Intervention and Debugging in Vision-Language Models.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02094) · 📚 被引 0
- **作者**: Pooyan Rahmanzadehgervi, Hung Huy Nguyen, Rosanne Liu, Long Mai, Anh Totti Nguyen
- **🏷️ 机构**: Auburn University, Google DeepMind, ML Collective, Adobe Research
- **会议**: ICCV 2025

## 跨领域论文（完整笔记在其他领域）

- MISSRAG: Addressing the Missing Modality Challenge in Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- Bilateral Collaboration with Large Vision-Language Models for Open Vocabulary Human-Object Interaction Detection. → [open-set-detection](../open-set-detection/Guideline%202025.md)
- Plug-in Feedback Self-Adaptive Attention in CLIP for Training-Free Open-Vocabulary Segmentation. → [open-set-detection](../open-set-detection/Guideline%202025.md)
- 풟ℐℋ-CLIP: Unleashing the Diversity of Multi-Head Self-Attention for Training-Free Open-Vocabulary Semantic Segmentation. → [open-set-detection](../open-set-detection/Guideline%202025.md)
- CLIP-Adapted Region-to-Text Learning for Generative Open-Vocabulary Semantic Segmentation. → [open-set-detection](../open-set-detection/Guideline%202025.md)
- ROVI: A VLM-LLM Re-Captioned Dataset for Open-Vocabulary Instance-Grounded Text-to-Image Generation. → [open-set-detection](../open-set-detection/Guideline%202025.md)
- CLIPeR: Hierarchically Improving Spatial Representation of CLIP for Open-Vocabulary Semantic Segmentation. → [open-set-detection](../open-set-detection/Guideline%202025.md)
- CorrCLIP: Reconstructing Patch Correlations in CLIP for Open-Vocabulary Semantic Segmentation. → [open-set-detection](../open-set-detection/Guideline%202025.md)
- SimpleVQA: Multimodal Factuality Evaluation for Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- Heuristic-Induced Multimodal Risk Distribution Jailbreak Attack for Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- How Do Multimodal Large Language Models Handle Complex Multimodal Reasoning? Placing Them in an Extensible Escape Game. → [multimodal](../multimodal/Guideline%202025.md)
- Kestrel: 3D Multimodal LLM for Part-Aware Grounded Description. → [multimodal](../multimodal/Guideline%202025.md)
- What Changed? Detecting and Evaluating Instruction-Guided Image Edits with Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- TWIST & SCOUT: Grounding Multimodal LLM-Experts by Forget-Free Tuning. → [multimodal](../multimodal/Guideline%202025.md)
- LLaVA-KD: A Framework of Distilling Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- CompCap: Improving Multimodal Large Language Models with Composite Captions. → [multimodal](../multimodal/Guideline%202025.md)
- MM-Spatial: Exploring 3D Spatial Understanding in Multimodal LLMs. → [multimodal](../multimodal/Guideline%202025.md)
- Visual Chronicles: Using Multimodal LLMs to Analyze Massive Collections of Images. → [multimodal](../multimodal/Guideline%202025.md)
- V2PE: Improving Multimodal Long-Context Capability of Vision-Language Models with Variable Visual Position Encoding. → [multimodal](../multimodal/Guideline%202025.md)
- Multimodal LLM Guided Exploration and Active Mapping Using Fisher Information. → [multimodal](../multimodal/Guideline%202025.md)
- Corvid: Improving Multimodal Large Language Models Towards Chain-of-Thought Reasoning. → [multimodal](../multimodal/Guideline%202025.md)
- Analyzing Fine-Tuning Representation Shift for Multimodal LLMs Steering. → [multimodal](../multimodal/Guideline%202025.md)
- CapeLLM: Support-Free Category-Agnostic Pose Estimation with Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- Token Activation Map to Visually Explain Multimodal LLMs. → [multimodal](../multimodal/Guideline%202025.md)
- WSI-LLaVA: A Multimodal Large Language Model for Whole Slide Image. → [multimodal](../multimodal/Guideline%202025.md)
- Controlling Multimodal Llms Via Reward-Guided Decoding. → [multimodal](../multimodal/Guideline%202025.md)
- Enhancing Spatial Reasoning in Multimodal Large Language Models Through Reasoning-Based Segmentation. → [multimodal](../multimodal/Guideline%202025.md)
- Enrich and Detect: Video Temporal Grounding With Multimodal Llms. → [multimodal](../multimodal/Guideline%202025.md)
- Benchmarking Multimodal Large Language Models Against Image Corruptions. → [multimodal](../multimodal/Guideline%202025.md)
- LLaVA-Prumerge: Adaptive Token Reduction for Efficient Large Multimodal Models. → [multimodal](../multimodal/Guideline%202025.md)
- Autocompose: Automatic Generation of Pose Transition Descriptions for Composed Pose Retrieval Using Multimodal LLMs. → [multimodal](../multimodal/Guideline%202025.md)
- FedMVP: Federated Multimodal Visual Prompt Tuning for Vision-Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- Multimodal Large Language Model-Guided ISP Hyperparameter Optimization with Dynamic Preference Learning. → [multimodal](../multimodal/Guideline%202025.md)
- BASIC: Boosting Visual Alignment with Intrinsic Refined Embeddings in Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- SHIFT: Smoothing Hallucinations by Information Flow Tuning for Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- VisNumBench: Evaluating Number Sense of Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- Bootstrapping Grounded Chain-of-Thought in Multimodal Llms for Data-Efficient Model Adaptation. → [multimodal](../multimodal/Guideline%202025.md)
- Learning to Inference Adaptively for Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- DocThinker: Explainable Multimodal Large Language Models with Rule-Based Reinforcement Learning for Document Understanding. → [multimodal](../multimodal/Guideline%202025.md)
- ShortV: Efficient Multimodal Large Language Models by Freezing Visual Tokens in Ineffective Layers. → [multimodal](../multimodal/Guideline%202025.md)
- Visual-Oriented Fine-Grained Knowledge Editing for MultiModal Large Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- AVAM: A Universal Training-Free Adaptive Visual Anchoring Embedded into Multimodal Large Language Model for Multi-Image Question Answering. → [multimodal](../multimodal/Guideline%202025.md)
- R1-VL: Learning to Reason with Multimodal Large Language Models via Step-Wise Group Relative Policy Optimization. → [multimodal](../multimodal/Guideline%202025.md)
- FALCON: Resolving Visual Redundancy and Fragmentation in High-Resolution Multimodal Large Language Models via Visual Registers. → [multimodal](../multimodal/Guideline%202025.md)
- 2.5 Years in Class: A Multimodal Textbook for Vision-Language Pretraining. → [multimodal](../multimodal/Guideline%202025.md)
- Jailbreaking Multimodal Large Language Models via Shuffle Inconsistency. → [multimodal](../multimodal/Guideline%202025.md)
- Hints of Prompt: Enhancing Visual Representation for Multimodal LLMs in Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202025.md)
- Aigi-Holmes: Towards Explainable and Generalizable AI-Generated Image Detection via Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- LIRA: Reasoning Reconstruction via Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- Are They the Same? Exploring Visual Correspondence Shortcomings of Multimodal LLMs. → [multimodal](../multimodal/Guideline%202025.md)
- Multimodal LLMs as Customized Reward Models for Text-to-Image Generation. → [multimodal](../multimodal/Guideline%202025.md)
- FIX-CLIP: Dual-Branch Hierarchical Contrastive Learning via Synthetic Captions for Better Understanding of Long Text. → [self-supervised-vision](../self-supervised-vision/Guideline%202025.md)
- Open-Ended Hierarchical Streaming Video Understanding with Vision Language Models. → [video-understanding](../video-understanding/Guideline%202025.md)
- Feather the Throttle: Revisiting Visual Token Pruning for Vision-Language Model Acceleration. → [network-pruning](../network-pruning/Guideline%202025.md)
- Keyframe-Oriented Vision Token Pruning: Enhancing Efficiency of Large Vision Language Models on Long-form Video Processing. → [network-pruning](../network-pruning/Guideline%202025.md)
- METEOR: Multi-Encoder Collaborative Token Pruning for Efficient Vision Language Models. → [network-pruning](../network-pruning/Guideline%202025.md)
- When Large Vision-Language Model Meets Large Remote Sensing Imagery: Coarse-to-Fine Text-Guided Token Pruning. → [network-pruning](../network-pruning/Guideline%202025.md)
- Pruning All-Rounder: Rethinking and Improving Inference Efficiency for Large Vision Language Models. → [network-pruning](../network-pruning/Guideline%202025.md)
- ZipVL: Accelerating Vision-Language Models Through Dynamic Token Sparsity. → [network-pruning](../network-pruning/Guideline%202025.md)
- SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference. → [network-pruning](../network-pruning/Guideline%202025.md)
