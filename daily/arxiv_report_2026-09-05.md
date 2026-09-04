# 📚 arXiv 每日论文报告（我的领域）

**报告日期**: 2026-09-05  
**论文来源**: [arXiv cs.CV Recent](https://arxiv.org/list/cs.CV/recent)  
**关注论文数**: 45 篇（其中 45 篇经大模型中文评估）

> 匹配领域: Object Detection、Autonomous Driving、3D Detection、BEV、Occupancy、Multi-camera Perception、Tracking、Open-set Detection、FOD Detection、VLM、Vision Transformer、Self-supervised Vision、Video Understanding、Multimodal、Continual Learning、Neural Architecture Search、Network Pruning、Knowledge Distillation

## 📑 目录

- [VLM](#vlm) (10篇)
- [Network Pruning](#network-pruning) (6篇)
- [Multimodal](#multimodal) (6篇)
- [Multi-camera Perception](#multi-camera-perception) (5篇)
- [Autonomous Driving](#autonomous-driving) (4篇)
- [Video Understanding](#video-understanding) (4篇)
- [Object Detection](#object-detection) (3篇)
- [Open-set Detection](#open-set-detection) (2篇)
- [Vision Transformer](#vision-transformer) (1篇)
- [Self-supervised Vision](#self-supervised-vision) (1篇)
- [Knowledge Distillation](#knowledge-distillation) (1篇)
- [Continual Learning](#continual-learning) (1篇)
- [Tracking](#tracking) (1篇)

## VLM

### 1. SafeRI: Recognition and Intervention for Token-Level Safety Intervention in Large Vision Language Models **⭐⭐⭐** (相关度: 40%, 质量: 0.7)

- **arXiv ID**: [2609.03544](https://arxiv.org/abs/2609.03544)  · [📄 PDF](https://arxiv.org/pdf/2609.03544)
- **作者**: Caoyuan Ma, Tian Gu, Wenpu Liu et al. (14 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-03 · **分类**: cs.CV
- **摘要（中）**: 针对视觉语言模型（VLM）现有安全对齐方法全局修改模型行为、干扰正常生成并损害通用多模态能力的问题，提出SafeRI框架，实现按需的安全干预。该方法在自回归生成过程中，通过轻量级识别器实时估计当前token生成状态的安全性，并据此动态控制LoRA模块的激活门控；LoRA模块在检测到不安全前缀时被激活，将生成重定向至安全响应，而安全生成则保持冻结主干策略。相比传统全局安全对齐，SafeRI仅在需要时介入，减少对原始推理路径的扰动。实验表明，该方法在多个安全与通用基准上均有效，适用于后对齐场景。
- **摘要（英）**: This paper addresses the issue that existing safety alignment methods for vision-language models globally modify behavior, perturbing normal generation and degrading general capabilities. It proposes SafeRI, a streaming recognition and gated LoRA framework that dynamically activates safety intervention only when unsafe token states are detected, preserving the frozen backbone otherwise. Experiments across safety and general benchmarks demonstrate effectiveness in post-alignment settings.
- **评估**: 该论文提出按需安全干预的新思路，对VLM安全对齐研究具有启发意义，但与本领域（自动驾驶感知）直接相关性较低。
- **核心贡献**: 提出流式识别与门控LoRA框架，实现VLM安全对齐的按需干预。
- **创新点**: 将安全对齐从全局永久修改转变为基于token级识别的动态门控机制。
- **结果**: 在多个安全与通用基准上验证了方法的有效性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing safety alignment methods for vision-language models usually modify the model behavior globally: once the safety parameters are trained or loaded, they participate in both unsafe and already-safe generations. This always-on intervention can unnecessarily perturb the model's original reasoning path and degrade general multimodal capabilities. We argue that safety alignment should be an on-demand intervention rather than a permanent modification to every decoding trajectory. To this end, we propose a streaming recognition and gated LoRA framework for intrinsic VLM safety. During autoregressive generation, a lightweight recognizer estimates whether the current pre-token generation state is safe or unsafe. Its output updates the LoRA gate for the following decoding step; otherwise, generation follows the frozen-backbone policy. The LoRA module is trained from unsafe prefixes, transition statements, and safe continuations, so that it learns to redirect unsafe generations back to safe responses after activation. Experiments across multiple safety and general-purpose benchmarks demonstrate the effectiveness of our method in post-alignment settings.

</details>

### 2. Solving the Needle-in-a-Haystack Problem in Mammography Vision-Language Model with Differentiable Subset Sampling **⭐⭐⭐** (相关度: 35%, 质量: 0.7)

- **arXiv ID**: [2609.03085](https://arxiv.org/abs/2609.03085)  · [📄 PDF](https://arxiv.org/pdf/2609.03085)
- **作者**: Young Seok Jeon, Beatrice Brown-Mulry, Rohan Satya Isaac et al. (8 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/Youngseok0001/TopKSigLIP](https://github.com/Youngseok0001/TopKSigLIP)
- **提交日期**: 2026-09-02 · **分类**: cs.CV
- **摘要（中）**: 针对乳腺X光摄影中CLIP风格VLM预训练性能受限的问题，指出高分辨率图像和放射报告同质性是主要原因。提出TopKSigLIP，一种通过TopK-Patch模块学习采样稀疏高分辨率补丁以定位病灶的VLM，避免下采样带来的信息损失，并解决分辨率与批大小的权衡。同时，用Sup-sigmoid损失替代对比损失，以处理报告同质性导致的语义相似对误排斥。该方法在癌症、发现类型和BI-RADS预测等临床任务中提升了零样本性能，并内置定位能力。
- **摘要（英）**: This paper addresses the limited zero-shot performance of CLIP-style VLMs in mammography due to high-resolution images and report homogeneity. It proposes TopKSigLIP, which introduces a TopK-Patch module to sample sparse high-res patches likely containing lesions, and replaces contrastive loss with Sup-sigmoid loss to handle semantically similar pairs. The method improves performance in cancer, finding-type, and BI-RADS predictions with built-in localization.
- **评估**: 该论文针对医学影像VLM的特定问题提出解决方案，方法有创新性，但与本领域（自动驾驶感知）相关性较低。
- **核心贡献**: 提出TopKSigLIP，解决高分辨率与报告同质性对乳腺VLM预训练的限制。
- **创新点**: 引入TopK-Patch模块和Sup-sigmoid损失，兼顾高分辨率采样与语义相似性处理。
- **结果**: 在临床任务中提升零样本性能并提供定位能力。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> There is growing interest in adopting CLIP-style vision--language model (VLM) pretraining for mammography. However, models that directly employ the standard CLIP architecture and training objective exhibit limited zero-shot performance in clinically important tasks such as cancer, finding-type, and BI-RADS predictions. We argue that this underwhelming performance is due to neglecting two characteristics of mammography data: (1) its high-res nature, and (2) homogeneity of radiology reports, largely driven by a predominance of negative/benign findings on examinations. We propose TopKSigLIP, a VLM designed to address these two limitations through a novel architecture and learning objectives. Instead of downscaling high-res mammography images to satisfy GPU memory constraints, TopKSigLIP introduces TopK-Patch module that learns to sample a sparse set of high-res patches likely to contain lesions, sidestepping the resolution--batch size tradeoff of VLM training. The sampled patch locations additionally serve as a built-in localization tool. To address report homogeneity, we replace the contrastive loss, which falsely repels semantically similar pairs, with a Sup-sigmoid loss. Sup-sigmoid loss extends the sigmoid loss from SigLIP with soft labels derived from structured data. TopKSigLIP outperforms existing open-source mammography and general medical VLMs on both internal and external benchmarks on density assessment, BI-RADS classification, finding subtyping, and cancer prediction under zero-shot evaluation. TopKSigLIP remains competitive under linear probing despite using a significantly smaller vision encoder and smaller training batches than baselines. The TopK-Patch module additionally achieves superior lesion localization over post-hoc Grad-CAM. Code and weights are made public:https://github.com/Youngseok0001/TopKSigLIP.

</details>

### 3. Seeing Before Synthesizing: VLM-Guided Transition Event Discovery for Weakly-Supervised Dense Video Captioning **⭐⭐⭐** (相关度: 40%, 质量: 0.7)

- **arXiv ID**: [2609.04183](https://arxiv.org/abs/2609.04183)  · [📄 PDF](https://arxiv.org/pdf/2609.04183)
- **作者**: Ye-Chan Kim, Seunghee Choi, SeungJu Cha et al. (7 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-03 · **分类**: cs.CV, cs.AI
- **摘要（中）**: 针对弱监督密集视频描述中合成过渡字幕缺乏视觉基础且位置时长固定分配的问题，提出Seeing Before Synthesizing (SBS)框架。该方法利用VLM生成帧级叙述并检测语义变化点，进而优化事件间时间掩码。相比已有工作，SBS仅在需要处提供视觉基础的语言引导，并在ActivityNet Captions和YouCook2上取得最优性能。
- **摘要（英）**: Addressing the issue of synthetic transition captions lacking visual grounding and rigid temporal assignment in weakly-supervised dense video captioning, this paper proposes the SBS framework. It uses a VLM to generate frame-level narratives, detect semantic transitions, and refine temporal masks, achieving state-of-the-art results on ActivityNet Captions and YouCook2.
- **评估**: 该工作对视频描述中的时间定位与语言引导结合有启发，但与自动驾驶感知核心方向关联较弱。
- **核心贡献**: 提出视觉基础引导的过渡事件发现框架，提升弱监督密集视频描述性能。
- **创新点**: 利用VLM语义变化检测替代固定位置的字幕合成。
- **结果**: 在ActivityNet Captions和YouCook2上达到最优性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Weakly-Supervised Dense Video Captioning aims to localize and describe multiple events in untrimmed videos given only an ordered set of event-level captions per video. Recent work synthesizes auxiliary transition captions via LLM to provide additional vision-language alignment, but these captions lack visual grounding and are rigidly assigned to every inter-event gap at a fixed location and duration. To address these, we propose Seeing Before Synthesizing (SBS), a framework that adaptively provides visually grounded linguistic guidance only where warranted. Leveraging a VLM, we generate frame-level narratives for the inter-event gaps and detect transitions from the semantic variation across them. For identified transitions, we then refine inter-event temporal masks by blending the temporal midpoint with the semantic change point and selecting the width that maximizes vision-language alignment. Experiments on ActivityNet Captions and YouCook2 demonstrate state-of-the-art performance in both captioning and localization.

</details>

### 4. LookStep: Efficient Vision-Language Navigation with Linguistic Foresight and Event Driven Memory **⭐⭐⭐** (相关度: 55%, 质量: 0.75)

- **arXiv ID**: [2609.02350](https://arxiv.org/abs/2609.02350)  · [📄 PDF](https://arxiv.org/pdf/2609.02350)
- **作者**: Kun-Yang Yu, Yingzhe Li, Hongyu Xu et al. (11 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/kunyang-YU/LookStep](https://github.com/kunyang-YU/LookStep)
- **提交日期**: 2026-09-02 · **分类**: cs.CV, cs.RO
- **摘要（中）**: 针对视觉语言导航中现有方法依赖大量数据和高计算内存开销的问题，提出LookStep框架，结合语言中心未来状态建模和事件驱动滚动记忆。该方法用语言标签生成候选动作的粗粒度导航进度和未来状态，并自主决定是否将观察写入有界滚动记忆。在VLN-CE任务上，LookStep在相同训练设置下优于现有方法，R2R-CE Val-Unseen成功率49.7%，且内存效率更高、数据使用更少。
- **摘要（英）**: To address high data and computational costs in vision-language navigation, this paper proposes LookStep, combining language-centric future state modeling and event-driven rolling memory. It achieves a 49.7% success rate on R2R-CE Val-Unseen with better memory efficiency and less data usage.
- **评估**: 该工作对多模态智能体导航有贡献，但应用场景与自动驾驶感知有距离。
- **核心贡献**: 提出高效端到端VLN框架，降低数据与内存需求。
- **创新点**: 语言标签驱动的未来状态建模与事件驱动记忆机制。
- **结果**: 在VLN-CE任务上以更少数据实现49.7%成功率。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-Language Navigation (VLN) requires an embodied agent to follow natural-language instructions in unseen environments. Recent progress has been largely driven by Multimodal Large Language Models (MLLMs). Existing methods follow a next-step action prediction paradigm, supervising only the expert action, which requires a high quantity of data for training. They also rely on cognitive maps, accumulated historical frames, or external 3D tools to maintain states, leading to high computational and memory overhead. To realize resource efficiency VLN, we propose LookStep, a unified end-to-end framework that combines Language Centric Future State Modeling and Event Driven Rolling Memory that uses language labels to generate coarse-grained navigation progress and future states for each candidate action, while autonomously deciding whether to write each observation into a bounded rolling memory with a semantic role. We validate LookStep empirically. On VLN-CE tasks, LookStep outperforms existing methods under the same training settings, achieving a 49.7\% success rate on R2R-CE Val-Unseen with better memory efficiency and less data usage. Code and model is available at https://github.com/kunyang-YU/LookStep.

</details>

### 5. SVG-Score: Human-Aligned Evaluation of Text-to-SVG Generation **⭐⭐** (相关度: 15%, 质量: 0.65)

- **arXiv ID**: [2609.03806](https://arxiv.org/abs/2609.03806)  · [📄 PDF](https://arxiv.org/pdf/2609.03806)
- **作者**: Marco Cipriano, Leonardo Zini, Alexandra Schild et al. (8 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-03 · **分类**: cs.AI, cs.CV
- **摘要（中）**: 针对文本到SVG生成缺乏领域专用评估协议的问题，提出SVG-Score评估框架。通过受控扰动实验证明CLIPScore对SVG生成错误不敏感，并引入人类标注数据集和两种评估器。该方法旨在提供与人类判断对齐的评估，但应用领域与自动驾驶感知无关。
- **摘要（英）**: Addressing the lack of evaluation protocols for text-to-SVG generation, this paper introduces SVG-Score, a human-aligned framework with adapted CLIP scorers and a fine-tuned VLM judge.
- **评估**: 该工作聚焦于SVG生成评估，与自动驾驶感知领域不相关。
- **核心贡献**: 提出首个面向文本到SVG生成的人类对齐评估框架。
- **创新点**: 结合CLIP适配与VLM微调实现领域专用评估。
- **结果**: 提供更符合人类判断的SVG生成评估方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Scalable Vector Graphics (SVG) generation is attracting increasing attention as generative models improve in expressiveness and controllability. Progress, however, is held back by the lack of domain-specific evaluation protocols: current practice relies on metrics designed for natural images, most notably CLIPScore, which was never trained on vector graphics and aligns only partially with human judgment. We introduce \textbf{\ours}, a human-aligned evaluation framework for text-to-SVG generation. Through controlled caption and image perturbations, we first show that CLIP-based scores barely react to the errors SVG generators actually make, such as wrong colors, counts, and spatial relations, and that off-the-shelf Vision-Language Model (VLM) judges, while more sensitive, respond unevenly across error types and SVG styles. We then introduce a human-annotated dataset for \textit{Semantic Alignment}, measuring how faithfully a generated SVG reflects its caption. Building on it, we develop two complementary evaluators: CLIP scorers adapted to vector graphics and then aligned to human preferences, for fast large-scale evaluation, and a VLM judge trained with supervised fine-tuning and reward-shaped reinforcement learning, for more expressive and interpretable assessment. Using both, we benchmark major open-source, commercial, and optimization-based SVG generators on an independent caption set.

</details>

### 6. Unfold The World: Factorize 4D Properties in Reinforcing Spatial Reasoning **⭐⭐⭐⭐** (相关度: 70%, 质量: 0.8)

- **arXiv ID**: [2609.03729](https://arxiv.org/abs/2609.03729)  · [📄 PDF](https://arxiv.org/pdf/2609.03729)
- **作者**: Yijun Yang, Shenghe Zheng, Wenbo Li et al. (11 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-03 · **分类**: cs.CV
- **摘要（中）**: 针对视觉语言模型在物理世界空间推理上的不足，提出FactoSR因子化强化学习框架。该方法将世界一致推理分解为平面对应、深度一致性和时间可逆性三个正交子目标，通过可验证约束优化。在多视图和视频基准上验证了分解策略的有效性，对自动驾驶中空间理解有潜在借鉴。
- **摘要（英）**: Addressing VLMs' flat spatial reasoning, this paper proposes FactoSR, a factorized RL framework decomposing world-consistent reasoning into planar, depth, and temporal objectives, showing substantial gains on multi-view and video benchmarks.
- **评估**: 该工作对提升VLM空间推理有重要价值，与自动驾驶3D感知相关。
- **核心贡献**: 提出因子化强化学习框架增强VLM空间推理能力。
- **创新点**: 将空间推理分解为可验证的几何子目标。
- **结果**: 在多视图和视频基准上取得显著性能提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite the remarkable prowess of Vision-Language Models (VLMs) in general multimodal tasks, they remain fundamentally ``flat'' when reasoning about the physical world. We argue that this spatial bottleneck stems from a profound dimensional mismatch: while VLMs are trained to interpret 2D projections, true spatial reasoning demands the recovery of latent 3D geometry and temporal continuity. To conquer this high-dimensional complexity, we advocate a shift from monolithic learning to a ``divide and conquer'' paradigm. We present FactoSR, a factorized reinforcement learning framework that explicitly interpret the dimensions collapsed by visual projection. At its core, FactoSR decomposes the monolithic problem of world-consistent reasoning into three orthogonal, geometric sub-objectives: planar correspondence ($XY$), depth consistency ($Z$), and temporal reversibility ($T$). By optimizing these verifiable constraints within a unified policy learning mechanism, we effectively transform an ill-posed projection recovery problem into a series of tangible reasoning steps. Extensive evaluations on multi-view and video benchmarks demonstrate that this elegant decomposition yields substantial gains in 3D and 4D reasoning, achieving a 5.9% boost on VSI-Bench and 4.5% on All-Angles-Bench. Our findings suggest that reinforcing explicit, factorized 4D consistency is a critical step toward evolving VLMs into robust, world-aware reasoners.

</details>

### 7. MetaStructAtlas: A Grounded 3D Vision-Language Dataset and Benchmark for Functional and Structural Reasoning in Whole-Body PET/CT **⭐⭐⭐** (相关度: 30%, 质量: 0.7)

- **arXiv ID**: [2609.03690](https://arxiv.org/abs/2609.03690)  · [📄 PDF](https://arxiv.org/pdf/2609.03690)
- **作者**: Chenguang Zheng, Le Xue, Yichi Zhang et al. (11 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-03 · **分类**: cs.CV
- **摘要（中）**: 针对全身PET/CT影像中功能与结构联合解读缺失的问题，提出MetaStructAtlas数据集和MetaStructVQA基准。该工作提供490个配准的3D PET/CT体数据、50,470个器官分割掩膜和100,565个QA对，并评估了现有3D医学VLM。虽属医学影像领域，但其3D多模态数据构建方法对自动驾驶3D感知有参考。
- **摘要（英）**: Addressing the gap in whole-body PET/CT interpretation, this paper introduces MetaStructAtlas, a large-scale dataset with 490 volumes and 100,565 QA pairs, and evaluates 3D medical VLMs, establishing a benchmark for multimodal reasoning.
- **评估**: 该工作为医学3D多模态推理提供基准，与自动驾驶感知关联有限。
- **核心贡献**: 构建全身PET/CT 3D视觉语言数据集和VQA基准。
- **创新点**: 整合解剖、代谢和语义标注的3D多模态数据。
- **结果**: 提供大规模基准并评估现有3D医学VLM。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The joint interpretation of metabolic function and anatomical structure is essential for clinical diagnosis in whole-body PET/CT. Although recent advances in 3D medical vision-language models have demonstrated remarkable progress, current efforts are limited to regional CT imaging, leaving a critical void in comprehensive whole-body PET/CT analysis. In this work, we introduce MetaStructAtlas, a large-scale dataset for grounded whole-body PET/CT interpretation that synthesizes multimodal imaging with integrated anatomical, metabolic, and semantic annotations. MetaStructAtlas provides 490 co-registered 3D PET and CT volumes with 50,470 organ-level segmentation masks and grounded radiology reports. To facilitate interactive reasoning, we further developed MetaStructVQA, a standardized 3D grounded visual question-answering benchmark containing 100,565 QA pairs. This framework explicitly links diagnostic queries to visual evidence across modalities, encompassing anatomical, morphological, and metabolic characteristics. Finally, we evaluate state-of-the-art 3D medical VLMs on MetaStructVQA, establishing a robust foundation for multimodal representation learning and integrated whole-body reasoning in nuclear medicine.

</details>

### 8. ViSAR: Training-Free Adaptive-$k$ Retrieval for Visual Document Question Answering **⭐⭐⭐** (相关度: 30%, 质量: 0.7)

- **arXiv ID**: [2609.02486](https://arxiv.org/abs/2609.02486)  · [📄 PDF](https://arxiv.org/pdf/2609.02486)
- **作者**: Adrien Mialland, Marc Plantevit, Julien Gallois et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-02 · **分类**: cs.IR, cs.AI, cs.CL
- **摘要（中）**: 针对文档视觉问答（DocVQA）中固定top-k检索导致延迟高且精度下降的问题，提出了一种无需训练的ViSAR方法，直接在嵌入空间中构建查询条件化的页面级相似度矩阵，动态确定检索页面数量。相比固定top-k和自适应检索启发式方法，ViSAR在保持或提升答案精度的同时，将RAG延迟降低高达58.7%。此外，相似度矩阵结构与答案精度相关，为检索质量感知的文档理解提供了新方向。
- **摘要（英）**: Addressing the issue of fixed top-k retrieval in DocVQA causing high latency and degraded accuracy, this paper proposes ViSAR, a training-free method that constructs a query-conditioned page-level similarity matrix in embedding space to dynamically determine retrieval count. It reduces RAG latency by up to 58.7% while maintaining or improving answer accuracy compared to fixed and heuristic retrieval. The correlation between matrix structure and accuracy suggests future directions for retrieval-quality-aware understanding.
- **评估**: 该方法对多模态检索效率有实际改进，但主题与自动驾驶感知关联较弱，创新性有限。
- **核心贡献**: 提出一种无需训练的适应性k检索方法，动态决定文档页面数量以提升效率。
- **创新点**: 利用嵌入空间的相似度矩阵结构实现查询自适应的检索数量决策。
- **结果**: 延迟降低58.7%，精度保持或提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Document Visual Question Answering (DocVQA) often leverages Retrieval-Augmented Generation (RAG), where late-interaction encoders are commonly used to identify document pages relevant to a user query, before answer generation by a Large Vision-Language Model (LVLM). Existing approaches typically retrieve a fixed top-$k$ number of pages regardless of query complexity, which increases LVLM latency and may degrade answer accuracy. We introduce ViSAR (Visual Semantic Activation Retrieval), a training-free adaptive-$k$ retrieval method for late-interaction visual document retrieval. ViSAR operates directly in the embedding space to construct a query-conditioned page-level similarity matrix that highlights query-relevant semantics and dynamically determines the number of pages to retrieve. Across multiple encoders and LVLMs, ViSAR retrieves compact, query-adapted page sets that reduce RAG latency by up to 58.7\%, while maintaining or improving answer accuracy compared with fixed top-$k$ and adaptive retrieval heuristics. Furthermore, we show that the similarity matrix structure correlates with answer accuracy, suggesting future directions for retrieval quality-aware document understanding.

</details>

### 9. GraFT: A Training-Free Framework for Spatial Reasoning in Multimodal Large Language Models via 3D Scene Graphs **⭐⭐⭐⭐** (相关度: 70%, 质量: 0.8)

- **arXiv ID**: [2609.03892](https://arxiv.org/abs/2609.03892)  · [📄 PDF](https://arxiv.org/pdf/2609.03892)
- **作者**: Junqing Du, Fernando Ropero, Erkin Turkoz et al. (5 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-03 · **分类**: cs.CV, cs.AI, cs.RO
- **摘要（中）**: 针对多模态大语言模型在3D空间推理中几何测量、视角转换和外观定位不可靠的问题，提出GraFT，一种无需训练的框架，通过紧凑的3D场景图提供缺失的3D结构。GraFT提供确定性几何符号工具、鸟瞰图渲染的异中心布局和任务相关自我中心帧的视觉属性定位。在ScanQA上，GraFT相比同骨干基线提升所有指标，CIDEr提高27%；在VSI-Bench上，提升冻结MLLM高达65%，超越多个专有和通用开源基线。
- **摘要（英）**: Addressing unreliable 3D spatial reasoning in MLLMs, GraFT introduces a training-free framework supplying 3D structure via compact 3D scene graphs. It offers deterministic geometry, BEV-rendered allocentric layout, and egocentric visual grounding. On ScanQA, it improves CIDEr by 27% over baseline; on VSI-Bench, it boosts frozen MLLMs by up to 65%, surpassing proprietary and open-source baselines.
- **评估**: 无需训练的3D场景图方法有效提升空间推理，BEV渲染与自动驾驶感知相关。
- **核心贡献**: 提出基于3D场景图的训练免费框架，增强MLLM的3D空间推理能力。
- **创新点**: 利用3DSG提供符号几何和BEV布局，无需微调或专用编码器。
- **结果**: ScanQA CIDEr提升27%，VSI-Bench提升65%。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D spatial reasoning underpins understanding and acting in the physical world, yet it remains unreliable in current multimodal large language models (MLLMs). These models falter at precise geometric measurement, at transforming between egocentric and allocentric viewpoints, and at grounding fine-grained appearance. The most common remedies fine-tune the model on large-scale curated spatial-reasoning datasets or attach dedicated encoders for 3D geometry, which typically couples the solution to costly supervision and a specific backbone. We instead introduce GraFT, a training-free framework that supplies the missing 3D structure through a compact, easily maintained 3D scene graph (3DSG). From this 3DSG, GraFT provides three spatial reasoning capabilities: (1) deterministic geometry through symbolic tools, (2) allocentric layout through a bird's-eye-view (BEV) rendering, and (3) visual-attribute grounding through task-relevant egocentric frames. On ScanQA, GraFT improves every metric over the same-backbone baseline, raising CIDEr by 27%. On VSI-Bench, GraFT improves frozen MLLMs by up to 65%, surpassing every proprietary and general-purpose open-source baseline, and several prominent fine-tuned spatial models.

</details>

### 10. When Do Frozen VLMs Respond to Image-Free Object-Token Edits? An Answer-Key-Free Protocol and What It Reveals **⭐⭐⭐** (相关度: 50%, 质量: 0.7)

- **arXiv ID**: [2609.03429](https://arxiv.org/abs/2609.03429)  · [📄 PDF](https://arxiv.org/pdf/2609.03429)
- **作者**: Wonbin Son, Gyumun Choi, Junil Seo et al. (6 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-03 · **分类**: cs.CV
- **摘要（中）**: 针对冻结视觉语言模型对对象级token编辑的响应条件不明确的问题，提出一种无答案键的协议，无需标注编辑后答案，通过逻辑确定答案并自审计。协议揭示响应并非自由：显式编辑教学而非普通VQA训练产生响应；响应受token清洁度和密度控制，检测器+分割器token可与oracle竞争并在VRSBench上超越；图像无关token路线保留匹配patch-token基线92-96%的自由文本VQA。
- **摘要（英）**: Addressing unclear conditions for frozen VLMs responding to object-token edits, this paper proposes an answer-key-free protocol scoring logically determined edits with self-audit. It reveals response requires explicit edit teaching, is governed by token cleanliness and density, and image-free token route preserves 92-96% of patch-token VQA. Detector+segmenter tokens are competitive with oracle and outperform on VRSBench.
- **评估**: 对VLM编辑机制有理论洞察，但与自动驾驶感知应用距离较远。
- **核心贡献**: 提出无答案键协议，系统分析冻结VLM对对象token编辑的响应条件。
- **创新点**: 通过自审计和逻辑确定答案，无需标注即可评估编辑响应。
- **结果**: 揭示响应依赖教学和token质量，保留高比例VQA性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Answering what-if queries about a scene with a VLM usually means injecting the assumption as text or repainting the scene with a generative model. We instead move the edit to the representation level, before the model input. The image is abstracted into a set of object-level tokens, and the original image never enters the VLM. This design rests on an open question: when do frozen VLMs actually respond to such token edits? We introduce an answer-key-free protocol: no post-edit answer is annotated. It scores edits whose answers are logically determined, and audits itself by reversing each scoreable choice. The protocol reveals three structures. The response is not free: explicit edit teaching, not ordinary VQA training, produces it in dense scenes and multiplies it in sparse ones, on all three operations. Once on, it is governed by token cleanliness and density, with deployable detector+segmenter tokens competitive with the oracle and outperforming it on VRSBench. And reading is a separable axis: the image-free token route preserves 92-96% of a matched patch-token baseline's free-text VQA, and the answers measurably depend on the tokens. The response, cleanliness, and reading structures are sign-preserved across two remote-sensing datasets (iSAID, VRSBench) and three frozen LM backbones. We release the probe generator, records, judge logs, and code.

</details>

---

## Network Pruning

### 1. Who Speaks for the Pruned? Visual Token Pruning as Coverage Optimization **⭐⭐⭐** (相关度: 50%, 质量: 0.75)

- **arXiv ID**: [2609.03158](https://arxiv.org/abs/2609.03158)  · [📄 PDF](https://arxiv.org/pdf/2609.03158)
- **作者**: Qingchan Zhu, Weihang You, Hanqi Jiang et al. (6 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-02 · **分类**: cs.CV, cs.CL, cs.LG
- **摘要（中）**: 针对视觉token剪枝方法仅关注保留哪些token，导致冗余高分数token被保留而重要证据缺乏代表的问题，提出CoverPruner，一种无需训练的剪枝器。该方法从需求侧出发，将剪枝建模为表示覆盖最大化（RCM）问题，确保每个被移除的token都有存活的原始token代表其信息。CoverPruner通过投影器空间覆盖和轻量级第一层注意力探针实例化RCM。在多种VLM架构和压缩率下，CoverPruner取得了所有对比方法中最高的平均准确率，且在激进压缩下提升最大。
- **摘要（英）**: This paper tackles the limitation of visual token pruning methods that only consider which tokens to keep, often retaining redundant high-scoring tokens while discarding evidence without representation. It proposes CoverPruner, a training-free pruner that formulates pruning as representational coverage maximization, ensuring each removed token is represented by a surviving one. Across multiple VLM architectures and compression rates, CoverPruner achieves the best average accuracy, with largest gains under aggressive compression.
- **评估**: 该论文提出新颖的覆盖优化视角，对VLM高效推理有实际价值，但与本领域（自动驾驶感知）相关性一般。
- **核心贡献**: 提出基于表示覆盖最大化的训练-free视觉token剪枝方法。
- **创新点**: 从需求侧重新定义剪枝问题，确保被移除token的表示覆盖。
- **结果**: 在多种VLM架构和压缩率下取得最佳平均准确率。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Visual token pruning reduces the inference cost of vision-language models (VLMs), but most methods only ask which tokens to keep. This retained-token view can keep redundant high-scoring tokens while leaving discarded evidence without a close representative. We propose CoverPruner, a training-free pruner that asks the complementary demand-side question: after a token is removed, which surviving original token represents it for the target VLM? CoverPruner formulates pruning as Representational Coverage Maximization (RCM), covering the full projected visual-token set with query-weighted demand. It instantiates RCM with projector-space coverage and a lightweight first-layer attention probe. Across multiple VLM architectures and compression rates, CoverPruner achieves the best average accuracy among all compared methods, with the largest gains usually appearing under aggressive compression.

</details>

### 2. Tree-Structured Vector Quantization For Efficient And Progressive Image Compression **⭐⭐⭐** (相关度: 20%, 质量: 0.7)

- **arXiv ID**: [2609.03641](https://arxiv.org/abs/2609.03641)  · [📄 PDF](https://arxiv.org/pdf/2609.03641)
- **作者**: Xinkun Wang, Tianyi Xu, Qingyu Luo et al. (7 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-03 · **分类**: cs.CV
- **摘要（中）**: ①针对基于向量量化的图像压缩方法无法提供渐进式比特流的问题，即每个前缀不能独立解码并逐步细化。②提出了Tree-VQ框架，将离散码字组织为层次二叉树，每个潜在token表示为从根到叶的路径，路径的每个前缀都是有效的量化表示，从而实现渐进解码。③相比现有可变码率方法，Tree-VQ无需重新编码即可从早期前缀解码并逐步改进，并引入了前缀兼容的树熵模型来编码渐进决策。④实验表明在率失真性能上取得显著提升，但摘要未提供具体数据。
- **摘要（英）**: This paper addresses the lack of progressive bitstreams in vector-quantization image compression by proposing Tree-VQ, which organizes codewords as a hierarchical binary tree where each prefix of a root-to-leaf path is a valid quantized representation. It enables decoding from early prefixes with successive refinements and introduces a prefix-compatible tree entropy model. Experiments demonstrate improved rate-distortion performance, though specific numbers are not provided in the abstract.
- **评估**: 该论文在图像压缩领域具有创新性，但与本用户关注的自动驾驶感知方向相关性较低。
- **核心贡献**: 提出了Tree-VQ，一种支持渐进式解码的树结构向量量化图像压缩框架。
- **创新点**: 利用二叉树路径前缀实现渐进式压缩表示，并设计前缀兼容熵模型。
- **结果**: 在率失真性能上优于现有方法，但具体数据未在摘要中给出。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vector-quantization based image compression has achieved strong rate--distortion performance, yet most of them still produce a separate compressed representation for each target bitrate. Such variable-rate behavior allows one model to operate at multiple rates, but it does not necessarily provide a progressive bitstream whose prefixes are themselves decodable and can be refined by appending additional bits. We propose \textbf{Tree-VQ}, a progressive tree-structured vector quantization framework for learned image compression. Tree-VQ organizes discrete codewords as a hierarchical binary tree and represents each latent token by a routed root-to-leaf path. Crucially, every prefix of this path corresponds to a valid quantized representation, so shallow internal nodes serve as coarse reconstruction codes and deeper nodes provide successive refinements. This allows a compressed image to be decoded from an early prefix and progressively improved as more branch symbols are received, rather than being re-encoded for different target rates. To make this structure practical for compression, we introduce a prefix-compatible tree entropy model that codes progressive continuation decisions and routed branch refinements using only causally available decoded contexts. We further use rate-aware refinement scheduling to decide which spatial blocks should receive additional tree bits under a given prefix budget, and hierarchical prefix supervision to ensure that internal nodes are directly decodable at low rates. Experiments show that Tree-VQ achieves a superior performance--efficiency trade-off, delivering the best perceptual compression results with much fewer parameters and lower latency than competing methods.

</details>

### 3. Neural Video Compression Based on Deformable Temporal Alignment and Difference-aware Fusion **⭐⭐** (相关度: 15%, 质量: 0.6)

- **arXiv ID**: [2609.03520](https://arxiv.org/abs/2609.03520)  · [📄 PDF](https://arxiv.org/pdf/2609.03520)
- **作者**: Chuyue Shan, Songlin Sun, Wang Chenwei et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-03 · **分类**: cs.CV, cs.AI
- **摘要（中）**: ①针对条件编码神经视频压缩中，复杂运动、遮挡和高频纹理区域因运动估计和对齐误差导致时间上下文不准确的问题。②提出了结合可变形时间对齐和差异感知空间选择性融合的方法，包括上下文感知时间对齐模块生成互补时间上下文，以及差异感知空间选择性融合模块自适应选择可靠时间信息并抑制错位。③相比DCVC-DC，该方法通过显式处理对齐误差和选择性融合提升了压缩性能。④实验表明在率失真性能上相比DCVC-DC有一定提升，但未提供具体数值。
- **摘要（英）**: This paper tackles inaccurate temporal context in conditional neural video compression caused by motion estimation and alignment errors in complex regions. It proposes a method combining deformable temporal alignment and difference-aware spatial selective fusion, with modules for generating complementary context and adaptively selecting reliable information. Experiments show rate-distortion improvements over DCVC-DC, though specific gains are not detailed.
- **评估**: 该论文聚焦视频压缩，与自动驾驶感知领域关联度低，但方法在视频处理上有一定参考价值。
- **核心贡献**: 提出了结合可变形对齐和差异感知融合的神经视频压缩方法。
- **创新点**: 通过差异感知选择性融合抑制时间错位信息。
- **结果**: 相比DCVC-DC取得率失真性能提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In conditional coding-based neural video compression, the quality of temporal context directly affects compression per- formance. Existing methods mostly construct context from prop- agated reference features, but they are vulnerable to motion esti- mation and local alignment errors in regions with complex mo- tion, occlusion, and high-frequency textures, resulting in inaccu- rate temporal information. To address this issue, this paper pro- poses a method combining deformable temporal alignment and difference-aware spatial selective fusion. A Context-aware Tem- poral Alignment Module is used to generate complementary tem- poral context, while a Difference-aware Spatial Selective Fusion module adaptively selects reliable temporal information and sup- presses misalignment. Experiments show that the proposed method achieves certain rate-distortion performance improve- ment over DCVC-DC.

</details>

### 4. Stable and Scalable Bundle Adjustment of Holistic 3D Structures **⭐⭐⭐** (相关度: 40%, 质量: 0.7)

- **arXiv ID**: [2609.04026](https://arxiv.org/abs/2609.04026)  · [📄 PDF](https://arxiv.org/pdf/2609.04026)
- **作者**: Shaohui Liu, Rémi Pautrat, Daniel Barath et al. (6 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-03 · **分类**: cs.CV
- **摘要（中）**: ①针对传统Bundle Adjustment（BA）仅优化相机参数和稀疏3D点，难以高效整合平行性、共面性等高层几何结构的问题。②提出一个统一框架，将几何特征和高阶关系联合优化，通过将组约束和跨特征关系（如点线关联）表达为2D重投影误差，并将组建模为类似相机的实体。③相比现有扩展方法，该框架在保持数值稳定性的同时，降低了计算成本，并支持可扩展的几何特征。④摘要未提供具体数据，但强调框架的稳定性和可扩展性。
- **摘要（英）**: This paper addresses the challenge of integrating high-order geometric structures like parallelism and coplanarity into Bundle Adjustment without sacrificing computational efficiency or numerical stability. It proposes a unified framework that models groups as camera-like entities and expresses group and cross-feature constraints via 2D reprojection errors. The approach improves scalability and stability over prior extensions, though specific quantitative results are not reported in the abstract.
- **评估**: 该论文对3D重建中的BA优化有理论贡献，但与自动驾驶感知核心任务（如检测、BEV）相关性较低，适合关注几何优化的研究者。
- **核心贡献**: 提出统一BA框架，联合优化几何特征和高阶关系，提升稳定性和可扩展性。
- **创新点**: 将组约束建模为相机实体，并用2D重投影统一表达。
- **结果**: 摘要未给出具体数据，但声称框架更稳定和可扩展。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Bundle Adjustment (BA) is a cornerstone of 3D computer vision and has benefited from decades of advances in sparse optimization and numerical methods. It was originally developed for jointly optimizing camera intrinsics, poses and sparse 3D points. While extensions incorporate lines and other primitives, integrating richer geometric structures such as parallelism, coplanarity, or wireframes often introduces significantly increased computational cost and reduced numerical stability. In this paper, we propose a unified framework that extends bundle adjustment to jointly optimize geometric features and higher-order relations. We first introduce a taxonomy that distinguishes scalable geometric features with direct 2D measurements (e.g., points and lines), from groups encoding higher-order relations (e.g., coplanarity, parallelism, etc.), where we show that groups can be modeled as camera-like entities within the bundle adjustment framework. Building on this formulation, we propose that both group constraints and cross-feature relations (i.e., point-line associations) can be expressed through 2D reprojection measurements. By formulating group-induced and cross-feature reprojection errors, we preserve the sparsity structure of classical point-based BA under Schur elimination, while avoiding direct 3D regularization that degrades the conditioning and stability. Experiments on both real-world and synthetic datasets demonstrate runtime performance comparable to classical point-only bundle adjustment, while producing significantly richer 3D structures and improved geometric accuracy.

</details>

### 5. Select, Compress, Reinvest: A Controlled Study of Visual-Token Allocation in Long-Video MLLMs **⭐⭐⭐⭐** (相关度: 60%, 质量: 0.8)

- **arXiv ID**: [2609.03820](https://arxiv.org/abs/2609.03820)  · [📄 PDF](https://arxiv.org/pdf/2609.03820)
- **作者**: Prakhar Khatri
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-03 · **分类**: cs.CV, cs.CL
- **摘要（中）**: ①针对长视频多模态大模型中视觉token分配策略（选择、压缩、再投资）未被系统研究的问题。②通过控制变量法，固定帧评分器、提示边界、分辨率策略和回答模型，逐一改变选择、空间压缩和再投资策略，在三个基准和两个模型上评估。③发现选择是最大杠杆：在LongVideoBench小时级任务中，8个查询选择帧比16个均匀采样帧高6.9分；OMP算法匹配或接近所有专用选择器。④压缩几乎免费（固定时间戳下空间预算减半最多损失0.44分），再投资可将预算转化为精度提升。
- **摘要（英）**: This paper systematically studies visual-token allocation in long-video MLLMs by isolating selection, compression, and reinvestment decisions. It finds selection is the dominant factor, with query-selected frames outperforming uniform sampling by 6.9 points, and OMP matching purpose-built selectors. Compression costs little, while reinvesting savings improves accuracy, providing actionable insights for video model design.
- **评估**: 该论文对视频理解和多模态模型有重要实践指导，虽非自动驾驶直接相关，但可迁移至多相机视频处理。
- **核心贡献**: 揭示长视频MLLM中token分配策略的影响，提供控制变量研究。
- **创新点**: 首次隔离选择、压缩和再投资的影响，并验证OMP的通用性。
- **结果**: 选择策略提升6.9分，压缩损失≤0.44分。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Long-video language models cannot look at every frame: an hour sampled once per second is 3,600 images, and a system keeps only a small fixed slice of that pool. Which frames survive that slice is usually treated as a preprocessing detail; we test whether it should be. Published selectors make the comparison hard because they change the frame scorer, the prompt boundary, the resolution policy, and the answering model all at once. We hold each fixed and vary one decision at a time: selection, spatial compression, and reinvestment of the savings, across six training-free selection rules, three long-video benchmarks, and two answering models. Selection is the largest single lever: on LongVideoBench's hour-long bin, eight query-selected frames beat sixteen uniformly spaced ones by 6.9 points, and Orthogonal Matching Pursuit, an unmodified decades-old sparse-approximation algorithm, matches or comes within a point of every purpose-built selector we compare it against, across all three benchmarks. Compression is close to free: halving each frame's spatial budget at fixed timestamps costs at most 0.44 points. Reinvestment is where that budget turns back into accuracy: spending the freed tokens on twice as many compressed frames, at a measured cost no higher than the original eight, returns a further two to three points; compression only pays off once its savings are spent this way. Along the way, an implementation bug in our own AKS baseline and a 0.07 to 3.74 point gap between two harnesses running the same published rules at the same budget show why these comparisons need to happen inside one controlled harness rather than across papers.

</details>

### 6. Rethinking 3D Noise: Learning 3D-Aware Video Priors via Optimization-Free Morphological Perturbations **⭐⭐⭐⭐** (相关度: 80%, 质量: 0.75)

- **arXiv ID**: [2609.03657](https://arxiv.org/abs/2609.03657)  · [📄 PDF](https://arxiv.org/pdf/2609.03657)
- **作者**: Onat Şahin, Mohammad Altillawi, George Eskandar et al. (5 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-03 · **分类**: cs.CV
- **摘要（中）**: ①针对NeRF和3DGS在稀疏视角下产生严重伪影，现有生成式修复依赖成对数据且需逐场景重建的问题。②提出3D形态扰动作为免优化的正则化器，利用3DGS将每个高斯视为基本单元，在尺度、旋转和剪枝上施加扰动，保持跨视角空间一致性。③相比2D增强，该方法无需逐场景优化循环，能学习更强的几何先验。④在轻量视频扩散模型上验证优于稀疏视角基线，扩展到14B参数视频模型后，平均深度误差降低12.5%。
- **摘要（英）**: This paper tackles artifacts in sparse-view 3D reconstruction by proposing 3D Morphological Perturbations, an optimization-free regularizer that perturbs Gaussian parameters to preserve spatial consistency. It eliminates per-scene optimization loops and improves geometric priors, reducing mean depth error by 12.5% in a 14B-parameter video model. The method is validated on NeRF and 3DGS, showing strong potential for autonomous driving perception.
- **评估**: 该论文对自动驾驶中稀疏视角3D感知有直接价值，方法创新且效果显著，值得关注。
- **核心贡献**: 提出3D形态扰动正则化，提升稀疏视角3D重建质量。
- **创新点**: 利用3DGS高斯作为基本单元，实现免优化的跨视角一致性增强。
- **结果**: 深度误差降低12.5%。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D scene representations like NeRF and 3D Gaussian Splatting (3DGS) suffer severe artifacts in sparse-view settings. Recent generative 3D artifact fixers attempt to address this, but rely on paired corrupted and clean renders requiring costly, per-scene reconstructions across varying view configurations. While 2D image augmentations act as instant regularizers, no explicit equivalents exist for 3D representations to preserve spatial consistency across views, an essential property for 3D-aware training. We propose 3D Morphological Perturbations as an optimization-free regularizer that preserves spatial consistency. Leveraging explicit 3DGS, we treat each Gaussian as a fundamental building block - analogous to a 2D pixel - and apply perturbations across its morphological parameter space via scale, rotation, and pruning. Our method eliminates per-scene 3DGS optimization loops from dataset curation while enabling models to learn stronger geometric priors than sparse-view baselines in diagnostic ablations conducted on a lightweight video diffusion sandbox. Scaled to a 14B-parameter video model via ControlNet, our approach maintains visual fidelity while reducing mean depth error by 12.5% over state-of-the-art image-to-image 3D artifact refiners, ultimately boosting downstream robotics policy success rates by up to 8.0% across 3 of 4 manipulation tasks.

</details>

---

## Multimodal

### 1. Puffin-World: Scaling a Unified Multimodal Model with Native 3D World States **⭐⭐⭐⭐** (相关度: 85%, 质量: 0.8)

- **arXiv ID**: [2609.04196](https://arxiv.org/abs/2609.04196)  · [📄 PDF](https://arxiv.org/pdf/2609.04196)
- **作者**: Kang Liao, Yihang Luo, Xiao-Ming Wu et al. (10 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-03 · **分类**: cs.CV
- **摘要（中）**: ①针对统一多模态模型缺乏原生3D世界状态建模和物理一致性生成的问题。②提出Puffin-World架构，联合建模物理（重力场、纬度）、几何（深度）和外观（图像）三种原生世界状态，并引入Omni-Camera表示支持多样任务和灵活运动，同时提出跨帧物理动力学传播策略，耦合外观和几何生成。③相比依赖外部离线模块的方法，实现端到端的3D世界生成与重建。④构建Puffin-16M数据集（1500万视觉-语言-相机三元组和100万其他数据），支持物理一致和视觉稳定的世界生成。
- **摘要（英）**: This paper addresses the lack of native 3D world state modeling and physical consistency in unified multimodal models. It proposes Puffin-World, jointly modeling physics, geometry, and appearance with an Omni-Camera representation and physical dynamics propagation, enabling closed-loop applications without external modules. It scales with a 15M vision-language-camera triplet dataset for physically consistent world generation.
- **评估**: 该工作将物理、几何和外观统一建模，推动多模态模型向3D世界理解与生成发展，对自动驾驶场景模拟有潜在价值。
- **核心贡献**: 提出统一多模态架构Puffin-World，原生集成3D世界状态和物理动力学传播。
- **创新点**: 联合建模物理、几何和外观三种世界状态，并耦合生成过程实现物理一致的3D世界模拟。
- **结果**: 构建Puffin-16M数据集，实现物理一致和视觉稳定的世界生成。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose Puffin-World, a unified multimodal architecture that integrates physical understanding, spatial simulation, and 3D world generation and reconstruction without relying on external offline modules. To reliably construct and interact with 3D worlds, our framework jointly models three native world states: physics (gravity field and latitude), geometry (depth), and appearance (image), together with a unified Omni-Camera representation that supports diverse tasks and flexible motions. Beyond modeling these states, we introduce a strategy for propagating physical dynamics across future frames. By grounding absolute camera properties in the real world, Puffin-World enables physically consistent and visually stable world generation. We further couple appearance and geometry within a single generative process, jointly synthesizing each future view and reconstructing its underlying geometry. This unified paradigm enables interleaved closed-loop applications requiring synergy across multiple tasks, including mimic and self-calibrated world exploration. To scale Puffin-World to complex scenarios, we construct Puffin-16M, comprising 15 million vision-language-camera triplets and 1 million trajectories featuring various and challenging motions. To foster further research in this area, we released the code, models, and datasets.

</details>

### 2. VisCAD: A Foundation Model Suite with Multimodal Industrial CAD Intelligence **⭐⭐⭐** (相关度: 40%, 质量: 0.7)

- **arXiv ID**: [2609.03811](https://arxiv.org/abs/2609.03811)  · [📄 PDF](https://arxiv.org/pdf/2609.03811)
- **作者**:  JoyIndustrial VisCAD Team, Linxin Cai, Qiuhe Hong et al. (13 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-03 · **分类**: cs.CV, cs.CL
- **摘要（中）**: ①针对工业CAD设计中现有模型输入域窄、泛化差，而通用前沿模型在CAD域表现不一致的问题。②提出VisCAD基础模型套件，核心是VisCAD-M1（27B参数），通过中期训练和后训练实现零件级设计生成，并复用为测试时验证器。③相比专用CAD模型和前沿模型，提供更广的泛化能力和强CAD能力。④在PubCADBench和RealCADBench上，VisCAD-M1平均零件级分数达0.5540，超过最强前沿模型的0.5496，测试时验证可提升至0.579。
- **摘要（英）**: This paper addresses poor generalization and inconsistent performance in industrial CAD generation across narrow and broad input domains. It proposes VisCAD, a foundation model suite with a 27B VisCAD-M1 model trained for part-level design generation and reused as a test-time verifier. It achieves the highest average part-level score of 0.5540 on benchmarks, surpassing the strongest frontier model.
- **评估**: 该工作展示了领域基础模型在CAD生成中的潜力，但相关性较低，主要面向工业设计而非自动驾驶。
- **核心贡献**: 提出VisCAD基础模型套件，实现跨模态工业CAD零件级和装配级生成。
- **创新点**: 通过中期和后训练结合测试时验证，提升CAD生成泛化能力。
- **结果**: 在基准上达到0.5540平均分数，超过最强前沿模型。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> AI-assisted computer-aided design (CAD) for industrial products involves two challenging phases. Part-level generation maps diverse forms of user intent, including renders, text descriptions, 2D drawings, and real photographs, to executable programs in a CAD domain-specific language. Assembly-level generation must additionally handle interacting parts, plan mating relations, estimate poses, and place all parts correctly. Existing specialized CAD models are commonly trained on narrow input domains, such as renders or texts, and often generalize poorly, while general-purpose frontier models cover broader inputs but perform inconsistently across CAD domains. We present VisCAD, a foundation model suite designed to provide both broad generalization and strong CAD capability for realistic industrial products. At its core is VisCAD-M1, a 27B model trained through mid-training and post-training for part-level design generation. On PubCADBench and RealCADBench, VisCAD-M1 achieves the highest average part-level score among the evaluated models, reaching 0.5540 compared with 0.5496 for the strongest frontier model. Reusing VisCAD-M1 as a test-time verifier can further raise the score to 0.5797, an approximately 5 percent relative improvement over the previous state of the art. VisCAD also includes a domain-specific harness that leverages frontier models for complex assembly generation and demonstrates advantages over general-purpose harnesses in both quantitative and qualitative evaluations.

</details>

### 3. Occlusion-Robust Multimodal Emotion Recognition in VR via Fusion of Facial Images and EMG **⭐⭐** (相关度: 30%, 质量: 0.6)

- **arXiv ID**: [2609.03569](https://arxiv.org/abs/2609.03569)  · [📄 PDF](https://arxiv.org/pdf/2609.03569)
- **作者**: Birgit Nierula, Karam Tomotaki-Dawoud, Mert Akguel et al. (8 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-03 · **分类**: cs.CV, cs.HC
- **摘要（中）**: ①针对VR中头戴显示器遮挡上半脸导致基于图像的情绪识别不完整的问题。②提出融合下半脸视频和上半脸肌电信号（EMG）的多模态情绪识别方法，引入20名受试者的同步数据集，采用晚期融合架构结合卷积视觉嵌入和RBF核EMG表示。③相比仅图像或仅EMG基线，利用EMG补充遮挡信息。④在受试者独立测试下，宏F1达51%，优于图像仅41%和EMG仅43%。
- **摘要（英）**: This paper addresses incomplete emotion recognition in VR due to HMD-induced upper-face occlusion. It proposes fusing lower-face video with upper-face EMG via a late-fusion architecture, introducing a synchronized multimodal dataset from 20 participants. It achieves 51% macro-F1, outperforming image-only and EMG-only baselines.
- **评估**: 该工作针对VR情绪识别，领域差异大，但对多模态融合策略有一定参考。
- **核心贡献**: 提出融合下半脸视频和EMG的VR情绪识别方法，并构建同步数据集。
- **创新点**: 利用EMG补充HMD遮挡下的上半脸信息，实现鲁棒多模态情绪分类。
- **结果**: 宏F1达51%，优于单模态基线。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Head-mounted displays (HMDs) fundamentally limit emotion recognition in virtual reality (VR): by occluding the upper face, they render conventional image-based facial expression analysis incomplete, particularly for applications requiring real-time affective assessment. We address this challenge by fusing lower-face video with facial electromyography (EMG) from the occluded upper face to classify seven emotional categories (six basic emotions plus neutral). We introduce a synchronized multimodal dataset from 20 participants, pairing lower-face video with seven-channel upper-face EMG elicited by validated emotion stimuli. Under subject-independent test, our proposed late-fusion architecture merging convolutional visual embeddings with RBF-kernel EMG representations achieves 51% macro-F1, outperforming both image-only (41%) and EMG-only (43%) baselines. These results demonstrate that upper-face EMG provides robust complementary information under HMD-induced visual occlusion and establish a foundation for multimodal emotion recognition in naturalistic VR environments. This approach facilitates affect-adaptive applications, including communication training and therapeutic interventions. The dataset will be shared upon request under an ethical-use agreement.

</details>

### 4. WIDE: Wildcard Inference with Dynamic Expansion for Cross-Modal Generative Retrieval **⭐⭐⭐** (相关度: 50%, 质量: 0.7)

- **arXiv ID**: [2609.03554](https://arxiv.org/abs/2609.03554)  · [📄 PDF](https://arxiv.org/pdf/2609.03554)
- **作者**: Teng Guo, Xin Wang, Jiayou Xu et al. (6 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-03 · **分类**: cs.CV, cs.AI
- **摘要（中）**: ①针对跨模态生成式检索中文本查询与视觉候选信息不对称导致强制幻觉和排名被无关候选劫持的问题。②提出WIDE方法，包含自适应熵阈值（AET）离线校准层特定不确定性边界，以及非对称感知通配符解码（AWD）在解码时检测语义盲区并发出通配符，动态扩展搜索空间，最后进行盲区重排序。③相比标准trie约束束搜索，避免对缺失细节的惩罚。④通过动态扩展和重排序提升检索准确性。
- **摘要（英）**: This paper addresses forced hallucination in cross-modal generative retrieval due to information asymmetry between text queries and visual candidates. It proposes WIDE with adaptive entropy thresholding and asymmetry-aware wildcard decoding to emit wildcards at semantic blind spots, dynamically expanding search space without penalties. This improves retrieval accuracy by avoiding irrelevant candidate hijacking.
- **评估**: 该工作针对生成式检索的幻觉问题，创新性强，但相关性一般，主要面向信息检索。
- **核心贡献**: 提出通配符推断与动态扩展方法，解决跨模态生成式检索中的信息不对称问题。
- **创新点**: 通过自适应熵阈值和非对称通配符解码，动态扩展搜索空间并避免惩罚。
- **结果**: 提升跨模态检索准确性，具体数据未在摘要中给出。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Generative retrieval has demonstrated significant success by unifying representation learning and search into a single sequence-to-sequence generation task. However, extending this paradigm to cross-modal retrieval reveals a critical challenge arising from the inherent information asymmetry across different modalities, such as the gap between concise text queries and dense visual candidates. This structural mismatch causes the autoregressive decoder to suffer from forced hallucination when generating identifiers via standard trie-constrained beam search, where the model is severely penalized for failing to guess fine-grained details absent from the query, allowing irrelevant candidates to hijack top rankings. To address this issue, we propose Wildcard Inference with Dynamic Expansion (WIDE). WIDE employs Adaptive Entropy Thresholding (AET) to calibrate layer-specific uncertainty boundaries offline. During the decoding generation phase, Asymmetry-aware Wildcard Decoding (AWD) detects semantic blind spots and emits wildcards instead of forced deterministic identifiers, dynamically expanding the search space without incurring log-probability penalties. Finally, Blind-Spot Re-ranking (BSR) evaluates the expanded candidate pool using a hybrid scoring mechanism that combines discrete generation confidence with continuous semantic similarity. Extensive experiments on the M-BEIR benchmark demonstrate that WIDE outperforms state-of-the-art generative retrieval methods, effectively suppressing forced hallucination while maintaining compact index structures.

</details>

### 5. KnowVis: Knowledge-Centric Visual Summarization for Video Lectures **⭐⭐** (相关度: 5%, 质量: 0.65)

- **arXiv ID**: [2609.03742](https://arxiv.org/abs/2609.03742)  · [📄 PDF](https://arxiv.org/pdf/2609.03742)
- **作者**: Yi Xu, Yifan Hou, Xiaoyu Zhang
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-03 · **分类**: cs.CV, cs.CL
- **摘要（中）**: ①针对视频讲座信息密集且线性传递，导致初学者认知过载的问题。②提出了KnowVis框架，从多模态视频内容提取概念图，识别阈值概念，构建结构化知识单元，并生成视觉摘要。③相比现有视频摘要方法，KnowVis将线性视频转换为基于教学法的视觉叙事，降低认知负担。④引入了包含125个教育视频和1079个视觉摘要的数据集，自动评估和人工研究表明优于最先进基线。
- **摘要（英）**: This paper addresses cognitive overload in video lectures by proposing KnowVis, a framework that extracts concept maps from multimodal content, identifies threshold concepts, and synthesizes visual summaries. It transforms linear videos into pedagogically grounded narratives, introducing a dataset of 125 videos with 1,079 summaries. Evaluations show superiority over state-of-the-art baselines.
- **评估**: 该论文面向教育视频摘要，与自动驾驶感知领域几乎无关。
- **核心贡献**: 提出了KnowVis，一种将视频讲座转化为视觉叙事摘要的框架。
- **创新点**: 利用概念图和阈值概念驱动视觉摘要生成。
- **结果**: 在自动评估和人工研究中优于基线方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Video lectures are valuable educational resources, but their dense and lengthy formats often overwhelm novice learners. This difficulty stems from a fundamental pedagogical mismatch: while videos deliver transient information linearly, human learning requires constructing interconnected cognitive networks, a task that induces severe cognitive overload for novice learners lacking prior domain knowledge. Existing video summarization methods fail to resolve this mismatch, as they primarily produce text-heavy, linear condensations that still demand high cognitive effort. To bridge this gap, we propose KnowVis, a framework that transforms linear video lectures into pedagogically grounded visual narratives. KnowVis first extracts a detailed concept map from multimodal video content to identify important and challenging threshold concepts, then constructs structured knowledge units, and finally synthesizes engaging visual summaries. Alongside the framework, we introduce a curated dataset of 125 educational videos across 10 academic disciplines, paired with 1,079 generated visual summaries. Extensive automated evaluations and a human study demonstrate that, compared to state-of-the-art baselines, KnowVis generates more accurate and clear visuals that successfully reduce cognitive load and significantly improve student learning effectiveness and knowledge retention.

</details>

### 6. Sensing Which Modality Matters: Evidence-Gated Regularization for Robust VLA Policies **⭐⭐⭐⭐** (相关度: 60%, 质量: 0.8)

- **arXiv ID**: [2609.03142](https://arxiv.org/abs/2609.03142)  · [📄 PDF](https://arxiv.org/pdf/2609.03142)
- **作者**: Yue Yang, Diego Romeres, Chiori Hori et al. (6 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-02 · **分类**: cs.RO, cs.CV, cs.LG
- **摘要（中）**: ①针对视觉-语言-动作策略在有限同质演示训练下产生模态纠缠，导致对无关传感器噪声敏感和单模态不足的问题。②提出了证据门控正则化，一种模态无关的训练目标，通过每帧每传感器的任务相关性信号门控两个一致性目标：低证据传感器上的不变性和高证据传感器上的单传感器充分性。③相比现有方法，EGR无需推理时开销，并引入基于BEHAVIOR-1K的基准，包含推理诊断套件和47个技能。④在BEHAVIOR-1K和两个真实机器人平台上验证了有效性，但摘要未提供具体数据。
- **摘要（英）**: This paper addresses modality entanglement in Vision-Language-Action policies, where spurious inter-sensor correlations cause nuisance sensitivity and single-modality insufficiency. It proposes Evidence-Gated Regularization (EGR), a training objective that gates consistency losses based on per-sensor task relevance, with zero inference overhead. EGR is validated on a BEHAVIOR-1K benchmark and two real-robot setups, showing improved robustness.
- **评估**: 该论文针对多模态机器人策略的鲁棒性，与自动驾驶多传感器感知有较强相关性，方法具有实际应用潜力。
- **核心贡献**: 提出了证据门控正则化，用于提升VLA策略对模态纠缠的鲁棒性。
- **创新点**: 利用任务相关性信号门控不变性和充分性约束。
- **结果**: 在仿真和真实机器人上验证了有效性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-Language-Action (VLA) policies fuse multimodal sensory inputs, but training on limited and homogeneous robot demonstrations encourages spurious inter-sensor correlations rather than task-relevant signal, a failure we term modality entanglement. Under real-world occlusions and distractors, this manifests as nuisance sensitivity to corruption of uninformative sensors and single-modality insufficiency when only one informative sensor remains intact. We propose Evidence-Gated Regularization (EGR), a modality-agnostic training objective that introduces zero inference-time overhead. EGR derives a per-frame and per-sensor task-relevance signal to gate two state-conditional consistency objectives: invariance on low-evidence sensors, and single-sensor sufficiency on high-evidence ones. We introduce a benchmark based on BEHAVIOR-1K, comprising a fast inference-only diagnostic suite and 47 rollout-based skills targeting modality entanglement. We validate EGR on this benchmark and on two real-robot setups with fundamentally different embodiments: a bi-manual setup with two Kinova arms and three RGB cameras, and a single-arm MELFA ASSISTA setup combining vision and GelSight tactile sensors. EGR improves simulation success rates (SR) from 12.5% to 16.4% under full modalities (+31%), from 9.4% to 16.5% under uninformative-sensor corruption (+75%), and from 2.8% to 6.1% under single-sensor fallback (+120%). Under physical-object distractors, EGR boosts SR from 30% to 85% on the bi-manual setup (+183%) and from 55% to 70% on the tactile setup (+27%).

</details>

---

## Multi-camera Perception

### 1. Sparse auto-regressive modeling for scene generation from multi-view images **⭐⭐⭐⭐** (相关度: 80%, 质量: 0.8)

- **arXiv ID**: [2609.03931](https://arxiv.org/abs/2609.03931)  · [📄 PDF](https://arxiv.org/pdf/2609.03931)
- **作者**: Thomas Lucas, Maxime Pietrantoni, Philippe Weinzaepfel et al. (7 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-03 · **分类**: cs.CV, cs.LG
- **摘要（中）**: 针对从稀疏无约束视图生成完整3D场景的挑战，提出SPAR3S，一种稀疏体素对齐的3D潜在生成模型，无需真实3D数据监督。核心思想是在仅表示占据体素的紧凑潜在空间中建模，通过可微3D高斯泼溅从多视图图像学习该空间。场景补全被转化为预测缺失潜在标记及其空间支持，使用掩码自回归Transformer联合建模占据和潜在特征。该方法在条件场景补全中实现了高效且可泛化的生成。
- **摘要（英）**: To generate complete 3D scenes from sparse views without 3D supervision, SPAR3S introduces a sparse voxel-aligned latent generative model, learning a compact latent space of occupied voxels via differentiable 3D Gaussian Splatting. Scene completion is formulated as predicting missing latent tokens and spatial support using a masked autoregressive transformer. This achieves efficient and generalizable conditional scene completion.
- **评估**: 该工作创新性地结合稀疏表示和自回归生成，解决了3D数据稀缺问题，对场景理解有潜力。
- **核心贡献**: 提出SPAR3S，首个无需3D监督的稀疏体素潜在自回归场景生成模型。
- **创新点**: 利用稀疏体素潜在空间和掩码自回归Transformer联合建模占据与特征。
- **结果**: 在条件场景补全中实现高效生成，优于现有前馈方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Generating complete 3D scenes from sparse, unconstrained views is a fundamental challenge in 3D vision which requires reasoning beyond observed content while remaining computationally tractable. Existing feed-forward reconstruction methods are inherently limited to content visible in the input images, while 3D generative modeling is hindered by the high computational cost of dense volumetric representations and the scarcity of large-scale 3D supervision. We introduce SPAR3S, a sparse voxel-aligned 3D latent generative model for conditional scene completion without requiring ground-truth 3D data for supervision. Our key insight is to formulate 3D scene generation in a structured, compact, voxel-aligned 3D latent space where only occupied voxels are represented. We learn this sparse latent space directly from multi-view images using photometric supervision via differentiable 3D Gaussian Splatting. Given a partial set of observed voxels encoded from sparse input views, scene completion reduces to predicting the missing latent tokens and their spatial support within the voxel grid. To this end, we train a masked autoregressive transformer that jointly models voxel occupancy and latent token values, enabling efficient and spatially consistent generation of unseen regions. We demonstrate the effectiveness of our method on synthetic indoor scenes, achieving higher novel-view quality than prior work. We further validate its generalization on RealEstate10k, highlighting its applicability to real-world data.

</details>

### 2. Urban Boundaries, Social Barriers: A Benchmark and Vision-Centric Framework for Mapping Gated Communities and Equity Implications **⭐⭐⭐** (相关度: 60%, 质量: 0.75)

- **arXiv ID**: [2609.03804](https://arxiv.org/abs/2609.03804)  · [📄 PDF](https://arxiv.org/pdf/2609.03804)
- **作者**: Minwei Zhao, Weiming Zhang, Jiawang Du et al. (7 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/MinweiZhao/GBA-GCs](https://github.com/MinweiZhao/GBA-GCs)
- **提交日期**: 2026-09-03 · **分类**: cs.CV
- **摘要（中）**: 针对封闭社区识别研究缺乏大规模可复现基准的问题，构建了GBA-GCs基准，覆盖粤港澳大湾区37,444个住宅区，包含边界多边形、高分辨率卫星图像、中文元数据和结构化属性。提出MCGC多模态分类器，基于DINOv3-SAT融合图像、文本和结构化线索，通过模态感知交叉注意和自适应门控缓解模态不平衡。实验表明MCGC优于强单模态和多模态基线，并应用于城市尺度映射揭示公平性影响。
- **摘要（英）**: To address the lack of large-scale benchmarks for gated community recognition, GBA-GCs covers 37,444 residential compounds with multimodal data. MCGC, a vision-centric framework based on DINOv3-SAT, fuses imagery, text, and structured cues via modality-aware cross-attention and adaptive gating. It outperforms baselines and enables city-scale equity analysis.
- **评估**: 该工作提供了稀缺的基准和实用框架，对城市计算和遥感应用有参考价值。
- **核心贡献**: 构建了首个大湾区封闭社区多模态基准并提出MCGC分类器。
- **创新点**: 通过自适应门控和跨注意融合多模态信息以缓解模态不平衡。
- **结果**: MCGC在基准上优于现有方法，并成功应用于城市尺度映射。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Communities are fundamental spatial units that shape urban form and social life. Whether a residential compound is spatially open or enclosed affects mobility, access to public services, and equity, yet studies of Chinese fengbi xiaoqu remain largely qualitative or small-scale, limiting reproducible city-scale analysis. We address this gap by introducing GBA-GCs, a metropolitan-scale multimodal benchmark for locally grounded gated/open community recognition in China's Greater Bay Area, covering 37,444 residential compounds with aligned boundary polygons, high-resolution satellite imagery, Chinese metadata, and structured attributes, together with expert-verified labels, inter-annotator reliability, and official evaluation splits. Built on this benchmark, we present Multimodal Classifier for Gated Community (MCGC), a vision-centric multimodal framework based on DINOv3-SAT that fuses imagery, text, and structured cues via modality-aware cross-attention and adaptive gating to mitigate modality imbalance. MCGC consistently outperforms strong unimodal and multimodal baselines. Finally, we apply the validated model to metropolitan-scale mapping and report equity-oriented findings including spatial clustering of GCs, privatized green space, and reduced pedestrian connectivity. The benchmark, code, and release documentation are available at https://github.com/MinweiZhao/GBA-GCs.

</details>

### 3. Learning from Scarce Labels: Multi-View Echocardiography for Ejection Fraction Prediction **⭐⭐⭐** (相关度: 40%, 质量: 0.7)

- **arXiv ID**: [2609.02969](https://arxiv.org/abs/2609.02969)  · [📄 PDF](https://arxiv.org/pdf/2609.02969)
- **作者**: Zhiyuan Gao, Dominic Yurk, Yaser S. Abu-Mostafa
- **🏷️ 机构**: Electrical Engineering Department, California Institute of Technology, Pasadena, CA 91125, USA, Asari AI, San Francisco, CA 94131, USA
- **💻 代码**: [github.com/Jeffrey4899/PLAX_EF_Labels_202509](https://github.com/Jeffrey4899/PLAX_EF_Labels_202509)
- **提交日期**: 2026-09-02 · **分类**: eess.IV, cs.CV, cs.LG
- **摘要（中）**: 针对胸骨旁长轴超声心动图预测射血分数缺乏公开数据集的问题，提出一种创新的数据生成策略，利用临床笔记和视频的时间相关性、微调视图分类器和代理标签，创建了超过25,000个PLAX视频的标注数据集。训练了首个可复现的PLAX EF模型，MAE为6.86%，与临床标准A4C方法（6%-7%）相当。进一步通过简单融合PLAX和A4C预测，MAE降至6.37%，展示了多视图集成的价值。
- **摘要（英）**: To overcome the lack of PLAX-EF datasets, a data generation strategy leverages time-based correlations and proxy labeling to create over 25,000 labeled videos. The first reproducible PLAX EF model achieves 6.86% MAE, comparable to clinical A4C methods. Late fusion of PLAX and A4C improves MAE to 6.37%, highlighting multi-view benefits.
- **评估**: 该工作解决了医学影像数据稀缺问题，方法实用，但领域相关性较低。
- **核心贡献**: 创建了首个公开PLAX-EF数据集并训练了可复现模型。
- **创新点**: 利用时间相关性和代理标签生成大规模标注数据。
- **结果**: PLAX模型MAE 6.86%，融合后达6.37%。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present, to the best of our knowledge, the first publicly available resource for predicting left ventricular ejection fraction (EF) from parasternal long-axis (PLAX) echocardiography. Because no PLAX-EF datasets previously existed, our work focuses on an innovative data generation strategy to overcome this scarcity. By leveraging a time-based correlation between clinical notes and echocardiographic videos, combined with fine-tuning view classifiers and proxy labeling, we created a labeled dataset of over 25,000 PLAX videos. This enables us to train the first reproducible PLAX EF model, achieving a mean absolute error (MAE) of 6.86%. Given that apical four-chamber (A4C) methods, the clinical standard, report MAE values of 6%-7%, our results demonstrate that EF estimation from PLAX views is both feasible and clinically relevant. This surpasses the performance of existing methods and provides a clinically relevant solution for situations where apical views may not be feasible. Going further, we demonstrate that combining PLAX and A4C predictions via simple unweighted late fusion improves both single-view baselines to a 6.37% MAE, underscoring the value of multi-view integration. To promote continued research, we release the dataset labels, trained models, and runnable demos on GitHub, Hugging Face, and Google Colab: https://github.com/Jeffrey4899/PLAX_EF_Labels_202509

</details>

### 4. BooM-VVT: Boosting Mask-Free Video Virtual Try-On with Image-Level Pseudo Data **⭐⭐⭐** (相关度: 50%, 质量: 0.7)

- **arXiv ID**: [2609.04120](https://arxiv.org/abs/2609.04120)  · [📄 PDF](https://arxiv.org/pdf/2609.04120)
- **作者**: Wei Zhang, Xin Li, Peishu Shi et al. (7 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-03 · **分类**: cs.CV
- **摘要（中）**: ①针对视频虚拟试穿依赖掩码定位，且视频级伪数据构建昂贵的问题。②提出BooM-VVT，基于关键帧驱动范式的无掩码框架，采用多阶段训练利用图像级伪数据学习无掩码定位，并提出服装敏感关键帧采样。③减少视频级伪数据需求，提升服装一致性。④实验验证了方法的有效性。
- **摘要（英）**: This paper addresses mask dependency and costly video-level pseudo data in video virtual try-on. It proposes BooM-VVT, a mask-free framework with multi-stage training using image-level pseudo data and garment-sensitive keyframe sampling. This reduces data costs and improves garment consistency.
- **评估**: 针对特定应用领域，方法有创新性，但与自动驾驶感知相关性低。
- **核心贡献**: 提出无掩码视频虚拟试穿框架BooM-VVT。
- **创新点**: 利用图像级伪数据实现无掩码定位，减少视频数据需求。
- **结果**: 在虚拟试穿任务中提升性能与一致性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Video virtual try-on (VVT) aims to generate realistic videos of a person wearing a target garment. Recent methods leverage a keyframe-driven video generation paradigm to improve in-the-wild performance, yet they still rely on masks to localize try-on regions, making them vulnerable to large motions and severe occlusions. Although mask-free image-based try-on methods have shown promising results by leveraging large-scale pseudo data, extending this paradigm to videos remains difficult, as constructing video-level pseudo data is prohibitively expensive. Furthermore, coarse keyframe sampling and the scarcity of multi-view try-on data limit existing keyframe-driven methods in maintaining garment consistency and handling diverse try-on tasks. To address these challenges, we propose BooM-VVT, a mask-free VVT framework built upon the keyframe-driven paradigm. To achieve mask-free VVT, we introduce a multi-stage training strategy that leverages image-level pseudo data for mask-free localization learning, substantially reducing the need for costly video-level pseudo data. To improve garment consistency, we propose Garment-Sensitive Keyframe Sampling, which selects keyframes based on garment-relevant body regions to better capture garment appearance. We further introduce Frame-Shared 3D-RoPE to establish spatiotemporal correspondences between keyframes and target video frames for accurate garment-detail transfer. Finally, we construct OmniView, a large-scale multi-view try-on dataset to support reliable try-on video generation under complex camera viewpoints and diverse try-on tasks. Extensive experiments demonstrate that BooM-VVT achieves superior temporal consistency and garment fidelity over existing methods. Project page: https://boomvvt.github.io/boomvvt.

</details>

### 5. Building Pretraining Data for World Models: An Unreal Engine-Based Pipeline for Action-Conditioned Video Generation **⭐⭐⭐⭐** (相关度: 85%, 质量: 0.8)

- **arXiv ID**: [2609.03557](https://arxiv.org/abs/2609.03557)  · [📄 PDF](https://arxiv.org/pdf/2609.03557)
- **作者**: Haoyu Wang, Songchun Zhang, Haoran Li et al. (6 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-03 · **分类**: cs.CV, cs.GR
- **摘要（中）**: ①针对动作条件视频模型缺乏与场景变化时间对齐的控制信号数据。②提出基于Unreal Engine的大规模合成数据生产管线，分两阶段执行：实时物理轨迹生成与离线高质量渲染，并集成分布式系统。③解决实时物理与离线渲染的冲突，提供多视角、动作对齐数据。④生产集群持续产出数据，支持世界模型预训练。
- **摘要（英）**: This paper addresses the scarcity of action-conditioned video data with aligned control signals. It presents an Unreal Engine-based pipeline with two-stage trajectory generation and offline rendering, plus a distributed production system. This enables large-scale synthetic data for world model pretraining.
- **评估**: 为自动驾驶世界模型提供关键数据基础设施，具有重要实用价值。
- **核心贡献**: 构建大规模动作条件多视角视频合成数据生产管线。
- **创新点**: 两阶段分离物理模拟与高质量渲染，实现可扩展数据生成。
- **结果**: 持续产出高质量合成数据，支持动作条件视频生成。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Action-conditioned video models require large-scale visual data paired with control signals that are temporally aligned with the resulting scene transitions. Such supervision is difficult to obtain from ordinary real-world video because the actions that caused each visual change are typically unknown. We present a large-scale synthetic data production pipeline built on Unreal Engine for generating action-conditioned, multi-view video. To accommodate the different execution requirements of real-time physics and high-quality offline rendering, the pipeline executes trajectory generation and final rendering in two stages: Stage I runs real physics in PIE and records per-frame character states, control inputs, and camera states into an intermediate trajectory representation; Stage II replays those trajectories in a new engine process and renders them offline with Movie Render Queue (MRQ). Around this core, we develop a distributed production system with cache-aware task partitioning, node-local slot scheduling, automated scene screening, aesthetic and luminance filtering, partial-output recovery, asynchronous upload, and continuous cluster health monitoring. The production cluster contains 25 servers with eight NVIDIA RTX 5090 GPUs per server. From 2,384 asset packs, 429 levels were retained for production together with a pool of 40 humanoid characters. The pipeline has produced 2,691 hours of 1080p video and 6,076 hours of 720p video. We describe the system architecture, the implementation decisions that emerged from production failures, and the limitations of using perceptual quality proxies for world-model data curation. The pipeline described in this report constitutes the Unreal Engine synthetic-data production component used in EchoWM.

</details>

---

## Autonomous Driving

### 1. Continuous Actions from Discrete Minds: Latent-Aligned Planning for End-to-End Autonomous Driving **⭐⭐⭐⭐** (相关度: 85%, 质量: 0.8)

- **arXiv ID**: [2609.04070](https://arxiv.org/abs/2609.04070)  · [📄 PDF](https://arxiv.org/pdf/2609.04070)
- **作者**: Ruoyu Yao, Yusen Xie, Qingzhao Liu et al. (8 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-03 · **分类**: cs.CV, cs.RO
- **摘要（中）**: 针对视觉语言模型（VLM）的离散推理与自动驾驶连续物理约束动作之间的鸿沟问题，提出LaPla，一种统一的视觉-语言-动作（VLA）框架。该方法设计基于残差向量量化变分自编码器（VQ-VAE）的动作分词器，将轨迹特征编码到结构化潜在空间，并作为物理先验而非离散码本查找，以减少量化误差。LaPla通过并发动作查询在多模态上下文中因果注意力，将隐藏状态直接投影到预训练的VQ-VAE潜在空间，再由冻结解码器生成连续动作。实验表明，该方法有效弥合语义理解与精确运动执行之间的差距。
- **摘要（英）**: This paper addresses the gap between discrete reasoning of VLMs and continuous, physics-constrained actions in autonomous driving. It proposes LaPla, a unified VLA framework with latent-aligned planning, using a VQ-VAE-based action tokenizer as a physical prior and concurrent action queries to project hidden states into the latent space for continuous action generation. The method effectively grounds semantic understanding in precise motion execution.
- **评估**: 该论文针对端到端自动驾驶中VLM离散与连续动作的融合问题，提出创新性潜在对齐方案，与自动驾驶感知高度相关。
- **核心贡献**: 提出LaPla框架，通过潜在对齐规划实现VLM语义理解到连续动作的映射。
- **创新点**: 将VQ-VAE潜在空间作为物理先验，避免离散量化误差并实现连续动作生成。
- **结果**: 有效弥合语义与动作之间的鸿沟，提升端到端驾驶性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Bridging the gap between the discrete reasoning of Vision-Language Models and the continuous, physics-constrained nature of autonomous driving remains a significant challenge. In this work, we introduce LaPla, a unified Vision-Language-Action (VLA) framework featuring latent-aligned planning to seamlessly ground semantic understanding in precise motion execution. We first design an action tokenizer based on a residual vector-quantized variational autoencoder (VQ-VAE), capturing vehicle kinematics and encoding trajectory features into a structured latent space. Rather than discrete codebook lookups that inevitably introduce quantization errors, LaPla repurposes this representation as a physical prior to bridge the modality gap between high-dimensional semantics and the raw action space. Specifically, given multimodal inputs integrating multi-view images, historical actions, and textual instructions, LaPla incorporates concurrent action queries to causally attend to the multimodal context in a single forward pass, projecting hidden states directly into the pretrained VQ-VAE latent space. The frozen decoder then translates these continuous latents into actions, effectively eliminating quantization errors and ensuring physically plausible trajectories while bypassing time-consuming autoregressive generation. Extensive experiments on the nuScenes benchmark demonstrate that LaPla achieves competitive open-loop performance, reducing long-horizon L2 error by 15.52% compared to state-of-the-art VLA methods. Closed-loop evaluations on the NVIDIA AlpaSim simulator further confirm its superior capability in ensuring smooth driving progress, improving the success rate by 33.34 percentage points with significantly reduced inference latency.

</details>

### 2. SV-WAM: An Efficient Surround-View World-Action Model for End-to-End Autonomous Driving **⭐⭐⭐⭐** (相关度: 90%, 质量: 0.85)

- **arXiv ID**: [2609.03602](https://arxiv.org/abs/2609.03602)  · [📄 PDF](https://arxiv.org/pdf/2609.03602)
- **作者**: Jinyang Wang, Shiwei Li, Junjian Wang et al. (15 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-03 · **分类**: cs.CV, cs.RO
- **摘要（中）**: 针对现有驾驶世界模型在推理时生成未来视频导致计算开销大、常采用单前视相机而限制安全关键场景空间覆盖的问题，提出SV-WAM，一种环视世界-动作模型。该方法保留完整六相机观测，同时保持高效推理，将未来视频预测作为动作学习的密集训练监督而非推理输出。核心是动作中心因果掩码，防止动作token在联合动作-视频去噪中关注未来视频token，从而在部署时可丢弃视频分支，实现仅动作规划。此外，引入可微分的可行驶区域合规正则化，惩罚车辆足迹角点接近或超出边界。实验表明，SV-WAM在安全关键操作中有效提升空间覆盖和规划性能。
- **摘要（英）**: This paper addresses the computational overhead and limited spatial coverage of driving world models that often use single front cameras. It proposes SV-WAM, a surround-view world-action model that preserves six-camera observations while using future-video prediction as dense training supervision, not inference output. With an action-centered causal mask and differentiable drivable-area regularizer, it enables efficient action-only planning at deployment, improving safety in maneuvers like lane changes and turns.
- **评估**: 该论文针对端到端驾驶中环视世界模型的高效推理问题，提出创新性训练策略，与自动驾驶感知高度相关且实验充分。
- **核心贡献**: 提出SV-WAM，实现环视世界-动作模型的高效推理与安全规划。
- **创新点**: 利用动作中心因果掩码将视频预测转为训练监督，部署时丢弃视频分支。
- **结果**: 在安全关键操作中提升空间覆盖和规划性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> World models (WMs) have demonstrated strong potential for end-to-end autonomous driving by learning predictive representations of future scene dynamics. However, generating future videos during inference introduces substantial computational overhead, leading many recent driving WMs to adopt a single front camera as input for efficient deployment. This design restricts spatial coverage in safety-critical maneuvers such as lane changes, merges, and turns. To address this limitation, we propose SV-WAM, a surround-view world-action model (WAM) that preserves full six-camera observations while maintaining efficient inference. SV-WAM leverages future-video prediction as dense training supervision for action learning within a shared generative model, rather than as an inference-time output. At the core of this design is an action-centered causal mask that prevents action tokens from attending to future-video tokens during joint action-video denoising. Consequently, the video branch can be discarded at deployment, enabling efficient action-only planning. Furthermore, we introduce a differentiable drivable-area compliance regularizer that penalizes vehicle-footprint corners approaching or crossing drivable boundaries, improving planning safety and boundary awareness. Extensive experiments on the closed-loop NAVSIMv2 benchmark and the open-loop nuScenes benchmark demonstrate that SV-WAM achieves state-of-the-art planning performance with low inference latency and competitive zero-shot transfer capability.

</details>

### 3. Understanding Autonomous Driving Datasets by Describing Differences between Image Subsets in Natural Language **⭐⭐⭐⭐** (相关度: 85%, 质量: 0.75)

- **arXiv ID**: [2609.03677](https://arxiv.org/abs/2609.03677)  · [📄 PDF](https://arxiv.org/pdf/2609.03677)
- **作者**: Julian Truetsch, Felix Hauser, Christoph Stiller et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/KIT-MRT/AD-Diff](https://github.com/KIT-MRT/AD-Diff)
- **提交日期**: 2026-09-03 · **分类**: cs.CV, cs.CL, cs.LG
- **摘要（中）**: 针对自动驾驶数据集分析依赖元数据或人工检查、缺乏语义洞察的问题，研究了集合差异描述任务，即给定两个图像子集，生成自然语言假设描述目标集与参考集的差异。通过两阶段公式，聚焦于目标检测得到的对象中心补丁，简化聚合并支持差异归因到具体对象实例或类别，并引入新基准AD-Diff Bench进行低浓度实验评估。实验限于开放权重模型，验证了该方法在稀疏真实差异场景中的适用性。
- **摘要（英）**: Addressing the lack of semantic insight in autonomous driving dataset analysis, this paper studies set difference captioning to generate natural-language hypotheses describing differences between image subsets. It adapts a two-stage method focusing on object-centric patches from detection, enabling attribution to instances, and introduces AD-Diff Bench for in-domain evaluation. Experiments with open-weight models demonstrate suitability for sparse real-world differences.
- **评估**: 为数据集理解提供了新视角，对自动驾驶领域的数据分析和域偏移检测有参考价值。
- **核心贡献**: 提出集合差异描述方法并构建自动驾驶专用基准，用于自然语言分析数据子集差异。
- **创新点**: 将对象中心补丁与两阶段描述结合，实现差异的实例级归因。
- **结果**: 在AD-Diff Bench上验证了低浓度差异下的有效性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Understanding the composition of large-scale autonomous driving datasets is essential for safety, robustness, and reliable operation across domains. For example, domain shift between locations could lead to the operating environment being misaligned with the training data, resulting in potentially dangerous performance degradation. Yet, existing data analysis pipelines largely rely on metadata, predefined labels, or manual inspection, which provide limited semantic insight or do not scale. This paper studies set difference captioning: given two subsets of images, the goal is to produce a natural-language hypothesis describing differences between the target and reference set. Building on a two-stage formulation, we adapt the method to autonomous driving by focusing on object-centric patches derived from object detection, which simplifies aggregation and enables attribution of differences to specific object instances or categories. To evaluate this setting in-domain, we introduce a new benchmark, AD-Diff Bench. Low-concentration experiments assess the suitability of set-difference-captioning approaches to sparse, real-world differences. We restrict our experiments to open-weight models to support reproducibility and ease of deployment. The proposed benchmark and analysis provide a step towards practical, human-interpretable dataset introspection for autonomous driving datasets. Our implementation and benchmark dataset are available at https://github.com/KIT-MRT/AD-Diff

</details>

### 4. Drive-HWM: Hierarchical World Models for Dynamic-Latent Guided Autonomous Driving **⭐⭐⭐⭐** (相关度: 95%, 质量: 0.8)

- **arXiv ID**: [2609.03572](https://arxiv.org/abs/2609.03572)  · [📄 PDF](https://arxiv.org/pdf/2609.03572)
- **作者**: Zhaoxin Fan, Tianbao Zhang, Wenjun Wu et al. (8 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-03 · **分类**: cs.CV
- **摘要（中）**: 针对现有世界模型将未来预测与动作生成分离或同尺度联合预测、难以同时实现长时预测和响应式决策的问题，提出Drive-HWM分层慢-快世界建模框架，在不同时间尺度上组织未来表示预测和动作生成。慢模型预测多步未来表示捕捉场景演化，引入动态感知潜变量通过光流预测学习；快模型利用轻量多模态骨干和自回归专家联合预测下一帧和即时动作。该方法旨在提升长时预测和基于观测的决策能力。
- **摘要（英）**: Addressing the difficulty of balancing long-horizon anticipation and responsive decision-making in world models, Drive-HWM proposes a hierarchical slow-fast framework organizing future representation prediction and action generation at complementary scales. The slow model predicts multi-step future representations with dynamic-aware latents from optical flow, while the fast model jointly predicts next frame and action. This enables improved scene evolution modeling and grounded decision making.
- **评估**: 分层时间尺度设计对自动驾驶世界模型有重要创新，与感知和决策紧密相关。
- **核心贡献**: 提出分层慢-快世界模型，分离长时预测与即时动作生成。
- **创新点**: 引入动态感知潜变量和双时间尺度联合预测机制。
- **结果**: 预期提升长时预测和响应式决策性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> World models offer a promising paradigm for autonomous driving by predicting how traffic scenes may evolve and using such predictions to support action generation. However, existing approaches either separate future prediction from action generation or jointly predict them at the same temporal scale, making it difficult to simultaneously achieve long-horizon anticipation and responsive, observation-grounded decision making. We present Drive-HWM, a hierarchical slow--fast world modeling framework that organizes future representation prediction and action generation at complementary temporal scales. The slow world model predicts multi-step future representations to capture extended scene evolution. To explicitly model the abundant motion dynamics in driving environments, we introduce Dynamic-Aware Latents learned through optical-flow prediction. Guided by these future representations, the fast model uses a lightweight multimodal backbone and an autoregressive expert to jointly predict the next frame and the immediate action from the latest observation. Next-frame prediction encourages the fast model to capture imminent scene evolution, while one-step action generation allows decisions to be continuously updated as new observations arrive. Extensive experiments on NAVSIM v1 and v2 demonstrate the strong driving performance of Drive-HWM. Comprehensive ablation studies further validate the effectiveness of the hierarchical slow--fast design, dynamics-aware future representations, and joint next-frame and action prediction.

</details>

---

## Video Understanding

### 1. Beyond Retrieval: Progressive Latent Memory Evolution for Streaming Video Understanding **⭐⭐⭐⭐** (相关度: 75%, 质量: 0.8)

- **arXiv ID**: [2609.04131](https://arxiv.org/abs/2609.04131)  · [📄 PDF](https://arxiv.org/pdf/2609.04131)
- **作者**: Hongyu Qu, Guangming Yao, Ling Xing et al. (10 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-03 · **分类**: cs.CV
- **摘要（中）**: ①针对流式视频理解中现有存储-检索范式无法将历史证据内化为紧凑演化潜在记忆的问题。②提出LatentStream框架，包含查询无关的层次流式记忆（短、中、长期）通过Jenks引导自适应整合，以及层次潜在记忆演化，使记忆令牌组具有渐进扩展的感受野，迭代检索历史信息。③相比外部记忆库方法，实现从存储-检索到检索-内化的转变。④在固定记忆预算下持续引导流式推理，提升理解性能。
- **摘要（英）**: This paper addresses the limitation of store-and-retrieve paradigms in streaming video understanding, which fail to internalize historical evidence into evolving latent memory. It proposes LatentStream with query-agnostic hierarchical streaming memory and hierarchical latent memory evolution, enabling progressive memory receptive fields for iterative retrieval. This shifts the paradigm to retrieve-and-internalize, improving streaming reasoning under bounded memory.
- **评估**: 该工作提出新颖的潜在记忆演化框架，对视频理解和在线感知有重要启示，与自动驾驶流式感知相关。
- **核心贡献**: 提出LatentStream框架，将流式视频记忆从存储-检索转变为检索-内化。
- **创新点**: 通过层次潜在记忆令牌和渐进扩展感受野，实现动态记忆演化。
- **结果**: 在固定记忆预算下提升流式视频理解性能，具体数据未在摘要中给出。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Streaming video understanding requires multimodal large language models (MLLMs) to process continuous visual inputs and respond to user queries under strict causality and bounded memory. Existing approaches typically compress historical observations into an external memory bank and retrieve query-relevant evidence as additional visual context. Though effective, this store-and-retrieve paradigm keeps historical evidence as external visual context, preventing it from being internalized into a compact, evolving latent memory that can continuously guide streaming reasoning. To bridge this gap, we introduce LatentStream, a progressive latent working memory framework that shifts streaming memory from store-and-retrieve to retrieve-and-internalize. Specifically, LatentStream comprises three coordinated components. First, Query-agnostic Hierarchical Streaming Memory organizes visual history into short-, mid-, and long-term levels under a fixed memory budget through Jenks-guided adaptive consolidation. Once a query arrives, Hierarchical Latent Memory Evolution equips groups of latent memory tokens with progressively expanding memory receptive fields, enabling them to iteratively retrieve historical evidence from their corresponding scopes and internalize it into a compact, fixed-length latent memory. Finally, Progressive Confidence-guided Latent Memory Optimization constructs a hierarchical progression reward from group-wise predictive entropy and jointly refines the latent memory tokens and retrieved evidence, encouraging increasingly confident streaming reasoning. Extensive experiments demonstrate that LatentStream achieves new state-of-the-art results on existing online and offline video benchmarks.

</details>

### 2. CoFiE: Coarse-to-Fine Evidence Selection for Efficient Streaming Video Understanding **⭐⭐⭐⭐** (相关度: 70%, 质量: 0.85)

- **arXiv ID**: [2609.03675](https://arxiv.org/abs/2609.03675)  · [📄 PDF](https://arxiv.org/pdf/2609.03675)
- **作者**: Jing Jiang, Yiran Ling, Ruonan Li et al. (5 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-03 · **分类**: cs.CV
- **摘要（中）**: 针对流式视频理解中视觉编码成本高、端到端延迟大的问题，提出CoFiE框架，将证据选择解耦为视觉编码前的粗粒度查询无关过滤和LLM预填充阶段的细粒度查询相关精炼。通过新颖性引导的帧过滤和查询特定证据精炼，在编码前去除冗余帧，同时保留语义信息后的精细选择。实验表明在多个视频理解基准上达到78.86%的准确率，实现了新的精度-效率权衡。
- **摘要（英）**: To address high visual encoding costs and end-to-end latency in streaming video understanding, CoFiE decouples evidence selection into coarse query-agnostic filtering before the vision encoder and fine query-specific refinement during LLM prefill. It introduces novelty-guided frame filtering and query-specific evidence refinement to remove redundancy pre-encoding while preserving semantic refinement. Experiments achieve 78.86% accuracy across benchmarks, setting a new accuracy-efficiency trade-off.
- **评估**: 该工作从系统层面优化视频理解流程，创新性地在编码前进行过滤，对实时应用有重要价值。
- **核心贡献**: 提出CoFiE，首个在视觉编码前进行粗粒度过滤的流式视频理解框架。
- **创新点**: 将证据选择解耦为编码前粗过滤和编码后细精炼两阶段。
- **结果**: 在多个基准上达到78.86%准确率，优于现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Streaming video understanding requires Vision Language Models (VLLMs) to process growing video streams and answer user questions under tight latency constraints. Existing methods improve efficiency through token pruning and memory-bank schemes, but mainly reduce visual tokens after visual encoding. Consequently, downstream token pruning alone cannot substantially reduce end-to-end latency because the expensive frame encoding cost has already been incurred. We propose CoFiE, a Coarse-to-Fine Evidence Selection framework that decouples evidence selection into a coarse, query-agnostic filtering stage before the vision encoder and a fine, query-specific refinement stage during LLM prefill. CoFiE introduces Novelty-Guided Frame Filtering to retain visually distinctive candidate frames and Query-Specific Evidence Refinement to select the frames most relevant to the user query. This design removes substantial redundancy before frame encoding while preserving query-specific refinement once semantic information becomes available. Experiments show that CoFiE establishes a new state-of-the-art accuracy-efficiency trade-off across multiple video understanding benchmarks, reaching 78.86% accuracy on StreamingBench and 68.72% on OvO-Bench, with improvements of up to 3.15% over prior methods. Even with up to 80% evidence-frame filtering, CoFiE outperforms strong open-source multimodal models while improving end-to-end inference latency by up to 2.54 times.

</details>

### 3. The Shape of Time: Video-Token Contrast for Temporal Understanding in VideoLMs **⭐⭐⭐⭐** (相关度: 70%, 质量: 0.8)

- **arXiv ID**: [2609.04110](https://arxiv.org/abs/2609.04110)  · [📄 PDF](https://arxiv.org/pdf/2609.04110)
- **作者**: Yumeng Shi, Quanyu Long, Yin Wu et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/ANDgate99/VT-Contrast](https://github.com/ANDgate99/VT-Contrast)
- **提交日期**: 2026-09-03 · **分类**: cs.CV
- **摘要（中）**: ①针对VideoLM中视频token表示缺乏时间理解监督，模型依赖物体、场景等捷径回答时间问题。②提出VT-Contrast，一种表示级时间反事实目标，监督晚期层最后一帧视频token，对比顺序保持视图与按Kendall tau距离排序的重排序反事实。③无需架构改动，兼容多种训练任务，直接作用于时间信息整合位置。④在时间理解基准上整体性能提升。
- **摘要（英）**: This paper addresses the lack of temporal supervision on video-token representations in VideoLMs, which allows shortcuts. It proposes VT-Contrast, a representation-level counterfactual objective that supervises late-layer last-frame tokens with order-preserving versus reordered views. It requires no architectural changes and improves temporal understanding benchmarks.
- **评估**: 该工作为视频时间理解提供了新的监督范式，对多模态感知中的时序建模有参考价值。
- **核心贡献**: 提出VT-Contrast，首个针对视频token表示的时间反事实对比目标。
- **创新点**: 在表示层而非文本层施加时间监督，利用Kendall tau距离分级反事实。
- **结果**: 在时间理解基准上整体性能提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Seeing frames in order does not mean representing time. Modern VideoLMs receive ordered video streams, yet their main supervision acts on generated text rather than video-token representations where event dynamics should first emerge. This mismatch allows models to learn temporal answers from shortcuts such as objects, scenes, and language priors, without requiring internal video representations to capture event progression. To address this, we propose VT-Contrast, a representation-level temporal counterfactual objective for VideoLMs. Its design asks where temporal supervision should act and what temporal differences it should expose. VT-Contrast supervises selected late-layer last-frame video tokens, where temporal information is expected to be integrated before language generation, and contrasts order-preserving views with same-video reordered counterfactuals graded by Kendall tau distance. It requires no architectural changes, is compatible with diverse VideoLM training tasks, and improves overall performance across temporal understanding benchmarks. Our code is available at https://github.com/ANDgate99/VT-Contrast.

</details>

### 4. FlashRender: Few-Step Generative Rendering via Camera-Controlled Video MeanFlow **⭐⭐⭐** (相关度: 60%, 质量: 0.7)

- **arXiv ID**: [2609.03563](https://arxiv.org/abs/2609.03563)  · [📄 PDF](https://arxiv.org/pdf/2609.03563)
- **作者**: Byeongjun Park, Byung-Hoon Kim, Hyungjin Chung
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-03 · **分类**: cs.CV
- **摘要（中）**: ①针对多步生成渲染模型中采样步数依赖的相机控制误差，导致去噪轨迹弯曲。②提出FlashRender框架，包含RETA对齐源视频表示与目标特征，MeanFlow目标微调，以及on-policy流图蒸馏。③RETA直接编码几何变换，降低轨迹曲率，使少步采样更有效。④实验表明三个组件互补，实现秒级重渲染。
- **摘要（英）**: This paper tackles sampling-step-dependent camera control errors in generative rendering. It introduces FlashRender with RETA for representation alignment, MeanFlow fine-tuning, and on-policy distillation. These components reduce trajectory curvature and enable few-step rendering in seconds.
- **评估**: 对视频生成与渲染领域有贡献，但与自动驾驶感知核心关联较弱。
- **核心贡献**: 提出FlashRender，实现少步生成渲染的相机控制一致性。
- **创新点**: RETA对齐源视频与目标几何特征，降低去噪轨迹曲率。
- **结果**: 在少步采样下实现秒级高质量渲染。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present FlashRender, a few-step generative rendering framework that retakes a source video along a target camera trajectory in seconds. We identify sampling-step-dependent camera control as a prominent manifestation of discretization error in existing multi-step generative rendering models and show that resolving this inconsistency substantially lowers denoising trajectory curvature, facilitating subsequent step distillation. To this end, we introduce Representation Transformation and Alignment (RETA), which aligns hidden source-video representations with target-video features from a frozen visual geometry model. This directly encodes the geometric transformation within the source-video stream, enabling sampling-step-consistent camera control. We then fine-tune the model with the MeanFlow objective on the lower-curvature denoising trajectory induced by RETA, allowing the model to more effectively address discretization error. Finally, we apply on-policy flow map distillation to correct self-rollout errors under fixed few-step sampling. Extensive experiments show that RETA, MeanFlow, and on-policy flow map distillation play complementary roles in few-step generative rendering. Together, they enable our approach to match multi-step baselines in video quality and geometric consistency at 25x lower sampling cost while achieving superior camera controllability, even under out-of-distribution target camera trajectories.

</details>

---

## Object Detection

### 1. Residual Optimal Transport-Based Experts Collaboration Towards Modality-Aware Infrared-Visible Object Detection **⭐⭐⭐⭐** (相关度: 90%, 质量: 0.8)

- **arXiv ID**: [2609.03516](https://arxiv.org/abs/2609.03516)  · [📄 PDF](https://arxiv.org/pdf/2609.03516)
- **作者**: Yue Zhao, Hua Yu, Yukun Zhao et al. (9 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-03 · **分类**: cs.CV
- **摘要（中）**: 针对红外-可见光目标检测中传感器缺失或间歇性导致固定融合失效的问题，提出FlexibleFusion，一种统一自适应方法，灵活分配集成路径和融合强度，在完整和缺失模态场景下均能工作。核心是模态感知专家协作机制，选择性激活跨模态或内模态专家路径，完整时跨模态融合，缺失时自融合；并设计残差自步熵最优传输对齐异构特征分布。该方法解决了光谱分布差异下的语义相关性估计挑战。
- **摘要（英）**: Addressing sensor failure in infrared-visible object detection where fixed fusion collapses, FlexibleFusion proposes a unified adaptive method allocating integration pathways and fusion strength across complete and missing-modality regimes. The Modality-Aware Experts Collaboration mechanism activates cross-modal or intra-modal paths, with Residual Self-Paced Entropic Optimal Transport aligning heterogeneous distributions. This handles missing modalities and spectral discrepancy effectively.
- **评估**: 针对实际传感器缺失场景的鲁棒融合方法，对自动驾驶多模态感知有重要价值。
- **核心贡献**: 提出FlexibleFusion，支持完整和缺失模态的自适应红外-可见光目标检测。
- **创新点**: 模态感知专家协作与残差最优传输结合，实现灵活融合。
- **结果**: 在缺失模态条件下保持检测性能，优于固定融合。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Infrared-visible object detection (IVOD) integrates complementary evidence from visible and infrared sensors for reliable perception in challenging scenes. In practice, sensors may fail or drop frames, leaving one modality unavailable or intermittent. Existing methods for IVOD assume both modalities are always present, and fixed fusion collapses when one stream is missing. Furthermore, it remains a critical challenge to reliably estimate semantic correlation across heterogeneous modalities, especially under spectral distribution discrepancy. We present FlexibleFusion, a unified and adaptive method that flexibly allocates integration pathways and fusion strength, operating seamlessly across complete and missing-modality regimes. At its core, the Modality-Aware Experts Collaboration (MAEC) mechanism selectively activates and aggregates cross-modal or intra-modal expert pathways. It allows cross-modal fusion when full modalities are available and falls back to self-fusion under missing conditions. Additionally, we design Residual Self-Paced Entropic Optimal Transport (RSPEOT) to align heterogeneous feature distributions from a transport perspective. Instead of relying on the fixed sparsity coefficient in standard entropic optimal transport (EOT), RSPEOT introduces a residual-driven self-paced update that prioritizes reliable matches and progressively refines harder ones. This design alleviates the additional optimization burden of standard EOT while preserving reliable semantic alignment. Comprehensive experiments under complete and missing-modality protocols show consistent performance across arbitrary modality configurations. Code will be released upon publication.

</details>

### 2. When Depth Hurts: Reliability-Aware Geometry Distillation for Depth-Free RGB-D Salient Object Detection **⭐⭐⭐** (相关度: 60%, 质量: 0.7)

- **arXiv ID**: [2609.03378](https://arxiv.org/abs/2609.03378)  · [📄 PDF](https://arxiv.org/pdf/2609.03378)
- **作者**: Xuehao Wang, Jiaxin Hua, Runmei Li et al. (7 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-03 · **分类**: cs.CV
- **摘要（中）**: ①针对RGB-D显著目标检测中传感器深度不可靠（如缺失区域、模糊边界）导致多模态融合性能下降的问题。②提出可靠性感知几何蒸馏框架，训练时用冻结的Depth Anything V2作为教师，将密集相对几何、层次空间注意力和边界结构蒸馏到紧凑的边缘感知几何分支，并通过像素级可靠性估计选择性注入兼容几何，推理时仅用RGB。③相比现有质量感知方法，不依赖数据集提供的深度，实现无深度推理。④在36个指标-数据集比较中，26个达到最佳或并列最佳。
- **摘要（英）**: This paper addresses unreliable sensor depth in RGB-D salient object detection that degrades fusion performance. It proposes a reliability-aware geometry distillation framework using a frozen Depth Anything V2 teacher to transfer geometry and boundary knowledge to a compact branch, with pixel-wise reliability estimation for selective injection, enabling RGB-only inference. It achieves best or tied-best results in 26 of 36 metric-dataset comparisons.
- **评估**: 该工作创新性地将深度蒸馏与可靠性估计结合，实现无深度推理，对多模态感知中的模态缺失问题有借鉴意义。
- **核心贡献**: 提出首个无需训练和推理深度数据的可靠性感知几何蒸馏框架，用于RGB-D显著目标检测。
- **创新点**: 利用冻结深度模型作为教师，通过像素级可靠性估计选择性注入几何信息，实现纯RGB推理。
- **结果**: 在36个指标-数据集比较中26个达到最佳或并列最佳。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Depth can resolve appearance ambiguity in RGB-D salient object detection (SOD), yet sensor depth is not uniformly reliable. Missing regions, blurred boundaries, and structural artifacts can propagate through multimodal fusion and make an RGB-D detector less accurate than its RGB-only counterpart. Existing quality-aware approaches regulate observed depth but remain dependent on the same potentially defective modality. We propose \method, a reliability-aware geometry distillation framework developed for RGB-D SOD benchmarks without using dataset-provided depth during training or inference. A frozen Depth Anything V2 model serves only as a training-time teacher, transferring dense relative geometry, hierarchical spatial attention, and boundary structure to a compact edge-aware geometry branch. Pooled bidirectional interaction aligns geometry with appearance, and a pixel-wise reliability estimator selectively injects geometry that is compatible with the current RGB representation. The teacher is removed after training, leaving an RGB-only inference network. Trained on 2,985 RGB-mask pairs, \method{} achieves the best or tied-best result in 26 of 36 metric-dataset comparisons against ten recent RGB-D SOD methods, including a 13.4\% relative MAE reduction on ReDWeb-S. When retrained on DUTS-TR, it also improves the strongest prior $F$-measure by 4.2\% on PASCAL-S, showing that the distilled geometry transfers beyond a particular sensor or dataset domain. Code will be released upon publication.

</details>

### 3. Preserving Knowledge across Space and Time for Continual Video Deepfake Detection **⭐⭐⭐⭐** (相关度: 30%, 质量: 0.8)

- **arXiv ID**: [2609.03446](https://arxiv.org/abs/2609.03446)  · [📄 PDF](https://arxiv.org/pdf/2609.03446)
- **作者**: Taehoon Kim, Jongwook Choi, Heejae Jo et al. (5 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-03 · **分类**: cs.CV
- **摘要（中）**: ①针对视频深度伪造检测中，现有持续学习方法仅针对图像，无法捕捉视频特有的时空线索，且不同伪造类型对空间和时间模态的依赖不同。②提出了模态特定频率蒸馏框架，在频域将视频特征分解为空间、时间和时空模态，实现各模态的独立保留，并采用跨模态去相关损失使时空表示与单模态线索正交。③相比现有方法，显式分解模态并独立蒸馏，适应不同伪造类型对模态的差异化依赖。④实验表明在多种视频深度伪造数据集上，相比最先进方法具有更强的适应性和性能保持能力。
- **摘要（英）**: This paper addresses the limitation of continual deepfake detection methods that ignore video-specific spatial and temporal cues by proposing Modality-Specific Frequency Distillation (MSFD), which decomposes video features into spatial, temporal, and spatiotemporal modalities in the frequency domain. It preserves each modality independently and uses cross-modality decorrelation to maintain orthogonal representations. Experiments show stronger adaptation and better performance retention than state-of-the-art methods across diverse datasets.
- **评估**: 该论文在持续学习领域有创新，但视频伪造检测与自动驾驶感知相关性有限，不过其模态分解思想可借鉴。
- **核心贡献**: 提出了MSFD，一种针对视频深度伪造检测的模态特定频率蒸馏持续学习框架。
- **创新点**: 在频域分解时空模态并独立蒸馏，结合跨模态去相关。
- **结果**: 在多个数据集上优于现有持续学习方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The continuous emergence of high-quality video deepfakes requires detectors that continually adapt to new forgery patterns, yet existing approaches, which are designed for deepfake images, fail to capture video-specific cues. Unlike deepfake images that contain only spatial artifacts, deepfake videos leave distinct evidence along both spatial and temporal axes, necessitating the separate preservation of each modality during sequential model updates. To overcome this limitation, we introduce a continual deepfake video detection framework, Modality-Specific Frequency Distillation (MSFD), that explicitly decomposes video features into spatial, temporal, and spatiotemporal modalities in the frequency domain. This decomposition enables independent preservation of each modality, as different deepfake video types exhibit varying reliance on spatial and temporal cues across tasks. Furthermore, MSFD adopts a cross-modality decorrelation loss that encourages spatiotemporal representations to remain orthogonal to single-modality cues. Extensive experiments show that our framework achieves stronger adaptation and preserves performance more effectively than state-of-the-art methods across diverse continual deepfake video scenarios.

</details>

---

## Open-set Detection

### 1. A Reverse Sign Language Dictionary: Open-Vocabulary Sign Recognition from Continuous Signing via Video Captioning and Description Retrieval **⭐⭐** (相关度: 20%, 质量: 0.6)

- **arXiv ID**: [2609.03788](https://arxiv.org/abs/2609.03788)  · [📄 PDF](https://arxiv.org/pdf/2609.03788)
- **作者**: Santiago Poveda-Gutiérrez, Hideki Nakayama, Mayumi Bono
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-03 · **分类**: cs.CV, cs.CL
- **摘要（中）**: 针对孤立手语识别局限于封闭词汇表的问题，提出通过视频字幕生成和描述检索实现开放词汇手语识别。该方法将手语片段字幕化为程序性描述，并用多语言编码器检索目标词汇。在日语手语数据集上，微调后top-10检索率从4.5%提升至49%，接近监督分类器性能。
- **摘要（英）**: Addressing closed-set limitations in sign language recognition, this paper proposes open-vocabulary recognition via video captioning and description retrieval, improving top-10 retrieval from 4.5% to 49% after fine-tuning.
- **评估**: 该工作领域特殊，与自动驾驶感知研究无直接关联。
- **核心贡献**: 提出无需词汇表监督的开放词汇手语识别方法。
- **创新点**: 利用视频字幕与描述检索实现开放词汇识别。
- **结果**: 在手语数据集上显著提升检索准确率。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Isolated Sign Language Recognition (ISLR) is conventionally cast as closed-set classification over gloss labels, which cannot generalize to signs unseen in training and ties every deployment to a gloss-annotated lexicon. We instead recognize signs extracted from continuous signing by (1) captioning a sign-level clip into a free-form procedural description of the articulation with an open-weight vision-language model, and (2) retrieving the closest entry from a vocabulary of target descriptions with a multilingual sentence encoder: a reverse sign language dictionary that needs no gloss supervision and admits an open vocabulary. On 1,300 sign-level segments from a Japanese Sign Language (JSL) dialogue corpus annotated with procedural descriptions (against a 2% top-10 chance floor over the 503-entry target vocabulary), fine-tuning the captioner substantially improves seen-class retrieval: language and vision tower fine-tuning raises top-10 retrieval on seen classes from 4.5% (untrained) to 49%, becoming statistically indistinguishable from a standard supervised closed-set classifier (I3D) on two of the three test sets where a closed-set classifier can be evaluated at all. More importantly, unseen-class retrieval also improves significantly over the untrained pipeline (11.5% -> 21.0% top-10, p=0.0094), a regime in which the closed-set classifier cannot participate. A matcher-side empirical upper-bound analysis shows the sentence encoder already recovers close to 100% of paraphrased gold descriptions, locating a gap in captioning quality that we aim to address in future work. To our knowledge this is the first description-based, open-vocabulary sign lookup from continuous signing without gloss supervision, and the first for JSL.

</details>

### 2. SignSeek: Learning Transferable Representations for Sign Dictionary Retrieval **⭐⭐⭐** (相关度: 10%, 质量: 0.75)

- **arXiv ID**: [2609.03695](https://arxiv.org/abs/2609.03695)  · [📄 PDF](https://arxiv.org/pdf/2609.03695)
- **作者**: Sobhan Asasi, Ozge Mercanoglu Sincan, Richard Bowden
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-03 · **分类**: cs.CV
- **摘要（中）**: ①针对手语词典检索中，现有表示学习方法基于闭集识别，无法泛化到开集、跨手语者场景的问题。②提出了SignSeek框架，通过显著性引导的发音器官掩蔽进行对比学习，包括掩蔽对比对齐损失和掩蔽预测损失，以学习跨手语者的同义词表示。③相比现有方法，SignSeek利用发音器官显著性掩蔽增强表示的可迁移性，并在多语言大规模数据上预训练。④在ASL-Citizen、WLASL和NMFs-CSL上实现了跨语料库检索的最新性能，但未提供具体数值。
- **摘要（英）**: This paper addresses the poor generalization of sign representation learning to open-set, signer-independent retrieval by proposing SignSeek, which uses saliency-guided articulator masking with contrastive and masked prediction losses. It aligns same-gloss signs across signers and reconstructs signs from context, pretraining on 266K samples across multiple languages. SignSeek achieves state-of-the-art cross-corpus retrieval on ASL-Citizen, WLASL, and NMFs-CSL.
- **评估**: 该论文专注于手语检索，与自动驾驶感知无关，但自监督对比学习方法有一定通用性。
- **核心贡献**: 提出了SignSeek，一种基于显著性引导掩蔽的自监督手语表示学习方法。
- **创新点**: 利用发音器官显著性掩蔽驱动对比和预测双目标。
- **结果**: 在多个跨语料库检索基准上达到最新性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Sign language dictionaries are essential resources for sign language learners, yet automatically retrieving a sign from a dictionary, given only a query video, remains a challenging problem due to the natural variability between signers. Existing sign representation learning methods are built for closed-set recognition, producing embeddings that do not generalise to the open-set, signer-independent setting that retrieval demands. \textbf{SignSeek} closes this gap by contrastively learning sign representations with saliency-guided articulator masking. A contrastive objective aligns same-gloss signs across signers, while our Articulator Saliency-Guided Masking (ASGM) pinpoints the single most critical articulator per sign. This drives two complementary objectives, a masked contrastive alignment (MAC) loss that sees the sign through a single articulator and a masked prediction (MAP) loss that reconstructs it in latent space from the surrounding spatio-temporal context. Pretrained on 266K samples ($\sim$5,700 glosses) across multiple sign languages, \textbf{SignSeek} sets a new state-of-the-art performance in cross-corpus retrieval on ASL-Citizen, WLASL, and NMFs-CSL without any downstream fine-tuning. Strikingly, it achieves zero-shot generalisation to an entirely unseen British Sign Language (BSL), surpassing methods explicitly trained on BSL, and transfers seamlessly to isolated sign recognition and subtitle alignment, outperforming prior skeleton-based methods.

</details>

---

## Vision Transformer

### 1. ProgResViT: Progressive Resolution and Width for Adaptive Vision Transformers **⭐⭐⭐** (相关度: 45%, 质量: 0.8)

- **arXiv ID**: [2609.03216](https://arxiv.org/abs/2609.03216)  · [📄 PDF](https://arxiv.org/pdf/2609.03216)
- **作者**: Ali Hojjat, Janek Haberer, Olaf Landsiedel
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/ds-kiel/ProgResViT](https://github.com/ds-kiel/ProgResViT)
- **提交日期**: 2026-09-02 · **分类**: cs.CV
- **摘要（中）**: 针对Vision Transformer（ViT）对所有图像使用固定输入分辨率和模型宽度、导致计算浪费的问题，提出ProgResViT，一种输入自适应的ViT。该方法通过多轮渐进推理，首轮使用低分辨率和窄子网络，若预测置信度不足则复用当前表示并升级到更高分辨率和更宽子网络。所有轮次共享单一骨干，并提出Progress-Conditioned Soft Gating（PSG）来根据当前轮次、块和分辨率调节token融合和层输出。在图像分类任务上，ProgResViT相比自适应宽度、深度和动态token基线取得了更好的精度-计算权衡；结合知识蒸馏，DeiT-based ProgResViT达到84.9% top-1准确率，略超DeiT-III-S。
- **摘要（英）**: This paper addresses the inefficiency of Vision Transformers that process all images at fixed resolution and width. It proposes ProgResViT, an input-adaptive ViT that performs progressive inference across rounds, starting with low resolution and narrow subnetwork, and refining with higher resolution and width when confidence is insufficient. With shared backbone and Progress-Conditioned Soft Gating, it achieves better accuracy-compute trade-offs than adaptive-width/depth/token baselines, reaching 84.9% top-1 accuracy with distillation.
- **评估**: 该论文提出渐进式分辨率与宽度的自适应推理方法，对高效ViT设计有参考价值，但与本领域（自动驾驶感知）相关性不高。
- **核心贡献**: 提出ProgResViT，一种输入自适应的渐进分辨率与宽度ViT。
- **创新点**: 通过多轮渐进推理和进度条件软门控实现动态计算分配。
- **结果**: 在图像分类上取得优于多种自适应基线的精度-计算权衡。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision Transformers (ViTs) typically process every image using a fixed input resolution and model width, even though many images can be classified with substantially less computation. We introduce ProgResViT, an input-adaptive ViT that performs inference progressively across multiple rounds. The first round processes a low-resolution image with a narrow subnetwork. Inference terminates when the prediction is sufficiently confident; otherwise, the model reuses the representations produced in the current round and proceeds with a higher-resolution input and a wider subnetwork to refine its prediction. As all rounds share a single backbone, we propose Progress-Conditioned Soft Gating (PSG), which conditions token fusion and layer outputs on the current round, block, and input resolution. On image classification, applying ProgResViT to DeiT yields better accuracy-compute trade-offs than adaptive-width, adaptive-depth, and dynamic-token baselines. With knowledge distillation, a DeiT-based ProgResViT achieves 84.9% top-1 accuracy, slightly exceeding the reported DeiT-III-S accuracy under a comparable evaluation setting. We show that the same design also provides favorable accuracy-compute trade-offs for self-supervised DINO representations and downstream semantic segmentation. Code is available at https://github.com/ds-kiel/ProgResViT.

</details>

---

## Self-supervised Vision

### 1. P-CORE: Self-Supervised Surface Consistency for Point-Based Neural Editing **⭐⭐⭐** (相关度: 50%, 质量: 0.75)

- **arXiv ID**: [2609.03349](https://arxiv.org/abs/2609.03349)  · [📄 PDF](https://arxiv.org/pdf/2609.03349)
- **作者**: Yanshu Zhang, Shichong Peng, Mehran Aghabozorgi et al. (5 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-03 · **分类**: cs.CV, cs.GR
- **摘要（中）**: 针对基于点的神经表示在大变形下出现孔洞和表面不连续的问题，提出一种自监督方法，使点表示适应大变形而无需真实变形几何的多视图图像。核心思想是生成随机变形并确保变形前后预测表面的一致性，即变形点云的表面预测应等于原始点云表面预测的变形。该方法集成到基于注意力的点表示中，利用学习插值核，不同于基于泼溅的方法。
- **摘要（英）**: To address holes and discontinuities in point-based representations under large deformations, a self-supervised method ensures surface consistency before and after random deformations. The deformed point cloud's surface prediction matches the deformation of the original prediction. Integrated into attention-based representations, it adapts to large deformations without ground truth.
- **评估**: 该工作提出新颖的自监督一致性约束，对神经编辑有理论价值，但应用场景较窄。
- **核心贡献**: 提出P-CORE，首个用于点神经编辑的自监督表面一致性方法。
- **创新点**: 利用变形前后表面一致性作为自监督信号。
- **结果**: 有效处理大变形，减少孔洞和不连续。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Advances in neural rendering have enabled high-fidelity multi-view reconstruction of 3D scenes. However, free-form non-rigid shape editing remains a significant challenge. Point-based neural representations are highly desirable for multi-view reconstruction because they lack fixed connectivity, which does not constrain the learned surface topology to that of the initialization. Yet this same property causes point-based representations to struggle with holes and surface discontinuities under large deformations. To address this, we propose a novel self-supervised method to enable point-based representations to adapt to large deformations without requiring ground truth multi-view images of deformed geometry. The key idea is to generate random deformations and to ensure consistency in the predicted surface before and after deformation. In particular, the surface prediction from the deformed point cloud should be the same as the deformation applied to the surface prediction from the original point cloud. We incorporate our approach into attention-based point representations, which differ from splatting-based point representations in their use of a learned interpolation kernel between points as opposed to a Gaussian kernel around each point. This learned interpolation kernel can learn to adapt to large deformations, without requiring addition or removal of points. We show that our framework significantly enhances its robustness to large deformations. Experiments on synthetic geometry editing benchmarks (Neural Editor, Objaverse) demonstrate that our approach outperforms existing point-based methods in zero-shot editing and significantly reduces artifacts. Furthermore, qualitative results on the DTU and Mip-NeRF 360 datasets demonstrate our method's effectiveness on real-world scenes.

</details>

---

## Knowledge Distillation

### 1. CORE: Improving Compositional Reasoning in MLLM Embedding via Reranker Distillation **⭐⭐⭐⭐** (相关度: 75%, 质量: 0.85)

- **arXiv ID**: [2609.04083](https://arxiv.org/abs/2609.04083)  · [📄 PDF](https://arxiv.org/pdf/2609.04083)
- **作者**: Tingyu Song, Mingxin Li, Yanzhao Zhang et al. (8 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-03 · **分类**: cs.CV, cs.AI, cs.CL
- **摘要（中）**: 针对多模态大语言模型嵌入在组合检索中区分属性-对象绑定能力不足的问题，提出CORE，通过将交叉注意力重排器的组合判断蒸馏到嵌入模型。CORE合成覆盖五个组合匹配级别的候选列表，并引入Rank-KL目标训练嵌入模型复现重排器的细粒度排序。在三个组合推理基准上，CORE-RERANKER-8B达到82.7%总平均，优于Jina-Reranker 10.7点，CORE-EMBED-8B在嵌入模型中取得最佳总平均0.666。
- **摘要（英）**: To improve compositional retrieval in MLLM embeddings, CORE distills reranker judgments via synthesized candidate lists and a Rank-KL objective. It trains embeddings to reproduce fine-grained rankings across five matching levels. CORE-RERANKER-8B achieves 82.7% average, outperforming Jina-Reranker by 10.7 points, and CORE-EMBED-8B leads embeddings with 0.666.
- **评估**: 该工作通过蒸馏有效提升嵌入模型的组合推理能力，方法创新且结果显著。
- **核心贡献**: 提出CORE，利用重排器蒸馏增强MLLM嵌入的组合检索。
- **创新点**: 引入Rank-KL列表级目标以复现重排器的细粒度排序。
- **结果**: 在多个基准上显著优于现有嵌入和重排模型。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> MLLM-based embedding models remain limited in compositional retrieval, often failing to distinguish scenes containing the same concepts but different attribute-object bindings. Yet the same backbone can resolve such distinctions when used as a cross-attentive reranker, motivating us to distill its compositional judgments into the embedding model. We propose CORE, which synthesizes candidate lists spanning five compositional matching levels and introduces a Rank-KL objective that trains the embedding model to reproduce the reranker's fine-grained ranking. We further introduce a graded evaluation protocol and compare contrastive learning, pairwise CoSENT, and listwise Rank-KL under the same data and tuning budget. Our comparison shows that both CoSENT and Rank-KL use the multi-level supervision more effectively than contrastive learning, with Rank-KL achieving the strongest overall performance. Across three compositional reasoning benchmarks (COLA, SUGARCREPE++, NEGBENCH), CORE-RERANKER-8B achieves an 82.7% total average, outperforming Jina-Reranker by 10.7 points, while CORE-EMBED-8B achieves the best total average (0.666) among all evaluated embedding models. The improvements transfer to the MCMR benchmark without sacrificing retrieval performance on COCO and Flickr30K.

</details>

---

## Continual Learning

### 1. Neural-Collapse-guided Task-Free Continual Anomaly Detection **⭐⭐⭐⭐** (相关度: 75%, 质量: 0.8)

- **arXiv ID**: [2609.03406](https://arxiv.org/abs/2609.03406)  · [📄 PDF](https://arxiv.org/pdf/2609.03406)
- **作者**: Xiaotong Kong, Chaoyang Song, Ziai Zhou et al. (6 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-03 · **分类**: cs.CV
- **摘要（中）**: ①针对工业异常检测中任务依赖的持续学习假设不现实，数据分布不可预测变化。②提出NC-TFAD，基于神经坍缩的几何驱动框架，冻结预训练骨干，对齐流特征到ETF原型空间，并生成合成异常样本作为辅助锚点。③引入类间类内正则化和FNCC损失，抑制表示漂移，提升正常-异常可分性。④在无任务边界流数据上有效。
- **摘要（英）**: This paper addresses task-free continual anomaly detection under unpredictable distribution shifts. It proposes NC-TFAD, a neural-collapse-inspired framework that aligns features to an ETF prototype space with synthetic anomaly anchors. Inter- and intra-class regularization and FNCC loss suppress drift and improve separability.
- **评估**: 将神经坍缩理论引入持续异常检测，方法新颖且对工业视觉有实际意义。
- **核心贡献**: 提出任务无关持续异常检测框架NC-TFAD。
- **创新点**: 利用神经坍缩几何和合成异常样本实现无任务边界学习。
- **结果**: 在持续异常检测任务中有效抑制漂移并提升性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent years have witnessed growing interest in continual anomaly detection for industrial visual inspection. However, real-world manufacturing environments exhibit unpredictable shifts in data distributions, rendering task-dependent continual learning assumptions impractical. To address this limitation, we formulate industrial anomaly detection as a task-free continual learning problem and propose NC-TFAD, a neural-collapse-inspired, geometry-driven framework for learning from non-stationary data streams without task boundaries. NC-TFAD freezes a pretrained backbone and aligns streaming features to a simplex Equiangular Tight Frame (ETF) prototype space to stabilize representation geometry under non-stationary streams. To satisfy the NC-inspired geometric construction in the absence of real anomalies, we generate synthetic anomaly samples as auxiliary anchors during training. Building on this geometry, we further introduce inter- and intra-class regularization together with a Focal Neural Collapse Contrastive (FNCC) loss to suppress representation drift and improve normal-anomaly separability. Finally, a normal-patch-prototype-guided localization branch constructs calibrated patch-wise deviation maps from normal training samples and fuses them with a weak self-attention prior, producing anomaly heatmaps without pixel-level annotations. Extensive experiments on MVTec AD and VisA show that NC-TFAD consistently outperforms representative task-free continual learning methods adapted from general vision, as well as unified anomaly detection baselines, in both image-level detection and pixel-level localization under the task-free continual learning protocol. These results highlight that geometry-driven modeling offers an effective and robust solution for task-free continual anomaly detection in real-world industrial applications.

</details>

---

## Tracking

### 1. Counting Animals in Camera-Traps Image Sequences without Count Labels: Winning Solution to the iWildCam 2021 Challenge **⭐⭐⭐** (相关度: 65%, 质量: 0.7)

- **arXiv ID**: [2609.03233](https://arxiv.org/abs/2609.03233)  · [📄 PDF](https://arxiv.org/pdf/2609.03233)
- **作者**: Fagner Cunha, Juan G. Colonna, Eulanda M. dos Santos
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/alcunha/iwildcam2021ufam](https://github.com/alcunha/iwildcam2021ufam)
- **提交日期**: 2026-09-03 · **分类**: cs.CV
- **摘要（中）**: ①针对相机陷阱图像序列中无计数标签的动物计数问题，传统多目标跟踪因时间不连续而不可靠。②提出MaxBoxCount方法，结合强物种分类管道和基于MegaDetector检测的简单计数启发式。③无需计数标签训练，利用检测框最大化计数。④赢得iWildCam 2021挑战赛。
- **摘要（英）**: This paper addresses animal counting in camera-trap sequences without count labels. It proposes MaxBoxCount, combining species classification with a detection-based counting heuristic. This approach avoids tracking and won the iWildCam 2021 Challenge.
- **评估**: 解决实际生态监测问题，方法简洁有效，但对自动驾驶感知参考有限。
- **核心贡献**: 提出无标签动物计数方法MaxBoxCount。
- **创新点**: 利用检测框计数启发式替代复杂跟踪。
- **结果**: 在iWildCam 2021挑战赛中获胜。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Camera traps have become an essential tool for wildlife monitoring, motivating the development of computer vision methods for the automated extraction of information from these data. While most prior work has focused on species identification, many ecological applications also require estimating the number of unique individuals appearing across short image sequences. This task is particularly challenging because camera traps typically acquire bursts of images at approximately one frame per second, creating large temporal discontinuities that may make conventional multi-object tracking methods unreliable, and because manually collecting individual count annotations is prohibitively expensive. In this work, we describe the winning solution to the iWildCam 2021 Challenge, which introduced a benchmark for counting animals at the sequence level under realistic annotation constraints where count annotations are unavailable for training. Our approach, MaxBoxCount, combines a strong species classification pipeline with a simple yet effective counting heuristic based on MegaDetector detections to estimate the number of unique individuals without requiring count annotations. Code is available at https://github.com/alcunha/iwildcam2021ufam.

</details>

---

## 📊 统计

| 领域 | 论文数 |
|------|--------|
| VLM | 10 |
| Network Pruning | 6 |
| Multimodal | 6 |
| Multi-camera Perception | 5 |
| Autonomous Driving | 4 |
| Video Understanding | 4 |
| Object Detection | 3 |
| Open-set Detection | 2 |
| Vision Transformer | 1 |
| Self-supervised Vision | 1 |
| Knowledge Distillation | 1 |
| Continual Learning | 1 |
| Tracking | 1 |
| **总计** | **45** |