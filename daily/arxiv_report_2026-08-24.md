# 📚 arXiv 每日论文报告（我的领域）

**报告日期**: 2026-08-24  
**论文来源**: [arXiv cs.CV Recent](https://arxiv.org/list/cs.CV/recent)  
**关注论文数**: 43 篇（其中 43 篇经大模型中文评估）

> 匹配领域: 3D Detection、BEV、Occupancy、Multi-camera Perception、Tracking、Open Vocabulary Detection、FOD Detection、VLM、Vision Transformer、Self-supervised Vision、Video Understanding、Multimodal、Continual Learning、Neural Architecture Search、Network Pruning、Knowledge Distillation

## 📑 目录

- [VLM](#vlm) (10篇)
- [Multimodal](#multimodal) (10篇)
- [Multi-camera Perception](#multi-camera-perception) (6篇)
- [Network Pruning](#network-pruning) (5篇)
- [Video Understanding](#video-understanding) (3篇)
- [Self-supervised Vision](#self-supervised-vision) (3篇)
- [Vision Transformer](#vision-transformer) (2篇)
- [Open Vocabulary Detection](#open-vocabulary-detection) (2篇)
- [Knowledge Distillation](#knowledge-distillation) (1篇)
- [BEV](#bev) (1篇)

## VLM

### 1. Is Visual Prompting All You Need? Studying VLM Spatial Reasoning under Progressive Visual Scaffolds **⭐⭐⭐⭐** (相关度: 85%, 质量: 0.8)

- **arXiv ID**: [2608.21170](https://arxiv.org/abs/2608.21170)  · [📄 PDF](https://arxiv.org/pdf/2608.21170)
- **作者**: Lars Benedikt Kaesberg, Tianyu Yang, Florian Valentin Wunderlich et al. (7 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV, cs.AI
- **摘要（中）**: ①这篇论文针对视觉语言模型（VLM）在空间推理任务中，视觉呈现方式如何影响模型性能和失败模式的问题。②提出了SPaRC基准，通过引入轻量级输入侧脚手架（scaffolds）来保留视觉模态的同时使空间结构更易被模型访问。③相比已有工作，系统性地研究了视觉呈现对VLM空间推理的影响，并发现脚手架能显著提升任务准确率。④实验表明，脚手架在多个VLM上将任务准确率提升了高达34.0个百分点，并进一步补充GRPO训练，额外获得最多4.6个准确率点，且增益与接地错误减少密切相关。
- **摘要（英）**: This paper investigates how visual presentation shapes VLM performance and failure modes in spatial reasoning tasks, introducing the SPaRC benchmark and lightweight input-side scaffolds that preserve visual modality while making spatial structure more accessible. Across multiple VLMs, scaffolds improve task accuracy by up to 34.0 percentage points and complement GRPO-based training with up to 4.6 additional points, with gains tied to reduced grounding errors.
- **评估**: 该论文系统性地揭示了视觉呈现对VLM空间推理的关键影响，为理解VLM的感知与推理边界提供了重要视角，值得关注。
- **核心贡献**: 提出了SPaRC基准和输入侧脚手架方法，量化了视觉呈现对VLM空间推理的影响。
- **创新点**: 通过轻量级输入侧脚手架系统性地研究视觉呈现对VLM空间推理的影响。
- **结果**: 脚手架提升任务准确率高达34.0个百分点，并补充GRPO训练额外获得4.6个准确率点。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-language models (VLMs) have advanced rapidly in multimodal reasoning, yet recent work shows that their failures often reflect an interaction between visual grounding and downstream reasoning. What remains less clear is how the visual presentation of a task shapes model performance and failure modes when the underlying reasoning problem is unchanged. We study this question in SPaRC, a benchmark for grid-based visual spatial planning, by introducing lightweight input-side scaffolds that preserve the visual modality while making spatial structure more accessible. Across multiple VLMs, these scaffolds improve task accuracy over the original visual setting by up to 34.0 percentage points and further complement GRPO-based training, yielding up to 4.6 additional accuracy points compared with near-zero gains on the original visual input. Analyses on both end-to-end task solving and object detection show that these gains are closely tied to reductions in grounding-related errors, while rule reasoning remains comparatively challenging. We find that visual presentation is a central factor that determines whether VLM benchmarks measure grounded perception, downstream reasoning, or a mixture of both.

</details>

### 2. CARD: Diagnosing Belief to Action Routing Failures in Vision Language Models **⭐⭐⭐** (相关度: 70%, 质量: 0.7)

- **arXiv ID**: [2608.20763](https://arxiv.org/abs/2608.20763)  · [📄 PDF](https://arxiv.org/pdf/2608.20763)
- **作者**: Souptik Kumar Majumdar, Fabian Kögel, Andreas Bulling
- **提交日期**: 2026-08-21 · **分类**: cs.CV, cs.AI
- **摘要（中）**: ①这篇论文针对视觉语言模型（VLM）内部表征的信念等心理状态是否被下游预测使用的问题。②提出了Cross-Axis Routing Diagnostic (CARD)方法，通过沿一个轴引导激活，同时测量另一个轴预测的响应，并引入合作网格世界基准Relay Chain。③相比已有工作，CARD能够诊断跨轴路由失败，揭示模型未能将信念表征整合到动作预测中。④实验发现，模型在Relay Chain上存在关键路由失败，未能利用关于合作伙伴的信念信息。
- **摘要（英）**: This paper addresses whether VLM internal representations of mental states like beliefs are used in downstream predictions, proposing CARD to steer activations along one axis while measuring another axis's prediction response on the new Relay Chain benchmark. Applied to open-weight VLMs, it diagnoses a critical routing failure where models fail to incorporate belief representations into next action prediction.
- **评估**: 该论文提供了诊断VLM内部表征与下游预测之间路由关系的新工具，对理解模型行为有参考价值。
- **核心贡献**: 提出了CARD诊断方法和Relay Chain基准，揭示了VLM信念表征到动作预测的路由失败。
- **创新点**: 通过跨轴激活引导诊断VLM内部表征与下游预测的路由关系。
- **结果**: 在Relay Chain上诊断出模型未能利用信念表征进行动作预测的关键失败。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Linear probes and activation steering have uncovered that vision-language models (VLMs) internally represent mental states such as agents' beliefs, knowledge, and intentions. However, it is unclear whether and how these representations are used by downstream predictions along these axes. To close this gap, we introduce Cross-Axis Routing Diagnostic (CARD), which steers activations along one axis while measuring the response of a different axis's prediction. Applied to open-weight VLMs on Relay Chain -- a new cooperative grid-world benchmark we propose -- we diagnose a critical routing failure: models fail to incorporate belief representations into their next action prediction, effectively leaving valuable information about their partners unused.

</details>

### 3. A VLM Answer Is Not an Anomaly Score: Rank Compression in Training-Free Video Anomaly Detection **⭐⭐⭐⭐** (相关度: 70%, 质量: 0.8)

- **arXiv ID**: [2608.21244](https://arxiv.org/abs/2608.21244)  · [📄 PDF](https://arxiv.org/pdf/2608.21244)
- **作者**: Inpyo Song, Jangwon Lee
- **提交日期**: 2026-08-21 · **分类**: cs.CV
- **摘要（中）**: 这篇论文针对训练-free视频异常检测（VAD）中，视觉语言模型（VLM）的答案输出与异常分数排名不一致的问题。作者提出将VLM的答案接口（包括答案尺度和读取规则）视为检测器的一部分，并系统比较了生成式读取（仅用最可能答案）和概率式读取（利用完整分布）两种方式。实验表明，概率式读取在四种7-8B VLM和所有测试组合上均优于生成式读取，平均提升5到13个点，原因是生成式读取导致排名压缩。
- **摘要（英）**: This paper addresses the mismatch between VLM answer outputs and anomaly score rankings in training-free video anomaly detection. It proposes treating the answer interface as part of the detector and compares generated readout versus probability readout, showing the latter consistently outperforms across four VLMs with 5-13 point gains due to avoiding rank compression.
- **评估**: 该论文揭示了VLM在VAD任务中一个被忽视的关键细节，对设计基于VLM的检测器具有重要指导意义。
- **核心贡献**: 核心贡献是提出并验证了概率式读取规则在VLM-based VAD中的优越性，并定义了答案接口概念。
- **创新点**: 创新点在于将答案接口形式化并识别出生成式读取导致的排名压缩问题。
- **结果**: 概率式读取在四个基准-指标对上平均提升5-13点。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-language models enable training-free video anomaly detection by answering questions about video segments. VAD benchmarks, however, require a scalar anomaly score for each segment and evaluate the resulting ranking using the AUROC or AP. A VLM-based detector should therefore define an answer interface: the answer scale specifies the admissible answers, and the readout rule maps the model's output distribution to a score. Because this interface can change the evaluated ranking, it is part of the detector rather than a formatting detail. The generated readout uses only the most likely answer, whereas the probability readout uses the full distribution over admissible answers. Across four 7-8B VLMs, the probability readout outperforms the generated readout for every tested combination of answer scale, benchmark, and metric, with average gains ranging from 5 to 13 points across the four benchmark-metric pairs. The gap arises because the generated readout keeps only one answer value per segment, so segment with different answer distributions can receive the same score and lose their relative order. We call this loss of relative order generated-answer rank compression. Even when the answer scale allows 91 answers, the generated readout produces only 4-18 distinct scores, whereas the probability readout retains substantially finer score resolution. The advantage persists under every decoding strategy, prompt wording, and joint scoring-explanation prompt we test. The answer interface is therefore a consequential component of VLM-based VAD and should be explicitly specified and evaluated.

</details>

### 4. Llama-Mobile: Efficient 2.7-Bit Quantization of VLMs **⭐⭐⭐** (相关度: 60%, 质量: 0.7)

- **arXiv ID**: [2608.21134](https://arxiv.org/abs/2608.21134)  · [📄 PDF](https://arxiv.org/pdf/2608.21134)
- **作者**: Luka Ribar, Jeevan Bhoot, Douglas Orr
- **提交日期**: 2026-08-21 · **分类**: cs.CV, cs.LG
- **摘要（中）**: 这篇论文针对VLM在移动设备上部署时内存和计算需求过大的问题。作者提出一个量化框架，利用模型自身生成训练数据，无需访问原始训练设置，并设计了一种2.7-bit每参数的格式，支持在Arm CPU上高效执行。通过压缩Llama 3.2 11B Vision Instruct模型至3.7 GB（8-bit激活），在标准视觉问答任务上保持了强性能。
- **摘要（英）**: This paper tackles the deployment challenge of VLMs on mobile devices by proposing a quantization framework that generates training data from the model itself and uses a novel 2.7-bit format for Arm CPUs. Compressing Llama 3.2 11B to 3.7 GB preserves strong VQA performance.
- **评估**: 该论文为VLM在资源受限设备上的实际部署提供了实用方案，但创新性相对常规。
- **核心贡献**: 核心贡献是提出无需原始训练数据的VLM量化框架和2.7-bit高效格式。
- **创新点**: 创新点在于利用模型自生成数据训练量化，以及针对Arm CPU的2.7-bit格式设计。
- **结果**: Llama 3.2 11B压缩至3.7 GB，VQA性能保持强。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deploying vision-language models (VLMs) on mobile devices is challenging due to their significant memory and compute requirements. We present a framework for quantizing VLMs for efficient inference on resource-constrained hardware. Our approach combines a quantization pipeline that uses the model itself to generate training data and does not require access to the training setup, with a novel 2.7-bit-per-parameter format supporting efficient execution on Arm CPUs. We validate our approach by compressing the Llama 3.2 11B Vision Instruct model to 3.7 GB with 8-bit activations, preserving strong performance on a set of standard visual question answering tasks.

</details>

### 5. Re$^3$Cap: Retrieval-Guided Refinement for Image Captioning Enhancement via Reinforcement Learning **⭐⭐⭐** (相关度: 50%, 质量: 0.75)

- **arXiv ID**: [2608.21305](https://arxiv.org/abs/2608.21305)  · [📄 PDF](https://arxiv.org/pdf/2608.21305)
- **作者**: Haonan Jia, Shichao Dong, Zenghui Sun et al. (10 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV, cs.AI
- **摘要（中）**: 这篇论文针对强化学习（RL）在图像描述中难以鼓励LVLM探索新推理策略的问题。作者提出Re$^3$Cap，一种检索引导的推理策略，通过多模态检索作为描述细化的推理信号，无需额外标注。该方法包含描述细化建议器（CRS）和质量评估器（CQA），识别幻觉和遗漏，生成更准确的描述。在COCO-LN500基准上，Re$^3$Cap在关系推理上平均比GRPO提升8.64%。
- **摘要（英）**: This paper addresses RL's limitation in encouraging LVLMs to explore novel reasoning for image captioning. Re$^3$Cap uses multimodal retrieval as a reasoning signal for refinement, outperforming GRPO by 8.64% on relation reasoning in COCO-LN500.
- **评估**: 该论文将检索引入RL训练，为图像描述增强提供了新思路，但领域相关性较低。
- **核心贡献**: 核心贡献是提出检索引导的RL策略，无需额外标注即可增强图像描述。
- **创新点**: 创新点在于利用多模态检索作为推理信号，结合CRS和CQA进行细化。
- **结果**: 在COCO-LN500上关系推理平均提升8.64%。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Reinforcement Learning (RL) has demonstrated significant gains in image captioning, yet it is still limited in encouraging Large Vision-Language Models (LVLMs) to explore novel reasoning strategies. This limitation leads to a performance gap between RL and Supervised Fine-Tuning (SFT). In this paper, we argue that multi-modal retrieval can serve as an effective reasoning signal for caption refinement. Based on this insight, we present the Retrieval-Guided Refinement for Image Captioning (Re$^3$Cap), a retrieval-guided reasoning strategy that enhances image captioning without requiring additional annotations. Instantiated by Caption Refinement Suggester (CRS) and Caption Quality Assessor (CQA), this strategy identifies hallucinations and omissions in image captions, leading to more accurate and detailed descriptions. Extensive experiments demonstrate the superiority of our method in image captioning, even compared with Supervised Fine-Tuning. Especially, Re$^3$Cap outperforms GRPO with an average improvement of 8.64% in relation reasoning on the COCO-LN500 benchmark.

</details>

### 6. Toward Vision Language Model-based Assessment of Clinical Quality and Usability of LGE-MR Images for Cardiac Ablation Planning **⭐⭐⭐** (相关度: 40%, 质量: 0.7)

- **arXiv ID**: [2608.21180](https://arxiv.org/abs/2608.21180)  · [📄 PDF](https://arxiv.org/pdf/2608.21180)
- **作者**: Bipasha Kundu, Abhishek Chaturvedi, Axel W. E. Wismueller et al. (5 authors)
- **提交日期**: 2026-08-21 · **分类**: eess.IV, cs.CV
- **摘要（中）**: 这篇论文针对LGE心脏MRI图像质量评估中缺乏可解释临床推理的问题。作者提出一个两阶段VLM框架，用于左心房LGE-MRI的临床接地质量评估，以支持房颤消融规划。该框架旨在自动化判断扫描是否达到最低质量阈值，并提供可解释的临床推理，克服手动评估的主观性和现有自动化方法的不可解释性。
- **摘要（英）**: This paper addresses the lack of interpretable clinical reasoning in LGE-MRI quality assessment for ablation planning. It proposes a two-stage VLM framework for clinically grounded IQA, automating threshold decisions with explainable reasoning.
- **评估**: 该论文将VLM应用于医学影像质量评估，具有临床价值，但领域与自动驾驶感知相关性低。
- **核心贡献**: 核心贡献是提出两阶段VLM框架，用于LGE-MRI的临床可解释质量评估。
- **创新点**: 创新点在于将VLM用于安全关键的IQA任务，提供可解释输出。
- **结果**: 框架设计用于自动化质量阈值判断，具体性能未在摘要中给出。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> LGE cardiac MRI is widely used for left atrial fibrosis assessment and ablation planning in atrial fibrillation patients as knowledge of fibrotic tissue regions identified from LGE-MRI is critical for catheter ablation. Often, poor quality images used during ablation planning can cause mis-localization of ablation targets, directly impacting procedure safety and outcome. The decision of whether a scan meets the minimum quality threshold for ablation planning is currently made informally by the reviewing radiologist and is not captured by any automated system, yet it is arguably the most safety-critical output of the image quality assessment (IQA) process. However, variations in image quality caused by noise, motion artifacts, and poor boundary definition significantly compromise the reliability of downstream segmentation and clinical decision-making tasks. Manual quality assessment by expert radiologists is subjective and difficult to scale, while existing automated methods produce scalar scores without interpretable clinical reasoning. In this work, we propose a two-stage vision language model (VLM) framework for clinically grounded image quality assessment of left atrial LGE-MRI. In the first stage, a fine-tuned VLM generates structured radiology-style quality reports predicting five radiologist-defined criteria: Noise, Motion Artifact, LA Boundary Accuracy, PV Region Accuracy, and Under-segmentation Severity. In the second stage, a GPT-based reasoning module maps the predicted quality and reports to a structured quality scores and binary clinical usability decision for ablation planning. We curate a dataset of 60 annotated image slice-text pairs from 20 patients and benchmark four state-of-the-art VLM architectures. InternVL2 achieves the highest criterion-level accuracy (Avg ACC=0.65, PLCC=0.79), while DeepSeek achieves perfect clinical usability agreement (Acc=1.00, kappa=1.00).

</details>

### 7. COMET: Contrastive Motion-Enhanced Temporal Reasoning for Video Multimodal Large Language Models **⭐⭐⭐⭐** (相关度: 75%, 质量: 0.8)

- **arXiv ID**: [2608.21030](https://arxiv.org/abs/2608.21030)  · [📄 PDF](https://arxiv.org/pdf/2608.21030)
- **作者**: Chenghua Zhu, Zhaolu Kang, Qifan Shi et al. (11 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV, cs.CL, cs.LG
- **摘要（中）**: 这篇论文针对视频多模态大模型中细粒度运动-时间理解脆弱的问题。作者提出COMET，一个时间接地框架，通过显式时间表示（基于泰勒帧差分的运动分支）、外观-运动融合（时间注意力偏置增强的交叉注意力）和方向感知优化（时间先验蒸馏和正反向TC-GRPO）来系统增强视频MLLM。在Qwen3-VL-8B上，动作中心任务（STAR, SSv2）平均提升4.9%。
- **摘要（英）**: This paper addresses fragile motion-temporal understanding in video MLLMs. COMET introduces explicit temporal representation, appearance-motion fusion, and direction-aware optimization, improving action-centric tasks by 4.9% on Qwen3-VL-8B.
- **评估**: 该论文针对视频理解中的关键瓶颈，提出了系统性的时间建模框架，对自动驾驶场景理解有潜在价值。
- **核心贡献**: 核心贡献是提出COMET框架，通过完整时间建模流程增强视频MLLM的运动-时间理解。
- **创新点**: 创新点在于结合泰勒差分、时间注意力偏置和正反向TC-GRPO优化。
- **结果**: 在Qwen3-VL-8B上，STAR和SSv2平均提升4.9%。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Video multimodal large language models have advanced significantly, yet fine-grained motion-temporal understanding remains fragile. The core bottleneck is not only sparse frame sampling, but also the lack of a complete temporal modeling pipeline for explicitly representing frame-to-frame change, enabling appearance-motion interaction, and optimizing temporal direction sensitivity. We propose COMET, a temporally grounded framework that systematically strengthens video MLLMs through explicit temporal representation, appearance-motion fusion, and direction-aware optimization. Architecturally, COMET introduces a temporal motion branch built on Taylor frame differences and injects its motion evidence into the appearance stream via temporal attention bias-enhanced cross-attention. For optimization, COMET combines temporal prior distillation with a forward-reverse TC-GRPO stage that turns temporal order into a direct learning signal and strengthens the model's use of directional motion patterns encoded by the temporal motion branch. The method achieves consistent overall improvements with a pronounced motion-temporal bias: on Qwen3-VL-8B, action-centric tasks (STAR, SSv2) improve by 4.9% on average, temporal reasoning tasks (NExT-QA, CLEVRER, LLaVA-178K) by 2.1% over BL-GRPO, while static perception tasks (PerceptionTest) remain on par. The same gain pattern also transfers to InternVL2.5-8B, indicating that COMET generalizes across model families.

</details>

### 8. A Modular Agent for Reliable and Auditable Spatial Relation Verification in CT Scans **⭐⭐⭐** (相关度: 60%, 质量: 0.65)

- **arXiv ID**: [2608.21140](https://arxiv.org/abs/2608.21140)  · [📄 PDF](https://arxiv.org/pdf/2608.21140)
- **作者**: Simon Vincent Abel, Heiko Hillenhagen, Michael Götz et al. (6 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV, cs.AI
- **摘要（中）**: ①针对医学视觉语言模型在CT切片空间关系验证中可靠性不足的问题。②提出模块化医学影像智能体，将任务分解为语言解析、解剖定位和确定性几何验证三个阶段，使用YOLO检测器定位器官，并通过几何规则计算空间关系。③相比端到端VLM，该方法通过显式分解和确定性验证提高了可审计性和可靠性。④在MIRP空间QA数据集上验证了有效性，但摘要未提供具体数值。
- **摘要（英）**: This paper tackles unreliable spatial reasoning in medical VLMs by introducing a modular agent that decomposes spatial relation verification into parsing, YOLO-based localization, and deterministic geometric verification. It enhances reliability and auditability over end-to-end approaches, with evaluation on the MIRP benchmark.
- **评估**: 模块化设计提升可解释性，对医学影像分析有参考价值，但领域较窄。
- **核心贡献**: 提出模块化智能体用于CT空间关系验证，提升可靠性和可审计性。
- **创新点**: 将空间推理分解为显式阶段，结合确定性几何规则。
- **结果**: 在MIRP空间QA上验证有效，但具体指标未给出。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Reliable spatial understanding is an important prerequisite for future medical vision-language systems that aim to support radiological report generation and structured image understanding. While modern vision-language models (VLMs) show promising performance on many medical imaging tasks, recent evidence suggests they remain weak in controlled spatial reasoning and often fail to reliably ground spatial relations in image evidence. Given that radiological reasoning hinges on understanding the relative positions of anatomical structures and findings, this spatial weakness poses risks to diagnostic accuracy. We present a modular medical imaging agent for binary spatial relation verification in axial CT slices. Instead of directly predicting spatial answers end-to-end, the system decomposes the task into explicit stages: language parsing, anatomical localization, and deterministic geometric verification. Natural-language queries are converted into structured relation tuples, queried organs are localized with a YOLO-based detector, and the final spatial decision is computed from object centers using deterministic geometric rules. We evaluate the approach on the held-out MIRP spatial QA benchmark and compare it against representative end-to-end VLM baselines. The best-performing hybrid configuration reaches 94.1% accuracy and 94.2% F1, outperforming direct Qwen2-VL prompting by 42.5 percentage points in accuracy, while preserving interpretable intermediate representations and auditable reasoning stages. The results suggest that explicit modular spatial verification can serve as a promising building block for future report-oriented medical imaging agents.

</details>

### 9. ArtiMo: Agent-Driven Articulated Mesh Animation **⭐⭐** (相关度: 30%, 质量: 0.5)

- **arXiv ID**: [2608.20699](https://arxiv.org/abs/2608.20699)  · [📄 PDF](https://arxiv.org/pdf/2608.20699)
- **作者**: Chunyu Zou, Peng Dai, Yi-Hua Huang et al. (7 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV
- **摘要（中）**: ①针对文本驱动的铰接式3D网格动画中运动约束和因果交互建模困难的问题。②提出ArtiMo，一个基于LLM/VLM的智能体框架，利用URDF的显式运动学约束和智能体推理能力，零样本生成动画，并通过视觉自改进机制迭代修正错误。③相比现有数据驱动方法，无需微调即可处理任意铰接物体。④贡献了覆盖21类物体的新基准数据集，但摘要未提供具体性能数据。
- **摘要（英）**: This paper addresses text-driven articulated mesh animation by proposing ArtiMo, an agent-driven framework using LLMs/VLMs and URDF kinematic constraints for zero-shot motion generation, with a visual self-improvement mechanism. It avoids fine-tuning and introduces a 21-category benchmark, though quantitative results are omitted.
- **评估**: 创新性尚可，但与自动驾驶感知领域相关性低，且实验证据不足。
- **核心贡献**: 提出零样本智能体框架ArtiMo用于铰接网格动画。
- **创新点**: 结合URDF约束和VLM推理实现无需微调的动画生成。
- **结果**: 提供新基准，但性能数据未明确。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Animating articulated 3D meshes via text requires satisfying strict kinematic constraints, modeling causal interactions between parts, and achieving instruction fidelity. Due to the absence of task-specific training data and explicit articulation supervision, existing data-driven mesh animation methods are largely inapplicable to this setting. To address this, we propose ArtiMo, a novel agent-driven framework for text-guided articulated mesh animation. Operating in a zero-shot manner, ArtiMo develops an agentic pipeline powered by Large Language and Vision-Language Models (LLMs/VLMs) to orchestrate motion generation. By synergizing the explicit kinematic constraints of URDF with the agent's reasoning and planning capabilities, it effectively produces causally coherent part motions and interactions without requiring model fine-tuning. To ensure motion correctness, the agent additionally utilizes a visual self-improvement mechanism: generated animations are rendered into compact keyframes and motion cues, enabling the VLM to iteratively diagnose and correct errors. Furthermore, we contribute a new benchmark dataset spanning 21 articulated object categories, featuring high-quality motion annotations enriched with causal relationships. Extensive experiments demonstrate that ArtiMo significantly outperforms baselines, particularly on complex, causally driven motions. The project page is available at https://zou-2004.github.io/ArtiMo/.

</details>

### 10. Latent Ordinal Evidence, Misaligned Outputs: Inference-Time Ordinal Lens Alignment for Multimodal LLMs **⭐⭐⭐⭐** (相关度: 80%, 质量: 0.7)

- **arXiv ID**: [2608.20999](https://arxiv.org/abs/2608.20999)  · [📄 PDF](https://arxiv.org/pdf/2608.20999)
- **作者**: Haiming Li, Yingsheng Liu, Jingmin Zhu et al. (8 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV
- **摘要（中）**: ①针对多模态大语言模型在序数回归任务中内部序数证据与输出不对齐的问题。②提出序数透镜对齐（OLA），一种冻结骨干的推理时方法，在解码器中间层训练轻量透镜，融合为序数分布并修正数字token logits。③相比LoRA微调方法，OLA在保持模型冻结的同时提升性能，且发现unembedding矩阵过滤序数方向。④在四个基准和四个MLLM骨干上，OLA优于SOTA的OrderChain基线，但摘要未提供具体数值。
- **摘要（英）**: This paper addresses misalignment between internal ordinal evidence and digit-token outputs in multimodal LLMs, proposing Ordinal Lens Alignment (OLA), a frozen-backbone inference-time method that trains lightweight lenses on decoder layers to correct logits. OLA outperforms LoRA-tuned baselines across four benchmarks while keeping the model frozen.
- **评估**: 针对MLLM序数推理的独特问题提出高效解决方案，对多模态感知有参考价值。
- **核心贡献**: 提出OLA方法，改善MLLM序数回归的推理时对齐。
- **创新点**: 利用中间层透镜融合序数分布，无需微调。
- **结果**: 在多数设置下优于SOTA基线。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal LLMs apply the language model interface to visual inputs, where ordinal regression tasks such as age estimation, image quality assessment, and disease grading require autoregressive decisions over ordered class labels. We ask whether MLLMs reliably convert internal ordinal evidence into ordered digit-token outputs. Across four ordinal benchmarks and four MLLM backbones, ordinal labels are linearly recoverable from hidden states with Spearman correlation up to 0.938, and a task-designed prompt further sharpens this structure. Yet native digit-token outputs weakly expose it: the unembedding matrix filters the ordinal direction, and the digit-token row space retains below 1.15% across all 16 model-dataset combinations, with a 16 to 77 absolute-point accuracy gap between linear-probe and native outputs. We introduce Ordinal Lens Alignment (OLA), a frozen-backbone inference-time method that trains lightweight W_S-anchored lenses on mid-to-deep decoder layers, fuses them into an ordinal distribution, and corrects only digit-token logits at generation. OLA outperforms the SOTA LoRA-tuned OrderChain baseline in most settings while keeping the MLLM frozen, surpasses discriminative ordinal baselines in most cells, and improves over an offline lens in every setting.

</details>

---

## Multimodal

### 1. A Collaborative Multi-Modality Interaction for VLA-based End-to-End Autonomous Driving **⭐⭐⭐⭐** (相关度: 95%, 质量: 0.8)

- **arXiv ID**: [2608.20890](https://arxiv.org/abs/2608.20890)  · [📄 PDF](https://arxiv.org/pdf/2608.20890)
- **作者**: Jingtao Sun, Xiaohai He, Yike Zhang et al. (7 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV, cs.RO
- **摘要（中）**: ①这篇论文针对现有VLA模型在端到端自动驾驶中将任务视为视觉问答，导致决策推理不可靠且缺乏可解释性，以及跨异构传感器多模态交互不足的问题。②提出了一个基于VLA的端到端自动驾驶系统，包含亲和引导最优传输用于主辅模态双向交互、分布一致模态迁移用于异构模态分布迁移和跨模态交互、以及多模态多轨迹规划与感知导向轨迹优化。③相比已有工作，该方法增强了多模态交互和轨迹规划，提高了决策的可靠性和可解释性。④实验表明，该方法在长尾驾驶场景中实现了更可靠、可解释和更安全的驾驶决策。
- **摘要（英）**: This paper addresses unreliable and less interpretable decision reasoning in VLA-based autonomous driving by proposing a robust system with affinity-guided optimal transport for main-auxiliary modality interaction, distribution-consistent modality transfer, and multi-modal multi-trajectory planning with perception-oriented refinement. It enhances multi-modal interaction and trajectory planning, leading to more reliable, interpretable, and safer driving decisions in long-tail scenarios.
- **评估**: 该论文针对VLA自动驾驶中的多模态交互和规划问题提出了系统化解决方案，对自动驾驶感知与决策研究有较高价值。
- **核心贡献**: 提出了一个结合多模态交互与多轨迹规划的VLA端到端自动驾驶系统。
- **创新点**: 通过亲和引导最优传输和分布一致模态迁移实现高效多模态交互。
- **结果**: 在长尾驾驶场景中实现了更可靠、可解释和更安全的驾驶决策。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-Language-Action (VLA) models have emerged as a powerful paradigm for end-to-end autonomous driving by jointly integrating perception, reasoning, and decision making within a unified multimodal framework. However, most existing VLA models formulate end-to-end autonomous driving as a visual question answering task, leading to unreliable and less interpretable decision reasoning. In addition, they fail to establish effective multi-modal interaction across heterogeneous sensors, thereby limiting robust scene perception and reliable driving reasoning in long-tail driving scenarios. To this end, we propose a robust VLA-based end-to-end autonomous driving system that combines multi-modality interaction with multi-trajectory planning and optimization, enabling more reliable, interpretable, and safer driving decisions. Our method comprises three core components: (1) Affinity-Guided Optimal Transport for main-auxiliary modality two-way interaction; (2) Distribution-Consistent Modality Transfer for heterogeneous modality distribution transfer and cross-modal interaction; (3) Multi-modal Multi-Trajectory Planning along with Perception-Oriented Trajectory Refinement for better driving decisions to long-tail driving scenarios. Experimental results in open-loop and closed-loop datasets demonstrate improvements in safety long-horizon driving reasoning and road scene perception over existing driving systems, highlighting the ability of our mutli-modality interaction and multi-trajectory planning and optimization for scalable VLA-based systems.

</details>

### 2. SuppreSensing: Expert-Guided Feature Recalibration and Discrepancy Augmentation for Multimodal Object Detection **⭐⭐⭐⭐** (相关度: 85%, 质量: 0.85)

- **arXiv ID**: [2608.20944](https://arxiv.org/abs/2608.20944)  · [📄 PDF](https://arxiv.org/pdf/2608.20944)
- **作者**: Xin Wu, Zhenyu Gao, Qiankun Zhang et al. (4 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV
- **摘要（中）**: 这篇论文针对遥感多模态目标检测中语义异质性和模态特定噪声干扰的问题。作者提出SuppreSensing，将多模态融合重构为选择性协作过程，包含专家驱动的多模态特征重校准（EMFR）模块和模态特定属性增强策略，以及专家驱动的定制特征净化（ECFP）模块。在DroneVehicle和VEDAI数据集上达到最先进检测性能，并验证了跨域评估。
- **摘要（英）**: This paper addresses semantic heterogeneity and modality-specific noise in remote sensing multimodal detection. SuppreSensing reformulates fusion as selective collaboration with expert-driven recalibration and discrepancy augmentation, achieving SOTA on DroneVehicle and VEDAI.
- **评估**: 该方法在多模态融合中引入专家机制，有效缓解了对称陷阱和异质性，对遥感感知有显著价值。
- **核心贡献**: 核心贡献是提出专家引导的特征重校准和差异增强的多模态融合框架。
- **创新点**: 创新点在于将融合过程建模为输入自适应的多专家选择，并设计双向差异增强。
- **结果**: 在DroneVehicle和VEDAI上达到SOTA性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal object detection in remote sensing faces challenges due to semantic heterogeneity and modality-specific noise interference. To this end, we propose SuppreSensing, which reformulates multimodal fusion as a selective collaboration process that jointly models shared information and modality-specific cues. SuppreSensing first designs an Expert-driven Multimodal Feature Recalibration (EMFR) module, which reformulates shared-consensus extraction as an input-adaptive multi-expert selection process to alleviate the symmetry trap in multimodal fusion. Complementing this, a modality-specific attribute augmentation strategy is employed to enhance specific modality features by modeling bidirectional discrepancy patterns, mitigating cross-modal heterogeneity. Furthermore, we propose an Expert-driven Customized Feature Purification (ECFP) module based on a "specialized inspection-comprehensive analysis-diagnostic update" physical examination paradigm to iteratively filter redundancies and reinforce task-relevant semantics. Extensive experiments on the DroneVehicle and VEDAI datasets demonstrate that SuppreSensing achieves state-of-the-art detection performance. Cross-domain evaluations on natural scene datasets (FLIR and LLVIP) further validate its superior robustness and generalization capability across diverse environmental conditions.

</details>

### 3. VT-MUSE: Multimodal Unified Sequential Visuotactile Representation Learning for Manipulation **⭐⭐⭐⭐** (相关度: 70%, 质量: 0.85)

- **arXiv ID**: [2608.21290](https://arxiv.org/abs/2608.21290)  · [📄 PDF](https://arxiv.org/pdf/2608.21290)
- **作者**: Congsheng Xu, Qiaochu Yang, Fangyuan Shi et al. (10 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.RO, cs.CV
- **摘要（中）**: ①针对视觉-触觉操作中现有方法独立编码视觉和触觉观测、难以捕捉细粒度跨模态依赖，且忽略接触的时间演化的问题。②提出了VT-MUSE，一个两阶段表示学习框架：第一阶段通过跨模态时间对齐和掩码视图一致性联合适应模态特定编码器；第二阶段使用条件变分潜变量模型处理掩码视觉序列和完整触觉历史，并通过辅助解码器重建掩码视觉观测和预测触觉深度变化。③相比已有工作，改进点在于同时建模跨模态依赖和时间演化，并通过门控交叉注意力将学习到的表示集成到轻量级Transformer策略中。④在仿真基准上，VT-MUSE在所有任务上比最强基线平均高出11个百分点。
- **摘要（英）**: This paper addresses the limitations of existing visuotactile manipulation methods that encode visual and tactile observations independently and overlook temporal evolution. It proposes VT-MUSE, a two-stage representation learning framework with cross-modal temporal alignment and conditional variational latent modeling, integrated into a lightweight Transformer policy via gated cross-attention. VT-MUSE outperforms the strongest baseline by 11 percentage points on average across all tasks in simulation.
- **评估**: 该论文在机器人操作领域具有重要价值，其两阶段框架和门控交叉注意力设计为多模态表示学习提供了新思路，实验结果显著。
- **核心贡献**: 提出了VT-MUSE，一个统一的多模态序列表示学习框架，有效融合视觉和触觉信息并建模时间演化。
- **创新点**: 通过条件变分潜变量模型和辅助解码器，联合建模跨模态依赖和接触动态。
- **结果**: 在仿真基准上平均性能提升11个百分点。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose VT-MUSE, a Multimodal Unified SEquential representation learning framework for visuotactilemanipulation. Existing approaches often encode visual and tactile observations independently before fusion, limiting their ability to capture fine-grained cross-modal dependencies. Moreover, most methods focus on observations at the current time step and overlook the temporal evolution of contact. VT-MUSE addresses both limitations through a two-stage representation learning framework. In Stage I, modality specific encoders are jointly adapted via cross-modal temporal alignment and masked-view consistency. In Stage II, a conditional variational latent model processes masked visual sequences together with full tactile histories. Auxiliary decoders reconstruct the masked recent visual observations and predict tactile depth changes, encouraging the latent representation to retain both global visual context and local contact dynamics. The learned representation is subsequently integrated into a lightweight Transformer policy through gated cross-attention. On the simulation benchmark, VT-MUSE outperforms the strongest baseline evaluated on all tasks by 11 percentage points and also achieves substantial improvements in real-world experiments.

</details>

### 4. Masking Is Not Enough: Generative Restoration for Multimodal De-Identification in Medical AI **⭐⭐⭐** (相关度: 60%, 质量: 0.75)

- **arXiv ID**: [2608.21133](https://arxiv.org/abs/2608.21133)  · [📄 PDF](https://arxiv.org/pdf/2608.21133)
- **作者**: Shiva Shrestha, Zongxing Xie, Chen Zhao et al. (6 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV, cs.CR
- **摘要（中）**: ①针对医疗图像-文本数据中可见图像内容和伴随文本可能暴露受保护健康信息（PHI），而现有去标识方法常与下游推理分离评估的问题。②提出了ClinX，一个端到端的多模态PHI净化框架，使用OCR检测可见标识符、构建二进制PHI掩码，并应用ClinX-PRISM（无跳跃连接的生成式恢复模块）抑制烧录标识符；文本侧通过渐进式去标识级别（正则掩码、上下文感知掩码、重写净化）减少PHI。③改进点在于联合处理图像和文本侧PHI，并在医学视觉问答（MedVQA）中同时评估PHI泄漏和下游效用。④在MedVQA评估中，ClinX在图像侧、文本侧和组合去标识下均有效减少PHI泄漏，同时保持下游任务性能。
- **摘要（英）**: This paper addresses the risk of protected health information (PHI) leakage in medical image-text data and the separate evaluation of de-identification from downstream reasoning. It proposes ClinX, an end-to-end multimodal PHI sanitization framework with OCR-based detection, generative restoration, and progressive text de-identification, evaluated in MedVQA for both PHI leakage and utility. ClinX effectively reduces PHI leakage while maintaining downstream task performance.
- **评估**: 该论文针对医疗AI隐私保护提供了实用框架，但创新性一般，评估范围有限。
- **核心贡献**: 提出了ClinX，一个端到端的多模态PHI净化框架，联合处理图像和文本侧隐私。
- **创新点**: 引入无跳跃连接的生成式恢复模块ClinX-PRISM用于烧录标识符抑制。
- **结果**: 在MedVQA中有效减少PHI泄漏并保持下游效用。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Medical image-text data can expose protected health information (PHI) through both visible image content as well as accompanying text, creating a barrier to privacy-preserving medical AI systems. This risk is especially prominent in multimodal systems, where images, questions, reports, and clinical context may enter training, evaluation, or inference pipelines. Existing medical vision-language benchmarks primarily emphasize task utility, while de-identification methods are often evaluated separately from downstream reasoning. We introduce ClinX, an end-to-end multimodal PHI sanitization framework for medical image-text data. ClinX detects visible identifiers with optical character recognition (OCR), constructs binary PHI masks, and applies ClinX-PRISM, a no-skip generative restoration module with privacy-oriented post-processing for burned-in identifier suppression. In parallel, text-side PHI is reduced through progressive de-identification levels: regex masking, context-aware masking, and rewrite-based sanitization. We evaluate ClinX in medical visual question answering (MedVQA), jointly measuring PHI leakage and downstream utility across image-side, text-side, and combined de-identification settings. Results show that OCR-only masking is not sufficient as a standalone solution, and restoration-based sanitization better preserves clinically relevant visual context while sharply reducing recoverable PHI.

</details>

### 5. A2DINOv3: Rethinking Multi-Modal Object Detection via Socialized Collaboration **⭐⭐⭐⭐** (相关度: 85%, 质量: 0.8)

- **arXiv ID**: [2608.21099](https://arxiv.org/abs/2608.21099)  · [📄 PDF](https://arxiv.org/pdf/2608.21099)
- **作者**: Jiekang Feng, Zhihe Fan, Yunqi Zhu et al. (8 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV, cs.AI
- **摘要（中）**: ①针对多模态目标检测中现有密集跨模态融合策略强制异构模态交互，可能引入冗余信息并破坏预训练表示的问题。②提出了A2DINOv3，一个多专家协作框架，采用社会化协作协议（SCP），将RGB和红外分支建模为异构专家，独立保留专业知识，同时通过选择性约束交互交换互补信息；并引入零初始化策略逐步激活跨模态协作。③改进点在于从社会化学习视角重新审视多模态融合，减少有害跨模态干扰，防止预训练先验退化。④在低光照和恶劣环境下的多模态目标检测任务中，A2DINOv3显著提升了性能，具体数据未在摘要中给出。
- **摘要（英）**: This paper addresses the issue of harmful cross-modal interference in dense fusion strategies for multi-modal object detection. It proposes A2DINOv3, a multi-expert collaboration framework with a Socialized Collaboration Protocol (SCP), where RGB and infrared branches preserve specialized knowledge while exchanging complementary information selectively, using zero-initialization for gradual activation. A2DINOv3 improves detection performance in challenging conditions, though specific metrics are not provided in the abstract.
- **评估**: 该论文为多模态检测提供了新颖的融合视角，与自动驾驶感知高度相关，但实验细节需进一步验证。
- **核心贡献**: 提出了A2DINOv3，一个基于社会化协作协议的多专家融合框架，适配DINOv3。
- **创新点**: 通过选择性约束交互和零初始化策略，减少跨模态干扰并保持预训练表示。
- **结果**: 在低光照和恶劣环境下提升了多模态目标检测性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-modal object detection is essential for robust scene understanding in challenging conditions, including low-light and adverse environments. Recent vision foundation models (e.g., DINOv3) have exhibited strong representation capabilities, yet adapting them to multi-modal scenarios remains challenging. Existing dense cross-modal fusion strategies often force heterogeneous modalities to interact indiscriminately, which may introduce redundant information and disrupt the valuable pre-trained representations. To address this issue, we revisit multi-modal fusion from the perspective of socialized learning and propose adapter to DINOv3 (A2DINOv3), a multi-expert collaboration framework with a Socialized Collaboration Protocol (SCP). Specifically, RGB and infrared branches are modeled as heterogeneous experts that independently preserve their specialized knowledge while exchanging complementary information through selective and constrained interactions. This design mitigates harmful cross-modal interference and prevents degradation of pre-trained priors during adaptation. Furthermore, a zero-initialization strategy is introduced to gradually activate cross-modal collaboration, enabling a smooth transition from modality-specific learning to cooperative representation learning. Extensive experiments on four multi-modal benchmarks, including aerial detection (GAIIC), autonomous driving (FLIR), low-light surveillance (LLVIP), and diverse real-world scenarios (M3FD), demonstrate that A2DINOv3 consistently achieves state-of-the-art performance in multi-modal object detection.

</details>

### 6. Kinematic Knowledge Maps for Pattern Alignment: Structured Latent Representational Learning in Multimodal Gait Analysis **⭐⭐⭐** (相关度: 50%, 质量: 0.7)

- **arXiv ID**: [2608.20969](https://arxiv.org/abs/2608.20969)  · [📄 PDF](https://arxiv.org/pdf/2608.20969)
- **作者**: Chen Dong, He Zonglin, Cheung Kenneth M. C
- **提交日期**: 2026-08-21 · **分类**: cs.CV
- **摘要（中）**: ①针对多模态临床AI中弱对齐输入和缺乏领域特定可解释表示的问题，特别是在从密集视频流、结构化时间序列和模板化运动学文本学习时。②提出了ScoliDetect，一个用于青少年特发性脊柱侧弯筛查的可解释框架，基于运动学知识图（KKM）和模板化运动学文本，通过双向交叉注意力与潜在瓶颈聚合集成视频、KKM和文本。③改进点在于KKM提供固定索引的结构化表示，支持锚定参考的多模态融合和因子级解释。④在多中心队列（n=1,858）中，KKM介导的多模态融合优于单模态模型和晚期拼接，具体性能数据未在摘要中给出。
- **摘要（英）**: This paper addresses weakly aligned inputs and lack of interpretable representations in multimodal clinical AI. It proposes ScoliDetect, an explainable framework with a kinematic knowledge map (KKM) and template-based text, integrated via bidirectional cross-attention with latent-bottleneck aggregation. In a multicenter cohort, KKM-mediated fusion outperforms unimodal models and late concatenation.
- **评估**: 该论文在医疗筛查领域有应用价值，但方法复杂度高，泛化性需进一步验证。
- **核心贡献**: 提出了ScoliDetect，一个基于运动学知识图的可解释多模态融合框架。
- **创新点**: 引入固定索引的KKM结构，支持因子级解释和锚定融合。
- **结果**: 在多中心队列中优于单模态和晚期拼接方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal clinical AI is limited by weakly aligned inputs and the absence of domain-specific interpretable representations, particularly when learning from dense video stream, structured time-series, and template-based kinematic text. Here we present ScoliDetect, an explainable framework for adolescent idiopathic scoliosis screening from monocular gait video, built around a kinematic knowledge map (KKM) and complementary template-based kinematic text derived from per-sequence pose statics. KKM is a fixed-index structured representation that encodes gait features across absolute motion, self-skeleton configuration and joint-joint signal correlation, providing anchor-referenced multimodal fusion and factor-level interpretation. We integrate video, KKM, and template-based kinematic text through bidirectional cross-attention with latent-bottleneck aggregation. In a multicenter cohort (n = 1,858 after exclusions), prespecified supervised ablations on an external screening cohort show that KKM-mediated multimodal fusion outperforms unimodal models and late concatenation. Under a staged training protocol, trimodal contrastive pretraining is applied after architecture selection as representation initialization, improving external ROC-AUC from 0.961 to 0.972. Furthermore, the structured nature of the KKM provides inherent, factor-level attributions mapped directly to specific kinematic phases and skeletal indices, offering verifiable interpretability. The results demonstrate that embedding explicit structural topologies into latent spaces significantly enhances both the generalization and explainability of multimodal pattern analysis systems.

</details>

### 7. EmotionDialogCN: A Spontaneous Multimodal Dataset for Mandarin Emotional Dialogue **⭐⭐⭐** (相关度: 40%, 质量: 0.8)

- **arXiv ID**: [2608.20905](https://arxiv.org/abs/2608.20905)  · [📄 PDF](https://arxiv.org/pdf/2608.20905)
- **作者**: Yi Zheng, Yifan Xu, Yan Zhou et al. (11 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV
- **摘要（中）**: ①针对现有情感对话数据集存在情感标注不足、情感多样性差和规模小的问题。②引入了EmotionDialogCN，一个大规模视听情感数据集，包含21,880个对话会话，由119名专业演员在20个日常场景中表演，覆盖18种情感类别，超过400小时录音。③改进点在于采用新颖的数据收集框架减少设备干扰，实现自然细腻的情感表达，并实现情感分布偏差仅为0.64（对比先前数据集的5.65）。④该数据集在声学、词汇和视觉模态上均表现出稳定的单模态和多模态性能，融合结果强调强多模态对齐和跨模态互补性。
- **摘要（英）**: This paper addresses the limitations of existing multimodal dialogue datasets, including inadequate annotations, poor diversity, and small scale. It introduces EmotionDialogCN, a large-scale audiovisual-emotional dataset with 21,880 sessions, 18 emotion categories, and over 400 hours, achieving an emotion distribution deviation of 0.64. The dataset enables stable unimodal and multimodal performance with strong cross-modal alignment.
- **评估**: 该论文贡献了一个高质量数据集，对情感计算和多模态研究有参考价值，但方法创新性有限。
- **核心贡献**: 构建了EmotionDialogCN，一个大规模、高多样性的中文情感对话数据集。
- **创新点**: 采用减少设备干扰的数据收集框架，实现自然情感表达。
- **结果**: 情感分布偏差仅0.64，显著优于先前数据集。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Face-to-face audiovisual interaction is central to human communication, conveying rich emotional and social cues. However, existing multimodal dialogue datasets remain limited by inadequate emotion annotations, poor emotional diversity, and small scale. We introduce EmotionDialogCN, a large-scale audiovisual-emotional dataset designed to capture authentic face-to-face communication. It contains 21,880 dialogue sessions performed by 119 professional actors across 20 everyday scenarios, covering 18 emotion categories with over 400 hours of recordings, the largest and most comprehensive dataset of its kind. A novel data collection framework minimizes equipment interference, enabling natural and nuanced emotional expressions. EmotionDialogCN achieves an emotion distribution deviation of 0.64 from real human emotion statistics (versus 5.65 for prior datasets) and consistent subject framing (52-59% frame occupancy). Together, these properties translate into stable unimodal and multimodal performance across acoustic, lexical, and visual modalities, with fusion results further underscoring strong multimodal alignment and cross-modal complementarity.

</details>

### 8. Recognition-Conditioned Reasoning: A Training-Free Multimodal-LLM Pipeline for Fine-Grained Micro-Action Understanding **⭐⭐⭐⭐** (相关度: 70%, 质量: 0.8)

- **arXiv ID**: [2608.21022](https://arxiv.org/abs/2608.21022)  · [📄 PDF](https://arxiv.org/pdf/2608.21022)
- **作者**: Fengshun Wang, Jin'ang Han, Zhigang Tu
- **提交日期**: 2026-08-21 · **分类**: cs.CV, cs.MM
- **摘要（中）**: ①针对微动作理解中细粒度分类和推理的挑战，现有模型难以同时处理识别和描述任务。②提出训练免费、仅提示的系统，基于冻结的多模态大语言模型，动态将八个子任务路由到最适合的MLLM。③创新点在于任务特定路由：判别式MLLM用于封闭式识别，生成式MLLM用于开放式描述和推理。④在MA-Bench上获得第一名，开放式任务平均得分2.68，远超第二名1.44。
- **摘要（英）**: This paper presents a training-free, prompt-only system for fine-grained micro-action understanding, winning first place in the MA-Bench challenge. It dynamically routes sub-tasks to the best-suited frozen MLLM, achieving an average score of 2.68 on open-ended tasks versus 1.44 for the second-best approach. The key innovation is task-specific routing between discriminative and generative MLLMs.
- **评估**: 该工作展示了无需微调即可通过任务路由提升多模态理解性能，具有实际应用价值。
- **核心贡献**: 提出基于任务路由的训练免费MLLM系统，在微动作理解中取得领先性能。
- **创新点**: 动态选择判别式或生成式MLLM以匹配子任务需求。
- **结果**: 在MA-Bench上获得第一名，开放式任务得分显著领先。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Micro-actions are subtle, short, low-amplitude body movements, such as a fidgeting hand or a slight head tilt, that humans perform with little conscious intent yet that reliably leak emotional and psychological state. Understanding them goes beyond assigning a label: a model must also describe which body parts move and reason, faithfully, about why a clip warrants a particular fine-grained category. We present the training-free, prompt-only system that won first place in the fine-grained understanding track (MA-Bench) of the MAC~2026 Micro-Action Challenge, where both fine-tuning and ground-truth supervision are disallowed. Built entirely upon frozen multimodal large language models (MLLMs), the system dynamically routes each of the eight sub-tasks to the MLLM empirically best suited for that task: a discriminative MLLM for closed-ended recognition tasks and a generative MLLM for open-ended description and reasoning tasks. This architecture achieves a statistically significant performance advantage on open-ended tasks, attaining an average score of 2.68 (on a five-point scale) compared to 1.44 for the second-best approach.

</details>

### 9. EviRank: Structured Relevance Evidence for Multimodal Image Re-ranking **⭐⭐⭐⭐** (相关度: 65%, 质量: 0.85)

- **arXiv ID**: [2608.20886](https://arxiv.org/abs/2608.20886)  · [📄 PDF](https://arxiv.org/pdf/2608.20886)
- **作者**: Enjun Du, Siyi Liu, Zirong Chen et al. (11 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV, cs.LG
- **摘要（中）**: ①针对多模态图像检索中查询的复杂性和组合性，现有重排序方法要么压缩为不透明嵌入，要么依赖易遗漏约束的自由文本推理。②提出EviRank，将重排序视为语义约束满足问题，解析查询为统一证据包，包含六个语义槽的类别化标准。③创新点在于证据条件验证，结合确定性评分和基于证据的列表比较，无需训练。④在五个基准上达到最先进性能，并支持蒸馏轻量学生模型。
- **摘要（英）**: This paper introduces EviRank, a training-free framework that recasts multimodal image re-ranking as semantic constraint satisfaction by parsing queries into typed evidence packages. It combines deterministic rubric scoring with evidence-grounded listwise comparison, achieving state-of-the-art results across five benchmarks. The explicit evidence also enables optional distillation of a lightweight student model.
- **评估**: 该工作将结构化证据引入重排序，提升了多模态检索的准确性和可解释性，值得关注。
- **核心贡献**: 提出基于语义约束满足的证据驱动重排序方法EviRank。
- **创新点**: 将查询解析为六槽证据包，实现训练免费的证据条件验证。
- **结果**: 在五个基准上达到最先进性能，并支持模型蒸馏。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Real-world image search queries are multimodal and compositional: ``find this shirt in pink'' specifies an entity to retain, an attribute to modify, and context to ignore. Yet existing re-rankers either compress such multifaceted relevance into an opaque embedding or rely on free-form chain-of-thought that easily omits or hallucinates fine-grained constraints. Drawing on rubric- and checklist-based evaluation from NLP, we recast multimodal image re-ranking as a semantic constraint satisfaction problem and propose EviRank, which parses any query - text-only, image-only, or composed - into a unified evidence package: typed criteria across six semantic slots (e.g., entities, attributes, relations), each labelled required, forbidden, or ignorable. Re-ranking then reduces to evidence-conditioned verification, combining deterministic rubric scoring and evidence-grounded listwise comparison in a single training-free procedure. The explicit evidence can further serve as structured supervision for optionally distilling a lightweight student. Across five benchmarks spanning text-to-image, image-to-image, and composed image retrieval, EviRank achieves state-of-the-art performance, and the distilled student preserves over 90% of the teacher's capability at substantially lower cost.

</details>

### 10. Multi-Modal Traffic Sign Detection with Semantic Attributes for Autonomous Driving **⭐⭐⭐⭐** (相关度: 90%, 质量: 0.8)

- **arXiv ID**: [2608.20874](https://arxiv.org/abs/2608.20874)  · [📄 PDF](https://arxiv.org/pdf/2608.20874)
- **作者**: Meda Lazar, Sourab Sridhar, Shashwata Gupta et al. (6 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV, cs.RO
- **摘要（中）**: ①针对交通标志检测中跨区域泛化差、小目标检测难和时序跟踪脆弱的问题，现有视觉方法存在根本局限。②提出多模态检测框架，结合相机和LiDAR，使用强度感知可变形融合模块对齐反射LiDAR线索与相机特征。③创新点在于基于几何不变量的检测和双运动模型跟踪器，适应非线性透视变换。④在长距离和跨区域场景中提升检测鲁棒性，具体数据未在摘要中给出。
- **摘要（英）**: This paper addresses traffic sign detection challenges by proposing a multi-modal framework combining camera and LiDAR with an Intensity-Aware Deformable Fusion module. It anchors detection on geometric invariants and introduces a dual motion-model tracker for non-linear perspective distortion. The method improves robustness in long-range and cross-regional scenarios.
- **评估**: 该工作针对自动驾驶感知中的实际痛点，多模态融合设计具有工程价值。
- **核心贡献**: 提出结合相机和LiDAR的多模态交通标志检测框架，提升跨区域和长距离性能。
- **创新点**: 强度感知可变形融合和双运动模型跟踪器处理透视失真。
- **结果**: 在长距离和跨区域场景中增强检测鲁棒性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Reliable traffic sign detection is a prerequisite for the global deployment of autonomous driving systems, where regulatory compliance and road safety depend on perceiving signs correctly across regions, ranges, and weather conditions. Despite recent progress, vision-based methods continue to face three fundamental limitations: poor cross-regional generalization due to high diversity across countries, degraded performance on small-object detection at long ranges (traffic signs occupy as little as $10{\times}10$ pixels at 200m), and fragile temporal tracking under the strongly non-linear perspective distortion that occurs as a vehicle approaches a sign. In this paper, we address the problem of robust, long-range, region-agnostic traffic sign perception by combining camera and Light Detection and Ranging (LiDAR) sensing. We present a multi-modal detection framework whose Intensity-Aware Deformable Fusion module aligns retro-reflective LiDAR cues with camera features, anchoring detection on geometric invariants rather than region-specific visual appearance. We further introduce a dual motion-model tracker that explicitly accounts for non-linear perspective transformations during vehicle approach, substantially improving temporal consistency over linear motion assumptions. Additionally, we develop a semantic attribute classification pipeline that estimates occlusion level, readability, sign embeddedness, and road relevance, providing actionable context to downstream planning. Extensive evaluation on our dataset, spanning 60+ countries and 2,500+ hours of driving data, shows that the proposed pipeline achieves an Object Miss Ratio (OMR) of 0.49% across 221,068 evaluation sequences, demonstrating globally generalizable traffic sign perception in commercial-grade autonomous driving systems.

</details>

---

## Multi-camera Perception

### 1. M2Depth: Unifying Monocular Depth Foundation Priors with Multi-View Stereo **⭐⭐⭐⭐** (相关度: 85%, 质量: 0.85)

- **arXiv ID**: [2608.20788](https://arxiv.org/abs/2608.20788)  · [📄 PDF](https://arxiv.org/pdf/2608.20788)
- **作者**: Byeonggwon Lee, Sanggi Lee, Siwoo Lee et al. (5 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV
- **摘要（中）**: ①针对多视图立体匹配在未见场景中泛化差的问题，现有方法集成深度基础模型时采用静态单向融合，未能充分利用互补优势。②提出新框架，通过双向互细化策略紧密耦合深度基础模型和级联MVS流程。③创新点在于利用MVS深度解决单目尺度模糊，同时单目深度增强MVS的结构完整性和细节，并引入先验引导的成本体细化。④在标准基准上超越最先进MVS方法，具体数据未在摘要中给出。
- **摘要（英）**: This paper proposes a novel MVS framework that tightly couples a Depth Foundation Model with a cascade MVS pipeline via bidirectional mutual refinement. It leverages MVS depth to resolve scale ambiguity and monocular depth to enhance structural completeness, with a prior-guided cost volume refinement. Experiments show state-of-the-art performance on standard benchmarks.
- **评估**: 该工作通过双向融合提升MVS泛化能力，对3D重建领域有重要贡献。
- **核心贡献**: 提出双向互细化策略统一单目深度先验和多视图立体匹配。
- **创新点**: 双向信息流和先验引导的成本体细化机制。
- **结果**: 在标准基准上超越最先进MVS方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep learning-based Multi-View Stereo (MVS) has advanced significantly but often generalizes poorly to unseen scenes, particularly in occluded areas or regions with limited view overlap. To mitigate this, recent approaches integrate Depth Foundation Models (DFMs) into MVS pipelines to provide monocular depth priors. However, existing methods typically rely on a static, one-way fusion scheme, which fails to fully exploit the complementary strengths of both modalities. We propose a novel framework that overcomes this limitation by tightly coupling a DFM with a cascade MVS pipeline through a bidirectional mutual refinement strategy. Our method leverages MVS depth to resolve the scale ambiguity in monocular predictions, while the monocular depth, in turn, enhances the structural completeness and fine-grained detail of the MVS estimate. Furthermore, we introduce a prior-guided cost volume refinement mechanism that effectively integrates multi-view and monocular information via attention-based fusion and discretized depth bins, thereby promoting local geometric consistency. Extensive experiments demonstrate that our method outperforms state-of-the-art MVS approaches on standard benchmarks, producing more complete and generalizable depth maps with sharp boundaries. Furthermore, although not explicitly designed for sparse-view settings, our framework generalizes remarkably well, competing favorably with even dedicated sparse-view methods while maintaining a superior accuracy-efficiency trade-off.

</details>

### 2. Generating Multi-view Adversarial Examples for Visual Geometry Grounded Transformer **⭐⭐⭐⭐** (相关度: 80%, 质量: 0.8)

- **arXiv ID**: [2608.20748](https://arxiv.org/abs/2608.20748)  · [📄 PDF](https://arxiv.org/pdf/2608.20748)
- **作者**: Qi Song, Ziyuan Luo, Haoliang Han et al. (4 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV
- **摘要（中）**: ①针对视觉几何基础模型VGGT的安全漏洞，现有对抗扰动需要昂贵的逐场景优化，而通用扰动无法有效攻击。②提出MVAP-G，多视图对抗扰动生成器，单次前向传播生成跨视图一致的不可感知扰动。③创新点在于跨视图对抗对齐机制，确保不同场景下的扰动一致性。④实验显示MVAP-G显著降低VGGT性能，无需推理时迭代优化，开创了3D基础模型的多视图对抗攻击。
- **摘要（英）**: This paper introduces MVAP-G, a multi-view adversarial perturbation generator that produces consistent perturbations across views in a single feed-forward pass to attack VGGT. It uses a cross-view adversarial alignment mechanism for consistency across scenes. Experiments show significant performance degradation without iterative optimization, pioneering multi-view attacks on 3D foundation models.
- **评估**: 该工作揭示3D基础模型的安全漏洞，对鲁棒3D视觉系统研究具有警示意义。
- **核心贡献**: 提出首个多视图对抗扰动生成器MVAP-G，攻击3D基础模型。
- **创新点**: 跨视图对抗对齐机制实现单次前向传播的扰动生成。
- **结果**: 显著降低VGGT性能，无需迭代优化。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The Visual Geometry Grounded Transformer (VGGT) enables unified feed-forward 3D reconstruction from multi-view images. However, deploying such a high-performance model may expose critical security vulnerabilities. Traditional adversarial perturbations require costly per-scene optimization, while Universal Adversarial Perturbations (UAPs) rely on a single static pattern and fail to effectively attack VGGT. To address these limitations, we propose \textbf{MVAP-G}, a multi-view adversarial perturbation generator that produces imperceptible consistent perturbations across multiple views in a single feed-forward pass. To ensure perturbation consistency across diverse scenes, we design a cross-view adversarial alignment mechanism to process multi-view images. Experiments demonstrate that MVAP-G significantly degrades VGGT performance without iterative optimization during inference. This work pioneers multi-view adversarial attacks on 3D foundation models, uncovering severe vulnerabilities and underscoring the urgent need for robust 3D vision systems. The code is available at https://github.com/qsong2001/mvap-g.

</details>

### 3. MV2GF: Multi-view Pedestrian Detection with a Visual Geometric Foundation Model **⭐⭐⭐⭐** (相关度: 95%, 质量: 0.85)

- **arXiv ID**: [2608.20639](https://arxiv.org/abs/2608.20639)  · [📄 PDF](https://arxiv.org/pdf/2608.20639)
- **作者**: Taiga Yamane, Satoshi Suzuki, Ryo Masumura et al. (7 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV
- **摘要（中）**: ①针对多视角行人检测（MVPD）在未见相机配置下泛化能力差的问题，其根源在于难以捕捉跨视角的准确视觉几何以及检测模型对训练时图像特征投影畸变模式的过度依赖。②提出了MV2GF框架，利用视觉几何基础模型提取通用几何特征，并与任务特定特征融合，以在未见配置下有效捕捉视觉几何；同时利用3D点图将图像特征中的每个像素投影到合适的3D位置。③相比现有统一投影框架，MV2GF通过引入基础模型增强了跨视角几何泛化能力，并缓解了畸变模式依赖。④实验表明，MV2GF在未见相机配置下显著提升了检测性能，但摘要未提供具体数值。
- **摘要（英）**: This paper addresses the poor generalization of multi-view pedestrian detection to unseen camera configurations by leveraging a visual geometric foundation model. The proposed MV2GF fuses task-specific features with general-purpose geometric features and uses 3D pointmaps for accurate pixel-to-3D projection, improving cross-view geometry capture and reducing distortion dependence. Experiments demonstrate significant performance gains on unseen configurations, though specific metrics are not detailed in the abstract.
- **评估**: 该工作针对多相机感知中的关键泛化难题，创新性地引入基础模型，对实际部署有重要价值。
- **核心贡献**: 提出MV2GF，利用视觉几何基础模型提升多视角行人检测在未见相机配置下的泛化能力。
- **创新点**: 将视觉几何基础模型与任务特定特征融合，并通过3D点图实现鲁棒的像素到3D投影。
- **结果**: 在未见相机配置下显著提升检测性能，但摘要未给出具体数值。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-View Pedestrian Detection (MVPD) aims to detect pedestrians in the form of a bird's eye view map from multi-view images. Recent MVPD methods adopt a unified framework that projects 2D image features into a 3D world space and aggregates them into a single feature. Although they are effective, they struggle to generalize to unseen camera configurations during training due to two main issues. First, they are difficult to capture accurate visual geometry across views in unseen camera configurations. Second, they make detection models highly dependent on distortion patterns during training arising from their image feature projection. To address these, we leverage a visual geometric foundation model and propose MV2GF. This foundation model has exhibited strong generalization in capturing visual geometry across views and predicting accurate 3D attributes in diverse camera configurations. MV2GF fuses task-specific features with general-purpose geometric features extracted by the foundation model to effectively capture the visual geometry even in unseen camera configurations. Furthermore, MV2GF projects each pixel in the image features to an appropriate 3D location using 3D pointmaps predicted by the foundation model, preventing the detection model from depending on distortion patterns during training. Our experiments demonstrate the effectiveness of leveraging a visual geometric foundation model for MVPD and that MV2GF generalizes better than existing methods.

</details>

### 4. DiGS-Avatar: Single-Image Animatable 3D Human Reconstruction via UV-Space Diffusion **⭐⭐⭐** (相关度: 30%, 质量: 0.75)

- **arXiv ID**: [2608.20759](https://arxiv.org/abs/2608.20759)  · [📄 PDF](https://arxiv.org/pdf/2608.20759)
- **作者**: Jiakun Li, Li Fang, Hao Zhu et al. (7 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV
- **摘要（中）**: ①针对单图像3D人体重建中纹理过度平滑和几何不一致的问题，现有扩散模型依赖多视图合成，计算昂贵且易产生视图不一致。②提出了DiGS-Avatar，将任务重构为基于扩散的UV潜在空间补全，通过教师-学生框架，多视图教师提供几何对齐的伪真值潜在特征来监督单视图学生，并注入高层语义特征恢复细节，最终解码为3D高斯原语。③改进点在于通过UV空间设计保证3D一致性，避免多视图合成，提高效率。④实验表明在视觉保真度和零样本泛化上达到最先进或极具竞争力水平，重建可动画3D头像仅需0.71秒。
- **摘要（英）**: This paper tackles over-smoothed textures and geometric inconsistencies in single-image 3D human reconstruction by reformulating it as UV-latent completion with diffusion models. A teacher-student framework with multi-view pseudo-ground-truth supervision ensures 3D consistency, and semantic feature injection recovers fine details. It achieves state-of-the-art visual fidelity and zero-shot generalization, reconstructing animatable avatars in 0.71 seconds.
- **评估**: 该论文在3D重建领域有创新，但与应用领域（自动驾驶感知）相关性低，主要面向图形学。
- **核心贡献**: 提出了一种基于UV空间扩散的高效单图像3D人体重建方法。
- **创新点**: 利用教师-学生框架和UV潜在补全，避免多视图合成，保证3D一致性。
- **结果**: 在视觉保真度和零样本泛化上达到最先进水平，重建时间仅0.71秒。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Single-image 3D human reconstruction often suffers from over-smoothed textures and geometric inconsistencies. While diffusion models improve generative quality, their reliance on multi-view synthesis prior to 3D reconstruction is computationally expensive and prone to view inconsistency. We propose DiGS-Avatar, which reformulates this task as an efficient, diffusion-based UV-latent completion task, ensuring 3D consistency by design. To capture accurate spatial structure, we introduce a teacher-student framework where a multi-view teacher provides geometrically aligned pseudo-ground-truth latents to supervise a single-view diffusion student. Treating this inferred latent as a robust structural skeleton, our method injects high-level semantic features to accurately recover fine textural details without disrupting spatial integrity. The refined representation is then decoded into 3D Gaussian primitives. Extensive experiments demonstrate that DiGS-Avatar achieves state-of-the-art or highly competitive visual fidelity and zero-shot generalization, while reconstructing a fully animatable 3D avatar in just 0.71 seconds. Code is available at https://github.com/KLMAV-CUC/DiGS-Avatar.

</details>

### 5. Identity-Aware Human-Object Interaction Motion Captioning **⭐⭐⭐** (相关度: 35%, 质量: 0.7)

- **arXiv ID**: [2608.20690](https://arxiv.org/abs/2608.20690)  · [📄 PDF](https://arxiv.org/pdf/2608.20690)
- **作者**: Yiming Wang, Yonghao Dang, Huilai Li et al. (5 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV, cs.AI
- **摘要（中）**: ①针对现有的人-物交互（HOI）运动描述方法通常使用“一个人”等通用术语，未将描述与主体身份关联的问题。②引入了身份感知的HOI运动描述任务，要求每个描述指定主体身份和交互运动，并基于BEHAVE和InterCap数据集设计了身份感知描述，提出了ID-HOINet，包含多视图身份-运动学习模块（MVIML）和两阶段描述重写策略（TSCR），支持单视图推理。③改进点在于将身份信息融入运动描述，提升描述的具体性和实用性。④实验表明该方法能生成身份感知的描述，但摘要未提供具体性能数据。
- **摘要（英）**: This paper addresses the limitation of generic subject terms in HOI motion captioning by introducing identity-aware captioning, where captions specify subject identity. It proposes ID-HOINet with multi-view learning and a two-stage rewriting strategy, enabling single-view inference. The method improves caption specificity, though quantitative results are not detailed.
- **评估**: 该论文聚焦于运动描述和身份识别，与自动驾驶感知领域相关性较低，但方法有创新性。
- **核心贡献**: 提出了身份感知的HOI运动描述任务和ID-HOINet方法。
- **创新点**: 通过多视图学习和两阶段重写策略，将身份信息融入运动描述。
- **结果**: 生成身份感知的描述，但具体效果未在摘要中给出。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing human-object interaction (HOI) motion captioning methods typically describe what happens while referring to the subject using generic terms such as "a person" or "someone", without grounding the caption in subject identity. To address this limitation, we introduce Identity-Aware Human-Object Interaction Motion Captioning task. This task requires each generated caption to specify both the subject identity and the corresponding HOI motion. For example, the model generates "Sub_ID lifts the chair" rather than "A person lifts the chair". For this task, we design identity-aware HOI motion captions based on the BEHAVE and InterCap datasets. We further propose ID-HOINet, which learns from multi-view videos while supporting single-view identity-aware HOI motion caption generation. ID-HOINet contains two core components: Multi-View Identity-Motion Learning Module (MVIML) and Two-Stage Caption Rewriting Strategy (TSCR). MVIML learns from multi-view videos by modeling dependencies across temporal stages and camera viewpoints, capturing identity and interaction motion features. At inference, the TSCR first retrieves the subject identity and generates identity-agnostic HOI motion captions. TSCR then rewrites these captions with the predicted identity to produce the final identity-aware HOI motion captions. Experiments demonstrate that ID-HOINet achieves state-of-the-art performance. Code will be released upon acceptance.

</details>

### 6. TopoSurfel: Closing the Loop between Gaussian Surfels and Meshes for Surface Reconstruction **⭐⭐⭐⭐** (相关度: 60%, 质量: 0.8)

- **arXiv ID**: [2608.20687](https://arxiv.org/abs/2608.20687)  · [📄 PDF](https://arxiv.org/pdf/2608.20687)
- **作者**: Chuanjin Fan, Wenjie Chang, Bohao Liao et al. (6 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV, cs.GR
- **摘要（中）**: ①针对3D高斯泼溅（3DGS）直接提取高保真表面困难，现有方法依赖多视图几何一致性或局部约束，在无纹理或遮挡区域易产生伪影和漂浮物的问题。②提出了TopoSurfel框架，通过非可训练的可微等值面提取过程动态生成连续代理网格，并利用网格引导的surfel演化策略（包括法线对齐和几何感知密度控制）抑制漂浮物和填充表面空洞，同时解决初始化问题。③改进点在于无需辅助神经网络或额外参数，将网格提取集成到可微流程中，提供结构化几何先验。④实验表明该方法在表面重建中有效减少伪影和漂浮物，但摘要未提供具体数值。
- **摘要（英）**: This paper addresses the challenge of extracting high-fidelity surfaces from 3DGS, which suffers from artifacts in textureless regions. TopoSurfel closes the loop between Gaussian surfels and meshes via a differentiable iso-surfacing process, using mesh-guided evolution to suppress floaters and fill holes. It improves reconstruction quality without auxiliary networks, though specific metrics are not given.
- **评估**: 该论文在3D重建和3DGS领域有重要贡献，与3D感知相关，但主要面向通用重建，而非自动驾驶特定场景。
- **核心贡献**: 提出了TopoSurfel，通过可微等值面提取和网格引导演化实现高质量表面重建。
- **创新点**: 利用非训练的可微等值面过程动态提取网格，无需额外参数。
- **结果**: 有效减少伪影和漂浮物，提升表面重建质量。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D Gaussian Splatting has achieved remarkable success in novel view synthesis. However, extracting high-fidelity surfaces directly from 3DGS remains challenging due to its discrete and unstructured nature. Existing 3DGS-based reconstruction methods typically rely on multi-view geometric consistency or local constraints. Without an explicit structured geometric prior during optimization, these methods often struggle to resolve structural ambiguities, leading to artifacts and floaters, particularly in textureless or occluded regions. To address this limitation, we propose TopoSurfel, a novel framework that closes the loop between Gaussian surfels and continuous meshes. Unlike recent methods that incorporate mesh extraction into the differentiable pipeline by introducing auxiliary neural networks or extra per-Gaussian parameters, we dynamically extract a continuous proxy mesh via a non-trainable differentiable iso-surfacing process. Leveraging this differentiable connection, we introduce a mesh-guided surfel evolution strategy, including normal alignment and geometry-aware density control, to effectively suppress floaters and fill surface holes. Furthermore, to address the initialization challenges in large-scale environments, we propose a spatially aware hybrid re-initialization strategy that ensures robust reconstruction across complex scenes. Extensive experiments demonstrate that TopoSurfel achieves competitive geometric reconstruction accuracy while maintaining high-quality mesh-based novel view synthesis. The code for our method is available at https://github.com/Fan-Treasure/TopoSurfel.

</details>

---

## Network Pruning

### 1. Just Noticeable Difference Modeling for Token Compression in Vision-Language-Action Models **⭐⭐⭐⭐** (相关度: 85%, 质量: 0.75)

- **arXiv ID**: [2608.21247](https://arxiv.org/abs/2608.21247)  · [📄 PDF](https://arxiv.org/pdf/2608.21247)
- **作者**: Zhuoyuan Li, Rui Zhao, Jin Wang et al. (8 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV, cs.RO
- **摘要（中）**: ①针对视觉-语言-动作模型中token压缩导致下游动作预测偏差的问题。②提出Action-JND，将人类视觉系统的恰可察觉差概念扩展到机器感知，通过语言条件动作响应定义token的可压缩性，指导压缩过程。③相比现有基于相似性或注意力的压缩方法，该方法直接衡量token变化对动作的影响，更安全有效。④实验表明，该方法在保持动作预测精度的同时显著降低推理成本，但摘要未提供具体数值。
- **摘要（英）**: This paper introduces Action-JND, extending just noticeable difference to embodied perception for token compression in vision-language-action models, defining noticeability via language-conditioned action responses. It outperforms similarity/attention-based methods by directly targeting downstream action deviation, reducing inference cost without compromising accuracy.
- **评估**: 针对具身智能的token压缩提出新视角，对自动驾驶决策有重要参考价值。
- **核心贡献**: 提出Action-JND概念，用于VLA模型的安全token压缩。
- **创新点**: 将JND从人类视觉扩展到机器动作响应。
- **结果**: 在保持精度的同时降低推理成本。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Token compression has become a key technique for reducing the inference cost of large foundation models, with approaches such as token pruning and KV-cache reuse widely adopted in vision-language models and recently explored for embodied agents. In embodied agents, tokens not only support perception and semantic understanding but also directly affect latency-sensitive closed-loop robot action prediction. Existing schemes typically guide compression using redundancy or importance cues, such as visual similarity, attention scores, and saliency. However, these cues only indirectly measure the key factor for safe compression: how much a token can change before causing an unacceptable deviation in downstream actions. This receiver-dependent tolerance is closely related to the principle of just noticeable difference (JND). Classical JND characterizes signal tolerance in the human visual system, while machine-oriented JND extends this concept to downstream machine responses. Building on this progression, we introduce Action-JND, which extends JND modeling to embodied perception by defining noticeability through the language-conditioned action response of a vision-language-action (VLA) policy in closed-loop control. A token change is considered admissible only when the induced action deviation remains within a tolerated margin. To realize this concept, we develop a lightweight token-wise JND estimator in deep visual-feature space to predict the maximum tolerable perturbation while preserving policy responses. The resulting action-tolerance score serves as a plug-and-play criterion for VLA compression paradigms, including stale-KV reuse and token pruning, prioritizing action-tolerant tokens for compression. Experiments on the LIBERO benchmark with OpenVLA and OpenVLA-OFT demonstrate that Action-JND consistently improves compression reliability, especially under aggressive compression ratios.

</details>

### 2. CubicSplat: Differentiable Vector Graphics via Error-Bounded Forward Relaxation **⭐⭐** (相关度: 10%, 质量: 0.7)

- **arXiv ID**: [2608.20803](https://arxiv.org/abs/2608.20803)  · [📄 PDF](https://arxiv.org/pdf/2608.20803)
- **作者**: Chenglong Liu, Xin Zhang, Yimeng Zhu et al. (8 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.GR, cs.CV, cs.LG
- **摘要（中）**: ①针对可微矢量图形光栅化中前向几何精确性与梯度信号质量之间的权衡问题，即梯度跷跷板效应。②提出了CubicSplat，一种可微矢量光栅化器，用均匀折线替代Bézier最近点求解器，其几何误差以O(S^-2)为界，通过静态计算图保证梯度条件良好，并利用合成导出的可见性机制剪枝退化图元。③相比现有平滑前向方法，CubicSplat在提高几何精确性的同时保持了良好梯度，无需辅助正则化。④在DIV2K和Kodak基准上，CubicSplat在封闭填充设置下实现了最先进的重建质量，PSNR提升超过2 dB，训练速度比先前方法快4倍。
- **摘要（英）**: This paper tackles the gradient seesaw between forward geometric exactness and gradient quality in differentiable vector graphics rasterization. CubicSplat replaces Bézier solvers with uniform polyline surrogates with bounded error, yielding well-conditioned gradients and pruning degenerate primitives via compositing-derived visibility. It achieves over 2 dB PSNR gain and 4x faster training on DIV2K and Kodak benchmarks.
- **评估**: 该工作虽与自动驾驶感知关联度低，但在可微渲染领域具有方法创新性。
- **核心贡献**: 提出CubicSplat，一种误差有界的可微矢量光栅化器，解决了梯度跷跷板问题。
- **创新点**: 用均匀折线替代Bézier求解器，结合静态计算图和合成可见性机制。
- **结果**: 在DIV2K和Kodak上PSNR提升超2 dB，训练速度提升4倍。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vector graphics are prized for their resolution independence, compact storage, and direct editability, making differentiable optimization of their parametric primitives an attractive goal. Yet classical rasterization is discontinuous with respect to geometry, and existing remedies that smooth the forward pass demand increasingly elaborate heuristics as scene complexity grows. We trace this fragility to a gradient seesaw: design choices that improve forward geometric exactness can systematically degrade the induced gradient signal, and vice versa. To navigate this tension we introduce CubicSplat, a differentiable vector rasterizer that replaces Bézier closest-point solvers with uniform polyline surrogates whose geometric error is bounded at $O(S^{-2})$. The resulting static computation graph yields well-conditioned gradients by construction, while a compositing-derived visibility mechanism prunes degenerate primitives without auxiliary regularization. On DIV2K and Kodak benchmarks CubicSplat achieves state-of-the-art reconstruction quality with over 2 dB PSNR gain in the closed-fill setting, while training up to 4x faster than prior methods. The code is available at https://github.com/CubicSplat/repo

</details>

### 3. Robust Validation to Geometric Perturbations for Autonomous Pose Estimation **⭐⭐⭐⭐** (相关度: 85%, 质量: 0.8)

- **arXiv ID**: [2608.21066](https://arxiv.org/abs/2608.21066)  · [📄 PDF](https://arxiv.org/pdf/2608.21066)
- **作者**: Gregoire Theau, Melanie Ducoffe
- **提交日期**: 2026-08-21 · **分类**: cs.CV
- **摘要（中）**: ①针对自动驾驶等安全关键系统中，姿态估计对几何扰动（如相机旋转和光照变化）的鲁棒性验证不足，标准梯度方法（如APGD）在姿态估计上表现不佳的问题。②提出了将姿态估计鲁棒性验证重构为全局Lipschitz优化（GLO）问题，利用GLO的理论收敛保证来定位全局最优，评估了YOLOv8-Pose关键点检测器和PnP求解器在旋转和对比度扰动下的表现。③改进点在于GLO能有效克服梯度方法的优化瓶颈，提供更可靠的鲁棒性验证。④实验表明GLO成功识别出位置偏差超过安全阈值的临界失败模式，并快速剪枝，但具体数值未给出。
- **摘要（英）**: This paper addresses the failure of gradient-based methods in robustness validation for pose estimation under geometric perturbations. It reformulates the problem as Global Lipschitzian Optimization (GLO), which provides theoretical convergence guarantees and effectively localizes global optima. Evaluations on YOLOv8-Pose show GLO identifies critical failure modes efficiently, though specific metrics are not detailed.
- **评估**: 该论文与自动驾驶感知高度相关，聚焦于姿态估计的鲁棒性验证，方法有理论支撑，实用价值高。
- **核心贡献**: 提出了基于全局Lipschitz优化的姿态估计鲁棒性验证框架。
- **创新点**: 将GLO应用于姿态估计鲁棒性，克服梯度方法的优化瓶颈。
- **结果**: 成功识别关键失败模式，提升鲁棒性验证效率。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deploying autonomous systems in safety-critical domains demands guaranteed robustness against physically plausible geometric perturbations rather than abstract pixel-wise noise. In vision-based navigation and autonomous landing, machine learning components require rigorous validation under dynamic operational conditions such as camera rotations and lighting shifts. Extending findings on the failure of first-order spatial attacks in classification, we show that standard gradient-based heuristics (e.g. APGD) similarly fail on for pose estimation, often performing worse than a simple random sampling baseline. To overcome these optimization bottlenecks, we reformulate pose estimation robustness within the framework of Global Lipschitzian Optimization (GLO). We argue that GLO offers a principled approach to robust validation, effectively localizing global optima with strong theoretical convergence guarantees. We evaluate this framework on a YOLOv8-Pose keypoint detector with a Perspective-n-Point (PnP) solver against rotation and contrast. In our evaluations, GLO successfully isolates critical failure modes where position deviations exceed safe operational limits, while rapidly pruning the search space by over 80%. To the best of our knowledge, this is the first study to extend geometric robustness validation to continuous keypoint regression and deep object detection, establishing a practical step toward certifying robust autonomous perception.

</details>

### 4. GAP-SAM: A Global Artifact Prior for Generalizable AI-Generated Image Manipulation Localization **⭐⭐⭐⭐** (相关度: 50%, 质量: 0.8)

- **arXiv ID**: [2608.20929](https://arxiv.org/abs/2608.20929)  · [📄 PDF](https://arxiv.org/pdf/2608.20929)
- **作者**: Haozhen Yan, Siyuan Shan, Zijian Yu et al. (7 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV
- **摘要（中）**: ①针对AI生成图像操作定位的分布外（OOD）性能不佳，像素级监督将取证证据与数据集特定的掩码几何和语义边界纠缠的问题。②构建了COCO-ControlNet数据集，使用源图像的Canny边缘和深度图对齐语义和几何，并提出了GAP-SAM，通过编码图像和冻结VAE重建的全局伪影令牌，注入SAM3的特征金字塔，使用零门控FiLM调制密集解码，避免语义边界捷径。③改进点在于全局伪影令牌不预设空间区域，保留定位能力同时抑制语义边界偏差。④实验在六个数据集上验证了方法的有效性，但摘要未提供具体数值。
- **摘要（英）**: This paper addresses poor OOD performance in AI-generated image manipulation localization by introducing COCO-ControlNet for semantic-geometric alignment and GAP-SAM, which injects a global artifact token into SAM3's feature pyramid. The method suppresses semantic-boundary shortcuts while preserving localization. It demonstrates effectiveness across six datasets, though specific metrics are not given.
- **评估**: 该论文在图像取证领域有创新，与FOD检测相关，但主要面向通用图像，与自动驾驶场景关联有限。
- **核心贡献**: 提出了GAP-SAM，利用全局伪影令牌提升操作定位的OOD泛化能力。
- **创新点**: 通过零门控FiLM注入全局伪影令牌，避免语义边界捷径。
- **结果**: 在多个数据集上提升了操作定位的泛化性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> AI-generated image manipulation localization identifies edited pixels, but its OOD performance lags behind image-level detection partly because pixel supervision entangles forensic evidence with dataset-specific mask geometry and semantic boundaries. Extending image-level distribution alignment to localization, we construct COCO-ControlNet with source-image Canny edges and depth maps to align semantics and geometry, improving OOD performance across multiple localizers. Yet tighter Mask-VAE Reconstruction Alignment (Mask-VAE) underperforms COCO-ControlNet, showing that VAE reconstruction artifacts transfer poorly to local diffusion-inpainting artifacts. We also identify \emph{boundary adhesion}, where fine-tuned segmentation models snap predictions to semantic object contours rather than true manipulation boundaries. These findings motivate GAP-SAM, which encodes an image and its frozen VAE reconstruction into a global artifact token and injects it into SAM3's feature pyramid via zero-gated FiLM before pixel decoding. Without prescribing a spatial region, this token modulates dense decoding to preserve localization while suppressing semantic-boundary shortcuts. Across six datasets, GAP-SAM averages 79.8 Pixel-F1, outperforming the strongest prior method by 12.6 points. It also performs best at every tested severity of JPEG compression, Gaussian blur, and resizing.

</details>

### 5. Aristotelian Manifolds: Leveraging Platonic Perceptual Features for Backpropagation Free Rapid Concept Learning **⭐⭐⭐** (相关度: 70%, 质量: 0.6)

- **arXiv ID**: [2608.20682](https://arxiv.org/abs/2608.20682)  · [📄 PDF](https://arxiv.org/pdf/2608.20682)
- **作者**: Michael Karnes, Alper Yilmaz
- **提交日期**: 2026-08-21 · **分类**: cs.CV
- **摘要（中）**: ①这篇论文针对预训练基础模型（如视觉Transformer）中特征表示如何随网络深度演化的问题，旨在为无需反向传播的快速概念学习提供理论依据。②作者提出了“亚里士多德流形”框架，基于柏拉图表示假说，将高容量基础模型视为通用感知滤波器，并对不同架构和多领域数据集进行逐层分析，绘制网络深度、降维与距离度量之间的相互作用。③相比已有工作，该研究揭示了语义成熟并非单调路径，而是呈现领域特异的几何响应轮廓（如临床模态的中间峰、自然视觉任务的S形平台），并据此建立了层选择和特征压缩的可预测分类法。④通过映射冻结表示的内部几何，证明了无需反向传播即可实现稳健的概念学习，但摘要未提供具体量化数据。
- **摘要（英）**: This paper addresses how feature representations evolve across layers in pretrained foundation models, proposing an Aristotelian Manifold framework grounded in the Platonic Representation Hypothesis to enable backpropagation-free rapid concept learning. Through systematic layer-wise analysis across architectures and multi-domain datasets, it reveals non-monotonic semantic maturation with domain-specific geometric profiles, such as mound-like peaks for clinical modalities and sigmoidal plateaus for natural tasks, establishing a taxonomy for layer selection and feature compression. The work demonstrates that mapping frozen representation geometry provides a robust, backpropagation-free learning paradigm, though quantitative results are not detailed in the abstract.
- **评估**: 该论文对表示几何的深入分析具有理论价值，但实验充分度一般，且与自动驾驶感知的直接关联较弱，适合关注自监督表示学习的读者。
- **核心贡献**: 提出了亚里士多德流形框架，系统刻画了预训练模型中特征表示随深度变化的几何规律，并建立了无需反向传播的概念学习路径。
- **创新点**: 揭示了语义成熟的多模态几何响应模式，并据此提出可预测的层选择和特征压缩策略。
- **结果**: 证明了基于冻结表示几何的映射可实现稳健的快速概念学习，但缺乏具体性能数据。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper formalizes and systematically characterizes Aristotelian Manifolds, a generalized structural framework built upon the Platonic Representation Hypothesis. We position high-capacity foundation models as universal perceptual filters and conduct a comprehensive layer-wise investigation to map how knowledge is functionally synthesized within these latent subspaces. Across diverse architectural paradigms and multi-domain datasets, we rigorously chart the interplay between network depth, dimensionality reduction, and distance metrics. Our characterization reveals that semantic maturation does not follow a singular, monotonic path; instead, different data domains exhibit highly distinct geometric response profiles, characterized by intermediate mound-like peaks for specialized clinical modalities and sigmoidal plateaus for natural visual tasks. By profiling the exact coordinates where these manifolds achieve peak representational efficiency, we establish a predictable taxonomy for layer selection and feature compression. Ultimately, this systematic characterization demonstrates that mapping the internal geometry of frozen representations provides a robust, backpropagation-free, and interpretable framework for understanding and exploiting foundation model latent spaces.

</details>

---

## Video Understanding

### 1. Enhancing Localized Reasoning for Long Video Understanding via Efficient Segment-to-Video Supervision **⭐⭐⭐⭐** (相关度: 80%, 质量: 0.8)

- **arXiv ID**: [2608.20814](https://arxiv.org/abs/2608.20814)  · [📄 PDF](https://arxiv.org/pdf/2608.20814)
- **作者**: Beibei Zhang, Chao Xu, Jun Lan et al. (7 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV
- **摘要（中）**: ①这篇论文针对长视频理解中，复杂上下文中的噪声干扰局部细节，导致MLLM产生错误答案，以及现有强化微调方法训练开销大和推理延迟高的问题。②提出了段到视频监督方法（S2V），基于局部片段生成VQA对，然后将这些片段级VQA迁移到整个视频进行训练。③相比已有工作，S2V通过聚焦短片段自然关注细节，避免了高注释成本和复杂奖励设计，并降低了推理延迟。④实验表明，S2V有效增强了长视频理解中的细粒度推理能力。
- **摘要（英）**: This paper addresses noisy distractions and high training overhead in long video understanding by proposing Segment-to-Video Supervision (S2V), which generates VQA pairs based on localized segments and transfers them to whole-video training. By focusing on short segments, S2V naturally captures details overlooked from a whole-video perspective, efficiently enhancing fine-grained reasoning with reduced annotation costs and inference latency.
- **评估**: 该论文提出了一种高效的长视频理解细粒度推理增强方法，对降低训练成本和提升推理效率有实际价值。
- **核心贡献**: 提出了S2V方法，通过段到视频监督高效增强长视频理解中的细粒度推理。
- **创新点**: 利用局部片段VQA迁移到全视频训练，避免高注释成本和复杂奖励设计。
- **结果**: S2V有效增强了长视频理解中的细粒度推理能力。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Though Multimodal Large Language Models (MLLMs) have shown impressive potential in video understanding, long video understanding (LVU) remains challenging since distracting noise in complex and lengthy contexts can obscure localized details, misleading MLLMs to produce incorrect answers. Recent works mitigate these issues by incentivizing deep reasoning to include relevant evidence. However, these methods have two main problems: First, the reinforcement fine-tuning framework (RFT) they leveraged incurs substantial training overheads, including high annotation costs and complicated reward designs. Second, the self-reflective and iterative-perception mechanism in some methods causes lengthy outputs and high inference latency. To alleviate these problems, we propose a novel Segment-to-Video Supervision} method (S2V) to efficiently enhance fine-grained reasoning in LVU. Specifically, we generate question answer pairs (VQA) based on localized segments, and then transfer these segment-based VQA back to the whole video for training. Due to focusing on short segments, segment-based VQA can naturally notice details which tend to be overlooked from a whole-video perspective. Training on such data can enforce MLLMs to correctly associate fine-grained details with QA while avoiding distracting noise in the whole video. The S2V training involves just reinforcement learning (RL) with a simple accuracy reward based on only 10K VQA samples and the resulting S2V model predicts answer using a single forward pass with limited output tokens. Experimental results demonstrate that S2V can consistently improve LVU performance across multiple LVU benchmarks, outperforming both general MLLMs and reasoning-based methods not only in LVU accuracy but also in training and inference efficiency.

</details>

### 2. Routing Before Looking: Query-Adaptive Evidence Acquisition for Long-form Video Understanding **⭐⭐⭐⭐** (相关度: 75%, 质量: 0.85)

- **arXiv ID**: [2608.20805](https://arxiv.org/abs/2608.20805)  · [📄 PDF](https://arxiv.org/pdf/2608.20805)
- **作者**: Tianyue Wang, Xuying Wu, Yuxiang Ma et al. (10 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV
- **摘要（中）**: ①针对长视频理解中查询需求与证据获取策略不匹配的问题，现有方法依赖单一策略（生成式或检索式）难以应对多样化查询。②提出Route2Look框架，采用Route-Look-Memorize循环，包含全局浏览、时间定位和语义检索三种工具，并通过路由策略动态选择工具。③创新点在于两阶段设计：先从生成式和检索式轨迹的对比分析中蒸馏路由技能，再在推理时应用硬路由规则和继续/停止准则。④在长视频基准上取得显著性能提升，具体数据未在摘要中给出。
- **摘要（英）**: This paper addresses the mismatch between query demands and evidence acquisition in long-form video understanding by proposing Route2Look, a lightweight framework with a Route-Look-Memorize loop and dynamic tool selection. The key innovation is a two-stage routing policy distilled from contrastive analysis of generation- and retrieval-based trajectories. Experiments on long-video benchmarks show improved performance over existing methods.
- **评估**: 该工作为长视频理解中的证据获取提供了新思路，路由策略的设计具有实用价值，值得关注。
- **核心贡献**: 提出查询自适应证据获取框架Route2Look，动态选择工具以提升长视频理解性能。
- **创新点**: 通过对比分析蒸馏路由技能，实现生成式和检索式策略的灵活切换。
- **结果**: 在长视频基准上超越现有方法，验证了路由策略的有效性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Long-form video understanding remains challenging for video agents due to the mismatch between query demands and evidence acquisition strategies. Although recent planning-before-perception methods outperform query-agnostic pipelines, they often rely on a single dominant strategy, either generation-based strategy or retrieval-based strategy, limiting their ability to handle diverse query demands. We propose Route2Look, a lightweight and model-agnostic framework for query-adaptive evidence acquisition in long-form video understanding. Route2Look operates in a Route-Look-Memorize loop with three tools: Global Browse for holistic context, Temporal Ground for explicit temporal cues, and Semantic Retrieve for semantic search. The core component is a routing policy that dynamically selects evidence acquisition tools based on the query. To build this policy, Route2Look adopts a two-stage design: first distilling the routing skill from differential contrastive analysis between generation-based and retrieval-based trajectories, and then applying the distilled skill with hard routing rules and continue-or-stop criteria during inference. Experiments on challenging long-video benchmarks show that Route2Look achieves state-of-the-art performance while maintaining strong frame efficiency across datasets and query types. Oracle routing analysis further reveals the potential of query-adaptive evidence acquisition for future long-form video understanding.

</details>

### 3. OmniAssistBench: Assistant-style Interaction Benchmark for Omni-LLMs **⭐⭐⭐** (相关度: 60%, 质量: 0.7)

- **arXiv ID**: [2608.21360](https://arxiv.org/abs/2608.21360)  · [📄 PDF](https://arxiv.org/pdf/2608.21360)
- **作者**: Xianyun Sun, Chaoyou Fu, Zhengye Zhang et al. (9 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV
- **摘要（中）**: ①针对全模态大语言模型（Omni-LLMs）作为实时视频助手时，交互式评估因模型响应动态改变用户行为而难以进行的问题。②提出了OmniAssistBench基准，通过从源视频中提取预定义先验，要求模型引导用户沿相同路径，并逆向工程互联网视频构建多轮交互数据集。③相比静态离线数据集，OmniAssistBench支持动态交互评估，解决了路径发散问题。④数据集构建耗时超过1000专家小时，结果显示专有Gemini-3-Pro达到了较高性能，但摘要未提供具体数值。
- **摘要（英）**: This paper addresses the challenge of evaluating Omni-LLMs as interactive video assistants, where dynamic responses alter user actions. OmniAssistBench provides predefined priors from source videos and reverse-engineers internet videos to create multi-turn interaction data. Results show Gemini-3-Pro achieves strong performance, though specific metrics are not detailed.
- **评估**: 该工作为交互式多模态评估提供了新基准，但领域相关性较低。
- **核心贡献**: 提出OmniAssistBench，一个用于Omni-LLMs交互式助手评估的基准。
- **创新点**: 利用视频逆向工程和预定义先验解决交互路径发散问题。
- **结果**: 数据集构建耗时超1000小时，Gemini-3-Pro表现优异但无具体数值。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent omni-modal large language models (Omni-LLMs) show great potential as real-time video assistants, which continuously perceive environments and guide users to achieve specific goals. Unlike traditional passive video understanding, interactive assistants should actively combine visual states, user goals, and prior knowledge to provide effective help. Evaluating this is rather challenging, as the model's unpredictable response dynamically changes the user's subsequent actions, which static offline datasets cannot accommodate. To address this bottleneck, we introduce OmniAssistBench. To solve the issue of diverging interaction paths where the same user goal can be achieved through various methods, we provide models with predefined priors derived from the source video, requiring them to guide users along the exact same routes. Since real interaction videos are rare, we construct the dataset by reverse-engineering existing Internet videos. We deduce logical user goals and segment the videos into multi-turn clips to simulate continuous interactions. This rigorous pipeline required over 1000 expert person-hours to build the dataset. Results show that the proprietary Gemini-3-Pro reaches 66.4 out of the max point of 100, while the open-source Qwen3-Omni-Instruct achieves 51.2. Although current models generally understand user inputs, they frequently provide incorrect or incomplete answers. Specifically, they struggle with visual prompts (e.g., hand gestures), fail to maintain historical context during multi-turn interactions, and fail to delay response until the target event. Results indicate substantial room for improvement before models can become reliable assistants.

</details>

---

## Self-supervised Vision

### 1. WA-JEPA: Rethinking the Video JEPA Paradigm for World-Action Modeling in Autonomous Driving **⭐⭐⭐⭐⭐** (相关度: 95%, 质量: 0.9)

- **arXiv ID**: [2608.20974](https://arxiv.org/abs/2608.20974)  · [📄 PDF](https://arxiv.org/pdf/2608.20974)
- **作者**: Xinlin Wang, Yujiao Xiang, Yuheng Zhou et al. (14 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV, cs.AI
- **摘要（中）**: ①针对视频联合嵌入预测架构（V-JEPA）基于随机掩码补全和确定性回归，不适合自动驾驶规划所需的与动作紧密耦合的未来预测的问题。②提出了WA-JEPA，一个V-JEPA原生的世界-动作模型，采用混合未来掩码预训练，从观测上下文推断未来潜变量；将未来预测重构为潜变量上的条件流匹配，并引入联合未来-动作预测器，在统一时空潜空间中联合去噪未来场景令牌和自车轨迹。③改进点在于用未来掩码替代随机掩码，用条件流匹配替代确定性回归，并通过动作监督直接塑造规划相关的世界表示。④在nuPlan视频上预训练并微调后，WA-JEPA在自动驾驶规划任务中显著提升了未来潜变量生成和规划性能，具体数据未在摘要中给出。
- **摘要（英）**: This paper addresses the inadequacy of V-JEPA's random-mask completion and deterministic regression for autonomous driving planning. It proposes WA-JEPA, a V-JEPA-native world-action model with hybrid future-masked pre-training, conditional flow matching for future prediction, and a joint future-action predictor. Pre-trained on nuPlan videos, WA-JEPA improves future latent generation and planning performance.
- **评估**: 该论文针对自动驾驶规划的核心挑战，创新性地重构了V-JEPA范式，具有高相关性和强实用性。
- **核心贡献**: 提出了WA-JEPA，一个V-JEPA原生的世界-动作模型，用于自动驾驶规划。
- **创新点**: 用未来掩码和条件流匹配替代随机掩码和确定性回归，并联合预测未来和动作。
- **结果**: 在nuPlan上预训练后显著提升规划性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Video Joint Embedding Predictive Architecture (V-JEPA) learns powerful spatiotemporal representations from video through self-supervised latent feature prediction. However, V-JEPA is built around random-mask completion and deterministic regression, making it fundamentally ill-suited for autonomous driving planning that demands future-directed prediction tightly coupled with action. To address this, we rethink the V-JEPA paradigm and present WA-JEPA, a V-JEPA-native world-action model designed for autonomous driving planning. Instead of random spatiotemporal masking, WA-JEPA employs hybrid future-masked pre-training, where the model infers future latents from observed context. Departing from deterministic regression, we recast future prediction as conditional flow matching over latent futures, which substantially improves the model's ability to generate plausible future latents for downstream planning. Finally, a joint future-action predictor is proposed to denoise future scene tokens and ego trajectories together in a unified spatiotemporal latent space, allowing action supervision to directly shape planning-relevant world representations. Pre-trained on nuPlan videos and fine-tuned on NAVSIM, WA-JEPA reaches 91.7 EPDMS on NAVSIM-v2, surpassing the strongest end-to-end and world-action baselines by 1.6 and 1.3 EPDMS, and, without HUGSIM-specific fine-tuning, attains the best HD-Score of 0.4462 on the closed-loop HUGSIM benchmark under the same evaluation protocol. These results validate V-JEPA-native world-action modeling as a powerful and scalable paradigm for autonomous driving planning. Code is available at https://github.com/AFARI-Research/WA-JEPA.

</details>

### 2. When does fusing hand-crafted knowledge with learned representations pay? A cost-normalized benchmark of stacking, substitution, and interference **⭐⭐⭐⭐** (相关度: 75%, 质量: 0.8)

- **arXiv ID**: [2608.21098](https://arxiv.org/abs/2608.21098)  · [📄 PDF](https://arxiv.org/pdf/2608.21098)
- **作者**: Ahmad AlMughrabi, Albert Clop, Benjamin Busam et al. (5 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV
- **摘要（中）**: ①针对手工知识与学习表示融合何时有效、冗余或有害的问题。②通过大规模基准测试，在13个数据集、9个骨干网络上，固定训练配方下比较Gabor先验与数据驱动方法（SimCLR、DINO等）的融合效果。③发现不同来源的知识可叠加（如ViT-B/16在224px下+26点），同来源知识会替代，强先验会干扰已初始化模型。④提供了成本归一化的系统分析，为知识融合策略提供指导。
- **摘要（英）**: This paper benchmarks fusing hand-crafted Gabor knowledge with learned representations across 13 datasets and 9 backbones, revealing that different-currency sources stack (e.g., +26 points for ViT-B/16), same-currency sources substitute, and strong priors interfere. It provides a cost-normalized account of when fusion helps, is redundant, or harms.
- **评估**: 系统性的基准研究，对自监督学习和知识蒸馏有重要指导意义。
- **核心贡献**: 提供知识融合的成本归一化基准，揭示融合条件。
- **创新点**: 大规模多维度比较不同知识源融合效果。
- **结果**: ViT-B/16在224px下提升26点。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Fusing prior knowledge with data-driven learning is attractive where data is scarce, yet no controlled account says when it helps, is redundant, or harms. We benchmark one fixed hand-crafted knowledge source, a pinned bank of Gabor targets injected only during training at $\sim$2\% overhead, against data-driven alternatives (SimCLR, SimSiam, DINO, ImageNet transfer, augmentation, learned teachers) under one frozen recipe with fixed subsets: 13 datasets, 9 backbones, 150 to 1.28M images, 32--224\,px, 2.5M--86M parameters ($\computeCells$ classification configurations over $\computeRuns$ runs, plus segmentation and detection transplants). Across the training-time combinations we measure, three outcomes recur (decision-level fusion differs). Different-\emph{currency} sources can stack: the prior composes with DeiT augmentation on attention backbones and is worth $+26$ points to ViT-B/16 at $224$\,px, $+6.7$ at twice that budget. Same-currency sources substitute: against effective self-supervised pretraining, the combination never usefully exceeds the better single source. Fusing at full strength into an already-informed initialization interferes in proportion to what it carries: ImageNet transfer, $-15$ to $-17$ points, removed by a weaker auxiliary weight. Frozen-feature diagnostics measured on each source alone separate these outcomes retrospectively but do not predict them: a rule built on them calls one of nine unseen pairs. At a practitioner's own label budget, the frozen-feature gain predicts the end-to-end gain to within $0.17$ points across 30 cells and seven datasets; the underlying decomposition, $Δ= G + \readout(\mathrm{base})$, holds in sign on $\auditRate\%$ of testable cells and is called an unseen backbone family's feature gain in advance. The project page is https://amughrabi.github.io/MomentAux.

</details>

### 3. Explainable Deepfake Detection with Feature-robust Augmentation and Evidence-grounded Explanation Optimization **⭐⭐⭐** (相关度: 40%, 质量: 0.7)

- **arXiv ID**: [2608.20913](https://arxiv.org/abs/2608.20913)  · [📄 PDF](https://arxiv.org/pdf/2608.20913)
- **作者**: Zhu Xu, Jiaqi Tang, Pokai Chen et al. (5 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV, cs.AI
- **摘要（中）**: ①针对可解释深度伪造检测中，低质量图像下检测精度下降以及解释模型产生事实性错误（遗漏或幻觉）的问题。②提出了一个包含特征鲁棒增强（Feature-robust Augmentation）和基于证据的偏好优化（Evidence-grounded Preference Optimization）的框架，前者通过多样化的退化感知增强和带均值教师架构的监督对比学习稳定特征，后者引导模型生成基于证据的解释。③改进点在于同时处理鲁棒性和可解释性，避免朴素增强导致的特征漂移，并减少解释中的事实错误。④实验表明该方法在低质量样本上提升了检测精度，并改善了解释的准确性，但摘要未提供具体数据。
- **摘要（英）**: This paper addresses the issues of performance degradation on low-quality images and factually flawed explanations in explainable deepfake detection. It proposes a framework with feature-robust augmentation using supervised contrastive learning and a mean-teacher architecture, plus evidence-grounded preference optimization for explanation. The method improves robustness and explanation quality, though specific quantitative results are not detailed in the abstract.
- **评估**: 该论文针对深度伪造检测的可解释性和鲁棒性，方法设计有创新性，但领域相关性较低，且摘要缺乏具体实验数据。
- **核心贡献**: 提出了一个同时增强深度伪造检测鲁棒性和解释准确性的统一框架。
- **创新点**: 引入特征鲁棒增强和证据偏好优化，解决低质量图像下的特征漂移和解释事实错误。
- **结果**: 在低质量样本上提升了检测精度和解释质量，但具体数值未给出。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Explainable deepfake detection extends binary classification by requiring models to not only predict authenticity but also provide interpretable justifications. This expanded scope is critical in practice, where users like forensic analysts need insight into the rationale behind the detection. Despite advancements, current approaches suffer from two critical deficiencies: (1)vulnerability to image quality degradation: detection accuracy plummets on low-quality samples, while naive augmentation strategies may induce feature drift and impair performance as diversity expands. (2) factually flawed explanations: explanation models may omit manipulation evidence or hallucinate irrelevant details, undermining interpretability. To address it, we propose a framework with two innovations. For robust deepfake detection, we introduce Feature-robust Augmentation, which comprises diversified degradation-aware augmentation strategies, and a supervised contrastive learning pattern paired with a mean-teacher architecture that stabilizes features against augmentations through consistency constraints. For explanation, we devise an evidence-grounded preference optimization process that guides model to prioritize genuine manipulation traces by learning from chosen-rejected explanation pairs, where rejected samples are constructed via evidence omission or irrelevant information injection. The proposed approach wins the first place in ACM Multimedia 2026 Explainable Deepfake Detection Challenge.The code is available at https://github.com/oceanflowlab/EDD.git.

</details>

---

## Vision Transformer

### 1. AT-ViT: Area-Targeted Multi-View Vision Transformer with Cross-Attention and Multi-Scale Patching for Plant Trait Recognition in Herbarium Images **⭐⭐⭐** (相关度: 60%, 质量: 0.7)

- **arXiv ID**: [2608.21067](https://arxiv.org/abs/2608.21067)  · [📄 PDF](https://arxiv.org/pdf/2608.21067)
- **作者**: Amani Sedrat, Takieddine Chehhat, Youcef Sklab et al. (8 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV, cs.AI
- **摘要（中）**: ①这篇论文针对植物标本图像中背景元素（如文本标签、安装伪影和色卡）导致捷径学习，使模型依赖非植物线索而非植物形态的问题。②提出了AT-ViT，一个双分支视觉Transformer，通过多尺度多视图交叉注意力融合方案联合编码原始扫描和分割衍生图像，并引入掩码引导的补丁加权机制。③相比已有工作，AT-ViT通过掩码引导补丁重加权增强植物相关区域并衰减背景特征。④在多个性状分类任务（如叶基形状、刺）上，AT-ViT持续提升准确率，改善注意力定位，并在合成背景扰动下表现出更强的鲁棒性。
- **摘要（英）**: This paper addresses shortcut learning in herbarium image trait recognition by proposing AT-ViT, a dual-branch Vision Transformer with multi-scale multi-view cross-attention fusion and mask-guided patch weighting to amplify plant-relevant regions. Across multiple trait classification tasks, AT-ViT delivers consistent accuracy gains, improves attention localization, and exhibits increased robustness under synthetic background perturbations.
- **评估**: 该论文针对特定领域（植物标本）的视觉识别问题提出了有效的注意力引导方法，对细粒度识别有参考价值。
- **核心贡献**: 提出了AT-ViT，通过掩码引导补丁加权和多视图交叉注意力增强植物性状识别。
- **创新点**: 利用分割掩码引导补丁重加权机制抑制背景捷径学习。
- **结果**: 在多个性状分类任务上持续提升准确率并增强鲁棒性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Automated plant traits recognition from herbarium images is essential for plant sciences, yet remains challenging because background elements (e.g., textual labels, mounting artifacts, and color charts) can introduce shortcut learning, leading models to rely on spurious non-plant cues rather than plant morphology. This bias degrades both generalization and interpretability. In this paper, we introduce AT-ViT, a dual-branch Vision Transformer that jointly encodes raw herbarium scans and their segmented-derived counterparts via a multi-scale, multi-view cross-attention fusion scheme. AT-ViT further incorporates a mask-guided patch weighting mechanism that amplifies plant-relevant regions and attenuates background-driven features. By learning from the original scans while being guided by segmentation masks through the mask-guided patch reweighting mechanism, the model is encouraged to focus on plant organs and learn plant-centric representations more effectively. Across multiple trait classification tasks (e.g., leaf base shape, thorns), AT-ViT delivers consistent accuracy gains, improves attention localization on plant regions, and exhibits increased robustness under synthetic background perturbations. Specifically, AT-ViT substantially improves spatial attention grounding, boosting plant-region alignment (Avg IoU_p: +15.66 to +18.03 pp) while reducing background overlap (Avg IoU_b: -27.92 to -31.02 pp) relative to CrossViT, and remains markedly more robust to background perturbations, outperforming ResNet101 by up to +32.32 accuracy points and CrossViT by up to +5.07 points under background-noise conditions.

</details>

### 2. Privacy-Preserving Object Detection for Vision Transformer-Based Models **⭐⭐⭐** (相关度: 70%, 质量: 0.6)

- **arXiv ID**: [2608.20712](https://arxiv.org/abs/2608.20712)  · [📄 PDF](https://arxiv.org/pdf/2608.20712)
- **作者**: Homare Sueyoshi, Kiyoshi Nishikawa, Hitoshi Kiya
- **提交日期**: 2026-08-21 · **分类**: cs.CR, cs.CV
- **摘要（中）**: ①针对视觉Transformer模型在目标检测任务中测试图像敏感视觉信息泄露的问题。②提出首个基于感知加密的目标检测方法，利用ViT的嵌入结构和带密钥的域自适应技术，在加密域中直接进行检测。③相比以往仅关注图像分类的隐私保护研究，该方法首次扩展到目标检测，且无需修改模型架构。④实验表明，在ViTdet检测器上，该方法在保持几乎相同精度的同时，有效保护了视觉信息。
- **摘要（英）**: This paper addresses privacy leakage in ViT-based object detection by proposing the first perceptual encryption method for detection, leveraging ViT embedding structure and key-based domain adaptation. It achieves nearly identical accuracy to unprotected models while ensuring visual protection, marking a novel extension from classification to detection.
- **评估**: 该研究填补了隐私保护目标检测的空白，对自动驾驶等敏感场景有潜在价值，但实验规模有限。
- **核心贡献**: 首次将感知加密应用于ViT目标检测，实现隐私保护与精度兼得。
- **创新点**: 利用ViT嵌入结构和密钥域自适应实现加密域检测。
- **结果**: 在ViTdet上精度几乎无损，视觉保护有效。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose a novel object detection method that enables us to protect sensitive visual information of test images. Previous studies considering visual information protection focus on image classification tasks. This paper proposes an object detection method using perceptual encryption for the first time. The proposed method can achieve almost the same accuracy as that of models without any protection by utilizing the embedding structure of the Vision Transformer (ViT) and a domain adaptation technique with keys. In experiments, the effectiveness of the proposed method is verified in terms of accuracy and visual protection under the use of ViTdet, which is a ViT-based object detection model.

</details>

---

## Open Vocabulary Detection

### 1. Stream3Dv2: Geometric-Semantic Fusion Enhanced Streaming Zero-Shot 3D Scene Understanding **⭐⭐⭐⭐** (相关度: 85%, 质量: 0.8)

- **arXiv ID**: [2608.21136](https://arxiv.org/abs/2608.21136)  · [📄 PDF](https://arxiv.org/pdf/2608.21136)
- **作者**: Jie Xu, Na Zhao
- **提交日期**: 2026-08-21 · **分类**: cs.CV
- **摘要（中）**: ①针对开放词汇零样本3D场景理解中，流式RGB-D输入处理效率低和2D分割掩码噪声敏感的问题。②提出了Stream3Dv2，一个无需训练的框架，通过嵌套的局部到历史架构处理序列数据，捕捉多视角一致性并降低计算开销；核心是几何-语义融合机制，利用语义指导解决几何噪声和语义歧义，将3D分割建模为点集合并与划分问题；还提出了基于流形距离的点云细化策略。③相比现有方法，Stream3Dv2无需训练即可处理流式输入，并显式处理噪声掩码。④实验表明，Stream3Dv2在流式3D感知任务中实现了鲁棒性能，但摘要未提供具体数值。
- **摘要（英）**: This paper addresses the inefficiency and noise sensitivity of streaming RGB-D inputs in open-vocabulary zero-shot 3D scene understanding. Stream3Dv2, a training-free framework, uses a nested local-to-historical architecture and a geometric-semantic fusion mechanism to handle multi-view consistency and noise, with a manifold-distance-based refinement strategy. It demonstrates robust performance in streaming 3D perception, though specific metrics are not detailed.
- **评估**: 该工作针对开放词汇3D感知的流式部署难题，提出无需训练的鲁棒方案，具有实际意义。
- **核心贡献**: 提出Stream3Dv2，一个无需训练的流式零样本3D场景理解框架。
- **创新点**: 引入几何-语义融合和流形距离细化，解决噪声和语义歧义。
- **结果**: 在流式3D感知中实现鲁棒性能，但摘要未给出具体数值。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, open-vocabulary zero-shot 3D scene understanding using vision foundation models has emerged as a promising alternative to data-intensive supervised methods. However, deploying these models in real-world scenarios is severely hindered by their inability to efficiently handle streaming RGB-D inputs and their inherent vulnerability to noise 2D segmentation masks. To address these critical limitations, we propose Stream3Dv2, a novel training-free framework designed for robust streaming 3D perception. Stream3Dv2 processes sequential data through an original nested local-to-historical architecture, capturing multi-view consistency while circumventing the high computational overhead so as to support timely responses. At its core, we introduce a comprehensive geometric-semantic fusion mechanism that resolves geometric noise and semantic ambiguity by explicitly utilizing semantic guidance and formulating 3D segmentation as solving point-and-set merging and partitioning problems. Furthermore, we present an innovative manifold-distance-based point cloud refinement strategy. This approach leverages local manifold graphs for point-to-manifold optimization that mitigates the boundary delineation failures caused by Euclidean-distance metrics, and employs geometric bounding boxes to dynamically activate and update historical instances for achieving rapid manifold-to-manifold refinement. Extensive experiments on public datasets demonstrate that Stream3Dv2 consistently outperforms existing baselines in foundational open-vocabulary streaming 3D segmentation and detection. Finally, we show that integrating our framework with an LLM-based agent enables advanced language-driven 3D scene understanding, underscoring its potential for open-world embodied intelligence. Code will be updated at https://github.com/SubmissionsIn/Stream3D.

</details>

### 2. Lift, Associate, and Fuse: A Decision-Centric Framework for 2D-to-3D Foundation Model Transfer **⭐⭐⭐** (相关度: 70%, 质量: 0.75)

- **arXiv ID**: [2608.20659](https://arxiv.org/abs/2608.20659)  · [📄 PDF](https://arxiv.org/pdf/2608.20659)
- **作者**: Wentao Sun, Yiping Chen, John S. Zelek et al. (4 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV
- **摘要（中）**: ①针对2D基础模型预测向3D分割迁移时，系统决策（如证据落地、身份识别、语义冲突处理）缺乏统一理解的问题。②提出了Lift, Associate, and Fuse (LAF)框架，将迁移系统表示为五个算子：生成、关联、调和、融合和持久化/查询，并定义了持久载体的显式契约，识别证据丢弃不可恢复的首个阶段。③相比按任务或表示分组的现有方法，LAF提供了决策中心的审计协议，适用于多种载体类型。④将该框架应用于161个系统，进行了表示、时间、关系和前馈压力测试，但摘要未提供具体结果。
- **摘要（英）**: This paper addresses the lack of unified understanding of decisions in transferring 2D foundation model predictions to 3D segmentation. LAF proposes a decision-centric framework with five operators and an explicit contract for the persistent carrier, enabling structured audits. Applied to 161 systems, it identifies unrecoverable evidence stages, though specific results are not detailed.
- **评估**: 该工作提供了系统化分析框架，对理解2D到3D迁移方法有理论价值，但实用性有限。
- **核心贡献**: 提出LAF框架，以决策为中心统一2D到3D基础模型迁移的审计协议。
- **创新点**: 定义五算子框架和持久载体契约，识别证据丢弃关键阶段。
- **结果**: 应用于161个系统，但摘要未提供具体性能数据。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Methods that transfer predictions from two-dimensional foundation models into three-dimensional segmentation are commonly grouped by task or representation. Those groupings obscure the decisions that determine whether a system remains coherent across views: where image evidence is grounded, when observations become one identity, how semantic and granularity conflicts are handled, which information is fused, and what state survives for later queries. We introduce \textbf{Lift, Associate, and Fuse (LAF)}, a decision-centric framework that represents a transfer system as five operators: \textbf{Generate, Associate, Reconcile, Fuse, and Persist/Query}. LAF defines an explicit contract for the persistent carrier---its spatial support, semantic state, identity state, uncertainty, provenance, and supported operations---and identifies the first stage at which discarded evidence becomes unrecoverable. We operationalize the framework as a structured audit protocol and apply it to 161 systems available through 7 August 2026, spanning point-, field-, Gaussian-, object-, graph-, and memory-based carriers. Representation, temporal, relational, and feed-forward stress tests required no additional analytical stage after the final confirmation pass. The resulting decision traces expose four recurring properties: association does not establish identity; carrier design fixes both the query interface and correction boundary; rendered-view, native-3D, and proposal-level evaluations are not interchangeable; and qualifiers such as \emph{training-free}, \emph{real-time}, \emph{open-vocabulary}, and \emph{generalizable} are meaningful only when attached to a stage and a complete cost ledger. LAF therefore supplies a representation-neutral method for comparing existing systems, diagnosing irreversible failures, and specifying revisable 3D perception for future agents.

</details>

---

## Knowledge Distillation

### 1. Semantically Compatible Knowledge Distillation for Cross-Domain Object Detection with Vision Foundation Models **⭐⭐⭐⭐** (相关度: 90%, 质量: 0.85)

- **arXiv ID**: [2608.20916](https://arxiv.org/abs/2608.20916)  · [📄 PDF](https://arxiv.org/pdf/2608.20916)
- **作者**: Qifeng Zhang, Ting Xiang, Zeyuan Bai et al. (4 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV
- **摘要（中）**: ①这篇论文针对基于视觉基础模型（VFM）的跨域目标检测中，教师和学生特征图之间的空间尺度差异导致语义不兼容，以及域偏移导致教师模型漏检目标的问题。②提出了语义定位增强教师（SLE-T），一个围绕轻量级SLE适配器构建的语义兼容知识蒸馏框架，用于DINOv2，注入预训练局部纹理先验并重构特征为与学生检测器兼容的密集表示。③相比已有工作，SLE-T通过适配器解决了空间尺度差异和伪标签质量问题。④在三个DAOD基准上的大量实验表明，SLE-T与更大的DINOv2-G教师相比，性能更优或相当。
- **摘要（英）**: This paper addresses spatial-scale discrepancy and semantic incompatibility in VFM-based cross-domain object detection by proposing SLE-T, a semantically compatible knowledge-distillation framework with a lightweight SLE Adapter for DINOv2 that injects local-texture priors and reformulates features into dense representations. Extensive experiments on three DAOD benchmarks demonstrate that SLE-T with DINOv2-B/L outperforms or matches the larger DINOv2-G teacher.
- **评估**: 该论文针对跨域检测中的知识蒸馏提出了有效的语义兼容方案，对利用VFM进行域自适应检测有重要参考意义。
- **核心贡献**: 提出了SLE-T框架，通过SLE适配器实现语义兼容的知识蒸馏用于跨域目标检测。
- **创新点**: 通过注入局部纹理先验和特征重构解决教师-学生特征空间尺度差异。
- **结果**: 在三个DAOD基准上，SLE-T与更大的DINOv2-G教师相比性能更优或相当。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision foundation models (VFMs) offer strong generalization capabilities for domain-adaptive object detection (DAOD). However, existing VFM-based methods overlook the spatial-scale discrepancy between teacher and student feature maps, resulting in semantic incompatibility that weakens both feature alignment and pseudo-label learning. Moreover, domain shift can cause source-trained VFM teachers to miss target-domain objects, limiting the quality of their pseudo-labels. To address these issues, we propose the Semantic Localization-Enhanced Teacher (SLE-T), a semantically compatible knowledge-distillation framework built around a lightweight SLE Adapter for DINOv2. SLE Adapter injects pretrained local-texture priors into DINOv2 to improve cross-domain recognition and reformulates its features into dense representations that are spatially and semantically compatible with the student detector. SLE-T transfers the resulting teacher knowledge through either pseudo-label learning or feature alignment. We instantiate SLE-T with DINOv2-B and DINOv2-L (the ViT-B and ViT-L variants) and compare them with the larger DINOv2-G teacher. Extensive experiments on three DAOD benchmarks demonstrate that our method achieves state-of-the-art performance, and ablation studies confirm the importance of teacher-student semantic compatibility. Notably, SLE-T with DINOv2-B produces competitive or superior pseudo-labels using approximately one-quarter of the training time of DINOv2-G and substantially less GPU memory, demonstrating efficient VFM knowledge transfer under limited computational resources.

</details>

---

## BEV

### 1. CoAnchor: Robust Collaborative Perception under Spatio-Temporal Misalignment via Object-Level Anchors **⭐⭐⭐⭐** (相关度: 90%, 质量: 0.85)

- **arXiv ID**: [2608.21055](https://arxiv.org/abs/2608.21055)  · [📄 PDF](https://arxiv.org/pdf/2608.21055)
- **作者**: Chi Li, Rui Lin, Aobo Ji et al. (4 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV, cs.AI
- **摘要（中）**: ①针对协同感知中通信延迟和相对位姿噪声导致的时空错位问题，现有方法通常分别处理空间或时间维度，缺乏统一高效的解决方案。②提出了CoAnchor，一个以锚点为中心的时空对齐框架，构建稀疏对象级时空锚点作为共享接口，将空间细化、时间传播和当前时间验证紧密集成在一个统一循环中，同时保持轻量级。③相比现有方法，CoAnchor在统一框架内联合处理时空错位，避免了密集BEV特征上的直接推理，提高了效率。④在模拟和真实数据集上的广泛实验表明，CoAnchor在干净设置下保持竞争力，并在联合错位条件下提升了鲁棒性。
- **摘要（英）**: This paper addresses spatio-temporal misalignment in collaborative perception caused by communication delay and pose noise, proposing CoAnchor, an anchor-centric framework that builds sparse object-level anchors for unified pose correction. It tightly couples spatial refinement, temporal propagation, and current-time verification in a lightweight loop. Experiments show competitive performance in clean settings and improved robustness under joint misalignment.
- **评估**: 该工作针对协同感知的实际部署难题，提出统一高效的时空对齐方案，具有较强应用价值。
- **核心贡献**: 提出CoAnchor，以对象级锚点为中心的协同感知时空对齐框架。
- **创新点**: 利用稀疏锚点作为共享接口，统一处理空间和时间错位。
- **结果**: 在联合错位条件下显著提升鲁棒性，同时保持干净设置下的竞争力。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Collaborative perception extends the sensing range of a single vehicle by fusing observations from nearby agents, which improves the robustness of autonomous driving. In realistic deployments, however, the received collaborator messages are often affected by both communication delay and relative-pose noise, which jointly cause stale observations, spatial misalignment, and unstable feature fusion. Existing methods usually address these issues from either the spatial or temporal side, but handling them jointly in a unified and efficient manner remains challenging. In this paper, we propose CoAnchor, an anchor-centric spatio-temporal alignment framework for asynchronous collaborative perception. Instead of directly reasoning on dense BEV features, CoAnchor builds sparse object-level spatio-temporal anchors as a shared interface for pose correction and tightly connects spatial refinement, temporal propagation, and current-time verification within one unified loop, while keeping the overall correction process lightweight. Extensive experiments on both simulated and real-world datasets illustrate that CoAnchor remains competitive under clean settings and improves the robustness under joint delay and pose perturbations with a favorable practical accuracy-efficiency trade-off.

</details>

---

## 📊 统计

| 领域 | 论文数 |
|------|--------|
| VLM | 10 |
| Multimodal | 10 |
| Multi-camera Perception | 6 |
| Network Pruning | 5 |
| Video Understanding | 3 |
| Self-supervised Vision | 3 |
| Vision Transformer | 2 |
| Open Vocabulary Detection | 2 |
| Knowledge Distillation | 1 |
| BEV | 1 |
| **总计** | **43** |