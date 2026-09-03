# 📚 arXiv 每日论文报告（我的领域）

**报告日期**: 2026-09-04  
**论文来源**: [arXiv cs.CV Recent](https://arxiv.org/list/cs.CV/recent)  
**关注论文数**: 53 篇（其中 53 篇经大模型中文评估）

> 匹配领域: Object Detection、Autonomous Driving、3D Detection、BEV、Occupancy、Multi-camera Perception、Tracking、Open-set Detection、FOD Detection、VLM、Vision Transformer、Self-supervised Vision、Video Understanding、Multimodal、Continual Learning、Neural Architecture Search、Network Pruning、Knowledge Distillation

## 📑 目录

- [VLM](#vlm) (10篇)
- [Object Detection](#object-detection) (8篇)
- [Vision Transformer](#vision-transformer) (5篇)
- [Multi-camera Perception](#multi-camera-perception) (5篇)
- [Self-supervised Vision](#self-supervised-vision) (5篇)
- [Video Understanding](#video-understanding) (4篇)
- [Autonomous Driving](#autonomous-driving) (4篇)
- [Multimodal](#multimodal) (3篇)
- [Network Pruning](#network-pruning) (3篇)
- [3D Detection](#3d-detection) (2篇)
- [Knowledge Distillation](#knowledge-distillation) (2篇)
- [Tracking](#tracking) (1篇)
- [Open-set Detection](#open-set-detection) (1篇)

## VLM

### 1. Detecting Object Hallucinations in Large Vision-Language Models via Cross-Modal Attention Drifts and Mask-Based Verification **⭐⭐⭐⭐** (相关度: 70%, 质量: 0.8)

- **arXiv ID**: [2609.02028](https://arxiv.org/abs/2609.02028)  · [📄 PDF](https://arxiv.org/pdf/2609.02028)
- **作者**: Xuanbing Wen, Boxu Chen, Le Yang et al. (7 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-02 · **分类**: cs.CV
- **摘要（中）**: ①针对大型视觉语言模型（LVLM）中的对象幻觉检测问题，现有方法仅利用单层注意力，忽略了跨层演化。②提出CADMP框架，结合相邻层跨模态注意力漂移与针对视觉掩蔽的预测敏感性，在解码时量化注意力分布变化并选择最大漂移区域进行掩蔽验证。③改进点在于利用跨层注意力漂移表征视觉接地稳定性，并通过掩蔽后的概率变化验证预测是否真正依赖视觉证据，形成互补信号。④在多个基准和代表性开源模型上验证了有效性，但摘要未提供具体数据。
- **摘要（英）**: This paper addresses object hallucination detection in LVLMs by proposing CADMP, which combines adjacent-layer cross-modal attention drift with mask-based prediction sensitivity. It captures abrupt transitions in visual grounding and verifies prediction dependence on visual evidence. Experiments on multiple benchmarks demonstrate its effectiveness, though specific metrics are not detailed in the abstract.
- **评估**: 该工作从跨层注意力动态角度切入幻觉检测，方法轻量且具有理论新意，对提升LVLM可靠性有实际价值。
- **核心贡献**: 提出一种轻量级对象幻觉检测框架，利用跨层注意力漂移和掩蔽验证信号。
- **创新点**: 首次将相邻层注意力漂移与掩蔽敏感性结合用于幻觉检测。
- **结果**: 在多个基准上验证了检测有效性，但未给出具体数值。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite recent advances in large vision-language models (LVLMs), object hallucination remains a major barrier to their reliable deployment. Existing detection methods often characterize visual grounding using attention from individual layers, leaving its evolution across layers underexplored. We propose CADMP, a lightweight object hallucination detection framework that combines adjacent-layer cross-modal attention drift with prediction sensitivity to targeted visual masking. During decoding, CADMP quantifies distributional changes between consecutive cross-modal attention maps to capture abrupt transitions in visual grounding. It then selects the transition with the largest drift, locates the corresponding visually relevant regions, and measures the change in prediction probability after masking these regions. These two signals provide complementary evidence: attention drift characterizes the stability of internal visual grounding, while probability variation verifies whether a prediction truly depends on the identified visual evidence. A lightweight detector integrates both signals to identify hallucinated predictions. Experiments on multiple benchmarks and representative open-source LVLMs demonstrate that CADMP achieves consistently competitive detection performance. Ablation studies further confirm the complementary contributions of adjacent-layer drift modeling and mask-based grounding verification.

</details>

### 2. InfraPatch: Cross-Task Targeted Grayscale Patch Attacks on Infrared-Adapted Vision-Language Models **⭐⭐⭐** (相关度: 60%, 质量: 0.7)

- **arXiv ID**: [2609.02233](https://arxiv.org/abs/2609.02233)  · [📄 PDF](https://arxiv.org/pdf/2609.02233)
- **作者**: Chengyin Hu, Dingyi Lu, Jiaju Han et al. (8 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-02 · **分类**: cs.CV, cs.AI
- **摘要（中）**: ①针对红外视觉语言模型（IR-VLM）在低可见度条件下对目标对抗攻击的鲁棒性理解不足，现有补丁攻击主要针对RGB模型或单一任务。②提出InfraPatch，一种白盒、逐实例的灰度补丁攻击框架，在约5%局部面积预算内优化紧凑单通道补丁，结合代理引导放置和任务自适应语义目标，诱导分类、字幕和二元VQA中的目标行为。③改进点在于首次系统研究IR-VLM的跨任务目标攻击，并采用代理位置搜索提升攻击效率。④在10个红外适配模型变体上，目标攻击成功率从86.00%到100%，在CLIP和BLIP-2上代理搜索分别提升成功率6.67和10.33个百分点。
- **摘要（英）**: This paper proposes InfraPatch, a white-box targeted grayscale patch attack framework for IR-VLMs, optimizing compact patches within a 5% area budget across classification, captioning, and binary VQA tasks. It introduces proxy-guided placement and task-adaptive objectives, achieving 86-100% attack success rates on ten model variants. Proxy location search improves success by 6.67 and 10.33 points on CLIP and BLIP-2, respectively.
- **评估**: 该研究填补了IR-VLM对抗鲁棒性研究的空白，对多模态感知安全有重要启示。
- **核心贡献**: 提出首个针对红外视觉语言模型的跨任务灰度补丁攻击框架。
- **创新点**: 结合代理引导放置与任务自适应语义目标，实现高效目标攻击。
- **结果**: 在10个模型上达到86%-100%攻击成功率。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Infrared vision-language models (IR-VLMs) have emerged as a promising paradigm for multimodal perception under low-visibility conditions, yet their robustness to targeted adversarial attacks remains poorly understood. Existing adversarial patch methods mainly study RGB-based models or a single downstream task and do not characterize whether localized perturbations can induce an intended semantic target in IR-VLMs. We propose InfraPatch, a white-box, per-instance framework for targeted digital grayscale patch attacks against IR-VLMs. InfraPatch optimizes a compact single-channel patch within an approximately 5% local-area budget, combines proxy-guided placement with task-adaptive semantic objectives, and induces target behaviors in image classification, image captioning, and binary visual question answering. We evaluate ten infrared-adapted model variants on 300 synthetic infrared-style images generated by applying DiffV2IR to a fixed 30-category COCO subset, using clean-conditioned targeted success criteria. InfraPatch achieves targeted attack success rates from 86.00% to 100% across the ten variants. On CLIP and BLIP-2, proxy location search improves success by 6.67 and 10.33 percentage points over optimized random placement, respectively; LLaVA-1.5 remains saturated near 100% under both settings. Patch-area and objective ablations further expose substantial differences in vulnerability across architectures and task formats. These results show that small grayscale patches can inject chosen target semantics across IR-VLM families under a controlled digital threat model, motivating stronger robustness evaluation for infrared multimodal systems.

</details>

### 3. TempoGround: State-Aware Streaming Visual Grounding with Vision-Language Models **⭐⭐⭐⭐** (相关度: 85%, 质量: 0.85)

- **arXiv ID**: [2609.02359](https://arxiv.org/abs/2609.02359)  · [📄 PDF](https://arxiv.org/pdf/2609.02359)
- **作者**: Leqian Ding, Junning Qiu, Manwen Yang et al. (5 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-02 · **分类**: cs.CV
- **摘要（中）**: ①针对流式输入下视觉定位中的身份漂移、跨帧不一致和部分遮挡下的脆弱定位问题。②提出TempoGround，一个VLM原生框架，检测跨帧对象对应关系并显式建模对象存在状态，通过状态感知的跨帧对应课程预测机制，解决2D实例关联、预测对象进入/持续/离开状态、解码2D框并提升至相机帧3D框。③改进点在于引入流式定位强化（SGR），用可验证的定位、身份和一致性奖励优化模型。④摘要未提供具体数据，但声称实现准确且一致的流式定位。
- **摘要（英）**: This paper presents TempoGround, a VLM-native framework for streaming visual grounding that models object presence states and cross-frame correspondence via a curriculum prediction mechanism. It introduces Streaming Grounding Reinforcement with verifiable rewards to enhance localization and identity consistency. The method addresses identity drift and occlusion issues, though specific performance metrics are not provided.
- **评估**: 该工作针对流式视觉定位的痛点，结合状态建模和强化学习，对自动驾驶等实时感知场景有较高参考价值。
- **核心贡献**: 提出状态感知的流式视觉定位框架，结合课程预测和强化学习。
- **创新点**: 显式建模对象存在状态并引入可验证的流式定位奖励。
- **结果**: 实现准确一致的流式定位，但未提供具体数值。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Visual grounding maps language referents to spatial targets and is central to open-vocabulary perception with vision-language models. Existing methods have made substantial progress on single-frame and video-based visual grounding, yet under streaming inputs they still suffer from identity drift, cross-frame inconsistency, and fragile localization under partial occlusion. To address these issues, we present TempoGround, a VLM-native framework that detects cross-frame object correspondence and explicitly models object presence states, thereby enabling accurate and consistent visual grounding under streaming inputs. The key is a curriculum prediction mechanism guided by state-aware cross-frame correspondence: TempoGround resolves 2D instance association, predicts whether each object newly enters, continues in, or leaves the view, decodes the 2D box, and then lifts it to a camera-frame 3D box. As token-level supervision alone cannot capture the geometric objectives of streaming grounding, we further introduce Streaming Grounding Reinforcement (SGR), which optimizes TempoGround with verifiable Grounding, Identity, and Consistency rewards, jointly reinforcing persistent localization and temporally consistent predictions. We carefully design a three-stage training strategy and train TempoGround on large-scale data. We evaluate visual grounding under causally streaming inputs on multiple challenging benchmarks: TempoGround improves F1_2D@0.5 and F1_2D@0.95 by 4.4 and 0.5 on average, and F1_3D@0.25 and AP_3D by 6.2 and 7.5, respectively. These results demonstrate that TempoGround provides a practical foundation for visual grounding under streaming inputs.

</details>

### 4. RVSD: Retrieval Vision Sparse Decoding for Mitigating Visual Hallucinations in Large Vision-Language Models **⭐⭐⭐⭐** (相关度: 75%, 质量: 0.8)

- **arXiv ID**: [2609.02731](https://arxiv.org/abs/2609.02731)  · [📄 PDF](https://arxiv.org/pdf/2609.02731)
- **作者**: Canjie Liu, Jiawen Kang, Jinbo Wen et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/canjie-liu/RVSD](https://github.com/canjie-liu/RVSD)
- **提交日期**: 2026-09-02 · **分类**: cs.CV, cs.AI
- **摘要（中）**: ①针对大型视觉语言模型中的视觉幻觉问题，现有解决方案需要精选数据集、额外训练或多轮解码，计算开销大。②提出RVSD，一个无需训练、即插即用的解码框架，首次在单次解码中统一令牌稀疏化和语义空间视觉检索（SSVR）。③改进点在于引入语义导向的令牌选择策略，选择性稀疏化冗余令牌同时保留关键视觉信息，并将视觉补偿重构为共享语义空间中的按需跨模态检索。④实验表明RVSD在缓解视觉幻觉方面达到最先进性能，并在长上下文生成中保持鲁棒抑制能力。
- **摘要（英）**: This paper proposes RVSD, a training-free decoding framework that unifies token sparsification and semantic-space visual retrieval to mitigate visual hallucinations in LVLMs. It introduces semantics-directed token selection and SSVR for on-demand cross-modal compensation. RVSD achieves state-of-the-art hallucination mitigation with robust performance in long-context generation.
- **评估**: 该工作提供了一种高效、无需训练的幻觉抑制方案，对实际部署有显著价值。
- **核心贡献**: 提出首个统一令牌稀疏化和语义检索的免训练解码框架。
- **创新点**: 在单次解码中结合语义导向令牌选择与跨模态检索。
- **结果**: 在幻觉缓解上达到最先进性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large vision-language models have achieved remarkable success in vision-language tasks. However, they remain prone to Visual Hallucinations (VHs), undermining their reliability in real-world applications. Existing solutions typically require curated datasets, additional training, or multi-round decoding, resulting in considerable computational overhead. In this paper, we propose \textbf{RVSD} (\underline{R}etrieval \underline{V}ision \underline{S}parse \underline{D}ecoding), a training-free and plug-and-play decoding framework that, for the first time, unifies token sparsification and \textbf{Semantic-Space Visual Retrieval} (SSVR) within a single decoding pass. Within RVSD, we introduce a \textbf{semantics-directed token selection} strategy that selectively sparsifies redundant tokens while preserving critical visual information. We further propose the SSVR mechanism, which reformulates visual compensation as an on-demand cross-modal retrieval process within a shared semantic space. Extensive experiments demonstrate that RVSD achieves state-of-the-art performance in mitigating VHs while maintaining robust suppression capabilities under long-context generation settings. Our code is available here.\footnote{https://github.com/canjie-liu/RVSD}

</details>

### 5. FairLens: Benchmarking Fairness in Vision-Language Models for High-Stakes Decision-Making **⭐⭐⭐** (相关度: 50%, 质量: 0.75)

- **arXiv ID**: [2609.01691](https://arxiv.org/abs/2609.01691)  · [📄 PDF](https://arxiv.org/pdf/2609.01691)
- **作者**: Vahid Reza Khazaie, Ahmed Y. Radwan, Shaina Raza
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-01 · **分类**: cs.CV, cs.LG
- **摘要（中）**: ①针对VLM在高风险决策（招聘、法律、医疗）中的公平性和有效性评估不足。②提出FAIRLENS基准和评估框架，配对真实人脸图像与封闭/开放问题，生成每模型超10万图像-问题对，从人口统计平价、合理性、人口统计关联和自由文本生成偏差四个视角评估。③改进点在于将合理性作为核心有效性标准，要求模型基于问题证据回答并在图像不支持时弃权。④评估8个VLM发现主要失败是无根据推断而非不平等对待，最弱模型在99%无法回答的问题上做出推断，法律和医疗领域失败最严重。
- **摘要（英）**: This paper introduces FAIRLENS, a benchmark for evaluating fairness and validity of VLM responses in hiring, legal, and healthcare domains, with over 100K image-question pairs per model. It assesses demographic parity, soundness, association, and text bias, finding that primary failures stem from unwarranted inference rather than unequal treatment. The weakest model infers on 99% of unanswerable questions, with severe issues in legal and healthcare.
- **评估**: 该基准为VLM在高风险场景的可靠性评估提供了重要工具，但领域相关性对自动驾驶研究者较低。
- **核心贡献**: 提出首个面向高风险决策的VLM公平性与有效性基准。
- **创新点**: 将合理性作为核心标准，结合多维度公平性评估。
- **结果**: 揭示VLM主要失败模式为无根据推断。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-language models (VLMs) are increasingly used to make decisions from visual inputs. We introduce FAIRLENS, a benchmark and evaluation framework for measuring both the fairness and the validity of VLM responses in three high-stakes domains: hiring, legal, and healthcare. FAIRLENS pairs real face images spanning gender, race, and age groups with closed- and open-ended questions, giving more than 100K image-question pairs per model, and evaluates responses from four complementary views: demographic parity over adverse outcome rates, soundness, demographic association over unsupported roles and statuses, and bias in free-text generation. Soundness is the central validity criterion: a response is sound when it follows the evidence stated in the question and abstains when the image cannot support an answer. Evaluating eight VLMs, we find that the primary failure is unwarranted inference rather than unequal treatment. Models routinely infer qualifications, threat, illness, or professional role from a face instead of abstaining, and the weakest model does so on 99% of the questions its input cannot answer. These failures are most severe in legal and healthcare, where recognizing insufficient evidence matters most, and disparity metrics alone would miss them: parity gaps are small in absolute terms, yet when baseline adverse rates are low the same gap means one demographic group receives adverse labels several times as often as another, and a small gap can equally reflect a model that treats every group unsafely. Bias in free-text responses is only loosely coupled to multiple-choice accuracy, so correct structured answers do not imply safe generation. FAIRLENS shows that fair high-stakes VLM behavior requires similar treatment across groups and refusal to infer high-stakes attributes from appearance, and its question suite transfers to any face corpus with demographic annotations.

</details>

### 6. Who Drives the Probability Game of VLMs? A Temporal Causal Drive Evaluation Framework **⭐⭐⭐** (相关度: 55%, 质量: 0.7)

- **arXiv ID**: [2609.02000](https://arxiv.org/abs/2609.02000)  · [📄 PDF](https://arxiv.org/pdf/2609.02000)
- **作者**: Shuyao Xiao, Shengling Wang, Haoyu Niu et al. (7 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-02 · **分类**: cs.CV
- **摘要（中）**: ①针对VLM评估中传统指标仅关注最终答案质量，无法揭示不同信息源对生成过程的影响。②提出因果和时间评估框架，基于结构因果模型，通过干预和后门调整推导三个逐步索引的因果驱动指标：视觉因果驱动（VCD）、问题因果驱动（QCD）和前缀因果驱动（PCD），无需参考答案。③改进点在于提供源特定生成模式的时序分析。④在Qwen3-VL-8B-Instruct和InternVL2-8B上验证，QCD和PCD比观测PMI基线降低恢复误差34.8%和47.1%，并发现从早期问题/视觉引导到后期前缀依赖的转变。
- **摘要（英）**: This paper proposes a causal and temporal evaluation framework for VLMs, deriving step-indexed metrics (VCD, QCD, PCD) via interventions and backdoor adjustment to trace information source influence during decoding. Experiments on multiple models show QCD and PCD reduce recovery error by 34.8% and 47.1% over PMI baselines, revealing a transition from early question/visual guidance to prefix reliance.
- **评估**: 该工作提供了VLM生成过程的因果分析新视角，对理解模型行为有理论价值。
- **核心贡献**: 提出基于因果模型的VLM时序驱动评估框架。
- **创新点**: 引入无需参考答案的因果驱动指标。
- **结果**: 显著降低恢复误差并揭示生成模式转变。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-language models (VLMs) are increasingly evaluated on complex image and video understanding tasks, yet conventional metrics primarily assess final-answer quality and reveal little about how different information sources shape the generation process. We propose a causal and temporal evaluation framework that traces the evolving roles of visual input, question text, and generated prefixes during autoregressive decoding. Grounded in a Structural Causal Model, we use interventions and backdoor adjustment to derive three step-indexed causal-drive metrics---Visual Causal Drive (VCD), Question Causal Drive (QCD), and Prefix Causal Drive (PCD)---for characterizing source-specific generation patterns without requiring reference answers. Experiments on Qwen3-VL-8B-Instruct across MAVIS, LLaVA-Video-178K, and MiraData, together with cross-model validation on InternVL2-8B, reveal a consistent transition from stronger early question and visual guidance toward increasing reliance on generated prefixes. Randomized-intervention validation shows that QCD and PCD reduce recovery error over observational PMI baselines by 34.8\% and 47.1\%, respectively. On VLMBias, the prefix--visual imbalance score achieves 0.767 AUROC and 0.873 AUPRC for distinguishing prior-driven from visually grounded generations. These results show that causal-drive trajectories provide complementary source-level diagnostics for multimodal generation.

</details>

### 7. Does Playing it Safe Count as Faithfulness? Reassessing LVLM Hallucination Mitigation Methods **⭐⭐⭐⭐** (相关度: 75%, 质量: 0.85)

- **arXiv ID**: [2609.01888](https://arxiv.org/abs/2609.01888)  · [📄 PDF](https://arxiv.org/pdf/2609.01888)
- **作者**: Mehrdad Fazli, Sina Mansouri, Mohit Marvania et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-01 · **分类**: cs.CV
- **摘要（中）**: ①该论文针对大型视觉语言模型（LVLM）在幻觉缓解方法评估中的问题，质疑现有基准分数下降是否真正反映多模态接地能力提升，而非保守生成。②作者评估了三种LVLM上的六种推理时缓解方法，并跨四个基准（包括幻觉专用基准和MMStar能力基准）进行分析。③相比已有工作，该研究揭示了两个一致模式：幻觉减少常伴随信息量降低（如对象召回、视觉覆盖或响应详细度下降），且幻觉基准上的改进不能可靠迁移到更广泛的多模态能力。④结果表明，当前评估协议可能因奖励保守生成而高估进展，主张幻觉缓解应作为忠实性-信息量-能力权衡来评估，而非仅依赖幻觉分数。
- **摘要（英）**: This paper questions whether lower hallucination scores in LVLMs reflect improved multimodal grounding or merely conservative generation, evaluating six mitigation methods across three models and four benchmarks. It finds hallucination reduction often couples with reduced informativeness and inconsistent transfer to broader capabilities, arguing for a faithfulness-informativeness-capability trade-off in evaluation.
- **评估**: 该论文对幻觉缓解领域的评估方法提出重要批判，具有方法论反思价值，对VLM可靠部署有指导意义。
- **核心贡献**: 揭示了幻觉缓解方法中保守生成与能力退化的问题，提出更全面的评估框架。
- **创新点**: 首次系统分析幻觉分数与信息量及多模态能力之间的权衡关系。
- **结果**: 证明现有幻觉基准可能高估进展，需采用多维评估标准。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent inference-time hallucination mitigation methods for large vision-language models (LVLMs) report strong gains on hallucination benchmarks. However, it remains unclear whether lower hallucination scores reflect improved multimodal grounding or more conservative generation. We evaluate six mitigation methods across three LVLMs and four benchmarks, including hallucination-focused evaluation and the diverse capability benchmark MMStar. Our analysis reveals two consistent patterns. First, hallucination reduction is often coupled with reduced informativeness: methods that lower hallucination rates also reduce object recall, visual coverage, or response detailedness. Second, improvements on hallucination benchmarks do not reliably transfer to broader multimodal capabilities, with methods showing inconsistent or degraded performance on fine-grained perception and reasoning tasks. Our findings suggest that current evaluation protocols may overestimate progress by rewarding conservative generation. We argue that hallucination mitigation should be evaluated as a faithfulness--informativeness--capability trade-off rather than through hallucination scores alone.

</details>

### 8. Lightweight Adaptation of General-Purpose VLMs for Multispectral and SAR Image Understanding **⭐⭐⭐** (相关度: 60%, 质量: 0.7)

- **arXiv ID**: [2609.02187](https://arxiv.org/abs/2609.02187)  · [📄 PDF](https://arxiv.org/pdf/2609.02187)
- **作者**: Shanji Liu, Kelu Yao, Junxiao Xue et al. (8 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-02 · **分类**: cs.CV
- **摘要（中）**: ①该论文针对通用视觉语言模型（VLM）难以直接处理多光谱和合成孔径雷达（SAR）图像的问题，因为预训练编码器基于三通道自然图像。②提出了一种轻量级适配协议，将每个观测渲染为五个光学视图和一个SAR视图，并通过LoRA适配语言网络和部分视觉Transformer块。③相比已有工作，该方法利用VLM的多图像接口，无需专用编码器或领域预训练，通过结构化监督和偏好对鼓励完整且一致的预测。④在六类土地覆盖识别任务上，该方法展示了有效性，但摘要未提供具体准确率数据。
- **摘要（英）**: This paper addresses VLM adaptation to multispectral and SAR imagery by proposing a lightweight protocol that renders observations as multiple views and uses LoRA for efficient tuning. It leverages the multi-image interface to avoid dedicated encoders, with structured supervision and preference pairs for consistent predictions, showing promise in land-cover recognition.
- **评估**: 该论文为遥感领域VLM适配提供轻量级方案，但实验细节有限，影响全面评估。
- **核心贡献**: 提出一种无需专用编码器的VLM多光谱和SAR图像适配方法。
- **创新点**: 利用多图像接口和LoRA实现跨传感器VLM迁移。
- **结果**: 在土地覆盖识别任务上验证了有效性，但具体数据未披露。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> General-purpose vision-language models (VLMs) now support strong visual recognition, instruction following, and generation. However, most pretrained visual encoders are built around three-channel natural images and do not directly accommodate observations such as native multispectral measurements or synthetic aperture radar (SAR). Adapting VLMs to these sensors typically requires dedicated encoders and domain pretraining, slowing the reuse of stronger general-purpose checkpoints. We show that the multi-image interface of general-purpose VLMs offers a lightweight alternative. Our protocol renders each observation as five optical views and one SAR view, names them in the prompt, and adapts the language network and selected visual transformer blocks with LoRA. This exposes band composites, spectral indices, and radar backscatter through an existing visual interface. For land-cover recognition, structured supervision couples predicted classes with sensor evidence. We further construct preference pairs in which a true label is omitted while its supporting evidence is retained, encouraging complete predictions that remain consistent with the observations. On a balanced six-class land-cover benchmark derived from BigEarthNet-v2, the adapted Qwen3-VL reaches 0.8275 micro F1. The same input and adaptation protocol improves all four tested VLM architectures and transfers to Sen1Floods11 flood verification and BigEarthNet.txt captioning. Image removal and mismatch controls show that the adapted models use the supplied sensor observations. Together, these results demonstrate that VLMs can be repurposed for multispectral and SAR tasks through rendered inputs and compact LoRA adaptation, without training a new foundation model.

</details>

### 9. Test-Time Logit Prompting for Source-Free Missing Modality Adaptation **⭐⭐⭐⭐** (相关度: 70%, 质量: 0.8)

- **arXiv ID**: [2609.02039](https://arxiv.org/abs/2609.02039)  · [📄 PDF](https://arxiv.org/pdf/2609.02039)
- **作者**: Taixi Chen, Nancy Guo
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-02 · **分类**: cs.CV
- **摘要（中）**: ①该论文针对视觉语言模型（VLM）在部署中遇到缺失模态输入时性能显著下降的问题，且现有方法依赖源训练数据，在隐私或存储限制下难以应用。②提出了测试时对数提示（TLP），一种轻量级无源测试时适应框架，通过不确定性感知调整和模态完整一致性正则化优化对数提示。③相比已有工作，TLP无需访问源数据，直接在测试时适应，适用于临床和个性化AI等场景。④摘要未提供具体性能数据，但方法设计针对缺失模态的预测偏移，具有实际应用潜力。
- **摘要（英）**: This paper addresses VLM performance degradation with missing modalities by proposing Test-Time Logit Prompting (TLP), a source-free adaptation framework. TLP optimizes logit prompts with uncertainty-aware adjustment and consistency regularization, enabling efficient test-time adaptation without source data, though specific results are not detailed.
- **评估**: 该论文解决实际部署中的缺失模态问题，方法新颖且实用，但缺乏实验数据支撑。
- **核心贡献**: 提出无源测试时适应框架TLP，处理VLM缺失模态输入。
- **创新点**: 利用对数提示和不确定性调整实现无需源数据的适应。
- **结果**: 摘要未给出具体效果，但框架设计有潜力。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-language models (VLMs) have achieved remarkable performance by leveraging complementary information from large-scale image-text pairs. However, missing-modality inputs are commonly encountered during real-world deployment, often leading to significant performance degradation. Existing methods primarily enhance model robustness by learning modality compensation strategies from source training data. However, their reliance on source training data makes them difficult to apply when original data are unavailable due to privacy, storage, or accessibility constraints, such as clinical applications and personalized AI services. This raises an important yet underexplored question: can VLMs be efficiently adapted at test time for visual recognition with missing modalities without accessing source training data? To this end, we propose Test-Time Logit Prompting (TLP), a lightweight source-free test-time adaptation framework for visual recognition with missing modalities. To address missing-induced prediction shifts, TLP optimizes logit prompts with uncertainty-aware adjustment and modality-complete consistency regularization, adaptively adjusting prediction confidence while preserving semantic consistency. Extensive experiments across diverse vision-language benchmarks demonstrate that TLP consistently enhances recognition performance under missing-modality scenarios, achieving up to 8\% improvements while requiring only hundreds of tunable parameters and a few test-time optimization steps.

</details>

### 10. Video2Reaction: Training Foundation Video Models to Predict Audience Reaction **⭐⭐⭐** (相关度: 30%, 质量: 0.6)

- **arXiv ID**: [2609.01816](https://arxiv.org/abs/2609.01816)  · [📄 PDF](https://arxiv.org/pdf/2609.01816)
- **作者**: Sidong Zhang, Trang Nguyen, Shiv Shankar et al. (7 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-01 · **分类**: cs.CV
- **摘要（中）**: 针对电影片段引发观众情绪反应预测缺乏大规模数据集的问题，提出了Video2Reaction多模态数据集，通过社交媒体评论聚合大规模情绪分布标签。方法上微调两个视觉语言模型（VLM）进行基准测试，并验证了预微调后向VCE数据集的迁移能力。相比现有工作，该数据集捕捉了情绪反应的自然多样性和主观性。实验表明，仅用VCE 1%训练数据微调的LLaVA-NeXT-Video-7B达到0.682的top-3准确率，与全量训练的最佳性能相当。
- **摘要（英）**: This paper introduces Video2Reaction, a multimodal dataset mapping movie segments to audience emotional reactions via social media comments, addressing the lack of large-scale induced-emotion data. It benchmarks LoRA-finetuned VLMs and demonstrates transfer to VCE, where LLaVA-NeXT-Video-7B with 1% VCE data achieves 0.682 top-3 accuracy, matching full-data performance.
- **评估**: 该论文贡献了一个新颖的数据集和迁移学习范式，但对自动驾驶感知领域相关性较低，主要面向视频理解与情感计算。
- **核心贡献**: 构建了大规模多模态情绪反应数据集Video2Reaction并验证了VLM的有效性。
- **创新点**: 利用社交媒体评论聚合情绪分布，建模主观情感标签。
- **结果**: 在VCE数据集上以1%训练数据达到与全量训练相当的性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce Video2Reaction, a multimodal dataset that maps short movie segments to the induced emotional reactions of viewers in the wild, as expressed through social media comments. Video2Reaction captures the natural diversity of emotional responses by aggregating reactions from online comments at scale, modeling labels as distributions over categorical emotions to better reflect the subjective and ambiguous nature of emotional perception. We benchmark two vision-language models (VLMs) finetuned with LoRA, showing that VLMs learn effectively from Video2Reaction and outperform specialized baselines on dominant reaction prediction. We further demonstrate that VLMs pre-finetuned on Video2Reaction transfer effectively to VCE, another induced emotion dataset with a different taxonomy and video domain. Notably, LLaVA-NeXT-Video-7B pre-finetuned on Video2Reaction and adapted on only 1% of VCE training data achieves a top-3 accuracy of 0.682, on par with the best reported VCE performance trained on the full dataset. The dataset is available at https://huggingface.co/datasets/infofusionlab/Video2Reaction

</details>

---

## Object Detection

### 1. UAV Thermal Imagery for Inert Ordnance Screening: Multi Campaign Dataset Development,Object Detection, and Practical Recommendations **⭐⭐⭐** (相关度: 50%, 质量: 0.75)

- **arXiv ID**: [2609.01738](https://arxiv.org/abs/2609.01738)  · [📄 PDF](https://arxiv.org/pdf/2609.01738)
- **作者**: Chad Melton,  PhD., Annabelle Kelton
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-01 · **分类**: cs.CV, cs.DB
- **摘要（中）**: ①该论文针对未爆炸弹药（UXO）污染区域的人道主义排雷问题，利用无人机热成像进行目标检测以辅助筛查。②创建了多战役UAV热图像数据集，包含惰性弹药，并训练了YOLOV11l和RT-DETR-R50算法进行自动候选检测。③相比已有工作，该研究提供了实际部署中的数据集和实用建议，涵盖不同季节、地面类型和飞行高度。④数据集包含5,855个热图像标签对，其中918个正图像和4,937个背景图像，但摘要未提供检测性能的具体指标。
- **摘要（英）**: This paper addresses UXO detection using UAV thermal imagery by creating a multi-campaign dataset and evaluating YOLOV11l and RT-DETR-R50 models. It provides practical recommendations for humanitarian demining, with a dataset of 5,855 label pairs across varied conditions, though specific detection metrics are not reported.
- **评估**: 该论文聚焦应用场景，数据集构建有实际价值，但方法创新性一般。
- **核心贡献**: 构建了多战役UAV热成像UXO数据集并评估了检测模型。
- **创新点**: 结合实际排雷需求提供数据集和操作建议。
- **结果**: 数据集和模型可用于自动化UXO筛查，但性能数据未明确。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Unexploded ordnance (UXO) continues to restrict civilian access, agricultural activity, infrastructure recovery, and environmental remediation in contaminated areas around the world. This study created a multi campaign UAV thermal image data set of inert ordnance, developed a labeled image set from collected imagery, tested object detection models, and identified practical considerations for humanitarian mine action and demining applications. Data were collected during four field campaigns in Tennessee under summer and winter conditions using inert mines, munitions, and other ordnance placed in short grass, tall vegetation, gravel, mulch, rock, compost, and compacted surfaces. Thermal imagery was collected under flight altitutes of 33 m and 15 m. The final source inventory contained 5,855 thermal image label pairs, including 918 positive images and 4,937 background images. After retaining all positive images and downsampling background images, the 33 m dataset contained 420 training and 106 validation images, while the 15 m dataset contained 629 training and 157 validation images. YOLOV11l and RT-DETR-R50 algorithms were trained and evaluated to develop an automated candidate detection model. Practical recommendations include collecting thermal and RGB imagery together, incorporating varied surfaces and background only imagery, considering periods following changes in solar exposure, balancing survey coverage against target pixel representation, calibrating models with representative local data, and retaining qualified human review. The intended use is screening and prioritization for follow on technical survey or EOD assessment, and not a standalone clearance.

</details>

### 2. Stereo 4D Radar for 3D Object Detection: Integrating Geometric Alignment and Absolute Velocity Estimation **⭐⭐⭐⭐** (相关度: 85%, 质量: 0.7)

- **arXiv ID**: [2609.02560](https://arxiv.org/abs/2609.02560)  · [📄 PDF](https://arxiv.org/pdf/2609.02560)
- **作者**: Seung-Hyun Song, Dong-Hee Paek, Woong-Chan Byun et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-02 · **分类**: cs.CV
- **摘要（中）**: 针对单4D雷达点云稀疏、多径干扰和仅能提供径向速度的问题，提出了基于立体4D雷达的3D目标检测框架，利用左右雷达的几何视差估计物体绝对速度，并融合互补特征增强感知鲁棒性。相比单雷达方法，在自建立体4D雷达数据集上AP 3D提升8.82点，AP BEV提升9.0点。该方法有效利用了雷达的几何和运动信息，改善了恶劣天气下的目标检测。
- **摘要（英）**: This paper proposes a stereo 4D radar-based 3D object detection framework that exploits geometric disparity between left and right radars to estimate absolute velocity and fuse complementary features, addressing sparse and noisy radar data. It achieves 8.82 AP 3D and 9.0 AP BEV improvements over state-of-the-art mono 4D radar methods on an in-house dataset.
- **评估**: 该论文针对自动驾驶中的雷达感知难题，提出立体雷达融合方案，具有实际应用价值，但数据集为自建，泛化性待验证。
- **核心贡献**: 提出立体4D雷达3D检测框架，结合几何对齐与绝对速度估计。
- **创新点**: 利用双雷达视差恢复物体全速度，融合特征提升鲁棒性。
- **结果**: 在自建数据集上AP 3D和AP BEV分别提升8.82和9.0点。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Four-dimensional (4D) Radar is a powerful sensing modality capable of detecting surrounding three-dimensional (3D) objects under diverse weather conditions and providing Doppler-based motion information. However, raw 4D Radar signals contain significant clutter from road surfaces, guardrails, and surrounding vehicles, along with multipath-induced ghost reflections and the receiver's inherent noise floor. Consequently, preprocessing algorithms designed to remove such invalid measurements often make the Radar data excessively sparse. Moreover, the Doppler measurements provided by 4D Radar describe only the radial component of an object's velocity, limiting their ability to recover the full motion state. In this paper, we introduce a stereo 4D Radar-based 3D object detection framework that exploits the geometric disparity between left and right Radars to estimate the absolute velocity of objects and achieve more robust perception through the fusion of their complementary features. The effectiveness of the proposed framework is validated on our in-house stereo 4D Radar dataset, demonstrating performance gains of 8.82 points in AP 3D and 9.0 points in AP BEV over state-of-the-art mono 4D Radar baselines. These results demonstrate that absolute velocity estimation combined with stereo geometry-aware feature fusion leads to substantial improvements in 3D object detection.

</details>

### 3. Domain shift-robust object detection with GenAI image editing **⭐⭐⭐** (相关度: 60%, 质量: 0.6)

- **arXiv ID**: [2609.02299](https://arxiv.org/abs/2609.02299)  · [📄 PDF](https://arxiv.org/pdf/2609.02299)
- **作者**: Isabel D. Stein, Thijs A. Eker, Sebastiaan P. Snel et al. (7 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-02 · **分类**: cs.CV
- **摘要（中）**: 针对目标检测在域偏移（如光照、天气、遮挡）下性能下降的问题，提出利用扩散模型生成图像编辑模拟受控域偏移，以增强训练数据并桥接源域与目标域。以伪装军事车辆检测为挑战场景，训练于非伪装数据的检测器在真实伪装图像上性能显著下降。使用两种扩散编辑模型（如Qwen Image）进行数据增强，初步验证了生成编辑提升跨域鲁棒性的潜力。
- **摘要（英）**: This paper addresses domain shift in object detection by using diffusion-based generative image editing to simulate controlled shifts, bridging source and target domains. In a camouflaged military vehicle detection scenario, detectors trained on uncamouflaged data degrade substantially, and generative editing shows promise for improving out-of-domain robustness.
- **评估**: 该论文探索了生成式编辑用于域鲁棒性，思路新颖，但应用场景特殊，对通用自动驾驶检测的参考价值有限。
- **核心贡献**: 验证了生成图像编辑模拟域偏移以提升检测器跨域鲁棒性的可行性。
- **创新点**: 利用扩散模型编辑模拟受控域偏移，而非传统风格迁移。
- **结果**: 在伪装车辆检测中展示了生成增强的潜力，但具体数据未完整给出。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Object detectors often degrade under domain shifts such as changes in lighting, weather, or occlusion. These shifts alter object appearance and expose a reliance on visual shortcuts learned from the training distribution that do not generalize across domains. Acquiring sufficient real-world samples to capture such domain variation is particularly difficult in specialized, low-data settings. Recent advances in diffusion-based generative image editing have shown promise for improving the in-domain performance of object detectors through synthetic data augmentation. However, their potential to improve out-of-domain robustness remains largely unexplored. We hypothesize that generative image editing can simulate a controlled domain shift in training data, effectively bridging the gap between source and target domains. To test this, we studied camouflaged military vehicle detection as a challenging domain shift scenario. Detectors trained on uncamouflaged data demonstrate substantial degradation on real test imagery containing foliage, netting, and multi-spectral camouflage across 15 vehicle classes in close-up, ground-level imagery. We used two diffusion-based editing models, Qwen Image Edit 2509 and Flux.2 Dev, to synthetically add camouflage to the training data, alongside a LoRA fine-tuned version of Qwen. A non-generative black-bar occlusion baseline served as a lower bound on augmentation quality. Using a GroundingDINO detector trained on real and synthetic data, generative camouflage augmentation yielded substantial mAP improvements for foliage (+20.1) and netting (+14.4) camouflage. Generating multi-spectral camouflage proved more challenging, but LoRA fine-tuning improved performance by 4.4 mAP over the uncamouflaged baseline.

</details>

### 4. Information Density Imbalance in Visual Object Detection **⭐⭐⭐** (相关度: 50%, 质量: 0.6)

- **arXiv ID**: [2609.02369](https://arxiv.org/abs/2609.02369)  · [📄 PDF](https://arxiv.org/pdf/2609.02369)
- **作者**: Ziwei Zhao, Yanxi Lu, Yuwei Hu et al. (11 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-02 · **分类**: cs.CV
- **摘要（中）**: 针对目标检测中类别偏差无法仅由实例数量解释的问题，提出了信息密度概念及其度量方法，并观察到类别信息密度与准确率显著负相关。通过实验研究了训练过程对关系的影响，表明信息密度不平衡可能是类别偏差的潜在来源。基于此，对三种先进检测损失函数进行了简单改进，在Pascal VOC、COCO-LT和LVIS数据集上显著减少模型偏差并提升性能。
- **摘要（英）**: This paper introduces information density to explain category bias in object detection beyond instance count, showing a negative correlation with accuracy. Simple improvements to three loss functions using this concept reduce model bias and enhance performance on Pascal VOC, COCO-LT, and LVIS.
- **评估**: 该论文提供了新的视角分析类别偏差，但概念定义和实际应用仍需深入验证，对自动驾驶检测有间接参考。
- **核心贡献**: 提出信息密度概念并验证其与类别偏差的关系。
- **创新点**: 将信息密度融入损失函数以缓解类别偏差。
- **结果**: 在多个数据集上减少偏差并提升检测性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In object detection, the number of instances is typically used to determine whether a dataset exhibits a long-tailed distribution, implicitly assuming that the model will perform poorly on categories with fewer instances. This assumption has led to extensive research on category bias in datasets with imbalanced instance numbers. However, even in datasets where instance numbers are relatively balanced, models still exhibit category bias, indicating that instance count alone cannot explain this phenomenon. In this work, we first introduce the concept and measurement of information density. We then observe a significant negative correlation between a category's information density and its accuracy, and we investigate how the training process impacts this relationship. Empirical studies suggest that information density imbalance may be a potential source of category bias. To preliminarily validate the potential of information density, we made simple improvements to three advanced object detection loss functions using this concept. Experiments on the Pascal VOC, COCO-LT, and LVIS datasets demonstrate that information density can significantly reduce model bias while effectively enhancing the overall performance of existing loss functions. This study provides a new perspective for understanding the generalized bias phenomenon in object detection models and offers new tools for designing fairer loss functions and training strategies.

</details>

### 5. If It Moves, Radar Knows: A Physics-Aware Radar Transformer for Class-Agnostic Moving-Object Detection **⭐⭐⭐⭐** (相关度: 90%, 质量: 0.75)

- **arXiv ID**: [2609.02289](https://arxiv.org/abs/2609.02289)  · [📄 PDF](https://arxiv.org/pdf/2609.02289)
- **作者**: Yinghao Sun, Shuguang Li, Jinliang Shao et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/sunyinghao-uestc/PART](https://github.com/sunyinghao-uestc/PART)
- **提交日期**: 2026-09-02 · **分类**: cs.CV
- **摘要（中）**: 针对封闭集标注检测器无法识别训练类别外的移动物体问题，提出了物理感知雷达Transformer（PART），一种全稀疏雷达专用检测器，预测存在置信度、代表性表面点和2D地面速度。创新包括多普勒感知查询初始化（DAQI）和物理引导交叉注意力（PGCA），利用径向多普勒一致性和雷达截面积改善稀疏场景中的查询-物体关联。不确定性感知监督通过随机掩码和软目标减少对完整标注的依赖，仅用雷达数据实现类无关移动物体检测。
- **摘要（英）**: This paper presents PART, a fully sparse radar-only detector for class-agnostic moving-object detection, predicting existence, surface points, and velocity. Doppler-Aware Query Initialization and Physics-Guided Cross-Attention improve association in sparse scenes, while uncertainty-aware supervision reduces annotation reliance, addressing open-set detection beyond closed-set taxonomies.
- **评估**: 该论文针对开放集移动物体检测，利用雷达物理特性，对自动驾驶安全至关重要，方法创新且实用。
- **核心贡献**: 提出雷达专用类无关移动物体检测器PART。
- **创新点**: 将多普勒物理约束融入查询初始化和交叉注意力。
- **结果**: 在稀疏雷达场景中有效检测移动物体，减少标注依赖。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Detectors trained on closed-set annotations can miss rare moving objects outside the training taxonomy. Automotive radar provides category-independent Doppler motion cues and is less affected by adverse illumination and weather, but sparse, noisy returns hinder class-aware 3D box detection. Surface location and velocity remain useful for motion reasoning and collision avoidance when full box geometry is difficult to recover. We present the Physics-Aware Radar Transformer (PART), a fully sparse radar-only detector that predicts existence confidence, a representative surface point, and 2D ground-plane velocity for each moving-object hypothesis. Doppler-Aware Query Initialization (DAQI) replaces scene-independent learned queries with input-dependent proposals by clustering radar returns in position and velocity, easing query-object assignment in sparse scenes. Physics-Guided Cross-Attention (PGCA) incorporates radial-Doppler consistency and radar cross section (RCS) into query-point association. Uncertainty-aware supervision randomly masks ground-truth objects and assigns soft existence targets to ambiguous radar-supported queries, reducing reliance on exhaustive annotations. With only 1.1 million parameters, PART achieves a class-agnostic average precision (CA-AP) of 0.8827, a mean average surface translation error (mASTE) of 0.3188 m, and a mean average velocity error (mAVE) of 0.8084 m/s on nuScenes. It attains 0.9203 recall on rare and safety-relevant categories excluded from the standard evaluation and remains effective at night, in rain, and under severe occlusion. Inspection of apparent false positives shows that some predictions correspond to moving objects absent from the nuScenes annotations. Code and pretrained model weights will be publicly available at https://github.com/sunyinghao-uestc/PART.

</details>

### 6. DESA-TTA: Dynamic EMA and Source Anchoring for Test-Time Adaptation **⭐⭐⭐⭐** (相关度: 70%, 质量: 0.85)

- **arXiv ID**: [2609.01795](https://arxiv.org/abs/2609.01795)  · [📄 PDF](https://arxiv.org/pdf/2609.01795)
- **作者**: Atif Belal, Lilian Hollard, Marco Pedersoli et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/imatif17/DESA-TTA](https://github.com/imatif17/DESA-TTA)
- **提交日期**: 2026-09-01 · **分类**: cs.CV
- **摘要（中）**: ①针对视觉语言目标检测器在部署时面临分布偏移，均值教师TTA对固定EMA系数敏感且噪声伪标签导致学生漂移。②提出了DESA-TTA方法，通过动态时间平均和源锚定联合调节教师更新和学生漂移，动态EMA系数基于伪标签置信度和框密度估计不确定性，源锚定根据漂移程度部分恢复预训练参数。③相比现有TTA方法，无需额外开销，自适应调整EMA和锚定强度。④实验在多种分布偏移和两种VLOD架构上显示一致改进，但摘要未提供具体数值。
- **摘要（英）**: This paper addresses robustness issues in vision-language object detectors under distribution shifts by proposing DESA-TTA, which dynamically adjusts EMA coefficients based on teacher uncertainty and anchors student parameters to source values to prevent drift. It improves over fixed-EMA mean-teacher methods without extra overhead. Experiments show consistent gains across diverse shifts and architectures.
- **评估**: 该论文针对开放集检测中的测试时适应问题，方法创新且实验充分，对自动驾驶感知的鲁棒性提升有借鉴意义。
- **核心贡献**: 提出了动态EMA和源锚定的测试时适应方法DESA-TTA。
- **创新点**: 基于不确定性动态选择EMA系数并结合源锚定抑制漂移。
- **结果**: 在多种分布偏移下取得一致改进。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-language object detectors (VLODs) achieve strong zero-shot performance but remain vulnerable to distribution shifts during deployment. Mean-teacher methods for test-time adaptation (TTA) can improve robustness by updating a student model using teacher-generated pseudo-labels. However, mean-teacher TTA is highly sensitive to the choice of a fixed exponential moving average (EMA) coefficient for teacher updates, and repeated optimization with noisy pseudo-labels can cause cumulative student drift. We propose Dynamic EMA and Source Anchoring for TTA (DESA-TTA), a low-overhead method that jointly regulates teacher updates and student drift through dynamic temporal averaging and source anchoring. Dynamic temporal averaging estimates teacher uncertainty from pseudo-label confidence and box density and uses it to select a sample-wise EMA coefficient within bounds determined by teacher parameter drift. Source anchoring partially restores the updated student parameters toward their pretrained values, with the anchoring strength increasing according to student drift. Experiments across diverse distribution shifts and two VLOD architectures show consistent improvements over existing TTA methods. On VOC-C, DESA-TTA improves AP$_{50}$ by 14.5 points over zero-shot inference while achieving 55\% higher inference throughput than the previous state-of-the-art TTA method for YOLO-World. Our code: https://github.com/imatif17/DESA-TTA

</details>

### 7. RGB-to-IR image translation for infrared vehicle detection in unseen UAV domains **⭐⭐⭐** (相关度: 60%, 质量: 0.7)

- **arXiv ID**: [2609.02556](https://arxiv.org/abs/2609.02556)  · [📄 PDF](https://arxiv.org/pdf/2609.02556)
- **作者**: Thijs A. Eker, Ella P. Fokkinga, Jan Erik van Woerden et al. (7 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-02 · **分类**: cs.CV
- **摘要（中）**: 针对热红外航空车辆检测中真实数据稀缺、RGB到IR翻译因不可观测热特征而难以学习的问题，本文研究了现代生成式翻译器能否克服跨模态差距以提升未见无人机域的红外车辆检测。在配对RGB-IR源数据集上训练翻译器，并应用于保留目标数据集的RGB训练图像以生成合成IR数据，评估了监督GAN、ControlNet扩散模型和LoRA基础模型编辑等方法。结果显示合成IR数据一致优于RGB和灰度基线，其中Stable Diffusion 3.5 with ControlNet效果最佳，在Kust4K上mAP从50.8提升至60.1，在VTUAV上从25.6提升至38.4。
- **摘要（英）**: This paper investigates whether modern generative translators can overcome the cross-modal gap in RGB-to-IR translation to improve infrared vehicle detection on unseen UAV domains. Training translators on paired RGB-IR source data and applying them to target RGB images, it finds synthetic IR consistently outperforms RGB and grayscale baselines, with Stable Diffusion 3.5 with ControlNet achieving the best results, improving mAP from 50.8 to 60.1 on Kust4K and from 25.6 to 38.4 on VTUAV.
- **评估**: 该论文系统评估了多种生成方法在跨域红外数据增强中的效果，对FOD检测数据稀缺问题有实际参考价值。
- **核心贡献**: 系统评估了RGB到IR翻译方法在未见无人机域红外车辆检测中的有效性。
- **创新点**: 利用现代扩散模型和LoRA编辑生成合成红外数据，提升检测性能。
- **结果**: Stable Diffusion 3.5 with ControlNet在Kust4K和VTUAV上分别提升mAP至60.1和38.4。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Synthetic training data is crucial for developing vision AI when real-world data is scarce, as in thermal infrared (IR) aerial vehicle detection. While abundant UAV RGB imagery motivates RGB-to-IR translation for data augmentation, unobservable thermal traits (e.g., engine heat) make learning transferable mappings challenging. This work investigates whether modern generative translators can overcome this cross-modal gap to improve infrared vehicle detection on unseen UAV target domains. Translators are trained on paired RGB-IR source datasets and applied to RGB training images from held-out target datasets to generate synthetic IR data. Evaluated methods include supervised GANs, ControlNet-based diffusion models, and foundation-model editing via LoRA. The resulting synthetic IR imagery is used to train RF-DETR vehicle detectors, which are evaluated on unseen IR target test splits across five aerial datasets, with Kust4K and VTUAV serving as target domains. Synthetic IR consistently outperforms RGB and grayscale baselines. Stable Diffusion 3.5 with ControlNet yields the best results, improving mAP from 50.8 to 60.1 on Kust4K and from 25.6 to 38.4 on VTUAV compared to models trained only on source-domain IR data. Increasing output diversity via multiple seeds (+1.1 mAP) and prompt variations (+3.3 mAP) provides additional gains on VTUAV. Although a performance gap to real target IR data remains, generative RGB-to-IR translation effectively mitigates IR data scarcity and improves cross-domain aerial vehicle detection.

</details>

### 8. Hardware-Accelerated Instance Segmentation for Resource-Constrained Space Robotics with Criticality Analysis **⭐⭐⭐** (相关度: 70%, 质量: 0.7)

- **arXiv ID**: [2609.02219](https://arxiv.org/abs/2609.02219)  · [📄 PDF](https://arxiv.org/pdf/2609.02219)
- **作者**: Siddhant Shete, Hilmi Dogu Kücüker, Udo Frese et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-02 · **分类**: cs.RO, cs.AR, cs.CV
- **摘要（中）**: ①针对资源受限的月球机器人中，极端低光、有限算力和辐射故障导致实例分割推理不准确的问题。②提出AVIS校准策略和基于YOLO的分割模型在DPU上的部署，并引入软件级关键性分析。③通过激活方差统计选择校准样本，减少CPU回退路径，实现静态编译执行。④在月球微车平台上，AVIS恢复69.8%的量化精度损失，推理延迟309毫秒，功耗5.7瓦。
- **摘要（英）**: This paper addresses real-time instance segmentation under extreme low-light, limited compute, and radiation faults for lunar robotics. It introduces AVIS calibration and a YOLO-based model on DPU with criticality analysis, recovering 69.8% of quantization accuracy loss at 309 ms latency and 5.7 W power.
- **评估**: 面向特定硬件部署的工程优化，对自动驾驶感知的硬件加速有参考价值，但场景差异较大。
- **核心贡献**: 提出联合量化校准和故障分析的部署框架，提升资源受限环境下的分割鲁棒性。
- **创新点**: 基于激活方差的免标签校准和软件级关键性分析。
- **结果**: 恢复69.8%量化精度损失，实现低延迟低功耗推理。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Autonomous lunar missions require real-time per- ception under three coupled constraints: extreme low-light conditions, limited onboard compute, and radiation-induced hardware faults that can silently corrupt inference. We present a deployment-oriented instance segmentation framework for resource-constrained lunar robotics that jointly addresses quan- tization calibration and system-level fault exposure under strict compute constraints. First, we introduce Activation Variance Informative Sampling (AVIS), a label-free calibration strategy that deterministically selects calibration samples based on activation variance statistics. Second, we deploy a YOLO-based segmentation model on a Deep Learning Processor Unit (DPU) with architectural modifications that reduce CPU fallback paths and enable statically compiled execution with bounded latency in low-lighting conditions. We further introduce a software-level criticality analysis to estimate fault exposure and guide mitigation under radiation-constrained operation. On a lunar micro-rover platform, AVIS with bias correction recovers 69.8% of quantization-induced accuracy loss while achieving 309 ms inference latency and 5.7 W power consumption. Targeted mitigation reduces global criticality by 31.7%. The results demonstrate an integrated approach and a blueprint for a reliable and safe AI perception framework under space deployment constraints.

</details>

---

## Vision Transformer

### 1. CoViT: Instance-Correspondence Contrastive Learning for Vision Transformer **⭐⭐⭐⭐** (相关度: 80%, 质量: 0.8)

- **arXiv ID**: [2609.01787](https://arxiv.org/abs/2609.01787)  · [📄 PDF](https://arxiv.org/pdf/2609.01787)
- **作者**: Yisen Wang, Zhirong Wu, Limin Wang
- **🏷️ 机构**: Peking University
- **提交日期**: 2026-09-01 · **分类**: cs.CV
- **摘要（中）**: ①该论文针对Vision Transformer（ViT）在语义理解上表现优异但难以区分对象实例（如两只狗的嵌入相同）的问题，限制了其在实例级任务（如目标检测和实例分割）中的应用。②提出了CoViT，一种自监督学习框架，通过几何引导的对比学习将实例感知注入ViT，利用注意力引导掩码生成实例掩码，并采用最难对比挖掘构建三元组。③相比已有工作，CoViT独特地协调ViT的注意力图和嵌入，通过压缩实例内方差和扩大实例间边界，迫使ViT辨别细微的几何和外观差异。④实验表明，该方法在实例级任务上显著提升ViT的判别能力，但摘要未提供具体数据。
- **摘要（英）**: This paper addresses ViT's failure to discriminate object instances by proposing CoViT, a self-supervised framework using geometry-guided contrastive learning with attention-guided masking and hardest contrastive mining. It coordinates attention maps and embeddings to compress intra-instance variance and expand inter-instance margins, enhancing instance-level discrimination.
- **评估**: 该论文针对ViT实例感知缺陷提出创新自监督方案，对检测和分割任务有潜在价值。
- **核心贡献**: 提出CoViT框架，通过对比学习增强ViT的实例级特征表示。
- **创新点**: 结合注意力引导掩码和最难正负样本挖掘，实现实例感知的对比学习。
- **结果**: 提升ViT在实例级任务中的判别能力，但具体性能数据未在摘要中给出。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision Transformers (ViT) excel in semantic understanding but fail to discriminate between object instances (e.g., identical embeddings for two dogs), limiting their use in instance-level tasks such as object detection and instance segmentation. We propose Contrastive Vision Transformer (CoViT), a self-supervised learning framework that injects instance-awareness into ViT through geometry-guided contrastive learning. CoViT uniquely coordinates ViT's attention maps and embeddings by constructing triplets: (1) Attention-guided masking: Refine multi-head attention via adaptive thresholding and morphological operations to generate instance masks, identifying foreground anchors; (2) Hardest contrastive mining: For each anchor, computing pairwise embedding similarities to select the intra-instance hardest positive (least similar patch within its mask) and inter-instance hardest negative (most similar patch from other instances), with intra-instance regions masked during negative search. These triplets drive a contrastive loss that simultaneously compresses intra-instance variance and expands inter-instance margins, forcing ViT to discern subtle geometric and appearance differences between instances. CoViT consistently achieves stable performance gains of over 2 AP points across multiple instance-level perception tasks by using ViT as backbone architecture. Notably, CoViT requires no extra decoders or labels, demonstrating that a pure ViT can learn instance-aware representations via inherent attention priors and targeted contrastive constraints. Code and models will be released.

</details>

### 2. Swin Meets EfficientNet: Lightweight Architectures for GAN-Based Face Forensics **⭐⭐** (相关度: 40%, 质量: 0.6)

- **arXiv ID**: [2609.01749](https://arxiv.org/abs/2609.01749)  · [📄 PDF](https://arxiv.org/pdf/2609.01749)
- **作者**: Sejuti Basu, Ashima Sood, Vijay Kumar et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-01 · **分类**: cs.CV, cs.AI
- **摘要（中）**: ①该论文针对GAN生成人脸图像的检测问题，现有方法依赖CNN或全局ViT，分别受限于局部纹理或高计算需求。②探索了基于Swin Transformer的三种实现：从头训练的紧凑Swin、ImageNet预训练的Swin-Tiny/Small，以及结合EfficientNet-B0的混合架构。③相比已有工作，该研究旨在平衡局部和全局特征提取，同时降低计算成本。④摘要未提供具体检测精度或效率数据，实验充分性有限。
- **摘要（英）**: This paper investigates lightweight architectures for GAN-based face forensics, comparing Swin Transformer variants and a hybrid with EfficientNet-B0. It aims to balance local and global feature extraction with reduced computation, but lacks reported performance metrics.
- **评估**: 该论文主题常规，方法探索有限，缺乏关键实验结果，关注度较低。
- **核心贡献**: 评估了Swin Transformer和混合架构在深度伪造检测中的适用性。
- **创新点**: 提出Swin与EfficientNet的混合设计以兼顾效率与精度。
- **结果**: 未提供具体效果数据，实用性待验证。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Modern generative models, such as GANs, diffusion architectures, and autoregressive systems, now produce facial images that are nearly indistinguishable from authentic photographs. This capability makes detecting forged images increasingly difficult, raising serious concerns about identity theft, fraud, and misinformation campaigns. Our research focuses specifically on GAN-generated synthetic faces, which underpin many face-centric deepfakes, and investigates efficient detection approaches using image analysis alone. Existing detection systems rely heavily on either convolutional neural networks (CNNs) or global vision transformers. While CNNs excel at identifying texture-based local features, they struggle with broader contextual understanding. Traditional Vision Transformer (ViT) models can capture long-range structures effectively, but demand substantial computational resources. Our work explores Swin-Transformer-based architectures across three implementations: a compact Swin Transformer trained from the ground up, ImageNet-1K pre-trained Swin-Tiny and Swin-Small models adapted for binary classification, and a novel hybrid combining EfficientNet-B0's convolutional processing with a Swin Transformer backend. We evaluated all models using the 140K Real and Fake Faces dataset, which includes StyleGAN-generated fake faces alongside authentic images from Flickr and DFDC, with balanced splits for training, validation, and testing. The EfficientNetB0+Swin hybrid achieved 99% accuracy and a 99.44% recall on 5,000 test images, outperforming both pure Swin variants and a previous CNN-only baseline on this dataset. Our results suggest that combining hierarchical CNN features with shifted-window self-attention provides an efficient and computationally lightweight method for detecting GAN-generated synthetic faces.

</details>

### 3. Source-Free Class Relearning: Diagnosing Forgetting in Class Unlearning **⭐⭐⭐⭐** (相关度: 60%, 质量: 0.8)

- **arXiv ID**: [2609.02018](https://arxiv.org/abs/2609.02018)  · [📄 PDF](https://arxiv.org/pdf/2609.02018)
- **作者**: Zahra Dehghani, Pablo Piantanida, Mohammadhadi Shateri
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-02 · **分类**: cs.LG, cs.CV
- **摘要（中）**: ①针对类遗忘中低遗忘准确率不代表类结构被擦除，现有恢复方法需要真实样本或辅助数据。②研究了严格无源设置下的类重学习，提出白盒无源重学习审计SFRA，基于理论分析建立充分对齐条件，通过合成探针集和模型引导置信过滤生成嵌入。③相比现有方法，仅使用遗忘模型，无需真实样本或参考检查点。④摘要未提供具体实验数据，但理论分析支持单步梯度更新可增加遗忘类期望logit边际。
- **摘要（英）**: This paper investigates class relearning in a source-free setting, proposing SFRA to recover forget classes using only the unlearned model via synthetic probes and confidence filtering. It establishes a theoretical alignment condition for effective recovery. The method avoids reliance on real samples or auxiliary data.
- **评估**: 该论文对类遗忘诊断有理论贡献，与持续学习相关，但对自动驾驶感知的直接应用有限。
- **核心贡献**: 提出了无源类重学习审计方法SFRA。
- **创新点**: 基于理论对齐条件，用合成探针实现类恢复。
- **结果**: 理论上单步更新可增加遗忘类边际，实验数据未详述。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Class unlearning aims to remove a model's ability to recognize designated forget classes while preserving performance on retain classes. However, low forget accuracy after unlearning does not necessarily mean the class structure has been erased. Approximate unlearning methods can alter classifier decision boundaries while leaving recoverable structure in the representation. Prior work has shown that forget classes can be recovered, but existing approaches require real forget or retain samples, auxiliary data, or reference checkpoints. We study class relearning in a strictly source-free setting, asking whether a forget class can be recovered through a classifier-head update using only the unlearned model. Our approach rests on a theoretical analysis establishing a sufficient alignment condition under which a single gradient step on a synthetic probe set increases the expected logit margin of the forget class. Building on this, we propose a white-box Source-Free Relearning Audit (SFRA), which generates candidate embeddings in representation space and uses model-guided confidence filtering to construct high-confidence retain probes and low-confidence boundary-adjacent probes that are relabelled as the forget class. Gaussian sampling and Softmax confidence are used by default, while ablations with alternative proposal distributions and uncertainty criteria show that recoverability is not specific to these choices. To quantify recoverability, we introduce the Relearning Score (RS), which jointly measures forget-class recovery and retain-accuracy preservation, and report class-matched $Δ$RS relative to a retrained reference. Experiments on CIFAR-10, CIFAR-100, and TinyImageNet with ResNet-18, ViT-B/16, and Swin-T show that several unlearning methods exhibit substantial source-free recoverability, and that for a subset of methods this recoverability exceeds the matched retrained reference.

</details>

### 4. LoFi RADIO: A Distilled In-Domain Backbone Applied for Artifact-Severity Grading of Ultra-Low-Field Neonatal Brain MR **⭐⭐** (相关度: 15%, 质量: 0.5)

- **arXiv ID**: [2609.02676](https://arxiv.org/abs/2609.02676)  · [📄 PDF](https://arxiv.org/pdf/2609.02676)
- **作者**: Jonathan B. Martin, Yashwant Kurmi, Charlotte R. Sappo
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-02 · **分类**: eess.IV, cs.CV
- **摘要（中）**: 针对超低场新生儿脑MRI图像中伪影严重度分级问题，现有单一骨干网络在不同伪影上表现不均。论文提出LoFi RADIO，通过蒸馏多个基础模型教师到一个域内ViT-S学生，并评估了按伪影门控路由策略。相比已有工作，蒸馏学生匹配或超越门控策略，且推理时无需部署多个大模型。实验表明，蒸馏策略提升了加权复合指标。
- **摘要（英）**: This paper addresses artifact-severity grading in ultra-low-field neonatal brain MRI, where no single backbone excels across artifacts. It proposes LoFi RADIO, a distilled in-domain ViT-S student from multiple foundation model teachers, compared with per-artifact gating. The distilled backbone matches or exceeds gating while reducing inference cost.
- **评估**: 该论文面向医学影像，与自动驾驶感知领域差异大，但知识蒸馏方法有通用性。
- **核心贡献**: 提出LoFi RADIO蒸馏骨干，用于多伪影严重度分级。
- **创新点**: 通过蒸馏多个教师到单一学生，平衡性能和部署效率。
- **结果**: 蒸馏模型匹配或超越门控策略。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Ultra-low-field MRI makes neonatal brain imaging deploy- able in low-resource settings, but its low SNR, lack of shielding, and long scan duration make it especially prone to acquisition artifacts, motivating automated quality control. We address the LISA 2026 Task 1a challenge: multi-label severity grading (0/1/2) of seven common image artifacts on ULF T2 weighted volumes. We identify that a number of backbones may be successfully paired with a classification MLP, but that no single backbone is uniformly best across artifacts. To improve performance, we evaluate routing complementary foundation model teachers through a per-artifact gate, as well as distilling the teachers into a single in-domain ViT-S student (LoFi RADIO) over an unlabeled low-field MRI corpus. Both of these strategies improve the weighted composite. The distilled backbone matches or exceeds the gate and has the added advantage of not requiring deployment of multiple large foundation models at infer- ence.

</details>

### 5. Aggregating Neighbor Embedding Projection and Rank-Based Manifold Learning for Image Retrieval **⭐⭐** (相关度: 25%, 质量: 0.5)

- **arXiv ID**: [2609.01963](https://arxiv.org/abs/2609.01963)  · [📄 PDF](https://arxiv.org/pdf/2609.01963)
- **作者**: Vinicius Atsushi Sato Kawai, Gustavo Rosseto Leticio, Lucas Pascotti Valem et al. (4 authors)
- **🏷️ 机构**: State University of S&#x00E3;o Paulo (UNESP),Department of Statistics, Applied Mathematics and Computing,Rio Claro,Brazil
- **提交日期**: 2026-09-02 · **分类**: cs.CV · **📚 被引**: 2
- **摘要（中）**: 针对图像检索中高维特征空间下成对距离无法捕捉上下文关系的问题，论文提出结合邻域嵌入投影和基于排序的流形学习框架。该方法利用UMAP生成低维表示，并通过Borda Count聚合来自UMAP投影和重排序方法的排序列表。相比已有工作，该框架结合了投影和排序策略的互补性。实验在多个公开数据集上进行，但摘要未提供具体数据。
- **摘要（英）**: This paper addresses image retrieval challenges in high-dimensional spaces, where pairwise distances fail to capture context. It proposes a framework combining UMAP projections with rank-based manifold learning via Borda Count aggregation. Experiments on public datasets show improved ranking, though specific metrics are omitted.
- **评估**: 该论文聚焦通用图像检索，与自动驾驶目标检测相关性较低，但流形学习思想可迁移。
- **核心贡献**: 提出结合UMAP和排序聚合的图像检索框架。
- **创新点**: 融合投影和排序策略以利用互补信息。
- **结果**: 在公开数据集上提升检索性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Content-based image retrieval (CBIR) has advanced significantly with deep learning, yet effectively ranking similar images remains challenging, particularly in high-dimensional feature spaces, where pairwise distances often fail to capture contextual relationships and the semantic gap between visual features and high-level concepts persists. Manifold learning and rank-based refinement methods have emerged as complementary strategies, respectively improving feature representations and exploiting contextual information embedded in ranked lists, such as neighborhood relationships among images. However, combining these projection-based and rank-based strategies to exploit their complementary properties remains a challenging research problem. To address this, we propose a framework that combines neighbor embedding projections with rank-based manifold learning through rank aggregation. Uniform Manifold Approximation and Projection (UMAP) generates alternative low-dimensional feature representations, and ranked lists obtained from UMAP projections and rank-based re-ranking methods are combined using the Borda Count aggregation strategy. Experiments were conducted on several public datasets using deep learning features extracted from ResNet152, Swin Transformer, and DINOv2 models. Results show that the proposed approach improves retrieval effectiveness in several scenarios, particularly when the baseline representation struggles to achieve high precision. The aggregation strategy also often improves the quality of top-ranked positions, leading to competitive Mean Average Precision (MAP) and Precision values across different datasets and feature extractors. These findings suggest that combining projection-based and rank-based manifold learning strategies through rank aggregation can provide complementary contextual information for image retrieval tasks.

</details>

---

## Multi-camera Perception

### 1. TAPVid-MV: A Benchmark for Tracking Any Point in 3D Across Multiple Views **⭐⭐⭐⭐** (相关度: 75%, 质量: 0.8)

- **arXiv ID**: [2609.01899](https://arxiv.org/abs/2609.01899)  · [📄 PDF](https://arxiv.org/pdf/2609.01899)
- **作者**: Skanda Koppula, Frano Rajic, Abdullah Faiz Ur Rahman et al. (12 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-01 · **分类**: cs.CV
- **摘要（中）**: 针对现有点跟踪基准仅覆盖单视频或静态多相机，缺乏跨多个同步视图的长期3D点跟踪问题，提出了TAPVid-MV基准，包含284个序列、1142个校准相机流和109769个点轨迹，覆盖室内外、驾驶和合成场景。通过传感器深度、LiDAR、SLAM等辅助模态获取轨迹并人工验证。评估30多个基线发现无方法接近解决任务，且多视图跟踪器未一致优于单目跟踪器，揭示了该任务的挑战性。
- **摘要（英）**: This paper introduces TAPVid-MV, the first benchmark for long-term 3D point tracking across multiple synchronized views, with 284 sequences and 109,769 tracks. Evaluation of 30+ baselines shows no method solves the task, and multi-view trackers do not consistently outperform monocular ones, highlighting significant challenges.
- **评估**: 该基准填补了多视图点跟踪的空白，对自动驾驶多相机感知具有重要评估价值，但方法创新有限。
- **核心贡献**: 构建了首个多视图3D点跟踪基准TAPVid-MV并系统评估现有方法。
- **创新点**: 整合多种辅助模态获取跨视图长期轨迹，并人工验证。
- **结果**: 30多个基线均未解决任务，多视图方法未超越单目。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-camera systems are increasingly practical for robotics, AR/VR, and autonomous driving because complementary views reduce depth ambiguity and preserve visibility under occlusion. Existing point-tracking benchmarks, however, focus on a single video or static multi-camera rigs. None test long-term 3D point tracking across several synchronized views under camera motion. We introduce TAPVid-MV (Tracking Any Point in Video across Multiple Views), the first benchmark for this setting. It contains a curated set of 284 sequences, 1,142 calibrated camera streams, and 109,769 point tracks across seven subsets spanning indoor and outdoor domains, from robotics and human activity to driving and synthetic procedural scenes. We obtain these trajectories using dataset-specific auxiliary modalities: sensor depth, LiDAR, SLAM and SfM points, human meshes, posed object meshes, and simulation. Every sequence and trajectory is visually verified by human annotators. Across more than 30 baselines, no method comes close to solving the task. Surprisingly, existing multi-view point trackers do not consistently outperform monocular point trackers. By evaluating reconstruction and point tracking on the same datasets, TAPVid-MV helps distinguish errors in recovered geometry from errors in point correspondence. Through this joint analysis, we identify geometry recovery as a major bottleneck for accurate 3D point tracking. Beyond multi-view 3D point tracking, our released annotations support monocular 2D and 3D point tracking, future-trajectory prediction, and 4D reconstruction.

</details>

### 2. MuyBridge: Mobile Human Center-of-Mass Estimation from Monocular Video via Sparse Fusion **⭐⭐⭐** (相关度: 60%, 质量: 0.7)

- **arXiv ID**: [2609.02854](https://arxiv.org/abs/2609.02854)  · [📄 PDF](https://arxiv.org/pdf/2609.02854)
- **作者**: Aidan Bradshaw, Marco Giordano, David Rode et al. (11 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/Abradshaw1/Muybridge](https://github.com/Abradshaw1/Muybridge)
- **提交日期**: 2026-09-02 · **分类**: cs.CV
- **摘要（中）**: ①针对单目视频中运动员3D质心估计缺乏解剖约束和部署困难的问题。②提出MuyBridge系统，结合紧凑2D姿态网络和蒸馏单步深度网络，通过解析度量融合利用解剖和物理先验。③无需3D或任务特定监督，实现单相机实时估计。④在AthletePose3D上，垂直质心误差33-41毫米，AbsRel 2.3-6.6%，处理速度63 FPS。
- **摘要（英）**: This work estimates 3D center of mass from monocular video using a compact pose network and distilled depth network with analytic fusion. It achieves 33-41 mm vertical error and 2.3-6.6% AbsRel without 3D supervision at 63 FPS.
- **评估**: 对运动分析有应用价值，但与自动驾驶感知核心领域相关性较低。
- **核心贡献**: 提出无监督单目质心估计系统，结合解剖先验。
- **创新点**: 解析度量融合和蒸馏深度网络。
- **结果**: 实现高精度实时质心估计。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The 3D center of mass (CoM) is a primary quantity in the biomechanical analysis of sport, rehabilitation, and clinical movement, yet existing 3D pose tracking, mesh recovery, and multi-view triangulation methods either optimize 3D keypoint accuracy without anatomical constraints or carry compute and capture infrastructure too heavy to deploy where CoM tracking is most useful. As a result, the metric CoM remains difficult for coaches and movement analysts to measure from a single camera where athletes train and compete. In this work, we introduce MuyBridge, an on-device system that estimates the athlete's segmental center of mass trajectory from a single phone camera video stream. MuyBridge couples a compact 2D pose network and a distilled single-step monocular depth network through an analytic metric fusion that uses anatomical and physical priors to anchor the metric CoM, requiring no 3D or task-specific supervision. Evaluated on the athletic movements of AthletePose3D (running, track and field, and figure skating), MuyBridge achieves 33-41 mm vertical CoM error and 2.3-6.6% absolute-relative range error (AbsRel) under a one-time calibration, and produces CoM estimates at the 63 FPS pose-estimation rate using asynchronous 2.86 Hz depth updates on iPhone 15. Code is available at: https://github.com/Abradshaw1/Muybridge

</details>

### 3. InceptionGS: Generative Bootstrapping for Large-Scale Gaussian Splatting under Unstructured View Sampling **⭐⭐⭐⭐** (相关度: 75%, 质量: 0.8)

- **arXiv ID**: [2609.02747](https://arxiv.org/abs/2609.02747)  · [📄 PDF](https://arxiv.org/pdf/2609.02747)
- **作者**: Tianheng Lu, Guangyu Wang, Ruqi Huang et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-02 · **分类**: cs.CV
- **摘要（中）**: ①针对大规模场景重建中非结构化视图采样导致部分区域观测不足的问题。②提出InceptionGS，通过生成式引导平衡重建和生成，修复视图稀缺区域并保持其他区域质量。③软性整合场景和视图自适应生成先验，提升3D一致性和可控性。④在真实大规模场景上验证了优越性和广泛适用性。
- **摘要（英）**: This paper addresses view scarcity in large-scale Gaussian splatting by bootstrapping with generative priors. InceptionGS balances reconstruction and generation, repairing under-observed regions while preserving quality, showing superiority on real scenes.
- **评估**: 对3D场景重建和自动驾驶高精地图生成有潜在价值，方法新颖。
- **核心贡献**: 提出生成引导的Gaussian Splatting方法处理非结构化视图。
- **创新点**: 软性整合生成先验平衡重建与生成。
- **结果**: 在大规模场景中优于现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Achieving truly immersive large-scale scene digitization necessitates consistent and visually pleasing rendering across all possible viewing perspectives. However, collecting multi-view images covering every fine detail of a large-scale scene is prohibitive due to scene complexity, capture cost, negligence, or accessibility constraints. As a result, the sampled views tend to be highly unstructured -- the majority of the scene is well covered yet certain regions inevitably lack sufficient observations. Existing reconstruction based methods are vulnerable to view scarcity while generation based approaches suffer from generalization, controllability, and 3D consistency issues. To address this challenge, we propose InceptionGS, which bootstraps Gaussian splatting by subtly balancing reconstruction and generation. Starting from an initial Gaussian splatting, InceptionGS reasonably rethinks and repairs problematic regions caused by view scarcity while preserving the quality elsewhere, by softly incorporating scene- and view-adaptive generative priors. Extensive experiments on real-world large-scale scenes demonstrate the superiority and broad applicability of our approach in handling unstructured imagery and boosting high-fidelity Gaussian splatting. Please refer to the supplementary video for better visual demonstrations.

</details>

### 4. Adapting a Foundation Model for Lunar Surface Height Estimation **⭐⭐⭐** (相关度: 65%, 质量: 0.6)

- **arXiv ID**: [2609.02448](https://arxiv.org/abs/2609.02448)  · [📄 PDF](https://arxiv.org/pdf/2609.02448)
- **作者**: Patrick Bauer, Marius Schwinning, Melanie Siegel et al. (5 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-02 · **分类**: cs.CV
- **摘要（中）**: ①针对月球表面高度估计中传统方法依赖2D图像和深度学习缺乏适应性的问题。②基于Depth Anything V2微调，开发相对高度估计器用于危险地形检测。③利用基础模型的零样本能力，适应月球表面特征。④摘要未提供具体性能数据，但强调对ESA月球任务的适用性。
- **摘要（英）**: This paper adapts Depth Anything V2 for lunar surface height estimation, providing relative elevation for hazard detection. It leverages foundation model zero-shot capabilities, targeting ESA lunar missions, though no quantitative results are given.
- **评估**: 基础模型适应特定场景，对自动驾驶中的非结构化地形感知有参考，但实验不充分。
- **核心贡献**: 将DAV2适配于月球高度估计。
- **创新点**: 利用基础模型零样本能力进行领域适应。
- **结果**: 未提供具体效果数据。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Digital elevation models (DEMs) can provide accurate height information, making it invaluable for analyzing the lunar surface. As the European Space Agency (ESA) prepares for future lunar missions that aim to land on the Moon, a precise method for height estimation will be essential for hazardous terrain that could endanger the landing approach. Traditional approaches to generate DEMs from imagery, such as shape from shading (SfS) and stereophotogrammetry (SPG) have been proven highly valuable for this task. However, due to advancements in machine learning, especially computer vision, the focus has shifted towards monocular depth estimation via deep learning. The lunar surface is covered by rocks and craters, and classic hazard detection methods rely solely on 2D image data. Our goal is to address this issue by developing a relative lunar surface height estimator that can provide additional information for hazard localization. In this letter, we present a methodology that builds on the well-known zero-shot relative depth estimation model Depth Anything V2 (DAV2). Other works have been using it as a state-of-the-art comparison for their proposed lunar DEM estimation method, but without adaptations to the target domain. Thus, it may underperform. Therefore, we propose a fine-tuning strategy with publicly available SPG-derived DEM data of the lunar surface. Our results demonstrate a significant improvement in performance compared to the zero-shot model, effectively transforming DAV2 into a reliable relative depth estimator of the lunar surface.

</details>

### 5. Cross-Model Distillation of a Human-Pose Foundation Model from Unannotated Infant Video for Markerless 3D Pose Estimation **⭐⭐⭐⭐** (相关度: 80%, 质量: 0.8)

- **arXiv ID**: [2609.01840](https://arxiv.org/abs/2609.01840)  · [📄 PDF](https://arxiv.org/pdf/2609.01840)
- **作者**: R. James Cotton, Divya Joshi, Colleen Peyton
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-01 · **分类**: cs.CV
- **摘要（中）**: ①针对婴儿无标记3D姿态估计中基础模型在成人数据上训练、跨模型性能权衡的问题。②执行从Sapiens 2到SAM 3D Body的跨模型蒸馏，使用未标注婴儿视频，教师提供伪标签，可微渲染器对齐网格。③改进点在于无需标注数据，解决2D精度和3D恢复的权衡。④在11个婴儿、18个会话、173个记录上，微调提升同视角2D关键点一致性，但具体数值未完整给出。
- **摘要（英）**: This paper performs cross-model distillation from Sapiens 2 to SAM 3D Body using unannotated infant video, with frozen teacher pseudo-labels and differentiable rendering. Fine-tuning improves 2D keypoint agreement on held-out infants, addressing the trade-off between 2D and 3D accuracy.
- **评估**: 跨模型蒸馏在无标注视频上的应用具有创新性，对自动驾驶中行人姿态估计有借鉴。
- **核心贡献**: 提出无标注婴儿视频的跨模型蒸馏框架。
- **创新点**: 利用可微渲染器对齐伪标签。
- **结果**: 提升2D关键点一致性，具体数值未完整。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Spontaneous movement is one of the earliest windows onto an infant's neuromotor health, and structured clinical instruments that score it are validated early predictors of cerebral-palsy risk. However, they require specially trained raters, are time-consuming, and carry inter-rater variability. This motivates automated, video-based markerless assessment, especially as marker-based motion capture is impractical in infants. Yet the foundation models that make markerless capture possible are trained almost entirely on adults: our recent multi-view infant study found that no single model is jointly best, with strong 2D keypoint accuracy and direct 3D body recovery split across different models. While that study identifies this trade-off, it does not resolve it. Here, we perform cross-model distillation from the Sapiens 2 pose model into the SAM 3D Body model, using unannotated infant video alone. A frozen teacher supplies dense pseudo-labels, and a differentiable renderer aligns the predicted mesh to them in the training loop. On eleven held-out infants (18 sessions, 173 recordings) under our prior study's multi-view protocol, fine-tuning improves same-view 2D keypoint agreement with the Sapiens reference (median body percentage of correct keypoints @ 10px 0.22 -> 0.42, face 0.22 -> 0.42) and Procrustes-aligned mean per joint 3D position error (25.5 -> 22.2 mm). This demonstrates how cross-model distillation improves SAM 3D Body model performance on infants.

</details>

---

## Self-supervised Vision

### 1. Physics-Driven Independent Pair Generation for Iterative Self-Supervised Low-Dose CT Denoising **⭐⭐** (相关度: 20%, 质量: 0.6)

- **arXiv ID**: [2609.02654](https://arxiv.org/abs/2609.02654)  · [📄 PDF](https://arxiv.org/pdf/2609.02654)
- **作者**: Xianlei Han, Shaoyu Wang, Jiancheng Fang et al. (5 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-01 · **分类**: cs.CV
- **摘要（中）**: 针对低剂量CT去噪中自监督方法未显式建模混合泊松-高斯噪声的问题，提出物理驱动的跨域迭代自监督框架。该方法利用学习到的正弦图先验和噪声模型推断光子计数，分离泊松和高斯分量；通过二项和高斯数据细化构造训练对，并用残差缩放匹配噪声水平；最后在图像域训练网络并前向投影更新先验。相比通用自监督方法，该方法显式建模噪声物理过程，提升去噪效果。
- **摘要（英）**: To address the lack of explicit noise modeling in self-supervised LDCT denoising, this paper proposes a physics-driven cross-domain iterative framework that separates Poisson and Gaussian components and constructs training pairs via data thinning. The prior and training pairs are progressively refined through cross-domain iteration. Experiments show improved denoising performance over generic self-supervised methods.
- **评估**: 该论文针对医学影像领域，与自动驾驶感知方向相关性低，但物理驱动自监督思路有一定参考价值。
- **核心贡献**: 提出物理驱动的跨域迭代自监督LDCT去噪框架，显式建模混合噪声。
- **创新点**: 利用泊松-高斯分离和数据细化构造独立噪声训练对。
- **结果**: 在低剂量CT去噪中取得优于通用自监督方法的效果。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Low-dose computed tomography (LDCT) measurements contain mixed Poisson-Gaussian noise. However, most self-supervised methods rely on generic image statistics and do not explicitly model this noise, which may limit their ability to effectively suppress realistic LDCT noise. To address this issue, we propose a physics-driven framework with cross-domain iteration for self-supervised LDCT denoising. The proposed framework proceeds in three main steps. First, a learned sinogram prior and the LDCT noise model guide posterior inference of photon counts, enabling separation of the Poisson and Gaussian components. Second, the separated Poisson and Gaussian components are respectively processed by binomial thinning and Gaussian data thinning to construct two branches, and residual scaling matches each branch's noise level to that of the observation, yielding a training pair with approximately independent noise realizations from one low-dose measurement. Finally, the pair is used to train an image-domain network whose forward-projected outputs update the prior. Through cross-domain iteration, the prior and the training pair are progressively refined while maintaining consistency with CT acquisition physics. Experiments on simulated data from AAPM, LIDC-IDRI, and LoDoPaB-CT and on real LDCT data show consistent gains over the evaluated self-supervised baselines across dose levels, with performance comparable to the evaluated supervised baseline.

</details>

### 2. ProSR: Semantic-Prototype-Guided Discrete Modeling for Physically Consistent SAR Super-Resolution **⭐⭐⭐** (相关度: 20%, 质量: 0.7)

- **arXiv ID**: [2609.02377](https://arxiv.org/abs/2609.02377)  · [📄 PDF](https://arxiv.org/pdf/2609.02377)
- **作者**: Byoungwoo Kim, Munchurl Kim
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-02 · **分类**: cs.CV
- **摘要（中）**: ①针对SAR图像超分辨率中扩散模型难以保持散射统计一致性，导致结构失真。②提出了ProSR框架，将SAR超分辨率重构为语义引导的离散令牌预测任务，在量化潜在空间中映射散射基元，并集成自监督学习骨干提取无标签语义先验。③相比平滑近似方法，通过语义对齐细节编码和原型图引导注意力保留SAR脉冲特性。④摘要未提供具体数据，但强调物理一致性和标签稀缺性克服。
- **摘要（英）**: This paper addresses physical inconsistency in SAR super-resolution by proposing ProSR, which reformulates the task as semantic-guided discrete token prediction in a quantized latent space. It integrates self-supervised learning to extract semantic priors without labels. The method preserves impulsive scattering characteristics and overcomes label scarcity.
- **评估**: 该论文针对SAR图像处理有特定应用价值，但与自动驾驶感知方向相关性较低。
- **核心贡献**: 提出了语义原型引导的SAR超分辨率框架ProSR。
- **创新点**: 用离散令牌预测和自监督先验保持散射物理一致性。
- **结果**: 摘要未提供具体性能数据。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> High-resolution Synthetic Aperture Radar (SAR) imagery is critical for precision analysis such as automatic target recognition, yet its acquisition is costly. Although generative image super-resolution (ISR) models offer a promising alternative, current smooth-approximation based diffusion frameworks often struggle to preserve the coherent scattering statistics, causing stochastic structural distortions that are less consistent with real SAR physics. To address this, we propose Semantic Prototype-Guided Super-Resolution (ProSR), reformulating SAR ISR as a semantically-guided discrete token prediction task within a quantized latent space. By mapping signal features to discrete scattering primitives, ProSR preserves the impulsive nature of SAR without over-smoothing. Furthermore, we integrate a Self-Supervised Learning backbone into SAR ISR to extract label-free semantic priors, overcoming label scarcity. Guided by these priors, we introduce Semantic-Aligned Detail Encoding to decouple high-frequency signals into discrete scattering primitives. In parallel, the Semantic Prototype Map Generator explicitly constructs semantic prototype maps, allowing Prototype-Map-Guided Attention to route the information flows within identical categories and mitigate inter-class interference. To validate our approach, we present a large-scale 0.25m resolution benchmark from the Umbra Open Dataset. Experimental results show ProSR achieves superior visual quality while preserving essential scattering characteristics required for practical SAR applications.

</details>

### 3. The Missing Temporal Link: Temporal Context Routing for Script-Driven Audio-Video Generation **⭐⭐** (相关度: 10%, 质量: 0.5)

- **arXiv ID**: [2609.02367](https://arxiv.org/abs/2609.02367)  · [📄 PDF](https://arxiv.org/pdf/2609.02367)
- **作者**: Yichen Liu, Quanwei Zhang, Haozhe Wang et al. (10 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-02 · **分类**: cs.MM, cs.CV
- **摘要（中）**: 针对脚本驱动的音视频生成中，镜头切换和对话时间难以精确控制的问题，现有生成模型仅对齐音视频时间轴，忽略脚本时间线。论文提出时间上下文路由（TCR），将脚本时间映射到共享时间轴，并路由每个提示到对应模态位置。相比基线，TCR在200个测试脚本上减少了镜头边界误差，但摘要未提供具体数值。
- **摘要（英）**: This paper addresses timing control in script-driven audio-video generation, where shots and dialogue deviate from script timelines. It proposes Temporal Context Routing (TCR) to map script timing onto the shared temporal axis and route guidance to both modalities. TCR reduces shot boundary errors on 200 test scripts.
- **评估**: 该论文涉及音视频生成，与自动驾驶感知领域无关，但时间对齐思想有启发。
- **核心贡献**: 提出TCR方法，实现脚本时间与音视频生成的精确对齐。
- **创新点**: 将结构化脚本时间纳入生成模型的时序对齐。
- **结果**: 减少镜头边界误差。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Joint audio-video generation models have made substantial progress in visual quality and audio-visual synchronization. However, they still provide limited control over when shot transitions occur and dialogue is spoken. This limitation constrains their application in script-driven content creation, where timing errors can undermine narrative coherence and the viewing experience. Current joint generators align video and audio representations on a shared temporal axis, yet the precise timing of shots and dialogue specified in a structured prompt is encoded only in the prompt's text representation and remains unaligned with the temporal coordinates of either modality. Consequently, video and audio may remain synchronized with each other while both fail to follow the script timeline. This mismatch motivates us to extend temporal alignment beyond video and audio to include the structured script. We therefore introduce Temporal Context Routing (TCR), which maps the script timing onto the shared temporal axis of video and audio generation and routes each prompt's guidance to the corresponding positions in both modalities. Compared with the baseline on 200 test scripts, TCR reduces Shot Boundary MAE by 96%, from 1.11 s to 0.042 s, and raises Dialogue Acc@0.5 s from 28.3% to 84.1%. TCR achieves these improvements while maintaining visual quality and audio-visual synchronization comparable to those of the baselines. A user study further shows that participants prefer TCR on all five evaluated dimensions.

</details>

### 4. Structured-Prior-Guided Diffusion Inpainting with Physical Consistency for Traffic Sign Augmentation **⭐⭐⭐⭐** (相关度: 80%, 质量: 0.7)

- **arXiv ID**: [2609.02348](https://arxiv.org/abs/2609.02348)  · [📄 PDF](https://arxiv.org/pdf/2609.02348)
- **作者**: Luo Li, Chongchong Huang, Jun Jia et al. (7 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/52hz-whale/TrafficSignInpaint](https://github.com/52hz-whale/TrafficSignInpaint)
- **提交日期**: 2026-09-02 · **分类**: cs.CV
- **摘要（中）**: 针对交通标志检测中长尾分布导致稀有标志样本不足的问题，通用修复模型会扭曲数字、几何和颜色。论文提出结构化先验引导的扩散修复框架，通过三个正交路径注入语义、外观和几何先验：JSON文本提示、带主色渲染的前视向量模板（IP-Adapter）和仿射对齐向量模板（ControlNet），并用CIELAB色度和Sobel梯度损失约束物理一致性。相比已有工作，该方法在自监督重建训练后，零样本迁移到TT100K-2021数据集，使用Stable Diffusion 1.5骨干，但摘要未提供具体性能数据。
- **摘要（英）**: This paper addresses long-tailed traffic sign detection by proposing a structured-prior-guided diffusion inpainting framework with physical consistency. It injects semantic, appearance, and geometric priors via text, IP-Adapter, and ControlNet, with CIELAB and Sobel losses. Trained self-supervised on in-house data, it generalizes zero-shot to TT100K-2021, though specific metrics are not reported.
- **评估**: 该论文直接面向自动驾驶交通标志检测的数据增强，方法创新且实用，值得关注。
- **核心贡献**: 提出结构化先验引导的扩散修复框架，用于交通标志数据增强。
- **创新点**: 通过多路径先验注入和物理一致性损失，解决通用修复模型的失真问题。
- **结果**: 零样本迁移到TT100K-2021，但未报告具体指标。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Traffic sign detection faces a long-tailed data distribution. Many rare signs matter as much as common ones from a regulatory standpoint, yet they have very few samples. Generative data augmentation is one way out. General-purpose inpainting models, however, distort digits, deform geometry and perspective, and shift colours when applied directly to sign regions. We trace this to a single gap: the conditioning signal is too abstract for the physical composition of a sign. We propose a structured-prior-guided diffusion inpainting framework with physical consistency. It injects the semantic, appearance and geometric priors of a sign through three orthogonal pathways: a JSON-formatted text prompt, a front-view vector template rendered with measured dominant colours (via IP-Adapter), and an affine-aligned vector template (via ControlNet). Two physical consistency losses constrain colour with a CIELAB chromaticity $L_1$ term and edge structure with a Sobel gradient term. We train by self-supervised reconstruction on a large set of images collected in-house at AMAP, then evaluate zero-shot on the public TT100K-2021 dataset, a different source. Our method uses a Stable Diffusion 1.5 backbone of about 1.4B parameters. It beats seven representative competitors on every metric of reconstruction fidelity, physical consistency and semantic controllability. Its OCR exact-match rate reaches 91.1\%, against 44.2\% for the 12B industrial model FLUX.1 Fill [dev], and it needs only $1/14$ of that model's inference time. Leave-one-out ablations confirm that each of the three prior pathways and both loss terms contribute on their own. In downstream detection, the synthetic data raises the group-pooled AP50 of rare classes by $1.23\times$ to $7.40\times$ over a real-data-only baseline. Code and pre-trained models are available at https://github.com/52hz-whale/TrafficSignInpaint.

</details>

### 5. Automated Maize Ear Phenotyping Using 3D Reconstructions **⭐⭐** (相关度: 30%, 质量: 0.6)

- **arXiv ID**: [2609.01921](https://arxiv.org/abs/2609.01921)  · [📄 PDF](https://arxiv.org/pdf/2609.01921)
- **作者**: Ritwesh A. Kumar, Som Tripathi, Peja Matthews et al. (8 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-01 · **分类**: cs.CV
- **摘要（中）**: ①针对玉米育种中人工测量穗部性状效率低的问题，提出自动化表型提取流程。②利用视频转点云平台，经COLMAP和NeRF重建，通过密度分离和PCA对齐，柱面展开成2D图像，再用Cellpose-SAM进行零微调实例分割。③采用三重拼接展开策略避免接缝处重复计数，并实现距离校准。④在168穗测试集上，籽粒计数R²=0.921（MAPE=10.33%），穗行数95.2%误差在±2行内（MAE=0.75行）。
- **摘要（英）**: This paper addresses the bottleneck of manual maize ear phenotyping by proposing a fully automated pipeline that reconstructs 3D point clouds from videos and extracts kernel traits via cylindrical unwrapping and Cellpose-SAM segmentation. The method achieves high accuracy on a held-out set, with kernel count R²=0.921 and row number MAE=0.75, demonstrating practical utility for breeding programs.
- **评估**: 该论文面向农业应用，方法工程性强，但与自动驾驶感知领域相关性较低，创新性有限。
- **核心贡献**: 提出了一种基于3D重建和实例分割的玉米穗表型自动化提取流程。
- **创新点**: 利用三重拼接展开策略和零微调分割模型解决点云展开中的计数问题。
- **结果**: 在168穗测试集上实现高精度籽粒计数和穗行数估计。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Maize kernel traits such as row number, kernels per row, and kernel size vary largely for genetic reasons and are consistently associated with regions of the genome that influence yield. Manual measurement of these traits, however, cannot keep pace with the volume of maize generated in a breeding program. To address this, we developed and validated a fully automated pipeline for extracting these traits from 3D point clouds of corn ears, built on a recently developed video-to-point-cloud platform. Raw video frames are processed through COLMAP and NeRF, the ear is isolated via density-based separation, and the point cloud is distance-calibrated to physical units. The calibrated ear point cloud was Z-axis aligned via PCA and cylindrically unwrapped to a 2D image. We enhanced contrast and performed zero-fine-tuning instance segmentation using Cellpose-SAM. A triple-juxtaposed unwrap strategy was used to prevent double-counting at the seam. The pipeline achieved kernel count R^2 = 0.921 (MAPE = 10.33%) and kernel row number within +-2 rows for 95.2% of ears (MAE = 0.75 rows) on a 168-ear held-out set from the 268-ear labeled dataset. The resulting multi-trait dataset has known genotype identity for each ear, positioning it for phenotype-to-genotype association analyses.

</details>

---

## Video Understanding

### 1. ShallowStream: Index Shallow then Answer Deep for Streaming Video Understanding **⭐⭐⭐⭐** (相关度: 75%, 质量: 0.8)

- **arXiv ID**: [2609.02780](https://arxiv.org/abs/2609.02780)  · [📄 PDF](https://arxiv.org/pdf/2609.02780)
- **作者**: Jitai Hao, Ke Yang, Qiang Huang et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/CURRENTF/ShallowStream](https://github.com/CURRENTF/ShallowStream)
- **提交日期**: 2026-09-02 · **分类**: cs.CV, cs.CL
- **摘要（中）**: 针对流式视频理解中多模态大模型（MLLM）全深度预填充计算开销大、KV缓存随深度线性增长的问题，提出ShallowStream框架。该方法利用MLLM的浅层同时进行帧编码和检索索引构建，在流处理时维护基于浅层KV缓存的轻量索引，查询时利用浅层注意力分数进行深度回答。相比现有视觉token剪枝、合并、量化等方法，首次从模型深度维度降低流式处理开销。实验表明该方法在保持性能的同时显著减少计算量和KV缓存增长。
- **摘要（英）**: To address the prohibitive computational cost and linearly growing KV cache in streaming video understanding with MLLMs, this paper proposes ShallowStream, which leverages shallow layers for simultaneous frame encoding and retrieval index building. It maintains an always-on lightweight index during streaming and uses shallow-layer attention scores for query-time answering, reducing overhead from the model-depth dimension. Experiments show significant computational savings and reduced KV cache growth while maintaining performance.
- **评估**: 该论文从模型深度维度创新性地解决流式视频理解的计算瓶颈，对自动驾驶等实时感知场景具有潜在应用价值。
- **核心贡献**: 提出首个利用MLLM浅层进行索引构建和深度回答的流式视频理解框架。
- **创新点**: 将模型深度作为优化维度，利用浅层KV缓存实现轻量索引和高效查询。
- **结果**: 在保持性能的同时显著降低计算开销和KV缓存增长。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Streaming video understanding is a critical capability for real-world applications, including embodied intelligence, autonomous driving, industrial monitoring, surveillance and early warning, and wearable assistants. However, processing continuous video streams with multimodal large language models (MLLMs) is computationally expensive. Existing efforts have explored reducing streaming overhead through visual token pruning, token merging, quantization, on-demand frame retrieval, and context offloading. However, most existing methods overlook the dimension of model depth. Repeatedly executing full-depth MLLM prefill over incoming frames is prohibitively expensive, incurring substantial computational overhead and causing the KV cache to grow at a rate directly proportional to the prefill depth. To address these challenges, we propose ShallowStream, a novel framework that leverages the shallow layers of an MLLM to simultaneously perform frame encoding and retrieval index building. During stream processing, ShallowStream maintains an always-on lightweight index using the KV cache of shallow layers. During query-time answering, we leverage the attention scores generated by the shallow layers to score context frames and employ a diversity-aware selection strategy to retrieve precise and comprehensive evidence. ShallowStream achieves performance on par with the strongest existing streaming methods, while reducing per-frame prefill latency and 10-second end-to-end latency by up to 52.1x and 11.9x, respectively. Our code is available at https://github.com/CURRENTF/ShallowStream.

</details>

### 2. TAME: Temporal-Aware Mixture-of-Experts for Text-Video Retrieval **⭐⭐⭐** (相关度: 60%, 质量: 0.7)

- **arXiv ID**: [2609.02204](https://arxiv.org/abs/2609.02204)  · [📄 PDF](https://arxiv.org/pdf/2609.02204)
- **作者**: Uicheol Jung, Juyoung Hong, Hojung Kwon et al. (4 authors)
- **🏷️ 机构**: Sejong University, Gwangjin-gu, Seoul, Republic of Korea, Wisenut, Bundang-gu, Seongnam-si, Gyeonggi-do, Republic of Korea
- **💻 代码**: [github.com/sejong-rcv/TAME](https://github.com/sejong-rcv/TAME)
- **提交日期**: 2026-09-02 · **分类**: cs.CV · **📚 被引**: 1
- **摘要（中）**: 针对文本-视频检索中CLIP模型缺乏时间建模、将所有帧压缩为单一表示会模糊时间结构的问题，提出TAME框架。该方法在CLIP双编码器中集成稀疏专家混合层，并在视觉分支采用帧一致路由使专家按帧级视觉模式特化；引入帧-时间令牌聚合全局跨帧信息并反馈至每帧；设计跨时间交互聚合模块细化帧级句子-视频相似度。相比现有方法，TAME同时建模帧级结构和时间关系，提升检索性能。
- **摘要（英）**: To address the lack of temporal modeling in CLIP-based text-video retrieval, this paper proposes TAME, integrating sparse Mixture-of-Experts layers with frame-consistent routing and Frame-Temporal tokens to capture long-range dependencies. A Cross-Temporal Interaction and Aggregation module refines frame-wise similarities. Experiments demonstrate improved retrieval performance over existing methods.
- **评估**: 该论文在视频检索中引入MoE和时间令牌，方法设计合理，但对自动驾驶核心任务相关性一般。
- **核心贡献**: 提出结合稀疏MoE和帧-时间令牌的CLIP框架，增强文本-视频检索的时间建模能力。
- **创新点**: 帧一致路由和帧-时间令牌机制实现局部细节与全局时间依赖的联合建模。
- **结果**: 在文本-视频检索基准上取得性能提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Text-Video Retrieval (TVR) retrieves videos that match a natural-language query, but extending image-text models such as CLIP to videos is fundamentally limited by the lack of temporal modeling. Videos exhibit frame-wise heterogeneity in appearance and motion, and compressing all frames into a single representation often obscures temporal structure and semantic transitions. To address this, we propose Temporal-Aware Mixture-of-Experts for Text-Video Retrieval (TAME), a CLIP-based framework that jointly models frame-level structure and temporal relations. First, we integrate sparse Mixture-of-Experts (MoE) layers into both CLIP encoders and apply frame-consistent routing on the vision branch so that experts specialize according to frame-level visual patterns while preserving the original vision-language alignment. Second, we introduce Frame-Temporal (FT) tokens that aggregate global cross-frame information and feed it back to each frame, enabling the visual encoder to capture long-range temporal dependencies without harming local details. Third, we design a Cross-Temporal Interaction and Aggregation (CTIA) module that refines frame-wise sentence-video similarities through staged temporal filtering and fusion. Experiments on standard TVR benchmarks show that TAME consistently improves over CLIP-based baselines. On MSR-VTT, it improves R@1 by 4.0 over CLIP4Clip, and also achieves consistent gains on DiDeMo, MSVD, LSMDC, and ActivityNet. The code is available at https://github.com/sejong-rcv/TAME.

</details>

### 3. Doppio: A Dataset for Contactless Weight Estimation of Falling Particles **⭐⭐** (相关度: 20%, 质量: 0.5)

- **arXiv ID**: [2609.02528](https://arxiv.org/abs/2609.02528)  · [📄 PDF](https://arxiv.org/pdf/2609.02528)
- **作者**: Simon Kiefhaber, Jan-Martin O. Steitz, Julia Grabinski et al. (8 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-02 · **分类**: cs.CV
- **摘要（中）**: 针对工业应用中粉末（如咖啡粉）下落颗粒的无接触质量测量问题，现有方案昂贵且复杂。论文提出了Doppio视频数据集，包含下落咖啡粉的视频和逐帧精确重量标注，并评估了从纯空间前馈网络到循环时空模型的深度学习方法。相比已有工作，该方法利用计算机视觉作为低成本替代方案。实验表明，深度学习模型能准确估计下落颗粒的累积重量，为未来视觉无接触测量奠定基础。
- **摘要（英）**: This paper addresses contactless mass estimation of falling particles in industrial settings, where existing solutions are costly and complex. It introduces Doppio, a video dataset of falling ground coffee with per-frame weight labels, and evaluates deep learning models from spatial to spatio-temporal architectures. Results show accurate cumulative weight estimation, establishing a foundation for vision-based measurement.
- **评估**: 该论文数据集和任务较为小众，与自动驾驶感知领域相关性低，但方法探索有一定参考价值。
- **核心贡献**: 提出了Doppio数据集和视觉无接触质量估计的基线评估。
- **创新点**: 将计算机视觉应用于下落颗粒质量估计，并构建了专用数据集。
- **结果**: 深度学习模型能准确估计累积重量。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Measuring the mass of powder, including falling particles, is a common task in industrial applications. While scales are effective for static measurements, many applications require contactless sensing, where existing solutions are often costly, application-specific, and technically complex. In this work, we investigate computer vision as a practical alternative for contactless mass estimation. As an accessible real-world case study, we focus on coffee grinding and introduce \emph{Doppio}, a novel video dataset capturing videos of falling ground coffee, paired with precise, per-frame ground-truth weight measurements. To demonstrate contactless measuring, we evaluate deep learning-based approaches ranging from purely spatial feed-forward networks to recurrent spatio-temporal models. These models are analyzed with respect to their predictive accuracy and computational trade-offs. We demonstrate that deep learning-based computer vision models accurately estimate the cumulative weight of falling particles, establishing a solid foundation for future vision-based contactless measurement solutions.

</details>

### 4. Allocate Before You Embed: Adaptive Visual Input Allocation for Video Embeddings **⭐⭐⭐** (相关度: 30%, 质量: 0.6)

- **arXiv ID**: [2609.01778](https://arxiv.org/abs/2609.01778)  · [📄 PDF](https://arxiv.org/pdf/2609.01778)
- **作者**: Song Jin, Zhongtao Jiang, Chenglei Shen et al. (8 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/jinsong8/AllocEmbed](https://github.com/jinsong8/AllocEmbed)
- **提交日期**: 2026-09-01 · **分类**: cs.CV
- **摘要（中）**: 针对大规模视频检索中嵌入模型在固定视觉输入和推理预算下，现有方法采样固定帧数且忽略帧重要性，导致时间覆盖不足的问题。论文提出AllocEmbed框架，在嵌入前通过轻量分配器将固定视觉预算重新分配到更多帧，并利用低成本预览分配帧级分辨率。相比已有工作，该方法通过检索驱动的策略优化（RDPO）直接学习分配器，提升时间覆盖和空间保真度的互补性。实验表明，扩大时间覆盖能提升检索性能，尤其在保留原始分辨率时增益更大。
- **摘要（英）**: This paper tackles video retrieval under tight visual-input budgets, where fixed frame sampling limits temporal coverage. It proposes AllocEmbed, an allocate-then-embed framework that reallocates budgets across more frames using a lightweight allocator, trained via Retrieval-Driven Policy Optimization. Results show improved retrieval with expanded temporal coverage, especially when preserving spatial fidelity.
- **评估**: 该论文聚焦视频检索，与自动驾驶多相机感知关联有限，但预算分配思想可借鉴。
- **核心贡献**: 提出AllocEmbed框架和RDPO优化策略，用于视频嵌入的视觉输入分配。
- **创新点**: 在嵌入前动态分配帧级分辨率，并利用检索反馈学习分配策略。
- **结果**: 在固定预算下提升视频检索性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large-scale video retrieval requires embedding models to encode long and diverse videos under tight visual-input and inference budgets. Existing methods typically sample a small, fixed set of frames at their original resolution, limiting temporal coverage and ignoring frame importance. Our empirical analysis shows that expanding temporal coverage improves retrieval even under a fixed visual-input budget. Gains are larger when the original per-frame resolution is preserved, highlighting the complementary roles of temporal coverage and spatial fidelity. Motivated by this finding, we propose AllocEmbed, an allocate-then-embed framework that reallocates a fixed visual-input budget across more frames. A lightweight allocator uses low-cost previews to assign frame-wise resolutions before the embedding backbone, preserving more detail where it most benefits retrieval while reducing visual cost elsewhere. We further introduce Retrieval-Driven Policy Optimization (RDPO), which learns the allocator directly from retrieval feedback using a rank-validated similarity gap and a confidence-guided efficiency incentive. Operating entirely before the backbone, AllocEmbed integrates with existing retrieval systems without modifying the embedding model or downstream pipeline. Experiments on the MMEB-V2 V-QA and V-RET tasks and our LongRet benchmark show that AllocEmbed achieves the best overall retrieval performance among the evaluated budget-matched methods and transfers across embedding backbones. Our code is publicly available at https://github.com/jinsong8/AllocEmbed.

</details>

---

## Autonomous Driving

### 1. VIPS: Vehicle-Infrastructure Cooperative Planning Benchmark via Pseudo-Simulation **⭐⭐⭐⭐** (相关度: 95%, 质量: 0.85)

- **arXiv ID**: [2609.02462](https://arxiv.org/abs/2609.02462)  · [📄 PDF](https://arxiv.org/pdf/2609.02462)
- **作者**: Hoonhee Cho, Jae-Young Kang, Giwon Lee et al. (6 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-02 · **分类**: cs.CV
- **摘要（中）**: ①针对V2I协同自动驾驶中开放环评估无法捕捉误差累积、闭环评估成本高且存在域差距的问题。②提出了VIPS基准，基于伪模拟整合车辆和基础设施观测，实现可扩展且逼真的鲁棒性和误差传播评估；并提出了CoS-V2X协同规划框架，使用稀疏表示建模车-基础设施交互。③相比现有协议，VIPS在无需完整模拟的情况下平衡了评估真实性和可扩展性，CoS-V2X通过紧凑特征实现高效通信和稳健决策。④摘要未提供具体数据，但强调了伪模拟的扩展性和CoS-V2X的鲁棒性优势。
- **摘要（英）**: This paper addresses the trade-off between open-loop and closed-loop evaluation in V2I cooperative driving by proposing VIPS, a pseudo-simulation benchmark integrating vehicle and infrastructure observations for scalable robustness assessment. It also introduces CoS-V2X, a sparse-representation-based planning framework for efficient communication and robust decision-making. The approach enables realistic error propagation analysis without full simulation costs.
- **评估**: 该论文针对V2I协同驾驶评估的空白，提出伪模拟基准和稀疏规划框架，对自动驾驶感知与规划研究具有重要参考价值。
- **核心贡献**: 提出了VIPS伪模拟基准和CoS-V2X稀疏协同规划框架。
- **创新点**: 将伪模拟扩展到V2I场景，并用稀疏表示实现高效协同规划。
- **结果**: 实现了可扩展的鲁棒性评估和高效决策，具体数据未在摘要中给出。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> End-to-end autonomous driving in urban environments requires robust decision-making under partial observability and complex multi-agent interactions. Severe occlusions and dense traffic at intersections limit the perception capability of single-agent systems, motivating recent efforts on Vehicle-to-Infrastructure (V2I) cooperation for perception and planning. However, existing evaluation protocols face a fundamental trade-off: open-loop evaluation fails to capture error accumulation and recovery from deviations, while closed-loop evaluation is costly, difficult to scale, and often relies on simulated environments that may suffer from domain gaps. To bridge this gap, we propose VIPS, a benchmark for cooperative autonomous driving in V2I settings based on pseudo-simulation. VIPS extends pseudo-simulation by integrating vehicle and infrastructure observations. This enables scalable yet realistic evaluation of robustness and error propagation without full simulation. We further present CoS-V2X, a cooperative planning framework based on sparse representations. CoS-V2X models vehicle-infrastructure interactions using compact features for efficient communication and robust decision-making under heterogeneous observations. Code and dataset are available at https://vips2026.github.io.

</details>

### 2. Towards Zero-Shot Transfer Across Embodiments For Driving VLAs **⭐⭐⭐⭐** (相关度: 95%, 质量: 0.85)

- **arXiv ID**: [2609.02341](https://arxiv.org/abs/2609.02341)  · [📄 PDF](https://arxiv.org/pdf/2609.02341)
- **作者**: Caio Azevedo, Stefano Sabatini, Sascha Hornauer et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-02 · **分类**: cs.CV
- **摘要（中）**: 针对驾驶视觉-语言-动作模型（VLA）在跨数据集和跨传感器配置下零样本迁移能力差的问题，本文提出BEV-Forcing辅助目标，将专用鸟瞰图（BEV）模型中的地面平面物体布局信息迁移到VLA骨干网络中。通过鼓励模型通过共享BEV空间接口表示物体位置，该方法在多数据集训练中提升了分布内和分布外性能。相比简单增加训练数据，该方法更有效地改善了跨具身泛化能力。
- **摘要（英）**: This paper addresses the poor zero-shot transfer of driving Vision-Language-Action models across datasets and camera rigs by proposing BEV-Forcing, an auxiliary objective that transfers ground-plane object-layout information from a specialized BEV model into the VLA backbone. By encouraging shared BEV spatial representations, it improves both in-distribution and out-of-distribution performance in multi-dataset training, outperforming naive data scaling.
- **评估**: 该论文针对自动驾驶VLA跨域泛化这一关键问题，提出了一种简洁有效的BEV辅助训练方法，具有较高的实用价值。
- **核心贡献**: 提出BEV-Forcing辅助目标，提升驾驶VLA的跨数据集和跨传感器零样本迁移能力。
- **创新点**: 利用BEV空间接口作为共享表示，将专用模型知识注入VLA训练。
- **结果**: 在多数据集训练中，BEV-Forcing显著提升了分布内和分布外性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-Language-Action models (VLAs) have shown strong potential in autonomous driving by leveraging multimodal pretraining for instruction following, visual reasoning, and scene-level generalization. In robotic manipulation, scaling VLA fine-tuning across multiple robot setups--especially when unifying representations across embodiments--has been shown to improve in-dataset performance and cross-embodiment generalization; in autonomous driving, however, VLAs remain largely trained on individual datasets and are rarely evaluated for zero-shot transfer to unseen datasets and camera rigs; furthermore naively adding more datasets to the training data does not necessarily lead to better performance within seen embodiments. To address these problems, we study multi-dataset training for the driving task and BEV-Forcing, an auxiliary objective that transfers ground-plane object-layout information from a specialized Bird's-Eye-View model into the VLA backbone. By encouraging the model to represent object position through a shared BEV spatial interface, we show that an auxiliary task such as BEV-Forcing can improve both in-distribution and out-of-distribution performance when training on a small number of camera rigs. As the number of training embodiments increases, however, the benefits of the auxiliary task are reduced; we present this as evidence that new techniques in the literature may see their benefits diminish when simply scaling up training diversity, which motivates presenting results taking into account data scaling.

</details>

### 3. InsightSeg: Reusing Correction Insights for Guideline-Consistent Segmentation **⭐⭐⭐** (相关度: 70%, 质量: 0.75)

- **arXiv ID**: [2609.02002](https://arxiv.org/abs/2609.02002)  · [📄 PDF](https://arxiv.org/pdf/2609.02002)
- **作者**: Vanshika Vats, Ashwani Rathee, James Davis
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-02 · **分类**: cs.CV, cs.AI
- **摘要（中）**: 针对多智能体细化系统中反馈被丢弃、导致相同错误重复出现的问题，本文提出InsightSeg，一种情景记忆机制，将成功的修正过程转化为可复用的、视觉锚定的自然语言洞察。通过元分析器将修正过程蒸馏为指令性洞察，并利用补丁级视觉概念向量锚定到相关图像区域，后续图像通过匹配密集补丁嵌入来检索相关洞察，从而在首次预测前条件化分割智能体。该方法将系统从纠正重复错误转变为预防错误，在Waymo和Cityscapes上提升了分割质量。
- **摘要（英）**: This paper introduces InsightSeg, an episodic memory mechanism that converts successful correction episodes into reusable, visually grounded insights for guideline-consistent segmentation. By distilling corrections into directive insights anchored to patch-level visual concepts and retrieving them for subsequent images, it shifts from correcting recurring errors to preventing them, improving segmentation quality on Waymo and Cityscapes.
- **评估**: 该论文提出了一种新颖的记忆增强机制，有效解决了多智能体分割系统中的重复修正问题，具有较好的创新性。
- **核心贡献**: 提出InsightSeg情景记忆机制，将修正洞察复用至后续分割预测，减少重复错误。
- **创新点**: 利用补丁级视觉概念向量锚定自然语言洞察，实现跨图像的洞察检索与条件化。
- **结果**: 在Waymo和Cityscapes上，InsightSeg在细化前即提升了分割质量。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Guideline-consistent semantic segmentation requires more than category recognition, as real-world labeling policies demand fine-grained, task-specific decisions. Recent multi-agent refinement systems improve compliance with such textual guidelines by detecting and correcting errors. However, they are stateless: feedback from the critiquing agent is discarded, causing the same guideline-specific mistakes to be repeatedly rediscovered and corrected across the dataset at the cost of additional refinement. We introduce InsightSeg, an episodic memory mechanism that converts successful correction episodes into reusable, visually grounded insights. A meta-analyzer distills each qualifying episode into directive natural-language insights and anchors them to the local image regions that caused the error using patch-level visual concept vectors. On subsequent images, these concepts are matched against dense patch embeddings to retrieve relevant insights, which condition the segmenting agent before making its first prediction. This shifts the system from correcting recurring errors to preventing them, improving segmentation quality before any refinement occurs. Across Waymo and Cityscapes, InsightSeg improves both first-pass and final guideline-consistent segmentation performance while requiring fewer refinement steps, demonstrating that multi-agent refinement can become more accurate and efficient by drawing on past correction experience.

</details>

### 4. Designing Versatile Samples for Learned Trajectory Scoring **⭐⭐⭐⭐** (相关度: 90%, 质量: 0.8)

- **arXiv ID**: [2609.01799](https://arxiv.org/abs/2609.01799)  · [📄 PDF](https://arxiv.org/pdf/2609.01799)
- **作者**: Yaguang Li, Jiaru Zhang, Chuheng Wei et al. (5 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-01 · **分类**: cs.RO, cs.CV
- **摘要（中）**: 针对端到端驾驶策略中轨迹评分器训练样本信息量不足的问题，本文设计了一种更具信息量的训练数据集，通过两个生成器沿横向（朝向可行驶边界）和纵向（朝向引导车辆）扰动记录的人类轨迹，生成比基础规划器提议池更具区分度的正负样本。将基于Transformer的评分器附加到DiffusionDrive和MeanFuser两个冻结生成式规划器上，在NAVSIM navtrain数据集上训练，实验结果显示在ResNet-34下分别达到90.1和90.4的EPDMS，相比基础数据集提升了0.4和0.3。
- **摘要（英）**: This paper addresses the limited supervision near decision boundaries in trajectory scoring by designing a training dataset with perturbed human trajectories along lateral and longitudinal axes, generating more informative positive and negative samples. Attaching a transformer-based scorer to frozen DiffusionDrive and MeanFuser planners, it achieves 90.1 and 90.4 EPDMS on NAVSIM navtrain with ResNet-34, improving by 0.4 and 0.3 over the base dataset.
- **评估**: 该论文针对轨迹评分训练数据设计提出了实用方案，显著提升了评分器性能，对端到端驾驶有直接贡献。
- **核心贡献**: 设计了一种基于轨迹扰动的训练数据集生成方法，提升轨迹评分器的监督信息质量。
- **创新点**: 沿横向和纵向扰动人类轨迹，生成决策边界附近的信息性样本。
- **结果**: 在DiffusionDrive和MeanFuser上分别达到90.1和90.4 EPDMS，较基线提升0.4和0.3。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Many current end-to-end driving policies emit a pool of candidate trajectories and select one, which makes selection a separable component: a scorer can be retrained while the planner, its backbone, and its trajectory generator all stay frozen. However, many strong planners concentrate their proposals around safe mode, providing limited supervision near decision boundaries. In this work, we design a training dataset that provides more informative supervision for the scorer. In particular, we construct two generators that perturb the logged human trajectory along the two axes a vehicle can be displaced: laterally toward the drivable boundary and longitudinally toward a leading vehicle. The designed dataset produces more informative positive and negative samples than the base planner's proposal pool. We attach a transformer-based scorer to two frozen generative planners, DiffusionDrive and MeanFuser, and train it on the NAVSIM navtrain dataset. The results of the experiments show that we achieve 90.1 EPDMS on DiffusionDrive and 90.4 EPDMS on MeanFuser when using ResNet-34, with 0.4 and 0.3 EPDMS respectively, from the designed training dataset.

</details>

---

## Multimodal

### 1. TC-Next: Zero-Shot Multimodal Cyclone Forecasting **⭐⭐⭐** (相关度: 50%, 质量: 0.75)

- **arXiv ID**: [2609.02085](https://arxiv.org/abs/2609.02085)  · [📄 PDF](https://arxiv.org/pdf/2609.02085)
- **作者**: Zhe Wang, Sijie Chen, Yiming Luo et al. (5 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-02 · **分类**: cs.LG, cs.CV
- **摘要（中）**: 针对热带气旋路径和强度预测中传统追踪器依赖规则、精度有限的问题，提出TC-Next多模态深度学习模型。该方法利用基础模型的预报场和红外卫星图像，在6-24小时预报时效内预测气旋轨迹和强度。相比规则追踪器TempestExtremes，在GraphCast上降低轨迹误差15-44%、强度误差3-6倍，且零样本迁移至Pangu-Weather和IFS HRES仍保持优势。
- **摘要（英）**: To improve tropical cyclone forecasting, this paper proposes TC-Next, a multimodal model leveraging foundation model forecast fields and satellite imagery. It reduces track error by 15-44% and intensity error by 3-6x over a rule-based tracker, and generalizes zero-shot to other forecast models.
- **评估**: 该论文聚焦气象预测，与自动驾驶感知领域相关性有限，但多模态融合和零样本迁移方法有借鉴意义。
- **核心贡献**: 提出多模态气旋预测模型，利用基础模型预报场和卫星图像提升预测精度。
- **创新点**: 结合基础模型预报场和卫星图像的多模态融合及零样本迁移。
- **结果**: 在多个预报模型上显著降低轨迹和强度误差。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present TropicalCycloneNext (TC-Next), a multimodal deep learning model that forecasts tropical cyclone track and intensity at $6$-$24$ h leads by leveraging a foundation model's forecast fields of atmospheric kinematic and thermodynamic fields and GridSat infrared satellite imagery. Trained only on GraphCast forecasts over the Western Pacific (WP), yet reliant only on generic atmospheric variables, TC-Next on GraphCast lowers track error by $15$-$44\%$ and intensity error by a factor of $3$-$6$ relative to a conventional, rule-based tracker, TempestExtremes; applied without retraining to the forecast fields of Pangu-Weather and IFS HRES, it stays ahead of TempestExtremes on both. Applied zero-shot to the generic weather fields of WeatherNext Cyclones on the 2025 WP season, TC-Next attains lower intensity error at every lead time, and lower or comparable track error, compared to that model's specialized direct tracker in a deterministic comparison. Our ablation studies show that our multimodal model is able to utilize the additional modality to improve performance in tracking errors at every lead time and in intensity prediction at longer lead times.

</details>

### 2. Evidential Deep Learning for Multi-Modal Anti-UAV Detection **⭐⭐⭐⭐** (相关度: 85%, 质量: 0.8)

- **arXiv ID**: [2609.01742](https://arxiv.org/abs/2609.01742)  · [📄 PDF](https://arxiv.org/pdf/2609.01742)
- **作者**: Dmitry Golovchits, Seyed Sahand Mohammadi Ziabari, Ali Mohammed Mansoor Alsahag
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-01 · **分类**: cs.CV
- **摘要（中）**: 针对反无人机系统中多传感器融合检测头缺乏逐模态可靠性信号的问题，系统评估证据深度学习头、Dempster-Shafer证据融合和不确定性驱动时间传感器门控的效果。在三个基准上的受控消融表明，EDL训练目标相比重训练的sigmoid基线提升准确率5.9个百分点（E1）和4.8个百分点（E2），且熵排序误差显著更好；但DS融合和Dirichlet空值假设未获支持。
- **摘要（英）**: To address the lack of per-modality reliability in anti-UAV detection, this paper systematically evaluates evidential deep learning heads, DS fusion, and uncertainty-driven gating. EDL improves accuracy by up to 5.9 points over sigmoid baselines and ranks errors better, while DS fusion and Dirichlet vacuity hypotheses are not supported.
- **评估**: 该论文对不确定性估计在多模态检测中的适用性进行了严谨消融，对自动驾驶多传感器感知的可靠性设计有重要参考价值。
- **核心贡献**: 系统评估证据深度学习在多模态反无人机检测中的有效性，揭示其优势与局限。
- **创新点**: 通过受控消融验证EDL头在精度和误差排序上的优势，并指出DS融合的不足。
- **结果**: EDL训练目标提升准确率最高5.9个百分点，熵排序UAUC约0.94。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Anti-UAV systems increasingly fuse multiple sensors, yet their detection heads provide no per-modality reliability signal. This study evaluates whether evidential deep learning (EDL) heads, Dempster-Shafer (DS) evidence fusion, and uncertainty-driven temporal sensor gating improve anti-UAV detection through a controlled ablation on three benchmarks: thermal tracking (AntiUAV600), RGB-audio-RF classification (TRIDENT), and RGB-IR tracking (MM-UAV). The EDL training objective improves accuracy over retrained sigmoid baselines (+5.9 percentage points in accuracy and a tripled tracker-on-absent rate in E1; +4.8 percentage points in classification accuracy in E2, surviving a clip-clustered bootstrap, p = 0.011) and ranks classification errors substantially better (entropy UAUC approximately 0.94 vs. 0.51). The remaining components do not support their respective hypotheses. DS fusion does not outperform simple probability averaging. Dirichlet vacuity adds no ranking power beyond predictive entropy and inverts at the detection level, where extreme background imbalance causes it to encode class membership rather than error likelihood, a failure also observed for entropy and sigmoid confidence. Temporal gating preserves accuracy only when nearly inactive and yields no realised latency saving on shared-backbone hardware. The benefit of evidential learning therefore arises primarily from its training objective rather than its uncertainty estimate; a crop-level control further localises the detection-level breakdown to anchor-level evaluation rather than the learned representation.

</details>

### 3. IT-TextFusion: Iterative Text-Image Interaction with Text-Guided Residual Refinement for Degradation-Aware Image Fusion **⭐⭐** (相关度: 40%, 质量: 0.55)

- **arXiv ID**: [2609.01092](https://arxiv.org/abs/2609.01092)  · [📄 PDF](https://arxiv.org/pdf/2609.01092)
- **作者**: Siyang Liu, Peiyi Zhou, Tianle Jin et al. (6 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-01 · **分类**: cs.CV
- **摘要（中）**: ①针对现有文本引导图像融合方法中语义-视觉交互浅层、注意力机制受限的问题，提出迭代式文本引导融合框架。②集成最深层交叉注意力、多尺度交叉门控融合和阶段特定文本调节，使全局文本嵌入条件化层次特征融合和残差细化。③通过重复注入文本嵌入实现退化感知的全局语义条件化，同时保留可见光和红外模态的互补信息。④在多个基准数据集上提升了信息保留指标，但摘要未给出具体数值。
- **摘要（英）**: This paper tackles the limitations of shallow semantic-visual interaction in text-guided image fusion by proposing an iterative framework with cross-attention, cross-gate fusion, and stage-specific text modulation. The method enhances degradation-aware global conditioning while preserving multimodal complementary information, showing improvements on benchmark datasets.
- **评估**: 该论文属于多模态融合领域，与自动驾驶感知有一定关联，但方法细节和实验数据不足，影响力一般。
- **核心贡献**: 提出了一种迭代式文本引导图像融合框架，增强全局语义条件化。
- **创新点**: 通过多阶段文本嵌入注入实现退化感知的层次化融合与细化。
- **结果**: 在多个基准上提升了信息保留性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Text-guided image fusion has recently emerged as an effective paradigm for integrating multi-modal information while enabling flexible and task-oriented fusion control. However, existing text-guided fusion methods often rely on shallow semantic-visual interaction and limited attention mechanisms, which restrict their ability to robustly handle complex degradations and fully exploit textual guidance. In this paper, we propose an iterative text-guided image fusion framework that incorporates text-conditioned feature interaction across multiple fusion and refinement stages. The proposed method integrates deepest-level Cross-Attention, multi-scale Cross-Gate Fusion, and stage-specific text-conditioned modulation, allowing the global text embedding to condition hierarchical feature fusion and residual refinement. By repeatedly injecting the pooled text embedding across hierarchical decoder and refinement stages, the proposed framework provides degradation-aware global semantic conditioning while preserving complementary information from the visible and infrared modalities. Experiments on several benchmark datasets show that the proposed method improves several information-preservation and perceptual-quality metrics, while exhibiting metric-dependent trade-offs on some datasets.

</details>

---

## Network Pruning

### 1. VoRTeC: Taming Foundation Flow for One-step Real time Video Compression **⭐⭐⭐** (相关度: 30%, 质量: 0.8)

- **arXiv ID**: [2609.02291](https://arxiv.org/abs/2609.02291)  · [📄 PDF](https://arxiv.org/pdf/2609.02291)
- **作者**: Yichong Xia, Qinhong Wu, Qinhong Wu et al. (6 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-02 · **分类**: cs.CV, cs.AI
- **摘要（中）**: ①针对超低码率视频压缩中传统方法产生模糊伪影、扩散方法解码延迟高和时间一致性差的问题。②提出了VoRTeC框架，基于基础流模型Wan2.1，通过紧凑编码潜在视频表示、预测流轨迹位置和集成多尺度先验，实现单步解码和高感知保真度。③相比现有扩散方法，无需访问流匹配网络参数或梯度，通过尾帧复用和先验缓存保持帧组一致性。④实验表明，比特消耗降低58%，解码速度提升3至197倍，720p下13 FPS，480p下32 FPS。
- **摘要（英）**: This work tackles ultra-low-bitrate video compression by proposing VoRTeC, a framework built on a foundational flow model that enables one-step decoding via compact latent encoding and flow-trajectory prediction. It avoids accessing flow network internals and uses tail-frame reuse for temporal consistency. Results show 58% bit reduction and 3-197x faster decoding compared to diffusion baselines.
- **评估**: 该论文在视频压缩领域有显著性能提升，但与自动驾驶感知方向相关性较低。
- **核心贡献**: 提出了基于流模型的单步实时视频压缩框架VoRTeC。
- **创新点**: 利用基础流模型先验实现无需参数访问的单步解码。
- **结果**: 比特消耗降低58%，解码速度提升3-197倍。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Ultra-low bitrate video compression still faces critical challenges: traditional neural video compression inevitably introduces blurring artifacts, while diffusion-based generative video compression suffers from excessive decoding latency and poor temporal consistency. To address these issues, we propose $\mathtt{VoRTeC}$, a Video Compression framework built upon a foundational flow model (Wan2.1). By compactly encoding latent video representations, predicting the positions of compressed representations along flow trajectories, and integrating multi-scale priors, $\mathtt{VoRTeC}$ enables the compressor to harness generative video flow priors effectively. Without accessing the parameters or gradients of flow matching networks, our framework achieves one-step decoding and reconstructions with high perceptual fidelity. Meanwhile, we maintain consistency across frame groups via tail-frame reuse and prior caching. Extensive experiments demonstrate that our method reduces bit consumption by 58\% compared to prior diffusion-based approaches, with decoding speed boosted by 3 to 197 times: $\mathtt{VoRTeC}$ achieves a decoding speed of 13 FPS at 720p and 32 FPS at 480p.

</details>

### 2. CC-4DGS: Computational Deformation and Point-Cloud Compression for Storage-Efficient Dynamic Gaussian Splatting **⭐⭐⭐** (相关度: 25%, 质量: 0.75)

- **arXiv ID**: [2609.02184](https://arxiv.org/abs/2609.02184)  · [📄 PDF](https://arxiv.org/pdf/2609.02184)
- **作者**: Kyungdae Park, Chae Eun Rhee
- **🏷️ 机构**: Hanyang University
- **提交日期**: 2026-09-02 · **分类**: cs.CV
- **摘要（中）**: ①针对动态4D高斯泼溅表示存储开销大，依赖大型多分辨率哈希表和高维属性。②提出了CC-4DGS框架，引入计算变形场替代可学习哈希表，使用确定性密集哈希编码和紧凑神经解码器，将变形存储降至每场景1-3MB；并设计点云属性压缩管道，通过条件自编码和量化实现3-5倍点云缩减。③相比现有方法，重新思考变形建模和属性存储，实现存储高效且可扩展。④摘要未提供具体质量数据，但强调保持实时渲染性能。
- **摘要（英）**: This paper addresses storage inefficiency in dynamic 4D Gaussian Splatting by proposing CC-4DGS, which uses a computational deformation field with deterministic hash encoding to reduce deformation storage to 1-3MB per scene. It also compresses point-cloud attributes via conditional autoencoding and quantization, achieving 3-5x reduction with minimal quality loss. The framework preserves real-time rendering while being storage-efficient.
- **评估**: 该论文在3D表示压缩方面有创新，但与自动驾驶感知核心领域关联较弱。
- **核心贡献**: 提出了存储高效的动态高斯泼溅框架CC-4DGS。
- **创新点**: 用计算变形场替代哈希表，并压缩点云属性。
- **结果**: 变形存储降至1-3MB，点云缩减3-5倍。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Dynamic four-dimensional (4D) Gaussian Splatting has emerged as a powerful explicit representation for high-quality view synthesis, yet existing methods still require tens to hundreds of megabytes per scene due to their heavy reliance on large multi-resolution hash tables and high-dimensional Gaussian attributes. This paper presents CC-4DGS, a storage-efficient and scalable framework that rethinks both deformation modeling and canonical attribute storage. First, we introduce a computational deformation field (CDF) that replaces large multi-resolution learnable hash tables with deterministic dense hash encoding and compact neural decoders, enabling on-the-fly synthesis of deformation features while reducing deformation storage to only 1--3 MB per scene. Second, we propose a compression of canonical point-cloud attributes (CCA) pipeline that compresses high-dimensional spherical harmonic appearance terms and auxiliary Gaussian attributes via conditional autoencoding, selective quantization, and residual codebooks, achieving 3--5$\times$ point-cloud reduction with negligible quality loss. Together, these components yield a unified representation that preserves real-time rendering performance while reducing total storage to 20--30 MB. Extensive experiments across the N3DV and Technicolor Light Field datasets demonstrate that CC-4DGS achieves reconstruction accuracy comparable to state-of-the-art methods such as Swift4D, while offering significantly improved storage efficiency and favorable runtime-memory trade-offs.

</details>

### 3. A Unified Rate-Distortion Perspective on Vector, Product, and Scalar Quantization **⭐⭐⭐** (相关度: 50%, 质量: 0.75)

- **arXiv ID**: [2609.02107](https://arxiv.org/abs/2609.02107)  · [📄 PDF](https://arxiv.org/pdf/2609.02107)
- **作者**: Xianghong Fang, Wenlong Mou, Yuan Yuan et al. (5 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-02 · **分类**: cs.LG, cs.CV
- **摘要（中）**: ①针对离散视觉标记化中向量、标量和乘积量化缺乏统一概念框架的问题，提出率失真视角。②将量化视为有损压缩，用标记数和码本大小表征标称固定长度编码率，量化误差作为失真。③理论上和实证上证明最小化失真是重建保真的主要内在目标，并建立公平比较条件，恢复VQ-PQ-SQ失真层级。④现代VQ方法在相同条件下实现最低失真，为离散视觉标记化提供基础性重框架。
- **摘要（英）**: This paper proposes a unified rate-distortion framework for discrete visual tokenization, characterizing quantization as lossy compression and resolving key questions about distortion minimization and fair comparison. It theoretically and empirically establishes the VQ-PQ-SQ distortion hierarchy, showing modern VQ methods achieve the lowest distortion under controlled conditions.
- **评估**: 该论文提供理论视角，对自监督视觉和表征学习有参考价值，但与自动驾驶感知的直接相关性较低。
- **核心贡献**: 提出统一率失真视角，重新定义离散视觉标记化的量化权衡。
- **创新点**: 通过率失真理论建立量化方法公平比较条件并揭示失真层级。
- **结果**: 理论上和实证上验证了现代VQ方法的优越性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Discrete visual tokenization, predominantly driven by vector, scalar, and product quantization, lacks a unified conceptual framework for understanding quantization tradeoffs. In this paper, we propose a unified rate--distortion perspective on modern discrete visual tokenization. By viewing quantization as lossy compression, we characterize the nominal fixed-length coding rate through token count and codebook size, and quantization error as the distortion. Within this framework, we resolve three central questions. First, we theoretically and empirically show that minimizing distortion, rather than maximizing codebook utilization, is the primary intrinsic objective for reconstruction fidelity, with a direct connection to the STE-induced gradient discrepancy. Second, we establish two critical fairness conditions for intrinsic quantization comparison: controlling latent feature statistics and enforcing identical coding rates. Third, under these conditions, we recover the VQ--PQ--SQ distortion hierarchy in modern visual tokenization and show empirically that modern VQ methods achieve the lowest distortion. This work provides a foundational rate--distortion reframing of modern discrete visual tokenization, resolves ambiguities in quantizer evaluation, and provides a controlled framework for isolating intrinsic quantization effectiveness under fixed-rate constraints.

</details>

---

## 3D Detection

### 1. KSG-Net: Key-Sparse and Global-Context Learning for Maritime 3D Ship Detection **⭐⭐⭐** (相关度: 75%, 质量: 0.7)

- **arXiv ID**: [2609.02077](https://arxiv.org/abs/2609.02077)  · [📄 PDF](https://arxiv.org/pdf/2609.02077)
- **作者**: Zhouyuan Huai, Meiqi Wan, Yan Yang et al. (7 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-02 · **分类**: cs.CV
- **摘要（中）**: 针对海事环境中3D船舶检测中小型船舶点云稀疏、大型船舶全局结构建模不足的问题，本文提出KSG-Net，一种关键稀疏与全局上下文学习网络。其核心思想是在统一的全稀疏检测框架内联合增强局部判别特征和全局结构感知，通过关键稀疏多尺度聚合模块选择信息性关键体素并聚合跨尺度邻域特征，以增强小型稀疏船舶的表示。该方法旨在平衡检测精度和计算效率，并改善对海事场景的泛化能力。
- **摘要（英）**: This paper proposes KSG-Net, a key-sparse and global-context learning network for maritime 3D ship detection, addressing weak features for small sparse vessels and insufficient global modeling for large ones. It jointly enhances local discriminative features and global structural awareness within a unified fully sparse framework via a Key Sparse Multi-scale Aggregation module, aiming to balance accuracy and efficiency.
- **评估**: 该论文针对海事3D检测的特定挑战提出了定制化方案，具有领域应用价值，但创新性一般。
- **核心贡献**: 提出KSG-Net，一种面向海事3D船舶检测的关键稀疏与全局上下文学习网络。
- **创新点**: 设计关键稀疏多尺度聚合模块，联合增强局部与全局特征。
- **结果**: KSG-Net旨在提升海事场景下小型稀疏和大型船舶的检测精度与效率。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Accurate 3D ship detection in maritime environments is critical for autonomous navigation, yet remains challenging due to large-scale vessel variations, sparse point clouds of small vessels, and severe sea-clutter interference. Existing methods, primarily based on 2D features or dense representations, struggle to balance detection accuracy and computational efficiency, while sparse 3D detectors designed for road scenes generalize poorly to maritime scenarios. This paper focuses on two key challenges in maritime LiDAR perception: weak feature representation for small and sparse vessels, and insufficient global structural modeling for large vessels due to the limited receptive field of local sparse convolutions. To address these issues, we propose KSG-Net, a Key-Sparse and Global-Context learning network for maritime 3D ship detection. The core idea is to jointly enhance local discriminative features and global structural awareness within a unified fully sparse detection framework. Specifically, a Key Sparse Multi-scale Aggregation (KSMA) module is designed to enhance the representation of small and sparse vessels by selecting informative key voxels and aggregating cross-scale neighborhood features. Furthermore, a Global Context Aggregation (GCA) module is introduced to capture long-range geometric dependencies through scene-level context modeling with gated residual interactions, thereby improving the representation of large vessels. Extensive experiments on the Thames River vessel dataset and simulated datasets demonstrate that KSG-Net consistently outperforms existing methods in multi-scale vessel detection and exhibits strong robustness in complex maritime environments.

</details>

### 2. RAFT-DVC: Resolution-Aware Machine Learning-Based Digital Volume Correlation **⭐⭐** (相关度: 20%, 质量: 0.6)

- **arXiv ID**: [2609.01876](https://arxiv.org/abs/2609.01876)  · [📄 PDF](https://arxiv.org/pdf/2609.01876)
- **作者**: Zixiang Tong, Lehu Bu, Jin Yang
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-01 · **分类**: cs.CV, cond-mat.mtrl-sci
- **摘要（中）**: 针对机器学习数字体积相关（DVC）模型中内部分辨率对精度和操作范围影响不明的问题，本文提出RAFT-DVC，一个分辨率感知的RAFT-based DVC求解器家族，具有编码器下采样因子s=2、4和8。通过匹配设计，发现三个求解器将位移定位到约0.017特征网格体素，经验原始体积误差缩放约为0.017s体素。合成基准显示，在细纹理、小到中等位移条件下，RAFT-DVC达到与经典DVC相同量级的误差，在粗纹理、大位移条件下具有竞争力或优势。
- **摘要（英）**: This paper presents RAFT-DVC, a resolution-aware family of RAFT-based DVC solvers with encoder downsampling factors of 2, 4, and 8, addressing how internal resolution affects accuracy and operating range. The solvers localize displacement to ~0.017 feature-grid voxel with error scaling of ~0.017s voxel, achieving errors comparable to classical DVC under fine-texture conditions and competitive under coarse-texture, large-displacement conditions.
- **评估**: 该论文属于材料力学与计算机视觉交叉领域，与自动驾驶感知相关性较低，但方法设计严谨。
- **核心贡献**: 提出分辨率感知的RAFT-DVC求解器家族，系统研究分辨率对DVC精度的影响。
- **创新点**: 通过匹配设计量化不同下采样因子下的误差缩放规律。
- **结果**: RAFT-DVC在多种条件下达到与经典DVC相当或更优的精度。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Digital volume correlation (DVC) provides three-dimensional full-field displacement measurements from volumetric images, but how the internal resolution of a machine-learning-based DVC model affects accuracy and operating range remains poorly understood. Here, we present RAFT-DVC, a resolution-aware family of recurrent all-pairs field transforms (RAFT)-based DVC solvers with encoder downsampling factors s = 2, 4, and 8. Using a matched design, we find that the three solvers localize displacement to approximately 0.017 feature-grid voxel, giving an empirical raw-volume error scaling of approximately 0.017s voxel. The solvers exhibit complementary operating regimes governed jointly by displacement reach and volumetric-texture compatibility. Synthetic benchmarks show that RAFT-DVC achieves errors of the same order as tuned classical DVC under fine-texture, small-to-moderate-displacement conditions and becomes competitive or advantageous under coarse-texture, large-displacement conditions. Frequency-swept tests quantify deformation spatial resolution, while tiled inference enables dense estimation on large volumes. Evaluation on confocal volumetric images acquired during indentation illustrates the importance of matching solver operating regime to deformation magnitude and image texture. Tests on micro-CT images of elastomeric foam, despite training only on particle-labeled synthetic data, provide evidence of cross-texture transfer. We also identify coordinate-order inconsistencies in three-dimensional RAFT correlation sampling and introduce a non-cubic impulse test to verify sampler geometry independently of network training. Correcting the sampler improves native-input accuracy and generalization to unseen volume dimensions. Together, these results establish RAFT-DVC as a fast, resolution-aware framework for dense DVC with characterized accuracy and operating regimes.

</details>

---

## Knowledge Distillation

### 1. Learning to Track from Privileged Target Appearances **⭐⭐⭐⭐** (相关度: 85%, 质量: 0.8)

- **arXiv ID**: [2609.02471](https://arxiv.org/abs/2609.02471)  · [📄 PDF](https://arxiv.org/pdf/2609.02471)
- **作者**: Xin Chen, Jiao Xu, Dong Wang et al. (5 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-02 · **分类**: cs.CV
- **摘要（中）**: ①针对视觉跟踪中目标模板在初始精确但易过时、近期模板新鲜但定位不确定的瓶颈，提出特权外观迁移跟踪框架。②引入非部署的oracle量化该瓶颈，显示LaSOT上AUC可提升15.2个百分点，并设计教师-学生训练框架PATT，教师观察过去、当前和未来帧的精确目标裁剪，学生仅用过去模板预测教师搜索表示。③通过多级表示预测和基于教师相对定位置信度的加权迁移，避免不可靠信号。④在LaSOT等基准上显著提升跟踪性能，具体数值未在摘要中给出。
- **摘要（英）**: This paper identifies the template bottleneck in visual tracking, where initial templates become stale and recent ones are uncertain, and proposes PATT, a teacher-student framework that transfers privileged future-frame appearances to a deployable tracker. The oracle analysis reveals a 15.2-point AUC gap on LaSOT, and PATT effectively closes this gap through multi-level representation prediction and confidence-weighted transfer.
- **评估**: 该论文针对跟踪核心问题提出创新训练范式，与自动驾驶多目标跟踪高度相关，实验充分，值得关注。
- **核心贡献**: 提出特权外观迁移训练框架，利用未来帧信息提升可部署跟踪器的性能。
- **创新点**: 通过教师-学生架构和置信度加权迁移，将不可部署的oracle优势转化为训练信号。
- **结果**: 在LaSOT上显著提升AUC，缩小了与oracle的差距。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Target templates define what a visual tracker searches for, yet the templates available at inference trade off localization certainty with appearance freshness: the initial ground-truth template is exact but becomes stale, whereas recent templates better reflect the current appearance but are cropped from uncertain predictions. We quantify this bottleneck with a non-deployable oracle that supplies an exact current-frame target crop, improving AUC on LaSOT by 15.2 percentage points. This gap reveals a training-only opportunity: frame-level ground truths provide exact current- and future-frame target crops, although such crops are unavailable at deployment. We introduce Privileged Appearance Transfer for Tracking (PATT), a teacher-student training framework that transfers these privileged appearances to a deployable tracker through multi-level representation prediction. The privileged teacher observes exact target crops from past, current, and future frames, whereas the student receives only past-frame templates and learns to predict the teacher's search representations. To avoid transferring unreliable teacher signals, PATT weights this transfer by the teacher's relative localization advantage over the student and its absolute localization accuracy. After training, the teacher, latent predictor, reliability weights, and privileged crops are removed, leaving standard student-only inference. Across seven benchmarks at two model scales, PATT achieves consistent gains under both long- and short-term tracking protocols.

</details>

### 2. Progressive Pseudo-Label Optimization for Point-Supervised Change Detection **⭐⭐⭐** (相关度: 70%, 质量: 0.7)

- **arXiv ID**: [2609.02171](https://arxiv.org/abs/2609.02171)  · [📄 PDF](https://arxiv.org/pdf/2609.02171)
- **作者**: Hailong Ning, Hao Wang, Yimeng Wang et al. (6 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-02 · **分类**: cs.CV
- **摘要（中）**: ①针对点监督变化检测中稀疏标注导致伪标签不完整和噪声的问题，提出两阶段框架。②第一阶段利用SAM2生成对象感知候选掩码，设计双时相掩码选择策略转换为变化伪标签，并用轻量CNN细化边界；第二阶段构建教师-学生自训练框架，教师通过指数移动平均更新并周期刷新伪标签。③形成伪标签细化和模型重优化的闭环过程。④在三个基准数据集上验证，包括WHU数据集，但摘要未给出具体数值。
- **摘要（英）**: This paper addresses incomplete and noisy pseudo-labels in point-supervised change detection by proposing a two-stage framework that integrates SAM2 priors and progressive adaptation. Stage I generates reliable change pseudo-labels via bi-temporal mask selection and refinement, while Stage II uses teacher-student self-training for closed-loop optimization, achieving improvements on three benchmarks.
- **评估**: 该论文聚焦变化检测，与自动驾驶场景理解相关，方法结合SAM2有创新性，但实验数据不完整。
- **核心贡献**: 提出渐进式伪标签优化框架，结合SAM2先验提升点监督变化检测性能。
- **创新点**: 通过双时相掩码选择和不确定性感知细化，将通用分割先验适配到变化检测任务。
- **结果**: 在三个基准数据集上取得性能提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Point-supervised change detection (PS-CD) aims to identify pixel-level changes between bi-temporal images using only sparsely annotated points. Although point annotations substantially reduce labeling costs, their limited spatial coverage often results in incomplete and noisy pseudo-labels. To address this issue, we propose a two-stage framework that introduces SAM2 priors into PS-CD and progressively adapts them to the target task. In Stage I, SAM2 generates object-aware candidate masks from point annotations on the bi-temporal images, and a bi-temporal mask selection strategy is designed to convert generic segmentation responses into more reliable change pseudo-labels. Subsequently, a lightweight CNN refinement module with an uncertainty-aware loss is employed to improve boundary quality and local structural consistency. In Stage II, we construct a teacher-student self-training framework in which the teacher is updated by exponential moving average and periodically refreshes the pseudo-labels. This design establishes a closed-loop optimization process that alternates between pseudo-label refinement and model re-optimization. Experiments on three benchmark datasets, including WHU-CD, LEVIR-CD, and SYSU-CD, demonstrate that the proposed method outperforms previous weakly supervised approaches on most benchmarks and remains competitive with several fully supervised methods.

</details>

---

## Tracking

### 1. YesTrack: Referring Multi-Object Tracking via MLLM-based Yes/No Verification **⭐⭐⭐⭐⭐** (相关度: 95%, 质量: 0.85)

- **arXiv ID**: [2609.02318](https://arxiv.org/abs/2609.02318)  · [📄 PDF](https://arxiv.org/pdf/2609.02318)
- **作者**: Quansheng Hu, Qin Sun, Qiansen Dai et al. (7 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/ggbondrighthere24/YesTrack](https://github.com/ggbondrighthere24/YesTrack)
- **提交日期**: 2026-09-02 · **分类**: cs.CV
- **摘要（中）**: 针对指代多目标跟踪中MLLM仅作为描述生成器、需外部模块决策导致延迟高且未充分利用视觉-语言对齐能力的问题，提出YesTrack两阶段方法。该方法将指代任务重构为判别式任务，直接利用MLLM进行是/否验证，无需显式文本生成；引入时间置信度先验和时间参考传播两个轻量时间一致性约束增强可靠性。实验在Refer-KITTI和Refer-KITTI-V2上显著超越现有方法，并验证了判别式范式在通用MOT中的泛化性。
- **摘要（英）**: To address the underutilization of MLLMs in referring multi-object tracking, this paper proposes YesTrack, reformulating referring as a discriminative Yes/No verification task without explicit text generation. Lightweight temporal consistency constraints enhance reliability, and the paradigm generalizes to generic MOT. Experiments on Refer-KITTI and Refer-KITTI-V2 show significant improvements.
- **评估**: 该论文创新性地将MLLM用于判别式验证，直接提升RMOT效率与性能，对自动驾驶多目标跟踪高度相关。
- **核心贡献**: 提出基于MLLM是/否验证的判别式指代跟踪框架，消除外部决策模块。
- **创新点**: 将指代任务从生成式重构为判别式，并引入时间一致性约束。
- **结果**: 在Refer-KITTI和Refer-KITTI-V2上显著超越现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Referring multi-object tracking (RMOT) aims to track every instance in a video that matches a given language expression. Despite the recent integration of multimodal large language models (MLLMs) to enhance generalization, existing methods predominantly relegate them to the role of caption generators, necessitating external modules for final decision-making. This paradigm not only introduces extra latency but also severely underutilizes the inherent vision-language alignment capabilities of MLLMs. To address these limitations, we propose YesTrack, a novel two-stage RMOT method that reformulates referring as a discriminative task, directly leveraging MLLMs for Yes/No verification without explicit text generation. To further enhance the reliability and efficiency of this MLLM-based verification, we introduce two lightweight temporal consistency constraints: Temporal Confidence Prior (TCP) and Temporal Reference Propagation (TRP). We further validate the generality of this discriminative paradigm by proposing YesTrack-MOT, a straightforward yet highly effective instantiation for generic multi-object tracking (MOT). Experiments on Refer-KITTI and Refer-KITTI-V2 show that YesTrack significantly outperforms existing state-of-the-art methods while maintaining high efficiency, even when implemented with the smallest variant of Qwen3-VL. Code is released at https://github.com/ggbondrighthere24/YesTrack.

</details>

---

## Open-set Detection

### 1. GeoStore: Finding Small Storefronts in Large Scenes -- A Fine-Grained POI Localization Benchmark with Global-to-Local Asymmetric Matching **⭐⭐⭐⭐** (相关度: 85%, 质量: 0.8)

- **arXiv ID**: [2609.02012](https://arxiv.org/abs/2609.02012)  · [📄 PDF](https://arxiv.org/pdf/2609.02012)
- **作者**: Lu Han, Xiting Sun, Hao Wang et al. (7 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-02 · **分类**: cs.CV, cs.IR
- **摘要（中）**: ①针对POI定位中近景查询与广角参考的非对称、细粒度、开放集匹配问题，现有VPR方法因全局描述符稀释小目标而失效。②提出GeoStore基准和GLAM方法，结合检索锚定全局描述符与非对称局部路径，通过可学习软后期交互匹配区域令牌。③改进点在于处理尺度差异和开放集场景，而非对称匹配提升小目标定位精度。④实验表明GLAM在GeoStore上显著优于VPR基线，但摘要未提供具体数值。
- **摘要（英）**: This paper tackles asymmetric fine-grained open-set POI localization, where global descriptors fail on small targets. It introduces GeoStore benchmark and GLAM with retrieval-anchored global and asymmetric local matching, outperforming VPR baselines.
- **评估**: 为开放集细粒度定位提供新基准和方法，对自动驾驶中的地标识别有借鉴意义。
- **核心贡献**: 首个非对称细粒度POI定位基准及全局-局部匹配方法。
- **创新点**: 非对称局部路径和软后期交互机制。
- **结果**: 在GeoStore上优于现有VPR方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Point-of-interest (POI) localization -- matching a user's close-up storefront photograph against large-scale geo-tagged street-view imagery -- underpins map construction, POI verification, and location-based services. Its closest existing paradigm, visual place recognition (VPR), assumes symmetric, whole-image matching of the same scene at a comparable scale; POI localization instead must match a close-up query, in which the target fills the frame, against wide references in which the same POI occupies only a small, off-center region among visually similar shops, under a substantial capture-domain gap. We introduce GeoStore, to our knowledge the first benchmark dedicated to this asymmetric, fine-grained, open-set formulation, and show that global-descriptor methods tuned for symmetric VPR are systematically limited on it, since a single global vector dilutes the small target. We further propose GLAM (Global-to-Local Asymmetric Matching), which couples a retrieval-anchoring global descriptor with an asymmetric local pathway: each reference is kept as a compact set of pooled region tokens and matched against a single query probe through a learnable soft late interaction; at inference, the same tokens enable a lightweight mutual-nearest-neighbor re-ranking. GLAM surpasses strong global and two-stage baselines on Recall@1/5/10 and mAP, with ~5x smaller re-ranking features and ~two orders of magnitude lower per-pair matching cost than prior local re-ranking. The benchmark and code will be publicly released.

</details>

---

## 📊 统计

| 领域 | 论文数 |
|------|--------|
| VLM | 10 |
| Object Detection | 8 |
| Vision Transformer | 5 |
| Multi-camera Perception | 5 |
| Self-supervised Vision | 5 |
| Video Understanding | 4 |
| Autonomous Driving | 4 |
| Multimodal | 3 |
| Network Pruning | 3 |
| 3D Detection | 2 |
| Knowledge Distillation | 2 |
| Tracking | 1 |
| Open-set Detection | 1 |
| **总计** | **53** |