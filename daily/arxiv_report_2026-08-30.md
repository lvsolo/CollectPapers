# 📚 arXiv 每日论文报告（我的领域）

**报告日期**: 2026-08-30  
**论文来源**: [arXiv cs.CV Recent](https://arxiv.org/list/cs.CV/recent)  
**关注论文数**: 10 篇（其中 10 篇经大模型中文评估）

> 匹配领域: Object Detection、Autonomous Driving、3D Detection、BEV、Occupancy、Multi-camera Perception、Tracking、Open-set Detection、FOD Detection、VLM、Vision Transformer、Self-supervised Vision、Video Understanding、Multimodal、Continual Learning、Neural Architecture Search、Network Pruning、Knowledge Distillation

## 📑 目录

- [VLM](#vlm) (9篇)
- [Multimodal](#multimodal) (1篇)

## VLM

### 1. ReViCo: Unveiling the Limitations of VLMs in Visual Text Understanding via Error Correction **⭐⭐⭐** (相关度: 70%, 质量: 0.7)

- **arXiv ID**: [2608.27154](https://arxiv.org/abs/2608.27154)  · [📄 PDF](https://arxiv.org/pdf/2608.27154)
- **作者**: Bojun Zhang, Junhong Liang, Feifei Zhai et al. (5 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-27 · **分类**: cs.CV
- **摘要（中）**: 这篇论文针对视觉语言模型（VLM）在图像中文本理解方面的不足，提出了一个名为ReViCo的基准测试，通过视觉文本纠错任务来评估模型。该任务要求模型识别并修正真实世界图像中的文本错误，需要深入理解视觉文本与其周围视觉上下文的交互。实验表明，即使最好的VLM与人类表现之间也存在显著差距，且大多数模型难以准确感知视觉文本，导致频繁的纠错错误。ReViCo为开发更鲁棒和文本感知的VLM提供了新的基准基础。
- **摘要（英）**: This paper addresses the limitations of Vision Language Models (VLMs) in understanding text within images by introducing ReViCo, a benchmark for visual text error correction. It evaluates models on identifying and fixing text errors in real-world images, revealing a significant performance gap between even the best VLMs and humans. The benchmark provides a foundation for developing more robust and text-aware VLMs.
- **评估**: 该论文通过新颖的纠错任务揭示了VLM在视觉文本理解上的关键缺陷，对多模态感知研究有参考价值，但领域相关性中等。
- **核心贡献**: 提出了ReViCo基准，用于评估VLM在视觉文本纠错任务中的能力。
- **创新点**: 设计了视觉文本纠错任务，强调视觉上下文与文本的交互理解。
- **结果**: 实验显示VLM与人类表现差距显著，多数模型纠错错误频繁。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision Language Models (VLMs) have shown great success in general visual tasks, yet they still struggle to deeply understand text within images. In this paper, we introduce ReViCo (Real Visual Correction), a benchmark designed to evaluate VLM text understanding through a novel task of visual text error correction. ReViCo challenges models to identify and fix text errors in real-world images, which requires a profound understanding of the interplay between visual text and its surrounding visual context. We benchmark various VLMs using two distinct paradigms: prompt-based strategy and targeted model training, both aimed at pushing the limits of current models. Our experiments reveal a striking performance gap between even the best VLMs and human, and further analysis also shows that most models struggle to accurately perceive the visual text, resulting in frequent correction errors. By highlighting these gaps, ReViCo provides a new benchmark foundation for developing more robust and text-aware VLMs.

</details>

### 2. Ancient-Bench: A Comprehensive Multi-millennial, Multi-medium, and Multi-script Benchmark for Ancient Chinese Artifact Text Recognition **⭐⭐⭐** (相关度: 60%, 质量: 0.75)

- **arXiv ID**: [2608.27169](https://arxiv.org/abs/2608.27169)  · [📄 PDF](https://arxiv.org/pdf/2608.27169)
- **作者**: Hiuyi Cheng, Nuo Xu, Yuyi Zhang et al. (12 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/SCUT-DLVCLab/Ancient_Bench](https://github.com/SCUT-DLVCLab/Ancient_Bench)
- **提交日期**: 2026-08-27 · **分类**: cs.CV
- **摘要（中）**: 这篇论文针对中国古代文物文本识别基准的碎片化问题，提出了Ancient-Bench，一个包含2700张图像的综合基准，涵盖三千年字符演变、九种文物类别和七种历史字体。他们定义了三种针对古代文本特性的标注标准，以确保跨异构媒介的一致评估。实验表明，通用VLM和OCR专用模型在古代文本识别上仍未解决，存在变体字符、专业符号和幻觉等挑战。
- **摘要（英）**: This paper addresses the fragmentation of ancient Chinese artifact text recognition benchmarks by introducing Ancient-Bench, a comprehensive benchmark with 2,700 images spanning 3,000 years, nine artifact categories, and seven script forms. It defines three annotation standards for consistent evaluation across heterogeneous media. Experiments reveal that ancient text recognition remains unsolved for both VLMs and OCR models, with challenges in variant characters and hallucinations.
- **评估**: 该论文提供了领域内稀缺的古代文本基准，对文化遗产数字化有贡献，但与自动驾驶感知相关性较低。
- **核心贡献**: 构建了Ancient-Bench基准，覆盖多时间、多媒介和多字体的古代文本识别。
- **创新点**: 提出了三种针对古代文本特性的标注标准化方法。
- **结果**: 实验表明现有模型在古代文本识别上表现不足，存在显著挑战。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Ancient Chinese artifact text recognition is fundamental to heritage digitization, and benchmarks for ancient texts are essential for evaluating current model capabilities. However, existing benchmarks suffer from ''fragmentation'', manifested in limited temporal coverage, limited medium diversity, and incomplete script types. Therefore, we present Ancient-Bench, a comprehensive benchmark of 2,700 images for ancient Chinese artifact text recognition, featuring three dimensions: Multi-millennial (spanning 3,000 years of character evolution), Multi-medium (covering nine artifact categories), and Multi-script (encompassing seven historical script forms). To enable consistent and fair evaluation across heterogeneous media, we further define three annotation standards tailored to the medium-specific characteristics of ancient texts: symbol standardization, character standardization, and parsing standardization. Extensive experiments on Ancient-Bench covering general Vision-Language Models (VLMs) and OCR-specialist models reveal that ancient Chinese artifact text recognition remains fundamentally unsolved, with persistent challenges in variant characters, specialized symbols, and hallucination. The dataset is available at https://github.com/SCUT-DLVCLab/Ancient_Bench.

</details>

### 3. Visual Information-Guided Parallel Decoding for Diffusion Multimodal Large Language Models **⭐⭐⭐** (相关度: 50%, 质量: 0.7)

- **arXiv ID**: [2608.26580](https://arxiv.org/abs/2608.26580)  · [📄 PDF](https://arxiv.org/pdf/2608.26580)
- **作者**: Insu Lee, Wooje Park, Wonseok Shin et al. (5 authors)
- **🏷️ 机构**: Standigm Inc.
- **提交日期**: 2026-08-27 · **分类**: cs.CV, cs.CL
- **摘要（中）**: 这篇论文针对扩散多模态大语言模型（dMLLMs）中解码顺序对生成质量的影响，提出了视觉信息引导采样器（VIG-Sampler）。该方法根据候选token对图像token的注意力来优先解码，并施加约束以惩罚与已选token图像注意力分布相似的候选，从而增加信息增益。在7个图像描述和VQA基准上，使用3个开源dMLLM的实验证明了VIG-Sampler的有效性。
- **摘要（英）**: This paper addresses the impact of decoding order on generation quality in diffusion multimodal large language models (dMLLMs) by proposing the Visual Information-Guided Sampler (VIG-Sampler). It prioritizes tokens based on their attention to image tokens and penalizes similar attention distributions to increase information gain. Experiments on 7 benchmarks with 3 dMLLMs demonstrate its effectiveness.
- **评估**: 该论文提出了一种创新的解码策略，对多模态生成有改进，但与应用领域相关性一般。
- **核心贡献**: 提出了VIG-Sampler，利用图像注意力指导dMLLM的解码顺序。
- **创新点**: 结合图像注意力分布和多样性约束来优化token选择。
- **结果**: 在多个基准上验证了方法有效性，提升了生成质量。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Diffusion multimodal large language models (dMLLMs) have recently emerged as a new decoding paradigm for multimodal generation. Starting from a fully masked sequence, dMLLMs progressively decode the sequence by unmasking a subset of the remaining masked positions at each step. Since the selected tokens serve as the prediction context for subsequent steps, deciding which tokens to decode is crucial to the quality of the final output. The most common strategy prioritizes tokens based on a certainty measure that tends to favor tokens frequently observed in the training data. Recent approaches instead order tokens according to their influence on subsequent predictions, but do not explicitly account for the input image. We propose the Visual Information-Guided Sampler (VIG-Sampler), which prioritizes tokens based on their attention to image tokens. We further impose a constraint that penalizes candidate tokens whose image-attention distributions are similar to those of previously selected tokens, thereby increasing the information gain of the decoded subset. Extensive experiments on 7 captioning and VQA benchmarks with 3 open-source dMLLMs demonstrate the effectiveness of VIG-Sampler, which outperforms the Info-Gain Sampler by an average of 19.3 CIDEr points across the captioning benchmarks and surpasses it on COCO Caption while using only half as many decoding steps.

</details>

### 4. 4DSynth: Controllable Procedural World Synthesis for Dynamic Embodied Simulation **⭐⭐⭐⭐** (相关度: 85%, 质量: 0.8)

- **arXiv ID**: [2608.26947](https://arxiv.org/abs/2608.26947)  · [📄 PDF](https://arxiv.org/pdf/2608.26947)
- **作者**: Zehao Qi, Haochen Luo, Jia-Wang Bian et al. (5 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-27 · **分类**: cs.RO, cs.CV
- **摘要（中）**: 这篇论文针对具身智能体需要视觉多样、物理交互和随时间变化的环境，提出了4DSynth，一个可控的程序化系统，可将自然语言描述、蓝图掩码或单张照片转换为可编辑的4D环境，包含显式几何、动画角色、无碰撞轨迹和物理就绪状态。他们构建了4DSynth-Nav导航基准，评估两个视觉语言模型，发现它们在多数任务上失败并停滞。该系统展示了程序化可控性在生成动态仿真环境中的潜力。
- **摘要（英）**: This paper addresses the need for visually diverse, interactive, and dynamic environments for embodied agents by proposing 4DSynth, a controllable procedural system that converts natural language, blueprints, or photos into editable 4D environments. It includes explicit geometry, animated actors, and physics-ready states. The 4DSynth-Nav benchmark shows that current VLMs fail most navigation tasks, highlighting the system's utility for testing.
- **评估**: 该论文对自动驾驶仿真环境生成有重要价值，提供了可控的4D世界合成方法，相关性高。
- **核心贡献**: 提出了4DSynth系统，实现从多种输入生成可控4D仿真环境。
- **创新点**: 统一了多模态输入到几何接地表示，支持动画和物理仿真。
- **结果**: 构建的基准显示现有VLM在导航任务上表现不佳，验证了系统挑战性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Embodied agents need environments that are visually diverse, physically interactive, and changing over time. Procedural simulators can generate large interactive scene collections, and recent 4D generators produce compelling visual dynamics. Combining these properties in one environment, however, still demands extensive manual effort, and the result is rarely editable or controllable enough to reuse at scale. We present 4DSynth, a controllable procedural system that turns a natural-language description, a blueprint mask, or a single photograph into an editable 4D environment with explicit geometry, animated actors, collision-free trajectories, and physics-ready simulation state. Multiple scene routes share one geometry-grounded representation, so the same pipeline handles animation, camera planning, rendering, and task generation. To validate the full pipeline, we construct 4DSynth-Nav, an interactive navigation benchmark generated entirely from 4DSynth's procedural scenes. Two vision-language models evaluated across three difficulty tiers both fail the majority of tasks and stall after early subtasks. The same procedural controllability that produces these environments also makes each failure reproducible and each difficulty axis independently tunable. This paper presents both a controllable generation pipeline and the scalable benchmark it enables, offering a practical foundation for developing and evaluating embodied agents.

</details>

### 5. Reason in the Words You Speak: Idiolectal Paraphrasing Off-Policy Traces for Reasoning Distillation in VideoLLMs **⭐⭐⭐⭐** (相关度: 75%, 质量: 0.8)

- **arXiv ID**: [2608.26684](https://arxiv.org/abs/2608.26684)  · [📄 PDF](https://arxiv.org/pdf/2608.26684)
- **作者**: Ji Soo Lee, Jinyoung Park, Seohyun Lee et al. (7 authors)
- **🏷️ 机构**: Korea University
- **提交日期**: 2026-08-27 · **分类**: cs.CV
- **摘要（中）**: 这篇论文针对GRPO在推理任务中受限于模型自身生成轨迹的问题，提出了Echo-GRPO框架，通过将教师模型的推理轨迹重写为学生模型自身的语言风格（idiolect），同时用双参考解码保持语义，来避免梯度裁剪问题。实验表明，该方法使模型能学习更高级的推理能力，超越了直接模仿教师轨迹的方法。
- **摘要（英）**: This paper addresses the limitation of GRPO in reasoning tasks, where on-policy optimization restricts learning to the model's own capabilities. It proposes Echo-GRPO, which rewrites teacher reasoning traces into the student's idiolect using dual-reference decoding to preserve semantics. Experiments show improved reasoning performance over direct imitation.
- **评估**: 该论文对视频推理蒸馏有创新贡献，方法设计巧妙，对多模态推理研究有参考价值。
- **核心贡献**: 提出了Echo-GRPO框架，通过idiolect重写解决推理蒸馏中的分布不匹配。
- **创新点**: 利用双参考解码将教师轨迹适配到学生语言风格。
- **结果**: 实验证明提升了模型推理能力，优于基线方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent large language models achieve strong performance on complex reasoning tasks, where reinforcement learning with Group Relative Policy Optimization (GRPO) has emerged as a leading paradigm for optimizing models on self-generated trajectories. However, the on-policy nature of GRPO bounds the model to the reasoning skills it can already produce, restricting to learn more advanced capabilities. Prior works inject privileged reasoning traces from a stronger teacher policy to guide training, yet these traces are inherently out of distribution with respect to the student policy. We observe that this mismatch between on-policy and off-policy causes gradient clipping on semantically critical reasoning tokens, ultimately rewarding correct answers while leaving the reasoning that justifies them unlearned. Hence, we propose \textbf{Echo-GRPO}, a framework that lets the model reason in the words it speaks. Rather than imitating low-probability privileged traces from the teacher model, Echo-GRPO rewrites them into the student policy's own \textit{idiolect}, that is, its own characteristic vocabulary and expression patterns, while preserving their semantics via Dual-Reference Decoding. We instantiate this framework as \textbf{VideoEcho-R1} for video reasoning distillation, achieving consistent improvements across three multimodal LLM backbones and five benchmarks. Finally, we show that our idiolectal paraphrasing is a plug-in module that consistently improves both RL and supervised fine-tuning frameworks for reasoning distillation, demonstrating that policy-aligned supervision extends beyond GRPO.

</details>

### 6. UrbanGround: From Local Perception to Spatial Agency in a Real-Scale City **⭐⭐⭐⭐** (相关度: 90%, 质量: 0.85)

- **arXiv ID**: [2608.27456](https://arxiv.org/abs/2608.27456)  · [📄 PDF](https://arxiv.org/pdf/2608.27456)
- **作者**: Tianjie Ju, Zheng Wu, Yueqing Sun et al. (18 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-27 · **分类**: cs.CV
- **摘要（中）**: 这篇论文针对多模态大语言模型（MLLM）在城市环境中从局部感知到空间行动的问题，提出了UrbanGround，一个基于香港3D地理空间数据构建的真实尺度城市沙盒。它支持第一人称视角的闭环交互和交互式地图导航，通过三个研究问题分析智能体的空间接地和导航能力。实验表明，当代MLLM智能体在原子视觉识别上有用，但在复杂城市导航中表现不足。
- **摘要（英）**: This paper addresses the challenge of turning local urban perception into reliable action for MLLM agents by proposing UrbanGround, a sandbox built from Hong Kong's 3D geospatial data. It supports closed-loop first-person interaction and map-based navigation. Analysis shows that current MLLM agents have useful atomic abilities but fail in complex navigation tasks.
- **评估**: 该论文对自动驾驶和城市感知研究高度相关，提供了真实尺度的测试平台，揭示了MLLM在空间推理上的局限。
- **核心贡献**: 构建了UrbanGround沙盒，用于测试MLLM在真实城市环境中的空间行动能力。
- **创新点**: 结合真实3D城市数据和闭环交互，支持多尺度空间问题分析。
- **结果**: 实验显示MLLM在复杂导航任务中表现不足，强调了空间代理的挑战。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal large language models (MLLMs) can interpret a street view, but urban agency depends on whether such local evidence remains useful after the agent starts to move. In this paper, we investigate how far current MLLM agents can turn local urban perception into reliable action in a complicated real-scale city. We propose UrbanGround, the first sandbox to make this question testable in a physically constrained replica of Hong Kong built from territory-wide 3D geospatial data. UrbanGround supports closed-loop interaction from a first-person view and provides an interactive map for navigation. Agents can directly enter the 3D city and explore from a first-person view. Our analysis follows the growth of the spatial problem through three research questions. We first test whether an agent can ground a local scene well enough to answer spatial questions after active observation. Then we ask whether that grounding supports navigation as destinations become farther away and less explicit. Finally, we examine whether the resulting behavior survives changes in route availability and pedestrian motion. Contemporary MLLM agents usually show useful atomic abilities in visual recognition and short-range spatial reasoning, while orientation and pedestrian-aware movement remain unreliable. Their central failure emerges over extended exploration, where local abilities do not compose into sustained goal-directed behavior and errors accumulate without effective correction. We hope UrbanGround will support broader study of how far current MLLM agents can explore reliably in complex, open-ended urban environments.

</details>

### 7. SAGE: Variate-Wise Semantic Augmentation for Vision-Language Time Series Forecasting **⭐⭐** (相关度: 10%, 质量: 0.6)

- **arXiv ID**: [2608.26829](https://arxiv.org/abs/2608.26829)  · [📄 PDF](https://arxiv.org/pdf/2608.26829)
- **作者**: Haizhao Fan, Xinyi Le
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-27 · **分类**: cs.LG, cs.CV
- **摘要（中）**: 该论文针对时间序列预测中缺乏语义知识的问题，提出SAGE框架，利用CLIP联合建模时间、跨变量、文本和视觉信息。通过CLIP文本编码器处理频率增强补丁和变量令牌，并用门控残差路径注入变量描述和统计描述符，同时冻结的视觉编码器通过对比目标对齐渲染序列与时间表示。相比依赖LLM或统一文本提示的方法，SAGE避免了推理时的高计算成本，并考虑了变量间的异质语义。在八个长期基准和M4上取得了最先进的结果。
- **摘要（英）**: This paper addresses the lack of semantic knowledge in time series forecasting by proposing SAGE, a CLIP-based framework that jointly models temporal, cross-variable, textual, and visual information. It uses the CLIP text encoder for frequency-enhanced patches and variable tokens, and a frozen vision encoder for contrastive alignment, avoiding LLM inference costs and handling heterogeneous variate semantics. SAGE achieves state-of-the-art results on eight long-term benchmarks and M4.
- **评估**: 该论文与自动驾驶感知领域相关性极低，主要面向通用时间序列预测，但方法上融合多模态信息有一定参考价值。
- **核心贡献**: 提出了一个无需LLM推理的CLIP-based多模态时间序列预测框架。
- **创新点**: 利用CLIP双编码器同时注入文本和视觉监督，实现变量级语义增强。
- **结果**: 在多个长期预测基准上达到最先进性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Time series forecasting models operate on raw numerical sequences, lacking the semantic knowledge that domain experts implicitly leverage, such as the physical meaning of each variable, its statistical behavior, and its temporal dynamics. Recent efforts to bridge this gap fall into two camps. Some rely on large language models at inference time, which is computationally expensive. Others apply uniform textual prompts at the dataset level, ignoring the heterogeneous semantics across individual variates. We propose SAGE (Seeing and Augmenting with Grounded Encoding), an end-to-end CLIP-based framework that jointly models temporal, cross-variable, textual, and visual information. The CLIP text encoder processes frequency-enhanced patches and variable tokens, while gated residual paths inject variable-specific descriptions and statistical descriptors. In parallel, the frozen CLIP vision encoder aligns rendered series with temporal representations through a training-only contrastive objective. This dual use of CLIP adds complementary semantic and visual supervision without placing an LLM in the forecasting loop. Across eight long-term benchmarks and M4, SAGE achieves state-of-the-art accuracy. Ablations confirm complementary gains from multimodal alignment and variable-level knowledge.

</details>

### 8. LiveVVT: High-Fidelity Video Virtual Try-On in Real Time **⭐⭐** (相关度: 15%, 质量: 0.7)

- **arXiv ID**: [2608.26714](https://arxiv.org/abs/2608.26714)  · [📄 PDF](https://arxiv.org/pdf/2608.26714)
- **作者**: Yushe Cao, Shikun Feng, Ruxiang Duan et al. (7 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-27 · **分类**: cs.CV, cs.AI
- **摘要（中）**: 该论文针对视频虚拟试穿中扩散模型因完整片段依赖导致的高延迟和计算开销问题，提出LiveVVT，一个滚动流式扩散框架，在因果循环生成中保持有界双向建模。通过固定大小窗口内联合去噪多个视频块，并利用有界时间记忆和全局外观记忆维持长期一致性，同时引入渐进式蒸馏框架加速推理。相比现有方法，LiveVVT在保持高保真度的同时实现了实时生成。
- **摘要（英）**: This paper addresses the prohibitive latency and computational overhead of diffusion-based video virtual try-on by proposing LiveVVT, a rolling streaming diffusion framework that preserves bounded bidirectional modeling within causal recurrent generation. It uses a fixed-size window for joint denoising and complementary memories for long-term consistency, along with progressive distillation for real-time inference. LiveVVT achieves high-fidelity synthesis with significantly reduced latency.
- **评估**: 该论文聚焦视频生成与虚拟试穿，与自动驾驶感知领域关联较弱，但流式扩散和蒸馏技术可能对视频理解有间接启发。
- **核心贡献**: 提出了首个实时高保真视频虚拟试穿流式扩散框架。
- **创新点**: 在因果生成中保留有界双向建模，并设计双记忆机制维持一致性。
- **结果**: 实现了实时视频虚拟试穿，同时保持高视觉保真度。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Diffusion-based Video Virtual Try-On (VVT) achieves high visual fidelity through bidirectional spatio-temporal modeling, but complete-clip dependence incurs prohibitive latency and computational overhead in practical continuous deployment. Naively enforcing causality disrupts pretrained bidirectional priors and substantially degrades synthesis quality. We introduce LiveVVT, a rolling streaming diffusion framework that preserves bounded bidirectional modeling within causal recurrent generation. Within a fixed-size window, LiveVVT jointly denoises multiple video chunks under bounded look-ahead, preserving local bidirectional interactions while emitting one clean chunk per iteration. Beyond the window, two complementary memories sustain long-term consistency: a bounded temporal memory propagates recent dynamics and occlusion context, whereas a persistent global appearance memory, constructed once from the target garment and a frontal try-on keyframe, anchors garment details and dressed appearance throughout the stream. We further introduce a progressive distillation framework integrating bidirectional VVT learning, teacher-trajectory regression for causal few-step adaptation, and Collaborative Matching Distillation, which couples teacher-distribution matching with rolling flow matching on real videos to align optimization with recurrent inference. Experiments on paired and unpaired long-sequence benchmarks demonstrate superior generation quality over similarly sized models, with $26\times$ lower latency and $11\times$ higher throughput, enabling high-fidelity real-time streaming VVT.

</details>

### 9. AesCanvas: A Large-Scale Dataset and Benchmark for Aesthetic Critique and Contextual Suitability **⭐⭐⭐** (相关度: 20%, 质量: 0.8)

- **arXiv ID**: [2608.26713](https://arxiv.org/abs/2608.26713)  · [📄 PDF](https://arxiv.org/pdf/2608.26713)
- **作者**: Xuanwei Hu, Haoyu Dong, Kejun Wu et al. (5 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-27 · **分类**: cs.CV, cs.AI
- **摘要（中）**: 该论文针对现有图像美学评估基准仅关注内在视觉质量或固定领域标准的问题，提出AesCanvas，一个包含CritiqueCanvas和ContextCanvas的统一套件，分别提供大规模多维度美学批评数据和专家审核的上下文适用性评估。通过统一协议评估闭源、开源通用和美学专用MLLM，发现批评生成与上下文敏感判断之间存在明显分离，美学专用模型在批评指标上表现良好但在上下文评估上落后于通用模型。
- **摘要（英）**: This paper addresses the limitation of existing image aesthetic assessment benchmarks that focus only on intrinsic quality or fixed criteria by introducing AesCanvas, a unified suite with CritiqueCanvas for large-scale multi-dimensional critique and ContextCanvas for contextual suitability evaluation. It evaluates various MLLMs under a unified protocol, revealing a gap between critique generation and context-sensitive judgment, with aesthetic specialists lagging on contextual tasks.
- **评估**: 该论文与自动驾驶感知领域相关性较低，但多模态评估方法可能对VLM在驾驶场景中的适用性研究有参考意义。
- **核心贡献**: 构建了首个同时评估美学批评和上下文适用性的大规模基准套件。
- **创新点**: 将美学评估从内在质量扩展到上下文适用性，并设计双组件基准。
- **结果**: 揭示了不同MLLM在批评和上下文任务上的性能差异。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advances in Multimodal Large Language Models (MLLMs) have extended Image Aesthetic Assessment (IAA) beyond scalar scores toward interpretable critique and guidance. Yet existing benchmarks mainly assess intrinsic visual quality or fixed domain criteria, leaving open whether an appealing image is appropriate for a specific purpose, audience, cultural setting, or domain convention. We introduce AesCanvas, a unified suite with two complementary components: CritiqueCanvas with 519,136 instruction-response pairs from 54,300 images supports long-form, multi-dimensional critique across photography, painting, and virtual imagery, whereas ContextCanvas with 301 expert-reviewed use scenarios evaluates contextual aesthetic suitability in realistic use scenarios. Under a unified protocol, we evaluate closed-source frontier, open-weight general, and aesthetic-specific MLLMs. Results reveal a clear separation between critique generation and context-sensitive judgment: reference-based lexical and semantic metrics only partially capture critique quality, while aesthetic specialists remain competitive on selected critique metrics yet substantially lag strong general-purpose MLLMs on ContextCanvas. Further analyses show that aesthetic specialization does not reliably transfer to contextual suitability and that model decisions may fail to track or ground themselves in decisive contextual visual cues. These findings establish culturally situated, evidence-grounded suitability as a distinct objective for aesthetic modeling.

</details>

---

## Multimodal

### 1. Video-FLAIR: Not Whether to Reason, But How **⭐⭐⭐⭐** (相关度: 70%, 质量: 0.85)

- **arXiv ID**: [2608.26495](https://arxiv.org/abs/2608.26495)  · [📄 PDF](https://arxiv.org/pdf/2608.26495)
- **作者**: Yogesh Kulkarni, Pooyan Fazli
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-27 · **分类**: cs.CV
- **摘要（中）**: 该论文针对多模态查询需要不同类型推理（感知、组合、深思）但现有方法采用统一推理策略的问题，提出Video-FLAIR，一个通过强化学习学习为每个查询选择合适推理模式的训练框架。训练时模型对同一提示生成三种模式的响应，通过复合奖励比较正确性、接地性和成本，生成监督信号，无需逐查询标注。相比Qwen2.5-VL基线，Video-FLAIR在MathVista、Video-Holmes和Video-MMMU上分别提升+5.4、+4.8和+4.8，同时平均token使用量从417降至95。
- **摘要（英）**: This paper addresses the issue of uniform reasoning strategies in multimodal models by proposing Video-FLAIR, a training framework that uses reinforcement learning to select the appropriate reasoning mode per query. It generates responses under three modes and uses a composite reward to favor the most effective one based on correctness, grounding, and cost, without per-query annotations. Video-FLAIR improves accuracy by +5.4 on MathVista, +4.8 on Video-Holmes, and +4.8 on Video-MMMU, while reducing token usage from 417 to 95.
- **评估**: 该论文提出的自适应推理选择机制对自动驾驶中的多模态感知和决策具有较高参考价值，可提升推理效率与准确性。
- **核心贡献**: 提出了一个基于强化学习的自适应推理模式选择框架，显著提升多模态推理效率。
- **创新点**: 通过复合奖励比较多种推理模式，实现无需标注的推理策略学习。
- **结果**: 在多个视频推理基准上提升准确率并大幅降低计算成本。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal queries can require different types of reasoning. Some can be answered via perceptual reasoning, extracting information directly from the visual signal, while others require compositional reasoning that combines observations or deliberative reasoning that evaluates competing hypotheses. However, many existing methods apply a uniform reasoning strategy across queries, leading to unnecessary computation on simple tasks and insufficient reasoning on complex ones. We introduce Video-FLAIR, a training framework that learns to select the appropriate reasoning mode for each query using reinforcement learning. During training, the model generates responses under all three modes for the same prompt, enabling direct comparison. A composite reward compares these responses to favor the most effective one based on correctness, grounding, and cost, while discouraging unsupported or misaligned deliberation. This yields a supervision signal for learning adaptive reasoning without per-query annotations. Video-FLAIR improves accuracy over the Qwen2.5-VL base model by +5.4 on MathVista, +4.8 on Video-Holmes, and +4.8 on Video-MMMU, while reducing average token usage to 95 compared to 417 for always-thinking baselines.

</details>

---

## 📊 统计

| 领域 | 论文数 |
|------|--------|
| VLM | 9 |
| Multimodal | 1 |
| **总计** | **10** |