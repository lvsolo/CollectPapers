# 📚 arXiv 每日论文报告（我的领域）

**报告日期**: 2026-08-29  
**论文来源**: [arXiv cs.CV Recent](https://arxiv.org/list/cs.CV/recent)  
**关注论文数**: 24 篇（其中 24 篇经大模型中文评估）

> 匹配领域: Object Detection、Autonomous Driving、3D Detection、BEV、Occupancy、Multi-camera Perception、Tracking、Open-set Detection、FOD Detection、VLM、Vision Transformer、Self-supervised Vision、Video Understanding、Multimodal、Continual Learning、Neural Architecture Search、Network Pruning、Knowledge Distillation

## 📑 目录

- [VLM](#vlm) (10篇)
- [Multimodal](#multimodal) (10篇)
- [Self-supervised Vision](#self-supervised-vision) (4篇)

## VLM

### 1. VIPER: An Expert-Curated Benchmark for Vision-Language Models in Veterinary Pathology **⭐⭐⭐** (相关度: 30%, 质量: 0.7)

- **arXiv ID**: [2608.26382](https://arxiv.org/abs/2608.26382)  · [📄 PDF](https://arxiv.org/pdf/2608.26382)
- **作者**: Luca L. Weishaupt, Simone de Brot, Javier Asin et al. (12 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/mahmoodlab/viper](https://github.com/mahmoodlab/viper)
- **提交日期**: 2026-08-26 · **分类**: cs.CV
- **摘要（中）**: 针对视觉语言模型在兽医病理学领域缺乏基准的问题，该论文提出了首个专家策展的基准VIPER，包含1251个问题、419张H&E染色大鼠组织图像，覆盖七个器官系统，并评估了16个模型。研究发现兽医与人类病理学之间存在显著领域差距，前沿模型存在正常组织过度诊断风险，且领域特定训练对视觉接地预测至关重要。
- **摘要（英）**: This paper introduces VIPER, the first expert-curated benchmark for vision-language models in toxicologic pathology, containing 1,251 questions across 419 rat histology images. Benchmarking 16 models reveals a substantial domain gap between veterinary and human pathology, highlighting the risk of over-diagnosis in frontier models and the critical role of domain-specific training.
- **评估**: 该论文填补了非人类病理学VLM评估的空白，但领域与自动驾驶感知相关性较低，主要贡献在于基准构建和领域差距分析。
- **核心贡献**: 首个兽医病理学VLM基准VIPER，提供专家验证的评估数据集。
- **创新点**: 首次将VLM评估扩展到毒理病理学领域，覆盖多格式问题。
- **结果**: 识别出兽医与人类病理学的显著领域差距，并揭示前沿模型的过度诊断风险。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pathology vision-language models are advancing rapidly, yet existing benchmarks remain focused on human tissue, particularly oncology, leaving non-human pathology largely unaddressed. This gap is especially important in toxicologic pathology, where microscopic tissue examination of laboratory animals is a core component of preclinical drug safety assessment. To address it, we introduce VIPER, the first expert-curated benchmark for vision-language model evaluation in toxicologic pathology. VIPER contains 1,251 questions associated with 419 H&E-stained rat histology images across seven organ systems, covering multiple-choice, KPrim, and free-text formats. All questions were curated and validated by board-certified veterinary pathologists. In total, we benchmarked 16 models, including two newly introduced veterinary-pathology models, seven human pathology-specialized models, and seven general-purpose frontier models. The results identify a substantial domain gap between veterinary and human pathology, expose the risk of over-diagnosis of normal tissue in frontier models, and show that domain-specific training remains critical for visually grounded predictions. VIPER data and evaluation code are available at https://github.com/mahmoodlab/viper.

</details>

### 2. Towards Purified Multi-Label Test-Time Adaptation of Vision-Language Models **⭐⭐⭐⭐** (相关度: 60%, 质量: 0.75)

- **arXiv ID**: [2608.25653](https://arxiv.org/abs/2608.25653)  · [📄 PDF](https://arxiv.org/pdf/2608.25653)
- **作者**: Yiwen Liang, Hui Chen, Yizhe Xiong et al. (10 authors)
- **🏷️ 机构**: NUS
- **提交日期**: 2026-08-26 · **分类**: cs.CV
- **摘要（中）**: 针对多标签测试时适应中共享全局表征导致的主导标签偏差和缓存校准问题，该论文提出PuRF方法，通过区域纯化识别可靠区域，提供全面的区域线索，并利用纯化驱动的缓存机制进行多标签适应。该方法解决了单标签TTA扩展到多标签场景时的一对多映射问题，提升了分布偏移下的识别性能。
- **摘要（英）**: This paper addresses multi-label test-time adaptation for vision-language models, proposing PuRF, a purification-driven cache-based method that identifies reliable regions to mitigate dominant-label bias. It effectively handles the one-to-many mapping problem and improves recognition under distribution shifts.
- **评估**: 该论文针对多标签TTA这一实用问题，方法设计合理，与视觉感知中的分布偏移处理相关，但领域更偏向通用VLM适应。
- **核心贡献**: 提出PuRF，一种纯化驱动的多标签测试时适应方法。
- **创新点**: 引入区域纯化机制，解决多标签场景下的共享表征纠缠问题。
- **结果**: 在分布偏移下提升多标签识别性能，优于现有缓存方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Test-time adaptation (TTA) has been widely explored in single-label recognition, effectively mitigating distribution shifts, especially when combined with vision-language models. However, real-world images often contain multiple objects, while the more practical multi-label test-time adaptation (MLTTA) has received little attention so far. Recent cache-based TTA methods have shown promising efficiency and effectiveness, yet directly extending them to multi-label scenarios suffers from a one-to-many mapping problem: a shared global representation entangling co-occurring objects is stored as class-wise cache prototypes, inducing dominant-label bias and compromised cache calibration. While introducing region-level cues helps isolate class-specific evidence, such regional evidence can also be unreliable under distribution shifts, making its identification and utilization non-trivial. To address these issues, we introduce PuRF, a novel PuRiFication-driven cache-based method for multi-label test-time adaptation of vision-language models. Specifically, PuRF first performs region purification to identify reliable regions, providing comprehensive regional cues for multi-label recognition and enabling fine-grained alignment. Based on these purified regions, PuRF conducts cache purification to enhance cache representation and adaptability, where episodic purification builds a discriminative region-based cache, and temporal refreshing further promotes long-term cache adaptability. Experiments demonstrate that PuRF consistently outperforms state-of-the-art methods, achieving a notable 4.05% mAP improvement on ViT-B/32 across five datasets.

</details>

### 3. Retrieval Heads Meet Vision: Uncovering How VLMs Locate and Extract Visual Information **⭐⭐⭐⭐** (相关度: 50%, 质量: 0.8)

- **arXiv ID**: [2608.27417](https://arxiv.org/abs/2608.27417)  · [📄 PDF](https://arxiv.org/pdf/2608.27417)
- **作者**: Chanho Park, Daehyeon Choi, Jihyun Lee et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-27 · **分类**: cs.CV
- **摘要（中）**: 针对视觉语言模型中文本描述定位图像区域的内部机制不明确的问题，该论文引入视觉检索头（VRHs），发现约1.7-2.6%的注意力头因果负责视觉接地。通过统一设计空间重铸头部评分方法，并证明从输出预测令牌评分最可靠，在11个VLM和5个基准上，掩蔽前20个VRHs可将接地精度降低高达80个百分点。
- **摘要（英）**: This paper introduces Visual Retrieval Heads (VRHs), a small subset of attention heads causally responsible for grounding text to image regions in VLMs. Across 11 VLMs and 5 benchmarks, masking top 20 VRHs reduces grounding accuracy by up to 80 percentage points, revealing a causal-sparse-universal mechanism.
- **评估**: 该论文深入揭示了VLM内部机制，具有理论价值，但与自动驾驶感知应用距离较远，主要贡献在可解释性。
- **核心贡献**: 首次识别并验证VLM中的视觉检索头机制。
- **创新点**: 将文本检索头概念扩展到视觉领域，并建立因果评分方法。
- **结果**: 掩蔽少量VRHs即可显著降低接地精度，证明其因果重要性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-language models (VLMs) can locate an image region referred to by a text prompt and route the corresponding visual evidence to the output, yet the internal mechanism behind this behavior is not understood. Inspired by retrieval heads in large language models, we ask whether VLMs contain an analogous mechanism for visual retrieval. We answer affirmatively by introducing Visual Retrieval Heads (VRHs), a small subset of attention heads (about 1.7-2.6%) that are causally responsible for grounding text descriptions to image regions. To find them, we recast existing head-scoring methods under a unified design space over query tokens, key aggregation, and cross-sample aggregation. We then show that scoring attention from output prediction tokens with a sum over the ground-truth referent region most reliably identifies causal heads. Across eleven VLMs and five referring-expression benchmarks, masking only the top 20 VRHs reduces grounding accuracy by up to 80 percentage points, while masking the same number of random heads has little effect. Beyond replicating the causal-sparse-universal triad established for text retrieval heads, VRHs exhibit several properties not previously reported: they generalize across visual reference tasks, remaining causal on attribute, spatial, counting, and visual-math benchmarks despite being discovered through bounding-box prediction; they are functionally specific, preserving output format while corrupting localization; and they are architecturally shared, transferring causally across VLMs that share an LLM backbone but differ in vision encoder, projector, and instruction tuning.

</details>

### 4. PACE: A Unified Condense-and-Extract Paradigm for Fast VLM Inference **⭐⭐⭐⭐** (相关度: 70%, 质量: 0.78)

- **arXiv ID**: [2608.27206](https://arxiv.org/abs/2608.27206)  · [📄 PDF](https://arxiv.org/pdf/2608.27206)
- **作者**: Junjie Liu, Shengyuan Ye, Xu Chen
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/jjL357/PACE](https://github.com/jjL357/PACE)
- **提交日期**: 2026-08-27 · **分类**: cs.CV, cs.AI
- **摘要（中）**: 针对VLM推理成本随视觉令牌数量激增的问题，该论文提出PACE框架，通过统一的Condense-and-Extract范式加速视觉编码器和LLM。Condense阶段使用自适应像素压缩器评估信息密度并下采样冗余输入，Extract阶段使用动态双注意力提取器选择性保留视觉令牌，无需训练即可提升推理效率。
- **摘要（英）**: This paper proposes PACE, a training-free inference framework that accelerates both vision encoder and LLM via a unified Condense-and-Extract paradigm. It uses an adaptive pixel compressor and dynamic dual-attention extractor to reduce redundant computation while preserving visual context and details.
- **评估**: 该论文针对VLM推理效率这一实用问题，方法无需训练，与自动驾驶中的实时感知需求相关，但主要面向通用VLM。
- **核心贡献**: 提出PACE，一种统一的VLM推理加速框架。
- **创新点**: 同时优化视觉编码和LLM阶段，结合像素级压缩和令牌提取。
- **结果**: 在保持性能的同时显著降低推理延迟。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-Language Models (VLMs) demonstrate exceptional visual reasoning capabilities, yet their inference costs escalate rapidly with the proliferation of visual tokens. Existing visual token pruning methods exhibit two fundamental limitations. First, most approaches operate exclusively post-vision encoder, leaving the substantial latency of the visual encoding phase unoptimized. Second, under strict token budgets, these methods often fail to jointly preserve holistic visual contexts and fine-grained details, leading to performance degradation. To address these bottlenecks, we propose PACE (Pixel-Adaptive Condense and Extract), a training-free inference framework that accelerates both the vision encoder and the Large Language Model (LLM) via a unified Condense-and-Extract paradigm. During the Condense stage, an Adaptive Pixel Compressor (APC) evaluates visual information density prior to encoding, adaptively downsampling redundant inputs, curtailing encoder computation while preserving global context and essential visual cues. In the Extract stage, a Dynamic Dual-Attention Extractor (DDAE) selectively retains visual tokens via a fusion of internal visual signals from the encoder and semantic signals from the LLM, safeguarding task-critical details. By integrating PACE into Qwen2.5-VL-7B, the model retains 93.8% of its original performance while utilizing only 10% of the visual tokens, yielding a 3.1x speedup in time to first token (TTFT). Our code is available at https://github.com/jjL357/PACE.

</details>

### 5. LLaVAFlow: Preserving Latent Alignment Flow for Parameter-Efficient Multimodal Fine-Tuning **⭐⭐⭐⭐** (相关度: 55%, 质量: 0.72)

- **arXiv ID**: [2608.26820](https://arxiv.org/abs/2608.26820)  · [📄 PDF](https://arxiv.org/pdf/2608.26820)
- **作者**: Muyao Yuan, Muyan Jiao, Jiangyong Ying et al. (8 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-27 · **分类**: cs.CV
- **摘要（中）**: 针对多模态大语言模型在下游任务微调中的灾难性遗忘问题，该论文提出LLaVAFlow，一个基于信息论的蒸馏框架。通过压缩提取关系与MLLM嵌入之间的互信息，并最大化预训练和微调模型对齐流之间的互信息，保留跨模态对齐流，提升下游性能和泛化能力。
- **摘要（英）**: This paper proposes LLaVAFlow, an information-theoretic distillation framework that preserves cross-modal alignment flow during visual instruction tuning. It compresses mutual information between extracted relations and embeddings, and maximizes alignment flow transfer between pretrained and fine-tuned MLLMs, enhancing downstream performance and generalization.
- **评估**: 该论文针对MLLM微调中的遗忘问题，方法具有理论深度，与多模态感知相关，但应用场景偏通用。
- **核心贡献**: 提出LLaVAFlow，一种保留对齐流的信息论蒸馏框架。
- **创新点**: 从信息压缩轨迹中提取并转移跨模态对齐流。
- **结果**: 在多个任务上提升下游性能和泛化能力。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While Multimodal Large Language Models (MLLMs) exhibit strong generalization, visual instruction tuning for downstream tasks inevitably causes catastrophic forgetting, impairing overall generalization. While existing methods regulate weight updates to reduce forgetting, they overlook the fundamental cross-modal alignment in MLLMs. Based on prior work and our observations, we argue that cross-modal alignment is implicitly captured in the information-compression trajectory. To preserve the alignment flow embedded in the trajectory, we propose LLaVAFlow, an information-theoretic distillation framework. First, we compress the mutual information between the extracted relations and MLLM embeddings, encouraging a learnable module to produce a refined alignment flow that benefits downstream tasks. Second, we maximize the mutual information between the extracted alignment flows of the pretrained and fine-tuned MLLMs, enabling the transfer of compact alignment information. Extensive experiments show that LLaVAFlow is an effective plug-and-play framework that preserves alignment flow and enhances both downstream performance and generalization.

</details>

### 6. Order Matters: A Chinese Multi-Panel Meme Benchmark for Vision-Language Reasoning **⭐⭐⭐** (相关度: 25%, 质量: 0.65)

- **arXiv ID**: [2608.26866](https://arxiv.org/abs/2608.26866)  · [📄 PDF](https://arxiv.org/pdf/2608.26866)
- **作者**: Haihan Li, Haihao Li, Zhenfei Xu et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-27 · **分类**: cs.CV
- **摘要（中）**: 针对视觉语言模型在多面板表情包推理中缺乏顺序感知能力的问题，该论文引入CMPM基准，包含1214个标注样本，覆盖五种结构类型和顺序依赖。通过两层评估协议，发现标准显示精度不能证明顺序理解，主要打乱条件导致性能显著下降。
- **摘要（英）**: This paper introduces CMPM, a Chinese multi-panel meme benchmark with 1,214 annotated samples, to evaluate sequence-aware reasoning in LVLMs. Results show that canonical-display accuracy is not evidence of order understanding, as shuffled conditions significantly degrade performance.
- **评估**: 该论文聚焦于多面板推理基准，与自动驾驶感知相关性低，主要贡献在VLM评估领域。
- **核心贡献**: 首个中文多面板表情包推理基准CMPM。
- **创新点**: 设计两层评估协议，区分结构类型和顺序理解。
- **结果**: 揭示LVLMs在顺序推理上的不足。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Many multimodal tasks depend on how visual elements are ordered and composed, not only on recognizing them in isolation. Internet memes are a compact case of this problem: their punchline often depends on a constrained reading order and cross-panel visual--textual cues. While large vision-language models (LVLMs) show strong performance on single-image understanding, it remains unclear whether they can perform sequence-aware reasoning over structured meme layouts, especially in Chinese social media. We introduce CMPM, a Chinese Multi-Panel Meme benchmark with 1,214 annotated samples covering five structural types, ordering dependency, panel-order constraints, and optional comment context. We formulate a two-layer evaluation: Task1 probes structure typing and order-sensitive panel sequencing (with a context ablation setting), and Task2 evaluates Chinese meme explanation generation with human ratings on five 1-3 Likert dimensions (visual, panel, humor, context, and faithfulness). We benchmark five representative LVLMs under a unified protocol. Results indicate that canonical-display accuracy is not by itself evidence of order understanding: the primary shuffled condition produces a sharp accuracy drop, revealing a persistent gap in order-sensitive multimodal reasoning. Task2 preferences place Gemini 3.1 Pro and GPT-5.5 above the open models, while comment context yields only a small and mixed Core4 gain. Code and data will be released upon acceptance.

</details>

### 7. Thinking on Shots: Consistent Multi-Shot Video Editing with Agentic Reasoning **⭐⭐⭐** (相关度: 40%, 质量: 0.6)

- **arXiv ID**: [2608.26809](https://arxiv.org/abs/2608.26809)  · [📄 PDF](https://arxiv.org/pdf/2608.26809)
- **作者**: Chenyang Wu, Fuchen Long, Binyuan Huang et al. (7 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-27 · **分类**: cs.CV, cs.MM
- **摘要（中）**: ①针对长视频多指令编辑中实体碎片化、编辑幻觉和时间连续性破坏的问题。②提出了MMLVE任务和基于LLM与VLM协同的智能体编辑框架，实现镜头级视频解耦和精确指令解析。③相比固定时长分块策略，通过智能体推理实现跨镜头一致性和多指令解耦。④构建了MMLVE-Bench数据集和评估指标，但摘要未提供具体性能数据。
- **摘要（英）**: This paper addresses challenges in long-video multi-instruction editing, proposing the MMLVE task and an agentic framework leveraging LLMs and VLMs for shot-level decoupling and instruction parsing. It introduces MMLVE-Bench for evaluation, though specific performance metrics are not detailed in the abstract.
- **评估**: 该工作为长视频编辑提供了新任务定义和框架，但缺乏定量结果，与自动驾驶感知领域关联较弱。
- **核心贡献**: 提出多指令多镜头长视频编辑任务及智能体推理框架。
- **创新点**: 利用LLM和VLM协同实现镜头级视频解耦。
- **结果**: 构建了评估基准，但未报告具体性能提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While generative AI has significantly advanced video editing, existing methods primarily focus on single-shot or short video clips. Editing long videos with multiple instructions remains a formidable challenge. Naive chunking strategies, e.g., fixed-duration segmentation, often lead to entity fragmentation, severe editing hallucinations, and disrupted temporal continuity. To bridge this gap, we introduce the Multi-Instruction Multi-Shot Long-Video Editing (MMLVE) task, which is structured around three core objectives: Cross-Shot Editing Consistency (CSEC), Multi-Instruction Decoupling (MID), and Zero-Destruction on Spatiotemporal Structure (ZDSS). To tackle these three unique challenges, we introduce an agentic editing framework that leverages the synergy of Large Language Models (LLMs) and Vision-Language Models (VLMs) to achieve shot-level video decoupling and precise instruction parsing. Furthermore, to comprehensively evaluate this task, we construct MMLVE-Bench, which is an MMLVE-focused dataset characterized by complex real-world spatiotemporal dynamics, high-density heterogeneous instructions, and sparse, random entity distributions. Three MMLVE-focused evaluation metrics are further exploited to assess the quality of the editing results. Extensive experiments demonstrate that our MMLVE-Agent outperforms existing closed-source SOTA approaches (e.g., Seedance 2.0), successfully eliminating editing hallucinations, preserving cross-shot editing consistency, and attaining seamless spatiotemporal transitions.

</details>

### 8. Multi-Image Visual Token Pruning in Large Visual Language Models **⭐⭐⭐⭐** (相关度: 70%, 质量: 0.75)

- **arXiv ID**: [2608.26806](https://arxiv.org/abs/2608.26806)  · [📄 PDF](https://arxiv.org/pdf/2608.26806)
- **作者**: Rongyang Zhang, Chengqiang Lu, Cong Li et al. (12 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/zry13/AVTP](https://github.com/zry13/AVTP)
- **提交日期**: 2026-08-27 · **分类**: cs.CV
- **摘要（中）**: ①针对多图像视觉语言模型中视觉token剪枝方法依赖静态策略和注意力计算、难以适配不同架构和高效技术的问题。②提出了训练无关的自适应视觉token剪枝框架AVTP，基于视觉注意力分布经验分析确定剪枝层，并在多图像场景中按图像重要性自适应调整剪枝比例。③相比现有静态剪枝方法，AVTP无需训练且兼容FlashAttention。④实验表明Qwen3VL-8B实现2倍推理加速，同时保持96.1%的原始准确率。
- **摘要（英）**: This paper tackles the limitations of static visual token pruning in LVLMs by proposing AVTP, a training-free framework that adaptively determines pruning layers and ratios based on attention distributions and image importance. It achieves 2x speedup on Qwen3VL-8B while retaining 96.1% accuracy, demonstrating robustness across architectures.
- **评估**: 该工作对多模态模型效率优化有实际价值，剪枝技术可迁移至自动驾驶多相机感知的token压缩。
- **核心贡献**: 提出训练无关的自适应视觉token剪枝框架。
- **创新点**: 基于注意力分布分析实现自适应剪枝层和比例选择。
- **结果**: 实现2倍加速并保持96.1%准确率。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> With the growing demand for processing multiple image sequences in real-world applications, various visual token pruning methods have emerged to mitigate the computational and context length constraints faced by Large Vision Language Models (LVLMs). However, most existing pruning approaches rely on static strategies that struggle to adapt across different architectural LVLMs and multi-image scenarios, and are additionally constrained by their dependence on attention computations that are incompatible with efficient techniques like FlashAttention. To address these limitations, we propose a training-free, Adaptive Visual Token Pruning (AVTP) framework, applicable to diverse LVLM architectures. We strategically determine pruning layers based on empirical analysis of visual attention distributions across various LVLMs, and implement adaptive pruning ratios in multi-image contexts where images of higher importance retain proportionally more tokens. We conduct extensive experiments across different LVLMs to demonstrate the effectiveness and robustness of AVTP. Specifically, Qwen3VL-8B achieves 2 times inference speedup while maintaining 96.1\% of its original accuracy on multiple multi-image benchmarks, InternVL3.5-8B retains 94.1\% accuracy, and LLaVA-OV-7B even exceeds its original baseline performance. Our code is available at \href{https://github.com/zry13/AVTP}{this link}.

</details>

### 9. G2D: Generative-to-Discriminative Collaborative Inference for Zero-Shot Image Classification **⭐⭐⭐** (相关度: 50%, 质量: 0.65)

- **arXiv ID**: [2608.26744](https://arxiv.org/abs/2608.26744)  · [📄 PDF](https://arxiv.org/pdf/2608.26744)
- **作者**: Zehua Hao, Fang Liu, Qinliang Wang et al. (6 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/Harzva/G2D](https://github.com/Harzva/G2D)
- **提交日期**: 2026-08-27 · **分类**: cs.CV
- **摘要（中）**: ①针对零样本图像分类中判别式模型（如CLIP）召回不足和生成式模型受限于大标签空间的问题。②提出了G2D框架，利用生成式VLM验证CLIP检索的候选标签，结合固定置信度路由、熵自适应候选大小和trie约束解码。③相比单独使用CLIP或VLM，G2D通过分离候选检索和细粒度验证提升互补性。④在八个基准上平均准确率68.85%，优于CLIP的59.35%和独立VLM的63.11%。
- **摘要（英）**: This paper addresses complementary failures of discriminative and generative models in zero-shot classification by proposing G2D, a training-free framework that uses a generative VLM to verify CLIP-retrieved candidates. It achieves 68.85% average accuracy across eight benchmarks, surpassing CLIP and standalone VLM.
- **评估**: 该工作对开放集识别有参考意义，但方法依赖生成模型推理，在自动驾驶实时场景中可能受限。
- **核心贡献**: 提出生成-判别协同推理框架用于零样本分类。
- **创新点**: 利用候选检索与生成验证分离策略。
- **结果**: 平均准确率提升至68.85%。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Zero-shot classification needs efficient label retrieval and fine-grained visual reasoning, yet discriminative and generative vision-language models fail in complementary ways.When CLIP's top-1 prediction is wrong, the correct label often remains in its top-$K$ shortlist, making disambiguation rather than recall the key challenge.Standalone generative models, however, are hindered by large label spaces and unconstrained outputs.This complementarity motivates separating broad candidate retrieval from fine-grained, image-grounded verification.We propose G2D, a training-free framework that uses a generative VLM to verify CLIP-retrieved candidates against the image.Candidate names and CLIP probabilities provide a structured prior for resolving visually similar classes.Fixed confidence routing, entropy-adaptive candidate sizing, and trie-constrained decoding focus generative reasoning on uncertain samples and ensure one valid output for each input at test time.Across eight benchmarks, G2D achieves 68.85% average accuracy, versus 59.35% for CLIP and 63.11% for the standalone VLM.Across seven generator configurations, candidate-set verification improves average accuracy by 1.08--27.42 percentage points.G2D also transfers to DCLIP, WaffleCLIP, and CuPL, supporting a practical interface between discriminative proposal and generative visual reasoning. Code: https://github.com/Harzva/G2D

</details>

### 10. Who Remains, What Changes: Identity Anchored Composed Gait Retrieval **⭐⭐⭐** (相关度: 45%, 质量: 0.6)

- **arXiv ID**: [2608.26632](https://arxiv.org/abs/2608.26632)  · [📄 PDF](https://arxiv.org/pdf/2608.26632)
- **作者**: Jingchen Fei, Zengbin Wang, Yukun Liu et al. (6 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-27 · **分类**: cs.CV
- **摘要（中）**: ①针对步态识别中缺乏自然语言交互检索能力的问题。②提出了组合步态检索任务CoGR和基于VLM的自动标注流程，构建了首个步态-语言数据集，并设计了身份锚定框架ComposeGait。③相比通用组合检索，通过Part-aware Identity Adapter防止身份漂移。④摘要未提供具体性能数据，但框架设计具有创新性。
- **摘要（英）**: This paper introduces Composed Gait Retrieval (CoGR) and ComposeGait, an identity-anchored framework with a Part-aware Identity Adapter to prevent identity drift. It constructs the first gait-language datasets via VLM-based annotation, though quantitative results are not detailed.
- **评估**: 该工作拓展了多模态检索到步态领域，但与自动驾驶感知核心任务关联度较低。
- **核心贡献**: 提出组合步态检索任务及身份锚定框架。
- **创新点**: 利用VLM自动构建步态语言数据集。
- **结果**: 未报告具体性能数据。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Gait recognition has achieved remarkable progress, yet existing methods remain confined to rigid visual matching and often overlook the potential of natural language instructions for interactive retrieval. In this paper, we introduce Composed Gait Retrieval (CoGR), a novel task that retrieves a target gait sequence based on a reference sequence and a natural language modification query. To address the absence of existing datasets for this task, we design an automated annotation pipeline powered by large vision-language models (VLMs) to construct the first gait-language datasets: Language-Augmented CCPG and Language-Augmented CASIA-B. Building on this, we propose ComposeGait, an identity-anchored composition framework designed to prevent the identity drift that arises when generic composed retrieval follows the instruction but returns the wrong person. Its Part-aware Identity Adapter (PIA) aggregates multi-frame, part-aware identity evidence into a sample-specific ID token. We inject the ID tokens into both branches of a shared Q-Former to preserve identity, while excluding the ID-token outputs from the final retrieval embeddings. Joint identity and task-adapted composed-retrieval objectives optimize this space end to end. We evaluate ComposeGait on both benchmarks and show that it achieves the best R@1 among the compared methods, reaching 72.38% on Language-Augmented CCPG and 83.61% on Language-Augmented CASIA-B. These results establish ComposeGait as a strong baseline for CoGR. The datasets and code will be made publicly available.

</details>

---

## Multimodal

### 1. Aphanta: Diagnosing Task-Aligned Image-Edited Intermediates for Multimodal Reasoning **⭐⭐⭐** (相关度: 55%, 质量: 0.65)

- **arXiv ID**: [2608.26993](https://arxiv.org/abs/2608.26993)  · [📄 PDF](https://arxiv.org/pdf/2608.26993)
- **作者**: Hengyuan Xu, Wei Cheng, Yumeng Ji et al. (7 authors)
- **🏷️ 机构**: Tencent
- **提交日期**: 2026-08-27 · **分类**: cs.CV
- **摘要（中）**: ①针对多模态大模型中图像编辑中间步骤的实际效用评估问题。②提出了Aphanta框架，通过自动化任务发现和闭环诊断，比较直接推理、编辑中间和理想参考三种条件。③相比现有评估方法，分离了视觉潜力与编辑器实际效用。④在选定的正任务子集上，Qwen管线将平均任务分数从0.343提升至0.445，相对提升29.7%。
- **摘要（英）**: This paper introduces Aphanta, an automated diagnostic framework for the MLLM-editor-MLLM pipeline, evaluating task-conditioned utility of visual intermediates. On positive tasks, it improves mean score from 0.343 to 0.445, highlighting gains in visual cue injection and grounding.
- **评估**: 该工作为多模态推理中的视觉中间步骤提供了系统评估方法，对自动驾驶中VLM辅助感知有启发。
- **核心贡献**: 提出多模态推理中图像编辑中间步骤的诊断框架。
- **创新点**: 通过理想参考对比分离视觉潜力与编辑器效用。
- **结果**: 正任务子集上平均分数提升29.7%。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Explicit visual intermediates can help multimodal large language models (MLLMs) externalize spatial evidence and updated visual states, but their utility depends on whether an image editor can faithfully realize the required transformation. We introduce \textbf{Aphanta}, an automated task-discovery and closed-loop diagnostic framework for the MLLM -> image editor -> MLLM pipeline. Aphanta evaluates three conditions---direct reasoning, reasoning with an editor-generated intermediate, and reasoning with an idealized reference intermediate---to separate potential visual headroom from the practical utility of current editors. Across 20 candidate tasks and multiple editor--MLLM combinations, we find that utility is strongly task-conditioned. Gains concentrate in visual cue injection, grounding, and counterfactual state realization, whereas intermediates requiring symbol-sensitive construction or structural extrapolation are substantially less reliable. On the selected positive-task subset, our consolidated Qwen pipeline improves the mean task score from 0.343 to 0.445 ($+10.2$ points; $+29.7\%$ relative), while the full study also retains filtered and unsuccessful tasks to expose the boundary. These results position image editing as a specialized visual workspace rather than a universal reasoning mechanism, and establish Aphanta as a reusable protocol for measuring task--representation alignment, editor realization, and downstream pipeline utility.

</details>

### 2. HUG-VIS: A Multimodal Benchmark for Human-centered Understanding and Generation in Visual Intelligence **⭐⭐⭐** (相关度: 40%, 质量: 0.6)

- **arXiv ID**: [2608.26517](https://arxiv.org/abs/2608.26517)  · [📄 PDF](https://arxiv.org/pdf/2608.26517)
- **作者**: Fei Ma, Zebang Cheng, Minghui Li et al. (14 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/GML-MMGroup/HUG-VIS](https://github.com/GML-MMGroup/HUG-VIS)
- **提交日期**: 2026-08-27 · **分类**: cs.CV
- **摘要（中）**: 该论文针对人类中心视觉智能中多模态基准缺失的问题，提出了HUG-VIS基准，包含8400个半身视频，覆盖情感识别、视频生成、声音克隆和视频抠图四个任务。该基准提供同步的视频、音频、文本和alpha遮罩，支持统一零样本评估协议。相比现有任务特定资源，它提供了共享基础以协调理解与生成。实验评估了多种开源和闭源模型，但摘要未提供具体性能数据。
- **摘要（英）**: This paper addresses the lack of a unified multimodal benchmark for human-centered visual intelligence by introducing HUG-VIS, containing 8,400 videos with synchronized modalities across four tasks. It provides a shared foundation for understanding and generation, evaluated under a zero-shot protocol, though specific results are not detailed in the abstract.
- **评估**: 该基准填补了人类中心多模态研究的空白，但相关性较低，且缺乏具体实验结果，影响力有限。
- **核心贡献**: 提出了一个统一的多模态人类中心视觉智能基准HUG-VIS。
- **创新点**: 整合理解与生成任务于单一基准，提供多模态同步数据。
- **结果**: 基准构建完成，但未报告具体性能数据。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Visual intelligence seeks to perceive, interpret, and synthesize the visual world and is central to modern computer vision. Human-centered visual intelligence is especially demanding because it studies people as expressive, socially situated subjects whose meaning is rarely conveyed by appearance alone. It couples vision with audio and language across four representative tasks: human emotion recognition, human video generation, human voice cloning, and human video matting. Yet existing resources remain task-specific, providing modalities and annotations for individual problems rather than a shared foundation coordinating understanding and generation. This limits multimodal signal use and broader research. We address this gap with HUG-VIS, a unified benchmark for Human-centered Understanding and Generation in Visual Intelligence. It contains 8,400 seated half-body videos of 30 professional actors, each performing the same 280 emotion-action-prompt assignments under a controlled Mandarin studio protocol, with synchronized video, audio, text, and alpha mattes. We evaluate diverse open- and closed-source models across the four tasks under a unified zero-shot protocol using automatic metrics, criterion-specific mean opinion scores, and multiple cross-task analyses. Results show that (i) linguistic content dominates current emotion recognition, while purely visual affect recognition is weakest; (ii) in video generation and voice cloning, automatic metrics and human judgment agree overall but differ in their top rankings, requiring joint reporting; (iii) boundary fidelity under motion is the main remaining obstacle for human matting; and (iv) task difficulty varies across emotions, models, and metrics, with notable cross-task correlations. The dataset and results are available at https://github.com/GML-MMGroup/HUG-VIS.

</details>

### 3. Zero-Shot Video Restoration and Enhancement with Text-to-Image Latent Diffusion Models and Multi-Modal References **⭐⭐⭐** (相关度: 30%, 质量: 0.7)

- **arXiv ID**: [2608.26476](https://arxiv.org/abs/2608.26476)  · [📄 PDF](https://arxiv.org/pdf/2608.26476)
- **作者**: Cong Cao, Huanjing Yue, Xin Liu et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-27 · **分类**: cs.CV
- **摘要（中）**: 该论文针对零样本视频恢复中的时间闪烁问题，提出了一种基于文本到图像潜在扩散模型和多模态参考的框架。通过双提示调优反转和采样，推理时间减少至原来的1/3，并增强了性能和时序一致性。还提出了纹理感知视频令牌合并和参考自注意力机制，以支持图像参考。实验证明了该方法在恢复和增强时序一致视频方面的优越性。
- **摘要（英）**: This paper tackles temporal flickering in zero-shot video restoration by proposing a framework using text-to-image latent diffusion models with multi-modal references. Dual prompt tuning inversion reduces inference time to one-third, while texture-aware token merging improves temporal consistency, with experiments showing superiority.
- **评估**: 方法在视频恢复领域有创新，但与本用户研究领域相关性较低。
- **核心贡献**: 提出了零样本视频恢复增强框架，提升时序一致性。
- **创新点**: 结合多模态参考和令牌合并技术优化扩散模型。
- **结果**: 推理时间减少至1/3，性能显著提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Zero-shot image restoration methods with text-to-image latent diffusion models have achieved great success in universal image restoration tasks without training. However, applying them to video restoration will result in severe temporal flickering. In this paper, we propose a novel framework for zero-shot video restoration and enhancement which uses a text-to-image latent diffusion model and multi-modal references. Through the proposed dual prompt tuning inversion and sampling, the inference time can be reduced to nearly 1/3 of the original. The performance and temporal consistency can be also significantly stregthened. By using the proposed texture-aware video token merging, the temporal correlation between frames can be further utilized to improve the temporal consistency. We futher propose the referenced self-attention and referenced token merging to support image reference. Experimental results demonstrate the superiority of the proposed method in restoring and enhancing temporally consistent videos.

</details>

### 4. Modality Maturity Index: A benchmark for assessing multimodal capabilities of omni models **⭐⭐⭐** (相关度: 50%, 质量: 0.6)

- **arXiv ID**: [2608.26317](https://arxiv.org/abs/2608.26317)  · [📄 PDF](https://arxiv.org/pdf/2608.26317)
- **作者**: Rohit Patel, Dieuwke Hupkes, Sloan Strader
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-26 · **分类**: cs.CV, cs.AI, cs.MM
- **摘要（中）**: 该论文针对现有评估框架仅关注双模态理解的问题，提出了模态成熟度指数（MMI）基准，用于评估大语言模型在五种模态及最多三模态组合下的能力。MMI包含893个问题，每个问题都有明确的模态要求和人工编写的评分标准。模型得分反映模态生成和内容正确性，但摘要未提供具体评估结果。
- **摘要（英）**: This paper proposes the Modality Maturity Index (MMI), a benchmark evaluating omni models across five modalities and combinations, with 893 questions and rubric criteria. It addresses the gap in multimodal evaluation, though no specific results are reported in the abstract.
- **评估**: 该基准对多模态评估有贡献，但相关性一般，且缺乏实验数据。
- **核心贡献**: 提出了多模态能力评估基准MMI。
- **创新点**: 覆盖多模态输入输出组合的评估框架。
- **结果**: 基准设计完成，但未报告模型性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Frontier language models are increasingly marketed as omni systems that can perceive and respond across modalities. Existing evaluation frameworks, however, focus almost exclusively on bimodal understanding, typically text plus one other modality. We propose the Modality Maturity Index (MMI), a benchmark designed to evaluate the multimodal capabilities of large language models across five modalities (text, image, audio, video and document) and combinations of up to three modalities in both inputs and outputs. MMI consists of 893 questions, each carefully crafted to require the model to demonstrate its understanding of multiple input modalities and to generate responses that incorporate various output formats. The questions are designed to be self-contained, with clear expectations for the correct modality or mix of modalities required for an accurate response. Every MMI prompt carries human-authored rubric criteria for each output modality expected in the response; a model's MMI Value expresses the average of the per-modality scores for each prompt. Because low scores can reflect either failure to generate a modality (lack of presence) or failure to generate correct content, we introduce also a supplementary Modality Presence Score (MPS), a per-prompt F1 over the expected output modalities. Applying MMI to five frontier multimodal models, we find that the MPS ranges from only 15.6 (Claude Opus 4.6) to 34.9 (GPT-5.4). Given the low availability of returned modalities to even grade, we report MPS as our main result pending model improvements. To assess the viability of judging output correctness with LLM judges and rubrics, we run a separate experiment with custom generation tools. On the assets that generates, we find that an LLM judge applying the rubrics agrees with rubric-blind human annotators (who score the outputs directly and never see the criteria) on 70.8% of judgments.

</details>

### 5. PlanSightRAG: A Visual-First Multimodal RAG for Automating Question Answering and Compliance Checking for Civil Standard Plans **⭐⭐⭐** (相关度: 40%, 质量: 0.7)

- **arXiv ID**: [2608.26091](https://arxiv.org/abs/2608.26091)  · [📄 PDF](https://arxiv.org/pdf/2608.26091)
- **作者**: Nabaraj Subedi, Shuvo Dip Datta, Ahmed Abdelaty et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-26 · **分类**: cs.IR, cs.CL, cs.CV
- **摘要（中）**: ①针对土木工程标准图纸合规检查依赖人工阅读和OCR丢失几何信息的问题。②提出PlanSightRAG，一种视觉优先的多模态RAG框架，直接索引和推理图纸图像，集成ColNomic-3B多向量检索、Planner-Retriever-Auditor-Synthesizer代理流程和MaxSim热图证据追踪。③引入来自五个州交通部的4,056对基准数据集，包含1,898页标准图纸。④在零样本检索上达到91.47%的Recall@5，在密歇根州交通部语料上达91.40%；在合成合规图纸上，Qwen2.5-VL-72B管道在预解析规则阈值下达到100%判定准确率，而非VLM的OCR基线为76.4%。
- **摘要（英）**: This paper tackles compliance checking of civil standard plans, where OCR fails to preserve geometry and layout. PlanSightRAG is a visual-first multimodal RAG that indexes plan imagery directly, using ColNomic-3B retrieval and an agentic pipeline, achieving 91.47% Recall@5 on zero-shot retrieval and 100% verdict accuracy with pre-resolved rules on synthetic drawings. It introduces a 4,056-pair benchmark from five DOTs, demonstrating superior performance over OCR baselines.
- **评估**: 该论文将多模态RAG应用于特定领域文档理解，方法新颖且实验充分，但对自动驾驶感知研究者的直接参考价值有限。
- **核心贡献**: 提出了视觉优先的多模态RAG框架PlanSightRAG，用于自动化土木标准图纸的问答和合规检查。
- **创新点**: 直接对图纸图像进行索引和推理，结合多向量检索和代理流程，保留几何信息。
- **结果**: 零样本检索Recall@5达91.47%，合规判定准确率在预解析规则下达100%。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Civil infrastructure compliance checking has long relied on engineers manually reading legacy 2D plans; however, OCR-based automation strips away the geometry and layout essential for interpreting these plans. We present a Visual-First Multimodal Retrieval-Augmented Generation (RAG) framework called PlanSightRAG. It indexes and reasons directly over plan imagery, integrates a ColNomic-3B multi-vector retrieval, an agentic Planner-Retriever-Auditor-Synthesizer, and MaxSim heatmaps as an evidence trail. We introduce a 4,056-pair benchmark from five state Departments of Transportation (DOT) standard plans (1,898 pages). PlanSightRAG achieves 91.47% Recall@5 on zero-shot retrieval, while on a held-out Michigan DOT corpus, it achieves 91.40%. On synthetic, parametrically-generated compliance drawings, our Qwen2.5-VL-72B pipeline reaches 100% verdict accuracy only when supplied a pre-resolved rule threshold, a controlled ceiling that a non-VLM OCR baseline already reaches at 76.4%. Finally, we demonstrate autonomous visual rule-grounding by extracting numeric limits directly from a specification corpus without any human-supplied rules.

</details>

### 6. PANDA - Prototype-Anchored Alignment for Partially Unpaired Multimodal Learning, with Applications to Alzheimers MRI and TCGA Pathology **⭐⭐** (相关度: 20%, 质量: 0.7)

- **arXiv ID**: [2608.25970](https://arxiv.org/abs/2608.25970)  · [📄 PDF](https://arxiv.org/pdf/2608.25970)
- **作者**: Sheethal Bhat, Mahfuzur Rahman Chowdhury, Paula Andrea Perez-Toro et al. (7 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-26 · **分类**: cs.CV, cs.AI
- **摘要（中）**: 该论文针对医学多模态预测中辅助模态不完整配对的问题，提出了PANDA框架，通过两阶段学习将辅助信息迁移到主模态模型。阶段一学习共享嵌入和类原型，阶段二训练主编码器对齐原型。在ADNI数据集上，PANDA相比MRI-only基线提升了AUC 7.9个百分点，并减少了假阳性。该方法适用于任意配对率，包括零重叠。
- **摘要（英）**: This paper introduces PANDA, a two-stage framework for partially unpaired multimodal learning, transferring auxiliary information via class prototypes. On ADNI, it improves AUC by 7.9pp over MRI-only baseline, accommodating arbitrary pairing rates.
- **评估**: 医学领域方法，与自动驾驶感知相关性低，但方法有普适性。
- **核心贡献**: 提出了处理不完整多模态配对的PANDA框架。
- **创新点**: 基于类原型的对齐机制，支持零配对率。
- **结果**: AUC提升7.9个百分点，假阳性减少24.3pp。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal medical prediction often faces incomplete pairing: auxiliary modalities with complementary signal are available for only a subset of subjects (or none) and cannot be assumed at deployment. We introduce PANDA (Prototype Anchored Data Alignment), a two-stage framework that transfers auxiliary information to a primary-modality model without auxiliary inputs at inference. Stage 1 learns a shared embedding from the paired subset and estimates class prototypes from auxiliary modalities; Stage 2 trains the primary encoder on all subjects using cross-entropy plus alignment to the frozen prototypes. Because supervision is defined at the class-prototype level, PANDA accommodates arbitrary pairing rates, including zero subject overlap. We evaluate PANDA on two applications. On a 1,021-subject multi-scanner ADNI cohort, we perform AD/CN classification with three auxiliary modalities at distinct pairing rates: tabular scores (44.8%), FDG-PET (18.7%), and external handwriting kinematics (0% overlap). Relative to the same-backbone MRI-only baseline, PANDA attains AUC 0.868 +-0.020 (+7.9pp) and reduces 1.5T CN false positives by 24.3pp; on a fully trainable Conv5-FC3 backbone it reaches AUC 0.893 (best overall). A pairing-rate ablation shows that the joint anchor remains within seed noise from 75% to 5% pairing. On TCGA-Lung survival prediction from whole-slide images with RNA-seq as auxiliary data, PANDA improves over WSI-only on 2-year OS (AUC +3.5pp) and Cox PH (C-index +9.0pts) and outperforms full-fusion training, which underperforms WSI-only, while requiring no RNA at inference; wide confidence intervals on this smaller cohort keep the gains below conventional significance. Overall, PANDA provides a deployment-oriented mechanism for leveraging incomplete auxiliary modalities to improve primary-modality prediction.

</details>

### 7. Attention-Guided Reliability Scaling for Contrastive Decoding in Robust Audio-Visual Speech Recognition **⭐⭐** (相关度: 25%, 质量: 0.6)

- **arXiv ID**: [2608.26213](https://arxiv.org/abs/2608.26213)  · [📄 PDF](https://arxiv.org/pdf/2608.26213)
- **作者**: YoungChae Kim, Da-Hee Yang, Joon-Hyuk Chang
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-26 · **分类**: cs.SD, cs.CV, eess.AS
- **摘要（中）**: 该论文针对音频-视觉语音识别中对比解码固定强度的问题，提出了可靠性感知的缩放方法。通过注意力动态和模型间预测差异来调整对比度影响，在LRS3上实验显示在干净和低信噪比条件下均有改进。该方法无需额外训练，适应不同噪声水平。
- **摘要（英）**: This paper proposes reliability-aware scaling for contrastive decoding in AVSR, adapting contrastive strength based on attention dynamics. Experiments on LRS3 show consistent improvements across noise levels.
- **评估**: 方法针对语音识别，与自动驾驶感知相关性低。
- **核心贡献**: 提出了自适应对比解码缩放方法。
- **创新点**: 利用可靠性信号动态调整对比度。
- **结果**: 在LRS3上性能一致提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large language model (LLM)-based audio-visual speech recognition (AVSR) systems are robust under noise. Contrastive decoding (CD), originally introduced to stabilize LLM generation by contrasting a weaker model against a stronger one at inference time, adjusts predictions without additional training. In this work, we apply CD to AVSR by contrasting audio-only conditioning with full audio-visual conditioning within the same underlying model. However, using a fixed contrastive strength introduces a trade-off across noise levels: stronger intervention helps under severe noise but may over-correct reliable predictions in clean conditions. We propose reliability-aware scaling of CD for AVSR. Instead of using a fixed strength, we adaptively modulate the contrastive influence at each token based on reliability signals derived from attention dynamics and inter-model predictive divergence. Experiments on LRS3 show consistent improvements across clean and low-SNR conditions.

</details>

### 8. Omni-Interactive Universal Embedder **⭐⭐⭐⭐** (相关度: 60%, 质量: 0.8)

- **arXiv ID**: [2608.27044](https://arxiv.org/abs/2608.27044)  · [📄 PDF](https://arxiv.org/pdf/2608.27044)
- **作者**: Wei-Yao Wang, Kazuya Tateishi, Shuyang Cui et al. (7 authors)
- **🏷️ 机构**: Sony
- **提交日期**: 2026-08-27 · **分类**: cs.AI, cs.CV
- **摘要（中）**: 该论文针对现有多模态嵌入器主要聚焦语言和图像、缺乏对视频和音频支持的问题，提出首个全交互通用嵌入器OmniUE。OmniUE通过可学习token的中间层表示，在文本、视频和音频间学习统一嵌入空间，并支持用户以文本、视觉区域和音频片段形式进行交互查询。视觉和音频分割器处理多样化用户交互，并与全模态LLM集成，通过上下文聚合产生用户条件下的任意到任意嵌入。为评估其能力，作者引入OmniCHOIR基准，测试基于文本、视频和音频的组合检索任务。该方法推动了多模态表示学习向更全面的交互式方向发展。
- **摘要（英）**: This paper addresses the limitation of existing multimodal embedders that focus mainly on language and image by proposing OmniUE, the first omni-interactive universal embedder supporting text, video, and audio. It learns a unified embedding space via learnable tokens and enables user-conditioned any-to-any embeddings through visual/audio segmenters and an omni-LLM. The introduced OmniCHOIR benchmark evaluates omni-interactive compositional retrieval, advancing multimodal representation learning.
- **评估**: 创新性强，扩展了多模态嵌入的交互维度，对自动驾驶多传感器融合有潜在启发。
- **核心贡献**: 提出首个支持文本、视频、音频统一嵌入及交互查询的通用嵌入器。
- **创新点**: 利用LLM中间层表示和可学习token实现跨模态统一嵌入与交互。
- **结果**: 在OmniCHOIR基准上展示了全交互组合检索能力。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal representation learning has been shifting from traditional two-tower architectures to large language model (LLM)-based embedders due to their strong instruction-following capabilities. Despite this progress, existing approaches primarily focus on language and image modalities, which also remain the dominant modalities for user-conditioned interactions in current embedders. In this paper, we propose the first Omni-Interactive Universal Embedder (OmniUE), which not only learns a unified embedding space across text, video, and audio by leveraging intermediate-layer representations from dedicated learnable tokens, but also supports omni-interactive querying, enabling users to provide inputs in the form of text, visual regions of interest, and audio spans. Within OmniUE, visual and audio segmenters process diverse user interactions and integrate them with an omni-LLM to produce user-conditioned any-to-any embeddings via context aggregation. To evaluate OmniUE's omni-interactive capabilities, we introduce OmniCHOIR, benchmarking models for omni-interactive compositional audio retrieval based on the given text, video, and audio as well as unimodal or multimodal interaction prompts. OmniUE consistently surpasses state-of-the-art baselines across diverse modalities, with average improvements of 10.5% on textual-interactive video benchmarks (MMEB-v2-video), 1.1% on audio tasks (MAEB), 83.7% on visual-interactive benchmarks (SCaR), and 24.1% on our omni-interactive OmniCHOIR benchmark. We believe that jointly advancing omni-modal representation learning and omni-interactive querying paves the way toward universal embedders.

</details>

### 9. AraMS-28k: The Largest Publicly Released Line-Level Dataset of Historical Arabic Manuscripts with Margin and Insertion-Anchor Annotations **⭐⭐** (相关度: 15%, 质量: 0.6)

- **arXiv ID**: [2608.26921](https://arxiv.org/abs/2608.26921)  · [📄 PDF](https://arxiv.org/pdf/2608.26921)
- **作者**: Mohamed Guechaoui, Mohamed Diaa Zellagui, Souleyman Chaib et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-27 · **分类**: cs.CV, cs.CL
- **摘要（中）**: 该论文针对历史阿拉伯语手稿行级标注数据稀缺的问题，发布了AraMS-28k数据集，包含14本书、3043页和28600行标注文本，其中27971行正文和629行边注。数据集覆盖三种手写体传统和一种石印版本，每行标注为主文本或边注，并进一步标注插入锚点以恢复非线性阅读顺序。作者还开发了RefLAM标注流水线，结合多模态LLM OCR与独立转录对齐，并通过人工审查确保质量。该数据集为历史文档分析提供了宝贵资源，但与自动驾驶感知无关。
- **摘要（英）**: This paper introduces AraMS-28k, the largest public line-level dataset of historical Arabic manuscripts with 28,600 annotated lines, including margin and insertion-anchor annotations. It covers multiple script traditions and provides both diacritised and normalized transcriptions, with a RefLAM pipeline for efficient annotation. This resource advances historical document analysis but has no direct relevance to autonomous driving.
- **评估**: 数据集构建严谨，对数字人文领域有贡献，但远离自动驾驶研究方向。
- **核心贡献**: 发布最大的历史阿拉伯语手稿行级数据集及标注流水线。
- **创新点**: 首次提供插入锚点标注以恢复非线性阅读顺序。
- **结果**: 提供了28600行高质量标注数据，支持历史文档研究。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce AraMS-28k, the largest publicly released line-level dataset of genuine historical Arabic manuscripts, comprising 14 books, 3,043 pages, and 28,600 annotated text lines (27,971 main-text, 629 margin). Thirteen books are hand-copied manuscripts spanning three script traditions -- Naskh, Ruq'ah, and Maghrebi -- and one is a lithographed printed edition included to broaden format diversity. Each line is labelled as main-text or margin, and margin lines that have an unambiguous attachment point in the main text are further annotated with an insertion anchor, recovering the manuscript's true non-linear reading order at line-level granularity -- to our knowledge the first such annotation released for a historical Arabic manuscript corpus. Because reference transcriptions are fully vocalised while manuscript hands are typically undiacritised, we release both the raw diacritised transcription and a diacritic-normalised counterpart for every line. The dataset was constructed with RefLAM, a reference-grounded annotation pipeline that aligns multimodal-LLM OCR against independently sourced clean transcriptions and routes every line through human review, combining automatic verification with expert oversight. We describe the construction and quality-control process, present the annotation schema, report dataset statistics at both the corpus and per-book level, and provide baseline HTR results using Kraken and HATFormer, including a cross-script generalisation gradient from in-distribution pages to fully unseen books. AraMS-28k is released with page images, line-level annotations, and fixed train/val/test splits under CC BY-NC-SA 4.0 to support reproducible research on Arabic manuscript recognition, layout analysis, and reading-order recovery.

</details>

### 10. Glass Surface Detection Grounded in 3D Visual Geometry **⭐⭐⭐⭐⭐** (相关度: 95%, 质量: 0.9)

- **arXiv ID**: [2608.26752](https://arxiv.org/abs/2608.26752)  · [📄 PDF](https://arxiv.org/pdf/2608.26752)
- **作者**: Yiwei Lu, Ke Xu, Tao Yan et al. (6 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/YT3DVision/VGGT_GLASS](https://github.com/YT3DVision/VGGT_GLASS)
- **提交日期**: 2026-08-27 · **分类**: cs.CV
- **摘要（中）**: 该论文针对玻璃表面检测中透明和反射导致2D外观线索失效的问题，提出将GSD建立在3D视觉几何上的范式转变。方法首先从视觉几何基础模型VGGT中蒸馏丰富的3D先验，生成玻璃感知的3D表示，然后利用多任务学习与新型玻璃检测头，包含频率自注意力模块（FSAM）和几何接地模块（GeGB），分别用于定位玻璃表面和将2D特征接地到3D几何进行分割。实验在七个标准GSD基准上达到最先进性能，并泛化到视频/多模态数据，显著改善玻璃场景的重建质量。该方法对自动驾驶中透明物体感知具有重要价值。
- **摘要（英）**: This paper addresses the challenge of glass surface detection by proposing a paradigm shift to ground GSD in 3D visual geometry, using priors distilled from VGGT and a novel detection head with FSAM and GeGB modules. It achieves state-of-the-art performance on seven benchmarks and improves reconstruction in glass scenes. The method is highly relevant to autonomous driving for transparent object perception.
- **评估**: 方法创新且实用，将3D几何先验引入玻璃检测，对自动驾驶场景理解有直接价值。
- **核心贡献**: 提出基于3D视觉几何的玻璃表面检测新范式。
- **创新点**: 利用VGGT蒸馏3D先验，结合频率自注意力和几何接地模块。
- **结果**: 在七个基准上达到SOTA，并提升玻璃场景重建质量。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Glass surface detection (GSD) is critical for scene understanding and reconstruction, and yet remains challenging due to the transparency and reflectivity of glass surfaces. Existing GSD methods typically rely on 2D appearance cues, which may fail in geometrically ambiguous scenes. In this paper, we propose a paradigm shift: grounding GSD in 3D visual geometry to explicitly model the physical existence of glass surfaces. Our method first distills rich 3D priors from the visual geometry grounded transformer (VGGT) and generates glass-aware 3D representations. It then exploits multi-tasking learning with a novel glass detection head, consisting of two core modules: a Frequency Self-Attention Module (FSAM) that identifies glass-specific spectral features for glass surface localization, and a Geometry Grounding Block (GeGB) that selectively grounds 2D features in 3D geometry for glass surface segmentation. Extensive experiments demonstrate that our method achieves state-of-the-art performance across seven standard GSD benchmarks, generalizes well to video/multi-modal data, and substantially improves reconstruction in glass scenes. Code is available in https://github.com/YT3DVision/VGGT_GLASS.

</details>

---

## Self-supervised Vision

### 1. Hyperspectral Diffusion Equivariant Imaging (HyDiff-EI): A Self-supervised Framework for Hyperspectral Image Inpainting **⭐⭐** (相关度: 30%, 质量: 0.55)

- **arXiv ID**: [2608.26812](https://arxiv.org/abs/2608.26812)  · [📄 PDF](https://arxiv.org/pdf/2608.26812)
- **作者**: Shuo Li, Mike Davies, Mehrdad Yaghoobi
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-27 · **分类**: cs.CV, cs.LG
- **摘要（中）**: ①针对高光谱图像修复中依赖大规模预训练和标注数据有限的问题。②提出了HyDiff-EI框架，在测试时从单个损坏图像学习，并嵌入等变一致性约束。③相比传统扩散方法，无需预训练且利用几何对称性增强鲁棒性。④在Chikusei、Botswana和EMIT数据集上展示了优于现有自监督和扩散算法的修复质量。
- **摘要（英）**: This paper proposes HyDiff-EI, a test-time optimization framework for hyperspectral inpainting that learns from a single corrupted image with equivariant consistency constraints. It outperforms existing self-supervised and diffusion methods on real-world datasets, offering flexibility for limited annotated data.
- **评估**: 该工作针对遥感图像修复，与自动驾驶感知的关联性较弱，但自监督思想有一定参考价值。
- **核心贡献**: 提出自监督扩散等变框架用于高光谱图像修复。
- **创新点**: 在扩散过程中嵌入等变一致性约束。
- **结果**: 在多个数据集上优于现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> A novel Hyperspectral diffusion Equivariant Imaging (HyDiff-EI) framework for solving the hyperspectral image (HSI) inpainting problem has been presented here. Unlike conventional diffusion-based methods that rely on large-scale pretraining, HyDiff-EI is a test-time optimization framework that learns directly from a single corrupted HSI acquisition. This makes it flexible for different sensor configurations and particularly well-suited for practical remote sensing scenarios where large annotated hyperspectral datasets are limited. To address the ill-posed nature of unsupervised inpainting, we embed equivariant consistency constraints within the diffusion process. By leveraging the inherent geometric symmetries and intrinsic characteristics of HSIs, HyDiff-EI bridges the gap between generative diffusion modeling and self-consistent physical priors. We empirically show that coupling diffusion modeling with equivariant priors substantially enhances noise robustness and generalizability. Extensive experiments on real-world datasets including Chikusei, Botswana, and EMIT demonstrate that HyDiff-EI offers remarkable inpainting quality over existing self-supervised and diffusion-based algorithms in both noiseless and noisy cases.

</details>

### 2. Cross-Architecture Knowledge Distillation from a Vision Foundation Model to a Lightweight Visual State Space Model for Tea Leaf Disease Classification **⭐⭐⭐** (相关度: 60%, 质量: 0.7)

- **arXiv ID**: [2608.26771](https://arxiv.org/abs/2608.26771)  · [📄 PDF](https://arxiv.org/pdf/2608.26771)
- **作者**: Zibo Zhou, Zongsen Qiu, Rui Chen et al. (6 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-27 · **分类**: cs.CV
- **摘要（中）**: 该论文针对茶叶病害分类中轻量模型在小型数据集上欠拟合的问题，研究了从DINOv2教师到轻量视觉状态空间模型学生的跨架构知识蒸馏。识别并修复了训练稳定性问题，通过渐进卷积茎和门控双向选择扫描块，学生模型准确率从92.32%提升至95.41%，最佳单次达96.20%。该方法展示了跨架构蒸馏的可行性。
- **摘要（英）**: This paper studies cross-architecture KD from DINOv2 to a lightweight SSM student for tea disease classification, fixing training stability issues. Accuracy improves from 92.32% to 95.41%, demonstrating effectiveness.
- **评估**: 知识蒸馏方法有参考价值，但应用领域与自动驾驶相关性中等。
- **核心贡献**: 实现了跨架构知识蒸馏到轻量SSM模型。
- **创新点**: 解决SSM学生训练稳定性问题。
- **结果**: 准确率提升3.09个百分点。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Automated tea leaf disease classification supports precision agriculture, yet deploying accurate models on edge devices remains challenging under tight compute budgets. Self-supervised vision foundation models such as DINOv2 provide strong features but are too large for field deployment, while lightweight models trained from scratch on small agricultural datasets often underfit. We study cross-architecture knowledge distillation (KD) from a fine-tuned DINOv2 teacher (Vision Transformer) to a compact bidirectional Visual State Space Model (LVSSM) student, an underexplored direction because the architectures use fundamentally different token-mixing mechanisms. We identify and fix two training-stability problems that prevent the from-scratch SSM student from learning on limited data: a single large patch-embedding convolution and a fusion layer that severs the residual path. With a progressive convolutional stem and gated bidirectional selective-scan block, the 4.45M-parameter student trains stably. Across three seeds, temperature-scaled logit distillation raises test accuracy from 92.32+/-2.14% to 95.41+/-1.17% (best single run: 96.20%; macro-F1: 94.45%), a +3.09 percentage-point mean gain. The student uses 5.0 times fewer parameters than the 22M-parameter teacher while retaining 98.3% of its accuracy. Ablations show that intermediate feature-alignment losses reduce accuracy, making simple logit-level KD the strongest configuration. A fair from-scratch comparison shows the gain is specific to students that start below the teacher. We report per-class metrics, confusion matrices, bootstrap confidence intervals, and FLOPs/latency measurements, and discuss limitations including the single-dataset scope and simplified non-official SSM implementation.

</details>

### 3. Systematic Literature Review of Machine Learning Models and Applications for Text Recognition **⭐⭐** (相关度: 20%, 质量: 0.5)

- **arXiv ID**: [2608.26500](https://arxiv.org/abs/2608.26500)  · [📄 PDF](https://arxiv.org/pdf/2608.26500)
- **作者**: Nuzhat Khan, Ab Al-Hadi Ab Rahman, Shahriyar Masud Rizvi et al. (8 authors)
- **🏷️ 机构**: Faculty of Electrical Engineering, Universiti Teknologi Malaysia, Johor Bahru, Malaysia, Faculty of Artificial Intelligence, Universiti Teknologi Malaysia, Kuala Lumpur, Malaysia, Department of Electrical and Electronic Engineering, American International University-Bangladesh, Dhaka, Bangladesh
- **提交日期**: 2026-08-27 · **分类**: cs.CV, cs.LG · **📚 被引**: 12
- **摘要（中）**: 该论文针对OCR领域缺乏系统性综述的问题，基于PRISMA指南对2015-2025年间97项研究进行了全面评估。论文梳理了AI模型从传统OCR到深度学习的演变，分析了应用领域、数据类型、语言覆盖范围及挑战。研究发现OCR技术已能处理结构化与非结构化文本、场景文本识别和多语言处理，但仍存在未解决的挑战。该综述为OCR领域提供了宏观视角，但与自动驾驶感知方向的相关性较低。
- **摘要（英）**: This paper addresses the lack of systematic reviews in OCR by conducting a PRISMA-based comprehensive assessment of 97 studies from 2015 to 2025. It traces the evolution of AI models, application domains, data types, and linguistic coverage, highlighting progress in handling structured/unstructured text and multilingual processing. The review provides a macro-level overview but has limited direct relevance to autonomous driving perception.
- **评估**: 作为OCR领域的系统综述，对文本识别研究者有参考价值，但与自动驾驶感知方向关联较弱。
- **核心贡献**: 提供了OCR领域近十年AI模型演变的系统性综述。
- **创新点**: 采用PRISMA指南进行严格的文献筛选与分析。
- **结果**: 识别出关键OCR模型并分析了其性能、优势与局限。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Optical Character Recognition (OCR) for text recognition using machine vision has significantly improved, particularly when handling heterogeneous textual data. Traditional OCR models struggle with script variations, writing styles, and degraded documents. Advancements in technology are leading to new AI models with improved architecture for handling multiple languages and complex data formats. Despite this progress, a comprehensive evaluation of OCR advancements remains limited. Based on the established preferred reporting items for systematic reviews and meta-analysis (PRISMA) guidelines, this literature review presents an extensive assessment of OCR research to trace the evolution of AI models over the past decade. It explores the transition in AI models, application domains, data types, linguistic coverage, and challenges. Through a detailed analysis of 97 selected studies published during January 2015 - January 2025, key OCR models are identified, and their performance, strengths, and limitations are analyzed. The findings highlight how OCR technologies have evolved to address structured and unstructured text, scene text recognition, and multilingual processing. Unresolved challenges include limited resources for underrepresented languages, high variability in handwritten text, visual similarity among characters, and constraints in real-time OCR applications. To address these issues, several promising approaches are proposed. Key suggestions include self-supervised learning, multimodal AI, automated machine learning (AutoML), AI-assisted postprocessing, tiny machine learning (TinyML), and the creation of joint corpora for script matching. The future recommendations aim to enhance OCR accuracy and tackle the challenges identified for real-time industrial applications. This study will guide future research and establish a foundation for OCR field.

</details>

### 4. Data-efficient crack quantification in lithium-ion cathodes using foundation model transfer **⭐⭐⭐** (相关度: 30%, 质量: 0.7)

- **arXiv ID**: [2608.27162](https://arxiv.org/abs/2608.27162)  · [📄 PDF](https://arxiv.org/pdf/2608.27162)
- **作者**: Thorsten Tegetmeyer-Kleine, Thomas Schmitt, Phillip Aquino et al. (6 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-27 · **分类**: cond-mat.mtrl-sci, cs.CV, cs.LG
- **摘要（中）**: 该论文针对锂离子电池阴极颗粒裂纹量化中标注瓶颈的问题，提出使用冻结的自监督视觉Transformer编码器结合轻量级可训练解码器和迭代模型辅助标注，将稀疏标注转化为群体级退化测量。在三个120兆像素NMC阴极截面上，该方法成功区分晶内裂纹与早期/晚期晶间裂纹，并得到裂纹宽度、曲折度和面积分数的逐颗粒分布。结果显示循环老化样本的晚期晶间裂纹覆盖率4.6%，远高于初始和日历老化样本的0.5%，与反复电化学循环导致的退化一致。该方法展示了自监督视觉模型在材料科学中的应用潜力。
- **摘要（英）**: This paper tackles the annotation bottleneck in quantifying particle cracking in lithium-ion cathodes by using a frozen self-supervised vision transformer encoder with a lightweight decoder and iterative model-assisted annotation. Applied to three 120-megapixel NMC cross-sections, it distinguishes crack types and yields per-particle distributions, finding 4.6% late intergranular crack coverage in cycled samples versus 0.5% in others. It demonstrates the potential of self-supervised vision for material science, though not directly related to autonomous driving.
- **评估**: 方法设计巧妙，展示了自监督视觉Transformer在科学图像分析中的泛化能力，但领域差异较大。
- **核心贡献**: 提出数据高效的裂纹量化框架，利用基础模型迁移解决标注稀缺问题。
- **创新点**: 冻结自监督编码器与轻量解码器结合，配合迭代标注策略。
- **结果**: 在NMC阴极数据上实现高精度裂纹分类与量化，揭示退化机制。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Battery lifetime is central to sustainable electrification, yet the particle cracking that drives lithium-ion cathode aging is hard to measure: quantitative microscopy of this degradation is bottlenecked by annotation, because each destructive electron-microscopy cross-section spans hundreds of megapixels and pixel-level expert labelling requires hours per image. We show that a frozen self-supervised vision-transformer encoder, combined with a lightweight trainable decoder and iterative model-assisted annotation, turns this sparse labelling budget into population-scale degradation measurements. Applied to three 120-megapixel NMC cathode cross-sections representing initial, cycled-aged and calendar-aged states, the framework distinguishes intragranular cracks from early- and late-stage intergranular cracks and yields per-particle distributions of crack width, tortuosity and area fraction. Late intergranular crack coverage reaches 4.6% in the cycled sample versus 0.5% in the initial and calendar-aged samples, forming more tortuous, higher-coverage networks, consistent with degradation from repeated electrochemical cycling rather than elevated-temperature storage alone. A single destructive image yields the population-level statistics needed for lifetime-extending design, aging assessment and second-life decisions.

</details>

---

## 📊 统计

| 领域 | 论文数 |
|------|--------|
| VLM | 10 |
| Multimodal | 10 |
| Self-supervised Vision | 4 |
| **总计** | **24** |